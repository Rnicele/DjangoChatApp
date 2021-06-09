from django.forms import CharField, Form, PasswordInput
from django.forms.widgets import TextInput


class LoginForm(Form):
    username = CharField(
        label='Username',
        max_length=100,
        widget=TextInput(attrs={'class': 'input'})
    )

    password = CharField(widget=PasswordInput(attrs={'class': 'input'}))
