# M1 - Introduction to Microservices

## Learning Objectives

By the end of this module you will be able to:

- Understand the concept of microservice architecture
- Compare monolithic and distributed systems
- Identify the advantages of microservices
- Understand service-to-service communication
- Analyze the main challenges of distributed systems

---

## Monolithic Architecture

Traditional applications are often developed as monolithic systems.

A monolithic application contains:

- user interface
- business logic
- database access
- networking logic

inside a single deployable unit.

### Advantages

- Simple initial development
- Easy deployment
- Centralized codebase

### Disadvantages

- Difficult scalability
- Poor fault isolation
- High coupling between components
- Difficult maintenance over time
- Complex deployments for large systems

---

## Microservice Architecture

Microservices split the application into multiple independent services.

Each microservice:

- performs a specific task
- can be deployed independently
- communicates through APIs
- can scale independently

---

## Advantages of Microservices

### Scalability

Each service can scale independently according to workload requirements.

### Fault Isolation

Failures inside a microservice do not necessarily affect the entire system.

### Independent Deployment

Services can be updated independently without redeploying the entire application.

### Technology Flexibility

Different services can use different technologies and frameworks.

---

## Challenges of Distributed Systems

Microservice architectures introduce new challenges:

- network latency
- service discovery
- fault tolerance
- distributed tracing
- observability
- traffic management
- secure communication

These problems require additional infrastructure components such as:

- Kubernetes
- Helm
- Service Meshes

---

## Service Communication

Microservices usually communicate through HTTP APIs or message brokers.

In this project:

```text
frontend-service
        |
        v
order-service
        |
        v
product-service
```

The frontend-service sends requests to order-service, which then communicates with product-service.

## Case Study Overview

The project implements a distributed cloud-native application composed of three services:

### frontend-service
Responsible for receiving external client requests.

### order-service
Handles order-related logic and communicates with the product-service.

### product-service
Provides product information through REST APIs.

## Cloud-Native Approach

The application follows cloud-native principles:

- containerization with Docker
- orchestration with Kubernetes
- configuration management with Helm
- service mesh integration with Istio
- observability with Kiali and Prometheus

## Summary

Microservices provide a modular and scalable architecture for modern distributed systems.

However, distributed applications require additional tools and infrastructure to manage deployment, networking, resiliency and observability.

Technologies such as Kubernetes, Helm and Istio help solve these challenges by providing orchestration, configuration management and advanced traffic control capabilities.