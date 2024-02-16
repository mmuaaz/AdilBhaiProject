from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    CNIC = models.IntegerField()
    designation = models.CharField(max_length=50)
    JobDescription = models.TextField(max_length=300)
    Holiday = models.CharField(max_length=10)
    Salary = models.IntegerField()
    holiday_group = models.CharField(max_length =10)
    
    def __str__(self):
        return f"{self.name} , {self.Last_name}" 
