"""Конфигурация приложения «Рекламные кампании»."""

from django.apps import AppConfig


class AdsConfig(AppConfig):
    """Конфигурация Django-приложения для управления рекламными кампаниями.

    :ivar name: Полный Python-путь к пакету приложения.
    :vartype name: str
    :ivar verbose_name: Читаемое название приложения.
    :vartype verbose_name: str
    """

    name = "apps.ads"
    verbose_name = "Рекламные кампании"
