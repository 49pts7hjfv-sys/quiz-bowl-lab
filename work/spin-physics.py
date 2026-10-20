import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."


def C(cid, tier, t, k, rabbit=None):
    d = {"id": cid, "tier": tier, "t": t, "k": k, "n": 0}
    if rabbit:
        d["rabbit"] = rabbit
    return d


LINE = "<b><u>spin</u></b> (accept <u>spin angular momentum</u>, <u>intrinsic angular momentum</u>, or <u>spin quantum number</u>; prompt on <u>angular momentum</u>)"

data = {
    "id": "spin-physics",
    "name": "Spin (physics)",
    "mono": "SPN",
    "category": "Physics",
    "qbCategory": "Science · Physics",
    "kicker": "A particle’s built-in angular momentum · Up or down for electrons",
    "dates": "Proposed by Uhlenbeck and Goudsmit, 1925",
    "briefing": "Spin is a built-in amount of angular momentum that electrons, protons, and many other particles carry, as if they were tiny spinning tops, though nothing is actually turning. An electron’s spin can point only “up” or “down,” which makes every electron a tiny magnet, the secret behind permanent magnets and MRI scans. Particles whose spin is a half (like 1/2 or 3/2) are called fermions, and those with whole-number spin are called bosons.",
    "answerHtml": LINE,
    "accept": [
        "spin",
        "spins",
        "spin angular momentum",
        "intrinsic angular momentum",
        "spin quantum number",
        "electron spin",
        "nuclear spin",
        "particle spin",
        "quantum spin",
        "intrinsic spin"
    ],
    "prompt": [
        "angular momentum",
        "angular momenta",
        "quantum number"
    ],
    "reject": [
        "orbital angular momentum",
        "isospin",
        "precession",
        "larmor precession",
        "magnetic moment",
        "magnetic dipole moment",
        "helicity",
        "chirality",
        "parity",
        "charge",
        "electric charge",
        "color charge",
        "strangeness",
        "rotation",
        "angular velocity",
        "torque",
        "spin orbit coupling",
        "spin orbit interaction",
        "spin statistics theorem",
        "pauli exclusion principle",
        "exclusion principle",
        "zeeman effect",
        "stern gerlach experiment",
        "fermion",
        "fermions",
        "boson",
        "bosons",
        "azimuthal quantum number",
        "angular momentum quantum number",
        "principal quantum number",
        "spintronics",
        "ferromagnetism"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Spin_(physics)",
    "qb": {"q": "spin", "found": 0, "tip": TIP},
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        {
            "p": "Ralph Kronig thought of this property early in 1925 but did not publish it after Wolfgang Pauli criticized the idea. Later that year, George Uhlenbeck [“OO-len-bek”] and Samuel Goudsmit [“GOWD-smit”] proposed it to explain why some spectral lines split into close pairs.",
            "r": "For 10 points, name this built-in angular momentum of particles, which for an electron can point only up or down."
        },
        {
            "p": "Hendrik Lorentz objected that if this property came from an electron actually turning, the electron’s surface would have to move faster than light. In 1928, Paul Dirac’s equation for the electron produced this property automatically.",
            "r": "For 10 points, name this quantum property, a built-in angular momentum that equals one-half for electrons."
        },
        {
            "p": "In 1922, Otto Stern and Walther Gerlach [“GAIR-lahk”] fired silver atoms through an uneven magnetic field and saw the beam split into two parts, a result later explained by this property of each atom’s outermost electron. For an electron, this property can take only two values.",
            "r": "For 10 points, name this built-in angular momentum of particles, often described as “up” or “down.”"
        },
        {
            "p": "Wolfgang Pauli proved in 1940 that this property decides whether a particle obeys his exclusion principle. Particles with half-integer values of this property, such as electrons, are called fermions, while those with whole-number values, such as photons, are called bosons.",
            "r": "For 10 points, name this built-in angular momentum carried by particles such as electrons and protons."
        },
        {
            "p": "A particle with a value of one-half for this property must be rotated a full 720 degrees, not just 360, before its wavefunction returns to exactly its original value. Electrons have that value of this property, which makes each electron act like a tiny magnet.",
            "r": "For 10 points, name this quantum property, a particle’s built-in angular momentum, which is up or down for an electron."
        },
        {
            "p": "Albert Fert and Peter Grünberg [“GROON-bairk”] won the 2007 Nobel Prize in Physics for discovering giant magnetoresistance, which depends on this property of electrons and let hard drives store far more data. In iron magnets, this property of many unpaired electrons lines up in small regions called domains.",
            "r": "For 10 points, name this built-in angular momentum of particles, which for an electron is one-half."
        },
        {
            "p": "Chemists identify molecules with NMR spectroscopy, which detects atomic nuclei that have this property. MRI scanners line up this property of hydrogen nuclei in the body with a powerful magnet, then flip it with pulses of radio waves.",
            "r": "For 10 points, name this built-in angular momentum of particles such as protons and electrons."
        },
        {
            "p": "Hydrogen atoms in space give off radio waves 21 centimeters long when the electron flips this property to point the opposite way from the proton’s. Astronomers use that 21-centimeter line to map the spiral arms of the Milky Way.",
            "r": "For 10 points, name this quantum property, a built-in angular momentum that makes particles act like tiny magnets."
        },
        {
            "p": "Atoms of helium-4 have a total of zero for this property, so they act as bosons, which lets liquid helium-4 flow without any friction as a superfluid at very low temperatures. Atoms of helium-3 have a total of one-half and act as fermions instead.",
            "r": "For 10 points, name this property, a particle’s built-in angular momentum, that is up or down for an electron."
        },
        {
            "p": "This property explained the “anomalous” Zeeman effect, in which spectral lines split into unexpected patterns in a magnetic field. It is described by the fourth quantum number, which is either plus one-half or minus one-half.",
            "r": "For 10 points, name this property, a particle’s built-in angular momentum, which makes each electron act like a tiny magnet."
        },
        {
            "p": "Wolfgang Pauli described this property for electrons using three two-by-two matrices now named for him. The Pauli exclusion principle says that two electrons sharing an orbital must have opposite values of this property.",
            "r": "For 10 points, name this quantum property, which can be “up” or “down” for an electron."
        },
        {
            "p": "The hypothetical graviton would have a value of two for this property, and the Higgs boson is the only known elementary particle with a value of zero. Photons and gluons each have a value of one for this property.",
            "r": "For 10 points, name this property, a built-in angular momentum that is one-half for electrons."
        },
        {
            "p": "This property is measured in units of h-bar, which is Planck’s constant divided by two pi, and an electron carries exactly one-half of a unit. In orbital diagrams, this property is shown by drawing each electron as an arrow pointing up or down.",
            "r": "For 10 points, name this built-in angular momentum carried by electrons, protons, and neutrons."
        },
        {
            "p": "In the Einstein–de Haas effect, magnetizing a hanging iron cylinder makes it start to rotate, because lining up its electrons’ magnetism also lines up this property, and the total angular momentum must stay the same. Particles called fermions have half-integer values of this property.",
            "r": "For 10 points, name this built-in angular momentum of particles, which is up or down for an electron."
        },
        {
            "p": "Liquid oxygen clings between the poles of a strong magnet because each oxygen molecule has two unpaired electrons with matching values of this property. Hund’s rule says that electrons fill orbitals of equal energy one at a time, all with the same value of this property, before any of them pair up.",
            "r": "For 10 points, name this quantum property, a built-in angular momentum that is “up” or “down” for an electron."
        }
    ],
    "clues": [
        C("built-in", "giveaway", "A particle’s own built-in angular momentum, carried by electrons, protons, and neutrons even though nothing is actually rotating", ["built-in", "angular momentum", "rotating"], "Angular momentum"),
        C("up-down", "giveaway", "For an electron it equals one-half and can point only “up” or “down”", ["one-half", "up", "down"], "Electrons"),
        C("fermion-boson", "giveaway", "Particles with half-integer values are fermions (like electrons); particles with whole-number values are bosons (like photons)", ["fermions", "bosons", "half-integer"], "Enrico Fermi"),
        C("mri", "giveaway", "MRI scanners line up this property of hydrogen nuclei with a strong magnet and flip it with radio waves to make images", ["mri", "hydrogen nuclei", "radio waves"], "Protons"),
        C("stern-gerlach", "middle", "Stern–Gerlach experiment (1922): a beam of silver atoms split in two in an uneven magnetic field, later explained by this property", ["stern–gerlach", "silver atoms", "1922"]),
        C("uhlenbeck-goudsmit", "middle", "Proposed in 1925 by George Uhlenbeck and Samuel Goudsmit to explain spectral lines that split into close pairs", ["uhlenbeck", "goudsmit", "1925"]),
        C("pauli", "middle", "Pauli exclusion principle: two electrons sharing an orbital must have opposite values", ["pauli exclusion principle", "opposite values", "orbital"], "Pauli exclusion principle"),
        C("fourth-number", "middle", "Described by the fourth quantum number, which is either plus one-half or minus one-half", ["fourth quantum number", "plus one-half"]),
        C("tiny-magnet", "middle", "Makes each electron act like a tiny magnet; in iron, the values of many unpaired electrons line up in regions called domains", ["tiny magnet", "domains", "unpaired"], "Ferromagnetism"),
        C("force-carriers", "middle", "Photons and gluons have a value of one; the Higgs boson is the only known elementary particle with a value of zero", ["photons", "gluons", "higgs boson"], "Higgs boson"),
        C("hydrogen-line", "middle", "Hydrogen’s 21-centimeter radio line comes from the electron flipping it to point opposite the proton’s; it maps the Milky Way’s spiral arms", ["21-centimeter", "flipping"], "Hydrogen"),
        C("orbital-arrows", "middle", "In orbital diagrams it is shown by drawing each electron as an arrow pointing up or down", ["orbital diagrams", "arrow"], "Atomic orbitals"),
        C("hund", "middle", "Hund’s rule: electrons fill equal-energy orbitals one at a time with matching values before any pair up", ["hund’s rule", "matching values"]),
        C("kronig", "power", "Ralph Kronig thought of it first, early in 1925, but did not publish after Wolfgang Pauli criticized the idea", ["kronig", "criticized"]),
        C("lorentz", "power", "Hendrik Lorentz objected that a literally rotating electron’s surface would have to move faster than light", ["lorentz", "faster than light"]),
        C("dirac", "power", "Paul Dirac’s 1928 equation for the electron produced it automatically", ["dirac", "1928"]),
        C("pauli-1940", "power", "Pauli proved in 1940 that it decides whether a particle obeys his exclusion principle (fermions do; bosons do not)", ["1940", "exclusion principle"]),
        C("seven-twenty", "power", "A particle with a value of one-half must be rotated 720 degrees, not 360, before its wavefunction returns to its original value", ["720 degrees", "rotated"]),
        C("gmr", "power", "Giant magnetoresistance, which depends on it and let hard drives store far more data, won Albert Fert and Peter Grünberg the 2007 Nobel Prize", ["giant magnetoresistance", "hard drives", "2007"]),
        C("pauli-matrices", "power", "Wolfgang Pauli described it for electrons using three two-by-two matrices, now called the Pauli matrices", ["pauli matrices", "two-by-two"]),
        C("helium", "power", "Helium-4 atoms have a total of zero and act as bosons, so liquid helium-4 can flow without friction as a superfluid; helium-3 atoms are fermions", ["helium-4", "superfluid", "helium-3"]),
        C("anomalous-zeeman", "power", "It explained the “anomalous” Zeeman effect, in which spectral lines split into unexpected patterns in a magnetic field", ["anomalous", "zeeman effect"]),
        C("graviton", "power", "The hypothetical graviton would have a value of two", ["graviton", "two"], "Gravity"),
        C("h-bar", "power", "Measured in units of h-bar (Planck’s constant divided by 2π); an electron carries one-half of a unit", ["h-bar", "planck’s constant"], "Max Planck"),
        C("einstein-de-haas", "power", "Einstein–de Haas effect: magnetizing a hanging iron cylinder makes it rotate, because lining up its electrons’ magnetism also lines up this property", ["einstein–de haas", "iron cylinder"]),
        C("oxygen", "power", "Liquid oxygen clings to a strong magnet because each oxygen molecule has two unpaired electrons with matching values", ["liquid oxygen", "unpaired electrons"]),
        C("nmr", "power", "NMR spectroscopy identifies molecules by detecting atomic nuclei that have this property", ["nmr", "nuclei"])
    ],
    "trap": {
        "title": "Spin or angular momentum?",
        "body": "This property is a particle’s built-in angular momentum, so plain “angular momentum” earns only a prompt here, while the angular momentum page does not accept “spin.” An electron also has orbital angular momentum from moving around the nucleus, which is a different thing, and “magnetic moment” names the tiny magnet that this property creates. Stern–Gerlach and Pauli exclusion clues can also lure a wrong buzz of “electrons” when the question asks for the property.",
        "fix": "Up or down, one-half, fermions and bosons, Uhlenbeck and Goudsmit, the Stern–Gerlach split, MRI, and the 21-centimeter line mean spin. If the giveaway asks for “these particles,” say electrons; if it asks for the rule that two electrons in one orbital must be opposite, say the Pauli exclusion principle.",
        "line": "Real answer line: " + LINE
    },
    "tests": {
        "right": [
            "Spin",
            "spin",
            "Electron spin",
            "Spin angular momentum",
            "Intrinsic angular momentun",
            "Spin quantum number"
        ],
        "prompt": [
            "Angular momentum"
        ],
        "wrong": [
            "Orbital angular momentum",
            "Isospin",
            "Precession",
            "Magnetic moment",
            "Spin-orbit coupling",
            "Charge"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
