#!/bin/bash

# Change to the Django project root
cd /mnt/c/Users/User/desktop/airbnb/alx-backend-graphql_crm

# Run Django shell command to delete inactive customers
deleted_count=$(python3 manage.py shell <<EOF
from crm.models import Customer
from datetime import datetime, timedelta

cutoff = datetime.now() - timedelta(days=365)
inactive_customers = Customer.objects.filter(order__isnull=True, created__lt=cutoff)
count = inactive_customers.count()
inactive_customers.delete()
print(count)
EOF
)

# Log the result to file
echo "$(date): Deleted $deleted_count inactive customers" >> /tmp/customer_cleanup_log.txt
