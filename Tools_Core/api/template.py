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
        templateList = Template.objects.filter(pk__in=templateIds).all()
        total = len(templateList)
    else:
        userId = query.get("userId")
        userId = djangoUtils.decodeId(userId)

        last = kwargs.get("last", None)
        start = kwargs.get("start", 0)
        count = kwargs.get("count", 24)
        last = djangoUtils.decodeId(last) if last else 0

        templateQuery = Template.objects.order_by('-id')
        if last and not start:
            templateQuery = templateQuery.filter(id__lt=djangoUtils.decodeId(last))
        templateList = templateQuery[start:start + count]
        total = templateQuery.count()

    templateData = []