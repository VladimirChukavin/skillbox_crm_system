from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from apps.ads.models import AdCampaign


class AdCampaignUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = AdCampaign
    fields = ["name", "product", "channel", "budget"]
    template_name = "ads/ads-edit.html"
    success_url = reverse_lazy("ads:ads-list")
    permission_required = "ads.change_adcampaign"
