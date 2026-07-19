"""Представление для отображения детальной информации об услуге."""

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import DetailView

from apps.products.models import Product


class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Представление для отображения детальной информации об услуге.

    :ivar model: Модель, связанная с представлением.
    :vartype model: type[Product]
    :ivar template_name: Путь к HTML-шаблону детальной страницы.
    :vartype template_name: str
    :ivar permission_required: Требуемое разрешение для доступа к представлению.
    :vartype permission_required: str
    """

    model = Product
    template_name = "products/products-detail.html"
    permission_required = "products.view_product"
