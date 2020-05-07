release: python legacybook_server/manage.py migrate -v3
web: newrelic-admin run-program gunicorn legacybook_server.core.wsgi DJANGO_SETTINGS_MODULE=legacybook_server.core.settings --pythonpath legacybook_server --log-file -
