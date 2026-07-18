"""Представление для редактирования рекламной кампании."""

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from apps.ads.models import AdCampaign


class AdCampaignUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Представление для редактирования существующей рекламной кампании.

    :ivar model: Модель, связанная с представлением.
    :vartype model: AdCampaign
    :ivar fields: Список полей формы, доступных для редактирования.
    :vartype fields: list[str]
    :ivar template_name: Путь к HTML-шаблону страницы редактирования.
    :vartype template_name: str
    :ivar success_url: URL для перенаправления после успешного обновления.
    :vartype success_url: str
    :ivar permission_required: Требуемое разрешение для доступа к представлению.
    :vartype permission_required: str
    """

    model = AdCampaign
    fields = ["name", "product", "channel", "budget"]
    template_name = "ads/ads-edit.html"
    success_url = reverse_lazy("ads:ads-list")
    permission_required = "ads.change_adcampaign"
