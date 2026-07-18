"""Management-команда для заполнения базы данных моковыми данными."""

from datetime import date, timedelta
from typing import Any

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from apps.ads.models import AdCampaign
from apps.contracts.models import Contract
from apps.customers.models import Customer
from apps.leads.models import Lead
from apps.products.models import Product

PRODUCTS_DATA: list[dict[str, str]] = [
    {
        "name": "SEO-продвижение",
        "description": "Комплексная поисковая оптимизация сайта",
        "price": "500000.00",
    },
    {
        "name": "Контекстная реклама",
        "description": "Настройка и ведение Яндекс.Директ",
        "price": "350000.00",
    },
    {
        "name": "SMM-продвижение",
        "description": "Ведение социальных сетей компании",
        "price": "400000.00",
    },
]

ADS_DATA: list[dict[str, Any]] = [
    {
        "name": "Яндекс.Директ - SEO",
        "product_index": 0,
        "channel": "Яндекс.Директ",
        "budget": "1000000.00",
    },
    {
        "name": "ВКонтакте - SMM",
        "product_index": 2,
        "channel": "ВКонтакте",
        "budget": "600000.00",
    },
    {
        "name": "Google Ads - Контекст",
        "product_index": 1,
        "channel": "Google Ads",
        "budget": "800000.00",
    },
    {
        "name": "Telegram-канал - SEO",
        "product_index": 0,
        "channel": "Telegram",
        "budget": "450000.00",
    },
]

LEADS_DATA: list[dict[str, Any]] = [
    {
        "full_name": "Иванов Иван Иванович",
        "phone": "+79990000001",
        "email": "ivanov@example.com",
        "ad_index": 0,
    },
    {
        "full_name": "Петров Пётр Петрович",
        "phone": "+79990000002",
        "email": "petrov@example.com",
        "ad_index": 0,
    },
    {
        "full_name": "Сидорова Анна Сергеевна",
        "phone": "+79990000003",
        "email": "sidorova@example.com",
        "ad_index": 1,
    },
    {
        "full_name": "Кузнецов Дмитрий Алексеевич",
        "phone": "+79990000004",
        "email": "kuznetsov@example.com",
        "ad_index": 1,
    },
    {
        "full_name": "Смирнова Елена Владимировна",
        "phone": "+79990000005",
        "email": "smirnova@example.com",
        "ad_index": 2,
    },
    {
        "full_name": "Попов Сергей Николаевич",
        "phone": "+79990000006",
        "email": "popov@example.com",
        "ad_index": 2,
    },
    {
        "full_name": "Волкова Ольга Андреевна",
        "phone": "+79990000007",
        "email": "volkova@example.com",
        "ad_index": 3,
    },
    {
        "full_name": "Морозов Артём Игоревич",
        "phone": "+79990000008",
        "email": "morozov@example.com",
        "ad_index": 0,
    },
    {
        "full_name": "Новикова Мария Дмитриевна",
        "phone": "+79990000009",
        "email": "novikova@example.com",
        "ad_index": 1,
    },
    {
        "full_name": "Фёдоров Алексей Романович",
        "phone": "+79990000010",
        "email": "fedorov@example.com",
        "ad_index": 2,
    },
]

CONTRACTS_DATA: list[dict[str, Any]] = [
    {
        "name": "Договор №001",
        "product_index": 0,
        "duration": 365,
        "amount": "1500000.00",
        "days_ago": 30,
    },
    {
        "name": "Договор №002",
        "product_index": 1,
        "duration": 180,
        "amount": "700000.00",
        "days_ago": 20,
    },
    {
        "name": "Договор №003",
        "product_index": 2,
        "duration": 365,
        "amount": "1200000.00",
        "days_ago": 15,
    },
    {
        "name": "Договор №004",
        "product_index": 0,
        "duration": 90,
        "amount": "500000.00",
        "days_ago": 10,
    },
    {
        "name": "Договор №005",
        "product_index": 1,
        "duration": 365,
        "amount": "950000.00",
        "days_ago": 5,
    },
]

CUSTOMER_LEAD_INDICES: list[int] = [0, 2, 4, 6, 8]
CUSTOMER_CONTRACT_INDICES: list[int] = [0, 1, 2, 3, 4]


