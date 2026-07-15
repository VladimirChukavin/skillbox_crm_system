from django.db import models


class AdCampaign(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Название")
    product = models.ForeignKey(
        "Product",
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

    def __str__(self):
        return self.name
