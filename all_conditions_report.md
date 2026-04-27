# 📋 Magic Modules Conditional Parameters Report

This report lists all resources that have conditional constraints (mutually exclusive fields, required groups).

## 📦 google_resourcemanager_lien

🔗 **API Reference**: https://docs.cloud.google.com/resource-manager/reference/rest

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parent | required |  |
| restrictions | required |  |
| reason | required |  |
| origin | required |  |

## 📦 google_privateca_certificate_authority

🔗 **API Reference**: https://cloud.google.com/certificate-authority-service/docs/reference/rest

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| certificateAuthorityId | required |  |
| pool | required |  |
| config | required |  |
| x509Config | required |  |
| critical | required |  |
| value | required |  |
| objectId | required |  |
| objectIdPath | required |  |
| objectIdPath | required |  |
| caOptions | required |  |
| isCa | required |  |
| keyUsage | required |  |
| baseKeyUsage | required |  |
| extendedKeyUsage | required |  |
| objectIdPath | required |  |
| critical | required |  |
| subjectConfig | required |  |
| subject | required |  |
| commonName | required |  |
| dnsNames | at_least_one_of | config.0.subject_config.0.subject_alt_name.0.dns_names, config.0.subject_config.0.subject_alt_name.0.uris, config.0.subject_config.0.subject_alt_name.0.email_addresses, config.0.subject_config.0.subject_alt_name.0.ip_addresses |
| uris | at_least_one_of | config.0.subject_config.0.subject_alt_name.0.dns_names, config.0.subject_config.0.subject_alt_name.0.uris, config.0.subject_config.0.subject_alt_name.0.email_addresses, config.0.subject_config.0.subject_alt_name.0.ip_addresses |
| emailAddresses | at_least_one_of | config.0.subject_config.0.subject_alt_name.0.dns_names, config.0.subject_config.0.subject_alt_name.0.uris, config.0.subject_config.0.subject_alt_name.0.email_addresses, config.0.subject_config.0.subject_alt_name.0.ip_addresses |
| ipAddresses | at_least_one_of | config.0.subject_config.0.subject_alt_name.0.dns_names, config.0.subject_config.0.subject_alt_name.0.uris, config.0.subject_config.0.subject_alt_name.0.email_addresses, config.0.subject_config.0.subject_alt_name.0.ip_addresses |
| keySpec | required |  |
| cloudKmsKeyVersion | exactly_one_of | key_spec.0.cloud_kms_key_version, key_spec.0.algorithm, name: algorithm |
| algorithm | exactly_one_of | key_spec.0.cloud_kms_key_version, key_spec.0.algorithm |
| certificateAuthority | exactly_one_of | subordinate_config.0.certificate_authority, subordinate_config.0.pem_issuer_chain |
| pemIssuerChain | exactly_one_of | subordinate_config.0.certificate_authority, subordinate_config.0.pem_issuer_chain |

## 📦 google_privateca_certificate_template

🔗 **API Reference**: https://cloud.google.com/certificate-authority-service/docs/reference/rest

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| location | required |  |
| objectIdPath | required |  |
| objectIdPath | required |  |
| objectId | required |  |
| objectIdPath | required |  |
| value | required | name: nameConstraints |
| critical | required | name: permittedDnsNames |
| allowSubjectPassthrough | required |  |
| allowSubjectAltNamesPassthrough | required |  |
| objectIdPath | required |  |

## 📦 google_privateca_ca_pool

🔗 **API Reference**: https://cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| tier | required |  |
| signatureAlgorithm | required |  |
| allowCsrBasedIssuance | required | name: allowConfigBasedIssuance |
| allowConfigBasedIssuance | required | name: identityConstraints |
| allowSubjectPassthrough | required |  |
| allowSubjectAltNamesPassthrough | required |  |
| expression | required | name: title |
| critical | required | name: value |
| value | required | name: objectId |
| objectId | required |  |
| objectIdPath | required |  |
| objectIdPath | required |  |
| caOptions | required |  |
| keyUsage | required |  |
| baseKeyUsage | required |  |
| extendedKeyUsage | required |  |
| objectIdPath | required |  |
| critical | required | name: permittedDnsNames |
| publishCaCert | required | name: publishCrl |
| publishCrl | required | name: encodingFormat |

## 📦 google_privateca_certificate

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| pool | required |  |
| name | required |  |
| pemCsr | exactly_one_of | pem_csr, config, name: config |
| config | exactly_one_of | pem_csr, config |
| x509Config | required |  |
| critical | required |  |
| value | required |  |
| objectId | required |  |
| objectIdPath | required |  |
| objectIdPath | required |  |
| keyUsage | required |  |
| baseKeyUsage | required |  |
| extendedKeyUsage | required |  |
| objectIdPath | required |  |
| critical | required |  |
| subjectConfig | required |  |
| subject | required |  |
| organization | required |  |
| commonName | required |  |
| dnsNames | at_least_one_of | config.0.subject_config.0.subject_alt_name.0.dns_names, config.0.subject_config.0.subject_alt_name.0.uris, config.0.subject_config.0.subject_alt_name.0.email_addresses, config.0.subject_config.0.subject_alt_name.0.ip_addresses |
| uris | at_least_one_of | config.0.subject_config.0.subject_alt_name.0.dns_names, config.0.subject_config.0.subject_alt_name.0.uris, config.0.subject_config.0.subject_alt_name.0.email_addresses, config.0.subject_config.0.subject_alt_name.0.ip_addresses |
| emailAddresses | at_least_one_of | config.0.subject_config.0.subject_alt_name.0.dns_names, config.0.subject_config.0.subject_alt_name.0.uris, config.0.subject_config.0.subject_alt_name.0.email_addresses, config.0.subject_config.0.subject_alt_name.0.ip_addresses |
| ipAddresses | at_least_one_of | config.0.subject_config.0.subject_alt_name.0.dns_names, config.0.subject_config.0.subject_alt_name.0.uris, config.0.subject_config.0.subject_alt_name.0.email_addresses, config.0.subject_config.0.subject_alt_name.0.ip_addresses |
| publicKey | required |  |
| format | required |  |

## 📦 google_cloudfunctions_cloud_function

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| name | required | name: description |
| sourceArchiveUrl | exactly_one_of | source_repository, source_archive_url, source_upload_url, name: sourceUploadUrl |
| sourceUploadUrl | exactly_one_of | source_repository, source_archive_url, source_upload_url, name: sourceRepository |
| sourceRepository | exactly_one_of | source_repository, source_archive_url, source_upload_url |
| url | required | name: deployedUrl |
| eventType | required | name: resource |
| resource | required | name: service |

## 📦 google_essentialcontacts_contact

🔗 **API Reference**: https://docs.cloud.google.com/resource-manager/docs/reference/essentialcontacts/rest/v1/projects.contacts

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parent | required |  |
| email | required |  |
| notificationCategorySubscriptions | required |  |
| languageTag | required |  |

## 📦 google_orgpolicy_policy

🔗 **API Reference**: https://docs.cloud.google.com/resource-manager/docs/reference/orgpolicy/rest/v2/organizations.policies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parent | required |  |
| name | required |  |

## 📦 google_orgpolicy_custom_constraint

🔗 **API Reference**: https://docs.cloud.google.com/resource-manager/docs/reference/orgpolicy/rest/v2/organizations.constraints

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parent | required |  |
| name | required |  |
| condition | required | name: actionType |
| actionType | required |  |
| methodTypes | required |  |
| resourceTypes | required |  |

## 📦 google_workstations_workstation_config

🔗 **API Reference**: https://cloud.google.com/workstations/docs/reference/rest/v1/projects.locations.workstationClusters.workstationConfigs/create

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| workstationConfigId | required |  |
| workstationClusterId | required |  |
| location | required |  |
| type | required | name: count |
| count | required | name: boostConfigs |
| id | required | name: machineType |
| type | required | name: count |
| count | required | name: vmTags |
| kmsKey | required | name: kmsKeyServiceAccount |
| kmsKeyServiceAccount | required | name: readinessChecks |
| path | required | name: port |
| port | required | name: degraded |

## 📦 google_workstations_workstation

🔗 **API Reference**: https://cloud.google.com/workstations/docs/reference/rest/v1/projects.locations.workstationClusters.workstationConfigs.workstations

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| workstationId | required |  |
| workstationConfigId | required |  |
| workstationClusterId | required |  |
| location | required |  |

## 📦 google_workstations_workstation_cluster

🔗 **API Reference**: https://cloud.google.com/workstations/docs/reference/rest/v1/projects.locations.workstationClusters/create

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| workstationClusterId | required |  |
| network | required |  |
| subnetwork | required |  |
| enablePrivateEndpoint | required |  |
| domain | required |  |

## 📦 google_datastream_private_connection

🔗 **API Reference**: https://cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.privateConnections

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| privateConnectionId | required |  |
| create_without_validation | required |  |
| location | required |  |
| displayName | required | name: state |
| vpcPeeringConfig | exactly_one_of | vpc_peering_config, psc_interface_config |
| vpc | required | name: subnet |
| subnet | required | name: pscInterfaceConfig |
| pscInterfaceConfig | exactly_one_of | vpc_peering_config, psc_interface_config |
| networkAttachment | required |  |

## 📦 google_datastream_stream

🔗 **API Reference**: https://cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| streamId | required |  |
| create_without_validation | required |  |
| location | required |  |
| displayName | required | name: sourceConfig |
| sourceConfig | required |  |
| sourceConnectionProfile | required |  |
| mysqlSourceConfig | exactly_one_of | source_config.0.mysql_source_config, source_config.0.oracle_source_config, source_config.0.postgresql_source_config, source_config.0.sql_server_source_config |
| mysqlDatabases | required |  |
| database | required | name: mysqlTables |
| table | required | name: mysqlColumns |
| mysqlDatabases | required |  |
| database | required | name: mysqlTables |
| table | required | name: mysqlColumns |
| binaryLogPosition | conflicts | source_config.0.mysql_source_config.gtid |
| gtid | conflicts | source_config.0.mysql_source_config.binaryLogPosition |
| oracleSourceConfig | exactly_one_of | source_config.0.mysql_source_config, source_config.0.oracle_source_config, source_config.0.postgresql_source_config, source_config.0.sql_server_source_config |
| oracleSchemas | required |  |
| schema | required | name: oracleTables |
| table | required | name: oracleColumns |
| oracleSchemas | required |  |
| schema | required | name: oracleTables |
| table | required | name: oracleColumns |
| postgresqlSourceConfig | exactly_one_of | source_config.0.mysql_source_config, source_config.0.oracle_source_config, source_config.0.postgresql_source_config, source_config.0.sql_server_source_config |
| postgresqlSchemas | required |  |
| schema | required | name: postgresqlTables |
| table | required | name: postgresqlColumns |
| postgresqlSchemas | required |  |
| schema | required | name: postgresqlTables |
| table | required | name: postgresqlColumns |
| replicationSlot | required | name: publication |
| publication | required | name: maxConcurrentBackfillTasks |
| sqlServerSourceConfig | exactly_one_of | source_config.0.mysql_source_config, source_config.0.oracle_source_config, source_config.0.postgresql_source_config, source_config.0.sql_server_source_config |
| schemas | required |  |
| schema | required | name: tables |
| table | required | name: columns |
| schemas | required |  |
| schema | required | name: tables |
| table | required | name: columns |
| salesforceSourceConfig | exactly_one_of | source_config.0.mysql_source_config, source_config.0.oracle_source_config, source_config.0.postgresql_source_config, source_config.0.sql_server_source_config |
| objects | required |  |
| objects | required |  |
| pollingInterval | required | name: spannerSourceConfig |
| spannerSourceConfig | exactly_one_of | source_config.0.mysql_source_config, source_config.0.oracle_source_config, source_config.0.postgresql_source_config, source_config.0.sql_server_source_config |
| schemas | required |  |
| schema | required | name: tables |
| table | required | name: columns |
| schemas | required |  |
| schema | required | name: tables |
| table | required | name: columns |
| mongodbSourceConfig | exactly_one_of | source_config.0.mysql_source_config, source_config.0.oracle_source_config, source_config.0.postgresql_source_config, source_config.0.sql_server_source_config |
| destinationConfig | required |  |
| destinationConnectionProfile | required |  |
| gcsDestinationConfig | exactly_one_of | destination_config.0.gcs_destination_config, destination_config.0.bigquery_destination_config |
| avroFileFormat | exactly_one_of | destination_config.0.gcs_destination_config.0.avro_file_format, destination_config.0.gcs_destination_config.0.json_file_format |
| jsonFileFormat | exactly_one_of | destination_config.0.gcs_destination_config.0.avro_file_format, destination_config.0.gcs_destination_config.0.json_file_format |
| bigqueryDestinationConfig | exactly_one_of | destination_config.0.gcs_destination_config, destination_config.0.bigquery_destination_config |
| singleTargetDataset | exactly_one_of | destination_config.0.bigquery_destination_config.0.single_target_dataset, destination_config.0.bigquery_destination_config.0.source_hierarchy_datasets |
| datasetId | required |  |
| sourceHierarchyDatasets | exactly_one_of | destination_config.0.bigquery_destination_config.0.single_target_dataset, destination_config.0.bigquery_destination_config.0.source_hierarchy_datasets |
| datasetTemplate | required |  |
| location | required | name: datasetIdPrefix |
| bucket | required | name: connectionName |
| connectionName | required | name: fileFormat |
| fileFormat | required |  |
| tableFormat | required |  |
| merge | conflicts | destination_config.0.bigquery_destination_config.0.append_only |
| appendOnly | conflicts | destination_config.0.bigquery_destination_config.0.merge |
| backfillAll | exactly_one_of | backfill_all, backfill_none |
| mysqlDatabases | required |  |
| database | required | name: mysqlTables |
| table | required | name: mysqlColumns |
| postgresqlSchemas | required |  |
| schema | required | name: postgresqlTables |
| table | required | name: postgresqlColumns |
| oracleSchemas | required |  |
| schema | required | name: oracleTables |
| table | required | name: oracleColumns |
| schemas | required |  |
| schema | required | name: tables |
| table | required | name: columns |
| objects | required |  |
| schemas | required |  |
| schema | required | name: tables |
| table | required | name: columns |
| column | required | name: dataType |
| mongodbExcludedObjects | required |  |
| mongodbExcludedObjects | required |  |
| mongodbExcludedObjects | required |  |
| backfillNone | exactly_one_of | backfill_all, backfill_none |
| customizationRules | required |  |
| column | required | name: start |
| start | required | name: end |
| end | required | name: interval |
| interval | required | name: timeUnitPartition |
| column | required | name: partitioningTimeGranularity |
| columns | required |  |
| objectFilter | required |  |
| schema | required | name: table |
| table | required | name: mysqlIdentifier |
| database | required | name: table |
| table | required | name: postgresqlIdentifier |
| schema | required | name: table |
| table | required | name: sqlServerIdentifier |
| schema | required | name: table |
| table | required | name: salesforceIdentifier |
| objectName | required | name: spannerIdentifier |
| table | required | name: mongodbIdentifier |
| database | required | name: collection |
| collection | required |  |

## 📦 google_datastream_connection_profile

🔗 **API Reference**: https://cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.connectionProfiles

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| connectionProfileId | required |  |
| create_without_validation | required |  |
| location | required |  |
| displayName | required | name: oracleProfile |
| oracleProfile | exactly_one_of | oracle_profile, gcs_profile, mysql_profile, bigquery_profile |
| hostname | required | name: port |
| username | required | name: password |
| databaseService | required | name: connectionAttributes |
| gcsProfile | exactly_one_of | oracle_profile, gcs_profile, mysql_profile, bigquery_profile |
| bucket | required | name: rootPath |
| mysqlProfile | exactly_one_of | oracle_profile, gcs_profile, mysql_profile, bigquery_profile |
| hostname | required | name: port |
| username | required | name: password |
| bigqueryProfile | exactly_one_of | oracle_profile, gcs_profile, mysql_profile, bigquery_profile |
| postgresqlProfile | exactly_one_of | oracle_profile, gcs_profile, mysql_profile, bigquery_profile |
| hostname | required | name: port |
| username | required | name: password |
| database | required | name: sslConfig |
| serverVerification | exactly_one_of | ssl_config.0.server_verification, ssl_config.0.server_and_client_verification |
| caCertificate | required |  |
| serverAndClientVerification | exactly_one_of | ssl_config.0.server_verification, ssl_config.0.server_and_client_verification |
| clientCertificate | required |  |
| clientKey | required |  |
| caCertificate | required |  |
| salesforceProfile | exactly_one_of | oracle_profile, gcs_profile, mysql_profile, bigquery_profile |
| domain | required | name: userCredentials |
| userCredentials | exactly_one_of | user_credentials, oauth2_client_credentials |
| oauth2ClientCredentials | exactly_one_of | user_credentials, oauth2_client_credentials |
| spannerProfile | exactly_one_of | oracle_profile, gcs_profile, mysql_profile, bigquery_profile |
| database | required | name: host |
| sqlServerProfile | exactly_one_of | oracle_profile, gcs_profile, mysql_profile, bigquery_profile |
| hostname | required | name: port |
| username | required | name: password |
| database | required | name: mongodbProfile |
| mongodbProfile | exactly_one_of | oracle_profile, gcs_profile, mysql_profile, bigquery_profile |
| hostAddresses | required |  |
| hostname | required | name: port |
| username | required | name: password |
| clientKey | required |  |
| clientKey | exactly_one_of | mongodb_profile.0.ssl_config.0.client_key, mongodb_profile.0.ssl_config.0.secret_manager_stored_client_key |
| secretManagerStoredClientKey | required |  |
| secretManagerStoredClientKey | exactly_one_of | mongodb_profile.0.ssl_config.0.client_key, mongodb_profile.0.ssl_config.0.secret_manager_stored_client_key |
| srvConnectionFormat | at_least_one_of | mongodb_profile.0.srv_connection_format, mongodb_profile.0.standard_connection_format |
| standardConnectionFormat | at_least_one_of | mongodb_profile.0.srv_connection_format, mongodb_profile.0.standard_connection_format |
| forwardSshConnectivity | conflicts | private_connectivity |
| hostname | required | name: username |
| username | required | name: port |
| password | conflicts | forward_ssh_connectivity.0.private_key |
| privateKey | conflicts | forward_ssh_connectivity.0.password |
| privateConnectivity | conflicts | forward_ssh_connectivity |
| privateConnection | required |  |

## 📦 google_servicenetworking_vpc_service_controls

🔗 **API Reference**: https://cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| network | required |  |
| service | required |  |
| project | required |  |
| enabled | required |  |

## 📦 google_binaryauthorization_policy

🔗 **API Reference**: https://cloud.google.com/binary-authorization/docs/reference/rest/

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| namePattern | required | name: clusterAdmissionRules |
| evaluationMode | required |  |
| enforcementMode | required |  |
| defaultAdmissionRule | required |  |
| evaluationMode | required |  |
| enforcementMode | required |  |

## 📦 google_binaryauthorization_attestor

🔗 **API Reference**: https://cloud.google.com/binary-authorization/docs/reference/rest/

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| attestationAuthorityNote | required |  |
| noteReference | required |  |

## 📦 google_apihub_curation

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: curationId |
| None | required |  |
| None | required | name: endpoint |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_apihub_host_project_registration

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: hostProjectRegistrationId |
| None | required |  |
| None | required |  |

## 📦 google_apihub_plugin

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: pluginId |
| None | required |  |
| None | required | name: displayName |
| None | required | name: description |
| None | required | name: triggerMode |
| None | required | name: documentation |
| None | required |  |
| None | required | name: additionalConfigTemplate |
| None | required | name: displayName |
| None | required | name: description |
| None | required | name: displayName |
| None | required | name: description |
| None | required | name: valueType |
| None | required | name: description |
| None | required | name: hostingService |

## 📦 google_apihub_plugin_instance

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: plugin |
| None | required | name: pluginInstanceId |
| None | required |  |
| None | required | name: userPasswordConfig |
| None | required | name: password |
| None | required |  |
| None | required | name: apiKeyConfig |
| None | required | name: apiKey |
| None | required |  |
| None | required | name: httpElementLocation |
| None | required | name: oauth2ClientCredentialsConfig |
| None | required |  |
| None | required | name: clientId |
| None | required | name: authType |
| None | required | name: state |
| None | required | name: errorMessage |
| None | required |  |
| None | required | name: state |
| None | required | name: curationType |
| None | required | name: scheduleTimeZone |

## 📦 google_apihub_api_hub_instance

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: apiHubInstanceId |
| None | required |  |

## 📦 google_beyondcorp_app_gateway

🔗 **API Reference**: https://cloud.google.com/beyondcorp/docs/reference/rest#rest-resource:-v1.projects.locations.appgateways

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |

## 📦 google_beyondcorp_security_gateway

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: securityGatewayId |
| None | required |  |

## 📦 google_beyondcorp_security_gateway_application

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: applicationId |
| None | required |  |
| None | required | name: ports |
| None | required |  |
| None | required |  |
| None | required | name: external |
| None | required |  |
| None | required | name: port |
| None | required | name: proxyProtocol |

## 📦 google_beyondcorp_app_connection

🔗 **API Reference**: https://cloud.google.com/beyondcorp/docs/reference/rest#rest-resource:-v1.projects.locations.appconnections

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| applicationEndpoint | required |  |
| host | required | name: port |
| port | required | name: connectors |
| appGateway | required | name: type |

## 📦 google_beyondcorp_app_connector

🔗 **API Reference**: https://cloud.google.com/beyondcorp/docs/reference/rest#rest-resource:-v1.projects.locations.appconnectors

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| principalInfo | required |  |
| serviceAccount | required |  |
| email | required | name: state |

## 📦 google_apigee_sync_authorization

🔗 **API Reference**: https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#getsyncauthorization

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| identities | required |  |

## 📦 google_apigee_environment_api_revision_deployment

🔗 **API Reference**: https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.deployments/deploy

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| org_id | required |  |
| environment | required |  |
| api | required |  |
| revision | required |  |

## 📦 google_apigee_api_product

🔗 **API Reference**: https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#ApiProduct

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_apigee_developer

🔗 **API Reference**: https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required | name: "lastName" |
| None | required | name: "userName" |
| None | required | name: "attributes" |

## 📦 google_apigee_security_monitoring_condition

🔗 **API Reference**: https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityMonitoringConditions/create

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| orgId | required |  |
| conditionId | required |  |
| profile | required | name: scope |
| scope | required | name: includeAllResources |
| includeAllResources | exactly_one_of | include_all_resources |
| includeAllResources | required |  |
| includeAllResources | required |  |
| includeAllResources | required |  |
| includeAllResources | exactly_one_of |  |

## 📦 google_apigee_api_deployment

🔗 **API Reference**: https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.deployments

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| org_id | required |  |
| environment | required |  |
| proxy_id | required |  |
| revision | required |  |

## 📦 google_apigee_developer_app

🔗 **API Reference**: https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required | name: "appFamily" |
| None | required | name: "keyExpiresIn" |

## 📦 google_apigee_instance_attachment

🔗 **API Reference**: https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances.attachments/create

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| instanceId | required |  |
| environment | required | name: name |

## 📦 google_apigee_environment_addons_config

🔗 **API Reference**: https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.addonsConfig/setAddonEnablement

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| envId | required |  |

## 📦 google_apigee_addons_config

🔗 **API Reference**: https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#setaddons

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| org | required |  |

## 📦 google_apigee_envgroup

🔗 **API Reference**: https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups/create

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| orgId | required |  |
| name | required |  |
| hostnames | required |  |

## 📦 google_apigee_target_server

🔗 **API Reference**: https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.targetservers/create

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| envId | required |  |
| name | required |  |
| host | required | name: port |
| port | required | name: isEnabled |
| enabled | required | name: clientAuthEnabled |

## 📦 google_apigee_security_profile_v2

🔗 **API Reference**: https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityProfilesV2/create

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| orgId | required |  |
| profileId | required |  |
| profileAssessmentConfigs | required |  |
| weight | required |  |

## 📦 google_apigee_env_references

🔗 **API Reference**: https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.references/create

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| envId | required |  |
| name | required |  |
| resourceType | required |  |
| refers | required |  |

## 📦 google_apigee_environment_keyvaluemaps_entries

🔗 **API Reference**: https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps.entries/create

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| env_keyvaluemap_id | required |  |
| name | required |  |
| value | required |  |

## 📦 google_apigee_security_feedback

🔗 **API Reference**: https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityFeedback/create

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| orgId | required |  |
| feedbackId | required |  |
| feedbackContexts | required |  |
| feedbackContexts | required |  |
| feedbackContexts | required |  |
| feedbackType | required |  |

## 📦 google_apigee_envgroup_attachment

🔗 **API Reference**: https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups.attachments/create

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| envgroupId | required |  |
| environment | required | name: name |

## 📦 google_apigee_instance

🔗 **API Reference**: https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances/create

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| orgId | required |  |
| name | required |  |
| location | required |  |
| consumerAcceptList | required |  |
| enabled | required |  |

## 📦 google_apigee_security_action

🔗 **API Reference**: https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityActions/create

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| orgId | required |  |
| envId | required |  |
| securityActionId | required |  |
| state | required |  |
| conditionConfig | required |  |
| allow | exactly_one_of | allow, deny, flag |
| deny | exactly_one_of | allow, deny, flag |
| flag | exactly_one_of | allow, deny, flag |
| expireTime | conflicts | ttl, name: ttl |
| ttl | conflicts | expireTime |

## 📦 google_apigee_nat_address

🔗 **API Reference**: https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances.natAddresses

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| instanceId | required |  |
| name | required |  |
| activate | required |  |

## 📦 google_apigee_endpoint_attachment

🔗 **API Reference**: https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.endpointAttachments/create

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| orgId | required |  |
| endpointAttachmentId | required |  |
| location | required | name: host |
| serviceAttachment | required | name: connectionState |

## 📦 google_apigee_environment_keyvaluemaps

🔗 **API Reference**: https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keyvaluemaps/create

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| envId | required |  |
| name | required |  |

## 📦 google_apigee_organization

🔗 **API Reference**: https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| projectId | required |  |
| retention | required |  |

## 📦 google_apigee_env_keystore

🔗 **API Reference**: https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keystores/create

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| envId | required |  |

## 📦 google_apigee_keystores_aliases_self_signed_cert

🔗 **API Reference**: https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keystores.aliases/create

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| orgId | required |  |
| environment | required |  |
| keystore | required |  |
| alias | required |  |
| sigAlg | required |  |
| subject | required |  |

## 📦 google_apigee_control_plane_access

🔗 **API Reference**: https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/updateControlPlaneAccess

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |

## 📦 google_apigee_environment

🔗 **API Reference**: https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/create

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| orgId | required |  |
| name | required |  |
| displayName | required |  |
| description | required |  |
| forwardProxyUri | required | name: properties |
| headerIndexAlgorithm | exactly_one_of | client_ip_resolution_config.0.header_index_algorithm |
| headerIndexAlgorithm | required | name: ipHeaderIndex |
| headerIndexAlgorithm | required |  |

## 📦 google_apigee_app_group

🔗 **API Reference**: https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |

## 📦 google_apigee_dns_zone

🔗 **API Reference**: https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.dnsZones/create

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| orgId | required |  |
| dnsZoneId | required |  |
| domain | required | name: description |
| description | required | name: peeringConfig |
| peeringConfig | required |  |
| targetProjectId | required | name: targetNetworkId |
| targetNetworkId | required |  |

## 📦 google_developerconnect_account_connector

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_developerconnect_connection

🔗 **API Reference**: https://cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| developer_connect_connection_http_conn_bearer | required | name: connectionId |
| developer_connect_connection_http_conn_bearer | required |  |
| developer_connect_connection_http_conn_bearer | required | name: authorizerCredential |
| developer_connect_connection_http_conn_bearer | required | name: username |
| developer_connect_connection_http_conn_bearer | required | name: serverVersion |
| developer_connect_connection_http_conn_bearer | required | name: appId |
| developer_connect_connection_http_conn_bearer | required |  |
| developer_connect_connection_http_conn_bearer | required | name: username |
| developer_connect_connection_http_conn_bearer | required | name: sslCaCertificate |
| developer_connect_connection_http_conn_bearer | required | name: webhookSecretSecretVersion |
| developer_connect_connection_http_conn_bearer | required | name: readAuthorizerCredential |
| developer_connect_connection_http_conn_bearer | required |  |
| developer_connect_connection_http_conn_bearer | required | name: username |
| developer_connect_connection_http_conn_bearer | required | name: webhookSecretSecretVersion |
| developer_connect_connection_http_conn_bearer | required | name: readAuthorizerCredential |
| developer_connect_connection_http_conn_bearer | required |  |
| developer_connect_connection_http_conn_bearer | required | name: username |
| developer_connect_connection_http_conn_bearer | required |  |
| developer_connect_connection_http_conn_bearer | required | name: username |
| developer_connect_connection_http_conn_bearer | required | name: readAuthorizerCredential |
| developer_connect_connection_http_conn_bearer | required |  |
| developer_connect_connection_http_conn_bearer | required | name: username |
| developer_connect_connection_http_conn_bearer | required |  |
| developer_connect_connection_http_conn_bearer | required | name: serviceDirectoryConfig |
| developer_connect_connection_http_conn_bearer | required | name: sslCaCertificate |
| developer_connect_connection_http_conn_bearer | required | name: updateTime |
| developer_connect_connection_http_conn_bearer | required | name: readAuthorizerCredential |
| developer_connect_connection_http_conn_bearer | required |  |
| developer_connect_connection_http_conn_bearer | required | name: username |
| developer_connect_connection_http_conn_bearer | required |  |
| developer_connect_connection_http_conn_bearer | required | name: username |
| developer_connect_connection_http_conn_bearer | required |  |
| developer_connect_connection_http_conn_bearer | required |  |
| developer_connect_connection_http_conn_bearer | required |  |
| developer_connect_connection_http_conn_bearer | required |  |

## 📦 google_developerconnect_insights_config

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| developer_connect_insights_config_projects | required | name: insightsConfigId |
| developer_connect_insights_config_projects | required |  |
| developer_connect_insights_config_projects | conflicts | targetProjects, name: targetProjects |
| developer_connect_insights_config_projects | conflicts | appHubApplication |
| developer_connect_insights_config_projects | required | name: artifactRegistryPackage |
| developer_connect_insights_config_projects | required | name: googleArtifactAnalysis |
| developer_connect_insights_config_projects | required | name: uri |
| developer_connect_insights_config_projects | required | name: state |
| developer_connect_insights_config_projects | required | name: deployment |
| developer_connect_insights_config_projects | required | name: state |

## 📦 google_developerconnect_git_repository_link

🔗 **API Reference**: https://cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| parent_connection | required |  |
| gitRepositoryLinkId | required |  |
| cloneUri | required | name: createTime |

## 📦 google_kms_organization_kaj_policy_config

🔗 **API Reference**: https://cloud.google.com/kms/docs/reference/rest/v1/KeyAccessJustificationsPolicyConfig

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| organization | required |  |

## 📦 google_kms_key_ring

🔗 **API Reference**: https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |

## 📦 google_kms_ekm_connection

🔗 **API Reference**: https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.ekmConnections

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| serviceResolvers | required |  |
| serviceDirectoryService | required | name: hostname |
| hostname | required | name: serverCertificates |
| serverCertificates | required |  |
| rawDer | required | name: parsed |
| endpointFilter | required |  |
| keyManagementMode | required |  |
| etag | required |  |
| cryptoSpacePath | required |  |

## 📦 google_kms_secret_ciphertext

🔗 **API Reference**: https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/encrypt

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |

## 📦 google_kms_crypto_key

🔗 **API Reference**: https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| keyRing | required |  |
| name | required |  |
| algorithm | required | name: protectionLevel |

## 📦 google_kms_crypto_key_version

🔗 **API Reference**: https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| cryptoKey | required |  |

## 📦 google_kms_folder_kaj_policy_config

🔗 **API Reference**: https://cloud.google.com/kms/docs/reference/rest/v1/KeyAccessJustificationsPolicyConfig

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| folder | required |  |

## 📦 google_kms_autokey_config

🔗 **API Reference**: https://cloud.google.com/kms/docs/reference/rest/v1/AutokeyConfig

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| folder | required |  |

## 📦 google_kms_key_ring_import_job

🔗 **API Reference**: https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_kms_key_handle

🔗 **API Reference**: https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyHandles

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| resourceTypeSelector | required |  |

## 📦 google_runtimeconfig_config

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |

## 📦 google_storagebatchoperations_job

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | exactly_one_of | bucket_list.0.buckets.0.prefix_list, bucket_list.0.buckets.0.manifest |
| None | exactly_one_of | bucket_list.0.buckets.0.prefix_list, bucket_list.0.buckets.0.manifest |
| None | exactly_one_of | delete_object, put_metadata, rewrite_object, put_object_hold |
| None | required |  |
| None | exactly_one_of | delete_object, put_metadata, rewrite_object, put_object_hold |
| None | at_least_one_of | put_metadata.0.content_disposition, put_metadata.0.content_encoding, put_metadata.0.content_language, put_metadata.0.content_type |
| None | at_least_one_of | put_metadata.0.content_disposition, put_metadata.0.content_encoding, put_metadata.0.content_language, put_metadata.0.content_type |
| None | at_least_one_of | put_metadata.0.content_disposition, put_metadata.0.content_encoding, put_metadata.0.content_language, put_metadata.0.content_type |
| None | at_least_one_of | put_metadata.0.content_disposition, put_metadata.0.content_encoding, put_metadata.0.content_language, put_metadata.0.content_type |
| None | at_least_one_of | put_metadata.0.content_disposition, put_metadata.0.content_encoding, put_metadata.0.content_language, put_metadata.0.content_type |
| None | at_least_one_of | put_metadata.0.content_disposition, put_metadata.0.content_encoding, put_metadata.0.content_language, put_metadata.0.content_type |
| None | at_least_one_of | put_metadata.0.content_disposition, put_metadata.0.content_encoding, put_metadata.0.content_language, put_metadata.0.content_type |
| None | exactly_one_of | delete_object, put_metadata, rewrite_object, put_object_hold |
| None | required |  |
| None | exactly_one_of | delete_object, put_metadata, rewrite_object, put_object_hold |

## 📦 google_saasservicemgmt_tenant

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: tenantId |
| None | required |  |
| None | required | name: uid |

## 📦 google_saasservicemgmt_unit_operation

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_saasservicemgmt_saas

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: saasId |
| None | required |  |

## 📦 google_saasservicemgmt_unit_kind

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: unitKindId |
| None | required |  |
| None | required | name: unitKind |
| None | required | name: etag |
| None | required | name: outputVariable |
| None | required | name: to |
| None | required | name: ignoreForLookup |
| None | required | name: variable |
| None | required | name: labels |
| None | required | name: outputVariable |
| None | required | name: to |
| None | required | name: ignoreForLookup |
| None | required | name: variable |
| None | required | name: saas |
| None | required | name: uid |

## 📦 google_saasservicemgmt_release

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: releaseId |
| None | required |  |
| None | required | name: inputVariables |
| None | required | name: labels |
| None | required | name: releaseRequirements |
| None | required | name: updateTime |

## 📦 google_saasservicemgmt_rollout_kind

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_saasservicemgmt_unit

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: unitId |
| None | required |  |
| None | required | name: message |
| None | required | name: reason |
| None | required | name: status |
| None | required | name: type |
| None | required | name: createTime |
| None | required | name: labels |
| None | required | name: pendingOperations |

## 📦 google_bigquerydatapolicyv2_data_policy

🔗 **API Reference**: https://cloud.google.com/bigquery/docs/reference/bigquerydatapolicy/rest/v2/projects.locations.dataPolicies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| bigquery_datapolicyv2_datapolicy_withgrantees_test | required |  |
| bigquery_datapolicyv2_datapolicy_withgrantees_test | required | name: etag |
| bigquery_datapolicyv2_datapolicy_withgrantees_test | required |  |

## 📦 google_privilegedaccessmanager_settings

🔗 **API Reference**: https://cloud.google.com/iam/docs/reference/pam/rest/v1beta/folders.locations/updateSettings

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| parent | required |  |
| disableAllNotifications | exactly_one_of | email_notification_settings.0.disable_all_notifications, email_notification_settings.0.custom_notification_behavior |
| customNotificationBehavior | exactly_one_of | email_notification_settings.0.disable_all_notifications, email_notification_settings.0.custom_notification_behavior |

## 📦 google_privilegedaccessmanager_entitlement

🔗 **API Reference**: https://cloud.google.com/iam/docs/reference/pam/rest

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| entitlementId | required |  |
| parent | required |  |
| eligibleUsers | required |  |
| principals | required |  |
| manualApprovals | required |  |
| steps | required |  |
| approvers | required |  |
| principals | required |  |
| privilegedAccess | required |  |
| gcpIamAccess | required |  |
| resourceType | required | name: resource |
| resource | required | name: roleBindings |
| roleBindings | required |  |
| role | required | name: conditionExpression |
| maxRequestDuration | required | name: state |
| requesterJustificationConfig | required |  |
| notMandatory | conflicts | unstructured |
| unstructured | conflicts | not_mandatory |

## 📦 google_tpuv2_queued_resource

🔗 **API Reference**: https://cloud.google.com/tpu/docs/reference/rest/v2/projects.locations.queuedResources

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_tpuv2_vm

🔗 **API Reference**: https://cloud.google.com/tpu/docs/reference/rest/v2/projects.locations.nodes

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | conflicts | accelerator_config |
| None | conflicts | network_configs |
| None | conflicts | network_config |
| None | required |  |
| None | required |  |
| None | conflicts | accelerator_type |
| None | required |  |
| None | required |  |

## 📦 google_networkservices_service_binding

🔗 **API Reference**: https://cloud.google.com/traffic-director/docs/reference/network-services/rest/v1beta1/projects.locations.serviceBindings

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| service | required |  |

## 📦 google_networkservices_mesh

🔗 **API Reference**: https://cloud.google.com/traffic-director/docs/reference/network-services/rest/v1beta1/projects.locations.meshes

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |

## 📦 google_networkservices_edge_cache_service

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| routing | required |  |
| host_rule | required |  |
| hosts | required |  |
| pathMatcher | required |  |
| path_matcher | required |  |
| name | required | name: description |
| route_rule | required |  |
| priority | required | name: description |
| match_rule | required |  |
| headerName | required | name: presentMatch |
| name | required | name: presentMatch |
| fullPathMatch | conflicts |  |
| headerName | required | name: headerValue |
| headerValue | required |  |
| headerName | required | name: headerValue |
| headerValue | required | name: replace |
| headerName | required |  |
| headerName | required |  |
| actions | required |  |
| maxAge | required | name: allowCredentials |
| enable | required |  |

## 📦 google_networkservices_http_route

🔗 **API Reference**: https://cloud.google.com/traffic-director/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| hostnames | required |  |
| rules | required |  |
| fullPathMatch | exactly_one_of | fullPathMatch, prefixMatch, regexMatch, name: prefixMatch |
| prefixMatch | exactly_one_of | fullPathMatch, prefixMatch, regexMatch, name: regexMatch |
| regexMatch | exactly_one_of | fullPathMatch, prefixMatch, regexMatch, name: queryParameters |
| exactMatch | exactly_one_of | exactMatch, regexMatch, presentMatch, name: regexMatch |
| regexMatch | exactly_one_of | exactMatch, regexMatch, presentMatch, name: presentMatch |
| presentMatch | exactly_one_of | exactMatch, regexMatch, presentMatch, name: headers |
| exactMatch | exactly_one_of | exactMatch, regexMatch, prefixMatch, presentMatch |
| regexMatch | exactly_one_of | exactMatch, regexMatch, prefixMatch, presentMatch |
| prefixMatch | exactly_one_of | exactMatch, regexMatch, prefixMatch, presentMatch |
| presentMatch | exactly_one_of | exactMatch, regexMatch, prefixMatch, presentMatch |
| suffixMatch | exactly_one_of | exactMatch, regexMatch, prefixMatch, presentMatch |
| rangeMatch | exactly_one_of | exactMatch, regexMatch, prefixMatch, presentMatch |
| start | required | name: end |
| end | required | name: action |

## 📦 google_networkservices_multicast_domain_activation

🔗 **API Reference**: https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomainActivations

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: multicastDomainActivationId |
| None | required |  |
| None | required | name: name |

## 📦 google_networkservices_lb_traffic_extension

🔗 **API Reference**: https://cloud.google.com/service-extensions/docs/reference/rest/v1beta1/projects.locations.lbTrafficExtensions

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| forwardingRules | required |  |
| extensionChains | required |  |
| name | required | name: matchCondition |
| matchCondition | required |  |
| celExpression | required | name: extensions |
| extensions | required |  |
| name | required | name: authority |
| service | required |  |
| loadBalancingScheme | required |  |

## 📦 google_networkservices_tls_route

🔗 **API Reference**: https://cloud.google.com/traffic-director/docs/reference/network-services/rest/v1beta1/projects.locations.tlsRoutes

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| rules | required |  |
| matches | required |  |
| action | required |  |

## 📦 google_networkservices_lb_route_extension

🔗 **API Reference**: https://cloud.google.com/service-extensions/docs/reference/rest/v1/projects.locations.lbRouteExtensions

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| forwardingRules | required |  |
| extensionChains | required |  |
| name | required | name: matchCondition |
| matchCondition | required |  |
| celExpression | required | name: extensions |
| extensions | required |  |
| name | required | name: authority |
| service | required |  |
| loadBalancingScheme | required |  |

## 📦 google_networkservices_lb_edge_extension

🔗 **API Reference**: https://cloud.google.com/service-extensions/docs/reference/rest/v1beta1/projects.locations.lbEdgeExtensions

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| forwardingRules | required |  |
| extensionChains | required |  |
| name | required | name: matchCondition |
| matchCondition | required |  |
| celExpression | required | name: extensions |
| extensions | required |  |
| name | required | name: service |
| service | required |  |
| loadBalancingScheme | required |  |

## 📦 google_networkservices_edge_cache_origin

🔗 **API Reference**: https://cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheOrigins

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| originAddress | required |  |
| connectTimeout | at_least_one_of | timeout.0.connect_timeout, timeout.0.max_attempts_timeout, timeout.0.response_timeout, timeout.0.read_timeout |
| maxAttemptsTimeout | at_least_one_of | timeout.0.connect_timeout, timeout.0.max_attempts_timeout, timeout.0.response_timeout, timeout.0.read_timeout |
| responseTimeout | at_least_one_of | timeout.0.connect_timeout, timeout.0.max_attempts_timeout, timeout.0.response_timeout, timeout.0.read_timeout |
| readTimeout | at_least_one_of | timeout.0.connect_timeout, timeout.0.max_attempts_timeout, timeout.0.response_timeout, timeout.0.read_timeout |
| accessKeyId | required | name: secretAccessKeyVersion |
| secretAccessKeyVersion | required | name: originRegion |
| originRegion | required | name: originOverrideAction |
| headerName | required | name: headerValue |
| headerValue | required | name: replace |

## 📦 google_networkservices_service_lb_policies

🔗 **API Reference**: https://cloud.google.com/service-mesh/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required | name: location |
| location | required |  |
| failoverHealthThreshold | required | name: isolationConfig |

## 📦 google_networkservices_multicast_group_consumer_activation

🔗 **API Reference**: https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupConsumerActivations

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: multicastGroupConsumerActivationId |
| None | required |  |
| None | required | name: multicastGroupRangeActivation |
| None | required | name: name |

## 📦 google_networkservices_grpc_route

🔗 **API Reference**: https://cloud.google.com/traffic-director/docs/reference/network-services/rest/v1beta1/projects.locations.grpcRoutes

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| hostnames | required |  |
| rules | required |  |
| key | required | name: value |
| value | required | name: type |
| grpcService | required | name: grpcMethod |
| grpcMethod | required | name: caseSensitive |

## 📦 google_networkservices_gateway

🔗 **API Reference**: https://cloud.google.com/traffic-director/docs/reference/network-services/rest/v1/projects.locations.gateways

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required | name: location |
| type | required |  |
| ports | required |  |

## 📦 google_networkservices_multicast_producer_association

🔗 **API Reference**: https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastProducerAssociations

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: multicastProducerAssociationId |
| None | required |  |
| None | required | name: name |
| None | required | name: state |

## 📦 google_networkservices_multicast_domain

🔗 **API Reference**: https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomains

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: multicastDomainId |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_networkservices_multicast_group_range_activation

🔗 **API Reference**: https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRangeActivations

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: multicastGroupRangeActivationId |
| None | required |  |
| None | required | name: multicastGroupConsumerActivations |
| None | required | name: name |

## 📦 google_networkservices_multicast_consumer_association

🔗 **API Reference**: https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastConsumerAssociations

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: multicastConsumerAssociationId |
| None | required |  |
| None | required | name: name |
| None | required | name: placementPolicy |

## 📦 google_networkservices_endpoint_policy

🔗 **API Reference**: https://cloud.google.com/traffic-director/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| type | required |  |
| ports | required |  |
| endpointMatcher | required |  |
| metadataLabelMatcher | required |  |
| metadataLabelMatchCriteria | required |  |
| labelName | required | name: labelValue |
| labelValue | required |  |

## 📦 google_networkservices_edge_cache_keyset

🔗 **API Reference**: https://cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheKeysets

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| public_key | at_least_one_of | public_key, validation_shared_keys |
| id | required | name: value |
| validationSharedKeys | at_least_one_of | public_key, validation_shared_keys |
| secretVersion | required |  |

## 📦 google_networkservices_authz_extension

🔗 **API Reference**: https://cloud.google.com/service-extensions/docs/reference/rest/v1beta1/projects.locations.authzExtensions

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| location | required |  |
| service | required |  |
| timeout | required |  |

## 📦 google_networkservices_multicast_domain_group

🔗 **API Reference**: https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomainGroups

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: multicastDomainGroupId |
| None | required |  |

## 📦 google_networkservices_tcp_route

🔗 **API Reference**: https://cloud.google.com/traffic-director/docs/reference/network-services/rest/v1beta1/projects.locations.tcpRoutes

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| rules | required |  |
| address | required | name: port |
| port | required | name: action |
| action | required |  |

## 📦 google_networkservices_agent_gateway

🔗 **API Reference**: https://cloud.google.com/network-services/docs/reference/network-services/rest/v1beta1/projects.locations.agentGateways

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required | name: location |
| location | required |  |
| protocols | required | name: googleManaged |
| googleManaged | exactly_one_of | google_managed, self_managed |
| governedAccessPath | required |  |
| selfManaged | exactly_one_of | google_managed, self_managed |
| resourceUri | required |  |
| egress | required |  |
| networkAttachment | required |  |

## 📦 google_networkservices_wasm_plugin

🔗 **API Reference**: https://cloud.google.com/service-extensions/docs/reference/rest/v1/projects.locations.wasmPlugins

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| mainVersionId | required | name: logConfig |
| versions | required |  |
| pluginConfigData | conflicts | pluginConfigUri |
| pluginConfigUri | conflicts | pluginConfigData, name: usedBy |

## 📦 google_networkservices_multicast_group_producer_activation

🔗 **API Reference**: https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupProducerActivations

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: multicastGroupProducerActivationId |
| None | required |  |
| None | required | name: multicastProducerAssociation |
| None | required | name: name |

## 📦 google_networkservices_multicast_group_range

🔗 **API Reference**: https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRanges

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: multicastGroupRangeId |
| None | required |  |
| None | required | name: name |
| None | required | name: state |

## 📦 google_netapp_backup

🔗 **API Reference**: https://cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.backupVaults.backups

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| vault_name | required |  |
| name | required |  |
| description | required | name: volumeUsageBytes |
| labels | required | name: chainStorageBytes |
| sourceSnapshot | required |  |

## 📦 google_netapp_volume_quota_rule

🔗 **API Reference**: https://cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.quotaRules

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| volume_name | required |  |
| name | required |  |
| type | required |  |
| diskLimitMib | required | name: state |

## 📦 google_netapp_host_group

🔗 **API Reference**: https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.hostGroups

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| description | required | name: labels |
| labels | required | name: type |
| type | required |  |
| hosts | required |  |
| osType | required |  |

## 📦 google_netapp_backup_vault

🔗 **API Reference**: https://cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.backupVaults

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| description | required | name: labels |
| labels | required | name: backupVaultType |
| backupMinimumEnforcedRetentionDays | required | name: dailyBackupImmutable |

## 📦 google_netapp_volume

🔗 **API Reference**: https://cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| storagePool | required | name: network |
| capacityGib | required | name: exportPolicy |
| rules | required |  |
| protocols | required |  |
| sourceSnapshot | exactly_one_of | restore_parameters.0.source_backup, restore_parameters.0.source_snapshot, name: sourceBackup |
| sourceBackup | exactly_one_of | restore_parameters.0.source_backup, restore_parameters.0.source_snapshot, name: kmsConfig |
| snapshotsToKeep | required | name: minute |
| snapshotsToKeep | required | name: minute |
| snapshotsToKeep | required | name: minute |
| snapshotsToKeep | required | name: minute |
| osType | required |  |

## 📦 google_netapp_volume_snapshot

🔗 **API Reference**: https://cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.snapshots

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| volume_name | required |  |
| name | required |  |

## 📦 google_netapp_active_directory

🔗 **API Reference**: https://cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.activeDirectories

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| domain | required | name: site |
| site | required | name: dns |
| dns | required | name: netBiosPrefix |
| netBiosPrefix | required | name: organizationalUnit |
| organizationalUnit | required |  |
| aesEncryption | required |  |
| username | required |  |
| password | required |  |
| backupOperators | required |  |
| administrators | required |  |
| securityOperators | required |  |
| kdcHostname | required | name: kdcIp |
| kdcIp | required | name: nfsUsersWithLdap |
| nfsUsersWithLdap | required | name: description |
| description | required | name: ldapSigning |
| ldapSigning | required | name: encryptDcConnections |
| encryptDcConnections | required | name: labels |
| labels | required | name: stateDetails |

## 📦 google_netapp_kmsconfig

🔗 **API Reference**: https://cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.kmsConfigs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| cryptoKeyName | required | name: instructions |

## 📦 google_netapp_backup_policy

🔗 **API Reference**: https://cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.backupPolicies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| dailyBackupLimit | required | name: weeklyBackupLimit |
| weeklyBackupLimit | required | name: monthlyBackupLimit |
| monthlyBackupLimit | required | name: description |

## 📦 google_netapp_storage_pool

🔗 **API Reference**: https://cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.storagePools

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| serviceLevel | required |  |
| capacityGib | required | name: volumeCapacityGib |
| network | required |  |

## 📦 google_netapp_volume_replication

🔗 **API Reference**: https://cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.replications

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| volumeName | required |  |
| name | required |  |
| replicationSchedule | required |  |
| storagePool | required |  |

## 📦 google_discoveryengine_data_store

🔗 **API Reference**: https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| dataStoreId | required |  |
| displayName | required | name: industryVertical |
| industryVertical | required |  |
| contentConfig | required |  |
| disableInitialIndex | required | name: disableAutomaticRefresh |
| disableAutomaticRefresh | required | name: kmsKeyName |
| kmsKeyName | required |  |
| documentProcessingConfig | required |  |
| name | required |  |
| chunkingConfig | required |  |
| layoutBasedChunkingConfig | required |  |
| chunkSize | required | name: includeAncestorHeadings |
| includeAncestorHeadings | required | name: defaultParsingConfig |
| defaultParsingConfig | required |  |
| digitalParsingConfig | required |  |
| digitalParsingConfig | exactly_one_of | default_parsing_config.0.digital_parsing_config, default_parsing_config.0.ocr_parsing_config, default_parsing_config.0.layout_parsing_config |
| ocrParsingConfig | required |  |
| ocrParsingConfig | exactly_one_of | default_parsing_config.0.digital_parsing_config, default_parsing_config.0.ocr_parsing_config, default_parsing_config.0.layout_parsing_config |
| useNativeText | required | name: layoutParsingConfig |
| layoutParsingConfig | required |  |
| layoutParsingConfig | exactly_one_of | default_parsing_config.0.digital_parsing_config, default_parsing_config.0.ocr_parsing_config, default_parsing_config.0.layout_parsing_config |
| enableTableAnnotation | required | name: enableImageAnnotation |
| enableImageAnnotation | required | name: structuredContentTypes |
| structuredContentTypes | required |  |
| excludeHtmlElements | required |  |
| excludeHtmlClasses | required |  |
| excludeHtmlIds | required |  |
| digitalParsingConfig | required |  |
| digitalParsingConfig | exactly_one_of | default_parsing_config.0.digital_parsing_config, default_parsing_config.0.ocr_parsing_config, default_parsing_config.0.layout_parsing_config |
| ocrParsingConfig | required |  |
| ocrParsingConfig | exactly_one_of | default_parsing_config.0.digital_parsing_config, default_parsing_config.0.ocr_parsing_config, default_parsing_config.0.layout_parsing_config |
| useNativeText | required | name: layoutParsingConfig |
| layoutParsingConfig | required |  |
| layoutParsingConfig | exactly_one_of | default_parsing_config.0.digital_parsing_config, default_parsing_config.0.ocr_parsing_config, default_parsing_config.0.layout_parsing_config |
| enableTableAnnotation | required | name: enableImageAnnotation |
| enableImageAnnotation | required | name: structuredContentTypes |
| structuredContentTypes | required |  |
| excludeHtmlElements | required |  |
| excludeHtmlClasses | required |  |
| excludeHtmlIds | required |  |

## 📦 google_discoveryengine_serving_config

🔗 **API Reference**: https://cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| engineId | required |  |

## 📦 google_discoveryengine_assistant

🔗 **API Reference**: https://cloud.google.com/generative-ai-app-builder/docs/reference/rpc/google.cloud.discoveryengine.v1#assistantservice

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| collectionId | required |  |
| engineId | required |  |
| assistantId | required |  |
| displayName | required |  |
| phrase | required |  |
| userPromptTemplate | required |  |
| responseTemplate | required |  |

## 📦 google_discoveryengine_chat_engine

🔗 **API Reference**: https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| engineId | required |  |
| collection_id | required |  |
| location | required |  |
| displayName | required | name: dataStoreIds |
| dataStoreIds | required |  |
| chatEngineConfig | required |  |
| agentCreationConfig | exactly_one_of | chat_engine_config.0.agent_creation_config, chat_engine_config.0.dialogflow_agent_to_link |
| defaultLanguageCode | required | name: timeZone |
| timeZone | required | name: location |
| dialogflowAgentToLink | exactly_one_of | chat_engine_config.0.agent_creation_config, chat_engine_config.0.dialogflow_agent_to_link, name: allowCrossRegion |

## 📦 google_discoveryengine_data_connector

🔗 **API Reference**: https://cloud.google.com/generative-ai-app-builder/docs/reference/rpc/google.cloud.discoveryengine.v1alpha#dataconnectorservice

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| collectionId | required |  |
| collectionDisplayName | required |  |
| dataSource | required |  |
| params | exactly_one_of | params, json_params, name: jsonParams |
| jsonParams | exactly_one_of | params, json_params, name: refreshInterval |
| refreshInterval | required | name: entities |

## 📦 google_discoveryengine_user_store

🔗 **API Reference**: https://cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.userStores

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |

## 📦 google_discoveryengine_license_config

🔗 **API Reference**: https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.licenseConfigs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| licenseConfigId | required |  |
| licenseCount | required | name: subscriptionTier |
| subscriptionTier | required |  |
| startDate | required |  |
| subscriptionTerm | required |  |

## 📦 google_discoveryengine_acl_config

🔗 **API Reference**: https://cloud.google.com/generative-ai-app-builder/docs/reference/rpc/google.cloud.discoveryengine.v1alpha#aclconfigservice

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |

## 📦 google_discoveryengine_sitemap

🔗 **API Reference**: https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.siteSearchEngine.sitemaps

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| dataStoreId | required |  |

## 📦 google_discoveryengine_schema

🔗 **API Reference**: https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.schemas

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| dataStoreId | required |  |
| schemaId | required |  |
| jsonSchema | exactly_one_of | json_schema |

## 📦 google_discoveryengine_widget_config

🔗 **API Reference**: https://cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.widgetConfigs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| engineId | required |  |
| field | required | name: displayName |
| field | required | name: deviceVisibility |
| url | exactly_one_of | url, name: homepageSetting |
| url | exactly_one_of | url, name: destinationUri |

## 📦 google_discoveryengine_target_site

🔗 **API Reference**: https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.siteSearchEngine.targetSites

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| dataStoreId | required |  |
| providedUriPattern | required |  |

## 📦 google_discoveryengine_cmek_config

🔗 **API Reference**: https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.cmekConfigs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| cmekConfigId | required |  |
| kmsKey | required |  |
| kmsKey | required | name: notebooklmState |

## 📦 google_discoveryengine_recommendation_engine

🔗 **API Reference**: https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| engineId | required |  |
| location | required |  |
| displayName | required | name: createTime |
| dataStoreIds | required |  |
| engineFeaturesConfig | exactly_one_of | recommended_for_you_config, most_popular_config |

## 📦 google_discoveryengine_search_engine

🔗 **API Reference**: https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| engineId | required |  |
| collectionId | required |  |
| location | required |  |
| displayName | required | name: dataStoreIds |
| dataStoreIds | required |  |
| searchEngineConfig | required |  |
| requiredSubscriptionTier | required |  |

## 📦 google_discoveryengine_control

🔗 **API Reference**: https://cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.controls

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| engineId | required |  |
| controlId | required |  |
| displayName | required | name: solutionType |
| solutionType | required |  |
| boostAction | exactly_one_of | boost_action, filter_action, redirect_action, synonyms_action |
| filter | required | name: dataStore |
| dataStore | required | name: fixedBoost |
| fixedBoost | exactly_one_of | boost_action.0.fixed_boost, boost_action.0.interpolation_boost_spec, name: interpolationBoostSpec |
| interpolationBoostSpec | exactly_one_of | boost_action.0.fixed_boost, boost_action.0.interpolation_boost_spec |
| filterAction | exactly_one_of | boost_action, filter_action, redirect_action, synonyms_action |
| filter | required | name: dataStore |
| dataStore | required | name: redirectAction |
| redirectAction | exactly_one_of | boost_action, filter_action, redirect_action, synonyms_action |
| redirectUri | required | name: synonymsAction |
| synonymsAction | exactly_one_of | boost_action, filter_action, redirect_action, synonyms_action |
| promoteAction | exactly_one_of | boost_action, filter_action, redirect_action, synonyms_action |
| dataStore | required | name: searchLinkPromotion |
| searchLinkPromotion | required |  |
| title | required | name: uri |

## 📦 google_gkeonprem_bare_metal_cluster

🔗 **API Reference**: https://cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| location | required |  |
| adminClusterMembership | required |  |
| bareMetalVersion | required | name: annotations |
| networkConfig | required |  |
| islandModeCidr | exactly_one_of | network_config.0.island_mode_cidr |
| serviceAddressCidrBlocks | required |  |
| podAddressCidrBlocks | required |  |
| controlPlane | required |  |
| controlPlaneNodePoolConfig | required |  |
| nodePoolConfig | required |  |
| argument | required | name: value |
| value | required | name: loadBalancer |
| loadBalancer | required |  |
| vipConfig | required |  |
| controlPlaneVip | required | name: ingressVip |
| ingressVip | required | name: portConfig |
| portConfig | required |  |
| controlPlaneLoadBalancerPort | required | name: metalLbConfig |
| metalLbConfig | exactly_one_of | load_balancer.0.metal_lb_config, load_balancer.0.manual_lb_config, load_balancer.0.bgp_lb_config |
| addressPools | required |  |
| pool | required | name: addresses |
| addresses | required |  |
| manualLbConfig | exactly_one_of | load_balancer.0.metal_lb_config, load_balancer.0.manual_lb_config, load_balancer.0.bgp_lb_config |
| enabled | required | name: bgpLbConfig |
| bgpLbConfig | exactly_one_of | load_balancer.0.metal_lb_config, load_balancer.0.manual_lb_config, load_balancer.0.bgp_lb_config |
| asn | required | name: bgpPeerConfigs |
| bgpPeerConfigs | required |  |
| asn | required | name: ipAddress |
| ipAddress | required | name: controlPlaneNodes |
| addressPools | required |  |
| pool | required | name: addresses |
| addresses | required |  |
| storage | required |  |
| lvpShareConfig | required |  |
| lvpConfig | required |  |
| path | required | name: storageClass |
| storageClass | required | name: sharedPathPvCount |
| lvpNodeMountsConfig | required |  |
| path | required | name: storageClass |
| storageClass | required | name: proxy |
| uri | required | name: noProxy |
| maintenanceAddressCidrBlocks | required |  |
| loginUser | required |  |
| packageRepoExcluded | required | name: securityConfig |
| adminUsers | required |  |
| username | required | name: binaryAuthorization |

## 📦 google_gkeonprem_vmware_node_pool

🔗 **API Reference**: https://cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters.vmwareNodePools

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| vmwareCluster | required |  |
| location | required |  |
| minReplicas | required | name: maxReplicas |
| maxReplicas | required | name: config |
| config | required |  |
| imageType | required | name: image |
| key | required | name: value |
| value | required | name: effect |

## 📦 google_gkeonprem_vmware_admin_cluster

🔗 **API Reference**: https://cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| gkeonprem_vmware_admin_cluster_metallb | required | type: String |
| gkeonprem_vmware_admin_cluster_metallb | required |  |
| gkeonprem_vmware_admin_cluster_metallb | required |  |
| gkeonprem_vmware_admin_cluster_metallb | required |  |
| gkeonprem_vmware_admin_cluster_metallb | required |  |
| gkeonprem_vmware_admin_cluster_metallb | exactly_one_of | network_config.0.static_ip_config, network_config.0.dhcp_ip_config |
| gkeonprem_vmware_admin_cluster_metallb | required | type: String |
| gkeonprem_vmware_admin_cluster_metallb | required | type: Array |
| gkeonprem_vmware_admin_cluster_metallb | required |  |
| gkeonprem_vmware_admin_cluster_metallb | required | type: String |
| gkeonprem_vmware_admin_cluster_metallb | exactly_one_of | network_config.0.static_ip_config, network_config.0.dhcp_ip_config |
| gkeonprem_vmware_admin_cluster_metallb | required | type: String |
| gkeonprem_vmware_admin_cluster_metallb | required | type: String |
| gkeonprem_vmware_admin_cluster_metallb | required | type: Array |
| gkeonprem_vmware_admin_cluster_metallb | required |  |
| gkeonprem_vmware_admin_cluster_metallb | required | type: String |
| gkeonprem_vmware_admin_cluster_metallb | required | type: NestedObject |
| gkeonprem_vmware_admin_cluster_metallb | required |  |
| gkeonprem_vmware_admin_cluster_metallb | required |  |
| gkeonprem_vmware_admin_cluster_metallb | exactly_one_of | loadBalancer.0.f5_config, loadBalancer.0.manual_lb_config, loadBalancer.0.metal_lb_config |
| gkeonprem_vmware_admin_cluster_metallb | exactly_one_of | loadBalancer.0.f5_config, loadBalancer.0.manual_lb_config, loadBalancer.0.metal_lb_config |
| gkeonprem_vmware_admin_cluster_metallb | exactly_one_of | loadBalancer.0.f5_config, loadBalancer.0.manual_lb_config, loadBalancer.0.metal_lb_config |
| gkeonprem_vmware_admin_cluster_metallb | required | type: NestedObject |
| gkeonprem_vmware_admin_cluster_metallb | required | type: NestedObject |
| gkeonprem_vmware_admin_cluster_metallb | required |  |
| state | required |  |

## 📦 google_gkeonprem_vmware_cluster

🔗 **API Reference**: https://cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | exactly_one_of | network_config.0.static_ip_config, network_config.0.dhcp_ip_config |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | exactly_one_of | network_config.0.static_ip_config, network_config.0.dhcp_ip_config |
| None | required |  |
| None | exactly_one_of | loadBalancer.0.f5_config, loadBalancer.0.manual_lb_config, loadBalancer.0.metal_lb_config |
| None | exactly_one_of | loadBalancer.0.f5_config, loadBalancer.0.manual_lb_config, loadBalancer.0.metal_lb_config |
| None | exactly_one_of | loadBalancer.0.f5_config, loadBalancer.0.manual_lb_config, loadBalancer.0.metal_lb_config |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_gkeonprem_bare_metal_admin_cluster

🔗 **API Reference**: https://cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| location | required |  |
| islandModeCidr | exactly_one_of | network_config.0.island_mode_cidr |
| serviceAddressCidrBlocks | required |  |
| podAddressCidrBlocks | required |  |
| controlPlaneNodePoolConfig | required |  |
| nodePoolConfig | required |  |
| argument | required | name: value |
| value | required | name: loadBalancer |
| vipConfig | required |  |
| controlPlaneVip | required | name: portConfig |
| portConfig | required |  |
| controlPlaneLoadBalancerPort | required | name: manualLbConfig |
| enabled | required | name: bgpLbConfig |
| lvpShareConfig | required |  |
| lvpConfig | required |  |
| path | required | name: storageClass |
| storageClass | required | name: sharedPathPvCount |
| lvpNodeMountsConfig | required |  |
| path | required | name: storageClass |
| storageClass | required | name: proxy |
| uri | required | name: noProxy |
| maintenanceAddressCidrBlocks | required |  |
| loginUser | required | name: securityConfig |
| adminUsers | required |  |
| username | required |  |

## 📦 google_gkeonprem_bare_metal_node_pool

🔗 **API Reference**: https://cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters.bareMetalNodePools

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| bareMetalCluster | required |  |
| location | required |  |
| nodePoolConfig | required |  |
| nodeConfigs | required |  |

## 📦 google_servicemanagement_service_consumers

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| serviceName | required | name: consumerProject |
| consumerProject | required |  |

## 📦 google_servicemanagement_service

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| serviceName | required |  |

## 📦 google_securitycenterv2_organization_mute_config

🔗 **API Reference**: https://cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.muteConfigs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| organization | required |  |
| mute_config_id | required |  |
| filter | required | name: createTime |
| type | required |  |

## 📦 google_securitycenterv2_project_scc_big_query_export

🔗 **API Reference**: https://cloud.google.com/security-command-center/docs/reference/rest/v2/projects.locations.bigQueryExports

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| bigQueryExportId | required |  |

## 📦 google_securitycenterv2_organization_scc_big_query_exports

🔗 **API Reference**: https://cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.locations.bigQueryExports

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| organization | required |  |
| bigQueryExportId | required |  |

## 📦 google_securitycenterv2_organization_source

🔗 **API Reference**: https://cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.sources

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| organization | required |  |
| displayName | required |  |

## 📦 google_securitycenterv2_organization_notification_config

🔗 **API Reference**: https://cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.locations.notificationConfigs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| organization | required |  |
| configId | required |  |
| pubsubTopic | required | name: serviceAccount |
| streamingConfig | required |  |
| filter | required |  |

## 📦 google_securitycenterv2_project_notification_config

🔗 **API Reference**: https://cloud.google.com/security-command-center/docs/reference/rest/v2/projects.locations.notificationConfigs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| configId | required |  |
| location | required |  |
| streamingConfig | required |  |
| filter | required |  |

## 📦 google_securitycenterv2_folder_notification_config

🔗 **API Reference**: https://cloud.google.com/security-command-center/docs/reference/rest/v2/folders.locations.notificationConfigs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| folder | required |  |
| location | required |  |
| configId | required |  |
| pubsubTopic | required | name: serviceAccount |
| streamingConfig | required |  |
| filter | required |  |

## 📦 google_securitycenterv2_organization_scc_big_query_export

🔗 **API Reference**: https://cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.locations.bigQueryExports

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| organization | required |  |
| bigQueryExportId | required |  |

## 📦 google_securitycenterv2_folder_mute_config

🔗 **API Reference**: https://cloud.google.com/security-command-center/docs/reference/rest/v2/folders.muteConfigs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| folder | required |  |
| mute_config_id | required |  |
| filter | required | name: createTime |
| type | required |  |

## 📦 google_securitycenterv2_project_mute_config

🔗 **API Reference**: https://cloud.google.com/security-command-center/docs/reference/rest/v2/projects.muteConfigs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| mute_config_id | required |  |
| filter | required | name: createTime |
| type | required |  |

## 📦 google_securitycenterv2_folder_scc_big_query_export

🔗 **API Reference**: https://cloud.google.com/security-command-center/docs/reference/rest/v2/folders.locations.bigQueryExports

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| folder | required |  |
| bigQueryExportId | required |  |

## 📦 google_vpcaccess_connector

🔗 **API Reference**: https://cloud.google.com/vpc/docs/reference/vpcaccess/rest/v1/projects.locations.connectors

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| network | exactly_one_of | network, subnet.0.name |
| minThroughput | conflicts | min_instances |
| minInstances | conflicts | min_throughput, name: maxInstances |
| maxInstances | conflicts | max_throughput, name: maxThroughput |
| maxThroughput | conflicts | max_instances |
| name | exactly_one_of | network, subnet.0.name, name: projectId |

## 📦 google_looker_instance

🔗 **API Reference**: https://cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| startDate | required |  |
| endDate | required |  |
| time | required |  |
| dayOfWeek | required |  |
| startTime | required |  |
| name | required |  |
| oauthConfig | required |  |
| clientId | required | name: clientSecret |
| clientSecret | required |  |
| kmsKey | required | name: gcsUri |
| gcsUri | required | name: startTime |
| startTime | required |  |

## 📦 google_bigqueryanalyticshub_data_exchange

🔗 **API Reference**: https://cloud.google.com/bigquery/docs/reference/analytics-hub/rest/v1/projects.locations.dataExchanges

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| data_exchange_id | required |  |
| location | required |  |
| displayName | required | name: description |
| defaultExchangeConfig | exactly_one_of | sharing_environment_config.0.default_exchange_config, sharing_environment_config.0.dcr_exchange_config |
| dcrExchangeConfig | exactly_one_of | sharing_environment_config.0.default_exchange_config, sharing_environment_config.0.dcr_exchange_config |

## 📦 google_bigqueryanalyticshub_data_exchange_subscription

🔗 **API Reference**: https://cloud.google.com/bigquery/docs/reference/analytics-hub/rest/v1/projects.locations.subscriptions

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| dataExchangeId | required | name: dataExchangeProject |
| dataExchangeProject | required |  |
| dataExchangeLocation | required | name: location |
| location | required |  |
| subscriptionId | required |  |
| location | required |  |
| datasetReference | required |  |
| datasetId | required | name: projectId |
| projectId | required |  |
| linkedDataset | exactly_one_of | linkedDataset, linkedPubsubSubscription, name: linkedPubsubSubscription |
| linkedPubsubSubscription | exactly_one_of | linkedDataset, linkedPubsubSubscription, name: linkedResources |

## 📦 google_bigqueryanalyticshub_listing_subscription

🔗 **API Reference**: https://cloud.google.com/bigquery/docs/reference/analytics-hub/rest/v1/projects.locations.subscriptions

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| dataExchangeId | required | name: listingId |
| listingId | required | name: location |
| location | required |  |
| destinationDataset | required |  |
| location | required |  |
| datasetReference | required |  |
| datasetId | required | name: projectId |
| projectId | required | name: friendlyName |

## 📦 google_bigqueryanalyticshub_listing

🔗 **API Reference**: https://cloud.google.com/bigquery/docs/reference/analytics-hub/rest/v1/projects.locations.dataExchanges.listings

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| data_exchange_id | required |  |
| listing_id | required |  |
| location | required |  |
| displayName | required | name: description |
| name | required | name: primaryContact |
| name | required | name: primaryContact |
| bigqueryDataset | exactly_one_of | pubsubTopic, bigqueryDataset |
| dataset | required |  |
| table | exactly_one_of | table, routine, name: routine |
| routine | exactly_one_of | table, routine, name: replicaLocations |
| pubsubTopic | exactly_one_of | pubsubTopic, bigqueryDataset |
| topic | required |  |

## 📦 google_bigtable_materialized_view

🔗 **API Reference**: https://cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.materializedViews

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| materializedViewId | required |  |
| query | required |  |

## 📦 google_bigtable_app_profile

🔗 **API Reference**: https://cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.appProfiles

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| appProfileId | required |  |
| multiClusterRoutingUseAny | exactly_one_of | single_cluster_routing, multi_cluster_routing_use_any |
| singleClusterRouting | exactly_one_of | single_cluster_routing, multi_cluster_routing_use_any |
| clusterId | required | name: allowTransactionalWrites |
| standardIsolation | conflicts | data_boost_isolation_read_only |
| priority | required |  |
| dataBoostIsolationReadOnly | conflicts | standard_isolation |
| computeBillingOwner | required |  |

## 📦 google_bigtable_schema_bundle

🔗 **API Reference**: https://cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.tables.schemaBundles

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| schemaBundleId | required |  |
| protoSchema | required |  |
| protoDescriptors | required |  |

## 📦 google_bigtable_logical_view

🔗 **API Reference**: https://cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.logicalViews

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| logicalViewId | required |  |
| query | required | name: deletionProtection |

## 📦 google_documentaiwarehouse_location

🔗 **API Reference**: https://cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| project_number | required | name: location |
| location | required |  |
| databaseType | required |  |
| accessControlMode | required |  |

## 📦 google_documentaiwarehouse_document_schema

🔗 **API Reference**: https://cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.documentSchemas

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| project_number | required |  |
| location | required |  |
| displayName | required | name: documentIsFolder |
| propertyDefinitions | required |  |
| name | required | name: displayName |
| propertyDefinitions | required |  |
| name | required | name: displayName |
| possibleValues | required |  |
| possibleValues | required |  |

## 📦 google_oslogin_ssh_public_key

🔗 **API Reference**: https://cloud.google.com/compute/docs/oslogin/rest/v1/users.sshPublicKeys

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| user | required |  |
| key | required |  |
| expirationTimeUsec | required | name: fingerprint |

## 📦 google_iam2_deny_policy

🔗 **API Reference**: https://cloud.google.com/iam/docs/reference/rest/v2/policies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| parent | required |  |
| rules | required |  |
| expression | required | name: title |

## 📦 google_iam2_access_boundary_policy

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| parent | required |  |
| rules | required |  |
| expression | required | name: title |

## 📦 google_gemini_data_sharing_with_google_setting_binding

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: settingBindingId |
| None | required |  |
| None | required |  |

## 📦 google_gemini_gemini_gcp_enablement_setting

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: geminiGcpEnablementSettingId |
| None | required |  |

## 📦 google_gemini_logging_setting

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: loggingSettingId |
| None | required |  |

## 📦 google_gemini_data_sharing_with_google_setting

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |

## 📦 google_gemini_release_channel_setting_binding

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: settingBindingId |
| None | required |  |
| None | required | name: product |

## 📦 google_gemini_code_repository_index

🔗 **API Reference**: https://cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.codeRepositoryIndexes

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| force_destroy | required | name: codeRepositoryIndexId |
| force_destroy | required |  |

## 📦 google_gemini_repository_group

🔗 **API Reference**: https://cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.codeRepositoryIndexes.repositoryGroups

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: codeRepositoryIndex |
| None | required | name: repositoryGroupId |
| None | required |  |
| None | required |  |
| None | required | name: branchPattern |
| None | required | name: name |

## 📦 google_gemini_logging_setting_binding

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: settingBindingId |
| None | required |  |
| None | required | name: product |

## 📦 google_gemini_gemini_gcp_enablement_setting_binding

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: settingBindingId |
| None | required |  |
| None | required | name: product |

## 📦 google_gemini_code_tools_setting

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required | name: tool |
| None | required | name: config |
| None | required | name: value |
| None | required | name: uriOverride |

## 📦 google_gemini_release_channel_setting

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: releaseChannelSettingId |
| None | required |  |

## 📦 google_gemini_code_tools_setting_binding

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: settingBindingId |
| None | required |  |
| None | required |  |

## 📦 google_gkehub_membership

🔗 **API Reference**: https://cloud.google.com/anthos/multicluster-management/reference/rest/v1/projects.locations.memberships

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| membershipId | required |  |
| resourceLink | required |  |
| issuer | required |  |

## 📦 google_cloudsecuritycompliance_framework

🔗 **API Reference**: https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/organizations.locations.frameworks

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: location |
| None | required | name: frameworkId |
| None | required |  |
| None | required | name: name |
| None | required | name: parameters |
| None | required | name: parameterValue |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_cloudsecuritycompliance_framework_deployment

🔗 **API Reference**: https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/organizations.locations.frameworkDeployments

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: location |
| None | required | name: frameworkDeploymentId |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required | name: name |
| None | required | name: parameters |
| None | required | name: parameterValue |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required | name: computedTargetResource |
| None | required |  |
| None | required | name: majorRevisionId |
| None | required | name: name |
| None | required |  |
| None | exactly_one_of | "target_resource_config.0.existing_target_resource", "target_resource_config.0.target_resource_creation_config", name: targetResourceCreationConfig |
| None | exactly_one_of | "target_resource_config.0.existing_target_resource", "target_resource_config.0.target_resource_creation_config" |
| None | exactly_one_of | "target_resource_config.0.target_resource_creation_config.0.folder_creation_config", "target_resource_config.0.target_resource_creation_config.0.project_creation_config" |
| None | required | name: parent |
| None | required | name: projectCreationConfig |
| None | exactly_one_of | "target_resource_config.0.target_resource_creation_config.0.folder_creation_config", "target_resource_config.0.target_resource_creation_config.0.project_creation_config" |
| None | required | name: parent |
| None | required | name: projectDisplayName |
| None | required | name: targetResourceDisplayName |

## 📦 google_cloudsecuritycompliance_cloud_control

🔗 **API Reference**: https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/organizations.locations.cloudControls

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: location |
| None | required | name: cloudControlId |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required | name: name |
| None | required | name: substitutionRules |
| None | required |  |
| None | required |  |
| None | required | name: name |
| None | required | name: substitutionRules |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required | name: min |
| None | required | name: regexpPattern |
| None | required | name: valueType |
| None | required | name: validation |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required | name: min |
| None | required | name: regexpPattern |
| None | required | name: valueType |
| None | required | name: relatedFrameworks |
| None | required | name: resourceTypesValues |
| None | required |  |
| None | required |  |

## 📦 google_securityposture_posture_deployment

🔗 **API Reference**: https://cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/organizations.locations.postureDeployments

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_securityposture_posture

🔗 **API Reference**: https://cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Posture

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parent | required |  |
| location | required |  |
| postureId | required |  |
| state | required |  |
| policySets | required |  |
| policySetId | required | name: description |
| policies | required |  |
| policyId | required | name: description |
| constraint | required |  |
| cannedConstraintId | required | name: policyRules |
| policyRules | required |  |
| expression | required | name: title |
| name | required |  |
| condition | required | name: actionType |
| actionType | required |  |
| methodTypes | required |  |
| resourceTypes | required |  |
| policyRules | required |  |
| expression | required | name: title |
| moduleName | required | name: moduleEnablementState |
| config | required |  |
| predicate | required |  |
| expression | required | name: title |
| name | required | name: valueExpression |
| expression | required | name: title |
| resourceSelector | required |  |
| resourceTypes | required |  |
| severity | required |  |

## 📦 google_networkconnectivityv1_service_connection_policy

🔗 **API Reference**: https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.serviceConnectionPolicies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| location | required |  |
| serviceClass | required |  |
| network | required |  |
| subnetworks | required |  |

## 📦 google_networkconnectivityv1_internal_range

🔗 **API Reference**: https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.internalRanges

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| network | required |  |
| usage | required |  |
| peering | required |  |
| source | required | name: target |
| target | required | name: immutable |

## 📦 google_networkmanagement_connectivity_test

🔗 **API Reference**: https://cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_networkmanagement_vpc_flow_logs_config

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |

## 📦 google_networkmanagement_organization_vpc_flow_logs_config

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| organization | required | name: location |
| location | required |  |
| vpcFlowLogsConfigId | required |  |

## 📦 google_securitycenter_folder_custom_module

🔗 **API Reference**: https://cloud.google.com/security-command-center/docs/reference/rest/v1/folders.securityHealthAnalyticsSettings.customModules

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| folder | required |  |
| displayName | required |  |
| enablementState | required |  |
| customConfig | required |  |
| predicate | required |  |
| expression | required | name: title |
| expression | required | name: title |
| resourceSelector | required |  |
| resourceTypes | required |  |
| severity | required |  |
| recommendation | required |  |

## 📦 google_securitycenter_source

🔗 **API Reference**: https://cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.sources

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| organization | required |  |
| displayName | required |  |

## 📦 google_securitycenter_project_scc_big_query_export

🔗 **API Reference**: https://cloud.google.com/security-command-center/docs/reference/rest/v1/projects.bigQueryExports

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| bigQueryExportId | required |  |

## 📦 google_securitycenter_notification_config

🔗 **API Reference**: https://cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.notificationConfigs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| organization | required |  |
| configId | required |  |
| pubsubTopic | required | name: serviceAccount |
| streamingConfig | required |  |
| filter | required |  |

## 📦 google_securitycenter_project_notification_config

🔗 **API Reference**: https://cloud.google.com/security-command-center/docs/reference/rest/v1/projects.notificationConfigs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| configId | required |  |
| pubsubTopic | required | name: serviceAccount |
| streamingConfig | required |  |
| filter | required |  |

## 📦 google_securitycenter_folder_notification_config

🔗 **API Reference**: https://cloud.google.com/security-command-center/docs/reference/rest/v1/folders.notificationConfigs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| folder | required |  |
| configId | required |  |
| pubsubTopic | required | name: serviceAccount |
| streamingConfig | required |  |
| filter | required |  |

## 📦 google_securitycenter_organization_scc_big_query_export

🔗 **API Reference**: https://cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.bigQueryExports

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| organization | required |  |
| bigQueryExportId | required |  |

## 📦 google_securitycenter_event_threat_detection_custom_module

🔗 **API Reference**: https://cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.eventThreatDetectionSettings.customModules

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| organization | required |  |
| config | required |  |
| enablementState | required |  |
| type | required |  |

## 📦 google_securitycenter_organization_custom_module

🔗 **API Reference**: https://cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.securityHealthAnalyticsSettings.customModules

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| organization | required |  |
| displayName | required |  |
| enablementState | required |  |
| customConfig | required |  |
| predicate | required |  |
| expression | required | name: title |
| expression | required | name: title |
| resourceSelector | required |  |
| resourceTypes | required |  |
| severity | required |  |
| recommendation | required |  |

## 📦 google_securitycenter_project_custom_module

🔗 **API Reference**: https://cloud.google.com/security-command-center/docs/reference/rest/v1/projects.securityHealthAnalyticsSettings.customModules

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| displayName | required |  |
| enablementState | required |  |
| customConfig | required |  |
| predicate | required |  |
| expression | required | name: title |
| expression | required | name: title |
| resourceSelector | required |  |
| resourceTypes | required |  |
| severity | required |  |
| recommendation | required |  |

## 📦 google_securitycenter_mute_config

🔗 **API Reference**: https://cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.muteConfigs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| muteConfigId | required |  |
| parent | required |  |
| filter | required | name: createTime |

## 📦 google_securitycenter_folder_scc_big_query_export

🔗 **API Reference**: https://cloud.google.com/security-command-center/docs/reference/rest/v1/folders.bigQueryExports

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| folder | required |  |
| bigQueryExportId | required |  |
| description | required |  |
| dataset | required | name: createTime |
| filter | required |  |

## 📦 google_apphub_service

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| applicationId | required |  |
| serviceId | required |  |
| type | required |  |
| type | required |  |
| email | required | name: operatorOwners |
| email | required | name: businessOwners |
| email | required | name: discoveredService |
| discoveredService | required |  |

## 📦 google_apphub_workload

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| applicationId | required |  |
| workloadId | required |  |
| discoveredWorkload | required |  |
| type | required |  |
| type | required |  |
| email | required | name: operatorOwners |
| email | required | name: businessOwners |
| email | required | name: createTime |

## 📦 google_apphub_service_project_attachment

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| serviceProjectAttachmentId | required |  |

## 📦 google_apphub_boundary

🔗 **API Reference**: https://docs.cloud.google.com/app-hub/docs/reference/rest/v1/Boundary

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |

## 📦 google_apphub_application

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| applicationId | required |  |
| type | required |  |
| type | required |  |
| email | required | name: operatorOwners |
| email | required | name: businessOwners |
| email | required | name: createTime |
| scope | required |  |
| type | required |  |

## 📦 google_dialogflow_fulfillment

🔗 **API Reference**: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent/getFulfillment

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| displayName | required | name: enabled |
| type | required |  |
| uri | required | name: username |

## 📦 google_dialogflow_intent

🔗 **API Reference**: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| displayName | required | name: webhookState |

## 📦 google_dialogflow_generator

🔗 **API Reference**: https://cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.generators

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| generatorId | required |  |
| generatorId | required |  |
| generatorId | required |  |
| generatorId | required |  |
| generatorId | required |  |

## 📦 google_dialogflow_agent

🔗 **API Reference**: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| displayName | required | name: defaultLanguageCode |
| defaultLanguageCode | required |  |
| timeZone | required | name: description |

## 📦 google_dialogflow_encryption_spec

🔗 **API Reference**: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.encryptionSpec

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| encryptionSpec | required |  |
| kmsKey | required |  |

## 📦 google_dialogflow_entity_type

🔗 **API Reference**: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.entityTypes

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| displayName | required | name: kind |
| kind | required |  |
| value | required | name: synonyms |
| synonyms | required |  |

## 📦 google_dialogflow_environment

🔗 **API Reference**: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: location |
| None | required |  |
| None | required | name: username |

## 📦 google_dialogflow_conversation_profile

🔗 **API Reference**: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| displayName | required | type: Boolean |
| displayName | required | type: String |
| displayName | required |  |
| displayName | required |  |
| displayName | required |  |
| displayName | required |  |
| displayName | required |  |

## 📦 google_storageinsights_dataset_config

🔗 **API Reference**: https://cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| datasetConfigId | required |  |
| retentionPeriodDays | required | name: activityDataRetentionPeriodDays |
| identity | required |  |
| type | required |  |
| projectNumbers | exactly_one_of | source_projects, source_folders, organization_scope, name: sourceFolders |
| folderNumbers | exactly_one_of | source_projects, source_folders, organization_scope, name: organizationScope |
| organizationScope | exactly_one_of | source_projects, source_folders, organization_scope, name: includeCloudStorageLocations |
| includeCloudStorageLocations | required |  |
| includeCloudStorageLocations | conflicts | exclude_cloud_storage_locations, name: excludeCloudStorageLocations |
| excludeCloudStorageLocations | required |  |
| excludeCloudStorageLocations | conflicts | include_cloud_storage_locations, name: includeCloudStorageBuckets |
| includeCloudStorageBuckets | required |  |
| includeCloudStorageBuckets | conflicts | exclude_cloud_storage_buckets, name: excludeCloudStorageBuckets |
| excludeCloudStorageBuckets | required |  |
| excludeCloudStorageBuckets | conflicts | include_cloud_storage_buckets |

## 📦 google_storageinsights_report_config

🔗 **API Reference**: https://cloud.google.com/storage/docs/json_api/v1/reportConfig

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| frequency | required |  |
| startDate | required |  |
| day | required | name: month |
| month | required | name: year |
| year | required | name: endDate |
| endDate | required |  |
| day | required | name: month |
| month | required | name: year |
| year | required | name: parquetOptions |
| parquetOptions | exactly_one_of | parquet_options, csv_options |
| csvOptions | exactly_one_of | parquet_options, csv_options |
| metadataFields | required |  |
| storageDestinationOptions | required |  |
| bucket | required | name: destinationPath |

## 📦 google_documentai_processor_default_version

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| processor | required |  |
| version | required |  |

## 📦 google_documentai_processor

🔗 **API Reference**: https://cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| type | required |  |
| displayName | required |  |

## 📦 google_artifactregistry_vpcsc_config

🔗 **API Reference**: https://cloud.google.com/artifact-registry/docs/reference/rest/v1/VPCSCConfig

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |

## 📦 google_artifactregistry_repository

🔗 **API Reference**: https://cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| repository_id | required |  |
| location | required |  |
| format | required |  |
| virtualRepositoryConfig | conflicts | remote_repository_config |
| condition | exactly_one_of |  |
| mostRecentVersions | exactly_one_of |  |
| remoteRepositoryConfig | conflicts | virtual_repository_config |
| aptRepository | exactly_one_of | remoteRepositoryConfig.0.apt_repository, remoteRepositoryConfig.0.docker_repository, remoteRepositoryConfig.0.maven_repository, remoteRepositoryConfig.0.npm_repository |
| repositoryBase | required |  |
| repositoryPath | required |  |
| dockerRepository | exactly_one_of | remoteRepositoryConfig.0.apt_repository, remoteRepositoryConfig.0.docker_repository, remoteRepositoryConfig.0.maven_repository, remoteRepositoryConfig.0.npm_repository |
| publicRepository | conflicts | remoteRepositoryConfig.0.docker_repository.0.custom_repository |
| customRepository | conflicts | remoteRepositoryConfig.0.docker_repository.0.public_repository |
| mavenRepository | exactly_one_of | remoteRepositoryConfig.0.apt_repository, remoteRepositoryConfig.0.docker_repository, remoteRepositoryConfig.0.maven_repository, remoteRepositoryConfig.0.npm_repository |
| publicRepository | conflicts | remoteRepositoryConfig.0.maven_repository.0.custom_repository |
| customRepository | conflicts | remoteRepositoryConfig.0.maven_repository.0.public_repository |
| npmRepository | exactly_one_of | remoteRepositoryConfig.0.apt_repository, remoteRepositoryConfig.0.docker_repository, remoteRepositoryConfig.0.maven_repository, remoteRepositoryConfig.0.npm_repository |
| publicRepository | conflicts | remoteRepositoryConfig.0.npm_repository.0.custom_repository |
| customRepository | conflicts | remoteRepositoryConfig.0.npm_repository.0.public_repository |
| pythonRepository | exactly_one_of | remoteRepositoryConfig.0.apt_repository, remoteRepositoryConfig.0.docker_repository, remoteRepositoryConfig.0.maven_repository, remoteRepositoryConfig.0.npm_repository |
| publicRepository | conflicts | remoteRepositoryConfig.0.python_repository.0.custom_repository |
| customRepository | conflicts | remoteRepositoryConfig.0.python_repository.0.public_repository |
| yumRepository | exactly_one_of | remoteRepositoryConfig.0.apt_repository, remoteRepositoryConfig.0.docker_repository, remoteRepositoryConfig.0.maven_repository, remoteRepositoryConfig.0.npm_repository |
| repositoryBase | required |  |
| repositoryPath | required |  |
| commonRepository | exactly_one_of | remoteRepositoryConfig.0.apt_repository, remoteRepositoryConfig.0.docker_repository, remoteRepositoryConfig.0.maven_repository, remoteRepositoryConfig.0.npm_repository |
| uri | required | name: upstreamCredentials |

## 📦 google_iam3_folders_policy_binding

🔗 **API Reference**: https://cloud.google.com/iam/docs/reference/rest/v3/folders.locations.policyBindings

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| folder | required |  |
| location | required |  |
| policyBindingId | required |  |
| target | required |  |
| policy | required |  |

## 📦 google_iam3_projects_policy_binding

🔗 **API Reference**: https://cloud.google.com/iam/docs/reference/rest/v3/projects.locations.policyBindings

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| policyBindingId | required |  |
| target | required |  |
| policy | required |  |

## 📦 google_iam3_organizations_policy_binding

🔗 **API Reference**: https://cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.policyBindings

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| organization | required |  |
| location | required |  |
| policyBindingId | required |  |
| target | required |  |
| policy | required |  |

## 📦 google_iam3_principal_access_boundary_policy

🔗 **API Reference**: https://cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.principalAccessBoundaryPolicies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| organization | required |  |
| location | required |  |
| principalAccessBoundaryPolicyId | required |  |
| rules | required |  |
| resources | required |  |
| effect | required | name: enforcementVersion |

## 📦 google_firestore_user_creds

🔗 **API Reference**: https://cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.userCreds

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| database | required |  |
| name | required |  |

## 📦 google_firestore_field

🔗 **API Reference**: https://cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.collectionGroups.fields

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| collection | required |  |
| field | required |  |
| order | exactly_one_of | order, arrayConfig |
| arrayConfig | exactly_one_of | order, arrayConfig |

## 📦 google_firestore_database

🔗 **API Reference**: https://cloud.google.com/firestore/docs/reference/rest/v1/projects.databases

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| locationId | required |  |
| type | required |  |
| databaseEdition | required |  |
| kmsKeyName | required |  |

## 📦 google_firestore_backup_schedule

🔗 **API Reference**: https://cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.backupSchedules

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| retention | required | name: dailyRecurrence |
| dailyRecurrence | exactly_one_of | daily_recurrence, weekly_recurrence |
| weeklyRecurrence | exactly_one_of | weekly_recurrence, daily_recurrence |

## 📦 google_firestore_document

🔗 **API Reference**: https://cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.documents

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| collection | required |  |
| documentId | required |  |
| fields | required |  |

## 📦 google_firestore_index

🔗 **API Reference**: https://cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.collectionGroups.indexes

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| collection | required |  |
| fields | required |  |

## 📦 google_redis_cluster_user_created_connections

🔗 **API Reference**: https://cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_redis_instance

🔗 **API Reference**: https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| name | required |  |
| persistenceMode | required |  |
| rdbSnapshotPeriod | required |  |
| day | required |  |
| startTime | required |  |
| maintenanceVersion | required |  |
| memorySizeGb | required | name: port |

## 📦 google_redis_cluster

🔗 **API Reference**: https://cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| region | required |  |
| gcsSource | conflicts | managedBackupSource |
| uris | required |  |
| managedBackupSource | conflicts | gcsSource |
| backup | required |  |
| fixedFrequencySchedule | required |  |
| startTime | required |  |
| hours | required | name: retention |
| retention | required | name: authorizationMode |
| authorizationMode | required |  |
| transitEncryptionMode | required |  |
| nodeType | required |  |
| network | required | name: discoveryEndpoints |
| replicaCount | required |  |
| shardCount | required | name: deletionProtectionEnabled |
| deletionProtectionEnabled | required |  |
| day | required |  |
| startTime | required |  |
| serverCaMode | required |  |

## 📦 google_mlengine_model

🔗 **API Reference**: https://cloud.google.com/ai-platform/prediction/docs/reference/rest/v1/projects.models

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| name | required |  |

## 📦 google_dataplex_entry

🔗 **API Reference**: https://cloud.google.com/dataplex/docs/reference/rest/v1/projects.locations.entryGroups.entries

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| entryType | required |  |
| aspectKey | required |  |
| aspect | required |  |
| data | required |  |

## 📦 google_dataplex_data_product

🔗 **API Reference**: https://cloud.google.com/dataplex/docs/reference/rest/v1/projects.locations.dataProducts

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| data_product_id | required |  |
| displayName | required |  |
| ownerEmails | required |  |
| group_id | required |  |
| displayName | required |  |
| principal | required |  |

## 📦 google_dataplex_glossary

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| glossaryId | required |  |
| displayName | required | name: description |
| description | required | name: labels |
| labels | required | name: uid |
| termCount | required |  |
| categoryCount | required |  |

## 📦 google_dataplex_task

🔗 **API Reference**: https://cloud.google.com/dataplex/docs/reference/rest/v1/projects.locations.lakes.tasks

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| triggerSpec | required |  |
| type | required |  |
| executionSpec | required |  |
| serviceAccount | required | name: project |
| spark | exactly_one_of | spark, notebook |
| network | exactly_one_of | network, subNetwork, name: subNetwork |
| subNetwork | exactly_one_of | network, subNetwork, name: mainJarFileUri |
| mainJarFileUri | exactly_one_of | mainJarFileUri, mainClass, pythonScriptFile, sqlScriptFile |
| mainClass | exactly_one_of | mainJarFileUri, mainClass, pythonScriptFile, sqlScriptFile |
| pythonScriptFile | exactly_one_of | mainJarFileUri, mainClass, pythonScriptFile, sqlScriptFile |
| sqlScriptFile | exactly_one_of | mainJarFileUri, mainClass, pythonScriptFile, sqlScriptFile |
| sqlScript | exactly_one_of | mainJarFileUri, mainClass, pythonScriptFile, sqlScriptFile |
| notebook | exactly_one_of | spark, notebook |
| notebook | required | name: infrastructureSpec |
| network | exactly_one_of | network, subNetwork, name: subNetwork |
| subNetwork | exactly_one_of | network, subNetwork, name: fileUris |

## 📦 google_dataplex_glossary_term

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| displayName | required | name: description |
| description | required | name: labels |
| labels | required | name: uid |
| parent | required |  |

## 📦 google_dataplex_glossary_category

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| displayName | required | name: description |
| description | required | name: labels |
| labels | required | name: uid |
| parent | required |  |

## 📦 google_dataplex_entry_link

🔗 **API Reference**: https://cloud.google.com/dataplex/docs/reference/rest/v1/projects.locations.entryGroups.entryLinks

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| entryGroupId | required | name: entryLinkId |
| entryLinkId | required | name: location |
| entryLinkId | required |  |
| entryLinkType | required | name: createTime |
| entryReferences | required |  |
| name | required | name: path |
| aspectKey | required |  |
| aspect | required |  |
| data | required |  |

## 📦 google_dataplex_datascan

🔗 **API Reference**: https://cloud.google.com/dataplex/docs/reference/rest

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| dataScanId | required |  |
| data | required |  |
| entity | exactly_one_of | data.0.entity, data.0.resource, name: resource |
| resource | exactly_one_of | data.0.entity, data.0.resource, name: executionSpec |
| executionSpec | required |  |
| trigger | required |  |
| onDemand | exactly_one_of | execution_spec.0.trigger.0.on_demand, execution_spec.0.trigger.0.schedule, execution_spec.0.trigger.0.one_time |
| schedule | exactly_one_of | execution_spec.0.trigger.0.on_demand, execution_spec.0.trigger.0.schedule, execution_spec.0.trigger.0.one_time |
| cron | required | name: oneTime |
| cron | exactly_one_of | execution_spec.0.trigger.0.on_demand, execution_spec.0.trigger.0.schedule, execution_spec.0.trigger.0.one_time |
| dataQualitySpec | exactly_one_of | data_quality_spec, data_profile_spec, data_discovery_spec, data_documentation_spec |
| recipients | required |  |
| dimension | required | name: threshold |
| values | required |  |
| regex | required | name: uniquenessExpectation |
| statistic | required |  |
| sqlExpression | required | name: tableConditionExpectation |
| sqlExpression | required | name: sqlAssertion |
| sqlStatement | required |  |
| dataProfileSpec | exactly_one_of | data_quality_spec, data_profile_spec, data_discovery_spec, data_documentation_spec |
| dataDiscoverySpec | exactly_one_of | data_quality_spec, data_profile_spec, data_discovery_spec, data_documentation_spec |
| dataDocumentationSpec | exactly_one_of | data_quality_spec, data_profile_spec, data_discovery_spec, data_documentation_spec |

## 📦 google_dataplex_data_asset

🔗 **API Reference**: https://cloud.google.com/dataplex/docs/reference/rest/v1/projects.locations.dataProducts.dataAssets

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| data_product_id | required |  |
| data_asset_id | required |  |
| resource | required |  |

## 📦 google_dataplex_data_product_data_asset

🔗 **API Reference**: https://cloud.google.com/dataplex/docs/reference/rest/v1/projects.locations.dataProducts.dataAssets

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| data_product_id | required |  |
| data_asset_id | required |  |
| resource | required |  |

## 📦 google_accessapproval_project_settings

🔗 **API Reference**: https://cloud.google.com/access-approval/docs/reference/rest/v1/projects

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| project_id | required |  |
| enrolledServices | required |  |
| cloudProduct | required | name: enrollmentLevel |

## 📦 google_accessapproval_folder_settings

🔗 **API Reference**: https://cloud.google.com/access-approval/docs/reference/rest/v1/folders

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_accessapproval_organization_settings

🔗 **API Reference**: https://cloud.google.com/access-approval/docs/reference/rest/v1/organizations

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| organization_id | required |  |
| enrolledServices | required |  |
| cloudProduct | required | name: enrollmentLevel |

## 📦 google_activedirectory_domain

🔗 **API Reference**: https://cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| domainName | required |  |
| reservedIpRange | required |  |
| locations | required |  |

## 📦 google_activedirectory_peering

🔗 **API Reference**: https://cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.peerings

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| peeringId | required |  |
| authorizedNetwork | required |  |
| domainResource | required |  |

## 📦 google_activedirectory_domain_trust

🔗 **API Reference**: https://cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains/attachTrust

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| domain | required |  |
| targetDomainName | required | name: trustType |
| trustType | required |  |
| trustDirection | required |  |
| targetDnsIpAddresses | required |  |
| trustHandshakeSecret | required |  |

## 📦 google_clouddomains_registration

🔗 **API Reference**: https://cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required | name: domainName |
| domainName | required |  |
| yearlyPrice | required |  |
| preferredRenewalMethod | at_least_one_of | managementSettings.0.preferredRenewalMethod, managementSettings.0.transferLockState, name: transferLockState |
| transferLockState | at_least_one_of | managementSettings.0.preferredRenewalMethod, managementSettings.0.transferLockState, name: dnsSettings |
| nameServers | required |  |
| hostName | required | name: ipv4Addresses |
| contactSettings | required |  |
| privacy | required | name: registrantContact |
| registrantContact | required |  |
| email | required | name: phoneNumber |
| phoneNumber | required | name: faxNumber |
| postalAddress | required |  |
| regionCode | required | name: postalCode |
| adminContact | required |  |
| email | required | name: phoneNumber |
| phoneNumber | required | name: faxNumber |
| postalAddress | required |  |
| regionCode | required | name: postalCode |
| technicalContact | required |  |
| email | required | name: phoneNumber |
| phoneNumber | required | name: faxNumber |
| postalAddress | required |  |
| regionCode | required | name: postalCode |

## 📦 google_parallelstore_instance

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| instanceId | required |  |
| capacityGib | required |  |

## 📦 google_contactcenterinsights_analysis_rule

🔗 **API Reference**: https://cloud.google.com/contact-center/insights/docs/reference/rest/v1/projects.locations.analysisRules

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| contact_center_insights_analysis_rule_profile | required |  |

## 📦 google_contactcenterinsights_assessment_rule

🔗 **API Reference**: https://cloud.google.com/contact-center/insights/docs/reference/rest/v1/projects.locations.assessmentRules

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| contact_center_insights_assessment_rule_full | required |  |
| contact_center_insights_assessment_rule_full | conflicts | sample_row, name: sampleRow |
| contact_center_insights_assessment_rule_full | conflicts | sample_percentage, name: scheduleInfo |

## 📦 google_contactcenterinsights_view

🔗 **API Reference**: https://cloud.google.com/contact-center/insights/docs/reference/rest/v1/projects.locations.views

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| contact_center_insights_view_full | required |  |

## 📦 google_contactcenterinsights_auto_labeling_rule

🔗 **API Reference**: https://cloud.google.com/contact-center/insights/docs/reference/rest/v1/projects.locations.autoLabelingRules

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| contact_center_insights_auto_labeling_rule_basic | required |  |

## 📦 google_cloudfunctions2_function

🔗 **API Reference**: https://cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| storageSource | exactly_one_of | storage_source, repo_source |
| repoSource | exactly_one_of | storage_source, repo_source |
| branchName | exactly_one_of | branch_name, tag_name, commit_sha, name: tagName |
| tagName | exactly_one_of | branch_name, tag_name, commit_sha, name: commitSha |
| commitSha | exactly_one_of | branch_name, tag_name, commit_sha, name: dir |
| automaticUpdatePolicy | exactly_one_of | automatic_update_policy, on_deploy_update_policy |
| onDeployUpdatePolicy | exactly_one_of | automatic_update_policy, on_deploy_update_policy |
| vpcConnector | conflicts | service_config.0.direct_vpc_network_interface, name: vpcConnectorEgressSettings |
| directVpcNetworkInterface | conflicts | service_config.0.vpc_connector |
| key | required | name: projectId |
| projectId | required | name: secret |
| secret | required | name: version |
| version | required | name: secretVolumes |
| mountPath | required | name: projectId |
| projectId | required | name: secret |
| secret | required | name: versions |
| version | required | name: path |
| path | required | name: binaryAuthorizationPolicy |
| eventType | required |  |
| attribute | required | name: value |
| value | required | name: operator |

## 📦 google_cloudidentity_policy

🔗 **API Reference**: https://cloud.google.com/identity/docs/reference/rest/v1beta1/policies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| customer | required |  |
| policyQuery | required |  |
| orgUnit | required | name: group |
| setting | required |  |
| type | required |  |
| valueJson | required |  |

## 📦 google_cloudidentity_group_membership

🔗 **API Reference**: https://cloud.google.com/identity/docs/reference/rest/v1/groups.memberships

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| group | required |  |
| memberKey | exactly_one_of | member_key, preferred_member_key |
| id | required |  |
| preferredMemberKey | exactly_one_of | member_key, preferred_member_key |
| id | required |  |
| roles | required |  |
| name | required |  |
| expireTime | required | name: type |

## 📦 google_cloudidentity_group

🔗 **API Reference**: https://cloud.google.com/identity/docs/reference/rest/v1beta1/groups

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| groupKey | required |  |
| id | required |  |
| parent | required |  |
| labels | required |  |

## 📦 google_healthcare_fhir_store

🔗 **API Reference**: https://cloud.google.com/healthcare/docs/reference/rest/v1/projects.locations.datasets.fhirStores

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| dataset | required |  |
| name | required |  |
| version | required |  |
| version | required |  |
| version | required |  |
| enableUpdateCreate | required | name: disableReferentialIntegrity |
| disableReferentialIntegrity | required |  |
| disableResourceVersioning | required |  |
| enableHistoryImport | required |  |
| enableHistoryModifications | required | name: labels |
| labels | required | name: notificationConfig |
| notificationConfig | required |  |
| pubsubTopic | required | name: selfLink |
| bigqueryDestination | required |  |
| datasetUri | required | name: schemaConfig |
| schemaConfig | required |  |
| recursiveStructureDepth | required | name: lastUpdatedPartitionConfig |
| type | required |  |
| pubsubTopic | required | name: sendFullResource |

## 📦 google_healthcare_workspace

🔗 **API Reference**: https://cloud.google.com/healthcare-api/healthcare-data-engine/docs/reference/rest/v1/projects.locations.datasets.dataMapperWorkspaces

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| dataset | required |  |
| name | required |  |
| settings | required |  |
| dataProjectIds | required |  |
| labels | required |  |

## 📦 google_healthcare_pipeline_job

🔗 **API Reference**: https://cloud.google.com/healthcare-api/healthcare-data-engine/docs/reference/rest/v1/projects.locations.datasets.pipelineJobs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| dataset | required |  |
| name | required | name: disableLineage |
| disableLineage | required |  |
| labels | required |  |
| selfLink | conflicts | reconciliationPipelineJob, backfillPipelineJob |
| selfLink | required |  |
| selfLink | required |  |
| selfLink | required | name: whistleConfigSource |
| selfLink | required |  |
| selfLink | required | name: importUriPrefix |
| selfLink | required | name: fhirStreamingSource |
| selfLink | required |  |
| selfLink | required | name: description |
| selfLink | required | name: fhirStoreDestination |
| selfLink | conflicts | reconciliationDestination |
| selfLink | required | name: reconciliationDestination |
| selfLink | conflicts | fhirStoreDestination |
| selfLink | required | name: reconciliationPipelineJob |
| selfLink | conflicts | mappingPipelineJob, backfillPipelineJob |
| selfLink | required |  |
| selfLink | required |  |
| selfLink | required | name: whistleConfigSource |
| selfLink | required |  |
| selfLink | required | name: importUriPrefix |
| selfLink | required | name: matchingUriPrefix |
| selfLink | required | name: fhirStoreDestination |
| selfLink | required | name: backfillPipelineJob |
| selfLink | conflicts | mappingPipelineJob, reconciliationPipelineJob |
| selfLink | required |  |
| selfLink | required |  |

## 📦 google_healthcare_dicom_store

🔗 **API Reference**: https://cloud.google.com/healthcare/docs/reference/rest/v1/projects.locations.datasets.dicomStores

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| dataset | required |  |
| name | required |  |
| labels | required | name: notificationConfig |
| notificationConfig | required |  |
| pubsubTopic | required | name: sendForBulkImport |
| sendForBulkImport | required | name: selfLink |
| streamConfigs | required |  |
| bigqueryDestination | required |  |
| tableUri | required |  |

## 📦 google_healthcare_hl7_v2_store

🔗 **API Reference**: https://cloud.google.com/healthcare/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| dataset | required |  |
| name | required |  |
| rejectDuplicateMessage | required |  |
| parserConfig | required |  |
| allowNullHeader | at_least_one_of | parser_config.0.allow_null_header, parser_config.0.segment_terminator, parser_config.0.schema, name: segmentTerminator |
| segmentTerminator | at_least_one_of | parser_config.0.allow_null_header, parser_config.0.segment_terminator, parser_config.0.schema |
| schema | at_least_one_of | parser_config.0.allow_null_header, parser_config.0.segment_terminator, parser_config.0.schema, parser_config.0.version |
| labels | required | name: notificationConfigs |
| pubsubTopic | required | name: filter |
| notificationConfig | required |  |
| pubsubTopic | required | name: notificationConfig |
| notificationConfig | required |  |
| pubsubTopic | required | name: selfLink |

## 📦 google_healthcare_dataset

🔗 **API Reference**: https://cloud.google.com/healthcare/docs/reference/rest/v1/projects.locations.datasets

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| timeZone | required |  |
| encryptionSpec | required |  |
| kmsKeyName | required |  |

## 📦 google_healthcare_consent_store

🔗 **API Reference**: https://cloud.google.com/healthcare/docs/reference/rest/v1/projects.locations.datasets.consentStores

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| dataset | required |  |
| name | required |  |
| defaultConsentTtl | required | name: enableConsentCreateOnUpdate |
| enableConsentCreateOnUpdate | required | name: labels |
| labels | required |  |

## 📦 google_composer_user_workloads_config_map

🔗 **API Reference**: https://cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments.userWorkloadsConfigMaps

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| environment | required |  |
| name | required |  |

## 📦 google_appengine_flexible_app_version

🔗 **API Reference**: https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| service | required |  |
| name | required | name: subnetwork |
| cpu | at_least_one_of | resources.0.cpu, resources.0.disk_gb, resources.0.memory_gb, resources.0.volumes |
| diskGb | at_least_one_of | resources.0.cpu, resources.0.disk_gb, resources.0.memory_gb, resources.0.volumes |
| memoryGb | at_least_one_of | resources.0.cpu, resources.0.disk_gb, resources.0.memory_gb, resources.0.volumes |
| volumes | at_least_one_of | resources.0.cpu, resources.0.disk_gb, resources.0.memory_gb, resources.0.volumes |
| name | required | name: volumeType |
| volumeType | required | name: sizeGb |
| sizeGb | required | name: runtime |
| runtime | required | name: runtimeChannel |
| securityLevel | required |  |
| login | required |  |
| authFailAction | required |  |
| redirectHttpResponseCode | required |  |
| scriptPath | required | name: staticFiles |
| script | required | name: securityLevel |
| readinessCheck | required |  |
| path | required | name: host |
| livenessCheck | required |  |
| path | required | name: host |
| zip | at_least_one_of | deployment.0.zip, deployment.0.files, deployment.0.container |
| sourceUrl | required | name: filesCount |
| files | at_least_one_of | deployment.0.zip, deployment.0.files, deployment.0.container |
| sourceUrl | required | name: container |
| container | at_least_one_of | deployment.0.zip, deployment.0.files, deployment.0.container |
| image | required | name: cloudBuildOptions |
| cloudBuildOptions | at_least_one_of | deployment.0.zip, deployment.0.files, deployment.0.container |
| appYamlPath | required | name: cloudBuildTimeout |
| name | required | name: configId |
| shell | required | name: vpcAccessConnector |
| name | required | name: automaticScaling |
| automaticScaling | exactly_one_of | automatic_scaling, manual_scaling |
| cpuUtilization | required |  |
| targetUtilization | required | name: maxConcurrentRequests |
| targetRequestCountPerSecond | at_least_one_of | automatic_scaling.0.request_utilization.0.target_request_count_per_second, automatic_scaling.0.request_utilization.0.target_concurrent_requests, name: targetConcurrentRequests |
| targetConcurrentRequests | at_least_one_of | automatic_scaling.0.request_utilization.0.target_request_count_per_second, automatic_scaling.0.request_utilization.0.target_concurrent_requests, name: diskUtilization |
| targetWriteBytesPerSecond | at_least_one_of | automatic_scaling.0.disk_utilization.0.target_write_bytes_per_second, automatic_scaling.0.disk_utilization.0.target_write_ops_per_second, automatic_scaling.0.disk_utilization.0.target_read_bytes_per_second, automatic_scaling.0.disk_utilization.0.target_read_ops_per_second |
| targetWriteOpsPerSecond | at_least_one_of | automatic_scaling.0.disk_utilization.0.target_write_bytes_per_second, automatic_scaling.0.disk_utilization.0.target_write_ops_per_second, automatic_scaling.0.disk_utilization.0.target_read_bytes_per_second, automatic_scaling.0.disk_utilization.0.target_read_ops_per_second |
| targetReadBytesPerSecond | at_least_one_of | automatic_scaling.0.disk_utilization.0.target_write_bytes_per_second, automatic_scaling.0.disk_utilization.0.target_write_ops_per_second, automatic_scaling.0.disk_utilization.0.target_read_bytes_per_second, automatic_scaling.0.disk_utilization.0.target_read_ops_per_second |
| targetReadOpsPerSecond | at_least_one_of | automatic_scaling.0.disk_utilization.0.target_write_bytes_per_second, automatic_scaling.0.disk_utilization.0.target_write_ops_per_second, automatic_scaling.0.disk_utilization.0.target_read_bytes_per_second, automatic_scaling.0.disk_utilization.0.target_read_ops_per_second |
| targetSentBytesPerSecond | at_least_one_of | automatic_scaling.0.network_utilization.0.target_sent_bytes_per_second, automatic_scaling.0.network_utilization.0.target_sent_packets_per_second, automatic_scaling.0.network_utilization.0.target_received_bytes_per_second, automatic_scaling.0.network_utilization.0.target_received_packets_per_second |
| targetSentPacketsPerSecond | at_least_one_of | automatic_scaling.0.network_utilization.0.target_sent_bytes_per_second, automatic_scaling.0.network_utilization.0.target_sent_packets_per_second, automatic_scaling.0.network_utilization.0.target_received_bytes_per_second, automatic_scaling.0.network_utilization.0.target_received_packets_per_second |
| targetReceivedBytesPerSecond | at_least_one_of | automatic_scaling.0.network_utilization.0.target_sent_bytes_per_second, automatic_scaling.0.network_utilization.0.target_sent_packets_per_second, automatic_scaling.0.network_utilization.0.target_received_bytes_per_second, automatic_scaling.0.network_utilization.0.target_received_packets_per_second |
| targetReceivedPacketsPerSecond | at_least_one_of | automatic_scaling.0.network_utilization.0.target_sent_bytes_per_second, automatic_scaling.0.network_utilization.0.target_sent_packets_per_second, automatic_scaling.0.network_utilization.0.target_received_bytes_per_second, automatic_scaling.0.network_utilization.0.target_received_packets_per_second |
| manualScaling | exactly_one_of | automatic_scaling, manual_scaling |
| instances | required |  |

## 📦 google_appengine_domain_mapping

🔗 **API Reference**: https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.domainMappings

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| domainName | required |  |
| sslManagementType | required |  |

## 📦 google_appengine_application_url_dispatch_rules

🔗 **API Reference**: https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps#UrlDispatchRule

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_appengine_service_network_settings

🔗 **API Reference**: https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| service | required | name: networkSettings |
| networkSettings | required |  |

## 📦 google_appengine_service_split_traffic

🔗 **API Reference**: https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| service | required | name: split |
| split | required |  |
| allocations | required |  |

## 📦 google_appengine_firewall_rule

🔗 **API Reference**: https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.firewall.ingressRules

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| description | required | name: sourceRange |
| sourceRange | required | name: action |
| action | required |  |

## 📦 google_appengine_standard_app_version

🔗 **API Reference**: https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| service | required |  |
| runtime | required | name: serviceAccount |
| securityLevel | required |  |
| login | required |  |
| authFailAction | required |  |
| redirectHttpResponseCode | required |  |
| scriptPath | required | name: staticFiles |
| deployment | required |  |
| zip | required |  |
| zip | at_least_one_of | deployment.0.zip, deployment.0.files |
| sourceUrl | required | name: filesCount |
| filesCount | required | name: files |
| files | required |  |
| files | at_least_one_of | deployment.0.zip, deployment.0.files |
| sourceUrl | required | name: entrypoint |
| entrypoint | required |  |
| shell | required | name: vpcAccessConnector |
| name | required | name: egressSetting |
| automaticScaling | conflicts | basic_scaling, manual_scaling |
| basicScaling | conflicts | automatic_scaling, manual_scaling |
| maxInstances | required | name: manualScaling |
| manualScaling | conflicts | automatic_scaling, basic_scaling |
| instances | required |  |

## 📦 google_filestore_backup

🔗 **API Reference**: https://cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.backups

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| sourceInstance | required | name: sourceFileShare |
| sourceFileShare | required |  |

## 📦 google_filestore_snapshot

🔗 **API Reference**: https://cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances.snapshots

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| instance | required |  |
| name | required |  |

## 📦 google_filestore_instance

🔗 **API Reference**: https://cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances/create

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| zone | exactly_one_of | zone, location |
| location | exactly_one_of | zone, location |
| name | required |  |
| tier | required |  |
| fileShares | required |  |
| name | required |  |
| capacityGb | required | name: sourceBackup |
| networks | required |  |
| network | required |  |
| modes | required |  |
| iopsPerTb | conflicts | fixed_iops |
| fixedIops | conflicts | iops_per_tb |
| peerInstance | required | name: effectiveReplication |
| domain | required |  |
| servers | required |  |

## 📦 google_bigqueryconnection_connection

🔗 **API Reference**: https://cloud.google.com/bigquery/docs/reference/bigqueryconnection/rest/v1/projects.locations.connections/create

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| connectionId | required |  |
| location | required |  |
| cloudSql | exactly_one_of | cloud_sql, aws, azure, cloud_spanner |
| instanceId | required | name: database |
| database | required | name: credential |
| credential | required |  |
| username | required | name: password |
| password | required |  |
| type | required |  |
| aws | exactly_one_of | cloud_sql, aws, azure, cloud_spanner |
| accessRole | required |  |
| iamRoleId | required | name: identity |
| azure | exactly_one_of | cloud_sql, aws, azure, cloud_spanner |
| customerTenantId | required | name: federatedApplicationClientId |
| cloudSpanner | exactly_one_of | cloud_sql, aws, azure, cloud_spanner |
| database | required | name: useParallelism |
| cloudResource | exactly_one_of | cloud_sql, aws, azure, cloud_spanner |
| spark | exactly_one_of | cloud_sql, aws, azure, cloud_spanner |

## 📦 google_securitycentermanagement_organization_event_threat_detection_custom_module

🔗 **API Reference**: https://cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.eventThreatDetectionCustomModules

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| organization | required |  |
| location | required |  |
| config | required |  |
| enablementState | required |  |
| type | required |  |

## 📦 google_securitycentermanagement_organization_security_health_analytics_custom_module

🔗 **API Reference**: https://cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.securityHealthAnalyticsCustomModules

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| organization | required |  |
| location | required |  |
| predicate | required |  |
| expression | required | name: title |
| expression | required | name: title |
| resourceSelector | required |  |
| resourceTypes | required |  |
| severity | required |  |
| recommendation | required |  |

## 📦 google_securitycentermanagement_project_security_health_analytics_custom_module

🔗 **API Reference**: https://cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/projects.locations.securityHealthAnalyticsCustomModules

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| displayName | required |  |
| enablementState | required |  |
| customConfig | required |  |
| predicate | required |  |
| expression | required | name: title |
| expression | required | name: title |
| resourceSelector | required |  |
| resourceTypes | required |  |
| severity | required |  |
| recommendation | required |  |

## 📦 google_securitycentermanagement_folder_security_health_analytics_custom_module

🔗 **API Reference**: https://cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/folders.locations.securityHealthAnalyticsCustomModules

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| folder | required |  |
| location | required |  |
| expression | required | name: title |
| expression | required | name: title |
| resourceTypes | required |  |

## 📦 google_firebasedataconnect_service

🔗 **API Reference**: https://firebase.google.com/docs/reference/data-connect/rest

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: serviceId |
| None | required |  |

## 📦 google_firebaseapphosting_traffic

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: backend |
| None | required |  |
| None | exactly_one_of | rolloutPolicy, target |
| None | required |  |
| None | required |  |
| None | required |  |
| None | exactly_one_of | rolloutPolicy, target |

## 📦 google_firebaseapphosting_domain

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: backend |
| None | required | name: domainId |
| None | required |  |
| None | required | name: status |

## 📦 google_firebaseapphosting_default_domain

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: backend |
| None | required | name: domainId |
| None | required |  |

## 📦 google_firebaseapphosting_backend

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: backendId |
| None | required |  |
| None | required | name: appId |
| None | required | name: serviceAccount |
| None | required | name: annotations |
| None | required | name: rootDirectory |

## 📦 google_firebaseapphosting_build

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: backend |
| None | required |  |
| None | required |  |
| None | required |  |
| None | exactly_one_of | source.0.container, source.0.codebase |
| None | required | name: codebase |
| None | exactly_one_of | source.0.container, source.0.codebase |

## 📦 google_firebasedatabase_instance

🔗 **API Reference**: https://firebase.google.com/docs/reference/rest/database/database-management/rest

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| instance_id | required |  |

## 📦 google_modelarmor_template

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| modelarmor_template_label | required | name: templateId |
| modelarmor_template_label | required |  |
| modelarmor_template_label | required |  |
| modelarmor_template_label | required |  |
| modelarmor_template_label | required | name: confidenceLevel |
| modelarmor_template_label | conflicts | filter_config.0.sdp_settings.0.basic_config |
| modelarmor_template_label | conflicts | filter_config.0.sdp_settings.0.advanced_config |
| modelarmor_template_label | required |  |

## 📦 google_deploymentmanager_deployment

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| target | required |  |
| config | required |  |
| content | required | name: imports |

## 📦 google_memorystore_instance

🔗 **API Reference**: https://cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| desired_psc_auto_connections | conflicts | desiredAutoCreatedEndpoints |
| desired_psc_auto_connections | required | type: String |
| desired_psc_auto_connections | required | name: desired_auto_created_endpoints |
| desired_auto_created_endpoints | conflicts | desiredPscAutoConnections |
| desired_auto_created_endpoints | required | type: String |
| desired_auto_created_endpoints | required |  |
| location | required |  |
| instanceId | required |  |
| fixedFrequencySchedule | required |  |
| startTime | required |  |
| hours | required | name: retention |
| retention | required | name: uid |
| shardCount | required | name: discoveryEndpoints |
| day | required |  |
| startTime | required |  |
| gcsSource | conflicts | managedBackupSource |
| uris | required |  |
| managedBackupSource | conflicts | gcsSource |
| backup | required | name: backupCollection |
| serverCaMode | required |  |

## 📦 google_memorystore_instance_desired_user_created_endpoints

🔗 **API Reference**: https://cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| region | required |  |
| pscConnectionId | required | name: ipAddress |
| ipAddress | required | name: forwardingRule |
| forwardingRule | required | name: projectId |
| network | required | name: serviceAttachment |
| serviceAttachment | required | name: pscConnectionStatus |

## 📦 google_datafusion_instance

🔗 **API Reference**: https://cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| name | required |  |
| type | required |  |
| keyReference | required |  |
| enabled | required | name: topic |
| topic | required |  |
| acceleratorType | required |  |
| state | required |  |

## 📦 google_storagetransfer_agent_pool

🔗 **API Reference**: https://cloud.google.com/storage-transfer/docs/reference/rest/v1/projects.agentPools

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| limitMbps | required |  |

## 📦 google_managedkafka_connector

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_managedkafka_acl

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| cluster | required |  |
| aclId | required |  |
| aclEntries | required |  |
| principal | required | name: permissionType |
| operation | required | name: host |

## 📦 google_managedkafka_topic

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| cluster | required |  |
| topicId | required |  |
| replicationFactor | required |  |

## 📦 google_managedkafka_cluster

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| clusterId | required |  |
| gcpConfig | required |  |
| accessConfig | required |  |
| networkConfigs | required |  |
| subnet | required |  |
| capacityConfig | required |  |
| vcpuCount | required | name: memoryBytes |
| memoryBytes | required | name: brokerCapacityConfig |
| caPool | required |  |

## 📦 google_managedkafka_connect_cluster

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_bigqueryreservation_capacity_commitment

🔗 **API Reference**: https://cloud.google.com/bigquery/docs/reference/reservations/rest/v1/projects.locations.capacityCommitments

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| slotCount | required |  |
| plan | required |  |

## 📦 google_bigqueryreservation_reservation_group

🔗 **API Reference**: https://cloud.google.com/bigquery/docs/reference/reservations/rest/v1/projects.locations.reservationGroups

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |

## 📦 google_bigqueryreservation_reservation_assignment

🔗 **API Reference**: https://cloud.google.com/bigquery/docs/reference/reservations/rest/v1/projects.locations.reservations.assignments

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| reservation | required |  |
| assignee | required |  |
| jobType | required | name: state |

## 📦 google_bigqueryreservation_bi_reservation

🔗 **API Reference**: https://cloud.google.com/bigquery/docs/reference/reservations/rest/v1/BiReservation

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |

## 📦 google_bigqueryreservation_reservation

🔗 **API Reference**: https://cloud.google.com/bigquery/docs/reference/reservations/rest/v1/projects.locations.reservations/create

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | conflicts | autoscale |
| None | conflicts | autoscale |

## 📦 google_firebaseailogic_prompt_template_lock

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |

## 📦 google_firebaseailogic_prompt_template

🔗 **API Reference**: https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_vectorsearch_collection

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | conflicts | sparseVector |
| None | required |  |
| None | required |  |
| None | required |  |
| None | conflicts | denseVector |

## 📦 google_backupdr_backup_plan_association

🔗 **API Reference**: https://cloud.google.com/backup-disaster-recovery/docs/reference/rest

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| backup_plan_association_id | required |  |
| resource | required |  |
| backupPlan | required |  |
| resourceType | required | name: createTime |

## 📦 google_backupdr_management_server

🔗 **API Reference**: https://cloud.google.com/backup-disaster-recovery/docs/deployment/deployment-plan

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required | name: name |
| name | required |  |
| network | required | name: peeringMode |

## 📦 google_backupdr_backup_vault

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| backupVaultId | required |  |
| force_delete | conflicts | ignore_inactive_datasources, name: ignore_inactive_datasources |
| ignore_inactive_datasources | conflicts | force_delete, name: ignore_backup_plan_references |
| backupMinimumEnforcedRetentionDuration | required | name: deletable |

## 📦 google_backupdr_restore_workload

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| backup_vault_id | required |  |
| data_source_id | required |  |
| backup_id | required |  |
| project | required |  |
| zone | required |  |
| project | required |  |
| zone | required |  |
| project | required |  |
| region | required |  |
| replicaZones | required |  |
| name | required |  |
| name | required |  |
| sizeGb | required |  |
| type | required |  |

## 📦 google_backupdr_service_config

🔗 **API Reference**: https://cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/projects.locations.serviceConfig

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| resourceType | required |  |

## 📦 google_backupdr_backup_plan

🔗 **API Reference**: https://cloud.google.com/backup-disaster-recovery/docs/reference/rest

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| backup_plan_id | required |  |
| backupVault | required |  |
| resourceType | required | name: createTime |
| ruleId | required | name: backupRetentionDays |
| backupRetentionDays | required | name: standardSchedule |
| standardSchedule | required |  |
| recurrenceType | required | name: hourlyFrequency |
| weekOfMonth | required | name: dayOfWeek |
| dayOfWeek | required | name: months |
| months | required | name: backupWindow |
| startHourOfDay | required | name: endHourOfDay |
| guestFlush | required |  |

## 📦 google_cloudbuild_bitbucket_server_config

🔗 **API Reference**: https://cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_cloudbuild_trigger

🔗 **API Reference**: https://cloud.google.com/cloud-build/docs/api/reference/rest/v1/projects.triggers

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| filename | exactly_one_of | filename, build, git_file_source, name: filter |
| gitFileSource | exactly_one_of | filename, git_file_source, build |
| path | required | name: uri |
| repoType | required |  |
| pullRequest | exactly_one_of | pull_request, push |
| branch | exactly_one_of | branch, name: invertRegex |
| push | exactly_one_of | pull_request, push |
| branch | exactly_one_of | branch, tag, name: tag |
| tag | exactly_one_of | branch, tag, name: invertRegex |
| ref | required | name: repoType |
| repoType | required |  |
| branchName | exactly_one_of | trigger_template.0.branch_name, trigger_template.0.tag_name, trigger_template.0.commit_sha, name: tagName |
| tagName | exactly_one_of | trigger_template.0.branch_name, trigger_template.0.tag_name, trigger_template.0.commit_sha, name: commitSha |
| commitSha | exactly_one_of | trigger_template.0.branch_name, trigger_template.0.tag_name, trigger_template.0.commit_sha, name: github |
| pullRequest | exactly_one_of | github.0.pull_request, github.0.push |
| branch | required | name: commentControl |
| push | exactly_one_of | github.0.pull_request, github.0.push |
| branch | exactly_one_of | github.0.push.0.branch, github.0.push.0.tag, name: tag |
| tag | exactly_one_of | github.0.push.0.branch, github.0.push.0.tag, name: enterpriseConfigResourceName |
| repoSlug | required | name: projectKey |
| projectKey | required | name: bitbucketServerConfigResource |
| bitbucketServerConfigResource | required | name: pullRequest |
| pullRequest | exactly_one_of | bitbucket_server_trigger_config.0.pull_request, bitbucket_server_trigger_config.0.push |
| branch | required | name: commentControl |
| push | exactly_one_of | bitbucket_server_trigger_config.0.pull_request, bitbucket_server_trigger_config.0.push |
| branch | exactly_one_of | bitbucket_server_trigger_config.0.push.0.branch, bitbucket_server_trigger_config.0.push.0.tag, name: tag |
| tag | exactly_one_of | bitbucket_server_trigger_config.0.push.0.branch, bitbucket_server_trigger_config.0.push.0.tag, name: pubsubConfig |
| topic | required | name: serviceAccountEmail |
| secret | required | name: state |
| build | exactly_one_of | filename, build, git_file_source |
| bucket | required | name: object |
| object | required | name: generation |
| repoName | required | name: dir |
| branchName | exactly_one_of | build.0.source.0.repo_source.0.branch_name, build.0.source.0.repo_source.0.commit_sha, build.0.source.0.repo_source.0.tag_name, name: tagName |
| tagName | exactly_one_of | build.0.source.0.repo_source.0.branch_name, build.0.source.0.repo_source.0.commit_sha, build.0.source.0.repo_source.0.tag_name, name: commitSha |
| commitSha | exactly_one_of | build.0.source.0.repo_source.0.branch_name, build.0.source.0.repo_source.0.commit_sha, build.0.source.0.repo_source.0.tag_name, name: tags |
| kmsKeyName | required | name: secretEnv |
| secretManager | required |  |
| versionName | required | name: env |
| env | required | name: step |
| step | required |  |
| name | required | name: args |
| name | required | name: path |
| path | required | name: waitFor |
| developerConnectEventConfig | exactly_one_of | pullRequest, push |
| gitRepositoryLink | required | name: gitRepositoryLinkType |
| push | exactly_one_of | branch, tag |

## 📦 google_secretmanager_secret_version

🔗 **API Reference**: https://cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets.versions

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| secret | required |  |
| payload | required |  |
| secretData | conflicts | secretDataWo |
| secretDataWo | conflicts | payload.0.secretData |

## 📦 google_secretmanager_secret

🔗 **API Reference**: https://cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| secretId | required |  |
| replication | required |  |
| auto | exactly_one_of | replication.0.user_managed, replication.0.auto |
| kmsKeyName | required | name: userManaged |
| userManaged | exactly_one_of | replication.0.user_managed, replication.0.auto |
| replicas | required |  |
| location | required |  |
| kmsKeyName | required |  |
| name | required | name: expireTime |

## 📦 google_transcoder_job_template

🔗 **API Reference**: https://cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobTemplates

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| jobTemplateId | required |  |
| location | required |  |
| frameRate | required | name: bitrateBps |
| bitrateBps | required | name: pixelFormat |
| bitrateBps | required | name: channelCount |
| type | required |  |
| uri | required | name: animations |
| fadeType | required |  |
| id | required | name: drmSystems |
| scheme | required | name: secretManagerKeySource |
| secretVersion | required |  |

## 📦 google_transcoder_job

🔗 **API Reference**: https://cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_accesscontextmanager_service_perimeter_dry_run_ingress_policy

🔗 **API Reference**: https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ingresspolicy

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| perimeter | required |  |

## 📦 google_accesscontextmanager_service_perimeter_ingress_policy

🔗 **API Reference**: https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ingresspolicy

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| perimeter | required |  |

## 📦 google_accesscontextmanager_service_perimeter_egress_policy

🔗 **API Reference**: https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#egresspolicy

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| perimeter | required |  |

## 📦 google_accesscontextmanager_service_perimeter_dry_run_egress_policy

🔗 **API Reference**: https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#egresspolicy

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| perimeter | required |  |

## 📦 google_accesscontextmanager_access_levels

🔗 **API Reference**: https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parent | required |  |
| name | required |  |
| title | required | name: description |
| basic | conflicts |  |
| conditions | required |  |
| osType | required |  |
| network | required | name: vpcIpSubnetworks |
| custom | conflicts |  |
| expr | required |  |
| expression | required | name: title |

## 📦 google_accesscontextmanager_egress_policy

🔗 **API Reference**: https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#egresspolicy

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| egressPolicyName | required |  |
| resource | required |  |

## 📦 google_accesscontextmanager_service_perimeter_dry_run_resource

🔗 **API Reference**: https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| perimeterName | required |  |
| resource | required |  |

## 📦 google_accesscontextmanager_access_level

🔗 **API Reference**: https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parent | required |  |
| name | required |  |
| title | required | name: description |
| basic | conflicts | custom |
| conditions | required |  |
| osType | required |  |
| network | required | name: vpcIpSubnetworks |
| custom | conflicts | basic |
| expr | required |  |
| expression | required | name: title |

## 📦 google_accesscontextmanager_access_level_condition

🔗 **API Reference**: https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| accessLevel | required |  |
| osType | required |  |
| network | required | name: vpcIpSubnetworks |

## 📦 google_accesscontextmanager_ingress_policy

🔗 **API Reference**: https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ingresspolicy

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| ingressPolicyName | required |  |
| resource | required |  |

## 📦 google_accesscontextmanager_service_perimeters

🔗 **API Reference**: https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parent | required |  |
| name | required |  |
| title | required | name: description |
| resources | at_least_one_of |  |
| accessLevels | at_least_one_of |  |
| restrictedServices | at_least_one_of |  |
| resources | at_least_one_of |  |

## 📦 google_accesscontextmanager_gcp_user_access_binding

🔗 **API Reference**: https://cloud.google.com/access-context-manager/docs/reference/rest/v1/organizations.gcpUserAccessBindings

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| organizationId | required |  |
| groupKey | required |  |

## 📦 google_accesscontextmanager_authorized_orgs_desc

🔗 **API Reference**: https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.authorizedOrgsDescs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parent | required |  |
| name | required |  |

## 📦 google_accesscontextmanager_access_policy

🔗 **API Reference**: https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parent | required |  |
| title | required | name: scopes |

## 📦 google_accesscontextmanager_service_perimeter

🔗 **API Reference**: https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parent | required |  |
| name | required |  |
| title | required | name: description |
| resources | at_least_one_of | status.0.resources, status.0.access_levels, status.0.restricted_services |
| accessLevels | at_least_one_of | status.0.resources, status.0.access_levels, status.0.restricted_services |
| restrictedServices | at_least_one_of | status.0.resources, status.0.access_levels, status.0.restricted_services |
| resources | at_least_one_of | spec.0.resources, spec.0.access_levels, spec.0.restricted_services |
| accessLevels | at_least_one_of | spec.0.resources, spec.0.access_levels, spec.0.restricted_services |
| restrictedServices | at_least_one_of | spec.0.resources, spec.0.access_levels, spec.0.restricted_services |

## 📦 google_accesscontextmanager_service_perimeter_resource

🔗 **API Reference**: https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| perimeterName | required |  |
| resource | required |  |

## 📦 google_parametermanagerregional_regional_parameter

🔗 **API Reference**: https://cloud.google.com/secret-manager/parameter-manager/docs/reference/rest/v1/projects.locations.parameters

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| parameterId | required |  |

## 📦 google_parametermanagerregional_regional_parameter_version

🔗 **API Reference**: https://cloud.google.com/secret-manager/parameter-manager/docs/reference/rest/v1/projects.locations.parameters.versions

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parameter | required |  |
| parameter_version_id | required |  |
| payload | required |  |
| parameter_data | required |  |

## 📦 google_bigquery_row_access_policy

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_bigquery_routine

🔗 **API Reference**: https://cloud.google.com/bigquery/docs/reference/rest/v2/routines

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| routineReference | required |  |
| datasetId | required |  |
| routineId | required |  |
| routineType | required |  |
| definitionBody | required | name: description |
| entryPoint | required | name: packages |

## 📦 google_bigquery_dataset_access

🔗 **API Reference**: https://cloud.google.com/bigquery/docs/reference/rest/v2/datasets

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| datasetId | required |  |
| userByEmail | exactly_one_of | user_by_email, group_by_email, domain, special_group |
| groupByEmail | exactly_one_of | user_by_email, group_by_email, domain, special_group |
| domain | exactly_one_of | user_by_email, group_by_email, domain, special_group |
| specialGroup | exactly_one_of | user_by_email, group_by_email, domain, special_group |
| iamMember | exactly_one_of | user_by_email, group_by_email, domain, special_group |
| view | exactly_one_of | user_by_email, group_by_email, domain, special_group |
| datasetId | required | name: projectId |
| projectId | required | name: tableId |
| tableId | required | name: dataset |
| dataset | exactly_one_of | user_by_email, group_by_email, domain, special_group |
| dataset | required |  |
| datasetId | required | name: projectId |
| projectId | required | name: targetTypes |
| targetTypes | required |  |
| routine | exactly_one_of | user_by_email, group_by_email, domain, special_group |
| datasetId | required | name: projectId |
| projectId | required | name: routineId |
| routineId | required | name: condition |
| condition | required |  |

## 📦 google_bigquery_job

🔗 **API Reference**: https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| configuration | required |  |
| query | exactly_one_of | configuration.0.query, configuration.0.load, configuration.0.copy, configuration.0.extract |
| query | required | name: destinationTable |
| projectId | required |  |
| datasetId | required |  |
| tableId | required |  |
| resourceUri | exactly_one_of |  |
| inlineCode | exactly_one_of |  |
| datasetId | required |  |
| projectId | required |  |
| kmsKeyName | required | name: kmsKeyVersion |
| statementTimeoutMs | at_least_one_of | configuration.0.query.0.script_options.0.statement_timeout_ms, configuration.0.query.0.script_options.0.statement_byte_budget, configuration.0.query.0.script_options.0.key_result_statement, name: statementByteBudget |
| statementByteBudget | at_least_one_of | configuration.0.query.0.script_options.0.statement_timeout_ms, configuration.0.query.0.script_options.0.statement_byte_budget, configuration.0.query.0.script_options.0.key_result_statement, name: keyResultStatement |
| keyResultStatement | at_least_one_of | configuration.0.query.0.script_options.0.statement_timeout_ms, configuration.0.query.0.script_options.0.statement_byte_budget, configuration.0.query.0.script_options.0.key_result_statement |
| key | required | name: value |
| value | required | name: load |
| load | exactly_one_of | configuration.0.query, configuration.0.load, configuration.0.copy, configuration.0.extract |
| sourceUris | required |  |
| destinationTable | required |  |
| projectId | required |  |
| datasetId | required |  |
| tableId | required |  |
| type | required | name: expirationMs |
| kmsKeyName | required | name: kmsKeyVersion |
| enableListInference | at_least_one_of | configuration.0.load.0.parquet_options.0.enum_as_string, configuration.0.load.0.parquet_options.0.enable_list_inference, name: copy |
| copy | exactly_one_of | configuration.0.query, configuration.0.load, configuration.0.copy, configuration.0.extract |
| sourceTables | required |  |
| projectId | required |  |
| datasetId | required |  |
| tableId | required |  |
| projectId | required |  |
| datasetId | required |  |
| tableId | required |  |
| kmsKeyName | required | name: kmsKeyVersion |
| extract | exactly_one_of | configuration.0.query, configuration.0.load, configuration.0.copy, configuration.0.extract |
| destinationUris | required |  |
| sourceTable | exactly_one_of | configuration.0.extract.0.source_table, configuration.0.extract.0.source_model |
| projectId | required |  |
| datasetId | required |  |
| tableId | required |  |
| sourceModel | exactly_one_of | configuration.0.extract.0.source_table, configuration.0.extract.0.source_model |
| projectId | required | name: datasetId |
| datasetId | required | name: modelId |
| modelId | required | name: reservation |
| jobId | required | name: location |

## 📦 google_bigquery_table

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| typeSystem | required |  |
| qualifierString | required | name: type |
| sourceProjectId | required | name: sourceDatasetId |
| sourceDatasetId | required | name: sourceTableId |
| sourceTableId | required | name: replicationIntervalMs |
| serializationLibrary | required | name: parameters |

## 📦 google_bigquery_dataset

🔗 **API Reference**: https://cloud.google.com/bigquery/docs/reference/rest/v2/datasets

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| datasetId | required | name: projectId |
| projectId | required | name: tableId |
| tableId | required | name: dataset |
| dataset | required |  |
| datasetId | required | name: projectId |
| projectId | required | name: targetTypes |
| targetTypes | required |  |
| datasetId | required | name: projectId |
| projectId | required | name: routineId |
| routineId | required | name: condition |
| condition | required |  |
| datasetReference | required |  |
| datasetId | required |  |
| externalSource | required |  |
| connection | required |  |
| kmsKeyName | required | name: isCaseInsensitive |

## 📦 google_storagecontrol_folder_intelligence_config

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| editionConfig | required |  |
| filter | required |  |
| filter | conflicts | filter.0.included_cloud_storage_buckets |
| filter | at_least_one_of | filter.0.included_cloud_storage_buckets, filter.0.excluded_cloud_storage_buckets, filter.0.included_cloud_storage_locations, filter.0.excluded_cloud_storage_locations |
| filter | required |  |
| filter | required |  |
| filter | conflicts | filter.0.excluded_cloud_storage_buckets |
| filter | at_least_one_of | filter.0.included_cloud_storage_buckets, filter.0.excluded_cloud_storage_buckets, filter.0.included_cloud_storage_locations, filter.0.excluded_cloud_storage_locations |
| filter | required |  |
| filter | required |  |
| filter | conflicts | filter.0.included_cloud_storage_locations |
| filter | at_least_one_of | filter.0.included_cloud_storage_buckets, filter.0.excluded_cloud_storage_buckets, filter.0.included_cloud_storage_locations, filter.0.excluded_cloud_storage_locations |
| filter | required |  |
| filter | required |  |
| filter | conflicts | filter.0.excluded_cloud_storage_locations |
| filter | at_least_one_of | filter.0.included_cloud_storage_buckets, filter.0.excluded_cloud_storage_buckets, filter.0.included_cloud_storage_locations, filter.0.excluded_cloud_storage_locations |
| filter | required |  |

## 📦 google_storagecontrol_organization_intelligence_config

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| editionConfig | required |  |
| filter | required |  |
| filter | conflicts | filter.0.included_cloud_storage_buckets |
| filter | at_least_one_of | filter.0.included_cloud_storage_buckets, filter.0.excluded_cloud_storage_buckets, filter.0.included_cloud_storage_locations, filter.0.excluded_cloud_storage_locations |
| filter | required |  |
| filter | required |  |
| filter | conflicts | filter.0.excluded_cloud_storage_buckets |
| filter | at_least_one_of | filter.0.included_cloud_storage_buckets, filter.0.excluded_cloud_storage_buckets, filter.0.included_cloud_storage_locations, filter.0.excluded_cloud_storage_locations |
| filter | required |  |
| filter | required |  |
| filter | conflicts | filter.0.included_cloud_storage_locations |
| filter | at_least_one_of | filter.0.included_cloud_storage_buckets, filter.0.excluded_cloud_storage_buckets, filter.0.included_cloud_storage_locations, filter.0.excluded_cloud_storage_locations |
| filter | required |  |
| filter | required |  |
| filter | conflicts | filter.0.excluded_cloud_storage_locations |
| filter | at_least_one_of | filter.0.included_cloud_storage_buckets, filter.0.excluded_cloud_storage_buckets, filter.0.included_cloud_storage_locations, filter.0.excluded_cloud_storage_locations |
| filter | required |  |

## 📦 google_storagecontrol_project_intelligence_config

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| editionConfig | required |  |
| filter | required |  |
| filter | conflicts | filter.0.included_cloud_storage_buckets |
| filter | at_least_one_of | filter.0.included_cloud_storage_buckets, filter.0.excluded_cloud_storage_buckets, filter.0.included_cloud_storage_locations, filter.0.excluded_cloud_storage_locations |
| filter | required |  |
| filter | required |  |
| filter | conflicts | filter.0.excluded_cloud_storage_buckets |
| filter | at_least_one_of | filter.0.included_cloud_storage_buckets, filter.0.excluded_cloud_storage_buckets, filter.0.included_cloud_storage_locations, filter.0.excluded_cloud_storage_locations |
| filter | required |  |
| filter | required |  |
| filter | conflicts | filter.0.included_cloud_storage_locations |
| filter | at_least_one_of | filter.0.included_cloud_storage_buckets, filter.0.excluded_cloud_storage_buckets, filter.0.included_cloud_storage_locations, filter.0.excluded_cloud_storage_locations |
| filter | required |  |
| filter | required |  |
| filter | conflicts | filter.0.excluded_cloud_storage_locations |
| filter | at_least_one_of | filter.0.included_cloud_storage_buckets, filter.0.excluded_cloud_storage_buckets, filter.0.included_cloud_storage_locations, filter.0.excluded_cloud_storage_locations |
| filter | required |  |

## 📦 google_firebaseappcheck_app_attest_config

🔗 **API Reference**: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.appAttestConfig

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| app_id | required |  |

## 📦 google_firebaseappcheck_debug_token

🔗 **API Reference**: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.debugTokens

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| app_id | required |  |
| displayName | required | name: token |
| token | required |  |

## 📦 google_firebaseappcheck_recaptcha_v3_config

🔗 **API Reference**: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaV3Config

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| app_id | required |  |
| siteSecret | required |  |

## 📦 google_firebaseappcheck_service_config

🔗 **API Reference**: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.services

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| service_id | required |  |

## 📦 google_firebaseappcheck_recaptcha_enterprise_config

🔗 **API Reference**: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.recaptchaEnterpriseConfig

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| app_id | required |  |
| siteKey | required |  |

## 📦 google_firebaseappcheck_play_integrity_config

🔗 **API Reference**: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.playIntegrityConfig

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| app_id | required |  |

## 📦 google_firebaseappcheck_device_check_config

🔗 **API Reference**: https://firebase.google.com/docs/reference/appcheck/rest/v1/projects.apps.deviceCheckConfig

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| app_id | required |  |
| keyId | required | name: privateKey |
| privateKey | required |  |

## 📦 google_firebasehosting_version

🔗 **API Reference**: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| site_id | required |  |
| glob | exactly_one_of |  |
| regex | exactly_one_of |  |
| path | exactly_one_of |  |
| function | exactly_one_of |  |
| run | exactly_one_of |  |
| serviceId | required | name: region |
| glob | exactly_one_of |  |
| regex | exactly_one_of |  |
| statusCode | required | name: location |
| location | required | name: headers |
| glob | exactly_one_of |  |
| regex | exactly_one_of |  |
| headers | required |  |

## 📦 google_firebasehosting_channel

🔗 **API Reference**: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.channels

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| site_id | required |  |
| channel_id | required |  |
| expireTime | conflicts | ttl, name: ttl |
| ttl | conflicts | expireTime |

## 📦 google_firebasehosting_release

🔗 **API Reference**: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.releases

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| site_id | required |  |

## 📦 google_firebasehosting_custom_domain

🔗 **API Reference**: https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites.customDomains

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| site_id | required |  |
| custom_domain | required |  |

## 📦 google_biglakeiceberg_iceberg_namespace

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| catalog | required |  |
| namespace_id | required |  |
| properties | required |  |

## 📦 google_biglakeiceberg_iceberg_catalog

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| credential_mode | required |  |
| catalog_type | required |  |

## 📦 google_biglakeiceberg_iceberg_table

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| catalog | required |  |
| namespace | required |  |
| name | required |  |
| schema | required |  |
| fields | required |  |
| id | required |  |
| name | required |  |
| type | required |  |
| required | required |  |
| fields | required |  |
| source_id | required |  |
| name | required |  |
| transform | required |  |
| properties | required |  |

## 📦 google_ces_app

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_ces_deployment

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_ces_example

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: app |
| None | required | name: exampleId |
| None | required |  |
| None | required | name: entryAgent |
| None | required | name: image |
| None | required | name: mimeType |
| None | required | name: text |
| None | required | name: toolId |
| None | required |  |
| None | required | name: toolId |

## 📦 google_ces_agent

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_ces_tool

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: app |
| None | required | name: toolId |
| None | required |  |
| None | required | name: parameters |
| None | required | name: uniqueItems |
| None | required | name: uniqueItems |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required | name: description |
| None | required | name: type |
| None | required | name: filter |
| None | required | name: rewriterConfig |
| None | required |  |
| None | required | name: displayName |
| None | required | name: preferredDomains |

## 📦 google_ces_guardrail

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_ces_app_version

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: app |
| None | required | name: appVersionId |
| None | required |  |

## 📦 google_ces_toolset

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: app |
| None | required | name: toolsetId |
| None | required |  |
| None | required | name: keyName |
| None | required | name: requestLocation |
| None | required | name: oauthConfig |
| None | required | name: clientSecretVersion |
| None | required | name: oauthGrantType |
| None | required | name: scopes |
| None | required | name: serviceAccountAuthConfig |
| None | required | name: scopes |
| None | required | name: serviceDirectoryConfig |
| None | required | name: tlsConfig |
| None | required |  |
| None | required | name: displayName |
| None | required | name: url |
| None | required | name: apiAuthentication |
| None | required | name: keyName |
| None | required | name: requestLocation |
| None | required | name: oauthConfig |
| None | required | name: clientSecretVersion |
| None | required | name: oauthGrantType |
| None | required | name: scopes |
| None | required | name: serviceAccountAuthConfig |
| None | required | name: scopes |
| None | required | name: tlsConfig |
| None | required |  |
| None | required | name: displayName |
| None | required | name: customHeaders |

## 📦 google_observability_project_settings

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |

## 📦 google_observability_folder_settings

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| folder | required |  |

## 📦 google_observability_trace_scope

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: traceScopeId |
| None | required |  |
| None | required |  |

## 📦 google_observability_organization_settings

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| organization | required |  |

## 📦 google_sourcerepo_repository

🔗 **API Reference**: https://cloud.google.com/source-repositories/docs/reference/rest/v1/projects.repos

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| messageFormat | required |  |

## 📦 google_storage_managed_folder

🔗 **API Reference**: https://cloud.google.com/storage/docs/json_api/v1/managedFolder

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| bucket | required |  |
| name | required |  |

## 📦 google_storage_folder

🔗 **API Reference**: https://cloud.google.com/storage/docs/json_api/v1/folders

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| bucket | required |  |
| name | required |  |

## 📦 google_storage_default_object_access_control

🔗 **API Reference**: https://cloud.google.com/storage/docs/json_api/v1/defaultObjectAccessControls

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| bucket | required |  |
| entity | required | name: entityId |
| object | required | name: projectTeam |
| role | required |  |

## 📦 google_storage_bucket

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| bucket | required |  |
| entity | required | name: entityId |
| bucket | required |  |
| entity | required | name: entityId |
| object | required | name: projectTeam |
| role | required |  |

## 📦 google_storage_anywhere_cache

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| bucket | required |  |
| zone | required |  |

## 📦 google_storage_hmac_key

🔗 **API Reference**: https://cloud.google.com/storage/docs/json_api/v1/projects/hmacKeys

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| serviceAccountEmail | required | name: state |

## 📦 google_storage_object_access_control

🔗 **API Reference**: https://cloud.google.com/storage/docs/json_api/v1/objectAccessControls

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| bucket | required |  |
| entity | required | name: entityId |
| object | required | name: projectTeam |
| role | required |  |

## 📦 google_storage_bucket_access_control

🔗 **API Reference**: https://cloud.google.com/storage/docs/json_api/v1/bucketAccessControls

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |

## 📦 google_tags_tag_key

🔗 **API Reference**: https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagKeys

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parent | required |  |
| shortName | required |  |

## 📦 google_tags_tag_binding

🔗 **API Reference**: https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagBindings

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parent | required | name: tagValue |
| tagValue | required |  |

## 📦 google_tags_tag_value

🔗 **API Reference**: https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parent | required |  |
| shortName | required |  |

## 📦 google_gkebackup_restore_channel

🔗 **API Reference**: https://cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restoreChannels

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| destinationProject | required |  |

## 📦 google_gkebackup_backup_channel

🔗 **API Reference**: https://cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupChannels

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| destinationProject | required |  |

## 📦 google_gkebackup_restore_plan

🔗 **API Reference**: https://cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| backupPlan | required |  |
| cluster | required |  |
| restoreConfig | required |  |
| allNamespaces | exactly_one_of | restoreConfig.0.allNamespaces, restoreConfig.0.excludedNamespaces, restoreConfig.0.selectedNamespaces, restoreConfig.0.selectedApplications |
| excludedNamespaces | exactly_one_of | restoreConfig.0.allNamespaces, restoreConfig.0.excludedNamespaces, restoreConfig.0.selectedNamespaces, restoreConfig.0.selectedApplications |
| namespaces | required |  |
| selectedNamespaces | exactly_one_of | restoreConfig.0.allNamespaces, restoreConfig.0.excludedNamespaces, restoreConfig.0.selectedNamespaces, restoreConfig.0.selectedApplications |
| namespaces | required |  |
| selectedApplications | exactly_one_of | restoreConfig.0.allNamespaces, restoreConfig.0.excludedNamespaces, restoreConfig.0.selectedNamespaces, restoreConfig.0.selectedApplications |
| namespacedNames | required |  |
| namespace | required | name: name |
| name | required | name: noNamespaces |
| noNamespaces | exactly_one_of | restoreConfig.0.allNamespaces, restoreConfig.0.excludedNamespaces, restoreConfig.0.selectedNamespaces, restoreConfig.0.selectedApplications |
| allGroupKinds | exactly_one_of | restoreConfig.0.clusterResourceRestoreScope.0.allGroupKinds, restoreConfig.0.clusterResourceRestoreScope.0.excludedGroupKinds, restoreConfig.0.clusterResourceRestoreScope.0.selectedGroupKinds, restoreConfig.0.clusterResourceRestoreScope.0.noGroupKinds |
| excludedGroupKinds | exactly_one_of | restoreConfig.0.clusterResourceRestoreScope.0.allGroupKinds, restoreConfig.0.clusterResourceRestoreScope.0.excludedGroupKinds, restoreConfig.0.clusterResourceRestoreScope.0.selectedGroupKinds, restoreConfig.0.clusterResourceRestoreScope.0.noGroupKinds |
| selectedGroupKinds | exactly_one_of | restoreConfig.0.clusterResourceRestoreScope.0.allGroupKinds, restoreConfig.0.clusterResourceRestoreScope.0.excludedGroupKinds, restoreConfig.0.clusterResourceRestoreScope.0.selectedGroupKinds, restoreConfig.0.clusterResourceRestoreScope.0.noGroupKinds |
| noGroupKinds | exactly_one_of | restoreConfig.0.clusterResourceRestoreScope.0.allGroupKinds, restoreConfig.0.clusterResourceRestoreScope.0.excludedGroupKinds, restoreConfig.0.clusterResourceRestoreScope.0.selectedGroupKinds, restoreConfig.0.clusterResourceRestoreScope.0.noGroupKinds |
| fieldActions | required |  |
| op | required |  |
| policy | required |  |
| volumeType | required |  |
| groupKindDependencies | required |  |
| satisfying | required |  |
| requiring | required |  |

## 📦 google_gkebackup_backup_plan

🔗 **API Reference**: https://cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| cluster | required |  |
| targetRpoMinutes | required | name: exclusionWindows |
| startTime | required |  |
| duration | required |  |
| gcpKmsEncryptionKey | required | name: allNamespaces |
| allNamespaces | exactly_one_of | backupConfig.0.allNamespaces, backupConfig.0.selectedNamespaces, backupConfig.0.selectedApplications, backupConfig.0.selectedNamespaceLabels |
| selectedNamespaces | exactly_one_of | backupConfig.0.allNamespaces, backupConfig.0.selectedNamespaces, backupConfig.0.selectedApplications, backupConfig.0.selectedNamespaceLabels |
| namespaces | required |  |
| selectedApplications | exactly_one_of | backupConfig.0.allNamespaces, backupConfig.0.selectedNamespaces, backupConfig.0.selectedApplications, backupConfig.0.selectedNamespaceLabels |
| namespacedNames | required |  |
| namespace | required | name: name |
| name | required | name: selectedNamespaceLabels |
| selectedNamespaceLabels | exactly_one_of | backupConfig.0.allNamespaces, backupConfig.0.selectedNamespaces, backupConfig.0.selectedApplications, backupConfig.0.selectedNamespaceLabels |
| resourceLabels | required |  |
| resourceLabels | required | name: "value" |
| resourceLabels | required | name: permissiveMode |

## 📦 google_cloudrun_domain_mapping

🔗 **API Reference**: https://cloud.google.com/run/docs/reference/rest/v1/projects.locations.domainmappings

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_cloudrun_service

🔗 **API Reference**: https://cloud.google.com/run/docs/reference/rest/v1/namespaces.services

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| spec | required |  |
| percent | required | name: tag |
| spec | required |  |
| containers | required |  |
| name | required | name: secretRef |
| name | required | name: optional |
| image | required | name: command |
| secretKeyRef | required |  |
| key | required | name: name |
| name | required | name: ports |
| mountPath | required | name: subPath |
| name | required | name: startupProbe |
| tcpSocket | exactly_one_of | template.0.spec.0.containers.0.startup_probe.0.tcp_socket, template.0.spec.0.containers.0.startup_probe.0.http_get, template.0.spec.0.containers.0.startup_probe.0.grpc |
| httpGet | exactly_one_of | template.0.spec.0.containers.0.startup_probe.0.tcp_socket, template.0.spec.0.containers.0.startup_probe.0.http_get, template.0.spec.0.containers.0.startup_probe.0.grpc |
| name | required | name: value |
| grpc | exactly_one_of | template.0.spec.0.containers.0.startup_probe.0.tcp_socket, template.0.spec.0.containers.0.startup_probe.0.http_get, template.0.spec.0.containers.0.startup_probe.0.grpc |
| httpGet | exactly_one_of | template.0.spec.0.containers.0.readiness_probe.0.http_get, template.0.spec.0.containers.0.readiness_probe.0.grpc |
| grpc | exactly_one_of | template.0.spec.0.containers.0.readiness_probe.0.http_get, template.0.spec.0.containers.0.readiness_probe.0.grpc |
| httpGet | exactly_one_of | template.0.spec.0.containers.0.liveness_probe.0.http_get, template.0.spec.0.containers.0.liveness_probe.0.grpc |
| name | required | name: value |
| grpc | exactly_one_of | template.0.spec.0.containers.0.liveness_probe.0.http_get, template.0.spec.0.containers.0.liveness_probe.0.grpc |
| name | required | name: secret |
| secretName | required | name: defaultMode |
| key | required | name: path |
| path | required | name: mode |
| driver | required | name: readOnly |
| server | required | name: path |
| path | required | name: readOnly |
| metadata | required |  |
| namespace | required |  |

## 📦 google_integrations_auth_config

🔗 **API Reference**: https://cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.authConfigs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| displayName | required | name: description |
| credentialType | required |  |
| usernameAndPassword | conflicts | decryptedCredential.0.oauth2_authorization_code, decryptedCredential.0.oauth2_client_credentials, decryptedCredential.0.jwt, decryptedCredential.0.auth_token |
| oauth2AuthorizationCode | conflicts | decryptedCredential.0.username_and_password, decryptedCredential.0.oauth2_client_credentials, decryptedCredential.0.jwt, decryptedCredential.0.auth_token |
| oauth2ClientCredentials | conflicts | decryptedCredential.0.username_and_password, decryptedCredential.0.oauth2_authorization_code, decryptedCredential.0.jwt, decryptedCredential.0.auth_token |
| jwt | conflicts | decryptedCredential.0.username_and_password, decryptedCredential.0.oauth2_authorization_code, decryptedCredential.0.oauth2_client_credentials, decryptedCredential.0.auth_token |
| authToken | conflicts | decryptedCredential.0.username_and_password, decryptedCredential.0.oauth2_authorization_code, decryptedCredential.0.oauth2_client_credentials, decryptedCredential.0.jwt |
| serviceAccountCredentials | conflicts | decryptedCredential.0.username_and_password, decryptedCredential.0.oauth2_authorization_code, decryptedCredential.0.oauth2_client_credentials, decryptedCredential.0.jwt |
| oidcToken | conflicts | decryptedCredential.0.username_and_password, decryptedCredential.0.oauth2_authorization_code, decryptedCredential.0.oauth2_client_credentials, decryptedCredential.0.jwt |
| ssl_certificate | required | name: encrypted_private_key |
| encrypted_private_key | required | name: passphrase |

## 📦 google_integrations_client

🔗 **API Reference**: https://cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.clients

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| kmsLocation | required | name: kmsRing |
| kmsRing | required | name: key |
| key | required | name: keyVersion |

## 📦 google_hypercomputecluster_cluster

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_container_cluster

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| enabled | required | name: provider |

## 📦 google_memcache_instance

🔗 **API Reference**: https://cloud.google.com/memorystore/docs/memcached/reference/rest/v1/projects.locations.instances

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_blockchainnodeengine_blockchain_nodes

🔗 **API Reference**: https://cloud.google.com/blockchain-node-engine/docs/reference/rest/v1/projects.locations.blockchainNodes

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |

## 📦 google_iap_settings

🔗 **API Reference**: https://cloud.google.com/iap/docs/reference/rest/v1/IapSettings

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| method | required |  |
| maxAge | required | name: policyType |
| policyType | required |  |

## 📦 google_iap_web_type_app_engine

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| appId | required |  |

## 📦 google_iap_tunnel_instance

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |

## 📦 google_iap_app_engine_version

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| appId | required | name: service |
| service | required | name: versionId |
| versionId | required |  |

## 📦 google_iap_brand

🔗 **API Reference**: https://cloud.google.com/iap/docs/reference/rest/v1/projects.brands

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| supportEmail | required | name: applicationTitle |
| applicationTitle | required | name: orgInternalOnly |

## 📦 google_iap_forwarding_rule_regional_service

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |

## 📦 google_iap_cloud_run_service

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |

## 📦 google_iap_tunnel_dest_group

🔗 **API Reference**: https://cloud.google.com/iap/docs/reference/rest/v1/projects.iap_tunnel.locations.destGroups

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| group_name | required |  |

## 📦 google_iap_app_engine_service

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| appId | required | name: service |
| service | required |  |

## 📦 google_iap_web

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |

## 📦 google_iap_forwarding_rule_service

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |

## 📦 google_iap_client

🔗 **API Reference**: https://cloud.google.com/iap/docs/reference/rest/v1/projects.brands.identityAwareProxyClients

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| brand | required |  |
| displayName | required |  |

## 📦 google_iap_web_backend_service

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |

## 📦 google_iap_tunnel

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| project | required |  |

## 📦 google_iap_web_region_backend_service

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |

## 📦 google_iap_web_type_compute

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |

## 📦 google_firebase_android_app

🔗 **API Reference**: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.androidApps

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| displayName | required | name: appId |
| packageName | required |  |

## 📦 google_firebase_web_app

🔗 **API Reference**: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.webApps

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| displayName | required | name: appId |

## 📦 google_firebase_apple_app

🔗 **API Reference**: https://firebase.google.com/docs/reference/firebase-management/rest/v1beta1/projects.iosApps

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| displayName | required | name: appId |
| bundleId | required |  |

## 📦 google_vertexai_feature_online_store

🔗 **API Reference**: https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featureOnlineStores

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| bigtable | exactly_one_of | bigtable, optimized |
| autoScaling | required |  |
| minNodeCount | required | name: maxNodeCount |
| maxNodeCount | required | name: cpuUtilizationTarget |
| optimized | conflicts | embeddingManagement |
| optimized | exactly_one_of | bigtable, optimized |
| enablePrivateServiceConnect | required | name: projectAllowlist |
| embeddingManagement | conflicts | optimized |
| kmsKeyName | required |  |

## 📦 google_vertexai_featurestore

🔗 **API Reference**: https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| fixedNodeCount | exactly_one_of | online_serving_config.0.fixed_node_count, online_serving_config.0.scaling, name: scaling |
| scaling | exactly_one_of | online_serving_config.0.fixed_node_count, online_serving_config.0.scaling |
| minNodeCount | required | name: maxNodeCount |
| maxNodeCount | required | name: onlineStorageTtlDays |
| kmsKeyName | required |  |

## 📦 google_vertexai_tensorboard

🔗 **API Reference**: https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.tensorboards

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| displayName | required | name: description |
| kmsKeyName | required |  |

## 📦 google_vertexai_endpoint

🔗 **API Reference**: https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.endpoints

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| displayName | required | name: description |
| kmsKeyName | required |  |
| network | conflicts | privateServiceConnectConfig, name: privateServiceConnectConfig |
| privateServiceConnectConfig | conflicts | network, dedicatedEndpointEnabled |
| enablePrivateServiceConnect | required |  |
| projectId | required |  |
| network | required |  |
| dedicatedEndpointEnabled | conflicts | privateServiceConnectConfig, name: dedicatedEndpointDns |

## 📦 google_vertexai_rag_engine_config

🔗 **API Reference**: https://cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/v1/RagEngineConfig

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| ragManagedDbConfig | required |  |
| scaled | exactly_one_of | rag_managed_db_config.0.scaled, rag_managed_db_config.0.basic, rag_managed_db_config.0.unprovisioned |
| basic | exactly_one_of | rag_managed_db_config.0.scaled, rag_managed_db_config.0.basic, rag_managed_db_config.0.unprovisioned |
| unprovisioned | exactly_one_of | rag_managed_db_config.0.scaled, rag_managed_db_config.0.basic, rag_managed_db_config.0.unprovisioned |

## 📦 google_vertexai_feature_group_feature

🔗 **API Reference**: https://cloud.google.com/vertex-ai/docs/reference/rest/v1beta1/projects.locations.featureGroups.features

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| featureGroup | required |  |
| region | required |  |
| name | required |  |

## 📦 google_vertexai_cache_config

🔗 **API Reference**: https://cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/v1/projects/updateCacheConfig

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| disableCache | required |  |

## 📦 google_vertexai_featurestore_entitytype_feature

🔗 **API Reference**: https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores.entityTypes.features

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| entitytype | required |  |
| valueType | required |  |

## 📦 google_vertexai_feature_group

🔗 **API Reference**: https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featureGroups

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| bigQuerySource | required |  |
| inputUri | required | name: entityIdColumns |

## 📦 google_vertexai_index_endpoint

🔗 **API Reference**: https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.indexEndpoints/

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| displayName | required | name: description |
| network | conflicts | privateServiceConnectConfig, name: privateServiceConnectConfig |
| privateServiceConnectConfig | conflicts | network |
| enablePrivateServiceConnect | required |  |
| projectId | required |  |
| network | required |  |
| kmsKeyName | required |  |

## 📦 google_vertexai_feature_online_store_featureview

🔗 **API Reference**: https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featureOnlineStores.featureViews

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| featureOnlineStore | required |  |
| region | required |  |
| cron | conflicts | sync_config.0.continuous |
| continuous | conflicts | sync_config.0.cron, name: bigQuerySource |
| bigQuerySource | exactly_one_of | big_query_source, feature_registry_source |
| uri | required | name: entityIdColumns |
| entityIdColumns | required |  |
| featureRegistrySource | conflicts | vector_search_config |
| featureRegistrySource | exactly_one_of | big_query_source, feature_registry_source |
| featureGroups | required |  |
| featureGroupId | required | name: featureIds |
| featureIds | required |  |
| vectorSearchConfig | conflicts | feature_registry_source |
| embeddingColumn | required | name: filterColumns |
| treeAhConfig | exactly_one_of | treeAhConfig, bruteForceConfig |
| bruteForceConfig | exactly_one_of | treeAhConfig, bruteForceConfig |

## 📦 google_vertexai_index_endpoint_deployed_index

🔗 **API Reference**: https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.indexEndpoints#DeployedIndex

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| indexEndpoint | required |  |
| deployedIndexId | required |  |
| index | required |  |
| machineSpec | required |  |
| minReplicaCount | required | name: maxReplicaCount |

## 📦 google_vertexai_reasoning_engine

🔗 **API Reference**: https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.reasoningEngines/

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| displayName | required | name: description |
| kmsKeyName | required | name: spec |
| name | required | name: value |
| value | required | name: secretEnv |
| name | required | name: secretRef |
| secretRef | required |  |
| secret | required | name: version |
| domain | required | name: targetProject |
| targetProject | required | name: targetNetwork |
| targetNetwork | required | name: resourceLimits |
| config | required |  |
| gitRepositoryLink | required |  |
| dir | required |  |
| revision | required |  |
| model | required | name: similaritySearchConfig |
| embeddingModel | required | name: ttlConfig |
| defaultTtl | exactly_one_of | defaultTtl, granularTtlConfig |

## 📦 google_vertexai_endpoint_with_model_garden_deployment

🔗 **API Reference**: https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations/deploy

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | exactly_one_of | "publisher_model_name", "hugging_face_model_id", name: huggingFaceModelId |
| None | exactly_one_of | "publisher_model_name", "hugging_face_model_id", name: modelConfig |
| None | required | name: command |
| None | required | name: value |
| None | required | name: acceptEula |
| None | required |  |
| None | required | name: network |
| None | required | name: ipAddress |
| None | required |  |
| None | required | name: key |
| None | required | name: maxReplicaCount |
| None | required | name: target |

## 📦 google_vertexai_dataset

🔗 **API Reference**: https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.datasets

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| displayName | required | name: createTime |
| metadataSchemaUri | required |  |

## 📦 google_vertexai_featurestore_entitytype

🔗 **API Reference**: https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores.entityTypes

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| featurestore | required |  |
| value | required | name: categoricalThresholdConfig |
| value | required | name: offlineStorageTtlDays |

## 📦 google_vertexai_deployment_resource_pool

🔗 **API Reference**: https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.deploymentResourcePools

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| machineSpec | required |  |
| minReplicaCount | required |  |
| metricName | required | name: target |

## 📦 google_vertexai_index

🔗 **API Reference**: https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.indexes/

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| displayName | required | name: description |
| metadata | required |  |
| config | required |  |
| dimensions | required | name: approximateNeighborsCount |
| treeAhConfig | exactly_one_of | treeAhConfig, bruteForceConfig |
| bruteForceConfig | exactly_one_of | treeAhConfig, bruteForceConfig |
| kmsKeyName | required |  |

## 📦 google_servicedirectory_service

🔗 **API Reference**: https://cloud.google.com/service-directory/docs/reference/rest/v1/projects.locations.namespaces.services

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| namespace | required |  |
| serviceId | required |  |

## 📦 google_servicedirectory_endpoint

🔗 **API Reference**: https://cloud.google.com/service-directory/docs/reference/rest/v1/projects.locations.namespaces.services.endpoints

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| service | required |  |
| endpointId | required |  |

## 📦 google_servicedirectory_namespace

🔗 **API Reference**: https://cloud.google.com/service-directory/docs/reference/rest/v1/projects.locations.namespaces

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| namespaceId | required |  |

## 📦 google_edgecontainer_node_pool

🔗 **API Reference**: https://cloud.google.com/distributed-cloud/edge/latest/docs/reference/container/rest/v1/projects.locations.clusters.nodePools

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| location | required |  |
| cluster | required |  |
| nodeLocation | required |  |
| nodeCount | required | name: machineFilter |

## 📦 google_edgecontainer_cluster

🔗 **API Reference**: https://cloud.google.com/distributed-cloud/edge/latest/docs/reference/container/rest/v1/projects.locations.clusters

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| fleet | required |  |
| project | required |  |
| networking | required |  |
| clusterIpv4CidrBlocks | required |  |
| servicesIpv4CidrBlocks | required |  |
| authorization | required |  |
| adminUsers | required |  |
| username | required | name: defaultMaxPodsPerNode |
| window | required |  |
| recurringWindow | required |  |
| maintenanceExclusions | required |  |
| remote | exactly_one_of | control_plane.0.remote, control_plane.0.local |
| local | exactly_one_of | control_plane.0.remote, control_plane.0.local |

## 📦 google_edgecontainer_vpn_connection

🔗 **API Reference**: https://cloud.google.com/distributed-cloud/edge/latest/docs/reference/container/rest/v1/projects.locations.vpnConnections

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| location | required |  |
| cluster | required |  |

## 📦 google_cloudasset_organization_feed

🔗 **API Reference**: https://cloud.google.com/asset-inventory/docs/reference/rest/

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| org_id | required |  |
| billing_project | required |  |
| feedId | required |  |
| feedOutputConfig | required |  |
| pubsubDestination | required |  |
| topic | required | name: condition |
| expression | required | name: title |

## 📦 google_cloudasset_project_feed

🔗 **API Reference**: https://cloud.google.com/asset-inventory/docs/reference/rest/

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| feedId | required |  |
| feedOutputConfig | required |  |
| pubsubDestination | required |  |
| topic | required | name: condition |
| expression | required | name: title |

## 📦 google_cloudasset_folder_feed

🔗 **API Reference**: https://cloud.google.com/asset-inventory/docs/reference/rest/

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| folder | required |  |
| billing_project | required |  |
| feedId | required |  |
| feedOutputConfig | required |  |
| pubsubDestination | required |  |
| topic | required | name: condition |
| expression | required | name: title |

## 📦 google_compute_router_nat

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/routers

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| router | required |  |
| region | required |  |
| name | required |  |
| natIpAllocateOption | required |  |
| initialNatIps | conflicts | natIps, drainNatIps |
| sourceSubnetworkIpRangesToNat | required |  |
| name | required |  |
| sourceIpRangesToNat | required |  |
| name | required |  |
| enable | required | name: filter |
| filter | required |  |
| ruleNumber | required |  |
| match | required | name: action |

## 📦 google_compute_organization_security_policy

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/organizationSecurityPolicies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parent | required |  |

## 📦 google_compute_security_policy_rule

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/securityPolicies/addRule

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| security_policy | required |  |
| priority | required |  |
| expression | required |  |
| recaptchaOptions | required |  |
| operator | required |  |
| operator | required |  |
| operator | required |  |
| operator | required |  |
| targetRuleSet | required | name: targetRuleIds |
| action | required | name: rateLimitOptions |

## 📦 google_compute_region_target_http_proxy

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/regionTargetHttpProxies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| name | required | name: urlMap |
| urlMap | required |  |

## 📦 google_compute_vpn_tunnel

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/vpnTunnels

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | conflicts | peer_gcp_gateway |
| None | conflicts | peer_external_gateway |
| None | required |  |

## 📦 google_compute_region_ssl_certificate

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/regionSslCertificates

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| certificate | required |  |
| privateKey | required |  |

## 📦 google_compute_interconnect_attachment_group

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/interconnects

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| availabilitySla | required | name: logicalStructure |

## 📦 google_compute_network_endpoints

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/beta/networkEndpointGroups

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| zone | required |  |
| networkEndpointGroup | required |  |
| ipAddress | required |  |

## 📦 google_compute_instance_settings

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/beta/instanceSettings

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| zone | required |  |

## 📦 google_compute_global_forwarding_rule

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| filterMatchCriteria | required |  |
| filterLabels | required |  |
| name | required | name: value |
| value | required |  |
| name | required | name: network |
| target | required |  |

## 📦 google_compute_network_peering_routes_config

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/networks/updatePeering

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| network | required |  |
| peering | required | name: exportCustomRoutes |
| exportCustomRoutes | required |  |
| importCustomRoutes | required |  |

## 📦 google_compute_service_attachment

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/beta/serviceAttachments

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| name | required |  |
| connectionPreference | required | name: connectedEndpoints |
| targetService | required |  |
| natSubnets | required |  |
| enableProxyProtocol | required | name: domainNames |
| connectionLimit | required |  |

## 📦 google_compute_region_per_instance_config

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| regionInstanceGroupManager | required |  |
| name | required |  |
| deviceName | required | name: source |
| source | required | name: mode |

## 📦 google_compute_instant_snapshot

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/instantSnapshots

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| sourceDisk | required |  |
| zone | required |  |
| name | required |  |
| description | required | name: sourceDiskId |

## 📦 google_compute_storage_pool_type

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/storagePoolTypes

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| zone | required |  |
| storagePoolType | required |  |

## 📦 google_compute_organization_security_policy_rule

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/beta/organizationSecurityPolicies/addRule

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| policyId | required |  |
| priority | required |  |
| match | required |  |
| expression | required | name: config |
| srcIpRanges | exactly_one_of | match.0.config.0.src_ip_ranges, match.0.config.0.dest_ip_ranges |
| destIpRanges | exactly_one_of | match.0.config.0.src_ip_ranges, match.0.config.0.dest_ip_ranges |
| ipProtocol | required | name: ports |
| action | required | name: preview |

## 📦 google_compute_instance_template

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |

## 📦 google_compute_firewall

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/v1/firewalls

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| allow | exactly_one_of | allow, deny |
| protocol | required |  |
| deny | exactly_one_of | allow, deny |
| protocol | required |  |
| metadata | required |  |
| name | required |  |
| network | required |  |
| sourceServiceAccounts | conflicts | source_tags, target_tags |
| sourceTags | conflicts | source_service_accounts, target_service_accounts |
| targetServiceAccounts | conflicts | source_tags, target_tags |
| targetTags | conflicts | source_service_accounts, target_service_accounts |

## 📦 google_compute_ssl_policy

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/sslPolicies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |

## 📦 google_compute_target_tcp_proxy

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/v1/targetTcpProxies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | at_least_one_of | backend_service, load_balancing_scheme |
| None | at_least_one_of | backend_service, load_balancing_scheme |

## 📦 google_compute_node_group

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/nodeGroups

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_compute_backend_bucket

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/v1/backendBuckets

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| bucketName | required | name: cdnPolicy |
| queryStringWhitelist | at_least_one_of | cdn_policy.0.cache_key_policy.0.query_string_whitelist, cdn_policy.0.cache_key_policy.0.include_http_headers |
| includeHttpHeaders | at_least_one_of | cdn_policy.0.cache_key_policy.0.query_string_whitelist, cdn_policy.0.cache_key_policy.0.include_http_headers |
| name | required |  |

## 📦 google_compute_region_network_firewall_policy_association

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/addAssociation

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_compute_region_composite_health_check

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/regionCompositeHealthChecks

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| name | required |  |
| healthDestination | required | name: id |

## 📦 google_compute_interconnect_attachment

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/interconnectAttachments

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| name | required |  |

## 📦 google_compute_router_route_policy

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/routers

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| router | required |  |
| region | required |  |
| name | required |  |
| terms | required |  |
| priority | required | name: match |
| match | required |  |
| expression | required | name: title |
| expression | required | name: title |

## 📦 google_compute_per_instance_config

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| zone | required |  |
| instanceGroupManager | required |  |
| name | required |  |
| deviceName | required | name: source |
| source | required | name: mode |

## 📦 google_compute_public_delegated_prefix

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/publicDelegatedPrefixes

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required | name: description |
| name | required | name: parentPrefix |
| parentPrefix | required |  |
| ipCidrRange | required | name: ipv6AccessType |

## 📦 google_compute_disk_resource_policy_attachment

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| disk | required |  |
| zone | required |  |
| name | required |  |

## 📦 google_compute_network_endpoint

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/beta/networkEndpointGroups

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| zone | required |  |
| networkEndpointGroup | required |  |
| ipAddress | required |  |

## 📦 google_compute_project_cloud_armor_tier

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/projects/setCloudArmorTier

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| cloudArmorTier | required |  |

## 📦 google_compute_region_disk_type

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |

## 📦 google_compute_region_target_tcp_proxy

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/regionTargetTcpProxies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | at_least_one_of | backend_service, load_balancing_scheme |
| None | at_least_one_of | backend_service, load_balancing_scheme |

## 📦 google_compute_region_disk

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/regionDisks

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| name | required |  |
| replicaZones | required |  |
| disk | required | name: guestOsFeatures |
| type | required |  |
| accessMode | required |  |

## 📦 google_compute_network_firewall_policy_with_rules

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| rule | required |  |
| priority | required | name: match |
| match | required |  |
| layer4Config | required |  |
| ipProtocol | required | name: ports |
| action | required | name: direction |

## 📦 google_compute_interconnect

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/interconnects

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_compute_global_address

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/v1/globalAddresses

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required | name: labels |

## 📦 google_compute_rollout_plan

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/beta/rolloutPlans

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| waves | required |  |
| selectors | required |  |
| validation | required |  |
| type | required |  |

## 📦 google_compute_ha_vpn_gateway

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/vpnGateways

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| name | required |  |
| network | required |  |

## 📦 google_compute_network_edge_security_service

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/networkEdgeSecurityServices

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| name | required |  |

## 📦 google_compute_health_check

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/healthChecks

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| httpHealthCheck | exactly_one_of | http_health_check, https_health_check, http2_health_check, tcp_health_check |
| host | at_least_one_of | http_health_check.0.host, http_health_check.0.request_path, http_health_check.0.response, http_health_check.0.port |
| requestPath | at_least_one_of | http_health_check.0.host, http_health_check.0.request_path, http_health_check.0.response, http_health_check.0.port |
| response | at_least_one_of | http_health_check.0.host, http_health_check.0.request_path, http_health_check.0.response, http_health_check.0.port |
| port | at_least_one_of | http_health_check.0.host, http_health_check.0.request_path, http_health_check.0.response, http_health_check.0.port |
| portName | at_least_one_of | http_health_check.0.host, http_health_check.0.request_path, http_health_check.0.response, http_health_check.0.port |
| proxyHeader | at_least_one_of | http_health_check.0.host, http_health_check.0.request_path, http_health_check.0.response, http_health_check.0.port |
| portSpecification | at_least_one_of | http_health_check.0.host, http_health_check.0.request_path, http_health_check.0.response, http_health_check.0.port |
| httpsHealthCheck | exactly_one_of | http_health_check, https_health_check, http2_health_check, tcp_health_check |
| host | at_least_one_of | https_health_check.0.host, https_health_check.0.request_path, https_health_check.0.response, https_health_check.0.port |
| requestPath | at_least_one_of | https_health_check.0.host, https_health_check.0.request_path, https_health_check.0.response, https_health_check.0.port |
| response | at_least_one_of | https_health_check.0.host, https_health_check.0.request_path, https_health_check.0.response, https_health_check.0.port |
| port | at_least_one_of | https_health_check.0.host, https_health_check.0.request_path, https_health_check.0.response, https_health_check.0.port |
| portName | at_least_one_of | https_health_check.0.host, https_health_check.0.request_path, https_health_check.0.response, https_health_check.0.port |
| proxyHeader | at_least_one_of | https_health_check.0.host, https_health_check.0.request_path, https_health_check.0.response, https_health_check.0.port |
| portSpecification | at_least_one_of | https_health_check.0.host, https_health_check.0.request_path, https_health_check.0.response, https_health_check.0.port |
| tcpHealthCheck | exactly_one_of | http_health_check, https_health_check, http2_health_check, tcp_health_check |
| request | at_least_one_of | tcp_health_check.0.request, tcp_health_check.0.response, tcp_health_check.0.port, tcp_health_check.0.port_name |
| response | at_least_one_of | tcp_health_check.0.request, tcp_health_check.0.response, tcp_health_check.0.port, tcp_health_check.0.port_name |
| port | at_least_one_of | tcp_health_check.0.request, tcp_health_check.0.response, tcp_health_check.0.port, tcp_health_check.0.port_name |
| portName | at_least_one_of | tcp_health_check.0.request, tcp_health_check.0.response, tcp_health_check.0.port, tcp_health_check.0.port_name |
| proxyHeader | at_least_one_of | tcp_health_check.0.request, tcp_health_check.0.response, tcp_health_check.0.port, tcp_health_check.0.port_name |
| portSpecification | at_least_one_of | tcp_health_check.0.request, tcp_health_check.0.response, tcp_health_check.0.port, tcp_health_check.0.port_name |
| sslHealthCheck | exactly_one_of | http_health_check, https_health_check, http2_health_check, tcp_health_check |
| request | at_least_one_of | ssl_health_check.0.request, ssl_health_check.0.response, ssl_health_check.0.port, ssl_health_check.0.port_name |
| response | at_least_one_of | ssl_health_check.0.request, ssl_health_check.0.response, ssl_health_check.0.port, ssl_health_check.0.port_name |
| port | at_least_one_of | ssl_health_check.0.request, ssl_health_check.0.response, ssl_health_check.0.port, ssl_health_check.0.port_name |
| portName | at_least_one_of | ssl_health_check.0.request, ssl_health_check.0.response, ssl_health_check.0.port, ssl_health_check.0.port_name |
| proxyHeader | at_least_one_of | ssl_health_check.0.request, ssl_health_check.0.response, ssl_health_check.0.port, ssl_health_check.0.port_name |
| portSpecification | at_least_one_of | ssl_health_check.0.request, ssl_health_check.0.response, ssl_health_check.0.port, ssl_health_check.0.port_name |
| http2HealthCheck | exactly_one_of | http_health_check, https_health_check, http2_health_check, tcp_health_check |
| host | at_least_one_of | http2_health_check.0.host, http2_health_check.0.request_path, http2_health_check.0.response, http2_health_check.0.port |
| requestPath | at_least_one_of | http2_health_check.0.host, http2_health_check.0.request_path, http2_health_check.0.response, http2_health_check.0.port |
| response | at_least_one_of | http2_health_check.0.host, http2_health_check.0.request_path, http2_health_check.0.response, http2_health_check.0.port |
| port | at_least_one_of | http2_health_check.0.host, http2_health_check.0.request_path, http2_health_check.0.response, http2_health_check.0.port |
| portName | at_least_one_of | http2_health_check.0.host, http2_health_check.0.request_path, http2_health_check.0.response, http2_health_check.0.port |
| proxyHeader | at_least_one_of | http2_health_check.0.host, http2_health_check.0.request_path, http2_health_check.0.response, http2_health_check.0.port |
| portSpecification | at_least_one_of | http2_health_check.0.host, http2_health_check.0.request_path, http2_health_check.0.response, http2_health_check.0.port |
| grpcHealthCheck | exactly_one_of | http_health_check, https_health_check, http2_health_check, tcp_health_check |
| port | at_least_one_of | grpc_health_check.0.port, grpc_health_check.0.port_name, grpc_health_check.0.port_specification, grpc_health_check.0.grpc_service_name |
| portName | at_least_one_of | grpc_health_check.0.port, grpc_health_check.0.port_name, grpc_health_check.0.port_specification, grpc_health_check.0.grpc_service_name |
| portSpecification | at_least_one_of | grpc_health_check.0.port, grpc_health_check.0.port_name, grpc_health_check.0.port_specification, grpc_health_check.0.grpc_service_name |
| grpcServiceName | at_least_one_of | grpc_health_check.0.port, grpc_health_check.0.port_name, grpc_health_check.0.port_specification, grpc_health_check.0.grpc_service_name |
| grpcTlsHealthCheck | exactly_one_of | http_health_check, https_health_check, http2_health_check, tcp_health_check |
| port | at_least_one_of | grpc_tls_health_check.0.port, grpc_tls_health_check.0.port_specification, grpc_tls_health_check.0.grpc_service_name, name: portSpecification |
| portSpecification | at_least_one_of | grpc_tls_health_check.0.port, grpc_tls_health_check.0.port_specification, grpc_tls_health_check.0.grpc_service_name |
| grpcServiceName | at_least_one_of | grpc_tls_health_check.0.port, grpc_tls_health_check.0.port_specification, grpc_tls_health_check.0.grpc_service_name, name: logConfig |

## 📦 google_compute_packet_mirroring

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/packetMirrorings

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| region | required |  |
| network | required |  |
| url | required |  |
| priority | required |  |
| collectorIlb | required |  |
| url | required |  |
| mirroredResources | required |  |
| subnetworks | at_least_one_of | mirrored_resources.0.subnetworks, mirrored_resources.0.instances, mirrored_resources.0.tags |
| url | required |  |
| instances | at_least_one_of | mirrored_resources.0.subnetworks, mirrored_resources.0.instances, mirrored_resources.0.tags |
| url | required |  |
| tags | at_least_one_of | mirrored_resources.0.subnetworks, mirrored_resources.0.instances, mirrored_resources.0.tags |

## 📦 google_compute_snapshot

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/snapshots

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| zone | required |  |
| sourceDisk | exactly_one_of | source_disk, source_instant_snapshot, name: sourceInstantSnapshot |
| sourceInstantSnapshot | exactly_one_of | source_instant_snapshot, source_disk, name: creationTimestamp |
| name | required |  |

## 📦 google_compute_router_named_set

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/beta/routers

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| router | required |  |
| region | required |  |
| name | required |  |
| type | required | name: elements |
| expression | required | name: title |

## 📦 google_compute_region_autoscaler

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| name | required |  |
| autoscalingPolicy | required |  |
| minReplicas | required |  |
| maxReplicas | required |  |
| maxScaledDownReplicas | at_least_one_of | autoscaling_policy.0.scale_down_control.0.max_scaled_down_replicas, autoscaling_policy.0.scale_down_control.0.time_window_sec |
| fixed | at_least_one_of | autoscaling_policy.0.scale_down_control.0.max_scaled_down_replicas.0.fixed, autoscaling_policy.0.scale_down_control.0.max_scaled_down_replicas.0.percent, name: percent |
| percent | at_least_one_of | autoscaling_policy.0.scale_down_control.0.max_scaled_down_replicas.0.fixed, autoscaling_policy.0.scale_down_control.0.max_scaled_down_replicas.0.percent, name: timeWindowSec |
| timeWindowSec | at_least_one_of | autoscaling_policy.0.scale_down_control.0.max_scaled_down_replicas, autoscaling_policy.0.scale_down_control.0.time_window_sec, name: scaleInControl |
| maxScaledInReplicas | at_least_one_of | autoscaling_policy.0.scale_in_control.0.max_scaled_in_replicas, autoscaling_policy.0.scale_in_control.0.time_window_sec |
| fixed | at_least_one_of | autoscaling_policy.0.scale_in_control.0.max_scaled_in_replicas.0.fixed, autoscaling_policy.0.scale_in_control.0.max_scaled_in_replicas.0.percent, name: percent |
| percent | at_least_one_of | autoscaling_policy.0.scale_in_control.0.max_scaled_in_replicas.0.fixed, autoscaling_policy.0.scale_in_control.0.max_scaled_in_replicas.0.percent, name: timeWindowSec |
| timeWindowSec | at_least_one_of | autoscaling_policy.0.scale_in_control.0.max_scaled_in_replicas, autoscaling_policy.0.scale_in_control.0.time_window_sec, name: cpuUtilization |
| target | required | name: predictiveMethod |
| name | required | name: singleInstanceAssignment |
| target | required | name: scalingSchedules |
| minRequiredReplicas | required |  |
| schedule | required | name: timeZone |
| durationSec | required | name: disabled |
| target | required |  |

## 📦 google_compute_subnetwork

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/subnetworks

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | at_least_one_of | log_config.0.aggregation_interval, log_config.0.flow_sampling, log_config.0.metadata, log_config.0.filterExpr |
| None | at_least_one_of | log_config.0.aggregation_interval, log_config.0.flow_sampling, log_config.0.metadata, log_config.0.filterExpr |
| None | at_least_one_of | log_config.0.aggregation_interval, log_config.0.flow_sampling, log_config.0.metadata, log_config.0.filterExpr |
| None | at_least_one_of | log_config.0.aggregation_interval, log_config.0.flow_sampling, log_config.0.metadata, log_config.0.filterExpr |

## 📦 google_compute_resize_request

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| zone | required |  |
| instanceGroupManager | required |  |
| name | required | name: description |
| resizeBy | required | name: requestedRunDuration |
| seconds | required | name: nanos |

## 📦 google_compute_machine_image

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/beta/machineImages

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |

## 📦 google_compute_ssl_certificate

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/sslCertificates

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| certificate | required |  |
| privateKey | required |  |

## 📦 google_compute_target_instance

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/v1/targetInstances

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| zone | required |  |
| name | required | name: creationTimestamp |
| instance | required |  |

## 📦 google_compute_vpn_gateway

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/targetVpnGateways

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| name | required |  |
| network | required |  |

## 📦 google_compute_wire_group

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/wireGroups

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| crossSiteNetwork | required |  |
| name | required |  |
| name | required |  |

## 📦 google_compute_instance

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| zone | required |  |
| storagePool | required |  |
| name | required | name: natIP |
| type | required |  |
| reservationAffinity | conflicts | guest_accelerators |
| enableConfidentialCompute | at_least_one_of | confidential_instance_config.0.enable_confidential_compute, confidential_instance_config.0.confidential_instance_type |
| confidentialInstanceType | required |  |
| confidentialInstanceType | at_least_one_of | confidential_instance_config.0.enable_confidential_compute, confidential_instance_config.0.confidential_instance_type |

## 📦 google_compute_storage_pool

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/storagePools

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required | name: "description" |
| None | required | name: "poolProvisionedCapacityGb" |
| None | required | name: "poolProvisionedIops" |
| None | required | name: "poolProvisionedThroughput" |
| None | required | name: "labelFingerprint" |
| None | required |  |
| None | required |  |

## 📦 google_compute_forwarding_rule

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/v1/forwardingRules

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| name | required | name: network |

## 📦 google_compute_snapshot_settings

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/snapshotSettings

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| storageLocation | required |  |
| policy | required |  |
| name | required |  |

## 📦 google_compute_region_instance_group_manager

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| baseInstanceName | required | name: instanceGroupManagerId |
| instanceTemplate | required |  |
| name | required |  |

## 📦 google_compute_firewall_policy

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| shortName | required |  |
| parent | required |  |

## 📦 google_compute_backend_bucket_signed_url_key

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/backendBuckets

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| backendBucket | required |  |
| name | required |  |
| keyValue | required |  |

## 📦 google_compute_autoscaler

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/autoscalers

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| zone | required |  |
| name | required |  |
| autoscalingPolicy | required |  |
| minReplicas | required |  |
| maxReplicas | required |  |
| scaleDownControl | required |  |
| maxScaledDownReplicas | at_least_one_of | autoscaling_policy.0.scale_down_control.0.max_scaled_down_replicas, autoscaling_policy.0.scale_down_control.0.time_window_sec |
| fixed | at_least_one_of | autoscaling_policy.0.scale_down_control.0.max_scaled_down_replicas.0.fixed, autoscaling_policy.0.scale_down_control.0.max_scaled_down_replicas.0.percent, name: percent |
| percent | at_least_one_of | autoscaling_policy.0.scale_down_control.0.max_scaled_down_replicas.0.fixed, autoscaling_policy.0.scale_down_control.0.max_scaled_down_replicas.0.percent, name: timeWindowSec |
| timeWindowSec | at_least_one_of | autoscaling_policy.0.scale_down_control.0.max_scaled_down_replicas, autoscaling_policy.0.scale_down_control.0.time_window_sec, name: scaleInControl |
| maxScaledInReplicas | at_least_one_of | autoscaling_policy.0.scale_in_control.0.max_scaled_in_replicas, autoscaling_policy.0.scale_in_control.0.time_window_sec |
| fixed | at_least_one_of | autoscaling_policy.0.scale_in_control.0.max_scaled_in_replicas.0.fixed, autoscaling_policy.0.scale_in_control.0.max_scaled_in_replicas.0.percent, name: percent |
| percent | at_least_one_of | autoscaling_policy.0.scale_in_control.0.max_scaled_in_replicas.0.fixed, autoscaling_policy.0.scale_in_control.0.max_scaled_in_replicas.0.percent, name: timeWindowSec |
| timeWindowSec | at_least_one_of | autoscaling_policy.0.scale_in_control.0.max_scaled_in_replicas, autoscaling_policy.0.scale_in_control.0.time_window_sec, name: cpuUtilization |
| target | required | name: predictiveMethod |
| name | required | name: singleInstanceAssignment |
| target | required | name: scalingSchedules |
| minRequiredReplicas | required |  |
| schedule | required | name: timeZone |
| durationSec | required | name: disabled |
| target | required |  |

## 📦 google_compute_network_firewall_policy_rule

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/networkFirewallPolicies/addRule

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | conflicts | match.0.src_network_context |
| None | conflicts | match.0.src_network_scope |
| None | conflicts | match.0.dest_network_context |
| None | conflicts | match.0.src_network_scope |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_compute_url_map

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/urlMaps

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| defaultService | exactly_one_of | default_service, default_url_redirect, default_route_action.0.weighted_backend_services |
| requestHeadersToAdd | at_least_one_of | header_action.0.request_headers_to_add, header_action.0.request_headers_to_remove, header_action.0.response_headers_to_add, header_action.0.response_headers_to_remove |
| headerName | required | name: headerValue |
| headerValue | required | name: replace |
| replace | required | name: requestHeadersToRemove |
| requestHeadersToRemove | at_least_one_of | header_action.0.request_headers_to_add, header_action.0.request_headers_to_remove, header_action.0.response_headers_to_add, header_action.0.response_headers_to_remove |
| responseHeadersToAdd | at_least_one_of | header_action.0.request_headers_to_add, header_action.0.request_headers_to_remove, header_action.0.response_headers_to_add, header_action.0.response_headers_to_remove |
| headerName | required | name: headerValue |
| headerValue | required | name: replace |
| replace | required | name: responseHeadersToRemove |
| responseHeadersToRemove | at_least_one_of | header_action.0.request_headers_to_add, header_action.0.request_headers_to_remove, header_action.0.response_headers_to_add, header_action.0.response_headers_to_remove |
| hosts | required |  |
| pathMatcher | required | name: name |
| name | required |  |
| defaultService | exactly_one_of |  |
| headerName | required | name: headerValue |
| headerValue | required | name: replace |
| replace | required | name: requestHeadersToRemove |
| headerName | required | name: headerValue |
| headerValue | required | name: replace |
| replace | required | name: responseHeadersToRemove |
| name | required | name: path_rule |
| paths | required |  |
| disabled | required | name: exposeHeaders |
| httpStatus | required | name: percentage |
| percentage | required | name: delay |
| fixedDelay | required |  |
| seconds | required | name: percentage |
| percentage | required | name: requestMirrorPolicy |
| backendService | required |  |
| seconds | required | name: retryConditions |
| seconds | required | name: maxStreamDuration |
| seconds | required | name: urlRewrite |
| backendService | required |  |
| headerName | required | name: headerValue |
| headerValue | required | name: replace |
| replace | required | name: requestHeadersToRemove |
| headerName | required | name: headerValue |
| headerValue | required | name: replace |
| replace | required | name: responseHeadersToRemove |
| weight | required | name: cachePolicy |
| seconds | required |  |
| seconds | required |  |
| seconds | required |  |
| seconds | required |  |
| seconds | required |  |
| stripQuery | required | name: routeRules |
| priority | required | name: service |
| headerName | required | name: headerValue |
| headerValue | required | name: replace |
| replace | required | name: requestHeadersToRemove |
| headerName | required | name: headerValue |
| headerValue | required | name: replace |
| replace | required | name: responseHeadersToRemove |
| headerName | required | name: invertMatch |
| rangeEnd | required | name: rangeStart |
| rangeStart | required | name: regexMatch |
| filterLabels | required |  |
| name | required | name: value |
| value | required |  |
| filterMatchCriteria | required |  |
| name | required | name: presentMatch |
| seconds | required | name: percentage |
| backendService | required |  |
| numRetries | required | name: perTryTimeout |
| seconds | required | name: retryConditions |
| seconds | required | name: maxStreamDuration |
| seconds | required | name: urlRewrite |
| backendService | required |  |
| headerName | required | name: headerValue |
| headerValue | required | name: replace |
| replace | required | name: requestHeadersToRemove |
| headerName | required | name: headerValue |
| headerValue | required | name: replace |
| replace | required | name: responseHeadersToRemove |
| weight | required | name: cachePolicy |
| seconds | required |  |
| seconds | required |  |
| seconds | required |  |
| seconds | required |  |
| seconds | required |  |
| defaultUrlRedirect | exactly_one_of |  |
| stripQuery | required | name: defaultRouteAction |
| defaultRouteAction | conflicts |  |
| weightedBackendServices | exactly_one_of |  |
| seconds | required | name: retryPolicy |
| backendService | required |  |
| seconds | required |  |
| seconds | required |  |
| seconds | required |  |
| seconds | required |  |
| seconds | required |  |
| host | required | name: path |
| path | required | name: headers |
| name | required | name: value |
| value | required | name: service |
| defaultUrlRedirect | conflicts | default_route_action |
| defaultUrlRedirect | exactly_one_of | default_service, default_url_redirect, default_route_action.0.weighted_backend_services |
| stripQuery | required | name: defaultRouteAction |
| defaultRouteAction | conflicts | default_url_redirect |
| weightedBackendServices | at_least_one_of | default_route_action.0.weighted_backend_services, default_route_action.0.url_rewrite, default_route_action.0.timeout, default_route_action.0.retry_policy |
| weightedBackendServices | exactly_one_of | default_service, default_url_redirect, default_route_action.0.weighted_backend_services |
| urlRewrite | at_least_one_of | default_route_action.0.weighted_backend_services, default_route_action.0.url_rewrite, default_route_action.0.timeout, default_route_action.0.retry_policy |
| pathPrefixRewrite | at_least_one_of | default_route_action.0.url_rewrite.0.path_prefix_rewrite, default_route_action.0.url_rewrite.0.host_rewrite, name: hostRewrite |
| hostRewrite | at_least_one_of | default_route_action.0.url_rewrite.0.path_prefix_rewrite, default_route_action.0.url_rewrite.0.host_rewrite, name: timeout |
| timeout | at_least_one_of | default_route_action.0.weighted_backend_services, default_route_action.0.url_rewrite, default_route_action.0.timeout, default_route_action.0.retry_policy |
| seconds | at_least_one_of | default_route_action.0.timeout.0.seconds, default_route_action.0.timeout.0.nanos, name: nanos |
| nanos | at_least_one_of | default_route_action.0.timeout.0.seconds, default_route_action.0.timeout.0.nanos, name: maxStreamDuration |
| seconds | required | name: retryPolicy |
| retryPolicy | at_least_one_of | default_route_action.0.weighted_backend_services, default_route_action.0.url_rewrite, default_route_action.0.timeout, default_route_action.0.retry_policy |
| retryConditions | at_least_one_of | default_route_action.0.retry_policy.0.retry_conditions, default_route_action.0.retry_policy.0.num_retries, default_route_action.0.retry_policy.0.per_try_timeout |
| numRetries | at_least_one_of | default_route_action.0.retry_policy.0.retry_conditions, default_route_action.0.retry_policy.0.num_retries, default_route_action.0.retry_policy.0.per_try_timeout |
| perTryTimeout | at_least_one_of | default_route_action.0.retry_policy.0.retry_conditions, default_route_action.0.retry_policy.0.num_retries, default_route_action.0.retry_policy.0.per_try_timeout |
| seconds | at_least_one_of | default_route_action.0.retry_policy.0.per_try_timeout.0.seconds, default_route_action.0.retry_policy.0.per_try_timeout.0.nanos, name: nanos |
| nanos | at_least_one_of | default_route_action.0.retry_policy.0.per_try_timeout.0.seconds, default_route_action.0.retry_policy.0.per_try_timeout.0.nanos, name: requestMirrorPolicy |
| requestMirrorPolicy | at_least_one_of | default_route_action.0.weighted_backend_services, default_route_action.0.url_rewrite, default_route_action.0.timeout, default_route_action.0.retry_policy |
| backendService | required |  |
| corsPolicy | at_least_one_of | default_route_action.0.weighted_backend_services, default_route_action.0.url_rewrite, default_route_action.0.timeout, default_route_action.0.retry_policy |
| allowOrigins | at_least_one_of | default_route_action.0.cors_policy.0.allow_origins, default_route_action.0.cors_policy.0.allow_origin_regexes, default_route_action.0.cors_policy.0.allow_methods, default_route_action.0.cors_policy.0.allow_headers |
| allowOriginRegexes | at_least_one_of | default_route_action.0.cors_policy.0.allow_origins, default_route_action.0.cors_policy.0.allow_origin_regexes, default_route_action.0.cors_policy.0.allow_methods, default_route_action.0.cors_policy.0.allow_headers |
| allowMethods | at_least_one_of | default_route_action.0.cors_policy.0.allow_origins, default_route_action.0.cors_policy.0.allow_origin_regexes, default_route_action.0.cors_policy.0.allow_methods, default_route_action.0.cors_policy.0.allow_headers |
| allowHeaders | at_least_one_of | default_route_action.0.cors_policy.0.allow_origins, default_route_action.0.cors_policy.0.allow_origin_regexes, default_route_action.0.cors_policy.0.allow_methods, default_route_action.0.cors_policy.0.allow_headers |
| exposeHeaders | at_least_one_of | default_route_action.0.cors_policy.0.allow_origins, default_route_action.0.cors_policy.0.allow_origin_regexes, default_route_action.0.cors_policy.0.allow_methods, default_route_action.0.cors_policy.0.allow_headers |
| maxAge | at_least_one_of | default_route_action.0.cors_policy.0.allow_origins, default_route_action.0.cors_policy.0.allow_origin_regexes, default_route_action.0.cors_policy.0.allow_methods, default_route_action.0.cors_policy.0.allow_headers |
| allowCredentials | at_least_one_of | default_route_action.0.cors_policy.0.allow_origins, default_route_action.0.cors_policy.0.allow_origin_regexes, default_route_action.0.cors_policy.0.allow_methods, default_route_action.0.cors_policy.0.allow_headers |
| disabled | at_least_one_of | default_route_action.0.cors_policy.0.allow_origins, default_route_action.0.cors_policy.0.allow_origin_regexes, default_route_action.0.cors_policy.0.allow_methods, default_route_action.0.cors_policy.0.allow_headers |
| faultInjectionPolicy | at_least_one_of | default_route_action.0.weighted_backend_services, default_route_action.0.url_rewrite, default_route_action.0.timeout, default_route_action.0.retry_policy |
| delay | at_least_one_of | default_route_action.0.fault_injection_policy.0.delay, default_route_action.0.fault_injection_policy.0.abort |
| fixedDelay | at_least_one_of | default_route_action.0.fault_injection_policy.0.delay.0.fixed_delay, default_route_action.0.fault_injection_policy.0.delay.0.percentage |
| seconds | at_least_one_of | default_route_action.0.fault_injection_policy.0.delay.0.fixed_delay.0.seconds, default_route_action.0.fault_injection_policy.0.delay.0.fixed_delay.0.nanos, name: nanos |
| nanos | at_least_one_of | default_route_action.0.fault_injection_policy.0.delay.0.fixed_delay.0.seconds, default_route_action.0.fault_injection_policy.0.delay.0.fixed_delay.0.nanos, name: percentage |
| percentage | at_least_one_of | default_route_action.0.fault_injection_policy.0.delay.0.fixed_delay, default_route_action.0.fault_injection_policy.0.delay.0.percentage |
| abort | at_least_one_of | default_route_action.0.fault_injection_policy.0.delay, default_route_action.0.fault_injection_policy.0.abort |
| httpStatus | at_least_one_of | default_route_action.0.fault_injection_policy.0.abort.0.http_status, default_route_action.0.fault_injection_policy.0.abort.0.percentage |
| percentage | at_least_one_of | default_route_action.0.fault_injection_policy.0.abort.0.http_status, default_route_action.0.fault_injection_policy.0.abort.0.percentage |
| cacheMode | at_least_one_of | default_route_action.0.cache_policy.0.cache_mode, default_route_action.0.cache_policy.0.default_ttl, default_route_action.0.cache_policy.0.max_ttl, default_route_action.0.cache_policy.0.client_ttl |
| defaultTtl | at_least_one_of | default_route_action.0.cache_policy.0.cache_mode, default_route_action.0.cache_policy.0.default_ttl, default_route_action.0.cache_policy.0.max_ttl, default_route_action.0.cache_policy.0.client_ttl |
| seconds | required |  |
| maxTtl | at_least_one_of | default_route_action.0.cache_policy.0.cache_mode, default_route_action.0.cache_policy.0.default_ttl, default_route_action.0.cache_policy.0.max_ttl, default_route_action.0.cache_policy.0.client_ttl |
| seconds | required |  |
| clientTtl | at_least_one_of | default_route_action.0.cache_policy.0.cache_mode, default_route_action.0.cache_policy.0.default_ttl, default_route_action.0.cache_policy.0.max_ttl, default_route_action.0.cache_policy.0.client_ttl |
| seconds | required |  |
| requestCoalescing | at_least_one_of | default_route_action.0.cache_policy.0.cache_mode, default_route_action.0.cache_policy.0.default_ttl, default_route_action.0.cache_policy.0.max_ttl, default_route_action.0.cache_policy.0.client_ttl |
| negativeCaching | at_least_one_of | default_route_action.0.cache_policy.0.cache_mode, default_route_action.0.cache_policy.0.default_ttl, default_route_action.0.cache_policy.0.max_ttl, default_route_action.0.cache_policy.0.client_ttl |
| negativeCachingPolicy | at_least_one_of | default_route_action.0.cache_policy.0.cache_mode, default_route_action.0.cache_policy.0.default_ttl, default_route_action.0.cache_policy.0.max_ttl, default_route_action.0.cache_policy.0.client_ttl |
| seconds | required |  |
| cacheBypassRequestHeaderNames | at_least_one_of | default_route_action.0.cache_policy.0.cache_mode, default_route_action.0.cache_policy.0.default_ttl, default_route_action.0.cache_policy.0.max_ttl, default_route_action.0.cache_policy.0.client_ttl |
| serveWhileStale | at_least_one_of | default_route_action.0.cache_policy.0.cache_mode, default_route_action.0.cache_policy.0.default_ttl, default_route_action.0.cache_policy.0.max_ttl, default_route_action.0.cache_policy.0.client_ttl |
| seconds | required |  |
| cacheKeyPolicy | at_least_one_of | default_route_action.0.cache_policy.0.cache_mode, default_route_action.0.cache_policy.0.default_ttl, default_route_action.0.cache_policy.0.max_ttl, default_route_action.0.cache_policy.0.client_ttl |
| includeProtocol | at_least_one_of | default_route_action.0.cache_policy.0.cache_key_policy.0.include_protocol, default_route_action.0.cache_policy.0.cache_key_policy.0.include_host, default_route_action.0.cache_policy.0.cache_key_policy.0.include_query_string, default_route_action.0.cache_policy.0.cache_key_policy.0.included_query_parameters |
| includeHost | at_least_one_of | default_route_action.0.cache_policy.0.cache_key_policy.0.include_protocol, default_route_action.0.cache_policy.0.cache_key_policy.0.include_host, default_route_action.0.cache_policy.0.cache_key_policy.0.include_query_string, default_route_action.0.cache_policy.0.cache_key_policy.0.included_query_parameters |
| includeQueryString | at_least_one_of | default_route_action.0.cache_policy.0.cache_key_policy.0.include_protocol, default_route_action.0.cache_policy.0.cache_key_policy.0.include_host, default_route_action.0.cache_policy.0.cache_key_policy.0.include_query_string, default_route_action.0.cache_policy.0.cache_key_policy.0.included_query_parameters |
| includedQueryParameters | conflicts | default_route_action.0.cache_policy.0.cache_key_policy.0.excluded_query_parameters |
| includedQueryParameters | at_least_one_of | default_route_action.0.cache_policy.0.cache_key_policy.0.include_protocol, default_route_action.0.cache_policy.0.cache_key_policy.0.include_host, default_route_action.0.cache_policy.0.cache_key_policy.0.include_query_string, default_route_action.0.cache_policy.0.cache_key_policy.0.included_query_parameters |
| excludedQueryParameters | conflicts | default_route_action.0.cache_policy.0.cache_key_policy.0.included_query_parameters |
| excludedQueryParameters | at_least_one_of | default_route_action.0.cache_policy.0.cache_key_policy.0.include_protocol, default_route_action.0.cache_policy.0.cache_key_policy.0.include_host, default_route_action.0.cache_policy.0.cache_key_policy.0.include_query_string, default_route_action.0.cache_policy.0.cache_key_policy.0.included_query_parameters |
| includedHeaderNames | at_least_one_of | default_route_action.0.cache_policy.0.cache_key_policy.0.include_protocol, default_route_action.0.cache_policy.0.cache_key_policy.0.include_host, default_route_action.0.cache_policy.0.cache_key_policy.0.include_query_string, default_route_action.0.cache_policy.0.cache_key_policy.0.included_query_parameters |
| includedCookieNames | at_least_one_of | default_route_action.0.cache_policy.0.cache_key_policy.0.include_protocol, default_route_action.0.cache_policy.0.cache_key_policy.0.include_host, default_route_action.0.cache_policy.0.cache_key_policy.0.include_query_string, default_route_action.0.cache_policy.0.cache_key_policy.0.included_query_parameters |

## 📦 google_compute_resource_policy_attachment

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |

## 📦 google_compute_route

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/routes

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| destRange | required | name: description |
| name | required |  |
| network | required |  |
| nextHopGateway | exactly_one_of | next_hop_gateway, next_hop_instance, next_hop_ip, next_hop_vpn_tunnel |
| nextHopInstance | exactly_one_of | next_hop_gateway, next_hop_instance, next_hop_ip, next_hop_vpn_tunnel |
| nextHopIp | exactly_one_of | next_hop_gateway, next_hop_instance, next_hop_ip, next_hop_vpn_tunnel |
| nextHopVpnTunnel | exactly_one_of | next_hop_gateway, next_hop_instance, next_hop_ip, next_hop_vpn_tunnel |
| nextHopIlb | exactly_one_of | next_hop_gateway, next_hop_instance, next_hop_ip, next_hop_vpn_tunnel |

## 📦 google_compute_region_ssl_policy

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/regionSslPolicies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |

## 📦 google_compute_target_grpc_proxy

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/targetGrpcProxies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |

## 📦 google_compute_network_firewall_policy_packet_mirroring_rule

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/beta/networkFirewallPolicies/addPacketMirroringRule

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| firewallPolicy | required |  |
| priority | required | name: match |
| match | required |  |
| layer4Configs | required |  |
| ipProtocol | required | name: ports |
| action | required | name: securityProfileGroup |
| direction | required |  |

## 📦 google_compute_machine_type

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| zone | required |  |

## 📦 google_compute_region_backend_service

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/latest/regionBackendServices

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| group | required |  |
| name | required |  |
| dryRun | required |  |
| connectTimeout | at_least_one_of | circuit_breakers.0.connect_timeout, circuit_breakers.0.max_requests_per_connection, circuit_breakers.0.max_connections, circuit_breakers.0.max_pending_requests |
| seconds | required | name: nanos |
| maxRequestsPerConnection | at_least_one_of | circuit_breakers.0.connect_timeout, circuit_breakers.0.max_requests_per_connection, circuit_breakers.0.max_connections, circuit_breakers.0.max_pending_requests |
| maxConnections | at_least_one_of | circuit_breakers.0.connect_timeout, circuit_breakers.0.max_requests_per_connection, circuit_breakers.0.max_connections, circuit_breakers.0.max_pending_requests |
| maxPendingRequests | at_least_one_of | circuit_breakers.0.connect_timeout, circuit_breakers.0.max_requests_per_connection, circuit_breakers.0.max_connections, circuit_breakers.0.max_pending_requests |
| maxRequests | at_least_one_of | circuit_breakers.0.connect_timeout, circuit_breakers.0.max_requests_per_connection, circuit_breakers.0.max_connections, circuit_breakers.0.max_pending_requests |
| maxRetries | at_least_one_of | circuit_breakers.0.connect_timeout, circuit_breakers.0.max_requests_per_connection, circuit_breakers.0.max_connections, circuit_breakers.0.max_pending_requests |
| httpCookie | at_least_one_of | consistent_hash.0.http_cookie, consistent_hash.0.http_header_name, consistent_hash.0.minimum_ring_size |
| ttl | at_least_one_of | consistent_hash.0.http_cookie.0.ttl, consistent_hash.0.http_cookie.0.name, consistent_hash.0.http_cookie.0.path |
| seconds | required | name: nanos |
| name | at_least_one_of | consistent_hash.0.http_cookie.0.ttl, consistent_hash.0.http_cookie.0.name, consistent_hash.0.http_cookie.0.path, name: path |
| path | at_least_one_of | consistent_hash.0.http_cookie.0.ttl, consistent_hash.0.http_cookie.0.name, consistent_hash.0.http_cookie.0.path, name: httpHeaderName |
| httpHeaderName | at_least_one_of | consistent_hash.0.http_cookie, consistent_hash.0.http_header_name, consistent_hash.0.minimum_ring_size, name: minimumRingSize |
| minimumRingSize | at_least_one_of | consistent_hash.0.http_cookie, consistent_hash.0.http_header_name, consistent_hash.0.minimum_ring_size |
| cacheKeyPolicy | at_least_one_of | cdn_policy.0.cache_key_policy, cdn_policy.0.signed_url_cache_max_age_sec |
| includeHost | at_least_one_of | cdn_policy.0.cache_key_policy.0.include_host, cdn_policy.0.cache_key_policy.0.include_protocol, cdn_policy.0.cache_key_policy.0.include_query_string, cdn_policy.0.cache_key_policy.0.query_string_blacklist |
| includeProtocol | at_least_one_of | cdn_policy.0.cache_key_policy.0.include_host, cdn_policy.0.cache_key_policy.0.include_protocol, cdn_policy.0.cache_key_policy.0.include_query_string, cdn_policy.0.cache_key_policy.0.query_string_blacklist |
| includeQueryString | at_least_one_of | cdn_policy.0.cache_key_policy.0.include_host, cdn_policy.0.cache_key_policy.0.include_protocol, cdn_policy.0.cache_key_policy.0.include_query_string, cdn_policy.0.cache_key_policy.0.query_string_blacklist |
| queryStringBlacklist | at_least_one_of | cdn_policy.0.cache_key_policy.0.include_host, cdn_policy.0.cache_key_policy.0.include_protocol, cdn_policy.0.cache_key_policy.0.include_query_string, cdn_policy.0.cache_key_policy.0.query_string_blacklist |
| queryStringWhitelist | at_least_one_of | cdn_policy.0.cache_key_policy.0.include_host, cdn_policy.0.cache_key_policy.0.include_protocol, cdn_policy.0.cache_key_policy.0.include_query_string, cdn_policy.0.cache_key_policy.0.query_string_blacklist |
| includeNamedCookies | at_least_one_of | cdn_policy.0.cache_key_policy.0.include_host, cdn_policy.0.cache_key_policy.0.include_protocol, cdn_policy.0.cache_key_policy.0.include_query_string, cdn_policy.0.cache_key_policy.0.query_string_blacklist |
| signedUrlCacheMaxAgeSec | at_least_one_of | cdn_policy.0.cache_key_policy, cdn_policy.0.signed_url_cache_max_age_sec |
| disableConnectionDrainOnFailover | at_least_one_of | failover_policy.0.disable_connection_drain_on_failover, failover_policy.0.drop_traffic_if_unhealthy, failover_policy.0.failover_ratio, name: dropTrafficIfUnhealthy |
| dropTrafficIfUnhealthy | at_least_one_of | failover_policy.0.disable_connection_drain_on_failover, failover_policy.0.drop_traffic_if_unhealthy, failover_policy.0.failover_ratio, name: failoverRatio |
| failoverRatio | at_least_one_of | failover_policy.0.disable_connection_drain_on_failover, failover_policy.0.drop_traffic_if_unhealthy, failover_policy.0.failover_ratio, name: enableCDN |
| enabled | required |  |
| name | required |  |
| name | required |  |
| dryRun | required |  |
| baseEjectionTime | at_least_one_of | outlier_detection.0.base_ejection_time, outlier_detection.0.consecutive_errors, outlier_detection.0.consecutive_gateway_failure, outlier_detection.0.enforcing_consecutive_errors |
| seconds | required | name: nanos |
| consecutiveErrors | at_least_one_of | outlier_detection.0.base_ejection_time, outlier_detection.0.consecutive_errors, outlier_detection.0.consecutive_gateway_failure, outlier_detection.0.enforcing_consecutive_errors |
| consecutiveGatewayFailure | at_least_one_of | outlier_detection.0.base_ejection_time, outlier_detection.0.consecutive_errors, outlier_detection.0.consecutive_gateway_failure, outlier_detection.0.enforcing_consecutive_errors |
| enforcingConsecutiveErrors | at_least_one_of | outlier_detection.0.base_ejection_time, outlier_detection.0.consecutive_errors, outlier_detection.0.consecutive_gateway_failure, outlier_detection.0.enforcing_consecutive_errors |
| enforcingConsecutiveGatewayFailure | at_least_one_of | outlier_detection.0.base_ejection_time, outlier_detection.0.consecutive_errors, outlier_detection.0.consecutive_gateway_failure, outlier_detection.0.enforcing_consecutive_errors |
| enforcingSuccessRate | at_least_one_of | outlier_detection.0.base_ejection_time, outlier_detection.0.consecutive_errors, outlier_detection.0.consecutive_gateway_failure, outlier_detection.0.enforcing_consecutive_errors |
| interval | at_least_one_of | outlier_detection.0.base_ejection_time, outlier_detection.0.consecutive_errors, outlier_detection.0.consecutive_gateway_failure, outlier_detection.0.enforcing_consecutive_errors |
| seconds | required | name: nanos |
| maxEjectionPercent | at_least_one_of | outlier_detection.0.base_ejection_time, outlier_detection.0.consecutive_errors, outlier_detection.0.consecutive_gateway_failure, outlier_detection.0.enforcing_consecutive_errors |
| successRateMinimumHosts | at_least_one_of | outlier_detection.0.base_ejection_time, outlier_detection.0.consecutive_errors, outlier_detection.0.consecutive_gateway_failure, outlier_detection.0.enforcing_consecutive_errors |
| successRateRequestVolume | at_least_one_of | outlier_detection.0.base_ejection_time, outlier_detection.0.consecutive_errors, outlier_detection.0.consecutive_gateway_failure, outlier_detection.0.enforcing_consecutive_errors |
| successRateStdevFactor | at_least_one_of | outlier_detection.0.base_ejection_time, outlier_detection.0.consecutive_errors, outlier_detection.0.consecutive_gateway_failure, outlier_detection.0.enforcing_consecutive_errors |
| ttl | at_least_one_of | strong_session_affinity_cookie.0.ttl, strong_session_affinity_cookie.0.name, strong_session_affinity_cookie.0.path |
| seconds | required | name: nanos |
| name | at_least_one_of | strong_session_affinity_cookie.0.ttl, strong_session_affinity_cookie.0.name, strong_session_affinity_cookie.0.path, name: path |
| path | at_least_one_of | strong_session_affinity_cookie.0.ttl, strong_session_affinity_cookie.0.name, strong_session_affinity_cookie.0.path, name: connectionTrackingPolicy |
| enable | at_least_one_of | log_config.0.enable, log_config.0.sample_rate, log_config.0.optional_mode, name: sampleRate |
| sampleRate | at_least_one_of | log_config.0.enable, log_config.0.sample_rate, log_config.0.optional_mode |
| optionalMode | at_least_one_of | log_config.0.enable, log_config.0.sample_rate, log_config.0.optional_mode |
| policy | required |  |
| enabled | required | name: proxyMode |
| proxyMode | required | name: haPolicy |
| haPolicy | conflicts | sessionAffinity, connectionTrackingPolicy, failoverPolicy, healthChecks |
| dnsName | exactly_one_of | tlsSettings.0.uniform_resource_identifier, tlsSettings.0.dns_name, name: uniformResourceIdentifier |
| uniformResourceIdentifier | exactly_one_of | tlsSettings.0.uniform_resource_identifier, tlsSettings.0.dns_name, name: authenticationConfig |

## 📦 google_compute_network_firewall_policy

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |

## 📦 google_compute_region_health_aggregation_policy

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/healthAggregationPolicies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| name | required |  |

## 📦 google_compute_network_attachment

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/networkAttachments

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| region | required |  |
| connectionPreference | required |  |
| subnetworks | required |  |

## 📦 google_compute_region_network_firewall_policy_with_rules

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| rule | required |  |
| priority | required | name: match |
| match | required |  |
| layer4Config | required |  |
| ipProtocol | required | name: ports |
| action | required | name: direction |

## 📦 google_compute_firewall_policy_with_rules

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parent | required |  |
| shortName | required |  |
| rule | required |  |
| priority | required | name: match |
| match | required |  |
| layer4Config | required |  |
| ipProtocol | required | name: ports |
| action | required | name: direction |

## 📦 google_compute_network

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/networks

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| routingMode | required |  |
| bgpAlwaysCompareMed | required |  |
| bgpInterRegionCost | required |  |

## 📦 google_compute_target_ssl_proxy

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/v1/targetSslProxies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| backendService | required |  |

## 📦 google_compute_region_backend_bucket

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/beta/regionBackendBuckets

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| bucketName | required | name: creationTimestamp |
| name | required |  |
| loadBalancingScheme | required |  |

## 📦 google_compute_region_network_endpoint_group

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/beta/regionNetworkEndpointGroups

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| name | required |  |
| cloudRun | conflicts | cloud_function, app_engine, serverless_deployment |
| service | at_least_one_of | cloud_run.0.service, cloud_run.0.url_mask, name: tag |
| urlMask | at_least_one_of | cloud_run.0.service, cloud_run.0.url_mask, name: appEngine |
| appEngine | conflicts | cloud_run, cloud_function, serverless_deployment |
| cloudFunction | conflicts | cloud_run, app_engine, serverless_deployment |
| function | at_least_one_of | cloud_function.0.function, cloud_function.0.url_mask, name: urlMask |
| urlMask | at_least_one_of | cloud_function.0.function, cloud_function.0.url_mask, name: serverlessDeployment |
| serverlessDeployment | conflicts | cloud_run, cloud_function, app_engine |
| platform | required | name: resource |
| urlMask | required |  |

## 📦 google_compute_region_url_map

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| defaultService | exactly_one_of | default_service, default_url_redirect, default_route_action.0.weighted_backend_services |
| hosts | required |  |
| pathMatcher | required | name: map_id |
| name | required |  |
| defaultService | exactly_one_of |  |
| name | required | name: routeRules |
| priority | required | name: service |
| headerName | required | name: headerValue |
| headerValue | required | name: replace |
| replace | required | name: requestHeadersToRemove |
| headerName | required | name: headerValue |
| headerValue | required | name: replace |
| replace | required | name: responseHeadersToRemove |
| headerName | required | name: invertMatch |
| rangeEnd | required | name: rangeStart |
| rangeStart | required | name: regexMatch |
| filterLabels | required |  |
| name | required | name: value |
| value | required |  |
| filterMatchCriteria | required |  |
| name | required | name: presentMatch |
| seconds | required | name: percentage |
| backendService | required |  |
| numRetries | required | name: perTryTimeout |
| seconds | required | name: retryConditions |
| seconds | required | name: urlRewrite |
| backendService | required |  |
| headerName | required | name: headerValue |
| headerValue | required | name: replace |
| replace | required | name: requestHeadersToRemove |
| headerName | required | name: headerValue |
| headerValue | required | name: replace |
| replace | required | name: responseHeadersToRemove |
| weight | required | name: urlRedirect |
| paths | required |  |
| disabled | required | name: exposeHeaders |
| httpStatus | required | name: percentage |
| percentage | required | name: delay |
| fixedDelay | required |  |
| seconds | required | name: percentage |
| percentage | required | name: requestMirrorPolicy |
| backendService | required |  |
| seconds | required | name: retryConditions |
| seconds | required | name: urlRewrite |
| backendService | required |  |
| headerName | required | name: headerValue |
| headerValue | required | name: replace |
| replace | required | name: requestHeadersToRemove |
| headerName | required | name: headerValue |
| headerValue | required | name: replace |
| replace | required | name: responseHeadersToRemove |
| weight | required | name: urlRedirect |
| stripQuery | required | name: defaultUrlRedirect |
| defaultUrlRedirect | exactly_one_of |  |
| stripQuery | required | name: defaultRouteAction |
| defaultRouteAction | conflicts |  |
| weightedBackendServices | exactly_one_of |  |
| pathTemplateRewrite | exactly_one_of |  |
| seconds | required | name: retryPolicy |
| backendService | required |  |
| host | required | name: path |
| path | required | name: service |
| service | required |  |
| defaultUrlRedirect | conflicts | default_route_action |
| defaultUrlRedirect | exactly_one_of | default_service, default_url_redirect, default_route_action.0.weighted_backend_services |
| stripQuery | required | name: defaultRouteAction |
| defaultRouteAction | conflicts | default_url_redirect |
| weightedBackendServices | at_least_one_of | default_route_action.0.weighted_backend_services, default_route_action.0.url_rewrite, default_route_action.0.timeout, default_route_action.0.retry_policy |
| weightedBackendServices | exactly_one_of | default_service, default_url_redirect, default_route_action.0.weighted_backend_services |
| urlRewrite | at_least_one_of | default_route_action.0.weighted_backend_services, default_route_action.0.url_rewrite, default_route_action.0.timeout, default_route_action.0.retry_policy |
| pathPrefixRewrite | at_least_one_of | default_route_action.0.url_rewrite.0.path_prefix_rewrite, default_route_action.0.url_rewrite.0.host_rewrite |
| hostRewrite | at_least_one_of | default_route_action.0.url_rewrite.0.path_prefix_rewrite, default_route_action.0.url_rewrite.0.host_rewrite |
| timeout | at_least_one_of | default_route_action.0.weighted_backend_services, default_route_action.0.url_rewrite, default_route_action.0.timeout, default_route_action.0.retry_policy |
| seconds | at_least_one_of | default_route_action.0.timeout.0.seconds, default_route_action.0.timeout.0.nanos, name: nanos |
| nanos | at_least_one_of | default_route_action.0.timeout.0.seconds, default_route_action.0.timeout.0.nanos |
| retryPolicy | at_least_one_of | default_route_action.0.weighted_backend_services, default_route_action.0.url_rewrite, default_route_action.0.timeout, default_route_action.0.retry_policy |
| retryConditions | at_least_one_of | default_route_action.0.retry_policy.0.retry_conditions, default_route_action.0.retry_policy.0.num_retries, default_route_action.0.retry_policy.0.per_try_timeout |
| numRetries | at_least_one_of | default_route_action.0.retry_policy.0.retry_conditions, default_route_action.0.retry_policy.0.num_retries, default_route_action.0.retry_policy.0.per_try_timeout |
| perTryTimeout | at_least_one_of | default_route_action.0.retry_policy.0.retry_conditions, default_route_action.0.retry_policy.0.num_retries, default_route_action.0.retry_policy.0.per_try_timeout |
| seconds | at_least_one_of | default_route_action.0.retry_policy.0.per_try_timeout.0.seconds, default_route_action.0.retry_policy.0.per_try_timeout.0.nanos, name: nanos |
| nanos | at_least_one_of | default_route_action.0.retry_policy.0.per_try_timeout.0.seconds, default_route_action.0.retry_policy.0.per_try_timeout.0.nanos |
| requestMirrorPolicy | at_least_one_of | default_route_action.0.weighted_backend_services, default_route_action.0.url_rewrite, default_route_action.0.timeout, default_route_action.0.retry_policy |
| corsPolicy | at_least_one_of | default_route_action.0.weighted_backend_services, default_route_action.0.url_rewrite, default_route_action.0.timeout, default_route_action.0.retry_policy |
| allowOrigins | at_least_one_of | default_route_action.0.cors_policy.0.allow_origins, default_route_action.0.cors_policy.0.allow_origin_regexes, default_route_action.0.cors_policy.0.allow_methods, default_route_action.0.cors_policy.0.allow_headers |
| allowOriginRegexes | at_least_one_of | default_route_action.0.cors_policy.0.allow_origins, default_route_action.0.cors_policy.0.allow_origin_regexes, default_route_action.0.cors_policy.0.allow_methods, default_route_action.0.cors_policy.0.allow_headers |
| allowMethods | at_least_one_of | default_route_action.0.cors_policy.0.allow_origins, default_route_action.0.cors_policy.0.allow_origin_regexes, default_route_action.0.cors_policy.0.allow_methods, default_route_action.0.cors_policy.0.allow_headers |
| allowHeaders | at_least_one_of | default_route_action.0.cors_policy.0.allow_origins, default_route_action.0.cors_policy.0.allow_origin_regexes, default_route_action.0.cors_policy.0.allow_methods, default_route_action.0.cors_policy.0.allow_headers |
| exposeHeaders | at_least_one_of | default_route_action.0.cors_policy.0.allow_origins, default_route_action.0.cors_policy.0.allow_origin_regexes, default_route_action.0.cors_policy.0.allow_methods, default_route_action.0.cors_policy.0.allow_headers |
| maxAge | at_least_one_of | default_route_action.0.cors_policy.0.allow_origins, default_route_action.0.cors_policy.0.allow_origin_regexes, default_route_action.0.cors_policy.0.allow_methods, default_route_action.0.cors_policy.0.allow_headers |
| allowCredentials | at_least_one_of | default_route_action.0.cors_policy.0.allow_origins, default_route_action.0.cors_policy.0.allow_origin_regexes, default_route_action.0.cors_policy.0.allow_methods, default_route_action.0.cors_policy.0.allow_headers |
| disabled | at_least_one_of | default_route_action.0.cors_policy.0.allow_origins, default_route_action.0.cors_policy.0.allow_origin_regexes, default_route_action.0.cors_policy.0.allow_methods, default_route_action.0.cors_policy.0.allow_headers |
| faultInjectionPolicy | at_least_one_of | default_route_action.0.weighted_backend_services, default_route_action.0.url_rewrite, default_route_action.0.timeout, default_route_action.0.retry_policy |
| delay | at_least_one_of | default_route_action.0.fault_injection_policy.0.delay, default_route_action.0.fault_injection_policy.0.abort |
| fixedDelay | at_least_one_of | default_route_action.0.fault_injection_policy.0.delay.0.fixed_delay, default_route_action.0.fault_injection_policy.0.delay.0.percentage |
| seconds | at_least_one_of | default_route_action.0.fault_injection_policy.0.delay.0.fixed_delay.0.seconds, default_route_action.0.fault_injection_policy.0.delay.0.fixed_delay.0.nanos, name: nanos |
| nanos | at_least_one_of | default_route_action.0.fault_injection_policy.0.delay.0.fixed_delay.0.seconds, default_route_action.0.fault_injection_policy.0.delay.0.fixed_delay.0.nanos |
| percentage | at_least_one_of | default_route_action.0.fault_injection_policy.0.delay.0.fixed_delay, default_route_action.0.fault_injection_policy.0.delay.0.percentage |
| abort | at_least_one_of | default_route_action.0.fault_injection_policy.0.delay, default_route_action.0.fault_injection_policy.0.abort |
| httpStatus | at_least_one_of | default_route_action.0.fault_injection_policy.0.abort.0.http_status, default_route_action.0.fault_injection_policy.0.abort.0.percentage |
| percentage | at_least_one_of | default_route_action.0.fault_injection_policy.0.abort.0.http_status, default_route_action.0.fault_injection_policy.0.abort.0.percentage |

## 📦 google_compute_backend_service_signed_url_key

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/backendServices

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_compute_address

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/beta/addresses

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| name | required |  |

## 📦 google_compute_region_commitment

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/regionCommitments

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| name | required |  |
| plan | required |  |
| license | required | name: amount |

## 📦 google_compute_region_security_policy_rule

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/beta/regionSecurityPolicies/addRule

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| security_policy | required |  |
| priority | required |  |
| expression | required | name: config |
| targetRuleSet | required | name: targetRuleIds |
| operator | required |  |
| operator | required |  |
| operator | required |  |
| operator | required |  |
| action | required | name: rateLimitOptions |

## 📦 google_compute_future_reservation

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/futureReservations

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| timeWindow | required |  |
| startTime | required | name: endTime |
| vmFamily | required |  |

## 📦 google_compute_router_nat_address

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/routers

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| router | required |  |
| routerNat | required |  |
| region | required |  |
| natIps | required |  |

## 📦 google_compute_resource_policy

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| TestAccComputeResourcePolicy_withTopologyMode | required |  |
| TestAccComputeResourcePolicy_withTopologyMode | conflicts | group_placement_policy, instance_schedule_policy, disk_consistency_group_policy |
| TestAccComputeResourcePolicy_withTopologyMode | required |  |
| TestAccComputeResourcePolicy_withTopologyMode | exactly_one_of | snapshot_schedule_policy.0.schedule.0.hourly_schedule, snapshot_schedule_policy.0.schedule.0.daily_schedule, snapshot_schedule_policy.0.schedule.0.weekly_schedule |
| TestAccComputeResourcePolicy_withTopologyMode | required |  |
| TestAccComputeResourcePolicy_withTopologyMode | required |  |
| TestAccComputeResourcePolicy_withTopologyMode | exactly_one_of | snapshot_schedule_policy.0.schedule.0.hourly_schedule, snapshot_schedule_policy.0.schedule.0.daily_schedule, snapshot_schedule_policy.0.schedule.0.weekly_schedule |
| TestAccComputeResourcePolicy_withTopologyMode | required |  |
| TestAccComputeResourcePolicy_withTopologyMode | required |  |
| TestAccComputeResourcePolicy_withTopologyMode | exactly_one_of | snapshot_schedule_policy.0.schedule.0.hourly_schedule, snapshot_schedule_policy.0.schedule.0.daily_schedule, snapshot_schedule_policy.0.schedule.0.weekly_schedule |
| TestAccComputeResourcePolicy_withTopologyMode | required |  |
| TestAccComputeResourcePolicy_withTopologyMode | required |  |
| TestAccComputeResourcePolicy_withTopologyMode | required |  |
| TestAccComputeResourcePolicy_withTopologyMode | required |  |
| TestAccComputeResourcePolicy_withTopologyMode | at_least_one_of | snapshot_schedule_policy.0.snapshot_properties.0.labels, snapshot_schedule_policy.0.snapshot_properties.0.storage_locations, snapshot_schedule_policy.0.snapshot_properties.0.guest_flush, name: storageLocations |
| TestAccComputeResourcePolicy_withTopologyMode | at_least_one_of | snapshot_schedule_policy.0.snapshot_properties.0.labels, snapshot_schedule_policy.0.snapshot_properties.0.storage_locations, snapshot_schedule_policy.0.snapshot_properties.0.guest_flush |
| TestAccComputeResourcePolicy_withTopologyMode | at_least_one_of | snapshot_schedule_policy.0.snapshot_properties.0.labels, snapshot_schedule_policy.0.snapshot_properties.0.storage_locations, snapshot_schedule_policy.0.snapshot_properties.0.guest_flush, name: chainName |
| TestAccComputeResourcePolicy_withTopologyMode | conflicts | instance_schedule_policy, snapshot_schedule_policy, disk_consistency_group_policy |
| TestAccComputeResourcePolicy_withTopologyMode | conflicts | group_placement_policy.0.gpu_topology, name: gpuTopology |
| TestAccComputeResourcePolicy_withTopologyMode | conflicts | group_placement_policy.0.max_distance, name: tpuTopology |
| TestAccComputeResourcePolicy_withTopologyMode | conflicts | snapshot_schedule_policy, group_placement_policy, disk_consistency_group_policy |
| TestAccComputeResourcePolicy_withTopologyMode | at_least_one_of | instance_schedule_policy.0.vm_start_schedule, instance_schedule_policy.0.vm_stop_schedule |
| TestAccComputeResourcePolicy_withTopologyMode | required |  |
| TestAccComputeResourcePolicy_withTopologyMode | at_least_one_of | instance_schedule_policy.0.vm_start_schedule, instance_schedule_policy.0.vm_stop_schedule |
| TestAccComputeResourcePolicy_withTopologyMode | required |  |
| TestAccComputeResourcePolicy_withTopologyMode | required |  |
| TestAccComputeResourcePolicy_withTopologyMode | conflicts | snapshot_schedule_policy, group_placement_policy, instance_schedule_policy |
| TestAccComputeResourcePolicy_withTopologyMode | required |  |
| TestAccComputeResourcePolicy_withTopologyMode | required |  |
| TestAccComputeResourcePolicy_withTopologyMode | conflicts | workload_policy.0.accelerator_topology, workload_policy.0.accelerator_topology_mode |
| TestAccComputeResourcePolicy_withTopologyMode | conflicts | workload_policy.0.max_topology_distance, name: acceleratorTopologyMode |
| TestAccComputeResourcePolicy_withTopologyMode | conflicts | workload_policy.0.max_topology_distance |

## 📦 google_compute_http_health_check

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/v1/httpHealthChecks

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |

## 📦 google_compute_instance_group_membership

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/instanceGroups

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| instanceGroup | required |  |
| instance | required |  |

## 📦 google_compute_disk_type

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| zone | required |  |

## 📦 google_compute_firewall_policy_association

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/addAssociation

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| firewallPolicy | required |  |
| name | required |  |
| attachmentTarget | required |  |

## 📦 google_compute_instance_group

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| zone | required |  |

## 📦 google_compute_managed_ssl_certificate

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/sslCertificates

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| domains | required |  |

## 📦 google_compute_region_network_endpoint

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/beta/regionNetworkEndpointGroups

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| regionNetworkEndpointGroup | required |  |
| port | required |  |
| fqdn | at_least_one_of | fqdn, ip_address, name: clientDestinationPort |

## 📦 google_compute_network_firewall_policy_association

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/networkFirewallPolicies/addAssociation

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| firewallPolicy | required |  |
| name | required | name: attachmentTarget |
| attachmentTarget | required |  |

## 📦 google_compute_region_disk_resource_policy_attachment

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |

## 📦 google_compute_global_network_endpoint_group

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/beta/networkEndpointGroups

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| networkEndpointType | required |  |

## 📦 google_compute_image

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/v1/images

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| type | required |  |
| name | required | name: rawDisk |
| source | required |  |
| content | required |  |
| content | required |  |
| content | required |  |
| content | required |  |

## 📦 google_compute_region_health_check

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| name | required |  |
| httpHealthCheck | exactly_one_of | http_health_check, https_health_check, http2_health_check, tcp_health_check |
| host | at_least_one_of | http_health_check.0.host, http_health_check.0.request_path, http_health_check.0.response, http_health_check.0.port |
| requestPath | at_least_one_of | http_health_check.0.host, http_health_check.0.request_path, http_health_check.0.response, http_health_check.0.port |
| response | at_least_one_of | http_health_check.0.host, http_health_check.0.request_path, http_health_check.0.response, http_health_check.0.port |
| port | at_least_one_of | http_health_check.0.host, http_health_check.0.request_path, http_health_check.0.response, http_health_check.0.port |
| portName | at_least_one_of | http_health_check.0.host, http_health_check.0.request_path, http_health_check.0.response, http_health_check.0.port |
| proxyHeader | at_least_one_of | http_health_check.0.host, http_health_check.0.request_path, http_health_check.0.response, http_health_check.0.port |
| portSpecification | at_least_one_of | http_health_check.0.host, http_health_check.0.request_path, http_health_check.0.response, http_health_check.0.port |
| httpsHealthCheck | exactly_one_of | http_health_check, https_health_check, http2_health_check, tcp_health_check |
| host | at_least_one_of | https_health_check.0.host, https_health_check.0.request_path, https_health_check.0.response, https_health_check.0.port |
| requestPath | at_least_one_of | https_health_check.0.host, https_health_check.0.request_path, https_health_check.0.response, https_health_check.0.port |
| response | at_least_one_of | https_health_check.0.host, https_health_check.0.request_path, https_health_check.0.response, https_health_check.0.port |
| port | at_least_one_of | https_health_check.0.host, https_health_check.0.request_path, https_health_check.0.response, https_health_check.0.port |
| portName | at_least_one_of | https_health_check.0.host, https_health_check.0.request_path, https_health_check.0.response, https_health_check.0.port |
| proxyHeader | at_least_one_of | https_health_check.0.host, https_health_check.0.request_path, https_health_check.0.response, https_health_check.0.port |
| portSpecification | at_least_one_of | https_health_check.0.host, https_health_check.0.request_path, https_health_check.0.response, https_health_check.0.port |
| tcpHealthCheck | exactly_one_of | http_health_check, https_health_check, http2_health_check, tcp_health_check |
| request | at_least_one_of | tcp_health_check.0.request, tcp_health_check.0.response, tcp_health_check.0.port, tcp_health_check.0.port_name |
| response | at_least_one_of | tcp_health_check.0.request, tcp_health_check.0.response, tcp_health_check.0.port, tcp_health_check.0.port_name |
| port | at_least_one_of | tcp_health_check.0.request, tcp_health_check.0.response, tcp_health_check.0.port, tcp_health_check.0.port_name |
| portName | at_least_one_of | tcp_health_check.0.request, tcp_health_check.0.response, tcp_health_check.0.port, tcp_health_check.0.port_name |
| proxyHeader | at_least_one_of | tcp_health_check.0.request, tcp_health_check.0.response, tcp_health_check.0.port, tcp_health_check.0.port_name |
| portSpecification | at_least_one_of | tcp_health_check.0.request, tcp_health_check.0.response, tcp_health_check.0.port, tcp_health_check.0.port_name |
| sslHealthCheck | exactly_one_of | http_health_check, https_health_check, http2_health_check, tcp_health_check |
| request | at_least_one_of | ssl_health_check.0.request, ssl_health_check.0.response, ssl_health_check.0.port, ssl_health_check.0.port_name |
| response | at_least_one_of | ssl_health_check.0.request, ssl_health_check.0.response, ssl_health_check.0.port, ssl_health_check.0.port_name |
| port | at_least_one_of | ssl_health_check.0.request, ssl_health_check.0.response, ssl_health_check.0.port, ssl_health_check.0.port_name |
| portName | at_least_one_of | ssl_health_check.0.request, ssl_health_check.0.response, ssl_health_check.0.port, ssl_health_check.0.port_name |
| proxyHeader | at_least_one_of | ssl_health_check.0.request, ssl_health_check.0.response, ssl_health_check.0.port, ssl_health_check.0.port_name |
| portSpecification | at_least_one_of | ssl_health_check.0.request, ssl_health_check.0.response, ssl_health_check.0.port, ssl_health_check.0.port_name |
| http2HealthCheck | exactly_one_of | http_health_check, https_health_check, http2_health_check, tcp_health_check |
| host | at_least_one_of | http2_health_check.0.host, http2_health_check.0.request_path, http2_health_check.0.response, http2_health_check.0.port |
| requestPath | at_least_one_of | http2_health_check.0.host, http2_health_check.0.request_path, http2_health_check.0.response, http2_health_check.0.port |
| response | at_least_one_of | http2_health_check.0.host, http2_health_check.0.request_path, http2_health_check.0.response, http2_health_check.0.port |
| port | at_least_one_of | http2_health_check.0.host, http2_health_check.0.request_path, http2_health_check.0.response, http2_health_check.0.port |
| portName | at_least_one_of | http2_health_check.0.host, http2_health_check.0.request_path, http2_health_check.0.response, http2_health_check.0.port |
| proxyHeader | at_least_one_of | http2_health_check.0.host, http2_health_check.0.request_path, http2_health_check.0.response, http2_health_check.0.port |
| portSpecification | at_least_one_of | http2_health_check.0.host, http2_health_check.0.request_path, http2_health_check.0.response, http2_health_check.0.port |
| grpcHealthCheck | exactly_one_of | http_health_check, https_health_check, http2_health_check, tcp_health_check |
| port | at_least_one_of | grpc_health_check.0.port, grpc_health_check.0.port_name, grpc_health_check.0.port_specification, grpc_health_check.0.grpc_service_name |
| portName | at_least_one_of | grpc_health_check.0.port, grpc_health_check.0.port_name, grpc_health_check.0.port_specification, grpc_health_check.0.grpc_service_name |
| portSpecification | at_least_one_of | grpc_health_check.0.port, grpc_health_check.0.port_name, grpc_health_check.0.port_specification, grpc_health_check.0.grpc_service_name |
| grpcServiceName | at_least_one_of | grpc_health_check.0.port, grpc_health_check.0.port_name, grpc_health_check.0.port_specification, grpc_health_check.0.grpc_service_name |
| grpcTlsHealthCheck | exactly_one_of | http_health_check, https_health_check, http2_health_check, tcp_health_check |
| port | at_least_one_of | grpc_tls_health_check.0.port, grpc_tls_health_check.0.port_specification, grpc_tls_health_check.0.grpc_service_name, name: portSpecification |
| portSpecification | at_least_one_of | grpc_tls_health_check.0.port, grpc_tls_health_check.0.port_specification, grpc_tls_health_check.0.grpc_service_name |
| grpcServiceName | at_least_one_of | grpc_tls_health_check.0.port, grpc_tls_health_check.0.port_specification, grpc_tls_health_check.0.grpc_service_name, name: logConfig |

## 📦 google_compute_region_security_policy

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/regionSecurityPolicies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| name | required |  |
| ddosProtection | required |  |
| ddosProtection | required | name: "logLevel" |
| base | required |  |
| priority | required | name: match |
| expression | required | name: config |
| targetRuleSet | required | name: targetRuleIds |
| operator | required |  |
| operator | required |  |
| operator | required |  |
| operator | required |  |
| action | required | name: rateLimitOptions |

## 📦 google_compute_interconnect_group

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/interconnects

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| topologyCapability | required | name: physicalStructure |

## 📦 google_compute_network_endpoint_group

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/beta/networkEndpointGroups

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| zone | required |  |
| name | required |  |
| network | required |  |

## 📦 google_compute_instance_group_named_port

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/instanceGroup

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| group | required |  |
| zone | required |  |
| name | required | name: port |
| port | required |  |

## 📦 google_compute_global_network_endpoint

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/beta/networkEndpointGroups

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| globalNetworkEndpointGroup | required |  |
| port | required |  |
| fqdn | at_least_one_of | fqdn, ip_address |

## 📦 google_compute_region_resize_request

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/beta/regionInstanceGroupManagerResizeRequests

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| instanceGroupManager | required |  |
| name | required | name: description |
| resizeBy | required | name: requestedRunDuration |
| seconds | required | name: nanos |

## 📦 google_compute_external_vpn_gateway

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/externalVpnGateways

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required | name: redundancyType |

## 📦 google_compute_region_health_source

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/regionHealthSources

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| name | required |  |
| sourceType | required |  |

## 📦 google_compute_router

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/routers

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| name | required |  |
| network | conflicts | nccGateway, name: bgp |
| asn | required |  |
| range | required |  |
| name | required | name: key |
| key | required | name: nccGateway |
| nccGateway | conflicts | network, name: params |

## 📦 google_compute_region_target_https_proxy

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/regionTargetHttpsProxies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| name | required |  |
| certificateManagerCertificates | conflicts | ssl_certificates |
| sslCertificates | conflicts | certificate_manager_certificates |
| urlMap | required |  |

## 📦 google_compute_organization_security_policy_association

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/organizationSecurityPolicies/addAssociation

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| policyId | required |  |
| name | required | name: attachmentId |
| attachmentId | required | name: displayName |

## 📦 google_compute_cross_site_network

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/crossSiteNetworks

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |

## 📦 google_compute_public_advertised_prefix

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/publicAdvertisedPrefixes

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required | name: dnsVerificationIp |
| ipCidrRange | required | name: pdpScope |

## 📦 google_compute_reservation

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/reservations

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| zone | required |  |
| name | required |  |
| specificReservation | required |  |
| count | required |  |
| instanceProperties | exactly_one_of | specific_reservation.0.instance_properties, specific_reservation.0.source_instance_template |
| machineType | required |  |
| acceleratorType | required |  |
| acceleratorCount | required |  |
| diskSizeGb | required |  |
| sourceInstanceTemplate | exactly_one_of | specific_reservation.0.instance_properties, specific_reservation.0.source_instance_template, name: deleteAtTime |
| deleteAtTime | conflicts | delete_after_duration.0.seconds, delete_after_duration.0.nanos, name: deleteAfterDuration |
| seconds | conflicts | delete_at_time, name: nanos |
| nanos | conflicts | delete_at_time, name: reservationSharingPolicy |

## 📦 google_compute_firewall_policy_rule

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/addRule

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| firewallPolicy | required |  |
| priority | required | name: match |
| match | required |  |
| srcNetworkScope | conflicts | match.0.src_network_context, name: srcNetworkContext |
| srcNetworkContext | conflicts | match.0.src_network_scope |
| destNetworkScope | conflicts | match.0.src_network_context, name: destNetworkContext |
| destNetworkContext | conflicts | match.0.src_network_scope, name: layer4Configs |
| layer4Configs | required |  |
| ipProtocol | required | name: ports |
| action | required | name: securityProfileGroup |
| direction | required |  |

## 📦 google_compute_preview_feature

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/previewFeatures

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| activationStatus | required |  |
| predefinedRolloutPlan | required |  |

## 📦 google_compute_region_network_firewall_policy

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |

## 📦 google_compute_region_network_firewall_policy_rule

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/regionNetworkFirewallPolicies/addRule

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| firewallPolicy | required |  |
| priority | required | name: match |
| match | required |  |
| srcNetworkScope | conflicts | match.0.src_network_context, name: srcNetworkContext |
| srcNetworkContext | conflicts | match.0.src_network_scope |
| destNetworkScope | conflicts | match.0.src_network_context, name: destNetworkContext |
| destNetworkContext | conflicts | match.0.src_network_scope, name: layer4Configs |
| layer4Configs | required |  |
| ipProtocol | required | name: ports |
| action | required | name: securityProfileGroup |
| direction | required |  |
| targetType | required |  |
| targetForwardingRules | required |  |

## 📦 google_compute_backend_service

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/v1/backendServices

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| group | required |  |
| name | required |  |
| dryRun | required |  |
| connectTimeout | at_least_one_of | circuit_breakers.0.connect_timeout, circuit_breakers.0.max_requests_per_connection, circuit_breakers.0.max_connections, circuit_breakers.0.max_pending_requests |
| seconds | required | name: nanos |
| maxRequestsPerConnection | at_least_one_of | circuit_breakers.0.connect_timeout, circuit_breakers.0.max_requests_per_connection, circuit_breakers.0.max_connections, circuit_breakers.0.max_pending_requests |
| maxConnections | at_least_one_of | circuit_breakers.0.connect_timeout, circuit_breakers.0.max_requests_per_connection, circuit_breakers.0.max_connections, circuit_breakers.0.max_pending_requests |
| maxPendingRequests | at_least_one_of | circuit_breakers.0.connect_timeout, circuit_breakers.0.max_requests_per_connection, circuit_breakers.0.max_connections, circuit_breakers.0.max_pending_requests |
| maxRequests | at_least_one_of | circuit_breakers.0.connect_timeout, circuit_breakers.0.max_requests_per_connection, circuit_breakers.0.max_connections, circuit_breakers.0.max_pending_requests |
| maxRetries | at_least_one_of | circuit_breakers.0.connect_timeout, circuit_breakers.0.max_requests_per_connection, circuit_breakers.0.max_connections, circuit_breakers.0.max_pending_requests |
| httpCookie | at_least_one_of | consistent_hash.0.http_cookie, consistent_hash.0.http_header_name, consistent_hash.0.minimum_ring_size |
| ttl | at_least_one_of | consistent_hash.0.http_cookie.0.ttl, consistent_hash.0.http_cookie.0.name, consistent_hash.0.http_cookie.0.path |
| seconds | required | name: nanos |
| name | at_least_one_of | consistent_hash.0.http_cookie.0.ttl, consistent_hash.0.http_cookie.0.name, consistent_hash.0.http_cookie.0.path, name: path |
| path | at_least_one_of | consistent_hash.0.http_cookie.0.ttl, consistent_hash.0.http_cookie.0.name, consistent_hash.0.http_cookie.0.path, name: httpHeaderName |
| httpHeaderName | at_least_one_of | consistent_hash.0.http_cookie, consistent_hash.0.http_header_name, consistent_hash.0.minimum_ring_size, name: minimumRingSize |
| minimumRingSize | at_least_one_of | consistent_hash.0.http_cookie, consistent_hash.0.http_header_name, consistent_hash.0.minimum_ring_size |
| cacheKeyPolicy | at_least_one_of | cdn_policy.0.cache_key_policy, cdn_policy.0.signed_url_cache_max_age_sec |
| includeHost | at_least_one_of | cdn_policy.0.cache_key_policy.0.include_host, cdn_policy.0.cache_key_policy.0.include_protocol, cdn_policy.0.cache_key_policy.0.include_query_string, cdn_policy.0.cache_key_policy.0.query_string_blacklist |
| includeProtocol | at_least_one_of | cdn_policy.0.cache_key_policy.0.include_host, cdn_policy.0.cache_key_policy.0.include_protocol, cdn_policy.0.cache_key_policy.0.include_query_string, cdn_policy.0.cache_key_policy.0.query_string_blacklist |
| includeQueryString | at_least_one_of | cdn_policy.0.cache_key_policy.0.include_host, cdn_policy.0.cache_key_policy.0.include_protocol, cdn_policy.0.cache_key_policy.0.include_query_string, cdn_policy.0.cache_key_policy.0.query_string_blacklist |
| queryStringBlacklist | at_least_one_of | cdn_policy.0.cache_key_policy.0.include_host, cdn_policy.0.cache_key_policy.0.include_protocol, cdn_policy.0.cache_key_policy.0.include_query_string, cdn_policy.0.cache_key_policy.0.query_string_blacklist |
| queryStringWhitelist | at_least_one_of | cdn_policy.0.cache_key_policy.0.include_host, cdn_policy.0.cache_key_policy.0.include_protocol, cdn_policy.0.cache_key_policy.0.include_query_string, cdn_policy.0.cache_key_policy.0.query_string_blacklist |
| includeHttpHeaders | at_least_one_of | cdn_policy.0.cache_key_policy.0.include_host, cdn_policy.0.cache_key_policy.0.include_protocol, cdn_policy.0.cache_key_policy.0.include_query_string, cdn_policy.0.cache_key_policy.0.query_string_blacklist |
| includeNamedCookies | at_least_one_of | cdn_policy.0.cache_key_policy.0.include_host, cdn_policy.0.cache_key_policy.0.include_protocol, cdn_policy.0.cache_key_policy.0.include_query_string, cdn_policy.0.cache_key_policy.0.query_string_blacklist |
| signedUrlCacheMaxAgeSec | at_least_one_of | cdn_policy.0.cache_key_policy, cdn_policy.0.signed_url_cache_max_age_sec |
| headerName | required | name: connectionDraining |
| enabled | required |  |
| policy | exactly_one_of | policy, customPolicy |
| name | required |  |
| customPolicy | exactly_one_of | policy, customPolicy |
| name | required | name: data |
| name | required |  |
| dryRun | required |  |
| name | required |  |
| baseEjectionTime | at_least_one_of | outlier_detection.0.base_ejection_time, outlier_detection.0.consecutive_errors, outlier_detection.0.consecutive_gateway_failure, outlier_detection.0.enforcing_consecutive_errors |
| seconds | required | name: nanos |
| consecutiveErrors | at_least_one_of | outlier_detection.0.base_ejection_time, outlier_detection.0.consecutive_errors, outlier_detection.0.consecutive_gateway_failure, outlier_detection.0.enforcing_consecutive_errors |
| consecutiveGatewayFailure | at_least_one_of | outlier_detection.0.base_ejection_time, outlier_detection.0.consecutive_errors, outlier_detection.0.consecutive_gateway_failure, outlier_detection.0.enforcing_consecutive_errors |
| enforcingConsecutiveErrors | at_least_one_of | outlier_detection.0.base_ejection_time, outlier_detection.0.consecutive_errors, outlier_detection.0.consecutive_gateway_failure, outlier_detection.0.enforcing_consecutive_errors |
| enforcingConsecutiveGatewayFailure | at_least_one_of | outlier_detection.0.base_ejection_time, outlier_detection.0.consecutive_errors, outlier_detection.0.consecutive_gateway_failure, outlier_detection.0.enforcing_consecutive_errors |
| enforcingSuccessRate | at_least_one_of | outlier_detection.0.base_ejection_time, outlier_detection.0.consecutive_errors, outlier_detection.0.consecutive_gateway_failure, outlier_detection.0.enforcing_consecutive_errors |
| interval | at_least_one_of | outlier_detection.0.base_ejection_time, outlier_detection.0.consecutive_errors, outlier_detection.0.consecutive_gateway_failure, outlier_detection.0.enforcing_consecutive_errors |
| seconds | required | name: nanos |
| maxEjectionPercent | at_least_one_of | outlier_detection.0.base_ejection_time, outlier_detection.0.consecutive_errors, outlier_detection.0.consecutive_gateway_failure, outlier_detection.0.enforcing_consecutive_errors |
| successRateMinimumHosts | at_least_one_of | outlier_detection.0.base_ejection_time, outlier_detection.0.consecutive_errors, outlier_detection.0.consecutive_gateway_failure, outlier_detection.0.enforcing_consecutive_errors |
| successRateRequestVolume | at_least_one_of | outlier_detection.0.base_ejection_time, outlier_detection.0.consecutive_errors, outlier_detection.0.consecutive_gateway_failure, outlier_detection.0.enforcing_consecutive_errors |
| successRateStdevFactor | at_least_one_of | outlier_detection.0.base_ejection_time, outlier_detection.0.consecutive_errors, outlier_detection.0.consecutive_gateway_failure, outlier_detection.0.enforcing_consecutive_errors |
| ttl | at_least_one_of | strong_session_affinity_cookie.0.ttl, strong_session_affinity_cookie.0.name, strong_session_affinity_cookie.0.path |
| seconds | required | name: nanos |
| name | at_least_one_of | strong_session_affinity_cookie.0.ttl, strong_session_affinity_cookie.0.name, strong_session_affinity_cookie.0.path, name: path |
| path | at_least_one_of | strong_session_affinity_cookie.0.ttl, strong_session_affinity_cookie.0.name, strong_session_affinity_cookie.0.path, name: timeoutSec |
| enable | at_least_one_of | log_config.0.enable, log_config.0.sample_rate, name: sampleRate |
| sampleRate | at_least_one_of | log_config.0.enable, log_config.0.sample_rate |
| optionalMode | at_least_one_of | log_config.0.enable, log_config.0.sample_rate, log_config.0.optional_mode |
| dnsName | exactly_one_of | tlsSettings.0.uniform_resource_identifier, tlsSettings.0.dns_name, name: uniformResourceIdentifier |
| uniformResourceIdentifier | exactly_one_of | tlsSettings.0.uniform_resource_identifier, tlsSettings.0.dns_name, name: authenticationConfig |
| seconds | required | name: nanos |

## 📦 google_compute_target_http_proxy

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/v1/targetHttpProxies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required | name: urlMap |
| urlMap | required |  |

## 📦 google_compute_disk

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/v1/disks

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| zone | required |  |
| name | required |  |
| enableConfidentialCompute | required |  |
| provisionedIops | required |  |
| disk | required | name: architecture |
| type | required | name: licenses |
| storagePool | required |  |
| accessMode | required |  |

## 📦 google_compute_instance_group_manager

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| zone | required |  |
| baseInstanceName | required | name: instanceGroupManagerId |
| instanceTemplate | required |  |
| name | required |  |

## 📦 google_compute_target_https_proxy

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/v1/targetHttpsProxies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| certificateManagerCertificates | conflicts | ssl_certificates |
| sslCertificates | conflicts | certificate_manager_certificates |
| urlMap | required |  |

## 📦 google_compute_node_template

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/nodeTemplates

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| name | required | name: nodeAffinityLabels |
| nodeType | conflicts | node_type_flexibility, name: nodeTypeFlexibility |
| nodeTypeFlexibility | conflicts | node_type |
| cpus | at_least_one_of | node_type_flexibility.0.cpus, node_type_flexibility.0.memory, name: memory |
| memory | at_least_one_of | node_type_flexibility.0.cpus, node_type_flexibility.0.memory, name: localSsd |
| type | required |  |

## 📦 google_compute_https_health_check

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/v1/httpsHealthChecks

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |

## 📦 google_lustre_instance

🔗 **API Reference**: https://cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.instances

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_workbench_instance

🔗 **API Reference**: https://cloud.google.com/vertex-ai/docs/workbench/reference/rest/v2/projects.locations.instances

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| vmImage | conflicts | gce_setup.0.container_image |
| containerImage | conflicts | gce_setup.0.vm_image |
| repository | required | name: tag |
| externalIp | required |  |

## 📦 google_containerattached_cluster

🔗 **API Reference**: https://cloud.google.com/anthos/clusters/docs/multi-cloud/reference/rest

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| oidcConfig | required |  |
| issuerUrl | required |  |
| platformVersion | required | name: distribution |
| distribution | required |  |
| fleet | required |  |
| project | required |  |
| name | required | name: namespace |
| namespace | required | name: securityPostureConfig |
| vulnerabilityMode | required |  |

## 📦 google_networkconnectivity_gateway_advertised_route

🔗 **API Reference**: https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.spokes.gatewayAdvertisedRoutes

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| spoke | required |  |
| name | required |  |

## 📦 google_networkconnectivity_regional_endpoint

🔗 **API Reference**: https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.regionalEndpoints

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| location | required |  |
| targetGoogleApi | required | name: network |
| accessType | required |  |

## 📦 google_networkconnectivity_multicloud_data_transfer_config

🔗 **API Reference**: https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.multicloudDataTransferConfigs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| service_name | required | name: states |

## 📦 google_networkconnectivity_destination

🔗 **API Reference**: https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.multicloudDataTransferConfigs.destinations

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| multicloudDataTransferConfig | required |  |
| location | required |  |
| name | required |  |
| ipPrefix | required |  |
| endpoints | required |  |
| asn | required |  |
| csp | required |  |

## 📦 google_networkconnectivity_transport

🔗 **API Reference**: https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.transport

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| name | required |  |
| remoteProfile | required |  |
| network | required | name: advertisedRoutes |

## 📦 google_networkconnectivity_spoke

🔗 **API Reference**: https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.spokes

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| hub | required |  |
| linkedVpnTunnels | conflicts | linked_interconnect_attachments, linked_router_appliance_instances, linked_vpc_network, linked_producer_vpc_network |
| uris | required |  |
| siteToSiteDataTransfer | required |  |
| linkedInterconnectAttachments | conflicts | linked_vpn_tunnels, linked_router_appliance_instances, linked_vpc_network, linked_producer_vpc_network |
| uris | required |  |
| siteToSiteDataTransfer | required |  |
| linkedRouterApplianceInstances | conflicts | linked_interconnect_attachments, linked_vpn_tunnels, linked_vpc_network, linked_producer_vpc_network |
| instances | required |  |
| virtualMachine | required |  |
| ipAddress | required | name: siteToSiteDataTransfer |
| siteToSiteDataTransfer | required |  |
| linkedVpcNetwork | conflicts | linked_interconnect_attachments, linked_router_appliance_instances, linked_vpn_tunnels, linked_producer_vpc_network |
| uri | required |  |
| includeExportRanges | conflicts | linked_interconnect_attachments, linked_router_appliance_instances, linked_vpn_tunnels, linked_vpc_network |
| includeExportRanges | required |  |
| includeExportRanges | required |  |
| includeExportRanges | conflicts | linked_interconnect_attachments, linked_router_appliance_instances, linked_vpn_tunnels, linked_vpc_network |
| includeExportRanges | required |  |
| includeExportRanges | required |  |
| includeExportRanges | required |  |
| state | exactly_one_of | STATE_UNSPECIFIED, CREATING, ACTIVE, DELETING |

## 📦 google_networkconnectivity_group

🔗 **API Reference**: https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.hubs.groups

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| hub | required |  |
| hub | required |  |
| hub | exactly_one_of | CREATING, ACTIVE, DELETING, name: autoAccept |
| hub | required |  |

## 📦 google_networkconnectivity_hub

🔗 **API Reference**: https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.hubs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| state | exactly_one_of | STATE_UNSPECIFIED, CREATING, ACTIVE, DELETING |

## 📦 google_networkconnectivity_policy_based_route

🔗 **API Reference**: https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.policyBasedRoutes

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required | name: description |
| network | required | name: filter |
| filter | required |  |
| protocolVersion | required |  |
| nextHopOtherRoutes | exactly_one_of | next_hop_ilb_ip, next_hop_other_routes |
| nextHopIlbIp | exactly_one_of | next_hop_ilb_ip, next_hop_other_routes, name: priority |
| virtualMachine | conflicts | interconnect_attachment |
| tags | required |  |
| interconnectAttachment | conflicts | virtual_machine |
| region | required | name: createTime |

## 📦 google_eventarc_channel

🔗 **API Reference**: https://cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.channels

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |

## 📦 google_eventarc_enrollment

🔗 **API Reference**: https://cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.enrollments

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: enrollmentId |
| None | required |  |
| None | required |  |
| None | required | name: destination |
| None | required | name: uid |

## 📦 google_eventarc_google_channel_config

🔗 **API Reference**: https://cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |

## 📦 google_eventarc_trigger

🔗 **API Reference**: https://cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.triggers

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required | name: path |
| None | required | name: location |
| None | required | name: namespace |
| None | required | name: service |
| None | required | name: path |
| None | required | name: networkConfig |
| None | required | name: transport |

## 📦 google_eventarc_google_api_source

🔗 **API Reference**: https://cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.googleApiSources

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: googleApiSourceId |
| None | required |  |
| None | required | name: loggingConfig |

## 📦 google_eventarc_pipeline

🔗 **API Reference**: https://cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.pipelines

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: pipelineId |
| None | required |  |
| None | required |  |
| None | required | name: audience |
| None | required | name: scope |
| None | required | name: messageBindingTemplate |

## 📦 google_eventarc_message_bus

🔗 **API Reference**: https://cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.messageBuses

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: messageBusId |
| None | required |  |

## 📦 google_billingbudget_budget

🔗 **API Reference**: https://cloud.google.com/billing/docs/reference/budget/rest/v1/billingAccounts.budgets

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| billingAccount | required |  |
| projects | at_least_one_of | budget_filter.0.projects, budget_filter.0.resource_ancestors, budget_filter.0.credit_types_treatment, budget_filter.0.services |
| resourceAncestors | at_least_one_of | budget_filter.0.projects, budget_filter.0.resource_ancestors, budget_filter.0.credit_types_treatment, budget_filter.0.services |
| creditTypesTreatment | at_least_one_of | budget_filter.0.projects, budget_filter.0.resource_ancestors, budget_filter.0.credit_types_treatment, budget_filter.0.services |
| services | at_least_one_of | budget_filter.0.projects, budget_filter.0.resource_ancestors, budget_filter.0.credit_types_treatment, budget_filter.0.services |
| creditTypes | at_least_one_of | budget_filter.0.projects, budget_filter.0.resource_ancestors, budget_filter.0.credit_types_treatment, budget_filter.0.services |
| subaccounts | at_least_one_of | budget_filter.0.projects, budget_filter.0.resource_ancestors, budget_filter.0.credit_types_treatment, budget_filter.0.services |
| labels | at_least_one_of | budget_filter.0.projects, budget_filter.0.resource_ancestors, budget_filter.0.credit_types_treatment, budget_filter.0.services |
| calendarPeriod | at_least_one_of | budget_filter.0.projects, budget_filter.0.resource_ancestors, budget_filter.0.credit_types_treatment, budget_filter.0.services |
| customPeriod | at_least_one_of | budget_filter.0.projects, budget_filter.0.resource_ancestors, budget_filter.0.credit_types_treatment, budget_filter.0.services |
| startDate | required |  |
| year | required |  |
| month | required |  |
| day | required |  |
| year | required |  |
| month | required |  |
| day | required |  |
| amount | required |  |
| specifiedAmount | exactly_one_of | amount.0.specified_amount, amount.0.last_period_amount |
| lastPeriodAmount | exactly_one_of | amount.0.specified_amount, amount.0.last_period_amount |
| thresholdPercent | required |  |
| pubsubTopic | at_least_one_of | all_updates_rule.0.pubsub_topic, all_updates_rule.0.monitoring_notification_channels, name: schemaVersion |
| monitoringNotificationChannels | at_least_one_of | all_updates_rule.0.pubsub_topic, all_updates_rule.0.monitoring_notification_channels |

## 📦 google_siteverification_web_resource

🔗 **API Reference**: https://developers.google.com/site-verification/v1

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| verification_method | required |  |
| site | required |  |
| type | required |  |
| identifier | required | name: owners |

## 📦 google_identityplatform_default_supported_idp_config

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| idpId | required |  |
| clientId | required | name: clientSecret |
| clientSecret | required | name: enabled |

## 📦 google_identityplatform_tenant

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| displayName | required | name: allowPasswordSignup |

## 📦 google_identityplatform_oauth_idp_config

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| issuer | required | name: clientId |
| clientId | required | name: clientSecret |

## 📦 google_identityplatform_config

🔗 **API Reference**: https://cloud.google.com/identity-platform/docs/reference/rest/v2/Config

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| enabled | required | name: passwordRequired |
| enabled | required | name: testPhoneNumbers |
| enabled | required |  |
| triggers | required |  |
| functionUri | required | name: updateTime |
| allowByDefault | exactly_one_of | sms_region_config.0.allow_by_default, sms_region_config.0.allowlist_only |
| allowlistOnly | exactly_one_of | sms_region_config.0.allow_by_default, sms_region_config.0.allowlist_only |

## 📦 google_identityplatform_inbound_saml_config

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| displayName | required | name: enabled |
| idpConfig | required |  |
| idpEntityId | required | name: ssoUrl |
| ssoUrl | required | name: signRequest |
| idpCertificates | required |  |
| spConfig | required |  |

## 📦 google_identityplatform_tenant_default_supported_idp_config

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| idpId | required |  |
| tenant | required |  |
| clientId | required | name: clientSecret |
| clientSecret | required | name: enabled |

## 📦 google_identityplatform_tenant_inbound_saml_config

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| tenant | required |  |
| displayName | required | name: enabled |
| idpConfig | required |  |
| idpEntityId | required | name: ssoUrl |
| ssoUrl | required | name: signRequest |
| idpCertificates | required |  |
| spConfig | required |  |
| spEntityId | required | name: callbackUri |
| callbackUri | required | name: spCertificates |

## 📦 google_identityplatform_tenant_oauth_idp_config

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| tenant | required |  |
| displayName | required | name: enabled |
| issuer | required | name: clientId |
| clientId | required | name: clientSecret |

## 📦 google_edgenetwork_interconnect_attachment

🔗 **API Reference**: https://cloud.google.com/distributed-cloud/edge/latest/docs/reference/network/rest/v1/projects.locations.zones.interconnectAttachments

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| zone | required |  |
| interconnect_attachment_id | required |  |
| labels | required | name: description |
| description | required | name: createTime |
| interconnect | required | name: network |
| network | required |  |
| vlanId | required | name: mtu |

## 📦 google_edgenetwork_subnet

🔗 **API Reference**: https://cloud.google.com/distributed-cloud/edge/latest/docs/reference/network/rest/v1/projects.locations.zones.subnets

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| zone | required |  |
| subnet_id | required |  |
| labels | required | name: description |
| description | required | name: createTime |
| network | required |  |

## 📦 google_edgenetwork_network

🔗 **API Reference**: https://cloud.google.com/distributed-cloud/edge/latest/docs/reference/network/rest/v1/projects.locations.zones.networks

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| zone | required |  |
| network_id | required |  |
| labels | required | name: description |
| description | required | name: createTime |

## 📦 google_iamworkforcepool_workforce_pool_provider_key

🔗 **API Reference**: https://cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| workforcePoolId | required |  |
| providerId | required |  |
| keyId | required |  |
| keyData | required |  |
| keySpec | required |  |
| use | required |  |

## 📦 google_iamworkforcepool_workforce_pool_provider_scim_token

🔗 **API Reference**: https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| workforcePoolId | required |  |
| providerId | required |  |
| scimTenantId | required |  |
| scimTokenId | required |  |

## 📦 google_iamworkforcepool_workforce_pool_provider_scim_tenant

🔗 **API Reference**: https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| workforcePoolId | required |  |
| providerId | required |  |
| scimTenantId | required |  |

## 📦 google_iamworkforcepool_workforce_pool

🔗 **API Reference**: https://cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| workforcePoolId | required |  |
| parent | required |  |

## 📦 google_iamworkforcepool_workforce_pool_provider

🔗 **API Reference**: https://cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | exactly_one_of | saml, oidc |
| None | required |  |
| None | exactly_one_of | saml, oidc |
| None | required |  |
| None | required |  |
| None | exactly_one_of | oidc.0.client_secret.0.value |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | exactly_one_of | extraAttributesOauth2Client.0.client_secret.0.value |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_iamworkforcepool_oauth_client

🔗 **API Reference**: https://cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: oauthClientId |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_iamworkforcepool_oauth_client_credential

🔗 **API Reference**: https://cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: oauthclient |
| None | required | name: oauthClientCredentialId |
| None | required |  |

## 📦 google_dlp_deidentify_template

🔗 **API Reference**: https://cloud.google.com/dlp/docs/reference/rest/v2/projects.deidentifyTemplates

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parent | required |  |
| deidentifyConfig | required |  |
| imageTransformations | exactly_one_of | deidentify_config.0.info_type_transformations, deidentify_config.0.record_transformations, deidentify_config.0.image_transformations |
| transforms | required |  |
| infoTypes | required |  |
| name | required | name: version |
| score | required |  |
| infoTypeTransformations | exactly_one_of | deidentify_config.0.info_type_transformations, deidentify_config.0.record_transformations, deidentify_config.0.image_transformations |
| transformations | required |  |
| name | required | name: version |
| score | required |  |
| primitiveTransformation | required |  |
| newValue | required |  |
| name | required | name: unwrapped |
| key | required | name: kmsWrapped |
| wrappedKey | required | name: cryptoKeyName |
| cryptoKeyName | required | name: surrogateInfoType |
| score | required |  |
| name | required | name: unwrapped |
| key | required | name: kmsWrapped |
| wrappedKey | required | name: cryptoKeyName |
| cryptoKeyName | required | name: context |
| score | required |  |
| wordList | required |  |
| words | required |  |
| name | required | name: cryptoKey |
| name | required | name: unwrapped |
| key | required | name: kmsWrapped |
| wrappedKey | required | name: cryptoKeyName |
| cryptoKeyName | required | name: upperBoundDays |
| upperBoundDays | required | name: lowerBoundDays |
| lowerBoundDays | required | name: fixedSizeBucketingConfig |
| lowerBound | required |  |
| upperBound | required |  |
| bucketSize | required | name: bucketingConfig |
| replacementValue | required |  |
| name | required | name: unwrapped |
| key | required | name: kmsWrapped |
| wrappedKey | required | name: cryptoKeyName |
| cryptoKeyName | required | name: recordTransformations |
| recordTransformations | exactly_one_of | deidentify_config.0.info_type_transformations, deidentify_config.0.record_transformations, deidentify_config.0.image_transformations |
| fieldTransformations | at_least_one_of | deidentify_config.0.record_transformations.0.field_transformations, deidentify_config.0.record_transformations.0.record_suppressions |
| fields | required |  |
| field | required |  |
| operator | required |  |
| newValue | required |  |
| name | required | name: unwrapped |
| key | required | name: kmsWrapped |
| wrappedKey | required | name: cryptoKeyName |
| cryptoKeyName | required | name: context |
| score | required |  |
| lowerBound | required |  |
| upperBound | required |  |
| bucketSize | required | name: bucketingConfig |
| replacementValue | required |  |
| name | required | name: unwrapped |
| key | required | name: kmsWrapped |
| wrappedKey | required | name: cryptoKeyName |
| cryptoKeyName | required | name: dateShiftConfig |
| upperBoundDays | required | name: lowerBoundDays |
| lowerBoundDays | required | name: context |
| name | required | name: unwrapped |
| key | required | name: kmsWrapped |
| wrappedKey | required | name: cryptoKeyName |
| cryptoKeyName | required | name: cryptoDeterministicConfig |
| name | required | name: unwrapped |
| key | required | name: kmsWrapped |
| wrappedKey | required | name: cryptoKeyName |
| cryptoKeyName | required | name: surrogateInfoType |
| score | required |  |
| words | required |  |
| transformations | required |  |
| name | required | name: version |
| score | required |  |
| primitiveTransformation | required |  |
| newValue | required |  |
| cryptoKey | required |  |
| name | required | name: unwrapped |
| key | required |  |
| wrappedKey | required | name: cryptoKeyName |
| cryptoKeyName | required | name: context |
| name | required | name: surrogateInfoType |
| name | required | name: version |
| score | required |  |
| lowerBound | required |  |
| upperBound | required |  |
| bucketSize | required | name: bucketingConfig |
| buckets | required |  |
| replacementValue | required |  |
| partToExtract | required |  |
| cryptoKey | required |  |
| name | required | name: unwrapped |
| key | required |  |
| wrappedKey | required | name: cryptoKeyName |
| cryptoKeyName | required | name: dateShiftConfig |
| upperBoundDays | required | name: lowerBoundDays |
| lowerBoundDays | required | name: context |
| name | required | name: cryptoKey |
| name | required | name: unwrapped |
| key | required |  |
| wrappedKey | required | name: cryptoKeyName |
| cryptoKeyName | required | name: cryptoDeterministicConfig |
| cryptoKey | required |  |
| name | required | name: unwrapped |
| key | required |  |
| wrappedKey | required | name: cryptoKeyName |
| cryptoKeyName | required | name: surrogateInfoType |
| surrogateInfoType | required |  |
| name | required | name: version |
| score | required |  |
| name | required | name: replaceDictionaryConfig |
| wordList | required |  |
| words | required |  |
| recordSuppressions | at_least_one_of | deidentify_config.0.record_transformations.0.field_transformations, deidentify_config.0.record_transformations.0.record_suppressions |
| field | required |  |
| operator | required |  |

## 📦 google_dlp_stored_info_type

🔗 **API Reference**: https://cloud.google.com/dlp/docs/reference/rest/v2/projects.storedInfoTypes

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parent | required |  |
| regex | exactly_one_of | dictionary, regex, large_custom_dictionary |
| pattern | required | name: groupIndexes |
| dictionary | exactly_one_of | dictionary, regex, large_custom_dictionary |
| wordList | exactly_one_of | dictionary.0.word_list, dictionary.0.cloud_storage_path |
| words | required |  |
| cloudStoragePath | exactly_one_of | dictionary.0.word_list, dictionary.0.cloud_storage_path |
| path | required | name: largeCustomDictionary |
| largeCustomDictionary | exactly_one_of | dictionary, regex, large_custom_dictionary |
| outputPath | required |  |
| path | required | name: cloudStorageFileSet |
| cloudStorageFileSet | exactly_one_of | large_custom_dictionary.0.cloud_storage_file_set, large_custom_dictionary.0.big_query_field |
| url | required | name: bigQueryField |
| bigQueryField | exactly_one_of | large_custom_dictionary.0.cloud_storage_file_set, large_custom_dictionary.0.big_query_field |
| table | required |  |
| projectId | required | name: datasetId |
| datasetId | required | name: tableId |
| tableId | required | name: field |
| field | required |  |
| name | required |  |

## 📦 google_dlp_discovery_config

🔗 **API Reference**: https://cloud.google.com/dlp/docs/reference/rest/v2/projects.locations.discoveryConfigs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parent | required |  |
| location | required |  |
| accountId | conflicts | other_cloud_starting_location.aws_location.all_assets_inventory_assets |
| allAssetInventoryAssets | conflicts | other_cloud_starting_location.aws_location.account_id |
| score | required |  |
| datasetId | required | name: tableId |
| tableId | required | name: conditions |
| filter | required |  |
| projectId | required | name: instance |
| instance | required | name: database |
| database | required | name: databaseResource |
| databaseResource | required | name: conditions |
| frequency | required |  |
| filter | required |  |
| namespacedTagValue | conflicts | targets.cloud_storage_target.filter.collection.include_tags.tag_filters.namespaced_tag_key, name: namespacedTagKey |
| namespacedTagKey | conflicts | targets.cloud_storage_target.filter.collection.include_tags.tag_filters.namespaced_tag_value, name: cloudStorageResourceReference |
| filter | required |  |

## 📦 google_dlp_inspect_template

🔗 **API Reference**: https://cloud.google.com/dlp/docs/reference/rest/v2/projects.inspectTemplates

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parent | required |  |
| maxFindingsPerItem | required | name: maxFindingsPerRequest |
| maxFindingsPerRequest | required | name: maxFindingsPerInfoType |
| name | required | name: version |
| score | required |  |
| maxFindings | required | name: infoTypes |
| name | required | name: version |
| score | required |  |
| infoTypes | required |  |
| name | required | name: version |
| score | required |  |
| rules | required |  |
| hotwordRegex | required |  |
| pattern | required | name: groupIndexes |
| proximity | required |  |
| likelihoodAdjustment | required |  |
| matchingType | required |  |
| words | required |  |
| path | required | name: regex |
| pattern | required | name: groupIndexes |
| infoTypes | required |  |
| name | required | name: version |
| score | required |  |
| hotwordRegex | required |  |
| pattern | required | name: groupIndexes |
| proximity | required |  |
| infoType | required |  |
| name | required | name: version |
| score | required |  |
| score | required |  |
| pattern | required | name: groupIndexes |
| words | required |  |
| path | required | name: surrogateType |
| name | required |  |

## 📦 google_dlp_job_trigger

🔗 **API Reference**: https://cloud.google.com/dlp/docs/reference/rest/v2/projects.jobTriggers

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parent | required |  |
| triggers | required |  |
| maxFindingsPerItem | at_least_one_of | inspect_job.0.inspect_config.0.limits.0.max_findings_per_item, inspect_job.0.inspect_config.0.limits.0.max_findings_per_request, inspect_job.0.inspect_config.0.limits.0.max_findings_per_info_type, name: maxFindingsPerRequest |
| maxFindingsPerRequest | at_least_one_of | inspect_job.0.inspect_config.0.limits.0.max_findings_per_item, inspect_job.0.inspect_config.0.limits.0.max_findings_per_request, inspect_job.0.inspect_config.0.limits.0.max_findings_per_info_type, name: maxFindingsPerInfoType |
| maxFindingsPerInfoType | at_least_one_of | inspect_job.0.inspect_config.0.limits.0.max_findings_per_item, inspect_job.0.inspect_config.0.limits.0.max_findings_per_request, inspect_job.0.inspect_config.0.limits.0.max_findings_per_info_type |
| name | required | name: version |
| score | required |  |
| name | required | name: version |
| score | required |  |
| name | required | name: version |
| score | required |  |
| rules | required |  |
| matchingType | required |  |
| words | required |  |
| path | required | name: regex |
| pattern | required | name: groupIndexes |
| infoTypes | required |  |
| name | required | name: version |
| score | required |  |
| infoType | required |  |
| name | required | name: version |
| score | required |  |
| score | required |  |
| pattern | required | name: groupIndexes |
| words | required |  |
| path | required | name: storedType |
| name | required | name: createTime |
| storageConfig | required |  |
| startTime | conflicts | inspect_job.0.storage_config.0.timespan_config.0.enable_auto_population_of_timespan_config |
| startTime | at_least_one_of | inspect_job.0.storage_config.0.timespan_config.0.start_time, inspect_job.0.storage_config.0.timespan_config.0.end_time, inspect_job.0.storage_config.0.timespan_config.0.enable_auto_population_of_timespan_config, name: endTime |
| endTime | at_least_one_of | inspect_job.0.storage_config.0.timespan_config.0.start_time, inspect_job.0.storage_config.0.timespan_config.0.end_time, inspect_job.0.storage_config.0.timespan_config.0.enable_auto_population_of_timespan_config, name: enableAutoPopulationOfTimespanConfig |
| enableAutoPopulationOfTimespanConfig | conflicts | inspect_job.0.storage_config.0.timespan_config.0.start_time |
| enableAutoPopulationOfTimespanConfig | at_least_one_of | inspect_job.0.storage_config.0.timespan_config.0.start_time, inspect_job.0.storage_config.0.timespan_config.0.end_time, inspect_job.0.storage_config.0.timespan_config.0.enable_auto_population_of_timespan_config, name: timestampField |
| name | required | name: datastoreOptions |
| partitionId | required |  |
| projectId | required | name: namespaceId |
| kind | required |  |
| name | required | name: cloudStorageOptions |
| fileSet | required |  |
| url | exactly_one_of | inspect_job.0.storage_config.0.cloud_storage_options.0.file_set.0.url, inspect_job.0.storage_config.0.cloud_storage_options.0.file_set.0.regex_file_set, name: regexFileSet |
| regexFileSet | exactly_one_of | inspect_job.0.storage_config.0.cloud_storage_options.0.file_set.0.url, inspect_job.0.storage_config.0.cloud_storage_options.0.file_set.0.regex_file_set |
| bucketName | required | name: includeRegex |
| tableReference | required |  |
| projectId | required | name: datasetId |
| datasetId | required | name: tableId |
| tableId | required | name: rowsLimit |
| name | required | name: includedFields |
| name | required | name: excludedFields |
| name | required | name: hybridOptions |
| name | required | name: labels |
| saveFindings | exactly_one_of |  |
| outputConfig | required |  |
| projectId | required | name: datasetId |
| datasetId | required | name: tableId |
| path | required | name: outputSchema |
| pubSub | exactly_one_of |  |
| topic | required | name: publishSummaryToCscc |
| publishSummaryToCscc | exactly_one_of |  |
| publishFindingsToDataplexCatalog | exactly_one_of |  |
| publishFindingsToCloudDataCatalog | exactly_one_of |  |
| jobNotificationEmails | exactly_one_of |  |
| deidentify | exactly_one_of |  |
| cloudStorageOutput | required | name: fileTypesToTransform |
| table | required |  |
| datasetId | required | name: projectId |
| projectId | required | name: tableId |
| publishToStackdriver | exactly_one_of |  |

## 📦 google_containeranalysis_note

🔗 **API Reference**: https://cloud.google.com/container-analysis/api/reference/rest/

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| url | required | name: label |
| attestationAuthority | required |  |
| hint | required |  |
| humanReadableName | required |  |

## 📦 google_containeranalysis_occurrence

🔗 **API Reference**: https://cloud.google.com/container-analysis/api/reference/rest/

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| resourceUri | required |  |
| noteName | required |  |
| attestation | required |  |
| serializedPayload | required | name: signatures |
| signatures | required |  |
| publicKeyId | required |  |

## 📦 google_osconfigv2_policy_orchestrator_for_organization

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: policyOrchestratorId |
| None | required |  |
| None | required | name: orchestratedResource |
| None | required |  |
| None | required |  |
| None | required | name: description |
| None | required | name: resourceGroups |
| None | required |  |
| None | required | name: osVersion |
| None | required |  |
| None | required |  |
| None | required | name: object |
| None | required | name: generation |
| None | required | name: sha256Checksum |
| None | required | name: outputFilePath |
| None | required | name: sha256Checksum |
| None | required | name: object |
| None | required | name: localPath |
| None | required | name: outputFilePath |
| None | required | name: generation |
| None | required | name: localPath |
| None | required | name: sha256Checksum |
| None | required | name: state |
| None | required | name: permissions |
| None | required | name: pkg |
| None | required |  |
| None | required | name: sha256Checksum |
| None | required | name: object |
| None | required | name: generation |
| None | required | name: apt |
| None | required | name: deb |
| None | required |  |
| None | required | name: sha256Checksum |
| None | required | name: object |
| None | required | name: generation |
| None | required | name: zypper |
| None | required | name: rpm |
| None | required |  |
| None | required | name: sha256Checksum |
| None | required | name: object |
| None | required | name: generation |
| None | required | name: repository |
| None | required | name: gpgKeys |
| None | required | name: zypper |
| None | required | name: displayName |
| None | required | name: gpgKeys |
| None | required | name: name |
| None | required | name: apt |
| None | required | name: uri |
| None | required | name: distribution |
| None | required | name: components |
| None | required |  |
| None | required |  |
| None | required | name: osVersion |
| None | required |  |
| None | required |  |
| None | required | name: revisionCreateTime |

## 📦 google_osconfigv2_policy_orchestrator

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required | name: orchestratedResource |
| None | required |  |
| None | required |  |
| None | required | name: resourceGroups |
| None | required |  |
| None | required | name: osVersion |
| None | required |  |
| None | required | name: displayName |
| None | required | name: gpgKeys |
| None | required | name: displayName |
| None | required | name: gpgKeys |
| None | required | name: url |
| None | required | name: apt |
| None | required | name: distribution |
| None | required | name: components |
| None | required |  |
| None | required | name: exec |
| None | required | name: outputFilePath |
| None | required | name: sha256Checksum |
| None | required | name: object |
| None | required | name: generation |
| None | required |  |
| None | required | name: object |
| None | required | name: generation |
| None | required | name: sha256Checksum |
| None | required | name: outputFilePath |
| None | required | name: sha256Checksum |
| None | required | name: generation |
| None | required | name: localPath |
| None | required | name: state |
| None | required | name: permissions |
| None | required | name: pkg |
| None | required |  |
| None | required | name: object |
| None | required | name: localPath |
| None | required | name: sha256Checksum |
| None | required | name: apt |
| None | required | name: deb |
| None | required |  |
| None | required | name: sha256Checksum |
| None | required | name: object |
| None | required | name: generation |
| None | required | name: zypper |
| None | required | name: rpm |
| None | required |  |
| None | required | name: sha256Checksum |
| None | required | name: object |
| None | required | name: localPath |
| None | required | name: allowNoResourceGroupMatch |
| None | required | name: description |
| None | required |  |
| None | required | name: osVersion |
| None | required |  |
| None | required |  |
| None | required | name: revisionCreateTime |

## 📦 google_osconfigv2_policy_orchestrator_for_folder

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: policyOrchestratorId |
| None | required |  |
| None | required | name: orchestratedResource |
| None | required |  |
| None | required |  |
| None | required | name: description |
| None | required | name: resourceGroups |
| None | required |  |
| None | required | name: osVersion |
| None | required |  |
| None | required | name: pkg |
| None | required | name: msi |
| None | required |  |
| None | required | name: sha256Checksum |
| None | required | name: object |
| None | required | name: generation |
| None | required | name: apt |
| None | required | name: deb |
| None | required |  |
| None | required | name: gcs |
| None | required | name: object |
| None | required | name: localPath |
| None | required | name: zypper |
| None | required | name: rpm |
| None | required |  |
| None | required | name: sha256Checksum |
| None | required | name: object |
| None | required | name: generation |
| None | required |  |
| None | required | name: uri |
| None | required | name: distribution |
| None | required | name: yum |
| None | required | name: gpgKeys |
| None | required | name: zypper |
| None | required | name: gpgKeys |
| None | required | name: displayName |
| None | required | name: url |
| None | required | name: exec |
| None | required |  |
| None | required | name: outputFilePath |
| None | required | name: sha256Checksum |
| None | required | name: object |
| None | required | name: generation |
| None | required | name: outputFilePath |
| None | required | name: sha256Checksum |
| None | required | name: object |
| None | required | name: generation |
| None | required | name: sha256Checksum |
| None | required | name: object |
| None | required | name: generation |
| None | required | name: state |
| None | required | name: permissions |
| None | required |  |
| None | required | name: osVersion |
| None | required |  |
| None | required |  |
| None | required | name: revisionCreateTime |

## 📦 google_cloudtasks_queue

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| samplingRatio | required | name: state |
| header | required |  |
| key | required | name: value |
| value | required | name: oauthToken |
| oauthToken | conflicts | oidcToken |
| serviceAccountEmail | required | name: scope |
| oidcToken | conflicts | oauthToken |
| serviceAccountEmail | required | name: audience |

## 📦 google_secretmanagerregional_regional_secret

🔗 **API Reference**: https://cloud.google.com/secret-manager/docs/reference/rest/v1/projects.locations.secrets

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| secretId | required |  |
| kmsKeyName | required | name: topics |
| name | required | name: rotation |

## 📦 google_secretmanagerregional_regional_secret_version

🔗 **API Reference**: https://cloud.google.com/secret-manager/docs/reference/rest/v1/projects.locations.secrets.versions

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| secret | required |  |
| payload | required |  |
| secret_data | required |  |

## 📦 google_colab_runtime

🔗 **API Reference**: https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.notebookRuntimes

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| notebookRuntimeTemplate | required |  |
| runtimeUser | required |  |
| displayName | required | name: description |

## 📦 google_colab_notebook_execution

🔗 **API Reference**: https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.notebookExecutionJobs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| displayName | required | name: dataformRepositorySource |
| dataformRepositorySource | exactly_one_of | dataform_repository_source, gcs_notebook_source, direct_notebook_source |
| dataformRepositoryResourceName | required |  |
| gcsNotebookSource | exactly_one_of | dataform_repository_source, gcs_notebook_source, direct_notebook_source |
| uri | required | name: generation |
| directNotebookSource | exactly_one_of | dataform_repository_source, gcs_notebook_source, direct_notebook_source |
| content | required |  |
| notebookRuntimeTemplateResourceName | exactly_one_of | notebook_runtime_template_resource_name, custom_environment_spec, name: customEnvironmentSpec |
| notebookRuntimeTemplateResourceName | exactly_one_of | notebook_runtime_template_resource_name, custom_environment_spec |
| gcsOutputUri | required |  |
| executionUser | exactly_one_of | execution_user, service_account |
| serviceAccount | exactly_one_of | execution_user, service_account |

## 📦 google_colab_schedule

🔗 **API Reference**: https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.schedules

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| displayName | required | name: startTime |
| cron | required | name: maxConcurrentRunCount |
| maxConcurrentRunCount | required |  |
| createNotebookExecutionJobRequest | required |  |
| notebookExecutionJob | required |  |
| displayName | required | name: dataformRepositorySource |
| dataformRepositorySource | exactly_one_of | create_notebook_execution_job_request.0.notebook_execution_job.0.dataform_repository_source, create_notebook_execution_job_request.0.notebook_execution_job.0.gcs_notebook_source |
| dataformRepositoryResourceName | required |  |
| gcsNotebookSource | exactly_one_of | create_notebook_execution_job_request.0.notebook_execution_job.0.dataform_repository_source, create_notebook_execution_job_request.0.notebook_execution_job.0.gcs_notebook_source |
| uri | required |  |
| notebookRuntimeTemplateResourceName | required | name: gcsOutputUri |
| gcsOutputUri | required |  |
| executionUser | exactly_one_of | create_notebook_execution_job_request.0.notebook_execution_job.0.execution_user, create_notebook_execution_job_request.0.notebook_execution_job.0.service_account |
| serviceAccount | exactly_one_of | create_notebook_execution_job_request.0.notebook_execution_job.0.execution_user, create_notebook_execution_job_request.0.notebook_execution_job.0.service_account |

## 📦 google_colab_runtime_template

🔗 **API Reference**: https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.notebookRuntimeTemplates

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| displayName | required |  |

## 📦 google_cloudquotas_quota_adjuster_settings

🔗 **API Reference**: https://cloud.google.com/docs/quotas/reference/rest/v1beta/projects.locations.quotaAdjusterSettings

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parent | required |  |
| enablement | required |  |

## 📦 google_cloudquotas_quota_preference

🔗 **API Reference**: https://cloud.google.com/docs/quotas/reference/rest/v1/projects.locations.quotaPreferences

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parent | required |  |
| service | required |  |
| quotaId | required |  |
| quotaConfig | required |  |
| preferredValue | required |  |

## 📦 google_pubsub_subscription

🔗 **API Reference**: https://cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | conflicts | push_config, cloud_storage_config |
| None | required |  |
| None | conflicts | use_table_schema, name: useTableSchema |
| None | conflicts | use_topic_schema |
| None | conflicts | push_config, bigquery_config |
| None | required |  |
| None | conflicts | bigquery_config, cloud_storage_config |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | exactly_one_of | javascript_udf, ai_inference |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_pubsub_topic

🔗 **API Reference**: https://cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| allowedPersistenceRegions | required |  |
| allowedPersistenceRegions | required |  |
| schema | required | name: encoding |
| awsKinesis | conflicts | aws_kinesis, cloud_storage, azure_event_hubs, aws_msk |
| streamArn | required | name: consumerArn |
| consumerArn | required | name: awsRoleArn |
| awsRoleArn | required | name: gcpServiceAccount |
| gcpServiceAccount | required | name: cloudStorage |
| cloudStorage | conflicts | aws_kinesis, cloud_storage, azure_event_hubs, aws_msk |
| bucket | required | name: textFormat |
| textFormat | exactly_one_of | text_format, avro_format, pubsub_avro_format |
| delimiter | required |  |
| avroFormat | exactly_one_of | text_format, avro_format, pubsub_avro_format |
| pubsubAvroFormat | exactly_one_of | text_format, avro_format, pubsub_avro_format |
| minimumObjectCreateTime | required | name: matchGlob |
| matchGlob | required | name: platformLogsSettings |
| platformLogsSettings | required |  |
| azureEventHubs | conflicts | aws_kinesis, cloud_storage, azure_event_hubs, aws_msk |
| awsMsk | conflicts | aws_kinesis, cloud_storage, azure_event_hubs, aws_msk |
| clusterArn | required | name: topic |
| topic | required | name: awsRoleArn |
| awsRoleArn | required | name: gcpServiceAccount |
| gcpServiceAccount | required | name: confluentCloud |
| confluentCloud | conflicts | aws_kinesis, cloud_storage, azure_event_hubs, aws_msk |
| bootstrapServer | required | name: clusterId |
| topic | required | name: identityPoolId |
| identityPoolId | required | name: gcpServiceAccount |
| gcpServiceAccount | required | name: messageTransforms |
| gcpServiceAccount | exactly_one_of | javascript_udf, ai_inference |
| gcpServiceAccount | required |  |
| gcpServiceAccount | required |  |
| gcpServiceAccount | required |  |

## 📦 google_pubsub_schema

🔗 **API Reference**: https://cloud.google.com/pubsub/docs/reference/rest/v1/projects.schemas

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |

## 📦 google_spanner_instance_config

🔗 **API Reference**: https://cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| displayName | required | name: baseConfig |
| replicas | required |  |

## 📦 google_spanner_instance

🔗 **API Reference**: https://cloud.google.com/spanner/docs/reference/rest/v1/projects.instances

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| config | required |  |
| displayName | required | name: num_nodes |
| num_nodes | at_least_one_of | num_nodes, processing_units, autoscaling_config, instance_type |
| num_nodes | conflicts | processing_units, autoscaling_config, name: processingUnits |
| processingUnits | at_least_one_of | num_nodes, processing_units, autoscaling_config, instance_type |
| processingUnits | conflicts | num_nodes, autoscaling_config, name: labels |
| autoscalingConfig | at_least_one_of | num_nodes, processing_units, autoscaling_config, instance_type |
| autoscalingConfig | conflicts | num_nodes, processing_units |
| minProcessingUnits | exactly_one_of | min_processing_units, min_nodes, name: maxProcessingUnits |
| maxProcessingUnits | exactly_one_of | max_processing_units, max_nodes, name: minNodes |
| minNodes | exactly_one_of | min_processing_units, min_nodes |
| maxNodes | exactly_one_of | max_processing_units, max_nodes |
| replicaSelection | required |  |
| location | required |  |
| overrides | required |  |
| minNodes | exactly_one_of | min_nodes, min_processing_units |
| maxNodes | exactly_one_of | max_nodes, max_processing_units |
| minProcessingUnits | exactly_one_of | min_nodes, min_processing_units |
| maxProcessingUnits | exactly_one_of | max_nodes, max_processing_units |
| instanceType | at_least_one_of | num_nodes, processing_units, autoscaling_config, instance_type |

## 📦 google_spanner_database

🔗 **API Reference**: https://cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| instance | required |  |
| name | required |  |
| kmsKeyName | exactly_one_of | encryption_config.0.kms_key_name, encryption_config.0.kms_key_names, name: kmsKeyNames |
| kmsKeyNames | exactly_one_of | encryption_config.0.kms_key_name, encryption_config.0.kms_key_names, name: databaseDialect |

## 📦 google_spanner_backup_schedule

🔗 **API Reference**: https://cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.backupSchedules

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| instance | required |  |
| database | required |  |
| retentionDuration | required | name: spec |
| fullBackupSpec | exactly_one_of | fullBackupSpec, incrementalBackupSpec |
| incrementalBackupSpec | exactly_one_of | fullBackupSpec, incrementalBackupSpec |
| encryptionType | required | name: kmsKeyName |
| kmsKeyName | conflicts | encryption_config.0.kms_key_names, name: kmsKeyNames |
| kmsKeyNames | conflicts | encryption_config.0.kms_key_name |

## 📦 google_spanner_instance_partition

🔗 **API Reference**: https://cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| instance | required |  |
| name | required |  |
| displayName | required |  |
| nodeCount | at_least_one_of | node_count, processing_units, autoscaling_config |
| nodeCount | conflicts | processing_units, autoscaling_config |
| processingUnits | at_least_one_of | node_count, processing_units, autoscaling_config |
| processingUnits | conflicts | node_count, autoscaling_config |
| autoscalingConfig | at_least_one_of | node_count, processing_units, autoscaling_config |
| autoscalingConfig | conflicts | node_count, processing_units |
| minProcessingUnits | exactly_one_of | min_processing_units, min_nodes, name: maxProcessingUnits |
| maxProcessingUnits | exactly_one_of | max_processing_units, max_nodes, name: minNodes |
| minNodes | exactly_one_of | min_processing_units, min_nodes |
| maxNodes | exactly_one_of | max_processing_units, max_nodes |
| config | required |  |

## 📦 google_clouddeploy_deploy_policy

🔗 **API Reference**: https://cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required | name: "invokers" |
| None | required | name: oneTimeWindows |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_clouddeploy_target

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |

## 📦 google_clouddeploy_delivery_pipeline

🔗 **API Reference**: https://cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |

## 📦 google_clouddeploy_custom_target_type

🔗 **API Reference**: https://cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| deployAction | required | name: includeSkaffoldModules |
| git | exactly_one_of | git, googleCloudStorage, googleCloudBuildRepo |
| repo | required | name: path |
| googleCloudStorage | exactly_one_of | git, googleCloudStorage, googleCloudBuildRepo |
| source | required | name: path |
| googleCloudBuildRepo | exactly_one_of | git, googleCloudStorage, googleCloudBuildRepo |
| repository | required | name: path |

## 📦 google_clouddeploy_automation

🔗 **API Reference**: https://cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| delivery_pipeline | required |  |
| name | required |  |
| serviceAccount | required | name: selector |
| selector | required |  |
| targets | required |  |
| rules | required |  |
| promoteReleaseRule | exactly_one_of | promoteReleaseRule, advanceRolloutRule, repairRolloutRule, timedPromoteReleaseRule |
| id | required | name: wait |
| advanceRolloutRule | exactly_one_of | promoteReleaseRule, advanceRolloutRule, repairRolloutRule, timedPromoteReleaseRule |
| id | required | name: wait |
| repairRolloutRule | exactly_one_of | promoteReleaseRule, advanceRolloutRule, repairRolloutRule, timedPromoteReleaseRule |
| id | required | name: phases |
| retry | exactly_one_of | retry, rollback |
| attempts | required | name: wait |
| rollback | exactly_one_of | retry, rollback |
| timedPromoteReleaseRule | exactly_one_of | promoteReleaseRule, advanceRolloutRule, repairRolloutRule, timedPromoteReleaseRule |
| id | required | name: destinationTargetId |
| schedule | required | name: timeZone |
| timeZone | required | name: destinationPhase |

## 📦 google_biglake_table

🔗 **API Reference**: https://cloud.google.com/bigquery/docs/reference/biglake/rest/v1/projects.locations.catalogs.databases.tables

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |

## 📦 google_biglake_database

🔗 **API Reference**: https://cloud.google.com/bigquery/docs/reference/biglake/rest/v1/projects.locations.catalogs.databases

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| catalog | required |  |
| name | required |  |
| type | required | name: hiveOptions |
| hiveOptions | required |  |

## 📦 google_biglake_catalog

🔗 **API Reference**: https://cloud.google.com/bigquery/docs/reference/biglake/rest/v1/projects.locations.catalogs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |

## 📦 google_gkehub2_feature

🔗 **API Reference**: https://cloud.google.com/anthos/fleet-management/docs/reference/rest/v1/projects.locations.features

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| configMembership | required | name: fleetobservability |
| upstreamFleets | required |  |
| postConditions | required |  |
| soaking | required | name: gkeUpgradeOverrides |
| upgrade | required |  |
| name | required | name: version |
| version | required | name: postConditions |
| postConditions | required |  |
| soaking | required | name: rbacrolebindingactuation |
| scopeTenancyPool | required | name: fleetDefaultMemberConfig |
| management | required |  |
| secretType | required | name: httpsProxy |
| secretType | required | name: gcpServiceAccountEmail |
| policyControllerHubConfig | required |  |
| installSpec | required |  |

## 📦 google_gkehub2_scope_rbac_role_binding

🔗 **API Reference**: https://cloud.google.com/anthos/fleet-management/docs/reference/rest/v1/projects.locations.scopes.rbacrolebindings

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| scope_id | required |  |
| scopeRbacRoleBindingId | required |  |
| user | exactly_one_of | user, group, name: group |
| group | exactly_one_of | user, group, name: role |
| role | required |  |
| predefinedRole | exactly_one_of | role.0.predefined_role, role.0.custom_role, name: customRole |
| customRole | exactly_one_of | role.0.predefined_role, role.0.custom_role, name: labels |

## 📦 google_gkehub2_scope

🔗 **API Reference**: https://cloud.google.com/anthos/fleet-management/docs/reference/rest/v1/projects.locations.scopes

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| scopeId | required |  |

## 📦 google_gkehub2_membership_rbac_role_binding

🔗 **API Reference**: https://cloud.google.com/anthos/fleet-management/docs/reference/rest/v1/projects.locations.memberships

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| membership_id | required |  |
| location | required |  |
| membershipRbacRoleBindingId | required |  |
| user | required | name: role |
| role | required |  |
| predefinedRole | required |  |

## 📦 google_gkehub2_membership_binding

🔗 **API Reference**: https://cloud.google.com/anthos/fleet-management/docs/reference/rest/v1/projects.locations.memberships.bindings

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| membership_id | required |  |
| location | required |  |
| membershipBindingId | required |  |
| scope | required |  |

## 📦 google_gkehub2_namespace

🔗 **API Reference**: https://cloud.google.com/anthos/fleet-management/docs/reference/rest/v1/projects.locations.scopes.namespaces

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| scope_id | required |  |
| scopeNamespaceId | required |  |
| scope | required |  |

## 📦 google_gkehub2_rollout_sequence

🔗 **API Reference**: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.rolloutSequences

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| rollout_sequence_id | required |  |
| stages | required |  |
| fleetProjects | required |  |
| labelSelector | required | name: soakDuration |

## 📦 google_serviceusage_consumer_quota_override

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_databasemigrationservice_private_connection

🔗 **API Reference**: https://cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| privateConnectionId | required |  |
| create_without_validation | required |  |
| location | required |  |
| vpcPeeringConfig | required |  |
| vpcName | required | name: subnet |
| subnet | required |  |

## 📦 google_databasemigrationservice_connection_profile

🔗 **API Reference**: https://cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles/create

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | exactly_one_of | mysql, postgresql, oracle, cloudsql |
| None | exactly_one_of | mysql, postgresql, oracle, cloudsql |
| None | exactly_one_of | mysql, postgresql, oracle, cloudsql |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | exactly_one_of | static_service_ip_connectivity, forward_ssh_connectivity, private_connectivity |
| None | exactly_one_of | static_service_ip_connectivity, forward_ssh_connectivity, private_connectivity |
| None | required |  |
| None | required |  |
| None | required |  |
| None | exactly_one_of | forward_ssh_connectivity.0.password, forward_ssh_connectivity.0.private_key |
| None | exactly_one_of | oracle.0.forward_ssh_connectivity.0.password, oracle.0.forward_ssh_connectivity.0.private_key |
| None | exactly_one_of | oracle.0.static_service_ip_connectivity, oracle.0.forward_ssh_connectivity, oracle.0.private_connectivity |
| None | required |  |
| None | exactly_one_of | mysql, postgresql, oracle, cloudsql |
| None | required |  |
| None | exactly_one_of | expire_time, ttl, name: ttl |
| None | required |  |
| None | exactly_one_of | mysql, postgresql, oracle, cloudsql |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_databasemigrationservice_migration_job

🔗 **API Reference**: https://cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/create

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | exactly_one_of | reverseSshConnectivity, vpcPeeringConnectivity |
| None | exactly_one_of | staticIpConnectivity, vpcPeeringConnectivity |
| None | exactly_one_of | staticIpConnectivity, reverseSshConnectivity |

## 📦 google_securesourcemanager_hook

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: location |
| None | required | name: repository_id |
| None | required |  |
| None | required | name: disabled |

## 📦 google_securesourcemanager_repository

🔗 **API Reference**: https://cloud.google.com/secure-source-manager/docs/reference/rest/v1/projects.locations.repositories

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required | name: repository_id |
| repository_id | required |  |
| instance | required |  |

## 📦 google_securesourcemanager_instance

🔗 **API Reference**: https://cloud.google.com/secure-source-manager/docs/reference/rest/v1/projects.locations.instances

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| instance_id | required |  |
| isPrivate | required |  |
| html | required | name: api |
| api | required | name: gitHttp |
| gitHttp | required | name: gitSsh |
| gitSsh | required | name: caPool |
| enabled | required |  |

## 📦 google_securesourcemanager_branch_rule

🔗 **API Reference**: https://cloud.google.com/secure-source-manager/docs/reference/rest/v1/projects.locations.repositories.branchRules

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_bigquerydatapolicy_data_policy

🔗 **API Reference**: https://cloud.google.com/bigquery/docs/reference/bigquerydatapolicy/rest/v1beta1/projects.locations.dataPolicies/create

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| dataPolicyId | required |  |
| location | required |  |
| policyTag | required |  |
| dataPolicyType | required |  |
| predefinedExpression | exactly_one_of | data_masking_policy.0.predefined_expression, data_masking_policy.0.routine |
| routine | exactly_one_of | data_masking_policy.0.predefined_expression, data_masking_policy.0.routine |

## 📦 google_alloydb_backup

🔗 **API Reference**: https://cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.backups/create

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| backupId | required |  |
| location | required |  |
| clusterName | required |  |

## 📦 google_alloydb_instance

🔗 **API Reference**: https://cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances/create

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| cluster | required |  |
| instanceId | required |  |
| instanceType | required |  |
| enabled | required | name: poolerCount |

## 📦 google_alloydb_cluster

🔗 **API Reference**: https://cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters/create

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| clusterId | required |  |
| location | required |  |
| network | exactly_one_of | network_config.0.network, psc_config.0.psc_enabled |
| user | at_least_one_of | initial_user.0.user, initial_user.0.password, name: password |
| password | at_least_one_of | initial_user.0.user, initial_user.0.password, name: restoreBackupSource |
| restoreBackupSource | conflicts | restore_continuous_backup_source, restore_backupdr_backup_source, restore_backupdr_pitr_source |
| backupName | required |  |
| restoreContinuousBackupSource | conflicts | restore_backup_source, restore_backupdr_backup_source, restore_backupdr_pitr_source |
| cluster | required |  |
| pointInTime | required |  |
| restoreBackupdrBackupSource | conflicts | restore_continuous_backup_source, restore_backup_source, restore_backupdr_pitr_source |
| backup | required |  |
| restoreBackupdrPitrSource | conflicts | restore_backup_source, restore_continuous_backup_source, restore_backupdr_backup_source |
| dataSource | required |  |
| pointInTime | required |  |
| startTimes | required |  |
| timeBasedRetention | conflicts | automated_backup_policy.0.quantity_based_retention |
| quantityBasedRetention | conflicts | automated_backup_policy.0.time_based_retention |
| primaryClusterName | required | name: maintenanceUpdatePolicy |
| day | required |  |
| startTime | required |  |
| hours | required | name: minutes |
| enabled | required |  |

## 📦 google_alloydb_user

🔗 **API Reference**: https://cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.users/create

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| cluster | required |  |
| userId | required |  |
| userType | required |  |

## 📦 google_securityscanner_scan_config

🔗 **API Reference**: https://cloud.google.com/security-scanner/docs/reference/rest/v1beta/projects.scanConfigs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | at_least_one_of | authentication.0.google_account, authentication.0.custom_account |
| None | required |  |
| None | required |  |
| None | at_least_one_of | authentication.0.google_account, authentication.0.custom_account |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_modelarmorglobal_floorsetting

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| modelarmor_floorsetting_ai_platform_metadata | required | name: parent |
| modelarmor_floorsetting_ai_platform_metadata | required |  |
| modelarmor_floorsetting_ai_platform_metadata | required |  |
| modelarmor_floorsetting_ai_platform_metadata | required |  |
| modelarmor_floorsetting_ai_platform_metadata | required | name: confidenceLevel |
| modelarmor_floorsetting_ai_platform_metadata | conflicts | filter_config.0.sdp_settings.0.basic_config |
| modelarmor_floorsetting_ai_platform_metadata | conflicts | filter_config.0.sdp_settings.0.advanced_config |
| modelarmor_floorsetting_ai_platform_metadata | exactly_one_of | ai_platform_floor_setting.0.inspect_only, ai_platform_floor_setting.0.inspect_and_block, name: inspectAndBlock |
| modelarmor_floorsetting_ai_platform_metadata | exactly_one_of | ai_platform_floor_setting.0.inspect_only, ai_platform_floor_setting.0.inspect_and_block, name: enableCloudLogging |
| modelarmor_floorsetting_ai_platform_metadata | exactly_one_of | google_mcp_server_floor_setting.0.inspect_only, google_mcp_server_floor_setting.0.inspect_and_block, name: inspectAndBlock |
| modelarmor_floorsetting_ai_platform_metadata | exactly_one_of | google_mcp_server_floor_setting.0.inspect_only, google_mcp_server_floor_setting.0.inspect_and_block, name: enableCloudLogging |
| modelarmor_floorsetting_ai_platform_metadata | required |  |

## 📦 google_dialogflowcx_webhook

🔗 **API Reference**: https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| displayName | required | name: timeout |
| disabled | required | name: clientSecret |
| disabled | required | name: parameterMapping |
| disabled | required | name: serviceAgentAuth |
| disabled | required |  |
| disabled | required | name: webhookType |
| service | required | name: genericWebService |
| service | required | name: clientSecret |
| service | required | name: parameterMapping |
| service | required | name: serviceAgentAuth |
| service | required |  |
| service | required | name: webhookType |

## 📦 google_dialogflowcx_tool_version

🔗 **API Reference**: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools.versions

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parent | required |  |
| displayName | required | name: tool |
| tool | required |  |
| displayName | required | name: description |
| description | required | name: toolType |
| keyName | required | name: apiKey |
| requestLocation | required | name: oauthConfig |
| oauthGrantType | required | name: clientId |
| clientId | required | name: clientSecret |
| tokenEndpoint | required | name: scopes |
| caCerts | required |  |
| displayName | required | name: cert |
| cert | required | name: serviceDirectoryConfig |
| service | required | name: textSchema |
| textSchema | required | name: dataStoreSpec |
| dataStoreConnections | required |  |
| fallbackPrompt | required |  |
| name | required |  |
| actions | required |  |
| entityId | required | name: operation |
| operation | required | name: endUserAuthConfig |
| oauthToken | required | name: oauth2JwtBearerConfig |
| issuer | required | name: subject |
| subject | required | name: clientKey |
| clientKey | required |  |

## 📦 google_dialogflowcx_intent

🔗 **API Reference**: https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| displayName | required |  |
| parts | required |  |
| text | required | name: parameterId |
| id | required | name: entityType |
| entityType | required | name: isList |

## 📦 google_dialogflowcx_generator

🔗 **API Reference**: https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.generators

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| displayName | required | name: llmModelSettings |
| promptText | required |  |

## 📦 google_dialogflowcx_version

🔗 **API Reference**: https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.versions

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| displayName | required |  |

## 📦 google_dialogflowcx_test_case

🔗 **API Reference**: https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.testCases

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| displayName | required |  |
| flow | conflicts | test_config.0.page, name: page |
| page | conflicts | test_config.0.flow, name: testCaseConversationTurns |
| text | required |  |
| event | required | name: dtmf |
| text | required |  |
| event | required | name: dtmf |

## 📦 google_dialogflowcx_agent

🔗 **API Reference**: https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| displayName | required | name: defaultLanguageCode |
| defaultLanguageCode | required |  |
| timeZone | required | name: description |
| engine | required |  |
| startPlaybook | conflicts | startFlow, name: enableMultiLanguageTraining |
| sslCertificate | required |  |
| privateKey | required |  |

## 📦 google_dialogflowcx_tool

🔗 **API Reference**: https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| displayName | required | name: description |
| description | required | name: toolType |
| keyName | required | name: apiKey |
| requestLocation | required | name: oauthConfig |
| oauthGrantType | required | name: clientId |
| clientId | required | name: clientSecret |
| tokenEndpoint | required | name: scopes |
| caCerts | required |  |
| displayName | required | name: cert |
| cert | required | name: serviceDirectoryConfig |
| service | required | name: textSchema |
| textSchema | required | name: dataStoreSpec |
| dataStoreConnections | required |  |
| fallbackPrompt | required |  |
| name | required |  |
| actions | required |  |
| entityId | required | name: operation |
| operation | required | name: endUserAuthConfig |
| oauthToken | required | name: oauth2JwtBearerConfig |
| issuer | required | name: subject |
| subject | required | name: clientKey |
| clientKey | required |  |

## 📦 google_dialogflowcx_playbook

🔗 **API Reference**: https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| displayName | required | name: goal |
| goal | required | name: instruction |

## 📦 google_dialogflowcx_security_settings

🔗 **API Reference**: https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| displayName | required | name: redactionStrategy |
| enableInsightsExport | required | name: retentionWindowDays |
| retentionWindowDays | conflicts | retentionStrategy, name: retentionStrategy |
| retentionStrategy | conflicts | retentionWindowDays |

## 📦 google_dialogflowcx_flow

🔗 **API Reference**: https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| displayName | required | name: description |
| audioUri | required | name: allowPlaybackInterruption |
| phoneNumber | required | name: webhook |
| audioUri | required | name: allowPlaybackInterruption |
| phoneNumber | required | name: webhook |
| text | required |  |
| audioUri | required | name: allowPlaybackInterruption |
| phoneNumber | required | name: knowledgeInfoCard |
| advancedSettings | required | name: speechSettings |

## 📦 google_dialogflowcx_entity_type

🔗 **API Reference**: https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.entityTypes

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| displayName | required |  |
| kind | required |  |
| entities | required |  |

## 📦 google_dialogflowcx_page

🔗 **API Reference**: https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| displayName | required |  |
| audioUri | required | name: allowPlaybackInterruption |
| phoneNumber | required | name: webhook |
| audioUri | required | name: allowPlaybackInterruption |
| phoneNumber | required | name: webhook |
| audioUri | required | name: allowPlaybackInterruption |
| phoneNumber | required | name: webhook |
| audioUri | required | name: allowPlaybackInterruption |
| phoneNumber | required | name: webhook |
| audioUri | required | name: allowPlaybackInterruption |
| phoneNumber | required | name: webhook |
| text | required |  |
| audioUri | required | name: allowPlaybackInterruption |
| phoneNumber | required | name: knowledgeInfoCard |
| advancedSettings | required | name: speechSettings |

## 📦 google_dialogflowcx_environment

🔗 **API Reference**: https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| displayName | required |  |
| versionConfigs | required |  |
| version | required | name: updateTime |

## 📦 google_dialogflowcx_generative_settings

🔗 **API Reference**: https://cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents/getGenerativeSettings

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| text | required | name: languageCode |
| languageCode | required | name: knowledgeConnectorSettings |
| languageCode | required | name: llmModelSettings |

## 📦 google_networksecurity_intercept_endpoint_group

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| interceptEndpointGroupId | required |  |
| interceptDeploymentGroup | required |  |

## 📦 google_networksecurity_security_profile

🔗 **API Reference**: https://cloud.google.com/firewall/docs/reference/network-security/rest/v1/organizations.locations.securityProfiles

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| action | required |  |
| severity | required |  |
| action | required |  |
| threatId | required | name: type |
| protocol | required |  |
| action | required |  |
| action | conflicts | urlFilteringProfile, customMirroringProfile, customInterceptProfile, name: urlFilteringProfile |
| filteringAction | required |  |
| priority | required |  |
| priority | conflicts | threatPreventionProfile, customMirroringProfile, customInterceptProfile, name: customMirroringProfile |
| customMirroringProfile | required | name: mirroringDeploymentGroups |
| mirroringEndpointGroupType | conflicts | threatPreventionProfile, urlFilteringProfile, customInterceptProfile, name: customInterceptProfile |
| customInterceptProfile | required |  |
| customInterceptProfile | conflicts | threatPreventionProfile, urlFilteringProfile, customMirroringProfile, name: type |
| type | required |  |

## 📦 google_networksecurity_mirroring_endpoint_group

🔗 **API Reference**: https://cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringEndpointGroups

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| mirroringEndpointGroupId | required |  |
| mirroringDeploymentGroup | exactly_one_of | mirroring_deployment_group, mirroring_deployment_groups, name: mirroringDeploymentGroups |
| mirroringDeploymentGroups | exactly_one_of | mirroring_deployment_group, mirroring_deployment_groups, name: state |

## 📦 google_networksecurity_security_profile_group

🔗 **API Reference**: https://cloud.google.com/firewall/docs/reference/network-security/rest/v1/organizations.locations.securityProfileGroups

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |

## 📦 google_networksecurity_firewall_endpoint_association

🔗 **API Reference**: https://cloud.google.com/firewall/docs/reference/network-security/rest/v1/projects.locations.firewallEndpointAssociations#FirewallEndpointAssociation

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| location | required |  |
| firewallEndpoint | required | name: network |
| network | required | name: tlsInspectionPolicy |

## 📦 google_networksecurity_tls_inspection_policy

🔗 **API Reference**: https://cloud.google.com/secure-web-proxy/docs/reference/network-security/rest/v1/projects.locations.tlsInspectionPolicies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required | name: location |
| caPool | required | name: trustConfig |

## 📦 google_networksecurity_mirroring_endpoint

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| mirroringEndpointId | required |  |
| mirroringEndpointGroup | required |  |

## 📦 google_networksecurity_firewall_endpoint

🔗 **API Reference**: https://cloud.google.com/firewall/docs/reference/network-security/rest/v1/organizations.locations.firewallEndpoints

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| location | required |  |
| parent | required |  |
| billingProjectId | required | name: endpointSettings |

## 📦 google_networksecurity_authz_policy

🔗 **API Reference**: https://cloud.google.com/load-balancing/docs/reference/network-security/rest/v1beta1/projects.locations.authzPolicies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| location | required |  |
| target | required |  |
| prefix | required | name: length |
| length | required | name: principals |
| prefix | required | name: length |
| length | required | name: principals |
| name | required |  |
| action | required |  |
| enabled | required | name: authzExtension |
| resources | required |  |

## 📦 google_networksecurity_server_tls_policy

🔗 **API Reference**: https://cloud.google.com/traffic-director/docs/reference/network-security/rest/v1beta1/projects.locations.serverTlsPolicies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| grpcEndpoint | exactly_one_of | grpc_endpoint, certificate_provider_instance |
| targetUri | required | name: certificateProviderInstance |
| certificateProviderInstance | exactly_one_of | grpc_endpoint, certificate_provider_instance |
| pluginInstance | required | name: mtlsPolicy |
| grpcEndpoint | exactly_one_of | grpc_endpoint, certificate_provider_instance |
| targetUri | required | name: certificateProviderInstance |
| certificateProviderInstance | exactly_one_of | grpc_endpoint, certificate_provider_instance |
| pluginInstance | required |  |

## 📦 google_networksecurity_mirroring_deployment

🔗 **API Reference**: https://cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringDeployments

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| mirroringDeploymentId | required |  |
| forwardingRule | required |  |
| mirroringDeploymentGroup | required |  |

## 📦 google_networksecurity_address_group

🔗 **API Reference**: https://cloud.google.com/traffic-director/docs/reference/network-security/rest/v1beta1/organizations.locations.addressGroups

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required | name: location |
| location | required |  |
| type | required |  |
| capacity | required |  |

## 📦 google_networksecurity_intercept_endpoint_group_association

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| interceptEndpointGroup | required |  |
| network | required |  |

## 📦 google_networksecurity_mirroring_deployment_group

🔗 **API Reference**: https://cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringDeploymentGroups

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| mirroringDeploymentGroupId | required |  |
| network | required |  |

## 📦 google_networksecurity_gateway_security_policy_rule

🔗 **API Reference**: https://cloud.google.com/secure-web-proxy/docs/reference/network-security/rest/v1/projects.locations.gatewaySecurityPolicies.rules

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| location | required |  |
| gateway_security_policy | required |  |
| enabled | required | name: priority |
| priority | required | name: description |
| sessionMatcher | required | name: applicationMatcher |
| basicProfile | required |  |

## 📦 google_networksecurity_backend_authentication_config

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |

## 📦 google_networksecurity_sac_attachment

🔗 **API Reference**: https://cloud.google.com/secure-access-connect/docs/reference/network-security/rest/v1beta1/projects.locations.sacAttachments

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| sacRealm | required | name: nccGateway |
| nccGateway | required | name: country |

## 📦 google_networksecurity_authorization_policy

🔗 **API Reference**: https://cloud.google.com/traffic-director/docs/reference/network-security/rest/v1beta1/projects.locations.authorizationPolicies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| action | required |  |
| hosts | required |  |
| ports | required |  |
| methods | required |  |
| headerName | required | name: regexMatch |
| regexMatch | required |  |

## 📦 google_networksecurity_ull_mirroring_collector

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| ullMirroringCollectorId | required |  |
| engine | required | name: forwardingRule |
| forwardingRule | required | name: labels |

## 📦 google_networksecurity_intercept_deployment_group

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| interceptDeploymentGroupId | required |  |
| network | required |  |

## 📦 google_networksecurity_dns_threat_detector

🔗 **API Reference**: https://cloud.google.com/dns/docs/create-threat-detector

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |

## 📦 google_networksecurity_url_lists

🔗 **API Reference**: https://cloud.google.com/secure-web-proxy/docs/reference/network-security/rest/v1/projects.locations.urlLists

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required | name: location |
| location | required |  |
| values | required |  |

## 📦 google_networksecurity_ull_mirroring_engine

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| ullMirroringEngineId | required |  |

## 📦 google_networksecurity_mirroring_endpoint_group_association

🔗 **API Reference**: https://cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringEndpointGroupAssociations

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| mirroringEndpointGroup | required |  |
| network | required |  |

## 📦 google_networksecurity_sac_realm

🔗 **API Reference**: https://cloud.google.com/secure-access-connect/docs/reference/network-security/rest/v1beta1/projects.locations.sacRealms

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| securityService | required |  |

## 📦 google_networksecurity_gateway_security_policy

🔗 **API Reference**: https://cloud.google.com/secure-web-proxy/docs/reference/network-security/rest/v1/projects.locations.gatewaySecurityPolicies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required | name: location |

## 📦 google_networksecurity_intercept_deployment

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| interceptDeploymentId | required |  |
| forwardingRule | required |  |
| interceptDeploymentGroup | required |  |

## 📦 google_networksecurity_client_tls_policy

🔗 **API Reference**: https://cloud.google.com/traffic-director/docs/reference/network-security/rest/v1beta1/projects.locations.clientTlsPolicies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| grpcEndpoint | exactly_one_of | grpc_endpoint, certificate_provider_instance |
| targetUri | required | name: certificateProviderInstance |
| certificateProviderInstance | exactly_one_of | grpc_endpoint, certificate_provider_instance |
| pluginInstance | required | name: serverValidationCa |
| grpcEndpoint | exactly_one_of | grpc_endpoint, certificate_provider_instance |
| targetUri | required | name: certificateProviderInstance |
| certificateProviderInstance | exactly_one_of | grpc_endpoint, certificate_provider_instance |
| pluginInstance | required |  |

## 📦 google_networksecurity_project_address_group

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required | name: location |
| location | required |  |

## 📦 google_monitoring_generic_service

🔗 **API Reference**: https://cloud.google.com/monitoring/api/ref_v3/rest/v3/services

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| serviceId | required |  |

## 📦 google_monitoring_uptime_check_config

🔗 **API Reference**: https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | at_least_one_of | http_check.0.auth_info, http_check.0.port, http_check.0.headers, http_check.0.path |
| None | exactly_one_of | password, password_wo |
| None | exactly_one_of | passwordWo, password |
| None | required |  |
| None | at_least_one_of | http_check.0.auth_info, http_check.0.port, http_check.0.headers, http_check.0.path |
| None | at_least_one_of | http_check.0.auth_info, http_check.0.port, http_check.0.headers, http_check.0.path |
| None | at_least_one_of | http_check.0.auth_info, http_check.0.port, http_check.0.headers, http_check.0.path |
| None | at_least_one_of | http_check.0.auth_info, http_check.0.port, http_check.0.headers, http_check.0.path |
| None | at_least_one_of | http_check.0.auth_info, http_check.0.port, http_check.0.headers, http_check.0.path |
| None | required |  |
| None | required |  |
| None | required |  |
| None | exactly_one_of | monitored_resource, resource_group, synthetic_monitor |
| None | at_least_one_of | resource_group.0.resource_type, resource_group.0.group_id |
| None | at_least_one_of | resource_group.0.resource_type, resource_group.0.group_id |
| None | exactly_one_of | monitored_resource, resource_group, synthetic_monitor |
| None | required |  |
| None | required |  |
| None | exactly_one_of | monitored_resource, resource_group, synthetic_monitor |
| None | required |  |
| None | exactly_one_of | cloud_function_v2 |
| None | required |  |

## 📦 google_monitoring_notification_channel

🔗 **API Reference**: https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| authToken | exactly_one_of | sensitive_labels.0.auth_token, sensitive_labels.0.password, sensitive_labels.0.service_key, name: password |
| password | exactly_one_of | sensitive_labels.0.auth_token, sensitive_labels.0.password, sensitive_labels.0.service_key, name: serviceKey |
| serviceKey | exactly_one_of | sensitive_labels.0.auth_token, sensitive_labels.0.password, sensitive_labels.0.service_key, name: name |
| type | required | name: userLabels |

## 📦 google_monitoring_monitored_project

🔗 **API Reference**: https://cloud.google.com/monitoring/api/ref_v3/rest/v1/locations.global.metricsScopes.projects

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| metricsScope | required |  |
| name | required |  |

## 📦 google_monitoring_slo

🔗 **API Reference**: https://cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| service | required |  |
| goal | required |  |
| rollingPeriodDays | exactly_one_of | rolling_period_days, calendar_period |
| calendarPeriod | exactly_one_of | rolling_period_days, calendar_period |
| basicSli | exactly_one_of | service_level_indicator.0.basic_sli, service_level_indicator.0.request_based_sli, service_level_indicator.0.windows_based_sli |
| latency | exactly_one_of | service_level_indicator.0.basic_sli.0.latency, service_level_indicator.0.basic_sli.0.availability |
| threshold | required | name: availability |
| availability | exactly_one_of | service_level_indicator.0.basic_sli.0.latency, service_level_indicator.0.basic_sli.0.availability |
| requestBasedSli | exactly_one_of | service_level_indicator.0.basic_sli, service_level_indicator.0.request_based_sli, service_level_indicator.0.windows_based_sli |
| goodTotalRatio | exactly_one_of | service_level_indicator.0.request_based_sli.0.good_total_ratio, service_level_indicator.0.request_based_sli.0.distribution_cut |
| goodServiceFilter | at_least_one_of | service_level_indicator.0.request_based_sli.0.good_total_ratio.0.good_service_filter, service_level_indicator.0.request_based_sli.0.good_total_ratio.0.bad_service_filter, service_level_indicator.0.request_based_sli.0.good_total_ratio.0.total_service_filter, name: badServiceFilter |
| badServiceFilter | at_least_one_of | service_level_indicator.0.request_based_sli.0.good_total_ratio.0.good_service_filter, service_level_indicator.0.request_based_sli.0.good_total_ratio.0.bad_service_filter, service_level_indicator.0.request_based_sli.0.good_total_ratio.0.total_service_filter, name: totalServiceFilter |
| totalServiceFilter | at_least_one_of | service_level_indicator.0.request_based_sli.0.good_total_ratio.0.good_service_filter, service_level_indicator.0.request_based_sli.0.good_total_ratio.0.bad_service_filter, service_level_indicator.0.request_based_sli.0.good_total_ratio.0.total_service_filter, name: distributionCut |
| distributionCut | exactly_one_of | service_level_indicator.0.request_based_sli.0.good_total_ratio, service_level_indicator.0.request_based_sli.0.distribution_cut |
| distributionFilter | required | name: range |
| range | required |  |
| min | at_least_one_of | service_level_indicator.0.request_based_sli.0.distribution_cut.0.range.0.min, service_level_indicator.0.request_based_sli.0.distribution_cut.0.range.0.max, name: max |
| max | at_least_one_of | service_level_indicator.0.request_based_sli.0.distribution_cut.0.range.0.min, service_level_indicator.0.request_based_sli.0.distribution_cut.0.range.0.max, name: windowsBasedSli |
| windowsBasedSli | exactly_one_of | service_level_indicator.0.basic_sli, service_level_indicator.0.request_based_sli, service_level_indicator.0.windows_based_sli |
| goodBadMetricFilter | exactly_one_of | service_level_indicator.0.windows_based_sli.0.good_bad_metric_filter, service_level_indicator.0.windows_based_sli.0.good_total_ratio_threshold, service_level_indicator.0.windows_based_sli.0.metric_mean_in_range, service_level_indicator.0.windows_based_sli.0.metric_sum_in_range |
| goodTotalRatioThreshold | exactly_one_of | service_level_indicator.0.windows_based_sli.0.good_bad_metric_filter, service_level_indicator.0.windows_based_sli.0.good_total_ratio_threshold, service_level_indicator.0.windows_based_sli.0.metric_mean_in_range, service_level_indicator.0.windows_based_sli.0.metric_sum_in_range |
| performance | exactly_one_of | service_level_indicator.0.windows_based_sli.0.good_total_ratio_threshold.0.performance, service_level_indicator.0.windows_based_sli.0.good_total_ratio_threshold.0.basic_sli_performance |
| goodTotalRatio | exactly_one_of | service_level_indicator.0.windows_based_sli.0.good_total_ratio_threshold.0.performance.0.good_total_ratio, service_level_indicator.0.windows_based_sli.0.good_total_ratio_threshold.0.performance.0.distribution_cut |
| goodServiceFilter | at_least_one_of | service_level_indicator.0.windows_based_sli.0.good_total_ratio_threshold.0.performance.0.good_total_ratio.0.good_service_filter, service_level_indicator.0.windows_based_sli.0.good_total_ratio_threshold.0.performance.0.good_total_ratio.0.bad_service_filter, service_level_indicator.0.windows_based_sli.0.good_total_ratio_threshold.0.performance.0.good_total_ratio.0.total_service_filter, name: badServiceFilter |
| badServiceFilter | at_least_one_of | service_level_indicator.0.windows_based_sli.0.good_total_ratio_threshold.0.performance.0.good_total_ratio.0.good_service_filter, service_level_indicator.0.windows_based_sli.0.good_total_ratio_threshold.0.performance.0.good_total_ratio.0.bad_service_filter, service_level_indicator.0.windows_based_sli.0.good_total_ratio_threshold.0.performance.0.good_total_ratio.0.total_service_filter, name: totalServiceFilter |
| totalServiceFilter | at_least_one_of | service_level_indicator.0.windows_based_sli.0.good_total_ratio_threshold.0.performance.0.good_total_ratio.0.good_service_filter, service_level_indicator.0.windows_based_sli.0.good_total_ratio_threshold.0.performance.0.good_total_ratio.0.bad_service_filter, service_level_indicator.0.windows_based_sli.0.good_total_ratio_threshold.0.performance.0.good_total_ratio.0.total_service_filter, name: distributionCut |
| distributionCut | exactly_one_of | service_level_indicator.0.windows_based_sli.0.good_total_ratio_threshold.0.performance.0.good_total_ratio, service_level_indicator.0.windows_based_sli.0.good_total_ratio_threshold.0.performance.0.distribution_cut |
| distributionFilter | required | name: range |
| range | required |  |
| min | at_least_one_of | service_level_indicator.0.windows_based_sli.0.good_total_ratio_threshold.0.performance.0.distribution_cut.0.range.0.min, service_level_indicator.0.windows_based_sli.0.good_total_ratio_threshold.0.performance.0.distribution_cut.0.range.0.max, name: max |
| max | at_least_one_of | service_level_indicator.0.windows_based_sli.0.good_total_ratio_threshold.0.performance.0.distribution_cut.0.range.0.min, service_level_indicator.0.windows_based_sli.0.good_total_ratio_threshold.0.performance.0.distribution_cut.0.range.0.max, name: basicSliPerformance |
| basicSliPerformance | exactly_one_of | service_level_indicator.0.windows_based_sli.0.good_total_ratio_threshold.0.performance, service_level_indicator.0.windows_based_sli.0.good_total_ratio_threshold.0.basic_sli_performance |
| latency | exactly_one_of | service_level_indicator.0.windows_based_sli.0.good_total_ratio_threshold.0.basic_sli_performance.0.latency, service_level_indicator.0.windows_based_sli.0.good_total_ratio_threshold.0.basic_sli_performance.0.availability |
| threshold | required | name: availability |
| availability | exactly_one_of | service_level_indicator.0.windows_based_sli.0.good_total_ratio_threshold.0.basic_sli_performance.0.latency, service_level_indicator.0.windows_based_sli.0.good_total_ratio_threshold.0.basic_sli_performance.0.availability |
| metricMeanInRange | exactly_one_of | service_level_indicator.0.windows_based_sli.0.good_bad_metric_filter, service_level_indicator.0.windows_based_sli.0.good_total_ratio_threshold, service_level_indicator.0.windows_based_sli.0.metric_mean_in_range, service_level_indicator.0.windows_based_sli.0.metric_sum_in_range |
| timeSeries | required | name: range |
| range | required |  |
| min | at_least_one_of | service_level_indicator.0.windows_based_sli.0.metric_mean_in_range.0.range.0.min, service_level_indicator.0.windows_based_sli.0.metric_mean_in_range.0.range.0.max, name: max |
| max | at_least_one_of | service_level_indicator.0.windows_based_sli.0.metric_mean_in_range.0.range.0.min, service_level_indicator.0.windows_based_sli.0.metric_mean_in_range.0.range.0.max, name: metricSumInRange |
| metricSumInRange | exactly_one_of | service_level_indicator.0.windows_based_sli.0.good_bad_metric_filter, service_level_indicator.0.windows_based_sli.0.good_total_ratio_threshold, service_level_indicator.0.windows_based_sli.0.metric_mean_in_range, service_level_indicator.0.windows_based_sli.0.metric_sum_in_range |
| timeSeries | required | name: range |
| range | required |  |
| min | at_least_one_of | service_level_indicator.0.windows_based_sli.0.metric_sum_in_range.0.range.0.min, service_level_indicator.0.windows_based_sli.0.metric_sum_in_range.0.range.0.max, name: max |
| max | at_least_one_of | service_level_indicator.0.windows_based_sli.0.metric_sum_in_range.0.range.0.min, service_level_indicator.0.windows_based_sli.0.metric_sum_in_range.0.range.0.max |

## 📦 google_monitoring_metric_descriptor

🔗 **API Reference**: https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| type | required |  |
| key | required | name: valueType |
| metricKind | required |  |
| valueType | required |  |
| samplePeriod | at_least_one_of | metadata.0.sample_period, metadata.0.ingest_delay, name: ingestDelay |
| ingestDelay | at_least_one_of | metadata.0.sample_period, metadata.0.ingest_delay, name: launchStage |

## 📦 google_monitoring_alert_policy

🔗 **API Reference**: https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| displayName | required | name: combiner |
| combiner | required |  |
| conditions | required |  |
| duration | required | name: filter |
| query | required | name: duration |
| duration | required | name: trigger |
| duration | required | name: forecastOptions |
| forecastHorizon | required | name: comparison |
| comparison | required |  |
| displayName | required | name: conditionMatchedLog |
| filter | required | name: labelExtractors |
| query | required | name: duration |
| query | required | name: minutes |
| periodicity | required |  |
| periodicity | exactly_one_of | minutes, hourly, daily, name: hourly |
| periodicity | required | name: minuteOffset |
| minuteOffset | exactly_one_of | minutes, hourly, daily, name: daily |
| daily | required | name: executionTime |
| nanos | exactly_one_of | minutes, hourly, daily, name: rowCountTest |
| comparison | required | name: threshold |
| threshold | required |  |
| threshold | exactly_one_of | rowCountTest, booleanTest, name: booleanTest |
| column | required |  |
| column | exactly_one_of | rowCountTest, booleanTest, name: notificationChannels |
| content | at_least_one_of | documentation.0.content, documentation.0.mime_type, documentation.0.subject, documentation.0.links |
| mimeType | at_least_one_of | documentation.0.content, documentation.0.mime_type, documentation.0.subject, documentation.0.links |
| subject | at_least_one_of | documentation.0.content, documentation.0.mime_type, documentation.0.subject, documentation.0.links |
| links | at_least_one_of | documentation.0.content, documentation.0.mime_type, documentation.0.subject, documentation.0.links |

## 📦 google_monitoring_group

🔗 **API Reference**: https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| displayName | required | name: filter |
| filter | required |  |

## 📦 google_cloudids_endpoint

🔗 **API Reference**: https://cloud.google.com/intrusion-detection-system/docs/configuring-ids

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| network | required |  |
| severity | required |  |

## 📦 google_cloudrunv2_service

🔗 **API Reference**: https://cloud.google.com/run/docs/reference/rest/v2/projects.locations.services

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| useDefault | conflicts | policy, name: policy |
| policy | conflicts | use_default, name: customAudiences |
| template | required |  |
| connector | conflicts | template.0.vpc_access.0.network_interfaces, name: egress |
| networkInterfaces | conflicts | template.0.vpc_access.0.connector |
| image | required | name: command |
| name | required | name: value |
| value | exactly_one_of |  |
| valueSource | exactly_one_of |  |
| secret | required | name: version |
| name | required | name: mountPath |
| mountPath | required | name: subPath |
| httpGet | exactly_one_of |  |
| name | required | name: value |
| port | required | name: startupProbe |
| name | required | name: value |
| tcpSocket | exactly_one_of |  |
| grpc | exactly_one_of |  |
| httpGet | exactly_one_of |  |
| grpc | exactly_one_of |  |
| cloudStorageSource | exactly_one_of | cloud_storage_source |
| bucket | required | name: object |
| object | required | name: generation |
| name | required | name: secret |
| secret | exactly_one_of |  |
| secret | required | name: defaultMode |
| path | required | name: version |
| cloudSqlInstance | exactly_one_of |  |
| emptyDir | exactly_one_of |  |
| gcs | exactly_one_of |  |
| bucket | required | name: readOnly |
| readOnly | required | name: mountOptions |
| server | required | name: path |
| path | required | name: readOnly |
| readOnly | required | name: executionEnvironment |
| accelerator | required | name: gpuZonalRedundancyDisabled |

## 📦 google_cloudrunv2_worker_pool

🔗 **API Reference**: https://cloud.google.com/run/docs/reference/rest/v2/projects.locations.workerPools

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| useDefault | conflicts | policy, name: policy |
| policy | conflicts | use_default, name: customAudiences |
| template | required |  |
| image | required | name: command |
| name | required | name: value |
| value | exactly_one_of |  |
| valueSource | exactly_one_of |  |
| secret | required | name: version |
| name | required | name: mountPath |
| mountPath | required | name: subPath |
| port | required |  |
| port | required |  |
| name | required | name: secret |
| secret | exactly_one_of |  |
| secret | required | name: defaultMode |
| path | required | name: version |
| cloudSqlInstance | exactly_one_of |  |
| emptyDir | exactly_one_of |  |
| gcs | exactly_one_of |  |
| bucket | required | name: readOnly |
| readOnly | required | name: mountOptions |
| server | required | name: path |
| path | required | name: readOnly |
| readOnly | required | name: encryptionKey |
| accelerator | required | name: gpuZonalRedundancyDisabled |

## 📦 google_cloudrunv2_job

🔗 **API Reference**: https://cloud.google.com/run/docs/reference/rest/v2/projects.locations.jobs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| useDefault | conflicts | policy, name: policy |
| policy | conflicts | use_default, name: startExecutionToken |
| startExecutionToken | conflicts | run_execution_token, name: runExecutionToken |
| runExecutionToken | conflicts | start_execution_token, name: template |
| template | required |  |
| template | required |  |
| image | required | name: command |
| name | required | name: value |
| value | exactly_one_of |  |
| valueSource | exactly_one_of |  |
| secret | required | name: version |
| version | required | name: resources |
| name | required | name: mountPath |
| mountPath | required | name: subPath |
| name | required | name: value |
| name | required | name: secret |
| secret | exactly_one_of |  |
| secret | required | name: defaultMode |
| path | required | name: version |
| version | required | name: mode |
| cloudSqlInstance | exactly_one_of |  |
| emptyDir | exactly_one_of |  |
| gcs | exactly_one_of |  |
| bucket | required | name: readOnly |
| nfs | exactly_one_of |  |
| server | required | name: path |
| connector | conflicts | template.0.vpc_access.0.network_interfaces, name: egress |
| networkInterfaces | conflicts | template.0.vpc_access.0.connector |
| accelerator | required | name: gpuZonalRedundancyDisabled |

## 📦 google_chronicle_data_access_scope

🔗 **API Reference**: https://cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.dataAccessScopes

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| chronicle_dataaccessscope_with_denied_labels | required | name: instance |
| chronicle_dataaccessscope_with_denied_labels | required | name: dataAccessScopeId |
| chronicle_dataaccessscope_with_denied_labels | required |  |
| chronicle_dataaccessscope_with_denied_labels | at_least_one_of | allowed_data_access_labels, allow_all |
| chronicle_dataaccessscope_with_denied_labels | required | name: ingestionLabelValue |
| chronicle_dataaccessscope_with_denied_labels | required | name: ingestionLabelValue |

## 📦 google_chronicle_rule

🔗 **API Reference**: https://cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.rules

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| deletion_policy | required | name: instance |
| deletion_policy | required |  |

## 📦 google_chronicle_reference_list

🔗 **API Reference**: https://cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.referenceLists

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| chronicle_referencelist_basic | required | name: instance |
| chronicle_referencelist_basic | required | name: referenceListId |
| chronicle_referencelist_basic | required |  |
| chronicle_referencelist_basic | required | name: entries |
| chronicle_referencelist_basic | required |  |
| chronicle_referencelist_basic | required | name: scopeInfo |
| chronicle_referencelist_basic | required | name: ruleAssociationsCount |

## 📦 google_chronicle_data_table_row

🔗 **API Reference**: https://cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.dataTables.dataTableRows

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| chronicle_data_table_row_basic | required | name: instance |
| chronicle_data_table_row_basic | required | name: dataTableId |
| chronicle_data_table_row_basic | required | name: dataTableRow |
| chronicle_data_table_row_basic | required |  |

## 📦 google_chronicle_retrohunt

🔗 **API Reference**: https://cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.rules.retrohunts

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| chronicle_retrohunt_basic | required | name: instance |
| chronicle_retrohunt_basic | required | name: rule |
| chronicle_retrohunt_basic | required | name: retrohunt |
| chronicle_retrohunt_basic | required |  |
| chronicle_retrohunt_basic | required |  |
| chronicle_retrohunt_basic | required |  |

## 📦 google_chronicle_dashboard_chart

🔗 **API Reference**: https://cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.dashboardCharts

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required | name: timeUnit |
| None | required |  |
| None | required | name: startY |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required | name: hyperlink |
| None | required | name: description |
| None | required | name: properties |
| None | required | name: displayName |
| None | required | name: defaultSettings |
| None | required | name: customSettings |
| None | required | name: leftClickColumn |
| None | required | name: filter |
| None | required |  |
| None | required | name: filterOperatorAndValues |
| None | required |  |
| None | required | name: description |
| None | required | name: displayName |
| None | required | name: defaultSettings |
| None | required | name: customSettings |
| None | required | name: query |
| None | required | name: filter |
| None | required |  |
| None | required | name: filterOperatorAndValues |
| None | required |  |
| None | required | name: description |

## 📦 google_chronicle_watchlist

🔗 **API Reference**: https://cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.watchlists

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| chronicle_watchlist_without_id | required | name: instance |
| chronicle_watchlist_without_id | required | name: watchlistId |
| chronicle_watchlist_without_id | required |  |
| chronicle_watchlist_without_id | required | name: description |
| chronicle_watchlist_without_id | required |  |

## 📦 google_chronicle_rule_deployment

🔗 **API Reference**: https://cloud.google.com/chronicle/docs/reference/rest/v1/RuleDeployment

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| chronicle_ruledeployment_run_frequency_missing | required | name: instance |
| chronicle_ruledeployment_run_frequency_missing | required | name: rule |
| chronicle_ruledeployment_run_frequency_missing | required |  |

## 📦 google_chronicle_data_table

🔗 **API Reference**: https://cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.dataTables

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| deletion_policy | required | name: instance |
| deletion_policy | required | name: dataTableId |
| deletion_policy | required |  |
| deletion_policy | required |  |
| deletion_policy | required |  |
| deletion_policy | required | name: displayName |
| deletion_policy | required |  |

## 📦 google_chronicle_native_dashboard

🔗 **API Reference**: https://cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.nativeDashboards

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_chronicle_data_access_label

🔗 **API Reference**: https://cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.dataAccessLabels

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| chronicle_dataaccesslabel_basic | required | name: instance |
| chronicle_dataaccesslabel_basic | required | name: dataAccessLabelId |
| chronicle_dataaccesslabel_basic | required |  |
| chronicle_dataaccesslabel_basic | required | name: name |

## 📦 google_chronicle_feed

🔗 **API Reference**: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.feeds

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | exactly_one_of | details.0.anomali_settings, details.0.azure_ad_context_settings, details.0.cloud_passage_settings, details.0.cortex_xdr_settings |
| feed_service_account | exactly_one_of |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | required |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | required |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | required |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |
| feed_service_account | exactly_one_of |  |

## 📦 google_cloudscheduler_job

🔗 **API Reference**: https://cloud.google.com/scheduler/docs/reference/rest/

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| name | required |  |
| description | required | name: schedule |
| schedule | required | name: timeZone |
| timeZone | required |  |
| paused | required |  |
| attemptDeadline | required |  |
| retryConfig | required |  |
| retryCount | required |  |
| retryCount | at_least_one_of | retry_config.0.retry_count, retry_config.0.max_retry_duration, retry_config.0.min_backoff_duration, retry_config.0.max_backoff_duration |
| maxRetryDuration | required |  |
| maxRetryDuration | at_least_one_of | retry_config.0.retry_count, retry_config.0.max_retry_duration, retry_config.0.min_backoff_duration, retry_config.0.max_backoff_duration |
| minBackoffDuration | required |  |
| minBackoffDuration | at_least_one_of | retry_config.0.retry_count, retry_config.0.max_retry_duration, retry_config.0.min_backoff_duration, retry_config.0.max_backoff_duration |
| maxBackoffDuration | required |  |
| maxBackoffDuration | at_least_one_of | retry_config.0.retry_count, retry_config.0.max_retry_duration, retry_config.0.min_backoff_duration, retry_config.0.max_backoff_duration |
| maxDoublings | required |  |
| maxDoublings | at_least_one_of | retry_config.0.retry_count, retry_config.0.max_retry_duration, retry_config.0.min_backoff_duration, retry_config.0.max_backoff_duration |
| pubsubTarget | exactly_one_of | pubsub_target, http_target, app_engine_http_target |
| topicName | required | name: data |
| data | required |  |
| attributes | required | name: appEngineHttpTarget |
| appEngineHttpTarget | exactly_one_of | pubsub_target, http_target, app_engine_http_target |
| httpMethod | required | name: appEngineRouting |
| appEngineRouting | required |  |
| service | required |  |
| service | at_least_one_of | app_engine_http_target.0.app_engine_routing.0.service, app_engine_http_target.0.app_engine_routing.0.version, app_engine_http_target.0.app_engine_routing.0.instance, name: version |
| version | required |  |
| version | at_least_one_of | app_engine_http_target.0.app_engine_routing.0.service, app_engine_http_target.0.app_engine_routing.0.version, app_engine_http_target.0.app_engine_routing.0.instance, name: instance |
| instance | required |  |
| instance | at_least_one_of | app_engine_http_target.0.app_engine_routing.0.service, app_engine_http_target.0.app_engine_routing.0.version, app_engine_http_target.0.app_engine_routing.0.instance, name: relativeUri |
| relativeUri | required | name: body |
| body | required |  |
| headers | required |  |
| httpTarget | exactly_one_of | pubsub_target, http_target, app_engine_http_target |
| uri | required |  |
| httpMethod | required | name: body |
| body | required |  |
| headers | required |  |
| serviceAccountEmail | required | name: scope |
| serviceAccountEmail | required | name: audience |

## 📦 google_vmwareengine_datastore

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: name |
| None | required |  |
| None | required |  |
| None | required | name: network |
| None | required | name: servers |
| None | required |  |

## 📦 google_vmwareengine_network_peering

🔗 **API Reference**: https://cloud.google.com/compute/docs/reference/rest/v1/networks/addPeering

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_vmwareengine_subnet

🔗 **API Reference**: https://cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.privateClouds.subnets

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parent | required |  |
| name | required |  |
| ipCidrRange | required |  |

## 📦 google_vmwareengine_private_cloud

🔗 **API Reference**: https://cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.privateClouds

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| networkConfig | required |  |
| managementCidr | required | name: vmwareEngineNetwork |
| managementCluster | required |  |
| clusterId | required | name: nodeTypeConfigs |
| nodeCount | required | name: customCoreCount |
| autoscalingPolicies | required |  |
| nodeTypeId | required |  |
| scaleOutSize | required |  |
| scaleOut | required |  |
| scaleIn | required |  |
| scaleOut | required |  |
| scaleIn | required |  |
| scaleOut | required |  |
| scaleIn | required |  |

## 📦 google_vmwareengine_network

🔗 **API Reference**: https://cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.vmwareEngineNetworks

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| type | required |  |

## 📦 google_vmwareengine_cluster

🔗 **API Reference**: https://cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.privateClouds.clusters

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parent | required |  |
| name | required |  |
| nodeCount | required | name: customCoreCount |
| autoscalingPolicies | required |  |
| nodeTypeId | required |  |
| scaleOutSize | required |  |
| scaleOut | required |  |
| scaleIn | required |  |
| scaleOut | required |  |
| scaleIn | required |  |
| scaleOut | required |  |
| scaleIn | required |  |
| coolDownPeriod | required |  |
| coolDownPeriod | required |  |
| coolDownPeriod | required | name: fileShare |

## 📦 google_vmwareengine_external_address

🔗 **API Reference**: https://cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.privateClouds.externalAddresses

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parent | required |  |
| name | required |  |
| internalIp | required | name: externalIp |

## 📦 google_vmwareengine_external_access_rule

🔗 **API Reference**: https://cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.networkPolicies.externalAccessRules

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parent | required |  |
| name | required |  |
| priority | required | name: action |
| action | required |  |
| ipProtocol | required | name: sourceIpRanges |
| sourceIpRanges | required |  |
| sourcePorts | required |  |
| destinationIpRanges | required |  |
| destinationPorts | required |  |

## 📦 google_vmwareengine_network_policy

🔗 **API Reference**: https://cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.networkPolicies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| edgeServicesCidr | required | name: description |
| vmwareEngineNetwork | required |  |

## 📦 google_resourcemanager3_capability

🔗 **API Reference**: https://docs.cloud.google.com/resource-manager/reference/rest

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parent | required |  |
| capability_name | required |  |
| value | required |  |

## 📦 google_dns_response_policy

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| responsePolicyName | required |  |
| description | required |  |
| networkUrl | required |  |
| gkeClusterName | required |  |

## 📦 google_dns_policy

🔗 **API Reference**: https://cloud.google.com/dns/docs/reference/v1beta2/policies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| targetNameServers | required |  |
| ipv4Address | required | name: forwardingPath |
| description | required |  |
| scope | required |  |
| name | required | name: networks |
| networkUrl | required |  |

## 📦 google_dns_response_policy_rule

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| response_policy | required |  |
| ruleName | required |  |
| dnsName | required | name: localData |
| localData | conflicts | behavior |
| localDatas | required |  |
| name | required | name: type |
| type | required |  |
| behavior | conflicts | local_data |

## 📦 google_dns_managed_zone

🔗 **API Reference**: https://cloud.google.com/dns/api/v1/managedZones

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| description | required |  |
| dnsName | required |  |
| kind | at_least_one_of | dnssec_config.0.kind, dnssec_config.0.non_existence, dnssec_config.0.state, dnssec_config.0.default_key_specs |
| nonExistence | at_least_one_of | dnssec_config.0.kind, dnssec_config.0.non_existence, dnssec_config.0.state, dnssec_config.0.default_key_specs |
| state | at_least_one_of | dnssec_config.0.kind, dnssec_config.0.non_existence, dnssec_config.0.state, dnssec_config.0.default_key_specs |
| defaultKeySpecs | at_least_one_of | dnssec_config.0.kind, dnssec_config.0.non_existence, dnssec_config.0.state, dnssec_config.0.default_key_specs |
| name | required |  |
| privateVisibilityConfig | at_least_one_of | gke_clusters, networks |
| gkeClusterName | required | name: networks |
| networkUrl | required |  |
| targetNameServers | required |  |
| forwardingPath | exactly_one_of | ipv4_address, ipv6_address, domain_name, name: peeringConfig |
| targetNetwork | required |  |
| networkUrl | required |  |
| namespace | required |  |
| namespaceUrl | required |  |
| enableLogging | required |  |

## 📦 google_integrationconnectors_connection

🔗 **API Reference**: https://cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_integrationconnectors_endpoint_attachment

🔗 **API Reference**: https://cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.endpointAttachments

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| serviceAttachment | required |  |

## 📦 google_integrationconnectors_managed_zone

🔗 **API Reference**: https://cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.global.managedZones

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| dns | required | name: targetProject |
| targetProject | required | name: targetVpc |
| targetVpc | required |  |

## 📦 google_dataprocgdc_application_environment

🔗 **API Reference**: https://cloud.google.com/dataproc-gdc/docs/reference/rest/v1/projects.locations.applicationEnvironments

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |

## 📦 google_dataprocgdc_spark_application

🔗 **API Reference**: https://cloud.google.com/dataproc-gdc/docs/reference/rest/v1/projects.locations.serviceInstances.sparkApplications

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | exactly_one_of | pyspark_application_config, spark_application_config, spark_sql_application_config, spark_r_application_config |
| None | required | name: args |
| None | exactly_one_of | pyspark_application_config, spark_application_config, spark_sql_application_config, spark_r_application_config |
| None | exactly_one_of | pyspark_application_config, spark_application_config, spark_sql_application_config, spark_r_application_config |
| None | required | name: args |
| None | exactly_one_of | pyspark_application_config, spark_application_config, spark_sql_application_config, spark_r_application_config |
| None | required |  |

## 📦 google_dataprocgdc_service_instance

🔗 **API Reference**: https://cloud.google.com/dataproc-gdc/docs/reference/rest/v1/projects.locations.serviceInstances

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_cloudbuildv2_connection

🔗 **API Reference**: https://cloud.google.com/build/docs/api/reference/rest

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | conflicts | github_enterprise_config, gitlab_config, bitbucket_cloud_config, bitbucket_data_center_config |
| None | conflicts | github_config, gitlab_config, bitbucket_cloud_config, bitbucket_data_center_config |
| None | required |  |
| None | required |  |
| None | conflicts | github_config, github_enterprise_config, bitbucket_cloud_config, bitbucket_data_center_config |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | conflicts | github_config, github_enterprise_config, bitbucket_cloud_config, gitlab_config |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | conflicts | github_config, github_enterprise_config, gitlab_config, bitbucket_data_center_config |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_cloudbuildv2_repository

🔗 **API Reference**: https://cloud.google.com/build/docs/api/reference/rest

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parent_connection | required |  |
| name | required |  |
| remoteUri | required |  |

## 📦 google_oracledatabase_db_system

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| deletion_protection | required | name: dbSystemId |
| deletion_protection | required |  |
| deletion_protection | required | name: entitlementId |
| deletion_protection | required | name: properties |
| deletion_protection | required | name: computeModel |
| deletion_protection | required |  |
| deletion_protection | required |  |
| deletion_protection | required | name: characterSet |
| deletion_protection | required | name: dbHomeName |
| deletion_protection | required | name: state |
| deletion_protection | required | name: displayName |
| deletion_protection | required |  |
| deletion_protection | required | name: lifecycleState |
| deletion_protection | required | name: sshPublicKeys |
| deletion_protection | required |  |

## 📦 google_oracledatabase_exadb_vm_cluster

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: exadbVmClusterId |
| None | required |  |
| None | required | name: createTime |
| None | required | name: entitlementId |
| None | required | name: properties |
| None | required |  |
| None | required | name: exascaleDbStorageVault |
| None | required | name: giVersion |
| None | required | name: hostname |
| None | required |  |
| None | required | name: ociUri |
| None | required | name: sshPublicKeys |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_oracledatabase_cloud_exadata_infrastructure

🔗 **API Reference**: https://cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| cloudExadataInfrastructureId | required |  |
| shape | required | name: ociUrl |
| email | required | name: monthlyStorageServerVersion |

## 📦 google_oracledatabase_cloud_vm_cluster

🔗 **API Reference**: https://cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| cloudVmClusterId | required |  |
| exadataInfrastructure | required | name: displayName |
| licenseType | required | name: giVersion |
| cpuCoreCount | required | name: systemVersion |
| cidr | required | name: backupSubnetCidr |
| backupSubnetCidr | required | name: network |
| network | required | name: odbNetwork |

## 📦 google_oracledatabase_autonomous_database

🔗 **API Reference**: https://cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| autonomousDatabaseId | required |  |
| dbWorkload | required | name: dbEdition |
| licenseType | required | name: customerContacts |
| email | required | name: secretId |
| network | required | name: cidr |
| cidr | required | name: odbNetwork |

## 📦 google_oracledatabase_exascale_db_storage_vault

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required | name: exascaleDbStorageVaultId |
| None | required |  |
| None | required | name: entitlementId |
| None | required |  |
| None | required |  |
| None | required | name: ociUri |

## 📦 google_oracledatabase_odb_network

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| deletion_protection | required | name: odbNetworkId |
| deletion_protection | required |  |
| deletion_protection | required | name: gcpOracleZone |

## 📦 google_oracledatabase_odb_subnet

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| deletion_protection | required | name: odbnetwork |
| deletion_protection | required | name: odbSubnetId |
| deletion_protection | required |  |
| deletion_protection | required | name: createTime |
| deletion_protection | required | name: state |

## 📦 google_dataform_folder

🔗 **API Reference**: https://cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.folders

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| displayName | required | name: containingFolder |

## 📦 google_dataform_repository_workflow_config

🔗 **API Reference**: https://cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workflowConfigs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |

## 📦 google_dataform_config

🔗 **API Reference**: https://cloud.google.com/dataform/reference/rest/v1beta1/projects.locations

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |

## 📦 google_dataform_repository

🔗 **API Reference**: https://cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| url | required | name: defaultBranch |
| defaultBranch | required | name: authenticationTokenSecretVersion |
| authenticationTokenSecretVersion | exactly_one_of | gitRemoteSettings.0.authenticationTokenSecretVersion, gitRemoteSettings.0.sshAuthenticationConfig, name: sshAuthenticationConfig |
| sshAuthenticationConfig | exactly_one_of | gitRemoteSettings.0.authenticationTokenSecretVersion, gitRemoteSettings.0.sshAuthenticationConfig |
| userPrivateKeySecretVersion | required | name: hostPublicKey |
| hostPublicKey | required | name: tokenStatus |

## 📦 google_dataform_repository_release_config

🔗 **API Reference**: https://cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.releaseConfigs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |

## 📦 google_dataform_team_folder

🔗 **API Reference**: https://cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.teamFolders

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| displayName | required |  |

## 📦 google_notebooks_runtime

🔗 **API Reference**: https://cloud.google.com/ai-platform/notebooks/docs/reference/rest

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| virtualMachine | exactly_one_of | virtual_machine |
| machineType | required | name: dataDisk |
| dataDisk | required |  |
| repository | required | name: tag |
| repository | required | name: tag |

## 📦 google_notebooks_instance

🔗 **API Reference**: https://cloud.google.com/ai-platform/notebooks/docs/reference/rest

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| name | required |  |
| machineType | required |  |
| type | required |  |
| coreCount | required | name: shieldedInstanceConfig |
| consumeReservationType | required |  |
| vmImage | exactly_one_of | vm_image, container_image |
| project | required | name: imageFamily |
| containerImage | exactly_one_of | vm_image, container_image |
| repository | required | name: tag |

## 📦 google_notebooks_environment

🔗 **API Reference**: https://cloud.google.com/ai-platform/notebooks/docs/reference/rest

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| location | required |  |
| vmImage | exactly_one_of | vm_image, container_image |
| project | required | name: imageName |
| containerImage | exactly_one_of | vm_image, container_image |
| repository | required | name: tag |

## 📦 google_parametermanager_parameter_version

🔗 **API Reference**: https://cloud.google.com/secret-manager/parameter-manager/docs/reference/rest/v1/projects.locations.parameters.versions

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parameter | required |  |
| parameter_version_id | required |  |
| payload | required |  |
| parameter_data | required |  |

## 📦 google_parametermanager_parameter

🔗 **API Reference**: https://cloud.google.com/secret-manager/parameter-manager/docs/reference/rest/v1/projects.locations.parameters

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parameterId | required |  |

## 📦 google_logging_folder_settings

🔗 **API Reference**: https://cloud.google.com/logging/docs/reference/v2/rest/v2/TopLevel/getSettings

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| folder | required |  |

## 📦 google_logging_metric

🔗 **API Reference**: https://cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics/create

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required | name: description |
| description | required | name: bucketName |
| filter | required | name: metricDescriptor |
| valueType | required |  |
| metricKind | required |  |
| labels | required |  |
| key | required |  |
| description | required | name: valueType |
| valueType | required |  |
| linearBuckets | at_least_one_of | bucket_options.0.linear_buckets, bucket_options.0.exponential_buckets, bucket_options.0.explicit_buckets |
| numFiniteBuckets | required | name: width |
| width | required | name: offset |
| offset | required | name: exponentialBuckets |
| exponentialBuckets | at_least_one_of | bucket_options.0.linear_buckets, bucket_options.0.exponential_buckets, bucket_options.0.explicit_buckets |
| numFiniteBuckets | required | name: growthFactor |
| growthFactor | required | name: scale |
| scale | required | name: explicitBuckets |
| explicitBuckets | at_least_one_of | bucket_options.0.linear_buckets, bucket_options.0.exponential_buckets, bucket_options.0.explicit_buckets |
| bounds | required |  |

## 📦 google_logging_linked_dataset

🔗 **API Reference**: https://cloud.google.com/logging/docs/reference/v2/rest/v2/locations.buckets.links

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| linkId | required |  |
| bucket | required |  |

## 📦 google_logging_saved_query

🔗 **API Reference**: https://cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.savedQueries

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| parent | required |  |
| location | required |  |
| name | required |  |
| displayName | required | name: description |
| visibility | required |  |
| loggingQuery | exactly_one_of | loggingQuery, opsAnalyticsQuery |
| filter | required | name: summaryFieldStart |
| summaryFieldStart | conflicts | loggingQuery.0.summaryFieldEnd, name: summaryFieldEnd |
| summaryFieldEnd | conflicts | loggingQuery.0.summaryFieldStart, name: summaryFields |
| opsAnalyticsQuery | exactly_one_of | opsAnalyticsQuery, loggingQuery |
| sqlQueryText | required |  |

## 📦 google_logging_log_view

🔗 **API Reference**: https://cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets.views

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| bucket | required |  |
| name | required |  |

## 📦 google_logging_organization_settings

🔗 **API Reference**: https://cloud.google.com/logging/docs/reference/v2/rest/v2/TopLevel/getSettings

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| organization | required |  |

## 📦 google_logging_log_scope

🔗 **API Reference**: https://cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.logScopes

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| resourceNames | required |  |

## 📦 google_datapipeline_pipeline

🔗 **API Reference**: https://cloud.google.com/dataflow/docs/reference/data-pipelines/rest/v1/projects.locations.pipelines

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| type | required |  |
| state | required |  |
| projectId | required | name: validateOnly |
| jobName | required | name: parameters |
| projectId | required | name: launchParameter |
| launchParameter | required |  |
| jobName | required | name: parameters |
| location | required | name: validateOnly |

## 📦 google_bigquerydatatransfer_config

🔗 **API Reference**: https://cloud.google.com/bigquery/docs/reference/datatransfer/rest/v1/projects.locations.transferConfigs/create

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| displayName | required | name: name |
| dataSourceId | required |  |
| disableAutoScheduling | at_least_one_of | schedule_options.0.disable_auto_scheduling, schedule_options.0.start_time, schedule_options.0.end_time, name: startTime |
| startTime | at_least_one_of | schedule_options.0.disable_auto_scheduling, schedule_options.0.start_time, schedule_options.0.end_time, name: endTime |
| endTime | at_least_one_of | schedule_options.0.disable_auto_scheduling, schedule_options.0.start_time, schedule_options.0.end_time, name: emailPreferences |
| enableFailureEmail | required | name: notificationPubsubTopic |
| kmsKeyName | required | name: disabled |
| params | required |  |
| secretAccessKey | at_least_one_of | sensitive_params.0.secretAccessKey, sensitive_params.0.secretAccessKeyWo |
| secretAccessKey | conflicts | sensitive_params.0.secretAccessKeyWo, name: secretAccessKeyWo # Wo is convention for writeonly properties |
| secretAccessKeyWo | at_least_one_of | sensitive_params.0.secretAccessKeyWo, sensitive_params.0.secretAccessKey |
| secretAccessKeyWo | conflicts | sensitive_params.0.secretAccessKey |

## 📦 google_datacatalog_tag_template

🔗 **API Reference**: https://cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.tagTemplates

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| tagTemplateId | required |  |
| fields | required |  |
| type | required |  |
| allowedValues | required |  |
| displayName | required | name: isRequired |

## 📦 google_datacatalog_policy_tag

🔗 **API Reference**: https://cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.taxonomies.policyTags

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| taxonomy | required |  |
| displayName | required | name: description |

## 📦 google_datacatalog_entry

🔗 **API Reference**: https://cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| entryGroup | required |  |
| entryId | required |  |
| type | exactly_one_of | type, user_specified_type |
| userSpecifiedType | exactly_one_of | type, user_specified_type |
| filePatterns | required |  |

## 📦 google_datacatalog_taxonomy

🔗 **API Reference**: https://cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.taxonomies

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| displayName | required | name: description |

## 📦 google_datacatalog_entry_group

🔗 **API Reference**: https://cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| region | required |  |
| entryGroupId | required |  |

## 📦 google_datacatalog_tag

🔗 **API Reference**: https://cloud.google.com/data-catalog/docs/reference/rest/v1/projects.locations.entryGroups.tags

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| template | required |  |
| fields | required |  |

## 📦 google_osconfig_guest_policies

🔗 **API Reference**: https://cloud.google.com/compute/docs/osconfig/rest

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| guestPolicyId | required |  |
| assignment | required |  |
| groupLabels | at_least_one_of | assignment.0.group_labels, assignment.0.zones, assignment.0.instances, assignment.0.instance_name_prefixes |
| labels | required | name: zones |
| zones | at_least_one_of | assignment.0.group_labels, assignment.0.zones, assignment.0.instances, assignment.0.instance_name_prefixes |
| instances | at_least_one_of | assignment.0.group_labels, assignment.0.zones, assignment.0.instances, assignment.0.instance_name_prefixes |
| instanceNamePrefixes | at_least_one_of | assignment.0.group_labels, assignment.0.zones, assignment.0.instances, assignment.0.instance_name_prefixes |
| osTypes | at_least_one_of | assignment.0.group_labels, assignment.0.zones, assignment.0.instances, assignment.0.instance_name_prefixes |
| name | required | name: desiredState |
| uri | required | name: distribution |
| distribution | required | name: components |
| components | required |  |
| id | required | name: displayName |
| baseUrl | required | name: gpgKeys |
| id | required | name: displayName |
| baseUrl | required | name: gpgKeys |
| name | required | name: url |
| url | required | name: recipes |
| name | required | name: version |
| id | required | name: allowInsecure |
| artifactId | required | name: destination |
| destination | required | name: overwrite |
| artifactId | required | name: destination |
| type | required |  |
| artifactId | required | name: flags |
| artifactId | required | name: rpmInstallation |
| artifactId | required | name: fileExec |
| script | required | name: allowedExitCodes |
| artifactId | required | name: destination |
| destination | required | name: overwrite |
| artifactId | required | name: destination |
| type | required |  |
| artifactId | required | name: flags |
| artifactId | required | name: rpmInstallation |
| artifactId | required | name: fileExec |
| script | required | name: allowedExitCodes |

## 📦 google_osconfig_patch_deployment

🔗 **API Reference**: https://cloud.google.com/compute/docs/osconfig/rest

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | at_least_one_of | instance_filter.0.all, instance_filter.0.group_labels, instance_filter.0.zones, instance_filter.0.instances |
| None | at_least_one_of | instance_filter.0.all, instance_filter.0.group_labels, instance_filter.0.zones, instance_filter.0.instances |
| None | required |  |
| None | at_least_one_of | instance_filter.0.all, instance_filter.0.group_labels, instance_filter.0.zones, instance_filter.0.instances |
| None | at_least_one_of | instance_filter.0.all, instance_filter.0.group_labels, instance_filter.0.zones, instance_filter.0.instances |
| None | at_least_one_of | instance_filter.0.all, instance_filter.0.group_labels, instance_filter.0.zones, instance_filter.0.instances |
| None | at_least_one_of | patch_config.0.reboot_config, patch_config.0.apt, patch_config.0.yum, patch_config.0.goo |
| None | at_least_one_of | patch_config.0.reboot_config, patch_config.0.apt, patch_config.0.yum, patch_config.0.goo |
| None | at_least_one_of | patch_config.0.reboot_config, patch_config.0.apt, patch_config.0.yum, patch_config.0.goo |
| None | at_least_one_of | patch_config.0.apt.0.type, patch_config.0.apt.0.excludes, patch_config.0.apt.0.exclusive_packages |
| None | at_least_one_of | patch_config.0.apt.0.type, patch_config.0.apt.0.excludes, patch_config.0.apt.0.exclusive_packages |
| None | at_least_one_of | patch_config.0.apt.0.type, patch_config.0.apt.0.excludes, patch_config.0.apt.0.exclusive_packages |
| None | at_least_one_of | patch_config.0.reboot_config, patch_config.0.apt, patch_config.0.yum, patch_config.0.goo |
| None | at_least_one_of | patch_config.0.yum.0.security, patch_config.0.yum.0.minimal, patch_config.0.yum.0.excludes, patch_config.0.yum.0.exclusive_packages |
| None | at_least_one_of | patch_config.0.yum.0.security, patch_config.0.yum.0.minimal, patch_config.0.yum.0.excludes, patch_config.0.yum.0.exclusive_packages |
| None | at_least_one_of | patch_config.0.yum.0.security, patch_config.0.yum.0.minimal, patch_config.0.yum.0.excludes, patch_config.0.yum.0.exclusive_packages |
| None | at_least_one_of | patch_config.0.yum.0.security, patch_config.0.yum.0.minimal, patch_config.0.yum.0.excludes, patch_config.0.yum.0.exclusive_packages |
| None | at_least_one_of | patch_config.0.reboot_config, patch_config.0.apt, patch_config.0.yum, patch_config.0.goo |
| None | required |  |
| None | at_least_one_of | patch_config.0.reboot_config, patch_config.0.apt, patch_config.0.yum, patch_config.0.goo |
| None | at_least_one_of | patch_config.0.zypper.0.withOptional, patch_config.0.zypper.0.withUpdate, patch_config.0.zypper.0.categories, patch_config.0.zypper.0.severities |
| None | at_least_one_of | patch_config.0.zypper.0.withOptional, patch_config.0.zypper.0.withUpdate, patch_config.0.zypper.0.categories, patch_config.0.zypper.0.severities |
| None | at_least_one_of | patch_config.0.zypper.0.withOptional, patch_config.0.zypper.0.withUpdate, patch_config.0.zypper.0.categories, patch_config.0.zypper.0.severities |
| None | at_least_one_of | patch_config.0.zypper.0.withOptional, patch_config.0.zypper.0.withUpdate, patch_config.0.zypper.0.categories, patch_config.0.zypper.0.severities |
| None | at_least_one_of | patch_config.0.zypper.0.withOptional, patch_config.0.zypper.0.withUpdate, patch_config.0.zypper.0.categories, patch_config.0.zypper.0.severities |
| None | at_least_one_of | patch_config.0.zypper.0.withOptional, patch_config.0.zypper.0.withUpdate, patch_config.0.zypper.0.categories, patch_config.0.zypper.0.severities |
| None | at_least_one_of | patch_config.0.reboot_config, patch_config.0.apt, patch_config.0.yum, patch_config.0.goo |
| None | conflicts | patch_config.0.windows_update.0.exclusive_patches |
| None | at_least_one_of | patch_config.0.windows_update.0.classifications, patch_config.0.windows_update.0.excludes, patch_config.0.windows_update.0.exclusive_patches |
| None | conflicts | patch_config.0.windows_update.0.exclusive_patches |
| None | at_least_one_of | patch_config.0.windows_update.0.classifications, patch_config.0.windows_update.0.excludes, patch_config.0.windows_update.0.exclusive_patches |
| None | conflicts | patch_config.0.windows_update.0.classifications, patch_config.0.windows_update.0.excludes |
| None | at_least_one_of | patch_config.0.windows_update.0.classifications, patch_config.0.windows_update.0.excludes, patch_config.0.windows_update.0.exclusive_patches |
| None | at_least_one_of | patch_config.0.reboot_config, patch_config.0.apt, patch_config.0.yum, patch_config.0.goo |
| None | at_least_one_of | patch_config.0.pre_step.0.linux_exec_step_config, patch_config.0.pre_step.0.windows_exec_step_config |
| None | exactly_one_of | patch_config.0.pre_step.0.linux_exec_step_config.0.local_path, patch_config.0.pre_step.0.linux_exec_step_config.0.gcs_object, name: gcsObject |
| None | exactly_one_of | patch_config.0.pre_step.0.linux_exec_step_config.0.local_path, patch_config.0.pre_step.0.linux_exec_step_config.0.gcs_object |
| None | required |  |
| None | required |  |
| None | required |  |
| None | at_least_one_of | patch_config.0.pre_step.0.linux_exec_step_config, patch_config.0.pre_step.0.windows_exec_step_config |
| None | exactly_one_of | patch_config.0.pre_step.0.windows_exec_step_config.0.local_path, patch_config.0.pre_step.0.windows_exec_step_config.0.gcs_object, name: gcsObject |
| None | exactly_one_of | patch_config.0.pre_step.0.windows_exec_step_config.0.local_path, patch_config.0.pre_step.0.windows_exec_step_config.0.gcs_object |
| None | required |  |
| None | required |  |
| None | required |  |
| None | at_least_one_of | patch_config.0.reboot_config, patch_config.0.apt, patch_config.0.yum, patch_config.0.goo |
| None | at_least_one_of | patch_config.0.post_step.0.linux_exec_step_config, patch_config.0.post_step.0.windows_exec_step_config |
| None | exactly_one_of | patch_config.0.post_step.0.linux_exec_step_config.0.local_path, patch_config.0.post_step.0.linux_exec_step_config.0.gcs_object, name: gcsObject |
| None | exactly_one_of | patch_config.0.post_step.0.linux_exec_step_config.0.local_path, patch_config.0.post_step.0.linux_exec_step_config.0.gcs_object |
| None | required |  |
| None | required |  |
| None | required |  |
| None | at_least_one_of | patch_config.0.post_step.0.linux_exec_step_config, patch_config.0.post_step.0.windows_exec_step_config |
| None | exactly_one_of | patch_config.0.post_step.0.windows_exec_step_config.0.local_path, patch_config.0.post_step.0.windows_exec_step_config.0.gcs_object, name: gcsObject |
| None | exactly_one_of | patch_config.0.post_step.0.windows_exec_step_config.0.local_path, patch_config.0.post_step.0.windows_exec_step_config.0.gcs_object |
| None | required |  |
| None | required |  |
| None | required |  |
| None | exactly_one_of | one_time_schedule, recurring_schedule |
| None | required |  |
| None | exactly_one_of | one_time_schedule, recurring_schedule |
| None | required |  |
| None | required |  |
| None | required |  |
| None | at_least_one_of | recurring_schedule.0.time_of_day.0.hours, recurring_schedule.0.time_of_day.0.minutes, recurring_schedule.0.time_of_day.0.seconds, recurring_schedule.0.time_of_day.0.nanos |
| None | at_least_one_of | recurring_schedule.0.time_of_day.0.hours, recurring_schedule.0.time_of_day.0.minutes, recurring_schedule.0.time_of_day.0.seconds, recurring_schedule.0.time_of_day.0.nanos |
| None | at_least_one_of | recurring_schedule.0.time_of_day.0.hours, recurring_schedule.0.time_of_day.0.minutes, recurring_schedule.0.time_of_day.0.seconds, recurring_schedule.0.time_of_day.0.nanos |
| None | at_least_one_of | recurring_schedule.0.time_of_day.0.hours, recurring_schedule.0.time_of_day.0.minutes, recurring_schedule.0.time_of_day.0.seconds, recurring_schedule.0.time_of_day.0.nanos |
| None | required |  |
| None | exactly_one_of | recurring_schedule.0.monthly.0.week_day_of_month, recurring_schedule.0.monthly.0.month_day |
| None | required |  |
| None | required |  |
| None | exactly_one_of | recurring_schedule.0.monthly.0.week_day_of_month, recurring_schedule.0.monthly.0.month_day |
| None | required |  |
| None | required |  |
| None | exactly_one_of | rollout.0.disruption_budget.0.fixed, rollout.0.disruption_budget.0.percentage |
| None | exactly_one_of | rollout.0.disruption_budget.0.fixed, rollout.0.disruption_budget.0.percentage |

## 📦 google_migrationcenter_preference_set

🔗 **API Reference**: https://cloud.google.com/migration-center/docs/reference/rest/v1

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |

## 📦 google_migrationcenter_group

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| location | required |  |
| groupId | required |  |

## 📦 google_billing_project_info

🔗 **API Reference**: https://cloud.google.com/billing/docs/reference/rest/v1/projects

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |

## 📦 google_apigateway_api

🔗 **API Reference**: https://cloud.google.com/api-gateway/docs/reference/rest/v1beta/projects.locations.apis

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| apiId | required |  |

## 📦 google_apigateway_api_config

🔗 **API Reference**: https://cloud.google.com/api-gateway/docs/reference/rest/v1beta/projects.locations.apis.configs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| api | required |  |
| backendConfig | required |  |
| googleServiceAccount | required |  |
| openapiDocuments | exactly_one_of | openapi_documents, grpc_services |
| document | required |  |
| path | required |  |
| contents | required |  |
| grpcServices | exactly_one_of | openapi_documents, grpc_services |
| fileDescriptorSet | required |  |
| path | required |  |
| contents | required |  |
| path | required |  |
| contents | required |  |
| path | required |  |
| contents | required |  |

## 📦 google_apigateway_gateway

🔗 **API Reference**: https://cloud.google.com/api-gateway/docs/reference/rest/v1beta/projects.locations.apis

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| gatewayId | required |  |
| apiConfig | required |  |

## 📦 google_metastore_federation

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| federationId | required |  |
| version | required |  |
| backendMetastores | required |  |
| name | required | name: metastoreType |
| metastoreType | required |  |

## 📦 google_metastore_service

🔗 **API Reference**: https://cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| serviceId | required |  |
| tier | conflicts | scalingConfig |
| instanceSize | required |  |
| instanceSize | conflicts | tier |
| instanceSize | exactly_one_of | scaling_config.0.instance_size, scaling_config.0.scaling_factor, scaling_config.0.autoscaling_config |
| scalingFactor | required | name: autoscalingConfig |
| autoscalingConfig | required |  |
| backupLocation | required | name: deletionProtection |
| hourOfDay | required | name: dayOfWeek |
| dayOfWeek | required |  |
| kmsKey | required |  |
| version | required |  |
| keytab | required |  |
| cloudSecret | required | name: principal |
| principal | required | name: krb5ConfigGcsUri |
| krb5ConfigGcsUri | required | name: auxiliaryVersions |
| version | required | name: configOverrides |
| consumers | required |  |
| subnetwork | required | name: customRoutesEnabled |
| dataCatalogConfig | required |  |
| enabled | required | name: telemetryConfig |

## 📦 google_metastore_table

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |

## 📦 google_metastore_database

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |

## 📦 google_pubsublite_subscription

🔗 **API Reference**: https://cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.subscriptions

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| topic | required |  |
| deliveryRequirement | required |  |

## 📦 google_pubsublite_topic

🔗 **API Reference**: https://cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.topics

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| count | required | name: capacity |
| publishMibPerSec | required | name: subscribeMibPerSec |
| subscribeMibPerSec | required | name: retentionConfig |
| perPartitionBytes | required | name: period |

## 📦 google_pubsublite_reservation

🔗 **API Reference**: https://cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.reservations

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| throughputCapacity | required |  |

## 📦 google_certificatemanager_dns_authorization

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| domain | required |  |

## 📦 google_certificatemanager_certificate_map_entry

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| map | required |  |
| certificates | required |  |
| hostname | exactly_one_of | hostname, matcher, name: matcher |
| matcher | exactly_one_of | hostname, matcher |

## 📦 google_certificatemanager_certificate_map

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |

## 📦 google_certificatemanager_trust_config

🔗 **API Reference**: https://cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.trustConfigs/create

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| location | required |  |
| pemCertificate | required |  |

## 📦 google_certificatemanager_certificate

🔗 **API Reference**: https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.certificates

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |
| selfManaged | exactly_one_of | self_managed, managed |
| certificatePem | exactly_one_of | self_managed.0.certificate_pem, self_managed.0.pem_certificate |
| privateKeyPem | exactly_one_of | self_managed.0.private_key_pem, self_managed.0.pem_private_key |
| pemCertificate | exactly_one_of | self_managed.0.certificate_pem, self_managed.0.pem_certificate, name: pemPrivateKey |
| pemPrivateKey | exactly_one_of | self_managed.0.private_key_pem, self_managed.0.pem_private_key, name: managed |
| managed | exactly_one_of | self_managed, managed |

## 📦 google_certificatemanager_certificate_issuance_config

🔗 **API Reference**: https://cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.certificateIssuanceConfigs

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required | name: location |
| rotationWindowPercentage | required | name: keyAlgorithm |
| keyAlgorithm | required |  |
| lifetime | required | name: createTime |
| certificateAuthorityConfig | required |  |
| caPool | required |  |

## 📦 google_firebaseextensions_instance

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| instance_id | required |  |
| config | required |  |
| params | required | name: systemParams |
| extensionRef | required |  |

## 📦 google_dataproc_autoscaling_policy

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | at_least_one_of | secondary_worker_config.0.min_instances, secondary_worker_config.0.max_instances, secondary_worker_config.0.weight, name: maxInstances |
| None | at_least_one_of | secondary_worker_config.0.min_instances, secondary_worker_config.0.max_instances, secondary_worker_config.0.weight, name: weight |
| None | at_least_one_of | secondary_worker_config.0.min_instances, secondary_worker_config.0.max_instances, secondary_worker_config.0.weight, name: basicAlgorithm |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_dataproc_batch

🔗 **API Reference**: https://cloud.google.com/dataproc-serverless/docs/reference/rest/v1/projects.locations.batches

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | conflicts | environment_config.0.execution_config.0.subnetwork_uri, name: subnetworkUri |
| None | conflicts | environment_config.0.execution_config.0.network_uri, name: authenticationConfig |
| None | exactly_one_of | pyspark_batch, spark_batch, spark_sql_batch, spark_r_batch |
| None | exactly_one_of | pyspark_batch, spark_batch, spark_sql_batch, spark_r_batch |
| None | exactly_one_of | spark_batch.0.main_class, name: mainClass |
| None | exactly_one_of | spark_batch.0.main_jar_file_uri, name: sparkRBatch |
| None | exactly_one_of | pyspark_batch, spark_batch, spark_sql_batch, spark_r_batch |
| None | exactly_one_of | pyspark_batch, spark_batch, spark_sql_batch, spark_r_batch |

## 📦 google_dataproc_session_template

🔗 **API Reference**: https://cloud.google.com/dataproc-serverless/docs/reference/rest/v1/projects.locations.sessionTemplates

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| name | required |  |

## 📦 google_iambeta_workload_identity_pool

🔗 **API Reference**: https://cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| workloadIdentityPoolId | required |  |
| caPools | exactly_one_of | inlineCertificateIssuanceConfig.0.ca_pools, inlineCertificateIssuanceConfig.0.use_default_shared_ca |
| useDefaultSharedCa | exactly_one_of | inlineCertificateIssuanceConfig.0.ca_pools, inlineCertificateIssuanceConfig.0.use_default_shared_ca |
| trustAnchors | required |  |
| pemCertificate | required | name: attestationRules |
| googleCloudResource | required |  |

## 📦 google_iambeta_workload_identity_pool_namespace

🔗 **API Reference**: https://cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| workload_identity_pool_id | required |  |
| workload_identity_pool_namespace_id | required |  |

## 📦 google_iambeta_workload_identity_pool_provider

🔗 **API Reference**: https://cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| workloadIdentityPoolId | required |  |
| workloadIdentityPoolProviderId | required |  |
| aws | exactly_one_of | aws, oidc, saml, x509 |
| accountId | required | name: oidc |
| oidc | exactly_one_of | aws, oidc, saml, x509 |
| issuerUri | required | name: jwksJson |
| jwksJson | required |  |
| saml | exactly_one_of | aws, oidc, saml, x509 |
| idpMetadataXml | required | name: x509 |
| x509 | exactly_one_of | aws, oidc, saml, x509 |
| trustStore | required |  |
| trustAnchors | required |  |

## 📦 google_iambeta_workload_identity_pool_managed_identity

🔗 **API Reference**: https://cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| workload_identity_pool_id | required |  |
| workload_identity_pool_namespace_id | required |  |
| workload_identity_pool_managed_identity_id | required |  |
| googleCloudResource | required |  |

## 📦 google_sql_source_representation_instance

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| None | required |  |
| None | required |  |
| None | required |  |
| None | required |  |

## 📦 google_sql_database

| Property | Condition Type | Constrained Fields |
| --- | --- | --- |
| instance | required |  |
| name | required |  |

