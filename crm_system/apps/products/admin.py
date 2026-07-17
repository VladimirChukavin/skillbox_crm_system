from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display: tuple[str, ...] = ("id", "name", "price")
    list_display_links: tuple[str, ...] = ("id", "name")
    search_fields: tuple[str, ...] = ("name",)
    ordering: tuple[str, ...] = ("name",)
