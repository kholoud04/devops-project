# Automated Cloud Infrastructure & CI/CD Pipeline on AWS

## Project Overview

This project implements an end-to-end DevOps workflow delivering a containerized web application to Amazon Web Services (AWS). It focuses on core cloud engineering practices: Infrastructure as Code (IaC), automated testing, continuous integration and deployment (CI/CD), containerization, and reverse proxy networking.

---

## Technical Implementations & Architecture

### 1. Infrastructure as Code (IaC) with Terraform
* Provisioned cloud infrastructure on **AWS** declaratively using **Terraform**.
* Automated the lifecycle of compute resources (**AWS EC2**) and firewall rules (**AWS Security Groups**), tracking infrastructure state via `terraform.tfstate`.

### 2. Infrastructure Security & Network Hardening
* Implemented the principle of least privilege using automated Security Groups to restrict inbound access strictly to port 80 (HTTP) and port 22 (SSH).
* Blocked internal container ports (8000) from public exposure, ensuring the application is accessible solely through the reverse proxy.

### 3. Application Containerization
* Containerized the backend service using **Docker** to ensure complete environment consistency between local development and cloud production.
* Handled environment variables, dependencies, and process isolation within a standardized container lifecycle.

### 4. Reverse Proxying & Traffic Routing
* Deployed and configured **Nginx** on the Ubuntu host as the primary ingress controller.
* Intercepted incoming HTTP traffic on port 80 and securely routed requests internally to the Docker container listening on port 8000.

### 5. Continuous Integration & Continuous Deployment (CI/CD)
* Built an automated **GitHub Actions** pipeline triggered on every commit to the repository.
* Integrated automated unit testing using **Pytest** to validate API endpoints prior to deployment.
* Executed automated zero-downtime updates on the EC2 host via encrypted SSH commands upon successful test runs.

---

## Tech Stack

* **Infrastructure as Code (IaC):** Terraform
* **Cloud Platform:** AWS (EC2, Security Groups)
* **CI/CD Automation:** GitHub Actions
* **Containerization:** Docker
* **Web Server & Routing:** Nginx (Reverse Proxy)
* **Testing & Backend:** Pytest, Python, FastAPI
* **Operating System & Scripting:** Ubuntu Linux, Bash