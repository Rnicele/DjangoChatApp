from django.forms import CharField, Form, PasswordInput, EmailField
from django.forms.fields import EmailField
from django.forms.widgets import TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class LoginForm(Form):
    username = CharField(
        label='Username',
        max_length=100,
        widget=TextInput(attrs={'class': 'input'})
    )

    password = CharField(widget=PasswordInput(attrs={'class': 'input'}))


class CreateUserForm(UserCreationForm):
    model = User

    first_name = CharField(
        label='First Name',
        max_length=100,
        widget=TextInput(attrs={'class': 'input'})
    )

    last_name = CharField(
        label='Last Name',
        max_length=100,
        widget=TextInput(attrs={'class': 'input'})
    )

    username = CharField(
        label='Username',
        max_length=100,
        widget=TextInput(attrs={'class': 'input'})
    )

    email = EmailField(
        label='Email',
        max_length=100,
        widget=TextInput(attrs={'class': 'input'})
    )

    password1 = CharField(
        label='Password', widget=PasswordInput(attrs={'class': 'input'}))
    password2 = CharField(label='Confirm Password',
                          widget=PasswordInput(attrs={'class': 'input'}))
