#!/usr/bin/env bash

cd /usr/share/webapps/calendario

mkdir -p /usr/share/webapps/calendario/var/run
rm -f /usr/share/webapps/calendario/var/run/*

exec /usr/share/envs/calendario/bin/gunicorn config.wsgi -c deploy/staging/gunicorn.conf.py  --env DJANGO_SETTINGS_MODULE=config.settings.production
