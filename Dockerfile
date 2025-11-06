FROM heroku/heroku:22

# Install Python and build dependencies similar to the Heroku Python buildpack
RUN set -eux; \
    apt-get update; \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        python3.11 \
        python3.11-dev \
        python3.11-venv \
        python3-pip \
        build-essential \
        libpq-dev \
        curl; \
    apt-get clean; \
    rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN python3.11 -m venv /app/.venv && \
    . /app/.venv/bin/activate && \
    pip install --upgrade pip setuptools wheel && \
    pip install -r requirements.txt

COPY . .

ENV PATH="/app/.venv/bin:${PATH}"

ENTRYPOINT ["/app/scripts/docker-entrypoint.sh"]
