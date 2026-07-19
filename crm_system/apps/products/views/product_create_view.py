"""Представление для создания услуги."""

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.products.models import Product


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Представление для создания новой услуги.

    :ivar model: Модель, связанная с представлением.
    :vartype model: type[Product]
    :ivar fields: Список полей формы, доступных для заполнения.
    :vartype fields: list[str]
    :ivar template_name: Путь к HTML-шаблону страницы создания.
    :vartype template_name: str
    :ivar success_url: URL для перенаправления после успешного создания.
    :vartype success_url: str
    :ivar permission_required: Требуемое разрешение для доступа к представлению.
    :vartype permission_required: str
    """

    model = Product
    fields = ["name", "description", "price"]
    template_name = "products/products-create.html"
    success_url = reverse_lazy("products:products-list")
    permission_required = "products.add_product"
