# myapp/urls.py
from django.urls import path
from . import views
app_name = 'furniture'

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/create/', views.post_create, name='post_create'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('signup/', views.frontend_signup, name='signup'),
    path('login/', views.frontend_login, name='login'),
    path('logout/', views.frontend_logout, name='logout'),
    path('posts/service/<str:service_slug>/', views.post_list, name='service_posts'),
]