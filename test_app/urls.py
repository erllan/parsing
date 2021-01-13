from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('parsering/', views.ParserSite.as_view(), name='parser'),

]
