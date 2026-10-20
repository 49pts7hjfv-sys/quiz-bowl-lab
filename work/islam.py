import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "islam",
    "name": "Islam",
    "mono": "IS",
    "category": "Religion",
    "qbCategory": "Religion",
    "kicker": "Faith of the Quran and the Prophet Muhammad · World’s second-largest religion",
    "dates": "Began in Arabia in the 600s CE",
    "briefing": "Five times a day, a call to prayer rings out from the towers of mosques, and Muslims around the world turn toward the Kaaba in Mecca to pray. Islam, whose name means “submission” to God, teaches that there is one God (Allah in Arabic) and that Muhammad was God’s final prophet. With nearly two billion followers, it is the world’s second-largest religion, and its believers follow the Five Pillars, from daily prayer to the pilgrimage called the Hajj.",
    "answerHtml": "<b><u>Islam</u></b> (accept word forms like <u>Muslim</u>s or the <u>Islamic</u> faith; do not accept a single branch such as “Sunni” or “Shia”; do not accept “Nation of Islam”)",
    "accept": [
        "islam",
        "muslim",
        "muslims",
        "moslem",
        "moslems",
        "islamic",
        "islamic faith",
        "islamic religion",
        "religion of islam",
        "muslim faith",
        "muslim religion",
        "al islam"
    ],
    "prompt": [],
    "reject": [
        "sunni",
        "sunnis",
        "sunni islam",
        "shia",
        "shias",
        "shia islam",
        "shiite",
        "shiites",
        "shiism",
        "ismaili",
        "ismailis",
        "sufism",
        "sufi",
        "sufis",
        "nation of islam",
        "black muslims",
        "ahmadiyya",
        "muhammad",
        "mohammed",
        "quran",
        "koran",
        "mecca",
        "makkah",
        "medina",
        "hajj",
        "ramadan",
        "five pillars",
        "five pillars of islam",
        "pillars of islam",
        "sharia",
        "hadith",
        "allah",
        "judaism",
        "christianity",
        "bahai",
        "bahai faith",
        "sikhism",
        "druze",
        "zoroastrianism"
    ],
    "tests": {
        "right": [
            "Islam",
            "Muslims",
            "the Islamic faith",
            "Islaam",
            "Muslim religion"
        ],
        "prompt": [],
        "wrong": [
            "Sunni",
            "Shia Islam",
            "Nation of Islam",
            "Muhammad",
            "Quran",
            "Christianity",
            "Sufism",
            "Five Pillars of Islam"
        ]
    },
    "mediaPending": True,
    "media": [],
    "wiki": "https://en.wikipedia.org/wiki/Islam",
    "qb": {
        "q": "Islam",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "On the day of Ashura [“AH-shoo-rah”], members of one branch of this religion mourn Husayn [“hoo-SAYN”], a grandson of its final prophet, who was killed with his small band of followers at the Battle of Karbala [“KAR-buh-luh”] in 680 CE. That branch believes Husayn’s father, Ali, should have been the community’s first leader.",
            "r": "That branch is Shia; the larger branch is Sunni. For 10 points, name this religion whose final prophet, its followers believe, was Muhammad."
        },
        {
            "p": "Each prayer in this religion is made up of units called rak’ahs [“RAK-ahz”], which include bowing and touching the forehead to the ground. Before praying, followers wash their hands, face, arms, and feet in a ritual called wudu [“woo-DOO”], and the day’s required prayers run from Fajr [“FAJ-er”] at dawn to Isha [“ih-SHAH”] at night.",
            "r": "Those five daily prayers, called salat, are one of its Five Pillars. For 10 points, name this religion whose followers pray facing Mecca."
        },
        {
            "p": "Abu Bakr, Umar, Uthman [“ooth-MAHN”], and Ali are honored as the four “Rightly Guided” caliphs [“KAY-lifs”] by this religion’s largest branch. After Ali’s death in 661, the Umayyad [“oo-MY-ad”] family took control of the caliphate and ruled from Damascus.",
            "r": "The caliphs were seen as successors to the Prophet Muhammad. For 10 points, name this religion whose holy book is the Quran."
        },
        {
            "p": "According to this religion’s tradition, the angel Israfil [“iz-rah-FEEL”] will blow a trumpet to announce the Day of Judgment, and two angels named Munkar [“MOON-kar”] and Nakir [“nah-KEER”] question each person in the grave. Belief in angels is one of its six articles of faith, along with belief in God’s prophets and holy books.",
            "r": "Its followers believe the angel Gabriel revealed the Quran to Muhammad. For 10 points, name this religion."
        },
        {
            "p": "A niche called a mihrab [“MIH-rahb”] shows worshippers which way to face in this religion’s houses of worship, and on Fridays a preacher gives a sermon from a stepped pulpit called a minbar. Five times a day, a man called a muezzin [“moo-EZ-in”] chants the call to prayer, or adhan [“ah-THAHN”], from a tall tower.",
            "r": "Those towers are minarets, and those buildings are mosques. For 10 points, name this religion whose followers face Mecca to pray."
        },
        {
            "p": "Years in this religion’s calendar are often marked AH, for the Latin words Anno Hegirae [“AN-oh heh-JY-ree”], because that calendar counts from the year 622 CE. It follows the moon, so its year is only about 354 days long, and its holy month of fasting moves through all the seasons over time.",
            "r": "Year one is the year of the Hijra, when Muhammad moved from Mecca to Medina. For 10 points, name this religion."
        },
        {
            "p": "According to this religion’s teachings, God sent earlier scriptures, including the Tawrat [“tow-RAHT”] to Moses, the Zabur [“zah-BOOR”] to David, and the Injil [“in-JEEL”] to Jesus, whom its followers honor as a prophet named Isa [“EE-sah”]. This religion calls Jews and Christians “People of the Book.”",
            "r": "Its followers believe its final scripture, the Quran, was revealed to Muhammad. For 10 points, name this religion."
        },
        {
            "p": "Followers of this religion whose savings stay above a set minimum for a full lunar year are expected to give a share, usually 2.5 percent, to the poor and others in need. That required charity is called zakat [“zuh-KAHT”], and many believers choose to pay it during their holy month of fasting.",
            "r": "Zakat is one of the Five Pillars, along with the Shahada and daily prayer. For 10 points, name this religion whose followers fast during Ramadan."
        },
        {
            "p": "The poet Rumi [“ROO-mee”] belonged to a mystical movement within this religion, and after his death his followers in Konya [“KOHN-yah”], Turkey, founded the Mevlevi [“MEV-leh-vee”] order, whose members spin in a prayerful dance as “whirling dervishes.” That mystical movement is called Sufism.",
            "r": "Sufis seek a close, personal experience of God, whom followers of this religion call Allah. For 10 points, name this religion of the Quran."
        },
        {
            "p": "In 732 CE, Charles Martel’s Franks defeated an Umayyad [“oo-MY-ad”] army from Spain at the Battle of Tours [“TOOR”], stopping its advance into France. For centuries, rulers who followed this religion held much of Spain, where they built a vast house of worship in Córdoba [“KOR-doh-bah”] famous for its red-and-white striped arches.",
            "r": "Today, Indonesia has more followers of this religion than any other country. For 10 points, name this religion whose final prophet, its followers believe, was Muhammad."
        },
        {
            "p": "Most members of one branch of this religion are “Twelvers,” who believe that the twelfth of their imams [“ih-MAHMZ”] went into hiding in the 800s and will one day return as the Mahdi [“MAH-dee”]. Iran is the largest country where most people belong to that branch, which honors Ali as the first imam.",
            "r": "That branch is Shia, and the larger branch is Sunni. For 10 points, name this religion that follows the teachings of Muhammad."
        },
        {
            "p": "This religion’s name comes from an Arabic word meaning “submission” to God, and that word shares a root with salaam [“sah-LAHM”], meaning “peace.” Its followers often greet each other with the words “as-salamu alaykum” [“ah-sah-LAH-moo ah-LAY-koom”], meaning “peace be upon you.”",
            "r": "Its declaration of faith, the Shahada, says there is no god but God and that Muhammad is God’s messenger. For 10 points, name this religion."
        },
        {
            "p": "Followers of this religion eat food that is halal [“hah-LAHL”], meaning “permitted,” and avoid foods and drinks that are haram [“hah-RAHM”], or “forbidden,” such as pork and alcohol. For meat to be halal, God’s name must be spoken when the animal is killed for food.",
            "r": "For 10 points, name this religion whose followers fast from dawn to sunset during the month of Ramadan."
        },
        {
            "p": "Before the special morning prayer of one festival of this religion, held on the first day of the month of Shawwal [“shah-WAHL”], believers give a charity gift so that poor families can celebrate too. Another festival remembers Abraham’s willingness to sacrifice his son, and many families share the meat of a sacrificed animal with relatives, neighbors, and the poor.",
            "r": "Those festivals are Eid al-Fitr and Eid al-Adha, which falls during the Hajj. For 10 points, name this religion."
        },
        {
            "p": "In 1924, the new Republic of Turkey abolished the office of caliph, a title that Ottoman sultans had claimed since 1517. Centuries earlier, Abbasid [“uh-BASS-id”] caliphs in Baghdad supported a House of Wisdom, where scholars translated Greek books into Arabic during this religion’s Golden Age.",
            "r": "The first caliphs led the community after the death of Muhammad. For 10 points, name this religion whose holy book is the Quran."
        }
    ],
    "clues": [
        {
            "id": "muhammad",
            "tier": "giveaway",
            "t": "Its followers regard Muhammad as God’s final prophet and believe the angel Gabriel revealed the Quran to him",
            "k": ["muhammad", "final prophet", "gabriel"],
            "n": 0,
            "rabbit": "Muhammad"
        },
        {
            "id": "quran",
            "tier": "giveaway",
            "t": "Holy book: the Quran, which believers regard as the word of God revealed in Arabic",
            "k": ["quran", "arabic", "holy book"],
            "n": 0,
            "rabbit": "Quran"
        },
        {
            "id": "one-god",
            "tier": "giveaway",
            "t": "Strictly monotheistic: there is one God, called Allah in Arabic",
            "k": ["allah", "one god", "monotheistic"],
            "n": 0
        },
        {
            "id": "five-pillars",
            "tier": "giveaway",
            "t": "The Five Pillars: Shahada (declaration of faith), salat (prayer), zakat (charity), sawm (fasting), and Hajj (pilgrimage)",
            "k": ["five pillars", "shahada", "salat", "sawm"],
            "n": 0
        },
        {
            "id": "second-largest",
            "tier": "giveaway",
            "t": "The world’s second-largest religion, with nearly two billion followers; Indonesia has more of them than any other country",
            "k": ["second-largest", "two billion", "indonesia"],
            "n": 0
        },
        {
            "id": "sunni-shia",
            "tier": "middle",
            "t": "Two main branches: Sunni, the large majority, and Shia, who believe Muhammad’s cousin Ali should have been his first successor",
            "k": ["sunni", "shia", "ali"],
            "n": 0
        },
        {
            "id": "hijra",
            "tier": "middle",
            "t": "The Hijra (622): Muhammad’s move from Mecca to Medina, year 1 of its lunar calendar; years are marked AH (Anno Hegirae)",
            "k": ["hijra", "622", "medina", "anno hegirae"],
            "n": 0
        },
        {
            "id": "mosque",
            "tier": "middle",
            "t": "House of worship: the mosque (masjid); a muezzin chants the call to prayer (adhan) from a tower called a minaret",
            "k": ["mosque", "minaret", "muezzin", "adhan"],
            "n": 0
        },
        {
            "id": "salat",
            "tier": "middle",
            "t": "Salat: five daily prayers facing the Kaaba in Mecca (the qibla), after a ritual washing called wudu",
            "k": ["salat", "five daily", "qibla", "wudu", "kaaba"],
            "n": 0
        },
        {
            "id": "ramadan",
            "tier": "middle",
            "t": "Believers fast from dawn to sunset during Ramadan, which ends with the festival of Eid al-Fitr",
            "k": ["ramadan", "eid al-fitr", "fast"],
            "n": 0,
            "rabbit": "Ramadan"
        },
        {
            "id": "hajj",
            "tier": "middle",
            "t": "The Hajj: a pilgrimage to Mecca required once in a lifetime of all who are able; Eid al-Adha falls during it",
            "k": ["hajj", "pilgrimage", "eid al-adha"],
            "n": 0,
            "rabbit": "Hajj"
        },
        {
            "id": "submission",
            "tier": "middle",
            "t": "Its name means “submission” to God and shares an Arabic root with salaam (“peace”)",
            "k": ["submission", "salaam", "peace"],
            "n": 0
        },
        {
            "id": "people-of-the-book",
            "tier": "middle",
            "t": "Honors earlier prophets such as Abraham, Moses, and Jesus (Isa); calls Jews and Christians “People of the Book”",
            "k": ["people of the book", "isa", "abraham"],
            "n": 0
        },
        {
            "id": "ashura",
            "tier": "power",
            "t": "On Ashura, Shia believers mourn Muhammad’s grandson Husayn, killed at the Battle of Karbala in 680",
            "k": ["ashura", "karbala", "husayn"],
            "n": 0
        },
        {
            "id": "twelvers",
            "tier": "power",
            "t": "Most Shia are Twelvers, who await the return of a hidden twelfth imam, the Mahdi; Iran is the largest Shia-majority country",
            "k": ["twelvers", "mahdi", "imam", "iran"],
            "n": 0
        },
        {
            "id": "rashidun",
            "tier": "power",
            "t": "The four “Rightly Guided” (Rashidun) caliphs: Abu Bakr, Umar, Uthman, and Ali",
            "k": ["rightly guided", "rashidun", "abu bakr", "caliphs"],
            "n": 0
        },
        {
            "id": "umayyad-abbasid",
            "tier": "power",
            "t": "Later caliphs: the Umayyads ruled from Damascus, and the Abbasids from Baghdad, home of the House of Wisdom",
            "k": ["umayyads", "abbasids", "damascus", "house of wisdom"],
            "n": 0
        },
        {
            "id": "six-articles",
            "tier": "power",
            "t": "Six articles of faith: belief in God, angels, holy books, prophets, the Day of Judgment, and God’s decree",
            "k": ["six articles", "angels", "day of judgment"],
            "n": 0
        },
        {
            "id": "angels",
            "tier": "power",
            "t": "Tradition says the angel Israfil will blow the trumpet of Judgment Day, and the angels Munkar and Nakir question the dead",
            "k": ["israfil", "munkar", "nakir", "trumpet"],
            "n": 0
        },
        {
            "id": "earlier-scriptures",
            "tier": "power",
            "t": "Earlier scriptures it honors: the Tawrat (Torah) of Moses, the Zabur (Psalms) of David, and the Injil (Gospel) of Jesus",
            "k": ["tawrat", "zabur", "injil"],
            "n": 0
        },
        {
            "id": "mihrab-minbar",
            "tier": "power",
            "t": "A mosque’s mihrab (a niche) shows the direction of Mecca; the Friday sermon is given from a pulpit called a minbar",
            "k": ["mihrab", "minbar", "niche", "friday"],
            "n": 0
        },
        {
            "id": "zakat",
            "tier": "power",
            "t": "Zakat: required charity, usually 2.5 percent of savings held for a full lunar year",
            "k": ["zakat", "2.5 percent", "charity"],
            "n": 0
        },
        {
            "id": "rakah",
            "tier": "power",
            "t": "Daily prayers run from Fajr (dawn) to Isha (night); each is made of units called rak’ahs, with bowing and prostration",
            "k": ["fajr", "isha", "prostration", "units"],
            "n": 0
        },
        {
            "id": "sufism",
            "tier": "power",
            "t": "Sufism is its mystical tradition; the poet Rumi’s followers in Konya founded the Mevlevi order of “whirling dervishes”",
            "k": ["sufism", "rumi", "whirling dervishes", "mevlevi"],
            "n": 0
        },
        {
            "id": "tours-cordoba",
            "tier": "power",
            "t": "Charles Martel halted its rulers’ advance into France at the Battle of Tours (732); in Spain they built the Great Mosque of Córdoba",
            "k": ["tours", "charles martel", "córdoba"],
            "n": 0
        },
        {
            "id": "halal",
            "tier": "power",
            "t": "Halal (“permitted”) food rules; pork and alcohol are haram (“forbidden”)",
            "k": ["halal", "haram", "pork"],
            "n": 0
        },
        {
            "id": "caliphate-1924",
            "tier": "power",
            "t": "Ottoman sultans claimed the title of caliph from 1517 until the Republic of Turkey abolished the caliphate in 1924",
            "k": ["1924", "caliphate", "ottoman"],
            "n": 0,
            "rabbit": "Ottoman Empire"
        }
    ],
    "trap": {
        "title": "Religion, not prophet",
        "body": "Islam tossups are crowded with other answer lines: Muhammad, the Quran, Mecca, the Hajj, and Ramadan all get tossups of their own, and their clues pile up in the middle of an Islam question. Clues like “one branch of this religion” mourning Husayn tempt players to say “Shia,” but a single branch is not accepted when the question wants the whole faith. The Nation of Islam, an American movement once led by Elijah Muhammad, is a different answer line too.",
        "fix": "Listen for the noun. “This religion” or “this faith” means Islam (or Muslims). “This prophet” means Muhammad, “this book” means the Quran, “this city” means Mecca, and “this month” means Ramadan. Say Sunni or Shia only when the question asks for “this branch” or “this sect.”",
        "line": "Real answer line: <b><u>Islam</u></b> (accept word forms like <u>Muslim</u>s; do not accept a single branch such as “Sunni” or “Shia”)"
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
