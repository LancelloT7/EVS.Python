from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.menu, name="menu"),  
    path('entrada/', views.entrada_produto, name="entrada_produto"),   
]