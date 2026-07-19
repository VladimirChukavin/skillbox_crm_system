"""Представление для отображения списка услуг."""

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView

from apps.products.models import Product


class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Представление для отображения списка всех услуг.

    :ivar model: Модель, связанная с представлением.
    :vartype model: type[Product]
    :ivar template_name: Путь к HTML-шаблону страницы списка.
    :vartype template_name: str
    :ivar context_object_name: Имя переменной контекста для списка объектов.
    :vartype context_object_name: str
    :ivar permission_required: Требуемое разрешение для доступа к представлению.
    :vartype permission_required: str
    """

    model = Product
    template_name = "products/products-list.html"
    context_object_name = "products"
    permission_required = "products.view_product"
