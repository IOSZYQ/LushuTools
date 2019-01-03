from django.db import models

# Create your models here.


class Image(models.Model):
    image = models.ImageField(verbose_name="图片", upload_to="images")

    class Meta:
        verbose_name = "图片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.image.name)
