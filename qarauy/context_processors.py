from django.utils.translation import gettext_lazy as _

from .i18n_config import LANGUAGE_BAR


def site(request):
    return {
        "SITE_NAME": "Qara Uy",
        "SITE_TAGLINE": _("Authentic Karakalpak National Dwellings"),
        "CONTACT_EMAIL": "info@qarauy.uz",
        "CONTACT_PHONE": "+998 61 123 45 67",
        "CONTACT_ADDRESS": _("Nukus, Republic of Karakalpakstan, Uzbekistan"),
    }


def language_bar(request):
    return {"LANGUAGE_BAR": LANGUAGE_BAR}
