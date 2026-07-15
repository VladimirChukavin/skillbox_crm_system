from django.db import models


class Contract(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Название")
    product = models.ForeignKey(
        "Product",
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

    def __str__(self):
        return self.name
