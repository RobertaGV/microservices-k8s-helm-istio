# M3 - Kubernetes Orchestration

## Learning Objectives

By the end of this module you will be able to:

- Understand Kubernetes architecture
- Deploy applications on Kubernetes
- Use Deployments and Services
- Understand service discovery
- Scale microservices
- Understand container orchestration concepts

---

## Kubernetes

Kubernetes is an open-source container orchestration platform.

It automates:

- deployment
- scaling
- networking
- service discovery
- self-healing
- workload management

Kubernetes is the standard platform for modern cloud-native applications.

---

## Why Kubernetes

Docker Compose is useful for local development, but distributed systems require more advanced orchestration features.

Kubernetes provides:

- automatic scheduling
- fault recovery
- scalability
- rolling updates
- service discovery
- infrastructure abstraction

---

## Kubernetes Architecture

A Kubernetes cluster is composed of:

### Control Plane

Responsible for cluster management.

### Worker Nodes

Execute application workloads inside Pods.

---

## Pods

A Pod is the smallest deployable unit in Kubernetes.

A Pod contains:

- one or more containers
- networking configuration
- storage configuration

In this project, each microservice runs inside a dedicated Pod.

---

## Deployments

Deployments manage Pods automatically.

Responsibilities include:

- Pod creation
- restart after failures
- scaling
- rolling updates

Example:

```yaml
apiVersion: apps/v1
kind: Deployment

metadata:
  name: product-service
 ```

## Services

Services provide stable networking access to Pods.

Kubernetes Services enable:
- internal communication
- DNS-based service discovery
- load balancing

Example:
```
apiVersion: v1
kind: Service

metadata:
  name: order-service
```

## Service Discovery

Kubernetes automatically creates internal DNS records.

This allows services to communicate using names such as:
```
http://order-service:5001
```
instead of hardcoded IP addresses.

## Kubernetes Architecture in the Project

The project deploys three microservices:
```
frontend-service
        |
        v
order-service
        |
        v
product-service
```
Each service is deployed using:
- Deployment
- Service

## Frontend Exposure

The frontend-service uses a NodePort Service.

Example:
```
type: NodePort
```
This allows external access to the application.

## Minikube

Minikube is used to execute Kubernetes locally.

Minikube provides:
- local Kubernetes cluster
- container runtime
- networking
- testing environment

## Kubernetes Deployment Process

### Apply Kubernetes Manifests
```
kubectl apply -f kubernetes/product
kubectl apply -f kubernetes/order
kubectl apply -f kubernetes/frontend
```
### Verify Pods
```
kubectl get pods
```
### Verify Services
```
kubectl get services
```
### Scaling

Kubernetes allows horizontal scaling.

Example:
```
kubectl scale deployment order-service --replicas=3
```
This creates multiple replicas of the service.

### Self-Healing

If a Pod crashes, Kubernetes automatically recreates it.

This behavior improves system reliability and availability.

## Challenges in Distributed Systems

Distributed systems introduce additional complexity:
- latency
- network failures
- retry management
- observability
- traffic control
- secure communication

These challenges motivate the use of Helm and Istio.

## Summary

Kubernetes provides advanced orchestration capabilities for distributed applications.

It simplifies deployment, networking, scalability and workload management for cloud-native microservice architectures.