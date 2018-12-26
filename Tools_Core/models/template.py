# _*_ coding: utf-8 _*_
__author__ = 'alan'
__date__ = '2018/12/26 4:12 PM'


from django.db import models


class Template(models.Model):
    html = models.TextField(verbose_name="模板html")
    publisherId = models.IntegerField(verbose_name=u'发布用户')

    class Meta:
        app_label = "Tools_Core"