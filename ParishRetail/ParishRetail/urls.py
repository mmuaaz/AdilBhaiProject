from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('admin_soft.urls')),
    path('Attendance/', include('Attendance.urls')),
    path('Employees/', include('Employees.urls')),
    path('Salaries/', include('Salaries.urls')),
    path('Sales/', include('Sales.urls')),
]

# superuser = adil
# pass = parish321