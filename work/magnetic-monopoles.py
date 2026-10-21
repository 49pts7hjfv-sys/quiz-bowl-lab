import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."


def C(cid, tier, t, k, rabbit=None):
    d = {"id": cid, "tier": tier, "t": t, "k": k, "n": 0}
    if rabbit:
        d["rabbit"] = rabbit
    return d


data = {
    "id": "magnetic-monopoles",
    "name": "Magnetic monopoles",
    "mono": "N",
    "category": "Physics",
    "qbCategory": "Science · Physics",
    "kicker": "Hypothetical lone magnetic poles · Never found, but physics allows them",
    "dates": "Predicted by Paul Dirac, 1931; never confirmed",
    "briefing": "Cut a bar magnet in half and you never get a lone north pole and a lone south pole: you get two smaller magnets, each with both. A magnetic monopole would be a particle with just one magnetic pole, the way an electron carries just one kind of electric charge. In 1931, Paul Dirac showed that even one monopole anywhere in the universe would explain why electric charge comes in fixed amounts, but no one has ever confirmed finding one.",
    "answerHtml": "<b><u>magnetic monopole</u></b>s (accept <u>monopole</u>s; prompt on <u>magnetic charge</u>; do not accept “magnetic dipole”)",
    "accept": [
        "magnetic monopoles",
        "magnetic monopole",
        "monopoles",
        "monopole",
        "dirac monopole",
        "dirac monopoles"
    ],
    "prompt": [
        "magnetic charge",
        "magnetic charges",
        "isolated magnetic pole",
        "isolated magnetic poles",
        "single magnetic pole",
        "lone magnetic pole",
        "isolated pole",
        "single pole",
        "lone pole",
        "magnetic pole",
        "magnetic poles"
    ],
    "reject": [
        "magnetic dipole",
        "magnetic dipoles",
        "dipole",
        "dipoles",
        "electric dipole",
        "electric dipoles",
        "electric monopole",
        "electric monopoles",
        "magnetic field",
        "magnetic fields",
        "earths magnetic field",
        "magnetism",
        "magnet",
        "magnets",
        "bar magnet",
        "electromagnet",
        "quadrupole",
        "magnetic moment",
        "magnetic domain",
        "electric charge",
        "electron",
        "electrons",
        "positron",
        "quasiparticle",
        "quasiparticles",
        "spin ice",
        "axion",
        "axions",
        "tachyon",
        "tachyons",
        "magnetar",
        "magnetars",
        "neutrino",
        "neutrinos",
        "dark matter",
        "higgs boson",
        "gausss law for magnetism",
        "gauss law for magnetism",
        "gausss law",
        "gauss law",
        "paul dirac",
        "dirac equation",
        "dirac string",
        "maxwells equations",
        "ferromagnetism",
        "monopoly",
        "monopolies"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Magnetic_monopole",
    "qb": {"q": "monopole", "found": 0, "tip": TIP},
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        {
            "p": "On February 14, 1982, Blas Cabrera’s superconducting loop at Stanford recorded a single jump in current that looked like one of these particles passing through. The event was never repeated, so physicists do not count it as a discovery.",
            "r": "For 10 points, name these hypothetical particles that would carry a single north or south magnetic pole."
        },
        {
            "p": "In 1931, Paul Dirac showed that if even one of these particles exists anywhere in the universe, then electric charge must come in whole-number multiples of a smallest unit. That would explain why all electric charges in nature come in fixed amounts.",
            "r": "For 10 points, name these hypothetical particles, never confirmed, that would be lone north or south magnetic poles."
        },
        {
            "p": "Gauss’s law for magnetism, one of Maxwell’s equations, says that the total magnetic flux out of any closed surface is zero, which means these objects do not appear in classical physics. If one were found, that equation would have to change.",
            "r": "For 10 points, name these hypothetical particles that would have only a north pole or only a south pole."
        },
        {
            "p": "Alan Guth’s theory of cosmic inflation was proposed partly to explain why the universe is not full of these heavy particles, which grand unified theories predict should have formed in huge numbers just after the Big Bang.",
            "r": "For 10 points, name these never-confirmed particles, each of which would have a single magnetic pole."
        },
        {
            "p": "In 1974, Gerard ’t Hooft [“ut HOHFT”] and Alexander Polyakov [“pull-YAH-koff”] independently showed that grand unified theories of particle physics predict these particles. Such particles would be far heavier than anything ever made in a particle accelerator.",
            "r": "For 10 points, name these hypothetical particles that would act as isolated north or south magnetic poles."
        },
        {
            "p": "The MoEDAL experiment at CERN’s Large Hadron Collider was built mainly to search for these particles in the debris of proton collisions. Part of the experiment is designed to trap any that are made, so they can be studied later.",
            "r": "None has ever been confirmed. For 10 points, name these hypothetical particles with only one magnetic pole."
        },
        {
            "p": "In materials called spin ice, defects in the arrangement of tiny atomic magnets behave like imitation versions of these particles. Physicists stress that these “quasiparticles” are not true elementary examples.",
            "r": "Paul Dirac argued that they could exist. For 10 points, name these hypothetical particles that would have only one magnetic pole, unlike every magnet ever found."
        },
        {
            "p": "If these objects existed, the equations of electricity and magnetism would become almost perfectly symmetrical, with a magnetic version of electric charge. A single electron is the electric counterpart of one of these objects.",
            "r": "For 10 points, name these hypothetical particles that would be lone north or south magnetic poles."
        },
        {
            "p": "A loop of superconducting wire can serve as a detector for these particles, because one passing through the loop would cause a sudden, lasting jump in the current flowing around it.",
            "r": "Each one would be a lone north or south pole. For 10 points, name these never-confirmed particles that would carry magnetic charge."
        },
        {
            "p": "In 1894, Pierre Curie suggested that free magnetic charges might exist in nature. His paper discussed the possible existence of “free magnetism.” Decades later, Paul Dirac gave the first strong argument from quantum theory that they could exist.",
            "r": "For 10 points, name these hypothetical particles that would each have just a north or just a south pole."
        },
        {
            "p": "Unlike electric field lines, which begin on positive charges and end on negative charges, magnetic field lines always form closed loops, because no one has ever confirmed finding one of these objects.",
            "r": "Paul Dirac predicted them in 1931. For 10 points, name these hypothetical particles that would be isolated north or south magnetic poles."
        },
        {
            "p": "The IceCube Neutrino Observatory at the South Pole has searched for fast-moving examples of these particles by looking for the light they would give off as they sped through the ice.",
            "r": "Cutting a bar magnet in half never produces one of these. For 10 points, name these hypothetical particles with a single magnetic pole."
        },
        {
            "p": "Physicists have searched moon rocks brought back by Apollo astronauts and ancient minerals for trapped examples of these particles, without success. In one search, samples were passed through a superconducting coil to look for a sudden jump in current.",
            "r": "For 10 points, name these hypothetical particles, each a lone north or south magnetic pole."
        },
        {
            "p": "In 1975, scientists claimed to have spotted the track of one of these particles in a detector carried by a high-altitude balloon, but most physicists concluded that the track came from an ordinary heavy atomic nucleus.",
            "r": "For 10 points, name these hypothetical particles that would be single north or south magnetic poles."
        },
        {
            "p": "Italy’s MACRO experiment, buried deep under a mountain, took its name partly from these particles, which it searched for during the 1990s without finding any. The experiment also studied cosmic rays and neutrinos.",
            "r": "Every magnet ever found has two poles. For 10 points, name these hypothetical particles that would carry a lone north or south magnetic pole."
        }
    ],
    "clues": [
        C("single-pole", "giveaway", "Hypothetical particles with just one magnetic pole: a lone north or a lone south",
          ["one magnetic pole", "lone north", "hypothetical"]),
        C("cut-magnet", "giveaway", "Cutting a bar magnet in half never makes one; each half gets its own north and south poles",
          ["bar magnet", "cutting", "each half"]),
        C("never-found", "giveaway", "Never confirmed in any experiment, as of 2025",
          ["never confirmed", "2025"]),
        C("magnetic-charge", "giveaway", "Each would carry “magnetic charge,” a magnetic version of electric charge",
          ["magnetic charge", "electric charge"]),
        C("dirac-1931", "middle", "Paul Dirac (1931): if even one exists, electric charge must come in fixed units (charge quantization)",
          ["paul dirac", "1931", "fixed units"]),
        C("closed-loops", "middle", "Magnetic field lines always form closed loops, since no lone poles have been found",
          ["closed loops", "field lines"], "Magnetic fields"),
        C("gauss-law", "middle", "Gauss’s law for magnetism, one of Maxwell’s equations, says the total magnetic flux out of any closed surface is zero",
          ["gauss’s law for magnetism", "maxwell’s equations", "closed surface"], "Gauss’s law"),
        C("symmetry", "middle", "If they existed, the equations of electricity and magnetism would be almost perfectly symmetrical",
          ["symmetrical", "equations"]),
        C("electron-counterpart", "middle", "A single electron is the electric counterpart; a magnet with two poles is a dipole",
          ["electric counterpart", "dipole"], "Dipoles"),
        C("cabrera", "middle", "Blas Cabrera’s superconducting loop at Stanford recorded one possible event on February 14, 1982, never repeated",
          ["cabrera", "stanford", "february 14"]),
        C("superconducting-loop", "power", "One passing through a superconducting loop would cause a sudden, lasting jump in current",
          ["superconducting loop", "jump in current"]),
        C("guth", "power", "Alan Guth’s cosmic inflation was proposed partly to explain why the universe isn’t full of them",
          ["alan guth", "inflation"]),
        C("gut", "power", "Grand unified theories predict extremely heavy ones that formed just after the Big Bang",
          ["grand unified theories", "big bang"]),
        C("thooft-polyakov", "power", "Gerard ’t Hooft and Alexander Polyakov (1974) showed that grand unified theories predict them",
          ["polyakov", "1974"]),
        C("moedal", "power", "The MoEDAL experiment at CERN’s Large Hadron Collider was built mainly to search for them",
          ["moedal", "large hadron collider", "cern"]),
        C("spin-ice", "power", "In spin ice, defects among tiny atomic magnets imitate them, but these quasiparticles are not true elementary ones",
          ["spin ice", "quasiparticles"]),
        C("curie", "power", "Pierre Curie suggested in 1894 that free magnetic charges might exist",
          ["pierre curie", "1894"]),
        C("icecube", "power", "The IceCube Neutrino Observatory at the South Pole has searched for light from fast-moving ones",
          ["icecube", "neutrino observatory"]),
        C("moon-rocks", "power", "Apollo moon rocks and ancient minerals have been searched for trapped ones, without success",
          ["moon rocks", "apollo", "minerals"]),
        C("balloon", "power", "A 1975 claim from a balloon-borne detector was later explained as an ordinary heavy nucleus",
          ["balloon", "1975", "heavy nucleus"]),
        C("macro", "power", "Italy’s MACRO experiment, deep under a mountain, searched for them in the 1990s and found none",
          ["macro", "italy", "1990s"])
    ],
    "trap": {
        "title": "One pole, not two",
        "body": "Every magnet ever found is a dipole, with both a north and a south pole, so “magnetic dipole” is the opposite of this answer. Tossups about these particles also mention magnetic fields, Gauss’s law for magnetism, and Paul Dirac, which are separate answer lines. Saying “magnetic charge” earns only a prompt.",
        "fix": "Lone north or south poles, Dirac’s 1931 argument, Cabrera’s 1982 event, and the cosmic inflation puzzle point to these particles. If the question asks for “this law” or “this equation,” the answer is Gauss’s law for magnetism instead.",
        "line": "Real answer line: <b><u>magnetic monopole</u></b>s (accept <u>monopole</u>s; prompt on <u>magnetic charge</u>; do not accept “magnetic dipole”)"
    },
    "tests": {
        "right": [
            "Magnetic monopoles",
            "magnetic monopole",
            "Monopoles",
            "Monopole",
            "Magnetic monopols"
        ],
        "prompt": [
            "Magnetic charge",
            "Isolated magnetic pole"
        ],
        "wrong": [
            "Magnetic dipole",
            "Magnetic field",
            "Electric monopole",
            "Quasiparticles",
            "Magnetism"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
