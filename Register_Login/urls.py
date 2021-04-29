from django.conf.urls import include
from django.urls import path
from . import views as login_views

app_name = 'Register_Login'

urlpatterns = [
    path('register', login_views.register, name='register'),
    path('login', login_views.user_login, name='user_login'),
    path('logout', login_views.user_logout, name='user_logout'),
]