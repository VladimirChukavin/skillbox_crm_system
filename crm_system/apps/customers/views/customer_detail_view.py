"""Представление для отображения детальной информации об активном клиенте."""

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import DetailView

from apps.customers.models import Customer


class CustomerDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Представление для отображения детальной информации об активном клиенте.

    :ivar model: Модель, связанная с представлением.
    :vartype model: type[Customer]
    :ivar template_name: Путь к HTML-шаблону детальной страницы.
    :vartype template_name: str
    :ivar permission_required: Требуемое разрешение для доступа к представлению.
    :vartype permission_required: str
    """

    model = Customer
    template_name = "customers/customers-detail.html"
    permission_required = "customers.view_customer"
