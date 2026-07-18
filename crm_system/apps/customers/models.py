"""Модель активного клиента."""

from django.db import models


class Customer(models.Model):
    """Модель для хранения данных об активном клиенте.

    Активный клиент создаётся из потенциального клиента (Lead) после
    заключения контракта. Связь OneToOne гарантирует, что каждый лид
    может быть переведён в активного клиента только один раз.

    :ivar lead: Потенциальный клиент (связь OneToOne с моделью Lead).
    :vartype lead: Lead
    :ivar contract: Контракт, заключённый с клиентом (связь с моделью Contract).
    :vartype contract: Contract
    """

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

    def __str__(self) -> str:
        """Возвращает строковое представление активного клиента.

        :returns: Название вида "Активный клиент: <Ф.И.О.>".
        :rtype: str
        """
        return f"Активный клиент: {self.lead.full_name}"
