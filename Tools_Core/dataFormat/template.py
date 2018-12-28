# _*_ coding: utf-8 _*_
__author__ = 'alan'
__date__ = '2018/12/26 5:13 PM'

from utilities import classproperty
from Tools.dataFormat import UserFields


class TemplateFields:
    @classproperty
    def full(self):
        return {
            "id": True,
            "html": True,
            "publish": UserFields.brief
        }