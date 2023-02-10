FROM python:3.9.7-slim

ENV FLASK_APP=app.app:app

RUN apt-get update && apt-get install -y libpq-dev gcc
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
COPY app /app

CMD ["flask", "run", "--host", "0.0.0.0"]
