"""Представление для удаления контракта."""

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from apps.contracts.models import Contract


class ContractDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Представление для удаления существующего контракта.

    :ivar model: Модель, связанная с представлением.
    :vartype model: type[Contract]
    :ivar template_name: Путь к HTML-шаблону страницы подтверждения удаления.
    :vartype template_name: str
    :ivar success_url: URL для перенаправления после успешного удаления.
    :vartype success_url: str
    :ivar permission_required: Требуемое разрешение для доступа к представлению.
    :vartype permission_required: str
    """

    model = Contract
    template_name = "contracts/contracts-delete.html"
    success_url = reverse_lazy("contracts:contracts-list")
    permission_required = "contracts.delete_contract"
