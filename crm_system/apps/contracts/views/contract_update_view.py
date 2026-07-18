"""Представление для редактирования контракта."""

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from apps.contracts.models import Contract


class ContractUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Представление для редактирования существующего контракта.

    :ivar model: Модель, связанная с представлением.
    :vartype model: type[Contract]
    :ivar fields: Список полей формы, доступных для редактирования.
    :vartype fields: list[str]
    :ivar template_name: Путь к HTML-шаблону страницы редактирования.
    :vartype template_name: str
    :ivar success_url: URL для перенаправления после успешного обновления.
    :vartype success_url: str
    :ivar permission_required: Требуемое разрешение для доступа к представлению.
    :vartype permission_required: str
    """

    model = Contract
    fields = ["name", "product", "document", "conclusion_date", "duration", "amount"]
    template_name = "contracts/contracts-edit.html"
    success_url = reverse_lazy("contracts:contracts-list")
    permission_required = "contracts.change_contract"
