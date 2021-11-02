#!/bin/bash -xue
# uvicorn main:app --reload
# celery -A celery_worker.celery worker --loglevel=info
# celery flower -A celery_worker.celery --broker:amqp://localhost//

docker-compose up -d --force-recreate