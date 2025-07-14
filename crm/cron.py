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

    mutation = gql("""
        mutation {
            updateLowStockProducts {
                success
                message
                updatedProducts
            }
        }
    """)

    transport = RequestsHTTPTransport(
        url='http://localhost:8000/graphql',
        verify=True,
        retries=3,
    )

    client = Client(transport=transport, fetch_schema_from_transport=True)

    try:
        result = client.execute(mutation)
        data = result["updateLowStockProducts"]
        success = data["success"]
        message = data["message"]
        updated_products = data["updatedProducts"]

        log_message = f"{timestamp} {message}: {', '.join(updated_products)}\n"

    except Exception as e:
        log_message = f"{timestamp} Failed to update stock: {e}\n"

    with open("/tmp/low_stock_updates_log.txt", "a") as f:
        f.write(log_message)

# def update_low_stock_products():
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     log_path = "/tmp/low_stock_updates_log.txt"
    
#     try:
#         transport = RequestsHTTPTransport(
#             url='http://localhost:8000/graphql',
#             use_json=True,
#             retries=3,
#         )
#         client = Client(transport=transport, fetch_schema_from_transport=True)

#         mutation = gql("""
#         mutation {
#             updateLowStockProducts {
#                 updatedProducts {
#                     name
#                     stock
#                 }
#                 message
#             }
#         }
#         """)

#         result = client.execute(mutation)
#         updated_products = result["updateLowStockProducts"]["updatedProducts"]
#         message = result["updateLowStockProducts"]["message"]

#         with open(log_path, "a") as log_file:
#             log_file.write(f"\n[{timestamp}] {message}\n")
#             for product in updated_products:
#                 log_file.write(f" - {product['name']}: {product['stock']}\n")

#     except Exception as e:
#         with open(log_path, "a") as log_file:
#             log_file.write(f"\n[{timestamp}] Failed to update stock: {e}\n")


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



