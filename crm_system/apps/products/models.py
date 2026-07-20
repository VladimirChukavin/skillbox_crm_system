"""Модель услуги."""

from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    """Модель для хранения данных об услуге.

    :ivar name: Название услуги.
    :vartype name: str
    :ivar description: Описание услуги.
    :vartype description: str
    :ivar price: Стоимость услуги.
    :vartype price: decimal.Decimal
    """

    name = models.CharField(max_length=255, unique=True, verbose_name="Название")
    description = models.TextField(blank=True, default="", verbose_name="Описание")
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Стоимость",
    )

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ("name",)

    def __str__(self) -> str:
        """Возвращает строковое представление услуги.

        :returns: Название услуги.
        :rtype: str
        """
        return self.name
