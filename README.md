# AI Log Summarizer

A simple Python project that uses OpenAI GPT models to turn raw logs into incident insights.
Think of it as your AI-powered junior on-call buddy, always ready to summarize, categorize, and suggest next steps.

## Features

- Reads plain text log files (sample_logs.txt)
- Summarizes errors, warnings, critical events
- Groups by severity and creates an incident timeline
- Suggests RCA hints + next actions



## Example
### Input (sample_logs.txt)
2025-09-19 09:32:15 ERROR Failed to connect to DB
2025-09-19 09:32:17 WARN Retry attempt 1
2025-09-19 09:32:20 ERROR Failed to connect to DB
2025-09-19 09:32:25 CRITICAL DB connection timeout



### AI Generated Summary

AI Summary:
**Incident Summary: Database Connection Failure**
- ERROR: 2 occurrences of DB connection failure.
- WARN: 1 retry attempt.
- CRITICAL: Timeout logged.

Action Required: Immediate investigation of DB connectivity.



## Setup

1. Clone repo
``` 
   git clone https://github.com/iqbalintouch/ai-sre-log-summarizer.git
   cd ai-sre-log-summarizer

2. Create virtual environment

python -m venv venv
``` 
    .\venv\Scripts\activate.bat   # Windows PowerShell
    source venv/bin/activate      # Linux/Mac

3. Install dependencies
pip install -r requirements.txt

4. Add your API key
``` 
    copy .env.example .env   # Windows
    cp .env.example .env     # Linux/Mac

Edit .env and paste your OpenAI API key


## Usage
Run the summarizer:
python log_summarizer.py

Change the input logs:
- Edit sample_logs.txt with your own Splunk/Grafana logs.
- Run again to get updated AI summaries.


## Notes
- .env is ignored via .gitignore → your API key stays private.
- This is an educational demo, not production-hardened.