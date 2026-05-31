# Qara Uy — Karakalpak National Dwellings

Django e-commerce catalogue for authentic **qara uy** (Karakalpak felt dwellings), inspired by the layout of [Groovy Yurts](https://www.groovyyurts.com/catalogue/mongolian-yurt-kit).

## Features

- Product catalogue with size/price/popularity sorting
- Product detail pages with color options
- About, anatomy, delivery, gallery, and FAQ pages
- Contact / quote request form (stored in admin)
- Django admin for products, gallery, and inquiries

## Quick start

```powershell
cd d:\jproject
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_catalogue
python manage.py compile_translations
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/

- **Catalogue:** http://127.0.0.1:8000/catalogue/
- **Admin:** http://127.0.0.1:8000/admin/

## Project structure

| Path | Purpose |
|------|---------|
| `catalogue/` | Products, colors, catalogue views |
| `pages/` | Home, about, contact, gallery, FAQs |
| `templates/` | HTML templates |
| `static/` | CSS and JavaScript |

## Languages

The site supports **ENG**, **RUS**, **UZB**, and **QARAQALPAQ** via the header language bar. Translations live in `qarauy/translations.py`. After editing them, run:

```powershell
python manage.py compile_translations
```

## Customization

Edit contact details in `qarauy/context_processors.py`. Add product images via the admin panel or by uploading to `media/products/`.
