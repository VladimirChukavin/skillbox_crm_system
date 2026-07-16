from django.db import models


class Lead(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="Ф.И.О")
    phone = models.CharField(max_length=15, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
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

    def __str__(self):
        return self.full_name
