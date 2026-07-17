from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from apps.customers.models import Customer


class CustomerUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Customer
    fields = ["lead", "contract"]
    template_name = "customers/customers-edit.html"
    success_url = reverse_lazy("customers:customers-list")
    permission_required = "customers.change_customer"
