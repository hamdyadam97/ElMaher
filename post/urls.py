# myapp/urls.py
from django.urls import path, re_path
from . import views
app_name = 'post'

urlpatterns = [

    path('detail/<str:slug>/', views.post_detail, name='post_detail'),
    re_path(r'^(?:(?P<service_slug>[\w-]+)/)?$', views.post_list, name='post_list'),
    path('posts/service/<str:service_slug>/', views.post_list, name='service_posts'),
    path('archive/<int:year>/<int:month>/', views.post_archive, name='post_archive'),
]