from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView

from apps.customers.models import Customer


class CustomerListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Customer
    template_name = "customers/customers-list.html"
    context_object_name = "customers"
    permission_required = "customers.view_customer"
