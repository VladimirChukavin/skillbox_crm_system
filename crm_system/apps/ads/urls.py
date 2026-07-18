"""URL-маршруты для приложения «Рекламные кампании»."""

from django.urls import path

from .views import (
    AdCampaignListView,
    AdCampaignCreateView,
    AdCampaignDetailView,
    AdCampaignUpdateView,
    AdCampaignDeleteView,
    AdCampaignStatisticView,
)

app_name = "ads"

urlpatterns = [
    path("", AdCampaignListView.as_view(), name="ads-list"),
    path("create/", AdCampaignCreateView.as_view(), name="ads-create"),
    path("statistic/", AdCampaignStatisticView.as_view(), name="ads-statistic"),
    path("<int:pk>/", AdCampaignDetailView.as_view(), name="ads-detail"),
    path("<int:pk>/edit/", AdCampaignUpdateView.as_view(), name="ads-edit"),
    path("<int:pk>/delete/", AdCampaignDeleteView.as_view(), name="ads-delete"),
]
