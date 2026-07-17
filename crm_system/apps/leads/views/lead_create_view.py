from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.leads.models import Lead


class LeadCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Lead
    fields = ["full_name", "phone", "email", "ad_campaign"]
    template_name = "leads/leads-create.html"
    success_url = reverse_lazy("leads:leads-list")
    permission_required = "leads.add_lead"
