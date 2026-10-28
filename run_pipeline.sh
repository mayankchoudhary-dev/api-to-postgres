
#!/usr/bin/env bash
set -Eeuo pipefail

# Move to the project directory
cd "$(dirname "$0")"

# Activate the virtual environment
if [[ -f "venv/bin/activate" ]]; then
    source venv/bin/activate
else
    echo "Error: Virtual environment not found."
    exit 1
fi

# Run the ETL pipeline
echo "Starting API to PostgreSQL ETL pipeline..."
python pipeline.py

echo "Pipeline finished successfully!"
