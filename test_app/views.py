from django.shortcuts import render
from .models import Url
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView
import time
from .parser import requests_parser
import threading


def index(request):
    url = Url.objects.all()
    return render(request, 'test_app/index.html', {'url': url})


class ParserSite(APIView):
    def get(self, request):
        URLS = Url.objects.all()
        result = []
        status = ''
        for url in URLS:
            time_parser = (url.minut * 60) + url.sec
            time.sleep(time_parser)
            result.append(timezone.datetime.now())
            t = threading.Thread(target=requests_parser, args=url)
            t.start()
        return Response(result)
