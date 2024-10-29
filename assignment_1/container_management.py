import docker

client = docker.from_env()

# List all containers
def list_containers():
    containers = client.containers.list()
    for container in containers:
        print(f"Container: {container.name}, Status: {container.status}")

# Health check for Flask container
def check_flask_health():
    container = client.containers.get("flask-app")
    if container.status != "running":
        print("Flask container is not healthy. Restarting...")
        container.restart()
        print("Flask container restarted.")
    else:
        print("Flask container is healthy.")

if __name__ == "__main__":
    list_containers()
    check_flask_health()
