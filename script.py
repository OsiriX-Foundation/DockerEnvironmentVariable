import dockerfile
import requests


dockerfile_url = {}
dockerfile_url["KheopsAuthorization"] = "https://raw.githubusercontent.com/OsiriX-Foundation/KheopsAuthorization/master/docker/Dockerfile"
dockerfile_url["KheopsNginx"] = "https://raw.githubusercontent.com/OsiriX-Foundation/KheopsNginx/master/Dockerfile"


file='README.md'
with open(file, 'w') as filetowrite:

    for repo in dockerfile_url:
        response = requests.get(dockerfile_url[repo])

        for command in dockerfile.parse_string(response.content.decode("utf-8")):
            if command.cmd == 'env':

                print(repo)
                filetowrite.write("## "+repo+"\n\n")
                for i in range(0, len(command.value), 2):
                    if not str(command.value[i+1]):
                        print("env_var : " + str(command.value[i]) + " no default value")
                        filetowrite.write("env_var : `" + str(command.value[i]) + "` no default value"+"<br>\n")
                    else:
                        print("env_var : " + str(command.value[i]) + " value : " + str(command.value[i+1]))
                        filetowrite.write("env_var : `" + str(command.value[i]) + "` default value : " + str(command.value[i+1])+"<br>\n")
