FROM python:3.9.5-alpine3.13

COPY requirements_build.txt /requirements_build.txt
# OS dependencies only required to build certain Python dependencies
RUN apk add --no-cache --virtual .build-deps gcc libc-dev make \
  && pip install -r /requirements_build.txt \
  && apk del .build-deps
RUN rm /requirements_build.txt
# OS dependencies required at runtime
RUN apk add --no-cache \
  bash \
  curl

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN rm /requirements.txt

COPY ./app /app


COPY ./config/gunicorn/gunicorn.conf.py /gunicorn.conf.py
CMD ["gunicorn", "-c", "/gunicorn.conf.py", "app.main:app", "--timeout", "185"]
