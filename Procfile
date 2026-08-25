web: gunicorn solutionsexperts.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn solutionsexperts.wsgi
web:pip install -r requirements.txt && python manage.py collectstatic --noinput