"""Настройки административной панели для контрактов."""

from django.contrib import admin

from .models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    """Конфигурация отображения контрактов в админ-панели Django.

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
    :ivar readonly_fields: Поля, доступные только для чтения.
    :vartype readonly_fields: tuple[str, ...]
    """

    list_display: tuple[str, ...] = (
        "id",
        "name",
        "product",
        "conclusion_date",
        "amount",
    )
    list_display_links: tuple[str, ...] = ("name",)
    search_fields: tuple[str, ...] = ("name",)
    list_filter: tuple[str, ...] = ("product", "conclusion_date", "amount")
    ordering: tuple[str, ...] = ("name", "-conclusion_date")
    autocomplete_fields: tuple[str, ...] = ("product",)
    readonly_fields: tuple[str, ...] = ("conclusion_date",)
