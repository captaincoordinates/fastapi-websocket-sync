FROM python:3.9.5-slim-buster

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update --fix-missing \
  && apt-get install -y --no-install-recommends \
  bash \
  build-essential \
  curl \
  && apt-get clean

COPY requirements.txt /requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r /requirements.txt

COPY ./app /src/app

COPY ./config/gunicorn/gunicorn.conf.py /gunicorn.conf.py

ENV CPU_CORE_LIMIT=1
ENV WORKERS_PER_CORE=2

WORKDIR /src

CMD ["gunicorn", "-c", "/gunicorn.conf.py", "app.main:app", "--timeout", "185", "--reload"]
