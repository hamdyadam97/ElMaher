# myapp/urls.py
from django.urls import path
from . import views
app_name = 'furniture'

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/create/', views.post_create, name='post_create'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/service/<str:service_slug>/', views.post_list, name='service_posts'),
    path('reviews/crud/', views.review_crud_page, name='review_crud_page'),
    path('reviews/<int:pk>/', views.review_detail, name='review_detail'),
]