from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('login/', views.loginpage, name = 'login'),
    path('signup/', views.register, name = 'register'),
    path('inbox/', views.inbox, name = 'inbox')
]