import urllib.request
import json
import re
import sys
import os
import datetime
from tf_iam.rules_engine import evaluate_conditional_permissions

# --- 1. Fetch API Method ID from Discovery Document ---
def find_gcp_api_method(discovery_url, target_http_method, target_path):
    # Caching logic
    cache_dir = os.path.join(".cache", "discovery")
    os.makedirs(cache_dir, exist_ok=True)
    
    # Derive a safe filename from the URL, e.g., compute_v1.json
    parts = discovery_url.split('/')
    if len(parts) >= 3:
        api_name = parts[-3]
        api_version = parts[-2]
        filename = f"{api_name}_{api_version}.json"
    else:
        filename = "unknown_api.json"
        
    cache_path = os.path.join(cache_dir, filename)
    
    data = None
    if os.path.exists(cache_path):
        try:
            with open(cache_path, 'r') as f:
                data = json.load(f)
        except Exception as e:
            print(f"⚠️ Cache corrupted for {filename}, refetching... ({e})")

    if not data:
        try:
            with urllib.request.urlopen(discovery_url) as response:
                raw_data = response.read().decode()
                data = json.loads(raw_data)
                # Save to cache
                with open(cache_path, 'w') as f:
                    f.write(raw_data)
        except Exception as e:
            print(f"\n❌ Error fetching Discovery URL {discovery_url}: {e}")
            print("💡 Tip: If you are on a corporate network, make sure you are authenticated (e.g., run 'gcert' or check your SSO tickets).")
            return None
        
    def search_resources(resources):
        for res_name, res_data in resources.items():
            if 'methods' in res_data:
                for method_name, method_data in res_data['methods'].items():
                    # Only check if the HTTP Methods match first (POST == POST)
                    if method_data.get('httpMethod') == target_http_method:
                        
                        # Grab the templated path from Google (e.g., projects/{project}/zones/{zone}/instances)
                        template_path = method_data.get('path', '')
                        
                        # Convert {variable} placeholders into Regex wildcards (.+?)
                        # Remove strict string boundaries to allow Google's path to be found anywhere inside the TF path
                        regex_pattern = re.sub(r'\{[^}]+\}', r'.+?', template_path)
                        
                        # Check if the real Terraform path matches our new wildcard pattern
                        # Some Paths from TF have query string like ?alt=json which should be stripped before regex check happens
                        clean_target_path = target_path.split('?')[0]
                        if re.search(regex_pattern, clean_target_path):
                            return method_data.get('id')
            
            # Dig deeper if there are nested resources
            if 'resources' in res_data:
                result = search_resources(res_data['resources'])
                if result:
                    return result
        return None
    return search_resources(data.get('resources', {}))

# --- 2. Map Method ID to IAM Permissions ---
def get_iam_permission(api_method_id):
    cache_dir = ".cache"
    os.makedirs(cache_dir, exist_ok=True)
    cache_path = os.path.join(cache_dir, "map.json")
    
    iam_map = None
    if os.path.exists(cache_path):
        try:
            with open(cache_path, 'r') as f:
                iam_map = json.load(f)
        except Exception as e:
             print(f"⚠️ Cache corrupted for map.json, refetching... ({e})")

    if not iam_map:
        dataset_url = "https://raw.githubusercontent.com/iann0036/iam-dataset/main/gcp/map.json"
        try:
            with urllib.request.urlopen(dataset_url) as response:
                raw_data = response.read().decode()
                iam_map = json.loads(raw_data)
                # Save to cache
                with open(cache_path, 'w') as f:
                    f.write(raw_data)
        except Exception as e:
            print(f"\n❌ Error fetching IAM map dataset: {e}")
            print("💡 Tip: If you are on a corporate network, make sure you are authenticated (e.g., run 'gcert' or check your SSO tickets).")
            iam_map = {} # If fetch fails, we continue with empty map to trigger fallback file check
        
    def search_dataset(data, target):
        if isinstance(data, dict):
            for k, v in data.items():
                if k == target:
                    return v
                result = search_dataset(v, target)
                if result is not None:
                    return result
        return None

    method_data = search_dataset(iam_map, api_method_id)
    if method_data and "permissions" in method_data:
        return [perm.get("name") for perm in method_data["permissions"] if "name" in perm]

    # Fallback checking
    current_dir = os.path.dirname(os.path.abspath(__file__))
    fallback_path = os.path.join(current_dir, "fallback_map.json")
    if os.path.exists(fallback_path):
        try:
            with open(fallback_path, 'r') as f:
                fallback_map = json.load(f)
                if api_method_id in fallback_map:
                    return fallback_map[api_method_id]
        except Exception as e:
            print(f"⚠️ Error reading fallback_map.json: {e}")

    return ["Mapping not found in dataset"]



