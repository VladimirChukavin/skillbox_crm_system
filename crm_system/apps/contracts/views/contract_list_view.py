"""Представление для отображения списка контрактов."""

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView

from apps.contracts.models import Contract


class ContractListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Представление для отображения списка всех контрактов.

    :ivar model: Модель, связанная с представлением.
    :vartype model: type[Contract]
    :ivar template_name: Путь к HTML-шаблону страницы списка.
    :vartype template_name: str
    :ivar context_object_name: Имя переменной контекста для списка объектов.
    :vartype context_object_name: str
    :ivar permission_required: Требуемое разрешение для доступа к представлению.
    :vartype permission_required: str
    """

    model = Contract
    template_name = "contracts/contracts-list.html"
    context_object_name = "contracts"
    permission_required = "contracts.view_contract"
