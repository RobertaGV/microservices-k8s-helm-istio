# M4 - Helm Package Manager

## Learning Objectives

By the end of this module you will be able to:

- Understand Helm architecture
- Create Helm charts
- Parameterize Kubernetes deployments
- Manage application releases
- Simplify Kubernetes application deployment

---

## Helm

Helm is the package manager for Kubernetes.

Helm simplifies the deployment and management of Kubernetes applications through reusable packages called Charts.

Helm helps developers manage:

- configuration
- versioning
- upgrades
- rollbacks
- reusable deployments

---

## Why Helm

Managing Kubernetes applications manually becomes difficult when systems grow.

Without Helm:

- many YAML files must be maintained
- configurations are duplicated
- deployments become difficult to manage
- updates become error-prone

Helm solves these issues through parametrized templates.

---

## Helm Charts

A Helm Chart is a collection of files describing a Kubernetes application.

The project uses the following structure:

```text
microservices-chart/
│
├── Chart.yaml
├── values.yaml
└── templates/
```

---

## Chart.yaml

`Chart.yaml` contains metadata about the application.

Example:

```yaml
apiVersion: v2
name: microservices-chart
description: A Helm chart for a distributed microservices platform
version: 0.1.0
```

---

## values.yaml

`values.yaml` contains configurable parameters.

Example:

```yaml
frontend:
  replicas: 1
  port: 5000
```

This allows configuration changes without modifying templates directly.

---

## Templates

The `templates/` directory contains parametrized Kubernetes manifests.

Example:

```yaml
name: {{ .Values.frontend.name }}
```

Helm replaces template variables using values from `values.yaml`.

---

## Helm in the Project

The project uses Helm to deploy:

- frontend-service
- order-service
- product-service

through a single reusable chart.

---

## Helm Installation

The application is installed using:

```bash
helm install microservices-platform ./helm/microservices-chart
```

This command deploys the entire distributed application.

---

## Release Management

Helm introduces the concept of Releases.

A Release represents an installed instance of a Helm Chart.

This allows:

- upgrades
- rollback
- version tracking

---

## Helm Upgrade

Applications can be updated using:

```bash
helm upgrade microservices-platform ./helm/microservices-chart
```

---

## Helm Rollback

Helm supports rollback to previous versions.

Example:

```bash
helm rollback microservices-platform 1
```

This improves deployment reliability.

---

## Advantages of Helm

### Reusability

Templates can be reused across environments.

### Maintainability

Configuration is centralized inside `values.yaml`.

### Scalability

Large deployments become easier to manage.

### Automation

Helm simplifies CI/CD workflows.

---

## Challenges Solved by Helm

Helm reduces:

- duplicated configuration
- deployment complexity
- manual YAML management
- configuration inconsistency

---

## Summary

Helm simplifies Kubernetes application deployment through reusable and parametrized templates.

It improves maintainability, scalability and deployment management in cloud-native distributed systems.