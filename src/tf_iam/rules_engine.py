def evaluate_conditional_permissions(method_id, request_body):
    """
    Evaluates the JSON request body against conditional rules to return additional required permissions.
    """
    extra_permissions = set()

    # Rule Set: Compute Instances
    if method_id in ("compute.instances.insert", "compute.instances.update"):
        # Network rules
        for interface in request_body.get("networkInterfaces", []):
            if "network" in interface:
                extra_permissions.add("compute.networks.use")
            if "subnetwork" in interface:
                extra_permissions.add("compute.subnetworks.use")

        # Disk/Image rules
        for disk in request_body.get("disks", []):
            if "initializeParams" in disk and "sourceImage" in disk["initializeParams"]:
                extra_permissions.add("compute.images.useReadOnly")

        # Service Account rules
        for sa in request_body.get("serviceAccounts", []):
            if "email" in sa:
                extra_permissions.add("iam.serviceAccounts.actAs")

    # Rule Set: Storage Buckets
    if method_id in ("storage.buckets.insert", "storage.buckets.update"):
        # CMEK rules
        if "encryption" in request_body and "defaultKmsKeyName" in request_body["encryption"]:
            extra_permissions.add("cloudkms.cryptoKeyVersions.useToEncrypt")

    # --- Generic Cross-Service Rules (Applied to ALL resources) ---
    
    # Generic KMS Search - if any body has a KMS key, require useToEncrypt
    def scan_for_kms(obj):
        perms = set()
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k in ("kmsKeyName", "defaultKmsKeyName", "kms_key_name"):
                    perms.add("cloudkms.cryptoKeyVersions.useToEncrypt")
                else:
                    perms.update(scan_for_kms(v))
        elif isinstance(obj, list):
            for item in obj:
                perms.update(scan_for_kms(item))
        return perms

    extra_permissions.update(scan_for_kms(request_body))

    # Generic Service Account Search - if any body has an email that looks like a service account
    def scan_for_sa(obj):
        perms = set()
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k in ("serviceAccount", "serviceAccountEmail", "email"):
                    if isinstance(v, str) and "@" in v:
                        perms.add("iam.serviceAccounts.actAs")
                else:
                    perms.update(scan_for_sa(v))
        elif isinstance(obj, list):
            for item in obj:
                perms.update(scan_for_sa(item))
        return perms

    extra_permissions.update(scan_for_sa(request_body))

    return list(extra_permissions)
