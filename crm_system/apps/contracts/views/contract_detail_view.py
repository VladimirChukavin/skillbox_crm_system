"""Представление для отображения детальной информации о контракте."""

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import DetailView

from apps.contracts.models import Contract


class ContractDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Представление для отображения детальной информации о контракте.

    :ivar model: Модель, связанная с представлением.
    :vartype model: type[Contract]
    :ivar template_name: Путь к HTML-шаблону детальной страницы.
    :vartype template_name: str
    :ivar permission_required: Требуемое разрешение для доступа к представлению.
    :vartype permission_required: str
    """

    model = Contract
    template_name = "contracts/contracts-detail.html"
    permission_required = "contracts.view_contract"
