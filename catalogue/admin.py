from django.contrib import admin

from .models import Color, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "diameter_m", "price_usd", "is_active", "popularity")
    list_filter = ("is_active", "is_tall")
    prepopulated_fields = {"slug": ("name",)}
    filter_horizontal = ("colors",)


admin.site.register(Color)
admin.site.register(Product, ProductAdmin)
