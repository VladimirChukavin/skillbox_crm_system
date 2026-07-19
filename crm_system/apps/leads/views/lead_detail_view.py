"""Представление для отображения детальной информации о потенциальном клиенте."""

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import DetailView

from apps.leads.models import Lead


class LeadDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Представление для отображения детальной информации о потенциальном клиенте.

    :ivar model: Модель, связанная с представлением.
    :vartype model: type[Lead]
    :ivar template_name: Путь к HTML-шаблону детальной страницы.
    :vartype template_name: str
    :ivar permission_required: Требуемое разрешение для доступа к представлению.
    :vartype permission_required: str
    """

    model = Lead
    template_name = "leads/leads-detail.html"
    permission_required = "leads.view_lead"
