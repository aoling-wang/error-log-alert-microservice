# Error Log Alert Service

**"Engineering Notified"** 

A lightweight Python microservice that monitors application logs, identifies critical errors, and sends real-time alerts to communication platforms such as **Discord** and **Slack** via webhooks.

<p align="center">
  <img width="485" height="300" alt="Error Log Alert Service" src="https://github.com/user-attachments/assets/9579c1a6-5bbe-4f52-9cf1-74504310b0a6" />
  <img width="332" height="300" alt="Webhook Alert" src="https://github.com/user-attachments/assets/eab46c6b-060c-44ad-835c-58ff62ae3e61" />
</p>

## Overview

This project explores how **webhooks, modular architecture, expression parsing, and microservices** can be combined to create a reusable application monitoring component. The service separates log processing, error detection, and alert delivery into distinct responsibilities, making the system easier to extend and integrate into larger applications.

The project is inspired by the roles played by cloud services such as:

* **AWS CloudWatch Logs** — log collection and monitoring
* **AWS SQS** — decoupled message processing
* **AWS SNS** — notification delivery

Rather than building a full cloud infrastructure, this project recreates the **separation of responsibility, modularity, continuous health assessment, and team notification**  at a smaller scale.

### Key Design Idea

> **Build the alerting system as a standalone module that can be attached to other applications with minimal changes.**

Webhook URLs and application configuration are supplied through environment variables, allowing the service to work with different communication platforms without changing the core application logic.

## The Stack

| Technology        | Purpose                                     |
| ----------------- | ------------------------------------------- |
| **Python**        | Application logic                           |
| **uv**            | Dependency management and project execution |
| **`re`**          | Log parsing and error detection             |
| **httpx**         | HTTP requests and webhook delivery          |
| **python-dotenv** | Environment configuration                   |
| **pytest**        | Automated testing                           |
| **Ruff**          | Linting and formatting                      |
| **ty**            | Static type checking                        |

## What I Practiced

* **Webhook integration** — connecting an application to external communication platforms
* **Modular architecture** — separating responsibilities into focused components
* **Microservice design** — building a reusable service that can operate independently
* **Environment-based configuration** — keeping deployment-specific values outside the source code
* **Log parsing** — using regular expressions to identify `ERROR` and `CRITICAL` events
* **HTTP communication** — constructing and sending structured alert payloads
* **Developer tooling** — using `uv`, pytest, Ruff, and ty as part of a Python development workflow

## Getting Started

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Install Dependencies

This project uses **uv** to manage the Python environment and dependencies.

```bash
uv sync
```

### 3. Configure Environment Variables

Create a `.env` file based on the included example:

```bash
cp .env.example .env
```

Add the appropriate webhook URL and log configuration to `.env`.

> **Reminder:** Never commit `.env` or private webhook URLs to the repository.

### 4. Run the Service

```bash
uv run python main.py
```

## Next Steps

### Intelligent Log Analysis

Integrate an LLM/NLP layer to analyze error patterns and identify potential **user pain points, recurring failures, and anomalous behavior**.

### Business Intelligence

Combine application logs with customer reviews and feedback to transform technical signals into **business insights for product and leadership teams**.

### Production Architecture

Explore additional features such as:

* LLM integration for solution generation
* Log sorting based on topic
* Authentication
* Containerization
* Observability dashboards

---

**Project Goal:** Explore how a small, modular alerting service can evolve from a developer utility into a broader platform for **application monitoring, user insight, and data-driven decision making**.

