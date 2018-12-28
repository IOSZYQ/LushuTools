from django.db import models

# Create your models here.

from django.db import models


class Template(models.Model):
    file = models.FileField(verbose_name="模板文件", null=True)

    class Meta:
        verbose_name = "Html模板"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)