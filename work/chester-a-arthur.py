import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "chester-a-arthur",
    "name": "Chester A. Arthur",
    "mono": "CAA",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "21st U.S. President · Signed the Pendleton Civil Service Act",
    "dates": "1829–1886",
    "briefing": "Chester Arthur spent years as a loyal member of Roscoe Conkling’s New York political machine, handing out jobs at the busy Port of New York. Then a disappointed office-seeker shot President James Garfield in 1881, and Arthur suddenly became the 21st president. To nearly everyone’s surprise, he backed reform and signed the Pendleton Act, which began filling some federal jobs through exams instead of political favors.",
    "answerHtml": "Chester A. <b><u>Arthur</u></b> (or Chester Alan <b><u>Arthur</u></b>; do not accept “James Garfield”)",
    "accept": [
        "chester a arthur",
        "chester alan arthur",
        "chester arthur",
        "arthur",
        "president arthur",
        "president chester arthur"
    ],
    "prompt": [
        "chester"
    ],
    "reject": [
        "james garfield",
        "garfield",
        "james a garfield",
        "rutherford b hayes",
        "rutherford hayes",
        "hayes",
        "grover cleveland",
        "cleveland",
        "benjamin harrison",
        "roscoe conkling",
        "conkling",
        "charles guiteau",
        "guiteau",
        "james g blaine",
        "blaine",
        "ulysses s grant",
        "george pendleton",
        "pendleton act",
        "chinese exclusion act",
        "king arthur",
        "arthur miller",
        "arthur schopenhauer",
        "douglas macarthur",
        "macarthur",
        "arthur macarthur",
        "chester nimitz",
        "nimitz"
    ],
    "mediaPending": True,
    "media": [],
    "wiki": "https://en.wikipedia.org/wiki/Chester_A._Arthur",
    "qb": {
        "q": "Chester Arthur",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "After this man became president, a New York woman named Julia Sand wrote him a series of letters urging him to rise above machine politics, and he later paid her a surprise visit. Many reformers had expected the worst from this longtime ally of Roscoe Conkling.",
            "r": "For 10 points, name this president who took office after the assassination of James Garfield."
        },
        {
            "p": "During the 1880 campaign, opponents claimed that this man had secretly been born in Canada, which would have made him ineligible to be president. This man was actually born in Fairfield, Vermont, the son of a Baptist preacher from Ireland.",
            "r": "For 10 points, name this vice president who became the 21st president in 1881."
        },
        {
            "p": "As a young lawyer, this man helped win a lawsuit for Elizabeth Jennings, a Black schoolteacher who had been forced off a New York City streetcar because of her race. During the Civil War, he served as quartermaster general of New York’s militia, supplying its troops.",
            "r": "For 10 points, name this New York Republican who became president after James Garfield was killed."
        },
        {
            "p": "Ulysses S. Grant named this man Collector of the Port of New York, a post that let him hand out hundreds of jobs at the busy Custom House. Rutherford B. Hayes removed him from that job in 1878 as part of a push for civil service reform.",
            "r": "This man later became vice president under James Garfield. For 10 points, name this Stalwart Republican who became the 21st president."
        },
        {
            "p": "At the 1880 Republican convention, delegates chose this man as the running mate of a dark-horse nominee who won on the 36th ballot, hoping to please Stalwarts who had wanted Ulysses S. Grant to return. Roscoe Conkling urged this man to turn down the nomination, but he accepted.",
            "r": "That nominee was James Garfield. For 10 points, name this man who became president in 1881 after Garfield’s death."
        },
        {
            "p": "After shooting a president at a Washington train station, Charles Guiteau [“gih-TOH”] shouted that he was “a Stalwart of the Stalwarts” and that this man would now be president. This man was sworn in at his New York City home in the middle of the night after that president died.",
            "r": "That president was James Garfield. For 10 points, name this vice president who succeeded Garfield and later signed the Pendleton Act."
        },
        {
            "p": "This president signed a law that created the Civil Service Commission and made it illegal to fire certain federal workers for refusing to give money to a political party. Public anger over his predecessor’s assassination helped that law pass in 1883.",
            "r": "That law was the Pendleton Act. For 10 points, name this 21st president, who took office after James Garfield was killed."
        },
        {
            "p": "This president vetoed a bill that would have banned Chinese laborers from immigrating for twenty years, saying it broke a treaty with China. He then signed a version that banned them for ten years, the first major U.S. law to keep out immigrants because of their nationality.",
            "r": "That 1882 law was the Chinese Exclusion Act. For 10 points, name this president who succeeded James Garfield."
        },
        {
            "p": "This president vetoed the Rivers and Harbors Act of 1882 as wasteful spending, but Congress overrode his veto. He also signed the Tariff of 1883, which critics nicknamed the “Mongrel Tariff.”",
            "r": "For 10 points, name this Republican president who served from 1881 to 1885, after the death of James Garfield."
        },
        {
            "p": "This president is called the “Father of the Steel Navy” because Congress approved the first steel warships, the cruisers _Atlanta_, _Boston_, and _Chicago_ and the dispatch boat _Dolphin_, during his term. His secretary of the navy was William Chandler.",
            "r": "For 10 points, name this president who took office after James Garfield died in 1881."
        },
        {
            "p": "This president refused to move into the White House until it was redecorated, and he sold off about two dozen wagonloads of old furniture. Louis Comfort Tiffany then added a huge stained-glass screen to the mansion’s entrance hall.",
            "r": "For 10 points, name this stylish president, nicknamed the “Gentleman Boss,” who succeeded James Garfield."
        },
        {
            "p": "Soon after becoming president, this man learned he had Bright’s disease, a serious kidney illness, but he kept it secret. He made only a halfhearted try for his party’s nomination in 1884, which went to James G. Blaine, and he died two years later.",
            "r": "Earlier, he had signed the Pendleton Act. For 10 points, name this 21st president, who succeeded James Garfield."
        },
        {
            "p": "During this man’s presidency, the International Meridian Conference in Washington chose Greenwich, England, as the starting point for measuring longitude. Near the end of his term, he dedicated the newly finished Washington Monument.",
            "r": "For 10 points, name this president who succeeded James Garfield in 1881 and later signed the Pendleton Act."
        },
        {
            "p": "This president’s Justice Department prosecuted the Star Route scandal, in which officials and contractors cheated the government on mail-delivery routes in the West. In 1883, he joined Governor Grover Cleveland at the opening of the Brooklyn Bridge.",
            "r": "For 10 points, name this New Yorker, the 21st president of the United States."
        },
        {
            "p": "Because his wife, Ellen, had died before he took office, this president’s sister Mary McElroy served as White House hostess. He served his entire term without a vice president, and shortly before his death he had most of his personal papers burned.",
            "r": "For 10 points, name this Stalwart Republican who became president after James Garfield was assassinated."
        }
    ],
    "clues": [
        {
            "id": "21st-president",
            "tier": "giveaway",
            "t": "21st President of the United States (1881–1885), a Republican from New York",
            "k": ["21st president", "21st", "republican", "new york"],
            "n": 0
        },
        {
            "id": "garfield",
            "tier": "giveaway",
            "t": "Vice president who took over when James Garfield died after being shot in 1881",
            "k": ["james garfield", "garfield", "1881"],
            "n": 0,
            "rabbit": "James Garfield"
        },
        {
            "id": "pendleton",
            "tier": "giveaway",
            "t": "Signed the Pendleton Civil Service Reform Act (1883), which required exams for some federal jobs",
            "k": ["pendleton", "civil service", "1883", "exams"],
            "n": 0
        },
        {
            "id": "chinese-exclusion",
            "tier": "giveaway",
            "t": "Signed the Chinese Exclusion Act (1882), which banned Chinese laborers from immigrating for ten years",
            "k": ["chinese exclusion act", "chinese exclusion", "1882", "ten years"],
            "n": 0
        },
        {
            "id": "collector",
            "tier": "middle",
            "t": "Ulysses S. Grant made him Collector of the Port of New York (1871), a job full of patronage at the Custom House",
            "k": ["collector", "port of new york", "custom house", "patronage"],
            "n": 0
        },
        {
            "id": "hayes-removed",
            "tier": "middle",
            "t": "Rutherford B. Hayes removed him as Collector in 1878, in a push for civil service reform",
            "k": ["rutherford b. hayes", "hayes", "1878", "removed"],
            "n": 0,
            "rabbit": "Rutherford B. Hayes"
        },
        {
            "id": "stalwarts",
            "tier": "middle",
            "t": "A Stalwart Republican and ally of New York boss Roscoe Conkling, who opposed civil service reform",
            "k": ["stalwart", "stalwarts", "roscoe conkling", "conkling"],
            "n": 0
        },
        {
            "id": "guiteau",
            "tier": "middle",
            "t": "Charles Guiteau, a disappointed office-seeker, shot Garfield and shouted, “I am a Stalwart of the Stalwarts!”",
            "k": ["charles guiteau", "guiteau", "office-seeker", "stalwart of the stalwarts"],
            "n": 0
        },
        {
            "id": "convention-1880",
            "tier": "middle",
            "t": "Picked as Garfield’s running mate in 1880 to please the Stalwarts, after Garfield won the nomination on the 36th ballot",
            "k": ["running mate", "36th ballot", "1880"],
            "n": 0
        },
        {
            "id": "sworn-in",
            "tier": "middle",
            "t": "Sworn in at his New York City home in the middle of the night after Garfield died (September 1881)",
            "k": ["sworn in", "new york city", "middle of the night", "september"],
            "n": 0
        },
        {
            "id": "steel-navy",
            "tier": "middle",
            "t": "“Father of the Steel Navy”: the first steel warships (_Atlanta_, _Boston_, _Chicago_, and _Dolphin_) were approved in 1883",
            "k": ["steel navy", "steel", "warships"],
            "n": 0
        },
        {
            "id": "tiffany",
            "tier": "middle",
            "t": "Had Louis Comfort Tiffany redecorate the White House, adding a stained-glass screen; sold about 24 wagonloads of old furniture",
            "k": ["louis comfort tiffany", "tiffany", "stained-glass", "wagonloads"],
            "n": 0
        },
        {
            "id": "gentleman-boss",
            "tier": "middle",
            "t": "Nicknamed the “Gentleman Boss” for his fancy clothes and manners; wore bushy side-whiskers",
            "k": ["gentleman boss", "fancy clothes", "side-whiskers"],
            "n": 0
        },
        {
            "id": "brights-disease",
            "tier": "middle",
            "t": "Secretly had Bright’s disease, a kidney illness; barely tried for the 1884 nomination (won by James G. Blaine) and died in 1886",
            "k": ["bright’s disease", "brights disease", "kidney", "1886"],
            "n": 0
        },
        {
            "id": "vermont-canada",
            "tier": "power",
            "t": "Born in Fairfield, Vermont (1829), son of an Irish-born Baptist preacher; opponents falsely claimed he was born in Canada",
            "k": ["fairfield", "vermont", "canada", "baptist"],
            "n": 0
        },
        {
            "id": "jennings",
            "tier": "power",
            "t": "As a young lawyer, helped win the case of Elizabeth Jennings, a Black teacher forced off a New York City streetcar",
            "k": ["elizabeth jennings", "jennings", "streetcar"],
            "n": 0
        },
        {
            "id": "quartermaster",
            "tier": "power",
            "t": "Quartermaster general of New York’s militia during the Civil War",
            "k": ["quartermaster", "militia", "civil war"],
            "n": 0
        },
        {
            "id": "julia-sand",
            "tier": "power",
            "t": "Julia Sand wrote him a series of letters urging him to rise above machine politics; he later visited her",
            "k": ["julia sand", "letters", "machine politics"],
            "n": 0
        },
        {
            "id": "veto-twenty-years",
            "tier": "power",
            "t": "Vetoed a first Chinese exclusion bill that would have lasted twenty years, saying it broke a treaty, then signed a ten-year version",
            "k": ["vetoed", "twenty years", "treaty"],
            "n": 0
        },
        {
            "id": "rivers-harbors",
            "tier": "power",
            "t": "Vetoed the Rivers and Harbors Act of 1882 as wasteful, but Congress overrode him",
            "k": ["rivers and harbors", "overrode", "wasteful"],
            "n": 0
        },
        {
            "id": "mongrel-tariff",
            "tier": "power",
            "t": "Signed the Tariff of 1883, nicknamed the “Mongrel Tariff”",
            "k": ["mongrel tariff", "mongrel", "tariff of 1883"],
            "n": 0
        },
        {
            "id": "star-route",
            "tier": "power",
            "t": "His Justice Department prosecuted the Star Route scandal over cheating on Western mail-delivery contracts",
            "k": ["star route", "mail-delivery", "scandal"],
            "n": 0
        },
        {
            "id": "brooklyn-bridge",
            "tier": "power",
            "t": "Attended the opening of the Brooklyn Bridge (1883) with Governor Grover Cleveland",
            "k": ["brooklyn bridge", "opening", "grover cleveland"],
            "n": 0
        },
        {
            "id": "washington-monument",
            "tier": "power",
            "t": "Dedicated the newly finished Washington Monument near the end of his term (1885)",
            "k": ["washington monument", "dedicated", "1885"],
            "n": 0
        },
        {
            "id": "meridian",
            "tier": "power",
            "t": "The International Meridian Conference in Washington (1884) chose Greenwich, England, as the prime meridian",
            "k": ["international meridian conference", "meridian", "greenwich"],
            "n": 0
        },
        {
            "id": "no-vp",
            "tier": "power",
            "t": "Had no vice president; his sister Mary McElroy was White House hostess because his wife, Ellen, had died in 1880",
            "k": ["mary mcelroy", "mcelroy", "no vice president", "ellen"],
            "n": 0
        },
        {
            "id": "burned-papers",
            "tier": "power",
            "t": "Had most of his personal papers burned shortly before he died",
            "k": ["papers", "burned"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Garfield’s successor, not Garfield",
        "body": "Many clues in this man’s tossups are really about James Garfield: the 1880 election, the dark-horse convention, and Charles Guiteau’s attack. If a question asks for the president who was shot in 1881, the answer is Garfield; if it asks who took over and then signed the Pendleton Act, it is Arthur. Players also mix up the Gilded Age presidents between Grant and McKinley: Hayes (1877–1881), Garfield (1881), Arthur (1881–1885), Cleveland (1885–1889 and 1893–1897), and Benjamin Harrison (1889–1893).",
        "fix": "Listen for what happened after September 1881: the Pendleton Act, the Chinese Exclusion Act, the Tiffany redecoration, and a background at the Port of New York all mean Arthur. Guiteau’s shout that “Arthur is president now” points to Arthur only when the question asks who took over.",
        "line": "Real answer line: Chester Alan <b><u>Arthur</u></b> (do not accept or prompt on “James Garfield”)"
    },
    "tests": {
        "right": [
            "Chester A. Arthur",
            "Chester Arthur",
            "Arthur",
            "Chester Alan Arthur",
            "President Arthur",
            "Chester Arther"
        ],
        "prompt": [
            "Chester"
        ],
        "wrong": [
            "James Garfield",
            "Rutherford B. Hayes",
            "Grover Cleveland",
            "Roscoe Conkling",
            "King Arthur",
            "Douglas MacArthur",
            "Charles Guiteau"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
