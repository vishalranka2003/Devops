## Dockerized Multi-Container Web Application with MongoDB and Flask

### Overview

This project creates a multi-container Dockerized application using Flask as the backend framework and MongoDB as the database. It supports basic CRUD operations and includes Python scripts for network management and container health checks.

### Project Structure

- **`app.py`**: Main Flask application with CRUD endpoints.
- **`Dockerfile`**: Docker configuration for the Flask application.
- **`docker-compose.yml`**: Defines the multi-container environment with Flask and MongoDB.
- **`network_management.py`**: Python script to set up Docker networks and connect containers.
- **`container_management.py`**: Script to list active containers, check Flask container health, and restart if necessary.

### Features

- **Flask-based API**: Provides CRUD operations for a sample resource.
- **MongoDB Backend**: Stores data for the application.
- **Docker Networking**: Manages container communication using a custom bridge network.
- **Health Monitoring**: Python script to check and restart the Flask container if it's unhealthy.

### Requirements

- **Docker**
- **Docker Compose**
- **Python 3.x** (for running management scripts)

### Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd assignment_1
   ```

2. **Start Containers**

   - Ensure Docker and Docker Compose are installed.
   - Run the following command to build and start all containers:
     ```bash
     docker-compose up --build
     ```

3. **Test the API**
   - After starting, the Flask API will be accessible at `http://localhost:5000`.
   - Use a tool like Postman or `curl` to test the following endpoints:
     - **Create an Item**: `POST /items` with JSON body `{"name": "<item_name>"}`
     - **Get All Items**: `GET /items`
     - **Update an Item**: `PUT /items/<id>` with JSON body `{"name": "<new_name>"}`
     - **Delete an Item**: `DELETE /items/<id>`

### Project Files

#### 1. `app.py`

- Flask app for handling CRUD operations.
- Connects to MongoDB using `pymongo`.

#### 2. `Dockerfile`

- Builds a Docker image for the Flask application.
- Installs necessary dependencies like Flask and pymongo.

#### 3. `docker-compose.yml`

- Defines services for `flask-app` and `mongo`.
- Connects the services in a bridge network (`mynetwork`).

#### 4. `network_management.py`

- Creates a custom Docker network and connects both containers.

#### 5. `container_management.py`

- Lists all running containers.
- Checks Flask container health and restarts if unhealthy.

### Running Management Scripts

To manage Docker networks and monitor container health:

1. **Network Management**:

   ```bash
   python network_management.py
   ```

2. **Container Health Check**:
   ```bash
   python container_management.py
   ```

### Example Requests

Using `curl`, here are some example API requests:

- **Create an Item**

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"name": "Sample Item"}' http://localhost:5000/items
  ```

- **Get All Items**

  ```bash
  curl -X GET http://localhost:5000/items
  ```

- **Update an Item**

  ```bash
  curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Item"}' http://localhost:5000/items/<item_id>
  ```

- **Delete an Item**
  ```bash
  curl -X DELETE http://localhost:5000/items/<item_id>
  ```

### Troubleshooting

- **docker-compose not recognized**: Ensure Docker Compose is installed and added to PATH.
- **Connection Issues**: Verify that both containers are running and properly connected to the network by using `docker network inspect mynetwork`.

### License

This project is licensed under the MIT License.

---

This `README.md` should help users understand, set up, and run your Dockerized Flask and MongoDB project! Let me know if you need further adjustments.
