import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "henrys-law",
    "name": "Henry’s law",
    "mono": "HL",
    "category": "Chemistry",
    "qbCategory": "Science · Chemistry",
    "kicker": "More pressure, more dissolved gas · Why soda fizzes and divers get the bends",
    "dates": "Stated by William Henry, 1803",
    "briefing": "Henry’s law, described by English chemist William Henry in 1803, says that the harder a gas presses on a liquid, the more of that gas dissolves into it. Soda makers force carbon dioxide into drinks under high pressure, so when you twist off the cap, the pressure drops and the gas fizzes back out. The same law explains the bends, a painful condition caused by nitrogen bubbles in a diver’s blood after rising to the surface too fast.",
    "answerHtml": "<b><u>Henry’s law</u></b> (prompt on <u>Henry</u>)",
    "accept": [
        "henrys law",
        "henry law",
        "henrys gas law"
    ],
    "prompt": [
        "henry",
        "henrys"
    ],
    "reject": [
        "raoults law",
        "raoult law",
        "daltons law",
        "dalton law",
        "law of partial pressures",
        "boyles law",
        "boyle law",
        "charless law",
        "charles law",
        "gay lussacs law",
        "grahams law",
        "ficks law",
        "hesss law",
        "hess law",
        "hesses law",
        "ideal gas law",
        "avogadros law",
        "sieverts law",
        "le chateliers principle",
        "hookes law",
        "solubility",
        "henry clay"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Henry%27s_law",
    "qb": {
        "q": "Henry's law",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In an 1803 paper, a chemist from Manchester, England, described experiments measuring how much of several gases water would absorb at different temperatures and pressures. The rule he found works best for dilute solutions of gases that do not react with the liquid.",
            "r": "For 10 points, name this gas law stating that the amount of a gas that dissolves in a liquid is proportional to that gas’s partial pressure."
        },
        {
            "p": "Washington Roebling, the chief engineer of the Brooklyn Bridge, fell seriously ill with “caisson disease” after working in pressurized chambers deep under the East River. This law explains that illness: under high pressure, extra nitrogen dissolved in the workers’ blood, then formed bubbles when they returned to normal pressure too quickly.",
            "r": "This law also explains why soda fizzes when it is opened. For 10 points, name this law about how gases dissolve in liquids."
        },
        {
            "p": "In 1986, a deadly cloud of carbon dioxide burst out of Lake Nyos in Cameroon, whose deep water had held huge amounts of the dissolved gas under high pressure. This law’s constant depends on temperature, and warm liquids hold less dissolved gas than cold ones.",
            "r": "For 10 points, name this law which says that a gas’s solubility in a liquid is proportional to its partial pressure."
        },
        {
            "p": "In a very dilute solution, the solvent follows Raoult’s [“rah-OOLZ”] law, but a dissolved gas follows this other law, which has its own proportionality constant. This law works poorly for gases such as ammonia and hydrogen chloride, which react with water.",
            "r": "For 10 points, name this law that explains why a bottle of soda fizzes when it is opened."
        },
        {
            "p": "Sieverts’ law, a variation of this law for gases like hydrogen dissolving into metals, says that their solubility grows with the square root of the pressure instead. This law itself is exact only for very dilute solutions, so it is called a “limiting law.”",
            "r": "For 10 points, name this gas law, which explains why scuba divers who rise too quickly can get the bends."
        },
        {
            "p": "Hyperbaric oxygen chambers rely on this law: raising the pressure around a patient who is breathing pure oxygen makes more oxygen dissolve in the patient’s blood. This law’s constant, written k-sub-H, is different for each pairing of a gas and a liquid.",
            "r": "Those chambers also treat divers who have the bends. For 10 points, name this law relating gas solubility to partial pressure."
        },
        {
            "p": "As carbon dioxide builds up in the atmosphere, this law predicts that more of it will dissolve into seawater, making the oceans more acidic. This law’s constant also depends on temperature, which is why warm water holds less dissolved oxygen for fish.",
            "r": "For 10 points, name this law that explains why soda fizzes when you twist off the cap and release the pressure."
        },
        {
            "p": "On a high mountain, the partial pressure of oxygen is low, so less oxygen dissolves in a climber’s blood plasma, as this law predicts. In a dilute solution, a dissolved gas follows this law, while the solvent follows Raoult’s [“rah-OOLZ”] law instead.",
            "r": "For 10 points, name this law that explains the bends, which can strike divers who rise to the surface too quickly."
        },
        {
            "p": "Environmental chemists use this law’s constant to predict how a pollutant will divide itself between a lake’s water and the air above it. That constant has a different value for every pairing of a gas and a liquid, and it changes with temperature.",
            "r": "For 10 points, name this gas solubility law, which explains why an open bottle of soda slowly goes flat."
        },
        {
            "p": "This law’s constant, written k-sub-H, changes with temperature: warm water holds less dissolved gas than cold water. That is why tiny bubbles of air appear on the sides of a pot of water long before it boils.",
            "r": "This law is often written C equals k P. For 10 points, name this law relating how much gas dissolves in a liquid to that gas’s partial pressure."
        },
        {
            "p": "Divers who breathe “nitrox,” an air mixture with extra oxygen and less nitrogen, absorb less nitrogen at depth, as this law predicts. Because each gas in air dissolves according to its own partial pressure, this law is often used together with Dalton’s law.",
            "r": "For 10 points, name this law which explains why scuba divers who surface too quickly can get the bends."
        },
        {
            "p": "Gas molecules constantly enter and leave the surface of a liquid, and once they do so at equal rates, this law gives the amount of gas that is dissolved. Champagne and soft drinks are bottled under high carbon dioxide pressure so that extra gas dissolves in them.",
            "r": "For 10 points, name this law which says that the solubility of a gas is directly proportional to its partial pressure."
        },
        {
            "p": "Every 10 meters of seawater adds about one atmosphere of pressure, so a diver breathing compressed air deep underwater absorbs extra nitrogen into the blood. To let that gas escape gradually, divers rise slowly and pause at decompression stops.",
            "r": "For 10 points, name this law which explains both the bends and the fizz that escapes when a soda bottle is opened."
        },
        {
            "p": "Ammonia and hydrogen chloride do not follow this law well, because those gases react with the water they dissolve in. A chemist from Manchester, the English city where John Dalton worked, first stated this law in 1803.",
            "r": "For 10 points, name this law which explains why carbon dioxide bubbles out of a soda when the bottle is opened."
        },
        {
            "p": "Power plants that release warm water into rivers can harm fish, since warmer water holds less dissolved oxygen, an effect built into the temperature dependence of this law’s constant. That constant is different for every gas, so oxygen and carbon dioxide dissolve in very different amounts.",
            "r": "For 10 points, name this law stating that the amount of a gas that dissolves in a liquid is proportional to the gas’s partial pressure."
        }
    ],
    "clues": [
        {
            "id": "definition",
            "tier": "giveaway",
            "t": "The amount of a gas that dissolves in a liquid is directly proportional to that gas’s partial pressure above the liquid",
            "k": ["partial pressure", "dissolves", "proportional"],
            "n": 0
        },
        {
            "id": "soda",
            "tier": "giveaway",
            "t": "Explains why soda fizzes when opened: releasing the pressure lets dissolved carbon dioxide escape as bubbles",
            "k": ["soda", "fizzes", "carbon dioxide"],
            "n": 0,
            "rabbit": "Carbon dioxide"
        },
        {
            "id": "bends",
            "tier": "giveaway",
            "t": "Explains the bends: divers who rise too fast form nitrogen bubbles in their blood",
            "k": ["bends", "divers", "nitrogen bubbles"],
            "n": 0
        },
        {
            "id": "gas-law",
            "tier": "giveaway",
            "t": "A gas law about solubility: more pressure pushes more gas into a liquid",
            "k": ["solubility", "more pressure"],
            "n": 0,
            "rabbit": "Solubility"
        },
        {
            "id": "formula",
            "tier": "middle",
            "t": "Often written C = kP: the dissolved concentration equals a constant times the gas’s partial pressure",
            "k": ["concentration", "constant", "c = kp"],
            "n": 0
        },
        {
            "id": "temperature",
            "tier": "middle",
            "t": "Its constant depends on temperature: warm liquids hold less dissolved gas, so warm soda goes flat faster",
            "k": ["temperature", "goes flat", "warm"],
            "n": 0
        },
        {
            "id": "bottling",
            "tier": "middle",
            "t": "Soft drinks and champagne are bottled under high carbon dioxide pressure to pack in extra gas",
            "k": ["champagne", "bottled", "soft drinks"],
            "n": 0
        },
        {
            "id": "decompression",
            "tier": "middle",
            "t": "Divers rise slowly and pause at decompression stops so dissolved nitrogen can leave the blood gradually",
            "k": ["decompression stops", "rise slowly"],
            "n": 0
        },
        {
            "id": "dalton",
            "tier": "middle",
            "t": "Each gas in a mixture like air dissolves by its own partial pressure, so it pairs with Dalton’s law of partial pressures",
            "k": ["dalton", "mixture", "air"],
            "n": 0,
            "rabbit": "Dalton’s law"
        },
        {
            "id": "pot-bubbles",
            "tier": "middle",
            "t": "Tiny air bubbles form in a pot of water long before it boils, since warmer water holds less dissolved gas",
            "k": ["air bubbles", "pot of water", "boils"],
            "n": 0
        },
        {
            "id": "fish",
            "tier": "middle",
            "t": "Warm water holds less dissolved oxygen, so warm water released by power plants (thermal pollution) can harm fish",
            "k": ["thermal pollution", "dissolved oxygen", "fish"],
            "n": 0
        },
        {
            "id": "manchester",
            "tier": "power",
            "t": "Its namesake, a chemist from Manchester, England (where John Dalton worked), stated it in an 1803 paper on how much gas water absorbs",
            "k": ["manchester", "1803", "john dalton", "absorbs"],
            "n": 0,
            "rabbit": "John Dalton"
        },
        {
            "id": "roebling",
            "tier": "power",
            "t": "Washington Roebling, chief engineer of the Brooklyn Bridge, fell ill with “caisson disease” (the bends) after working in pressurized chambers",
            "k": ["roebling", "brooklyn bridge", "caisson disease"],
            "n": 0,
            "rabbit": "Brooklyn Bridge"
        },
        {
            "id": "lake-nyos",
            "tier": "power",
            "t": "In 1986, a deadly cloud of carbon dioxide burst from Lake Nyos in Cameroon, whose deep water held huge amounts of the dissolved gas",
            "k": ["lake nyos", "cameroon", "1986"],
            "n": 0
        },
        {
            "id": "raoult",
            "tier": "power",
            "t": "In a dilute solution, the dissolved gas follows it, while the solvent follows Raoult’s law",
            "k": ["raoult", "solvent", "dilute"],
            "n": 0,
            "rabbit": "Raoult’s law"
        },
        {
            "id": "limiting",
            "tier": "power",
            "t": "A “limiting law”: exact only for very dilute solutions",
            "k": ["limiting", "very dilute"],
            "n": 0
        },
        {
            "id": "reacting-gases",
            "tier": "power",
            "t": "Works poorly for gases that react with water, such as ammonia and hydrogen chloride",
            "k": ["ammonia", "hydrogen chloride", "react"],
            "n": 0,
            "rabbit": "Ammonia"
        },
        {
            "id": "sieverts",
            "tier": "power",
            "t": "Sieverts’ law, a variation for gases like hydrogen dissolving in metals, uses the square root of the pressure",
            "k": ["sieverts", "square root", "metals"],
            "n": 0
        },
        {
            "id": "k-sub-h",
            "tier": "power",
            "t": "Its constant, written k-sub-H, has a different value for each pairing of a gas and a liquid",
            "k": ["k-sub-h", "each pairing"],
            "n": 0
        },
        {
            "id": "pollutants",
            "tier": "power",
            "t": "Environmental chemists use its constant to predict how a pollutant divides between water and the air above it",
            "k": ["pollutant", "environmental"],
            "n": 0
        },
        {
            "id": "oceans",
            "tier": "power",
            "t": "As carbon dioxide builds up in the air, more of it dissolves into seawater, making the oceans more acidic",
            "k": ["oceans", "acidic", "seawater"],
            "n": 0
        },
        {
            "id": "altitude",
            "tier": "power",
            "t": "On a high mountain, the low partial pressure of oxygen means less oxygen dissolves in blood plasma",
            "k": ["mountain", "plasma", "altitude"],
            "n": 0
        },
        {
            "id": "hyperbaric",
            "tier": "power",
            "t": "Hyperbaric chambers raise the pressure so more oxygen dissolves in a patient’s blood; they also treat the bends",
            "k": ["hyperbaric", "chambers"],
            "n": 0
        },
        {
            "id": "depth",
            "tier": "power",
            "t": "Every 10 meters of seawater adds about one atmosphere of pressure, so deep divers absorb extra nitrogen",
            "k": ["10 meters", "one atmosphere", "seawater"],
            "n": 0
        },
        {
            "id": "surface-balance",
            "tier": "power",
            "t": "Gas molecules enter and leave a liquid’s surface; once the rates are equal, it gives how much gas is dissolved",
            "k": ["surface", "rates are equal"],
            "n": 0
        },
        {
            "id": "nitrox",
            "tier": "power",
            "t": "Divers who breathe “nitrox,” a mixture with extra oxygen and less nitrogen, absorb less nitrogen at depth",
            "k": ["nitrox", "less nitrogen"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Which gas law?",
        "body": "Chemistry has a crowd of laws named for people, and several of them involve pressure. Boyle’s law links a gas’s pressure and volume, Dalton’s law says partial pressures add up to the total pressure, and Raoult’s law is about the vapor pressure of the solvent in a solution. Players who hear “partial pressure” and buzz with Dalton’s law lose the tossup.",
        "fix": "This law is the one about how much gas dissolves in a liquid. Soda fizz, divers and the bends, dissolved oxygen in warm water, and “solubility is proportional to partial pressure” all mean this law. Say the full name, with “law” at the end.",
        "line": "Real answer line: <b><u>Henry’s law</u></b> (prompt on <u>Henry</u>)"
    },
    "tests": {
        "right": [
            "Henry’s law",
            "Henry's Law",
            "henrys law",
            "Henry law",
            "Henerys law"
        ],
        "prompt": [
            "Henry"
        ],
        "wrong": [
            "Raoult's law",
            "Dalton's law",
            "Boyle's law",
            "Hess's law",
            "Charles's law",
            "Henry Clay"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
