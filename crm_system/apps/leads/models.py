"""Модель потенциального клиента."""

from django.core.validators import RegexValidator
from django.db import models


class Lead(models.Model):
    """Модель для хранения данных о потенциальном клиенте.

    :ivar full_name: Ф.И.О потенциального клиента.
    :vartype full_name: str
    :ivar phone: Номер телефона.
    :vartype phone: str
    :ivar email: Электронная почта.
    :vartype email: str
    :ivar ad_campaign: Рекламная кампания, из которой пришёл лид (связь с моделью AdCampaign).
    :vartype ad_campaign: AdCampaign
    """

    full_name = models.CharField(
        max_length=255,
        validators=[
            RegexValidator(
                regex=r"^[А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+$",
                message="Ф.И.О должно быть в формате: Иванов Иван Иванович",
            )
        ],
        verbose_name="Ф.И.О",
    )
    phone = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r"^\+?1?\d{9,15}$",
                message="Номер телефона должен быть в формате: +71234567890",
            )
        ],
        verbose_name="Телефон",
        null=True,
        blank=True,
    )
    email = models.EmailField(
        max_length=255, verbose_name="Email", null=True, blank=True
    )
    ad_campaign = models.ForeignKey(
        "ads.AdCampaign",
        on_delete=models.CASCADE,
        related_name="leads",
        verbose_name="Рекламная кампания",
    )

    class Meta:
        verbose_name = "Потенциальный клиент"
        verbose_name_plural = "Потенциальные клиенты"
        ordering = ("full_name",)

    def __str__(self) -> str:
        """Возвращает строковое представление потенциального клиента.

        :returns: Ф.И.О потенциального клиента.
        :rtype: str
        """
        return self.full_name
