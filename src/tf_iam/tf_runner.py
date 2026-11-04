import subprocess
import os
import sys
import json
import argparse
from tf_iam.tool import process_terraform_log

# Built-in list of provider `*_custom_endpoint` arguments. Only used as a fallback when the
# installed provider's schema cannot be read (see _discover_custom_endpoints), because the
# exact set of arguments changes between provider versions (e.g. `ml_engine_custom_endpoint`
# and `notebooks_custom_endpoint` were removed in google provider v8).
FALLBACK_ENDPOINTS = [
    "access_approval_custom_endpoint", "access_context_manager_custom_endpoint", "active_directory_custom_endpoint",
    "alloydb_custom_endpoint", "apigee_custom_endpoint", "apihub_custom_endpoint", "apikeys_custom_endpoint",
    "app_engine_custom_endpoint", "apphub_custom_endpoint", "artifact_registry_custom_endpoint",
    "assured_workloads_custom_endpoint", "backup_dr_custom_endpoint", "beyondcorp_custom_endpoint",
    "big_query_custom_endpoint", "biglake_custom_endpoint", "biglake_hive_custom_endpoint", "biglake_iceberg_custom_endpoint",
    "bigquery_analytics_hub_custom_endpoint", "bigquery_connection_custom_endpoint", "bigquery_data_transfer_custom_endpoint",
    "bigquery_datapolicy_custom_endpoint", "bigquery_datapolicyv2_custom_endpoint", "bigquery_reservation_custom_endpoint",
    "bigtable_custom_endpoint", "billing_budgets_custom_endpoint", "billing_custom_endpoint", "binary_authorization_custom_endpoint",
    "blockchain_node_engine_custom_endpoint", "certificate_manager_custom_endpoint", "ces_custom_endpoint", "chronicle_custom_endpoint",
    "cloud_asset_custom_endpoint", "cloud_billing_custom_endpoint", "cloud_build_custom_endpoint", "cloud_functions_custom_endpoint",
    "cloud_identity_custom_endpoint", "cloud_ids_custom_endpoint", "cloud_quotas_custom_endpoint", "cloud_resource_manager_custom_endpoint",
    "cloud_run_custom_endpoint", "cloud_run_v2_custom_endpoint", "cloud_scheduler_custom_endpoint", "cloud_security_compliance_custom_endpoint",
    "cloud_tasks_custom_endpoint", "cloudbuildv2_custom_endpoint", "clouddeploy_custom_endpoint", "clouddomains_custom_endpoint",
    "cloudfunctions2_custom_endpoint", "colab_custom_endpoint", "composer_custom_endpoint", "compute_custom_endpoint",
    "config_custom_endpoint", "contact_center_insights_custom_endpoint", "container_analysis_custom_endpoint",
    "container_attached_custom_endpoint", "container_aws_custom_endpoint", "container_azure_custom_endpoint", "container_custom_endpoint",
    "core_billing_custom_endpoint", "data_catalog_custom_endpoint", "data_fusion_custom_endpoint", "data_lineage_custom_endpoint",
    "data_loss_prevention_custom_endpoint", "data_pipeline_custom_endpoint", "database_migration_service_custom_endpoint",
    "dataflow_custom_endpoint", "dataform_custom_endpoint", "dataplex_custom_endpoint", "dataproc_custom_endpoint",
    "dataproc_gdc_custom_endpoint", "dataproc_metastore_custom_endpoint", "datastream_custom_endpoint", "deployment_manager_custom_endpoint",
    "developer_connect_custom_endpoint", "dialogflow_custom_endpoint", "dialogflow_cx_custom_endpoint", "discovery_engine_custom_endpoint",
    "dns_custom_endpoint", "document_ai_custom_endpoint", "document_ai_warehouse_custom_endpoint", "edgecontainer_custom_endpoint",
    "edgenetwork_custom_endpoint", "essential_contacts_custom_endpoint", "eventarc_custom_endpoint", "filestore_custom_endpoint",
    "firebase_app_check_custom_endpoint", "firebase_app_hosting_custom_endpoint", "firebase_data_connect_custom_endpoint",
    "firebase_remote_config_custom_endpoint", "firebaserules_custom_endpoint", "firestore_custom_endpoint", "gemini_custom_endpoint",
    "gke_backup_custom_endpoint", "gke_hub2_custom_endpoint", "gke_hub_custom_endpoint", "gkeonprem_custom_endpoint",
    "healthcare_custom_endpoint", "hypercomputecluster_custom_endpoint", "iam2_custom_endpoint", "iam3_custom_endpoint",
    "iam_beta_custom_endpoint", "iam_credentials_custom_endpoint", "iam_custom_endpoint", "iam_workforce_pool_custom_endpoint",
    "iap_custom_endpoint", "identity_platform_custom_endpoint", "integration_connectors_custom_endpoint", "integrations_custom_endpoint",
    "kms_custom_endpoint", "license_manager_custom_endpoint", "logging_custom_endpoint", "looker_custom_endpoint",
    "lustre_custom_endpoint", "managed_kafka_custom_endpoint", "memcache_custom_endpoint", "memorystore_custom_endpoint",
    "migration_center_custom_endpoint", "model_armor_custom_endpoint", "model_armor_global_custom_endpoint",
    "monitoring_custom_endpoint", "netapp_custom_endpoint", "network_connectivity_custom_endpoint", "network_connectivityv1_custom_endpoint",
    "network_management_custom_endpoint", "network_security_custom_endpoint", "network_services_custom_endpoint",
    "observability_custom_endpoint", "oracle_database_custom_endpoint", "org_policy_custom_endpoint", "os_config_custom_endpoint",
    "os_config_v2_custom_endpoint", "os_login_custom_endpoint", "parallelstore_custom_endpoint", "parameter_manager_custom_endpoint",
    "parameter_manager_regional_custom_endpoint", "privateca_custom_endpoint", "privileged_access_manager_custom_endpoint",
    "public_ca_custom_endpoint", "pubsub_custom_endpoint", "pubsub_lite_custom_endpoint", "recaptcha_enterprise_custom_endpoint",
    "redis_custom_endpoint", "resource_manager3_custom_endpoint", "resource_manager_custom_endpoint", "resource_manager_v3_custom_endpoint",
    "secret_manager_custom_endpoint", "secret_manager_regional_custom_endpoint", "secure_source_manager_custom_endpoint",
    "security_center_custom_endpoint", "security_center_management_custom_endpoint", "security_center_v2_custom_endpoint",
    "securityposture_custom_endpoint", "service_directory_custom_endpoint", "service_management_custom_endpoint",
    "service_networking_custom_endpoint", "service_usage_custom_endpoint", "site_verification_custom_endpoint",
    "source_repo_custom_endpoint", "spanner_custom_endpoint", "sql_custom_endpoint", "storage_batch_operations_custom_endpoint",
    "storage_control_custom_endpoint", "storage_custom_endpoint", "storage_insights_custom_endpoint", "storage_transfer_custom_endpoint",
    "tags_custom_endpoint", "tags_location_custom_endpoint", "transcoder_custom_endpoint", "vector_search_custom_endpoint",
    "vertex_ai_custom_endpoint", "vmwareengine_custom_endpoint", "vpc_access_custom_endpoint", "workbench_custom_endpoint",
    "workflows_custom_endpoint", "workload_identity_custom_endpoint", "workstations_custom_endpoint"
]

