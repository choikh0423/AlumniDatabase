from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.contrib.auth import update_session_auth_hash, authenticate, login as auth_login
from .forms import CustomAuthenticationForm, CustomSignupForm, ProfileSignupForm, CustomPasswordResetForm

from django.core.exceptions import ValidationError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.core.validators import validate_email
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.template import loader
from django.core.mail import send_mail
from django.utils.encoding import force_bytes

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Alumni, College, Industry, Employer, Location
from django.db.models import Q

from .functions import partition

import logging
import difflib


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


class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm

    # def change_password1(request):
    #     if request.method == "POST":
    #         _form = CustomChangePasswordForm(request.POST)
    #         if email_form.is_valid():
    #             user = email_form.save()
    #             update_session_auth_hash(request, user)  # Important!
    #             messages.success(
    #                 request, 'Your password was successfully updated!')
    #             return redirect('change_password')
    #     else:
    #         email_form = CustomChangePasswordForm()
    #     return render(request, 'password_reset_form.html', {"form": email_form})

    # # Customized Reset Password View
    # class ResetPasswordRequestView(FormView):
    #     template_name = 'registration/password_reset_email.html'
    #     success_url = '/signup/'
    #     form_class = PasswordResetEmailForm

    #     def validate_email_address(email):
    #         try:
    #             validate_email(email)
    #             return True
    #         except ValidationError:
    #             return False

    #     def post(self, request, *args, **kwargs):
    #         form = self.form_class(request.POST)
    #         DEFAULT_FROM_EMAIL = 'webadmin@gmail.com'
    #         if form.is_valid():
    #             data = form.cleaned_data['email']
    #             if User.objects.filter(email=data).exists():
    #                 user = User.objects.get(email=data)
    #                 c = {
    #                     'email': user.email,
    #                     'domain': request.META['HTTP_HOST'],
    #                     'site_name': 'your site',
    #                     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
    #                     'user': user,
    #                     'token': default_token_generator.make_token(user),
    #                     'protocol': 'http',
    #                 }
    #             subject_template_name = 'registration/password_reset_subject.txt'
    #             email_template_name = 'registration/password_reset_email.html'
    #             subject = loader.render_to_string(subject_template_name, c)
    #             subject = ''.join(subject.splitlines())
    #             email = loader.render_to_string(email_template_name, c)
    #             send_mail(subject, email, DEFAULT_FROM_EMAIL,
    #                       [user.email], fail_silently=False)
    #             result = self.form_valid(form)
    #             return result

    #         result = self.form_invalid(form)
    #         return result

    # def password_confirm(request):
    #     return render(response, 'registration/password_reset_confirm.html')
    # def change_password2(request):
 #   if request.method == "POST":

    # def search(request):
    #     template = 'index.html'

    #     query = request.GET.get('q')

    #     results = Post.object.filter(
    #         Q(name__icontains=query) | Q(email__icontains=query))


@login_required
def alumnilist(request):
    alumni_list = Alumni.objects.all()
    college_list = College.objects.all()
    industry_list = Industry.objects.all()
    employer_list = Employer.objects.all()

    static_alumni_list = Alumni.objects.all()

    query = request.GET.get("q")

    alist = list(alumni_list)
    # clist = list(college_list)
    # ilist = list(industry_list)
    # elist = list(employer_list)
    # finallist = alist + clist + ilist + elist
    # static_finallist = finallist

    if query:
        alumni_list = alumni_list.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(college__name__icontains=query) |
            Q(industry__name__icontains=query) |
            Q(graduation_date__icontains=query) |
            Q(industry__name__icontains=query) |
            Q(current_employer__name__icontains=query) |
            Q(past_employer__name__icontains=query)
        ).distinct()

        alist = list(alumni_list)
        # finallist = alist

        #college and employer
        #order_by, distinct()

        for alum in static_alumni_list:

            full_name = alum.first_name + ' ' + alum.last_name
            past_employer_list = list(alum.past_employer.all())

            if difflib.SequenceMatcher(None, query, full_name).ratio() >= 0.6:
                alist.append(alum)

            if difflib.SequenceMatcher(None, query, alum.first_name).ratio() >= 0.6:
                alist.append(alum)

            if difflib.SequenceMatcher(None, query, alum.last_name).ratio() >= 0.6:
                alist.append(alum)

            if difflib.SequenceMatcher(None, query, alum.college.name).ratio() >= 0.6:
                alist.append(alum)

            if difflib.SequenceMatcher(None, query, alum.industry.name).ratio() >= 0.6:
                alist.append(alum)

            if difflib.SequenceMatcher(None, query, alum.current_employer.name).ratio() >= 0.6:
                alist.append(alum)

            for employer in past_employer_list:
                if difflib.SequenceMatcher(None, query, employer.name).ratio() >= 0.6:
                    alist.append(alum)

        alist = list(set(alist))

    paginator = Paginator(alist, 8)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_obj_divided = partition(page_obj, 4)
    return render(request, 'search.html', {'page_obj_divided': page_obj_divided, 'page_obj': page_obj})


def directorylist(request):
    alumni_list = Alumni.objects.all()
    alist = list(alumni_list)

    paginator = Paginator(alist, 8)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_obj_divided = partition(page_obj, 4)

    return render(request, 'directory.html', {'page_obj_divided': page_obj_divided, 'page_obj': page_obj})
