from django.contrib import admin

from .models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "product", "conclusion_date", "amount")
    list_display_links = ("name",)
    search_fields = ("name",)
    list_filter = ("product", "conclusion_date", "amount")
