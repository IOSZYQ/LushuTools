# _*_ coding: utf-8 _*_
__author__ = 'alan'
__date__ = '2019/1/24 4:33 PM'

import os
from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LuShuTools.settings")

#Celery的参数是当前项目的名称
app = Celery('LuShuTools')
app.config_from_object('django.conf:settings', namespace='CELERY', force=True)
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)