FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
  build-essential \
  libpq-dev \
  && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir uv 

WORKDIR /app

ENV PYTHONDONTWRITEBYTHECODE=1
ENV PYTHONUNBUFFERED=1

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen

COPY . .

EXPOSE 8000

CMD [ "uv", "run", "app/main.py" ]