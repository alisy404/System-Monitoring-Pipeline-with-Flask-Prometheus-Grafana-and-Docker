import os
import time
import requests
from prometheus_client import start_http_server, Gauge

TARGET = os.environ.get("TARGET", "http://flask-app:5000/metrics")
SCRAPE_INTERVAL = float(os.environ.get("SCRAPE_INTERVAL", "5"))

cpu_g = Gauge("device_cpu_percent", "CPU percent")
mem_total_g = Gauge("device_memory_total_bytes", "Memory total bytes")
mem_used_g = Gauge("device_memory_used_bytes", "Memory used bytes")
mem_percent_g = Gauge("device_memory_percent", "Memory percent")
disk_total_g = Gauge("device_disk_total_bytes", "Disk total bytes")
disk_used_g = Gauge("device_disk_used_bytes", "Disk used bytes")
disk_percent_g = Gauge("device_disk_percent", "Disk percent")
net_up_g = Gauge("device_network_upload_bytes_per_second", "Network upload Bps")
net_down_g = Gauge("device_network_download_bytes_per_second", "Network download Bps")
battery_percent_g = Gauge("device_battery_percent", "Battery percent")
timestamp_g = Gauge("device_metrics_timestamp_seconds", "Metrics timestamp")

def scrape_and_set():
    try:
        res = requests.get(TARGET, timeout=3)
        data = res.json()
    except Exception as e:
        print("Scrape error:", e)
        return

    cpu_g.set(data.get("cpu_percent", 0))

    mem = data.get("memory", {})
    mem_total_g.set(mem.get("total", 0))
    mem_used_g.set(mem.get("used", 0))
    mem_percent_g.set(mem.get("percent", 0))

    disk = data.get("disk", {})
    disk_total_g.set(disk.get("total", 0))
    disk_used_g.set(disk.get("used", 0))
    disk_percent_g.set(disk.get("percent", 0))

    net = data.get("network", {})
    net_up_g.set(net.get("upload_Bps", 0))
    net_down_g.set(net.get("download_Bps", 0))

    batt = data.get("battery")
    if batt and isinstance(batt, dict):
        battery_percent_g.set(batt.get("percent", 0))
    else:
        battery_percent_g.set(0)

    timestamp_g.set(data.get("timestamp", time.time()))


if __name__ == "__main__":
    start_http_server(9110)
    print("Exporter running on :9110")
    while True:
        scrape_and_set()
        time.sleep(SCRAPE_INTERVAL)
