FROM python:3.8-slim

RUN pip install pydantic==1.9.0 pydantic-to-typescript==1.0.8 watchdog==2.1.6

RUN apt-get -y update --fix-missing \
    && apt-get install --no-install-recommends -y \
    curl \
    && apt-get clean

RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean

RUN npm install -g json-schema-to-typescript@^10.1.5

COPY entrypoint.sh /

WORKDIR /tsgen

COPY watch.py .
COPY generate.py .
