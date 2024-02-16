from django.contrib import admin
from .models import AttendanceRecord, Overtime
# Register your models here.
admin.site.register(AttendanceRecord)
admin.site.register(Overtime)