import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "xylem",
    "name": "Xylem",
    "mono": "XYL",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Plant tissue that carries water up from the roots · Wood is made of it",
    "dates": "Named by Carl Nägeli in 1858",
    "briefing": "Xylem is a plant’s plumbing: tubes of tough, dead, hollow cells that carry water and minerals from the roots up to the leaves. As water evaporates from the leaves, it pulls the column of water behind it upward, lifting water more than 100 meters to the tops of the tallest redwoods. Wood is mostly xylem, and a tree’s rings are layers of it added year after year.",
    "answerHtml": "<b><u>Xylem</u></b> (prompt on <u>vascular tissue</u>; do not accept “phloem”)",
    "accept": [
        "xylem",
        "xylems",
        "xylem tissue",
        "xylem vessels",
        "primary xylem",
        "secondary xylem"
    ],
    "prompt": [
        "vascular tissue",
        "vascular tissues",
        "vascular bundle",
        "vascular bundles"
    ],
    "reject": [
        "phloem",
        "cambium",
        "vascular cambium",
        "cork cambium",
        "cork",
        "bark",
        "pith",
        "cortex",
        "epidermis",
        "endodermis",
        "stomata",
        "stoma",
        "tracheid",
        "tracheids",
        "vessel element",
        "vessel elements",
        "sieve tube",
        "sieve tubes",
        "companion cells",
        "wood",
        "sapwood",
        "heartwood",
        "lignin",
        "cellulose",
        "root hairs",
        "xylene"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Xylem",
    "qb": {
        "q": "xylem",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Swiss botanist Carl Nägeli [“NAY-guh-lee”] named this tissue in 1858 from the Greek word for “wood.” In a tree trunk, the vascular cambium adds a new layer of this tissue each year, forming growth rings that can be counted to find the tree’s age.",
            "r": "It works alongside phloem. For 10 points, name this plant tissue that carries water up from the roots."
        },
        {
            "p": "Henry Dixon and John Joly [“JOH-lee”] proposed in the 1890s that water is pulled up this tissue as one unbroken column, held together by hydrogen bonds. In their cohesion-tension theory, the pull comes from water evaporating out of leaves through tiny pores called stomata.",
            "r": "It can lift water more than 100 meters up the tallest redwoods. For 10 points, name this vascular tissue, which works alongside phloem."
        },
        {
            "p": "In his 1727 book _Vegetable Staticks_, Stephen Hales measured how much water plants lose through their leaves and how strongly their roots push water upward. That push, called root pressure, can force water up this tissue and out of leaf edges as droplets, a process called guttation [“guh-TAY-shun”].",
            "r": "Phloem works alongside it. For 10 points, name this plant tissue made of tracheids and vessel elements."
        },
        {
            "p": "In flowering plants, cells called vessel elements are stacked end to end and joined by openings called perforation plates, forming long, open pipes in this tissue. Narrower, tapered cells called tracheids [“TRAY-kee-idz”] also carry water through this tissue.",
            "r": "For 10 points, name this vascular tissue that moves water and minerals up from a plant’s roots."
        },
        {
            "p": "Conifer wood is made almost entirely of cells called tracheids, which pass water to one another through thin spots called pits; in many conifers, each pit has a valve-like plug called a torus. Those cells belong to this tissue, which also includes the wider vessels of flowering trees.",
            "r": "It works with phloem. For 10 points, name this plant tissue that carries water upward from the roots."
        },
        {
            "p": "Balloon-like growths called tyloses [“tye-LOH-seez”] plug the old vessels of this tissue in white oak, making that wood watertight enough to hold liquid in barrels. In a tree trunk, the heartwood at the center is made of old layers of this tissue that no longer carry water.",
            "r": "It carries water up from the roots. For 10 points, name this vascular tissue whose outer, working layers form the sapwood."
        },
        {
            "p": "A bacterium that causes Pierce’s disease in grapevines is spread by insects called sharpshooters and can kill vines by clogging this tissue. Dutch elm disease, caused by a fungus, can also kill trees by blocking water flow through this tissue.",
            "r": "For 10 points, name this plant tissue that carries water and minerals, unlike phloem, which carries sugar."
        },
        {
            "p": "In late winter, the sugary sap that people collect from maple trees and boil down into syrup comes from this tissue. The sap flows best when freezing nights are followed by thawing days, which build up pressure inside the trunk.",
            "r": "Wood is made mostly of it. For 10 points, name this plant tissue that carries water and minerals up from the roots."
        },
        {
            "p": "During droughts or hard freezes, air bubbles can form inside this tissue and break its water columns, a problem called cavitation or embolism. Plants survive this partly because water can detour sideways around a blocked cell through thin spots in the cell walls called pits.",
            "r": "Phloem works alongside it. For 10 points, name this vascular tissue that carries water up from the roots."
        },
        {
            "p": "Before water from the soil can enter this tissue in a root, it must pass through living cells at the Casparian [“kas-PAIR-ee-un”] strip, a waxy band in the endodermis. In the center of many roots, this tissue forms an X- or star-shaped core.",
            "r": "It works alongside phloem. For 10 points, name this vascular tissue that carries water up to the leaves."
        },
        {
            "p": "The first cells of this tissue to form in a young stem have ring- or spiral-shaped thickenings in their walls, which let them stretch as the stem grows longer. Later cells of this tissue have thicker walls stiffened with lignin.",
            "r": "For 10 points, name this plant tissue that carries water and minerals up from the roots."
        },
        {
            "p": "Vascular plants are sometimes called tracheophytes, after one kind of cell in this tissue. Mosses and other bryophytes lack this tissue, which is one reason they stay small and grow in damp places.",
            "r": "Wood is made mostly of it. For 10 points, name this water-carrying plant tissue that works alongside phloem."
        },
        {
            "p": "In leaf veins, this tissue usually lies on the upper side, with phloem below it. If you stand a stalk of celery or a white carnation in colored water, the dye climbs through tubes of this tissue and tints the leaves or petals.",
            "r": "For 10 points, name this vascular tissue that carries water and minerals up from the roots."
        },
        {
            "p": "In a typical stem, this tissue sits on the inner side of each vascular bundle, with phloem on the outer side. As a tree trunk thickens, the vascular cambium adds new cells of this tissue toward the inside and new phloem toward the outside.",
            "r": "It carries water up from the roots. For 10 points, name this plant tissue that makes up wood."
        },
        {
            "p": "This plant tissue is made of dead, hollow cells with stiff walls that link up into tiny pipes. It carries water and dissolved minerals from the roots up to the leaves, pulled along as water evaporates from the leaves.",
            "r": "Wood is made mostly of it. For 10 points, name this vascular tissue that works alongside phloem."
        }
    ],
    "clues": [
        {
            "id": "water-up",
            "tier": "giveaway",
            "t": "Plant tissue that carries water and dissolved minerals up from the roots to the leaves",
            "k": ["water", "minerals", "roots"],
            "n": 0
        },
        {
            "id": "vascular",
            "tier": "giveaway",
            "t": "One of the two vascular tissues, along with phloem, which carries sugar",
            "k": ["vascular", "phloem"],
            "n": 0,
            "rabbit": "Phloem"
        },
        {
            "id": "wood",
            "tier": "giveaway",
            "t": "Wood is mostly made of it, and tree rings are yearly layers of it",
            "k": ["wood", "tree rings"],
            "n": 0,
            "rabbit": "Trees"
        },
        {
            "id": "dead-cells",
            "tier": "giveaway",
            "t": "Its water-carrying cells are dead and hollow when they do their job",
            "k": ["dead", "hollow"],
            "n": 0
        },
        {
            "id": "one-way",
            "tier": "giveaway",
            "t": "Water moves through it in one direction, upward, while phloem carries sugar both up and down",
            "k": ["one direction", "upward"],
            "n": 0
        },
        {
            "id": "tracheids-vessels",
            "tier": "middle",
            "t": "Made of two kinds of water-carrying cells: long, narrow tracheids and wider vessel elements",
            "k": ["tracheids", "vessel elements"],
            "n": 0
        },
        {
            "id": "lignin",
            "tier": "middle",
            "t": "Its cell walls are stiffened with lignin, which also helps hold the plant up",
            "k": ["lignin", "stiffened"],
            "n": 0
        },
        {
            "id": "transpiration",
            "tier": "middle",
            "t": "Water evaporating from leaves (transpiration) pulls water up through it, as high as the tops of redwoods more than 100 meters tall",
            "k": ["transpiration", "evaporating", "redwoods"],
            "n": 0
        },
        {
            "id": "cohesion-tension",
            "tier": "middle",
            "t": "The cohesion-tension theory: hydrogen bonds hold the water column together as it is pulled up",
            "k": ["cohesion-tension", "hydrogen bonds"],
            "n": 0
        },
        {
            "id": "root-pressure",
            "tier": "middle",
            "t": "Root pressure can push water up it and out of leaf edges as droplets, which is called guttation",
            "k": ["root pressure", "guttation"],
            "n": 0
        },
        {
            "id": "cambium",
            "tier": "middle",
            "t": "The vascular cambium adds new layers of it toward the inside of a stem and new phloem toward the outside",
            "k": ["vascular cambium", "inside"],
            "n": 0
        },
        {
            "id": "heartwood-sapwood",
            "tier": "middle",
            "t": "Heartwood is old, non-working layers of it at a tree’s center; sapwood is the outer, working part",
            "k": ["heartwood", "sapwood"],
            "n": 0
        },
        {
            "id": "celery",
            "tier": "middle",
            "t": "Celery stalks or white carnations stood in colored water show dye climbing up through it",
            "k": ["celery", "carnations", "colored water"],
            "n": 0
        },
        {
            "id": "bryophytes",
            "tier": "middle",
            "t": "Mosses and other bryophytes lack it, which helps keep them small; vascular plants are called tracheophytes",
            "k": ["mosses", "bryophytes", "tracheophytes"],
            "n": 0
        },
        {
            "id": "veins-bundles",
            "tier": "middle",
            "t": "Runs with phloem in leaf veins and vascular bundles, usually on the upper side of a vein and the inner side of a bundle",
            "k": ["veins", "vascular bundles", "upper side"],
            "n": 0
        },
        {
            "id": "nageli",
            "tier": "power",
            "t": "Swiss botanist Carl Nägeli named it in 1858, from the Greek word for “wood”",
            "k": ["nägeli", "1858", "greek"],
            "n": 0
        },
        {
            "id": "dixon-joly",
            "tier": "power",
            "t": "Henry Dixon and John Joly proposed the cohesion-tension theory in the 1890s",
            "k": ["dixon", "joly", "1890s"],
            "n": 0
        },
        {
            "id": "hales",
            "tier": "power",
            "t": "Stephen Hales measured water loss and root pressure in his 1727 book _Vegetable Staticks_",
            "k": ["stephen hales", "vegetable staticks", "1727"],
            "n": 0
        },
        {
            "id": "perforation-plates",
            "tier": "power",
            "t": "Vessel elements are stacked end to end and joined by openings called perforation plates",
            "k": ["perforation plates", "end to end"],
            "n": 0
        },
        {
            "id": "pits-torus",
            "tier": "power",
            "t": "Water passes sideways between its cells through thin spots called pits; many conifer pits have a valve-like plug called a torus",
            "k": ["pits", "torus", "valve-like"],
            "n": 0
        },
        {
            "id": "softwood",
            "tier": "power",
            "t": "Conifer wood (softwood) is almost all tracheids; flowering trees (hardwoods) also have wide vessels",
            "k": ["softwood", "hardwoods", "conifer"],
            "n": 0
        },
        {
            "id": "cavitation",
            "tier": "power",
            "t": "Air bubbles from drought or freezing can break its water columns, which is called cavitation or embolism",
            "k": ["cavitation", "embolism", "air bubbles"],
            "n": 0
        },
        {
            "id": "tyloses",
            "tier": "power",
            "t": "Balloon-like tyloses plug its old vessels; in white oak they make the wood watertight enough for barrels",
            "k": ["tyloses", "white oak", "barrels"],
            "n": 0
        },
        {
            "id": "pierces-disease",
            "tier": "power",
            "t": "The bacterium behind Pierce’s disease of grapevines, spread by sharpshooter insects, clogs it",
            "k": ["pierce’s disease", "sharpshooter", "grapevines"],
            "n": 0
        },
        {
            "id": "dutch-elm",
            "tier": "power",
            "t": "Dutch elm disease, caused by a fungus, can kill trees by blocking water flow through it",
            "k": ["dutch elm disease", "fungus"],
            "n": 0
        },
        {
            "id": "maple-sap",
            "tier": "power",
            "t": "The sugary maple sap that is boiled down into maple syrup in late winter comes from it; it flows best after freezing nights and thawing days",
            "k": ["maple syrup", "sap", "thawing"],
            "n": 0
        },
        {
            "id": "spiral-thickenings",
            "tier": "power",
            "t": "Its first-formed cells have ring- or spiral-shaped wall thickenings that let them stretch as the stem grows",
            "k": ["spiral", "ring", "stretch"],
            "n": 0
        },
        {
            "id": "casparian-strip",
            "tier": "power",
            "t": "Water must pass through living cells at the root’s Casparian strip, in the endodermis, before entering it",
            "k": ["casparian strip", "endodermis"],
            "n": 0,
            "rabbit": "Roots"
        }
    ],
    "trap": {
        "title": "Xylem or phloem?",
        "body": "Xylem and phloem are the two vascular tissues, and tossups often mention both. Xylem carries water and minerals up from the roots and is made mostly of dead, hollow cells; phloem carries sugar from the leaves to the rest of the plant through living sieve-tube cells. The vascular cambium, which makes new xylem and phloem, is a third answer that players confuse with both.",
        "fix": "Water, minerals, transpiration, tracheids, vessel elements, lignin, wood, or tree rings mean xylem. Sugar, sap flowing both up and down, sieve tubes, companion cells, or aphids mean phloem. A memory trick: phloem carries food.",
        "line": "Real answer line: <b><u>Xylem</u></b> (prompt on <u>vascular tissue</u>; do not accept “phloem”)"
    },
    "tests": {
        "right": [
            "Xylem",
            "xylem",
            "Xylem tissue",
            "Zylem",
            "Secondary xylem"
        ],
        "prompt": [
            "Vascular tissue"
        ],
        "wrong": [
            "Phloem",
            "Vascular cambium",
            "Tracheids",
            "Wood",
            "Stomata",
            "Cork"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
