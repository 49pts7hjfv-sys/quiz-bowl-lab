import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."


def C(cid, tier, t, k, rabbit=None):
    d = {"id": cid, "tier": tier, "t": t, "k": k, "n": 0}
    if rabbit:
        d["rabbit"] = rabbit
    return d


LINE = "<b><u>Coulomb’s law</u></b> (accept <u>Coulomb’s inverse-square law</u>; prompt on <u>Coulomb</u>, <u>inverse-square law</u>, or <u>electrostatic force</u>; do not accept “Gauss’s law,” “Ohm’s law,” or “Newton’s law of gravitation”)"

data = {
    "id": "coulombs-law",
    "name": "Coulomb’s law",
    "mono": "CLW",
    "category": "Physics",
    "qbCategory": "Science · Physics",
    "kicker": "The force between two charges · Weakens with distance squared",
    "dates": "Published by Charles-Augustin de Coulomb, 1785",
    "briefing": "Rub a balloon on your hair and it can lift the strands, because electric charges push and pull on each other. Coulomb’s law tells exactly how hard: the force grows with the sizes of the two charges and falls off with the square of the distance between them, so twice as far means one-fourth the force. French engineer Charles-Augustin de Coulomb measured it in 1785 with a delicate twisting-wire instrument called a torsion balance.",
    "answerHtml": LINE,
    "accept": [
        "coulombs law",
        "coulomb law",
        "coulomb s law",
        "coulombs laws",
        "coulombs inverse square law",
        "coulomb inverse square law",
        "coulombs law of electrostatics",
        "coulombs law of electric force",
        "law of coulomb"
    ],
    "prompt": [
        "coulomb",
        "coulombs",
        "charles augustin de coulomb",
        "charles coulomb",
        "charles de coulomb",
        "inverse square law",
        "inverse square",
        "electrostatic force",
        "electric force",
        "coulomb force",
        "coulombic force",
        "coulomb interaction",
        "electrostatics"
    ],
    "reject": [
        "gausss law",
        "gauss law",
        "gausss law for magnetism",
        "ohms law",
        "amperes law",
        "faradays law",
        "lenzs law",
        "biot savart law",
        "kirchhoffs law",
        "kirchhoffs laws",
        "hookes law",
        "newtons law of universal gravitation",
        "newtons law of gravitation",
        "newtons law of gravity",
        "law of universal gravitation",
        "universal gravitation",
        "law of gravity",
        "gravity",
        "newtons third law",
        "electric field",
        "electric charge",
        "electric potential",
        "voltage",
        "coulombs constant",
        "coulomb constant",
        "coulomb barrier",
        "coulomb friction",
        "coulombs law of friction",
        "static electricity",
        "conservation of charge"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Coulomb%27s_law",
    "qb": {"q": "Coulomb", "found": 0, "tip": TIP},
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        {
            "p": "Henry Cavendish appears to have discovered this law in the 1770s, but his results stayed unpublished until James Clerk Maxwell edited his papers about a century later. In 1767, Joseph Priestley had guessed this law by analogy with gravity, reasoning from the fact that a charged hollow metal container exerts no electric force on objects inside it.",
            "r": "It was published by a French engineer in 1785. For 10 points, name this inverse-square law for the force between two electric charges."
        },
        {
            "p": "This law’s discoverer also showed that the poles of magnets attract and repel with a force that weakens with the square of the distance. To establish this law in 1785, he measured how far a thin wire twisted in a torsion balance when two small charged balls pushed each other apart.",
            "r": "For 10 points, name this law stating that the electric force between two charges equals k times the product of the charges divided by the distance squared."
        },
        {
            "p": "The scientist who formulated this law also wrote a prize-winning study of friction, and the simple model of dry friction in which sliding friction does not depend on speed is often named for him. He spent years as a military engineer on the Caribbean island of Martinique.",
            "r": "The SI unit of charge is named for him. For 10 points, name this inverse-square law of electric force."
        },
        {
            "p": "Ernest Rutherford’s formula for alpha particles bouncing off gold nuclei assumed this law, and its match with Hans Geiger and Ernest Marsden’s data supported the idea of a tiny, dense nucleus. In Niels Bohr’s model of hydrogen, this law gives the attraction that keeps the electron in orbit.",
            "r": "Like charges repel under it. For 10 points, name this law describing the electric force between two point charges."
        },
        {
            "p": "Chemists use this law to explain why magnesium oxide, made of ions with charges of plus two and minus two, has a far higher melting point and lattice energy than sodium chloride. Because water weakens the force described by this law about 80 times compared with a vacuum, salt crystals can come apart into ions when they dissolve.",
            "r": "For 10 points, name this law, which says the electric force between charges is proportional to the product of the charges."
        },
        {
            "p": "The constant in this law, about 9 times 10 to the ninth in SI units, equals one divided by four pi times the permittivity of free space. That huge constant means two charges of one SI unit each, held one meter apart, would exert a force of about 9 billion newtons on each other.",
            "r": "For 10 points, name this law for the force between two point charges, written F equals k q one q two over r squared."
        },
        {
            "p": "Between a proton and an electron, the force described by this law is roughly 10 to the 39th power times stronger than the gravitational pull between them. Unlike Newton’s law of universal gravitation, which it closely resembles, this law describes a force that can either attract or repel.",
            "r": "For 10 points, name this inverse-square law of electrostatics, which says like charges repel and opposite charges attract."
        },
        {
            "p": "According to this law, the positively charged protons packed into an atomic nucleus should push one another apart with enormous force; the strong nuclear force overcomes that push at very short range. In stars, protons must get past a barrier set by this law, with help from quantum tunneling, before they can fuse.",
            "r": "For 10 points, name this law stating that the electric force between two charges falls off with the square of the distance."
        },
        {
            "p": "Under this law, moving two charged objects twice as far apart cuts the force between them to one-fourth, while doubling both of their charges makes the force four times as strong. So doubling both charges and the distance at the same time leaves the force unchanged.",
            "r": "For 10 points, name this law for the force between electric charges, which has the same inverse-square form as Newton’s law of gravitation."
        },
        {
            "p": "Applying Gauss’s law to a sphere drawn around a single point charge gives back this law, which is valid for charges at rest. When several charges are present, the principle of superposition says the total force on one charge is the vector sum of the forces this law gives for each of the others.",
            "r": "For 10 points, name this law of electrostatics, which says the force between two charges is inversely proportional to the square of the distance between them."
        },
        {
            "p": "Dividing the force given by this law by the size of a small test charge gives the electric field around a point charge. The force in this law points along the straight line joining the two charges, and by Newton’s third law, each charge feels an equal and opposite push or pull.",
            "r": "For 10 points, name this law, written F equals k q one q two over r squared."
        },
        {
            "p": "Thirteen years before Henry Cavendish used a torsion balance to measure the density of Earth, a French physicist used a similar twisting-wire instrument to establish this law. This law has the same form as Newton’s law of gravitation, with electric charges taking the place of masses.",
            "r": "For 10 points, name this law stating that the force between two charges is proportional to the product of the charges and inversely proportional to the distance squared."
        },
        {
            "p": "Chemists use this law to explain periodic trends: an outer electron that sits closer to a nucleus with a larger effective charge is pulled more strongly, so more energy is needed to remove it. That is why ionization energy generally rises from left to right across a period.",
            "r": "For 10 points, name this law, which says opposite charges attract with a force that grows as they get closer."
        },
        {
            "p": "Photocopiers depend on the force described by this law, which pulls tiny charged toner particles onto oppositely charged areas of a drum. The same force lets electrostatic precipitators in smokestacks pull charged specks of ash out of the air.",
            "r": "For 10 points, name this law stating that the electric force between two charges is proportional to the product of the charges."
        },
        {
            "p": "Outside a uniformly charged sphere, this law works as if all of the sphere’s charge were squeezed into a single point at its center, just as Isaac Newton showed for the gravity of a planet. Inside a charged hollow metal shell, the forces this law predicts from all parts of the shell cancel out.",
            "r": "Like charges repel under it, and opposite charges attract. For 10 points, name this inverse-square law for the force between electric charges."
        }
    ],
    "clues": [
        C("formula", "giveaway", "The force between two charges equals k times the product of the charges divided by the distance squared (F = kq₁q₂/r²)", ["product of the charges", "distance squared"]),
        C("like-repel", "giveaway", "Like charges repel and opposite charges attract", ["like charges repel", "opposite charges attract"], "Electric charge"),
        C("inverse-square", "giveaway", "An inverse-square law: double the distance and the force drops to one-fourth", ["inverse-square", "one-fourth"]),
        C("namesake", "giveaway", "Named for a French military engineer who published it in 1785; the SI unit of charge is named for him too", ["french", "1785", "unit of charge"]),
        C("torsion-1785", "middle", "Established in 1785 with a torsion balance, which measures tiny forces by how far a thin wire twists", ["torsion balance", "twists"]),
        C("gravity-analogy", "middle", "Same form as Newton’s law of universal gravitation, with charges in place of masses, but it can repel as well as attract", ["gravitation", "masses", "repel"], "Gravity"),
        C("constant", "middle", "Its constant k is about 9 × 10⁹ in SI units and equals 1 divided by (4π × the permittivity of free space)", ["permittivity of free space", "constant"]),
        C("doubling", "middle", "Doubling both charges makes the force 4 times as strong; doubling the distance makes it one-fourth as strong", ["doubling", "4 times"]),
        C("nucleus", "middle", "It says the protons in a nucleus should fly apart; the strong nuclear force holds them together", ["protons", "strong nuclear force"]),
        C("bohr", "middle", "Gives the attraction that keeps the electron in orbit in Niels Bohr’s model of hydrogen", ["bohr", "orbit"], "Niels Bohr"),
        C("electric-field", "middle", "Dividing its force by a small test charge gives the electric field around a point charge", ["test charge", "electric field"], "Electric field"),
        C("third-law", "middle", "The force acts along the line joining the charges, and the two charges feel equal and opposite forces", ["line joining", "equal and opposite"]),
        C("superposition", "middle", "With many charges, add the forces from each one as vectors (the principle of superposition)", ["superposition", "vectors"]),
        C("cavendish", "power", "Henry Cavendish found it in the 1770s but never published; James Clerk Maxwell edited his papers about a century later", ["cavendish", "maxwell", "never published"]),
        C("priestley", "power", "Joseph Priestley guessed it in 1767, because a charged hollow metal container exerts no force on objects inside", ["priestley", "1767", "hollow"]),
        C("magnetic-poles", "power", "Its discoverer also showed that magnetic poles attract and repel with an inverse-square force", ["magnetic poles"]),
        C("friction", "power", "Its discoverer, a military engineer who served on Martinique, wrote a prize-winning study of friction; a dry-friction model is named for him", ["friction", "martinique", "military engineer"], "Friction"),
        C("rutherford", "power", "Rutherford’s formula for alpha particles scattering off gold nuclei assumed it, supporting a tiny, dense nucleus", ["rutherford", "alpha particles", "gold"]),
        C("lattice", "power", "Explains why magnesium oxide (ions with charges +2 and −2) has a far higher melting point and lattice energy than sodium chloride", ["magnesium oxide", "lattice energy"], "Lattice energy"),
        C("water-80", "power", "Water weakens the force about 80 times compared with a vacuum, which helps salt crystals dissolve", ["water", "80 times", "dissolve"]),
        C("billion", "power", "Two charges of one SI unit each, held 1 meter apart, would feel a force of about 9 billion newtons", ["9 billion", "newtons"]),
        C("vs-gravity", "power", "Between a proton and an electron, this force is about 10³⁹ times stronger than their gravitational pull", ["stronger", "gravitational pull"]),
        C("fusion-barrier", "power", "In stars, protons must get past the barrier this force creates, with help from quantum tunneling, before they fuse", ["barrier", "quantum tunneling"], "Nuclear fusion"),
        C("gauss-derive", "power", "Gauss’s law applied to a sphere around a point charge gives it back; it holds for charges at rest", ["gauss’s law", "at rest"], "Gauss’s law"),
        C("ionization", "power", "Explains why ionization energy rises across a period: electrons nearer a more highly charged nucleus are pulled harder", ["ionization energy", "period"]),
        C("photocopier", "power", "Photocopiers pull charged toner onto oppositely charged areas of a drum; smokestack precipitators pull out charged ash", ["photocopiers", "toner", "precipitators"]),
        C("shell", "power", "Outside a uniformly charged sphere, it works as if all the charge sat at the center, just like Newton’s gravity", ["charged sphere", "center"])
    ],
    "trap": {
        "title": "Which inverse-square law?",
        "body": "Several laws show up in the same tossups. Coulomb’s law gives the force between two charges; Gauss’s law links the electric flux through a closed surface to the charge inside; Ohm’s law links voltage, current, and resistance. Newton’s law of universal gravitation has exactly the same inverse-square form, so “proportional to the product, inversely proportional to the distance squared” fits both until you hear whether the clue is about charges or masses.",
        "fix": "Charges, k, “like charges repel,” torsion balances, and 1785 mean Coulomb’s law. Masses, G, and planets mean Newton’s law of gravitation; closed surfaces and flux mean Gauss’s law. Saying only “Coulomb” or “inverse-square law” earns a prompt, so be ready to say the whole name.",
        "line": "Real answer line: " + LINE
    },
    "tests": {
        "right": [
            "Coulomb's law",
            "Coulombs law",
            "Coulomb’s Law",
            "Coulomb law",
            "Colomb's law",
            "Coulomb's inverse-square law"
        ],
        "prompt": [
            "Coulomb",
            "Inverse-square law",
            "Electrostatic force",
            "Charles-Augustin de Coulomb"
        ],
        "wrong": [
            "Gauss's law",
            "Ohm's law",
            "Newton's law of universal gravitation",
            "Hooke's law",
            "Ampère's law",
            "Electric field",
            "Coulomb's constant",
            "Electric charge"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
