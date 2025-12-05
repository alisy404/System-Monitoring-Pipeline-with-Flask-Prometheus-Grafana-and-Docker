FROM python:3.11-slim

WORKDIR /exporter

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
EXPOSE 9110

CMD ["python", "app.py"]
