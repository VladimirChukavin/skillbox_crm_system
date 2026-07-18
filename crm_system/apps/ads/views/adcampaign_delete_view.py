"""Представление для удаления рекламной кампании."""

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from apps.ads.models import AdCampaign


class AdCampaignDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Представление для удаления существующей рекламной кампании.

    :ivar model: Модель, связанная с представлением.
    :vartype model: type[AdCampaign]
    :ivar template_name: Путь к HTML-шаблону страницы подтверждения удаления.
    :vartype template_name: str
    :ivar success_url: URL для перенаправления после успешного удаления.
    :vartype success_url: str
    :ivar permission_required: Требуемое разрешение для доступа к представлению.
    :vartype permission_required: str
    """

    model = AdCampaign
    template_name = "ads/ads-delete.html"
    success_url = reverse_lazy("ads:ads-list")
    permission_required = "ads.delete_adcampaign"
