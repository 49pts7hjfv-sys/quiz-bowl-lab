import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "hillary-clinton",
    "name": "Hillary Clinton",
    "mono": "HRC",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "First Lady, senator, and Secretary of State · 2016 Democratic nominee",
    "dates": "Born 1947; Secretary of State 2009–2013",
    "briefing": "Hillary Rodham Clinton gave the first student commencement speech in Wellesley College’s history and met her future husband, Bill Clinton, at Yale Law School. While serving as First Lady (1993–2001), she won a U.S. Senate seat from New York in 2000, becoming the first First Lady elected to public office, and she later served as Secretary of State (2009–2013). In 2016 she became the first woman nominated for president by a major party; she won the national popular vote but lost the Electoral College to Donald Trump.",
    "answerHtml": "<b><u>Hillary</u></b> Rodham <b><u>Clinton</u></b> (accept <u>Hillary Rodham</u>; prompt on <u>Clinton</u> or <u>Hillary</u> alone; do not accept “Bill Clinton” or “Chelsea Clinton”)",
    "accept": [
        "hillary clinton",
        "hillary rodham clinton",
        "hillary diane rodham clinton",
        "hillary diane rodham",
        "hillary rodham",
        "hillary r clinton",
        "secretary clinton"
    ],
    "prompt": [
        "clinton",
        "hillary",
        "senator clinton",
        "mrs clinton"
    ],
    "reject": [
        "bill clinton",
        "william clinton",
        "william jefferson clinton",
        "william j clinton",
        "president clinton",
        "governor clinton",
        "chelsea clinton",
        "chelsea",
        "dewitt clinton",
        "george clinton",
        "henry clinton",
        "roger clinton",
        "edmund hillary",
        "barack obama",
        "michelle obama",
        "donald trump",
        "tim kaine",
        "bernie sanders",
        "joe biden",
        "condoleezza rice",
        "madeleine albright",
        "john kerry",
        "eleanor roosevelt",
        "nancy pelosi",
        "kamala harris",
        "geraldine ferraro",
        "sarah palin",
        "elizabeth warren",
        "laura bush",
        "barbara bush"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Hillary_Clinton",
    "qb": {
        "q": "Hillary",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In 1969, this woman became the first student to give a commencement speech at Wellesley College, and she began by answering the remarks of the previous speaker, Senator Edward Brooke. _Life_ magazine featured her and her speech that summer.",
            "r": "She went on to earn a law degree from Yale. For 10 points, name this woman who served as First Lady from 1993 to 2001."
        },
        {
            "p": "As a high school student in Park Ridge, Illinois, this future politician campaigned for Republican Barry Goldwater in 1964, calling herself a “Goldwater Girl.” After law school, she worked for Marian Wright Edelman’s Children’s Defense Fund.",
            "r": "She later became a Democratic senator from New York. For 10 points, name this woman who was Secretary of State from 2009 to 2013."
        },
        {
            "p": "In 1974, this young lawyer joined the staff of the House Judiciary Committee’s impeachment inquiry into President Richard Nixon. Later that year, she moved to Fayetteville to teach at the University of Arkansas law school, and in 1975 she married a fellow Yale Law graduate there.",
            "r": "For 10 points, name this woman who became First Lady when her husband, Bill Clinton, took office in 1993."
        },
        {
            "p": "In 1979, this lawyer became the first woman made a full partner at the Rose Law Firm in Little Rock. She kept her maiden name for several years after her 1975 wedding to a man who was elected governor of Arkansas in 1978.",
            "r": "For 10 points, name this First Lady of Arkansas who became First Lady of the United States in 1993."
        },
        {
            "p": "In 1993, this woman was put in charge of a task force on national health care reform, and the plan it produced failed to pass Congress and was dropped in 1994. In 1997, she won a Grammy Award for reading the audiobook of her book about raising children.",
            "r": "That book was _It Takes a Village_. For 10 points, name this First Lady, the wife of Bill Clinton."
        },
        {
            "p": "This author took the title of a 1996 book from a saying, often called an African proverb, that a whole community helps raise each child. The book argued that families, neighbors, schools, businesses, and governments all share responsibility for children’s well-being.",
            "r": "That book is _It Takes a Village_. For 10 points, name this First Lady who wrote it while her husband was president."
        },
        {
            "p": "At the United Nations’ Fourth World Conference on Women in 1995, this speaker told the audience that “human rights are women’s rights and women’s rights are human rights, once and for all.” She gave that speech in Beijing, China.",
            "r": "For 10 points, name this First Lady of the United States from 1993 to 2001, who later became a senator from New York."
        },
        {
            "p": "In a 2000 Senate race, this candidate defeated Republican congressman Rick Lazio, who had entered the race after New York City mayor Rudy Giuliani dropped out. That campaign began with a “listening tour” of New York State in 1999.",
            "r": "She became the first First Lady elected to public office. For 10 points, name this senator from New York from 2001 to 2009."
        },
        {
            "p": "When she ended her 2008 presidential campaign, this candidate said that although her supporters had not shattered “that highest, hardest glass ceiling,” it had “about 18 million cracks in it.” Earlier that year, she won the New Hampshire primary.",
            "r": "She lost the Democratic nomination to Barack Obama, who then named her Secretary of State. For 10 points, name this senator from New York."
        },
        {
            "p": "In 2009, this diplomat gave Russia’s foreign minister, Sergey Lavrov, a button meant to say “reset” in Russian, but its label actually read “overload.” Weeks earlier, at her confirmation hearing, she had called for a foreign policy built on “smart power.”",
            "r": "For 10 points, name this woman who served as Secretary of State from 2009 to 2013 under Barack Obama."
        },
        {
            "p": "In 2011, this diplomat traveled to Myanmar, the first visit there by a top U.S. diplomat in more than 50 years, and met the democracy leader Aung San Suu Kyi [“awng sahn soo CHEE”]. That year, her article “America’s Pacific Century” called for the United States to focus more on Asia.",
            "r": "For 10 points, name this Secretary of State from 2009 to 2013, who had earlier served as a senator from New York."
        },
        {
            "p": "Pete Souza’s photograph of officials in the White House Situation Room during the 2011 raid on Osama bin Laden’s hideout shows this woman holding her hand over her mouth. She wrote about that period of her life in the 2014 memoir _Hard Choices_.",
            "r": "For 10 points, name this woman who was Secretary of State during Barack Obama’s first term."
        },
        {
            "p": "Vermont senator Bernie Sanders asked that this candidate be nominated by acclamation at the 2016 Democratic convention in Philadelphia, ending their long primary race. She chose Virginia senator Tim Kaine as her running mate.",
            "r": "She was the first woman nominated for president by a major party. For 10 points, name this Democrat who lost the 2016 election to Donald Trump."
        },
        {
            "p": "This author co-wrote the 2021 thriller _State of Terror_ with the Canadian mystery novelist Louise Penny. Her memoirs include _Living History_ (2003), _Hard Choices_ (2014), and _What Happened_ (2017).",
            "r": "For 10 points, name this Democrat who won the popular vote but lost the Electoral College to Donald Trump in 2016."
        },
        {
            "p": "In January 2025, President Joe Biden awarded this politician the Presidential Medal of Freedom. Born in Chicago in 1947, she grew up in the suburb of Park Ridge, Illinois, and graduated from Wellesley College.",
            "r": "She later served as a senator from New York and as Secretary of State. For 10 points, name this wife of the 42nd president, Bill Clinton."
        }
    ],
    "clues": [
        {
            "id": "first-lady",
            "tier": "giveaway",
            "t": "First Lady of the United States (1993–2001), the wife of the 42nd president, Bill Clinton",
            "k": ["first lady", "42nd president", "wife"],
            "n": 0,
            "rabbit": "Bill Clinton"
        },
        {
            "id": "senator",
            "tier": "giveaway",
            "t": "U.S. senator from New York (2001–2009), the first First Lady elected to public office",
            "k": ["senator", "new york", "public office"],
            "n": 0
        },
        {
            "id": "secretary-of-state",
            "tier": "giveaway",
            "t": "Secretary of State (2009–2013) under President Barack Obama",
            "k": ["secretary of state", "barack obama", "obama"],
            "n": 0,
            "rabbit": "Secretary of State"
        },
        {
            "id": "election-2016",
            "tier": "giveaway",
            "t": "2016 Democratic nominee, the first woman nominated for president by a major party; won the popular vote but lost the Electoral College to Donald Trump",
            "k": ["2016", "first woman", "popular vote", "electoral college", "donald trump"],
            "n": 0,
            "rabbit": "Electoral College"
        },
        {
            "id": "yale",
            "tier": "middle",
            "t": "Met her future husband at Yale Law School, where she earned her law degree in 1973",
            "k": ["yale law school", "yale", "1973"],
            "n": 0
        },
        {
            "id": "wellesley",
            "tier": "middle",
            "t": "Graduated in 1969 from Wellesley College, a women’s college in Massachusetts",
            "k": ["wellesley", "1969"],
            "n": 0
        },
        {
            "id": "village",
            "tier": "middle",
            "t": "Wrote _It Takes a Village_ (1996), named for a saying that a whole community helps raise each child",
            "k": ["it takes a village", "village", "1996"],
            "n": 0
        },
        {
            "id": "beijing",
            "tier": "middle",
            "t": "At a 1995 UN conference on women in Beijing, declared that “women’s rights are human rights”",
            "k": ["beijing", "human rights", "1995"],
            "n": 0
        },
        {
            "id": "health-care",
            "tier": "middle",
            "t": "Led a 1993 task force on national health care reform; its plan failed to pass Congress in 1994",
            "k": ["health care", "task force", "1993"],
            "n": 0
        },
        {
            "id": "glass-ceiling",
            "tier": "middle",
            "t": "Lost the 2008 Democratic nomination to Barack Obama; said her campaign left “about 18 million cracks” in the “highest, hardest glass ceiling”",
            "k": ["glass ceiling", "18 million cracks", "2008"],
            "n": 0
        },
        {
            "id": "arkansas",
            "tier": "middle",
            "t": "First Lady of Arkansas while her husband was governor (1979–1981 and 1983–1992)",
            "k": ["arkansas", "governor"],
            "n": 0
        },
        {
            "id": "goldwater",
            "tier": "power",
            "t": "Grew up in Park Ridge, Illinois; as a teenager, campaigned for Republican Barry Goldwater in 1964 as a “Goldwater Girl”",
            "k": ["goldwater girl", "goldwater", "park ridge"],
            "n": 0
        },
        {
            "id": "commencement",
            "tier": "power",
            "t": "First student to give a commencement speech at Wellesley (1969), answering Senator Edward Brooke; featured in _Life_ magazine",
            "k": ["commencement", "edward brooke", "life magazine"],
            "n": 0
        },
        {
            "id": "defense-fund",
            "tier": "power",
            "t": "Worked for Marian Wright Edelman’s Children’s Defense Fund and on the House impeachment inquiry into Richard Nixon (1974)",
            "k": ["defense fund", "impeachment inquiry", "marian wright edelman", "nixon"],
            "n": 0
        },
        {
            "id": "rose-law",
            "tier": "power",
            "t": "Taught law at the University of Arkansas; first woman made a full partner at Little Rock’s Rose Law Firm (1979)",
            "k": ["rose law firm", "little rock", "partner"],
            "n": 0
        },
        {
            "id": "grammy",
            "tier": "power",
            "t": "Won a Grammy Award (1997) for reading the audiobook of _It Takes a Village_",
            "k": ["grammy", "audiobook"],
            "n": 0
        },
        {
            "id": "lazio",
            "tier": "power",
            "t": "Won the 2000 Senate race over Rick Lazio after Rudy Giuliani dropped out; the campaign began with a 1999 “listening tour”",
            "k": ["rick lazio", "lazio", "giuliani", "listening tour"],
            "n": 0
        },
        {
            "id": "reset",
            "tier": "power",
            "t": "Called for “smart power” at her 2009 confirmation hearing; gave Russia’s Sergey Lavrov a “reset” button whose Russian label actually meant “overload”",
            "k": ["reset", "lavrov", "overload", "smart power"],
            "n": 0
        },
        {
            "id": "myanmar",
            "tier": "power",
            "t": "Visited Myanmar in 2011, the first visit by a U.S. Secretary of State in more than 50 years, and met Aung San Suu Kyi",
            "k": ["myanmar", "aung san suu kyi", "burma"],
            "n": 0
        },
        {
            "id": "pacific-century",
            "tier": "power",
            "t": "Her 2011 article “America’s Pacific Century” urged the United States to focus more on Asia",
            "k": ["pacific century", "asia"],
            "n": 0
        },
        {
            "id": "situation-room",
            "tier": "power",
            "t": "Holds her hand over her mouth in Pete Souza’s photo of the Situation Room during the 2011 raid on Osama bin Laden",
            "k": ["situation room", "pete souza", "bin laden"],
            "n": 0
        },
        {
            "id": "memoirs",
            "tier": "power",
            "t": "Memoirs: _Living History_ (2003), _Hard Choices_ (2014), and _What Happened_ (2017)",
            "k": ["living history", "hard choices", "what happened"],
            "n": 0
        },
        {
            "id": "kaine",
            "tier": "power",
            "t": "Her 2016 running mate was Virginia senator Tim Kaine; Bernie Sanders asked that she be nominated by acclamation",
            "k": ["tim kaine", "kaine", "bernie sanders", "acclamation"],
            "n": 0,
            "rabbit": "Bernie Sanders"
        },
        {
            "id": "gutsy-women",
            "tier": "power",
            "t": "Wrote _The Book of Gutsy Women_ (2019) with her daughter, Chelsea, and the thriller _State of Terror_ (2021) with Louise Penny",
            "k": ["gutsy women", "state of terror", "louise penny", "chelsea"],
            "n": 0
        },
        {
            "id": "medal-of-freedom",
            "tier": "power",
            "t": "Received the Presidential Medal of Freedom from President Joe Biden in January 2025",
            "k": ["medal of freedom", "joe biden", "2025"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Hillary, not Bill",
        "body": "Hillary and Bill Clinton share a lot of clues: Arkansas, Yale Law School, the White House years from 1993 to 2001, and the health care plan that failed in 1994. Saying only “Clinton” earns a prompt, and “Bill Clinton” is wrong when the question wants her. Two earlier New York politicians, George Clinton and DeWitt Clinton, share the last name too.",
        "fix": "“She,” the Senate seat from New York (2001–2009), Secretary of State, Wellesley, the Beijing speech, and the 2016 election mean Hillary. The saxophone, NAFTA, welfare reform, and the 1998 impeachment mean Bill. If you are prompted after saying “Clinton,” add “Hillary.”",
        "line": "Real answer line: <b><u>Hillary</u></b> Rodham <b><u>Clinton</u></b> (accept <u>Hillary Rodham</u>; prompt on <u>Clinton</u>; do not accept “Bill Clinton”)"
    },
    "tests": {
        "right": [
            "Hillary Clinton",
            "Hillary Rodham Clinton",
            "Hilary Clinton",
            "Hillary Rodham",
            "Secretary Clinton",
            "Hillary Diane Rodham Clinton"
        ],
        "prompt": [
            "Clinton",
            "Hillary",
            "Mrs. Clinton"
        ],
        "wrong": [
            "Bill Clinton",
            "Chelsea Clinton",
            "DeWitt Clinton",
            "Edmund Hillary",
            "President Clinton",
            "Barack Obama",
            "Condoleezza Rice",
            "Donald Trump"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
