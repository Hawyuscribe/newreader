web: python -m gunicorn neurology_mcq.wsgi:application --chdir django_neurology_mcq --log-file - --workers 3 --timeout 120
release: python django_neurology_mcq/manage.py migrate --noinput && python django_neurology_mcq/manage.py collectstatic --noinput
# Ensure the Django project package (under django_neurology_mcq) is importable by the worker
worker: PYTHONPATH=django_neurology_mcq celery -A django_neurology_mcq.neurology_mcq.celery_app worker -l info
