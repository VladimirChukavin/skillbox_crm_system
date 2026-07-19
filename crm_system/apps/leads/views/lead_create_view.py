"""Представление для создания потенциального клиента."""

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.leads.models import Lead


class LeadCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Представление для создания нового потенциального клиента.

    :ivar model: Модель, связанная с представлением.
    :vartype model: type[Lead]
    :ivar fields: Список полей формы, доступных для заполнения.
    :vartype fields: list[str]
    :ivar template_name: Путь к HTML-шаблону страницы создания.
    :vartype template_name: str
    :ivar success_url: URL для перенаправления после успешного создания.
    :vartype success_url: str
    :ivar permission_required: Требуемое разрешение для доступа к представлению.
    :vartype permission_required: str
    """

    model = Lead
    fields = ["full_name", "phone", "email", "ad_campaign"]
    template_name = "leads/leads-create.html"
    success_url = reverse_lazy("leads:leads-list")
    permission_required = "leads.add_lead"
