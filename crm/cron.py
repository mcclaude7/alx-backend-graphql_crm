import logging
from datetime import datetime
import requests

def log_crm_heartbeat():
    try:
        # Optional: Check GraphQL endpoint responsiveness via hello query
        url = 'http://localhost:8000/graphql'
        query = '{"query":"{ hello }"}'
        response = requests.post(url, data=query, headers={'Content-Type': 'application/json'}, timeout=5)
        response.raise_for_status()

        hello_response = response.json().get('data', {}).get('hello', 'No response')

    except Exception:
        hello_response = "GraphQL endpoint not responsive"

    # Format current timestamp
    now = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")

    # Compose the log message
    message = f"{now} CRM is alive - GraphQL hello: {hello_response}\n"

    # Append the message to the log file
    with open("/tmp/crm_heartbeat_log.txt", "a") as logfile:
        logfile.write(message)
