"""Тесты для приложения «Рекламные кампании»."""

import pytest
from django.urls import reverse
from django.test import Client

from .models import AdCampaign
from apps.customers.models import Customer
from apps.leads.models import Lead


@pytest.mark.django_db
def test_ads_list_view(admin_client: Client, ad_campaign: AdCampaign) -> None:
    """Тест отображения списка рекламных кампаний.

    :param admin_client: Авторизованный клиент суперпользователя.
    :type admin_client: django.test.Client
    :param ad_campaign: Фикстура рекламной кампании.
    :type ad_campaign: AdCampaign
    """
    response = admin_client.get(reverse("ads:ads-list"))
    assert response.status_code == 200
    assert ad_campaign.name.encode() in response.content


@pytest.mark.django_db
def test_ads_statistic_view(
    admin_client: Client,
    ad_campaign: AdCampaign,
    lead: Lead,
    customer: Customer,
) -> None:
    """Тест отображения статистики с заполненными данными.

    Проверяет корректность аннотаций: число лидов, активных клиентов
    и сумму контрактов для кампании с привязанными данными.

    :param admin_client: Авторизованный клиент суперпользователя.
    :type admin_client: django.test.Client
    :param ad_campaign: Фикстура рекламной кампании.
    :type ad_campaign: AdCampaign
    :param lead: Фикстура потенциального клиента.
    :type lead: Lead
    :param customer: Фикстура активного клиента.
    :type customer: Customer
    """
    response = admin_client.get(reverse("ads:ads-statistic"))
    assert response.status_code == 200
    qs = response.context["ads"]
    item = qs.get(pk=ad_campaign.pk)
    assert item.leads_count == 1
    assert item.active_customers_count == 1
    assert item.total_contract_amount == 150000


@pytest.mark.django_db
def test_ads_statistic_empty_campaign(
    admin_client: Client, ad_campaign: AdCampaign
) -> None:
    """Тест статистики для кампании без лидов и клиентов.

    Проверяет, что аннотированные поля принимают значения по умолчанию (0).

    :param admin_client: Авторизованный клиент суперпользователя.
    :type admin_client: django.test.Client
    :param ad_campaign: Фикстура рекламной кампании.
    :type ad_campaign: AdCampaign
    """
    response = admin_client.get(reverse("ads:ads-statistic"))
    qs = response.context["ads"]
    item = qs.get(pk=ad_campaign.pk)
    assert item.leads_count == 0
    assert item.active_customers_count == 0
    assert item.total_contract_amount == 0


@pytest.mark.django_db
def test_ads_create_permission_denied(operator_client: Client) -> None:
    """Тест запрета доступа к созданию кампании для оператора.

    :param operator_client: Авторизованный клиент с ролью «Оператор».
    :type operator_client: django.test.Client
    """
    response = operator_client.get(reverse("ads:ads-create"))
    assert response.status_code == 403
