#!/usr/bin/env bash
# exit on error
# build_files.sh
pip install -r requirements.txt

# make migrations
python manage.py migrate 
python manage.py collectstatic
