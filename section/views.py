from django.shortcuts import render
from django.utils import translation
from user.models import Employee
from .models import AboutUs


def home(request):
    about = AboutUs.objects.last()
    manager = Employee.objects.filter(job_title="manager", is_active=True).first()
    current_lang = translation.get_language()
    return render(request, 'section/home.html', {
        'about': about,
        'lang': current_lang,
        'manager':manager
    })
