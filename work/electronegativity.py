import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "electronegativity",
    "name": "Electronegativity",
    "mono": "EN",
    "category": "Chemistry",
    "qbCategory": "Science · Chemistry",
    "kicker": "How hard an atom pulls on shared electrons · Makes bonds polar",
    "dates": "Pauling’s scale introduced 1932",
    "briefing": "Electronegativity measures how hard an atom tugs on the electrons it shares in a chemical bond, like one team in a tug-of-war. Linus Pauling built the first scale for it in 1932, and fluorine tops his chart at nearly 4. When two atoms pull unequally, the shared electrons drift toward the stronger puller, which is why the oxygen end of a water molecule is slightly negative.",
    "answerHtml": "<b><u>Electronegativity</u></b> (do not accept “electron affinity”)",
    "accept": [
        "electronegativity",
        "electronegativities"
    ],
    "prompt": [],
    "reject": [
        "electron affinity",
        "electron affinities",
        "ionization energy",
        "first ionization energy",
        "electropositivity",
        "electron",
        "electrons",
        "polarity",
        "bond polarity",
        "dipole moment",
        "dipole",
        "dipoles",
        "effective nuclear charge",
        "atomic radius",
        "linus pauling",
        "valence electrons",
        "metallic character",
        "oxidation number",
        "oxidation state"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Electronegativity",
    "qb": {
        "q": "electronegativity",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Robert Mulliken defined this quantity as the average of an atom’s first ionization energy and its electron affinity. A different scale for this quantity, created by Allred and Rochow, is based on the pull of the effective nuclear charge felt at an atom’s covalent radius.",
            "r": "Fluorine has the highest value of this quantity. For 10 points, name this measure of how strongly an atom attracts the electrons it shares in a bond."
        },
        {
            "p": "In 1932, a chemist built the first scale for this property by comparing bond dissociation energies, measuring how much stronger a bond between two different atoms is than expected. Values on that scale, named for Linus Pauling, have no units, and the highest is nearly 4.",
            "r": "This property increases from left to right across the periodic table. For 10 points, name this tendency of an atom to pull bonding electrons toward itself."
        },
        {
            "p": "Trifluoroacetic acid is a far stronger acid than acetic acid because of an inductive effect caused by fluorine’s high value of this property. Differences in this property put partial positive and partial negative charges on the two ends of a polar bond.",
            "r": "For 10 points, name this property, measured on a scale by Linus Pauling, that describes how strongly an atom pulls on the electrons it shares."
        },
        {
            "p": "Beryllium and aluminum behave alike partly because they have nearly equal values of this property, an example of the diagonal relationship on the periodic table. Cesium and francium have the lowest values of this property, while noble gases like neon are often left off its scales.",
            "r": "For 10 points, name this property, which is highest for fluorine, that measures an atom’s pull on shared electrons."
        },
        {
            "p": "Leland Allen proposed a scale for this property based on the average energy of an atom’s valence electrons. R. T. Sanderson argued that when atoms join into a molecule, their values of this property even out to a single value, a principle called equalization.",
            "r": "Fluorine’s value of this property on Pauling’s scale is nearly 4. For 10 points, name this measure of how strongly an atom attracts bonding electrons."
        },
        {
            "p": "In the compound cesium auride, gold forms a negative ion, partly because gold has an unusually high value of this property for a metal. When chemists assign oxidation numbers, all of the shared electrons in a bond are counted for the atom with the higher value of this property.",
            "r": "For 10 points, name this property, symbolized by the Greek letter chi [“KYE”], that measures an atom’s attraction for the electrons in a bond."
        },
        {
            "p": "Hydrogen bonds form when hydrogen is attached to nitrogen, oxygen, or fluorine, small atoms with high values of this property. Because oxygen ranks second only to fluorine in this property, the oxygen end of a water molecule carries a partial negative charge.",
            "r": "For 10 points, name this property, which describes how strongly an atom attracts the electrons it shares in a bond."
        },
        {
            "p": "Many chemistry textbooks say that when two atoms differ in this property by more than about 1.7 on Pauling’s scale, the bond between them is ionic. Carbon and hydrogen are close enough in this property that their bonds are considered nearly nonpolar.",
            "r": "For 10 points, name this property that increases across a period and decreases down a group, measuring an atom’s pull on bonding electrons."
        },
        {
            "p": "This property is a central idea of _The Nature of the Chemical Bond_, a book by the scientist who won the 1954 Nobel Prize in Chemistry for his research on chemical bonding. Elements with low values of this property, such as sodium and potassium, are often called electropositive.",
            "r": "That scientist, Linus Pauling, made its best-known scale. For 10 points, name this property, highest for fluorine, that measures how strongly an atom draws shared electrons toward itself."
        },
        {
            "p": "Chlorine releases more energy than fluorine when it gains an electron, yet fluorine beats chlorine in this related property, which deals with electrons shared inside a bond. Robert Mulliken calculated this property by averaging ionization energy and electron affinity.",
            "r": "For 10 points, name this property that Linus Pauling put on a scale on which fluorine has the highest value."
        },
        {
            "p": "The most common modern value of this property for fluorine is 3.98, and the values have no units because they only compare atoms with one another. Oxygen comes second in this property, followed by chlorine and nitrogen.",
            "r": "For 10 points, name this property, which tells how strongly an atom attracts shared electrons and explains why some covalent bonds are polar."
        },
        {
            "p": "The Allred–Rochow scale for this property depends on the effective nuclear charge felt by an atom’s outer electrons. This property generally decreases going down a group, because the outer electrons sit farther from the nucleus and are shielded by inner electrons.",
            "r": "For 10 points, name this property, highest near the upper right of the periodic table at fluorine, that measures an atom’s pull on bonding electrons."
        },
        {
            "p": "Because only differences in this property can be found from bond energies, the chemist who built its best-known scale chose hydrogen as a reference point, and hydrogen’s value on that scale is now listed as 2.20. A very large difference in this property between two atoms, as in sodium chloride, means one atom essentially pulls the electrons away from the other.",
            "r": "The result is an ionic bond. For 10 points, name this property that measures how strongly an atom attracts bonding electrons."
        },
        {
            "p": "Oxygen has a positive oxidation number only in compounds with fluorine, such as oxygen difluoride, because fluorine is the only element with a higher value of this property. Fluorine’s value of this property is so high that it has an oxidation number of negative 1 in all of its compounds.",
            "r": "For 10 points, name this property that increases from left to right across a period, which measures how strongly an atom pulls on shared electrons."
        },
        {
            "p": "Carbon dioxide’s bonds are polar because oxygen beats carbon in this property, but the molecule has no overall dipole moment, since its two oxygen atoms pull equally in opposite directions. This property is often written with the Greek letter chi [“KYE”].",
            "r": "For 10 points, name this property, which is highest for fluorine and lowest near cesium, measuring an atom’s pull on bonding electrons."
        }
    ],
    "clues": [
        {
            "id": "definition",
            "tier": "giveaway",
            "t": "Measures how strongly an atom attracts the shared electrons in a chemical bond toward itself",
            "k": ["shared electrons", "attracts", "chemical bond"],
            "n": 0
        },
        {
            "id": "fluorine-top",
            "tier": "giveaway",
            "t": "Fluorine has the highest value of any element, nearly 4 on the most common scale",
            "k": ["fluorine", "highest value"],
            "n": 0,
            "rabbit": "Fluorine"
        },
        {
            "id": "pauling-scale",
            "tier": "giveaway",
            "t": "Linus Pauling created the first and most widely used scale for it in 1932",
            "k": ["linus pauling", "pauling", "1932"],
            "n": 0,
            "rabbit": "Linus Pauling"
        },
        {
            "id": "trend",
            "tier": "giveaway",
            "t": "Increases from left to right across a period and decreases going down a group",
            "k": ["left to right", "down a group", "period"],
            "n": 0
        },
        {
            "id": "bond-types",
            "tier": "giveaway",
            "t": "The difference between two atoms’ values tells whether a bond is ionic, polar covalent, or nonpolar covalent",
            "k": ["polar covalent", "ionic", "nonpolar", "difference"],
            "n": 0
        },
        {
            "id": "partial-charges",
            "tier": "middle",
            "t": "Unequal pulling gives the two ends of a polar bond partial charges (δ+ and δ−), making a dipole",
            "k": ["partial charges", "dipole", "polar bond"],
            "n": 0,
            "rabbit": "Dipoles"
        },
        {
            "id": "lowest",
            "tier": "middle",
            "t": "Cesium and francium, in the lower left corner of the periodic table, have the lowest values",
            "k": ["cesium", "francium", "lower left"],
            "n": 0
        },
        {
            "id": "runners-up",
            "tier": "middle",
            "t": "Oxygen is second only to fluorine, followed by chlorine and nitrogen",
            "k": ["oxygen", "chlorine", "nitrogen", "second"],
            "n": 0
        },
        {
            "id": "hydrogen-bonds",
            "tier": "middle",
            "t": "Hydrogen bonds form when hydrogen is attached to nitrogen, oxygen, or fluorine, small atoms that pull hard on electrons",
            "k": ["hydrogen bonds", "pull hard"],
            "n": 0,
            "rabbit": "Hydrogen bonds"
        },
        {
            "id": "noble-gases",
            "tier": "middle",
            "t": "Noble gases like helium and neon are often left off the scale because they rarely form bonds",
            "k": ["noble gases", "left off"],
            "n": 0,
            "rabbit": "Noble gases"
        },
        {
            "id": "electropositive",
            "tier": "middle",
            "t": "Elements with low values, such as sodium, potassium, and the other alkali metals, are called electropositive",
            "k": ["electropositive", "alkali metals"],
            "n": 0
        },
        {
            "id": "chi",
            "tier": "middle",
            "t": "Often written with the Greek letter chi (χ); values on Pauling’s scale have no units",
            "k": ["greek letter", "chi", "no units"],
            "n": 0
        },
        {
            "id": "oxidation-numbers",
            "tier": "middle",
            "t": "In assigning oxidation numbers, shared electrons are counted for the atom with the higher value",
            "k": ["oxidation numbers", "higher value"],
            "n": 0
        },
        {
            "id": "ionic-cutoff",
            "tier": "middle",
            "t": "Many textbooks treat a difference of more than about 1.7 on Pauling’s scale as an ionic bond",
            "k": ["textbooks", "1.7", "ionic bond"],
            "n": 0
        },
        {
            "id": "carbon-hydrogen",
            "tier": "middle",
            "t": "Carbon (2.55) and hydrogen (2.20) are so close that C–H bonds are nearly nonpolar",
            "k": ["nearly nonpolar", "carbon", "2.55"],
            "n": 0
        },
        {
            "id": "bond-energies",
            "tier": "power",
            "t": "Pauling based his scale on bond dissociation energies: the extra strength of an A–B bond compared with A–A and B–B bonds",
            "k": ["bond dissociation", "extra strength"],
            "n": 0
        },
        {
            "id": "hydrogen-reference",
            "tier": "power",
            "t": "Pauling used hydrogen as his reference point; its value on his scale is now listed as 2.20",
            "k": ["reference point", "2.20"],
            "n": 0
        },
        {
            "id": "mulliken",
            "tier": "power",
            "t": "Robert Mulliken’s scale averages an atom’s first ionization energy and its electron affinity",
            "k": ["mulliken", "ionization energy", "electron affinity"],
            "n": 0
        },
        {
            "id": "allred-rochow",
            "tier": "power",
            "t": "The Allred–Rochow scale uses the pull of the effective nuclear charge at an atom’s covalent radius",
            "k": ["effective nuclear charge", "allred", "rochow"],
            "n": 0
        },
        {
            "id": "allen",
            "tier": "power",
            "t": "Leland Allen’s scale uses the average energy of an atom’s valence electrons",
            "k": ["leland allen", "valence electrons"],
            "n": 0
        },
        {
            "id": "sanderson",
            "tier": "power",
            "t": "R. T. Sanderson’s principle of equalization: atoms’ values even out when they join into a molecule",
            "k": ["sanderson", "equalization"],
            "n": 0
        },
        {
            "id": "inductive",
            "tier": "power",
            "t": "Inductive effect: fluorine atoms pull so hard that trifluoroacetic acid is far stronger than acetic acid",
            "k": ["inductive effect", "trifluoroacetic"],
            "n": 0,
            "rabbit": "Acetic acid"
        },
        {
            "id": "diagonal",
            "tier": "power",
            "t": "Diagonal relationship: beryllium and aluminum have nearly equal values, so they behave alike",
            "k": ["diagonal relationship", "beryllium", "aluminum"],
            "n": 0
        },
        {
            "id": "auride",
            "tier": "power",
            "t": "Gold’s unusually high value for a metal lets it form negative auride ions in cesium auride",
            "k": ["cesium auride", "auride", "gold"],
            "n": 0
        },
        {
            "id": "nobel",
            "tier": "power",
            "t": "Pauling explained it in _The Nature of the Chemical Bond_ and won the 1954 Nobel Prize in Chemistry",
            "k": ["nature of the chemical bond", "nobel", "1954"],
            "n": 0
        },
        {
            "id": "oxygen-difluoride",
            "tier": "power",
            "t": "Fluorine is always −1 in compounds, and oxygen is positive only when bonded to fluorine, as in oxygen difluoride",
            "k": ["oxygen difluoride", "always"],
            "n": 0
        },
        {
            "id": "chlorine-affinity",
            "tier": "power",
            "t": "Chlorine has a higher electron affinity than fluorine, but fluorine still pulls harder on shared electrons",
            "k": ["electron affinity", "chlorine"],
            "n": 0
        },
        {
            "id": "carbon-dioxide",
            "tier": "power",
            "t": "Carbon dioxide has polar bonds but no overall dipole, because its two oxygen atoms pull equally in opposite directions",
            "k": ["carbon dioxide", "overall dipole"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Not electron affinity!",
        "body": "Electron affinity is the energy change when a single, lone gas atom gains an extra electron; this property is about an atom’s pull on electrons it shares inside a bond. The two follow similar trends across the periodic table, so they are easy to mix up, but they are different answers. In fact, chlorine, not fluorine, has the highest electron affinity of any element. Ionization energy, the energy needed to pull an electron off, is another close cousin.",
        "fix": "Listen for “shared electrons,” “bonds,” “Pauling,” “polar,” or the Greek letter chi: that means this property. “Energy released when an atom gains an electron” means electron affinity, and “energy needed to remove an electron” means ionization energy.",
        "line": "Real answer line: <b><u>Electronegativity</u></b> (do not accept “electron affinity”)"
    },
    "tests": {
        "right": [
            "Electronegativity",
            "electronegativty",
            "Electronegativities",
            "Pauling electronegativity",
            "electro-negativity"
        ],
        "prompt": [],
        "wrong": [
            "Electron affinity",
            "Ionization energy",
            "Electropositivity",
            "Polarity",
            "Electrons",
            "Dipole moment"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
