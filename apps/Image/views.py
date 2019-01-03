from django.shortcuts import render

# Create your views here.
import os
from toolset.viewUtils import viewResponse, viewErrorResponse
from rest_framework.views import APIView
from django.conf import settings

from Image.models import Image
from .forms import UploadImageForm

# from .tasks import add
from utilities.djangoUtils import sendEmail

class UploadImageView(APIView):
    def get(self, request, id):
        file_name = Image.objects.filter(id=id).values_list('file', flat=True).first()
        if file_name:
            file_name = os.path.join(settings.IMAGE_DIR, file_name)
            return viewResponse({"fileName": file_name})
        else:
            return viewErrorResponse("dont exist")

    def post(self, request, format=None):
        # add.delay(11,11)
        image_form = UploadImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            name = str(image_form.cleaned_data['image']).replace(' ', '_')
            image = Image.objects.filter(image='images/{}'.format(name))
            if len(image) > 0:
                return viewErrorResponse("image exist")
            image_form.save()
            path = os.path.join(settings.IMAGE_DIR, name)
            return viewResponse({"url": path})
        else:
            return viewErrorResponse("")


    def delete(self, request, id):
        file = Image.objects.filter(id=id)
        if len(file):
            file_name = file.first()
            file_name = os.path.join(settings.Image_DIR, str(file_name.file))
            os.unlink(file_name)
        file.delete()
        return viewResponse()




class ImageListView(APIView):
    def get(self, request):
        allFiles = list(Image.objects.values('id', 'file'))
        # for file in allFiles:
        #     file['file'] = os.path.join(settings.Image_DIR, file['file'])
        # serializer = TempateSerializer(allFiles, many=True)
        return viewResponse(allFiles)