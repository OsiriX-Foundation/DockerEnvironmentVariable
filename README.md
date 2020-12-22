## KheopsAuthorization

`KHEOPS_AUTHDB_USER` default value : kheopsuser<br>
`KHEOPS_AUTHDB_URL` default value : postgresql://authdb:5432<br>
`KHEOPS_AUTHDB_NAME` default value : kheops<br>
`KHEOPS_ROOT_URL` this env var is mandatory<br>
`KHEOPS_PACS_PEP_URL` default value : http://pacsauthorizationproxy:80<br>
`KHEOPS_OIDC_PROVIDER` this env var is mandatory<br>
`KHEOPS_CLIENT_DICOMWEBPROXYCLIENTID` default value : DICOMWebProxy<br>
`KHEOPS_CLIENT_ZIPPERCLIENTID` default value : Zipper<br>
`KHEOPS_WELCOMEBOT_WEBHOOK` this env var is optional<br>
`KHEOPS_USE_KHEOPS_SCOPE` default value : true<br>
`KHEOPS_AUTHDB_PASS_FILE` default value : /run/secrets/kheops_authdb_pass<br>
`KHEOPS_AUTH_HMASECRET_FILE` default value : /run/secrets/kheops_auth_hmasecret<br>
`KHEOPS_CLIENT_DICOMWEBPROXY_SECRET_FILE` default value : /run/secrets/kheops_client_dicomwebproxysecret<br>
`KHEOPS_CLIENT_ZIPPER_SECRET_FILE` default value : /run/secrets/kheops_client_zippersecret<br>
`KHEOPS_AUTHORIZATION_ENABLE_ELASTIC` default value : false<br>
`KHEOPS_AUTHORIZATION_ELASTIC_INSTANCE` default value : only_if_KHEOPS_AUTHORIZATION_ENABLE_ELASTIC_is_true<br>
`KHEOPS_AUTHORIZATION_LOGSTASH_URL` default value : only_if_KHEOPS_AUTHORIZATION_ENABLE_ELASTIC_is_true<br>
## KheopsNginx

`LETS_ENCRYPT_EMAIL` default value : spalte@naturalimage.ch<br>
`SECRET_FILE_PATH` default value : /run/secrets<br>
## KheopsUI

`SECRET_FILE_PATH` default value : /run/secrets<br>
`SERVER_NAME` default value : localhost<br>
## KheopsDICOMwebProxy

## KheopsZipper

## PACS_PEP

