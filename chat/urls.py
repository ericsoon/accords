from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpage, name = 'login'),
    path('signup/', views.register, name = 'register'),
    path('inbox/', views.inbox, name = 'inbox'),
    path('home/', views.home, name = 'home')
]