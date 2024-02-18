FROM python:3.11
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code

RUN pip install -r requirements.txt

COPY entrypoint.sh /code

COPY server /code

CMD ["sh", "entrypoint.sh"]