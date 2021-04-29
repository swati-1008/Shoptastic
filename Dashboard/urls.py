from django.conf.urls import include
from django.urls import path
from . import views

app_name = 'Dashboard'

urlpatterns = [
    path('', views.index, name='index'),
]