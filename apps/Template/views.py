from django.shortcuts import render

# Create your views here.
import os, json, time, pytz

from datetime import datetime, timezone, timedelta


from toolset.viewUtils import viewResponse, viewErrorResponse
from rest_framework.views import APIView
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from Template.models import TemplateFile, SendEmailInfo
from django.template.loader import get_template


from .forms import UploadTemplateForm
from .tasks import sendMultiEmailDelay, sendCeleryEmail

from secretKeys import TEMPLATE_API_HOST, PASSWORD


class TemplateView(APIView):
    def get(self, request, id):
        file_name = Template.objects.filter(id=id).values_list('file', flat=True).first()
        return render(request, file_name)

    def post(self, request, format=None):
        file_form = UploadTemplateForm(request.POST, request.FILES)
        if file_form.is_valid():
            file = file_form.cleaned_data['file']
            name = str(file).replace(' ', '_')
            html = Template.objects.filter(file=name)
            if len(html) > 0:
                return viewErrorResponse("file exist")

            default_storage.save('templates/mail/{}'.format(name), ContentFile(file.read()))
            template = Template.objects.create(file=name)
            template_dic = {
                "id": template.id,
                "file": str(template.file),
                "load": '{}{}/'.format(TEMPLATE_API_HOST, template.id)
            }
            return viewResponse(template_dic)


    def delete(self, request, id):
        file = Template.objects.filter(id=id)
        if len(file):
            file_name = file.first().file
            file_path = "{}/templates/mail/{}".format(settings.MEDIA_ROOT, file_name)
            os.unlink(file_path)
        file.delete()
        return viewResponse()


class TemplateListView(APIView):
    def get(self, request):
        allFiles = list(Template.objects.values('id', 'file'))
        for file in allFiles:
            file['load'] = '{}{}/'.format(TEMPLATE_API_HOST, file['id'])
        return viewResponse(allFiles)


class SendEmail(APIView):
    def post(self, request):
        password = request.data.get("password")
        if password != PASSWORD:
            return viewErrorResponse("密码错误")

        sendTo = request.data.get("sendTo")
        sendWay = int(request.data.get("sendWay"))
        template = int(request.data.get("template"))
        # htmlPath = request.data.get("html")
        # context = request.data.get("context")
        subject = request.data.get("subject")
        configure = request.data.get("configure")
        date = request.data.get("date")

        date = date + ':00' if date else date
        if date:
            try:

                date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
                # time_struct = time.mktime(date.timetuple())
                # date = datetime.utcfromtimestamp(time_struct)
            except:
                return viewErrorResponse("时间格式不对")
            SendEmailInfo.objects.create(sendTo=sendTo, sendWay=sendWay, template=Template.objects.get(pk=template), subject=subject, dateTime=date)
        else:
            sendMultiEmailDelay.delay(subject=subject, sendTo=sendTo, sendWay=sendWay, templateId=template, configure=configure)
        return viewResponse()


class ToolsView(APIView):
    def get(self, request):
        return render(request, 'base.html')



