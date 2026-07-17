from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from apps.leads.models import Lead


class LeadDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Lead
    template_name = "leads/leads-delete.html"
    success_url = reverse_lazy("leads:leads-list")
    permission_required = "leads.delete_lead"
