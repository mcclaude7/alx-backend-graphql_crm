import datetime
import logging
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

logger = logging.getLogger(__name__)


def clean_inactive_customers():
    logger.info("Running clean_inactive_customers task")
    # Add cleanup logic if needed


def send_order_reminders():
    logger.info("Running send_order_reminders task")
    # Add reminder logic if needed


def log_heartbeat():
    now = datetime.datetime.now()
    logger.info(f"CRM Heartbeat at {now}")

def update_low_stock_products():
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

    transport = RequestsHTTPTransport(
        url='http://localhost:8000/graphql',
        verify=True,
        retries=3,
    )

    client = Client(transport=transport, fetch_schema_from_transport=True)

    mutation = gql("""
    mutation {
        updateLowStockProducts {
            success
            message
            updatedProducts
        }
    }
    """)

    try:
        result = client.execute(mutation)
        updates = result["updateLowStockProducts"]["updatedProducts"]
        message = result["updateLowStockProducts"]["message"]
        with open("/tmp/low_stock_updates_log.txt", "a") as f:
            f.write(f"{timestamp} {message}\n")
            for item in updates:
                f.write(f"{timestamp} Updated: {item}\n")
    except Exception as e:
        with open("/tmp/low_stock_updates_log.txt", "a") as f:
            f.write(f"{timestamp} Failed to update stock: {e}\n")

def log_crm_heartbeat():
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    log_message = f"{timestamp} CRM is alive\n"

    try:
        transport = RequestsHTTPTransport(
            url='http://localhost:8000/graphql',
            verify=True,
            retries=3,
        )
        client = Client(transport=transport, fetch_schema_from_transport=True)

        query = gql("""
        query {
            hello
        }
        """)
        result = client.execute(query)
        hello_value = result.get("hello", "No response")
        log_message += f" - GraphQL hello: {hello_value}\n"

    except Exception as e:
        log_message += f" - GraphQL error: {e}\n"

    with open("/tmp/crm_heartbeat_log.txt", "a") as f:
        f.write(log_message)



