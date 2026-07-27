import subprocess
import os
import sys
import argparse
from tf_iam.tool import process_terraform_log
from tf_iam.rules_engine import evaluate_conditional_permissions

def run_terraform_and_parse(action=None, var_file=None, auto_approve=False, dry_run=False):
    # 1. Prepare environment with debug logging
    env = os.environ.copy()
    env["TF_LOG"] = "DEBUG"
    
    log_file = "tf_apply_debug.log"
    override_file = "tf_iam_override.tf"
    mock_server = None
    
    # 1.1 Start local mock server if dry-run is requested
    if dry_run:
        from tf_iam.mock_server import MockServer
        mock_server = MockServer(port=8080)
        mock_server.start()
        
        all_endpoints = [
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
            "migration_center_custom_endpoint", "ml_engine_custom_endpoint", "model_armor_custom_endpoint", "model_armor_global_custom_endpoint",
            "monitoring_custom_endpoint", "netapp_custom_endpoint", "network_connectivity_custom_endpoint", "network_connectivityv1_custom_endpoint",
            "network_management_custom_endpoint", "network_security_custom_endpoint", "network_services_custom_endpoint", "notebooks_custom_endpoint",
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
        
        lines = []
        for provider_name in ["google", "google-beta"]:
            lines.append(f'provider "{provider_name}" {{')
            for ep in all_endpoints:
                svc_prefix = ep.replace("_custom_endpoint", "")
                if ep == "compute_custom_endpoint":
                    url = "http://localhost:8080/compute/v1/"
                elif ep == "storage_custom_endpoint":
                    url = "http://localhost:8080/storage/v1/"
                elif ep == "container_custom_endpoint":
                    url = "http://localhost:8080/container/v1/"
                elif ep == "dns_custom_endpoint":
                    url = "http://localhost:8080/dns/v1/"
                elif ep == "kms_custom_endpoint":
                    url = "http://localhost:8080/cloudkms/v1/"
                elif ep == "cloud_billing_custom_endpoint":
                    url = "http://localhost:8080/cloudbilling/v1/"
                else:
                    url = f"http://localhost:8080/{svc_prefix}/"
                lines.append(f'  {ep:<42} = "{url}"')
            lines.append("}\n")
            
        override_content = "\n".join(lines)
        with open(override_file, "w") as f:
            f.write(override_content)




    tf_cmd = ["terraform", action]
    if auto_approve or dry_run:
        tf_cmd.append("-auto-approve")
    if var_file:
        tf_cmd.append(f"-var-file={var_file}")
        
    print(f"🚀 Running '{' '.join(tf_cmd)}' and capturing logs to {log_file}...\n")
        
    # 1.5 Initialize Terraform
    print("📦 Initializing Terraform...")
    subprocess.run(["terraform", "init"])
    print() # Spacer
    
    # 2. Run Terraform and redirect stderr (debug logs) to the file
    try:
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
        print(f"\n❌ Terraform apply failed with exit code {process.returncode}")
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
    
    # 3. Call your tool to parse the log
    print("\n--- 🔍 Parsing Permissions Used ---")
    process_terraform_log(log_file)

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
        run_terraform_and_parse(args.action, args.var_file, args.auto_approve, dry_run)




if __name__ == "__main__":
    main()
