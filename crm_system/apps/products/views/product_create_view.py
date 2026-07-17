from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.products.models import Product


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    fields = ["name", "description", "price"]
    template_name = "products/products-create.html"
    success_url = reverse_lazy("products:products-list")
    permission_required = "products.add_product"
