from rest_framework import serializers
from .models import Url, ResultUrl


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultUrl
        fields = '__all__'


class UrlSerializer(serializers.ModelSerializer):
    resulturl_set = ResultSerializer(many=True, read_only=True)

    class Meta:
        model = Url
        fields = ('id', 'url', 'resulturl_set')
