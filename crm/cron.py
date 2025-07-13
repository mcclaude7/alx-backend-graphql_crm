from datetime import datetime
import logging

# Required imports for GraphQL check
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

def log_crm_heartbeat():
    # Setup log file
    log_file = "/tmp/crm_heartbeat_log.txt"
    timestamp = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    message = f"{timestamp} CRM is alive\n"

    try:
        with open(log_file, "a") as file:
            file.write(message)

        # Optional GraphQL "hello" check
        transport = RequestsHTTPTransport(
            url='http://localhost:8000/graphql',
            verify=False,
            retries=3,
        )
        client = Client(transport=transport, fetch_schema_from_transport=True)

        query = gql('''
            query {
                hello
            }
        ''')
        result = client.execute(query)
        with open(log_file, "a") as file:
            file.write(f"GraphQL hello response: {result.get('hello')}\n")

    except Exception as e:
        with open(log_file, "a") as file:
            file.write(f"Error: {e}\n")
