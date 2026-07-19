"""Представление для отображения списка потенциальных клиентов."""

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import QuerySet
from django.views.generic import ListView

from apps.leads.models import Lead


class LeadListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Представление для отображения списка потенциальных клиентов.

    В список не попадают лиды, которые уже были преобразованы в активных
    клиентов (исключаются через фильтр customer__isnull=True).

    :ivar model: Модель, связанная с представлением.
    :vartype model: type[Lead]
    :ivar template_name: Путь к HTML-шаблону страницы списка.
    :vartype template_name: str
    :ivar context_object_name: Имя переменной контекста для списка объектов.
    :vartype context_object_name: str
    :ivar permission_required: Требуемое разрешение для доступа к представлению.
    :vartype permission_required: str
    """

    model = Lead
    template_name = "leads/leads-list.html"
    context_object_name = "leads"
    permission_required = "leads.view_lead"

    def get_queryset(self) -> QuerySet[Lead]:
        """Возвращает queryset лидов, не преобразованных в активных клиентов.

        :returns: QuerySet лидов без связи с моделью Customer.
        :rtype: QuerySet[Lead]
        """
        return Lead.objects.filter(customer__isnull=True)
