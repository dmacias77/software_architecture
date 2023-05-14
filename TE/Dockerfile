# Edited by David Macías (MX)
FROM python:3.9

# Python
ENV PYTHONUNBUFFERED=1 \
    # Prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # PIP
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

RUN pip install --upgrade pip
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

# MX: Added installation of x-www-browser
RUN apt-get update \
    && apt-get install -y --no-install-recommends x-www-browser \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /src

COPY src/ /src/
RUN pip install -e /src
COPY tests/ /tests/
# MX: Added missing COPY of test file taxi-data.csv
COPY taxi-data.csv /src/

WORKDIR /src
# MX: Added x-www-browser to open HTML file on creation.
CMD python main.py && x-www-browser financial-report.html
