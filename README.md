### 📊 System Monitoring Pipeline  
### Flask • Prometheus • Grafana • Docker • Custom Exporter

This project implements a complete, lightweight monitoring and observability pipeline using Flask, Prometheus, Grafana, and Docker Compose. It collects host system metrics using Python (`psutil`), exposes them via a Flask API, converts them into Prometheus-formatted metrics through a custom exporter, stores them in Prometheus, and visualizes them with Grafana dashboards.

The goal of this project is to demonstrate real-world monitoring concepts: metric collection, exporters, Prometheus scraping, dashboarding, and containerized observability workflows.

-----------------------------------------------------------------------------------

## 🚀 Features
- **System Metrics Collection:** CPU, Memory, Disk, and Network usage gathered via `psutil` and exposed as JSON at `/metrics`.
- **Custom Prometheus Exporter:** Fetches JSON metrics from Flask and converts them into Prometheus metrics exposed on `9110/metrics`.
- **Prometheus Integration:** Scrapes exporter metrics and stores them in a time-series database.
- **Grafana Dashboards:** Preconfigured Prometheus datasource and visual dashboards for CPU, memory, disk, and network trends.
- **Dockerized Environment:** All components containerized and orchestrated using Docker Compose.

-----------------------------------------------------------------------------------

## 🧱 Architecture

Flask (psutil metrics)
↓ JSON /metrics
Custom Exporter
↓ Prometheus metrics
Prometheus (scrapes & stores)
↓ API
Grafana (visual dashboards)

-----------------------------------------------------------------------------------

## 🔄 Workflow
1. Flask collects system metrics using `psutil` and exposes them via `/metrics`.
2. The custom exporter pulls this JSON and translates it to Prometheus format.
3. Prometheus scrapes the exporter periodically and stores the metrics.
4. Grafana connects to Prometheus and visualizes the data on dashboards.

-----------------------------------------------------------------------------------

## 🛠 Tech Stack
- Python • Flask • psutil  
- Prometheus  
- Grafana  
- Docker & Docker Compose  
- Custom Exporter Pattern

-----------------------------------------------------------------------------------

## 📁 Folder Structure
project/
├── app
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── templates
│       └── index.html
├── docker-compose.yaml
├── exporter
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── grafana  [error opening dir]
├── graffana
│   └── provisioning
│       ├── dashboards
│       │   └── sample-dashboards.json
│       └── datasources
│           └── datasource.yaml
├── prometheus
│   └── prometheus.yaml
└── README.md
-----------------------------------------------------------------------------------

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
git clone <your-repo-url>
cd <project-folder>

### 2️⃣ Start the monitoring stack
docker compose up --build -d

### 3️⃣ Access the services

| Service | URL |
|---------|-----|
| Flask App | http://localhost:5000 |
| Flask JSON Metrics | http://localhost:5000/metrics |
| Exporter Metrics | http://localhost:9110/metrics |
| Prometheus UI | http://localhost:9090 |
| Grafana UI | http://localhost:3010 (admin/admin) |

-----------------------------------------------------------------------------------

## 📊 Prometheus Metrics Provided
These metrics become available for querying and dashboards:

device_cpu_percent
device_memory_percent
device_disk_percent
device_network_upload_bytes_per_second
device_network_download_bytes_per_second

-----------------------------------------------------------------------------------

## 📈 Grafana Dashboard
The dashboard includes:
- CPU usage trend  
- Memory usage trend  
- Disk space trend  
- Network throughput over time  

Dashboard files located under:
grafana/provisioning/dashboards/

-----------------------------------------------------------------------------------

## 🔮 Future Enhancements
- Add Alertmanager for Slack/email alerting  
- Integrate Node Exporter for deeper host monitoring  
- Add cAdvisor for container-level metrics  
- Add Loki + Promtail for log collection  
- Deploy stack to Kubernetes with Helm charts  

-----------------------------------------------------------------------------------

## 🎯 Resume Highlights
This project demonstrates:
- Strong understanding of observability & monitoring pipelines  
- Custom metrics exporter development  
- Prometheus scraping model & TSDB concepts  
- Grafana dashboard provisioning  
- Docker-based DevOps engineering  
- System metrics collection & visualization  


______________________________________________________________________________________

THANK YOU!!