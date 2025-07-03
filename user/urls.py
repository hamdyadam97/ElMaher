from django.urls import path
from . import views
app_name = 'user'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('sign_out/', views.sign_out, name='sign_out'),
]
