import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "entropy",
    "name": "Entropy",
    "mono": "ENT",
    "category": "Physics",
    "qbCategory": "Science · Physics",
    "kicker": "Measure of disorder · Never decreases in an isolated system",
    "dates": "Named by Rudolf Clausius, 1865",
    "briefing": "Entropy measures disorder: how many different ways the tiny particles in a system can be arranged. It explains why ice melts in a warm room and why a dropped egg never puts itself back together, because in an isolated system, entropy never goes down. Rudolf Clausius named it in 1865, and Ludwig Boltzmann’s formula for it, S = k log W, is carved on his tombstone in Vienna.",
    "answerHtml": "<b><u>Entropy</u></b> (prompt on <u>S</u> or <u>disorder</u>)",
    "accept": [
        "entropy",
        "entropies",
        "thermodynamic entropy"
    ],
    "prompt": [
        "s",
        "disorder"
    ],
    "reject": [
        "enthalpy",
        "second law of thermodynamics",
        "second law",
        "thermodynamics",
        "gibbs free energy",
        "free energy",
        "energy",
        "heat",
        "temperature",
        "heat capacity",
        "maxwells demon",
        "heat death"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Entropy",
    "qb": {
        "q": "entropy",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Ludwig Boltzmann’s [“BOHLTS-mahnz”] tombstone in Vienna is carved with a formula for this quantity: a constant k times the logarithm of W, the number of tiny arrangements a system’s particles can have. For a reversible process, a change in this quantity equals the heat added divided by the absolute temperature.",
            "r": "For 10 points, name this measure of a system’s disorder, which never decreases in an isolated system."
        },
        {
            "p": "Rudolf Clausius [“KLOW-zee-us”] coined this quantity’s name in 1865 from a Greek word for “transformation,” choosing it to sound like the word “energy.” Clausius summed up thermodynamics by saying that the energy of the universe is constant, while this quantity tends toward a maximum.",
            "r": "It is measured in joules per kelvin. For 10 points, name this quantity, symbolized S, often described as a measure of disorder."
        },
        {
            "p": "Rolf Landauer’s [“LAN-dow-erz”] principle, which says that erasing a bit of information always releases heat, helps explain why a tiny imaginary being cannot lower this quantity for free. That being opens a door between two boxes of gas only for fast molecules, sorting them from slow ones without doing work.",
            "r": "That being is Maxwell’s demon. For 10 points, name this quantity that the second law of thermodynamics says never decreases in an isolated system."
        },
        {
            "p": "Jacob Bekenstein [“BEK-en-stine”] proposed that a black hole has an amount of this quantity proportional to the area of its event horizon, an idea supported when Stephen Hawking showed that black holes give off radiation.",
            "r": "A substance’s gas form has more of this quantity than its liquid or solid forms. For 10 points, name this measure of disorder."
        },
        {
            "p": "In 1948, Claude Shannon defined a version of this quantity that measures the average information in a message, counted in bits. The total change in this quantity for an engine and its surroundings is zero for a perfectly reversible cycle, but positive for any real engine.",
            "r": "For 10 points, name this quantity that measures disorder, which the second law of thermodynamics says tends to increase."
        },
        {
            "p": "Linus Pauling explained why ordinary ice keeps a leftover amount of this quantity even close to absolute zero: its hydrogen atoms can be arranged in a huge number of ways. The third law of thermodynamics says that this quantity is zero for a perfect crystal at absolute zero.",
            "r": "For 10 points, name this quantity, symbolized S, which increases when ice melts into liquid water."
        },
        {
            "p": "On a graph of temperature versus this quantity, a Carnot [“kar-NOH”] cycle forms a rectangle, since its two reversible adiabatic steps leave this quantity unchanged. The area enclosed by a cycle on that kind of graph equals the net work the engine does.",
            "r": "Heat flowing from a hot object to a cold one increases this quantity. For 10 points, name this measure of disorder, symbolized S."
        },
        {
            "p": "Chemists predict whether a reaction will happen on its own by multiplying this quantity by temperature and subtracting the result from the enthalpy, giving the Gibbs free energy. A reaction that releases heat and also increases this quantity is spontaneous at every temperature.",
            "r": "Melting ice and boiling water both increase this quantity. For 10 points, name this measure of disorder, symbolized S."
        },
        {
            "p": "Arthur Eddington coined the phrase “arrow of time” for the one-way direction that the steady rise of this quantity seems to give the universe. This quantity explains why a shattered glass never jumps back together, even though the laws of motion work the same forward and backward.",
            "r": "The second law of thermodynamics says this quantity never decreases in an isolated system. For 10 points, name this measure of disorder, symbolized S."
        },
        {
            "p": "In a possible far-future “heat death,” this quantity would reach its maximum value for the whole universe, leaving no temperature differences to power anything. A change in this quantity can be found by dividing the heat added in a reversible process by the absolute temperature.",
            "r": "Ice melting in a warm room increases it. For 10 points, name this measure of disorder, which never decreases in an isolated system."
        },
        {
            "p": "The Gibbs paradox asks why removing a wall between two samples of the same gas does not increase this quantity, while removing a wall between two different gases does. Ludwig Boltzmann explained this quantity by counting the number of ways a system’s particles can be arranged.",
            "r": "The total amount of this quantity rises whenever heat flows from a hot object to a cold one. For 10 points, name this measure of disorder, symbolized S."
        },
        {
            "p": "When an ideal gas expands freely into a vacuum, no heat flows in and its temperature stays the same, yet this quantity still increases. This quantity is a state function, so its change depends only on a system’s starting and ending states, not on the path between them.",
            "r": "The second law of thermodynamics says this quantity never decreases in an isolated system. For 10 points, name this measure of disorder."
        },
        {
            "p": "Erwin Schrödinger’s [“SHROH-ding-erz”] 1944 book _What Is Life?_ argued that living things stay alive by “feeding on” the negative of this quantity. A living cell can lower this quantity inside itself only by releasing heat that raises it even more in its surroundings.",
            "r": "For 10 points, name this measure of disorder, which the second law of thermodynamics says tends to increase."
        },
        {
            "p": "Josef Loschmidt [“LOHSH-mit”] objected that the laws governing colliding molecules work the same backward in time, so they could not explain why this quantity only increases. That objection targeted Ludwig Boltzmann’s H-theorem, which claimed to show this quantity rising as gas molecules collide.",
            "r": "For 10 points, name this measure of disorder, symbolized S, whose change equals heat divided by temperature in a reversible process."
        },
        {
            "p": "The Clausius [“KLOW-zee-us”] inequality leads to the rule that, in any real process, the change in this quantity is greater than the heat added divided by the temperature. This quantity, measured in joules per kelvin, has the same units as the Boltzmann constant.",
            "r": "For 10 points, name this quantity that increases when ice melts, often described as a measure of disorder."
        }
    ],
    "clues": [
        {
            "id": "disorder",
            "tier": "giveaway",
            "t": "A measure of disorder: how many ways a system’s particles can be arranged",
            "k": ["disorder", "arranged"],
            "n": 0
        },
        {
            "id": "second-law",
            "tier": "giveaway",
            "t": "The second law of thermodynamics says it never decreases in an isolated system",
            "k": ["second law", "isolated system", "never decreases"],
            "n": 0,
            "rabbit": "Second law of thermodynamics"
        },
        {
            "id": "units",
            "tier": "giveaway",
            "t": "Symbolized S and measured in joules per kelvin",
            "k": ["joules per kelvin", "kelvin"],
            "n": 0
        },
        {
            "id": "melting",
            "tier": "giveaway",
            "t": "Increases when ice melts or water boils, as particles spread out and move more freely",
            "k": ["ice melts", "water boils"],
            "n": 0
        },
        {
            "id": "heat-over-t",
            "tier": "middle",
            "t": "Its change equals the heat added in a reversible process divided by the absolute temperature (Q/T)",
            "k": ["heat added", "absolute temperature", "reversible"],
            "n": 0
        },
        {
            "id": "clausius-1865",
            "tier": "middle",
            "t": "Rudolf Clausius named it in 1865 from a Greek word for “transformation,” to sound like “energy”",
            "k": ["clausius", "1865", "transformation"],
            "n": 0
        },
        {
            "id": "boltzmann",
            "tier": "middle",
            "t": "Boltzmann’s formula S = k log W is carved on his tombstone in Vienna; W counts the possible arrangements (microstates)",
            "k": ["boltzmann", "tombstone", "microstates"],
            "n": 0
        },
        {
            "id": "gibbs",
            "tier": "middle",
            "t": "Multiplied by temperature and subtracted from enthalpy to give the Gibbs free energy (G = H − TS)",
            "k": ["gibbs free energy", "enthalpy"],
            "n": 0,
            "rabbit": "Gibbs free energy"
        },
        {
            "id": "third-law",
            "tier": "middle",
            "t": "The third law of thermodynamics: it is zero for a perfect crystal at absolute zero",
            "k": ["third law", "perfect crystal", "absolute zero"],
            "n": 0,
            "rabbit": "Absolute zero"
        },
        {
            "id": "maxwell-demon",
            "tier": "middle",
            "t": "Maxwell’s demon: an imaginary being that sorts fast and slow molecules seems to lower it without doing work",
            "k": ["maxwell", "demon", "fast and slow"],
            "n": 0,
            "rabbit": "Maxwell’s demon"
        },
        {
            "id": "heat-flow",
            "tier": "middle",
            "t": "Heat flows on its own from hot to cold, never cold to hot, because that direction raises its total",
            "k": ["hot to cold", "cold to hot"],
            "n": 0
        },
        {
            "id": "state-function",
            "tier": "middle",
            "t": "A state function: its change depends only on the starting and ending states, not the path between them",
            "k": ["state function", "path"],
            "n": 0
        },
        {
            "id": "bekenstein",
            "tier": "power",
            "t": "Jacob Bekenstein: a black hole’s amount is proportional to the area of its event horizon",
            "k": ["bekenstein", "black hole", "event horizon"],
            "n": 0,
            "rabbit": "Black Holes"
        },
        {
            "id": "shannon",
            "tier": "power",
            "t": "Claude Shannon (1948) defined an information version of it, counted in bits",
            "k": ["shannon", "information", "bits"],
            "n": 0
        },
        {
            "id": "eddington",
            "tier": "power",
            "t": "Arthur Eddington coined “arrow of time” for the one-way direction its rise gives time",
            "k": ["eddington", "arrow of time"],
            "n": 0
        },
        {
            "id": "heat-death",
            "tier": "power",
            "t": "“Heat death”: a far-future universe at its maximum value, with no temperature differences left to power anything",
            "k": ["heat death", "maximum"],
            "n": 0
        },
        {
            "id": "carnot-graph",
            "tier": "power",
            "t": "On a temperature-versus-it graph, a Carnot cycle is a rectangle; the reversible adiabatic steps keep it constant",
            "k": ["carnot", "rectangle", "adiabatic"],
            "n": 0
        },
        {
            "id": "pauling-ice",
            "tier": "power",
            "t": "Linus Pauling explained ice’s leftover (residual) amount near absolute zero: its hydrogen atoms can be arranged many ways",
            "k": ["pauling", "residual", "leftover"],
            "n": 0
        },
        {
            "id": "gibbs-paradox",
            "tier": "power",
            "t": "Gibbs paradox: mixing two different gases raises it, but mixing two samples of the same gas does not",
            "k": ["gibbs paradox", "mixing"],
            "n": 0
        },
        {
            "id": "free-expansion",
            "tier": "power",
            "t": "An ideal gas expanding freely into a vacuum gains it, even though no heat flows in and its temperature stays the same",
            "k": ["vacuum", "expanding freely"],
            "n": 0
        },
        {
            "id": "schrodinger",
            "tier": "power",
            "t": "Erwin Schrödinger’s 1944 book _What Is Life?_ says living things survive by “feeding on” its negative",
            "k": ["schrödinger", "what is life", "negative"],
            "n": 0
        },
        {
            "id": "loschmidt",
            "tier": "power",
            "t": "Loschmidt’s paradox: time-reversible molecular laws seem to clash with Boltzmann’s H-theorem, which shows it rising",
            "k": ["loschmidt", "h-theorem", "time-reversible"],
            "n": 0
        },
        {
            "id": "clausius-inequality",
            "tier": "power",
            "t": "Clausius inequality: in a real process, its change is greater than the heat added divided by the temperature",
            "k": ["clausius inequality", "inequality"],
            "n": 0
        },
        {
            "id": "landauer",
            "tier": "power",
            "t": "Landauer’s principle: erasing information always releases heat, which explains why Maxwell’s demon cannot win",
            "k": ["landauer", "erasing"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Entropy, not enthalpy",
        "body": "Entropy (S, disorder) and enthalpy (H, heat content) sound alike and sit side by side in the Gibbs free energy equation, G = H − TS, so players mix them up. Players also blurt “second law of thermodynamics” when the question wants the quantity that law is about.",
        "fix": "Disorder, Boltzmann’s S = k log W, “joules per kelvin,” and anything that “never decreases” point to entropy. Heat content, heats of reaction, and Hess’s law point to enthalpy. If the question asks for “this quantity,” name the quantity, not the law.",
        "line": "Real answer line: <b><u>Entropy</u></b> (prompt on <u>S</u> or <u>disorder</u>)"
    },
    "tests": {
        "right": [
            "Entropy",
            "entropy",
            "Entrophy",
            "Thermodynamic entropy",
            "Entropies"
        ],
        "prompt": [
            "S",
            "Disorder"
        ],
        "wrong": [
            "Enthalpy",
            "Second law of thermodynamics",
            "Gibbs free energy",
            "Heat",
            "Temperature"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
