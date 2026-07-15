from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Product


class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Product
    template_name = "products/products-list.html"
    context_object_name = "products"
    permission_required = "products.view_product"


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    fields = ["name", "description", "price"]
    template_name = "products/products-create.html"
    success_url = reverse_lazy("products:products-list")
    permission_required = "products.add_product"


class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Product
    template_name = "products/products-detail.html"
    permission_required = "products.view_product"


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    fields = ["name", "description", "price"]
    template_name = "products/products-edit.html"
    success_url = reverse_lazy("products:products-list")
    permission_required = "products.change_product"


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = "products/products-delete.html"
    success_url = reverse_lazy("products:products-list")
    permission_required = "products.delete_product"
