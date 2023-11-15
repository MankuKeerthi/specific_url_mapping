from cew.views import *

from django.urls import path

app_name='anything'

urlpatterns=[
    path('cha/',cha,name='cha'),
    path('eun/',eun,name='eun'),
]
