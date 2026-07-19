"""Тесты для приложения «Услуги»."""

import pytest
from django.urls import reverse
from django.test import Client

from .models import Product


@pytest.mark.django_db
def test_product_list_view(admin_client: Client) -> None:
    """Тест отображения списка услуг.

    :param admin_client: Авторизованный клиент суперпользователя.
    :type admin_client: django.test.Client
    """
    Product.objects.create(name="Test", price="100.00")
    response = admin_client.get(reverse("products:products-list"))
    assert response.status_code == 200
    assert b"Test" in response.content


@pytest.mark.django_db
def test_product_create_view(admin_client: Client) -> None:
    """Тест создания услуги администратором через POST-запрос.

    :param admin_client: Авторизованный клиент суперпользователя.
    :type admin_client: django.test.Client
    """
    response = admin_client.post(
        reverse("products:products-create"),
        data={
            "name": "New service",
            "description": "New service description",
            "price": "999.00",
        },
    )
    assert response.status_code == 302
    assert Product.objects.filter(name="New service").exists()


@pytest.mark.django_db
def test_product_detail_view(admin_client: Client, product: Product) -> None:
    """Тест отображения детальной страницы услуги.

    :param admin_client: Авторизованный клиент суперпользователя.
    :type admin_client: django.test.Client
    :param product: Фикстура услуги.
    :type product: Product
    """
    response = admin_client.get(
        reverse("products:products-detail", kwargs={"pk": product.pk}),
    )
    assert response.status_code == 200
    assert product.name.encode() in response.content


@pytest.mark.django_db
def test_product_delete_view(admin_client: Client, product: Product) -> None:
    """Тест удаления услуги администратором через POST-запрос.

    :param admin_client: Авторизованный клиент суперпользователя.
    :type admin_client: django.test.Client
    :param product: Фикстура услуги.
    :type product: Product
    """
    response = admin_client.post(
        reverse("products:products-delete", kwargs={"pk": product.pk}),
    )
    assert response.status_code == 302
    assert not Product.objects.filter(pk=product.pk).exists()


@pytest.mark.django_db
def test_product_list_permission_denied(operator_client: Client) -> None:
    """Тест запрета доступа к списку услуг для оператора.

    :param operator_client: Авторизованный клиент с ролью «Оператор».
    :type operator_client: django.test.Client
    """
    response = operator_client.get(reverse("products:products-list"))
    assert response.status_code == 403
