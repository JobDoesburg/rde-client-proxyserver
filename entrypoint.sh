#!/bin/bash

set -e

echo "Running application"

chown -R www-data:www-data /code/

cd /code/proxyserver

gunicorn -b 0.0.0.0:5000 --workers 1 --threads 100 app:app
