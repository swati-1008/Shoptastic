from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from .views import *

app_name = 'Mobiles'

urlpatterns = [
    path('oneplus', oneplus, name = 'oneplus'),
    path('redmi9power', redmi9power, name = 'redmi9power'),
    path('samsunggalaxym51', samsunggalaxym51, name = 'samsunggalaxym51'),
    path('iphone12mini', iphone12mini, name = 'iphone12mini'),
    path('nokia3.4', nokia34, name = 'nokia3.4'),
    path('vivoy20', vivoy20, name = 'vivoy20'),
]