FROM python:3.11 AS base
WORKDIR /app

# Install Poetry
RUN pip install poetry


# Turn-off Poetry-venv, so that the dependencies go directly to /usr/local
RUN poetry config virtualenvs.create false \
 && poetry config virtualenvs.in-project false


RUN pip install --upgrade pip setuptools wheel
RUN pip uninstall -y urllib3 || true
RUN pip install urllib3==2.4.0
# Copy the dependency manifests and install them
COPY pyproject.toml poetry.lock* ./

RUN poetry install --no-root --no-interaction

# Copy all code of app
COPY . .



FROM base AS backend
CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]

# Celery worker
FROM base AS celery
CMD ["celery", "-A app worker", "--loglevel=info"]

# Celery beat
FROM base AS beat
CMD ["celery", "-A app beat", "--loglevel=info"]

EXPOSE 8002