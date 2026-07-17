from django.contrib import admin

from .models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
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
