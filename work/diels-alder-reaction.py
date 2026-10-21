import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

LINE = "<b><u>Diels–Alder</u></b> reaction (accept <u>Diels–Alder</u> cycloaddition or <u>diene synthesis</u>; prompt on <u>cycloaddition</u>, [4+2] <u>cycloaddition</u>, or <u>pericyclic</u> reaction)"

data = {
    "id": "diels-alder-reaction",
    "name": "Diels–Alder reaction",
    "mono": "DA",
    "category": "Chemistry",
    "qbCategory": "Science · Chemistry",
    "kicker": "Diene plus dienophile makes a ring · Won the 1950 Nobel Prize in Chemistry",
    "dates": "First described 1928; Nobel Prize 1950",
    "briefing": "The Diels–Alder reaction snaps two molecules together into a six-membered ring in a single step. One partner, the diene, has two double bonds; the other, the dienophile, usually has one. German chemists Otto Diels and his former student Kurt Alder first described it in 1928 and shared the 1950 Nobel Prize in Chemistry, and chemists still use it to build complicated molecules, from medicines to plastics.",
    "answerHtml": LINE,
    "accept": [
        "diels alder reaction",
        "diels alder reactions",
        "diels alder",
        "diels alder cycloaddition",
        "diels alder cycloadditions",
        "diels alder synthesis",
        "diels alder addition",
        "diene synthesis"
    ],
    "prompt": [
        "cycloaddition",
        "cycloadditions",
        "cycloaddition reaction",
        "4 2 cycloaddition",
        "4 2",
        "pericyclic reaction",
        "pericyclic",
        "diels",
        "alder",
        "otto diels",
        "kurt alder"
    ],
    "reject": [
        "retro diels alder",
        "retro diels alder reaction",
        "alder ene reaction",
        "alder ene",
        "ene reaction",
        "aldol reaction",
        "aldol condensation",
        "aldol addition",
        "aldol",
        "grignard reaction",
        "wittig reaction",
        "friedel crafts reaction",
        "friedel crafts",
        "claisen rearrangement",
        "claisen condensation",
        "cope rearrangement",
        "michael addition",
        "robinson annulation",
        "electrocyclic reaction",
        "sigmatropic rearrangement",
        "1 3 dipolar cycloaddition",
        "huisgen cycloaddition",
        "2 2 cycloaddition",
        "electrophilic addition",
        "nucleophilic substitution",
        "sn2",
        "sn1",
        "e2",
        "elimination",
        "polymerization",
        "hydrogenation",
        "ozonolysis",
        "esterification",
        "dienophile",
        "dienophiles",
        "cyclohexene",
        "cyclohexane",
        "butadiene",
        "maleic anhydride",
        "cyclopentadiene",
        "benzene",
        "alkene",
        "alkenes",
        "woodward hoffmann rules",
        "woodward hoffmann",
        "endo rule",
        "molecular orbital theory"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Diels%E2%80%93Alder_reaction",
    "qb": {"q": "Diels-Alder", "found": 0, "tip": TIP},
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        {
            "p": "The insecticides aldrin and dieldrin, both made using this reaction and later banned in many countries, were named after the two chemists who discovered it. This reaction makes two new carbon–carbon single bonds in one step.",
            "r": "For 10 points, name this reaction in which a diene and a dienophile join to form a six-membered ring."
        },
        {
            "p": "Kenichi Fukui [“foo-KOO-ee”] and Roald Hoffmann shared the 1981 Nobel Prize in Chemistry partly for explaining how reactions like this one take place. Fukui’s frontier orbital theory says this reaction depends on the highest occupied orbital of one reactant overlapping the lowest unoccupied orbital of the other.",
            "r": "For 10 points, name this reaction in which a diene and a dienophile join to form a six-membered ring."
        },
        {
            "p": "The Woodward–Hoffmann rules use orbital symmetry to show that this reaction is “thermally allowed,” so heat alone can make it go. The same rules explain why joining two alkenes into a four-membered ring needs light instead of heat.",
            "r": "This reaction’s namesakes won the 1950 Nobel Prize. For 10 points, name this [4+2] cycloaddition between a diene and a dienophile."
        },
        {
            "p": "Bottles of cyclopentadiene [“sy-kloh-pen-tuh-DY-een”] slowly turn into dicyclopentadiene at room temperature, because the compound undergoes this reaction with itself. Chemists get fresh cyclopentadiene back by heating the dimer, which runs this reaction in reverse.",
            "r": "For 10 points, name this reaction in which a diene and a dienophile combine to make a six-membered ring."
        },
        {
            "p": "This reaction was first described in 1928 by a chemistry professor at the University of Kiel [“KEEL”] and his former doctoral student. The professor had earlier discovered carbon suboxide, a gas with the formula C₃O₂.",
            "r": "Those German chemists shared the 1950 Nobel Prize for it. For 10 points, name this reaction between a diene and a dienophile."
        },
        {
            "p": "In a common college teaching lab, anthracene is heated with maleic anhydride, a very reactive partner for this reaction, to make a new ring bridging the middle of anthracene. Maleic anhydride works well because its carbonyl groups pull electrons away from its double bond.",
            "r": "It forms a six-membered ring in one step. For 10 points, name this cycloaddition between a diene and a dienophile."
        },
        {
            "p": "For this reaction to work, its four-carbon partner must twist into an s-cis shape, with both of its double bonds on the same side of the single bond that joins them. Molecules locked into the opposite, s-trans shape cannot react this way.",
            "r": "For 10 points, name this reaction between a diene and a dienophile that makes cyclohexene rings."
        },
        {
            "p": "When a cyclic partner reacts this way, the “endo” product, with the two-carbon partner’s groups tucked under the four-carbon partner, usually forms faster than the “exo” product. This reaction is stereospecific, so groups that start out cis on the two-carbon partner stay cis in the product.",
            "r": "For 10 points, name this reaction in which a diene and a dienophile form a six-membered ring."
        },
        {
            "p": "In “hetero” versions of this reaction, an atom other than carbon, such as oxygen or nitrogen, becomes part of the new ring. Lewis acids such as aluminum chloride can speed up this reaction by pulling electrons away from one of the partners.",
            "r": "It joins a diene and a dienophile. For 10 points, name this [4+2] cycloaddition, named for two Nobel-winning German chemists."
        },
        {
            "p": "If the two-carbon partner in this reaction is an alkyne instead of an alkene, the product ring keeps two double bonds and is called a cyclohexadiene [“sy-kloh-hex-uh-DY-een”]. With an ordinary alkene partner, the ring keeps just one double bond.",
            "r": "For 10 points, name this reaction, in which a diene and a dienophile join to make a cyclohexene ring."
        },
        {
            "p": "In one step, this reaction breaks three pi bonds and forms two new sigma bonds and one new pi bond, with no intermediate along the way. Because all of those bonds change at the same time, chemists call it a concerted reaction.",
            "r": "For 10 points, name this reaction that combines a diene and a dienophile into a six-membered ring."
        },
        {
            "p": "When the four-carbon and two-carbon parts sit on the same molecule, an intramolecular version of this reaction can build two rings at once. Chemists use such steps to build complex natural products that contain several rings.",
            "r": "For 10 points, name this reaction, in which a diene and a dienophile form a six-membered ring."
        },
        {
            "p": "Some self-healing plastics are held together by links made through this reaction between furan [“FYOOR-an”] and maleimide [“muh-LAY-ih-mide”] groups. Heating such a plastic breaks the links by running this reaction in reverse, and cooling lets them form again, mending cracks.",
            "r": "For 10 points, name this reaction between a diene and a dienophile that forms a six-membered ring."
        },
        {
            "p": "Along with electrocyclic reactions and sigmatropic shifts like the Cope rearrangement, this reaction is a pericyclic reaction, in which electrons flow around a ring of atoms in a single step. Unlike those reactions, this one usually joins two separate molecules into one ring.",
            "r": "For 10 points, name this reaction between a diene and a dienophile, named for two German chemists."
        },
        {
            "p": "The simplest textbook example of this reaction joins two small hydrocarbons, but it is slow and needs high heat and pressure. In its product, the single bond that was in the middle of the four-carbon reactant becomes a double bond.",
            "r": "That example makes cyclohexene from butadiene and ethylene. For 10 points, name this [4+2] cycloaddition, which won a 1950 Nobel Prize."
        }
    ],
    "clues": [
        {
            "id": "diene-dienophile",
            "tier": "giveaway",
            "t": "A diene and a dienophile join to make a six-membered ring",
            "k": ["diene", "dienophile", "six-membered ring"],
            "n": 0,
            "rabbit": "Alkenes"
        },
        {
            "id": "cycloaddition",
            "tier": "giveaway",
            "t": "A [4+2] cycloaddition: a four-carbon partner with two double bonds plus a two-carbon partner",
            "k": ["cycloaddition", "four-carbon", "two-carbon"],
            "n": 0
        },
        {
            "id": "nobel-1950",
            "tier": "giveaway",
            "t": "Its two German namesakes, a professor and his former student, shared the 1950 Nobel Prize in Chemistry",
            "k": ["1950", "nobel prize", "german"],
            "n": 0
        },
        {
            "id": "cyclohexene",
            "tier": "giveaway",
            "t": "Joining butadiene and ethylene this way makes cyclohexene, the simplest textbook example",
            "k": ["butadiene", "ethylene", "cyclohexene"],
            "n": 0
        },
        {
            "id": "concerted",
            "tier": "middle",
            "t": "Concerted: everything happens in one step, with no intermediate",
            "k": ["concerted", "one step", "intermediate"],
            "n": 0
        },
        {
            "id": "bonds",
            "tier": "middle",
            "t": "Breaks three pi bonds and forms two new sigma bonds and one new pi bond; the diene’s middle single bond becomes a double bond",
            "k": ["sigma bonds", "pi bonds", "middle single bond"],
            "n": 0
        },
        {
            "id": "s-cis",
            "tier": "middle",
            "t": "The diene must twist into an s-cis shape, with both double bonds on the same side of the single bond between them",
            "k": ["s-cis", "same side"],
            "n": 0
        },
        {
            "id": "electron-withdrawing",
            "tier": "middle",
            "t": "Dienophiles with electron-withdrawing groups, such as the carbonyl groups of maleic anhydride, react fastest",
            "k": ["electron-withdrawing", "maleic anhydride", "carbonyl"],
            "n": 0
        },
        {
            "id": "pericyclic",
            "tier": "middle",
            "t": "A pericyclic reaction, like electrocyclic reactions and sigmatropic shifts such as the Cope rearrangement",
            "k": ["pericyclic", "cope rearrangement", "electrocyclic"],
            "n": 0
        },
        {
            "id": "endo-stereospecific",
            "tier": "middle",
            "t": "Stereospecific (cis groups on the dienophile stay cis); the endo product usually forms faster than the exo product",
            "k": ["stereospecific", "endo", "exo"],
            "n": 0
        },
        {
            "id": "alkyne",
            "tier": "middle",
            "t": "An alkyne partner gives a ring with two double bonds, a cyclohexadiene",
            "k": ["alkyne", "cyclohexadiene"],
            "n": 0
        },
        {
            "id": "cyclopentadiene",
            "tier": "middle",
            "t": "Cyclopentadiene reacts with itself this way to form dicyclopentadiene; heating the dimer runs it in reverse",
            "k": ["cyclopentadiene", "dicyclopentadiene", "reverse"],
            "n": 0
        },
        {
            "id": "aldrin-dieldrin",
            "tier": "power",
            "t": "The insecticides aldrin and dieldrin, made using it and later banned in many countries, were named for its discoverers",
            "k": ["aldrin", "dieldrin", "insecticides"],
            "n": 0
        },
        {
            "id": "fukui-hoffmann",
            "tier": "power",
            "t": "Kenichi Fukui and Roald Hoffmann shared the 1981 Nobel Prize in Chemistry partly for explaining reactions like it",
            "k": ["fukui", "roald hoffmann", "1981"],
            "n": 0
        },
        {
            "id": "frontier-orbitals",
            "tier": "power",
            "t": "Frontier orbitals: the highest occupied orbital of one reactant overlaps the lowest unoccupied orbital of the other",
            "k": ["frontier", "highest occupied", "lowest unoccupied"],
            "n": 0,
            "rabbit": "Molecular orbital theory"
        },
        {
            "id": "woodward-hoffmann",
            "tier": "power",
            "t": "The Woodward–Hoffmann rules show it is “thermally allowed”; joining two alkenes into a four-membered ring needs light instead",
            "k": ["woodward", "thermally allowed", "four-membered"],
            "n": 0
        },
        {
            "id": "kiel-1928",
            "tier": "power",
            "t": "First described in 1928 at the University of Kiel by a professor and his former doctoral student",
            "k": ["1928", "kiel", "doctoral student"],
            "n": 0
        },
        {
            "id": "carbon-suboxide",
            "tier": "power",
            "t": "The professor who shared in its discovery had earlier discovered carbon suboxide, C₃O₂",
            "k": ["carbon suboxide", "professor"],
            "n": 0
        },
        {
            "id": "anthracene",
            "tier": "power",
            "t": "A common teaching lab heats anthracene with maleic anhydride, making a new ring across anthracene’s middle",
            "k": ["anthracene", "teaching lab"],
            "n": 0
        },
        {
            "id": "hetero",
            "tier": "power",
            "t": "In “hetero” versions, an atom such as oxygen or nitrogen becomes part of the new ring; Lewis acids like aluminum chloride speed it up",
            "k": ["hetero", "lewis acids", "aluminum chloride"],
            "n": 0
        },
        {
            "id": "intramolecular",
            "tier": "power",
            "t": "An intramolecular version, with both partners on one molecule, can build two rings at once",
            "k": ["intramolecular", "two rings"],
            "n": 0
        },
        {
            "id": "self-healing",
            "tier": "power",
            "t": "Some self-healing plastics use it between furan and maleimide groups: heat breaks the links, and cooling re-forms them",
            "k": ["self-healing", "furan", "maleimide"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Name the whole reaction",
        "body": "Tossups on this reaction are full of its parts, so players blurt “diene,” “dienophile,” or “cyclohexene,” which are reactants or products, not the reaction. Saying only “cycloaddition” or “[4+2] cycloaddition” earns a prompt, and the Alder–ene reaction, named for just one of the two chemists, is a different answer. The similar-sounding aldol reaction is unrelated.",
        "fix": "When you hear a four-carbon partner with two double bonds, a dienophile, s-cis, endo, or a new six-membered ring made in one step, say “Diels–Alder.” If you are prompted after “cycloaddition,” add the two names. Two carbonyl compounds joining through an enolate mean the aldol reaction instead.",
        "line": "Real answer line: " + LINE
    },
    "tests": {
        "right": [
            "Diels-Alder reaction",
            "Diels–Alder",
            "diels alder cycloaddition",
            "Deils-Alder reaction",
            "the Diels-Alder reaction"
        ],
        "prompt": [
            "Cycloaddition",
            "[4+2] cycloaddition",
            "Pericyclic reaction"
        ],
        "wrong": [
            "Aldol reaction",
            "Retro-Diels-Alder reaction",
            "Grignard reaction",
            "Alder-ene reaction",
            "Dienophile",
            "Wittig reaction",
            "Friedel-Crafts reaction",
            "Electrophilic addition"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
