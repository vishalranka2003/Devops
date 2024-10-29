import docker

client = docker.from_env()

network = client.networks.create("mynetwork", driver="bridge")

network.connect("flask-app")
network.connect("mongo")

print("Network created and containers connected.")
