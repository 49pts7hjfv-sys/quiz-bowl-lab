import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."


def C(cid, tier, t, k, rabbit=None):
    d = {"id": cid, "tier": tier, "t": t, "k": k, "n": 0}
    if rabbit:
        d["rabbit"] = rabbit
    return d


LINE = "<b><u>diodes</u></b> (accept <u>diode</u>; prompt on <u>rectifier</u>s or <u>p-n junction</u>s; do not accept “LEDs” or “transistors”)"

data = {
    "id": "diodes",
    "name": "Diodes",
    "mono": "PN",
    "category": "Physics",
    "qbCategory": "Science · Physics",
    "kicker": "One-way valves for electric current · Turn AC into DC",
    "dates": "First vacuum-tube version by John Ambrose Fleming, 1904",
    "briefing": "A diode is an electronic part that lets electric current flow in only one direction, like a one-way valve for electricity. Most diodes today are made by joining two kinds of silicon, called p-type and n-type, and they are used to turn the alternating current from a wall outlet into the direct current that electronics need. Light-emitting diodes, or LEDs, are diodes that glow when current passes through them.",
    "answerHtml": LINE,
    "accept": [
        "diode",
        "diodes",
        "semiconductor diode",
        "semiconductor diodes",
        "p n junction diode",
        "p n junction diodes",
        "pn junction diode",
        "junction diode",
        "crystal diode",
        "vacuum tube diode",
        "rectifier diode",
        "rectifier diodes"
    ],
    "prompt": [
        "rectifier",
        "rectifiers",
        "p n junction",
        "p n junctions",
        "pn junction",
        "semiconductor",
        "semiconductors",
        "vacuum tube",
        "vacuum tubes",
        "valve",
        "valves",
        "thermionic valve",
        "fleming valve",
        "oscillation valve"
    ],
    "reject": [
        "transistor",
        "transistors",
        "triode",
        "triodes",
        "audion",
        "resistor",
        "resistors",
        "capacitor",
        "capacitors",
        "inductor",
        "inductors",
        "led",
        "leds",
        "light emitting diode",
        "light emitting diodes",
        "electrode",
        "electrodes",
        "anode",
        "cathode",
        "battery",
        "batteries",
        "solar cell",
        "solar cells",
        "thyristor",
        "integrated circuit",
        "switch",
        "fuse"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Diode",
    "qb": {"q": "diode", "found": 0, "tip": TIP},
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        {
            "p": "In 1904, John Ambrose Fleming built an early version of these devices from a vacuum tube, calling it an “oscillation valve,” to detect radio signals for Guglielmo Marconi’s wireless company. Modern versions of these devices are usually made from silicon.",
            "r": "For 10 points, name these electronic components that let electric current flow in only one direction."
        },
        {
            "p": "Lee de Forest added a third electrode, a wire grid, to the vacuum-tube type of these devices, creating the Audion, which could amplify signals. Early crystal radio sets used a crude type of these devices called a “cat’s whisker,” a thin wire touching a crystal of galena.",
            "r": "For 10 points, name these two-terminal parts that act as one-way valves for electric current."
        },
        {
            "p": "In 1874, Karl Ferdinand Braun [“BROWN”] found that a metal point touching certain crystals could rectify electricity, the first semiconductor example of these devices. Modern examples of these devices are made at a junction between p-type and n-type silicon.",
            "r": "For 10 points, name these electronic components that let current flow in only one direction."
        },
        {
            "p": "Zener [“ZEE-ner”] types of these devices, named for Clarence Zener, are designed to conduct backward once a set breakdown voltage is reached, so they can hold a voltage steady. When an ordinary one of these devices is reverse biased, it blocks nearly all flow.",
            "r": "For 10 points, name these components, made from p-n junctions, that pass current in just one direction."
        },
        {
            "p": "Leo Esaki [“eh-SAH-kee”] shared the 1973 Nobel Prize in Physics after inventing a “tunnel” type of these devices, in which the current drops as the voltage rises over a certain range. Ordinary types of these devices are called “non-ohmic,” since their current does not grow in proportion to the voltage.",
            "r": "For 10 points, name these electronic parts, used as rectifiers, that let current flow only one way."
        },
        {
            "p": "Isamu Akasaki, Hiroshi Amano, and Shuji Nakamura won the 2014 Nobel Prize in Physics for making efficient blue light-emitting versions of these devices, which made bright, energy-saving white lighting possible. In 1962, Nick Holonyak Jr. made the first light-emitting one that gave off visible red light.",
            "r": "For 10 points, name these electronic components that let current pass in only one direction."
        },
        {
            "p": "Four of these devices arranged in a diamond-shaped bridge make a full-wave rectifier, which flips the backward half of each cycle of alternating current so that both halves come out flowing the same way. A single one of these devices instead blocks every backward half-cycle.",
            "r": "For 10 points, name these components that change AC into DC by letting current flow in just one direction."
        },
        {
            "p": "Schottky [“SHOT-kee”] types of these devices join a metal directly to a semiconductor, which lets them switch on with less voltage than usual. On a circuit diagram, one of these devices is drawn as a triangle pointing at a short bar.",
            "r": "A painted stripe marks its cathode end. For 10 points, name these components that let current flow in only one direction."
        },
        {
            "p": "A silicon one of these devices needs about 0.7 volts across it in the forward direction before it conducts well. That happens when its p side is connected to the positive side of a battery, a setup called forward bias.",
            "r": "For 10 points, name these components, used as rectifiers, that block current flowing the wrong way."
        },
        {
            "p": "At the heart of most of these devices is a thin depletion region, where electrons from the n-type side have filled the “holes” on the p-type side. That region acts as a barrier that only a large enough forward voltage can push current across.",
            "r": "For 10 points, name these electronic parts, used in rectifiers, that let current flow just one way."
        },
        {
            "p": "A solar cell is basically a large, flat version of these devices: light striking its p-n junction knocks electrons loose and drives them around a circuit. Light-emitting versions of these devices do the reverse, giving off light when electrons cross the junction and fill holes.",
            "r": "For 10 points, name these components, which pass current in only one direction and can turn AC into DC."
        },
        {
            "p": "Blu-ray players read discs using a laser type of these devices that gives off blue-violet light, while CD players use a type that gives off infrared light. Other types of these devices glow in many colors in traffic lights and screens.",
            "r": "For 10 points, name these electronic components that let current flow in only one direction."
        },
        {
            "p": "Varactor [“vuh-RAK-ter”] types of these devices behave like capacitors whose value changes with the voltage across them, so they can tune radios without moving parts. Placing an ordinary one of these devices in line with a battery holder protects a gadget if the batteries go in backward.",
            "r": "For 10 points, name these components, often marked with a stripe, that let current flow in only one direction."
        },
        {
            "p": "In the early 1880s, Thomas Edison noticed that a heated filament inside a light bulb sent electricity across the vacuum to a nearby metal plate, but only when the plate was connected to the positive side. That “Edison effect” is the basis of vacuum-tube types of these devices.",
            "r": "For 10 points, name these components that let electric current flow in only one direction."
        },
        {
            "p": "A TV remote control flashes coded pulses of infrared light from a light-emitting type of these devices, and the TV picks them up with a light-sensitive type of these devices. Both types are built around a junction of p-type and n-type material.",
            "r": "For 10 points, name these components that let current flow in only one direction, often used as rectifiers."
        }
    ],
    "clues": [
        C("one-way", "giveaway", "Electronic parts that let electric current flow in only one direction, like a one-way valve", ["one direction", "one-way valve"], "Electric current"),
        C("rectify", "giveaway", "Used as rectifiers to change alternating current (AC) into direct current (DC)", ["rectifiers", "alternating current", "direct current"]),
        C("anode-cathode", "giveaway", "Current enters at the anode and leaves at the cathode, which is marked with a painted stripe", ["anode", "cathode", "stripe"]),
        C("leds", "middle", "Light-emitting versions, called LEDs, glow when current flows through them", ["light-emitting", "leds", "glow"]),
        C("pn", "middle", "Most are made from a p-n junction, where p-type and n-type silicon meet", ["p-n junction", "silicon"], "Semiconductors"),
        C("bias", "middle", "Conduct when forward biased (p side to the positive terminal) and block when reverse biased", ["forward biased", "reverse biased"]),
        C("point-seven", "middle", "A silicon one needs about 0.7 volts across it in the forward direction before it conducts well", ["0.7 volts", "silicon"]),
        C("symbol", "middle", "Circuit symbol: a triangle pointing at a short bar, showing the direction current can flow", ["triangle", "short bar", "circuit symbol"]),
        C("bridge", "middle", "Four in a diamond-shaped bridge make a full-wave rectifier; a single one makes a half-wave rectifier", ["bridge", "full-wave", "half-wave"]),
        C("non-ohmic", "middle", "Non-ohmic: their current does not grow in proportion to the voltage", ["non-ohmic", "proportion"], "Electrical resistance"),
        C("depletion", "middle", "A thin depletion region, where electrons from the n side have filled holes on the p side, forms a barrier at the junction", ["depletion region", "holes", "barrier"]),
        C("solar", "middle", "A solar cell is basically a large, flat one: light striking its junction knocks electrons loose and drives them around a circuit", ["solar cell", "light striking"]),
        C("battery-protect", "middle", "One placed in line with a battery holder protects a gadget if the batteries go in backward", ["battery holder", "backward"]),
        C("fleming", "power", "John Ambrose Fleming built a vacuum-tube version, the “oscillation valve,” in 1904 to detect radio signals for Marconi’s company", ["fleming", "oscillation valve", "1904"]),
        C("edison", "power", "Edison effect (early 1880s): a heated filament sent electricity to a metal plate in a bulb, but only when the plate was positive", ["edison effect", "filament"]),
        C("de-forest", "power", "Lee de Forest added a third electrode, a wire grid, to the vacuum-tube type to make the Audion, which could amplify signals", ["de forest", "audion", "grid"]),
        C("braun", "power", "Karl Ferdinand Braun (1874) found that a metal point touching certain crystals could rectify electricity, the first semiconductor version", ["braun", "1874", "crystals"]),
        C("cats-whisker", "power", "Early crystal radios used a “cat’s whisker,” a thin wire touching a crystal of galena", ["cat’s whisker", "galena", "crystal radios"]),
        C("zener", "power", "Zener types, named for Clarence Zener, conduct backward at a set breakdown voltage, so they can hold a voltage steady", ["zener", "breakdown voltage"]),
        C("tunnel", "power", "Leo Esaki shared the 1973 Nobel Prize after inventing the tunnel type, in which current drops as voltage rises over a certain range", ["esaki", "tunnel", "1973"]),
        C("blue-led", "power", "Isamu Akasaki, Hiroshi Amano, and Shuji Nakamura won the 2014 Nobel Prize in Physics for efficient blue light-emitting ones", ["blue", "2014", "nakamura"]),
        C("holonyak", "power", "Nick Holonyak Jr. made the first light-emitting one that gave off visible (red) light in 1962", ["holonyak", "1962", "red"]),
        C("schottky", "power", "Schottky types join a metal directly to a semiconductor, so they switch on with less voltage", ["schottky", "metal"]),
        C("varactor", "power", "Varactor types act like capacitors whose value changes with the voltage, so they can tune radios without moving parts", ["varactor", "tune radios"], "Capacitors"),
        C("laser", "power", "Laser types read Blu-ray discs with blue-violet light and CDs with infrared light", ["blu-ray", "laser", "infrared"], "Lasers"),
        C("remote", "power", "A TV remote flashes infrared light from a light-emitting type, and the TV picks it up with a light-sensitive type", ["remote", "light-sensitive"])
    ],
    "trap": {
        "title": "The device, not LEDs",
        "body": "Light-emitting diodes (LEDs) are just one kind of this device, so this page does not accept “LED” or “light-emitting diode” when a tossup is about the general one-way part. Players also confuse it with the transistor, which usually has three terminals and can amplify or switch signals, and with the triode, the three-electrode vacuum tube that Lee de Forest made by adding a grid. Saying “rectifier” earns only a prompt, since that word names the job, not the part.",
        "fix": "One-way flow, AC to DC, p-n junctions, anode and cathode, Fleming’s valve, and Zener types mean diodes. Three terminals, amplifying, and switching mean transistors. If a question asks specifically for the devices that give off light, then answer “LEDs.”",
        "line": "Real answer line: " + LINE
    },
    "tests": {
        "right": [
            "Diodes",
            "diode",
            "Semiconductor diode",
            "Diods",
            "P-N junction diode"
        ],
        "prompt": [
            "Rectifier",
            "Vacuum tube"
        ],
        "wrong": [
            "Transistor",
            "Capacitor",
            "LED",
            "Light-emitting diode",
            "Resistor",
            "Triode"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
