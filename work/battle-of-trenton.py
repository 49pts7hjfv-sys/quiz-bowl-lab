import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "battle-of-trenton",
    "name": "Battle of Trenton",
    "mono": "TRN",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Washington’s Christmas-night surprise · Revived the American cause",
    "dates": "Fought December 26, 1776",
    "briefing": "On Christmas night in 1776, George Washington’s ragged army rowed across the ice-choked Delaware River in a freezing storm, then marched nine miles through sleet and snow. On the morning of December 26, they surprised about 1,500 Hessian soldiers at Trenton, New Jersey, and captured nearly 900 of them in less than an hour. After months of defeats, the victory gave the American Revolution new life.",
    "answerHtml": "Battle of <b><u>Trenton</u></b> (prompt on <u>crossing</u> of the <u>Delaware</u>; do not accept “Princeton”)",
    "accept": [
        "trenton",
        "battle of trenton",
        "first battle of trenton",
        "trenton new jersey"
    ],
    "prompt": [
        "crossing of the delaware",
        "crossing the delaware",
        "crossing of the delaware river",
        "delaware crossing",
        "delaware river crossing",
        "washington crossing the delaware",
        "washingtons crossing of the delaware",
        "trenton and princeton",
        "battles of trenton and princeton",
        "ten crucial days"
    ],
    "reject": [
        "princeton",
        "battle of princeton",
        "second battle of trenton",
        "assunpink creek",
        "battle of the assunpink creek",
        "battle of assunpink creek",
        "saratoga",
        "battle of saratoga",
        "yorktown",
        "battle of yorktown",
        "monmouth",
        "battle of monmouth",
        "brandywine",
        "germantown",
        "long island",
        "battle of long island",
        "bunker hill",
        "battle of bunker hill",
        "lexington and concord",
        "valley forge",
        "fort washington",
        "white plains",
        "morristown",
        "the alamo",
        "battle of the alamo"
    ],
    "mediaPending": True,
    "media": [],
    "wiki": "https://en.wikipedia.org/wiki/Battle_of_Trenton",
    "qb": {
        "q": "Trenton",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "On the night before this battle, John Glover’s regiment of Marblehead fishermen ferried troops in big flat-bottomed Durham boats, which had been built to carry iron ore. Henry Knox’s booming voice helped direct that crossing through a storm of sleet and snow.",
            "r": "For 10 points, name this December 26, 1776, battle in which George Washington surprised Hessian soldiers in New Jersey."
        },
        {
            "p": "The army that won this battle set out from McConkey’s Ferry in Pennsylvania. It landed at Johnson’s Ferry, New Jersey, about three hours behind schedule, and then began a nine-mile march through a storm.",
            "r": "The ferry site is now called Washington Crossing. For 10 points, name this battle won after George Washington crossed the Delaware River on Christmas night, 1776."
        },
        {
            "p": "About two weeks before this battle, British cavalry captured the American general Charles Lee at a tavern in Basking Ridge, New Jersey. By then, the American army had lost New York City and retreated across New Jersey, and many soldiers’ enlistments would run out at the end of the year.",
            "r": "For 10 points, name this morale-boosting battle in which George Washington’s army crossed the Delaware and surprised the Hessians."
        },
        {
            "p": "In this battle, Nathanael Greene’s division struck from the north along the Pennington Road while John Sullivan’s division advanced along the River Road. When Sullivan sent word that his men’s muskets were too wet to fire, their commander supposedly replied that they should use the bayonet.",
            "r": "For 10 points, name this December 1776 battle in which George Washington surprised Hessian soldiers in New Jersey."
        },
        {
            "p": "Colonel Johann Rall [“RAHL”] was mortally wounded in this battle while trying to rally his three regiments, which came from the German state of Hesse-Kassel. Nearly 900 of his soldiers were captured in less than an hour.",
            "r": "For 10 points, name this battle that George Washington won the morning after crossing the Delaware River on Christmas night, 1776."
        },
        {
            "p": "Shortly before this battle, its winning commander had his soldiers hear a new essay warning that “the summer soldier and the sunshine patriot” would shrink from serving their country. The password for the night march before this battle was “Victory or Death.”",
            "r": "That essay was Thomas Paine’s _The American Crisis_. For 10 points, name this battle where George Washington surprised the Hessians in December 1776."
        },
        {
            "p": "Captain William Washington and Lieutenant James Monroe were both wounded in this battle while leading a charge that captured two enemy cannons on King Street. Monroe, a future president, is traditionally said to be the man holding the flag in a famous painting of the river crossing before this battle.",
            "r": "For 10 points, name this December 26, 1776, battle in which George Washington defeated the Hessians."
        },
        {
            "p": "A week after this battle, Charles Cornwallis was held off at Assunpink Creek and supposedly boasted that he would “bag” the “old fox” in the morning. His enemy slipped away overnight, leaving campfires burning, and won at Princeton on January 3, 1777.",
            "r": "For 10 points, name this December 1776 battle in New Jersey, where George Washington captured hundreds of Hessians."
        },
        {
            "p": "Emanuel Leutze [“LOYT-suh”] painted the river crossing before this battle while living in Düsseldorf, Germany, and he mistakenly showed a Stars and Stripes flag that was not adopted until 1777. His painting of that crossing hangs in New York’s Metropolitan Museum of Art.",
            "r": "For 10 points, name this December 26, 1776, battle that followed George Washington’s crossing of the Delaware River."
        },
        {
            "p": "New Jersey’s 1999 state quarter, labeled “Crossroads of the Revolution,” shows the river crossing that led to this battle. This battle and a victory at Princeton about a week later formed the heart of the “Ten Crucial Days.”",
            "r": "For 10 points, name this battle in which George Washington surprised Hessian soldiers on December 26, 1776."
        },
        {
            "p": "Two American soldiers died from the cold during the night march before this battle, as a nor’easter pelted the army with sleet and snow. Some of the marchers had no shoes and wrapped their feet in rags.",
            "r": "Their commander, George Washington, had crossed the Delaware River on Christmas night. For 10 points, name this 1776 battle in New Jersey."
        },
        {
            "p": "After this battle, the winning army recrossed the river into Pennsylvania that same day, bringing nearly 900 prisoners along with captured muskets and cannons. Those prisoners were German soldiers whose ruler had rented them to the British army.",
            "r": "Those prisoners were Hessians. For 10 points, name this battle that George Washington won on December 26, 1776."
        },
        {
            "p": "General Hugh Mercer was mortally wounded at a battle fought about a week after this one, and the Americans then went into winter quarters at Morristown, New Jersey. In this earlier battle, about 2,400 Americans attacked at around eight in the morning after a night march of about nine miles.",
            "r": "For 10 points, name this battle in which George Washington surprised the Hessians the morning after Christmas, 1776."
        },
        {
            "p": "Alexander Hamilton, then a young captain, commanded a company of New York artillery in this battle. Henry Knox placed cannons at the head of the town’s two main streets, King and Queen Streets, which fired down on enemy soldiers as they tried to form ranks.",
            "r": "For 10 points, name this battle in which George Washington defeated Hessian soldiers in New Jersey in December 1776."
        },
        {
            "p": "Because ice kept James Ewing’s militia from crossing the river to seize a bridge, several hundred enemy soldiers escaped across Assunpink Creek during this battle. John Cadwalader’s planned crossing farther south also failed.",
            "r": "For 10 points, name this battle in which George Washington captured nearly 900 Hessians after crossing the Delaware on Christmas night, 1776."
        }
    ],
    "clues": [
        {
            "id": "crossing",
            "tier": "giveaway",
            "t": "George Washington crossed the icy Delaware River on Christmas night 1776 to launch this attack",
            "k": ["delaware river", "delaware", "christmas", "crossed"],
            "n": 0,
            "rabbit": "George Washington"
        },
        {
            "id": "hessians",
            "tier": "giveaway",
            "t": "Surprised and captured Hessians, German soldiers hired by the British",
            "k": ["hessians", "hessian", "german"],
            "n": 0
        },
        {
            "id": "date-place",
            "tier": "giveaway",
            "t": "Fought December 26, 1776, in a New Jersey town that is now the state capital",
            "k": ["december 26", "1776", "new jersey"],
            "n": 0
        },
        {
            "id": "morale",
            "tier": "giveaway",
            "t": "A small battle but a huge morale boost after months of American defeats",
            "k": ["morale", "defeats", "boost"],
            "n": 0,
            "rabbit": "American Revolutionary War"
        },
        {
            "id": "rall",
            "tier": "middle",
            "t": "The Hessian commander, Colonel Johann Rall, was mortally wounded",
            "k": ["johann rall", "rall", "colonel"],
            "n": 0
        },
        {
            "id": "victory-or-death",
            "tier": "middle",
            "t": "The Americans’ password for the night march was “Victory or Death”",
            "k": ["victory or death", "password"],
            "n": 0
        },
        {
            "id": "american-crisis",
            "tier": "middle",
            "t": "Washington had Thomas Paine’s _The American Crisis_ (“These are the times that try men’s souls”) read to his troops beforehand",
            "k": ["american crisis", "thomas paine", "paine", "try men’s souls"],
            "n": 0,
            "rabbit": "Common Sense"
        },
        {
            "id": "leutze",
            "tier": "middle",
            "t": "Emanuel Leutze’s 1851 painting shows the crossing; James Monroe is traditionally said to hold the flag",
            "k": ["leutze", "emanuel leutze", "1851", "painting"],
            "n": 0
        },
        {
            "id": "princeton",
            "tier": "middle",
            "t": "About a week later, Washington won again at Princeton (January 3, 1777)",
            "k": ["princeton", "january 3", "1777"],
            "n": 0
        },
        {
            "id": "glover",
            "tier": "middle",
            "t": "John Glover’s regiment of Marblehead fishermen rowed the boats across the river",
            "k": ["john glover", "glover", "marblehead"],
            "n": 0
        },
        {
            "id": "captured",
            "tier": "middle",
            "t": "Nearly 900 Hessians were captured in less than an hour; only a handful of Americans were wounded",
            "k": ["900", "captured", "less than an hour"],
            "n": 0
        },
        {
            "id": "monroe",
            "tier": "middle",
            "t": "James Monroe and William Washington were wounded leading a charge that captured two Hessian cannons",
            "k": ["james monroe", "monroe", "william washington"],
            "n": 0,
            "rabbit": "James Monroe"
        },
        {
            "id": "knox",
            "tier": "power",
            "t": "Henry Knox directed the crossing with his booming voice and aimed cannons down King and Queen Streets",
            "k": ["henry knox", "knox", "booming voice", "king and queen streets"],
            "n": 0,
            "rabbit": "Henry Knox"
        },
        {
            "id": "durham",
            "tier": "power",
            "t": "The troops crossed in Durham boats, big flat-bottomed boats built to haul iron ore",
            "k": ["durham boats", "durham", "iron ore"],
            "n": 0
        },
        {
            "id": "mcconkey",
            "tier": "power",
            "t": "They crossed from McConkey’s Ferry, Pennsylvania (now Washington Crossing), to Johnson’s Ferry, New Jersey, about three hours late",
            "k": ["mcconkey", "johnson’s ferry", "johnsons ferry", "washington crossing"],
            "n": 0
        },
        {
            "id": "ewing-cadwalader",
            "tier": "power",
            "t": "Ice stopped two other crossings, by James Ewing and John Cadwalader, so some Hessians escaped over Assunpink Creek",
            "k": ["ewing", "cadwalader", "ice"],
            "n": 0
        },
        {
            "id": "columns",
            "tier": "power",
            "t": "Two columns attacked: Nathanael Greene’s on the Pennington Road and John Sullivan’s on the River Road (“use the bayonet”)",
            "k": ["nathanael greene", "john sullivan", "two columns", "bayonet"],
            "n": 0
        },
        {
            "id": "storm",
            "tier": "power",
            "t": "A nor’easter brought sleet and snow; two Americans died from the cold on the march",
            "k": ["nor’easter", "noreaster", "sleet", "cold"],
            "n": 0
        },
        {
            "id": "hamilton",
            "tier": "power",
            "t": "Captain Alexander Hamilton commanded a company of New York artillery",
            "k": ["alexander hamilton", "hamilton", "artillery"],
            "n": 0,
            "rabbit": "Alexander Hamilton"
        },
        {
            "id": "charles-lee",
            "tier": "power",
            "t": "About two weeks earlier, British cavalry captured General Charles Lee at a tavern in Basking Ridge, New Jersey",
            "k": ["charles lee", "basking ridge", "tavern"],
            "n": 0
        },
        {
            "id": "old-fox",
            "tier": "power",
            "t": "A week later, Cornwallis was held off at Assunpink Creek and supposedly planned to “bag” the “old fox,” but Washington slipped away, leaving campfires burning",
            "k": ["old fox", "assunpink", "campfires", "cornwallis"],
            "n": 0
        },
        {
            "id": "ten-crucial-days",
            "tier": "power",
            "t": "The heart of the “Ten Crucial Days” (December 25, 1776–January 3, 1777)",
            "k": ["ten crucial days", "crucial"],
            "n": 0
        },
        {
            "id": "mercer",
            "tier": "power",
            "t": "General Hugh Mercer was mortally wounded at Princeton; the army then wintered at Morristown",
            "k": ["hugh mercer", "mercer", "morristown"],
            "n": 0
        },
        {
            "id": "nj-quarter",
            "tier": "power",
            "t": "New Jersey’s 1999 state quarter (“Crossroads of the Revolution”) shows the crossing",
            "k": ["quarter", "crossroads of the revolution", "1999"],
            "n": 0
        },
        {
            "id": "leutze-details",
            "tier": "power",
            "t": "Leutze painted it in Düsseldorf, Germany; its Stars and Stripes flag is a mistake (adopted 1777); it hangs in the Metropolitan Museum of Art",
            "k": ["dusseldorf", "metropolitan museum", "stars and stripes"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Trenton or Princeton?",
        "body": "George Washington won two surprise victories in New Jersey about a week apart: Trenton on December 26, 1776, where he captured Hessians after crossing the Delaware, and Princeton on January 3, 1777, where he beat British troops after slipping away from Cornwallis. In between came a second fight at Trenton, at Assunpink Creek on January 2. The password “Victory or Death” can trick you too: William Travis signed his famous 1836 letter from the Alamo with the same words.",
        "fix": "Christmas night, the Delaware crossing, Hessians, Johann Rall, and Durham boats mean Trenton. Hugh Mercer’s death and campfires left burning to fool Cornwallis mean Princeton. If you only say “crossing the Delaware,” expect a prompt, because the moderator wants the battle.",
        "line": "Real answer line: Battle of <b><u>Trenton</u></b> (prompt on <u>crossing</u> of the <u>Delaware</u>; do not accept “Princeton”)"
    },
    "tests": {
        "right": [
            "Trenton",
            "Battle of Trenton",
            "Trenton, New Jersey",
            "Trentin",
            "first Battle of Trenton"
        ],
        "prompt": [
            "crossing of the Delaware",
            "Washington Crossing the Delaware"
        ],
        "wrong": [
            "Princeton",
            "Second Battle of Trenton",
            "Saratoga",
            "Yorktown",
            "Valley Forge",
            "Long Island",
            "Assunpink Creek"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
