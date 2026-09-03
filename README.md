# Automated Cloud Infrastructure & CI/CD Pipeline on AWS

## Project Overview

This project showcases a complete DevOps lifecycle implementation, transforming a manual deployment process into an automated, reliable, and secure cloud delivery workflow.
---
## Technical Implementations & Workflow

### 1. Continuous Integration & Automated Testing
* Implemented a multi-stage CI pipeline using **GitHub Actions** triggered automatically upon every commit to the main branch.
* Integrated automated unit testing using **Pytest** to validate application health, routing logic, and HTTP endpoints before any build actions take place.
* Configured workflow exit safeguards to stop the delivery lifecycle immediately if any test fails, preventing broken code from ever reaching the production environment.

### 2. Application Containerization
* Packaged the application into an isolated **Docker** image using an optimized `Dockerfile`.
* Eliminated environment inconsistencies between local development and cloud production hosts by encapsulating all dependencies, runtimes, and system configurations.
* Enabled lightweight process management, allowing fast restart cycles and isolated resource allocation on the host machine.

### 3. Cloud Provisioning & Server Management
* Provisioned an **AWS EC2** virtual compute instance running **Ubuntu Linux** as the dedicated hosting environment.
* Configured Linux user permissions, environment variables, and SSH keys for secure non-interactive deployment operations.
* Managed runtime container lifecycles on the remote server using headless shell commands executed securely from the CI/CD runner.

### 4. Reverse Proxying & Traffic Routing
* Deployed and configured **Nginx** as a reverse proxy on the host server to handle incoming public web traffic on port 80.
* Designed the internal networking scheme so Nginx forwards inbound HTTP requests locally to the Docker container listening on port 8000.
* Decoupled public traffic management from the application runtime, enhancing stability and preparing the architecture for seamless SSL/TLS integration.

### 5. Infrastructure Security & Network Hardening
* Hardened network perimeter security by configuring strict **AWS Security Groups**.
* Implemented the principle of least privilege by exposing only port 80 (HTTP) for public users and port 22 (SSH) for administrative management.
* Completely blocked the application container's internal port (8000) from direct internet exposure, protecting internal endpoints against unauthorized external scanning.

---

## Tech Stack

* **Cloud Platform:** AWS EC2, VPC Security Groups
* **Automation & CI/CD:** GitHub Actions
* **Containerization:** Docker
* **Web Server & Routing:** Nginx (Reverse Proxy)
* **Testing:** Pytest
* **Operating System & Scripting:** Ubuntu Linux, Bash
* **Application Framework:** Python, FastAPI