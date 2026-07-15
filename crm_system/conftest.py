from collections.abc import Generator
from typing import Any

import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.test import Client

from apps.ads.models import AdCampaign
from apps.contracts.models import Contract
from apps.customers.models import Customer
from apps.leads.models import Lead
from apps.products.models import Product

User = get_user_model()


@pytest.fixture
def admin_user(db: Any) -> User:
    return User.objects.create_superuser(
        username="admin",
        password="admin123",
        email="admin@test.com",
    )


@pytest.fixture
def admin_client(client: Client, admin_user: User) -> Client:
    client.force_login(admin_user)
    return client


@pytest.fixture
def operator_group(db: Any) -> Group:
    group = Group.objects.create(name="Оператор")
    group.permissions.add(
        *Permission.objects.filter(
            codename__in=["view_lead", "add_lead", "change_lead"]
        ),
    )
    return group


@pytest.fixture
def marketer_group(db: Any) -> Group:
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
def operator(db: Any, operator_group: Group) -> User:
    user = User.objects.create_user(
        username="operator", password="op123", email="op@test.com"
    )
    user.groups.add(operator_group)
    return user


@pytest.fixture
def operator_client(client: Client, operator: User) -> Client:
    client.force_login(operator)
    return client


@pytest.fixture
def manager_client(client: Client, manager_group: Group) -> Client:
    user = User.objects.create_user(
        username="manager", password="mgr123", email="mgr@test.com"
    )
    user.groups.add(manager_group)
    client.force_login(user)
    return client


@pytest.fixture
def product(db: Any) -> Product:
    return Product.objects.create(
        name="SEO-продвижение",
        description="Поисковая оптимизация",
        price="50000.00",
    )


@pytest.fixture
def ad_campaign(db: Any, product: Product) -> AdCampaign:
    return AdCampaign.objects.create(
        name="Яндекс.Директ",
        product=product,
        channel="Контекстная реклама",
        budget="100000.00",
    )


@pytest.fixture
def lead(db: Any, ad_campaign: AdCampaign) -> Lead:
    return Lead.objects.create(
        full_name="Иван Иванов",
        phone="+79991234567",
        email="ivan@test.com",
        ad_campaign=ad_campaign,
    )


@pytest.fixture
def contract(db: Any, product: Product) -> Contract:
    from datetime import date
    from django.core.files.uploadedfile import SimpleUploadedFile

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
    return Customer.objects.create(lead=lead, contract=contract)
