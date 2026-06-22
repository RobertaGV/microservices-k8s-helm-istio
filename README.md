# Distributed Microservices with Kubernetes, Helm and Istio

## Project Overview

This project demonstrates the design and deployment of a distributed microservice architecture using modern cloud-native technologies.

The system is composed of three interoperable microservices:

* `frontend-service`
* `order-service`
* `product-service`

The application is first containerized with Docker, executed locally through Docker Compose, then deployed on Kubernetes and managed with Helm.

Istio Service Mesh is used to provide advanced traffic management, resilience, security and observability capabilities.

---

## Architecture

```text
frontend-service
        |
        v
order-service
        |
        v
product-service
```

---

## Technologies

* Python Flask
* Docker
* Docker Compose
* Kubernetes
* Minikube
* Helm
* Istio
* Kiali
* Prometheus
* Grafana

---

## Modules

* M1 - Introduction to Microservices
* M2 - Docker and Containerization
* M3 - Kubernetes Orchestration
* M4 - Helm Package Manager
* M5 - Istio Service Mesh
* M6 - Observability and Resilience

---

## Repository Structure

```text
microservices-k8s-helm-istio/
│
├── services/
│   ├── frontend-service/
│   ├── order-service/
│   └── product-service/
│
├── kubernetes/
│   ├── frontend/
│   ├── order/
│   └── product/
│
├── helm/
│   └── microservices-chart/
│
├── istio/
│   ├── gateway.yaml
│   ├── virtualservice.yaml
│   ├── destinationrule.yaml
│   ├── fault-injection.yaml
│   └── mtls.yaml
│
├── modules/
│   ├── m1-introduction/
│   ├── m2-docker/
│   ├── m3-kubernetes/
│   ├── m4-helm/
│   ├── m5-istio/
│   └── m6-observability/
│
└── screenshots/
```

---

## Execution Flow

### 1. Run with Docker Compose

Build and start the microservices locally:

```bash
docker compose up --build
```

Open the application:

```text
http://localhost:5000
```

---

### 2. Deploy on Kubernetes

Apply Kubernetes manifests:

```bash
kubectl apply -f kubernetes/product
kubectl apply -f kubernetes/order
kubectl apply -f kubernetes/frontend
```

Check resources:

```bash
kubectl get pods
kubectl get services
```

---

### 3. Deploy with Helm

Install the application using Helm:

```bash
helm install microservices-platform ./helm/microservices-chart
```

Verify the Helm release:

```bash
helm list
```

---

### 4. Enable Istio Service Mesh

Install Istio:

```bash
istioctl install --set profile=demo -y
```

Enable automatic sidecar injection:

```bash
kubectl label namespace default istio-injection=enabled
```

Restart deployments:

```bash
kubectl rollout restart deployment frontend-service
kubectl rollout restart deployment order-service
kubectl rollout restart deployment product-service
```

Verify sidecar injection:

```bash
kubectl get pods
```

Each pod should display:

```text
2/2 Running
```

---

### 5. Apply Istio Traffic Management

Apply Istio configurations:

```bash
kubectl apply -f istio/gateway.yaml
kubectl apply -f istio/virtualservice.yaml
kubectl apply -f istio/destinationrule.yaml
kubectl apply -f istio/mtls.yaml
```

---

### 6. Fault Injection Example

Apply fault injection:

```bash
kubectl apply -f istio/fault-injection.yaml
```

Remove fault injection:

```bash
kubectl delete -f istio/fault-injection.yaml
```

---

### 7. Observability with Kiali

Open the Kiali dashboard:

```bash
istioctl dashboard kiali
```

Kiali provides a graphical visualization of traffic flows and communication between microservices.

---

## Main Concepts Demonstrated

* Microservice architecture
* Containerization with Docker
* Kubernetes orchestration
* Service discovery
* Helm chart parametrization
* Service Mesh architecture
* Retry and timeout management
* Fault injection
* mTLS communication security
* Observability with Kiali

---

## Resilience and Traffic Management

Istio provides advanced traffic management capabilities such as:

* request retries
* timeout configuration
* fault injection
* traffic routing
* secure service-to-service communication

These features are implemented without modifying the application source code thanks to the Envoy sidecar proxies automatically injected into each pod.

---

## Observability

Kiali, Prometheus and Grafana are used to monitor the system.

The observability stack allows:

* visualization of service dependencies
* monitoring of request traffic
* analysis of latency and errors
* inspection of service mesh communication

---

## Final Result

The project demonstrates a complete cloud-native distributed system deployed and managed through Kubernetes, Helm and Istio Service Mesh.

The final architecture provides:

* modularity
* scalability
* resilience
* secure communication
* centralized traffic management
* observability
