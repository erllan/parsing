from django.shortcuts import render
from .models import Url
from .parser import requests_parser
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UrlSerializer
import threading
from time import sleep


def index(request):
    url = Url.objects.all()
    return render(request, 'test_app/index.html', {'url': url})


class ParserSite(APIView):
    def get(self, request):
        URLS = Url.objects.all()
        urls = UrlSerializer(URLS, many=True, read_only=True)
        result = ''
        date = []
        for url in URLS:
            time = (url.minut * 60) + url.sec
            sleep(time)
            date.append(timezone.datetime.now())
            t = threading.Thread(target=requests_parser, args=(url,))
            t.start()
        return Response({'result': result, 'date': date, 'url': urls.data})
