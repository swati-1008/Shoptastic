from django.shortcuts import render
from Mobiles.forms import *

# Create your views here.

def index(request):
    return render(request, 'Dashboard/index.html')

def about(request):
    return render(request, 'Dashboard/about_us.html')

def add_product(request):
    mobile_form = MobileForm()
    mobile_feature_form = FeaturesForm()
    context = {'mobile_form': mobile_form,
                'mobile_feature_form': mobile_feature_form,}
    return render(request, 'Dashboard/add_product.html', context)
