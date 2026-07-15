from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from .models import Contract


class ContractListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Contract
    template_name = "contracts/contracts-list.html"
    context_object_name = "contracts"
    permission_required = "contracts.view_contract"


class ContractCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Contract
    fields = ["name", "product", "document", "conclusion_date", "duration", "amount"]
    template_name = "contracts/contracts-create.html"
    success_url = reverse_lazy("contracts:contracts-list")
    permission_required = "contracts.add_contract"


class ContractDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Contract
    template_name = "contracts/contracts-detail.html"
    permission_required = "contracts.view_contract"


class ContractUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Contract
    fields = ["name", "product", "document", "conclusion_date", "duration", "amount"]
    template_name = "contracts/contracts-edit.html"
    success_url = reverse_lazy("contracts:contracts-list")
    permission_required = "contracts.change_contract"


class ContractDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Contract
    template_name = "contracts/contracts-delete.html"
    success_url = reverse_lazy("contracts:contracts-list")
    permission_required = "contracts.delete_contract"
