from django.db import models
from django.utils import timezone
from datetime import datetime, time, timedelta, date

# Assuming you have an Employee model in your Employees app
from Employees.models import Employee

class AttendanceRecord(models.Model):
    # Defining attendance statuses as a choice field for clarity and validation
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('leave', 'Leave'),
        ('half_day', 'Half Day'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField(default=timezone.now)
    in_time = models.TimeField(blank=True, null=True)  # Optional, as there might be absent days
    out_time = models.TimeField(blank=True, null=True) # Optional, as there might be absent days
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='present')
    punctuality_bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, help_text="Punctuality/Attendance bonus for the day")

    class Meta:
        unique_together = ('employee', 'date')  # Ensuring one record per employee per day
        ordering = ['-date', 'employee']  # Default ordering

    def __str__(self):
        return f"{self.employee.name} - {self.date} - {self.status}"

    @property
    def is_present(self):
        return self.status == 'present'

    @property
    def is_absent(self):
        return self.status == 'absent'

    # Additional methods can be added here to handle business logic, like calculating overtime
class Holiday(models.Model):
    date = models.DateField(unique=True)
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=50, blank=True, null=True, help_text="Group designation for targeted holidays")

    class Meta:
        ordering = ['date']

    def __str__(self):
        group_part = f" - {self.group}" if self.group else ""
        return f"{self.name} on {self.date}{group_part}"

class Overtime(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='overtimes')
    date = models.DateField()
    in_time = models.TimeField()
    out_time = models.TimeField()
    is_half_day = models.BooleanField(default=False, help_text="Indicates if the work duration was less than standard, marking it as a half day")
    # total_overtime = models.DurationField(help_text="Calculated as the difference between OUT and IN time")
    total_overtime = models.DurationField(help_text="Calculated as the difference between OUT and IN time", blank=True, null=True)

    class Meta:
        unique_together = ('employee', 'date')
        ordering = ['-date', 'employee']

    def __str__(self):
        overtime_hours = self.total_overtime.total_seconds() / 3600 if self.total_overtime else 0
        half_day_status = "Half Day" if self.is_half_day else "Full Day"
        return f"{self.employee.name} - {self.date}: {overtime_hours} hours ({half_day_status})"

    def save(self, *args, **kwargs):
        if self.in_time and self.out_time:
            start = datetime.combine(self.date, self.in_time)
            end = datetime.combine(self.date, self.out_time)
            worked_duration = end - start
            standard_work_duration = timedelta(hours=9)  # 9 hours of standard work duration
            overtime = worked_duration - standard_work_duration
            
            # Check if worked duration is less than standard, indicating a half day
            if worked_duration < standard_work_duration:
                self.is_half_day = True
                self.total_overtime = timedelta()  # Reset overtime to zero since it's a half day
            else:
                self.is_half_day = False
                self.total_overtime = overtime  # Record overtime only if it's positive
                
        super(Overtime, self).save(*args, **kwargs)