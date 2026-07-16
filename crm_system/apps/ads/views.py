from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Count, QuerySet, Sum
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import AdCampaign


class AdCampaignListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = AdCampaign
    template_name = "ads/ads-list.html"
    context_object_name = "ads"
    permission_required = "ads.view_adcampaign"


class AdCampaignCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = AdCampaign
    fields = ["name", "product", "channel", "budget"]
    template_name = "ads/ads-create.html"
    success_url = reverse_lazy("ads:ads-list")
    permission_required = "ads.add_adcampaign"


class AdCampaignDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = AdCampaign
    template_name = "ads/ads-detail.html"
    permission_required = "ads.view_adcampaign"


class AdCampaignUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = AdCampaign
    fields = ["name", "product", "channel", "budget"]
    template_name = "ads/ads-edit.html"
    success_url = reverse_lazy("ads:ads-list")
    permission_required = "ads.change_adcampaign"


class AdCampaignDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = AdCampaign
    template_name = "ads/ads-delete.html"
    success_url = reverse_lazy("ads:ads-list")
    permission_required = "ads.delete_adcampaign"


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
