# _*_ coding: utf-8 _*_
__author__ = 'alan'
__date__ = '2018/12/26 3:38 PM'


from rest_framework.views import APIView


class TemplateFind(APIView):
    def get(self, request, format=None):
        pass


class TemplateInfo(APIView):
    def get(self, request, templateId, format=None):
        pass

    def delet(self, request, templateId, format=None):
        pass