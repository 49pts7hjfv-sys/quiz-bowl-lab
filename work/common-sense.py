import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "common-sense",
    "name": "Common Sense",
    "mono": "CS",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Thomas Paine’s 1776 pamphlet · Made the case for independence",
    "dates": "Published January 10, 1776",
    "briefing": "In January 1776, many colonists still hoped to make peace with King George III. Then an English immigrant named Thomas Paine published a short pamphlet in plain, punchy language, arguing that kings were a bad idea and that America should break away from Britain. Copies were reprinted across the colonies and read aloud in taverns, and six months later Congress declared independence.",
    "answerHtml": "<b><u>Common Sense</u></b> (prompt on <u>Thomas Paine</u>; do not accept “The American Crisis” or “Rights of Man”)",
    "accept": [
        "common sense"
    ],
    "prompt": [
        "thomas paine",
        "paine",
        "tom paine",
        "paines pamphlet",
        "thomas paines pamphlet"
    ],
    "reject": [
        "the american crisis",
        "american crisis",
        "the crisis",
        "crisis",
        "rights of man",
        "the rights of man",
        "age of reason",
        "the age of reason",
        "agrarian justice",
        "plain truth",
        "declaration of independence",
        "thoughts on government",
        "federalist papers",
        "the federalist papers",
        "the federalist",
        "letters from a farmer in pennsylvania",
        "poor richards almanack",
        "poor richards almanac",
        "olive branch petition",
        "common sense realism",
        "scottish common sense realism"
    ],
    "mediaPending": True,
    "media": [],
    "wiki": "https://en.wikipedia.org/wiki/Common_Sense",
    "qb": {
        "q": "Common Sense",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "The Loyalist James Chalmers answered this work with a pamphlet titled _Plain Truth_. This work’s author had arrived in Philadelphia just over a year before it appeared, carrying a letter of introduction from Benjamin Franklin.",
            "r": "For 10 points, name this January 1776 pamphlet in which Thomas Paine argued for American independence."
        },
        {
            "p": "The Scottish-born printer Robert Bell published the first edition of this work, but its author quarreled with him over the profits and took an expanded edition, with an added appendix, to other printers.",
            "r": "For 10 points, name this pamphlet, first published without its author’s name in 1776, in which Thomas Paine urged the colonies to break from Britain."
        },
        {
            "p": "This work pointed to the Old Testament stories of Gideon, who refused to become king, and of the Israelites who demanded that the prophet Samuel give them a king. Its section “Of Monarchy and Hereditary Succession” attacked the idea of passing a crown from parent to child.",
            "r": "For 10 points, name this January 1776 pamphlet in which Thomas Paine urged the colonies to declare independence."
        },
        {
            "p": "This work proposed a “Continental Charter” and a national congress whose president would come from a colony chosen by lot. It also argued that it was absurd for a continent to be ruled forever by an island.",
            "r": "For 10 points, name this pamphlet published in January 1776 by Thomas Paine, who argued for American independence."
        },
        {
            "p": "John Adams disliked this work’s plan for a one-house legislature and wrote _Thoughts on Government_ partly in response. Even so, Adams admitted that its case for independence summed up arguments he had been making in Congress for months.",
            "r": "For 10 points, name this best-selling pamphlet that Thomas Paine published in January 1776 to argue for independence."
        },
        {
            "p": "This work mocked King George III as the “Royal Brute of Britain” and argued that any peace deal with Britain would only leave the quarrel for the next generation. Its author declared that “the cause of America is in a great measure the cause of all mankind.”",
            "r": "For 10 points, name this 1776 pamphlet by Thomas Paine that pushed the colonies toward independence."
        },
        {
            "p": "This work opens by contrasting society with government, calling society “a blessing” but government, “even in its best state,” only “a necessary evil.” That first section also criticized Britain’s constitution, with its mix of king, lords, and commons. Later, it tells readers that “’Tis time to part.”",
            "r": "For 10 points, name this January 1776 pamphlet in which Thomas Paine called for independence from Britain."
        },
        {
            "p": "This work’s author declared that “we have it in our power to begin the world over again” and argued that the colonies could build a navy of their own. Its fourth section discussed America’s present ability to defend itself.",
            "r": "For 10 points, name this 1776 pamphlet by Thomas Paine that called for independence from Britain."
        },
        {
            "p": "In a letter written three weeks after this work appeared, George Washington praised its “sound doctrine and unanswerable reasoning.” Copies of this work were read aloud in taverns and passed from hand to hand across the colonies.",
            "r": "For 10 points, name this pamphlet published in January 1776 by Thomas Paine."
        },
        {
            "p": "Before writing this work, its author had worked in England as a corset maker and as a tax collector, and he had written a pamphlet asking Parliament to raise the pay of tax officers. He published this work without his name on it.",
            "r": "For 10 points, name this pamphlet by Thomas Paine that argued for American independence in January 1776."
        },
        {
            "p": "By some estimates, more than 100,000 copies of this work were sold in 1776, though historians disagree about the exact number. It was written in plain language so that ordinary farmers and workers could follow its arguments.",
            "r": "For 10 points, name this pamphlet by Thomas Paine that argued for independence from Britain."
        },
        {
            "p": "This work’s author later defended the French Revolution against Edmund Burke in _Rights of Man_ and promoted deism in _The Age of Reason_. During the Reign of Terror, he was jailed in Paris until James Monroe helped free him.",
            "r": "For 10 points, name this 1776 pamphlet, the first famous work of Thomas Paine."
        },
        {
            "p": "Months after writing this work, its author began a series of essays that opens “These are the times that try men’s souls,” which George Washington had read to his troops shortly before the Battle of Trenton.",
            "r": "That series was _The American Crisis_. For 10 points, name this earlier 1776 pamphlet by Thomas Paine."
        },
        {
            "p": "The physician Benjamin Rush encouraged a recent English immigrant to write this work and suggested its title. It first appeared without the author’s name, and some readers guessed it had been written by John Adams or Benjamin Franklin.",
            "r": "For 10 points, name this pamphlet that Thomas Paine published in January 1776."
        },
        {
            "p": "This work insisted that “Europe, and not England, is the parent country of America,” and it warned that ties to Britain kept dragging the colonies into Europe’s wars. Its author urged the colonies to declare independence months before Congress did.",
            "r": "For 10 points, name this pamphlet by Thomas Paine, published on January 10, 1776."
        }
    ],
    "clues": [
        {
            "id": "paine",
            "tier": "giveaway",
            "t": "Written by Thomas Paine, an English immigrant who had arrived in Philadelphia in 1774",
            "k": ["thomas paine", "paine", "1774"],
            "n": 0
        },
        {
            "id": "january-1776",
            "tier": "giveaway",
            "t": "Published in Philadelphia on January 10, 1776, half a year before the Declaration of Independence",
            "k": ["january 10", "1776", "philadelphia"],
            "n": 0
        },
        {
            "id": "independence",
            "tier": "giveaway",
            "t": "Argued in plain language that the colonies should break away from Britain and declare independence",
            "k": ["independence", "plain language", "britain"],
            "n": 0
        },
        {
            "id": "best-seller",
            "tier": "giveaway",
            "t": "A short pamphlet and a huge best-seller (by some estimates, more than 100,000 copies in 1776), often read aloud in taverns",
            "k": ["pamphlet", "best-seller", "taverns"],
            "n": 0
        },
        {
            "id": "monarchy",
            "tier": "middle",
            "t": "Attacked monarchy and hereditary succession, the idea of passing a crown from parent to child",
            "k": ["monarchy", "hereditary succession", "hereditary"],
            "n": 0
        },
        {
            "id": "royal-brute",
            "tier": "middle",
            "t": "Called King George III the “Royal Brute of Britain”",
            "k": ["royal brute", "george iii", "brute"],
            "n": 0
        },
        {
            "id": "island",
            "tier": "middle",
            "t": "Said it was absurd for a continent to be ruled forever by an island",
            "k": ["island", "continent", "absurd"],
            "n": 0
        },
        {
            "id": "anonymous",
            "tier": "middle",
            "t": "First published anonymously by the printer Robert Bell; some readers guessed John Adams or Benjamin Franklin wrote it",
            "k": ["anonymously", "robert bell", "printer"],
            "n": 0
        },
        {
            "id": "rush",
            "tier": "middle",
            "t": "The physician Benjamin Rush encouraged Paine to write it and suggested the title",
            "k": ["benjamin rush", "rush", "title"],
            "n": 0
        },
        {
            "id": "necessary-evil",
            "tier": "middle",
            "t": "Society is “a blessing,” but government “even in its best state is but a necessary evil”",
            "k": ["necessary evil", "blessing", "best state"],
            "n": 0
        },
        {
            "id": "mankind",
            "tier": "middle",
            "t": "“The cause of America is in a great measure the cause of all mankind”",
            "k": ["cause of all mankind", "mankind", "cause of america"],
            "n": 0
        },
        {
            "id": "washington-praise",
            "tier": "middle",
            "t": "George Washington praised its “sound doctrine and unanswerable reasoning” (January 1776)",
            "k": ["sound doctrine", "unanswerable reasoning", "washington"],
            "n": 0
        },
        {
            "id": "american-crisis",
            "tier": "middle",
            "t": "Paine’s later series _The American Crisis_ (“These are the times that try men’s souls”) was read to Washington’s troops before Trenton",
            "k": ["american crisis", "try men’s souls", "trenton"],
            "n": 0,
            "rabbit": "Battle of Trenton"
        },
        {
            "id": "begin-the-world",
            "tier": "power",
            "t": "“We have it in our power to begin the world over again”; argued the colonies could build their own navy",
            "k": ["begin the world over again", "navy"],
            "n": 0
        },
        {
            "id": "time-to-part",
            "tier": "power",
            "t": "Urged readers that “’Tis time to part” from Britain",
            "k": ["time to part"],
            "n": 0
        },
        {
            "id": "sections",
            "tier": "power",
            "t": "Sections include “Of Monarchy and Hereditary Succession” and “Thoughts on the Present State of American Affairs”",
            "k": ["of monarchy", "thoughts on the present state", "american affairs"],
            "n": 0
        },
        {
            "id": "gideon-samuel",
            "tier": "power",
            "t": "Used Old Testament stories (Gideon refusing a crown; the Israelites demanding a king from Samuel) against monarchy",
            "k": ["gideon", "samuel", "old testament", "israelites"],
            "n": 0
        },
        {
            "id": "continental-charter",
            "tier": "power",
            "t": "Proposed a “Continental Charter” and a congress whose president came from a colony chosen by lot",
            "k": ["continental charter", "chosen by lot", "charter"],
            "n": 0
        },
        {
            "id": "parent-country",
            "tier": "power",
            "t": "“Europe, and not England, is the parent country of America”; ties to Britain dragged the colonies into Europe’s wars",
            "k": ["parent country", "europe", "wars"],
            "n": 0
        },
        {
            "id": "bell-quarrel",
            "tier": "power",
            "t": "Paine quarreled with Robert Bell over profits and took an expanded edition, with an appendix, to other printers",
            "k": ["quarreled", "profits", "expanded edition", "appendix"],
            "n": 0
        },
        {
            "id": "chalmers",
            "tier": "power",
            "t": "The Loyalist James Chalmers answered it with the pamphlet _Plain Truth_",
            "k": ["james chalmers", "chalmers", "plain truth", "loyalist"],
            "n": 0
        },
        {
            "id": "adams-thoughts",
            "tier": "power",
            "t": "John Adams disliked its plan for a one-house legislature and wrote _Thoughts on Government_ partly in response",
            "k": ["john adams", "thoughts on government", "one-house"],
            "n": 0,
            "rabbit": "John Adams"
        },
        {
            "id": "franklin-letter",
            "tier": "power",
            "t": "Paine came to Philadelphia in 1774 with a letter of introduction from Benjamin Franklin",
            "k": ["benjamin franklin", "franklin", "letter of introduction"],
            "n": 0
        },
        {
            "id": "excise",
            "tier": "power",
            "t": "In England, Paine had been a corset maker and an excise (tax) officer who wrote a pamphlet asking for better pay for tax officers",
            "k": ["corset", "excise", "tax officer"],
            "n": 0
        },
        {
            "id": "later-works",
            "tier": "power",
            "t": "Paine later wrote _Rights of Man_ (defending the French Revolution against Edmund Burke) and _The Age of Reason_ (deism)",
            "k": ["rights of man", "edmund burke", "age of reason", "deism"],
            "n": 0
        },
        {
            "id": "monroe-prison",
            "tier": "power",
            "t": "During the Reign of Terror, Paine was jailed in Paris until James Monroe helped free him (1794)",
            "k": ["reign of terror", "james monroe", "jailed"],
            "n": 0
        }
    ],
    "trap": {
        "title": "The pamphlet, not the author",
        "body": "The answer is the pamphlet, not the man who wrote it. Thomas Paine also wrote _The American Crisis_ (December 1776, “These are the times that try men’s souls”), _Rights of Man_ (1791), and _The Age of Reason_ (1790s), so clues about his later life can sneak into these tossups. Don’t confuse it with the Declaration of Independence, either: Paine’s pamphlet came out six months earlier and argued for independence; it did not declare it.",
        "fix": "If you hear January 1776, Robert Bell, Benjamin Rush, the “Royal Brute of Britain,” or an island ruling a continent, say the title. On this site, “Thomas Paine” earns a prompt, but in a real match a moderator may simply rule the author wrong, so always name the pamphlet.",
        "line": "Real answer line: <b><u>Common Sense</u></b> (do not accept “The American Crisis” or “Rights of Man”)"
    },
    "tests": {
        "right": [
            "Common Sense",
            "common sence",
            "Commonsense",
            "Common Sense by Thomas Paine",
            "Thomas Paine's Common Sense"
        ],
        "prompt": [
            "Thomas Paine",
            "Paine"
        ],
        "wrong": [
            "The American Crisis",
            "Rights of Man",
            "The Age of Reason",
            "Declaration of Independence",
            "Plain Truth",
            "The Federalist Papers",
            "Thoughts on Government"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