# Endpoints whose provider default base path carries a "<service>/<version>/" prefix that the
# log parser expects to find in the request path. Everything else is mocked at "/<service>/".
# NOTE: the provider's hand-written clients (IAM, Resource Manager, Service Usage, ...) strip
# the last path segment of a custom endpoint before appending their own "v1/...", so a two
# segment "<service>/<version>/" value is what keeps the service prefix in the logged path.
ENDPOINT_PATHS = {
    "compute_custom_endpoint": "compute/v1/",
    "storage_custom_endpoint": "storage/v1/",
    "container_custom_endpoint": "container/v1/",
    "dns_custom_endpoint": "dns/v1/",
    "kms_custom_endpoint": "cloudkms/v1/",
    "cloud_billing_custom_endpoint": "cloudbilling/v1/",
    "iam_custom_endpoint": "iam/v1/",
    # The hand-written IAM client (google_service_account, *_iam_member, custom roles, ...) is
    # built from the *iam_beta* base path, not iam_custom_endpoint. Both default to
    # https://iam.googleapis.com/v1/.
    "iam_beta_custom_endpoint": "iam/v1/",
}

MOCKABLE_PROVIDERS = ("google", "google-beta")


def _discover_custom_endpoints():
    """Read the installed providers' schemas and return {provider_local_name: [endpoint_arg, ...]}.

    Requires `terraform init` to have run. Returns None if the schema cannot be read, so the
    caller can fall back to the built-in list.
    """
    try:
        result = subprocess.run(
            ["terraform", "providers", "schema", "-json"],
            capture_output=True, text=True, check=True,
        )
        schema = json.loads(result.stdout)
    except Exception as e:
        print(f"⚠️ Could not read provider schema ({e}); falling back to the built-in endpoint list.")
        return None

    endpoints = {}
    for address, provider_schema in schema.get("provider_schemas", {}).items():
        local_name = address.rsplit("/", 1)[-1]
        if local_name not in MOCKABLE_PROVIDERS:
            continue
        attributes = provider_schema.get("provider", {}).get("block", {}).get("attributes", {})
        endpoints[local_name] = sorted(a for a in attributes if a.endswith("_custom_endpoint"))
    return endpoints or None


