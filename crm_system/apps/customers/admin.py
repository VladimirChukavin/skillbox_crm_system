from django.contrib import admin

from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "lead", "contract")
    list_display_links = ("lead",)
    search_fields = ("lead__full_name",)
