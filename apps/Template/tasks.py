# _*_ coding: utf-8 _*_
__author__ = 'alan'
__date__ = '2019/1/3 6:24 PM'

import django
django.setup()

import json, requests, secretKeys
import django.utils.timezone as timezone

from celery_app import app
from django.template.loader import get_template
from Template.models import SendEmailInfo, TemplateFile


@app.task()
def sendMultiEmailDelay(subject, sendTo, sendWay, templateId=None, templateFile=None, configure=None):
    configure = json.loads(configure) if configure else {}
    htmlContent = None
    if templateFile:
        htmlContent = get_template(templateFile).render(configure)
    elif templateId:
        template = TemplateFile.objects.filter(id=int(templateId)).first()
        if template:
            htmlPath = str(template.file)
            htmlContent = get_template(htmlPath).render(configure)

    s = json.dumps({'subject': subject,
                    'sendTo': sendTo,
                    'sendWay': sendWay,
                    'htmlContent': htmlContent})
    headers = {'content-type': 'application/json'}
    r = requests.post(secretKeys.SEND_EMAIL_HOST, data=s, headers=headers)



@app.task()
def sendCeleryEmail():
    notSendEmails = SendEmailInfo.objects.filter(sendSuccess=False, dateTime__lte=timezone.now())
    for emails in notSendEmails:
        subject = emails.subject
        sendTo = emails.sendTo
        sendWay = emails.sendWay
        templateFile = emails.template.file
        sendMultiEmailDelay.delay(subject=subject, sendTo=sendTo, sendWay=sendWay, templateFile=templateFile)
    notSendEmails.update(sendSuccess=True)


