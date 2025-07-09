from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.utils import translation
from user.forms import RegisterForm
from user.models import Employee
from .models import AboutUs, Service, Work


def home(request):
    about = AboutUs.objects.last()
    manager = Employee.objects.filter(job_title="manager", is_active=True).first()
    employees = Employee.objects.filter(is_active=True).exclude(job_title="manager")
    services = Service.objects.all()
    works = Work.objects.all()
    form_signup = RegisterForm()
    form_signin = AuthenticationForm()
    current_lang = translation.get_language()
    return render(request, 'section/home.html', {
        'about': about,
        'lang': current_lang,
        'manager': manager,
        'form_signup': form_signup,
        'form_signin': form_signin,
        'services': services,
        'works': works,
        'employees': employees,
    })
