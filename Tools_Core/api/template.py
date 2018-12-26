# _*_ coding: utf-8 _*_
__author__ = 'alan'
__date__ = '2018/12/26 5:51 PM'


from Tools_Core.models.template import Template
from utilities import apiUtils, djangoUtils

def read(**kwargs):
    query = kwargs.get('query', {})
    fields = kwargs.get('fields')
    ids = query.get('id')

    if ids:
        templateIds = djangoUtils.decodeIdList(ids)
        hasMore = False
    else:
        userId = query.get("userId")
        userId = djangoUtils.decodeId(userId)
        templateIds = list(Template.objects.filter(publisherId=userId).values_list('id', flat=True))

    templateList = Template.objects.filter(pk__in=templateIds).all()
    total = len(templateList)
