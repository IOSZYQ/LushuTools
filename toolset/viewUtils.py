# _*_ coding: utf-8 _*_
__author__ = 'alan'
__date__ = '2018/12/28 5:13 PM'

from rest_framework.response import Response
from utilities import djangoUtils

def viewResponse(context=None, content_type=None):
    return Response(djangoUtils.ajaxResponse(context if context else {}), content_type=content_type)


def viewErrorResponse(errMsg, errCode=None):
    return Response(djangoUtils.ajaxErrorResponse(errMsg, errCode))