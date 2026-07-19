"""Настройки административной панели для рекламных кампаний."""

from typing import ClassVar

from django.contrib import admin

from .models import AdCampaign


@admin.register(AdCampaign)
class AdCampaignAdmin(admin.ModelAdmin):
    """Конфигурация отображения рекламных кампаний в админ-панели Django.

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

    list_display: tuple[str, ...] = ("id", "name", "product", "channel", "budget")
    list_display_links: tuple[str, ...] = ("id", "name")
    search_fields: ClassVar[tuple[str, ...]] = ("id", "name", "channel", "budget")
    list_filter: ClassVar[tuple[str, ...]] = ("product", "channel", "budget")
    ordering: ClassVar[tuple[str, ...]] = ("name",)
    autocomplete_fields: ClassVar[tuple[str, ...]] = ("product",)
