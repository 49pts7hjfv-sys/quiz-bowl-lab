import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."


def C(cid, tier, t, k, rabbit=None):
    d = {"id": cid, "tier": tier, "t": t, "k": k, "n": 0}
    if rabbit:
        d["rabbit"] = rabbit
    return d


LINE = "<b><u>electric current</u></b> (accept <u>current</u>; prompt on <u>I</u> or <u>flow of electrons</u>; do not accept “voltage” or “electric charge”)"

data = {
    "id": "electric-current",
    "name": "Electric current",
    "mono": "AMP",
    "category": "Physics",
    "qbCategory": "Science · Physics",
    "kicker": "The flow of electric charge · Measured in amperes",
    "dates": "First steady flow from Volta’s battery, 1800",
    "briefing": "Electric current is a flow of electric charge, usually electrons drifting through a wire, and it is measured in amperes, or amps. Alessandro Volta’s battery made the first steady current in 1800, and in 1820 Hans Christian Ørsted noticed that a wire carrying current made a compass needle swing. Wall outlets supply alternating current, which flips direction many times each second, while batteries supply direct current, which flows one way.",
    "answerHtml": LINE,
    "accept": [
        "electric current",
        "electric currents",
        "electrical current",
        "electrical currents",
        "current",
        "currents",
        "conventional current",
        "current of electricity",
        "amperage"
    ],
    "prompt": [
        "i",
        "flow of electrons",
        "electron flow",
        "flow of charge",
        "charge flow"
    ],
    "reject": [
        "voltage",
        "potential difference",
        "electric potential",
        "resistance",
        "electrical resistance",
        "electric charge",
        "charge",
        "electrons",
        "electron",
        "ampere",
        "amperes",
        "amp",
        "amps",
        "coulomb",
        "coulombs",
        "electric power",
        "power",
        "electric field",
        "magnetic field",
        "electromotive force",
        "emf",
        "ohms law",
        "amperes law",
        "kirchhoffs current law",
        "alternating current",
        "direct current",
        "ac",
        "dc",
        "eddy current",
        "eddy currents",
        "displacement current",
        "convection current",
        "convection currents",
        "ocean current",
        "ocean currents",
        "current density",
        "electricity",
        "static electricity",
        "lightning"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Electric_current",
    "qb": {"q": "current", "found": 0, "tip": TIP},
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        {
            "p": "Before 2019, the SI base unit of this quantity was defined by the force between two long, parallel wires placed one meter apart. Since 2019, that unit has been defined by fixing the exact value of the elementary charge.",
            "r": "For 10 points, name this flow of electric charge, symbolized I and measured in amperes."
        },
        {
            "p": "This quantity’s usual symbol, I, comes from the French phrase intensité du courant [“an-tahn-see-TAY doo koo-RAHN”]. In 1820, a French physicist showed that two parallel wires carrying this quantity in the same direction attract each other, and its SI unit is named for him.",
            "r": "It is measured with an ammeter. For 10 points, name this flow of charge, measured in amperes."
        },
        {
            "p": "The Biot–Savart [“bee-OH suh-VAR”] law adds up the magnetic field made by each tiny piece of a wire carrying this quantity. In 1820, Hans Christian Ørsted noticed that a compass needle swung whenever this quantity flowed through a nearby wire.",
            "r": "This quantity is symbolized I. For 10 points, name this flow of electric charge, measured in amperes."
        },
        {
            "p": "In a copper wire, the electrons that carry this quantity usually drift along at less than a millimeter per second. Because of a naming choice by Benjamin Franklin, the conventional direction of this quantity runs from positive to negative, opposite to the way the electrons move.",
            "r": "An ammeter measures it. For 10 points, name this flow of electric charge, measured in amperes."
        },
        {
            "p": "A galvanometer, named for the Italian scientist Luigi Galvani, detects small amounts of this quantity by how far its needle turns. Alessandro Volta’s pile of zinc and copper disks, built in 1800, was the first battery to produce a steady flow of this quantity.",
            "r": "Batteries supply its direct form. For 10 points, name this quantity, measured with an ammeter in amperes."
        },
        {
            "p": "Gustav Kirchhoff’s junction rule says that the total amount of this quantity flowing into any point in a circuit equals the total flowing out, because charge is conserved. In a parallel circuit, this quantity splits among the branches.",
            "r": "In a series circuit, it is the same at every point. For 10 points, name this quantity, measured in amperes."
        },
        {
            "p": "In the late 1880s, Thomas Edison promoted one form of this quantity, while Nikola Tesla and George Westinghouse promoted a form that reverses direction many times each second. The reversing form won out partly because transformers can raise and lower its voltage.",
            "r": "For 10 points, name this quantity, which comes in AC and DC forms and is measured in amperes."
        },
        {
            "p": "Outlets in the United States supply the alternating form of this quantity at 60 hertz, while much of Europe uses 50 hertz. Power companies send electricity over long lines at very high voltages so that less of this quantity flows, which cuts the energy wasted as heat.",
            "r": "Batteries supply its direct form. For 10 points, name this flow of charge, measured in amperes."
        },
        {
            "p": "James Prescott Joule found that the heat given off by a wire each second equals the square of this quantity times the wire’s resistance. Fuses melt and circuit breakers trip when too much of this quantity flows through a circuit.",
            "r": "Ohm’s law says it equals voltage divided by resistance. For 10 points, name this quantity, measured in amperes."
        },
        {
            "p": "In the Hall effect, a magnetic field pushes the moving charges that carry this quantity toward one edge of a metal strip, creating a small voltage across the strip. A ring of superconducting wire can keep this quantity circulating for years with no battery attached.",
            "r": "For 10 points, name this flow of charge, measured with an ammeter in amperes."
        },
        {
            "p": "Michael Faraday found that the amount of metal plated out during electrolysis is proportional to this quantity multiplied by the time it flows. An ideal meter for measuring this quantity has almost no resistance and is connected in series with the part being tested.",
            "r": "That meter is an ammeter. For 10 points, name this flow of charge, measured in amperes."
        },
        {
            "p": "About 6.24 billion billion electrons must pass a point each second to make one unit of this quantity. A lightning bolt carries tens of thousands of those units, though only for a tiny fraction of a second.",
            "r": "For 10 points, name this quantity, the rate at which electric charge flows, measured in amperes."
        },
        {
            "p": "This quantity’s unit is the only electrical unit among the seven SI base units, which also include the meter, the kilogram, the second, and the kelvin. One of those units equals one coulomb of charge passing a point each second.",
            "r": "It is measured with an ammeter. For 10 points, name this flow of charge, measured in amperes."
        },
        {
            "p": "Inside a long coil called a solenoid, the magnetic field equals the permeability of free space times the number of turns per meter times this quantity. An electromagnet gets stronger with more turns of wire or more of this quantity.",
            "r": "For 10 points, name this flow of charge, symbolized I and measured in amperes."
        },
        {
            "p": "Multiplying this quantity by voltage gives electric power in watts, so a 60-watt bulb on a 120-volt line draws half a unit of this quantity. A diode lets this quantity pass in only one direction.",
            "r": "It is symbolized I. For 10 points, name this flow of electric charge, measured in amperes."
        }
    ],
    "clues": [
        C("flow", "giveaway", "The flow of electric charge, usually electrons moving through a wire", ["flow of electric charge", "electrons"]),
        C("amperes", "giveaway", "Measured in amperes (amps): one ampere is one coulomb of charge passing a point each second", ["amperes", "amps", "coulomb"], "Electric charge"),
        C("ac-dc", "giveaway", "Comes in alternating (AC) and direct (DC) forms; wall outlets supply AC and batteries supply DC", ["alternating", "direct", "batteries"]),
        C("ohms-law", "giveaway", "Symbolized I; Ohm’s law says it equals voltage divided by resistance (I = V/R)", ["ohm’s law", "voltage divided by resistance"], "Electrical resistance"),
        C("ammeter", "giveaway", "Measured with an ammeter, which is connected in series with the part being tested", ["ammeter", "series"]),
        C("series-parallel", "middle", "The same at every point in a series circuit; splits among the branches of a parallel circuit", ["series circuit", "parallel circuit", "branches"]),
        C("kirchhoff", "middle", "Kirchhoff’s junction rule: the total flowing into any point equals the total flowing out, because charge is conserved", ["kirchhoff", "junction rule"], "Gustav Kirchhoff"),
        C("orsted", "middle", "Hans Christian Ørsted (1820) saw it swing a nearby compass needle, the first link between electricity and magnetism", ["ørsted", "oersted", "compass needle"], "Magnetic fields"),
        C("conventional", "middle", "Its conventional direction runs from positive to negative, opposite to the electrons, because of a naming choice by Benjamin Franklin", ["conventional direction", "franklin", "opposite"]),
        C("volta", "middle", "Alessandro Volta’s pile (1800), the first battery, gave the first steady flow of it", ["volta", "pile", "1800"]),
        C("edison-tesla", "middle", "Late 1880s: Thomas Edison backed DC, while Nikola Tesla and George Westinghouse backed AC; AC won partly because transformers can change its voltage", ["edison", "tesla", "westinghouse", "transformers"]),
        C("fuses", "middle", "Fuses melt and circuit breakers trip when too much of it flows", ["fuses", "circuit breakers"]),
        C("joule", "middle", "Joule heating: heat given off each second equals its square times the resistance, so power lines use high voltage to keep it small", ["joule", "heat", "power lines"]),
        C("power-iv", "middle", "Electric power equals it times voltage (P = IV), so a 60-watt bulb on a 120-volt line draws half an ampere", ["electric power", "60-watt"]),
        C("diode", "middle", "A diode lets it pass in only one direction", ["diode", "one direction"], "Diodes"),
        C("symbol-french", "power", "Its symbol, I, comes from the French phrase intensité du courant", ["intensité", "french phrase"]),
        C("ampere-1820", "power", "In 1820, André-Marie Ampère showed that parallel wires carrying it in the same direction attract; its unit is named for him", ["andré-marie ampère", "parallel wires", "attract"], "Ampère’s law"),
        C("si-2019", "power", "Before 2019, its unit was defined by the force between two parallel wires one meter apart; since 2019, by fixing the elementary charge", ["2019", "elementary charge"]),
        C("base-unit", "power", "Its unit is the only electrical unit among the seven SI base units", ["base units", "seven"]),
        C("drift", "power", "Electrons carrying it through a copper wire drift at less than a millimeter per second", ["drift", "millimeter"]),
        C("per-second", "power", "One ampere is about 6.24 billion billion electrons passing a point each second", ["6.24 billion billion", "electrons"]),
        C("lightning", "power", "A lightning bolt carries tens of thousands of amperes for a tiny fraction of a second", ["lightning", "tens of thousands"]),
        C("galvanometer", "power", "A galvanometer, named for Luigi Galvani, detects small amounts of it by how far a needle turns", ["galvanometer", "galvani"]),
        C("biot-savart", "power", "The Biot–Savart law adds up the magnetic field made by each tiny piece of a wire carrying it", ["biot–savart", "biot"], "Magnetic fields"),
        C("hall", "power", "Hall effect: a magnetic field pushes its moving charges to one edge of a strip, making a small voltage across the strip", ["hall effect", "edge"], "Hall effect"),
        C("superconductor", "power", "A ring of superconducting wire can keep it circulating for years with no battery attached", ["superconducting", "circulating"], "Superconductivity"),
        C("electrolysis", "power", "Michael Faraday: the metal plated out in electrolysis is proportional to it multiplied by the time it flows", ["electrolysis", "faraday"], "Michael Faraday"),
        C("ideal-ammeter", "power", "An ideal ammeter has almost no resistance, so it does not change what it measures", ["ideal ammeter", "almost no resistance"]),
        C("hertz", "power", "U.S. outlets supply the alternating form at 60 hertz; much of Europe uses 50 hertz", ["60 hertz", "50 hertz"]),
        C("solenoid", "power", "Inside a long solenoid, the magnetic field equals the permeability of free space × turns per meter × this quantity", ["solenoid", "turns per meter"])
    ],
    "trap": {
        "title": "Current, voltage, or charge?",
        "body": "Circuit tossups mix three related answers. Current is how fast charge flows (amperes), voltage is the push that drives it (volts), and charge is the stuff that flows (coulombs). Some tossups want one specific kind instead: questions about Edison, Tesla, and the “War of the Currents” often ask for alternating current, and Earth science tossups ask about ocean currents.",
        "fix": "Amperes, ammeters, the symbol I, I = V/R, and Kirchhoff’s junction rule mean current. Volts and potential difference mean voltage; coulombs, Millikan’s oil drops, and “positive or negative” mean charge. If the giveaway asks for the form that reverses direction many times a second, say “alternating current.”",
        "line": "Real answer line: " + LINE
    },
    "tests": {
        "right": [
            "Electric current",
            "current",
            "Electrical current",
            "Electric curent",
            "Currents"
        ],
        "prompt": [
            "I",
            "Flow of electrons"
        ],
        "wrong": [
            "Voltage",
            "Amperes",
            "Electric charge",
            "Resistance",
            "Alternating current",
            "Ocean currents",
            "Electricity"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
