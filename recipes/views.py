from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html')


def sobre(request):
    return render(request, 'recipes/sobre.html')
