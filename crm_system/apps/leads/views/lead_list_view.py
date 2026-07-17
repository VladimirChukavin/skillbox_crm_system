from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import QuerySet
from django.views.generic import ListView

from apps.leads.models import Lead


class LeadListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Lead
    template_name = "leads/leads-list.html"
    context_object_name = "leads"
    permission_required = "leads.view_lead"

    def get_queryset(self) -> QuerySet[Lead]:
        return Lead.objects.filter(customer__isnull=True)
