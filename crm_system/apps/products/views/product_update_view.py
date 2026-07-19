"""Представление для редактирования услуги."""

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from apps.products.models import Product


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Представление для редактирования существующей услуги.

    :ivar model: Модель, связанная с представлением.
    :vartype model: type[Product]
    :ivar fields: Список полей формы, доступных для редактирования.
    :vartype fields: list[str]
    :ivar template_name: Путь к HTML-шаблону страницы редактирования.
    :vartype template_name: str
    :ivar success_url: URL для перенаправления после успешного обновления.
    :vartype success_url: str
    :ivar permission_required: Требуемое разрешение для доступа к представлению.
    :vartype permission_required: str
    """

    model = Product
    fields = ["name", "description", "price"]
    template_name = "products/products-edit.html"
    success_url = reverse_lazy("products:products-list")
    permission_required = "products.change_product"
