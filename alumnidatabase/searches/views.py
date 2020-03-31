from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm, CustomSignupForm


@login_required
def index(request):
    return render(request, 'index.html')


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm


def signup(response):
    if response.method == "POST":
        signup_form = CustomSignupForm(response.POST)

        if signup_form.is_valid():
            signup_form.save()
            return redirect('/searches/accounts/login')

    else:
        signup_form = CustomSignupForm()

    return render(response, 'signup.html', {"form": signup_form})
