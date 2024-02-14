# Generated by Django 5.0.2 on 2024-02-12 19:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Employees", "0002_rename_employee_cnic_employee_employee_cnic_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="employee",
            old_name="employee_CNIC",
            new_name="CNIC",
        ),
        migrations.RenameField(
            model_name="employee",
            old_name="employee_Holiday",
            new_name="Holiday",
        ),
        migrations.RenameField(
            model_name="employee",
            old_name="employee_JobDescription",
            new_name="JobDescription",
        ),
        migrations.RenameField(
            model_name="employee",
            old_name="employee_Designation",
            new_name="Last_name",
        ),
        migrations.RenameField(
            model_name="employee",
            old_name="employee_Salary",
            new_name="Salary",
        ),
        migrations.RenameField(
            model_name="employee",
            old_name="employee_Last_name",
            new_name="designation",
        ),
        migrations.RenameField(
            model_name="employee",
            old_name="employee_holiday_group",
            new_name="holiday_group",
        ),
        migrations.RenameField(
            model_name="employee",
            old_name="employee_name",
            new_name="name",
        ),
    ]