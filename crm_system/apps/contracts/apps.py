"""Конфигурация приложения «Контракты»."""

from django.apps import AppConfig


class ContractsConfig(AppConfig):
    """Конфигурация Django-приложения для управления контрактами.

    :ivar name: Полный Python-путь к пакету приложения.
    :vartype name: str
    :ivar verbose_name: Читаемое название приложения.
    :vartype verbose_name: str
    """

    name = "apps.contracts"
    verbose_name = "Контракты"
