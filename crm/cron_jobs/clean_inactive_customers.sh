#!/bin/bash

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Activate the virtual environment if it exists
if [ -f "$PROJECT_ROOT/venv/bin/activate" ]; then
  source "$PROJECT_ROOT/venv/bin/activate"
else
  echo "Virtual environment not found in $PROJECT_ROOT/venv"
  exit 1
fi

# Run the Django shell command to delete inactive customers
deleted_count=$(echo "
from crm.models import Customer
count = Customer.objects.filter(is_active=False).count()
Customer.objects.filter(is_active=False).delete()
print(count)
" | python "$PROJECT_ROOT/manage.py" shell)

# Log the result with full path
LOG_FILE="/tmp/customer_cleanup_log.txt"
if [ -n "$deleted_count" ]; then
  echo "$(date): Deleted $deleted_count inactive customers" >> "$LOG_FILE"
else
  echo "$(date): Failed to retrieve deleted count" >> "$LOG_FILE"
fi

