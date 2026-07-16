from datetime import datetime

import pytest

from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from .models import Contract


@pytest.mark.django_db
def test_contract_create_view(manager_client, product) -> None:
    response = manager_client.post(
        reverse("contracts:contracts-create"),
        data={
            "name": "Договор №100",
            "product": product.pk,
            "document": SimpleUploadedFile("doc.pdf", b"content"),
            "conclusion_date": "2025-03-01",
            "duration": 180,
            "amount": "75000.00",
        },
    )
    assert response.status_code == 302
    assert Contract.objects.filter(name="Договор №100").exists()


@pytest.mark.django_db
def test_contract_list_view(manager_client, contract: Contract) -> None:
    response = manager_client.get(reverse("contracts:contracts-list"))
    assert response.status_code == 200
    assert contract.name.encode() in response.content


@pytest.mark.django_db
def test_contract_permission_denied(operator_client) -> None:
    response = operator_client.get(reverse("contracts:contracts-list"))
    assert response.status_code == 403
