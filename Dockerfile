FROM python:3.8.5-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/

RUN mkdir /app/

WORKDIR /app/

COPY django_server/ /app/django_server/
COPY frontend/ /app/frontend/
COPY requirements.txt /app/

RUN pip install -r requirements.txt

CMD python django_server/manage.py migrate && python django_server/manage.py runserver --noreload 0.0.0.0:8080
