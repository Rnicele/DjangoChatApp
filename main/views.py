from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from .forms import CreateUserForm, LoginForm


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
            else:
                messages.error(
                    request, "Username or password is incorrect.", extra_tags='danger')

    return render(request, 'login.html', {'form': form})


def sign_up(request):
    form = CreateUserForm()

    print(request.method)
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(
                request, 'Account was created for ' + user, extra_tags='success')
            return redirect('login')
        else:
            print(form.errors)
            for error in form.errors:
                print(error)
                if error == 'password2':
                    messages.error(
                        request, "Password did not match.", extra_tags='password')
                elif error == 'username':
                    messages.error(
                        request, "Username already existed.", extra_tags='username')

    context = {'form': form}
    return render(request, 'register.html', context)


def sign_out(request):
    logout(request)
    return HttpResponseRedirect('/login/')


@login_required(login_url='/login/')
def chat(request):
    return render(request, 'chat.html')
