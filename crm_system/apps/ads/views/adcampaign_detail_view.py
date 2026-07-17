from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import DetailView

from apps.ads.models import AdCampaign


class AdCampaignDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = AdCampaign
    template_name = "ads/ads-detail.html"
    permission_required = "ads.view_adcampaign"
