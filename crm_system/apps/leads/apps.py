"""Конфигурация приложения «Потенциальные клиенты»."""

from django.apps import AppConfig


class LeadsConfig(AppConfig):
    """Конфигурация Django-приложения для управления потенциальными клиентами.

    :ivar name: Полный Python-путь к пакету приложения.
    :vartype name: str
    :ivar verbose_name: Читаемое название приложения.
    :vartype verbose_name: str
    """

    name = "apps.leads"
    verbose_name = "Потенциальные клиенты"
