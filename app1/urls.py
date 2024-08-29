from django.urls import path
from app1.views import *

app_name='FirstPage'

urlpatterns=[
    path('temp1/', temp1, name='temp1'),
]