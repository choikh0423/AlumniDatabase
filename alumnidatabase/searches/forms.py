import unicodedata
from django import forms
from django.forms import ModelForm
from django.contrib.auth import (
    get_user_model,
)
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from .models import Profile
import datetime
from string import ascii_lowercase, digits
from random import choice
from django.core.mail import send_mail

from django.core.exceptions import ValidationError

UserModel = get_user_model()


def _unicode_ci_compare(s1, s2):
    return unicodedata.normalize('NFKC', s1).casefold() == unicodedata.normalize('NFKC', s2).casefold()


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='Email Address',
        widget=forms.TextInput(attrs={'autofocus': True})
    )


class CustomSignupForm(UserCreationForm):

    firstname = forms.CharField(
        label='First Name',
        widget=forms.TextInput(attrs={'autofocus': True}),
        required=True,
        error_messages={
            'invalid': "Please provide proper first name.",
            'required': "First name is required."
        }
    )

    lastname = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(attrs={'autofocus': True}),
        required=True,
        error_messages={
            'invalid': "Please provide proper last name.",
            'required': "Last name is required."
        }
    )

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={'placeholder': "8+ characters with mix of letters and numbers & symbols"}),
        required=True,
        help_text="It must not be commonly used and too similar to your personal information.",
        error_messages={
            'invalid': "Please make sure that your password is correctly formatted",
            'required': "Password is required."
        },
    )

    password2 = forms.CharField(
        label='Password Confirmation:',
        widget=forms.PasswordInput,
        help_text=None,
        required=True,
        error_messages={
            'invalid': "Your password did not matched.",
            'required': "Password Confirmation is required."
        },
    )

    email = forms.EmailField(
        label='Email Address',
        widget=forms.TextInput(attrs={'autofocus': True}),
        required=True,
        error_messages={
            'invalid': "Please provide a correct email",
            'required': "Email is required."
        },
    )

    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email

    def save(self, commit=True):
        pw_choice = ascii_lowercase+digits

        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.username = ''.join([choice(pw_choice) for i in range(20)])
        user.email = self.cleaned_data['email']
        user.is_active = True
        user.first_name = self.cleaned_data['firstname']
        user.last_name = self.cleaned_data['lastname']

        if commit:
            user.save()
        return user


class ProfileSignupForm(ModelForm):

    YEAR_CHOICE = [(y, y)
                   for y in range(2010, datetime.date.today().year+1)]

    joined_year = forms.ChoiceField(
        label='Year of Joining Organization',
        choices=YEAR_CHOICE,
        required=True,
        initial=datetime.date.today().year+1,
    )

    class Meta:
        model = Profile
        fields = ('joined_year',)


class CustomPasswordResetForm(PasswordResetForm):

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists() == False:
            raise forms.ValidationError("non-registered email")
        return email
