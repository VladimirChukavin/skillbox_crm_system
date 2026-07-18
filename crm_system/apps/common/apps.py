"""Конфигурация приложения «Общие настройки»."""

from django.apps import AppConfig


class CommonConfig(AppConfig):
    """Конфигурация Django-приложения для общих настроек.

    :ivar name: Полный Python-путь к пакету приложения.
    :vartype name: str
    """

    name = "apps.common"
