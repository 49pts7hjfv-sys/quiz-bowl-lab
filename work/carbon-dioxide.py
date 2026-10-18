import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "carbon-dioxide",
    "name": "Carbon dioxide",
    "mono": "CO2",
    "category": "Chemistry",
    "qbCategory": "Science · Chemistry",
    "kicker": "One carbon, two oxygens · The gas we exhale and plants breathe in",
    "dates": "Described as “fixed air” in the 1750s",
    "briefing": "Carbon dioxide is the gas you breathe out with every breath, and the gas plants soak up to build sugar during photosynthesis. Freeze it and you get dry ice, which skips the liquid stage and turns straight into gas. It also puts the fizz in soda, and because it traps heat in the atmosphere, scientists have tracked its rising level at a Hawaii observatory since 1958.",
    "answerHtml": "<b><u>Carbon dioxide</u></b> (accept <u>CO2</u>; prompt on <u>dry ice</u>; do not accept “carbon monoxide”)",
    "accept": [
        "carbon dioxide",
        "co2",
        "co 2"
    ],
    "prompt": [
        "dry ice"
    ],
    "reject": [
        "carbon monoxide",
        "co",
        "carbon trioxide",
        "carbon suboxide",
        "carbonic acid",
        "carbonate",
        "carbonates",
        "bicarbonate",
        "calcium carbonate",
        "methane",
        "oxygen",
        "nitrogen",
        "water vapor",
        "ozone",
        "silicon dioxide",
        "sulfur dioxide",
        "nitrogen dioxide",
        "nitrous oxide",
        "carbon disulfide",
        "carbon tetrachloride",
        "greenhouse gas",
        "greenhouse gases"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Carbon_dioxide",
    "qb": {
        "q": "carbon dioxide",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Jan Baptist van Helmont [“HEL-mont”] called this substance “gas sylvestre,” or “wild gas,” after noticing that it came off burning charcoal and fermenting grape juice. Joseph Black later called it “fixed air” after showing that it is released when limestone is heated.",
            "r": "For 10 points, name this gas that plants absorb during photosynthesis and animals breathe out."
        },
        {
            "p": "In 1767, Joseph Priestley invented soda water by hanging a bowl of water above a fermenting vat at a brewery in Leeds, England, where this gas collected. Soft drinks fizz when opened because this gas, dissolved under pressure, comes back out of solution.",
            "r": "Plants take in this gas during photosynthesis. For 10 points, name this gas, whose solid form is called dry ice."
        },
        {
            "p": "Charles David Keeling began measuring this gas at Mauna Loa Observatory in Hawaii in 1958, producing a sawtooth-shaped graph that rises every year. The graph’s yearly zigzag comes from plants in the Northern Hemisphere taking in this gas each spring and summer.",
            "r": "For 10 points, name this greenhouse gas that humans exhale and plants use in photosynthesis."
        },
        {
            "p": "In 1986, a huge cloud of this gas burst out of Lake Nyos in Cameroon and flowed downhill, killing more than 1,700 people, because this gas is heavier than air. Scientists later installed pipes to pull this gas out of the lake’s deep water and prevent another disaster.",
            "r": "This gas turns limewater milky. For 10 points, name this gas, which plants take in during photosynthesis."
        },
        {
            "p": "This substance’s triple point lies at about 5.1 atmospheres, so at normal air pressure it cannot exist as a liquid. Instead, its solid form sublimes directly into a gas at about −78 °C.",
            "r": "That solid is called dry ice. For 10 points, name this compound of one carbon atom and two oxygen atoms."
        },
        {
            "p": "Companies remove caffeine from coffee beans using this compound in a supercritical state, above its critical temperature of about 31 °C. Fire extinguishers filled with this gas smother flames by pushing away the oxygen around them.",
            "r": "Plants take in this gas, and people exhale it. For 10 points, name this greenhouse gas."
        },
        {
            "p": "The enzyme carbonic anhydrase, one of the fastest enzymes known, combines this gas with water in red blood cells to form bicarbonate. Most of this gas travels through the blood as bicarbonate ions until the lungs release it.",
            "r": "For 10 points, name this gas, which people breathe out and plants take in."
        },
        {
            "p": "The Bohr effect describes how higher levels of this gas in the blood make hemoglobin release oxygen more easily. The level of this gas in the blood, more than the level of oxygen, is what mainly controls how fast you breathe.",
            "r": "For 10 points, name this waste gas that you exhale, made during cellular respiration."
        },
        {
            "p": "Stalactites grow in caves when dripping water releases this dissolved gas, causing calcium carbonate to come out of solution. Bubbling this gas through limewater, a solution of calcium hydroxide, turns it milky.",
            "r": "Mixing baking soda and vinegar makes bubbles of this gas. For 10 points, name this gas whose solid form is dry ice."
        },
        {
            "p": "This gas makes up about 96 percent of Venus’s thick atmosphere, causing a runaway greenhouse effect that makes Venus the hottest planet. On Mars, this gas freezes onto the polar caps each winter.",
            "r": "On Earth, plants use this gas in photosynthesis. For 10 points, name this greenhouse gas that people exhale."
        },
        {
            "p": "Kumar Patel invented a powerful infrared laser in 1964 that uses this gas, and such lasers are used to cut metal and wood in factories. This linear molecule is nonpolar even though both of its bonds are polar, because the two bonds’ pulls cancel out.",
            "r": "For 10 points, name this gas made of one carbon and two oxygen atoms."
        },
        {
            "p": "The enzyme RuBisCO [“roo-BISS-koh”], which may be the most abundant protein on Earth, grabs this gas at the start of the Calvin cycle. Cactuses and other CAM plants take in this gas only at night to save water.",
            "r": "For 10 points, name this gas that plants use, along with water, to make sugar during photosynthesis."
        },
        {
            "p": "When this gas dissolves in seawater, it forms carbonic acid, lowering the ocean’s pH and making it harder for corals and shellfish to build their shells. Yeast also releases this gas, which makes bread dough rise.",
            "r": "For 10 points, name this gas, the main greenhouse gas released by burning fossil fuels."
        },
        {
            "p": "In 1856, Eunice Foote showed that a glass cylinder filled with this gas grew hotter in sunlight than one filled with ordinary air. Forty years later, Svante Arrhenius calculated that doubling this gas in the atmosphere would warm Earth by several degrees.",
            "r": "Plants absorb this greenhouse gas. For 10 points, name this gas, whose solid form is called dry ice."
        },
        {
            "p": "After an oxygen tank exploded on Apollo 13 in 1970, the astronauts used tape, plastic bags, and cardboard to make square filters fit a round opening. Those filters used lithium hydroxide to soak up this gas from the cabin air.",
            "r": "For 10 points, name this gas that people breathe out and plants take in."
        }
    ],
    "clues": [
        {
            "id": "formula",
            "tier": "giveaway",
            "t": "A molecule of one carbon atom double-bonded to two oxygen atoms",
            "k": ["two oxygen", "double-bonded"],
            "n": 0
        },
        {
            "id": "exhale",
            "tier": "giveaway",
            "t": "The waste gas people and animals breathe out, made by cellular respiration",
            "k": ["breathe out", "cellular respiration", "waste gas"],
            "n": 0
        },
        {
            "id": "photosynthesis",
            "tier": "giveaway",
            "t": "Plants take it in, with water, to make sugar during photosynthesis",
            "k": ["photosynthesis", "sugar"],
            "n": 0,
            "rabbit": "Photosynthesis"
        },
        {
            "id": "dry-ice",
            "tier": "giveaway",
            "t": "Its solid form is dry ice, which sublimes, turning straight from a solid into a gas",
            "k": ["dry ice", "sublimes"],
            "n": 0
        },
        {
            "id": "greenhouse",
            "tier": "giveaway",
            "t": "The main greenhouse gas released by burning fossil fuels",
            "k": ["greenhouse gas", "fossil fuels"],
            "n": 0
        },
        {
            "id": "fizz",
            "tier": "middle",
            "t": "Dissolved under pressure, it gives soda its fizz; opening the bottle lets it escape",
            "k": ["fizz", "soda", "pressure"],
            "n": 0,
            "rabbit": "Henry’s law"
        },
        {
            "id": "limewater",
            "tier": "middle",
            "t": "Turns limewater (calcium hydroxide solution) milky by forming calcium carbonate",
            "k": ["limewater", "milky", "calcium carbonate"],
            "n": 0
        },
        {
            "id": "baking-soda",
            "tier": "middle",
            "t": "Baking soda and vinegar make bubbles of it, and yeast releases it to make bread rise",
            "k": ["baking soda", "vinegar", "yeast"],
            "n": 0
        },
        {
            "id": "heavier",
            "tier": "middle",
            "t": "Heavier than air, so fire extinguishers use it to smother flames",
            "k": ["heavier than air", "fire extinguishers"],
            "n": 0
        },
        {
            "id": "carbonic",
            "tier": "middle",
            "t": "Dissolves in water to form carbonic acid, which lowers the ocean’s pH",
            "k": ["carbonic acid", "ocean"],
            "n": 0
        },
        {
            "id": "keeling",
            "tier": "middle",
            "t": "Charles David Keeling began measuring it at Mauna Loa, Hawaii, in 1958, producing the Keeling Curve",
            "k": ["keeling", "mauna loa", "1958"],
            "n": 0
        },
        {
            "id": "venus",
            "tier": "middle",
            "t": "Makes up about 96% of Venus’s atmosphere, causing a runaway greenhouse effect; it freezes onto Mars’s polar caps",
            "k": ["venus", "runaway", "polar caps"],
            "n": 0,
            "rabbit": "Venus (planet)"
        },
        {
            "id": "linear",
            "tier": "middle",
            "t": "A linear molecule that is nonpolar because the pulls of its two polar bonds cancel",
            "k": ["linear", "nonpolar", "cancel"],
            "n": 0
        },
        {
            "id": "van-helmont",
            "tier": "power",
            "t": "Jan Baptist van Helmont called it “gas sylvestre,” or “wild gas”",
            "k": ["van helmont", "gas sylvestre", "wild gas"],
            "n": 0
        },
        {
            "id": "black",
            "tier": "power",
            "t": "Joseph Black called it “fixed air” in the 1750s after releasing it from heated limestone",
            "k": ["joseph black", "fixed air", "limestone"],
            "n": 0
        },
        {
            "id": "priestley",
            "tier": "power",
            "t": "Joseph Priestley invented soda water in 1767 using it from a brewery in Leeds, England",
            "k": ["priestley", "soda water", "1767"],
            "n": 0
        },
        {
            "id": "triple-point",
            "tier": "power",
            "t": "Its triple point is about 5.1 atmospheres, so it has no liquid form at normal pressure; it sublimes at about −78 °C",
            "k": ["triple point", "5.1 atmospheres", "−78"],
            "n": 0
        },
        {
            "id": "supercritical",
            "tier": "power",
            "t": "Above about 31 °C and high pressure it becomes supercritical, a form used to decaffeinate coffee",
            "k": ["supercritical", "decaffeinate", "31"],
            "n": 0
        },
        {
            "id": "nyos",
            "tier": "power",
            "t": "In 1986, a cloud of it burst from Lake Nyos in Cameroon, and more than 1,700 people died",
            "k": ["lake nyos", "cameroon", "1986"],
            "n": 0
        },
        {
            "id": "carbonic-anhydrase",
            "tier": "power",
            "t": "The enzyme carbonic anhydrase turns it and water into bicarbonate in red blood cells",
            "k": ["carbonic anhydrase", "bicarbonate"],
            "n": 0,
            "rabbit": "Red blood cells"
        },
        {
            "id": "bohr-effect",
            "tier": "power",
            "t": "The Bohr effect: more of it in the blood makes hemoglobin release oxygen",
            "k": ["bohr effect", "hemoglobin"],
            "n": 0,
            "rabbit": "Hemoglobin"
        },
        {
            "id": "rubisco",
            "tier": "power",
            "t": "RuBisCO, perhaps the most abundant protein on Earth, grabs it at the start of the Calvin cycle",
            "k": ["rubisco", "calvin cycle"],
            "n": 0,
            "rabbit": "Calvin cycle"
        },
        {
            "id": "cam",
            "tier": "power",
            "t": "CAM plants, like cactuses, take it in only at night to save water",
            "k": ["cam plants", "night", "cactuses"],
            "n": 0
        },
        {
            "id": "patel",
            "tier": "power",
            "t": "Kumar Patel invented a powerful infrared laser using it in 1964",
            "k": ["patel", "laser", "1964"],
            "n": 0,
            "rabbit": "Lasers"
        },
        {
            "id": "foote-arrhenius",
            "tier": "power",
            "t": "Eunice Foote (1856) showed it traps the Sun’s heat; Svante Arrhenius (1896) calculated how doubling it would warm Earth",
            "k": ["eunice foote", "arrhenius", "1856"],
            "n": 0
        },
        {
            "id": "apollo-13",
            "tier": "power",
            "t": "Apollo 13’s crew rigged square lithium hydroxide filters into a round opening to remove it from their air",
            "k": ["apollo 13", "lithium hydroxide"],
            "n": 0
        },
        {
            "id": "stalactites",
            "tier": "power",
            "t": "Stalactites grow when dripping cave water releases it, leaving calcium carbonate behind",
            "k": ["stalactites", "cave"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Not carbon monoxide!",
        "body": "Carbon monoxide, CO, has just one oxygen atom, and it is a poisonous gas made when fuel burns without enough oxygen. Its name differs from this compound’s by only a few letters, so a rushed buzz can lose the tossup. Dry ice is a second trap: it is this compound’s solid form, so saying “dry ice” may only earn a prompt.",
        "fix": "Count the oxygens in the clues: photosynthesis, exhaling, soda fizz, limewater, and the greenhouse effect mean this compound. Carbon monoxide clues talk about car exhaust, binding tightly to hemoglobin, and home detectors that beep. If you are prompted after saying “dry ice,” give the compound’s name.",
        "line": "Real answer line: <b><u>Carbon dioxide</u></b> (accept <u>CO2</u>; prompt on <u>dry ice</u>; do not accept “carbon monoxide”)"
    },
    "tests": {
        "right": [
            "Carbon dioxide",
            "CO2",
            "carbon dioxde",
            "Carbon dioxide gas",
            "co 2"
        ],
        "prompt": [
            "Dry ice"
        ],
        "wrong": [
            "Carbon monoxide",
            "CO",
            "Methane",
            "Oxygen",
            "Carbonic acid",
            "Sulfur dioxide",
            "Carbon"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
