"""Представление для создания контракта."""

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.contracts.models import Contract


class ContractCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Представление для создания нового контракта.

    :ivar model: Модель, связанная с представлением.
    :vartype model: type[Contract]
    :ivar fields: Список полей формы, доступных для заполнения.
    :vartype fields: list[str]
    :ivar template_name: Путь к HTML-шаблону страницы создания.
    :vartype template_name: str
    :ivar success_url: URL для перенаправления после успешного создания.
    :vartype success_url: str
    :ivar permission_required: Требуемое разрешение для доступа к представлению.
    :vartype permission_required: str
    """

    model = Contract
    fields = ["name", "product", "document", "conclusion_date", "duration", "amount"]
    template_name = "contracts/contracts-create.html"
    success_url = reverse_lazy("contracts:contracts-list")
    permission_required = "contracts.add_contract"
