from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("history/", views.HistoryView.as_view(), name="history"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("anatomy/", views.AnatomyView.as_view(), name="anatomy"),
    path("delivery/", views.DeliveryView.as_view(), name="delivery"),
    path("pricing/", views.PricingView.as_view(), name="pricing"),
    path("gallery/", views.gallery, name="gallery"),
    path("faqs/", views.faqs, name="faqs"),
    path("contact/", views.contact, name="contact"),
]
