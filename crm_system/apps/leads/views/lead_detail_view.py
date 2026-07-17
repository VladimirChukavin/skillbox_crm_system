from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import DetailView

from apps.leads.models import Lead


class LeadDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Lead
    template_name = "leads/leads-detail.html"
    permission_required = "leads.view_lead"
