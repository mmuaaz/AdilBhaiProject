# Generated by Django 5.0.2 on 2024-02-12 15:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("Employees", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SalaryBreakdown",
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
                ("period", models.DateField()),
                ("base_salary", models.DecimalField(decimal_places=2, max_digits=15)),
                (
                    "lunch_allowance",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "attendance_bonus",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "sales_bonus",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "overtime_bonus",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "deductions",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        help_text="Sum of all deductions like half day, leaves, etc.",
                        max_digits=10,
                    ),
                ),
                (
                    "total_salary",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        help_text="Automatically calculated",
                        max_digits=15,
                        null=True,
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="salary_breakdowns",
                        to="Employees.employee",
                    ),
                ),
            ],
            options={
                "ordering": ["-period", "employee"],
            },
        ),
    ]
