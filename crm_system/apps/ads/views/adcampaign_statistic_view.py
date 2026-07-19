"""Представление для отображения статистики по рекламным кампаниям."""

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.db.models import Count, QuerySet, Sum
from django.views.generic import ListView

from apps.ads.models import AdCampaign


class AdCampaignStatisticView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    ListView,
):
    """Представление для отображения статистики эффективности рекламных кампаний.

    Использует аннотации Django ORM для подсчёта количества привлечённых
    лидов, активных клиентов и суммарного дохода от контрактов в одном
    SQL-запросе.

    :ivar model: Модель, связанная с представлением.
    :vartype model: type[AdCampaign]
    :ivar template_name: Путь к HTML-шаблону страницы статистики.
    :vartype template_name: str
    :ivar context_object_name: Имя переменной контекста для списка объектов.
    :vartype context_object_name: str
    :ivar permission_required: Требуемое разрешение для доступа к представлению.
    :vartype permission_required: str
    :ivar cache_timeout: Время жизни кеша в секундах.
    :vartype cache_timeout: int
    """

    model = AdCampaign
    template_name = "ads/ads-statistic.html"
    context_object_name = "ads"
    permission_required = "ads.view_adcampaign"

    def get_queryset(self) -> QuerySet[AdCampaign]:
        """Возвращает queryset рекламных кампаний с аннотированной статистикой.

        Результат выполнения запроса кешируется. При повторном
        обращении данные берутся из кеша, не выполняя SQL-запрос.

        Аннотирует каждую кампанию следующими вычисляемыми полями:

        - leads_count — количество привлечённых потенциальных клиентов.
        - active_customers_count — количество лидов, ставших активными клиентами.
        - total_contract_amount — суммарный доход от контрактов активных клиентов.

        :returns: QuerySet рекламных кампаний с аннотированными полями статистики.
        :rtype: QuerySet[AdCampaign]
        """
        cache_key = "ads:statistic:queryset"
        queryset: QuerySet[AdCampaign] | None = cache.get(cache_key)

        if queryset is None:
            queryset = AdCampaign.objects.annotate(
                leads_count=Count("leads", distinct=True),
                active_customers_count=Count("leads__customer", distinct=True),
                total_contract_amount=Sum(
                    "leads__customer__contract__amount",
                    default=0,
                ),
            )
            cache.set(cache_key, queryset)

        return queryset
