import docker
client = docker.from_env()
print(client.containers.run("ubuntu", "echo Hello Mundo"))

