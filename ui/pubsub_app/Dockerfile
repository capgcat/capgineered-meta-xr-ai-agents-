FROM python:3.11.3
ENV PYTHONUNBUFFERED True

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r  requirements.txt

ENV APP_HOME /root
WORKDIR $APP_HOME
COPY /pubsub $APP_HOME/pubsub

EXPOSE 8080
CMD exec uvicorn pubsub.main:app --host 0.0.0.0 --port $PORT
