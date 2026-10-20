import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "plymouth-colony",
    "name": "Plymouth Colony",
    "mono": "PLY",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Founded by the Mayflower Pilgrims in 1620 · Site of the 1621 harvest feast",
    "dates": "Founded 1620; joined Massachusetts 1691",
    "briefing": "In December 1620, about 100 passengers from the _Mayflower_ began building a settlement on the coast of present-day Massachusetts. About half of them died that first winter, but with help from Squanto and a peace treaty with the Wampanoag leader Massasoit, Plymouth Colony survived and held a famous harvest feast in 1621. Governed for decades by William Bradford, it became part of Massachusetts in 1691.",
    "answerHtml": "<b><u>Plymouth</u></b> Colony (or <u>Plimoth</u> or New <u>Plymouth</u>; prompt on <u>Pilgrims</u>; do not accept “Massachusetts Bay Colony,” “Jamestown,” or “Mayflower”)",
    "accept": [
        "plymouth colony",
        "plymouth",
        "plimoth",
        "plimoth colony",
        "plymouth plantation",
        "plimoth plantation",
        "new plymouth",
        "colony of new plymouth",
        "plymouth massachusetts"
    ],
    "prompt": [
        "pilgrims",
        "the pilgrims",
        "pilgrim colony",
        "pilgrims colony",
        "pilgrim settlement"
    ],
    "reject": [
        "massachusetts bay colony",
        "massachusetts bay",
        "massachusetts colony",
        "province of massachusetts bay",
        "commonwealth of massachusetts",
        "jamestown",
        "roanoke",
        "mayflower",
        "the mayflower",
        "mayflower compact",
        "plymouth rock",
        "plymouth england",
        "plymouth devon",
        "plymouth company",
        "virginia company of plymouth",
        "popham colony",
        "of plymouth plantation",
        "plymouth county",
        "plymouth brethren",
        "new haven colony",
        "connecticut colony",
        "rhode island",
        "providence plantations",
        "salem",
        "boston",
        "cape cod",
        "provincetown",
        "new amsterdam",
        "st augustine",
        "puritans",
        "separatists",
        "wampanoag",
        "squanto",
        "massasoit",
        "william bradford",
        "bradford"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Plymouth_Colony",
    "qb": {
        "q": "Plymouth",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In March 1621, an Abenaki [“AB-uh-NAH-kee”] man named Samoset walked into this settlement and greeted its colonists in English. He soon returned with Squanto, who taught the settlers to plant corn using fish as fertilizer.",
            "r": "For 10 points, name this colony founded in 1620 by Pilgrims who had sailed on the _Mayflower_."
        },
        {
            "p": "Many founders of this colony had moved to the Dutch city of Leiden [“LYE-den”] in 1609 so they could worship freely as Separatists. When they sailed for America, their other ship, the _Speedwell_, leaked so badly that they left it behind.",
            "r": "They crossed the Atlantic on the _Mayflower_ instead. For 10 points, name this colony founded in 1620 in present-day Massachusetts."
        },
        {
            "p": "Peregrine White, born aboard ship in Cape Cod Harbor in November 1620, is remembered as the first English child born in New England, weeks before his family helped found this colony. Another passenger, Oceanus Hopkins, had been born at sea during the same voyage.",
            "r": "For 10 points, name this colony founded by Pilgrims who had sailed from England on the _Mayflower_."
        },
        {
            "p": "In 1621, the Wampanoag [“wahm-puh-NOH-ag”] leader Massasoit agreed to a treaty of peace and mutual defense with this colony, and the alliance lasted for more than fifty years. Squanto served as an interpreter during the talks.",
            "r": "That fall, Massasoit and about 90 of his men joined the colonists for a three-day harvest feast. For 10 points, name this colony remembered for that “first Thanksgiving.”"
        },
        {
            "p": "Edward Winslow described a three-day gathering at this colony in a 1621 letter printed in _Mourt’s Relation_, writing that the Wampanoag guests went out and killed five deer for the colony’s governor.",
            "r": "That gathering was a harvest feast often called the first Thanksgiving. For 10 points, name this colony, founded by the Pilgrims."
        },
        {
            "p": "This colony never received a royal charter of its own, and in 1691 a new charter from King William III and Queen Mary II made it part of the Province of Massachusetts Bay. Before that, Edmund Andros had ruled it as part of the Dominion of New England.",
            "r": "For 10 points, name this colony founded in 1620 by Pilgrims who sailed on the _Mayflower_."
        },
        {
            "p": "In 1628, Myles Standish arrested Thomas Morton, whose nearby trading post at Merrymount angered this colony’s leaders with a maypole celebration and with trading guns to Native Americans, and Morton was shipped back to England.",
            "r": "Standish was the military leader of this colony. For 10 points, name this colony governed for many years by William Bradford."
        },
        {
            "p": "After two hungry years of farming in common, Governor William Bradford gave each family in this colony its own plot of land in 1623, and harvests improved. Bradford later wrote a history of this colony in which he called its founders “pilgrims.”",
            "r": "For 10 points, name this colony settled in 1620 by passengers of the _Mayflower_."
        },
        {
            "p": "The handwritten history of this colony by its longtime governor disappeared from Boston during the American Revolution. Decades later it turned up in a library in London, and it was returned to Massachusetts in 1897.",
            "r": "That governor, William Bradford, led this colony for about thirty years. For 10 points, name this colony founded by the Pilgrims."
        },
        {
            "p": "One Native helper of this colony had been kidnapped by an English captain in 1614 and taken to Spain to be sold into slavery, but he made his way to England and back home, only to find that disease had wiped out his Patuxet [“puh-TUX-et”] village. This colony was built on that village’s site.",
            "r": "That helper was Squanto. For 10 points, name this colony founded in 1620 by Pilgrims from the _Mayflower_."
        },
        {
            "p": "John Carver was chosen as this colony’s first governor right after he and 40 other men signed an agreement to make “just and equal laws.” Carver died the next spring and was replaced by William Bradford.",
            "r": "That agreement was the Mayflower Compact. For 10 points, name this colony founded by the Pilgrims."
        },
        {
            "p": "In a Henry Wadsworth Longfellow poem, a soldier of this colony sends his friend John Alden to propose to Priscilla Mullins for him, and she replies, “Why don’t you speak for yourself, John?”",
            "r": "That soldier, Myles Standish, led this colony’s militia. For 10 points, name this colony founded by Pilgrims who sailed on the _Mayflower_."
        },
        {
            "p": "Captain Christopher Jones’s ship first anchored off the tip of Cape Cod, near present-day Provincetown, in November 1620, but its passengers soon moved across the bay to found this colony. About half of those settlers died during the first winter.",
            "r": "That ship was the _Mayflower_. For 10 points, name this colony founded by the Pilgrims."
        },
        {
            "p": "In 1741, a 94-year-old church elder named Thomas Faunce pointed out a granite boulder that he said marked the spot where this colony’s founders had first stepped ashore. That boulder was later broken in two while people tried to move it.",
            "r": "For 10 points, name this colony whose famous “Rock” is said to mark the Pilgrims’ landing place."
        },
        {
            "p": "Massasoit’s son Metacom, whom the English called King Philip, went to war against the New England colonies in 1675, after this colony executed three Wampanoag men for the death of John Sassamon.",
            "r": "That war ended the alliance Massasoit had made with this colony in 1621. For 10 points, name this colony founded by the Pilgrims."
        }
    ],
    "clues": [
        {
            "id": "pilgrims-1620",
            "tier": "giveaway",
            "t": "Founded in 1620 by the Pilgrims, who sailed from England on the _Mayflower_",
            "k": ["pilgrims", "1620", "mayflower"],
            "n": 0,
            "rabbit": "Mayflower"
        },
        {
            "id": "massachusetts",
            "tier": "giveaway",
            "t": "In present-day Massachusetts; it became part of the Province of Massachusetts Bay in 1691",
            "k": ["massachusetts", "1691"],
            "n": 0,
            "rabbit": "Massachusetts"
        },
        {
            "id": "thanksgiving",
            "tier": "giveaway",
            "t": "Its 1621 harvest feast with the Wampanoag is often called the first Thanksgiving",
            "k": ["thanksgiving", "harvest feast", "1621"],
            "n": 0
        },
        {
            "id": "squanto",
            "tier": "giveaway",
            "t": "Squanto (Tisquantum) taught the colonists to plant corn, using fish as fertilizer",
            "k": ["squanto", "tisquantum", "corn"],
            "n": 0
        },
        {
            "id": "compact",
            "tier": "middle",
            "t": "Mayflower Compact (1620): 41 men agreed to make “just and equal laws” before going ashore",
            "k": ["mayflower compact", "just and equal", "41 men"],
            "n": 0
        },
        {
            "id": "bradford",
            "tier": "middle",
            "t": "William Bradford governed it for about thirty years and wrote its history",
            "k": ["william bradford", "bradford", "thirty years"],
            "n": 0
        },
        {
            "id": "carver",
            "tier": "middle",
            "t": "John Carver was its first governor; he died in the spring of 1621",
            "k": ["john carver", "carver", "first governor"],
            "n": 0
        },
        {
            "id": "massasoit",
            "tier": "middle",
            "t": "Massasoit, a Wampanoag leader, made a 1621 peace treaty with the colony that lasted more than 50 years",
            "k": ["massasoit", "wampanoag", "treaty"],
            "n": 0
        },
        {
            "id": "samoset",
            "tier": "middle",
            "t": "Samoset walked into the settlement in March 1621 and greeted the colonists in English",
            "k": ["samoset", "english"],
            "n": 0
        },
        {
            "id": "standish",
            "tier": "middle",
            "t": "Myles Standish, a soldier, led its militia",
            "k": ["myles standish", "standish", "militia"],
            "n": 0
        },
        {
            "id": "first-winter",
            "tier": "middle",
            "t": "About half of the colonists died during the first winter",
            "k": ["first winter", "half"],
            "n": 0
        },
        {
            "id": "separatists",
            "tier": "middle",
            "t": "The Pilgrims were Separatists, who broke away from the Church of England",
            "k": ["separatists", "church of england"],
            "n": 0,
            "rabbit": "Puritans"
        },
        {
            "id": "leiden",
            "tier": "power",
            "t": "Many founders had lived in Leiden, in the Netherlands; their leaky ship _Speedwell_ was left behind",
            "k": ["leiden", "netherlands", "speedwell"],
            "n": 0
        },
        {
            "id": "provincetown",
            "tier": "power",
            "t": "The _Mayflower_, captained by Christopher Jones, first anchored near present-day Provincetown on Cape Cod",
            "k": ["provincetown", "cape cod", "christopher jones"],
            "n": 0,
            "rabbit": "Cape Cod"
        },
        {
            "id": "peregrine",
            "tier": "power",
            "t": "Peregrine White, born aboard the _Mayflower_, was the first English child born in New England; Oceanus Hopkins was born at sea",
            "k": ["peregrine white", "peregrine", "oceanus"],
            "n": 0
        },
        {
            "id": "patuxet",
            "tier": "power",
            "t": "Squanto had been kidnapped in 1614 and taken to Spain; disease wiped out his Patuxet village, where the colony was built",
            "k": ["patuxet", "kidnapped", "spain"],
            "n": 0
        },
        {
            "id": "winslow",
            "tier": "power",
            "t": "Edward Winslow’s 1621 letter in _Mourt’s Relation_: Massasoit and about 90 men feasted with the colonists for three days",
            "k": ["edward winslow", "winslow", "mourt’s relation", "three days"],
            "n": 0
        },
        {
            "id": "plots-1623",
            "tier": "power",
            "t": "In 1623, Bradford gave each family its own plot of land instead of farming in common",
            "k": ["1623", "plot", "in common"],
            "n": 0
        },
        {
            "id": "manuscript",
            "tier": "power",
            "t": "Bradford’s handwritten history vanished during the Revolution and was returned from London in 1897",
            "k": ["handwritten", "london", "1897"],
            "n": 0
        },
        {
            "id": "charter",
            "tier": "power",
            "t": "It never had a royal charter of its own; Edmund Andros ruled it in the Dominion of New England (1686–1689)",
            "k": ["dominion of new england", "royal charter", "andros"],
            "n": 0
        },
        {
            "id": "morton",
            "tier": "power",
            "t": "Standish arrested Thomas Morton of Merrymount (1628), known for his maypole",
            "k": ["thomas morton", "merrymount", "maypole"],
            "n": 0
        },
        {
            "id": "longfellow",
            "tier": "power",
            "t": "Longfellow’s poem about Standish: John Alden and Priscilla Mullins (“Why don’t you speak for yourself, John?”)",
            "k": ["longfellow", "john alden", "priscilla", "speak for yourself"],
            "n": 0
        },
        {
            "id": "faunce",
            "tier": "power",
            "t": "In 1741, elder Thomas Faunce pointed out the granite boulder said to mark the landing place",
            "k": ["thomas faunce", "faunce", "granite", "boulder"],
            "n": 0
        },
        {
            "id": "king-philip",
            "tier": "power",
            "t": "King Philip’s War (1675–1676), led by Massasoit’s son Metacom, began after the colony executed three Wampanoag men",
            "k": ["king philip", "metacom", "1675"],
            "n": 0,
            "rabbit": "King Philip’s War"
        },
        {
            "id": "roger-williams",
            "tier": "power",
            "t": "Roger Williams lived in the colony for about two years before he founded Providence",
            "k": ["roger williams", "providence", "two years"],
            "n": 0,
            "rabbit": "Roger Williams"
        }
    ],
    "trap": {
        "title": "Colony, Ship, or Rock?",
        "body": "Plymouth Colony shares clues with several other answer lines. The _Mayflower_ was the ship, and the Mayflower Compact was the agreement signed aboard it; Massachusetts Bay Colony was a separate, larger Puritan colony founded around Boston in 1630 that absorbed Plymouth in 1691; and Jamestown (1607, Virginia) was England’s first permanent colony in North America. Saying “Plymouth Rock” when the question wants the colony is wrong too.",
        "fix": "Listen for the noun. “This colony” with the Pilgrims, Bradford, Squanto, Massasoit, or the 1621 harvest feast means Plymouth; “this ship” means the _Mayflower_; “this document” means the Mayflower Compact; John Winthrop, Boston, and the “city upon a hill” mean Massachusetts Bay. John Smith, Pocahontas, and tobacco mean Jamestown.",
        "line": "Real answer line: <b><u>Plymouth</u></b> Colony (or <u>Plimoth</u>; do not accept “Massachusetts Bay Colony”)"
    },
    "tests": {
        "right": [
            "Plymouth Colony",
            "Plymouth",
            "Plimoth",
            "Plymouth Plantation",
            "Plymoth Colony",
            "New Plymouth"
        ],
        "prompt": [
            "Pilgrims",
            "the Pilgrim colony"
        ],
        "wrong": [
            "Massachusetts Bay Colony",
            "Jamestown",
            "Mayflower",
            "Plymouth Rock",
            "Mayflower Compact",
            "Plymouth Company",
            "Roanoke",
            "Salem"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
