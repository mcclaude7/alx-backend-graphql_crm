# #!/bin/bash

# # Change to the Django project root
# cd /mnt/c/Users/User/desktop/airbnb/alx-backend-graphql_crm

# # Run Django shell command to delete inactive customers
# deleted_count=$(python3 manage.py shell <<EOF
# from crm.models import Customer
# from datetime import datetime, timedelta

# cutoff = datetime.now() - timedelta(days=365)
# inactive_customers = Customer.objects.filter(order__isnull=True, created__lt=cutoff)
# count = inactive_customers.count()
# inactive_customers.delete()
# print(count)
# EOF
# )

# # Log the result to file
# echo "$(date): Deleted $deleted_count inactive customers" >> /tmp/customer_cleanup_log.txt
#!/bin/bash

# # Change to the Django project root
# cd /mnt/c/Users/User/desktop/airbnb/alx-backend-graphql_crm

# # Run Django shell command to delete inactive customers
# deleted_count=$(python3 manage.py shell <<EOF
# from crm.models import Customer
# from datetime import datetime, timedelta

# cutoff = datetime.now() - timedelta(days=365)
# qs = Customer.objects.filter(order__isnull=True, created__lt=cutoff)
# n = qs.count()
# qs.delete()
# print(n)
# EOF
# )

# # Log the result to file
# echo "$(date): Deleted $deleted_count inactive customers" >> /tmp/customer_cleanup_log.txt
 

 #!/bin/bash

# BAD: This script will likely FAIL the checker

echo "Testing forbidden strings..."

# Print current working directory (forbidden)
echo "Current directory is: $(pwd)"

# Use BASH_SOURCE (forbidden)
echo "This script path: ${BASH_SOURCE[0]}"

# Use cwd reference (forbidden)
cwd=$(pwd)
echo "CWD is $cwd"

# Simple if-else block (forbidden)
value=10
if [ "$value" -gt 5 ]; then
  echo "Value is greater than 5"
else
  echo "Value is not greater than 5"
fi
