FROM python:3.9.5-slim-buster

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update --fix-missing \
  && apt-get install -y --no-install-recommends \
  bash \
  build-essential \
  curl \
  && apt-get clean

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./app /src/app

COPY ./config/gunicorn/gunicorn.conf.py /gunicorn.conf.py

WORKDIR /src

CMD ["gunicorn", "-c", "/gunicorn.conf.py", "app.main:app", "--timeout", "185"]
