from django import forms
from django.utils.translation import gettext_lazy as _

from .models import ContactInquiry


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInquiry
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "country",
            "region",
            "intended_use",
            "subject",
            "preferred_contact",
            "message",
        ]
        widgets = {
            "first_name": forms.TextInput(
                attrs={"placeholder": _("First name"), "class": "form-control"}
            ),
            "last_name": forms.TextInput(
                attrs={"placeholder": _("Last name"), "class": "form-control"}
            ),
            "email": forms.EmailInput(
                attrs={"placeholder": _("Email"), "class": "form-control"}
            ),
            "phone": forms.TextInput(
                attrs={"placeholder": _("Phone"), "class": "form-control"}
            ),
            "country": forms.TextInput(
                attrs={"placeholder": _("Country"), "class": "form-control"}
            ),
            "region": forms.TextInput(
                attrs={"placeholder": _("Province / Region"), "class": "form-control"}
            ),
            "intended_use": forms.Select(attrs={"class": "form-control"}),
            "subject": forms.Select(attrs={"class": "form-control"}),
            "preferred_contact": forms.Select(attrs={"class": "form-control"}),
            "message": forms.Textarea(
                attrs={
                    "placeholder": _("Your message..."),
                    "rows": 5,
                    "class": "form-control",
                }
            ),
        }
