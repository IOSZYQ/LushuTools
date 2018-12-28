from django.shortcuts import render

# Create your views here.
import os
from toolset.viewUtils import viewResponse, viewErrorResponse
from rest_framework.views import APIView
from django.conf import settings
from utilities.djangoUtils import sendEmail

from Template.models import Template
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives


class TemplateView(APIView):
    def get(self, request, id):
        file_name = Template.objects.filter(id=id).values_list('file', flat=True).first()
        if file_name:
            # file_name = os.path.join(settings.TEMPLATE_DIR, file_name)
            return viewResponse({"fileName": file_name})
        else:
            return viewErrorResponse("dont exist")

    def post(self, request, format=None):
        myFile = request.FILES.get("file", None)  # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return viewResponse("no files for upload!")
        template, create = Template.objects.get_or_create(file=myFile.name)
        if create:
            destination = open(os.path.join(settings.TEMPLATE_DIR, myFile.name), 'wb+')
            #是否可以一次读取文件，每次读取2.5M
            if myFile.multiple_chunks() == False:
                destination.write(myFile.read())
            else:
                for chunk in myFile.chunks():  # 分块写入文件
                    destination.write(chunk)
            destination.close()

            fileDic = {"id": template.id, "file": template.file}
            return viewResponse(fileDic)
        else:
            return viewErrorResponse("file exist")

    def delete(self, request, id):
        file = Template.objects.filter(id=id)
        if len(file):
            file_name = file.first()
            file_name = os.path.join(settings.TEMPLATE_DIR, str(file_name.file))
            os.unlink(file_name)
        file.delete()
        return viewResponse()




class TemplateListView(APIView):
    def get(self, request):
        allFiles = list(Template.objects.values('id', 'file'))
        # for file in allFiles:
        #     file['file'] = os.path.join(settings.TEMPLATE_DIR, file['file'])
        # serializer = TempateSerializer(allFiles, many=True)
        return viewResponse(allFiles)


class SendEmail(APIView):
    def post(self, request):
        sendTo = request.data.get("sendTo")
        template = request.data.get("template")

        sendTo = ["hualing_zyq@126.com", "416834256@qq.com"]
        template = Template.objects.filter(id=17).first()

        htmlPath = None
        plainPath = None
        context = None
        subject = "主题"
        if template:
            htmlPath = template.file

        textContent = get_template(plainPath).render(context) if plainPath else ""
        htmlContent = get_template(htmlPath).render(context) if htmlPath else None

        msg = EmailMultiAlternatives(subject, textContent,
                                     "{0} <{1}>".format(settings.EMAIL_HOST_NAME, settings.EMAIL_HOST_USER), sendTo)
        if htmlContent:
            msg.attach_alternative(htmlContent, "text/html")

        msg.send()
        return viewResponse()

