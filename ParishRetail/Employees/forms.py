from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'  # Includes all fields from the model
        widgets = {
            'Employee_JobDescription': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }
