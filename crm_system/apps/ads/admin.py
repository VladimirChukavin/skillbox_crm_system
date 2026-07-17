from django.contrib import admin

from .models import AdCampaign


@admin.register(AdCampaign)
class AdCampaignAdmin(admin.ModelAdmin):
    list_display: tuple[str, ...] = ("id", "name", "product", "channel", "budget")
    list_display_links: tuple[str, ...] = ("id", "name")
    search_fields: tuple[str, ...] = ("id", "name", "channel", "budget")
    list_filter: tuple[str, ...] = ("product", "channel", "budget")
    ordering: tuple[str, ...] = ("name",)
    autocomplete_fields: tuple[str, ...] = ("product",)
