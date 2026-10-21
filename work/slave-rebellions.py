import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

data = {
    "id": "slave-rebellions",
    "name": "Slave rebellions",
    "mono": "SR",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Enslaved people taking up arms for freedom · Stono, Vesey, Nat Turner",
    "dates": "Major U.S. examples, 1739–1841",
    "briefing": "Enslaved people resisted slavery in many ways, and sometimes they took up arms. In 1739, men near South Carolina’s Stono River marched toward Spanish Florida, which promised them freedom, and in 1831 the preacher Nat Turner led a revolt in Virginia that terrified slaveholders, who answered with harsher laws. The most successful began in 1791 in Haiti, where formerly enslaved people won their independence in 1804.",
    "answerHtml": "<b><u>slave rebellions</u></b> (or slave <u>revolts</u>, <u>uprisings</u>, or <u>insurrections</u>; prompt on <u>rebellions</u> or <u>revolts</u> alone)",
    "accept": [
        "slave rebellions",
        "slave rebellion",
        "slave revolts",
        "slave revolt",
        "slave uprisings",
        "slave uprising",
        "slave insurrections",
        "slave insurrection",
        "rebellions of enslaved people",
        "rebellion of enslaved people",
        "revolts of enslaved people",
        "revolt of enslaved people",
        "uprisings of enslaved people",
        "uprising of enslaved people"
    ],
    "prompt": [
        "rebellions",
        "rebellion",
        "revolts",
        "revolt",
        "uprisings",
        "uprising",
        "insurrections",
        "insurrection",
        "slave resistance",
        "resistance to slavery",
        "armed resistance"
    ],
    "reject": [
        "nat turners rebellion",
        "turners rebellion",
        "southampton insurrection",
        "stono rebellion",
        "gabriels rebellion",
        "german coast uprising",
        "haitian revolution",
        "john browns raid",
        "raid on harpers ferry",
        "underground railroad",
        "united states v the amistad",
        "shays rebellion",
        "whiskey rebellion",
        "bacons rebellion",
        "peasants revolt",
        "abolition",
        "abolitionism",
        "abolitionists",
        "emancipation",
        "fugitive slave act"
    ],
    "tests": {
        "right": [
            "slave rebellions",
            "Slave revolt",
            "slave uprisings",
            "slave insurrection",
            "slave rebelions"
        ],
        "prompt": [
            "rebellions",
            "revolt"
        ],
        "wrong": [
            "Nat Turner's Rebellion",
            "Shays' Rebellion",
            "Haitian Revolution",
            "Underground Railroad",
            "John Brown's raid",
            "Whiskey Rebellion"
        ]
    },
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Slave_rebellion",
    "qb": {
        "q": "slave revolt",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Many of the men who took part in one of these events are thought to have come from the Kingdom of Kongo in Central Africa, and their leader was a man named Jemmy. In 1739, they seized guns from a store and marched south, beating drums and calling out “Liberty!”",
            "r": "That event began near the Stono River in South Carolina. For 10 points, name these events in which enslaved people took up arms for their freedom."
        },
        {
            "p": "South Carolina’s Negro Act of 1740, which banned enslaved people from gathering in groups and made it illegal to teach them to write, was a response to one of these events. People in that event were heading for Spanish Florida, where the town of Fort Mose [“MOH-say”] near St. Augustine sheltered people who had escaped slavery in the Carolinas.",
            "r": "For 10 points, name these events, like the one near the Stono River in 1739, in which enslaved people fought for their freedom."
        },
        {
            "p": "One of these events was to be fought under a banner reading “Death or Liberty,” but on the planned night in August 1800, a huge storm washed out roads and bridges near Richmond. Two men revealed the plan to their enslaver, and Governor James Monroe called out the militia.",
            "r": "Its leader was a blacksmith named Gabriel. For 10 points, name these events, such as Nat Turner’s in 1831, in which enslaved people took up arms."
        },
        {
            "p": "After a plan to capture Richmond fell apart, the leader of one of these events escaped on a ship sailing down the James River, but he was turned in and captured at Norfolk. That leader, a blacksmith enslaved on Thomas Prosser’s plantation, was executed along with about two dozen of his followers in 1800.",
            "r": "For 10 points, name these events, also including Denmark Vesey’s planned one and Nat Turner’s, in which enslaved people fought for freedom."
        },
        {
            "p": "In January 1811, Charles Deslondes [“day-LOHND”] led hundreds of people down the Mississippi River toward New Orleans in the largest of these events in U.S. history. Militia and U.S. Army troops stopped the marchers on a stretch of plantations called the German Coast, in the Territory of Orleans.",
            "r": "That territory became the state of Louisiana the next year. For 10 points, name these events, such as Nat Turner’s in Virginia, in which enslaved people took up arms."
        },
        {
            "p": "A man who won 1,500 dollars in a city lottery used part of it to buy his freedom, then worked for years as a carpenter in Charleston before planning one of these events. He hoped his followers could later sail to Haiti, but informers revealed the plan in 1822 before it began.",
            "r": "That man was Denmark Vesey. For 10 points, name these events, such as Nat Turner’s in 1831, in which enslaved people fought for their freedom."
        },
        {
            "p": "After one of these events was uncovered in 1822, Charleston’s African Methodist Episcopal church was destroyed, and South Carolina began jailing free Black sailors whenever their ships were in port. That church’s congregation later rebuilt as Emanuel AME, known as “Mother Emanuel.”",
            "r": "Denmark Vesey had planned that event. For 10 points, name these events in which enslaved people took up arms, including Nat Turner’s in Virginia."
        },
        {
            "p": "Lawyer Thomas R. Gray interviewed the leader of one of these events in jail and published the leader’s “confessions” as a pamphlet in 1831. In 1968, William Styron won a Pulitzer Prize for a novel that retold the same story in the leader’s own voice.",
            "r": "That leader was Nat Turner. For 10 points, name these events, also including Denmark Vesey’s planned one in Charleston, in which enslaved people took up arms."
        },
        {
            "p": "A solar eclipse in February 1831 convinced a preacher that God was signaling him to prepare for one of these events. After it was put down, that preacher hid for about two months near the farm where he had lived before he was captured, tried, and executed.",
            "r": "The event took place in Southampton County, Virginia. For 10 points, name these events, such as the one led by Nat Turner, in which enslaved people fought for their freedom."
        },
        {
            "p": "In 1832, Virginia’s legislature debated a plan to slowly end slavery in the state after one of these events, but it chose harsher laws instead, including new limits on Black preachers and church meetings. Southern leaders blamed William Lloyd Garrison’s new newspaper, _The Liberator_, for stirring up such events.",
            "r": "That 1831 event was led by Nat Turner. For 10 points, name these events in which enslaved people took up arms against their enslavers."
        },
        {
            "p": "Yale professor Josiah Gibbs found an interpreter for the people involved in one of these events by walking New York’s docks and counting aloud in their Mende language. Those people had taken control of a Spanish schooner off Cuba in 1839 and were captured off Long Island.",
            "r": "John Quincy Adams helped win their freedom. For 10 points, name these events, such as the one aboard the _Amistad_, in which enslaved people fought for freedom."
        },
        {
            "p": "Justice Joseph Story wrote an 1841 Supreme Court decision that freed the survivors of one of these events, and they sailed home to Sierra Leone the next year. Their leader, Sengbe Pieh, was known in the United States as Joseph Cinqué [“sin-KAY”].",
            "r": "Their ship was the _Amistad_. For 10 points, name these events, also including Nat Turner’s, in which enslaved people took up arms for their freedom."
        },
        {
            "p": "In 1841, Madison Washington led one of these events aboard the _Creole_, a ship carrying people from Virginia to be sold in New Orleans. The ship then sailed to Nassau in the British Bahamas, where most of the people aboard were freed because Britain had ended slavery in its colonies.",
            "r": "Frederick Douglass later wrote a novella about Madison Washington. For 10 points, name these events, such as the one on the _Amistad_, in which enslaved people seized their freedom."
        },
        {
            "p": "One of these events began in the French colony of Saint-Domingue [“san doh-MANG”] in 1791 and frightened enslavers in the United States for decades. Napoleon’s failure to win back that colony led him to sell Louisiana, and after Toussaint Louverture [“too-SAN loo-vair-TOOR”] died in a French prison, Jean-Jacques Dessalines [“deh-sah-LEEN”] declared independence in 1804.",
            "r": "For 10 points, name these events in which enslaved people took up arms, one of which created the nation of Haiti."
        },
        {
            "p": "In 1843, Henry Highland Garnet told a convention in Buffalo, “Let your motto be resistance!” Years earlier, David Walker’s _Appeal_ had urged enslaved Americans to fight back, and in 1859 John Brown hoped his raid on Harpers Ferry would spark a huge one of these events.",
            "r": "For 10 points, name these events, such as Gabriel’s planned one in 1800 and Nat Turner’s in 1831, in which enslaved people took up arms for their freedom."
        }
    ],
    "clues": [
        {
            "id": "definition",
            "tier": "giveaway",
            "t": "Events in which enslaved people took up arms to fight for their freedom",
            "k": ["took up arms", "enslaved", "freedom"],
            "n": 0
        },
        {
            "id": "nat-turner",
            "tier": "giveaway",
            "t": "Nat Turner led the most famous U.S. example, in Southampton County, Virginia, in 1831",
            "k": ["nat turner", "southampton", "1831"],
            "n": 0,
            "rabbit": "Nat Turner"
        },
        {
            "id": "amistad",
            "tier": "giveaway",
            "t": "_Amistad_ (1839): captive Africans led by Sengbe Pieh (Cinqué) took over a Spanish ship; the Supreme Court freed them in 1841",
            "k": ["amistad", "cinqué", "sengbe pieh"],
            "n": 0,
            "rabbit": "John Quincy Adams"
        },
        {
            "id": "haiti",
            "tier": "giveaway",
            "t": "The Haitian Revolution (1791–1804) began when enslaved people rose up and ended with Haiti’s independence",
            "k": ["haitian revolution", "haiti", "independence"],
            "n": 0,
            "rabbit": "Haitian Revolution"
        },
        {
            "id": "stono",
            "tier": "middle",
            "t": "Stono (1739): the largest in the thirteen colonies; enslaved men near Charleston, South Carolina, marched toward Spanish Florida",
            "k": ["stono", "spanish florida", "1739"],
            "n": 0
        },
        {
            "id": "gabriel",
            "tier": "middle",
            "t": "Gabriel (1800): an enslaved blacksmith planned to seize Richmond, Virginia; a storm and informers stopped the plan",
            "k": ["gabriel", "blacksmith", "richmond"],
            "n": 0
        },
        {
            "id": "german-coast",
            "tier": "middle",
            "t": "German Coast (1811): Charles Deslondes led hundreds toward New Orleans, the largest in U.S. history",
            "k": ["german coast", "deslondes", "new orleans", "1811"],
            "n": 0
        },
        {
            "id": "vesey",
            "tier": "middle",
            "t": "Denmark Vesey (1822): a free Black carpenter in Charleston who bought his freedom with lottery winnings and hoped to sail to Haiti; informers exposed his plan",
            "k": ["denmark vesey", "vesey", "lottery", "charleston"],
            "n": 0,
            "rabbit": "Denmark Vesey"
        },
        {
            "id": "eclipse",
            "tier": "middle",
            "t": "Nat Turner, an enslaved preacher, took a February 1831 solar eclipse as a sign from God",
            "k": ["eclipse", "preacher", "sign"],
            "n": 0
        },
        {
            "id": "confessions",
            "tier": "middle",
            "t": "Thomas R. Gray published _The Confessions of Nat Turner_ (1831); William Styron’s 1967 novel of the same name won a Pulitzer Prize",
            "k": ["confessions", "gray", "styron", "pulitzer"],
            "n": 0
        },
        {
            "id": "harsher-laws",
            "tier": "middle",
            "t": "Afterward, Southern states passed harsher laws, and after Nat Turner’s, white mobs killed many Black people who had no part in it",
            "k": ["harsher laws", "white mobs", "backlash"],
            "n": 0
        },
        {
            "id": "jqa",
            "tier": "middle",
            "t": "John Quincy Adams argued the _Amistad_ case before the Supreme Court; Steven Spielberg filmed the story in 1997",
            "k": ["john quincy adams", "spielberg"],
            "n": 0
        },
        {
            "id": "john-brown",
            "tier": "middle",
            "t": "John Brown hoped his 1859 raid on Harpers Ferry would start a huge one across the South",
            "k": ["john brown", "harpers ferry"],
            "n": 0,
            "rabbit": "John Brown"
        },
        {
            "id": "jemmy",
            "tier": "power",
            "t": "Stono’s leader was named Jemmy; many of the marchers likely came from Kongo and called out “Liberty!” as they went",
            "k": ["jemmy", "kongo", "liberty"],
            "n": 0
        },
        {
            "id": "negro-act",
            "tier": "power",
            "t": "South Carolina’s Negro Act of 1740 banned enslaved people from gathering in groups or learning to write",
            "k": ["negro act", "1740", "learning to write"],
            "n": 0
        },
        {
            "id": "fort-mose",
            "tier": "power",
            "t": "Fort Mose, near St. Augustine in Spanish Florida, sheltered people who escaped slavery in the Carolinas",
            "k": ["fort mose", "mose", "st. augustine"],
            "n": 0
        },
        {
            "id": "death-or-liberty",
            "tier": "power",
            "t": "Gabriel planned to march under a banner reading “Death or Liberty”; he was enslaved by Thomas Prosser, and Governor James Monroe called out the militia",
            "k": ["death or liberty", "prosser", "james monroe"],
            "n": 0
        },
        {
            "id": "norfolk",
            "tier": "power",
            "t": "Gabriel fled by ship down the James River but was caught at Norfolk; he and about 25 others were executed",
            "k": ["norfolk", "james river"],
            "n": 0
        },
        {
            "id": "mother-emanuel",
            "tier": "power",
            "t": "Vesey’s African Methodist Episcopal church in Charleston was destroyed afterward; its congregation became Emanuel AME (“Mother Emanuel”)",
            "k": ["african methodist episcopal", "mother emanuel", "emanuel"],
            "n": 0
        },
        {
            "id": "sailors",
            "tier": "power",
            "t": "After Vesey’s plot, South Carolina began jailing free Black sailors while their ships were in port",
            "k": ["sailors", "jailing", "port"],
            "n": 0
        },
        {
            "id": "turner-hid",
            "tier": "power",
            "t": "Nat Turner hid for about two months before he was captured and executed in Jerusalem, Virginia (1831)",
            "k": ["two months", "jerusalem"],
            "n": 0
        },
        {
            "id": "virginia-debate",
            "tier": "power",
            "t": "Virginia’s legislature debated slowly ending slavery (1832) but chose harsher laws; Southerners blamed Garrison’s _The Liberator_",
            "k": ["legislature", "liberator", "garrison"],
            "n": 0
        },
        {
            "id": "creole",
            "tier": "power",
            "t": "_Creole_ (1841): Madison Washington led the takeover of a ship that sailed to the British Bahamas, where most aboard were freed",
            "k": ["creole", "madison washington", "bahamas"],
            "n": 0
        },
        {
            "id": "gibbs",
            "tier": "power",
            "t": "Yale’s Josiah Gibbs found an _Amistad_ interpreter by counting aloud in the Mende language on New York’s docks",
            "k": ["gibbs", "mende", "interpreter"],
            "n": 0
        },
        {
            "id": "story-sierra-leone",
            "tier": "power",
            "t": "Justice Joseph Story wrote the 1841 _Amistad_ ruling; the survivors sailed home to Sierra Leone in 1842",
            "k": ["joseph story", "sierra leone"],
            "n": 0
        },
        {
            "id": "garnet-walker",
            "tier": "power",
            "t": "David Walker’s _Appeal_ (1829) and Henry Highland Garnet (“Let your motto be resistance!”, 1843) urged enslaved people to fight back",
            "k": ["david walker", "garnet", "resistance"],
            "n": 0
        },
        {
            "id": "toussaint",
            "tier": "power",
            "t": "In Haiti, Toussaint Louverture led much of the fight, and Jean-Jacques Dessalines declared independence in 1804",
            "k": ["toussaint", "dessalines", "1804"],
            "n": 0,
            "rabbit": "Toussaint Louverture"
        }
    ],
    "trap": {
        "title": "The kind, not one",
        "body": "Tossups on this answer line march through famous examples (Stono, Gabriel, Denmark Vesey, Nat Turner, the _Amistad_), but they ask for the whole category: “these events.” Answering with one example, like “Nat Turner’s Rebellion,” or with a related answer line, like the Haitian Revolution, John Brown’s raid, or the Underground Railroad, loses the tossup. Saying just “rebellion” or “revolt” earns a prompt.",
        "fix": "When you hear “these events” or “this kind of event,” say “slave rebellions” (or “slave revolts”). Save the leaders’ names for questions that ask for “this man,” like Nat Turner, Denmark Vesey, or Gabriel.",
        "line": "Real answer line: <b><u>slave rebellions</u></b> (or slave <u>revolts</u>; accept slave <u>uprisings</u> or slave <u>insurrections</u>; prompt on <u>rebellions</u> or <u>revolts</u> alone)"
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
