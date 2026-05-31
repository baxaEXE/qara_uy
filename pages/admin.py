from django.contrib import admin

from .models import ContactInquiry, FAQ, GalleryImage


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("title", "sort_order", "is_featured")


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "sort_order")


@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "subject", "created_at", "is_read")
    list_filter = ("subject", "is_read")
    readonly_fields = ("created_at",)
