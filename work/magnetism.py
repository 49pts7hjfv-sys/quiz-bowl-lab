import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."


def C(cid, tier, t, k, rabbit=None):
    d = {"id": cid, "tier": tier, "t": t, "k": k, "n": 0}
    if rabbit:
        d["rabbit"] = rabbit
    return d


LINE = "<b><u>magnetism</u></b> (accept <u>magnetic force</u>; prompt on <u>electromagnetism</u> or on a specific kind such as <u>ferromagnetism</u>; do not accept “magnetic field,” “electricity,” or “magnetite”)"

data = {
    "id": "magnetism",
    "name": "Magnetism",
    "mono": "NS",
    "category": "Physics",
    "qbCategory": "Science · Physics",
    "kicker": "The push and pull of north and south poles · Moves compasses and motors",
    "dates": "Earth called a giant magnet by Gilbert, 1600; linked to electricity, 1820",
    "briefing": "Magnetism is the invisible push and pull between north and south poles, the force that snaps a fridge magnet onto the door and turns a compass needle toward the north. Ancient people found it in lodestone, a naturally magnetic rock, and in 1600 William Gilbert argued that Earth itself is a giant magnet. In 1820, Hans Christian Ørsted discovered that electric currents produce magnetism too, a link that led to electric motors, generators, and MRI machines.",
    "answerHtml": LINE,
    "accept": [
        "magnetism",
        "magnetisms",
        "magnetic force",
        "magnetic forces"
    ],
    "prompt": [
        "electromagnetism",
        "electromagnetic force",
        "electromagnetics",
        "electromagnetic interaction",
        "ferromagnetism",
        "ferromagnetic",
        "paramagnetism",
        "paramagnetic",
        "diamagnetism",
        "diamagnetic",
        "magnet",
        "magnets",
        "magnetic"
    ],
    "reject": [
        "magnetic field",
        "magnetic fields",
        "b field",
        "earths magnetic field",
        "geomagnetism",
        "magnetic monopole",
        "magnetic monopoles",
        "monopole",
        "monopoles",
        "magnetite",
        "lodestone",
        "lodestones",
        "electricity",
        "static electricity",
        "electric field",
        "electric charge",
        "electric current",
        "electromagnet",
        "electromagnets",
        "electromagnetic induction",
        "induction",
        "gravity",
        "magnetar",
        "magnetars",
        "magnetosphere",
        "compass",
        "compasses",
        "magnetic resonance imaging",
        "mri",
        "magnetic pole",
        "magnetic poles",
        "magnetic domain",
        "magnetic domains",
        "magnetic flux",
        "magnetic moment",
        "magnetization",
        "tesla",
        "teslas",
        "gauss"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Magnetism",
    "qb": {"q": "magnetism", "found": 0, "tip": TIP},
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        {
            "p": "Aristotle reported that Thales [“THAY-leez”] of Miletus believed lodestone must have a soul, since it could move iron by this force. According to a legend retold by Pliny the Elder, a shepherd named Magnes discovered this force when the iron nails in his shoes stuck to a rock.",
            "r": "This force makes compass needles point north. For 10 points, name this force, which lets lodestone attract iron."
        },
        {
            "p": "In a 1269 letter, the French scholar Petrus Peregrinus described how to find the two poles of a round lodestone and how to build a compass with a pivoting needle. About two centuries earlier, the Chinese scholar Shen Kuo [“shun KWOH”] had described needles that pointed south because of this force.",
            "r": "For 10 points, name this force that turns compass needles and makes iron stick to lodestone."
        },
        {
            "p": "William Gilbert, a physician to Queen Elizabeth I, studied this force with a small lodestone sphere he called a terrella, or “little Earth.” In a 1600 book written in Latin, he concluded that the whole planet behaves like a giant lodestone.",
            "r": "Compass needles point north because Earth has this property. For 10 points, name this force between north and south poles."
        },
        {
            "p": "During a lecture in April 1820, Hans Christian Ørsted [“UR-sted”] noticed a compass needle swing whenever he switched on an electric current in a nearby wire, showing that electricity can produce this force. Soon after, André-Marie Ampère showed that two parallel wires carrying currents attract or repel each other through this force.",
            "r": "Iron, nickel, and cobalt are strongly attracted by it. For 10 points, name this force, which makes compass needles point north."
        },
        {
            "p": "In 1997, Andre Geim used an extremely strong field to float a live frog in midair, because the water in its body is weakly pushed away by this force. That stunt won a humorous Ig Nobel Prize in 2000, and Geim later shared a real Nobel Prize for his work on graphene.",
            "r": "For 10 points, name this force, which also makes compass needles point north and pulls on iron."
        },
        {
            "p": "Pierre Curie found that heating iron above about 770 degrees Celsius makes it lose its strong form of this property, a threshold named for him. Inside iron, tiny regions called domains have their atoms’ tiny poles lined up in one direction, and stroking a steel needle with lodestone lines up those domains.",
            "r": "Iron, nickel, and cobalt are strongly attracted by it. For 10 points, name this force that makes compass needles point north."
        },
        {
            "p": "In 1922, Otto Stern and Walther Gerlach sent a beam of silver atoms through an uneven field of this force and saw it split in two, evidence of a quantum property later called spin. The spin of electrons, more than their orbits, is the main source of this force in materials like iron.",
            "r": "Like poles repel under it. For 10 points, name this force, which makes a compass needle line up north–south."
        },
        {
            "p": "Liquid oxygen clings between the two poles of a strong horseshoe-shaped device, because its molecules are weakly pulled by this force. Bismuth, by contrast, is weakly pushed away by this force more strongly than any other metal is.",
            "r": "Iron, nickel, and cobalt are strongly pulled by it. For 10 points, name this force associated with north and south poles."
        },
        {
            "p": "In 1831, Michael Faraday found that moving a coil of wire near a source of this force, or changing the strength of this force through the coil, produces an electric current. Power-plant generators and electric guitar pickups both depend on that discovery, called induction.",
            "r": "For 10 points, name this force that turns compass needles, which James Clerk Maxwell joined with electricity in a single theory."
        },
        {
            "p": "MRI scanners use superconducting coils cooled by liquid helium to create a field of this force tens of thousands of times stronger than Earth’s, usually 1.5 or 3 teslas. Radio pulses tip the hydrogen nuclei in the body’s water, and the signals they give off as they realign are turned into images.",
            "r": "Like poles repel under it. For 10 points, name this force that holds decorations onto a steel refrigerator door."
        },
        {
            "p": "In 1931, Paul Dirac showed that if even one isolated pole of this force existed anywhere, electric charge would have to come in fixed units, but no such monopole has ever been confirmed. Breaking a compass needle in half only makes two shorter needles, each with its own north and south ends.",
            "r": "For 10 points, name this force, in which like poles repel and opposite poles attract."
        },
        {
            "p": "The strongest permanent sources of this force, used in earbuds and electric-car motors, are made of neodymium, iron, and boron. A rare kind of neutron star, nicknamed for this force, has the most intense fields of it known in the universe.",
            "r": "For 10 points, name this force that makes compass needles swing toward the north."
        },
        {
            "p": "A charged particle moving through a field of this force is pushed sideways, at right angles to its motion, so it curves into a circle or spiral; a right-hand rule gives the direction of that push. Electric motors and loudspeakers turn electrical energy into motion using this force.",
            "r": "Earth itself has this property, which compass needles respond to. For 10 points, name this force between north and south poles."
        },
        {
            "p": "In the 1820s, William Sturgeon wrapped bare wire around a varnished iron horseshoe and found that it could lift several pounds by this force while a current flowed, then let go when the current stopped. Joseph Henry later built far stronger versions of that device using insulated wire wound in many layers.",
            "r": "Scrapyard cranes use such devices to lift cars. For 10 points, name this force that iron feels near lodestone."
        },
        {
            "p": "The north end of a compass needle points toward a spot in the Arctic that is, in physics terms, actually a south pole of this force. Sea turtles, homing pigeons, and some bacteria sense Earth’s field of this force to find their way.",
            "r": "Opposite poles attract under it. For 10 points, name this force produced by lodestone and by electric currents."
        }
    ],
    "clues": [
        C("poles", "giveaway", "Anything that shows it has a north pole and a south pole", ["north pole", "south pole"]),
        C("like-poles", "giveaway", "Like poles repel and opposite poles attract", ["like poles repel", "opposite poles attract"]),
        C("compass", "giveaway", "Makes compass needles line up north–south, because Earth itself has this property", ["compass", "north–south"], "Earth’s magnetic field"),
        C("iron-ncc", "giveaway", "Iron, nickel, and cobalt are strongly attracted by it", ["iron", "nickel", "cobalt"], "Ferromagnetism"),
        C("lodestone", "giveaway", "Lodestone, a natural iron-oxide rock, shows it and was used in the first compasses", ["lodestone", "first compasses"]),
        C("currents", "middle", "Electric currents and other moving charges produce it", ["electric currents", "moving charges"], "Electric current"),
        C("orsted", "middle", "Hans Christian Ørsted (1820) saw an electric current swing a compass needle, linking electricity with this force", ["ørsted", "oersted", "1820"]),
        C("gilbert", "middle", "William Gilbert’s 1600 book _De Magnete_ said Earth acts like a giant lodestone; he modeled it with a sphere called a terrella", ["gilbert", "1600", "terrella"]),
        C("no-monopoles", "middle", "Breaking a compass needle in half makes two smaller needles, each with both poles; no lone pole (monopole) has been confirmed", ["monopole", "both poles"], "Magnetic monopoles"),
        C("domains", "middle", "Materials like iron contain domains, tiny regions whose atoms all point the same way", ["domains"]),
        C("curie", "middle", "Heating iron above its Curie temperature (about 770 °C) destroys its strong form of this property", ["curie temperature", "770"]),
        C("field-lines", "middle", "Iron filings trace its field lines, which run from the north pole to the south pole", ["iron filings", "field lines"], "Magnetic fields"),
        C("motors", "middle", "Electric motors, loudspeakers, and generators all depend on it", ["motors", "loudspeakers", "generators"]),
        C("mri", "middle", "MRI scanners use superconducting coils to make very strong fields of it, usually 1.5 or 3 teslas", ["mri", "teslas", "superconducting"]),
        C("faraday", "middle", "Michael Faraday (1831): moving a coil near a source of it, or changing it, makes an electric current (induction)", ["faraday", "1831", "induction"], "Michael Faraday"),
        C("thales", "power", "Thales of Miletus thought lodestone had a soul because it could move iron (as Aristotle reported)", ["thales", "soul"]),
        C("magnes", "power", "Pliny the Elder retold a legend of a shepherd, Magnes, whose iron shoe nails stuck to a rock; the name traces to Magnesia", ["pliny", "shepherd", "magnesia"]),
        C("shen-kuo", "power", "Shen Kuo’s _Dream Pool Essays_ (1088) described needle compasses in China", ["shen kuo", "dream pool essays", "1088"]),
        C("peregrinus", "power", "Petrus Peregrinus’s 1269 letter explained how to find the poles of a round lodestone and build a pivoting compass", ["peregrinus", "1269"]),
        C("ampere", "power", "André-Marie Ampère (1820) showed that parallel wires carrying currents attract or repel each other", ["ampère", "parallel wires"], "Ampère’s law"),
        C("geim-frog", "power", "Andre Geim floated a live frog in a very strong field in 1997 (Ig Nobel Prize, 2000), since water is weakly pushed away", ["frog", "geim", "ig nobel"]),
        C("oxygen-bismuth", "power", "Liquid oxygen is weakly pulled toward the poles, while bismuth is pushed away more strongly than any other metal", ["liquid oxygen", "bismuth"]),
        C("stern-gerlach", "power", "Stern and Gerlach (1922) split a beam of silver atoms in an uneven field, evidence of electron spin, the main source of it in iron", ["stern", "gerlach", "silver atoms"], "Spin (physics)"),
        C("dirac", "power", "Paul Dirac (1931): one lone pole anywhere would force electric charge to come in fixed units", ["dirac", "1931"]),
        C("neodymium", "power", "The strongest permanent sources of it are neodymium-iron-boron alloys, used in earbuds and electric-car motors", ["neodymium", "boron"]),
        C("magnetars", "power", "A rare kind of neutron star, nicknamed for this force, has the strongest fields of it known in the universe", ["neutron star", "strongest"]),
        C("sturgeon", "power", "William Sturgeon (1820s) wrapped wire around an iron horseshoe to lift weights with a current; Joseph Henry later used insulated wire", ["sturgeon", "joseph henry", "horseshoe"]),
        C("arctic", "power", "The Arctic spot a compass needle’s north end points to is, in physics terms, a south pole of it", ["arctic", "south pole"])
    ],
    "trap": {
        "title": "The force, not the field",
        "body": "Quiz bowl has separate answer lines for magnetism (the force and the whole phenomenon), magnetic fields (the region around a magnet or current, measured in teslas), and Earth’s magnetic field. Ferromagnetism, the strong kind shown by iron, is its own answer too, and electromagnetism covers electricity and magnetism together. On this page “magnetic field” is ruled wrong, while “electromagnetism” or a specific kind like “ferromagnetism” only earns a prompt.",
        "fix": "If the giveaway asks for “this force” or “this phenomenon” behind poles, lodestone, and compasses, say magnetism. If it asks for “this quantity” or “this field,” measured in teslas, say magnetic field; clues about the planet’s own field, its flips, or auroras want Earth’s magnetic field.",
        "line": "Real answer line: " + LINE
    },
    "tests": {
        "right": [
            "Magnetism",
            "magnetism",
            "Magentism",
            "Magnetic force",
            "Magnetic forces"
        ],
        "prompt": [
            "Electromagnetism",
            "Ferromagnetism",
            "Magnets",
            "Magnetic"
        ],
        "wrong": [
            "Magnetic field",
            "Electricity",
            "Magnetic monopoles",
            "Magnetite",
            "Lodestone",
            "Electromagnet",
            "Earth's magnetic field",
            "Gravity",
            "Static electricity"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
