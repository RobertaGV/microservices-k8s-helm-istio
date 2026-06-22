# M5 - Istio Service Mesh

## Learning Objectives

By the end of this module you will be able to:

- Understand the concept of Service Mesh
- Understand Istio architecture
- Configure traffic management
- Apply retry and timeout policies
- Use fault injection
- Configure mTLS communication
- Understand observability in distributed systems

---

## Service Mesh

A Service Mesh is an infrastructure layer dedicated to managing communication between microservices.

The Service Mesh handles:

- traffic management
- security
- observability
- resiliency
- service-to-service communication

without modifying application source code.

---

## Why a Service Mesh

Distributed systems introduce complex networking challenges:

- network failures
- retry handling
- latency management
- timeout configuration
- secure communication
- observability

Managing these features directly inside application code increases complexity.

A Service Mesh centralizes these responsibilities.

---

## Istio

Istio is one of the most widely used Service Mesh platforms for Kubernetes.

Istio extends Kubernetes with advanced networking capabilities.

Main features include:

- traffic routing
- retry policies
- timeout management
- fault injection
- observability
- mTLS security

---

## Istio Architecture

Istio is composed of:

### Control Plane

Responsible for configuration and policy management.

### Data Plane

Composed of Envoy sidecar proxies injected into application Pods.

---

## Sidecar Proxy

Istio automatically injects an Envoy proxy next to each microservice container.

Example:

```text
frontend-service Pod
├── frontend-service container
└── Envoy sidecar proxy
```

This architecture allows Istio to intercept and manage all network traffic.

---

## Sidecar Injection

Automatic sidecar injection is enabled using:

```bash
kubectl label namespace default istio-injection=enabled
```

After restarting deployments, Pods display:

```text
2/2 Running
```

The two containers are:

- application container
- Envoy sidecar proxy

---

## Traffic Management

Istio controls communication between services through VirtualServices and DestinationRules.

This allows advanced traffic routing and resiliency policies.

---

## VirtualService

A VirtualService defines traffic routing rules.

Example:

```yaml
timeout: 2s

retries:
  attempts: 3
  perTryTimeout: 1s
```

This configuration introduces:

- request timeout
- automatic retry handling

---

## Retry Management

Retries improve resiliency when transient failures occur.

Istio automatically retries failed requests without modifying application code.

Advantages:

- improved reliability
- reduced transient failures
- improved fault tolerance

---

## Timeout Management

Timeouts prevent requests from hanging indefinitely.

Example:

```yaml
timeout: 2s
```

This improves system responsiveness and stability.

---

## Fault Injection

Istio allows simulation of failures and delays.

Example:

```yaml
fault:
  delay:
    percentage:
      value: 50
    fixedDelay: 3s
```

This configuration delays 50% of requests by 3 seconds.

Fault injection is useful for:

- resiliency testing
- chaos engineering
- distributed system validation

---

## mTLS Security

Istio supports automatic mutual TLS authentication between services.

Example:

```yaml
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
```

mTLS provides:

- encrypted communication
- service authentication
- secure service-to-service traffic

without modifying application code.

---

## Istio in the Project

The project uses Istio to provide:

- retry policies
- timeout configuration
- fault injection
- secure communication
- traffic observability

for the following services:

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

## Gateway

Istio Gateways expose services outside the cluster.

Example:

```yaml
kind: Gateway
```

The Gateway controls incoming traffic into the Service Mesh.

---

## DestinationRule

DestinationRules configure traffic policies.

Example features include:

- connection pooling
- circuit breaking
- outlier detection

These improve distributed system stability.

---

## Challenges Solved by Istio

Istio helps solve:

- traffic management complexity
- resiliency implementation
- secure communication
- distributed observability
- fault simulation

without changing application logic.

---

## Summary

Istio extends Kubernetes with advanced Service Mesh capabilities.

It provides centralized traffic management, resiliency, observability and security for distributed cloud-native applications.