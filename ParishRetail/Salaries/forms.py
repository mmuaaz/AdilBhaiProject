from django import forms
from .models import SalaryBreakdown

class SalaryForm(forms.ModelForm):
    class Meta:
        model = SalaryBreakdown
        fields = [
            'employee', 'period', 'base_salary', 'lunch_allowance', 
            'attendance_bonus', 'sales_bonus', 'overtime_bonus', 
            'deductions'
        ]
        widgets = {
            'period': forms.DateInput(attrs={'type': 'month'}),
        }
