from django.shortcuts import render
from django.utils import translation
from .models import AboutUs


def home(request):
    about = AboutUs.objects.last()
    current_lang = translation.get_language()

    return render(request, 'section/home.html', {
        'about': about,
        'lang': current_lang,
    })
