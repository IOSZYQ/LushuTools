# _*_ coding: utf-8 _*_
__author__ = 'alan'
__date__ = '2019/1/3 6:24 PM'

from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

@shared_task
def sendMultiEmailDelay(subject, sendTo, textContent, htmlContent):
    sendTo = sendTo if isinstance(sendTo, list) else [sendTo]
    msg = EmailMultiAlternatives(subject, textContent,
                                 "{0} <{1}>".format(settings.EMAIL_HOST_NAME, settings.EMAIL_HOST_USER), sendTo)
    if htmlContent:
        msg.attach_alternative(htmlContent, "text/html")

    msg.send()


def sendToEmails(sendTo="Tos"):
    if sendTo == "Tos":
        return ['alan@lushu.co', 'hualing_zyq@126.com']
    else:
        return ['416834256@qq.com']