"""Представление для создания активного клиента."""

from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.customers.models import Customer
from apps.leads.models import Lead


class CustomerCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Представление для создания нового активного клиента из потенциального.

    Поле lead предзаполняется из GET-параметра запроса.

    :ivar model: Модель, связанная с представлением.
    :vartype model: type[Customer]
    :ivar fields: Список полей формы, доступных для заполнения.
    :vartype fields: list[str]
    :ivar template_name: Путь к HTML-шаблону страницы создания.
    :vartype template_name: str
    :ivar success_url: URL для перенаправления после успешного создания.
    :vartype success_url: str
    :ivar permission_required: Требуемое разрешение для доступа к представлению.
    :vartype permission_required: str
    """

    model = Customer
    fields = ["lead", "contract"]
    template_name = "customers/customers-create.html"
    success_url = reverse_lazy("customers:customers-list")
    permission_required = "customers.add_customer"

    def get_form(self, form_class: type[Any] | None = None) -> Any:
        """Возвращает экземпляр формы с отфильтрованным queryset для поля lead.

        В список выбора попадают только лиды, у которых ещё нет связи
        с активным клиентом (customer__isnull=True).

        :returns: Экземпляр формы.
        :rtype: forms.Form
        """
        form = super().get_form()
        form.fields["lead"].queryset = Lead.objects.filter(customer__isnull=True)
        return form

    def get_initial(self) -> dict[str, Any]:
        """Возвращает словарь начальных значений для формы.

        Предзаполняет поле lead значением из GET-параметра lead,
        переданного в URL (например, ?lead=5).

        :returns: Словарь с начальными значениями полей формы.
        :rtype: dict[str, Any]
        """
        initial = super().get_initial()
        lead_pk = self.request.GET.get("lead")

        if lead_pk:
            initial["lead"] = lead_pk

        return initial
