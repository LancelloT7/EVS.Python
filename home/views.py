from django.shortcuts import render

def menu(request):
    return render(request, 'menu.html')

def entrada_produto(request):
    return render(request, 'entrada.html')

# Create your views here.
