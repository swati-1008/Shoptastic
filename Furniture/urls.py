from django.urls import path
from .views import *

app_name = 'Furniture'

urlpatterns = [
    path('mdfwalldecor', mdfwalldecor, name='mdfwalldecor'),
]