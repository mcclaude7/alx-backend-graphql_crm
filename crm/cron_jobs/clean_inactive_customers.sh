#!/bin/bash

# Activate the virtual environment
source /mnt/c/users/user/desktop/airbnb/alx-backend-graphql_crm/venv/bin/activate

# Navigate to project root
cd /mnt/c/users/user/desktop/airbnb/alx-backend-graphql_crm/

# Run Django shell to delete inactive customers
deleted_count=$(echo "
from datetime import timedelta
from django.utils import timezone
from crm.models import Customer, Order

one_year_ago = timezone.now() - timedelta(days=365)
inactive_customers = Customer.objects.exclude(
    id__in=Order.objects.values_list('customer_id', flat=True)
).filter(created_at__lt=one_year_ago)

count = inactive_customers.count()
inactive_customers.delete()
print(count)
" | python3 manage.py shell)

# Log result with timestamp
echo "$(date): Deleted $deleted_count inactive customers" >> /tmp/customer_cleanup_log.txt

#echo "\"$(date): Deleted \$deleted_count inactive customers\"" >> /tmp/customer_cleanup_log.txt

