from django.db import models
from django.utils import timezone


class Url(models.Model):
    url = models.CharField(max_length=255)
    time = models.TimeField(default=timezone.now)
    minut = models.PositiveIntegerField(default=0)
    sec = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.url


class ResultUrl(models.Model):
    title = models.CharField(max_length=255)
    url = models.ForeignKey(Url, on_delete=models.CASCADE)
    h1 = models.CharField(max_length=255)
    encoding = models.CharField(max_length=100)


