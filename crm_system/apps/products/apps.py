"""Конфигурация приложения «Услуги»."""

from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """Конфигурация Django-приложения для управления услугами.

    :ivar name: Полный Python-путь к пакету приложения.
    :vartype name: str
    :ivar verbose_name: Читаемое название приложения.
    :vartype verbose_name: str
    """

    name = "apps.products"
    verbose_name = "Услуги"
