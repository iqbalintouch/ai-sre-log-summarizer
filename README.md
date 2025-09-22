# AI Log Summarizer

A simple Python project that uses OpenAI GPT models to turn raw logs into incident insights.  
Think of it as your AI-powered junior on-call buddy, always ready to summarize, categorize, and suggest next steps.

## Features

- Reads plain text log files (`sample_logs.txt`)
- Summarizes errors, warnings, critical events
- Groups by severity and creates an incident timeline
- Suggests RCA hints + next actions

## Example

### Input (`sample_logs.txt`)
2025-09-19 09:32:15 ERROR Failed to connect to DB
2025-09-19 09:32:17 WARN Retry attempt 1
2025-09-19 09:32:20 ERROR Failed to connect to DB
2025-09-19 09:32:25 CRITICAL DB connection timeout

### AI Generated Summary
AI Summary:
Incident Summary: Database Connection Failure

ERROR: 2 occurrences of DB connection failure.
WARN: 1 retry attempt.
CRITICAL: Timeout logged.
Action Required: Immediate investigation of DB connectivity.


## Setup

1. Clone repo
```bash
git clone https://github.com/iqbalintouch/ai-sre-log-summarizer.git
cd ai-sre-log-summarizer
Create virtual environment

python -m venv venv
.\venv\Scripts\activate.bat   # Windows PowerShell

source venv/bin/activate      # Linux/Mac
Install dependencies

pip install -r requirements.txt
Add your API key

copy .env.example .env   # Windows
cp .env.example .env     # Linux/Mac

Edit .env and paste your OpenAI API key

Usage (Log Summarizer)
Run the summarizer:


python log_summarizer.py
Change the input logs:

Edit sample_logs.txt with your own Splunk/Grafana logs.

Run again to get updated AI summaries.

Prometheus Summarizer
This script (prometheus_summarizer.py) connects to a local Prometheus instance, runs a few standard queries (CPU, memory, disk), and uses OpenAI to generate a human-friendly health summary.

Example Usage

python prometheus_summarizer.py
Example Output

AI Generated Summary:

### Node Health Summary
- CPU Usage: ~8% (healthy)
- Memory Usage: ~72% available
- Disk Usage: ~64% used on /etc/hosts
Overall system health looks fine with no critical issues.
⚠️ Note on Docker Desktop
Since this lab is running on Docker Desktop with node-exporter inside a container, some metrics may look unusual:

- CPU usage may sometimes appear negative (due to irate() with limited history).
- Memory is reported as "available %" instead of "used %".
- Disk mountpoints like / are not visible; only /etc/hosts, /etc/hostname, /etc/resolv.conf show up.

✅ On a real VM or Kubernetes cluster with node-exporter, these queries will return normal system metrics.

Notes
.env is ignored via .gitignore → your API key stays private.
This is an educational demo, not production-hardened.