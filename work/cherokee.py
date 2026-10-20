import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

data = {
    "id": "cherokee",
    "name": "Cherokee",
    "mono": "CHK",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Native nation of the Southeast · Sequoyah’s syllabary and forced removal",
    "dates": "Syllabary c. 1821; removal 1838–1839",
    "briefing": "Around 1821, a Cherokee silversmith named Sequoyah did something almost no one in history has done alone: he invented a complete writing system for his people’s language. Within a few years, thousands of Cherokee could read, and they printed their own newspaper, the _Cherokee Phoenix_. Even after winning a Supreme Court case, the Cherokee Nation was forced off its Southeastern homeland in 1838, and it rebuilt its government in present-day Oklahoma.",
    "answerHtml": "<b><u>Cherokee</u></b> (accept <u>Cherokee Nation</u> or <u>Tsalagi</u>; prompt on <u>Five Civilized Tribes</u>; do not accept “Trail of Tears”)",
    "accept": [
        "cherokee",
        "cherokees",
        "the cherokee",
        "cherokee nation",
        "cherokee people",
        "cherokee indians",
        "cherokee tribe",
        "tsalagi"
    ],
    "prompt": [
        "five civilized tribes",
        "civilized tribes",
        "five tribes"
    ],
    "reject": [
        "trail of tears",
        "cherokee removal",
        "removal of the cherokee",
        "indian removal",
        "indian removal act",
        "cherokee nation v georgia",
        "worcester v georgia",
        "cherokee phoenix",
        "creek",
        "creeks",
        "muscogee",
        "muskogee",
        "choctaw",
        "chickasaw",
        "seminole",
        "seminoles",
        "iroquois",
        "haudenosaunee",
        "cheyenne",
        "comanche",
        "shawnee",
        "navajo",
        "sioux",
        "sequoyah",
        "john ross"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Cherokee",
    "qb": {
        "q": "Cherokee",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "This people’s language is the only member of the southern branch of the Iroquoian [“eer-uh-KWOY-un”] language family. Around 1821, a silversmith who could not read English finished an 85-character system for writing that language, and within a few years thousands of this people had learned to read with it.",
            "r": "Its inventor was Sequoyah [“sih-KWOY-uh”]. For 10 points, name this Native American nation forced west on the Trail of Tears."
        },
        {
            "p": "Former U.S. Attorney General William Wirt argued this nation’s 1831 lawsuit against Georgia before the Supreme Court. Chief Justice John Marshall ruled that the Court could not hear the case, because this nation was not a foreign country but one of the “domestic dependent nations.”",
            "r": "Its Principal Chief was John Ross. For 10 points, name this Native American nation removed from Georgia on the Trail of Tears."
        },
        {
            "p": "Major Ridge, his son John Ridge, and Elias Boudinot [“BOO-dih-noh”] led a small Treaty Party that agreed to give up this nation’s homeland without the approval of most of its people. All three men were killed in 1839 by members of this nation who were angry about that treaty.",
            "r": "The treaty was signed at New Echota [“eh-CHOH-tuh”] in 1835. For 10 points, name this nation forced west on the Trail of Tears."
        },
        {
            "p": "Elias Boudinot [“BOO-dih-noh”] edited this people’s newspaper, the _Phoenix_, which began printing in 1828 at their capital of New Echota [“eh-CHOH-tuh”]. Printed in English and in this people’s own language, it was the first newspaper published by Native Americans.",
            "r": "Its type used the syllabary invented by Sequoyah [“sih-KWOY-uh”]. For 10 points, name this nation that was forced west on the Trail of Tears in 1838."
        },
        {
            "p": "In 1827, this nation adopted a written constitution that created three branches of government, much like the U.S. Constitution. The next year, its legislature chose a Principal Chief who held that post for nearly forty years, leading his people through removal and the Civil War.",
            "r": "That chief was John Ross. For 10 points, name this nation whose homeland in Georgia was taken after the Indian Removal Act."
        },
        {
            "p": "After gold was discovered near Dahlonega [“duh-LON-uh-guh”] in 1829, Georgia passed laws claiming this nation’s land and began giving it away to white settlers in lotteries. Because Georgia also banned this nation’s government from meeting in the state, its council moved to Red Clay, Tennessee.",
            "r": "For 10 points, name this nation led by John Ross, which was forced west on the Trail of Tears."
        },
        {
            "p": "In 1838, soldiers under General Winfield Scott forced thousands of this people out of their homes and into crowded stockades. The next year, survivors rebuilt their government in the West and made Tahlequah [“TAL-uh-kwah”] their new capital.",
            "r": "For 10 points, name this Native American nation whose forced removal from the Southeast is called the Trail of Tears."
        },
        {
            "p": "Members of this nation who stayed in the mountains of North Carolina avoided removal, and their descendants make up the Eastern Band, whose land is called the Qualla [“KWAH-luh”] Boundary. Another federally recognized tribe of this people is the United Keetoowah [“kee-TOO-wah”] Band.",
            "r": "For 10 points, name this people, whose writing system was created by Sequoyah and most of whom were forced west on the Trail of Tears."
        },
        {
            "p": "Stand Watie, a member of this nation, became a Confederate general and was the last Confederate general in the field to surrender, in June 1865. His brother, Elias Boudinot [“BOO-dih-noh”], had signed the treaty that gave away this nation’s eastern homeland.",
            "r": "For 10 points, name this nation, led for decades by John Ross, whose removal was called the Trail of Tears."
        },
        {
            "p": "Dragging Canoe opposed a 1775 deal at Sycamore Shoals that sold much of present-day Kentucky to Richard Henderson’s Transylvania Company. He then led a band of this people called the Chickamauga [“chik-uh-MAW-guh”] in years of war against American settlers.",
            "r": "For 10 points, name this nation, whose writing system was later created by Sequoyah, that was forced west on the Trail of Tears."
        },
        {
            "p": "At the 1814 Battle of Horseshoe Bend, hundreds of warriors from this nation fought on Andrew Jackson’s side against the Red Stick Creeks. By the 1830s, this nation’s homeland covered parts of Georgia, Tennessee, North Carolina, and Alabama.",
            "r": "Jackson later signed the Indian Removal Act. For 10 points, name this nation forced west on the Trail of Tears."
        },
        {
            "p": "Wilma Mankiller became the first woman to serve as this nation’s Principal Chief, leading it from 1985 to 1995, and she later appeared on a U.S. quarter. The humorist Will Rogers had been born a citizen of this nation in Indian Territory.",
            "r": "This nation’s capital is Tahlequah, Oklahoma. For 10 points, name this nation, which was forced west on the Trail of Tears."
        },
        {
            "p": "Nancy Ward held the title “Beloved Woman” among this people, who were organized into seven clans and traced family membership through their mothers. During the American Revolution, Ward urged peace and warned American settlers about planned attacks.",
            "r": "Sequoyah [“sih-KWOY-uh”] later created a writing system for this people. For 10 points, name this nation, one of the “Five Civilized Tribes,” that the U.S. forced west in 1838."
        },
        {
            "p": "John Ross sent Congress petitions signed by thousands of his people, protesting a treaty that traded this nation’s eastern lands for five million dollars and land in the West. The U.S. Senate approved that treaty anyway in 1836.",
            "r": "That treaty was signed by a small Treaty Party at New Echota. For 10 points, name this nation whose removal became known as the Trail of Tears."
        },
        {
            "p": "Missionaries Samuel Worcester and Elizur Butler were sentenced to hard labor for living among this people without a license from Georgia. When the Supreme Court overturned their convictions, Andrew Jackson supposedly said, “John Marshall has made his decision; now let him enforce it.”",
            "r": "That 1832 case was _Worcester v. Georgia_. For 10 points, name this nation forced west on the Trail of Tears."
        }
    ],
    "clues": [
        {
            "id": "trail-of-tears",
            "tier": "giveaway",
            "t": "Forced west to Indian Territory (present-day Oklahoma) on the Trail of Tears, 1838–1839",
            "k": ["trail of tears", "indian territory", "oklahoma", "1838"],
            "n": 0,
            "rabbit": "Trail of Tears"
        },
        {
            "id": "sequoyah",
            "tier": "giveaway",
            "t": "Sequoyah, a silversmith, created their writing system, a syllabary, around 1821",
            "k": ["sequoyah", "syllabary", "1821"],
            "n": 0,
            "rabbit": "Sequoyah"
        },
        {
            "id": "southeast",
            "tier": "giveaway",
            "t": "A Native nation of the Southeast (Georgia, Tennessee, North Carolina, Alabama); one of the “Five Civilized Tribes”",
            "k": ["five civilized tribes", "southeast", "georgia"],
            "n": 0
        },
        {
            "id": "removal-act",
            "tier": "giveaway",
            "t": "Lost their homeland after the Indian Removal Act, signed by President Andrew Jackson in 1830",
            "k": ["indian removal act", "andrew jackson", "1830"],
            "n": 0,
            "rabbit": "Andrew Jackson"
        },
        {
            "id": "john-ross",
            "tier": "middle",
            "t": "John Ross, Principal Chief from 1828 to 1866, fought removal with lawsuits and petitions",
            "k": ["john ross", "principal chief", "petitions"],
            "n": 0
        },
        {
            "id": "worcester",
            "tier": "middle",
            "t": "_Worcester v. Georgia_ (1832): John Marshall’s Supreme Court said Georgia’s laws had no force on their land, but Jackson ignored it",
            "k": ["worcester", "supreme court", "marshall"],
            "n": 0,
            "rabbit": "Worcester v. Georgia"
        },
        {
            "id": "new-echota-treaty",
            "tier": "middle",
            "t": "Treaty of New Echota (1835): a small Treaty Party traded their eastern land for $5 million and land in the West",
            "k": ["new echota", "treaty party", "5 million"],
            "n": 0
        },
        {
            "id": "phoenix",
            "tier": "middle",
            "t": "Their newspaper, the _Phoenix_ (1828), edited by Elias Boudinot, was the first newspaper published by Native Americans",
            "k": ["phoenix", "boudinot", "newspaper"],
            "n": 0
        },
        {
            "id": "domestic-dependent",
            "tier": "middle",
            "t": "In their 1831 case against Georgia (argued by William Wirt), John Marshall called Native nations “domestic dependent nations”",
            "k": ["domestic dependent", "1831", "wirt"],
            "n": 0
        },
        {
            "id": "winfield-scott",
            "tier": "middle",
            "t": "In 1838, General Winfield Scott’s soldiers forced them into stockades before the march west",
            "k": ["winfield scott", "stockades"],
            "n": 0
        },
        {
            "id": "dahlonega",
            "tier": "middle",
            "t": "An 1829 gold rush near Dahlonega led Georgia to claim their land and give it away in lotteries",
            "k": ["dahlonega", "gold rush", "lotteries"],
            "n": 0
        },
        {
            "id": "constitution",
            "tier": "middle",
            "t": "Adopted a written constitution with three branches in 1827, modeled on the U.S. Constitution",
            "k": ["constitution", "1827", "three branches"],
            "n": 0
        },
        {
            "id": "treaty-party",
            "tier": "power",
            "t": "Major Ridge, John Ridge, and Elias Boudinot led the Treaty Party; all three were killed in 1839",
            "k": ["major ridge", "john ridge", "1839"],
            "n": 0
        },
        {
            "id": "capitals",
            "tier": "power",
            "t": "Capitals: New Echota, Georgia (from 1825); Red Clay, Tennessee (1832–1838); Tahlequah, Oklahoma (from 1839)",
            "k": ["tahlequah", "red clay", "capitals"],
            "n": 0
        },
        {
            "id": "syllabary-85",
            "tier": "power",
            "t": "The syllabary has 85 characters, each standing for a syllable; their language is Iroquoian",
            "k": ["85 characters", "iroquoian", "syllable"],
            "n": 0
        },
        {
            "id": "eastern-band",
            "tier": "power",
            "t": "Some stayed in North Carolina; their descendants form the Eastern Band (Qualla Boundary). The United Keetoowah Band is in Oklahoma",
            "k": ["eastern band", "qualla", "keetoowah"],
            "n": 0
        },
        {
            "id": "stand-watie",
            "tier": "power",
            "t": "Stand Watie, Elias Boudinot’s brother, was the last Confederate general in the field to surrender (June 1865)",
            "k": ["stand watie", "watie", "confederate"],
            "n": 0
        },
        {
            "id": "dragging-canoe",
            "tier": "power",
            "t": "Dragging Canoe opposed the 1775 Sycamore Shoals land sale and led the Chickamauga in war against settlers",
            "k": ["dragging canoe", "chickamauga", "sycamore shoals"],
            "n": 0
        },
        {
            "id": "horseshoe-bend",
            "tier": "power",
            "t": "Their warriors fought on Andrew Jackson’s side against the Red Stick Creeks at Horseshoe Bend (1814)",
            "k": ["horseshoe bend", "red stick", "1814"],
            "n": 0
        },
        {
            "id": "mankiller",
            "tier": "power",
            "t": "Wilma Mankiller was the first woman Principal Chief (1985–1995) and appears on a 2022 U.S. quarter",
            "k": ["mankiller", "wilma", "quarter"],
            "n": 0
        },
        {
            "id": "will-rogers",
            "tier": "power",
            "t": "The humorist Will Rogers was born a citizen of their nation in Indian Territory (1879)",
            "k": ["will rogers", "humorist"],
            "n": 0
        },
        {
            "id": "nancy-ward",
            "tier": "power",
            "t": "Nancy Ward, honored as a “Beloved Woman,” urged peace during the American Revolution",
            "k": ["nancy ward", "beloved woman"],
            "n": 0
        },
        {
            "id": "clans",
            "tier": "power",
            "t": "Organized into seven clans; family membership passed through the mother",
            "k": ["seven clans", "clans", "mother"],
            "n": 0
        },
        {
            "id": "worcester-butler",
            "tier": "power",
            "t": "Missionaries Samuel Worcester and Elizur Butler were sentenced to hard labor for living among them without a Georgia license",
            "k": ["elizur butler", "butler", "hard labor"],
            "n": 0
        }
    ],
    "trap": {
        "title": "People or event?",
        "body": "Most Cherokee clues, like John Ross, the Treaty of New Echota, Winfield Scott, and _Worcester v. Georgia_, also lead tossups on the Trail of Tears, Indian removal, and Andrew Jackson. If the question asks for “this nation” or “this people,” answering “Trail of Tears” is wrong. It is also easy to name the wrong member of the “Five Civilized Tribes,” since all five were forced west in the 1830s.",
        "fix": "Listen for the noun: “this nation” or “this people” wants Cherokee, while “this event” or “this march” wants the Trail of Tears. Sequoyah, the _Phoenix_ newspaper, and Tahlequah mean Cherokee; Osceola means Seminole, the Red Sticks were Creek, and Dancing Rabbit Creek means Choctaw.",
        "line": "Real answer line: <b><u>Cherokee</u></b> (accept <u>Cherokee Nation</u> or <u>Tsalagi</u>; prompt on <u>Five Civilized Tribes</u>; do not accept “Trail of Tears”)"
    },
    "tests": {
        "right": [
            "Cherokee",
            "Cherokee Nation",
            "the Cherokees",
            "Cherokee people",
            "Cherokie",
            "Tsalagi"
        ],
        "prompt": [
            "Five Civilized Tribes"
        ],
        "wrong": [
            "Trail of Tears",
            "Creek",
            "Seminole",
            "Choctaw",
            "Cherokee Nation v. Georgia",
            "Iroquois",
            "Sequoyah"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
