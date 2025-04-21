from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Employee, Service, Work, Client


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee_detail.html'

class EmployeeCreateView(CreateView):
    model = Employee
    fields = '__all__'
    template_name = 'employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee_confirm_delete.html'
    success_url = reverse_lazy('employee_list')



class ServiceListView(ListView):
    model = Service
    template_name = 'services/service_list.html'

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/service_detail.html'

class ServiceCreateView(CreateView):
    model = Service
    fields = '__all__'
    template_name = 'services/service_form.html'
    success_url = reverse_lazy('service_list')

class ServiceUpdateView(UpdateView):
    model = Service
    fields = '__all__'
    template_name = 'services/service_form.html'
    success_url = reverse_lazy('service_list')

class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'services/service_confirm_delete.html'
    success_url = reverse_lazy('service_list')



# Clients Views
class ClientListView(ListView):
    model = Client
    template_name = 'clients/client_list.html'

class ClientDetailView(DetailView):
    model = Client
    template_name = 'clients/client_detail.html'

class ClientCreateView(CreateView):
    model = Client
    fields = '__all__'
    template_name = 'clients/client_form.html'
    success_url = reverse_lazy('client_list')

class ClientUpdateView(UpdateView):
    model = Client
    fields = '__all__'
    template_name = 'clients/client_form.html'
    success_url = reverse_lazy('client_list')

class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'clients/client_confirm_delete.html'
    success_url = reverse_lazy('client_list')


# Projects Views
class ProjectListView(ListView):
    model = Work
    template_name = 'projects/project_list.html'

class ProjectDetailView(DetailView):
    model = Work
    template_name = 'projects/project_detail.html'

class ProjectCreateView(CreateView):
    model = Work
    fields = '__all__'
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project_list')

class ProjectUpdateView(UpdateView):
    model = Work
    fields = '__all__'
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project_list')

class ProjectDeleteView(DeleteView):
    model = Work
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('project_list')