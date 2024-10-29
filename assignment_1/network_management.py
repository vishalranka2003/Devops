import docker

client = docker.from_env()

# Create a custom network
network = client.networks.create("mynetwork", driver="bridge")

# Connect the Flask and MongoDB containers
network.connect("flask-app")
network.connect("mongo")

print("Network created and containers connected.")
