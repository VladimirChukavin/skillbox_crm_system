from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView

from apps.ads.models import AdCampaign


class AdCampaignListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = AdCampaign
    template_name = "ads/ads-list.html"
    context_object_name = "ads"
    permission_required = "ads.view_adcampaign"
