from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .forms import Registration, Authentication
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def main(request):
    return render(request, 'Ridak/Home.html')


def registr(request):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password_confirm']:
                user = User(username=form.cleaned_data['username'], email=form.cleaned_data['email'])
                user.set_password(form.cleaned_data['password'])
                user.save()
            else:
                form.add_error('password_confirm', 'Password do not match')
    else:
        form = Registration()

    return render(request, 'Ridak/Registr_form.html', context={'form': form})


def authentication(request):
    if request.method == "POST":
        form_auth = Registration(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('Hello')
    else:
        form_auth = Authentication()
    return render(request, 'Ridak/Auth.html', context={'form': form_auth})
