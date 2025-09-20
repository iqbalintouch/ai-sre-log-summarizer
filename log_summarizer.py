import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Sample logs (replace with your own later)
logs = """
2025-09-19 09:32:15 ERROR Failed to connect to DB
2025-09-19 09:32:17 WARN Retry attempt 1
2025-09-19 09:32:20 ERROR Failed to connect to DB
2025-09-19 09:32:25 CRITICAL DB connection timeout
"""

# Call GPT model
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are an SRE assistant. Summarize logs for incident triage."},
        {"role": "user", "content": logs}
    ]
)

print("AI Generated Summary:\n")
print(response.choices[0].message.content)
