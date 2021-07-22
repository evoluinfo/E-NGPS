FROM python:3.9.5

COPY . .

WORKDIR /var/www

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