def _installed_providers():
    """Return the google providers selected by `terraform init` (for the fallback path)."""
    try:
        result = subprocess.run(["terraform", "version", "-json"], capture_output=True, text=True, check=True)
        selections = json.loads(result.stdout).get("provider_selections", {})
        found = [addr.rsplit("/", 1)[-1] for addr in selections]
        return [p for p in found if p in MOCKABLE_PROVIDERS] or list(MOCKABLE_PROVIDERS)
    except Exception:
        return list(MOCKABLE_PROVIDERS)


def _write_override_file(path, provider_endpoints, base_url):
    """Write a Terraform override file pointing every custom endpoint at the mock server."""
    lines = []
    for provider_name, endpoint_args in provider_endpoints.items():
        lines.append(f'provider "{provider_name}" {{')
        for ep in endpoint_args:
            svc_path = ENDPOINT_PATHS.get(ep, ep.replace("_custom_endpoint", "") + "/")
            lines.append(f'  {ep:<42} = "{base_url}/{svc_path}"')
        lines.append("}\n")
    with open(path, "w") as f:
        f.write("\n".join(lines))


def run_terraform_and_parse(action=None, var_file=None, auto_approve=False, dry_run=False):
    """Run `terraform <action>` with debug logging, then parse the log. Returns Terraform's exit code."""
    # 1. Prepare environment with debug logging
    env = os.environ.copy()
    env["TF_LOG"] = "DEBUG"

    if dry_run:
        # Every request goes to the local mock server, so no real credentials are needed. A static
        # access token makes the provider skip the ADC/OAuth flow entirely (otherwise a dry-run
        # fails when ADC is missing or needs re-auth) and guarantees that any endpoint that is not
        # mocked would be rejected with 401 instead of reaching real GCP with real credentials.
        env["GOOGLE_OAUTH_ACCESS_TOKEN"] = "tf-iam-dry-run-token"
        for credentials_var in ("GOOGLE_CREDENTIALS", "GOOGLE_CLOUD_KEYFILE_JSON", "GCLOUD_KEYFILE_JSON",
                                "GOOGLE_APPLICATION_CREDENTIALS", "GOOGLE_IMPERSONATE_SERVICE_ACCOUNT"):
            env.pop(credentials_var, None)
    
    log_file = "tf_apply_debug.log"
    override_file = "tf_iam_override.tf"
    mock_server = None

    tf_cmd = ["terraform", action]
    if auto_approve or dry_run:
        tf_cmd.append("-auto-approve")
    if var_file:
        tf_cmd.append(f"-var-file={var_file}")

    # 2. Initialize Terraform first so the installed provider schema is available
    print("📦 Initializing Terraform...")
    init = subprocess.run(["terraform", "init"])
    print() # Spacer
    if init.returncode != 0:
        print(f"❌ 'terraform init' failed with exit code {init.returncode}")
        return init.returncode

    process = None
    try:
        # 3. Dry-run: start the local mock server and point every provider endpoint at it
        if dry_run:
            from tf_iam.mock_server import MockServer
            # Persist mocked resources between runs so a dry-run destroy can "see" what a
            # previous dry-run apply created (otherwise every refresh is a 404 and no DELETE
            # calls are ever issued).
            mock_server = MockServer(port=8080, state_file=os.path.join(".cache", "mock_state.json"))
            mock_server.start()

            provider_endpoints = _discover_custom_endpoints()
            if provider_endpoints:
                summary = ", ".join(f"{name} ({len(eps)})" for name, eps in provider_endpoints.items())
                print(f"🔎 Custom endpoints discovered from provider schema: {summary}")
            else:
                provider_endpoints = {name: FALLBACK_ENDPOINTS for name in _installed_providers()}

            _write_override_file(override_file, provider_endpoints, f"http://{mock_server.host}:{mock_server.port}")

        # 4. Run Terraform and redirect stderr (debug logs) to the file
        print(f"🚀 Running '{' '.join(tf_cmd)}' and capturing logs to {log_file}...\n")
        with open(log_file, "w") as f:
            process = subprocess.run(
                tf_cmd,
                env=env,
                stdout=None,
                stderr=f
            )
    finally:
        if mock_server:
            mock_server.stop()
        if os.path.exists(override_file):
            try:
                os.remove(override_file)
            except Exception:
                pass

    if process.returncode != 0:
        print(f"\n❌ Terraform {action} failed with exit code {process.returncode}")
        print("--- 🔴 Error Details from Log ---")
        try:
            with open(log_file, 'r') as f:
                in_error_block = False
                for line in f:
                    # Catch the pretty terraform error blocks
                    if "╷" in line or "┌" in line: # Support different box drawing chars if any
                        in_error_block = True
                    
                    if in_error_block:
                        print(line.rstrip())
                    
                    if "╵" in line or "└" in line:
                        in_error_block = False
                        print() # Newline between blocks
                    
                    # Catch structural [ERROR] lines as well
                    if not in_error_block and "[ERROR]" in line:
                        print(line.rstrip())
        except Exception as e:
            print(f"Could not read log file for errors: {e}")
        
        print(f"\n🛑 Stopping: {action.capitalize()} failed. Fix the errors above and try again.")
    
    # 5. Call your tool to parse the log
    print("\n--- 🔍 Parsing Permissions Used ---")
    process_terraform_log(log_file)
    return process.returncode

