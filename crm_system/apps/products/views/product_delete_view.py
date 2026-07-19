"""Представление для удаления услуги."""

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from apps.products.models import Product


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Представление для удаления существующей услуги.

    :ivar model: Модель, связанная с представлением.
    :vartype model: type[Product]
    :ivar template_name: Путь к HTML-шаблону страницы подтверждения удаления.
    :vartype template_name: str
    :ivar success_url: URL для перенаправления после успешного удаления.
    :vartype success_url: str
    :ivar permission_required: Требуемое разрешение для доступа к представлению.
    :vartype permission_required: str
    """

    model = Product
    template_name = "products/products-delete.html"
    success_url = reverse_lazy("products:products-list")
    permission_required = "products.delete_product"
