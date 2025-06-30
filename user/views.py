from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import RegisterForm





# إضافة تقييم شركة

def frontend_signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            request.session['from_frontend'] = True
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'user/signup.html', {'form': form})


