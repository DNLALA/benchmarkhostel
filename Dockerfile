FROM --platform=linux/amd64 python:3.11 as build
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app/
# && python group.py && python group_permission.py
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000