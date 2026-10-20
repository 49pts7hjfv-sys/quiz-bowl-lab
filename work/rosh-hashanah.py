import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "rosh-hashanah",
    "name": "Rosh Hashanah",
    "mono": "RH",
    "category": "Religion",
    "qbCategory": "Religion",
    "kicker": "The Jewish New Year · Begins the Days of Awe with the shofar",
    "dates": "Fall · the 1st and 2nd of Tishrei",
    "briefing": "On Rosh Hashanah, the Jewish New Year, many families dip slices of apple in honey and wish each other a sweet year. In synagogue, worshippers hear the shofar, a trumpet made from a ram’s horn, sounded again and again. The two-day holiday falls on the first and second of Tishrei, in September or October, and begins the Days of Awe, ten days of reflection and repentance that end on Yom Kippur.",
    "answerHtml": "<b><u>Rosh Hashanah</u></b> (or <u>Rosh Hashana</u> or other spellings; accept <u>Jewish New Year</u> or <u>Yom Teruah</u>; prompt on <u>New Year</u> or <u>High Holy Days</u>; do not accept “Yom Kippur”)",
    "accept": [
        "rosh hashanah",
        "rosh hashana",
        "rosh ha shanah",
        "rosh ha shana",
        "rosh hashono",
        "rosh hashonah",
        "rosh hoshanah",
        "jewish new year",
        "yom teruah",
        "yom truah"
    ],
    "prompt": [
        "new year",
        "high holy days",
        "high holy day",
        "high holidays",
        "days of awe",
        "yamim noraim",
        "ten days of repentance"
    ],
    "reject": [
        "yom kippur",
        "yom kipur",
        "day of atonement",
        "passover",
        "pesach",
        "hanukkah",
        "chanukah",
        "hanukah",
        "sukkot",
        "sukkos",
        "purim",
        "shavuot",
        "simchat torah",
        "tu bishvat",
        "shabbat",
        "sabbath",
        "rosh chodesh",
        "tisha bav",
        "lag baomer",
        "fast of gedaliah",
        "tzom gedaliah",
        "selichot",
        "tashlich",
        "shofar",
        "chinese new year",
        "lunar new year",
        "nowruz",
        "diwali"
    ],
    "tests": {
        "right": [
            "Rosh Hashanah",
            "Rosh Hashana",
            "Jewish New Year",
            "Rosh Hashonah",
            "Yom Teruah",
            "Rosh Hashanna"
        ],
        "prompt": [
            "New Year",
            "High Holy Days",
            "Days of Awe"
        ],
        "wrong": [
            "Yom Kippur",
            "Passover",
            "Hanukkah",
            "Sukkot",
            "Purim",
            "Chinese New Year",
            "Rosh Chodesh",
            "Shabbat"
        ]
    },
    "mediaPending": True,
    "media": [],
    "wiki": "https://en.wikipedia.org/wiki/Rosh_Hashanah",
    "qb": {
        "q": "Rosh Hashanah",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "A tractate of the Mishnah named for this holiday lists four different new years, including one for trees, celebrated as Tu BiShvat [“TOO bish-VAHT”], and one on the first day of Nisan [“nee-SAHN”] for counting the reigns of kings.",
            "r": "This holiday marks the new year for counting the years themselves. For 10 points, name this Jewish festival on the first two days of Tishrei [“TISH-ray”]."
        },
        {
            "p": "The Torah never calls this holiday by its usual name. Instead, Leviticus describes a day of rest on the first day of the seventh month, remembered with loud blasts, and the Book of Numbers calls it a “day of blowing.”",
            "r": "Those blasts are sounded on the shofar. For 10 points, name this Jewish holiday that celebrates the start of a new year in the fall."
        },
        {
            "p": "This holiday’s additional, or Musaf [“MOO-sahf”], prayer service has three special sections: Malchuyot [“mahl-khoo-YOHT”], about God’s kingship; Zichronot [“zikh-roh-NOHT”], about remembrance; and Shofarot [“shoh-fah-ROHT”]. Each section includes ten verses from the Hebrew Bible and is followed by blasts of a ram’s horn.",
            "r": "That horn is the shofar. For 10 points, name this Jewish holiday held on the first of Tishrei [“TISH-ray”]."
        },
        {
            "p": "On the second day of this holiday, synagogues read the Binding of Isaac, in which Abraham sacrifices a ram caught by its horns in a thicket instead of his son. On the first day, they read about Isaac’s birth and hear the prayer of Hannah, the mother of the prophet Samuel.",
            "r": "That ram is one reason a ram’s horn, the shofar, is blown on this holiday. For 10 points, name this Jewish holiday that starts the new year."
        },
        {
            "p": "The prayer Unetanneh Tokef [“oo-neh-TAH-neh TOH-kef”] imagines all people passing before God like sheep before a shepherd as each one’s fate is decided: “who shall live and who shall die.” Tradition says that on this holiday, God opens books that record every person’s deeds.",
            "r": "Fates are said to be written on this holiday and sealed on Yom Kippur. For 10 points, name this Jewish holiday."
        },
        {
            "p": "On the afternoon of this holiday, many Jews walk to a river, lake, or ocean and toss bread crumbs into the water in a ceremony called Tashlich [“TAHSH-likh”]. The ceremony takes its name from a verse of Micah [“MY-kuh”] that says God will “cast all their sins into the depths of the sea.”",
            "r": "For 10 points, name this Jewish holiday that begins the Days of Awe leading up to Yom Kippur."
        },
        {
            "p": "Some families eat the head of a fish on this holiday, hoping to be “the head and not the tail” in the coming year, and many eat pomegranates, whose many seeds stand for good deeds. Its challah [“KHAH-luh”] bread is usually baked in a round, spiral shape to show the circle of the year.",
            "r": "Many families also dip apples in honey for a sweet year. For 10 points, name this Jewish holiday that begins the new year."
        },
        {
            "p": "A long blast called tekiah [“teh-KEE-ah”], three broken blasts called shevarim [“sheh-vah-REEM”], and nine short blasts called teruah [“teh-ROO-ah”] are sounded in set patterns on this holiday, ending with an extra-long tekiah gedolah [“teh-KEE-ah geh-doh-LAH”].",
            "r": "Those blasts come from a ram’s horn, the shofar. For 10 points, name this Jewish holiday on the first of Tishrei [“TISH-ray”]."
        },
        {
            "p": "People greet each other on this holiday with “L’shanah tovah tikatevu” [“leh-shah-NAH toh-VAH tee-kah-TAY-voo”], meaning “May you be written down for a good year.” Worshippers also chant Avinu Malkeinu [“ah-VEE-noo mahl-KAY-noo”], a prayer whose name means “Our Father, Our King.”",
            "r": "This holiday begins the Ten Days of Repentance. For 10 points, name this Jewish holiday celebrated with apples and honey."
        },
        {
            "p": "Jewish tradition holds that this holiday marks the anniversary of the creation of Adam and Eve on the sixth day of creation, and one of its prayers calls it “the birthday of the world.” Its other names include the Day of Judgment and the Day of Remembrance.",
            "r": "For 10 points, name this Jewish holiday that starts the year with the sound of the shofar."
        },
        {
            "p": "During most of the month of Elul [“eh-LOOL”] before this holiday, many synagogues sound a ram’s horn after weekday morning prayers. In the days just before it, many communities also gather to recite special prayers for forgiveness called selichot [“slee-KHOHT”].",
            "r": "This holiday falls on the first of Tishrei [“TISH-ray”]. For 10 points, name this Jewish holiday, the first of the High Holy Days."
        },
        {
            "p": "Unlike most Jewish festivals, this holiday lasts two days even in Israel, where its two days are treated as “one long day.” If its first day falls on the Sabbath, the ram’s horn is not sounded that day.",
            "r": "The Fast of Gedaliah [“ged-uh-LYE-uh”] comes the day after it ends. For 10 points, name this two-day Jewish holiday that begins the Days of Awe."
        },
        {
            "p": "This holiday is the only major Jewish festival that falls on the first day of a month, at the new moon. The rabbis connected it to a psalm that tells the people to blow the horn at the new moon, on their feast day.",
            "r": "That horn is the shofar, and that month is Tishrei. For 10 points, name this Jewish holiday that comes about ten days before Yom Kippur."
        },
        {
            "p": "The Hebrew calendar’s year number goes up by one on this holiday; for example, the year 5785 began on it in October 2024. Jewish tradition counts those years from the creation of the world described in Genesis.",
            "r": "This holiday falls on the first two days of Tishrei. For 10 points, name this Jewish holiday celebrated with apples dipped in honey."
        },
        {
            "p": "Many Sephardic [“seh-FAR-dik”] families hold a short seder on this holiday’s first night with symbolic foods such as leeks, beets, and dates. Each food is followed by a blessing that begins “May it be Your will,” often based on a pun on the food’s Hebrew or Aramaic name.",
            "r": "Families everywhere also dip apples in honey for a sweet year. For 10 points, name this Jewish holiday of the new year."
        }
    ],
    "clues": [
        {
            "id": "new-year",
            "tier": "giveaway",
            "t": "The new year festival of Judaism, celebrated in the fall",
            "k": ["new year", "judaism", "fall"],
            "n": 0
        },
        {
            "id": "shofar",
            "tier": "giveaway",
            "t": "The shofar, a trumpet made from a ram’s horn, is sounded many times in synagogue",
            "k": ["shofar", "horn", "trumpet"],
            "n": 0
        },
        {
            "id": "apples-honey",
            "tier": "giveaway",
            "t": "Families dip apples in honey to wish for a sweet new year",
            "k": ["apples", "honey", "sweet"],
            "n": 0
        },
        {
            "id": "tishrei",
            "tier": "giveaway",
            "t": "Falls on the 1st and 2nd of Tishrei, in September or October",
            "k": ["tishrei", "september", "october"],
            "n": 0
        },
        {
            "id": "days-of-awe",
            "tier": "giveaway",
            "t": "Begins the Days of Awe (the Ten Days of Repentance), which end on Yom Kippur",
            "k": ["days of awe", "yom kippur", "ten days of repentance"],
            "n": 0,
            "rabbit": "Yom Kippur"
        },
        {
            "id": "tashlich",
            "tier": "middle",
            "t": "Tashlich: tossing bread crumbs into flowing water to symbolize casting away sins, from a verse of Micah",
            "k": ["tashlich", "bread crumbs", "micah"],
            "n": 0
        },
        {
            "id": "book-of-life",
            "tier": "middle",
            "t": "Tradition: each person’s fate is written in the Book of Life on this day and sealed on Yom Kippur",
            "k": ["book of life", "written", "sealed"],
            "n": 0
        },
        {
            "id": "greeting",
            "tier": "middle",
            "t": "Greeting: “L’shanah tovah” (“for a good year”), or in full, “May you be written down for a good year”",
            "k": ["l’shanah tovah", "good year"],
            "n": 0
        },
        {
            "id": "symbolic-foods",
            "tier": "middle",
            "t": "Round challah (the circle of the year), pomegranates (many good deeds), and fish heads (“the head and not the tail”)",
            "k": ["challah", "pomegranates", "head and not the tail"],
            "n": 0
        },
        {
            "id": "two-days",
            "tier": "middle",
            "t": "Kept for two days, even in Israel; the first of the two High Holy Days",
            "k": ["two days", "high holy days", "israel"],
            "n": 0
        },
        {
            "id": "binding-of-isaac",
            "tier": "middle",
            "t": "Torah readings: Isaac’s birth (day 1) and the Binding of Isaac, where a ram takes Isaac’s place (day 2)",
            "k": ["binding of isaac", "isaac", "ram"],
            "n": 0
        },
        {
            "id": "four-new-years",
            "tier": "power",
            "t": "A Mishnah tractate named for it lists four new years, including Tu BiShvat (trees) and the first of Nisan (kings)",
            "k": ["mishnah", "four new years", "tu bishvat", "nisan"],
            "n": 0
        },
        {
            "id": "seventh-month",
            "tier": "power",
            "t": "Leviticus: a day of rest with loud blasts on the first day of the seventh month; the Book of Numbers calls it a “day of blowing”",
            "k": ["seventh month", "day of blowing", "leviticus"],
            "n": 0
        },
        {
            "id": "musaf",
            "tier": "power",
            "t": "Its Musaf service has three sections: Malchuyot (kingship), Zichronot (remembrance), and Shofarot",
            "k": ["musaf", "malchuyot", "zichronot", "shofarot"],
            "n": 0
        },
        {
            "id": "hannah",
            "tier": "power",
            "t": "The first day’s reading from the prophets is the prayer of Hannah, mother of Samuel",
            "k": ["hannah", "samuel"],
            "n": 0
        },
        {
            "id": "unetanneh-tokef",
            "tier": "power",
            "t": "Unetanneh Tokef: “who shall live and who shall die,” as all people pass before God like sheep",
            "k": ["unetanneh tokef", "who shall live", "sheep"],
            "n": 0
        },
        {
            "id": "blasts",
            "tier": "power",
            "t": "Shofar calls: tekiah (long), shevarim (three broken), teruah (nine short), and tekiah gedolah (extra-long)",
            "k": ["tekiah", "shevarim", "teruah", "gedolah"],
            "n": 0
        },
        {
            "id": "avinu-malkeinu",
            "tier": "power",
            "t": "Worshippers chant Avinu Malkeinu (“Our Father, Our King”)",
            "k": ["avinu malkeinu", "our father"],
            "n": 0
        },
        {
            "id": "creation",
            "tier": "power",
            "t": "Marks the creation of Adam and Eve, “the birthday of the world”; also called the Day of Judgment and the Day of Remembrance",
            "k": ["adam and eve", "birthday of the world", "day of judgment", "day of remembrance"],
            "n": 0
        },
        {
            "id": "elul",
            "tier": "power",
            "t": "Preceded by the month of Elul, with weekday shofar blasts and selichot (prayers for forgiveness)",
            "k": ["elul", "selichot"],
            "n": 0
        },
        {
            "id": "gedaliah",
            "tier": "power",
            "t": "No shofar is sounded if the first day falls on the Sabbath; the Fast of Gedaliah comes the day after",
            "k": ["sabbath", "fast of gedaliah", "gedaliah"],
            "n": 0
        },
        {
            "id": "new-moon",
            "tier": "power",
            "t": "The only major festival on the first of a month (the new moon); linked to a psalm about blowing the horn at the new moon",
            "k": ["new moon", "psalm", "first of a month"],
            "n": 0
        },
        {
            "id": "year-number",
            "tier": "power",
            "t": "The Hebrew year number rises by one (5785 began in October 2024), counting from creation",
            "k": ["5785", "year number", "creation"],
            "n": 0
        },
        {
            "id": "sephardic-seder",
            "tier": "power",
            "t": "Sephardic families hold a seder of symbolic foods (leeks, beets, dates), each with a “May it be Your will” blessing",
            "k": ["sephardic", "symbolic foods", "may it be your will", "leeks"],
            "n": 0
        }
    ],
    "trap": {
        "title": "New Year or Atonement?",
        "body": "Rosh Hashanah and Yom Kippur are the two High Holy Days, about ten days apart in the month of Tishrei, and they share the shofar, the Book of Life, and the Days of Awe that link them. Tradition says each person’s fate is written on Rosh Hashanah and sealed on Yom Kippur, so buzzing on a Book of Life clue alone is risky. The Torah’s own name for this holiday, Yom Teruah (“day of blowing”), is accepted too.",
        "fix": "Apples and honey, Tashlich, round challah, the Binding of Isaac reading, and many shofar blasts mean Rosh Hashanah. The 25-hour fast, Kol Nidre, Ne’ila, the Book of Jonah, and the scapegoat mean Yom Kippur. “New Year” or “High Holy Days” alone only earns a prompt.",
        "line": "Real answer line: <b><u>Rosh Hashanah</u></b> (accept <u>Jewish New Year</u> or <u>Yom Teruah</u>; prompt on <u>High Holy Days</u>; do not accept “Yom Kippur”)"
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
