from django.db import models
from django.urls import reverse


class Color(models.Model):
    name = models.CharField(max_length=64)
    hex_code = models.CharField(max_length=7, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    diameter_m = models.DecimalField(
        max_digits=4, decimal_places=1, help_text="Diameter in meters"
    )
    price_usd = models.DecimalField(max_digits=10, decimal_places=2)
    tagline = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    colors = models.ManyToManyField(Color, blank=True, related_name="products")
    is_tall = models.BooleanField(default=False, help_text="Tall / high-wall variant")
    popularity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-popularity", "diameter_m"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalogue:product_detail", kwargs={"slug": self.slug})

    @property
    def diameter_display(self):
        return f"{self.diameter_m:g} m"
