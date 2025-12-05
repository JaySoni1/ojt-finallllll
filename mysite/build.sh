#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Current Directory: $(pwd)"
ls -la
echo "Content of requirements.txt:"
cat requirements.txt

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
