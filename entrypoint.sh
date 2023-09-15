#!/bin/sh

# Apply database migrations
python manage.py migrate

# Populate products table
python manage.py populate_products

# Start the web server
exec "$@"
