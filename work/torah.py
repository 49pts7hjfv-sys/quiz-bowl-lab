import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

LINE = "<b><u>Torah</u></b> (or <b><u>Pentateuch</u></b> or <b><u>Five Books of Moses</u></b>; accept <u>Chumash</u> or <u>Tawrat</u>; prompt on <u>Tanakh</u>, Hebrew <u>Bible</u>, or <u>Old Testament</u>; do not accept “Talmud”)"

data = {
    "id": "torah",
    "name": "Torah",
    "mono": "TOR",
    "category": "Religion",
    "qbCategory": "Religion",
    "kicker": "Judaism’s holiest text · The five books from Genesis to Deuteronomy",
    "dates": "Traditionally credited to Moses",
    "briefing": "The Torah is Judaism’s holiest text: the five books from Genesis to Deuteronomy, which Jewish tradition says God gave to Moses at Mount Sinai. In synagogues it is handwritten on a parchment scroll by a trained scribe, and readers follow its words with a pointer called a yad so their fingers never touch the parchment. Each fall, on Simchat Torah, communities dance with the scrolls as they finish the yearly reading and start again from “In the beginning.”",
    "answerHtml": LINE,
    "accept": [
        "torah",
        "the torah",
        "pentateuch",
        "the pentateuch",
        "five books of moses",
        "the five books of moses",
        "books of moses",
        "chumash",
        "humash",
        "sefer torah",
        "torah scroll",
        "torah scrolls",
        "written torah",
        "tawrat",
        "taurat"
    ],
    "prompt": [
        "tanakh",
        "tanach",
        "hebrew bible",
        "the hebrew bible",
        "old testament",
        "the old testament",
        "bible",
        "the bible",
        "hebrew scriptures",
        "law",
        "the law",
        "law of moses",
        "the law of moses",
        "mosaic law"
    ],
    "reject": [
        "talmud",
        "babylonian talmud",
        "jerusalem talmud",
        "mishnah",
        "mishna",
        "gemara",
        "midrash",
        "oral torah",
        "oral law",
        "mishneh torah",
        "simchat torah",
        "torah portion",
        "weekly torah portion",
        "parashah",
        "parsha",
        "haftarah",
        "shulchan aruch",
        "zohar",
        "kabbalah",
        "neviim",
        "ketuvim",
        "prophets",
        "writings",
        "genesis",
        "book of genesis",
        "first book of moses",
        "exodus",
        "leviticus",
        "numbers",
        "deuteronomy",
        "ten commandments",
        "decalogue",
        "tablets",
        "dead sea scrolls",
        "septuagint",
        "new testament",
        "gospels",
        "quran",
        "koran",
        "judaism",
        "jewish",
        "jews"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Torah",
    "qb": {
        "q": "Torah",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "One opinion in the Talmud says that Joshua wrote the last eight verses of this text, which describe how Moses died after seeing the Promised Land from Mount Nebo [“NEE-boh”]. Jewish tradition holds that Moses wrote down the rest of it as God gave it to him.",
            "r": "It begins with the Book of Genesis and ends with Deuteronomy. For 10 points, name this collection of the first five books of the Hebrew Bible."
        },
        {
            "p": "A scribe called a sofer [“SOH-fer”] copies this text by hand with a quill on parchment, and a single mistake that is not fixed makes a scroll unfit to use. Each finished scroll is wound on two wooden rollers called “trees of life.”",
            "r": "It is kept in the synagogue’s Ark and read aloud on Saturday mornings. For 10 points, name this scripture that begins with Genesis."
        },
        {
            "p": "On a fall holiday whose Hebrew name means “Rejoicing of” this text, people dance in seven circles around the synagogue while carrying it. On that holiday, readers finish its last passage and immediately begin again at its first words, “In the beginning.”",
            "r": "For 10 points, name this Jewish scripture, the first five books of the Hebrew Bible, which is read aloud in sections each week."
        },
        {
            "p": "According to the Letter of Aristeas [“uh-RISS-tee-us”], seventy-two Jewish scholars translated this text into Greek in Alexandria for King Ptolemy [“TOL-uh-mee”] II, beginning the translation known as the Septuagint. Another name for this text comes from the Greek word for “five.”",
            "r": "In the Tanakh, it comes before the Prophets and the Writings. For 10 points, name this scripture that runs from Genesis to Deuteronomy."
        },
        {
            "p": "A rabbi in the Talmud counted 613 commandments in this text: 248 positive commands, matching the number of parts of the human body, and 365 prohibitions, one for each day of the solar year. Maimonides [“my-MON-ih-deez”] listed every one of them in his _Book of the Commandments_.",
            "r": "Jewish tradition holds that God gave this text to Moses at Mount Sinai. For 10 points, name this scripture made up of Genesis, Exodus, Leviticus, Numbers, and Deuteronomy."
        },
        {
            "p": "In the Book of Nehemiah, the scribe Ezra stands on a wooden platform and reads this text aloud to the people of Jerusalem from early morning until midday, while Levites explain its meaning. The Sadducees accepted only this written law and rejected the oral traditions of the Pharisees.",
            "r": "For 10 points, name this Jewish scripture, which tradition says was given to Moses at Mount Sinai."
        },
        {
            "p": "The Samaritans keep their own version of this text, written in an old form of the Hebrew alphabet, and they accept no other books as holy scripture. In Islam, it is honored as a holy book that God revealed to the prophet Musa.",
            "r": "Its first book is Genesis. For 10 points, name this scripture, the first part of the Hebrew Bible."
        },
        {
            "p": "After a reading in the synagogue, one person lifts this open scroll high to show the congregation, and another rolls it closed and, in many synagogues, dresses it in a cloth cover and silver ornaments. It is kept in a cabinet called the Ark on the wall that faces Jerusalem.",
            "r": "Readers follow its text with a pointer called a yad, meaning “hand.” For 10 points, name this scroll of the first five books of the Hebrew Bible."
        },
        {
            "p": "A famous passage of the Mishnah says that Moses received this text at Sinai and handed it down to Joshua, Joshua to the elders, the elders to the prophets, and the prophets to the Men of the Great Assembly.",
            "r": "Rabbis teach that an oral law explaining it was later written down in the Mishnah. For 10 points, name this written scripture of Judaism, whose five books begin with Genesis."
        },
        {
            "p": "Julius Wellhausen [“VEL-how-zen”] popularized the theory that this text was woven together from four older sources, called J, E, D, and P. The source called D is named for its last book, which is mostly made up of Moses’s farewell speeches to the Israelites.",
            "r": "For 10 points, name this collection of five books, beginning with Genesis, that is the holiest text of Judaism."
        },
        {
            "p": "The books of this text have Hebrew names taken from words near their beginnings, such as Shemot [“sheh-MOHT”], meaning “names,” and Bamidbar [“bah-mid-BAR”], meaning “in the wilderness.” Its third book, Leviticus, is full of laws about priests, offerings, and holiness.",
            "r": "For 10 points, name this scripture whose five books run from Genesis to Deuteronomy."
        },
        {
            "p": "This text is divided into fifty-four weekly portions, and short sections of it are also read in synagogues on Monday and Thursday mornings. A bar mitzvah or bat mitzvah often chants a passage from it for the first time in front of the congregation.",
            "r": "Most synagogues read the whole thing once a year. For 10 points, name this Jewish scripture whose first book is Genesis."
        },
        {
            "p": "Shavuot [“shah-voo-OHT”], which comes seven weeks after Passover, celebrates the day that Jewish tradition says God gave this text at Mount Sinai, and many people stay up all night on Shavuot to study it.",
            "r": "That text includes the Ten Commandments, which appear in both Exodus and Deuteronomy. For 10 points, name this scripture, the first five books of the Hebrew Bible."
        },
        {
            "p": "Passages from this text are written on tiny parchment scrolls placed inside a mezuzah [“meh-ZOO-zuh”] on a doorpost and inside the small leather boxes called tefillin [“teh-FIL-in”]. One of those passages, the Shema [“shuh-MAH”], comes from its fifth book, Deuteronomy.",
            "r": "For 10 points, name this Jewish scripture, which tradition says Moses received on Mount Sinai."
        },
        {
            "p": "As traditionally counted, the last of the 613 commandments in this text tells every Jew to write a copy of it, so many people help pay for a new scroll and take part in filling in its final letters. Worn-out scrolls of this text are not thrown away but are buried, often in a Jewish cemetery.",
            "r": "For 10 points, name this scroll of the first five books of the Hebrew Bible, kept in a synagogue’s Ark."
        }
    ],
    "clues": [
        {
            "id": "five-books",
            "tier": "giveaway",
            "t": "The first five books of the Hebrew Bible: Genesis, Exodus, Leviticus, Numbers, and Deuteronomy",
            "k": ["first five books", "genesis", "deuteronomy", "leviticus"],
            "n": 0,
            "rabbit": "Book of Genesis"
        },
        {
            "id": "sinai",
            "tier": "giveaway",
            "t": "Jewish tradition holds that God gave it to Moses on Mount Sinai",
            "k": ["sinai", "moses"],
            "n": 0,
            "rabbit": "Moses"
        },
        {
            "id": "holiest",
            "tier": "giveaway",
            "t": "Judaism’s holiest text and the first part of the Tanakh, the Hebrew Bible",
            "k": ["tanakh", "holiest", "hebrew bible"],
            "n": 0,
            "rabbit": "Judaism"
        },
        {
            "id": "scroll",
            "tier": "giveaway",
            "t": "Handwritten on a parchment scroll and kept in the synagogue’s Ark",
            "k": ["scroll", "parchment", "ark"],
            "n": 0
        },
        {
            "id": "yad",
            "tier": "giveaway",
            "t": "Read aloud with a pointer called a yad (“hand”), so readers don’t touch the parchment",
            "k": ["yad", "pointer", "hand"],
            "n": 0
        },
        {
            "id": "sofer",
            "tier": "middle",
            "t": "Copied by hand with a quill by a trained scribe called a sofer; one uncorrected mistake makes a scroll unfit",
            "k": ["sofer", "scribe", "quill"],
            "n": 0
        },
        {
            "id": "weekly-portions",
            "tier": "middle",
            "t": "Divided into 54 weekly portions, so most synagogues read all of it once a year",
            "k": ["weekly portions", "54", "once a year"],
            "n": 0
        },
        {
            "id": "rejoicing",
            "tier": "middle",
            "t": "A fall holiday whose name means “Rejoicing of” it celebrates finishing and restarting the yearly reading, with dancing",
            "k": ["rejoicing", "dancing", "restarting"],
            "n": 0
        },
        {
            "id": "mitzvot",
            "tier": "middle",
            "t": "Tradition counts 613 commandments (mitzvot) in it",
            "k": ["613", "mitzvot", "commandments"],
            "n": 0
        },
        {
            "id": "oral-law",
            "tier": "middle",
            "t": "Rabbis teach that Moses also received an oral law explaining it, later written down in the Mishnah and discussed in the Talmud",
            "k": ["oral law", "mishnah", "talmud"],
            "n": 0
        },
        {
            "id": "shema",
            "tier": "middle",
            "t": "Its passages, including the Shema from Deuteronomy, go inside mezuzahs and tefillin",
            "k": ["shema", "mezuzah", "tefillin"],
            "n": 0
        },
        {
            "id": "shavuot",
            "tier": "middle",
            "t": "Shavuot celebrates the day tradition says it was given at Sinai; many people study all night",
            "k": ["shavuot", "all night"],
            "n": 0
        },
        {
            "id": "hebrew-names",
            "tier": "middle",
            "t": "Its books’ Hebrew names come from early words, such as Bereshit, Shemot (“names”), and Bamidbar (“in the wilderness”)",
            "k": ["bereshit", "shemot", "bamidbar"],
            "n": 0
        },
        {
            "id": "bar-mitzvah",
            "tier": "middle",
            "t": "At a bar or bat mitzvah, a young person often chants a passage from it for the first time",
            "k": ["bar mitzvah", "bat mitzvah", "chants"],
            "n": 0
        },
        {
            "id": "joshua-verses",
            "tier": "power",
            "t": "One Talmud opinion says Joshua wrote its last eight verses, about Moses’s death after he saw the Promised Land from Mount Nebo",
            "k": ["joshua", "eight verses", "nebo"],
            "n": 0
        },
        {
            "id": "trees-of-life",
            "tier": "power",
            "t": "Its scroll is wound on two wooden rollers called “trees of life”",
            "k": ["trees of life", "rollers"],
            "n": 0
        },
        {
            "id": "septuagint",
            "tier": "power",
            "t": "Letter of Aristeas: 72 scholars translated it into Greek in Alexandria for Ptolemy II, starting the Septuagint",
            "k": ["septuagint", "aristeas", "ptolemy", "alexandria"],
            "n": 0
        },
        {
            "id": "248-365",
            "tier": "power",
            "t": "A Talmud rabbi split the 613 into 248 positive commands (parts of the body) and 365 prohibitions (days of the year); Maimonides listed them all",
            "k": ["maimonides", "248", "365", "prohibitions"],
            "n": 0
        },
        {
            "id": "ezra",
            "tier": "power",
            "t": "Ezra the scribe read it aloud in Jerusalem from early morning until midday, as told in the Book of Nehemiah",
            "k": ["ezra", "nehemiah", "midday"],
            "n": 0
        },
        {
            "id": "sadducees",
            "tier": "power",
            "t": "The Sadducees accepted only this written law and rejected the Pharisees’ oral traditions",
            "k": ["sadducees", "pharisees", "written law"],
            "n": 0
        },
        {
            "id": "samaritans",
            "tier": "power",
            "t": "The Samaritans keep their own version and accept no other scripture; Islam honors it as revealed to the prophet Musa",
            "k": ["samaritans", "musa", "islam"],
            "n": 0
        },
        {
            "id": "hagbah",
            "tier": "power",
            "t": "After a reading, one person lifts the open scroll high (hagbah) and another rolls it and dresses it",
            "k": ["hagbah", "lifts", "dresses"],
            "n": 0
        },
        {
            "id": "pirkei-avot",
            "tier": "power",
            "t": "Pirkei Avot: Moses received it at Sinai and handed it to Joshua, the elders, the prophets, and the Men of the Great Assembly",
            "k": ["pirkei avot", "great assembly", "elders"],
            "n": 0
        },
        {
            "id": "wellhausen",
            "tier": "power",
            "t": "Documentary hypothesis: Julius Wellhausen popularized the idea of four sources, J, E, D, and P",
            "k": ["wellhausen", "documentary hypothesis", "four sources"],
            "n": 0
        },
        {
            "id": "last-commandment",
            "tier": "power",
            "t": "The last of its 613 commandments, as traditionally counted, tells every Jew to write a copy; worn-out scrolls are buried",
            "k": ["write a copy", "buried", "last"],
            "n": 0
        },
        {
            "id": "monday-thursday",
            "tier": "power",
            "t": "Short sections are also read in synagogues on Monday and Thursday mornings",
            "k": ["monday", "thursday"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Text, Tanakh, or Talmud?",
        "body": "Several Jewish texts sound alike. The Torah is the five books from Genesis to Deuteronomy, written on the scroll kept in every synagogue. The Tanakh is the whole Hebrew Bible, of which the Torah is only the first part, so naming it earns just a prompt. The Talmud is a later collection of rabbinic discussion built on the Mishnah, and naming a single book, such as Genesis, is wrong too.",
        "fix": "A scroll, a sofer, a yad, Simchat Torah, the 613 commandments, or “Genesis through Deuteronomy” mean the Torah (“Pentateuch” and “Five Books of Moses” also work). Rabbis debating, the Gemara, or “six orders” mean the Talmud or Mishnah. If the clues add the Prophets and the Writings, the answer is the Tanakh.",
        "line": "Real answer line: " + LINE
    },
    "tests": {
        "right": [
            "Torah",
            "Pentateuch",
            "Five Books of Moses",
            "the Torah",
            "Chumash",
            "Tora",
            "Sefer Torah",
            "Pentatuch"
        ],
        "prompt": [
            "Tanakh",
            "Hebrew Bible",
            "Old Testament"
        ],
        "wrong": [
            "Talmud",
            "Genesis",
            "Mishnah",
            "Moses",
            "Judaism",
            "Ten Commandments",
            "Simchat Torah",
            "Oral Torah"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
