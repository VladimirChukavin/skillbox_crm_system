"""Общие фикстуры pytest для всех приложений CRM-системы."""

from datetime import date
from typing import Any

import pytest
from django.contrib.auth.models import Group, Permission, User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client

from apps.ads.models import AdCampaign
from apps.contracts.models import Contract
from apps.customers.models import Customer
from apps.leads.models import Lead
from apps.products.models import Product


@pytest.fixture
def admin_user(db: Any) -> User:
    """Создаёт суперпользователя для тестов.

    :param db: Маркер доступа к базе данных pytest-django.
    :returns: Объект суперпользователя.
    :rtype: User
    """
    return User.objects.create_superuser(
        username="admin",
        password="admin123",
        email="admin@test.com",
    )


@pytest.fixture
def admin_client(client: Client, admin_user: User) -> Client:
    """Возвращает авторизованный клиент суперпользователя.

    :param client: Базовый тестовый клиент Django.
    :type client: Client
    :param admin_user: Фикстура суперпользователя.
    :type admin_user: User
    :returns: Авторизованный тестовый клиент.
    :rtype: Client
    """
    client.force_login(admin_user)
    return client


@pytest.fixture
def operator_group(db: Any) -> Group:
    """Создаёт группу «Оператор» с разрешениями на работу с лидами.

    :param db: Маркер доступа к базе данных pytest-django.
    :returns: Объект группы «Оператор».
    :rtype: Group
    """
    group = Group.objects.create(name="Оператор")
    group.permissions.add(
        *Permission.objects.filter(
            codename__in=["view_lead", "add_lead", "change_lead"]
        ),
    )
    return group


@pytest.fixture
def marketer_group(db: Any) -> Group:
    """Создаёт группу «Маркетолог» с разрешениями на работу с услугами и РК.

    :param db: Маркер доступа к базе данных pytest-django.
    :returns: Объект группы «Маркетолог».
    :rtype: Group
    """
    group = Group.objects.create(name="Маркетолог")
    group.permissions.add(
        *Permission.objects.filter(
            codename__in=[
                "view_product",
                "add_product",
                "change_product",
                "view_adcampaign",
                "add_adcampaign",
                "change_adcampaign",
            ]
        ),
    )
    return group


@pytest.fixture
def manager_group(db: Any) -> Group:
    """Создаёт группу «Менеджер» с разрешениями на работу с контрактами и клиентами.

    :param db: Маркер доступа к базе данных pytest-django.
    :returns: Объект группы «Менеджер».
    :rtype: Group
    """
    group = Group.objects.create(name="Менеджер")
    group.permissions.add(
        *Permission.objects.filter(
            codename__in=[
                "view_contract",
                "add_contract",
                "change_contract",
                "view_lead",
                "view_customer",
                "add_customer",
                "change_customer",
            ]
        ),
    )
    return group


@pytest.fixture
def operator_client(client: Client, operator_group: Group) -> Client:
    """Создаёт и возвращает авторизованный клиент пользователя с ролью «Оператор».

    :param client: Базовый тестовый клиент Django.
    :type client: Client
    :param operator_group: Фикстура группы «Оператор».
    :type operator_group: Group
    :returns: Авторизованный тестовый клиент.
    :rtype: Client
    """
    user = User.objects.create_user(
        username="operator", password="op123", email="op@test.com"
    )
    user.groups.add(operator_group)
    client.force_login(user)
    return client


@pytest.fixture
def manager_client(client: Client, manager_group: Group) -> Client:
    """Создаёт и возвращает авторизованный клиент пользователя с ролью «Менеджер».

    :param client: Базовый тестовый клиент Django.
    :type client: Client
    :param manager_group: Фикстура группы «Менеджер».
    :type manager_group: Group
    :returns: Авторизованный тестовый клиент.
    :rtype: Client
    """
    user = User.objects.create_user(
        username="manager", password="mgr123", email="mgr@test.com"
    )
    user.groups.add(manager_group)
    client.force_login(user)
    return client


@pytest.fixture
def product(db: Any) -> Product:
    """Создаёт услугу для тестов.

    :param db: Маркер доступа к базе данных pytest-django.
    :returns: Объект услуги.
    :rtype: Product
    """
    return Product.objects.create(
        name="SEO-продвижение",
        description="Поисковая оптимизация",
        price="50000.00",
    )


@pytest.fixture
def ad_campaign(db: Any, product: Product) -> AdCampaign:
    """Создаёт рекламную кампанию для тестов.

    :param db: Маркер доступа к базе данных pytest-django.
    :param product: Фикстура услуги.
    :type product: Product
    :returns: Объект рекламной кампании.
    :rtype: AdCampaign
    """
    return AdCampaign.objects.create(
        name="Яндекс.Директ",
        product=product,
        channel="Контекстная реклама",
        budget="100000.00",
    )


@pytest.fixture
def lead(db: Any, ad_campaign: AdCampaign) -> Lead:
    """Создаёт потенциального клиента для тестов.

    :param db: Маркер доступа к базе данных pytest-django.
    :param ad_campaign: Фикстура рекламной кампании.
    :type ad_campaign: AdCampaign
    :returns: Объект потенциального клиента.
    :rtype: Lead
    """
    return Lead.objects.create(
        full_name="Иван Иванов",
        phone="+79991234567",
        email="ivan@test.com",
        ad_campaign=ad_campaign,
    )


@pytest.fixture
def contract(db: Any, product: Product) -> Contract:
    """Создаёт контракт для тестов.

    :param db: Маркер доступа к базе данных pytest-django.
    :param product: Фикстура услуги.
    :type product: Product
    :returns: Объект контракта.
    :rtype: Contract
    """
    return Contract.objects.create(
        name="Договор №001",
        product=product,
        document=SimpleUploadedFile("test.pdf", b"file content"),
        conclusion_date=date(2025, 1, 15),
        duration=365,
        amount="150000.00",
    )


@pytest.fixture
def customer(db: Any, lead: Lead, contract: Contract) -> Customer:
    """Создаёт активного клиента для тестов.

    :param db: Маркер доступа к базе данных pytest-django.
    :param lead: Фикстура потенциального клиента.
    :type lead: Lead
    :param contract: Фикстура контракта.
    :type contract: Contract
    :returns: Объект активного клиента.
    :rtype: Customer
    """
    return Customer.objects.create(lead=lead, contract=contract)
