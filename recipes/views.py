from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Recipes'})


def about(request):
    return render(request, 'recipes/pages/about.html', context={
        'name': 'About'})
