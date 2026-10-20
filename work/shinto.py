import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

LINE = "<b><u>Shinto</u></b> (or <u>Shintoism</u>; accept <u>kami-no-michi</u>)"

data = {
    "id": "shinto",
    "name": "Shinto",
    "mono": "SHN",
    "category": "Religion",
    "qbCategory": "Religion",
    "kicker": "Native religion of Japan · Kami spirits, shrines, and torii gates",
    "dates": "Ancient · Myths first written down in 712 CE",
    "briefing": "Walk through an orange-red torii gate in Japan and you enter a Shinto shrine, a place where people honor kami: spirits found in mountains, waterfalls, and ancient trees, in ancestors, and even in great scholars. Shinto has no founder and no single holy book, but its myths, written down in the _Kojiki_ in 712 CE, tell how the sun goddess Amaterasu became the ancestor of Japan’s emperors.",
    "answerHtml": LINE,
    "accept": [
        "shinto",
        "shintoism",
        "shinto religion",
        "shintoist",
        "shinto faith",
        "kami no michi",
        "kaminomichi"
    ],
    "prompt": [],
    "reject": [
        "buddhism",
        "zen",
        "zen buddhism",
        "amaterasu",
        "taoism",
        "daoism",
        "confucianism",
        "bushido",
        "shintai",
        "shingon",
        "tendai",
        "shinran",
        "shinshu",
        "tenrikyo"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Shinto",
    "qb": {"q": "Shinto", "found": 0, "tip": TIP},
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        {
            "p": "The scholar Motoori Norinaga [“moh-toh-OH-ree noh-ree-NAH-gah”] spent decades writing a commentary on the _Kojiki_ [“KOH-jee-kee”], hoping to recover the beliefs of this religion as they were before Buddhism and Confucianism reached Japan. He belonged to the National Learning, or Kokugaku [“koh-koo-GAH-koo”], movement of the 1700s.",
            "r": "Its spirits are called kami. For 10 points, name this native religion of Japan, whose shrines are marked by torii gates."
        },
        {
            "p": "Every 20 years, the main buildings of this religion’s holiest shrine, at Ise [“EE-say”], are rebuilt on a neighboring site using the same ancient methods, a ritual that was held for the 62nd time in 2013. That ritual is called the Shikinen Sengu [“shee-kee-NEN SEN-goo”].",
            "r": "That shrine honors the sun goddess Amaterasu. For 10 points, name this native religion of Japan."
        },
        {
            "p": "In 712 CE, the court official Ō no Yasumaro [“OH noh yah-soo-MAH-roh”] wrote down myths that Hieda no Are [“hee-EH-dah noh AH-reh”] had memorized, producing the _Kojiki_, a key text of this religion. The _Nihon Shoki_ [“nee-HOHN SHOH-kee”] followed in 720.",
            "r": "Those books tell of spirits called kami, such as the sun goddess Amaterasu. For 10 points, name this native religion of Japan."
        },
        {
            "p": "In this religion’s creation story, the divine couple Izanagi [“ee-zah-NAH-gee”] and Izanami [“ee-zah-NAH-mee”] stirred the ocean with a jeweled spear, and the drops that fell from its tip formed the first island. They went on to create the islands of Japan.",
            "r": "The sun goddess Amaterasu was born when Izanagi washed his left eye. For 10 points, name this native religion of Japan."
        },
        {
            "p": "In one myth of this religion, the world went dark when the sun goddess shut herself in a cave, until the goddess Ame-no-Uzume [“AH-meh noh oo-ZOO-meh”] danced on an overturned tub so wildly that the other gods roared with laughter. A mirror hung outside helped draw the sun goddess back out.",
            "r": "That sun goddess, Amaterasu, is honored at the Ise Shrine. For 10 points, name this religion of Japan."
        },
        {
            "p": "In a myth of this religion, the storm god Susanoo [“soo-SAH-noh-oh”] tricked the eight-headed serpent Yamata no Orochi [“yah-MAH-tah noh oh-ROH-chee”] and slew it, then found the sword Kusanagi [“koo-sah-NAH-gee”] inside one of its tails. Susanoo did this to save a young woman named Kushinada-hime [“koo-shee-NAH-dah HEE-meh”], whom he then married.",
            "r": "That sword became one of Japan’s three Imperial Regalia. For 10 points, name this religion, whose kami include Susanoo’s sister Amaterasu."
        },
        {
            "p": "In this religion’s myths, the sun goddess gave her grandson Ninigi [“nee-NEE-gee”] a mirror, a sword, and a jewel when she sent him down from heaven to rule Japan. Ninigi’s great-grandson Jimmu was said to be the first emperor.",
            "r": "Those three treasures became the Imperial Regalia. For 10 points, name this native religion of Japan, which honors kami."
        },
        {
            "p": "In 1868, Japan’s new Meiji [“MAY-jee”] government ordered this religion’s shrines to be separated from Buddhist temples and later promoted a state form of this religion. After World War II, a 1945 directive from the Allied occupation ended government support for it.",
            "r": "For 10 points, name this native religion of Japan, whose priests serve spirits called kami."
        },
        {
            "p": "Students often pray for success on exams at shrines of this religion devoted to Tenjin [“TEN-jin”], the spirit of the scholar Sugawara no Michizane [“soo-gah-WAH-rah noh mee-chee-ZAH-neh”], who came to be honored as a spirit of learning after his death.",
            "r": "Visitors write their wishes on small wooden plaques called ema. For 10 points, name this native religion of Japan, whose shrines are marked by torii."
        },
        {
            "p": "Statues of foxes, believed to be messengers of the rice deity Inari [“ee-NAH-ree”], guard many shrines of this religion. The head shrine of Inari, Fushimi Inari [“foo-SHEE-mee ee-NAH-ree”] in Kyoto, sits at the foot of a sacred mountain.",
            "r": "Thousands of bright orange torii gates line the paths up that mountain. For 10 points, name this religion of Japan."
        },
        {
            "p": "Before approaching a shrine of this religion, visitors rinse their hands and mouth with water from a stone basin, a purification rite called temizu [“teh-MEE-zoo”]. Priests also purify worshippers by waving a wooden wand covered with white paper streamers.",
            "r": "The entrance to such a shrine is marked by a gateway called a torii. For 10 points, name this religion."
        },
        {
            "p": "Thick ropes of rice straw called shimenawa [“shee-meh-NAH-wah”], often hung with zigzag strips of white paper, mark trees, rocks, and other places that this religion treats as sacred. Sumo wrestlers toss salt into the ring before bouts, a purification ritual with roots in this religion.",
            "r": "Many of those sacred places are believed to be home to spirits called kami. For 10 points, name this religion of Japan."
        },
        {
            "p": "The shrine of Itsukushima [“ee-tsoo-koo-SHEE-mah”] on the island of Miyajima [“mee-yah-JEE-mah”] is built over the water, so that at high tide it seems to float. Its huge gate, which stands in the sea, is one of Japan’s most famous sights.",
            "r": "That gate is a torii, the symbol of this religion’s shrines. For 10 points, name this native religion of Japan."
        },
        {
            "p": "On the festival of Shichi-Go-San [“shee-chee-goh-SAHN”], or “Seven-Five-Three,” families take children of those ages to shrines of this religion to pray for their health. Millions of people also visit those shrines in the first days of each new year, a custom called hatsumode [“hah-tsoo-MOH-deh”].",
            "r": "Festivals called matsuri often feature portable shrines carried through the streets. For 10 points, name this native religion of Japan, which honors spirits called kami."
        },
        {
            "p": "For centuries, many people in Japan treated this religion’s spirits as local forms of buddhas, an idea called honji suijaku [“HOHN-jee soo-ee-JAH-koo”]. Babies are often blessed at this religion’s shrines, but because it links death with impurity, most funerals in Japan follow Buddhist rites.",
            "r": "For 10 points, name this native religion of Japan, centered on shrines and spirits called kami."
        }
    ],
    "clues": [
        {
            "id": "japan",
            "tier": "giveaway",
            "t": "Native religion of Japan, with no founder and no single holy book",
            "k": ["japan", "native", "no founder"],
            "n": 0
        },
        {
            "id": "kami",
            "tier": "giveaway",
            "t": "Honors kami: spirits or gods found in nature, places, ancestors, and great people",
            "k": ["kami", "spirits", "nature"],
            "n": 0
        },
        {
            "id": "torii",
            "tier": "giveaway",
            "t": "Its shrines are marked by torii, gateways that are often painted orange-red",
            "k": ["torii", "shrines", "gateways"],
            "n": 0
        },
        {
            "id": "amaterasu",
            "tier": "giveaway",
            "t": "The sun goddess Amaterasu is its most important kami; in myth, Japan’s emperors descend from her",
            "k": ["amaterasu", "sun goddess", "emperors"],
            "n": 0,
            "rabbit": "Amaterasu"
        },
        {
            "id": "way-of-gods",
            "tier": "giveaway",
            "t": "Its name means “way of the gods”",
            "k": ["way of the gods", "gods"],
            "n": 0
        },
        {
            "id": "ise",
            "tier": "middle",
            "t": "Ise Grand Shrine, its holiest shrine, honors Amaterasu and is rebuilt every 20 years",
            "k": ["ise", "rebuilt", "20 years"],
            "n": 0
        },
        {
            "id": "kojiki",
            "tier": "middle",
            "t": "Key texts: the _Kojiki_ (712) and _Nihon Shoki_ (720), Japan’s oldest books of myths and history",
            "k": ["kojiki", "nihon shoki", "712"],
            "n": 0
        },
        {
            "id": "izanagi",
            "tier": "middle",
            "t": "Creator couple Izanagi and Izanami stirred the sea with a jeweled spear to make the first island",
            "k": ["izanagi", "izanami", "jeweled spear"],
            "n": 0
        },
        {
            "id": "cave",
            "tier": "middle",
            "t": "Amaterasu hid in a cave and the world went dark until Ame-no-Uzume’s dance and a mirror drew her out",
            "k": ["cave", "ame-no-uzume", "mirror"],
            "n": 0
        },
        {
            "id": "susanoo",
            "tier": "middle",
            "t": "Storm god Susanoo slew the eight-headed serpent Yamata no Orochi and found the sword Kusanagi in its tail",
            "k": ["susanoo", "yamata no orochi", "kusanagi"],
            "n": 0
        },
        {
            "id": "regalia",
            "tier": "middle",
            "t": "Three Imperial Regalia: a mirror, a sword (Kusanagi), and a jewel",
            "k": ["imperial regalia", "mirror", "jewel"],
            "n": 0
        },
        {
            "id": "purification",
            "tier": "middle",
            "t": "Purification is central: visitors rinse hands and mouth (temizu) before praying, and priests wave paper-streamer wands",
            "k": ["purification", "temizu", "rinse"],
            "n": 0
        },
        {
            "id": "buddhism",
            "tier": "middle",
            "t": "Mixed with Buddhism for centuries until the Meiji government separated them in 1868",
            "k": ["buddhism", "meiji", "1868"],
            "n": 0,
            "rabbit": "Zen Buddhism"
        },
        {
            "id": "matsuri",
            "tier": "middle",
            "t": "Festivals (matsuri) carry portable shrines (mikoshi) through the streets",
            "k": ["matsuri", "mikoshi", "portable shrines"],
            "n": 0
        },
        {
            "id": "motoori",
            "tier": "power",
            "t": "Motoori Norinaga, a National Learning (Kokugaku) scholar of the 1700s, studied the _Kojiki_ to recover pre-Buddhist beliefs",
            "k": ["motoori norinaga", "kokugaku", "national learning"],
            "n": 0
        },
        {
            "id": "yasumaro",
            "tier": "power",
            "t": "Ō no Yasumaro wrote the _Kojiki_ from myths memorized by Hieda no Are",
            "k": ["yasumaro", "hieda no are"],
            "n": 0
        },
        {
            "id": "jimmu",
            "tier": "power",
            "t": "Amaterasu’s grandson Ninigi came down to rule Japan; his great-grandson Jimmu was, in myth, the first emperor",
            "k": ["ninigi", "jimmu", "first emperor"],
            "n": 0
        },
        {
            "id": "directive-1945",
            "tier": "power",
            "t": "A 1945 directive from the Allied occupation ended state support for this faith after World War II",
            "k": ["1945", "directive", "occupation"],
            "n": 0
        },
        {
            "id": "tenjin",
            "tier": "power",
            "t": "Tenjin, the spirit of the scholar Sugawara no Michizane, is honored for learning; students pray at his shrines before exams",
            "k": ["tenjin", "michizane", "exams"],
            "n": 0
        },
        {
            "id": "inari",
            "tier": "power",
            "t": "Inari, the kami of rice, uses foxes as messengers; Kyoto’s Fushimi Inari shrine has thousands of torii",
            "k": ["inari", "foxes", "fushimi"],
            "n": 0
        },
        {
            "id": "shimenawa",
            "tier": "power",
            "t": "Shimenawa (rice-straw ropes) hung with zigzag paper strips mark sacred places",
            "k": ["shimenawa", "straw", "zigzag"],
            "n": 0
        },
        {
            "id": "sumo",
            "tier": "power",
            "t": "Sumo wrestlers throw salt into the ring to purify it, a ritual rooted in this faith",
            "k": ["sumo", "salt"],
            "n": 0
        },
        {
            "id": "itsukushima",
            "tier": "power",
            "t": "Itsukushima Shrine on Miyajima seems to float at high tide, and its torii stands in the sea",
            "k": ["itsukushima", "miyajima", "high tide"],
            "n": 0
        },
        {
            "id": "shichi-go-san",
            "tier": "power",
            "t": "Shichi-Go-San: children aged 3, 5, and 7 visit shrines; hatsumode is the first shrine visit of the new year",
            "k": ["shichi-go-san", "hatsumode", "seven-five-three"],
            "n": 0
        },
        {
            "id": "honji-suijaku",
            "tier": "power",
            "t": "Honji suijaku: the idea that kami are local forms of buddhas",
            "k": ["honji suijaku", "buddhas"],
            "n": 0
        },
        {
            "id": "kegare",
            "tier": "power",
            "t": "Death is linked with impurity (kegare), so most funerals are Buddhist, while babies are blessed at shrines",
            "k": ["kegare", "impurity", "funerals"],
            "n": 0
        },
        {
            "id": "ema",
            "tier": "power",
            "t": "Visitors write wishes on wooden plaques called ema",
            "k": ["ema", "wooden plaques", "wishes"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Religion or spirits?",
        "body": "Shinto clues are full of kami, the spirits it honors, and some tossups ask for the kami themselves, so answering “kami” to a question about the religion (or “Shinto” to a question about the spirits) loses the points. Buddhism is the other trap: most people in Japan take part in both, and shrines and temples often stand side by side.",
        "fix": "Listen to the noun: “these spirits” or “these beings” means kami; “this religion” or “this faith” means Shinto (or Shintoism). Shrines, torii, Amaterasu, and the _Kojiki_ mean Shinto; temples, pagodas, Zen, and the Buddha mean Buddhism.",
        "line": "Real answer line: " + LINE
    },
    "tests": {
        "right": [
            "Shinto",
            "Shintoism",
            "Shintō",
            "kami-no-michi",
            "Shinto religion",
            "Shintu"
        ],
        "prompt": [],
        "wrong": [
            "Buddhism",
            "Zen Buddhism",
            "Kami",
            "Amaterasu",
            "Confucianism",
            "Taoism"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
