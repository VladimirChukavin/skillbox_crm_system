from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from apps.contracts.models import Contract


class ContractUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Contract
    fields = ["name", "product", "document", "conclusion_date", "duration", "amount"]
    template_name = "contracts/contracts-edit.html"
    success_url = reverse_lazy("contracts:contracts-list")
    permission_required = "contracts.change_contract"
