# M2 - Docker and Containerization

## Learning Objectives

By the end of this module you will be able to:

- Understand containerization concepts
- Use Docker to package applications
- Build Docker images
- Execute containers
- Use Docker Compose to orchestrate multiple services locally

---

## Containerization

Containerization is a lightweight virtualization technology used to package applications together with their dependencies.

A container includes:

- application code
- runtime
- libraries
- dependencies
- configuration files

This guarantees that the application behaves consistently across different environments.

---

## Advantages of Containers

### Portability

Containers can run consistently on different machines and operating systems.

### Isolation

Each container runs in an isolated environment.

### Lightweight Execution

Containers share the host operating system kernel and require fewer resources compared to virtual machines.

### Scalability

Containers can be replicated easily to support larger workloads.

---

## Docker

Docker is the most widely used container platform.

Docker allows developers to:

- build container images
- execute containers
- distribute applications
- simplify deployment

---

## Dockerfile

A Dockerfile defines how a Docker image is built.

Example:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]
```

This Dockerfile:
- uses a Python base image
- installs dependencies
- copies the application source code
- starts the Flask application

## Microservices Containerization

Each microservice in the project is containerized independently.

The project contains:
- frontend-service
- order-service
- product-service

Each service has:
- `app.py`
- `requirements.txt`
- `Dockerfile`

This allows independent execution and deployment.

## Docker Compose

Docker Compose is used to orchestrate multiple containers locally.

The project uses the following architecture:
```
frontend-service
        |
        v
order-service
        |
        v
product-service
```
Docker Compose automatically creates:
- networking
- service discovery
- container startup order

## Docker Compose Configuration

Example:

```
services:

  product-service:
    build: ./services/product-service

  order-service:
    build: ./services/order-service

  frontend-service:
    build: ./services/frontend-service
```

## Local Execution

The application can be executed locally using:
```
docker compose up --build
```
This command:
- builds all images
- creates the containers
- starts the distributed application

## Service Communication

Docker Compose automatically creates an internal network.

This allows services to communicate using service names.

Example:
```
http://order-service:5001
```
Instead of using IP addresses, services use DNS-based service discovery.

## Challenges of Docker Compose

Docker Compose is useful for local development but has limitations:
- limited scalability
- no advanced orchestration
- no automatic self-healing
- no advanced traffic management
- difficult management in large distributed systems

These limitations motivate the adoption of Kubernetes.

## Summary

Docker simplifies application deployment through containerization.

Docker Compose allows local orchestration of multiple services and simplifies microservice development.

However, production-grade distributed systems require more advanced orchestration tools such as Kubernetes.