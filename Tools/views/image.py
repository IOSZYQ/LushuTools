# _*_ coding: utf-8 _*_
__author__ = 'alan'
__date__ = '2018/12/26 3:40 PM'


from rest_framework.views import APIView


class ImageFind(APIView):
    def get(self, request, format=None):
        pass


class ImageInfo(APIView):
    def delete(self, request, image, format=None):
        pass


class UploadImage(APIView):
    def post(self, request, format=None):
        pass
