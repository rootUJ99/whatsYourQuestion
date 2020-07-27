FROM python:3.8-buster

RUN mkdir app
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY pyproject.toml /app/
RUN poetry export -f requirements.txt -o requirements.txt


# RUN poetry install --no-interaction --no-dev

RUN pip install -r requirements.txt

COPY . /app

