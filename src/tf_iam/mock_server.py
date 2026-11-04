import json
import os
import re
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

class GCPMockHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        # Print standard requests for dry-run insight
        sys.stdout.write(f"   [Mock HTTP] {args[0]} -> Response {args[1]}\n")

    def do_GET(self):
        clean_path = self.path.split("?")[0].rstrip("/")
        
        # Check if the resource was dynamically created during the run
        if hasattr(self.server, "mock_resources") and clean_path in self.server.mock_resources:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            resp = self.server.mock_resources[clean_path]
            # Populate basic fields if they are missing
            if isinstance(resp, dict):
                if "id" not in resp:
                    resp["id"] = "1234567890"
                if "selfLink" not in resp:
                    resp["selfLink"] = f"http://{self.headers.get('Host', 'localhost')}{clean_path}"
                if "name" not in resp:
                    resp["name"] = clean_path.split("/")[-1]
                # Enrich project resources with fields expected by CRM provider code
                if clean_path.startswith("/v1/projects/"):
                    if "lifecycleState" not in resp:
                        resp["lifecycleState"] = "ACTIVE"
                    if "projectNumber" not in resp:
                        resp["projectNumber"] = "1234567890"
                    if "projectId" not in resp:
                        resp["projectId"] = clean_path.split("/")[-1]
                # Enrich compute instance resources with status = RUNNING
                if "/instances/" in clean_path:
                    if "status" not in resp:
                        resp["status"] = "RUNNING"
                # Zonal/regional resources: the provider reads zone/region back from the API response
                # (e.g. "Cannot determine zone" on refresh/destroy if missing), so derive them from the path.
                zone_match = re.search(r"/zones/([^/]+)/", clean_path)
                if zone_match and "zone" not in resp:
                    resp["zone"] = zone_match.group(1)
                region_match = re.search(r"/regions/([^/]+)/", clean_path)
                if region_match and "region" not in resp:
                    resp["region"] = region_match.group(1)
                
                # Apply generic active/ready state fields to satisfy provider wait loops on other resources
                if "status" not in resp:
                    resp["status"] = "RUNNING"
                if "state" not in resp:
                    resp["state"] = "ENABLED" if "serviceusage" in clean_path else "READY"
                if "lifecycleState" not in resp:
                    resp["lifecycleState"] = "ACTIVE"
            self.wfile.write(json.dumps(resp).encode('utf-8'))
            return


        # 1. Handle operations polling
        if "operations/" in self.path or "operation-mock-12345" in self.path:


            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            resp = {
                "kind": "compute#operation",
                "status": "DONE",
                "progress": 100,
                "done": True,
                "response": {
                    "@type": "type.googleapis.com/google.protobuf.Empty"
                }
            }
            self.wfile.write(json.dumps(resp).encode('utf-8'))
            return



        # 1.5 Handle billing info checks
        if "billingInfo" in self.path:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            
            clean_path = self.path.split("?")[0].rstrip("/")
            if hasattr(self.server, "mock_resources") and clean_path in self.server.mock_resources:
                self.wfile.write(json.dumps(self.server.mock_resources[clean_path]).encode('utf-8'))
                return
                
            # Extract project_id from path
            match = re.search(r"projects/([^/]+)", self.path)
            project_id = match.group(1) if match else "unknown"
            
            resp = {
                "name": f"projects/{project_id}/billingInfo",
                "projectId": project_id,
                "billingAccountName": "billingAccounts/000000-000000-000000",
                "billingEnabled": True
            }
            self.wfile.write(json.dumps(resp).encode('utf-8'))
            return

        if re.search(r"/projects/[^/]+$", self.path.split("?")[0]):
            project_id = self.path.split("/")[-1].split("?")[0]
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            if "compute" in self.path:
                resp = {
                    "kind": "compute#project",
                    "name": project_id,
                    "id": "1234567890"
                }
            else:
                resp = {
                    "projectNumber": "1234567890",
                    "projectId": project_id,
                    "lifecycleState": "ACTIVE",
                    "name": project_id
                }
            self.wfile.write(json.dumps(resp).encode('utf-8'))
            return
        # 2.25 Handle KMS Key Lookups
        if "cryptoKeys" in self.path:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            resp = {
                "name": self.path.split("?")[0],
                "primary": {
                    "state": "ENABLED"
                }
            }
            self.wfile.write(json.dumps(resp).encode('utf-8'))
            return
        # 2.27 Handle SQL sub-resource lookups (users, databases)
        if "/instances/" in self.path and (self.path.endswith("/users") or self.path.endswith("/databases") or "/users?" in self.path or "/databases?" in self.path):
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            resp = {"items": []}
            self.wfile.write(json.dumps(resp).encode('utf-8'))
            return

        # 2.26 Handle GCE Image Lookups
        if "/global/images/" in self.path:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            resp = {
                "name": self.path.split("/")[-1].split("?")[0],
                "id": "1234567890",
                "selfLink": f"http://{self.headers.get('Host', 'localhost')}{self.path.split('?')[0]}"
            }
            self.wfile.write(json.dumps(resp).encode('utf-8'))
            return


        # 2.3 Handle list services checks
        if "/services" in self.path.split("?")[0] and not "/services/" in self.path:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            
            # Extract project_id from path
            match = re.search(r"projects/([^/]+)", self.path)
            project_id = match.group(1) if match else "unknown"
            
            resp = {
                "services": [
                    {
                        "name": f"projects/{project_id}/services/compute.googleapis.com",
                        "state": "ENABLED"
                    },
                    {
                        "name": f"projects/{project_id}/services/serviceusage.googleapis.com",
                        "state": "ENABLED"
                    }
                ]
            }
            self.wfile.write(json.dumps(resp).encode('utf-8'))
            return

        # 2.5 Handle Service Usage checks (enable API checks)

        if "/services/" in self.path:
            # Extract parent project from path to keep project ID consistent
            match = re.search(r"projects/([^/]+)", self.path)
            project_id = match.group(1) if match else "unknown"
            parent = f"projects/{project_id}"
            service_name = self.path.split("/")[-1].split("?")[0]
            
            if project_id == "00000000000":
                # Return 403 Forbidden to satisfy the provider's prerequisite check logic
                self.send_response(403)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                resp = {
                    "error": {
                        "code": 403,
                        "message": "Project '00000000000' not found or permission denied.",
                        "status": "PERMISSION_DENIED"
                    }
                }
                self.wfile.write(json.dumps(resp).encode('utf-8'))
                return
                
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            resp = {
                "name": f"{parent}/services/{service_name}",
                "parent": parent,
                "state": "ENABLED",
                "config": {
                    "name": service_name,
                    "title": service_name,
                    "apis": [
                        {
                            "name": service_name,
                            "version": "v1"
                        }
                    ]
                }
            }
            self.wfile.write(json.dumps(resp).encode('utf-8'))
            return




        # 3. Otherwise return 404 Not Found to force Terraform to create/POST the resource
        self.send_response(404)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"error": {"code": 404, "message": "Resource not found (Mocked)"}}).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body_str = self.rfile.read(content_length).decode('utf-8') if content_length else ""
        
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        
        # If it's a testIamPermissions call, return all requested permissions as granted
        if "testIamPermissions" in self.path:
            try:
                req_data = json.loads(body_str) if body_str else {}
                permissions = req_data.get("permissions", [])
                resp = {"permissions": permissions}
            except Exception:
                resp = {"permissions": []}
            self.wfile.write(json.dumps(resp).encode('utf-8'))
            return
            
        # If it's a billingInfo update, return the ProjectBillingInfo payload directly
        if "billingInfo" in self.path:
            try:
                req_data = json.loads(body_str) if body_str else {}
                billing_account = req_data.get("billingAccountName", "billingAccounts/000000-000000-000000")
            except Exception:
                billing_account = "billingAccounts/000000-000000-000000"
                
            match = re.search(r"projects/([^/]+)", self.path)
            project_id = match.group(1) if match else "unknown"
            resp = {
                "name": f"projects/{project_id}/billingInfo",
                "projectId": project_id,
                "billingAccountName": billing_account,
                "billingEnabled": True
            }
            # Save it so GET checks also return this correct billing account!
            clean_path = self.path.split("?")[0].rstrip("/")
            if hasattr(self.server, "mock_resources"):
                self.server.mock_resources[clean_path] = resp
                
            self.wfile.write(json.dumps(resp).encode('utf-8'))
            return

        # If it's a getIamPolicy call, return stashed IAM policy if available
        if "getIamPolicy" in self.path:
            match = re.search(r"projects/([^:/]+)", self.path)
            project_id = match.group(1) if match else "unknown"
            key = f"projects/{project_id}/iamPolicy"
            if hasattr(self.server, "mock_resources") and key in self.server.mock_resources:
                resp = self.server.mock_resources[key]
            else:
                resp = {
                    "bindings": [],
                    "etag": "BwW4c/8k/8w="
                }
            self.wfile.write(json.dumps(resp).encode('utf-8'))
            return

        # If it's a setIamPolicy call, save the policy state and echo it back
        if "setIamPolicy" in self.path:
            try:
                req_data = json.loads(body_str) if body_str else {}
                resp = req_data.get("policy", req_data)
            except Exception:
                resp = {}
            match = re.search(r"projects/([^:/]+)", self.path)
            project_id = match.group(1) if match else "unknown"
            if hasattr(self.server, "mock_resources"):
                self.server.mock_resources[f"projects/{project_id}/iamPolicy"] = resp
            self.wfile.write(json.dumps(resp).encode('utf-8'))
            return

        # If it's a service account creation, enrich response with email/uniqueId
        if "serviceAccounts" in self.path and self.command == "POST":
            try:
                req_data = json.loads(body_str) if body_str else {}
                account_id = req_data.get("accountId", "test-sa")
            except Exception:
                account_id = "test-sa"
            
            match = re.search(r"projects/([^/]+)", self.path)
            project_id = match.group(1) if match else "unknown"
            
            resp = {
                "name": f"projects/{project_id}/serviceAccounts/{account_id}@{project_id}.iam.gserviceaccount.com",
                "projectId": project_id,
                "uniqueId": "12345678901234567890",
                "email": f"{account_id}@{project_id}.iam.gserviceaccount.com",
                "displayName": req_data.get("displayName", "Mock SA")
            }
            # Also stash it in mock_resources under both paths
            clean_path = self.path.split("?")[0].rstrip("/")
            if hasattr(self.server, "mock_resources"):
                self.server.mock_resources[clean_path + "/" + resp["email"]] = resp
                self.server.mock_resources[clean_path + "/" + account_id] = resp
            
            self.wfile.write(json.dumps(resp).encode('utf-8'))
            return


        # Save resource details to allow subsequent GET calls to retrieve it
        try:
            req_data = json.loads(body_str) if body_str else {}
            clean_path = self.path.split("?")[0].rstrip("/")
            if self.command == "DELETE":
                if hasattr(self.server, "mock_resources"):
                    self.server.mock_resources.pop(clean_path, None)
            elif self.command in ["PUT", "PATCH"]:
                if hasattr(self.server, "mock_resources"):
                    self.server.mock_resources[clean_path] = req_data
            else: # POST
                res_name = req_data.get("projectId") or req_data.get("name")
                if res_name and hasattr(self.server, "mock_resources"):
                    self.server.mock_resources[clean_path + "/" + res_name] = req_data
        except Exception:
            pass

        resp = {
            "kind": "compute#operation",
            "name": "operations/operation-mock-12345",
            "status": "DONE",
            "targetLink": f"http://{self.headers.get('Host', 'localhost')}{self.path}",
            "progress": 100
        }
        self.wfile.write(json.dumps(resp).encode('utf-8'))



    def do_PUT(self):
        self.do_POST()

    def do_PATCH(self):
        self.do_POST()

    def do_DELETE(self):
        self.do_POST()

