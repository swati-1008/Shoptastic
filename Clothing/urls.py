from django.urls import path
from .views import *

app_name = 'Clothing'

urlpatterns = [
    path('zeellehenga', zeellehenga, name='zeellehenga'),
    path('babyjumpsuit', babyjumpsuit, name='babyjumpsuit'),
    path('mensweatshirt', mensweatshirt, name='mensweatshirt'),
    path('menshirt', menshirt, name='menshirt'),
    path('babyromper', babyromper, name='babyromper'),
    path('bandhejsaree', bandhejsaree, name='bandhejsaree'),
]