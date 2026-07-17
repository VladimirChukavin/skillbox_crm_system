from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.contracts.models import Contract


class ContractCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Contract
    fields = ["name", "product", "document", "conclusion_date", "duration", "amount"]
    template_name = "contracts/contracts-create.html"
    success_url = reverse_lazy("contracts:contracts-list")
    permission_required = "contracts.add_contract"
