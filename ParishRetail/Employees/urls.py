# Add the URL pattern in your urls.py
from django.urls import path
from .views import EmployeeCreateView, EmployeeListView, EmployeeDetailView


app_name = 'Employees'
urlpatterns = [
    path('employee/add/', EmployeeCreateView.as_view(), name='employee_add'),
    path('employees/', EmployeeListView.as_view(), name='employee_list'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),
    
 ]