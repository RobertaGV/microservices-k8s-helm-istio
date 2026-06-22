# M6 - Observability and Resilience

## Learning Objectives

By the end of this module you will be able to:

- Understand observability concepts
- Monitor distributed systems
- Analyze traffic between microservices
- Use Kiali for Service Mesh visualization
- Understand resiliency in distributed applications
- Identify failures and latency issues

---

## Observability

Observability is the ability to understand the internal state of a distributed system through collected data.

Modern distributed applications require observability because:

- services are distributed
- requests travel across multiple components
- failures can occur at different layers
- debugging becomes more complex

---

## Observability Components

Observability usually includes:

- metrics
- logs
- traces
- traffic visualization

These components help developers analyze system behavior.

---

## Challenges in Distributed Systems

Distributed systems introduce several operational challenges:

- network latency
- communication failures
- timeout propagation
- cascading failures
- service dependency complexity

Observability tools help detect and analyze these problems.

---

## Kiali

Kiali is an observability dashboard for Istio Service Mesh.

Kiali provides:

- service topology visualization
- traffic flow analysis
- error monitoring
- latency monitoring
- request statistics
- Service Mesh inspection

---

## Kiali Graph Visualization

Kiali displays communication between services graphically.

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

Kiali visualizes:

- requests between services
- traffic direction
- error rates
- request volume
- latency

---

## Prometheus

Prometheus is used to collect metrics from the Service Mesh.

Prometheus stores:

- request count
- latency
- traffic statistics
- service metrics

These metrics are used by Kiali and Grafana.

---

## Grafana

Grafana is used to visualize metrics through dashboards.

Grafana provides:

- charts
- traffic statistics
- latency graphs
- resource monitoring

---

## Traffic Monitoring

Istio and Kiali allow monitoring of:

- successful requests
- failed requests
- retry attempts
- timeout events
- delayed responses

This provides visibility into distributed communication.

---

## Fault Injection Analysis

The project uses Istio fault injection to simulate delays.

Example:

```yaml
fault:
  delay:
    percentage:
      value: 50
    fixedDelay: 3s
```

This configuration delays part of the traffic to test system resiliency.

Kiali visually highlights degraded communication paths.

---

## Resilience

Resilience is the ability of a distributed system to tolerate failures while continuing to operate.

The project improves resiliency through:

- retries
- timeout management
- fault isolation
- Kubernetes self-healing
- Service Mesh traffic management

---

## Retry and Timeout Policies

Retry and timeout policies improve communication reliability.

Example:

```yaml
timeout: 2s

retries:
  attempts: 3
```

These policies reduce transient communication failures.

---

## Self-Healing

Kubernetes automatically recreates failed Pods.

This improves:

- availability
- reliability
- fault tolerance

without manual intervention.

---

## mTLS Security Observability

Istio also provides visibility into secure service-to-service communication.

This allows monitoring of encrypted traffic inside the Service Mesh.

---

## Distributed System Visibility

Observability tools provide a complete view of:

- service dependencies
- communication paths
- traffic behavior
- error propagation

This is essential in large cloud-native systems.

---

## Summary

Observability and resiliency are fundamental requirements for distributed cloud-native applications.

Istio, Kiali, Prometheus and Grafana provide advanced monitoring and traffic analysis capabilities, while Kubernetes and Istio improve system resiliency through self-healing and traffic management features.# M6 - Observability and Resilience

## Learning Objectives

By the end of this module you will be able to:

- Understand observability concepts
- Monitor distributed systems
- Analyze traffic between microservices
- Use Kiali for Service Mesh visualization
- Understand resiliency in distributed applications
- Identify failures and latency issues

---

## Observability

Observability is the ability to understand the internal state of a distributed system through collected data.

Modern distributed applications require observability because:

- services are distributed
- requests travel across multiple components
- failures can occur at different layers
- debugging becomes more complex

---

## Observability Components

Observability usually includes:

- metrics
- logs
- traces
- traffic visualization

These components help developers analyze system behavior.

---

## Challenges in Distributed Systems

Distributed systems introduce several operational challenges:

- network latency
- communication failures
- timeout propagation
- cascading failures
- service dependency complexity

Observability tools help detect and analyze these problems.

---

## Kiali

Kiali is an observability dashboard for Istio Service Mesh.

Kiali provides:

- service topology visualization
- traffic flow analysis
- error monitoring
- latency monitoring
- request statistics
- Service Mesh inspection

---

## Kiali Graph Visualization

Kiali displays communication between services graphically.

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

Kiali visualizes:

- requests between services
- traffic direction
- error rates
- request volume
- latency

---

## Prometheus

Prometheus is used to collect metrics from the Service Mesh.

Prometheus stores:

- request count
- latency
- traffic statistics
- service metrics

These metrics are used by Kiali and Grafana.

---

## Grafana

Grafana is used to visualize metrics through dashboards.

Grafana provides:

- charts
- traffic statistics
- latency graphs
- resource monitoring

---

## Traffic Monitoring

Istio and Kiali allow monitoring of:

- successful requests
- failed requests
- retry attempts
- timeout events
- delayed responses

This provides visibility into distributed communication.

---

## Fault Injection Analysis

The project uses Istio fault injection to simulate delays.

Example:

```yaml
fault:
  delay:
    percentage:
      value: 50
    fixedDelay: 3s
```

This configuration delays part of the traffic to test system resiliency.

Kiali visually highlights degraded communication paths.

---

## Resilience

Resilience is the ability of a distributed system to tolerate failures while continuing to operate.

The project improves resiliency through:

- retries
- timeout management
- fault isolation
- Kubernetes self-healing
- Service Mesh traffic management

---

## Retry and Timeout Policies

Retry and timeout policies improve communication reliability.

Example:

```yaml
timeout: 2s

retries:
  attempts: 3
```

These policies reduce transient communication failures.

---

## Self-Healing

Kubernetes automatically recreates failed Pods.

This improves:

- availability
- reliability
- fault tolerance

without manual intervention.

---

## mTLS Security Observability

Istio also provides visibility into secure service-to-service communication.

This allows monitoring of encrypted traffic inside the Service Mesh.

---

## Distributed System Visibility

Observability tools provide a complete view of:

- service dependencies
- communication paths
- traffic behavior
- error propagation

This is essential in large cloud-native systems.

---

## Summary

Observability and resiliency are fundamental requirements for distributed cloud-native applications.

Istio, Kiali, Prometheus and Grafana provide advanced monitoring and traffic analysis capabilities, while Kubernetes and Istio improve system resiliency through self-healing and traffic management features.