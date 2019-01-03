# -*- coding: utf-8 -*-
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LuShuTools.settings')

app = Celery('LuShuTools')
# app = Celery('LuShuTools', broker='redis://127.0.0.1:6379/0')
# app = Celery('tasks', broker='redis://127.0.0.1:6379/0')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()