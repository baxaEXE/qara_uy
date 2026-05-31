from decimal import Decimal
from pathlib import Path

from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand

from catalogue.models import Color, Product
from pages.models import FAQ

COLORS = [
    ("Natural Felt", "#e8dcc8"),
    ("White Wool", "#f5f0e8"),
    ("Indigo Blue", "#1e3a5f"),
    ("Terracotta", "#c45c26"),
    ("Crimson Red", "#8b1a1a"),
    ("Golden Yellow", "#d4a017"),
    ("Sky Blue", "#5b9bd5"),
    ("Charcoal Grey", "#4a4a4a"),
    ("Natural Wood", "#8b6914"),
]

# Four qara uy models from product photos
PRODUCTS = [
    {
        "name": "6 m Classic Qara Uy",
        "slug": "classic-qara-uy",
        "diameter_m": Decimal("6.0"),
        "price_usd": Decimal("9950.00"),
        "tagline": "Traditional steppe dwelling — felt dome & shiy walls",
        "description": (
            "Authentic six-meter qara uy with a white felt dome reinforced by dark "
            "cross-straps, natural shiy (reed-mat) walls with traditional patterned "
            "bands, and a handcrafted wooden door. Ideal for permanent homes, guest "
            "houses, and cultural projects on the steppe."
        ),
        "popularity": 100,
        "is_tall": False,
        "image": "qara-uy-classic-exterior.png",
        "color_names": ["Natural Felt", "Golden Yellow", "Natural Wood", "Charcoal Grey"],
    },
    {
        "name": "7 m Ornate Qara Uy",
        "slug": "ornate-qara-uy",
        "diameter_m": Decimal("7.0"),
        "price_usd": Decimal("16900.00"),
        "tagline": "Museum-quality beldeu & basqur ornamentation",
        "description": (
            "Premium seven-meter display qara uy featuring a white felt roof, golden "
            "shiy reed walls, wide multi-coloured beldeu horizontal bands, vertical "
            "basqur accents at the entrance, and diamond lattice cordwork. A "
            "showpiece for museums, resorts, and cultural festivals."
        ),
        "popularity": 95,
        "is_tall": False,
        "image": "qara-uy-ornate-display.png",
        "color_names": [
            "White Wool",
            "Golden Yellow",
            "Crimson Red",
            "Sky Blue",
            "Indigo Blue",
        ],
    },
    {
        "name": "6 m Furnished Qara Uy",
        "slug": "furnished-qara-uy",
        "diameter_m": Decimal("6.0"),
        "price_usd": Decimal("14500.00"),
        "tagline": "Complete interior — sandıq, kurpacha & shyrdak",
        "description": (
            "Fully furnished six-meter qara uy kit including kerege lattice walls, "
            "uuk roof poles, decorative sandıq chests with traditional black "
            "geometric patterns, stacked kurpacha quilts, shyrdak floor coverings, "
            "and wall ornaments. Move-in ready for living or exhibition."
        ),
        "popularity": 90,
        "is_tall": False,
        "image": "qara-uy-furnished-interior.png",
        "color_names": [
            "Crimson Red",
            "Indigo Blue",
            "Natural Wood",
            "Natural Felt",
            "Golden Yellow",
        ],
    },
    {
        "name": "5 m Traditional Interior Qara Uy",
        "slug": "traditional-interior-qara-uy",
        "diameter_m": Decimal("5.0"),
        "price_usd": Decimal("12900.00"),
        "tagline": "Red baskur textiles & authentic sandıq set",
        "description": (
            "Five-meter qara uy with richly decorated interior: dark-stained kerege "
            "lattice, red-and-white baskur wall hangings, traditional gilam floor "
            "coverings, stacked sandıq storage chests, and classic Karakalpak "
            "household vessels. Perfect for couples and cultural guest spaces."
        ),
        "popularity": 85,
        "is_tall": False,
        "image": "qara-uy-traditional-interior.png",
        "color_names": ["Crimson Red", "Natural Wood", "Natural Felt", "Terracotta"],
    },
]

FAQS = [
    (
        "What is a qara uy?",
        "Qara uy (Karakalpak: «black house») is the traditional felt dwelling of the "
        "Karakalpak people—cousin to the Mongol ger and Kazakh kiiz ui. Our kits are "
        "built by artisans in Karakalpakstan using centuries-old methods.",
    ),
    (
        "How long does assembly take?",
        "Two experienced people can erect a standard six-meter qara uy in four to six hours. "
        "We include a detailed assembly guide and optional video support.",
    ),
    (
        "Do you ship internationally?",
        "Yes. We deliver throughout Central Asia, Europe, and North America. See our "
        "Delivery page for tour schedules and shipping estimates.",
    ),
    (
        "What is included in the kit?",
        "Each kit includes lattice walls, roof wheel (shanyrak), roof poles, felt covers, "
        "inner decorative liners, door frame, and all ropes and hardware.",
    ),
    (
        "Can I customize colors and patterns?",
        "Absolutely. Choose from our standard felt colors or commission custom shyrdak "
        "patterns with our weavers—lead time adds approximately four weeks.",
    ),
]


class Command(BaseCommand):
    help = "Seed catalogue with 4 photo qara uy products, colors, and FAQs"

    def handle(self, *args, **options):
        media_dir = Path(settings.BASE_DIR) / "media" / "products"

        color_objs = {}
        for name, hex_code in COLORS:
            obj, _ = Color.objects.get_or_create(name=name, defaults={"hex_code": hex_code})
            color_objs[name] = obj

        # Remove old placeholder products not in the photo set
        keep_slugs = {p["slug"] for p in PRODUCTS}
        removed = Product.objects.exclude(slug__in=keep_slugs).delete()[0]
        if removed:
            self.stdout.write(f"Removed {removed} old product(s)")

        for data in PRODUCTS:
            image_name = data.pop("image")
            color_names = data.pop("color_names")
            slug = data["slug"]

            product, created = Product.objects.update_or_create(
                slug=slug,
                defaults={k: v for k, v in data.items() if k != "slug"},
            )

            product.colors.set([color_objs[n] for n in color_names if n in color_objs])

            image_path = media_dir / image_name
            if image_path.exists():
                with image_path.open("rb") as img_file:
                    product.image.save(image_name, File(img_file), save=True)
            else:
                self.stdout.write(self.style.WARNING(f"Image not found: {image_path}"))

            action = "Created" if created else "Updated"
            self.stdout.write(f"{action}: {product.name} — ${product.price_usd}")

        for i, (q, a) in enumerate(FAQS):
            FAQ.objects.update_or_create(
                question=q,
                defaults={"answer": a, "sort_order": i},
            )

        self.stdout.write(self.style.SUCCESS("Seed complete — 4 qara uy products ready."))
