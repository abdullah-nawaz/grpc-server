#!/usr/bin/env bash

celery -A server.tasks.celery_app worker --pool=gevent --concurrency=20 --loglevel=info
