from django.shortcuts import render
from .forms import UserForm
from django.contrib.auth.models import User
from .models import *


from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'Register_Login/index.html')

def register(request):
    registered = False
    first_name = ''
    last_name = ''
    email = ''
    username = ''
    password = ''
    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            # print(User.objects.get(username=request.POST.get('username')).exists())
            user = user_form.save()
            user.set_password(user.password)        # Hashing the passwords -> Encrypting them
            user.save()
            length = len(Customer.objects.all())
            customer = Customer.objects.create(uid='CUS' + str(length + 1), user=user)
            customer.save()
            registered = True
            if user.is_authenticated:
                return HttpResponseRedirect(reverse('Register_Login:user_login'))
        else:
            errors = [(k, v[0]) for k, v in user_form.errors.items()]
            # print(errors[0][1])
            print(errors)
            for i in errors:
                print(f'i = {i[0]}, first_name = {first_name}, last_name = {last_name}, email = {email}, username = {username}, password = {password}')
                if i[0] == 'first_name':
                    first_name = i[1]
                if i[0] == 'last_name':
                    last_name = i[1]
                if i[0] == 'email':
                    email = i[1]
                if i[0] == 'username':
                    username = i[1]
                if i[0] == 'password':
                    password = i[1]
            # print(f'Error = {user_form.errors}')
    else:
        user_form = UserForm()

    return render(request, 'Register_Login/register.html', {'user_form': user_form, 'registered': registered, 'first_name': first_name, 'last_name': last_name, 'email': email, 'username': username, 'password': password})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            print("Someone tried to login and failed")
            print(f'Username: {username} and Password: {password}')
            return HttpResponse("Invalid login details supplied")
    return render(request, 'Register_Login/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))