from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from apps.products.models import Product


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    fields = ["name", "description", "price"]
    template_name = "products/products-edit.html"
    success_url = reverse_lazy("products:products-list")
    permission_required = "products.change_product"
