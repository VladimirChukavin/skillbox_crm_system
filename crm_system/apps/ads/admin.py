from django.contrib import admin

from .models import AdCampaign


@admin.register(AdCampaign)
class AdCampaignAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "product", "channel", "budget")
    list_display_links = ("id", "name")
    search_fields = ("id", "name", "channel", "budget")
