FROM python:3.10-slim

WORKDIR /usr/src/app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
ENV PYTHONPATH=/usr/src/app/web

CMD ["sh", "-c", "\
  python web/manage.py migrate --noinput && \
  python web/manage.py flush --noinput && \
  python web/manage.py loaddata web/fixtures/data.json && \
  python web/manage.py createsuperuser --username admin --email admin@example.com --password adminpassword && \
  python web/manage.py collectstatic --noinput && \
  gunicorn web.wsgi:application --bind 0.0.0.0:8000\
"]
