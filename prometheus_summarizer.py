"""
Prometheus Summarizer
--------------------------
Author: Iqbal
Purpose: Fetch CPU, Memory, and Disk metrics from Prometheus and summarize them using OpenAI.
"""

import os
import requests
import json
from dotenv import load_dotenv
from openai import OpenAI

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Prometheus API endpoint
PROM_URL = "http://localhost:9090/api/v1/query"

# Step 1: Define queries for node health
# ⚠️ NOTE: Running on Docker Desktop (local lab) comes with quirks:
#   - CPU usage may show negative values because Prometheus irate() has too little history.
#   - Memory query here reports "available %" (you can flip it to "used %" if preferred).
#   - Disk mountpoints like "/" may not exist; node-exporter inside Docker only sees
#       /etc/hosts, /etc/hostname, /etc/resolv.conf.
#
# ✅ In a real VM or Kubernetes node-exporter setup, these queries will return normal,
#    meaningful CPU/Memory/Disk stats.
queries = {
    "CPU Usage": '100 - (avg by(instance)(irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)',
    "Memory Usage": '(node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) * 100',
    "Disk Usage": '(node_filesystem_size_bytes - node_filesystem_free_bytes) / node_filesystem_size_bytes * 100'
}

results = {}

# Step 2: Fetch metrics from Prometheus
for name, query in queries.items():
    try:
        response = requests.get(PROM_URL, params={'query': query})
        data = response.json()
        results[name] = data
    except Exception as e:
        results[name] = {"error": str(e)}

# Step 3: Format results for AI
metrics_text = json.dumps(results, indent=2)

# Step 4: Send to OpenAI for summarization
ai_response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system",
            "content": "You are an SRE assistant. Summarize node health (CPU, memory, disk) clearly and concisely."},
        {"role": "user", "content": metrics_text}
    ]
)

# Step 5: Print AI summary
print("AI Generated Summary:\n")
print(ai_response.choices[0].message.content)