def main():
    parser = argparse.ArgumentParser(description="Automate Terraform Apply/Destroy and map IAM permissions.")
    parser.add_argument(
        "action", 
        nargs="?", 
        choices=["apply", "destroy", "parse"], 
        help="The action to perform: 'apply', 'destroy', or 'parse' an existing log file."
    )
    parser.add_argument(
        "--log-file",
        "-f",
        type=str,
        help="Path to an existing Terraform debug log file to parse directly (used with action='parse')."
    )
    parser.add_argument(
        "--var-file",
        type=str,
        help="Path to a Terraform variables file (passed as -var-file to terraform commands)."
    )
    parser.add_argument(
        "--auto-approve",
        action="store_true",
        help="Skip interactive approval of plan before applying or destroying."
    )
    parser.add_argument(
        "--live",
        action="store_true",
        help="Run Terraform operations against real live GCP services instead of the default local mock dry-run."
    )
    args = parser.parse_args()
    
    if not args.action:
        parser.print_help()
        sys.exit(1)
        
    if args.action == "parse":
        if not args.log_file:
            print("❌ Error: When using 'parse', you must provide a log file with '--log-file <path>'")
            sys.exit(1)
        if not os.path.exists(args.log_file):
            print(f"❌ Error: Log file '{args.log_file}' does not exist.")
            sys.exit(1)
        print(f"\n--- 🔍 Parsing Permissions from User Log: {args.log_file} ---")
        process_terraform_log(args.log_file)
    elif args.action in ["apply", "destroy"]:
        dry_run = not args.live
        exit_code = run_terraform_and_parse(args.action, args.var_file, args.auto_approve, dry_run)
        sys.exit(exit_code)




if __name__ == "__main__":
    main()
