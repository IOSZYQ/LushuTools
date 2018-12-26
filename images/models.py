__author__ = 'swolfod'

from django.db import models


class LocalImage(models.Model):
    imageName = models.CharField(verbose_name='图片文件名', max_length=64, unique=True)
    imageUrl = models.CharField(verbose_name='图片远程URL', max_length=1000, blank=True, null=True)
    ready = models.BooleanField(verbose_name='是否远程', default=False)
    def __str__(self):
        return self.imageName

    class Meta:
        verbose_name = '本地图片库'
        verbose_name_plural = '本地图片库'