# --- 3. Parse Terraform Log and Execute ---
def _save_call(current_call, json_buffer, found_calls):
    try:
        json_str = "".join(json_buffer)
        if json_str.strip() and json_str.strip() != "(null)":
             json_str = re.sub(r'^\d{4}/\d{2}/\d{2}.*?\[DEBUG\]\s+', '', json_str, flags=re.MULTILINE)
             current_call['body'] = json.loads(json_str)
        else:
            current_call['body'] = {}
    except json.JSONDecodeError as e:
        pass
    found_calls.append(current_call.copy())

def process_terraform_log(log_file_path):
    print(f"Scanning '{log_file_path}' for Terraform API calls...\n")
    
    # Init report tracking
    report_lines = []
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_lines.append(f"IAM Permission Report - Generated on {timestamp}\n")
    report_lines.append(f"Log parsed: {log_file_path}\n")
    report_lines.append("-" * 50 + "\n")
    
    req_start_legacy = re.compile(r"Google API Request:\s+(POST|PUT|PATCH|DELETE)\s+(https?://[^/]+)(/[^\s]+)")
    req_start_modern = re.compile(r"---\[\s*REQUEST\s*\]---")
    modern_method_path = re.compile(r"^(GET|POST|PUT|PATCH|DELETE)\s+(/[^\s]+)\s+HTTP")
    
    found_calls = [] # List of dicts: {'method': ..., 'path': ..., 'body': ...}
    
    try:
        with open(log_file_path, 'r') as file:
            in_request = False
            in_headers = False
            current_call = {}
            json_buffer = []
            
            for line in file:
                # Strip typical logger prefix "... [DEBUG] provider...:"
                prefix_match = re.search(r"\] (provider[^\s:]*):\s+(.*)", line)
                if prefix_match:
                    payload_line = prefix_match.group(2)
                else:
                    payload_line = line.strip('\n')

                # Check for Legacy format
                legacy_match = req_start_legacy.search(payload_line)
                if legacy_match:
                    if in_request and current_call and 'method' in current_call:
                        _save_call(current_call, json_buffer, found_calls)
                        
                    in_request = True
                    in_headers = False
                    current_call = {
                        "method": legacy_match.group(1),
                        "host": legacy_match.group(2),
                        "path": legacy_match.group(3),
                        "body": {}
                    }
                    json_buffer = []
                    continue

                # Check for Modern format start
                modern_match = req_start_modern.search(payload_line)
                if modern_match:
                    if in_request and current_call and 'method' in current_call:
                        _save_call(current_call, json_buffer, found_calls)
                        
                    in_request = True
                    in_headers = True 
                    current_call = {"body": {}}
                    json_buffer = []
                    continue

                if in_request:
                    # Break out if we see RESPONSE block
                    if "Google API Response" in payload_line or "---[ RESPONSE" in payload_line:
                        if 'method' in current_call:
                            _save_call(current_call, json_buffer, found_calls)
                        in_request = False
                        current_call = {}
                        json_buffer = []
                        continue

                    if in_headers:
                        # If we haven't found method/path yet, look for it
                        if 'method' not in current_call:
                            mm = modern_method_path.search(payload_line)
                            if mm:
                                current_call['method'] = mm.group(1)
                                current_call['path'] = mm.group(2)
                            continue

                        # Look for Host header
                        if payload_line.lower().startswith('host:'):
                            current_call['host'] = payload_line.split(':', 1)[1].strip()
                            continue
                        
                        # Check for end of headers (empty line or just spaces)
                        if not payload_line.strip():
                            in_headers = False
                        continue
                    
                    # Not in headers, capture JSON body
                    json_buffer.append(payload_line + "\n")

            # End of file
            if in_request and current_call and 'method' in current_call:
                _save_call(current_call, json_buffer, found_calls)
    except FileNotFoundError:
        print(f"Error: Could not find '{log_file_path}'.")
        return

    if not found_calls:
        print("No mutating API calls (POST/PUT/PATCH/DELETE) found in the log.")
        return

    # Process each unique API call found in the log
    printed_signatures = set()
    for call in found_calls:
        http_method = call['method']
        full_path = call['path']
        request_body = call.get('body', {})
        if request_body:
            msg_keys = f"Payload keys: {list(request_body.keys())}"
            print(msg_keys)
            report_lines.append(msg_keys + "\n")

        # Skip extremely generic polling paths to keep the output clean
        if "nextPageToken" in full_path or "state%3AENABLED" in full_path:
            continue
        
        # Extract API Name from Host Header if available
        # e.g., Host: cloudbilling.googleapis.com -> api_name = cloudbilling
        # Host: storage.googleapis.com -> api_name = storage
        api_name = None
        if 'host' in call and call['host'].endswith('.googleapis.com'):
            api_name = call['host'].split('.')[0]
        clean_path = full_path.split('?')[0].strip("/")
        parts = clean_path.split("/")
        if len(parts) >= 2 or api_name:
            if not api_name:
                api_name = parts[0]      # fallback if api name not found 
            
            # The version is usually the first part of the path that looks like v1, v2beta, etc.
            # E.g., /v1/billingAccounts -> v1
            # /compute/v1/projects -> v1
            api_version = parts[1] if (len(parts) > 1 and parts[1].startswith('v')) else None
            if not api_version:
                api_version = 'v1' # Fallback default
            
            # Dynamically build the Discovery URL
            discovery_url = f"https://www.googleapis.com/discovery/v1/apis/{api_name}/{api_version}/rest"
            
            # Trips the api name from the path to construct the clean path for the discovery url
            try:
                version_index = parts.index(api_version)
                api_path = "/".join(parts[version_index:])
            except ValueError:
                api_path = clean_path

            method_id = find_gcp_api_method(discovery_url, http_method, api_path)
            if method_id:
                # 👈 DEDUPLICATION CHECK!
                sig = (method_id, http_method)
                if sig in printed_signatures:
                    continue
                printed_signatures.add(sig)

                sep = "-" * 50
                print(sep)
                report_lines.append(sep + "\n")
                
                msg = f"Detected TF Action: {http_method} {full_path}"
                print(msg)
                report_lines.append(msg + "\n")
                
                if request_body:
                    msg_keys = f"Payload keys: {list(request_body.keys())}"
                    print(msg_keys)
                    report_lines.append(msg_keys + "\n")

                msg_mapped = f"Mapped API Method:  {method_id}"
                print(msg_mapped)
                report_lines.append(msg_mapped + "\n")
                
                base_permissions = get_iam_permission(method_id)
                cond_permissions = evaluate_conditional_permissions(method_id, request_body)
                
                # Merge and deduplicate
                all_permissions = list(set(base_permissions + cond_permissions))
                
                msg_iam = f"✅ Required IAM:      {all_permissions}"
                print(msg_iam)
                report_lines.append(msg_iam + "\n")
                
                if cond_permissions:
                    msg_cond = f"   (Included conditional IAM: {cond_permissions})"
                    print(msg_cond)
                    report_lines.append(msg_cond + "\n")
            else:
                msg_warn = "⚠️ Could not match this exact path in the Discovery API."
                print(msg_warn)
                report_lines.append(msg_warn + "\n")
        else:
            msg_warn2 = "⚠️ URL path is too short to parse dynamically."
            print(msg_warn2)
            report_lines.append(msg_warn2 + "\n")

    # Write report to file
    reports_dir = os.path.join(".cache", "reports")
    os.makedirs(reports_dir, exist_ok=True)
    report_file = os.path.join(reports_dir, f"permissions_{timestamp}.txt")
    try:
        with open(report_file, 'w') as f:
            f.writelines(report_lines)
        print(f"\n💾 Report saved to: {report_file}")
    except Exception as e:
        print(f"\n❌ Error saving report: {e}")

# --- Execution Entry Point ---
if __name__ == "__main__":
    # Allow passing the log file as a command line argument, default to tf_debug.log
    log_file = sys.argv[1] if len(sys.argv) > 1 else "tf_debug.log"
    process_terraform_log(log_file)