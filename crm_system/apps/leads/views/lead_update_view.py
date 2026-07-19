"""Представление для редактирования потенциального клиента."""

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from apps.leads.models import Lead


class LeadUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Представление для редактирования существующего потенциального клиента.

    :ivar model: Модель, связанная с представлением.
    :vartype model: type[Lead]
    :ivar fields: Список полей формы, доступных для редактирования.
    :vartype fields: list[str]
    :ivar template_name: Путь к HTML-шаблону страницы редактирования.
    :vartype template_name: str
    :ivar success_url: URL для перенаправления после успешного обновления.
    :vartype success_url: str
    :ivar permission_required: Требуемое разрешение для доступа к представлению.
    :vartype permission_required: str
    """

    model = Lead
    fields = ["full_name", "phone", "email", "ad_campaign"]
    template_name = "leads/leads-edit.html"
    success_url = reverse_lazy("leads:leads-list")
    permission_required = "leads.change_lead"
