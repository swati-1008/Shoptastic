from django.conf.urls import include
from django.urls import path
from . import views

app_name = 'Dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('product', views.add_product, name='product'),
]