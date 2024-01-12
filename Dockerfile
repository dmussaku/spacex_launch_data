FROM python:3.11

RUN pip install --upgrade pip
RUN pip install --no-cache-dir poetry
WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

COPY . /app
CMD ["python", "main.py"]
