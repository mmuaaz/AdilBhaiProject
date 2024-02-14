# Generated by Django 5.0.2 on 2024-02-12 15:24

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Employee_name", models.CharField(max_length=50)),
                ("Employee_Last_name", models.CharField(max_length=50)),
                ("Employee_CNIC", models.IntegerField()),
                ("Employee_Designation", models.CharField(max_length=50)),
                ("Employee_JobDescription", models.TextField(max_length=300)),
                ("Employee_Holiday", models.CharField(max_length=10)),
                ("Employee_Salary", models.IntegerField()),
                ("Employee_holiday_group", models.CharField(max_length=10)),
            ],
        ),
    ]
