from pathlib import Path

import polib
from django.conf import settings
from django.core.management.base import BaseCommand

from qarauy.translations import TRANSLATIONS


class Command(BaseCommand):
    help = "Compile locale/*/LC_MESSAGES/django.mo from qarauy/translations.py"

    def handle(self, *args, **options):
        base = Path(settings.BASE_DIR) / "locale"
        for lang, messages in TRANSLATIONS.items():
            if lang == "en":
                continue
            po = polib.POFile()
            po.metadata = {
                "Content-Type": "text/plain; charset=utf-8",
                "Language": lang,
            }
            for msgid, msgstr in messages.items():
                po.append(polib.POEntry(msgid=msgid, msgstr=msgstr))
            dest_dir = base / lang / "LC_MESSAGES"
            dest_dir.mkdir(parents=True, exist_ok=True)
            mo_path = dest_dir / "django.mo"
            po.save_as_mofile(str(mo_path))
            self.stdout.write(f"Compiled {mo_path} ({len(messages)} strings)")

        self.stdout.write(self.style.SUCCESS("Translations compiled."))
