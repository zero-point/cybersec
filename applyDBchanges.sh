#!/bin/bash          

#helper script to repopulate the database and run the application
rm db.sqlite3
python manage.py syncdb
python sample_population.py
python manage.py runserver
