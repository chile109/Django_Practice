FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1
RUN pip install pipenv
COPY Pipfile* /code/
WORKDIR /code
RUN pipenv install --system
COPY . /code/
ENTRYPOINT [ "bash", "entrypoint.sh" ]