from django.utils.translation import gettext_lazy as _

HISTORY_SECTIONS = [
    {
        "id": "origins",
        "title": _("Origins of the Qara Uy"),
        "paragraphs": [
            _(
                "The qara uy — literally «black house» in Karakalpak — is one of the oldest "
                "portable dwellings of Central Asia. Its roots reach back more than two "
                "thousand years to the nomadic Turkic and Iranian peoples who moved across "
                "the steppes between the Caspian Sea and the Tian Shan mountains."
            ),
            _(
                "The name qara (black) refers to the dark outer felt covers that protected "
                "the dwelling from rain, snow, and sun. Inside, families lined the walls "
                "with bright shyrdak and alasha textiles — the contrast gave the home its "
                "distinctive Karakalpak character."
            ),
        ],
    },
    {
        "id": "karakalpak",
        "title": _("The Karakalpak People & the Amu Darya"),
        "paragraphs": [
            _(
                "The Karakalpak people — Qaraqalpaqlar — have lived for centuries along "
                "the lower Amu Darya river, on the Ustyurt Plateau, and around the Aral "
                "Sea. Their name means «black hat» or «black hood,» reflecting ancient "
                "tribal traditions shared with neighbouring Kazakh and Nogai groups."
            ),
            _(
                "For the Karakalpak, the qara uy was not merely a tent but the centre of "
                "family life: births, weddings, hospitality, and council gatherings all "
                "took place within its round walls. The circular form symbolised the unity "
                "of the family and the eternal cycle of seasons on the steppe."
            ),
        ],
    },
    {
        "id": "ancient",
        "title": _("Ancient & Medieval History"),
        "paragraphs": [
            _(
                "Archaeological evidence from Khorezm and the Aral Sea region shows that "
                "felt-covered wooden-frame dwellings similar to the qara uy existed as "
                "early as the first millennium BCE. Arab travellers of the 10th century "
                "described nomadic camps along the Amu Darya with round felt tents."
            ),
            _(
                "During the Golden Horde and later Khanate periods, Karakalpak ancestors "
                "migrated between summer pastures (jailau) on the Ustyurt and winter "
                "quarters (qystau) in the river delta. Each migration required dismantling "
                "and rebuilding the qara uy — a skill passed from father to son."
            ),
            _(
                "The 19th-century Russian explorer Nikolay Muravyov noted that Karakalpak "
                "yurts differed from Kazakh and Uzbek types in their taller walls, "
                "richer inner decoration, and distinctive shiy (reed-mat) screens."
            ),
        ],
    },
    {
        "id": "craft",
        "title": _("Traditional Craftsmanship"),
        "paragraphs": [
            _(
                "Building a qara uy was a community effort. Men cut and bent willow for "
                "the kerege (lattice walls) and uuk (roof poles). Women pressed wool into "
                "felt (kiyiz) and wove shyrdak carpets with geometric patterns passed down "
                "through generations."
            ),
            _(
                "The shanyrak — the circular roof wheel — was the most honoured part of "
                "the dwelling. When a family moved permanently, the shanyrak was kept and "
                "passed to the eldest son, while the felt covers were replaced. A Karakalpak "
                "proverb says: «When the shanyrak rises, the home lives.»"
            ),
            _(
                "Decorative elements — beldeu bands, basqur tassels, janbau wall hangings, "
                "and sandıq chests — were not mere ornament but carried symbolic meaning: "
                "protection, fertility, and connection to ancestors."
            ),
        ],
    },
    {
        "id": "daily-life",
        "title": _("Life Inside the Qara Uy"),
        "paragraphs": [
            _(
                "The interior was arranged by tradition: the honour place (tor) faced the "
                "door; bedding (kurpacha) was stacked on wooden sandıq chests; the hearth "
                "occupied the centre. Guests were always seated in the place of honour."
            ),
            _(
                "Seasonal rhythms governed life: spring brought felt-making and repairs; "
                "summer meant migration to pasture; autumn was for hunting and storing "
                "provisions; winter gatherings centred around the hearth inside the warm "
                "felt walls. Songs, epic poetry (dastan), and oral history were shared "
                "in the qara uy on long winter nights."
            ),
        ],
    },
    {
        "id": "aral",
        "title": _("The Aral Sea Crisis & Sedentarization"),
        "paragraphs": [
            _(
                "In the 20th century, Soviet collectivization and the dramatic shrinking "
                "of the Aral Sea transformed Karakalpak life. Nomadic pastoralism declined; "
                "many families settled in villages and cities like Nukus, Muynak, and "
                "Turtkul. Qara uy building skills were at risk of disappearing."
            ),
            _(
                "The drying of the Aral Sea — one of the world's worst ecological disasters "
                "— forced mass relocation. Yet even in new settlements, Karakalpak families "
                "erected qara uys for weddings, Nauryz celebrations, and cultural festivals, "
                "keeping the tradition alive in changed circumstances."
            ),
        ],
    },
    {
        "id": "revival",
        "title": _("Cultural Revival & Modern Heritage"),
        "paragraphs": [
            _(
                "Since Uzbekistan's independence in 1991, Karakalpakstan has invested in "
                "reviving its cultural heritage. The Savitsky Museum in Nukus, UNESCO "
                "recognition efforts, and folk festivals on the Ustyurt have brought new "
                "attention to qara uy architecture."
            ),
            _(
                "Master craftsmen in Nukus, Muynak, and rural districts now build qara uys "
                "for museums, eco-tourism camps, international buyers, and diaspora "
                "communities. Each dwelling is numbered and signed by its lead artisan — "
                "a mark of authenticity and pride."
            ),
        ],
    },
    {
        "id": "today",
        "title": _("The Qara Uy Today"),
        "paragraphs": [
            _(
                "Today the qara uy stands as a symbol of Karakalpak resilience and identity. "
                "It serves as guest accommodation, cultural centres, yoga retreats, and "
                "living museums across Central Asia, Europe, and North America."
            ),
            _(
                "When you purchase a qara uy from our workshop, you support master "
                "artisans, fair wages for felt-makers and weavers, and the survival of a "
                "two-thousand-year building tradition. The black house remains — as it "
                "always has — a home for the spirit of the Karakalpak people."
            ),
        ],
    },
]

TIMELINE = [
    ("1000 BCE", _("Early felt dwellings in Khorezm and Aral region")),
    ("10th c.", _("Arab travellers describe Amu Darya nomad camps")),
    ("19th c.", _("Muravyov documents Karakalpak yurt traditions")),
    ("1930s", _("Soviet collectivization; nomadic life declines")),
    ("1960s–80s", _("Aral Sea shrinks; mass sedentarization")),
    ("1991", _("Independence; cultural revival begins")),
    ("Today", _("Qara uys built worldwide by Karakalpak masters")),
]
