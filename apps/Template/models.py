from django.db import models

class TemplateFile(models.Model):
    file = models.FileField(verbose_name="模板文件", null=True)

    class Meta:
        verbose_name = "Html模板"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.file.name)


class SendEmailInfo(models.Model):
    subject = models.CharField(verbose_name="邮件标题", null=True, max_length=200)
    context = models.TextField(verbose_name="邮件正文", null=True)
    sendTo = models.CharField(verbose_name="邮件发送对象", max_length=200)
    sendWay = models.IntegerField(verbose_name="邮件发送方式")
    template = models.ForeignKey(TemplateFile, related_name="sendEmailInfos", on_delete=models.CASCADE)
    dateTime = models.DateTimeField(verbose_name="邮件发送时间", null=True)
    sendSuccess = models.BooleanField(verbose_name="是否发送", default=False)

    def __str__(self):
        return str(self.subject)