class Command(BaseCommand):
    """Команда для заполнения базы данных моковыми данными.

    Создает 3 услуги, 4 рекламные кампании, 10 потенциальных клиентов,
    5 контрактов и 5 активных клиентов. Команда идемпотентна —
    повторный запуск не создает дубликаты.

    :ivar help: Текст справки, отображаемый при вызове python manage.py help.
    :vartype help: str
    """

    help = (
        "Заполняет БД моковыми данными: "
        "3 услуги, 4 РК, 10 лидов, 5 контрактов, 5 клиентов"
    )

    def _log_created(self, created: bool, label: str) -> None:
        """Выводит в консоль информацию о созданном или существующем объекте.

        :param created: Флаг, указывающий был ли объект создан.
        :type created: bool
        :param label: Читаемое название объекта для вывода.
        :type label: str
        """
        if created:
            self.stdout.write(f" ✓ Создано: {label}")
        else:
            self.stdout.write(f" → Уже существует: {label}")

    def handle(self, *args: Any, **kwargs: Any) -> None:
        """Обработчик команды.

        Последовательно создает объекты: услуги, рекламные кампании,
        лидов, контракты и активных клиентов. Для каждого объекта
        используется get_or_create для предотвращения дубликатов.

        :param args: Позиционные аргументы командной строки.
        :param options: Именованные аргументы командной строки.
        """
        self.stdout.write("Начало заполнения БД моковыми данными...")

        # ----------- Услуги ------------------
        products: list[Product] = []

        for item in PRODUCTS_DATA:
            product, created = Product.objects.get_or_create(
                name=item["name"],
                defaults={
                    "description": item["description"],
                    "price": item["price"],
                },
            )
            products.append(product)
            self._log_created(created, f"Услуга: {product.name}")

        # ----------- Рекламные кампании ------------------
        ads: list[AdCampaign] = []

        for item in ADS_DATA:
            ad, created = AdCampaign.objects.get_or_create(
                name=item["name"],
                defaults={
                    "product": products[item["product_index"]],
                    "channel": item["channel"],
                    "budget": item["budget"],
                },
            )
            ads.append(ad)
            self._log_created(created, f"Рекламная кампания: {ad.name}")

        # ----------- Потенциальные клиенты ------------------
        leads: list[Lead] = []

        for item in LEADS_DATA:
            lead, created = Lead.objects.get_or_create(
                full_name=item["full_name"],
                defaults={
                    "phone": item["phone"],
                    "email": item["email"],
                    "ad_campaign": ads[item["ad_index"]],
                },
            )
            leads.append(lead)
            self._log_created(created, f"Лид: {lead.full_name}")

        # ----------- Контракты ------------------
        contracts: list[Contract] = []

        for item in CONTRACTS_DATA:
            contract, created = Contract.objects.get_or_create(
                name=item["name"],
                defaults={
                    "product": products[item["product_index"]],
                    "conclusion_date": date.today() - timedelta(days=item["days_ago"]),
                    "duration": item["duration"],
                    "amount": item["amount"],
                },
            )

            if not contract.document:
                fake_pdf = ContentFile(
                    b"%PDF-1.4 mock document content",
                    name=f'{item["name"]}.pdf',
                )
                contract.document.save(
                    f'{item["name"]}.pdf',
                    fake_pdf,
                    save=True,
                )

            contracts.append(contract)
            self._log_created(created, f"Контракт: {contract.name}")

        # ----------- Активные клиенты ------------------
        for lead_idx, contract_idx in zip(
            CUSTOMER_LEAD_INDICES, CUSTOMER_CONTRACT_INDICES
        ):
            lead = leads[lead_idx]
            contract = contracts[contract_idx]
            customer, created = Customer.objects.get_or_create(
                lead=lead,
                defaults={
                    "contract": contract,
                },
            )
            self._log_created(created, f"Активный клиент: {customer.lead.full_name}")

        # ----------- Вывод ------------------
        self.stdout.write(
            self.style.SUCCESS(
                f"\nГотово!\n"
                f" Услуг: {Product.objects.count()}\n"
                f" Рекламных кампаний: {AdCampaign.objects.count()}\n"
                f" Потенциальных клиентов: {Lead.objects.count()}\n"
                f" Контрактов: {Contract.objects.count()}\n"
                f" Активных клиентов: {Customer.objects.count()}"
            )
        )
