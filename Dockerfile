FROM python:3.8
ENV PYTHONUNBUFFERED 1
COPY Pipfile* /code/
WORKDIR /code
RUN pip install pipenv
RUN pipenv install --system
COPY . /code/