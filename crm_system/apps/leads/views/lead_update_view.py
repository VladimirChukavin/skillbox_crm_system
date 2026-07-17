from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from apps.leads.models import Lead


class LeadUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Lead
    fields = ["full_name", "phone", "email", "ad_campaign"]
    template_name = "leads/leads-edit.html"
    success_url = reverse_lazy("leads:leads-list")
    permission_required = "leads.change_lead"
