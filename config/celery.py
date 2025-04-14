# celery.py

from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# Setting an environment variable for project settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# Creating an instance of a Celery object
app = Celery("config")

# Downloading settings from a Django file
app.config_from_object("django.conf:settings", namespace="CELERY")

# Automatic detection and registration of tasks from files tasks.py in Django apps
app.autodiscover_tasks()
