from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Employee
from .forms import EmployeeForm
from django.shortcuts import HttpResponse

class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee_add.html'  # Specify your template name
    success_url = reverse_lazy('Employees:employee_list')  # Adjusted to include namespace

    def form_valid(self, form):
        # Optional: Place for additional logic after form is validated, before saving the object.
        print("Successfully added New Employee")  # This should be in a method, not directly in the class body.
        return super().form_valid(form)

class EmployeeListView(ListView):
    model = Employee
    context_object_name = 'employees'
    template_name = 'employee_list.html'
# class EmployeeListView(ListView):
#     model = Employee
#     context_object_name = 'employees'
#     template_name = 'employee_list.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['test_data'] = 'This is a test'  # Add test data to the context
#         return context
    

class EmployeeDetailView(DetailView):
    model = Employee
    context_object_name = 'employee'
    template_name = 'employee_detail.html'

