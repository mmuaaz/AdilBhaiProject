from django.db import models
from Employees.models import Employee

# Create your models here.
class SalaryBreakdown(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='salary_breakdowns')
    period = models.DateField()
    base_salary = models.DecimalField(max_digits=15, decimal_places=2)
    lunch_allowance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    attendance_bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sales_bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    overtime_bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0, help_text="Sum of all deductions like half day, leaves, etc.")
    total_salary = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, help_text="Automatically calculated")

    class Meta:
        ordering = ['-period', 'employee']

    def __str__(self):
        return f"{self.employee.name} - Salary Breakdown for {self.period.strftime('%B %Y')}"

    def save(self, *args, **kwargs):
        self.total_salary = self.base_salary + self.lunch_allowance + self.attendance_bonus + self.sales_bonus + self.overtime_bonus - self.deductions
        super(SalaryBreakdown, self).save(*args, **kwargs)
# Needs to check if the overtime calculations update was incorporated or not