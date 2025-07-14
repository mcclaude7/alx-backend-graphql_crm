import os
import django
import datetime
from graphene.test import Client
from crm.schema import schema

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm.settings')
django.setup()

def update_low_stock():
    client = Client(schema)
    query = '''
        mutation {
            updateLowStockProducts {
                success
                message
                updatedProducts {
                    id
                    name
                    stock
                }
            }
        }
    '''
    result = client.execute(query)
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    log_path = '/tmp/low_stock_updates_log.txt'
    with open(log_path, 'a') as log_file:
        log_file.write(f"\n=== {now} ===\n")
        if result.get('data') and result['data']['updateLowStockProducts']['success']:
            for product in result['data']['updateLowStockProducts']['updatedProducts']:
                log_file.write(f"{product['name']} updated to stock: {product['stock']}\n")
        else:
            log_file.write("Failed to update products.\n")