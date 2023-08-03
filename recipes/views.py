from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html')


def about(request):
    return render(request, 'recipes/about.html')
