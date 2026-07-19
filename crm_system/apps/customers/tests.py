"""Тесты для приложения «Активные клиенты»."""

import pytest
from django.urls import reverse
from django.test import Client

from .models import Customer
from ..leads.models import Lead
from ..contracts.models import Contract


@pytest.mark.django_db
def test_customer_create_prefilled_lead(manager_client: Client, lead: Lead) -> None:
    """Тест предзаполнения поля лида в форме создания активного клиента.

    Проверяет, что GET-параметр lead корректно подставляется
    в начальные значения формы.

    :param manager_client: Авторизованный клиент с ролью «Менеджер».
    :type manager_client: django.test.Client
    :param lead: Фикстура потенциального клиента.
    :param contract: Фикстура контракта.
    """
    response = manager_client.get(
        reverse("customers:customers-create") + f"?lead={lead.pk}",
    )
    assert response.status_code == 200
    initial = response.context["form"].initial
    assert int(initial["lead"]) == lead.pk


@pytest.mark.django_db
def test_customer_create_post(
    manager_client: Client, lead: Lead, contract: Contract
) -> None:
    """Тест создания активного клиента менеджером через POST-запрос.

    :param manager_client: Авторизованный клиент с ролью «Менеджер».
    :type manager_client: django.test.Client
    :param lead: Фикстура потенциального клиента.
    :param contract: Фикстура контракта.
    """
    response = manager_client.post(
        reverse("customers:customers-create"),
        data={"lead": lead.pk, "contract": contract.pk},
    )
    assert response.status_code == 302
    assert Customer.objects.filter(lead=lead).exists()


@pytest.mark.django_db
def test_customer_list_view(manager_client: Client, customer: Customer) -> None:
    """Тест отображения списка активных клиентов.

    :param manager_client: Авторизованный клиент с ролью «Менеджер».
    :type manager_client: django.test.Client
    :param customer: Фикстура активного клиента.
    :type customer: Customer
    """
    response = manager_client.get(reverse("customers:customers-list"))
    assert response.status_code == 200
    assert customer.lead.full_name.encode() in response.content


@pytest.mark.django_db
def test_customer_delete_view(manager_client: Client, customer: Customer) -> None:
    """Тест удаления активного клиента.

    :param manager_client: Авторизованный клиент с ролью «Менеджер».
    :type manager_client: django.test.Client
    :param customer: Фикстура активного клиента.
    :type customer: Customer
    """
    response = manager_client.post(
        reverse("customers:customers-delete", kwargs={"pk": customer.pk}),
    )
    assert response.status_code == 302
    assert not Customer.objects.filter(pk=customer.pk).exists()
