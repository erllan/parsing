from django.shortcuts import render
from .models import Url, ResultUrl
from .parser import parser_html, requests_parser
from django.utils import timezone


def index(request):
    URLS = Url.objects.all()
    result = ''
    status = ''
    for url in URLS:
        html = requests_parser(url.url)
        if html.status_code == 200:
            status = html.status_code
            title = parser_html(html.text, 'title')
            h1 = parser_html(html.text, 'h1')
            result = timezone.datetime.now()
            ResultUrl.objects.create(url=url,
                                     title=title,
                                     h1=h1
                                     )
        else:
            status = html.status_code

    return render(request, 'test_app/index.html', {'result': result, 'status': status, 'url': URLS})
