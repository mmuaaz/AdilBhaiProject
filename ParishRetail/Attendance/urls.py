from django.urls import path
from .views import AttendanceSheetView, OvertimeReportView, MarkAttendanceView

urlpatterns = [
    path('attendance/<int:pk>/', AttendanceSheetView.as_view(), name='attendance_sheet'),
    path('overtime-report/', OvertimeReportView.as_view(), name='overtime_report'),
    path('mark-attendance/', MarkAttendanceView.as_view(), name='mark_attendance'),
]