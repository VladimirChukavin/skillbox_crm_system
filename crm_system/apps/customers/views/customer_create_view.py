from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.customers.models import Customer


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
