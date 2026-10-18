import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "galileo-galilei",
    "name": "Galileo Galilei",
    "mono": "GG",
    "category": "Physics",
    "qbCategory": "Science · Physics",
    "kicker": "Italian scientist with the telescope · Jupiter’s moons and a famous trial",
    "dates": "1564–1642",
    "briefing": "Starting in 1609, Galileo Galilei pointed his homemade telescopes at the night sky and found mountains on the Moon, the phases of Venus, and four moons circling Jupiter. He also rolled balls down ramps to work out how objects fall, laying groundwork for Isaac Newton. Because he defended Copernicus’s idea that Earth moves around the Sun, the Roman Inquisition put him on trial in 1633 and kept him under house arrest for the rest of his life.",
    "answerHtml": "<b><u>Galileo</u></b> Galilei (accept <u>Galilei</u>; do not accept “Vincenzo Galilei,” his father)",
    "accept": [
        "galileo galilei",
        "galileo",
        "galilei"
    ],
    "prompt": [],
    "reject": [
        "vincenzo galilei",
        "vincenzo",
        "galileo spacecraft",
        "galileo probe",
        "galileo mission",
        "galilean moons",
        "galilean moon",
        "galilean",
        "galilean transformation",
        "galilean relativity",
        "galileo thermometer",
        "nicolaus copernicus",
        "copernicus",
        "johannes kepler",
        "kepler",
        "tycho brahe",
        "isaac newton",
        "newton",
        "giordano bruno",
        "aristotle",
        "ptolemy",
        "simon marius",
        "christoph scheiner",
        "pope urban viii",
        "urban viii",
        "medici"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Galileo_Galilei",
    "qb": {
        "q": "Galileo",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "This scientist recorded Neptune in his notes in 1612 and 1613 but mistook it for a fixed star. When he looked at Saturn, his telescope could not show its rings, so he described the planet as three bodies, a large one with a smaller companion on each side.",
            "r": "For 10 points, name this Italian astronomer who discovered the four largest moons of Jupiter in 1610."
        },
        {
            "p": "This scientist’s 1610 book _Sidereus Nuncius_ [“sih-DEER-ee-us NUN-see-us”], or _Starry Messenger_, reported mountains and craters on the Moon and showed that the Milky Way is made of countless stars. In that book, he named four new objects the “Medicean Stars” to honor the ruling family of Florence.",
            "r": "For 10 points, name this Italian astronomer who discovered the largest moons of Jupiter and was later tried by the Inquisition."
        },
        {
            "p": "In this scientist’s 1632 _Dialogue Concerning the Two Chief World Systems_, a character named Simplicio defends the old Earth-centered view against Salviati, who speaks for the author. Simplicio also repeats an argument made by Pope Urban VIII, which angered the pope.",
            "r": "For 10 points, name this Italian scientist, sentenced to house arrest in 1633 for supporting the idea that Earth moves around the Sun."
        },
        {
            "p": "In a 1638 book written under house arrest and printed in the Netherlands, this scientist explained why a giant animal would need proportionally thicker bones, an idea now called the square-cube law. That book, _Two New Sciences_, also showed that a thrown object follows a parabola.",
            "r": "For 10 points, name this Italian physicist who studied falling bodies and was tried by the Roman Inquisition."
        },
        {
            "p": "A paradox named for this man notes that there seem to be as many perfect squares as there are counting numbers, even though most counting numbers are not squares. This man also tried to measure the speed of light by uncovering lanterns on distant hills, but the light was too fast to time.",
            "r": "For 10 points, name this scientist who supported Copernicus and was sentenced to house arrest after a trial in 1633."
        },
        {
            "p": "This scientist rolled balls down gently sloping ramps to slow their fall, finding that the distance traveled grows with the square of the time. He concluded that a ball rolling on a level surface would keep moving unless something stopped it, an early form of the idea of inertia.",
            "r": "For 10 points, name this Italian physicist who supposedly dropped two balls from the Leaning Tower of Pisa."
        },
        {
            "p": "This man’s father was a lute player and music theorist. A story told by this man’s student Vincenzo Viviani [“vee-VYAH-nee”] says this man noticed that a swinging lamp in Pisa’s cathedral took the same time for each swing, whether the swing was wide or narrow.",
            "r": "He built his own telescope in 1609. For 10 points, name this Italian scientist who studied pendulums and falling objects."
        },
        {
            "p": "This scientist argued with the Jesuit Christoph Scheiner [“SHY-ner”] over who first saw sunspots and what they were. This man’s observation that Venus goes through a full set of phases like the Moon was strong evidence against Ptolemy’s Earth-centered model.",
            "r": "He discovered four moons of Jupiter in 1610. For 10 points, name this Italian astronomer who championed the Copernican system."
        },
        {
            "p": "In 1992, Pope John Paul II acknowledged that this scientist had been wrongly condemned, after a commission studied his case. This man is buried in Florence’s Basilica of Santa Croce, near the tomb of Michelangelo.",
            "r": "For 10 points, name this Italian scientist who was tried by the Inquisition in 1633 for supporting heliocentrism."
        },
        {
            "p": "Bertolt Brecht wrote a play about this scientist’s life, and a NASA probe named for him orbited Jupiter from 1995 to 2003. The four largest moons of Jupiter are known as a group by this man’s name.",
            "r": "For 10 points, name this Italian astronomer who discovered those moons in 1610 with a telescope he built himself."
        },
        {
            "p": "In _The Assayer_, this scientist argued with Orazio Grassi about comets and wrote that the book of nature is written in the language of mathematics. He wrongly argued that the tides were caused by Earth’s motions, using them as proof that Earth moves.",
            "r": "For 10 points, name this Italian scientist who supported the Copernican model and was tried in 1633."
        },
        {
            "p": "Johannes Kepler wrote a reply welcoming this man’s 1610 discoveries, and Simon Marius later gave the moons this man discovered the names Io, Europa, Ganymede, and Callisto. This man was the first to report seeing those moons through a telescope.",
            "r": "For 10 points, name this Italian astronomer, who was later put on trial by the Roman Inquisition."
        },
        {
            "p": "In 1616, Cardinal Robert Bellarmine warned this man not to hold or defend the idea that Earth moves, and Copernicus’s book was suspended until corrected. Seventeen years later, this man was forced to take back his views and spent the rest of his life under house arrest near Florence.",
            "r": "He also studied falling bodies and pendulums. For 10 points, name this Italian scientist who discovered Jupiter’s four largest moons."
        },
        {
            "p": "Letters to this man from his eldest daughter, a nun known as Sister Maria Celeste, were the basis of a 1999 book by Dava Sobel. According to a legend, after being forced to take back his claim that Earth moves, this man muttered “And yet it moves.”",
            "r": "This man was born in Pisa in 1564. For 10 points, name this Italian scientist who used a telescope to discover four moons of Jupiter."
        },
        {
            "p": "A unit of acceleration used in gravity surveys, equal to one centimeter per second squared, is named for this man. In a thought experiment, he argued that a person in a closed cabin below the deck of a smoothly sailing ship could not tell that the ship was moving.",
            "r": "For 10 points, name this Italian scientist, the subject of a famous 1633 trial before the Inquisition."
        }
    ],
    "clues": [
        {
            "id": "jupiter-moons",
            "tier": "giveaway",
            "t": "Discovered the four largest moons of Jupiter in 1610: Io, Europa, Ganymede, and Callisto",
            "k": ["four largest moons", "jupiter", "1610"],
            "n": 0,
            "rabbit": "Jupiter"
        },
        {
            "id": "telescope",
            "tier": "giveaway",
            "t": "Built his own telescope in 1609 and turned it on the night sky",
            "k": ["telescope", "1609"],
            "n": 0
        },
        {
            "id": "inquisition",
            "tier": "giveaway",
            "t": "Tried by the Roman Inquisition in 1633 and kept under house arrest for supporting heliocentrism",
            "k": ["inquisition", "1633", "house arrest"],
            "n": 0
        },
        {
            "id": "copernican",
            "tier": "giveaway",
            "t": "Supported Copernicus’s idea that Earth moves around the Sun",
            "k": ["copernicus", "around the sun"],
            "n": 0
        },
        {
            "id": "leaning-tower",
            "tier": "giveaway",
            "t": "Supposedly dropped two balls from the Leaning Tower of Pisa to show they fall together",
            "k": ["leaning tower", "pisa"],
            "n": 0
        },
        {
            "id": "starry-messenger",
            "tier": "middle",
            "t": "_Sidereus Nuncius_ (_Starry Messenger_, 1610): mountains on the Moon and a Milky Way made of countless stars",
            "k": ["sidereus nuncius", "starry messenger"],
            "n": 0
        },
        {
            "id": "medicean-stars",
            "tier": "middle",
            "t": "Named Jupiter’s moons the “Medicean Stars” to honor the Medici family of Florence",
            "k": ["medicean stars", "medici"],
            "n": 0
        },
        {
            "id": "venus-phases",
            "tier": "middle",
            "t": "Saw that Venus goes through a full set of phases like the Moon, evidence against Ptolemy’s system",
            "k": ["venus", "phases", "ptolemy"],
            "n": 0,
            "rabbit": "Venus (planet)"
        },
        {
            "id": "dialogue",
            "tier": "middle",
            "t": "_Dialogue Concerning the Two Chief World Systems_ (1632): Simplicio vs. Salviati; Pope Urban VIII was angered when Simplicio repeated his argument",
            "k": ["two chief world systems", "simplicio", "urban viii"],
            "n": 0
        },
        {
            "id": "ramps",
            "tier": "middle",
            "t": "Rolled balls down ramps (inclined planes): the distance fallen grows with the square of the time",
            "k": ["ramps", "inclined planes", "square of the time"],
            "n": 0
        },
        {
            "id": "inertia",
            "tier": "middle",
            "t": "A ball on a level surface would keep rolling unless stopped: an early form of the idea of inertia",
            "k": ["inertia", "level surface"],
            "n": 0,
            "rabbit": "Inertia"
        },
        {
            "id": "pendulum",
            "tier": "middle",
            "t": "A story told by his student Vincenzo Viviani says a swinging lamp in Pisa’s cathedral led him to study pendulums",
            "k": ["pendulums", "viviani", "lamp"],
            "n": 0,
            "rabbit": "Pendulums"
        },
        {
            "id": "and-yet-it-moves",
            "tier": "middle",
            "t": "Legend says he muttered “And yet it moves” after being forced to take back his views",
            "k": ["and yet it moves", "legend"],
            "n": 0
        },
        {
            "id": "born-pisa",
            "tier": "middle",
            "t": "Born in Pisa in 1564, the same year as William Shakespeare; later taught at Padua",
            "k": ["1564", "shakespeare", "padua"],
            "n": 0
        },
        {
            "id": "neptune",
            "tier": "power",
            "t": "Recorded Neptune in 1612 and 1613 but mistook it for a fixed star",
            "k": ["neptune", "1612", "fixed star"],
            "n": 0
        },
        {
            "id": "saturn",
            "tier": "power",
            "t": "His telescope could not show Saturn’s rings, so Saturn looked like three bodies, a large one with a companion on each side",
            "k": ["saturn", "three bodies"],
            "n": 0
        },
        {
            "id": "two-new-sciences",
            "tier": "power",
            "t": "_Two New Sciences_ (1638), printed in the Netherlands: the square-cube law and the parabolic path of a thrown object",
            "k": ["two new sciences", "square-cube", "parabolic"],
            "n": 0
        },
        {
            "id": "paradox-lanterns",
            "tier": "power",
            "t": "His paradox: there seem to be as many perfect squares as counting numbers; he also tried to time light with lanterns on distant hills",
            "k": ["paradox", "perfect squares", "lanterns"],
            "n": 0
        },
        {
            "id": "father",
            "tier": "power",
            "t": "His father, Vincenzo, was a lute player and music theorist",
            "k": ["lute", "music theorist", "vincenzo"],
            "n": 0
        },
        {
            "id": "scheiner",
            "tier": "power",
            "t": "Argued with the Jesuit Christoph Scheiner about who first saw sunspots and what they were",
            "k": ["scheiner", "sunspots", "jesuit"],
            "n": 0,
            "rabbit": "Sunspots"
        },
        {
            "id": "assayer",
            "tier": "power",
            "t": "_The Assayer_: argued with Orazio Grassi about comets and wrote that nature is written in the language of mathematics",
            "k": ["the assayer", "grassi", "language of mathematics"],
            "n": 0
        },
        {
            "id": "tides",
            "tier": "power",
            "t": "Wrongly argued that Earth’s motions cause the tides, as proof that Earth moves",
            "k": ["tides", "wrongly"],
            "n": 0
        },
        {
            "id": "kepler-marius",
            "tier": "power",
            "t": "Johannes Kepler welcomed his 1610 discoveries; Simon Marius gave the four moons their names",
            "k": ["kepler", "simon marius"],
            "n": 0,
            "rabbit": "Johannes Kepler"
        },
        {
            "id": "bellarmine",
            "tier": "power",
            "t": "1616: Cardinal Robert Bellarmine warned him not to hold or defend the idea that Earth moves",
            "k": ["bellarmine", "1616"],
            "n": 0
        },
        {
            "id": "john-paul-ii",
            "tier": "power",
            "t": "In 1992, Pope John Paul II acknowledged he had been wrongly condemned; he is buried in Santa Croce in Florence",
            "k": ["1992", "john paul ii", "santa croce"],
            "n": 0
        },
        {
            "id": "brecht-probe",
            "tier": "power",
            "t": "Subject of a Bertolt Brecht play; a NASA probe named for him orbited Jupiter from 1995 to 2003",
            "k": ["brecht", "nasa probe", "1995"],
            "n": 0,
            "rabbit": "Bertolt Brecht"
        },
        {
            "id": "maria-celeste",
            "tier": "power",
            "t": "His eldest daughter, the nun Sister Maria Celeste, wrote him letters used in Dava Sobel’s 1999 book",
            "k": ["maria celeste", "dava sobel"],
            "n": 0
        },
        {
            "id": "gal-ship",
            "tier": "power",
            "t": "The gal, a unit of acceleration, is named for him; his closed-ship-cabin thought experiment shows that steady motion cannot be felt",
            "k": ["thought experiment", "ship", "gal"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Copernicus, Kepler, or him?",
        "body": "Copernicus (the Polish astronomer who published the Sun-centered model in 1543), Johannes Kepler (who found that planets move in ellipses), and this man all show up in questions about heliocentrism. Tycho Brahe, Kepler’s mentor, made the best measurements of the sky without a telescope. Isaac Newton came later and built his laws of motion on this man’s work.",
        "fix": "A telescope, Jupiter’s moons, Venus’s phases, sunspots, falling bodies, pendulums, the Inquisition, or house arrest point to this man. Ellipses and three laws of planetary motion mean Kepler, and _De revolutionibus_ or 1543 means Copernicus.",
        "line": "Real answer line: <b><u>Galileo</u></b> Galilei (accept <u>Galilei</u>)"
    },
    "tests": {
        "right": [
            "Galileo Galilei",
            "Galileo",
            "Galilei",
            "Galilleo",
            "Galileo Galile"
        ],
        "prompt": [],
        "wrong": [
            "Copernicus",
            "Johannes Kepler",
            "Isaac Newton",
            "Vincenzo Galilei",
            "Tycho Brahe",
            "Galilean moons"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
