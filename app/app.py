from flask import Flask, Response, render_template, request
from prometheus_client import Counter, Histogram, generate_latest
import time

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint"]
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "Request latency",
    ["endpoint"]
)

@app.before_request
def before():
    request.start_time = time.time()

@app.after_request
def after(response):
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.path
    ).inc()

    REQUEST_LATENCY.labels(
        endpoint=request.path
    ).observe(time.time() - request.start_time)

    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
