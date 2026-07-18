"""Представление для отображения списка рекламных кампаний."""

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView

from apps.ads.models import AdCampaign


class AdCampaignListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Представление для отображения списка всех рекламных кампаний.

    :ivar model: Модель, связанная с представлением.
    :vartype model: type[AdCampaign]
    :ivar template_name: Путь к HTML-шаблону страницы списка.
    :vartype template_name: str
    :ivar context_object_name: Имя переменной контекста для списка объектов.
    :vartype context_object_name: str
    :ivar permission_required: Требуемое разрешение для доступа к представлению.
    :vartype permission_required: str
    """

    model = AdCampaign
    template_name = "ads/ads-list.html"
    context_object_name = "ads"
    permission_required = "ads.view_adcampaign"
