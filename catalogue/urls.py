from django.urls import path

from . import views

app_name = "catalogue"

urlpatterns = [
    path("", views.CatalogueListView.as_view(), name="catalogue"),
    path("<slug:slug>/", views.ProductDetailView.as_view(), name="product_detail"),
]
