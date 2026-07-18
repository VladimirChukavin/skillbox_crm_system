"""Представление для редактирования активного клиента."""

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from apps.customers.models import Customer


class CustomerUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Представление для редактирования существующего активного клиента.

    :ivar model: Модель, связанная с представлением.
    :vartype model: type[Customer]
    :ivar fields: Список полей формы, доступных для редактирования.
    :vartype fields: list[str]
    :ivar template_name: Путь к HTML-шаблону страницы редактирования.
    :vartype template_name: str
    :ivar success_url: URL для перенаправления после успешного обновления.
    :vartype success_url: str
    :ivar permission_required: Требуемое разрешение для доступа к представлению.
    :vartype permission_required: str
    """

    model = Customer
    fields = ["lead", "contract"]
    template_name = "customers/customers-edit.html"
    success_url = reverse_lazy("customers:customers-list")
    permission_required = "customers.change_customer"
