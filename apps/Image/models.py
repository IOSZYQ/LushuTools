from django.db import models

# Create your models here.


class Image(models.Model):
    imageName = models.CharField(verbose_name='图片文件名', max_length=64, unique=True)

    class Meta:
        verbose_name = "图片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.imageName)
