"""Тесты для приложения «Контракты»."""

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.test import Client

from .models import Contract
from ..products.models import Product


@pytest.mark.django_db
def test_contract_create_view(manager_client: Client, product: Product) -> None:
    """Тест создания контракта менеджером через POST-запрос.

    :param manager_client: Авторизованный клиент с ролью «Менеджер».
    :type manager_client: django.test.Client
    :param product: Фикстура услуги.
    :type product: apps.products.models.Product
    """
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
def test_contract_list_view(manager_client: Client, contract: Contract) -> None:
    """Тест отображения списка контрактов.

    :param manager_client: Авторизованный клиент с ролью «Менеджер».
    :type manager_client: django.test.Client
    :param contract: Фикстура контракта.
    :type contract: Contract
    """
    response = manager_client.get(reverse("contracts:contracts-list"))
    assert response.status_code == 200
    assert contract.name.encode() in response.content


@pytest.mark.django_db
def test_contract_permission_denied(operator_client: Client) -> None:
    """Тест запрета доступа к списку контрактов для оператора.

    :param operator_client: Авторизованный клиент с ролью «Оператор».
    :type operator_client: django.test.Client
    """
    response = operator_client.get(reverse("contracts:contracts-list"))
    assert response.status_code == 403
