## KheopsAuthorization

`KHEOPS_AUTHDB_USER` default value : kheopsuser<br>
`KHEOPS_AUTHDB_URL` default value : postgresql://authdb:5432<br>
`KHEOPS_AUTHDB_NAME` default value : kheops<br>
`KHEOPS_ROOT_URL` this env var is mandatory<br>
`KHEOPS_PACS_PEP_URL` default value : http://pacsauthorizationproxy:80<br>
`KHEOPS_OIDC_PROVIDER` this env var is mandatory<br>
`KHEOPS_CLIENT_DICOMWEBPROXYCLIENTID` default value : DICOMWebProxy<br>
`KHEOPS_CLIENT_ZIPPERCLIENTID` default value : Zipper<br>
`KHEOPS_WELCOMEBOT_WEBHOOK` this env var is obtional<br>
`KHEOPS_USE_KHEOPS_SCOPE` default value : true<br>
## KheopsNginx

`SECRET_FILE_PATH` default value : /run/secrets<br>
## KheopsUI

`SECRET_FILE_PATH` default value : /run/secrets<br>
`SERVER_NAME` default value : localhost<br>
## KheopsDICOMwebProxy

`SECRET_FILE_PATH` default value : /run/secrets<br>
`REPLACE_FILE_PATH` default value : /usr/local/tomcat/conf/context.xml<br>
## KheopsZipper

`SECRET_FILE_PATH` default value : /run/secrets<br>
`REPLACE_FILE_PATH` default value : /usr/local/tomcat/conf/context.xml<br>
## PACS_PEP

`OPENRESTY_VERSION` default value : 1.9.3.1<br>
`OPENRESTY_PREFIX` default value : /opt/openresty<br>
`NGINX_PREFIX` default value : /opt/openresty/nginx<br>
`VAR_PREFIX` default value : /var/nginx<br>
