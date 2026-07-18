"""Представление для удаления активного клиента."""

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from apps.customers.models import Customer


class CustomerDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Представление для удаления существующего активного клиента.

    :ivar model: Модель, связанная с представлением.
    :vartype model: type[Customer]
    :ivar template_name: Путь к HTML-шаблону страницы подтверждения удаления.
    :vartype template_name: str
    :ivar success_url: URL для перенаправления после успешного удаления.
    :vartype success_url: str
    :ivar permission_required: Требуемое разрешение для доступа к представлению.
    :vartype permission_required: str
    """

    model = Customer
    template_name = "customers/customers-delete.html"
    success_url = reverse_lazy("customers:customers-list")
    permission_required = "customers.delete_customer"
