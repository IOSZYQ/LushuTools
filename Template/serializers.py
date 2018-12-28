# _*_ coding: utf-8 _*_
__author__ = 'alan'
__date__ = '2018/12/27 7:47 PM'

from rest_framework import serializers

from Template.models import Template


class TempateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = "__all__"
