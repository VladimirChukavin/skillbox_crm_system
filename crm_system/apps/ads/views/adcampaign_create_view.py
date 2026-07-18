"""Представление для создания рекламной кампании."""

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.ads.models import AdCampaign


class AdCampaignCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Представление для создания новой рекламной кампании.

    :ivar model: Модель, связанная с представлением.
    :vartype model: type[AdCampaign]
    :ivar fields: Список полей формы, доступных для заполнения.
    :vartype fields: list[str]
    :ivar template_name: Путь к HTML-шаблону страницы создания.
    :vartype template_name: str
    :ivar success_url: URL для перенаправления после успешного создания.
    :vartype success_url: str
    :ivar permission_required: Требуемое разрешение для доступа к представлению.
    :vartype permission_required: str
    """

    model = AdCampaign
    fields = ["name", "product", "channel", "budget"]
    template_name = "ads/ads-create.html"
    success_url = reverse_lazy("ads:ads-list")
    permission_required = "ads.add_adcampaign"
