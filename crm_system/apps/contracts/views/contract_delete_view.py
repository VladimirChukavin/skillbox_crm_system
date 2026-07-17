from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from apps.contracts.models import Contract


class ContractDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Contract
    template_name = "contracts/contracts-delete.html"
    success_url = reverse_lazy("contracts:contracts-list")
    permission_required = "contracts.delete_contract"
