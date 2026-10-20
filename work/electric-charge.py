import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."


def C(cid, tier, t, k, rabbit=None):
    d = {"id": cid, "tier": tier, "t": t, "k": k, "n": 0}
    if rabbit:
        d["rabbit"] = rabbit
    return d


LINE = "<b><u>electric charge</u></b> (accept <u>charge</u>; prompt on <u>q</u>; do not accept “electric current” or “elementary charge”)"

data = {
    "id": "electric-charge",
    "name": "Electric charge",
    "mono": "Q",
    "category": "Physics",
    "qbCategory": "Science · Physics",
    "kicker": "Positive or negative property of matter · Measured in coulombs",
    "dates": "Two kinds named positive and negative by Franklin, 1740s",
    "briefing": "Electric charge is a basic property of matter that comes in two kinds, positive and negative, names chosen by Benjamin Franklin. Like charges repel and opposite charges attract, which is why a balloon rubbed on your hair can stick to a wall. Charge is measured in coulombs, and every proton and electron carries the same tiny amount, about 1.6 × 10⁻¹⁹ coulombs: positive for the proton, negative for the electron.",
    "answerHtml": LINE,
    "accept": [
        "electric charge",
        "electric charges",
        "electrical charge",
        "electrical charges",
        "charge",
        "charges",
        "net charge",
        "electrostatic charge"
    ],
    "prompt": [
        "q"
    ],
    "reject": [
        "electric current",
        "current",
        "electric field",
        "electric force",
        "electrostatic force",
        "electric potential",
        "voltage",
        "electric flux",
        "coulomb",
        "coulombs",
        "coulombs law",
        "elementary charge",
        "electron charge",
        "charge of an electron",
        "charge of the electron",
        "electrons",
        "electron",
        "protons",
        "proton",
        "ions",
        "ion",
        "static electricity",
        "electricity",
        "capacitance",
        "color charge",
        "colour charge",
        "effective nuclear charge",
        "nuclear charge",
        "formal charge",
        "magnetic charge",
        "charge of the light brigade",
        "light brigade",
        "electronegativity"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Electric_charge",
    "qb": {"q": "charge", "found": 0, "tip": TIP},
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        {
            "p": "In 1733, Charles du Fay [“dew FAY”] described two kinds of this property, calling one “vitreous” because it came from rubbed glass and the other “resinous” because it came from rubbed amber and other resins. Benjamin Franklin later gave those two kinds new names.",
            "r": "Like kinds repel and opposite kinds attract. For 10 points, name this property, measured in coulombs, that comes in positive and negative forms."
        },
        {
            "p": "Quarks carry fractions of this property, such as plus two-thirds or minus one-third of a proton’s amount, but they are never found alone. In a neutral atom, the positive amount of this property on the protons exactly balances the negative amount on the electrons.",
            "r": "Opposite kinds of it attract. For 10 points, name this property, measured in coulombs."
        },
        {
            "p": "The Faraday constant, about 96,485 coulombs per mole, is the total amount of this property carried by a mole of electrons. Gauss’s law says the electric flux through any closed surface equals the amount of this property inside, divided by the permittivity of free space.",
            "r": "It is measured in coulombs. For 10 points, name this property of matter that comes in positive and negative kinds."
        },
        {
            "p": "In 1785, Charles-Augustin de Coulomb [“KOO-lohm”] used a torsion balance to show that the force between two small objects carrying this property falls off with the square of the distance between them. That force is proportional to the product of the two amounts of this property.",
            "r": "Its SI unit is named for Coulomb. For 10 points, name this property, which can be positive or negative."
        },
        {
            "p": "Benjamin Franklin pictured electricity as a single fluid, calling an object with too much of that fluid positive and an object with too little negative. In an isolated system, the total amount of this property never changes, because it is conserved.",
            "r": "Objects with the same kind of it repel each other. For 10 points, name this property, measured in coulombs."
        },
        {
            "p": "Thales [“THAY-leez”] of Miletus is said to have noticed that amber rubbed with fur attracts bits of straw, and William Gilbert later named “electric” effects after the Greek word for amber. Amber rubbed that way picks up a negative amount of this property.",
            "r": "For 10 points, name this property of matter, measured in coulombs, that comes in positive and negative kinds."
        },
        {
            "p": "Bringing a rubbed plastic rod near a metal sphere, without touching it, pulls the opposite kind of this property toward the near side, a process called induction. In a gold-leaf electroscope, two thin strips of gold spread apart when they carry the same kind of this property.",
            "r": "It is measured in coulombs. For 10 points, name this property that protons and electrons carry in equal and opposite amounts."
        },
        {
            "p": "Robert Millikan won the 1923 Nobel Prize in Physics partly for measuring the smallest free amount of this property, about 1.6 times ten to the negative nineteenth coulombs. He found it by balancing tiny oil drops in an electric field between two metal plates.",
            "r": "For 10 points, name this property that protons carry in a positive form and electrons in a negative form."
        },
        {
            "p": "This property is quantized, meaning that every free particle or object carries a whole-number multiple of the amount on one proton. An atom becomes an ion when it gains or loses electrons and ends up with a net amount of this property.",
            "r": "For 10 points, name this property, measured in coulombs, which comes in positive and negative kinds."
        },
        {
            "p": "Electric current is the rate at which this property flows, so one ampere equals one coulomb of it passing a point each second. Lightning strikes when huge amounts of this property built up in a storm cloud jump to the ground or to another cloud.",
            "r": "Like kinds of it repel. For 10 points, name this property of matter, measured in coulombs."
        },
        {
            "p": "Any extra amount of this property placed on a metal object spreads out over the object’s outer surface. A Van de Graaff [“van duh GRAHF”] generator piles up so much of this property on its metal dome that it can make a person’s hair stand on end.",
            "r": "For 10 points, name this property, measured in coulombs, that makes objects with the same kind repel."
        },
        {
            "p": "The triboelectric [“TRY-boh-ih-LEK-trik”] series ranks materials by whether they tend to gain or lose electrons when rubbed together, which decides what kind of this property each one ends up with. Rubbing a balloon on your hair builds up a static amount of this property on the balloon.",
            "r": "For 10 points, name this property, measured in coulombs, that can be positive or negative."
        },
        {
            "p": "In 1897, J. J. Thomson measured the ratio of this property to mass for the particles in cathode rays, which turned out to be electrons. In 1932, James Chadwick discovered a particle in the nucleus that has none of this property.",
            "r": "For 10 points, name this property, which is positive for protons and negative for electrons."
        },
        {
            "p": "Benjamin Franklin’s famous 1752 kite experiment is said to have drawn this property from a storm cloud down a wet string to a metal key, where Franklin stored it in a Leyden jar. Franklin also gave the names “positive” and “negative” to the two kinds of this property.",
            "r": "Its SI unit is the coulomb. For 10 points, name this property, whose opposite kinds attract each other."
        },
        {
            "p": "A capacitor’s capacitance equals the amount of this property stored on one plate divided by the voltage across the plates. An electric field is defined as the force on a small test object divided by the amount of this property it carries.",
            "r": "Protons carry a positive amount of it. For 10 points, name this property, symbolized q and measured in coulombs."
        }
    ],
    "clues": [
        C("two-kinds", "giveaway", "Comes in two kinds, positive and negative: protons carry the positive kind and electrons the negative kind", ["positive and negative", "protons", "electrons"]),
        C("like-repel", "giveaway", "Like kinds repel each other and opposite kinds attract", ["repel", "attract"]),
        C("coulombs", "giveaway", "Measured in coulombs, named for Charles-Augustin de Coulomb; symbolized q or Q", ["coulombs", "coulomb"]),
        C("balloon", "giveaway", "Rubbing a balloon on your hair moves electrons and leaves a static amount on the balloon, so it can stick to a wall", ["balloon", "static"]),
        C("lightning", "giveaway", "Lightning happens when huge amounts built up in a storm cloud jump to the ground or to another cloud", ["lightning", "storm cloud"]),
        C("franklin-names", "middle", "Benjamin Franklin named its two kinds “positive” and “negative”", ["franklin", "positive", "negative"], "Benjamin Franklin"),
        C("conserved", "middle", "Conserved: the total amount in an isolated system never changes", ["conserved", "isolated system"]),
        C("quantized", "middle", "Quantized: every free object carries a whole-number multiple of the amount on one proton", ["quantized", "whole-number multiple"]),
        C("millikan", "middle", "Robert Millikan balanced tiny oil drops between metal plates to measure its smallest free amount, about 1.6 × 10⁻¹⁹ coulombs", ["millikan", "oil drops"], "Millikan oil drop experiment"),
        C("coulombs-law", "middle", "Coulomb’s law: the force between two small objects is proportional to the product of their amounts and falls off with the square of the distance", ["coulomb’s law", "square of the distance"], "Coulomb’s law"),
        C("current", "middle", "Electric current is its rate of flow: one ampere is one coulomb passing a point each second", ["electric current", "rate of flow", "ampere"], "Electric current"),
        C("ion", "middle", "An atom that gains or loses electrons ends up with a net amount and is called an ion", ["gains or loses", "ion"]),
        C("neutral-atom", "middle", "In a neutral atom, the protons’ positive amount exactly balances the electrons’ negative amount", ["neutral atom", "balances"]),
        C("electroscope", "middle", "A gold-leaf electroscope detects it: the two thin gold leaves spread apart when they carry the same kind", ["electroscope", "gold leaves"]),
        C("neutron", "middle", "Neutrons, discovered by James Chadwick in 1932, have none", ["neutrons", "chadwick", "1932"], "Neutrons"),
        C("field-definition", "middle", "An electric field is the force on a small test object divided by the amount it carries", ["electric field", "test object"], "Electric field"),
        C("du-fay", "power", "Charles du Fay (1733) called its two kinds “vitreous” (from rubbed glass) and “resinous” (from rubbed amber and other resins)", ["du fay", "vitreous", "resinous"]),
        C("single-fluid", "power", "Franklin pictured electricity as a single fluid: too much made an object positive, and too little made it negative", ["single fluid", "too much", "too little"]),
        C("quarks", "power", "Quarks carry fractions of the basic amount, such as plus two-thirds or minus one-third, but are never found alone", ["quarks", "two-thirds", "one-third"], "Quarks"),
        C("millikan-nobel", "power", "Millikan won the 1923 Nobel Prize in Physics partly for measuring its smallest free amount", ["1923", "nobel prize"]),
        C("faraday-constant", "power", "The Faraday constant, about 96,485 coulombs per mole, is the amount carried by a mole of electrons", ["faraday constant", "96,485", "mole"], "Michael Faraday"),
        C("gauss", "power", "Gauss’s law: the electric flux through a closed surface equals the amount inside divided by the permittivity of free space", ["gauss’s law", "electric flux"], "Gauss’s law"),
        C("torsion", "power", "Coulomb measured the forces between small objects carrying it with a torsion balance in 1785", ["torsion balance", "1785"]),
        C("thales-gilbert", "power", "Thales of Miletus is said to have seen rubbed amber attract straw; William Gilbert named “electric” effects after the Greek word for amber", ["thales", "amber", "gilbert"]),
        C("induction", "power", "Induction: a rubbed rod held near a metal sphere, without touching, pulls the opposite kind toward the near side", ["induction", "without touching"]),
        C("outer-surface", "power", "Extra amounts placed on a metal object spread out over its outer surface", ["outer surface", "metal object"]),
        C("van-de-graaff", "power", "A Van de Graaff generator piles up so much on its metal dome that it can make a person’s hair stand on end", ["van de graaff", "dome", "hair"]),
        C("triboelectric", "power", "The triboelectric series ranks materials by whether they gain or lose electrons when rubbed together; amber rubbed with fur becomes negative", ["triboelectric series", "rubbed"]),
        C("thomson", "power", "J. J. Thomson (1897) measured its ratio to mass for the particles in cathode rays, which turned out to be electrons", ["thomson", "cathode rays", "1897"], "Electrons"),
        C("kite", "power", "Franklin’s 1752 kite experiment is said to have drawn it from a storm cloud down a wet string to a key and into a Leyden jar", ["kite", "leyden jar", "1752"]),
        C("capacitance", "power", "A capacitor’s capacitance equals the amount stored on one plate divided by the voltage across the plates (C = Q/V)", ["capacitance", "capacitor"], "Capacitors")
    ],
    "trap": {
        "title": "Charge, not current",
        "body": "Electric charge is the stuff itself, measured in coulombs; electric current is how fast it flows, measured in amperes; and voltage is the push that moves it. Tossups about Millikan’s oil drops can also tempt you to say “electrons” or “elementary charge,” but when the giveaway asks for the property that comes in positive and negative kinds, the answer is just charge.",
        "fix": "Coulombs, q, “positive and negative,” “like kinds repel,” conservation, and quantization mean charge. Amperes, ammeters, and I mean current; volts mean voltage. The elementary charge (about 1.6 × 10⁻¹⁹ coulombs) is one specific amount of it, not the property itself.",
        "line": "Real answer line: " + LINE
    },
    "tests": {
        "right": [
            "Electric charge",
            "charge",
            "Electrical charge",
            "Electric chrage",
            "Charges"
        ],
        "prompt": [
            "q"
        ],
        "wrong": [
            "Electric current",
            "Coulombs",
            "Elementary charge",
            "Static electricity",
            "Electrons",
            "The Charge of the Light Brigade",
            "Voltage"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
