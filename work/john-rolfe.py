import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

data = {
    "id": "john-rolfe",
    "name": "John Rolfe",
    "mono": "JR",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Jamestown tobacco planter · Husband of Pocahontas",
    "dates": "c. 1585–1622",
    "briefing": "On his way to Jamestown, John Rolfe was shipwrecked on Bermuda, then reached a colony that had found nothing worth selling in England. Around 1612, he planted a sweeter kind of tobacco from seeds that came from Spanish colonies, and it soon sold for high prices in London, saving Virginia’s economy. In 1614, he married Pocahontas, the daughter of Powhatan, and their wedding brought several years of peace.",
    "answerHtml": "<b><u>John Rolfe</u></b> (prompt on <u>Rolfe</u>; do not accept “John Smith” or “Thomas Rolfe”)",
    "accept": [
        "john rolfe",
        "mister john rolfe",
        "master john rolfe"
    ],
    "prompt": [
        "rolfe",
        "mr rolfe"
    ],
    "reject": [
        "john smith",
        "captain john smith",
        "thomas rolfe",
        "rebecca rolfe",
        "lady rebecca",
        "pocahontas",
        "powhatan",
        "opechancanough",
        "thomas dale",
        "samuel argall",
        "thomas gates",
        "christopher newport",
        "john ratcliffe",
        "edwin sandys",
        "george yeardley",
        "lord de la warr",
        "william strachey"
    ],
    "tests": {
        "right": [
            "John Rolfe",
            "Jon Rolfe",
            "john rolf",
            "Mr. John Rolfe"
        ],
        "prompt": [
            "Rolfe"
        ],
        "wrong": [
            "John Smith",
            "Captain John Smith",
            "Powhatan",
            "Thomas Rolfe",
            "Pocahontas",
            "Rebecca Rolfe",
            "Thomas Dale"
        ]
    },
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/John_Rolfe",
    "qb": {
        "q": "John Rolfe",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "William Strachey’s account of a 1609 shipwreck records the christening of this man’s baby daughter, who was named Bermuda after the island where she was born. The baby died there before the castaways could leave the island.",
            "r": "This man later began growing a sweeter kind of tobacco in Virginia. For 10 points, name this Jamestown colonist who married Pocahontas."
        },
        {
            "p": "This man was among the castaways who built two small boats, the _Deliverance_ and the _Patience_, on Bermuda and sailed them to Jamestown in 1610. A few years later, he planted seeds from Spanish colonies that grew a milder leaf than the kind the Powhatan grew.",
            "r": "For 10 points, name this colonist who made tobacco Virginia’s cash crop and married Pocahontas in 1614."
        },
        {
            "p": "In a letter to Sir Edwin Sandys of the Virginia Company, this colony secretary reported that a ship had arrived at Point Comfort in 1619 and traded about 20 Africans for food, the first recorded enslaved Africans in English Virginia.",
            "r": "Years earlier, he had married Pocahontas. For 10 points, name this Jamestown colonist who first grew tobacco for export."
        },
        {
            "p": "This widower wrote a long letter to Sir Thomas Dale explaining why he wished to marry a young woman who was being held by the English at Henricus and had recently become a Christian. Their wedding in April 1614 began several years of peace between the colonists and her father’s people.",
            "r": "That woman was Pocahontas. For 10 points, name this tobacco planter who married her."
        },
        {
            "p": "Christian Bale played this man in Terrence Malick’s 2005 film _The New World_, which shows him marrying a Native woman who had earlier befriended John Smith. In real life, this man brought his wife to England, where she met King James I.",
            "r": "For 10 points, name this Jamestown tobacco planter who married Pocahontas."
        },
        {
            "p": "After his wife died at Gravesend in 1617, this man left their sick young son, Thomas, to be raised in England and sailed back to Virginia without him. That son returned to Virginia as an adult.",
            "r": "This man’s wife was Pocahontas. For 10 points, name this Jamestown colonist who made tobacco Virginia’s cash crop."
        },
        {
            "p": "This man was born around 1585 in the village of Heacham in Norfolk, England, and he later served as secretary and recorder of the Virginia colony. He was a widower when he married a Native woman who had taken the Christian name Rebecca.",
            "r": "That woman was Pocahontas. For 10 points, name this colonist who made tobacco Virginia’s cash crop."
        },
        {
            "p": "This man died in 1622, the year Opechancanough [“oh-puh-CHAN-kuh-noh”] led a surprise attack that killed about a quarter of the English colonists in Virginia. Historians do not know whether he died in that attack or of illness.",
            "r": "For 10 points, name this Jamestown colonist who had married Pocahontas and made tobacco the colony’s cash crop."
        },
        {
            "p": "King James I had condemned the habit of using this man’s famous crop in a 1604 pamphlet, but the leaf he grew sold for high prices in London. By 1617, colonists were planting that crop even in the streets of Jamestown.",
            "r": "That crop was tobacco. For 10 points, name this colonist who first grew it for export and married Pocahontas."
        },
        {
            "p": "In 1616, the Virginia Company paid for this man to sail to England with his wife and baby son to help attract new investors to its colony. In London, his wife was introduced to high society as “Lady Rebecca.”",
            "r": "His wife, Pocahontas, died at Gravesend the next year. For 10 points, name this Jamestown tobacco planter."
        },
        {
            "p": "Virginia’s new lieutenant governor, Sir Thomas Gates, was shipwrecked on Bermuda in 1609 along with this man, in a disaster that may have inspired William Shakespeare’s _The Tempest_. Their ship was the _Sea Venture_.",
            "r": "This man later married Pocahontas. For 10 points, name this colonist who made tobacco Virginia’s cash crop."
        },
        {
            "p": "English buyers disliked the harsh-tasting _Nicotiana rustica_ grown by the Powhatan, so this colonist began planting a sweeter species, _Nicotiana tabacum_, from seeds that came from Spanish colonies to the south.",
            "r": "For 10 points, name this Jamestown settler who first grew tobacco for export around 1612 and later married Pocahontas."
        },
        {
            "p": "In 1613, Captain Samuel Argall captured a daughter of Powhatan and held her for ransom, and while she was a captive of the English, this man asked permission to marry her. She took the Christian name Rebecca before the wedding.",
            "r": "That woman was Pocahontas. For 10 points, name this English colonist who made tobacco Virginia’s cash crop."
        },
        {
            "p": "First Lady Edith Wilson was one of the many Virginians who descended from this man’s son, Thomas, who was born in 1615. Thomas never saw his mother again after she died in England when he was a small child.",
            "r": "His mother was Pocahontas. For 10 points, name this father of Thomas, a Jamestown colonist famous for growing tobacco."
        },
        {
            "p": "Although Powhatan had not met all of the English demands for ransom, he agreed to let this man marry his daughter in the church at Jamestown. Their April 1614 wedding began years of calm sometimes called the “Peace of Pocahontas.”",
            "r": "For 10 points, name this colonist who married Pocahontas and made tobacco Virginia’s cash crop."
        }
    ],
    "clues": [
        {
            "id": "tobacco",
            "tier": "giveaway",
            "t": "Grew a sweeter kind of tobacco at Jamestown around 1612 and made it Virginia’s cash crop",
            "k": ["tobacco", "1612", "sweeter", "cash crop"],
            "n": 0,
            "rabbit": "Tobacco"
        },
        {
            "id": "pocahontas",
            "tier": "giveaway",
            "t": "Married Pocahontas, the daughter of Powhatan, in April 1614",
            "k": ["pocahontas", "1614", "married"],
            "n": 0,
            "rabbit": "Pocahontas"
        },
        {
            "id": "jamestown",
            "tier": "giveaway",
            "t": "English colonist at Jamestown, in the Colony of Virginia",
            "k": ["jamestown", "virginia", "colonist"],
            "n": 0,
            "rabbit": "Jamestown"
        },
        {
            "id": "peace",
            "tier": "giveaway",
            "t": "His wedding began several years of peace with the Powhatan people, sometimes called the “Peace of Pocahontas”",
            "k": ["peace", "wedding", "powhatan"],
            "n": 0
        },
        {
            "id": "sea-venture",
            "tier": "middle",
            "t": "Sailed on the _Sea Venture_, which wrecked on Bermuda in 1609 (perhaps inspiring _The Tempest_); reached Jamestown in 1610",
            "k": ["sea venture", "bermuda", "1609", "tempest"],
            "n": 0
        },
        {
            "id": "spanish-seeds",
            "tier": "middle",
            "t": "Grew his tobacco from seeds from Spanish colonies, sweeter than the harsh kind the Powhatan grew",
            "k": ["spanish colonies", "seeds", "harsh"],
            "n": 0
        },
        {
            "id": "rebecca",
            "tier": "middle",
            "t": "His wife became a Christian and was baptized with the name Rebecca; in London she was called “Lady Rebecca”",
            "k": ["rebecca", "baptized", "lady rebecca"],
            "n": 0
        },
        {
            "id": "thomas",
            "tier": "middle",
            "t": "Father of Thomas (born 1615), his only child with Pocahontas",
            "k": ["thomas", "1615", "only child"],
            "n": 0
        },
        {
            "id": "england-trip",
            "tier": "middle",
            "t": "The Virginia Company paid for his family’s trip to England (1616); his wife died at Gravesend in 1617 as they started home",
            "k": ["gravesend", "1616", "1617", "england"],
            "n": 0
        },
        {
            "id": "dale-letter",
            "tier": "middle",
            "t": "Wrote a long letter to Sir Thomas Dale asking permission to marry her",
            "k": ["thomas dale", "dale", "letter", "permission"],
            "n": 0
        },
        {
            "id": "died-1622",
            "tier": "middle",
            "t": "Died in 1622, the year of Opechancanough’s attack; no one knows whether he died in it or of illness",
            "k": ["1622", "opechancanough"],
            "n": 0
        },
        {
            "id": "bermuda-daughter",
            "tier": "power",
            "t": "His baby daughter, Bermuda, was christened and died on the island; William Strachey’s account of the wreck records her christening",
            "k": ["strachey", "daughter", "christened"],
            "n": 0
        },
        {
            "id": "deliverance-patience",
            "tier": "power",
            "t": "The castaways built two boats, the _Deliverance_ and the _Patience_, and sailed to Jamestown in 1610",
            "k": ["deliverance", "patience", "castaways"],
            "n": 0
        },
        {
            "id": "gates",
            "tier": "power",
            "t": "Was shipwrecked with Virginia’s new lieutenant governor, Sir Thomas Gates",
            "k": ["thomas gates", "gates", "lieutenant governor"],
            "n": 0
        },
        {
            "id": "point-comfort",
            "tier": "power",
            "t": "His letter to Sir Edwin Sandys records about 20 Africans traded at Point Comfort in 1619, the first recorded enslaved Africans in English Virginia",
            "k": ["point comfort", "edwin sandys", "sandys", "1619"],
            "n": 0
        },
        {
            "id": "secretary",
            "tier": "power",
            "t": "Served as secretary and recorder of the Virginia colony",
            "k": ["secretary", "recorder"],
            "n": 0
        },
        {
            "id": "heacham",
            "tier": "power",
            "t": "Born around 1585 in the village of Heacham in Norfolk, England",
            "k": ["heacham", "norfolk", "1585"],
            "n": 0
        },
        {
            "id": "nicotiana",
            "tier": "power",
            "t": "Replaced the Powhatan’s harsh _Nicotiana rustica_ with the sweeter species _Nicotiana tabacum_",
            "k": ["nicotiana", "rustica", "tabacum"],
            "n": 0
        },
        {
            "id": "counterblaste",
            "tier": "power",
            "t": "King James I had condemned smoking in _A Counterblaste to Tobacco_ (1604), yet by 1617 colonists planted the crop even in Jamestown’s streets",
            "k": ["counterblaste", "streets", "king james"],
            "n": 0
        },
        {
            "id": "argall",
            "tier": "power",
            "t": "Captain Samuel Argall captured his future wife in 1613 and held her for ransom at Henricus",
            "k": ["argall", "henricus", "ransom", "1613"],
            "n": 0
        },
        {
            "id": "thomas-in-england",
            "tier": "power",
            "t": "Left his sick son Thomas to be raised in England when he sailed back to Virginia in 1617",
            "k": ["raised in england", "sailed back"],
            "n": 0
        },
        {
            "id": "edith-wilson",
            "tier": "power",
            "t": "First Lady Edith Wilson was one of the many Virginians descended from his son Thomas",
            "k": ["edith wilson", "descended"],
            "n": 0
        },
        {
            "id": "new-world",
            "tier": "power",
            "t": "Christian Bale played him in Terrence Malick’s 2005 film _The New World_",
            "k": ["christian bale", "new world", "malick"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Smith or Rolfe?",
        "body": "Two Johns from Jamestown are both tied to Pocahontas. John Smith led the colony in 1608–1609 and claimed that she saved his life; John Rolfe married her in 1614. Disney’s 1995 movie made Smith her love interest, so players who know only the film buzz with the wrong John. Her son Thomas Rolfe and Pocahontas herself, baptized Rebecca, are wrong answers too.",
        "fix": "Tobacco, the _Sea Venture_ wreck, the 1614 wedding, the trip to England, and a son named Thomas mean Rolfe. The rescue story, “he that will not work shall not eat,” a gunpowder injury, and mapping New England mean Smith. Say the first name, since “Rolfe” alone earns only a prompt.",
        "line": "Real answer line: <b><u>John Rolfe</u></b> (prompt on <u>Rolfe</u>; do not accept “John Smith”)"
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
