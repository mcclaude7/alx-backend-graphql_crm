import datetime
import logging

logger = logging.getLogger(__name__)

def clean_inactive_customers():
    # Logic to delete customers with no orders since 1 year ago
    logger.info("Running clean_inactive_customers task")
    # Your cleanup code here

def send_order_reminders():
    # Logic to find pending orders from last 7 days and log reminders
    logger.info("Running send_order_reminders task")
    # Your order reminder code here

def log_heartbeat():
    # Log heartbeat to confirm CRM is healthy
    now = datetime.datetime.now()
    logger.info(f"CRM Heartbeat at {now}")

def update_low_stock_products():
    # Update products with stock < 10 via GraphQL mutation
    logger.info("Running update_low_stock_products task")
    # Your stock update logic here

def log_crm_heartbeat():
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    log_import datetime
import requests

def log_crm_heartbeat():
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    log_message = f"{timestamp} CRM is alive\n"

    try:
        response = requests.post(
            'http://localhost:8000/graphql',
            json={"query": "{ hello }"}
        )
        if response.ok:
            result = response.json()
            log_message += f"GraphQL hello: {result.get('data', {}).get('hello', 'No response')}\n"
        else:
            log_message += "GraphQL endpoint unreachable.\n"
    except Exception as e:
        log_message += f"GraphQL error: {e}\n"

    with open("/tmp/crm_heartbeat_log.txt", "a") as f:
        f.write(log_message)
    
