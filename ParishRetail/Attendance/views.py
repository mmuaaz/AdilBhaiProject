from django.views.generic import UpdateView, ListView, View
from .models import AttendanceRecord, Overtime
from .forms import AttendanceForm, AttendanceFormSet
from django.shortcuts import render, redirect, HttpResponse
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime, timedelta


class AttendanceSheetView(UpdateView):
    model = AttendanceRecord
    form_class = AttendanceForm
    template_name = 'attendance_sheet.html'
    success_url = '/attendance_sheet/'  # Adjust the URL as needed

class OvertimeReportView(ListView):
    model = Overtime
    context_object_name = 'overtime_records'
    template_name = 'overtime_report.html'
    
class MarkAttendanceView(View):
    template_name = 'mark_attendance.html'
    formset_class = AttendanceFormSet

    def get_formset(self, data=None):
        return self.formset_class(data, queryset=AttendanceRecord.objects.none())

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return render(request, self.template_name, {'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return HttpResponse('Submitted Successfully')  # Update with your actual URL name
        return render(request, self.template_name, {'formset': formset})
    

@receiver(post_save, sender=AttendanceRecord)
def create_update_overtime_record(sender, instance, created, **kwargs):
    # Calculate worked duration and check against the standard work duration of 9 hours
    if instance.in_time and instance.out_time:
        start = datetime.combine(instance.date, instance.in_time)
        end = datetime.combine(instance.date, instance.out_time)
        worked_duration = end - start
        standard_work_duration = timedelta(hours=9)
        
        if worked_duration > standard_work_duration:
            overtime_duration = worked_duration - standard_work_duration
            Overtime.objects.update_or_create(
                employee=instance.employee,
                date=instance.date,
                defaults={'in_time': instance.in_time, 'out_time': instance.out_time, 'total_overtime': overtime_duration, 'is_half_day': False}
            )
