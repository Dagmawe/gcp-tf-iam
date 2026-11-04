# Terraform IAM Permission Mapper 🛠🔍

A robust Python orchestration tool that automates Terraform operations, parses debug logs, and maps executed API calls to required Google Cloud IAM permissions. 

Use it to discover exactly which IAM permissions a Terraform configuration needs — either **offline in dry-run mode** (the provider is pointed at a local mock server through its custom endpoints) or **live against GCP** — and turn that list into a least-privilege role for the service account that runs your pipeline.

---

## 🚀 Features

-   **One-Click Execution**: Runs `terraform init`, `terraform apply` (or `destroy`), and parses logs in one sweep.
-   **Dynamic API Mapping**: Resolves raw HTTP paths into readable GCP API Methods (e.g., `storage.buckets.get`) using the official Google Discovery API.
-   **Least-Privilege Auditing**: Lists the exact IAM permissions your Terraform run *actually used*.
-   **Deep Inspection for Write Actions**: Automatically inspects JSON payloads to find "hidden" permissions (like `compute.images.useReadOnly` inside VM creation).
-   **Dry-Run Auditing (Default)**: Runs Terraform operations offline against a local mock server to capture permissions without deploying anything. Every `*_custom_endpoint` of the installed `google`/`google-beta` provider is discovered from the provider schema (so new provider versions keep working) and pointed at the mock; no Google credentials are required.
-   **Fast Caching**: Caches Discovery Documents and IAM maps locally in `.cache/` to speed up subsequent runs.
---

## 📋 Prerequisites

1.  **Python 3.x** (Using standard libraries).
2.  **Terraform CLI** installed and in your system PATH.
3.  **Google Cloud SDK (`gcloud`)** for authentication (only needed if running in `--live` mode; dry-run mode uses a placeholder token and never contacts GCP).

Make sure you are authenticated with Application Default Credentials if running `--live`:
```bash
gcloud auth application-default login
```

---

## 📂 Repository Structure

```text
/
├── src/tf_iam/
│   ├── tf_runner.py       # Orchestrates Terraform Apply/Destroy
│   ├── tool.py            # The log parser & API Mapper
│   ├── rules_engine.py    # Deep inspection rules for complex resources
│   └── mock_server.py     # Local mock server for offline dry-run simulations
├── examples/              # Sample Terraform deployment scenarios
└── tests/                 # Unit test suite
```

---

## 📥 Installation

You can install this tool globally on your machine to run it from anywhere. Run this command at the root of the repository:

```bash
pip install .
```

### 🏢 Corporate Network Troubleshooting
If you are on a corporate network and encounter errors like `Could not find a version that satisfies the requirement setuptools` or SSO timeout errors, use this bypass flag to use the `setuptools` already on your machine:

```bash
pip install --no-build-isolation .
```

Make sure your corporate SSO ticketing is refreshed (e.g., run `gcert` if your organization uses it).

---

## ⚙️ Usage

### 1. Run a Dry-Run Apply (Default, offline mock server):
Audits permissions for a planned deployment without creating any real GCP resources.
```bash
tf-iam apply --var-file dry_run.tfvars --auto-approve
```

### 2. Run a Live Apply (Opt-in, deploys to real GCP):
Deploys real resources onto GCP and records the exact permissions used by the live apply.
```bash
tf-iam apply --live --var-file production.tfvars --auto-approve
```

### 3. Run a Dry-Run Destroy:
Audits permissions needed to destroy resources without modifying real resources. Run it in the same directory as a previous dry-run `apply`: the mocked resources are remembered in `.cache/mock_state.json` (alongside Terraform's own state) so the destroy actually issues the DELETE calls.
```bash
tf-iam destroy --var-file dry_run.tfvars --auto-approve
```

### 4. Run a Live Destroy (deletes real GCP resources):
```bash
tf-iam destroy --live --var-file production.tfvars --auto-approve
```

### 5. Parse an existing log file offline:
Parses any pre-existing Terraform debug log file to extract IAM permissions (useful for CI/CD audit jobs).
```bash
tf-iam parse --log-file /path/to/existing_debug.log
```

### 6. See the Help Menu:
```bash
tf-iam --help
```

`tf-iam apply` / `tf-iam destroy` exit with Terraform's exit code, so a failed run fails your CI job. The permissions found so far are still printed and saved to `.cache/reports/`.

---

## 🎯 Accuracy notes (read before enforcing a role)

-   Permissions come from the community-maintained [iann0036/iam-dataset](https://github.com/iann0036/iam-dataset) (`gcp/map.json`), a curated `fallback_map.json`, and the payload rules in `rules_engine.py`. The dataset can **over-approximate**: it lists every permission that *may* be involved in a method (e.g. `compute.machineImages.useReadOnly` for any `compute.instances.insert`). Review the aggregated list before turning it into a custom role.
-   Dry-run mode only sees the API calls the provider makes against the mock server. Calls that depend on real server state (e.g. long-running operation polling, IAM policy ETags) can differ slightly from a live run; use `--live` on a sandbox project for the final confirmation.
-   Resources whose provider defaults block deletion (`google_project` `deletion_policy = "PREVENT"`, `google_sql_database_instance` `deletion_protection = true`) must be configured explicitly for a destroy dry-run to reach the DELETE calls.




---

## 🧪 Running Tests

We use Python's built-in `unittest` framework. To run the tests, run this command from the root of the repository:

```bash
python3 -m unittest discover tests
```

---

## 🧩 How It Works

1.  **Orchestration**: `tf_runner.py` runs `terraform init`, sets `TF_LOG=DEBUG` and runs the requested action, redirecting standard error (where debug logs live) to `tf_apply_debug.log`.
2.  **Dry-run wiring** (default): after `init`, the installed provider schema (`terraform providers schema -json`) is read to list every `*_custom_endpoint` argument; a temporary `tf_iam_override.tf` points all of them at the local mock server (`mock_server.py`) and a placeholder `GOOGLE_OAUTH_ACCESS_TOKEN` is used so no real credentials are needed. Mocked resources are persisted in `.cache/mock_state.json` so a later dry-run `destroy` can find them. The override file is removed when the run finishes.
3.  **Log Scanning**: `tool.py` scans for `---[ REQUEST ]---` blocks (and the legacy `Google API Request:` format), capturing the verb, path, `Host` header and JSON body of every call.
4.  **API Resolution**: It takes the HTTP Verb + Path and matches it against the templated paths in the Google Discovery document to find the canonical method ID (e.g. `storage.buckets.get`).
5.  **IAM Mapping**: It cross-references the Method ID with the open-source IAM dataset (and `fallback_map.json`).
6.  **Contextual Evaluation**: `rules_engine.py` looks at the sent JSON body to determine if extra flags (like using a custom encryption key) pull in extra required permissions.

---

## ❤️ Contributions

Feel free to open issues or PRs if you want to extend the `rules_engine.py` to support more complex GCP resources!
