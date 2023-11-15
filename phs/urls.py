from phs.views import *

from django.urls import path

app_name='thing'

urlpatterns=[
    path('park/',park,name='park'),
    path('hyung/',hyung,name='hyung'),
]
