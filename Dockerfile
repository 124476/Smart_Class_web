FROM python:3.10-slim

WORKDIR /usr/src/app/web

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
ENV PYTHONPATH=/usr/src/app/web

CMD ["sh", "-c", "\
  python manage.py migrate --noinput && \
  python manage.py flush --noinput && \
  python manage.py loaddata fixtures/data.json && \
  echo \"from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin123') if not User.objects.filter(username='admin').exists() else None\" | python manage.py shell && \
  python manage.py collectstatic --noinput && \
  gunicorn wsgi:application --bind 0.0.0.0:8000\
"]
