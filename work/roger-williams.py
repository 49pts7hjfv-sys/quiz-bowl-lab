import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "roger-williams",
    "name": "Roger Williams",
    "mono": "RW",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Founder of Providence, Rhode Island · Early champion of religious freedom",
    "dates": "c. 1603–1683",
    "briefing": "Roger Williams was a Puritan minister who kept telling Massachusetts leaders things they did not want to hear: that the government had no business punishing people for their religious beliefs, and that colonists had no right to Native land they had not bought. Banished in 1635, he fled in the middle of winter and in 1636 founded Providence on land from the Narragansett people. His colony, Rhode Island, became a refuge for people of many faiths.",
    "answerHtml": "Roger <b><u>Williams</u></b> (do not accept “Rhode Island” or “Anne Hutchinson”)",
    "accept": [
        "roger williams",
        "williams"
    ],
    "prompt": [
        "roger",
        "william"
    ],
    "reject": [
        "rhode island",
        "anne hutchinson",
        "hutchinson",
        "thomas hooker",
        "hooker",
        "john winthrop",
        "winthrop",
        "john cotton",
        "william penn",
        "john clarke",
        "william coddington",
        "providence",
        "massachusetts bay",
        "tennessee williams",
        "william carlos williams",
        "ralph vaughan williams",
        "roger sherman",
        "william i",
        "william the conqueror"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Roger_Williams",
    "qb": {
        "q": "Roger Williams",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "This minister argued that government officials had no right to punish anyone for breaking the “first table” of the Ten Commandments, the laws about a person’s duties to God. He also argued that the king’s charter did not give colonists a fair claim to Native land, which they should buy from its owners.",
            "r": "For spreading these ideas, he was banished from Massachusetts Bay in 1635. For 10 points, name this founder of Providence."
        },
        {
            "p": "As a young man, this future minister was a protégé of the famous English judge Sir Edward Coke [“COOK”], who helped pay for his education at Cambridge. After sailing to Boston on the ship _Lyon_ in 1631, he refused a post at the Boston church because it had not separated from the Church of England.",
            "r": "He later wrote _A Key into the Language of America_. For 10 points, name this minister who founded Providence."
        },
        {
            "p": "This writer pictured a “hedge or wall of separation” between the “garden of the church” and the “wilderness of the world.” In 1644, while in England to get a patent for his colony, he published _The Bloudy Tenent of Persecution_, which argued against punishing people for their beliefs.",
            "r": "He had been banished from Massachusetts Bay in 1635. For 10 points, name this champion of religious freedom who founded the colony of Rhode Island."
        },
        {
            "p": "Boston minister John Cotton answered this man’s arguments with a book titled _The Bloudy Tenent, Washed and Made White in the Bloud of the Lambe_. This man had argued that forcing people to worship against their conscience was wrong, an idea often called “soul liberty.”",
            "r": "Banished from Massachusetts Bay, he founded a colony that welcomed people of many faiths. For 10 points, name this founder of Providence."
        },
        {
            "p": "When the Pequot War broke out, this man set out alone in a canoe through stormy seas to meet Narragansett leaders, and he helped persuade them to side with the English instead of the Pequot. Those leaders, Canonicus and Miantonomi, had earlier given him land at the head of Narragansett Bay.",
            "r": "He later wrote a guide to the Narragansett language. For 10 points, name this exile from Massachusetts Bay who founded Providence in 1636."
        },
        {
            "p": "This author wrote that he first drafted a 1643 book at sea, on a voyage to England, to help his own memory. That book lists words and phrases of the Narragansett language and describes Narragansett customs. On the same trip, he won a patent from Parliament for the towns around Narragansett Bay.",
            "r": "That book is _A Key into the Language of America_. For 10 points, name this founder of Providence, Rhode Island."
        },
        {
            "p": "A settler named Ezekiel Holliman baptized this man, who then baptized Holliman and several others, starting the congregation that became the First Baptist Church in America. Within months, this man left that church and became known as a “Seeker,” waiting for a true church to appear.",
            "r": "He believed the government should stay out of religion. For 10 points, name this minister who founded Providence after Massachusetts Bay banished him."
        },
        {
            "p": "This man helped followers of Anne Hutchinson buy Aquidneck [“uh-KWID-nek”] Island from the Narragansett in 1638, and they founded Portsmouth there. Six years later, he brought home from England a patent from Parliament that joined Portsmouth, Newport, and his own town under one government.",
            "r": "For 10 points, name this founder of Providence, who was banished from Massachusetts Bay in 1635."
        },
        {
            "p": "In 1672, when he was nearly seventy, this man traveled to Newport to debate followers of the Quaker founder George Fox. He then attacked Fox in a book titled _George Fox Digg’d out of his Burrowes_, though his colony still let Quakers worship freely.",
            "r": "He had fled Massachusetts Bay in 1636. For 10 points, name this founder of Providence, a champion of freedom of conscience."
        },
        {
            "p": "From 1654 to 1657, this man served as president of the colony he had founded. During that time, he wrote a letter comparing a society to a ship carrying Catholics, Protestants, Jews, and Muslims, none of whom should be forced to attend the ship’s prayers.",
            "r": "He had been banished from Massachusetts Bay. For 10 points, name this founder of Providence, who argued for separating church and state."
        },
        {
            "p": "The Massachusetts General Court ruled that this minister had spread “new and dangerous opinions,” such as his attacks on an oath that he said non-church members should not have to swear. When officials planned to ship him to England, John Winthrop privately warned him to flee.",
            "r": "He escaped in the middle of winter in 1636. For 10 points, name this founder of Providence."
        },
        {
            "p": "This man and the Revolutionary War general Nathanael Greene were chosen for their state’s two statues in the National Statuary Hall Collection at the U.S. Capitol. A national memorial run by the National Park Service honors this man near the spot where his settlement began in 1636.",
            "r": "For 10 points, name this Puritan minister who founded Providence after his banishment from Massachusetts Bay."
        },
        {
            "p": "This man first planted crops on the east bank of the Seekonk River, but he moved across the river after Plymouth Colony told him he was on its land. He then received land from the Narragansett leaders Canonicus and Miantonomi.",
            "r": "He named his new town for God’s “merciful providence” to him. For 10 points, name this founder of Rhode Island, who had been banished from Massachusetts."
        },
        {
            "p": "In 1676, during King Philip’s War, much of the town this aging man had founded forty years earlier was burned. For decades he had served as a go-between for the English and the Narragansett, whose language he explained in a 1643 book.",
            "r": "For 10 points, name this founder of Providence, who had been banished from Massachusetts Bay."
        },
        {
            "p": "A 1663 royal charter, won in London by John Clarke, promised that no one in this man’s colony would be punished for “differences in opinion in matters of religion.” Nearly twenty years earlier, this man had won the colony’s first patent from Parliament.",
            "r": "For 10 points, name this founder of Providence, who had been banished from Massachusetts Bay."
        }
    ],
    "clues": [
        {
            "id": "providence",
            "tier": "giveaway",
            "t": "Founded Providence in 1636, naming it for God’s “merciful providence” to him",
            "k": ["providence", "1636", "merciful"],
            "n": 0
        },
        {
            "id": "rhode-island",
            "tier": "giveaway",
            "t": "Founder of the colony of Rhode Island, a refuge for people of many faiths",
            "k": ["rhode island", "refuge", "founder"],
            "n": 0,
            "rabbit": "Rhode Island"
        },
        {
            "id": "banished",
            "tier": "giveaway",
            "t": "Banished from the Massachusetts Bay Colony in 1635; fled in the middle of winter in 1636",
            "k": ["banished", "massachusetts bay", "1635"],
            "n": 0
        },
        {
            "id": "church-state",
            "tier": "giveaway",
            "t": "Early champion of religious freedom and the separation of church and state",
            "k": ["religious freedom", "separation", "church and state"],
            "n": 0
        },
        {
            "id": "narragansett",
            "tier": "middle",
            "t": "Got the land for Providence from the Narragansett leaders Canonicus and Miantonomi",
            "k": ["narragansett", "canonicus", "miantonomi"],
            "n": 0
        },
        {
            "id": "key",
            "tier": "middle",
            "t": "Wrote _A Key into the Language of America_ (1643), a guide to the Narragansett language and customs",
            "k": ["key into the language", "1643", "language"],
            "n": 0
        },
        {
            "id": "native-land",
            "tier": "middle",
            "t": "Argued that the king’s charter did not give colonists a fair claim to Native land; they should buy it from its owners",
            "k": ["charter", "native land", "buy"],
            "n": 0
        },
        {
            "id": "bloudy-tenent",
            "tier": "middle",
            "t": "Wrote _The Bloudy Tenent of Persecution_ (1644) against punishing people for their beliefs",
            "k": ["bloudy tenent", "persecution", "1644"],
            "n": 0
        },
        {
            "id": "first-baptist",
            "tier": "middle",
            "t": "Helped start the First Baptist Church in America in Providence, then left it within months to become a “Seeker”",
            "k": ["first baptist", "baptist", "seeker"],
            "n": 0
        },
        {
            "id": "patent",
            "tier": "middle",
            "t": "Sailed to England and won a 1644 patent from Parliament joining Providence, Portsmouth, and Newport",
            "k": ["patent", "parliament", "portsmouth", "newport"],
            "n": 0
        },
        {
            "id": "salem-plymouth",
            "tier": "middle",
            "t": "A Puritan who wanted a full split from the Church of England; preached in Salem and lived two years in Plymouth Colony",
            "k": ["salem", "plymouth", "puritan"],
            "n": 0
        },
        {
            "id": "pequot",
            "tier": "middle",
            "t": "In the Pequot War (1636–1638), canoed through stormy seas to keep the Narragansett on the English side",
            "k": ["pequot", "canoed"],
            "n": 0
        },
        {
            "id": "coke",
            "tier": "power",
            "t": "Protégé of the famous English judge Sir Edward Coke (said “COOK”), who helped pay for his education at Cambridge",
            "k": ["edward coke", "coke", "cambridge"],
            "n": 0
        },
        {
            "id": "lyon",
            "tier": "power",
            "t": "Arrived in Boston on the _Lyon_ (1631); refused a post at the Boston church because it had not separated from the Church of England",
            "k": ["lyon", "1631", "separated"],
            "n": 0
        },
        {
            "id": "first-table",
            "tier": "power",
            "t": "Said officials should not punish people for breaking the “first table” of the Ten Commandments (duties to God)",
            "k": ["first table", "ten commandments"],
            "n": 0
        },
        {
            "id": "oath",
            "tier": "power",
            "t": "The General Court condemned his “new and dangerous opinions,” including his attack on an oath for non-church members",
            "k": ["dangerous opinions", "oath", "general court"],
            "n": 0
        },
        {
            "id": "winthrop",
            "tier": "power",
            "t": "John Winthrop privately warned him to flee before officials could ship him back to England",
            "k": ["winthrop", "warned"],
            "n": 0
        },
        {
            "id": "seekonk",
            "tier": "power",
            "t": "First planted on the east bank of the Seekonk River, then moved when Plymouth Colony said that land was theirs",
            "k": ["seekonk", "east bank"],
            "n": 0
        },
        {
            "id": "hedge-wall",
            "tier": "power",
            "t": "Pictured a “hedge or wall of separation” between the “garden of the church” and the “wilderness of the world”",
            "k": ["hedge", "wall of separation", "garden", "wilderness"],
            "n": 0
        },
        {
            "id": "cotton",
            "tier": "power",
            "t": "Argued in print with Boston minister John Cotton, who answered with _The Bloudy Tenent, Washed and Made White in the Bloud of the Lambe_",
            "k": ["john cotton", "cotton", "washed"],
            "n": 0
        },
        {
            "id": "aquidneck",
            "tier": "power",
            "t": "Helped Anne Hutchinson’s followers buy Aquidneck Island (1638), where they founded Portsmouth",
            "k": ["aquidneck", "hutchinson", "1638"],
            "n": 0,
            "rabbit": "Anne Hutchinson"
        },
        {
            "id": "ship-letter",
            "tier": "power",
            "t": "President of the colony (1654–1657); his “ship” letter said Catholics, Protestants, Jews, and Muslims aboard should not be forced into the ship’s prayers",
            "k": ["president", "ship", "1654"],
            "n": 0
        },
        {
            "id": "quakers",
            "tier": "power",
            "t": "Debated followers of George Fox in Newport (1672) and wrote _George Fox Digg’d out of his Burrowes_",
            "k": ["george fox", "quaker", "1672", "burrowes"],
            "n": 0
        },
        {
            "id": "king-philip",
            "tier": "power",
            "t": "Much of his town was burned in 1676, during King Philip’s War",
            "k": ["king philip", "1676", "burned"],
            "n": 0,
            "rabbit": "King Philip’s War"
        },
        {
            "id": "charter-1663",
            "tier": "power",
            "t": "John Clarke won a 1663 royal charter from Charles II that protected religious freedom in his colony",
            "k": ["john clarke", "1663", "royal charter"],
            "n": 0
        },
        {
            "id": "statue",
            "tier": "power",
            "t": "One of Rhode Island’s two statues in the National Statuary Hall Collection (with Nathanael Greene); a national memorial honors him",
            "k": ["statuary hall", "nathanael greene", "national memorial"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Williams, Hutchinson, or Hooker?",
        "body": "Three famous Puritans left the Massachusetts Bay Colony in the 1630s. Roger Williams was banished in 1635 and founded Providence; Anne Hutchinson was banished after her 1637 trial and helped found Portsmouth, also in what became Rhode Island; and Thomas Hooker led his congregation away in 1636 to found Hartford, Connecticut. A question that asks for the colony itself wants “Rhode Island,” not its founder.",
        "fix": "Williams clues: Providence, the Narragansett, _A Key into the Language of America_, _The Bloudy Tenent of Persecution_, and the First Baptist Church in America. Hutchinson clues: a woman, the Antinomian Controversy, and meetings in her home to discuss sermons; Hooker clues: Hartford and the Fundamental Orders of Connecticut. Listen for “this man,” “this woman,” or “this colony.”",
        "line": "Real answer line: Roger <b><u>Williams</u></b> (do not accept “Rhode Island” or “Anne Hutchinson”)"
    },
    "tests": {
        "right": [
            "Roger Williams",
            "Williams",
            "Roger Wiliams",
            "Reverend Roger Williams"
        ],
        "prompt": [
            "Roger",
            "William"
        ],
        "wrong": [
            "Rhode Island",
            "Anne Hutchinson",
            "Thomas Hooker",
            "William Penn",
            "Tennessee Williams",
            "John Winthrop",
            "William I"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
