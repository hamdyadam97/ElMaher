# myapp/urls.py
from django.urls import path
from . import views
app_name = 'furniture'

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/create/', views.post_create, name='post_create'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]