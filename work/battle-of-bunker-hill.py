import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "battle-of-bunker-hill",
    "name": "Battle of Bunker Hill",
    "mono": "BKH",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Costly British win near Boston, 1775 · Famous for “the whites of their eyes”",
    "dates": "Fought June 17, 1775",
    "briefing": "On the night of June 16, 1775, colonial militiamen secretly dug earthworks on Breed’s Hill, overlooking Boston from the Charlestown peninsula; the battle is named for nearby Bunker Hill. The next day, British troops under General William Howe charged up the hill three times. The colonists drove back the first two attacks and retreated only when their gunpowder ran low, and the British won the hill at a cost of more than 1,000 casualties.",
    "answerHtml": "Battle of <b><u>Bunker Hill</u></b> (or Battle of <b><u>Breed’s Hill</u></b>; prompt on Siege of <u>Boston</u>)",
    "accept": [
        "bunker hill",
        "battle of bunker hill",
        "the battle of bunker hill",
        "bunkers hill",
        "battle of bunkers hill",
        "breeds hill",
        "battle of breeds hill",
        "breed hill",
        "battle of breed hill"
    ],
    "prompt": [
        "siege of boston",
        "the siege of boston",
        "boston campaign",
        "charlestown",
        "battle of charlestown"
    ],
    "reject": [
        "bunker hill monument",
        "the bunker hill monument",
        "lexington and concord",
        "battles of lexington and concord",
        "battle of lexington",
        "lexington",
        "concord",
        "boston massacre",
        "boston tea party",
        "dorchester heights",
        "fortification of dorchester heights",
        "dorchester",
        "battle of saratoga",
        "saratoga",
        "battle of trenton",
        "trenton",
        "battle of yorktown",
        "yorktown",
        "fort ticonderoga",
        "ticonderoga",
        "battle of long island",
        "long island",
        "battle of brooklyn",
        "battle of quebec",
        "american revolutionary war",
        "revolutionary war",
        "american revolution",
        "copps hill",
        "battle of chelsea creek"
    ],
    "mediaPending": True,
    "media": [],
    "wiki": "https://en.wikipedia.org/wiki/Battle_of_Bunker_Hill",
    "qb": {
        "q": "Bunker Hill",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "At dawn, the British warship HMS _Lively_ opened fire on earthworks that colonists had secretly built overnight, starting the day of this battle. Colonel William Prescott commanded the men inside that earthen fort, called a redoubt.",
            "r": "For 10 points, name this June 1775 battle on the Charlestown peninsula, a costly British victory near Boston."
        },
        {
            "p": "Abigail Adams and her seven-year-old son, John Quincy, watched the smoke rising from burning Charlestown during this battle from Penn’s Hill, near their home in Braintree, Massachusetts. The next day, Abigail wrote to her husband that their dear friend Dr. Joseph Warren had been killed in this battle.",
            "r": "British troops under General William Howe won this battle only after three attacks. For 10 points, name this June 1775 battle near Boston."
        },
        {
            "p": "Daniel Webster gave speeches at both the 1825 cornerstone ceremony and the 1843 dedication of a granite obelisk honoring this battle. That 221-foot monument is the last stop on Boston’s Freedom Trail.",
            "r": "For 10 points, name this battle fought on June 17, 1775, in which colonial militia twice drove back British attacks near Boston."
        },
        {
            "p": "When the Marquis de Lafayette died in 1834, he was buried in Paris under soil he had taken home from the site of this battle. Nine years earlier, he had laid the cornerstone of a monument there during his farewell tour of the United States.",
            "r": "For 10 points, name this 1775 battle near Boston, where colonial militia drove back two British attacks before retreating."
        },
        {
            "p": "Fourteen officers signed a petition praising Salem Poor, a free Black soldier, for his bravery in this battle. Another Black soldier, Peter Salem, was credited with shooting the British major John Pitcairn during this battle.",
            "r": "For 10 points, name this June 1775 battle in which colonists defended a hill across the river from Boston."
        },
        {
            "p": "Months after this battle, Paul Revere identified the remains of his friend Joseph Warren, who had been killed in it, by recognizing a false tooth that Revere had made for him.",
            "r": "For 10 points, name this June 1775 battle where the colonists ran low on gunpowder and retreated after three British attacks."
        },
        {
            "p": "New Hampshire troops under John Stark lined a rail fence and a narrow beach along the Mystic River to stop British light infantry from getting around the colonists’ flank in this battle, and the light infantry fell back after heavy losses.",
            "r": "Colonel William Prescott commanded the colonists’ main earthwork. For 10 points, name this June 1775 battle on the Charlestown peninsula."
        },
        {
            "p": "During this battle, British cannon fire from ships and from Copp’s Hill in Boston set the nearby town of Charlestown on fire, because colonial snipers had been shooting from its buildings.",
            "r": "General William Howe’s troops finally took the colonists’ earthwork on their third attack. For 10 points, name this June 1775 battle."
        },
        {
            "p": "Two days before this battle, the Second Continental Congress named George Washington commander of the Continental Army, so he was not present. Artemas Ward commanded the colonial army around Boston at the time.",
            "r": "For 10 points, name this battle fought near Boston on June 17, 1775, two months after Lexington and Concord."
        },
        {
            "p": "Either Israel Putnam or William Prescott is said to have given a famous order in this battle, telling the colonists to save their scarce gunpowder by holding their fire until the enemy came very close.",
            "r": "That order was “Don’t fire until you see the whites of their eyes!” For 10 points, name this June 1775 battle."
        },
        {
            "p": "After this battle’s heavy losses, General Thomas Gage was called home, and the general who had led the attack replaced him as the British commander in America. Gage had sent troops into this battle after colonists fortified the heights across the river from Boston overnight.",
            "r": "That general was William Howe. For 10 points, name this June 1775 battle on the Charlestown peninsula."
        },
        {
            "p": "Colonists were ordered to fortify one hill on the Charlestown peninsula but built their main earthwork on a lower hill closer to Boston instead, so most of this battle was actually fought there.",
            "r": "This battle is still named for the first hill. For 10 points, name this battle of June 17, 1775."
        },
        {
            "p": "Suffolk County, Massachusetts, which includes Boston, marks a legal holiday every June 17 in honor of this battle. At the end of this battle, the colonists retreated across the narrow Charlestown Neck to the mainland.",
            "r": "For 10 points, name this battle near Boston that came two months after the fighting at Lexington and Concord."
        },
        {
            "p": "John Trumbull painted _The Death of General Warren_ at this battle, showing a Patriot leader who had recently been named a general but chose to fight as a volunteer. Warren had sent Paul Revere on his famous ride two months earlier.",
            "r": "For 10 points, name this June 1775 battle near Boston, where William Prescott commanded the colonists’ earthwork."
        },
        {
            "p": "Historians often call the British win in this battle a Pyrrhic [“PIR-ik”] victory, because more than 1,000 British soldiers were killed or wounded while capturing a single hill. The colonists, who lost far fewer men, retreated only when they ran low on gunpowder.",
            "r": "For 10 points, name this battle of June 17, 1775, on the Charlestown peninsula across from Boston."
        }
    ],
    "clues": [
        {
            "id": "june-17",
            "tier": "giveaway",
            "t": "Fought June 17, 1775, on the Charlestown peninsula across the river from Boston",
            "k": ["june 17", "1775", "charlestown"],
            "n": 0
        },
        {
            "id": "lower-hill",
            "tier": "giveaway",
            "t": "Most of the fighting took place on a lower hill closer to Boston, not on the hill the battle is named for",
            "k": ["lower hill", "named for"],
            "n": 0
        },
        {
            "id": "whites-eyes",
            "tier": "giveaway",
            "t": "“Don’t fire until you see the whites of their eyes!” (said to be ordered by Prescott or Putnam)",
            "k": ["whites of their eyes", "whites"],
            "n": 0
        },
        {
            "id": "costly-win",
            "tier": "giveaway",
            "t": "A British victory, but a costly one: more than 1,000 British soldiers killed or wounded",
            "k": ["costly", "1,000", "british victory"],
            "n": 0
        },
        {
            "id": "prescott",
            "tier": "middle",
            "t": "Colonel William Prescott commanded the colonists’ earthwork (a redoubt), built overnight",
            "k": ["prescott", "redoubt", "overnight"],
            "n": 0
        },
        {
            "id": "howe",
            "tier": "middle",
            "t": "General William Howe led the British attacks; only the third succeeded",
            "k": ["william howe", "howe", "third"],
            "n": 0
        },
        {
            "id": "gunpowder",
            "tier": "middle",
            "t": "The colonists retreated after running low on gunpowder",
            "k": ["gunpowder", "retreated"],
            "n": 0
        },
        {
            "id": "warren",
            "tier": "middle",
            "t": "Patriot leader Joseph Warren, recently named a general, was killed fighting as a volunteer",
            "k": ["joseph warren", "warren", "volunteer"],
            "n": 0
        },
        {
            "id": "siege",
            "tier": "middle",
            "t": "Part of the Siege of Boston, two months after Lexington and Concord",
            "k": ["siege of boston", "lexington", "concord"],
            "n": 0,
            "rabbit": "Battles of Lexington and Concord"
        },
        {
            "id": "putnam",
            "tier": "middle",
            "t": "Israel Putnam of Connecticut also led the colonists",
            "k": ["israel putnam", "putnam"],
            "n": 0
        },
        {
            "id": "charlestown-fire",
            "tier": "middle",
            "t": "British cannon fire from ships and from Copp’s Hill in Boston set Charlestown on fire",
            "k": ["copp’s hill", "on fire", "charlestown"],
            "n": 0
        },
        {
            "id": "monument",
            "tier": "middle",
            "t": "A 221-foot granite obelisk marks the site; it is the last stop on Boston’s Freedom Trail",
            "k": ["obelisk", "freedom trail", "221"],
            "n": 0
        },
        {
            "id": "lively",
            "tier": "power",
            "t": "At dawn, the British warship HMS _Lively_ fired on the colonists’ new earthworks",
            "k": ["lively", "dawn", "warship"],
            "n": 0
        },
        {
            "id": "salem",
            "tier": "power",
            "t": "Peter Salem, a Black soldier, was credited with shooting Major John Pitcairn; 14 officers praised Salem Poor’s bravery",
            "k": ["peter salem", "pitcairn", "salem poor"],
            "n": 0
        },
        {
            "id": "revere-tooth",
            "tier": "power",
            "t": "Paul Revere identified Warren’s remains by a false tooth he had made",
            "k": ["paul revere", "revere", "tooth"],
            "n": 0
        },
        {
            "id": "trumbull",
            "tier": "power",
            "t": "John Trumbull painted _The Death of General Warren_",
            "k": ["trumbull", "death of general warren"],
            "n": 0
        },
        {
            "id": "penns-hill",
            "tier": "power",
            "t": "Abigail Adams and seven-year-old John Quincy Adams watched the smoke from Penn’s Hill in Braintree",
            "k": ["abigail adams", "john quincy", "penn’s hill", "braintree"],
            "n": 0
        },
        {
            "id": "webster",
            "tier": "power",
            "t": "Daniel Webster spoke at the monument’s cornerstone ceremony (1825) and its dedication (1843)",
            "k": ["daniel webster", "webster", "1825", "1843"],
            "n": 0
        },
        {
            "id": "lafayette",
            "tier": "power",
            "t": "Lafayette laid the monument’s cornerstone (1825) and was buried in Paris under soil from the battlefield",
            "k": ["lafayette", "soil", "cornerstone"],
            "n": 0
        },
        {
            "id": "stark",
            "tier": "power",
            "t": "John Stark’s New Hampshire men held a rail fence and the Mystic River beach",
            "k": ["john stark", "stark", "rail fence", "mystic river"],
            "n": 0
        },
        {
            "id": "ward",
            "tier": "power",
            "t": "Artemas Ward commanded the colonial army around Boston; Washington had been named commander two days earlier",
            "k": ["artemas ward", "ward", "two days"],
            "n": 0
        },
        {
            "id": "gage",
            "tier": "power",
            "t": "General Thomas Gage, the British commander in Boston, was replaced by Howe afterward",
            "k": ["thomas gage", "gage", "replaced"],
            "n": 0
        },
        {
            "id": "holiday",
            "tier": "power",
            "t": "Suffolk County, Massachusetts, marks a legal holiday every June 17",
            "k": ["suffolk county", "holiday"],
            "n": 0
        },
        {
            "id": "pyrrhic",
            "tier": "power",
            "t": "Often called a Pyrrhic victory: a win that costs the winner too much",
            "k": ["pyrrhic"],
            "n": 0
        },
        {
            "id": "neck",
            "tier": "power",
            "t": "The colonists retreated across the narrow Charlestown Neck",
            "k": ["charlestown neck", "neck"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Bunker or Breed’s?",
        "body": "This battle is named for Bunker Hill, but most of the fighting happened on Breed’s Hill, a lower hill closer to Boston, so this answer line accepts either name. Players also mix it up with Lexington and Concord (April 1775, the war’s first shots) and with Dorchester Heights (March 1776), where Henry Knox’s cannons forced the British out of Boston.",
        "fix": "June 1775, Charlestown, Prescott, Howe, Joseph Warren, and “the whites of their eyes” mean this battle. Paul Revere’s ride and “the shot heard round the world” mean Lexington and Concord; cannons from Fort Ticonderoga mean Dorchester Heights.",
        "line": "Real answer line: Battle of <b><u>Bunker Hill</u></b> (or Battle of <b><u>Breed’s Hill</u></b>)"
    },
    "tests": {
        "right": [
            "Bunker Hill",
            "Battle of Bunker Hill",
            "Breed's Hill",
            "Battle of Breed's Hill",
            "Bunker Hil",
            "Bunker's Hill"
        ],
        "prompt": [
            "Siege of Boston",
            "Charlestown"
        ],
        "wrong": [
            "Lexington and Concord",
            "Dorchester Heights",
            "Boston Massacre",
            "Battle of Saratoga",
            "Bunker Hill Monument",
            "Yorktown",
            "Battle of Long Island"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", data["id"])
