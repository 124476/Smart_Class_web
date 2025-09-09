FROM python:3.10-slim

WORKDIR /usr/src/app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
ENV PYTHONPATH=/usr/src/app/web

RUN sh -c "\
  python web/manage.py migrate --noinput && \
  python web/manage.py loaddata web/fixtures/data.json && \
  echo \"from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin123') if not User.objects.filter(username='admin').exists() else None\" | python web/manage.py shell && \
  cd web && python manage.py collectstatic --noinput && cd .. \
"

CMD ["sh", "-c", "\
  python web/manage.py migrate --noinput && \
  python web/manage.py loaddata web/fixtures/data.json && \
  echo \"from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin123') if not User.objects.filter(username='admin').exists() else None\" | python web/manage.py shell && \
  gunicorn web.wsgi:application --bind 0.0.0.0:8000 --preload \
"]