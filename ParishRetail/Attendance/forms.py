from django import forms
from .models import AttendanceRecord, Overtime

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = AttendanceRecord
        fields = ['employee', 'date', 'in_time', 'out_time', 'status']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'in_time': forms.TimeInput(attrs={'type': 'time'}),
            'out_time': forms.TimeInput(attrs={'type': 'time'}),
        }

class OvertimeForm(forms.ModelForm):
    class Meta:
        model = Overtime
        fields = ['employee', 'date', 'in_time', 'out_time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'in_time': forms.TimeInput(attrs={'type': 'time'}),
            'out_time': forms.TimeInput(attrs={'type': 'time'}),
        }

