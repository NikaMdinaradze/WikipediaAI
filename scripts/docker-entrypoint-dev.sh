#!/bin/sh
set -e

echo "Check mongo service availability"
python ~/check_service.py --service-name "${DATABASE_HOST}" --ip "${DATABASE_HOST}" --port "${DATABASE_PORT}"

echo "Running app with uvicorn"
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

exec "$@"
