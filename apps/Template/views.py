from django.shortcuts import render

# Create your views here.
import os
from toolset.viewUtils import viewResponse, viewErrorResponse
from rest_framework.views import APIView
from django.conf import settings
# from utilities.djangoUtils import sendEmail

from Template.models import Template
from django.template.loader import get_template

from .forms import UploadTemplateForm
from .tasks import sendMultiEmailDelay, sendToEmails


class TemplateView(APIView):
    def get(self, request, id):
        file_name = Template.objects.filter(id=id).values_list('file', flat=True).first()
        if file_name:
            # file_name = os.path.join(settings.TEMPLATE_DIR, file_name)
            return viewResponse({"fileName": file_name})
        else:
            return viewErrorResponse("dont exist")

    def post(self, request, format=None):
        file_form = UploadTemplateForm(request.POST, request.FILES)
        if file_form.is_valid():
            name = str(file_form.cleaned_data['file']).replace(' ', '_')
            file = Template.objects.filter(file='templates/{}'.format(name))
            if len(file) > 0:
                return viewErrorResponse("file exist")

            file_form.save()
            path = os.path.join(settings.TEMPLATE_DIR, name)
            return viewResponse({"url": path})


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
        htmlPath = request.data.get("html")
        plainPath = request.data.get("plain")
        context = request.data.get("context")
        subject = request.data.get("subject")

        sendTo = sendToEmails(sendTo)
        template = Template.objects.filter(id=17).first()

        subject = "主题"
        if template:
            htmlPath = template.file

        textContent = get_template(plainPath).render(context) if plainPath else ""
        htmlContent = get_template(htmlPath).render(context) if htmlPath else None

        sendMultiEmailDelay(subject=subject, sendTo=sendTo, textContent=textContent, htmlContent=htmlContent)
        return viewResponse()



