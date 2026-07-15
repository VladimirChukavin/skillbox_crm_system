from django.contrib import admin

from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "phone", "email", "ad_campaign")
    list_display_links = ("full_name",)
    search_fields = ("full_name", "phone", "email")
    list_filter = ("ad_campaign",)
