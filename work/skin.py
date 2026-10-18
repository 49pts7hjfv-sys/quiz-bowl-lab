import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "skin",
    "name": "Skin",
    "mono": "SKN",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "The body’s largest organ · A waterproof, germ-blocking shield",
    "dates": "The largest organ of the human body",
    "briefing": "Your skin is your largest organ, and you are constantly shedding its outer cells and growing new ones to replace them. Its outer layer, the epidermis, is a waterproof shield topped with tough, dead cells full of keratin, while the dermis beneath holds sweat glands, nerves, and hair follicles. It also makes vitamin D in sunlight and gets its color from a pigment called melanin.",
    "answerHtml": "<b><u>Skin</u></b> (accept <u>integument</u>; prompt on <u>epidermis</u>, <u>dermis</u>, or <u>integumentary system</u>)",
    "accept": [
        "skin",
        "human skin",
        "integument"
    ],
    "prompt": [
        "epidermis",
        "dermis",
        "integumentary system",
        "integumentary"
    ],
    "reject": [
        "hair",
        "nails",
        "keratin",
        "melanin",
        "collagen",
        "sweat glands",
        "sweat gland",
        "sweat",
        "hypodermis",
        "subcutaneous layer",
        "subcutaneous tissue",
        "stratum corneum",
        "keratinocytes",
        "melanocytes",
        "scales",
        "fur",
        "feathers",
        "dermatitis",
        "epithelium"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Skin",
    "qb": {
        "q": "skin",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Surgeons try to cut along Langer’s lines, which follow the direction of the collagen fibers in this organ, so that cuts heal with smaller scars. The deeper of this organ’s two main layers, the dermis, holds blood vessels, nerves, and hair follicles.",
            "r": "Its outer layer, the epidermis, contains the pigment melanin. For 10 points, name this largest organ of the human body."
        },
        {
            "p": "Lungless salamanders take in all of their oxygen through the lining of their mouths and through this organ, which must stay moist to work. Snakes shed the outer layer of this organ, often in one piece, in a process called ecdysis [“EK-dih-sis”].",
            "r": "In humans, it is the body’s largest organ. For 10 points, name this organ whose layers include the epidermis."
        },
        {
            "p": "A mnemonic for the layers in the outer part of this organ is “Come, Let’s Get Sun Burned,” for the strata corneum, lucidum, granulosum, spinosum, and basale. The stratum lucidum shows up only in the thick parts of this organ on the palms and soles.",
            "r": "Sweat glands and hair follicles sit in its deeper layer, the dermis. For 10 points, name this organ whose outer layer is the epidermis."
        },
        {
            "p": "Langerhans [“LAHNG-er-hahns”] cells in this organ’s outer layer act as lookouts for the immune system, while Merkel cells near the base of that layer help sense light touch. That outer layer, the epidermis, has no blood vessels of its own.",
            "r": "For 10 points, name this organ, the body’s largest, which protects against germs and water loss."
        },
        {
            "p": "Onion-like Pacinian [“puh-SIN-ee-un”] corpuscles deep in this organ sense pressure and vibration, while Meissner’s [“MYSE-nerz”] corpuscles near its surface sense light touch. Ruffini endings in it respond to stretching, and free nerve endings in it detect pain, heat, and cold.",
            "r": "For 10 points, name this organ that covers the body and gives people their sense of touch."
        },
        {
            "p": "When ultraviolet B light strikes this organ, a molecule in it called 7-dehydrocholesterol is turned into vitamin D3. Too much ultraviolet light can cause sunburn and damage the DNA in this organ’s cells.",
            "r": "Its outer layer is called the epidermis. For 10 points, name this organ, whose color comes mainly from the pigment melanin."
        },
        {
            "p": "Brown-black eumelanin [“yoo-MEL-uh-nin”] and red-yellow pheomelanin [“fee-oh-MEL-uh-nin”] help give this organ its color. People with darker or lighter coloring have about the same number of melanocytes, the pigment-making cells in this organ, but those cells make different amounts of pigment.",
            "r": "People with albinism make little or no melanin. For 10 points, name this organ, whose outer layer is called the epidermis."
        },
        {
            "p": "Eccrine [“EK-rin”] glands cover most of this organ and release watery sweat that cools the body, while apocrine glands open into hair follicles in places like the armpits. Sebaceous [“sih-BAY-shus”] glands in this organ release an oily substance called sebum.",
            "r": "Its outer layer is the epidermis. For 10 points, name this organ, the largest in the human body."
        },
        {
            "p": "Tiny muscles called arrector pili [“uh-REK-ter PYE-lye”] attach to hair follicles in this organ and cause goosebumps when they contract. When the body overheats, vessels in this organ widen to release heat, which can make a person look flushed.",
            "r": "For 10 points, name this organ made up of the epidermis and the dermis."
        },
        {
            "p": "A polar bear’s fur looks white, but this organ underneath it is black. In humans, the outermost layer of this organ, the stratum corneum, is made of flat, dead cells filled with the tough protein keratin.",
            "r": "Hair and nails grow from this organ. For 10 points, name this organ that covers the outside of the body."
        },
        {
            "p": "Doctors use the “rule of nines” to estimate how much of this organ has been damaged by a burn. A first-degree burn, like a typical sunburn, affects only this organ’s outer layer, the epidermis.",
            "r": "Its deeper layer, the dermis, holds sweat glands and hair follicles. For 10 points, name this organ, the largest in the body."
        },
        {
            "p": "Francis Galton sorted the ridge patterns that this organ forms on the fingertips into arches, loops, and whorls. Koalas have ridge patterns on their fingers so similar to human ones that they can be hard to tell apart.",
            "r": "Those patterns are fingerprints. For 10 points, name this organ that covers the human body."
        },
        {
            "p": "New keratinocytes [“keh-RAT-in-oh-sites”] form in the stratum basale at the bottom of this organ’s outer layer, then move upward as they fill with a tough protein and die. Those dead cells are constantly shed from the surface of this organ.",
            "r": "For 10 points, name this organ whose outer layer is the epidermis and whose inner layer is the dermis."
        },
        {
            "p": "The Greek word “derma” and the Latin word “cutis” both name this organ, which is why a shot given just beneath it is called “subcutaneous.” Doctors called dermatologists specialize in treating it.",
            "r": "It gets its color from melanin and makes vitamin D in sunlight. For 10 points, name this largest organ of the human body."
        },
        {
            "p": "Collagen and elastin fibers give this organ’s dermis its strength and stretch, and as those fibers break down with age, wrinkles form. The unbroken surface of this organ is the body’s first line of defense against germs.",
            "r": "For 10 points, name this organ that covers the outside of the human body and is its largest organ."
        }
    ],
    "clues": [
        {
            "id": "largest-organ",
            "tier": "giveaway",
            "t": "The largest organ of the human body",
            "k": ["largest organ", "organ"],
            "n": 0
        },
        {
            "id": "two-layers",
            "tier": "giveaway",
            "t": "Two main layers: the outer epidermis and the inner dermis, with a fatty layer below",
            "k": ["epidermis", "dermis", "fatty layer"],
            "n": 0
        },
        {
            "id": "melanin",
            "tier": "giveaway",
            "t": "Gets its color mainly from the pigment melanin",
            "k": ["melanin", "pigment"],
            "n": 0
        },
        {
            "id": "barrier",
            "tier": "giveaway",
            "t": "A waterproof barrier and the body’s first line of defense against germs",
            "k": ["waterproof", "barrier", "first line of defense"],
            "n": 0
        },
        {
            "id": "sweat",
            "tier": "giveaway",
            "t": "Sweat glands in it cool the body as sweat evaporates",
            "k": ["sweat glands", "evaporates"],
            "n": 0
        },
        {
            "id": "vitamin-d",
            "tier": "middle",
            "t": "Makes vitamin D when ultraviolet (UVB) sunlight hits it",
            "k": ["vitamin d", "ultraviolet", "uvb"],
            "n": 0,
            "rabbit": "Vitamins"
        },
        {
            "id": "keratinocytes",
            "tier": "middle",
            "t": "Most cells of its outer layer are keratinocytes, which fill with the tough protein keratin",
            "k": ["keratinocytes", "keratin"],
            "n": 0,
            "rabbit": "Keratin"
        },
        {
            "id": "melanocytes",
            "tier": "middle",
            "t": "Melanocytes make melanin; people of all colorings have similar numbers of them but make different amounts of pigment",
            "k": ["melanocytes", "similar numbers"],
            "n": 0
        },
        {
            "id": "stratum-corneum",
            "tier": "middle",
            "t": "Its outermost layer, the stratum corneum, is made of flat, dead cells that are constantly shed",
            "k": ["stratum corneum", "dead cells", "shed"],
            "n": 0
        },
        {
            "id": "collagen",
            "tier": "middle",
            "t": "The dermis gets strength and stretch from collagen and elastin fibers",
            "k": ["collagen", "elastin"],
            "n": 0,
            "rabbit": "Collagen"
        },
        {
            "id": "goosebumps",
            "tier": "middle",
            "t": "Tiny arrector pili muscles pull hairs upright, causing goosebumps",
            "k": ["arrector pili", "goosebumps"],
            "n": 0
        },
        {
            "id": "sebaceous",
            "tier": "middle",
            "t": "Sebaceous glands release oily sebum into hair follicles",
            "k": ["sebaceous", "sebum", "hair follicles"],
            "n": 0
        },
        {
            "id": "fingerprints",
            "tier": "middle",
            "t": "Its ridges on the fingertips form fingerprints, which are unique to each person",
            "k": ["fingerprints", "ridges"],
            "n": 0
        },
        {
            "id": "strata",
            "tier": "power",
            "t": "Its outer layer has up to five strata: corneum, lucidum, granulosum, spinosum, and basale (“Come, Let’s Get Sun Burned”)",
            "k": ["corneum", "lucidum", "granulosum", "spinosum", "basale"],
            "n": 0
        },
        {
            "id": "stratum-lucidum",
            "tier": "power",
            "t": "The stratum lucidum appears only in the thick parts on the palms and soles",
            "k": ["stratum lucidum", "palms", "soles"],
            "n": 0
        },
        {
            "id": "langerhans",
            "tier": "power",
            "t": "Langerhans cells in its outer layer are lookouts for the immune system; that layer has no blood vessels",
            "k": ["langerhans", "immune", "blood vessels"],
            "n": 0
        },
        {
            "id": "touch-receptors",
            "tier": "power",
            "t": "Merkel cells and Meissner’s corpuscles sense light touch; onion-like Pacinian corpuscles sense pressure and vibration",
            "k": ["merkel", "meissner’s corpuscles", "pacinian", "vibration"],
            "n": 0
        },
        {
            "id": "langers-lines",
            "tier": "power",
            "t": "Langer’s lines follow the direction of its collagen fibers; surgeons cut along them to reduce scarring",
            "k": ["langer’s lines", "surgeons", "scarring"],
            "n": 0
        },
        {
            "id": "eccrine-apocrine",
            "tier": "power",
            "t": "Eccrine sweat glands cover most of the body; apocrine glands open into hair follicles in places like the armpits",
            "k": ["eccrine", "apocrine", "armpits"],
            "n": 0
        },
        {
            "id": "dehydrocholesterol",
            "tier": "power",
            "t": "UVB light turns 7-dehydrocholesterol in it into vitamin D3",
            "k": ["7-dehydrocholesterol", "vitamin d3"],
            "n": 0
        },
        {
            "id": "eumelanin",
            "tier": "power",
            "t": "Melanin comes in two main forms: brown-black eumelanin and red-yellow pheomelanin",
            "k": ["eumelanin", "pheomelanin"],
            "n": 0
        },
        {
            "id": "rule-of-nines",
            "tier": "power",
            "t": "Doctors estimate burned areas with the “rule of nines”; first-degree burns affect only the outer layer",
            "k": ["rule of nines", "first-degree", "burned"],
            "n": 0
        },
        {
            "id": "lungless-salamanders",
            "tier": "power",
            "t": "Lungless salamanders breathe entirely through it and the lining of their mouths",
            "k": ["lungless salamanders", "breathe"],
            "n": 0
        },
        {
            "id": "polar-bear",
            "tier": "power",
            "t": "A polar bear’s is black under its white-looking fur",
            "k": ["polar bear", "black", "fur"],
            "n": 0
        },
        {
            "id": "ecdysis",
            "tier": "power",
            "t": "Snakes shed the outer layer of theirs, often in one piece, in a process called ecdysis",
            "k": ["snakes", "ecdysis"],
            "n": 0,
            "rabbit": "Snakes"
        },
        {
            "id": "galton",
            "tier": "power",
            "t": "Francis Galton sorted fingerprints into arches, loops, and whorls; koala fingerprints look very similar to ours",
            "k": ["galton", "arches", "loops", "whorls", "koala"],
            "n": 0
        },
        {
            "id": "word-roots",
            "tier": "power",
            "t": "Greek “derma” and Latin “cutis” name it, giving us “dermatology” and “subcutaneous”",
            "k": ["derma", "cutis", "dermatology", "subcutaneous"],
            "n": 0
        }
    ],
    "trap": {
        "title": "The organ, or one layer?",
        "body": "Because this topic includes the epidermis, many clues describe only the outer layer: its strata, keratinocytes, melanocytes, and Langerhans cells. Quiz bowl also has tossups that want the epidermis itself, and on those, “skin” is too general. Tossups on the whole organ, in turn, only prompt on “epidermis” or “dermis.”",
        "fix": "Listen to the noun. “This organ” or “this largest organ” means skin; “this layer” or “this outermost layer” means epidermis; “this layer beneath the epidermis,” with collagen and sweat glands, means dermis.",
        "line": "Real answer line: <b><u>Skin</u></b> (accept <u>integument</u>; prompt on <u>epidermis</u>, <u>dermis</u>, or <u>integumentary system</u>)"
    },
    "tests": {
        "right": [
            "Skin",
            "skin",
            "Human skin",
            "Integument",
            "Intergument"
        ],
        "prompt": [
            "Epidermis",
            "Dermis",
            "Integumentary system"
        ],
        "wrong": [
            "Hair",
            "Keratin",
            "Melanin",
            "Hypodermis",
            "Sweat glands",
            "Collagen"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
