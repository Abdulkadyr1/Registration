from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('registr/', views.registr, name='reg'),
    path('login/', views.authentication, name='log'),
]
