"""Представление для отображения списка активных клиентов."""

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView

from apps.customers.models import Customer


class CustomerListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Представление для отображения списка всех активных клиентов.

    :ivar model: Модель, связанная с представлением.
    :vartype model: type[Customer]
    :ivar template_name: Путь к HTML-шаблону страницы списка.
    :vartype template_name: str
    :ivar context_object_name: Имя переменной контекста для списка объектов.
    :vartype context_object_name: str
    :ivar permission_required: Требуемое разрешение для доступа к представлению.
    :vartype permission_required: str
    """

    model = Customer
    template_name = "customers/customers-list.html"
    context_object_name = "customers"
    permission_required = "customers.view_customer"
