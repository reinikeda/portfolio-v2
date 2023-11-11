release: python portfolio_project/manage.py migrate && python portfolio_project/manage.py collectstatic --noinput
web: gunicorn --pythonpath portfolio_project portfolio_project.wsgi