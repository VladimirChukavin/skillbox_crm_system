from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import DetailView

from apps.contracts.models import Contract


class ContractDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Contract
    template_name = "contracts/contracts-detail.html"
    permission_required = "contracts.view_contract"
