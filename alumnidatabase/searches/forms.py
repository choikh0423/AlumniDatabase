from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth.models import User
import datetime
from string import ascii_lowercase, digits
from random import choice


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
        widget=forms.PasswordInput,
        required=True,
        help_text=["Use 8 or more characters with a mix of letters, numbers & symbols.",
                   "It must not be commonly used and too similar to your personal information."],
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

    YEAR_CHOICE = [(y, y) for y in range(2010, datetime.date.today().year+1)]

    joined_year = forms.ChoiceField(
        label='Year of Joining Organization',
        choices=YEAR_CHOICE,
        required=True,
        initial=datetime.date.today().year+1,
    )

    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'email',
                  'joined_year', 'password1', 'password2']

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

        if commit:
            user.save()
        return user
