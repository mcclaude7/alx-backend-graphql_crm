import requests
import json
from datetime import datetime

def update_low_stock():
    query = '''
    mutation {
      updateLowStockProducts {
        updatedProducts {
          name
          stock
        }
        message
      }
    }
    '''

    response = requests.post(
        'http://localhost:8000/graphql/',
        json={'query': query}
    )

    with open('/tmp/low_stock_updates_log.txt', 'a') as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if response.status_code == 200:
            data = response.json()
            if 'errors' in data:
                f.write(f"[{timestamp}] GraphQL Error: {data['errors']}\n")
            else:
                updates = data['data']['updateLowStockProducts']['updatedProducts']
                msg = data['data']['updateLowStockProducts']['message']
                f.write(f"[{timestamp}] {msg}\n")
                for product in updates:
                    f.write(f" - {product['name']}: stock={product['stock']}\n")
        else:
            f.write(f"[{timestamp}] Request failed with status code {response.status_code}\n")
