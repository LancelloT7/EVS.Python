from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def logar(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')  # Verifique se 'username' é a chave correta
        password = request.POST.get('password')  # Verifique se 'password' é a chave correta

        user = authenticate(request, username=username, password=password)  # A função authenticate
        if user is not None:
            login(request, user)  # A função login
            return render(request, 'menu.html')
        else:
            return HttpResponse('Usuário ou senha inválidos.')
        
        

def cadastrar(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    
    elif request.method == "POST":
        login = request.POST.get('login')
        senha = request.POST.get('senha')

        # Verifica se o usuário já existe
        if User.objects.filter(username=login).exists():
            return render(request, 'cadastro.html', {'error': 'Usuário já existe.'})

        # Cria o novo usuário
        usuario = User.objects.create_user(username=login, password=senha)

        # Redireciona após o cadastro
        return render(request, 'login.html')  # Altere para a URL do login

