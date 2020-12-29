FROM ubuntu:focal

# Install dependencies
RUN apt-get update -y \
    && apt-get install -y --no-install-recommends python3-pip python3-dev python3-setuptools python3-venv build-essential curl

RUN pip3 install --upgrade pip

# Set python aliases for python3
RUN ln -s /usr/bin/python3 /usr/bin/python

# Poetry installation and setup
RUN curl -sSLO https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py \
    && python get-poetry.py --version 1.0.0 \
    && rm get-poetry.py
ENV PATH="/root/.poetry/bin:/opt/venv/bin:${PATH}"

COPY . /app
WORKDIR /app

# Install Python dependencies
COPY pyproject.toml poetry.lock manage.py app config ./
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi \
    && python manage.py migrate

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
