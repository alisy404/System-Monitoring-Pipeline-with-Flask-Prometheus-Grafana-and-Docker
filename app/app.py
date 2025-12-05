from flask import Flask, jsonify, render_template
import psutil
import time
import os

app = Flask(__name__)

# For network speed measurement we store previous counters/time
_prev = {
    "bytes_sent": None,
    "bytes_recv": None,
    "time": None
}

def format_bytes(n):
    # human-readable bytes
    for unit in ["B","KB","MB","GB","TB"]:
        if n < 1024.0:
            return f"{n:3.1f} {unit}"
        n /= 1024.0
    return f"{n:.1f} PB"

def get_disk_root():
    # cross-platform root mount
    return "C:\\" if os.name == "nt" else "/"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/metrics")
def metrics():
    global _prev
    # CPU usage (short sample to get an updated value)
    cpu = psutil.cpu_percent(interval=0.12)

    # Memory
    vm = psutil.virtual_memory()
    mem_total = vm.total
    mem_used = vm.used
    mem_percent = vm.percent

    # Disk (root)
    root = get_disk_root()
    try:
        du = psutil.disk_usage(root)
        disk_total = du.total
        disk_used = du.used
        disk_percent = du.percent
    except Exception:
        # fallback: first partition
        parts = psutil.disk_partitions()
        if parts:
            du = psutil.disk_usage(parts[0].mountpoint)
            disk_total = du.total
            disk_used = du.used
            disk_percent = du.percent
        else:
            disk_total = disk_used = disk_percent = 0

    # Battery
    batt = psutil.sensors_battery()
    if batt:
        battery = {
            "percent": round(batt.percent, 1),
            "secsleft": batt.secsleft,
            "power_plugged": batt.power_plugged
        }
    else:
        battery = None

    # Network speed - compute delta since last call
    now = time.time()
    net = psutil.net_io_counters()
    bytes_sent = net.bytes_sent
    bytes_recv = net.bytes_recv

    if _prev["bytes_sent"] is None:
        # first call - can't compute speed yet
        up_bps = 0.0
        down_bps = 0.0
    else:
        dt = now - _prev["time"]
        if dt <= 0:
            dt = 1e-6
        up_bps = (bytes_sent - _prev["bytes_sent"]) / dt
        down_bps = (bytes_recv - _prev["bytes_recv"]) / dt

    # store for next time
    _prev["bytes_sent"] = bytes_sent
    _prev["bytes_recv"] = bytes_recv
    _prev["time"] = now

    return jsonify({
        "cpu_percent": round(cpu, 1),
        "memory": {
            "total": mem_total,
            "used": mem_used,
            "percent": mem_percent,
            "human_total": format_bytes(mem_total),
            "human_used": format_bytes(mem_used)
        },
        "disk": {
            "total": disk_total,
            "used": disk_used,
            "percent": disk_percent,
            "human_total": format_bytes(disk_total),
            "human_used": format_bytes(disk_used)
        },
        "battery": battery,
        "network": {
            "upload_Bps": up_bps,
            "download_Bps": down_bps,
            "upload_human_s": f"{format_bytes(up_bps)}/s",
            "download_human_s": f"{format_bytes(down_bps)}/s"
        },
        "timestamp": now
    })

if __name__ == "__main__":
    # Initialize prev values to avoid huge first delta
    n = psutil.net_io_counters()
    _prev["bytes_sent"] = n.bytes_sent
    _prev["bytes_recv"] = n.bytes_recv
    _prev["time"] = time.time()
    # Run app
    app.run(host="0.0.0.0", port=5000, debug=True)
