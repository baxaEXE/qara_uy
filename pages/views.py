from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _
from django.views.generic import TemplateView

from catalogue.selectors import get_active_products
from .forms import ContactForm
from .history_content import HISTORY_SECTIONS, TIMELINE
from .models import FAQ, GalleryImage


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["featured_products"] = get_active_products().order_by("-popularity")
        return ctx


class AboutView(TemplateView):
    template_name = "pages/about.html"


class AnatomyView(TemplateView):
    template_name = "pages/anatomy.html"


class DeliveryView(TemplateView):
    template_name = "pages/delivery.html"


class HistoryView(TemplateView):
    template_name = "pages/history.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["history_sections"] = HISTORY_SECTIONS
        ctx["timeline"] = TIMELINE
        ctx["products"] = get_active_products().order_by("-popularity")
        return ctx


class PricingView(TemplateView):
    template_name = "pages/pricing.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["products"] = get_active_products().order_by("-popularity")
        return ctx


def gallery(request):
    products = get_active_products().order_by("-popularity")
    extra_images = GalleryImage.objects.all()
    return render(
        request,
        "pages/gallery.html",
        {"products": products, "extra_images": extra_images},
    )


def faqs(request):
    faq_list = FAQ.objects.all()
    return render(request, "pages/faqs.html", {"faqs": faq_list})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                _("Thanks for reaching out. We will get back to you soon!"),
            )
            return redirect("pages:contact")
        messages.error(request, _("Please correct the errors below."))
    else:
        form = ContactForm()
    return render(request, "pages/contact.html", {"form": form})
