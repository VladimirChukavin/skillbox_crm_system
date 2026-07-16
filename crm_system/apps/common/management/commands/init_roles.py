from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

ROLE_PERMISSIONS = {
    "Оператор": [
        "leads.view_lead",
        "leads.add_lead",
        "leads.change_lead",
        "ads.view_adcampaign",
    ],
    "Маркетолог": [
        "products.view_product",
        "products.add_product",
        "products.change_product",
        "ads.view_adcampaign",
        "ads.add_adcampaign",
        "ads.change_adcampaign",
    ],
    "Менеджер": [
        "contracts.view_contract",
        "contracts.add_contract",
        "contracts.change_contract",
        "leads.view_lead",
        "customers.view_customer",
        "customers.add_customer",
        "customers.change_customer",
        "ads.view_adcampaign",
    ],
}


class Command(BaseCommand):
    help = "Создает преднастроенные роли пользователей"

    def handle(self, *args, **options):
        for role_name, perm_codenames in ROLE_PERMISSIONS.items():
            group, _created = Group.objects.get_or_create(name=role_name)
            group.permissions.clear()
            for perm_str in perm_codenames:
                app_label, codename = perm_str.split(".", 1)
                perm = Permission.objects.filter(
                    content_type__app_label=app_label,
                    codename=codename,
                ).first()

                if perm:
                    group.permissions.add(perm)
                else:
                    self.stdout.write(
                        self.style.WARNING(f"Не найдено разрешение {perm_str}")
                    )

            self.stdout.write(
                self.style.SUCCESS(
                    f"Роль {role_name} - {group.permissions.count()} разрешений"
                ),
            )
