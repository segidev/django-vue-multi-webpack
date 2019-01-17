FROM python:latest

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
CMD python manage.py runserver 0:8000
