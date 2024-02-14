from django.urls import path
from .views import SalesDashboardView


app_name = 'Sales'
urlpatterns = [
    path('sales-dashboard/', SalesDashboardView.as_view(), name='sales_dashboard'),
   ]