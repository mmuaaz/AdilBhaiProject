from django.urls import path
from .views import SalarySlipView

app_name = 'Salaries'
urlpatterns = [
    path('salary-slip/<int:pk>/', SalarySlipView.as_view(), name='salary_slip'),
    
]