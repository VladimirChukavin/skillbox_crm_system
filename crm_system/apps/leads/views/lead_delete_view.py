"""Представление для удаления потенциального клиента."""

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from apps.leads.models import Lead


class LeadDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Представление для удаления существующего потенциального клиента.

    :ivar model: Модель, связанная с представлением.
    :vartype model: type[Lead]
    :ivar template_name: Путь к HTML-шаблону страницы подтверждения удаления.
    :vartype template_name: str
    :ivar success_url: URL для перенаправления после успешного удаления.
    :vartype success_url: str
    :ivar permission_required: Требуемое разрешение для доступа к представлению.
    :vartype permission_required: str
    """

    model = Lead
    template_name = "leads/leads-delete.html"
    success_url = reverse_lazy("leads:leads-list")
    permission_required = "leads.delete_lead"
