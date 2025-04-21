from django.urls import path
from . import views
app_name = 'user'
urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='employee_list'),
    path('employee/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('employee/create/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('employee/<int:pk>/update/', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('employee/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee_delete'),
    path('services', views.ServiceListView.as_view(), name='service_list'),
    path('service/<int:pk>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path('service/create/', views.ServiceCreateView.as_view(), name='service_create'),
    path('service/<int:pk>/update/', views.ServiceUpdateView.as_view(), name='service_update'),
    path('service/<int:pk>/delete/', views.ServiceDeleteView.as_view(), name='service_delete'),
]
