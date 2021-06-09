from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

from .forms import LoginForm, CreateUserForm


def sign_in(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/chat/')

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/chat/')

    return render(request, 'login.html', {'form': form})


def sign_up(request):
    form = CreateUserForm()

    print(request.method)
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'register.html', context)


def sign_out(request):
    logout(request)
    return HttpResponseRedirect('/login/')


@login_required(login_url='/login/')
def chat(request):
    return render(request, 'chat.html')
