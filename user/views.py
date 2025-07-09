from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .forms import RegisterForm


def signup(request):
    if request.method == 'POST':
        form_signup = RegisterForm(request.POST)
        if form_signup.is_valid():

            user = form_signup.save()
            login(request, user)

            return JsonResponse({"status": "success"})
        else:

            return JsonResponse({"errors": form_signup.errors}, status=400)
    else:
        form_signup = RegisterForm()
    return render(request, 'user/signup-login.html', {'form_signup': form_signup})


def signin(request):
    if request.method == 'POST':
        form_signin = AuthenticationForm(request, data=request.POST)
        if form_signin.is_valid():
            login(request, form_signin.get_user())
            return JsonResponse({"status": "success"})
        else:

            return JsonResponse({"errors": form_signin.errors}, status=400)
    else:
        form_signin = AuthenticationForm()
    return render(request, 'user/signup-login.html', {'form_signin': form_signin})


def sign_out(request):
    logout(request)
    request.session.flush()
    return redirect('/')




