from django.shortcuts import render

# Create your views here.


def signin(request):
    return render(request, 'login.html')


def signout(request):
    return render(request, 'logout.html')
