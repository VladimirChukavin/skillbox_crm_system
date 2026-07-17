from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Count, Sum
from django.views.generic import ListView

from apps.ads.models import AdCampaign


class AdCampaignStatisticView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = AdCampaign
    template_name = "ads/ads-statistic.html"
    context_object_name = "ads"
    permission_required = "ads.view_adcampaign"

    def get_queryset(self):
        return AdCampaign.objects.annotate(
            leads_count=Count("leads", distinct=True),
            active_customers_count=Count("leads__customer", distinct=True),
            total_contract_amount=Sum(
                "leads__customer__contract__amount",
                default=0,
            ),
        )
