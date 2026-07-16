import pytest

from django.urls import reverse

from .models import Lead


@pytest.mark.django_db
def test_lead_list_view(operator_client, lead: Lead) -> None:
    response = operator_client.get(reverse("leads:leads-list"))
    assert response.status_code == 200
    assert lead.full_name.encode() in response.content


@pytest.mark.django_db
def test_lead_create_view(operator_client, ad_campaign) -> None:
    response = operator_client.post(
        reverse("leads:lead-create"),
        data={
            "full_name": "Василий Пупкин",
            "phone": "+79111111111",
            "email": "pupkin@test.com",
            "ad_campaign": ad_campaign.pk,
        },
    )
    assert response.status_code == 302
    assert Lead.objects.filter(full_name="Василий Пупкин").exists()


@pytest.mark.django_db
def test_lead_detail_view(operator_client, lead: Lead) -> None:
    response = operator_client.get(
        reverse("leads:leads-detail", kwargs={"pk": lead.pk}),
    )
    assert response.status_code == 200
