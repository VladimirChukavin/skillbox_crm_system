"""Настройки административной панели для потенциальных клиентов."""

from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    """Конфигурация отображения потенциальных клиентов в админ-панели Django.

    В список не попадают лиды, которые уже были преобразованы в активных
    клиентов (исключаются через фильтр customer__isnull=True).

    :ivar list_display: Поля, отображаемые в списке записей.
    :vartype list_display: tuple[str, ...]
    :ivar list_display_links: Поля, являющиеся ссылками на форму редактирования.
    :vartype list_display_links: tuple[str, ...]
    :ivar search_fields: Поля, доступные для поиска.
    :vartype search_fields: tuple[str, ...]
    :ivar list_filter: Поля для боковой панели фильтрации.
    :vartype list_filter: tuple[str, ...]
    :ivar ordering: Порядок сортировки записей по умолчанию.
    :vartype ordering: tuple[str, ...]
    :ivar autocomplete_fields: Поля с автодополнением.
    :vartype autocomplete_fields: tuple[str, ...]
    """

    list_display: tuple[str, ...] = ("id", "full_name", "phone", "email", "ad_campaign")
    list_display_links: tuple[str, ...] = ("full_name",)
    search_fields: tuple[str, ...] = ("full_name", "phone", "email")
    list_filter: tuple[str, ...] = ("ad_campaign", "ad_campaign__product")
    ordering: tuple[str, ...] = ("full_name",)
    autocomplete_fields: tuple[str, ...] = ("ad_campaign",)

    def get_queryset(self, request: HttpRequest) -> QuerySet[Lead]:
        """Возвращает queryset лидов, не преобразованных в активных клиентов.

        :param request: HTTP-запрос текущего пользователя админ-панели.
        :type request: HttpRequest
        :returns: QuerySet лидов без связи с моделью Customer.
        :rtype: QuerySet[Lead]
        """
        return super().get_queryset(request).filter(customer__isnull=True)
