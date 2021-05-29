from django import forms
from .models import *

class MobileForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = Mobiles
        fields = '__all__'

class FeaturesForm(forms.ModelForm):
    class Meta():
        model = Features
        fields = ('features',)