import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "nathan-hale",
    "name": "Nathan Hale",
    "mono": "NH",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Patriot spy executed by the British in 1776 · Connecticut’s state hero",
    "dates": "1755–1776",
    "briefing": "Nathan Hale was a 21-year-old Yale graduate and Connecticut schoolteacher when he volunteered to spy on the British on Long Island in September 1776. Disguised as a schoolmaster, he was caught and executed by the British on September 22, 1776. According to later accounts, his last words were “I only regret that I have but one life to lose for my country,” and today he is Connecticut’s official state hero.",
    "answerHtml": "Nathan <b><u>Hale</u></b>",
    "accept": [
        "nathan hale",
        "hale",
        "capt nathan hale"
    ],
    "prompt": [
        "nathan"
    ],
    "reject": [
        "john andre",
        "major john andre",
        "andre",
        "benedict arnold",
        "nathanael greene",
        "nathaniel greene",
        "nathan greene",
        "benjamin tallmadge",
        "tallmadge",
        "thomas knowlton",
        "knowlton",
        "william hull",
        "edward everett hale",
        "sarah josepha hale",
        "enoch hale",
        "patrick henry",
        "paul revere",
        "robert rogers",
        "culper ring",
        "james armistead",
        "james armistead lafayette"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Nathan_Hale",
    "qb": {
        "q": "Nathan Hale",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "This man’s most famous words may have been inspired by a line in Joseph Addison’s play _Cato_ about dying “but once to serve our country.” A British officer, John Montresor, later told American officers about this man’s calm last moments.",
            "r": "For 10 points, name this patriot spy who supposedly said, “I only regret that I have but one life to lose for my country.”"
        },
        {
            "p": "This man was captured on September 21, 1776, the same day a great fire swept through British-occupied New York City. He was taken to the headquarters of General William Howe.",
            "r": "Howe ordered him executed the next day without a trial. For 10 points, name this Connecticut schoolteacher who had been spying for George Washington."
        },
        {
            "p": "This officer belonged to Knowlton’s Rangers, an elite scouting unit whose commander was killed at the Battle of Harlem Heights while this officer was behind enemy lines on Long Island.",
            "r": "He had volunteered when George Washington asked for a spy. For 10 points, name this Connecticut patriot executed in 1776."
        },
        {
            "p": "Posing as a schoolmaster looking for work, this man crossed Long Island Sound from Norwalk, Connecticut, to gather information about British troops. He carried his college diploma as part of his disguise.",
            "r": "For 10 points, name this American spy who was captured and executed by the British in September 1776."
        },
        {
            "p": "This man’s Yale classmate and friend Benjamin Tallmadge later organized the Culper Ring, a spy network based in New York City and on Long Island that gave George Washington much better information about the British than this man had been able to gather.",
            "r": "For 10 points, name this patriot spy who supposedly regretted having “but one life to lose” for his country."
        },
        {
            "p": "After graduating from Yale in 1773, this man taught school in East Haddam and then at the Union School in New London, Connecticut, before joining the army in 1775. Both of those schoolhouses are now museums.",
            "r": "In 1776, he volunteered to spy on the British. For 10 points, name this Connecticut patriot who was executed that September."
        },
        {
            "p": "A copy of Bela Pratt’s statue of this man, whose original stands outside Connecticut Hall at Yale, was placed at the headquarters of the Central Intelligence Agency in Langley, Virginia.",
            "r": "Connecticut later named him its official state hero. For 10 points, name this patriot spy executed by the British in 1776."
        },
        {
            "p": "Frederick MacMonnies’s 1890s bronze statue of this man stands in City Hall Park in lower Manhattan, the island where he died in 1776, only three years after graduating from Yale.",
            "r": "For 10 points, name this patriot spy who supposedly said, “I only regret that I have but one life to lose for my country.”"
        },
        {
            "p": "This man’s grandnephew, a Boston minister, wrote the 1863 story “The Man Without a Country,” about an army officer sentenced to spend the rest of his life on Navy ships without ever hearing news of the United States.",
            "r": "For 10 points, name this Connecticut schoolteacher who was executed as a spy in 1776."
        },
        {
            "p": "This man’s friend William Hull, who later surrendered Detroit to the British in the War of 1812, reportedly tried to talk him out of his dangerous mission and later recorded his famous last words.",
            "r": "For 10 points, name this Connecticut patriot who was executed after spying on the British in 1776."
        },
        {
            "p": "This man was born in 1755 in Coventry, Connecticut, where his family’s homestead is now a museum, and he was only 21 years old when he died. His older brother Enoch went to Yale with him.",
            "r": "He was a captain in the Continental Army when he volunteered to spy behind British lines. For 10 points, name this patriot executed in September 1776."
        },
        {
            "p": "After George Washington’s army lost the Battle of Long Island in August 1776, this young captain volunteered to slip behind enemy lines and find out where the British would strike next.",
            "r": "He was caught and executed that September. For 10 points, name this patriot spy who is the official state hero of Connecticut."
        },
        {
            "p": "According to one account, the Loyalist ranger Robert Rogers tricked this man into revealing his mission by pretending to be a fellow patriot. Rogers had become famous leading a unit of rangers in the French and Indian War.",
            "r": "For 10 points, name this American spy executed by the British in 1776, who supposedly regretted having “but one life to lose” for his country."
        },
        {
            "p": "As a Yale student, this man joined the Linonian [“lih-NOH-nee-un”] Society, a club for debate and literature, and he graduated in 1773 at age 18, only three years before his death.",
            "r": "He later taught school and then spied for George Washington. For 10 points, name this Connecticut patriot executed in 1776."
        },
        {
            "p": "While this man was behind enemy lines in September 1776, the British landed at Kips Bay and captured New York City. He was caught as he tried to make his way back to the American lines.",
            "r": "For 10 points, name this Connecticut schoolteacher and spy who supposedly said, “I only regret that I have but one life to lose for my country.”"
        }
    ],
    "clues": [
        {
            "id": "one-life",
            "tier": "giveaway",
            "t": "Supposedly said, “I only regret that I have but one life to lose for my country”",
            "k": ["one life to lose", "regret", "my country"],
            "n": 0
        },
        {
            "id": "spy-1776",
            "tier": "giveaway",
            "t": "American spy executed by the British on September 22, 1776, at age 21",
            "k": ["september 22", "spy", "1776", "age 21"],
            "n": 0
        },
        {
            "id": "schoolteacher",
            "tier": "giveaway",
            "t": "Connecticut schoolteacher who spied on the British for George Washington",
            "k": ["schoolteacher", "george washington"],
            "n": 0
        },
        {
            "id": "state-hero",
            "tier": "giveaway",
            "t": "Official state hero of Connecticut",
            "k": ["state hero", "connecticut"],
            "n": 0,
            "rabbit": "Connecticut"
        },
        {
            "id": "yale",
            "tier": "middle",
            "t": "Graduated from Yale in 1773, then taught school in Connecticut",
            "k": ["yale", "1773"],
            "n": 0
        },
        {
            "id": "long-island",
            "tier": "middle",
            "t": "Volunteered to spy on British troops on Long Island after Washington lost the Battle of Long Island (August 1776)",
            "k": ["battle of long island", "long island", "volunteered"],
            "n": 0
        },
        {
            "id": "disguise",
            "tier": "middle",
            "t": "Posed as a schoolmaster looking for work and carried his Yale diploma as part of his disguise",
            "k": ["schoolmaster", "diploma", "disguise"],
            "n": 0
        },
        {
            "id": "howe",
            "tier": "middle",
            "t": "Executed without a trial on the orders of General William Howe",
            "k": ["william howe", "howe", "without a trial"],
            "n": 0
        },
        {
            "id": "knowlton",
            "tier": "middle",
            "t": "Served in Knowlton’s Rangers, a scouting unit whose commander was killed at the Battle of Harlem Heights",
            "k": ["knowlton’s rangers", "harlem heights", "knowlton"],
            "n": 0
        },
        {
            "id": "cia-statue",
            "tier": "middle",
            "t": "A copy of Bela Pratt’s statue of him stands at CIA headquarters; the original is at Yale",
            "k": ["bela pratt", "statue", "cia"],
            "n": 0,
            "rabbit": "Central Intelligence Agency"
        },
        {
            "id": "great-fire",
            "tier": "middle",
            "t": "Captured on September 21, 1776, the same day a great fire swept through British-held New York City",
            "k": ["great fire", "september 21", "captured"],
            "n": 0
        },
        {
            "id": "cato",
            "tier": "power",
            "t": "His last words may echo a line in Joseph Addison’s play _Cato_ about dying “but once to serve our country”",
            "k": ["cato", "addison", "but once"],
            "n": 0
        },
        {
            "id": "montresor",
            "tier": "power",
            "t": "British officer John Montresor told American officers about his calm last moments",
            "k": ["montresor", "john montresor"],
            "n": 0
        },
        {
            "id": "tallmadge",
            "tier": "power",
            "t": "His Yale classmate Benjamin Tallmadge later organized the Culper Ring spy network for Washington",
            "k": ["benjamin tallmadge", "culper ring", "tallmadge"],
            "n": 0
        },
        {
            "id": "schools",
            "tier": "power",
            "t": "Taught school in East Haddam and at the Union School in New London, Connecticut; both schoolhouses are museums",
            "k": ["east haddam", "new london", "union school"],
            "n": 0
        },
        {
            "id": "norwalk",
            "tier": "power",
            "t": "Crossed Long Island Sound from Norwalk, Connecticut, to begin his mission",
            "k": ["norwalk", "long island sound"],
            "n": 0
        },
        {
            "id": "macmonnies",
            "tier": "power",
            "t": "Frederick MacMonnies’s 1890s statue of him stands in City Hall Park in Manhattan",
            "k": ["macmonnies", "city hall park"],
            "n": 0
        },
        {
            "id": "grandnephew",
            "tier": "power",
            "t": "His grandnephew, a Boston minister, wrote the story “The Man Without a Country” (1863)",
            "k": ["man without a country", "grandnephew"],
            "n": 0
        },
        {
            "id": "hull",
            "tier": "power",
            "t": "His friend William Hull, who later surrendered Detroit in the War of 1812, recorded his last words",
            "k": ["william hull", "detroit", "hull"],
            "n": 0
        },
        {
            "id": "coventry",
            "tier": "power",
            "t": "Born in Coventry, Connecticut (1755); his family’s homestead there is a museum; his brother Enoch went to Yale with him",
            "k": ["coventry", "homestead", "enoch"],
            "n": 0
        },
        {
            "id": "rogers",
            "tier": "power",
            "t": "One account says the Loyalist ranger Robert Rogers tricked him into revealing his mission",
            "k": ["robert rogers", "loyalist", "tricked"],
            "n": 0
        },
        {
            "id": "linonian",
            "tier": "power",
            "t": "At Yale, joined the Linonian Society, a club for debate and literature; graduated at 18",
            "k": ["linonian", "debate"],
            "n": 0
        },
        {
            "id": "kips-bay",
            "tier": "power",
            "t": "The British landed at Kips Bay and captured New York City while he was behind their lines (September 1776)",
            "k": ["kips bay", "new york city"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Hale or André?",
        "body": "Two famous spies were executed during the Revolution. Nathan Hale was an American captain caught on a mission for George Washington in 1776. John André was a British major caught in 1780 while helping Benedict Arnold plot to hand over West Point, and the Americans executed him. Players also mix up Hale’s “one life to lose” with Patrick Henry’s “Give me liberty, or give me death!”",
        "fix": "Hale clues: Yale, Connecticut schoolteacher, Long Island, Knowlton’s Rangers, 1776, and “one life to lose.” André clues: Benedict Arnold, West Point, captured near Tarrytown, and papers hidden in his stocking. Patrick Henry was a Virginia speaker, not a spy. Saying just “Hale” is enough.",
        "line": "Real answer line: Nathan <b><u>Hale</u></b>"
    },
    "tests": {
        "right": [
            "Nathan Hale",
            "Hale",
            "Captain Nathan Hale",
            "Nathen Hale",
            "nathan hail"
        ],
        "prompt": [
            "Nathan"
        ],
        "wrong": [
            "John Andre",
            "Benedict Arnold",
            "Nathanael Greene",
            "Benjamin Tallmadge",
            "Patrick Henry",
            "Edward Everett Hale",
            "William Hull"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
