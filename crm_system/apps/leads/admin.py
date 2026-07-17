from django.contrib import admin
from django.db.models import QuerySet

from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display: tuple[str, ...] = ("id", "full_name", "phone", "email", "ad_campaign")
    list_display_links: tuple[str, ...] = ("full_name",)
    search_fields: tuple[str, ...] = ("full_name", "phone", "email")
    list_filter: tuple[str, ...] = ("ad_campaign", "ad_campaign__product")
    ordering: tuple[str, ...] = ("full_name",)
    autocomplete_fields: tuple[str, ...] = ("ad_campaign",)

    def get_queryset(self, request) -> QuerySet[Lead]:
        return super().get_queryset(request).filter(customer__isnull=True)
