from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from apps.ads.models import AdCampaign


class AdCampaignDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = AdCampaign
    template_name = "ads/ads-delete.html"
    success_url = reverse_lazy("ads:ads-list")
    permission_required = "ads.delete_adcampaign"
