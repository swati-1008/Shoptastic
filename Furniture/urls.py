from django.urls import path
from .views import *

app_name = 'Furniture'

urlpatterns = [
    path('mdfwalldecor', mdfwalldecor, name='mdfwalldecor'),
    path('furniturecafestool', furniturecafestool, name='furniturecafestool'),
    path('woodkeyholder', woodkeyholder, name='woodkeyholder'),
    path('storagecase', storagecase, name='storagecase'),
    path('wallmirror', wallmirror, name='wallmirror'),
    path('entunit', entunit, name='entunit'),
]