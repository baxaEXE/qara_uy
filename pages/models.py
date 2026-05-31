from django.db import models
from django.utils.translation import gettext_lazy as _


class GalleryImage(models.Model):
    title = models.CharField(max_length=200)
    caption = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to="gallery/", blank=True, null=True)
    sort_order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["sort_order", "-id"]

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order"]
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question


class ContactInquiry(models.Model):
    SUBJECT_CHOICES = [
        ("buy", _("Buy a Qara Uy")),
        ("parts", _("Parts & Furniture")),
        ("technical", _("Technical Support")),
        ("general", _("General Inquiry")),
    ]
    USE_CHOICES = [
        ("living", _("Extra Living Space")),
        ("housing", _("Affordable Housing (Off-grid)")),
        ("rental", _("Airbnb / Guest House")),
        ("yoga", _("Yoga / Meditation / Spiritual Space")),
        ("campsite", _("Campsite / Resort")),
        ("education", _("Education / Classroom")),
        ("therapy", _("Healing / Therapy")),
        ("festival", _("Festival / Cultural Event")),
        ("other", _("Other")),
    ]
    CONTACT_METHOD_CHOICES = [
        ("call", _("Call")),
        ("text", _("Text")),
        ("email", _("Email")),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)
    intended_use = models.CharField(max_length=32, choices=USE_CHOICES, blank=True)
    subject = models.CharField(max_length=32, choices=SUBJECT_CHOICES, default="buy")
    preferred_contact = models.CharField(
        max_length=16, choices=CONTACT_METHOD_CHOICES, default="email"
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Contact inquiries"

    def __str__(self):
        return f"{self.first_name} {self.last_name} — {self.get_subject_display()}"
