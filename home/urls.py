from django.urls import path
from django.conf.urls import url
from . import views
app_name= 'home'
urlpatterns = [
    path('', views.HomeView, name= 'all'),
    path('register', views.register, name= 'register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]