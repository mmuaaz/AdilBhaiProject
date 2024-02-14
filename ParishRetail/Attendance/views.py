from django.views.generic import UpdateView, ListView
from .models import AttendanceRecord, Overtime
from .forms import AttendanceForm

class AttendanceSheetView(UpdateView):
    model = AttendanceRecord
    form_class = AttendanceForm
    template_name = 'attendance_sheet.html'
    success_url = '/attendance_sheet/'  # Adjust the URL as needed

class OvertimeReportView(ListView):
    model = Overtime
    context_object_name = 'overtime_records'
    template_name = 'overtime_report.html'
