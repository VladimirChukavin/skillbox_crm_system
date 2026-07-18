"""Настройки административной панели для активных клиентов."""

from django.contrib import admin

from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Конфигурация отображения активных клиентов в админ-панели Django.

    :ivar list_display: Поля, отображаемые в списке записей.
    :vartype list_display: tuple[str, ...]
    :ivar list_display_links: Поля, являющиеся ссылками на форму редактирования.
    :vartype list_display_links: tuple[str, ...]
    :ivar search_fields: Поля, доступные для поиска.
    :vartype search_fields: tuple[str, ...]
    :ivar ordering: Порядок сортировки записей по умолчанию.
    :vartype ordering: tuple[str, ...]
    :ivar autocomplete_fields: Поля с автодополнением.
    :vartype autocomplete_fields: tuple[str, ...]
    """

    list_display: tuple[str, ...] = ("id", "lead", "contract")
    list_display_links: tuple[str, ...] = ("lead",)
    search_fields: tuple[str, ...] = ("lead__full_name", "contract__name")
    ordering: tuple[str, ...] = ("lead__full_name",)
    autocomplete_fields: tuple[str, ...] = ("lead", "contract")
