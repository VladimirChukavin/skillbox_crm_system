"""Настройки административной панели для услуг."""

from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Конфигурация отображения услуг в админ-панели Django.

    :ivar list_display: Поля, отображаемые в списке записей.
    :vartype list_display: tuple[str, ...]
    :ivar list_display_links: Поля, являющиеся ссылками на форму редактирования.
    :vartype list_display_links: tuple[str, ...]
    :ivar search_fields: Поля, доступные для поиска.
    :vartype search_fields: tuple[str, ...]
    :ivar ordering: Порядок сортировки записей по умолчанию.
    :vartype ordering: tuple[str, ...]
    """

    list_display: tuple[str, ...] = ("id", "name", "price")
    list_display_links: tuple[str, ...] = ("id", "name")
    search_fields: tuple[str, ...] = ("name",)
    ordering: tuple[str, ...] = ("name",)
