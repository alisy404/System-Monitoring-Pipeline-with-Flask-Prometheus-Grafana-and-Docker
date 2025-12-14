# 📊 Production-Style Monitoring Stack
### Flask • Prometheus • Grafana • Alertmanager • Node Exporter • Docker

This project implements a real-world monitoring and alerting system using Prometheus and Grafana.  
A Flask application exposes **application-level metrics**, while system-level metrics are collected using **Node Exporter**. Prometheus scrapes all metrics, Alertmanager handles alerting, and Grafana provides dashboards for visualization.

The architecture and practices used in this project closely follow industry-standard DevOps and SRE monitoring patterns.

---

## 🎯 Project Objectives
- Implement application-level monitoring using Prometheus instrumentation
- Collect host-level system metrics using Node Exporter
- Centralize metric storage and querying with Prometheus
- Enable alerting using Alertmanager
- Visualize metrics using Grafana dashboards
- Run the entire stack using Docker Compose

---

## 🧱 Architecture Overview

Flask Application
└── /metrics (Prometheus format)
↓
Prometheus
├── Scrapes Flask metrics
├── Scrapes Node Exporter metrics
└── Evaluates alert rules
↓
Alertmanager ──▶ Notifications (Webhook / Slack-ready)
↓
Grafana ──▶ Dashboards & Visualization



---

## 🔄 Monitoring Flow
1. Flask exposes application metrics (`/metrics`) using `prometheus_client`
2. Node Exporter exposes host system metrics (`/metrics`)
3. Prometheus scrapes both targets periodically
4. Alert rules are evaluated inside Prometheus
5. Alerts are routed via Alertmanager
6. Grafana queries Prometheus to visualize metrics

---

## 🛠 Tech Stack
- **Python / Flask**
- **Prometheus**
- **Grafana**
- **Alertmanager**
- **Node Exporter**
- **Docker & Docker Compose**

---

## 📁 Project Structure
prom-app/
├── app/ # Flask application
├── prometheus/ # Prometheus config & alert rules
├── alertmanager/ # Alertmanager config & templates
├── grafana/ # Grafana provisioning
├── docs/ # Operational documentation
├── docker-compose.yaml
└── README.md


---

## ⚙️ How to Run

```bash
docker compose up --build -d


🌐 Service Access
Service	URL
Flask App	    http://localhost:5000
Flask Metrics	http://localhost:5000/metrics
Node Exporter	http://localhost:9100
Prometheus	    http://localhost:9090
Grafana	        http://localhost:3010
Alertmanager	http://localhost:9093


Grafana Login:
    admin / admin


📊 Example Metrics

http_requests_total
http_request_duration_seconds
node_cpu_seconds_total
node_memory_MemAvailable_bytes

🚨 Alerting

Alert rules detect:
Application downtime
High request latency

Alertmanager is configured with a webhook receiver and can be extended to Slack, Email, or PagerDuty.


📈 Dashboards

Grafana dashboards visualize:
    HTTP request rate & latency
    CPU & memory usage
    Host-level metrics


----------------THANK YOU-----------------------