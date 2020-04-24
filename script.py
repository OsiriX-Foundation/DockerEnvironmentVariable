import dockerfile
import requests


dockerfile_url = {}
dockerfile_url["KheopsAuthorization"] = "https://raw.githubusercontent.com/OsiriX-Foundation/KheopsAuthorization/dev_env_var/docker/Dockerfile"
dockerfile_url["KheopsNginx"] = "https://raw.githubusercontent.com/OsiriX-Foundation/KheopsNginx/master/Dockerfile"
dockerfile_url["KheopsUI"] = "https://raw.githubusercontent.com/OsiriX-Foundation/KheopsUI/master/Dockerfile"
dockerfile_url["KheopsDICOMwebProxy"] = "https://raw.githubusercontent.com/OsiriX-Foundation/KheopsDICOMwebProxy/master/docker/Dockerfile"
dockerfile_url["KheopsZipper"] = "https://raw.githubusercontent.com/OsiriX-Foundation/KheopsZipper/master/docker/Dockerfile"
dockerfile_url["PACS_PEP"] = "https://raw.githubusercontent.com/OsiriX-Foundation/PACSProxyAuthorization/master/hosts/proxy/Dockerfile"



file='README.md'
with open(file, 'w') as filetowrite:

    for repo in dockerfile_url:
        response = requests.get(dockerfile_url[repo])

        print(repo)
        filetowrite.write("## "+repo+"\n\n")
        
        for command in dockerfile.parse_string(response.content.decode("utf-8")):
            if command.cmd == 'env':
                for i in range(0, len(command.value), 2):
                    if not str(command.value[i+1]):
                        print(str(command.value[i]) + " no default value")
                        filetowrite.write("`" + str(command.value[i]) + "` no default value"+"<br>\n")
                    else:
                        print(str(command.value[i]) + " value : " + str(command.value[i+1]))
                        filetowrite.write("`" + str(command.value[i]) + "` default value : " + str(command.value[i+1])+"<br>\n")