class MockServer:
    def __init__(self, host="127.0.0.1", port=8080, state_file=None):
        self.host = host
        self.port = port
        self.state_file = state_file
        self.server = None
        self.thread = None

    def _load_state(self):
        """Resources created by a previous dry-run (e.g. apply) so a later destroy can find them."""
        if self.state_file and os.path.exists(self.state_file):
            try:
                with open(self.state_file, "r") as f:
                    return json.load(f)
            except Exception as e:
                print(f"⚠️ Could not read mock state {self.state_file} ({e}); starting empty.")
        return {}

    def _save_state(self):
        if not self.state_file or self.server is None:
            return
        try:
            os.makedirs(os.path.dirname(os.path.abspath(self.state_file)), exist_ok=True)
            with open(self.state_file, "w") as f:
                json.dump(self.server.mock_resources, f, indent=2)
        except Exception as e:
            print(f"⚠️ Could not save mock state to {self.state_file}: {e}")

    def start(self):
        self.server = HTTPServer((self.host, self.port), GCPMockHandler)
        self.server.mock_resources = self._load_state()
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        print(f"📡 Started local GCP Mock Server on http://{self.host}:{self.port}")
        if self.server.mock_resources:
            print(f"   (loaded {len(self.server.mock_resources)} mocked resources from {self.state_file})")


    def stop(self):
        if self.server:
            self._save_state()
            self.server.shutdown()
            self.server.server_close()
            print("📡 Stopped local GCP Mock Server.")
