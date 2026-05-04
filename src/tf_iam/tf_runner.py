import subprocess
import os
import sys
import argparse
from tf_iam.tool import process_terraform_log
from tf_iam.rules_engine import evaluate_conditional_permissions

def run_terraform_and_parse(action=None):
    # 1. Prepare environment with debug logging
    env = os.environ.copy()
    env["TF_LOG"] = "DEBUG"
    
    log_file = "tf_apply_debug.log"
    print(f"🚀 Running 'terraform apply -auto-approve' and capturing logs to {log_file}...\n")
        
    # 1.5 Initialize Terraform
    print("📦 Initializing Terraform...")
    subprocess.run(["terraform", "init"])
    print() # Spacer
    
    # 2. Run Terraform and redirect stderr (debug logs) to the file
    with open(log_file, "w") as f:
        process = subprocess.run(
            ["terraform", action, "-auto-approve"],
            env=env,
            stdout=None,
            stderr=f
        )
    
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
        run_terraform_and_parse(args.action)

if __name__ == "__main__":
    main()
