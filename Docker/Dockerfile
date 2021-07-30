FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY django_sample/requirements.txt /code/
RUN pip install -r requirements.txt
COPY django_sample/ /code/
