from django.db import models
from Employees.models import Employee
from django.utils import timezone

class SalesRecord(models.Model):
    date = models.DateField()
    total_sales = models.DecimalField(max_digits=15, decimal_places=2)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='sales_records')
    # Additional fields can be added to track sales by item or category if needed

    class Meta:
        unique_together = ('employee', 'date')  # Assuming an employee can have only one sales record per day
        ordering = ['-date', 'employee']

    def __str__(self):
        return f"Sales on {self.date} by {self.employee.name if self.employee else 'N/A'}: {self.total_sales}"


class SalesTarget(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='sales_targets')
    month = models.DateField()
    target_amount = models.DecimalField(max_digits=15, decimal_places=2)
    actual_amount = models.DecimalField(max_digits=15, decimal_places=2)
    achievement_percentage = models.FloatField(help_text="Automatically calculated as actual/target * 100", blank=True, null=True)

    class Meta:
        unique_together = ('employee', 'month')
        ordering = ['-month', 'employee']

    def __str__(self):
        return f"{self.employee.name} - Target for {self.month.strftime('%B %Y')}: {self.achievement_percentage}%"

    def save(self, *args, **kwargs):
        if self.actual_amount and self.target_amount:
            self.achievement_percentage = (self.actual_amount / self.target_amount) * 100
        super(SalesTarget, self).save(*args, **kwargs)
