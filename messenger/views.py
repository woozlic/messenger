from django.shortcuts import render


def index(request):
    return render(request, 'main.html')


def profile(request):
    return render(request, 'account/profile.html')
