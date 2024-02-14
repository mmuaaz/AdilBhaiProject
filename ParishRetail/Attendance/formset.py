from django.forms import modelformset_factory
from .models import AttendanceRecord
from .forms import AttendanceForm

AttendanceFormSet = modelformset_factory(
    AttendanceRecord,
    form=AttendanceForm,
    extra=0,  # Set to 0 if you don't want any extra empty forms
)
