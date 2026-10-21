import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

LINE = "<b><u>Samson</u></b> (accept <u>Shimshon</u>; do not accept “Delilah”)"

data = {
    "id": "samson",
    "name": "Samson",
    "mono": "SAM",
    "category": "Religion",
    "qbCategory": "Religion",
    "kicker": "Strongman of the Book of Judges · His strength lay in his uncut hair",
    "dates": "Era of the judges, c. 1200–1000 BCE",
    "briefing": "In the Book of Judges, Samson is an Israelite strongman whose power is tied to his hair: before he was born, an angel declared that no razor must ever touch his head. He tears apart a lion with his bare hands, strikes down a thousand Philistines with a donkey’s jawbone, and carries off a city’s gates, until Delilah learns his secret and has his hair cut. Blinded and imprisoned, he prays for strength one last time and pulls down the temple of Dagon.",
    "answerHtml": LINE,
    "accept": [
        "samson",
        "shimshon"
    ],
    "prompt": [],
    "reject": [
        "delilah",
        "delila",
        "dalila",
        "samson and delilah",
        "samson et dalila",
        "samson agonistes",
        "samson carrasco",
        "manoah",
        "manoa",
        "samuel",
        "saul",
        "solomon",
        "david",
        "goliath",
        "gideon",
        "deborah",
        "jephthah",
        "barak",
        "ehud",
        "eli",
        "harapha",
        "dagon",
        "philistines",
        "nazirite",
        "hercules",
        "heracles"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Samson",
    "qb": {
        "q": "Samson",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "An angel told this man’s mother, the wife of Manoah [“muh-NOH-uh”], that she must not drink wine and that no razor could ever touch her son’s head. When Manoah later offered a sacrifice, the angel rose toward heaven in the flame from the altar.",
            "r": "Her son, a Nazirite from birth, grew up to fight the Philistines. For 10 points, name this biblical strongman whose strength was tied to his uncut hair."
        },
        {
            "p": "At his wedding feast, this man challenged thirty guests with the riddle “Out of the eater, something to eat; out of the strong, something sweet.” After they pressured his bride into telling them the answer, he complained, “If you had not plowed with my heifer, you would not have solved my riddle.”",
            "r": "The answer was honey that he had found in the body of a lion. For 10 points, name this strongman from the Book of Judges."
        },
        {
            "p": "Tins of Lyle’s Golden Syrup show bees swarming around a lion’s body above the words “Out of the strong came forth sweetness,” a line from this man’s story. In that story, he found bees and honey inside a lion that he had earlier torn apart with his bare hands.",
            "r": "For 10 points, name this Nazirite from the Book of Judges whose hair was cut off while he slept on Delilah’s lap."
        },
        {
            "p": "After his father-in-law gave his wife to another man, this man caught three hundred foxes, tied them tail to tail in pairs with a torch between each pair of tails, and set them loose in the Philistines’ fields, burning their grain, vineyards, and olive groves.",
            "r": "Earlier, he had torn apart a lion with his bare hands. For 10 points, name this strongman who was later betrayed by Delilah."
        },
        {
            "p": "After a battle at a place called Ramath Lehi [“RAY-muth LEE-hy”], or “Jawbone Hill,” this man was so thirsty that he called out to God, and water poured out of a hollow place in the ground.",
            "r": "In that battle, he had struck down a thousand Philistines with the jawbone of a donkey. For 10 points, name this strongman whose strength came from his uncut hair."
        },
        {
            "p": "When the people of Gaza waited at the city gate to ambush this man at dawn, he got up at midnight, tore the doors of the gate loose along with the two posts, and carried them on his shoulders to the top of a hill facing Hebron.",
            "r": "Later, the Philistines held him prisoner in that same city after Delilah betrayed him. For 10 points, name this strongman from the Book of Judges."
        },
        {
            "p": "The rulers of the Philistines each promised a woman from the Valley of Sorek [“SOR-ek”] eleven hundred pieces of silver to learn the secret of this man’s strength. He fooled her three times, claiming he could be held by seven fresh bowstrings, then by new ropes, and then by weaving his seven braids into a loom.",
            "r": "Finally he told that woman, Delilah, the truth about his uncut hair. For 10 points, name this strongman."
        },
        {
            "p": "About three thousand people were watching from the roof of a temple when this blinded prisoner was brought out to entertain the crowd, and he asked the servant leading him by the hand to let him feel the pillars that held up the building.",
            "r": "That temple belonged to the god Dagon. Praying for strength one last time, he pushed against its two central pillars and brought the temple down on himself and the Philistines. For 10 points, name this strongman."
        },
        {
            "p": "In a dramatic poem by John Milton, this man laments that he is “Eyeless in Gaza at the mill with slaves,” a phrase that Aldous Huxley later used as the title of a novel. In that poem, a boastful giant named Harapha [“HAR-uh-fuh”] taunts this man, and his father, Manoa, tries to buy his freedom.",
            "r": "In the Bible, he loses his strength when Delilah has his hair cut. For 10 points, name this hero of the Book of Judges."
        },
        {
            "p": "In an opera by Camille Saint-Saëns [“san-SAHNS”], a woman sings the aria “My heart opens to your voice” to win over this man, and the last act features a wild dance called the Bacchanale [“bah-kuh-NAHL”]. Franz Liszt helped arrange that opera’s 1877 premiere in Weimar [“VY-mar”].",
            "r": "For 10 points, name this biblical strongman who loses his strength when the opera’s title woman, Dalila, has his hair cut."
        },
        {
            "p": "Peter Paul Rubens painted this man asleep in a woman’s lap while a man carefully cuts his hair by candlelight and soldiers wait at the door. That painting hangs in London’s National Gallery.",
            "r": "In the Bible, this Nazirite lost his great strength once his hair was cut. For 10 points, name this man who was betrayed by Delilah."
        },
        {
            "p": "George Frideric Handel based an oratorio about this man on a poem by John Milton, and it includes the soprano aria “Let the bright Seraphim.” In the New Testament, the Letter to the Hebrews names this man among heroes of faith, along with Gideon, Barak, and Jephthah [“JEF-thuh”].",
            "r": "For 10 points, name this Nazirite whose strength left him after Delilah had his hair cut."
        },
        {
            "p": "This man’s parents asked why he wanted to marry a Philistine woman from Timnah [“TIM-nuh”] instead of a woman from his own people. On the way to Timnah, a young lion came roaring toward him, and he tore it apart with his bare hands.",
            "r": "He later posed a riddle about that lion at his wedding feast. For 10 points, name this Israelite judge whose uncut hair gave him great strength."
        },
        {
            "p": "This man was buried between Zorah [“ZOR-uh”] and Eshtaol [“ESH-tay-ol”] in the tomb of his father, Manoah, after leading Israel for twenty years. The Book of Judges says that he killed more Philistines when he died than he had while he lived.",
            "r": "He had been dedicated to God as a Nazirite, so no razor was ever supposed to touch his head. For 10 points, name this strongman."
        },
        {
            "p": "After attacking the Philistines, this man went to live in a cave in the rock of Etam [“EE-tum”], where three thousand men of Judah came to tie him up and hand him over to the Philistines. He let them bind him with two new ropes, but when the Philistines rushed at him, the ropes fell from his arms like burned flax.",
            "r": "He then struck down a thousand Philistines with the jawbone of a donkey. For 10 points, name this strongman."
        }
    ],
    "clues": [
        {
            "id": "uncut-hair",
            "tier": "giveaway",
            "t": "His great strength was tied to his uncut hair",
            "k": ["uncut hair", "strength", "hair"],
            "n": 0
        },
        {
            "id": "delilah",
            "tier": "giveaway",
            "t": "Delilah learned his secret and had his hair cut off while he slept, so his strength left him",
            "k": ["delilah", "secret", "slept"],
            "n": 0
        },
        {
            "id": "judges",
            "tier": "giveaway",
            "t": "A strongman and leader of Israel in the Book of Judges, in the Hebrew Bible (Old Testament)",
            "k": ["book of judges", "judges", "strongman"],
            "n": 0
        },
        {
            "id": "philistines",
            "tier": "giveaway",
            "t": "Fought the Philistines, enemies of the Israelites",
            "k": ["philistines", "israelites"],
            "n": 0
        },
        {
            "id": "dagon",
            "tier": "giveaway",
            "t": "Blinded and captured, he pushed down the pillars of the temple of Dagon, killing himself and the Philistines inside",
            "k": ["dagon", "pillars", "temple"],
            "n": 0
        },
        {
            "id": "nazirite",
            "tier": "middle",
            "t": "Dedicated to God as a Nazirite from birth, so no razor could touch his head",
            "k": ["nazirite", "razor"],
            "n": 0
        },
        {
            "id": "lion",
            "tier": "middle",
            "t": "Tore apart a young lion with his bare hands on the way to Timnah",
            "k": ["lion", "bare hands", "timnah"],
            "n": 0
        },
        {
            "id": "riddle",
            "tier": "middle",
            "t": "Wedding riddle: “Out of the eater, something to eat; out of the strong, something sweet” (honey in the lion)",
            "k": ["riddle", "honey", "something sweet"],
            "n": 0
        },
        {
            "id": "jawbone",
            "tier": "middle",
            "t": "Struck down a thousand Philistines with the jawbone of a donkey",
            "k": ["jawbone", "donkey", "thousand"],
            "n": 0
        },
        {
            "id": "foxes",
            "tier": "middle",
            "t": "Tied torches between the tails of 300 foxes, in pairs, and sent them into the Philistines’ fields",
            "k": ["foxes", "torches", "300"],
            "n": 0
        },
        {
            "id": "gaza-gates",
            "tier": "middle",
            "t": "Carried off the doors and posts of Gaza’s city gate to a hill facing Hebron",
            "k": ["gaza", "city gate", "hebron"],
            "n": 0
        },
        {
            "id": "blinded",
            "tier": "middle",
            "t": "The Philistines blinded him and made him grind grain in a prison in Gaza",
            "k": ["blinded", "grind grain", "prison"],
            "n": 0
        },
        {
            "id": "manoah",
            "tier": "middle",
            "t": "Son of Manoah, of the tribe of Dan; an angel announced his birth to his mother",
            "k": ["manoah", "tribe of dan", "angel"],
            "n": 0
        },
        {
            "id": "saint-saens",
            "tier": "power",
            "t": "Camille Saint-Saëns’s 1877 opera about him: Dalila sings “My heart opens to your voice,” and Liszt helped arrange its premiere in Weimar",
            "k": ["saint-saëns", "dalila", "my heart opens", "weimar"],
            "n": 0
        },
        {
            "id": "milton",
            "tier": "power",
            "t": "In John Milton’s dramatic poem about him, he is “Eyeless in Gaza at the mill with slaves,” and the giant Harapha taunts him",
            "k": ["milton", "eyeless in gaza", "harapha"],
            "n": 0
        },
        {
            "id": "lyle",
            "tier": "power",
            "t": "Lyle’s Golden Syrup tins show bees around a lion with the words “Out of the strong came forth sweetness”",
            "k": ["lyle", "golden syrup", "bees"],
            "n": 0
        },
        {
            "id": "heifer",
            "tier": "power",
            "t": "Told his wedding guests, “If you had not plowed with my heifer, you would not have solved my riddle”",
            "k": ["heifer", "plowed"],
            "n": 0
        },
        {
            "id": "sorek",
            "tier": "power",
            "t": "Each Philistine ruler offered Delilah, of the Valley of Sorek, 1,100 pieces of silver for his secret",
            "k": ["sorek", "silver", "1,100"],
            "n": 0
        },
        {
            "id": "false-answers",
            "tier": "power",
            "t": "His false answers to Delilah: seven fresh bowstrings, new ropes, and weaving his seven braids into a loom",
            "k": ["bowstrings", "new ropes", "loom", "seven braids"],
            "n": 0
        },
        {
            "id": "ramath-lehi",
            "tier": "power",
            "t": "At Ramath Lehi (“Jawbone Hill”), God made water pour from a hollow in the ground when he was thirsty",
            "k": ["ramath lehi", "jawbone hill", "thirsty"],
            "n": 0
        },
        {
            "id": "etam",
            "tier": "power",
            "t": "Lived in a cave in the rock of Etam; 3,000 men of Judah tied him with new ropes, which fell off like burned flax",
            "k": ["etam", "men of judah", "flax"],
            "n": 0
        },
        {
            "id": "roof",
            "tier": "power",
            "t": "About 3,000 people watched from the temple roof; he asked the servant leading him to let him feel the pillars",
            "k": ["roof", "servant", "3,000"],
            "n": 0
        },
        {
            "id": "burial",
            "tier": "power",
            "t": "Led Israel 20 years and was buried between Zorah and Eshtaol in his father Manoah’s tomb",
            "k": ["zorah", "eshtaol", "20 years"],
            "n": 0
        },
        {
            "id": "hebrews-handel",
            "tier": "power",
            "t": "Hebrews 11 lists him among heroes of faith with Gideon, Barak, and Jephthah; Handel wrote an oratorio about him",
            "k": ["hebrews", "gideon", "jephthah", "handel", "oratorio"],
            "n": 0
        },
        {
            "id": "rubens",
            "tier": "power",
            "t": "Rubens painted him asleep in Delilah’s lap as a man cuts his hair (National Gallery, London)",
            "k": ["rubens", "national gallery", "asleep"],
            "n": 0
        },
        {
            "id": "angel-flame",
            "tier": "power",
            "t": "When Manoah offered a sacrifice, the angel who announced the birth rose toward heaven in the altar’s flame",
            "k": ["flame", "altar", "sacrifice"],
            "n": 0
        }
    ],
    "trap": {
        "title": "The strongman, not Delilah",
        "body": "Many Samson clues are really about the people around him, so early buzzers grab the wrong name. Delilah is the woman who betrayed him, and Manoah is his father. Gideon and Jephthah are other judges in the same book, and Samuel, whose name starts the same way, is the later judge who anointed Saul as king. A question can also ask for a work about him, such as Milton’s _Samson Agonistes_ or Saint-Saëns’s opera _Samson et Dalila_.",
        "fix": "If the question says “this man” or “this judge” and mentions long hair, a lion, foxes, a jawbone, or pillars, say Samson. Say Delilah only for “this woman.” If it asks for “this poem” or “this opera,” give the title instead.",
        "line": "Real answer line: " + LINE
    },
    "tests": {
        "right": [
            "Samson",
            "Sampson",
            "Shimshon",
            "Samsom",
            "Judge Samson"
        ],
        "prompt": [],
        "wrong": [
            "Delilah",
            "Samuel",
            "Saul",
            "Gideon",
            "Goliath",
            "Hercules",
            "Samson and Delilah",
            "Solomon"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
