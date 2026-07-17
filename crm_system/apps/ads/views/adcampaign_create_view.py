from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.ads.models import AdCampaign


class AdCampaignCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = AdCampaign
    fields = ["name", "product", "channel", "budget"]
    template_name = "ads/ads-create.html"
    success_url = reverse_lazy("ads:ads-list")
    permission_required = "ads.add_adcampaign"
