import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "secretary-of-state",
    "name": "Secretary of State",
    "mono": "SOS",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "The nation’s top diplomat · Fourth in line for the presidency",
    "dates": "Office created 1789",
    "briefing": "The Secretary of State is the president’s top adviser on foreign affairs and the nation’s chief diplomat, leading the department that runs American embassies and issues passports. Thomas Jefferson held the job first, and five more holders later became president. Holders of the office arranged the purchase of Alaska, launched the Marshall Plan to rebuild Europe, and broke barriers: Madeleine Albright was the first woman in the job, and Colin Powell was the first African American.",
    "answerHtml": "<b><u>Secretary of State</u></b> (prompt on <u>Secretary</u> or <u>State Department</u>; do not accept other cabinet posts or “Vice President”)",
    "accept": [
        "secretary of state",
        "us secretary of state",
        "united states secretary of state",
        "american secretary of state",
        "secretaries of state",
        "sec of state"
    ],
    "prompt": [
        "secretary",
        "state",
        "state department",
        "department of state",
        "us department of state",
        "united states department of state",
        "foreign minister"
    ],
    "reject": [
        "secretary of war",
        "secretary of defense",
        "defense secretary",
        "secretary of the treasury",
        "treasury secretary",
        "secretary of the navy",
        "secretary of the interior",
        "secretary of homeland security",
        "secretary of commerce",
        "secretary of labor",
        "secretary of agriculture",
        "secretary of education",
        "secretary of energy",
        "attorney general",
        "vice president",
        "vice president of the united states",
        "speaker of the house",
        "president pro tempore",
        "national security adviser",
        "national security advisor",
        "ambassador to the united nations",
        "chief of staff",
        "henry kissinger"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/United_States_Secretary_of_State",
    "qb": {
        "q": "Secretary of State",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "A 1792 law says that a president who resigns must deliver a signed letter to the office of this official. Following that law, Richard Nixon addressed his one-sentence resignation letter in 1974 to the holder of this post, Henry Kissinger.",
            "r": "For 10 points, name this cabinet office, first held by Thomas Jefferson, whose holder is the president’s top foreign-policy adviser."
        },
        {
            "p": "After Ronald Reagan was shot in 1981, Alexander Haig, who held this office, told reporters that he was “in control here” at the White House, even though the law placed others ahead of him in the line of succession.",
            "r": "This official is fourth in that line. For 10 points, name this cabinet post held by Henry Kissinger and Hillary Clinton."
        },
        {
            "p": "Martin Van Buren resigned this office in 1831 during the Petticoat Affair, and James Buchanan held it while negotiating the 1846 Oregon Treaty with Britain. Those two men were the last presidents to have held this job earlier in their careers.",
            "r": "It was also a stepping-stone to the presidency for James Madison and James Monroe. For 10 points, name this cabinet office whose first holder, Thomas Jefferson, also became president."
        },
        {
            "p": "On the night Abraham Lincoln was shot, Lewis Powell attacked the holder of this office at his home in Washington, but the victim survived. Two years later, that same official arranged to buy a huge territory from Russia for about $7.2 million.",
            "r": "Critics called that 1867 purchase of Alaska “Seward’s Folly.” For 10 points, name this cabinet post held by William Seward."
        },
        {
            "p": "A former Army chief of staff who won the 1953 Nobel Peace Prize held this office from 1947 to 1949. In a June 1947 speech at Harvard, he proposed a huge American aid program to rebuild Europe after World War II.",
            "r": "That program was the Marshall Plan. For 10 points, name this cabinet office held by George Marshall under Harry Truman."
        },
        {
            "p": "Born in Prague, Madeleine Albright became the first woman to hold this office in 1997, after serving as ambassador to the United Nations. Four years later, a former chairman of the Joint Chiefs of Staff became the first African American to hold it.",
            "r": "That man, Colin Powell, was followed by Condoleezza Rice. For 10 points, name this cabinet office, the nation’s top diplomat."
        },
        {
            "p": "Daniel Webster held this office when he negotiated the 1842 Webster–Ashburton Treaty, which settled the border between Maine and British Canada, and he held it again under Millard Fillmore. Years earlier, Andrew Jackson called Henry Clay’s appointment to this office part of a “corrupt bargain.”",
            "r": "Clay got this job from John Quincy Adams after the election of 1824. For 10 points, name this cabinet office first held by Thomas Jefferson."
        },
        {
            "p": "A man who had been a young secretary to Abraham Lincoln later held this office and signed a 1901 treaty with Britain’s Lord Pauncefote that cleared the way for an American-controlled canal in Central America. That man also sent the Open Door Notes about trade with China.",
            "r": "For 10 points, name this cabinet office held by John Hay under William McKinley and Theodore Roosevelt."
        },
        {
            "p": "Frank Kellogg won the Nobel Peace Prize for a 1928 pact that tried to outlaw war, and Cordell Hull won it for helping to create the United Nations. Hull held this office for nearly twelve years under Franklin Roosevelt, longer than anyone else.",
            "r": "Its holder leads the department that runs American embassies. For 10 points, name this cabinet office, the president’s chief adviser on foreign affairs."
        },
        {
            "p": "Luis de Onís [“oh-NEES”] negotiated an 1819 treaty with the holder of this office that gave Florida to the United States. That treaty, also called the Transcontinental Treaty, set a border with Spain’s lands all the way to the Pacific Ocean.",
            "r": "That official also wrote much of the Monroe Doctrine. For 10 points, name this cabinet office held by John Quincy Adams under James Monroe."
        },
        {
            "p": "John Jay ran foreign affairs under the Articles of Confederation and briefly stayed on until the first holder of this new office arrived in 1790. That first holder quarreled with Treasury Secretary Alexander Hamilton and resigned at the end of 1793.",
            "r": "This office’s department was first named the Department of Foreign Affairs. For 10 points, name this cabinet post first held by Thomas Jefferson under George Washington."
        },
        {
            "p": "The holder of this office keeps the Great Seal of the United States, and that holder’s department is nicknamed for its home in the Foggy Bottom neighborhood of Washington, D.C. That department’s headquarters is named for Harry S Truman.",
            "r": "That department issues passports and runs embassies. For 10 points, name this cabinet office, fourth in the line of presidential succession."
        },
        {
            "p": "Edward Everett, the main speaker at the Gettysburg ceremony where Lincoln gave his famous address, had earlier held this office. Charles Evans Hughes held it while hosting the Washington Naval Conference, which limited the battleships of the major naval powers.",
            "r": "William Jennings Bryan resigned from this office in 1915 after the _Lusitania_ sinking. For 10 points, name this cabinet office first held by Thomas Jefferson."
        },
        {
            "p": "After the 1973 Yom Kippur War, the holder of this office used “shuttle diplomacy,” flying back and forth between Middle Eastern capitals to work out agreements between Israel and its neighbors. That holder was the first person to hold this office while also serving as National Security Adviser.",
            "r": "That man, Henry Kissinger, served under Richard Nixon and Gerald Ford. For 10 points, name this cabinet post, the nation’s chief diplomat."
        },
        {
            "p": "Dean Acheson won a Pulitzer Prize for _Present at the Creation_, a memoir of his years in this office under Harry Truman. His successor, John Foster Dulles, argued that the United States should be willing to go to the brink of war, a policy critics called “brinkmanship.”",
            "r": "An airport outside Washington, D.C., is named for Dulles. For 10 points, name this cabinet office that Hillary Clinton held from 2009 to 2013."
        }
    ],
    "clues": [
        {
            "id": "top-diplomat",
            "tier": "giveaway",
            "t": "The nation’s top diplomat: the cabinet officer who advises the president on foreign affairs",
            "k": ["diplomat", "foreign affairs", "cabinet"],
            "n": 0
        },
        {
            "id": "jefferson-first",
            "tier": "giveaway",
            "t": "First held by Thomas Jefferson, under George Washington (1790–1793)",
            "k": ["thomas jefferson", "jefferson", "first held"],
            "n": 0,
            "rabbit": "Thomas Jefferson"
        },
        {
            "id": "fourth-in-line",
            "tier": "giveaway",
            "t": "Fourth in the presidential line of succession, after the vice president, the Speaker of the House, and the president pro tempore",
            "k": ["fourth", "line of succession", "succession"],
            "n": 0,
            "rabbit": "Vice President of the United States"
        },
        {
            "id": "famous-holders",
            "tier": "giveaway",
            "t": "Famous holders include Henry Kissinger (1973–1977) and Hillary Clinton (2009–2013)",
            "k": ["kissinger", "hillary clinton", "clinton"],
            "n": 0
        },
        {
            "id": "seward-alaska",
            "tier": "middle",
            "t": "William Seward arranged the purchase of Alaska from Russia in 1867 (“Seward’s Folly”)",
            "k": ["seward", "alaska", "1867", "folly"],
            "n": 0,
            "rabbit": "William Henry Seward"
        },
        {
            "id": "marshall-plan",
            "tier": "middle",
            "t": "George Marshall, a former Army chief of staff, proposed the Marshall Plan in a 1947 Harvard speech; he won the 1953 Nobel Peace Prize",
            "k": ["marshall plan", "george marshall", "harvard", "1953"],
            "n": 0,
            "rabbit": "Marshall Plan"
        },
        {
            "id": "firsts",
            "tier": "middle",
            "t": "Firsts: Madeleine Albright (first woman, 1997), Colin Powell (first African American, 2001), and Condoleezza Rice (first African American woman, 2005)",
            "k": ["albright", "colin powell", "condoleezza rice", "powell"],
            "n": 0
        },
        {
            "id": "six-presidents",
            "tier": "middle",
            "t": "Six holders later became president: Jefferson, Madison, Monroe, John Quincy Adams, Van Buren, and Buchanan",
            "k": ["six", "madison", "monroe", "van buren", "buchanan"],
            "n": 0
        },
        {
            "id": "corrupt-bargain",
            "tier": "middle",
            "t": "Henry Clay got the job from John Quincy Adams after the 1824 election, which Andrew Jackson called a “corrupt bargain”",
            "k": ["corrupt bargain", "henry clay", "1824"],
            "n": 0,
            "rabbit": "Henry Clay"
        },
        {
            "id": "jqa",
            "tier": "middle",
            "t": "John Quincy Adams wrote much of the Monroe Doctrine and won Florida from Spain in the Adams–Onís Treaty (1819)",
            "k": ["john quincy adams", "monroe doctrine", "florida", "1819"],
            "n": 0
        },
        {
            "id": "embassies",
            "tier": "middle",
            "t": "Leads the department that runs American embassies and issues passports",
            "k": ["embassies", "passports"],
            "n": 0
        },
        {
            "id": "bryan-resigns",
            "tier": "middle",
            "t": "William Jennings Bryan resigned in 1915 after the _Lusitania_ sinking",
            "k": ["bryan", "lusitania", "1915"],
            "n": 0
        },
        {
            "id": "resignation-letter",
            "tier": "power",
            "t": "A 1792 law says a president resigns by sending a signed letter to this office; Nixon’s 1974 letter went to Henry Kissinger",
            "k": ["1792", "resignation", "nixon"],
            "n": 0
        },
        {
            "id": "haig",
            "tier": "power",
            "t": "Alexander Haig said he was “in control here” after Ronald Reagan was shot (1981), though others came before him in the line of succession",
            "k": ["haig", "in control here", "1981"],
            "n": 0
        },
        {
            "id": "webster",
            "tier": "power",
            "t": "Daniel Webster negotiated the Webster–Ashburton Treaty (1842), settling the Maine–Canada border",
            "k": ["daniel webster", "ashburton", "1842"],
            "n": 0
        },
        {
            "id": "van-buren-buchanan",
            "tier": "power",
            "t": "Martin Van Buren resigned it during the Petticoat Affair (1831); James Buchanan negotiated the Oregon Treaty (1846)",
            "k": ["petticoat", "oregon treaty", "1846"],
            "n": 0
        },
        {
            "id": "hay",
            "tier": "power",
            "t": "John Hay, once Lincoln’s young secretary, sent the Open Door Notes on China and signed the Hay–Pauncefote Treaty (1901)",
            "k": ["john hay", "open door", "pauncefote"],
            "n": 0
        },
        {
            "id": "nobel-winners",
            "tier": "power",
            "t": "Nobel Peace Prize winners Frank Kellogg (Kellogg–Briand Pact, 1928) and Cordell Hull, the longest-serving holder (1933–1944)",
            "k": ["kellogg", "cordell hull", "longest-serving"],
            "n": 0
        },
        {
            "id": "jay-foreign-affairs",
            "tier": "power",
            "t": "John Jay ran foreign affairs under the Articles of Confederation; in 1789 the new department was first called the Department of Foreign Affairs",
            "k": ["john jay", "articles of confederation", "1789"],
            "n": 0
        },
        {
            "id": "jefferson-hamilton",
            "tier": "power",
            "t": "Jefferson quarreled with Treasury Secretary Alexander Hamilton and resigned at the end of 1793",
            "k": ["alexander hamilton", "hamilton", "1793"],
            "n": 0
        },
        {
            "id": "great-seal",
            "tier": "power",
            "t": "Keeps the Great Seal of the United States; its department’s home is in Foggy Bottom, in the Harry S Truman Building",
            "k": ["great seal", "foggy bottom", "truman building"],
            "n": 0
        },
        {
            "id": "everett-hughes",
            "tier": "power",
            "t": "Holders included Edward Everett, the main Gettysburg speaker, and Charles Evans Hughes, who hosted the Washington Naval Conference and later became Chief Justice",
            "k": ["everett", "charles evans hughes", "naval conference"],
            "n": 0
        },
        {
            "id": "shuttle-diplomacy",
            "tier": "power",
            "t": "Henry Kissinger’s “shuttle diplomacy” after the 1973 Yom Kippur War; first to hold it while also National Security Adviser",
            "k": ["shuttle diplomacy", "yom kippur", "national security"],
            "n": 0
        },
        {
            "id": "seward-attack",
            "tier": "power",
            "t": "Lewis Powell attacked William Seward at home on the night Lincoln was shot; Seward survived",
            "k": ["lewis powell", "survived"],
            "n": 0
        },
        {
            "id": "acheson-dulles",
            "tier": "power",
            "t": "Dean Acheson wrote _Present at the Creation_; John Foster Dulles was linked to “brinkmanship,” and Dulles Airport is named for him",
            "k": ["acheson", "present at the creation", "brinkmanship", "dulles"],
            "n": 0
        }
    ],
    "trap": {
        "title": "The office, not the person",
        "body": "Tossups on this office are packed with famous holders, such as Thomas Jefferson, William Seward, George Marshall, and Henry Kissinger, so it is tempting to buzz with a name; that is wrong when the question asks for “this office” or “this cabinet post.” Players also mix it up with other cabinet jobs: Alexander Hamilton was Secretary of the Treasury, and the Secretary of War ran the Army until 1947. The department this official runs, the State Department, is a separate answer line.",
        "fix": "Listen for the noun. “This office,” “this post,” or “this position” wants the Secretary of State; “this department” wants the State Department; “this man” or “this woman” wants a person. Treaties, embassies, and diplomats point here, not to Defense or the Treasury.",
        "line": "Real answer line: <b><u>Secretary of State</u></b> (prompt on <u>Secretary</u> or <u>State Department</u>; do not accept other cabinet posts or “Vice President”)"
    },
    "tests": {
        "right": [
            "Secretary of State",
            "U.S. Secretary of State",
            "secretary of sate",
            "United States Secretary of State"
        ],
        "prompt": [
            "Secretary",
            "State Department"
        ],
        "wrong": [
            "Secretary of War",
            "Secretary of Defense",
            "Secretary of the Treasury",
            "Vice President",
            "Attorney General",
            "Henry Kissinger"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
