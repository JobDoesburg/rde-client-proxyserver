FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN mkdir /code/
RUN mkdir /code/log/

WORKDIR /code/proxyserver/

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python -

COPY pyproject.toml /code/
COPY poetry.lock /code/

RUN /etc/poetry/bin/poetry config virtualenvs.create false --local && /etc/poetry/bin/poetry install --only main

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

COPY proxyserver /code/proxyserver/

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
