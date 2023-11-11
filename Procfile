release: python ./manage.py migrate && python ./manage.py collectstatic --noinput
web: gunicorn --pythonpath portfolio_project portfolio_project.wsgi