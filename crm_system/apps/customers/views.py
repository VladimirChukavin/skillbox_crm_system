from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from .models import Customer


class CustomerListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Customer
    template_name = "customers/customers-list.html"
    context_object_name = "customers"
    permission_required = "customers.view_customer"


class CustomerCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Customer
    fields = ["lead", "contract"]
    template_name = "customers/customers-create.html"
    success_url = reverse_lazy("customers:customers-list")
    permission_required = "customers.add_customer"

    def get_initial(self):
        initial = super().get_initial()
        lead_pk = self.request.GET.get("lead")

        if lead_pk:
            initial["lead"] = lead_pk

        return initial


class CustomerDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Customer
    template_name = "customers/customers-detail.html"
    permission_required = "customers.view_customer"


class CustomerUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Customer
    fields = ["lead", "contract"]
    template_name = "customers/customers-edit.html"
    success_url = reverse_lazy("customers:customers-list")
    permission_required = "customers.change_customer"


class CustomerDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Customer
    template_name = "customers/customers-delete.html"
    success_url = reverse_lazy("customers:customers-list")
    permission_required = "customers.delete_customer"
