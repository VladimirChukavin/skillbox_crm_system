from django.db import models


class Customer(models.Model):
    lead = models.OneToOneField(
        "leads.Lead",
        on_delete=models.CASCADE,
        related_name="customer",
        verbose_name="Активный клиент",
    )
    contract = models.ForeignKey(
        "contracts.Contract",
        on_delete=models.CASCADE,
        related_name="customers",
        verbose_name="Контракт",
    )

    class Meta:
        verbose_name = "Активный клиент"
        verbose_name_plural = "Активные клиенты"
        ordering = ("lead__full_name",)

    def __str__(self):
        return f"Активный клиент: {self.lead.full_name}"
