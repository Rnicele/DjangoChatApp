from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import LoginForm


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
    return render(request, 'register.html')


def sign_out(request):
    logout(request)
    return HttpResponseRedirect('/login/')


@login_required(login_url='/login/')
def chat(request):
    return render(request, 'chat.html')
