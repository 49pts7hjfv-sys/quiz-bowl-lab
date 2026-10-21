import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."


def C(cid, tier, t, k, rabbit=None):
    d = {"id": cid, "tier": tier, "t": t, "k": k, "n": 0}
    if rabbit:
        d["rabbit"] = rabbit
    return d


LINE = "<b><u>voltage</u></b> (accept <u>potential difference</u> or <u>electric potential</u>; prompt on <u>V</u> or <u>electromotive force</u>; do not accept “current,” “resistance,” “power,” or “Ohm’s law”)"

data = {
    "id": "voltage",
    "name": "Voltage",
    "mono": "VLT",
    "category": "Physics",
    "qbCategory": "Science · Physics",
    "kicker": "The push that drives electric current · Measured in volts",
    "dates": "Volta’s pile, the first battery, 1800; Ohm’s law, 1827",
    "briefing": "Voltage is the electrical “push” that drives current through a circuit, a little like water pressure pushing water through a pipe. It is measured in volts, named for Alessandro Volta, who built the first battery in 1800. An AA battery supplies about 1.5 volts and a U.S. wall outlet about 120, while a bolt of lightning can involve hundreds of millions.",
    "answerHtml": LINE,
    "accept": [
        "voltage",
        "voltages",
        "potential difference",
        "potential differences",
        "electric potential difference",
        "electrical potential difference",
        "electric potential",
        "electrical potential",
        "voltage difference"
    ],
    "prompt": [
        "v",
        "potential",
        "electromotive force",
        "emf",
        "e m f"
    ],
    "reject": [
        "current",
        "electric current",
        "electrical current",
        "resistance",
        "electrical resistance",
        "power",
        "electric power",
        "ohms law",
        "kirchhoffs voltage law",
        "kirchhoffs law",
        "kirchhoffs laws",
        "voltage divider",
        "voltmeter",
        "voltmeters",
        "volt",
        "volts",
        "volta",
        "alessandro volta",
        "electric potential energy",
        "electrical potential energy",
        "potential energy",
        "energy",
        "electric charge",
        "charge",
        "electric field",
        "capacitance",
        "amperage",
        "amperes",
        "amps",
        "watts",
        "electricity",
        "impedance"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Voltage",
    "qb": {"q": "voltage", "found": 0, "tip": TIP},
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        {
            "p": "Particle physicists measure energy in a unit equal to the energy an electron gains when it moves through one unit of this quantity, about 1.6 times 10 to the negative 19th joules. One unit of this quantity equals one joule of energy per coulomb of charge.",
            "r": "For 10 points, name this quantity, measured in volts, that pushes electric current through a circuit."
        },
        {
            "p": "In 2019, scientists described a new species of electric eel that can deliver a jolt of about 860 units of this quantity, the strongest known from any animal. They named it in honor of the Italian scientist for whom this quantity’s unit is named.",
            "r": "For 10 points, name this quantity, measured in volts, that equals current times resistance."
        },
        {
            "p": "This quantity’s unit honors a scientist who argued with Luigi Galvani over whether frog legs twitched because of “animal electricity” or because of the two different metals touching them. That Italian scientist was made a count by Napoleon.",
            "r": "He also stacked zinc and copper disks into the first battery, a pile announced in 1800. For 10 points, name this quantity, measured in volts."
        },
        {
            "p": "A bird can perch safely on a bare power line because there is almost none of this quantity between its two feet, so almost no current flows through its body. A squirrel that touches two different wires at once, however, can cause a power outage.",
            "r": "For 10 points, name this quantity, the push that drives current, measured in volts."
        },
        {
            "p": "Gustav Kirchhoff’s loop rule says that the changes in this quantity around any closed path in a circuit add up to zero, a consequence of the conservation of energy. In a series circuit, this quantity across all of the parts adds up to the battery’s value.",
            "r": "For 10 points, name this quantity, measured in volts, which equals current times resistance in Ohm’s law."
        },
        {
            "p": "A resting nerve cell keeps about negative 70 thousandths of a unit of this quantity across its membrane, using pumps that move sodium ions out and potassium ions in. During a nerve signal, called an action potential, this quantity across the membrane briefly flips to positive.",
            "r": "For 10 points, name this quantity, measured in volts, that a battery supplies to a circuit."
        },
        {
            "p": "Transformers, which came into wide use in the 1880s, use two coils with different numbers of turns to raise or lower this quantity for alternating current. Long-distance power lines carry hundreds of thousands of units of this quantity so that a smaller current wastes less energy as heat.",
            "r": "U.S. wall outlets supply about 120 of its units. For 10 points, name this quantity, measured in volts."
        },
        {
            "p": "A meter that measures this quantity must be connected in parallel with the part being tested, and a good one has an enormous resistance so that it draws almost no current. In a parallel circuit, every branch has the same value of this quantity.",
            "r": "For 10 points, name this quantity, which Ohm’s law says equals current times resistance."
        },
        {
            "p": "This quantity supplied by a battery when no current flows is called the battery’s electromotive force; it drops a little under load because of the battery’s internal resistance. Two AA batteries placed end to end in series give 3 units of this quantity, double what one gives.",
            "r": "Ohm’s law relates it to current and resistance. For 10 points, name this quantity, measured in volts."
        },
        {
            "p": "A current of 2 amperes flowing through a 6-ohm resistor requires 12 units of this quantity across it, and that resistor then turns 24 watts of electrical power into heat. Multiplying this quantity by current always gives electric power.",
            "r": "For 10 points, name this quantity, measured in volts, which Georg Ohm related to current and resistance."
        },
        {
            "p": "The electric field points from places where this quantity is high toward places where it is low, so the field’s units can be written as this quantity’s unit per meter. Surfaces on which this quantity stays constant, called equipotentials, always cross electric field lines at right angles.",
            "r": "For 10 points, name this quantity, measured in volts, that drives current through a circuit."
        },
        {
            "p": "Lightning can involve hundreds of millions of units of this quantity, and a tabletop Van de Graaff [“van duh GRAHF”] generator can build up hundreds of thousands. Even the small spark from touching a doorknob after shuffling across a carpet involves thousands of units of this quantity.",
            "r": "A standard AA battery supplies about 1.5 of its units. For 10 points, name this quantity, measured in volts."
        },
        {
            "p": "Chemists combine the standard reduction potentials of two half-reactions to find this quantity for a galvanic cell, and the Nernst equation shows how it changes with concentration. A lemon with a copper coin and a zinc-coated nail stuck into it produces a small amount of this quantity.",
            "r": "Ohm’s law says it equals current times resistance. For 10 points, name this quantity, measured in volts, that batteries supply."
        },
        {
            "p": "A capacitor’s capacitance equals the charge on one plate divided by this quantity across the plates, and the energy it stores equals one-half the capacitance times the square of this quantity. Doubling this quantity across a capacitor therefore stores four times as much energy.",
            "r": "For 10 points, name this quantity, measured in volts, that a battery provides to push current."
        },
        {
            "p": "Travelers from the United States to Europe may need a converter, because European outlets supply about 230 units of this quantity, nearly twice the U.S. value. Japan’s outlets supply even less, about 100 units, and standard USB ports supply just 5.",
            "r": "For 10 points, name this quantity, measured in volts, which is about 120 for a U.S. wall outlet."
        }
    ],
    "clues": [
        C("definition", "giveaway", "The electrical “push” between two points that drives current through a circuit", ["push", "two points"]),
        C("volts", "giveaway", "Measured in volts, named for the Italian scientist Alessandro Volta", ["volts", "volta"]),
        C("ohms-law", "giveaway", "Ohm’s law: it equals current times resistance (V = IR)", ["ohm’s law", "current times resistance", "v = ir"], "Electrical resistance"),
        C("batteries", "giveaway", "Batteries supply it: an AA battery gives about 1.5 volts and a car battery about 12; two AAs in series give 3", ["batteries", "1.5", "series"]),
        C("outlets", "giveaway", "U.S. wall outlets supply about 120 volts; much of Europe uses about 230", ["outlets", "120", "230"]),
        C("joule-per-coulomb", "middle", "One volt is one joule of energy per coulomb of charge", ["joule", "coulomb"], "Electric charge"),
        C("voltmeter", "middle", "Measured with a voltmeter connected in parallel; a good voltmeter has a huge resistance and draws almost no current", ["voltmeter", "parallel"]),
        C("series-parallel", "middle", "Adds up across the parts of a series circuit; is the same across every branch of a parallel circuit", ["series circuit", "parallel circuit", "branch"]),
        C("power", "middle", "Electric power equals it times current (P = IV)", ["power", "p = iv"], "Power (physics)"),
        C("volta-pile", "middle", "Alessandro Volta stacked zinc and copper disks into the first battery, the voltaic pile (1800)", ["voltaic pile", "zinc", "1800"], "Electric current"),
        C("transformers", "middle", "Transformers raise or lower it for alternating current; power lines use hundreds of thousands of volts to cut heat losses", ["transformers", "power lines"]),
        C("emf", "middle", "The value a source gives with no current flowing is called its electromotive force (EMF)", ["electromotive force", "emf"]),
        C("birds", "middle", "Birds sit safely on a power line because there is almost none of it between their two feet", ["birds", "power line"]),
        C("kirchhoff", "middle", "Kirchhoff’s loop rule: its changes around any closed loop add to zero (conservation of energy)", ["kirchhoff", "loop rule"], "Gustav Kirchhoff"),
        C("electron-volt", "power", "The electron volt, a unit of energy, is the energy an electron gains moving through 1 volt: about 1.6 × 10⁻¹⁹ joules", ["electron volt", "1.6"]),
        C("eel", "power", "A species of electric eel described in 2019 and named for Volta can make about 860 volts, the strongest of any animal", ["electric eel", "860"]),
        C("galvani", "power", "Volta argued with Luigi Galvani over whether “animal electricity” made frog legs twitch", ["galvani", "frog legs", "animal electricity"]),
        C("napoleon", "power", "Napoleon made Alessandro Volta a count", ["napoleon", "count"]),
        C("neuron", "power", "A resting nerve cell holds about −70 millivolts across its membrane; the value flips positive during an action potential", ["nerve cell", "action potential", "millivolts"]),
        C("internal-resistance", "power", "A battery’s internal resistance makes its value drop a little when it delivers current", ["internal resistance"]),
        C("computation", "power", "2 amperes through a 6-ohm resistor needs 12 volts, and the resistor turns 24 watts into heat", ["12 volts", "24 watts"]),
        C("field", "power", "The electric field points from high values to low ones and can be measured in volts per meter; equipotentials cross field lines at right angles", ["volts per meter", "equipotentials"], "Electric field"),
        C("static", "power", "Lightning can involve hundreds of millions of volts, a tabletop Van de Graaff generator hundreds of thousands, and a doorknob spark thousands", ["lightning", "van de graaff", "doorknob"]),
        C("nernst", "power", "A galvanic cell’s value comes from combining standard reduction potentials; the Nernst equation adjusts it for concentration", ["nernst", "reduction potentials", "galvanic"]),
        C("lemon", "power", "A lemon with a copper coin and a zinc-coated nail stuck in it makes a small amount", ["lemon", "copper", "zinc"]),
        C("capacitor", "power", "Capacitance = charge ÷ this quantity; stored energy = ½ × capacitance × its square, so doubling it stores 4 times the energy", ["capacitance", "stored energy"], "Capacitors"),
        C("japan-usb", "power", "Japan’s outlets supply about 100 volts; standard USB ports supply 5", ["japan", "usb"])
    ],
    "trap": {
        "title": "Push, flow, or resistance?",
        "body": "Circuit tossups mix up four answers. Voltage is the push that drives charge (volts); current is the flow itself (amperes); resistance opposes the flow (ohms); and power is how fast energy is used (watts). Ohm’s law, V = IR, ties three of them together, so hearing “Ohm’s law” does not tell you which one the tossup wants, and “Ohm’s law” itself is never the answer to “name this quantity.”",
        "fix": "Volts, voltmeters, batteries rated at 1.5 or 9, outlets at 120, and potential difference mean voltage. Amperes and ammeters mean current; ohms mean resistance; watts mean power. A battery’s electromotive force (EMF) earns only a prompt here, so be ready to say “voltage.”",
        "line": "Real answer line: " + LINE
    },
    "tests": {
        "right": [
            "Voltage",
            "potential difference",
            "Electric potential difference",
            "Electric potential",
            "Voltge",
            "Voltages"
        ],
        "prompt": [
            "V",
            "EMF",
            "Electromotive force",
            "Potential"
        ],
        "wrong": [
            "Current",
            "Electric current",
            "Resistance",
            "Power",
            "Ohm's law",
            "Volts",
            "Electric potential energy",
            "Voltmeter",
            "Potential energy"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
