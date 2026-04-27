# Terraform IAM Permission Mapper 🛠🔍

A robust Python orchestration tool that automates Terraform operations, parses debug logs, and maps executed API calls to required Google Cloud IAM permissions. 

Perfect for auditing exactly what permissions your Service Account uses, or for generating least-privilege IAM roles for your CI/CD pipelines!

---

## 🚀 Features

-   **One-Click Execution**: Runs `terraform init`, `terraform apply` (or `destroy`), and parses logs in one sweep.
-   **Dynamic API Mapping**: Resolves raw HTTP paths into readable GCP API Methods (e.g., `storage.buckets.get`) using the official Google Discovery API.
-   **Least-Privilege Auditing**: Lists the exact IAM permissions your Terraform run *actually used*.
-   **Deep Inspection for Write Actions**: Automatically inspects JSON payloads to find "hidden" permissions (like `compute.images.useReadOnly` inside VM creation).
-   **Fast Caching**: Caches Discovery Documents and IAM maps locally in `.cache/` to speed up subsequent runs.
---

## 📋 Prerequisites

1.  **Python 3.x** (Using standard libraries).
2.  **Terraform CLI** installed and in your system PATH.
3.  **Google Cloud SDK (`gcloud`)** for authentication.

Make sure you are authenticated with Application Default Credentials:
```bash
gcloud auth application-default login
```

---

## 📂 Repository Structure

```text
/
├── tf_runner.py       # Orchestrates Terraform Apply/Destroy + runs tool.py
├── tool.py            # The log parser & API Mapper
├── rules_engine.py    # Deep inspection rules for complex resources
└── examples/          # Sample Terraform deployment scenarios
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

### 1. Run an Apply and map permissions:
```bash
tf-iam apply
```

### 2. Run a Destroy and map permissions:
```bash
tf-iam destroy
```

### 3. Parse an existing log offline:
```bash
tf-iam parse --log-file /path/to/existing_debug.log
```

### 4. See the Help Menu:
```bash
tf-iam --help
```

---

## 🧪 Running Tests

We use Python's built-in `unittest` framework. To run the tests, run this command from the root of the repository:

```bash
python3 -m unittest discover tests
```

---

## 🧩 How It Works

1.  **Orchestration**: `tf_runner.py` sets `TF_LOG=DEBUG` and runs Terraform. It redirects standard error (where debug logs live) to `tf_apply_debug.log`.
2.  **Log Scanning**: `tool.py` scans for patterns like `---[ REQUEST ]---` or legacy `Google API Request:`.
3.  **API Resolution**: It takes the HTTP Verb + Path and hits the Google Discovery API to find the canonical `storage.buckets.get`.
4.  **IAM Mapping**: It cross-references the Method ID with the open-source IAM dataset.
5.  **Contextual Evaluation**: `rules_engine.py` looks at the sent JSON body to determine if extra flags (like using a custom encryption key) pull in extra required permissions.

---

## ❤️ Contributions

Feel free to open issues or PRs if you want to extend the `rules_engine.py` to support more complex GCP resources!
