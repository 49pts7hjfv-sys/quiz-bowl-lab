import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "battle-of-yorktown",
    "name": "Battle of Yorktown",
    "mono": "YT",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Cornwallis’s 1781 surrender · Effectively ended the American Revolution",
    "dates": "Fought September 28–October 19, 1781",
    "briefing": "In the fall of 1781, British general Lord Cornwallis dug in at Yorktown, a tobacco port on Virginia’s York River, expecting the Royal Navy to rescue him. Instead, a French fleet blocked the Chesapeake Bay, while George Washington’s Americans and the Comte de Rochambeau’s French soldiers surrounded the town and pounded it with cannons. On October 19, Cornwallis surrendered his whole army, which effectively ended the American Revolution.",
    "answerHtml": "Battle of <b><u>Yorktown</u></b> (or Siege of <b><u>Yorktown</u></b>; prompt on descriptions of Cornwallis’s surrender)",
    "accept": [
        "yorktown",
        "battle of yorktown",
        "siege of yorktown",
        "yorktown campaign",
        "surrender at yorktown",
        "yorktown virginia"
    ],
    "prompt": [
        "cornwallis surrender",
        "cornwalliss surrender",
        "surrender of cornwallis"
    ],
    "reject": [
        "jamestown",
        "saratoga",
        "battle of saratoga",
        "trenton",
        "battle of trenton",
        "bunker hill",
        "battle of bunker hill",
        "lexington and concord",
        "battles of lexington and concord",
        "battle of the chesapeake",
        "battle of the capes",
        "battle of the virginia capes",
        "virginia capes",
        "uss yorktown",
        "williamsburg",
        "cowpens",
        "guilford courthouse",
        "kings mountain",
        "monmouth",
        "brandywine",
        "siege of charleston",
        "treaty of paris",
        "green spring",
        "gloucester point"
    ],
    "mediaPending": True,
    "media": [],
    "wiki": "https://en.wikipedia.org/wiki/Siege_of_Yorktown",
    "qb": {
        "q": "Yorktown",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Claiming to be ill, the losing commander at this battle sent his deputy, Charles O’Hara, to the surrender ceremony, where O’Hara tried to hand his sword to the Comte de Rochambeau [“roh-sham-BOH”]. Rochambeau pointed him toward the American commander, who sent him to his own second-in-command, Benjamin Lincoln.",
            "r": "Lord Cornwallis had surrendered his army. For 10 points, name this 1781 battle in Virginia that effectively ended the American Revolution."
        },
        {
            "p": "John Trumbull’s painting of the surrender that ended this battle hangs in the U.S. Capitol Rotunda. It shows Benjamin Lincoln riding a white horse between a line of French officers and a line of American officers.",
            "r": "That painting is titled _Surrender of Lord Cornwallis_. For 10 points, name this 1781 battle in Virginia."
        },
        {
            "p": "James Armistead, an enslaved man, posed as a runaway to spy on the British camp before this battle, and he later took the last name of the French general he worked for, the Marquis de Lafayette. Virginia’s legislature freed him in 1787.",
            "r": "For 10 points, name this 1781 siege where Lord Cornwallis surrendered to George Washington."
        },
        {
            "p": "One night near the end of this siege, the trapped commander tried to ferry his troops across a river to Gloucester Point, but a sudden storm scattered his boats. The next morning, he asked for terms.",
            "r": "That commander was Lord Cornwallis. For 10 points, name this battle on Virginia’s York River that effectively ended the American Revolution."
        },
        {
            "p": "Officers from both sides met at the Augustine Moore House on October 18 to work out the Articles of Capitulation that ended this siege. John Laurens helped negotiate them for the Americans, and they were signed the next day.",
            "r": "For 10 points, name this 1781 siege where Lord Cornwallis surrendered his army to American and French forces."
        },
        {
            "p": "The Comte de Barras [“bah-RAHS”] sailed from Newport, Rhode Island, carrying the heavy French siege guns used in this battle. Those cannons and American guns began bombarding the enemy’s defenses on October 9.",
            "r": "For 10 points, name this battle in which George Washington and the Comte de Rochambeau trapped Lord Cornwallis."
        },
        {
            "p": "When Lord George Germain brought him news of this battle, Prime Minister Lord North reportedly cried out, “Oh God! It is all over!” North resigned a few months later, in March 1782.",
            "r": "For 10 points, name this 1781 battle in Virginia, where the surrender of Lord Cornwallis’s army effectively ended the American Revolution."
        },
        {
            "p": "At the end of this siege, the defeated army was denied the honors of war and had to march out with its flags cased, as revenge for the way Americans who surrendered at Charleston in 1780 had been treated.",
            "r": "According to legend, a band played “The World Turned Upside Down” during the surrender. For 10 points, name this 1781 battle in Virginia where Lord Cornwallis surrendered."
        },
        {
            "p": "After winning a costly victory over Nathanael Greene at Guilford Courthouse in North Carolina, the British commander at this battle marched north into Virginia, where the Marquis de Lafayette’s small army shadowed him. That commander then fortified a tobacco port to wait for British ships.",
            "r": "That commander was Lord Cornwallis. For 10 points, name this 1781 siege where he surrendered."
        },
        {
            "p": "During this siege, Henry Knox commanded the American artillery, and soldiers dug long trenches called parallels so they could move their cannons closer to the enemy’s earthworks. The first parallel was begun on October 6.",
            "r": "For 10 points, name this battle in Virginia where Lord Cornwallis surrendered to George Washington."
        },
        {
            "p": "On October 17, exactly four years after John Burgoyne’s surrender at Saratoga, a British drummer and an officer waving a white handkerchief appeared on the defenses during this battle to ask for a cease-fire.",
            "r": "Two days later, Lord Cornwallis’s army surrendered. For 10 points, name this battle that effectively ended the American Revolution."
        },
        {
            "p": "On the night of October 14, French troops captured Redoubt No. 9 during this siege, while Americans led by Alexander Hamilton stormed Redoubt No. 10 with bayonets. Capturing those two small forts let the attackers extend their trench lines.",
            "r": "For 10 points, name this 1781 siege in Virginia where Lord Cornwallis surrendered to George Washington."
        },
        {
            "p": "On September 5, a French fleet under the Comte de Grasse [“GRAHSS”] drove off British ships under Thomas Graves in the Battle of the Chesapeake, cutting off any rescue by sea for the British army at this battle.",
            "r": "De Grasse had sailed north from the Caribbean with thousands of French soldiers. For 10 points, name this 1781 siege where George Washington trapped Lord Cornwallis."
        },
        {
            "p": "Weeks before this battle, American and French armies secretly marched south from New York, fooling the British commander Henry Clinton into expecting an attack on New York City. A national historic trail follows their route to this battle.",
            "r": "Those armies were led by George Washington and the Comte de Rochambeau. For 10 points, name this battle where Lord Cornwallis surrendered."
        },
        {
            "p": "A few months before this siege, Anthony Wayne’s Americans narrowly escaped a trap set by the British army at the Battle of Green Spring, near Jamestown. The town where this siege took place forms Virginia’s Historic Triangle with Jamestown and Williamsburg.",
            "r": "For 10 points, name this 1781 battle where Lord Cornwallis surrendered, effectively ending the American Revolution."
        }
    ],
    "clues": [
        {
            "id": "cornwallis-surrender",
            "tier": "giveaway",
            "t": "British general Lord Charles Cornwallis surrendered his army there on October 19, 1781",
            "k": ["cornwallis", "october 19", "1781", "surrendered"],
            "n": 0,
            "rabbit": "Charles Cornwallis"
        },
        {
            "id": "virginia",
            "tier": "giveaway",
            "t": "Fought in Virginia, at a tobacco port on the York River near the Chesapeake Bay",
            "k": ["virginia", "york river", "chesapeake bay", "tobacco port"],
            "n": 0
        },
        {
            "id": "ended-war",
            "tier": "giveaway",
            "t": "The last major battle of the American Revolution; it effectively ended the war",
            "k": ["last major battle", "american revolution", "ended"],
            "n": 0,
            "rabbit": "American Revolutionary War"
        },
        {
            "id": "washington-french",
            "tier": "giveaway",
            "t": "George Washington’s American army fought alongside a French army",
            "k": ["george washington", "washington", "french"],
            "n": 0,
            "rabbit": "George Washington"
        },
        {
            "id": "rochambeau",
            "tier": "middle",
            "t": "The French army was led by the Comte de Rochambeau",
            "k": ["comte de rochambeau", "rochambeau"],
            "n": 0
        },
        {
            "id": "de-grasse",
            "tier": "middle",
            "t": "Admiral de Grasse’s French fleet sailed from the Caribbean and blocked the Chesapeake Bay",
            "k": ["de grasse", "caribbean", "fleet"],
            "n": 0
        },
        {
            "id": "chesapeake-battle",
            "tier": "middle",
            "t": "The French beat a British fleet under Thomas Graves at the Battle of the Chesapeake (Virginia Capes), September 5, 1781",
            "k": ["battle of the chesapeake", "virginia capes", "thomas graves", "september 5"],
            "n": 0
        },
        {
            "id": "lafayette",
            "tier": "middle",
            "t": "The Marquis de Lafayette’s small army had been shadowing Cornwallis in Virginia",
            "k": ["marquis de lafayette", "lafayette", "shadowing"],
            "n": 0,
            "rabbit": "Marquis de Lafayette"
        },
        {
            "id": "redoubt-10",
            "tier": "middle",
            "t": "Alexander Hamilton led a night bayonet attack that captured Redoubt No. 10 (October 14, 1781); French troops took Redoubt No. 9",
            "k": ["alexander hamilton", "redoubt", "bayonet"],
            "n": 0,
            "rabbit": "Alexander Hamilton"
        },
        {
            "id": "siege",
            "tier": "middle",
            "t": "A siege (September 28–October 19, 1781): the allies dug trenches called parallels and bombarded the town",
            "k": ["siege", "parallels", "trenches", "bombarded"],
            "n": 0
        },
        {
            "id": "treaty-paris",
            "tier": "middle",
            "t": "Led to peace talks and the Treaty of Paris (1783), which recognized American independence",
            "k": ["treaty of paris", "1783", "independence"],
            "n": 0
        },
        {
            "id": "march-south",
            "tier": "middle",
            "t": "American and French armies secretly marched south from New York, fooling Henry Clinton into expecting an attack on New York City",
            "k": ["henry clinton", "clinton", "marched south"],
            "n": 0
        },
        {
            "id": "upside-down",
            "tier": "middle",
            "t": "According to legend, a British band played “The World Turned Upside Down” at the surrender",
            "k": ["world turned upside down", "upside down", "legend"],
            "n": 0
        },
        {
            "id": "ohara",
            "tier": "power",
            "t": "Cornwallis said he was ill; his deputy Charles O’Hara tried to hand his sword to Rochambeau, who pointed him to Washington",
            "k": ["charles o’hara", "o’hara", "sword"],
            "n": 0
        },
        {
            "id": "benjamin-lincoln",
            "tier": "power",
            "t": "Washington had his own second-in-command, Benjamin Lincoln, accept the British sword",
            "k": ["benjamin lincoln", "second-in-command"],
            "n": 0
        },
        {
            "id": "trumbull",
            "tier": "power",
            "t": "John Trumbull’s painting _Surrender of Lord Cornwallis_ hangs in the U.S. Capitol Rotunda",
            "k": ["john trumbull", "trumbull", "rotunda"],
            "n": 0
        },
        {
            "id": "james-armistead",
            "tier": "power",
            "t": "James Armistead, an enslaved man, spied on the British camp for Lafayette and later took the name James Armistead Lafayette",
            "k": ["james armistead", "armistead", "spied"],
            "n": 0
        },
        {
            "id": "gloucester",
            "tier": "power",
            "t": "Cornwallis tried to escape across the river to Gloucester Point, but a storm stopped him (October 16–17)",
            "k": ["gloucester point", "gloucester", "storm"],
            "n": 0
        },
        {
            "id": "moore-house",
            "tier": "power",
            "t": "The Articles of Capitulation were worked out at the Moore House on October 18, 1781",
            "k": ["moore house", "articles of capitulation"],
            "n": 0
        },
        {
            "id": "de-barras",
            "tier": "power",
            "t": "The Comte de Barras brought French siege guns by sea from Newport, Rhode Island",
            "k": ["de barras", "barras", "newport", "siege guns"],
            "n": 0
        },
        {
            "id": "lord-north",
            "tier": "power",
            "t": "Hearing the news, Prime Minister Lord North reportedly cried, “Oh God! It is all over!”; he resigned in 1782",
            "k": ["lord north", "it is all over", "1782"],
            "n": 0
        },
        {
            "id": "honors-of-war",
            "tier": "power",
            "t": "The British were denied the honors of war (flags cased), as revenge for the American surrender at Charleston in 1780",
            "k": ["honors of war", "charleston", "cased"],
            "n": 0
        },
        {
            "id": "guilford",
            "tier": "power",
            "t": "Before coming to Virginia, Cornwallis won a costly victory over Nathanael Greene at Guilford Courthouse (March 1781)",
            "k": ["guilford courthouse", "nathanael greene", "greene"],
            "n": 0
        },
        {
            "id": "henry-knox",
            "tier": "power",
            "t": "Henry Knox commanded the American artillery",
            "k": ["henry knox", "knox", "artillery"],
            "n": 0,
            "rabbit": "Henry Knox"
        },
        {
            "id": "saratoga-anniversary",
            "tier": "power",
            "t": "Cornwallis asked for terms on October 17, 1781, exactly four years after Burgoyne surrendered at Saratoga",
            "k": ["saratoga", "burgoyne", "four years", "october 17"],
            "n": 0,
            "rabbit": "Battle of Saratoga"
        },
        {
            "id": "historic-triangle",
            "tier": "power",
            "t": "Forms Virginia’s Historic Triangle with Jamestown and Williamsburg, linked by the Colonial Parkway",
            "k": ["historic triangle", "colonial parkway", "jamestown"],
            "n": 0,
            "rabbit": "Jamestown"
        }
    ],
    "trap": {
        "title": "Yorktown or Saratoga?",
        "body": "Two big Revolutionary War surrenders get mixed up. At Saratoga (1777, New York), John Burgoyne surrendered to Horatio Gates, and that victory convinced France to join the war; at Yorktown (1781, Virginia), Charles Cornwallis surrendered to Washington and the French, which effectively ended the war. Players also blurt out the Battle of the Chesapeake, the French naval victory that trapped Cornwallis, or Jamestown, Yorktown’s neighbor in Virginia’s Historic Triangle.",
        "fix": "Burgoyne, Gates, Benedict Arnold, and 1777 mean Saratoga; Cornwallis, Rochambeau, de Grasse, Redoubt No. 10, and 1781 mean Yorktown. If the question asks for “this naval battle,” the answer is the Battle of the Chesapeake (also called the Battle of the Virginia Capes).",
        "line": "Real answer line: Battle of <b><u>Yorktown</u></b> (or Siege of <b><u>Yorktown</u></b>)"
    },
    "tests": {
        "right": [
            "Yorktown",
            "Battle of Yorktown",
            "Siege of Yorktown",
            "Yorktwon",
            "Yorktown, Virginia"
        ],
        "prompt": [
            "Cornwallis's surrender"
        ],
        "wrong": [
            "Saratoga",
            "Jamestown",
            "Trenton",
            "Battle of the Chesapeake",
            "Bunker Hill",
            "Cornwallis",
            "Treaty of Paris"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
