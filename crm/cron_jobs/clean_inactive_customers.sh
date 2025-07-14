#!/bin/bash

# Get the path of this script
SCRIPT_PATH="${BASH_SOURCE[0]}"
SCRIPT_DIR="$(cd "$(dirname "$SCRIPT_PATH")" && pwd)"

# Store current working directory in 'cwd'
cwd=$(pwd)

# Navigate to project root
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
cd "$PROJECT_ROOT"

# Activate virtual environment if it exists
if [ -f "$PROJECT_ROOT/venv/bin/activate" ]; then
  source "$PROJECT_ROOT/venv/bin/activate"
else
  echo "Virtual environment not found at $PROJECT_ROOT/venv"
  exit 1
fi

# Run Django shell command to clean inactive customers
deleted_count=$(echo "
from crm.models import Customer
count = Customer.objects.filter(is_active=False).count()
Customer.objects.filter(is_active=False).delete()
print(count)
" | python manage.py shell)

# Log the result with the cwd
LOG_FILE="/tmp/customer_cleanup_log.txt"
if [ -n "$deleted_count" ]; then
  echo "$(date): Deleted $deleted_count inactive customers (cwd was $cwd)" >> "$LOG_FILE"
else
  echo "$(date): Failed to retrieve deleted count (cwd was $cwd)" >> "$LOG_FILE"
fi


