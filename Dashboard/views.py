from django.shortcuts import render
from Mobiles.forms import *

# Create your views here.

def index(request):
    return render(request, 'Dashboard/index.html')

def about(request):
    return render(request, 'Dashboard/about_us.html')