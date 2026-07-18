"""URL-маршруты для приложения «Услуги»."""

from django.urls import path

from .views import (
    ProductListView,
    ProductCreateView,
    ProductDetailView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name = "products"

urlpatterns = [
    path("", ProductListView.as_view(), name="products-list"),
    path("create/", ProductCreateView.as_view(), name="products-create"),
    path("<int:pk>/", ProductDetailView.as_view(), name="products-detail"),
    path("<int:pk>/edit/", ProductUpdateView.as_view(), name="products-edit"),
    path("<int:pk>/delete/", ProductDeleteView.as_view(), name="products-delete"),
]
