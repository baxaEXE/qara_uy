from catalogue.models import Product


def get_active_products():
    return Product.objects.filter(is_active=True).prefetch_related("colors")
