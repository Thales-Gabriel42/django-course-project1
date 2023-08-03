from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html')


def about(request):
    return render(request, 'recipes/pages/about.html')
