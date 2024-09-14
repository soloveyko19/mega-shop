FROM python:3.12-alpine

ENV PYTHONPATH=/src

RUN mkdir /src && \
    pip install poetry==1.8.2

COPY ./src/poetry.lock ./src/pyproject.toml /src/

WORKDIR /src

RUN poetry install --no-dev

COPY ./src /src


CMD poetry run alembic upgrade head && \
    poetry run uvicorn asgi:app --port 5000 --host 0.0.0.0

