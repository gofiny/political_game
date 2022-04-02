# syntax=docker/dockerfile:experimental

FROM python:3.10.4

ENV PIPENV_VENV_IN_PROJECT 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -U pip wheel setuptools
RUN pip install --no-cache-dir pipenv

RUN mkdir /opt/app

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --deploy --ignore-pipfile

COPY . .
ENV PYTHONPATH=/opt/app

CMD ["pipenv", "run", "main"]