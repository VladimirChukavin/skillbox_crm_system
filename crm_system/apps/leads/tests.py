"""Тесты для приложения «Потенциальные клиенты»."""

import pytest
from django.urls import reverse
from django.test import Client

from .models import Lead
from ..ads.models import AdCampaign


@pytest.mark.django_db
def test_lead_list_view(operator_client: Client, lead: Lead) -> None:
    """Тест отображения списка потенциальных клиентов.

    :param operator_client: Авторизованный клиент с ролью «Оператор».
    :type operator_client: django.test.Client
    :param lead: Фикстура потенциального клиента.
    :type lead: Lead
    """
    response = operator_client.get(reverse("leads:leads-list"))
    assert response.status_code == 200
    assert lead.full_name.encode() in response.content


@pytest.mark.django_db
def test_lead_create_view(operator_client: Client, ad_campaign: AdCampaign) -> None:
    """Тест создания потенциального клиента оператором через POST-запрос.

    :param operator_client: Авторизованный клиент с ролью «Оператор».
    :type operator_client: django.test.Client
    :param ad_campaign: Фикстура рекламной кампании.
    """
    response = operator_client.post(
        reverse("leads:leads-create"),
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
def test_lead_detail_view(operator_client: Client, lead: Lead) -> None:
    """Тест отображения детальной страницы потенциального клиента.

    :param operator_client: Авторизованный клиент с ролью «Оператор».
    :type operator_client: django.test.Client
    :param lead: Фикстура потенциального клиента.
    :type lead: Lead
    """
    response = operator_client.get(
        reverse("leads:leads-detail", kwargs={"pk": lead.pk}),
    )
    assert response.status_code == 200
