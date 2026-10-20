import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

LINE = "<b><u>Mecca</u></b> (or <u>Makkah</u>; do not accept “Medina”)"

data = {
    "id": "mecca",
    "name": "Mecca",
    "mono": "MK",
    "category": "Religion",
    "qbCategory": "Religion",
    "kicker": "Islam’s holiest city · Birthplace of Muhammad and home of the Kaaba",
    "dates": "Muhammad born there c. 570",
    "briefing": "Five times a day, Muslims all over the world turn to face one city when they pray: Mecca, in the rocky valleys of western Saudi Arabia. Muhammad was born there around 570, and at its heart stands the Kaaba, a cube-shaped shrine draped in black cloth inside the world’s largest mosque. Every Muslim who is able is expected to make the Hajj pilgrimage there at least once.",
    "answerHtml": LINE,
    "accept": [
        "mecca",
        "makkah",
        "makka",
        "mekka",
        "meccah",
        "makkah al mukarramah"
    ],
    "prompt": [],
    "reject": [
        "medina",
        "madinah",
        "al madinah",
        "medinah",
        "yathrib",
        "jeddah",
        "jidda",
        "jiddah",
        "riyadh",
        "taif",
        "jerusalem",
        "al quds",
        "hajj",
        "umrah",
        "kaaba",
        "kabah",
        "masjid al haram",
        "great mosque",
        "grand mosque",
        "al haram",
        "black stone",
        "zamzam",
        "arafat",
        "mount arafat",
        "mina",
        "muzdalifah",
        "hira"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Mecca",
    "qb": {"q": "Mecca", "found": 0, "tip": TIP},
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        {
            "p": "In 1916, Hussein bin Ali, who held the title of Sharif of this city, launched the Arab Revolt against the Ottoman Empire. In 1924, the forces of Ibn Saud [“IB-un sah-OOD”] captured this city, which later became part of the kingdom of Saudi Arabia.",
            "r": "Muslims around the world face this city when they pray. For 10 points, name this holiest city of Islam."
        },
        {
            "p": "A short chapter of the Quran called “The Elephant” is traditionally linked to an army led by Abraha [“uh-BRAH-hah”], a ruler of Yemen, that marched on this city with at least one elephant but was turned back, according to Muslim tradition, by flocks of birds.",
            "r": "Muhammad was born in this city in that “Year of the Elephant.” For 10 points, name this city, home of the Kaaba."
        },
        {
            "p": "The Abraj Al Bait [“AHB-rahj al-BAYT”] towers rise over this city, and their central clock tower, finished in 2012, is one of the tallest buildings in the world and has the world’s largest clock faces. Those towers overlook the Masjid al-Haram [“MAS-jid al-hah-RAHM”], the largest mosque on Earth.",
            "r": "That mosque surrounds the Kaaba. For 10 points, name this Saudi Arabian city, the holiest in Islam."
        },
        {
            "p": "The Quran calls this city Umm al-Qura [“OOM al-KOO-rah”], the “Mother of Cities,” and one verse that Muslims understand to refer to it calls it Bakkah [“BAK-kah”], site of the first house of worship built for humanity.",
            "r": "Muslims believe that house, the Kaaba, was built by Abraham and Ishmael. For 10 points, name this city where the Hajj takes place."
        },
        {
            "p": "The British explorer Richard Francis Burton traveled to this city in disguise in 1853 and later wrote a famous account of his pilgrimage there. He hid his identity because only Muslims are allowed to enter this city.",
            "r": "Its Great Mosque surrounds the cube-shaped Kaaba. For 10 points, name this city in Saudi Arabia."
        },
        {
            "p": "Pilgrims who set out from this city’s Great Mosque during one ritual camp in the tent city of Mina, pray on the plain of Arafat, and spend a night under the open sky at Muzdalifah [“mooz-DAH-lih-fah”] before returning to circle its shrine.",
            "r": "A niche called a mihrab in each mosque points toward this city. For 10 points, name this city, the destination of the Hajj."
        },
        {
            "p": "Muslims believe the first verses of the Quran were revealed to Muhammad in the cave of Hira [“hih-RAH”], on the Mountain of Light, or Jabal al-Nour [“JAH-bal an-NOOR”], which rises on the edge of this city. That revelation came around the year 610.",
            "r": "Muhammad was born in this city around 570 and later left it for Medina. For 10 points, name this city."
        },
        {
            "p": "Before Islam, the Quraysh [“koo-RAYSH”] tribe controlled this city’s trade and guarded a shrine filled with statues of many gods, including Hubal [“hoo-BAHL”]. In 630, Muhammad returned to this city with about 10,000 followers, met little resistance, and removed those idols.",
            "r": "That shrine, the Kaaba, became the center of Islam. For 10 points, name this city, Islam’s holiest."
        },
        {
            "p": "In 622, Muhammad and his friend Abu Bakr hid for three days in the cave of Thawr [“THOWR”] while men from this city searched for them. That journey, the Hijra [“HIJ-rah”], marks the start of the Islamic calendar.",
            "r": "It took them from this city to Medina. For 10 points, name this city, Muhammad’s birthplace."
        },
        {
            "p": "In 1964, Malcolm X wrote letters from this city describing pilgrims of every color worshipping together, an experience that changed his views on race. In 1325, Ibn Battuta left Tangier on a journey to this city that grew into nearly 30 years of travel.",
            "r": "Mansa Musa also passed through Cairo on his way here in 1324. For 10 points, name this city, the destination of the Hajj."
        },
        {
            "p": "Saudi kings have taken the title “Custodian of the Two Holy Mosques,” referring to the Prophet’s Mosque in Medina and the Great Mosque in this city. That Great Mosque contains the Zamzam well and the shrine that holds the Black Stone.",
            "r": "Every Muslim who is able must make a pilgrimage here once in a lifetime. For 10 points, name this holiest city of Islam."
        },
        {
            "p": "This city lies in a narrow valley among rocky hills in the Hejaz [“heh-JAHZ”] region. Most pilgrims reach it through Jeddah, a Red Sea port about 70 kilometers to the west, and highway signs direct non-Muslims away from it.",
            "r": "Huge crowds come here each year for the Hajj. For 10 points, name this city where Muhammad was born."
        },
        {
            "p": "A chapter of the Quran called “The Night Journey” opens by praising God, who carried His servant by night from the Sacred Mosque in this city to the Farthest Mosque, which Muslims identify with Jerusalem.",
            "r": "Muhammad, that servant, was born in this city. For 10 points, name this city where the Kaaba stands."
        },
        {
            "p": "According to tradition, Muhammad’s grandfather Abd al-Muttalib [“AHB-dul moo-TAH-lib”], a leader of this city’s Quraysh [“koo-RAYSH”] tribe, dug out a long-lost well there. Muslims believe that well, Zamzam [“ZAHM-zahm”], first appeared in the desert to save Hagar and her baby, Ishmael.",
            "r": "Pilgrims drink its water after circling the Kaaba. For 10 points, name this city in Saudi Arabia."
        },
        {
            "p": "An army from this city lost the Battle of Badr [“BAH-der”] in 624, and the next year Abu Sufyan [“AH-boo soo-FYAHN”] led its forces against Muhammad’s followers at the Battle of Uhud [“oo-HOOD”], near Medina. In 627, this city’s leaders headed an alliance that besieged Medina in the Battle of the Trench.",
            "r": "In 630, Muhammad took control of this city with little fighting. For 10 points, name this holy city, where the Kaaba stands."
        }
    ],
    "clues": [
        {
            "id": "holiest-city",
            "tier": "giveaway",
            "t": "Holiest city of Islam, in western Saudi Arabia",
            "k": ["holiest city", "saudi arabia", "islam"],
            "n": 0
        },
        {
            "id": "kaaba",
            "tier": "giveaway",
            "t": "Home of the Kaaba, the cube-shaped shrine draped in black cloth in the courtyard of the Great Mosque",
            "k": ["kaaba", "cube-shaped", "great mosque"],
            "n": 0
        },
        {
            "id": "hajj",
            "tier": "giveaway",
            "t": "Destination of the Hajj, the pilgrimage that every Muslim who is able must make at least once",
            "k": ["hajj", "pilgrimage"],
            "n": 0,
            "rabbit": "Hajj"
        },
        {
            "id": "qibla",
            "tier": "giveaway",
            "t": "Muslims everywhere face it when they pray; that direction is called the qibla",
            "k": ["qibla", "face", "pray"],
            "n": 0
        },
        {
            "id": "birthplace",
            "tier": "giveaway",
            "t": "Birthplace of Muhammad, around 570",
            "k": ["birthplace", "muhammad", "570"],
            "n": 0,
            "rabbit": "Muhammad"
        },
        {
            "id": "hijra",
            "tier": "middle",
            "t": "Muhammad left it for Medina in the Hijra (622), year 1 of the Islamic calendar",
            "k": ["hijra", "medina", "622"],
            "n": 0
        },
        {
            "id": "conquest-630",
            "tier": "middle",
            "t": "Muhammad returned in 630 with about 10,000 followers, met little fighting, and cleared the idols from the Kaaba",
            "k": ["630", "10,000", "idols"],
            "n": 0
        },
        {
            "id": "non-muslims",
            "tier": "middle",
            "t": "Only Muslims may enter the city; highway signs direct others away",
            "k": ["only muslims", "non-muslims", "highway signs"],
            "n": 0
        },
        {
            "id": "quraysh",
            "tier": "middle",
            "t": "The Quraysh tribe controlled its trade and opposed Muhammad’s early preaching",
            "k": ["quraysh", "trade"],
            "n": 0
        },
        {
            "id": "masjid-al-haram",
            "tier": "middle",
            "t": "The Masjid al-Haram (Great Mosque), the world’s largest mosque, surrounds the Kaaba",
            "k": ["masjid al-haram", "largest mosque"],
            "n": 0
        },
        {
            "id": "hira",
            "tier": "middle",
            "t": "Muslims believe Muhammad received the first revelation around 610 in the cave of Hira, on the nearby Mountain of Light (Jabal al-Nour)",
            "k": ["hira", "mountain of light", "jabal al-nour"],
            "n": 0
        },
        {
            "id": "zamzam",
            "tier": "middle",
            "t": "The Zamzam well, which Muslims believe appeared for Hagar and her baby Ishmael",
            "k": ["zamzam", "hagar", "well"],
            "n": 0
        },
        {
            "id": "mihrab",
            "tier": "middle",
            "t": "A mihrab, a niche in a mosque wall, points toward it",
            "k": ["mihrab", "niche"],
            "n": 0
        },
        {
            "id": "hajj-sites",
            "tier": "middle",
            "t": "During the Hajj, pilgrims go out to Mina, Arafat, and Muzdalifah, then return to circle the Kaaba",
            "k": ["mina", "arafat", "muzdalifah"],
            "n": 0
        },
        {
            "id": "sharif-1916",
            "tier": "power",
            "t": "In 1916 its Sharif, Hussein bin Ali, began the Arab Revolt against the Ottoman Empire",
            "k": ["sharif", "hussein", "arab revolt", "1916"],
            "n": 0
        },
        {
            "id": "ibn-saud",
            "tier": "power",
            "t": "Ibn Saud’s forces captured it in 1924; it later became part of Saudi Arabia",
            "k": ["ibn saud", "1924"],
            "n": 0
        },
        {
            "id": "elephant",
            "tier": "power",
            "t": "Year of the Elephant: Abraha of Yemen marched on it with an elephant, remembered in the Quran’s chapter “The Elephant”",
            "k": ["abraha", "year of the elephant", "elephant"],
            "n": 0
        },
        {
            "id": "clock-tower",
            "tier": "power",
            "t": "The clock tower of the Abraj Al Bait towers (finished 2012) is one of the world’s tallest buildings and has the world’s largest clock faces",
            "k": ["abraj al bait", "clock", "2012"],
            "n": 0
        },
        {
            "id": "umm-al-qura",
            "tier": "power",
            "t": "The Quran calls it Umm al-Qura (“Mother of Cities”); one verse calls it Bakkah",
            "k": ["umm al-qura", "mother of cities", "bakkah"],
            "n": 0
        },
        {
            "id": "burton",
            "tier": "power",
            "t": "Richard Francis Burton entered it in disguise in 1853 and wrote about his pilgrimage",
            "k": ["burton", "disguise", "1853"],
            "n": 0
        },
        {
            "id": "hubal",
            "tier": "power",
            "t": "Before Islam, the Kaaba held idols of many gods, including Hubal",
            "k": ["hubal", "idols"],
            "n": 0
        },
        {
            "id": "thawr",
            "tier": "power",
            "t": "During the Hijra, Muhammad and Abu Bakr hid for three days in the cave of Thawr",
            "k": ["thawr", "abu bakr"],
            "n": 0
        },
        {
            "id": "night-journey",
            "tier": "power",
            "t": "Quran chapter 17, “The Night Journey”: God carried Muhammad by night from its Sacred Mosque to the Farthest Mosque (Jerusalem)",
            "k": ["night journey", "sacred mosque", "farthest mosque"],
            "n": 0,
            "rabbit": "Jerusalem"
        },
        {
            "id": "custodian",
            "tier": "power",
            "t": "Saudi kings take the title “Custodian of the Two Holy Mosques” (its Great Mosque and Medina’s Prophet’s Mosque)",
            "k": ["custodian", "two holy mosques"],
            "n": 0
        },
        {
            "id": "abd-al-muttalib",
            "tier": "power",
            "t": "Muhammad’s grandfather Abd al-Muttalib, a Quraysh leader, is said to have dug out the long-lost Zamzam well",
            "k": ["abd al-muttalib", "grandfather"],
            "n": 0
        },
        {
            "id": "travelers",
            "tier": "power",
            "t": "Mansa Musa (1324), Ibn Battuta (1325), and Malcolm X (1964) all made the pilgrimage here",
            "k": ["mansa musa", "ibn battuta", "malcolm x"],
            "n": 0
        },
        {
            "id": "battles",
            "tier": "power",
            "t": "Its army lost at Badr (624), fought at Uhud (625) under Abu Sufyan, and besieged Medina at the Trench (627)",
            "k": ["badr", "uhud", "abu sufyan", "trench"],
            "n": 0
        },
        {
            "id": "jeddah-hejaz",
            "tier": "power",
            "t": "It lies in a narrow valley in the Hejaz region; pilgrims arrive through Jeddah, a Red Sea port about 70 km west",
            "k": ["hejaz", "jeddah", "valley"],
            "n": 0
        }
    ],
    "trap": {
        "title": "City, not shrine",
        "body": "Clues about this city are full of things inside it, so players blurt “Kaaba,” “Masjid al-Haram,” or “Hajj,” which name a shrine, a mosque, and a pilgrimage, not the city. Medina, Islam’s second-holiest city, is the other trap: Muhammad moved there in the Hijra, built his mosque there, and is buried there.",
        "fix": "If the question says “this city,” answer Mecca (or Makkah). Muhammad’s birthplace, the qibla, the Kaaba, and Zamzam mean Mecca; the old name Yathrib, the Prophet’s Mosque, the Ansar, and Muhammad’s tomb mean Medina; al-Aqsa and the Dome of the Rock mean Jerusalem.",
        "line": "Real answer line: " + LINE
    },
    "tests": {
        "right": [
            "Mecca",
            "Makkah",
            "Mekka",
            "Meca",
            "Mecca, Saudi Arabia",
            "Makkah al-Mukarramah"
        ],
        "prompt": [],
        "wrong": [
            "Medina",
            "Kaaba",
            "Hajj",
            "Masjid al-Haram",
            "Jerusalem",
            "Jeddah",
            "Great Mosque of Mecca"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
