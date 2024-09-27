from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.logar, name="logar"),  
    path('cadastrar/', views.cadastrar, name="cadastrar"),  
]
