#!/bin/sh
set -e

echo "Check mongo service availability"
python ~/check_service.py

echo "Running app with uvicorn"
uvicorn src.main:app --host 0.0.0.0 --port 8000

exec "$@"
