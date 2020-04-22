from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login as auth_login
from .forms import CustomAuthenticationForm, CustomSignupForm, ProfileSignupForm

from django.db.models import Q


@login_required
def index(request):
    return render(request, 'index.html')


def login(response):
    login_form = CustomAuthenticationForm()

    return render(response, 'registration/login.html', {"form": login_form})


def signup(request):
    if request.method == "POST":
        signup_form = CustomSignupForm(request.POST)
        profile_form = ProfileSignupForm(request.POST)

        if signup_form.is_valid() and profile_form.is_valid():
            user = signup_form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            username = signup_form.cleaned_data.get('email')
            password = signup_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)

            return redirect('/searches')

    else:
        signup_form = CustomSignupForm()
        profile_form = ProfileSignupForm()

    return render(request, 'signup.html', {"form": signup_form, "profile_form": profile_form})


# def search(request):
#     template = 'index.html'

#     query = request.GET.get('q')

#     results = Post.object.filter(
#         Q(name__icontains=query) | Q(email__icontains=query))
