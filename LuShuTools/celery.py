# -*- coding: utf-8 -*-
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'An_Server.settings.prod')

app = Celery('An_Server')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()