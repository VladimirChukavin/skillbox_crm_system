import pytest

from django.urls import reverse

from .models import AdCampaign


@pytest.mark.django_db
def test_ads_list_view(admin_client, ad_campaign: AdCampaign) -> None:
    response = admin_client.get(reverse("ads:ads-list"))
    assert response.status_code == 200
    assert ad_campaign.name.encode() in response.content


@pytest.mark.django_db
def test_ads_statistic_view(admin_client, ad_campaign, lead, customer) -> None:
    response = admin_client.get(reverse("ads:ads-statistic"))
    assert response.status_code == 200
    qs = response.context["ads"]
    item = qs.get(pk=ad_campaign.pk)
    assert item.leads_count == 1
    assert item.active_customer_count == 1
    assert item.total_contract_amount == 150000


@pytest.mark.django_db
def test_ads_statistic_empty_campaign(admin_client, ad_campaign) -> None:
    response = admin_client.get(reverse("ads:ads-statistic"))
    qs = response.context["ads"]
    item = qs.get(pk=ad_campaign.pk)
    assert item.leads_count == 0
    assert item.active_customer_count == 0
    assert item.total_contract_amount == 0


@pytest.mark.django_db
def test_ads_create_permission_denied(operator_client) -> None:
    response = operator_client.get(reverse("ads:ads-create"))
    assert response.status_code == 403
