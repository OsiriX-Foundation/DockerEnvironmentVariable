## KheopsAuthorization

env_var : `SECRET_FILE_PATH` default value : /run/secrets<br>
env_var : `REPLACE_FILE_PATH` default value : /usr/local/tomcat/conf/context.xml<br>
env_var : `KHEOPS_AUTHDB_USER` default value : kheopsuser<br>
env_var : `KHEOPS_AUTHDB_URL` default value : postgresql://authdb:5432<br>
env_var : `KHEOPS_AUTHDB_NAME` default value : kheops<br>
env_var : `KHEOPS_ROOT_URL` default value : ""<br>
env_var : `KHEOPS_PACS_PEP_HOST` default value : pacsauthorizationproxy<br>
env_var : `KHEOPS_PACS_PEP_PORT` default value : 80<br>
env_var : `KHEOPS_OIDC_PROVIDER` default value : ""<br>
env_var : `KHEOPS_CLIENT_DICOMWEBPROXYCLIENTID` default value : DICOMWebProxy<br>
env_var : `KHEOPS_CLIENT_ZIPPERCLIENTID` default value : Zipper<br>
env_var : `KHEOPS_WELCOMEBOT_WEBHOOK` default value : ""<br>
env_var : `KHEOPS_USE_KHEOPS_SCOPE` default value : ""<br>
## KheopsNginx

env_var : `SECRET_FILE_PATH` default value : /run/secrets<br>
## KheopsUI

env_var : `SECRET_FILE_PATH` default value : /run/secrets<br>
env_var : `SERVER_NAME` default value : localhost<br>
## KheopsDICOMwebProxy

env_var : `SECRET_FILE_PATH` default value : /run/secrets<br>
env_var : `REPLACE_FILE_PATH` default value : /usr/local/tomcat/conf/context.xml<br>
## KheopsZipper

env_var : `SECRET_FILE_PATH` default value : /run/secrets<br>
env_var : `REPLACE_FILE_PATH` default value : /usr/local/tomcat/conf/context.xml<br>
## PACS_PEP

env_var : `OPENRESTY_VERSION` default value : 1.9.3.1<br>
env_var : `OPENRESTY_PREFIX` default value : /opt/openresty<br>
env_var : `NGINX_PREFIX` default value : /opt/openresty/nginx<br>
env_var : `VAR_PREFIX` default value : /var/nginx<br>
