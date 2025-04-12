# myapp/urls.py
from django.urls import path
from . import views
app_name = 'furniture'

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
]