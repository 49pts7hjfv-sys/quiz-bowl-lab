import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

data = {
    "id": "john-smith",
    "name": "John Smith",
    "mono": "CJS",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Leader of Jamestown · Said Pocahontas saved his life",
    "dates": "c. 1580–1631",
    "briefing": "Captain John Smith was a soldier and explorer who helped keep Jamestown alive by making the colonists work, ruling that “he that will not work shall not eat.” He mapped the Chesapeake Bay, gave New England its name, and wrote best-selling books about his adventures. In one of them, he claimed that Pocahontas saved his life when her father was about to have him killed, a story many historians doubt.",
    "answerHtml": "<b><u>John Smith</u></b> (accept Captain <u>John Smith</u>; prompt on <u>Smith</u>; do not accept “John Rolfe” or “Joseph Smith”)",
    "accept": [
        "john smith",
        "captain john smith",
        "capt john smith",
        "captaine john smith"
    ],
    "prompt": [
        "smith",
        "captain smith",
        "capt smith"
    ],
    "reject": [
        "john rolfe",
        "rolfe",
        "joseph smith",
        "adam smith",
        "jedediah smith",
        "pocahontas",
        "powhatan",
        "opechancanough",
        "christopher newport",
        "edward maria wingfield",
        "wingfield",
        "john ratcliffe",
        "bartholomew gosnold",
        "thomas dale",
        "samuel argall",
        "john winthrop",
        "myles standish",
        "william bradford",
        "squanto"
    ],
    "tests": {
        "right": [
            "John Smith",
            "Captain John Smith",
            "Capt. John Smith",
            "Jon Smith",
            "john smyth"
        ],
        "prompt": [
            "Smith",
            "Captain Smith"
        ],
        "wrong": [
            "John Rolfe",
            "Joseph Smith",
            "Pocahontas",
            "Adam Smith",
            "Christopher Newport",
            "John Winthrop"
        ]
    },
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/John_Smith_(explorer)",
    "qb": {
        "q": "John Smith",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "This man claimed that while fighting the Ottoman Turks in Hungary, he won three duels against Turkish champions and earned a coat of arms from a prince of Transylvania. He also claimed that he was later captured, sold into slavery, and escaped through Russia.",
            "r": "He went on to lead the colony at Jamestown. For 10 points, name this English captain who said Pocahontas saved his life."
        },
        {
            "p": "Accused of plotting a mutiny during the voyage to Virginia, this man spent much of the trip under arrest, but sealed orders opened after the ships landed named him to the colony’s governing council.",
            "r": "In 1608, he became president of that council at Jamestown. For 10 points, name this captain who was supposedly rescued by Pocahontas."
        },
        {
            "p": "In 1608, a stingray stung this explorer near the mouth of the Rappahannock River, and the spot is still called Stingray Point. That year, he explored the Chesapeake Bay and the Potomac River, and he later published a detailed _Map of Virginia_.",
            "r": "For 10 points, name this leader of Jamestown who told colonists that “he that will not work shall not eat.”"
        },
        {
            "p": "This explorer named a cape in Massachusetts “Tragabigzanda” after a woman he said he had met as a captive in Constantinople, but Prince Charles renamed it Cape Ann. In 1614, this man mapped the coast from Penobscot Bay to Cape Cod.",
            "r": "He gave that region the name New England. For 10 points, name this former leader of Jamestown."
        },
        {
            "p": "This man’s 1608 book _A True Relation_ described his capture by Opechancanough [“oh-puh-CHAN-kuh-noh”] but said nothing about a girl saving his life. He told that famous story years later, after the girl had died, so many historians doubt it.",
            "r": "The girl was Pocahontas. For 10 points, name this English captain who led Jamestown in 1608 and 1609."
        },
        {
            "p": "The full title of this man’s 1624 _Generall Historie_ also names New England and the Summer Isles, an old name for Bermuda. That book includes a letter he said he had written to Queen Anne in 1616 about a visiting Native woman.",
            "r": "It also tells how that woman, Pocahontas, saved his life. For 10 points, name this English captain who led Jamestown."
        },
        {
            "p": "In 1609, this man was badly hurt when his bag of gunpowder accidentally exploded while he was in a boat, and he sailed home to England that October. He never returned to Virginia, and the colony soon suffered through the “Starving Time.”",
            "r": "For 10 points, name this captain who had ruled that colonists who would not work would not eat."
        },
        {
            "p": "This leader borrowed a line from the Bible’s Second Letter to the Thessalonians for a famous rule aimed at colonists who were “gentlemen” unused to hard labor. He also traded with the Powhatan for corn to keep the colony fed.",
            "r": "His rule was “He that will not work shall not eat.” For 10 points, name this president of the Jamestown council."
        },
        {
            "p": "Colin Farrell played this man in Terrence Malick’s 2005 film _The New World_. In real life, this man was about 27 years old when he was captured and brought before the chief Powhatan in December 1607.",
            "r": "Mel Gibson voiced him in Disney’s 1995 movie _Pocahontas_. For 10 points, name this English captain who led Jamestown."
        },
        {
            "p": "This man’s 1616 book _A Description of New England_ praised the fish, furs, and harbors of a coast he had mapped in 1614. Years earlier, he had explored the Chesapeake Bay in a small open boat.",
            "r": "He had also led the Jamestown colony. For 10 points, name this captain who claimed that Pocahontas saved his life."
        },
        {
            "p": "This man was born around 1580 in Willoughby, Lincolnshire, and as a young man he fought as a soldier in the Netherlands and in Hungary. In 1606, he sailed for Virginia on one of three ships commanded by Christopher Newport.",
            "r": "For 10 points, name this captain who later led the colony at Jamestown and wrote about Pocahontas."
        },
        {
            "p": "While exploring the Chickahominy River in December 1607, this man was captured and taken to Werowocomoco [“wair-uh-wuh-KOH-muh-koh”] to meet the chief Powhatan. Some historians think the ceremony that followed was a ritual of adoption, not a real threat to his life.",
            "r": "He later wrote that Pocahontas saved his life. For 10 points, name this English captain who led Jamestown."
        },
        {
            "p": "This author of _The True Travels, Adventures, and Observations_, published in 1630, died in London the next year and was buried at the Church of St. Sepulchre. That book retold his adventures as a soldier fighting the Ottoman Turks.",
            "r": "For 10 points, name this English captain who led the Jamestown colony and wrote about Pocahontas."
        },
        {
            "p": "In 2006, Congress created the first national historic trail made up entirely of water routes, following the paths this man took in small boats while exploring the Chesapeake Bay in 1608. His _Map of Virginia_ was published in 1612.",
            "r": "For 10 points, name this explorer and leader of Jamestown who claimed that Pocahontas saved him."
        },
        {
            "p": "This man wrote that when he visited a young Powhatan woman near London in 1616, she turned away and hid her face, because she had been told for years that he was dead.",
            "r": "That woman, Pocahontas, had supposedly saved his life in Virginia. For 10 points, name this captain who led Jamestown."
        }
    ],
    "clues": [
        {
            "id": "jamestown-leader",
            "tier": "giveaway",
            "t": "Leader of Jamestown; president of its council from 1608 to 1609",
            "k": ["jamestown", "president", "council", "1608"],
            "n": 0,
            "rabbit": "Jamestown"
        },
        {
            "id": "pocahontas-rescue",
            "tier": "giveaway",
            "t": "Claimed that Pocahontas saved his life when her father, Powhatan, was about to have him killed (1607); many historians doubt it",
            "k": ["pocahontas", "saved", "powhatan"],
            "n": 0,
            "rabbit": "Pocahontas"
        },
        {
            "id": "work-eat",
            "tier": "giveaway",
            "t": "His rule for lazy colonists: “He that will not work shall not eat”",
            "k": ["will not work", "shall not eat", "work"],
            "n": 0
        },
        {
            "id": "disney",
            "tier": "giveaway",
            "t": "English captain shown as Pocahontas’s love interest in Disney’s 1995 movie (voiced by Mel Gibson), though there was no romance",
            "k": ["disney", "mel gibson", "1995"],
            "n": 0
        },
        {
            "id": "gunpowder",
            "tier": "middle",
            "t": "Badly hurt when his bag of gunpowder exploded in 1609; went home to England and never returned to Virginia",
            "k": ["gunpowder", "1609", "never returned"],
            "n": 0
        },
        {
            "id": "captured",
            "tier": "middle",
            "t": "Captured by Opechancanough on the Chickahominy River (December 1607) and taken to Powhatan at Werowocomoco",
            "k": ["opechancanough", "werowocomoco", "chickahominy"],
            "n": 0
        },
        {
            "id": "chesapeake",
            "tier": "middle",
            "t": "Explored the Chesapeake Bay and the Potomac River in 1608; published his _Map of Virginia_ in 1612",
            "k": ["chesapeake", "map of virginia", "potomac", "1612"],
            "n": 0,
            "rabbit": "Potomac River"
        },
        {
            "id": "new-england",
            "tier": "middle",
            "t": "Mapped the coast of New England in 1614 and gave the region its name in _A Description of New England_ (1616)",
            "k": ["new england", "description of new england", "1614"],
            "n": 0
        },
        {
            "id": "generall-historie",
            "tier": "middle",
            "t": "Wrote _The Generall Historie of Virginia, New-England, and the Summer Isles_ (1624), which tells the full rescue story",
            "k": ["generall historie", "summer isles", "1624"],
            "n": 0
        },
        {
            "id": "true-relation",
            "tier": "middle",
            "t": "His first book, _A True Relation_ (1608), describes his capture but never mentions Pocahontas saving him",
            "k": ["true relation", "first book"],
            "n": 0
        },
        {
            "id": "turks",
            "tier": "middle",
            "t": "Earlier fought the Ottoman Turks in Hungary; claimed he won three duels against Turkish champions and got a coat of arms",
            "k": ["ottoman", "turks", "three duels", "coat of arms"],
            "n": 0
        },
        {
            "id": "corn",
            "tier": "middle",
            "t": "Traded with the Powhatan for corn to keep the colonists fed",
            "k": ["corn", "traded"],
            "n": 0
        },
        {
            "id": "sealed-orders",
            "tier": "power",
            "t": "Arrested for plotting mutiny on the voyage over, but sealed orders opened in Virginia named him to the governing council",
            "k": ["sealed orders", "mutiny", "sealed"],
            "n": 0
        },
        {
            "id": "stingray",
            "tier": "power",
            "t": "A stingray stung him near the mouth of the Rappahannock River (1608); the spot is still called Stingray Point",
            "k": ["stingray", "rappahannock"],
            "n": 0
        },
        {
            "id": "slavery",
            "tier": "power",
            "t": "Claimed he was captured by the Turks, sold into slavery, and escaped through Russia",
            "k": ["slavery", "escaped", "russia"],
            "n": 0
        },
        {
            "id": "tragabigzanda",
            "tier": "power",
            "t": "Named Cape Ann “Cape Tragabigzanda” after a woman he met as a captive in Constantinople; Prince Charles renamed it",
            "k": ["tragabigzanda", "cape ann", "prince charles"],
            "n": 0
        },
        {
            "id": "willoughby",
            "tier": "power",
            "t": "Born around 1580 in Willoughby, Lincolnshire; fought as a young soldier in the Netherlands and Hungary",
            "k": ["willoughby", "lincolnshire", "1580"],
            "n": 0
        },
        {
            "id": "thessalonians",
            "tier": "power",
            "t": "His work rule echoed the Bible’s Second Letter to the Thessalonians; many colonists were “gentlemen” unused to labor",
            "k": ["thessalonians", "gentlemen"],
            "n": 0
        },
        {
            "id": "adoption",
            "tier": "power",
            "t": "Some historians think the “rescue” was really a ritual of adoption",
            "k": ["adoption", "ritual"],
            "n": 0
        },
        {
            "id": "hid-face",
            "tier": "power",
            "t": "Wrote that when he met Pocahontas near London in 1616, she hid her face because she had been told he was dead; printed a letter he said he wrote to Queen Anne about her",
            "k": ["hid her face", "queen anne", "1616"],
            "n": 0
        },
        {
            "id": "true-travels",
            "tier": "power",
            "t": "_The True Travels, Adventures, and Observations_ (1630) retold his years as a soldier",
            "k": ["true travels", "1630"],
            "n": 0
        },
        {
            "id": "died-1631",
            "tier": "power",
            "t": "Died in London in 1631; buried at the Church of St. Sepulchre",
            "k": ["1631", "sepulchre"],
            "n": 0
        },
        {
            "id": "water-trail",
            "tier": "power",
            "t": "A national historic trail of water routes on the Chesapeake, created in 2006, follows his voyages",
            "k": ["water routes", "historic trail", "2006"],
            "n": 0
        },
        {
            "id": "new-world",
            "tier": "power",
            "t": "Colin Farrell played him in Terrence Malick’s _The New World_ (2005); he was about 27 when he was brought before Powhatan",
            "k": ["colin farrell", "new world", "malick"],
            "n": 0
        },
        {
            "id": "newport-voyage",
            "tier": "power",
            "t": "Sailed in 1606 with Christopher Newport’s three ships, the _Susan Constant_, _Godspeed_, and _Discovery_",
            "k": ["newport", "susan constant", "godspeed"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Which John? Which Smith?",
        "body": "John Smith and John Rolfe both lived at Jamestown and are both tied to Pocahontas: Smith said she saved his life, but Rolfe is the one who married her. Other famous Smiths are different answers entirely, like Joseph Smith, who founded the Latter Day Saint movement in 1830, and Adam Smith, the economist who wrote _The Wealth of Nations_.",
        "fix": "The rescue story, the gunpowder injury, “he that will not work shall not eat,” the Chesapeake map, and naming New England mean John Smith. Tobacco and the 1614 wedding mean John Rolfe. Say “John Smith,” since “Smith” alone earns only a prompt.",
        "line": "Real answer line: <b><u>John Smith</u></b> (accept Captain <u>John Smith</u>; prompt on <u>Smith</u>; do not accept “John Rolfe”)"
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
