from django import forms
from .models import SalesRecord

class SalesRecordForm(forms.ModelForm):
    class Meta:
        model = SalesRecord
        fields = ['date', 'total_sales', 'employee']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
