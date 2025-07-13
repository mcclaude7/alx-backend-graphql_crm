#!/usr/bin/env python3
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from datetime import datetime, timedelta
import logging
import traceback
import os

# Configure loggingimport os
log_file = os.path.join(os.path.dirname(__file__), "order_reminders_log.txt")


#log_file = "/tmp/order_reminders_log.txt"
logging.basicConfig(filename=log_file, level=logging.INFO)

# GraphQL client setup
transport = RequestsHTTPTransport(
    url='http://localhost:8000/graphql',
    verify=False,
    retries=3,
)

client = Client(transport=transport, fetch_schema_from_transport=True)

# Compute date 7 days ago
seven_days_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")

# GraphQL query — adjust the query field names to match your schema
query = gql("""
query GetRecentOrders($after: Date!) {
  orders(orderDate_Gte: $after) {
    id
    customer {
      email
    }
  }
}
""")

# Variables for the query
variables = {
    "after": seven_days_ago
}

try:
    result = client.execute(query, variable_values=variables)

    orders = result.get("orders", [])
    for order in orders:
        order_id = order.get("id")
        email = order.get("customer", {}).get("email")
        logging.info(f"{datetime.now()}: Order {order_id} for {email}")

    print("Order reminders processed!")

except Exception as e:
    logging.error("Error processing order reminders", exc_info=True)
    print("Failed to process order reminders.")
    traceback.print_exc()

