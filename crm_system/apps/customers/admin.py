from django.contrib import admin

from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display: tuple[str, ...] = ("id", "lead", "contract")
    list_display_links: tuple[str, ...] = ("lead",)
    search_fields: tuple[str, ...] = ("lead__full_name", "contract__name")
    ordering: tuple[str, ...] = ("lead__full_name",)
    autocomplete_fields: tuple[str, ...] = ("lead", "contract")
