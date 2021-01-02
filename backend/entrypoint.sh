#!/bin/bash

set -e
set -u

python manage.py flush --no-input
python manage.py migrate

exec "$@"
