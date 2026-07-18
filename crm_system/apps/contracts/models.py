"""Модель контракта."""

from django.db import models


class Contract(models.Model):
    """Модель для хранения данных о контракте на предоставление услуги.

    :ivar name: Название контракта.
    :vartype name: str
    :ivar product: Предоставляемая услуга (связь с моделью Product).
    :vartype product: Product
    :ivar document: Файл с документом контракта.
    :vartype document: django.db.models.fields.files.FieldFile
    :ivar conclusion_date: Дата заключения контракта.
    :vartype conclusion_date: datetime.date
    :ivar duration: Период действия контракта в днях.
    :vartype duration: int
    :ivar amount: Сумма контракта.
    :vartype amount: decimal.Decimal
    """

    name = models.CharField(max_length=255, unique=True, verbose_name="Название")
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="contracts",
        verbose_name="Услуга",
    )
    document = models.FileField(
        upload_to="contracts/documents/%Y/%m", verbose_name="Файл"
    )
    conclusion_date = models.DateField(verbose_name="Дата заключения")
    duration = models.PositiveIntegerField(verbose_name="Период действия (дней)")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")

    class Meta:
        verbose_name = "Контракт"
        verbose_name_plural = "Контракты"
        ordering = ("-conclusion_date",)

    def __str__(self) -> str:
        """Возвращает строковое представление контракта.

        :returns: Название контракта.
        :rtype: str
        """
        return self.name
