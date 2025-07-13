# #!/bin/bash
# # Script to delete inactive customers and log cleanup

# #cd /mnt/c/Users/User/desktop/airbnb/alx-backend-graphql_crm/alx_backend_graphql_crm
# cd /mnt/c/Users/User/desktop/airbnb/alx-backend-graphql_crm

# DELETED_COUNT=$(python3 manage.py shell << END
# from datetime import timedelta
# from django.utils import timezone
# from crm.models import Customer

# cutoff = timezone.now() - timedelta(days=365)
# deleted, _ = Customer.objects.filter(last_order_date__lt=cutoff).delete()
# print(deleted)
# END
# )

# echo "$(date): Deleted \$DELETED_COUNT inactive customers" >> /tmp/customer_cleanup_log.txt

#!/bin/bash

# Navigate to the Django project root where manage.py is located
cd /mnt/c/Users/User/desktop/airbnb/alx-backend-graphql_crm

# Activate virtual environment (adjust path if needed)
#source venv/bin/activate

# Run Django shell command to delete inactive customers
deleted_count=$(echo "
from crm.models import Customer
from datetime import datetime, timedelta

cutoff = datetime.now() - timedelta(days=365)
inactive_customers = Customer.objects.filter(order__isnull=True, created__lt=cutoff)
count = inactive_customers.count()
inactive_customers.delete()
print(count)
" | python3 manage.py shell)

# Log the result to file
echo \"$(date): Deleted \$deleted_count inactive customers\" >> /tmp/customer_cleanup_log.txt
