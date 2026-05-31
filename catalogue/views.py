from django.views.generic import DetailView, ListView

from .models import Product

SORT_MAP = {
    "size_asc": "diameter_m",
    "size_desc": "-diameter_m",
    "price_asc": "price_usd",
    "price_desc": "-price_usd",
    "popularity": "-popularity",
}


class CatalogueListView(ListView):
    model = Product
    template_name = "catalogue/catalogue.html"
    context_object_name = "products"
    paginate_by = 12

    def get_queryset(self):
        qs = Product.objects.filter(is_active=True).prefetch_related("colors")
        sort = self.request.GET.get("sort", "popularity")
        return qs.order_by(SORT_MAP.get(sort, "-popularity"))

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["current_sort"] = self.request.GET.get("sort", "popularity")
        return ctx


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalogue/product_detail.html"
    context_object_name = "product"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return Product.objects.filter(is_active=True).prefetch_related("colors")
