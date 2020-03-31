from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth.models import User
import datetime


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='Email Address',
        widget=forms.TextInput(attrs={'autofocus': True})
    )


class CustomSignupForm(UserCreationForm):

    firstname = forms.CharField(
        label='First Name',
        widget=forms.TextInput(attrs={'autofocus': True})
    )

    lastname = forms.CharField(
        label='First Name',
        widget=forms.TextInput(attrs={'autofocus': True})
    )

    email = forms.EmailField(
        label='Email Address',
        widget=forms.TextInput(attrs={'autofocus': True})
    )

    YEAR_CHOICE = [(y, y) for y in range(2010, datetime.date.today().year+1)]

    joined_year = forms.ChoiceField(
        label='Year of Joining Organization',
        choices=YEAR_CHOICE,
        initial=datetime.date.today().year+1,
    )

    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'username',
                  'email', 'joined_year', 'password1', 'password2']
