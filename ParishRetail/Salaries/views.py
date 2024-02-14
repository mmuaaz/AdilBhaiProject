from django.views.generic import DetailView
from .models import SalaryBreakdown

class SalarySlipView(DetailView):
    model = SalaryBreakdown
    context_object_name = 'salary'
    template_name = 'salary_slip.html'
