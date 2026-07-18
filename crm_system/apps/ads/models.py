"""Модель рекламной кампании."""

from django.db import models


class AdCampaign(models.Model):
    """Модель для хранения данных о рекламной кампании.

    :ivar name: Название рекламной кампании.
    :vartype name: str
    :ivar product: Рекламируемая услуга (связь с моделью Product).
    :vartype product: Product
    :ivar channel: Канал продвижения.
    :vartype channel: str
    :ivar budget: Бюджет на рекламу.
    :vartype budget: decimal.Decimal
    """

    name = models.CharField(max_length=255, unique=True, verbose_name="Название")
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="ad_campaigns",
        verbose_name="Рекламируемая услуга",
    )
    channel = models.CharField(max_length=255, verbose_name="Канал продвижения")
    budget = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Бюджет")

    class Meta:
        verbose_name = "Рекламная кампания"
        verbose_name_plural = "Рекламные кампании"
        ordering = ("name",)

    def __str__(self) -> str:
        """Возвращает строковое представление рекламной кампании.

        :returns: Название рекламной кампании.
        :rtype: str
        """
        return self.name
