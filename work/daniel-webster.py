import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def T(p, r):
    return {"p": p, "r": r}


def C(cid, tier, t, k, rabbit=None):
    c = {"id": cid, "tier": tier, "t": t, "k": k, "n": 0}
    if rabbit:
        c["rabbit"] = rabbit
    return c


data = {
    "id": "daniel-webster",
    "name": "Daniel Webster",
    "mono": "DW",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Massachusetts senator and orator · “Liberty and Union, now and forever”",
    "dates": "1782–1852",
    "briefing": "Daniel Webster was the most famous speechmaker of his age, a senator from Massachusetts who could hold a crowded Senate gallery spellbound for hours. In 1830 he ended a famous debate with the words “Liberty and Union, now and forever, one and inseparable!” He won landmark Supreme Court cases, served twice as secretary of state, and even stars in a short story where he out-argues the devil himself.",
    "answerHtml": "Daniel <b><u>Webster</u></b> (do not accept “Noah Webster”)",
    "accept": [
        "daniel webster",
        "webster",
        "dan webster",
        "senator webster"
    ],
    "prompt": [
        "daniel",
        "dan",
        "black dan",
        "godlike daniel",
        "the godlike daniel"
    ],
    "reject": [
        "noah webster",
        "websters dictionary",
        "webster dictionary",
        "merriam webster",
        "john webster",
        "webster hayne debate",
        "webster ashburton treaty",
        "devil and daniel webster",
        "the devil and daniel webster",
        "henry clay",
        "clay",
        "john c calhoun",
        "calhoun",
        "robert hayne",
        "robert y hayne",
        "hayne",
        "daniel boone",
        "jabez stone",
        "dartmouth college",
        "dartmouth college v woodward",
        "great triumvirate",
        "lord ashburton"
    ],
    "tests": {
        "right": [
            "Daniel Webster",
            "Webster",
            "Daniel Webstar",
            "Dan Webster"
        ],
        "prompt": [
            "Daniel",
            "Black Dan"
        ],
        "wrong": [
            "Noah Webster",
            "Henry Clay",
            "John C. Calhoun",
            "Robert Hayne",
            "The Devil and Daniel Webster",
            "Webster-Hayne debate"
        ]
    },
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Daniel_Webster",
    "qb": {
        "q": "Daniel Webster",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        T("A debate over Samuel Foot’s resolution to limit sales of western land grew into this senator’s famous clash with Robert Hayne of South Carolina, while Vice President John C. Calhoun presided over the Senate. Hayne defended a state’s right to nullify federal laws.",
          "This senator replied, “Liberty and Union, now and forever, one and inseparable!” For 10 points, name this Massachusetts orator."),
        T("John Greenleaf Whittier attacked this man in the poem “Ichabod,” whose title means “the glory has departed,” after this man spoke in favor of a stricter Fugitive Slave Act. Many abolitionists in his home state felt betrayed by that speech.",
          "For 10 points, name this Massachusetts senator who gave the Seventh of March speech in 1850."),
        T("This lawyer told the Supreme Court, “It is, sir, as I have said, a small college. And yet there are those who love it!” He won that case when John Marshall ruled that the college’s charter was a contract that New Hampshire could not change.",
          "For 10 points, name this lawyer who won _Dartmouth College v. Woodward_ and later became a senator from Massachusetts."),
        T("This secretary of state and Lord Ashburton signed an 1842 treaty that settled the border between Maine and New Brunswick and set up joint naval patrols against the African slave trade. That treaty ended a dispute that had led to the bloodless “Aroostook War.”",
          "For 10 points, name this Massachusetts statesman, the senator who said “Liberty and Union, now and forever.”"),
        T("In the election of 1836, this man was one of several Whig candidates for president, but he carried only Massachusetts. With Henry Clay, he had helped found the Whig Party to oppose Andrew Jackson.",
          "For 10 points, name this senator who formed the “Great Triumvirate” with Clay and John C. Calhoun."),
        T("On June 17, 1825, the 50th anniversary of a famous battle, this man gave the main speech at the laying of the Bunker Hill Monument’s cornerstone, with the Marquis de Lafayette looking on. He spoke again when the finished monument was dedicated in 1843.",
          "He later served as secretary of state under three presidents. For 10 points, name this Massachusetts senator and orator."),
        T("This lawyer argued for the national bank in _McCulloch v. Maryland_ and for a steamboat operator in _Gibbons v. Ogden_, two cases won by his side before John Marshall’s Supreme Court. He also won a case protecting the charter of his old college.",
          "For 10 points, name this lawyer and Massachusetts senator who debated Robert Hayne in 1830."),
        T("In a short story by Stephen Vincent Benét [“beh-NAY”], this man defends the New Hampshire farmer Jabez Stone, who sold his soul to Mr. Scratch. This man wins the case before a jury of villains from American history, with Judge John Hathorne of the Salem witch trials presiding.",
          "For 10 points, name this real-life senator from Massachusetts, famous for his Seventh of March speech."),
        T("John F. Kennedy’s book _Profiles in Courage_ praises this senator for risking his career with a speech supporting the Compromise of 1850. In 1957, a Senate committee led by Kennedy named this man one of the five greatest senators in history.",
          "For 10 points, name this Massachusetts senator, part of the “Great Triumvirate” with Henry Clay and John C. Calhoun."),
        T("As a young Federalist congressman from New Hampshire, this man opposed the War of 1812 and gave a speech in 1814 against a plan to draft soldiers. He later moved to Boston and represented Massachusetts in both houses of Congress.",
          "For 10 points, name this orator who said “Liberty and Union, now and forever, one and inseparable!”"),
        T("This man was born in 1782 in Salisbury, New Hampshire, and graduated from Dartmouth College in 1801. A statue of this man represents New Hampshire in the U.S. Capitol’s National Statuary Hall collection.",
          "For 10 points, name this man who later represented Massachusetts in the Senate and served as secretary of state."),
        T("This man died in 1852 at his farm in Marshfield, Massachusetts, a few months after his fellow Whig Henry Clay. Two years earlier, Millard Fillmore had made him secretary of state for the second time.",
          "For 10 points, name this Whig orator who debated Robert Hayne of South Carolina in 1830."),
        T("George P. A. Healy’s enormous painting in Boston’s Faneuil [“FAN-yul”] Hall shows this senator standing to speak in a packed Senate chamber in January 1830. The speech it shows was a reply to a senator from South Carolina who defended nullification.",
          "In that speech, he said, “Liberty and Union, now and forever, one and inseparable!” For 10 points, name this Massachusetts senator."),
        T("William Henry Harrison chose this man as secretary of state in 1841, and this man was the only cabinet member to stay when the rest of the cabinet quit after John Tyler vetoed bills for a national bank.",
          "For 10 points, name this Massachusetts Whig, a member of the “Great Triumvirate” with Henry Clay and John C. Calhoun."),
        T("This senator began one speech, “I wish to speak today, not as a Massachusetts man, nor as a Northern man, but as an American.” In that speech, he angered many abolitionists by supporting a tougher law for returning people who had escaped slavery.",
          "For 10 points, name this senator who gave the Seventh of March speech in support of the Compromise of 1850.")
    ],
    "clues": [
        C("liberty-union", "giveaway",
          "Ended his “Second Reply to Hayne” (1830) with “Liberty and Union, now and forever, one and inseparable!”",
          ["liberty and union", "one and inseparable", "second reply"]),
        C("massachusetts-orator", "giveaway",
          "The most famous orator of his age; represented Massachusetts in the House and the Senate",
          ["orator", "massachusetts", "senate"]),
        C("triumvirate", "giveaway",
          "Formed the “Great Triumvirate” of senators with Henry Clay and John C. Calhoun",
          ["great triumvirate", "triumvirate", "henry clay", "calhoun"], "Henry Clay"),
        C("seventh-of-march", "giveaway",
          "Seventh of March speech (1850): backed the Compromise of 1850, including a tougher Fugitive Slave Act",
          ["seventh of march", "compromise of 1850", "fugitive slave act"], "Compromise of 1850"),
        C("hayne", "middle",
          "Debated Robert Hayne of South Carolina in 1830; Hayne defended states’ rights and nullification",
          ["robert hayne", "hayne", "nullification", "states’ rights"]),
        C("dartmouth", "middle",
          "Won _Dartmouth College v. Woodward_ (1819): “It is, sir, as I have said, a small college. And yet there are those who love it!”",
          ["dartmouth", "small college", "woodward"]),
        C("ashburton", "middle",
          "As secretary of state, signed an 1842 treaty with Lord Ashburton settling the Maine–New Brunswick border",
          ["ashburton", "maine", "1842"]),
        C("secretary-of-state", "middle",
          "Secretary of state under William Henry Harrison and John Tyler (1841–1843) and again under Millard Fillmore (1850–1852)",
          ["secretary of state", "tyler", "fillmore"]),
        C("benet", "middle",
          "Defends farmer Jabez Stone against the devil, Mr. Scratch, in a short story by Stephen Vincent Benét",
          ["jabez stone", "mr. scratch", "benét", "devil"]),
        C("whig-founder", "middle",
          "Helped Henry Clay found the Whig Party to oppose Andrew Jackson",
          ["whig party", "whig", "andrew jackson"]),
        C("tyler-cabinet", "middle",
          "The only cabinet member who stayed when John Tyler’s cabinet resigned over his bank vetoes in 1841",
          ["cabinet", "resigned", "1841"]),
        C("ichabod", "power",
          "John Greenleaf Whittier attacked him in the poem “Ichabod” (1850) after the Seventh of March speech",
          ["ichabod", "whittier"]),
        C("mcculloch-gibbons", "power",
          "Argued and won _McCulloch v. Maryland_ (1819) for the national bank and _Gibbons v. Ogden_ (1824) for Gibbons",
          ["mcculloch", "gibbons", "ogden"]),
        C("bunker-hill", "power",
          "Gave the speeches at the Bunker Hill Monument’s cornerstone laying (1825) and its dedication (1843)",
          ["bunker hill", "1825", "1843"]),
        C("election-1836", "power",
          "Ran as one of several Whig presidential candidates in 1836 but carried only Massachusetts",
          ["1836", "only massachusetts", "candidates"]),
        C("profiles", "power",
          "Praised in John F. Kennedy’s _Profiles in Courage_; a 1957 Senate committee named him one of the five greatest senators",
          ["profiles in courage", "kennedy", "1957", "five greatest"]),
        C("foot-resolution", "power",
          "The debate with Hayne began over Samuel Foot’s resolution on western land sales; Vice President Calhoun presided",
          ["samuel foot", "foot", "western land"]),
        C("war-of-1812", "power",
          "As a New Hampshire Federalist congressman, opposed the War of 1812 and a plan to draft soldiers (1814)",
          ["federalist", "war of 1812", "draft"]),
        C("birth", "power",
          "Born in Salisbury, New Hampshire (1782); graduated from Dartmouth College (1801)",
          ["salisbury", "1782", "1801"]),
        C("marshfield", "power",
          "Died at his farm in Marshfield, Massachusetts, in 1852, a few months after Henry Clay",
          ["marshfield", "1852"]),
        C("aroostook", "power",
          "His 1842 treaty ended the dispute behind the bloodless “Aroostook War” and set up joint patrols against the slave trade",
          ["aroostook", "slave trade", "patrols"]),
        C("healy", "power",
          "George P. A. Healy’s huge painting of his reply to Hayne hangs in Boston’s Faneuil Hall",
          ["healy", "faneuil hall", "painting"]),
        C("statuary", "power",
          "His statue represents New Hampshire in the National Statuary Hall collection",
          ["statuary hall", "new hampshire", "statue"])
    ],
    "trap": {
        "title": "Daniel, not Noah",
        "body": "Two famous Websters lived at the same time. Noah Webster wrote the first great American dictionary (1828) and the “Blue-Backed Speller,” while Daniel Webster was the Massachusetts senator and orator, so naming the wrong one loses the tossup. Some questions also want something named for him instead of the man himself: the Webster–Hayne debate, the Webster–Ashburton Treaty, or Stephen Vincent Benét’s story “The Devil and Daniel Webster.”",
        "fix": "Dictionaries and spelling books mean Noah; speeches, the Senate, and Supreme Court cases mean Daniel. If you know it is a Webster, say the full name, “Daniel Webster.” Listen for “this debate,” “this treaty,” or “this story” before you buzz with the person.",
        "line": "Real answer line: Daniel <b><u>Webster</u></b> (do not accept “Noah Webster”)"
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
