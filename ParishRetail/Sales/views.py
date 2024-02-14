from django.views.generic import TemplateView
from .models import SalesRecord

class SalesDashboardView(TemplateView):
    template_name = 'sales_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sales_records'] = SalesRecord.objects.all()  # Adjust the query as needed
        return context
