"""Представление для отображения детальной информации о рекламной кампании."""

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import DetailView

from apps.ads.models import AdCampaign


class AdCampaignDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Представление для отображения детальной информации о рекламной кампании.

    :ivar model: Модель, связанная с представлением.
    :vartype model: type[AdCampaign]
    :ivar template_name: Путь к HTML-шаблону детальной страницы.
    :vartype template_name: str
    :ivar permission_required: Требуемое разрешение для доступа к представлению.
    :vartype permission_required: str
    """

    model = AdCampaign
    template_name = "ads/ads-detail.html"
    permission_required = "ads.view_adcampaign"
