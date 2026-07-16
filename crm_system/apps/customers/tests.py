import pytest

from django.urls import reverse

from .models import Customer


@pytest.mark.django_db
def test_customer_create_prefilled_lead(manager_client, lead, contract) -> None:
    response = manager_client.get(
        reverse("customers:customers-list") + f"?lead={lead.pk}",
    )
    assert response.status_code == 200
    initial = response.context["form"].initial
    assert int(initial["lead"]) == lead.pk


@pytest.mark.django_db
def test_customer_create_post(manager_client, lead, contract) -> None:
    response = manager_client.post(
        reverse("customers:customers-list"),
        data={"lead": lead.pk, "contract": contract.pk},
    )
    assert response.status_code == 302
    assert Customer.objects.filter(lead=lead).exists()


@pytest.mark.django_db
def test_customer_list_view(manager_client, customer: Customer) -> None:
    response = manager_client.get(reverse("customers:customers-list"))
    assert response.status_code == 200
    assert customer.lead.full_name.encode() in response.content


@pytest.mark.django_db
def test_customer_delete_view(manager_client, customer: Customer) -> None:
    response = manager_client.post(
        reverse("customers:customers-delete", kwargs={"pk": customer.pk}),
    )
    assert response.status_code == 302
    assert not Customer.objects.filter(pk=customer.pk).exists()
