# _*_ coding: utf-8 _*_
__author__ = 'alan'
__date__ = '2018/12/26 3:38 PM'


from rest_framework.views import APIView
# from Tools_Core.api

class TemplateFind(APIView):
    def get(self, request, format=None):
        pass


class TemplateInfo(APIView):
    def get(self, request, templateId, format=None):
        pass

    def delete(self, request, templateId, format=None):
        pass


class TemplateNew(APIView):
    def post(self, request, format=None):
        pass