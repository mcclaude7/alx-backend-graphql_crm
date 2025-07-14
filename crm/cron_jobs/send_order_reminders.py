# # Task 1 python script for sending order reminders

# def send_reminders():
#     print("Sending order reminders for pending orders from last 7 days")

# if __name__ == "__main__":
#     send_reminders()
#!/usr/bin/env python3

import datetime
import logging
import traceback
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

# Logging setup
log_file = "/tmp/order_reminders_log.txt"
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s: %(message)s')

# GraphQL client setup
transport = RequestsHTTPTransport(url='http://localhost:8000/graphql', verify=False, retries=3)
client = Client(transport=transport, fetch_schema_from_transport=False)

# Date range: last 7 days
today = datetime.date.today()
seven_days_ago = today - datetime.timedelta(days=7)

# GraphQL query for pending orders in the last 7 days
query = gql(f"""
query {{
  allOrders {{
    id
    orderDate
    customer {{
      email
    }}
  }}
}}
""")

try:
    result = client.execute(query)
    orders = result.get("allOrders", [])
    for order in orders:
        order_date = datetime.datetime.strptime(order["orderDate"], "%Y-%m-%d").date()
        if seven_days_ago <= order_date <= today:
            order_id = order["id"]
            customer_email = order["customer"]["email"]
            logging.info(f"Reminder: Order ID {order_id} for {customer_email}")
    print("Order reminders processed!")
# except Exception as e:
#     logging.error(f"Failed to process order reminders: {e}")
#     print("Failed to process order reminders.")

except Exception as e:
    logging.error("Failed to process order reminders")
    logging.error(traceback.format_exc())  # Log full traceback
    print("Failed to process order reminders.")