import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "george-meade",
    "name": "George Meade",
    "mono": "GGM",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Union general who won at Gettysburg · Led the Army of the Potomac, 1863–1865",
    "dates": "1815–1872",
    "briefing": "George Meade was born in Spain to American parents, trained as an army engineer, and designed lighthouses in New Jersey and Florida. On June 28, 1863, he was suddenly put in command of the Union’s Army of the Potomac, and just three days later his army met Robert E. Lee’s at Gettysburg and won. Abraham Lincoln was frustrated when Meade let Lee’s beaten army escape, but Meade led the army until the war ended in 1865.",
    "answerHtml": "George <b><u>Meade</u></b> (or George Gordon <b><u>Meade</u></b>)",
    "accept": [
        "george meade",
        "meade",
        "george gordon meade",
        "george g meade",
        "general meade",
        "general george meade"
    ],
    "prompt": [
        "george"
    ],
    "reject": [
        "robert e lee",
        "lee",
        "joseph hooker",
        "hooker",
        "george mcclellan",
        "george b mcclellan",
        "mcclellan",
        "ambrose burnside",
        "burnside",
        "john pope",
        "irvin mcdowell",
        "ulysses s grant",
        "grant",
        "winfield scott hancock",
        "hancock",
        "daniel sickles",
        "sickles",
        "john reynolds",
        "joshua chamberlain",
        "george pickett",
        "pickett",
        "george armstrong custer",
        "george custer",
        "philip sheridan",
        "sheridan",
        "henry halleck",
        "william tecumseh sherman",
        "george thomas",
        "george h thomas",
        "james longstreet",
        "stonewall jackson",
        "margaret mead",
        "margaret meade",
        "fort meade",
        "fort george g meade",
        "fort george meade",
        "george meany"
    ],
    "mediaPending": True,
    "media": [],
    "wiki": "https://en.wikipedia.org/wiki/George_Meade",
    "qb": {
        "q": "Meade",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "This general was born in Cádiz [“kuh-DIZ”], Spain, on the last day of 1815, while his American father was working there as a merchant. He graduated from West Point in 1835 and later served under Zachary Taylor in the Mexican-American War.",
            "r": "For 10 points, name this Union general who replaced Joseph Hooker shortly before winning the Battle of Gettysburg."
        },
        {
            "p": "As an army engineer, this man designed lighthouses at Barnegat and Absecon [“ab-SEE-kun”] in New Jersey, as well as several on the Florida coast. He later led a survey of the Great Lakes until the Civil War began.",
            "r": "Three days before the Battle of Gettysburg, he took command of the Union’s Army of the Potomac. For 10 points, name this general."
        },
        {
            "p": "At the Battle of Fredericksburg in December 1862, this general’s division of Pennsylvania troops briefly broke through Stonewall Jackson’s line, but no reinforcements came to help, and his men were driven back. Months earlier, he had been badly wounded at Glendale during the Seven Days Battles.",
            "r": "For 10 points, name this Pennsylvanian who commanded the Union army that won at Gettysburg in July 1863."
        },
        {
            "p": "Early on June 28, 1863, a messenger woke this general in his tent near Frederick, Maryland, and he at first thought he was being arrested. Instead, the messenger brought orders putting him in command of an entire army.",
            "r": "Three days later, his Army of the Potomac began fighting at Gettysburg. For 10 points, name this general who replaced Joseph Hooker."
        },
        {
            "p": "On the night of July 2, 1863, this general held a council of war with his corps commanders in a small farmhouse behind his lines, and they agreed to stay and fight another day.",
            "r": "The next afternoon, his men turned back Pickett’s Charge. For 10 points, name this Union commander who won the Battle of Gettysburg."
        },
        {
            "p": "Abraham Lincoln wrote this general a letter saying that his “golden opportunity is gone,” but Lincoln never sent it. Lincoln was upset that this general had let the enemy army escape across the Potomac River in July 1863.",
            "r": "That army belonged to Robert E. Lee, who had just lost to this general at Gettysburg. For 10 points, name this Union general."
        },
        {
            "p": "After a great victory, this general ordered his men to “drive from our soil every vestige of the presence of the invader.” Lincoln privately complained about that order, saying, “The whole country is our soil.”",
            "r": "That victory, in July 1863, was the Battle of Gettysburg. For 10 points, name this commander of the Army of the Potomac."
        },
        {
            "p": "This general feuded for years with Daniel Sickles, a corps commander who had moved his troops forward to a peach orchard without orders. Sickles later told a committee of Congress that this general had planned to retreat from that battlefield.",
            "r": "That battle was Gettysburg, where this general commanded the Army of the Potomac. For 10 points, name this general."
        },
        {
            "p": "This general’s quick temper earned him the nickname “Old Snapping Turtle” among his soldiers, and he often clashed with other officers and with reporters. His horse, Old Baldy, was wounded several times during the war but lived for many years afterward.",
            "r": "For 10 points, name this Union general who took command of the Army of the Potomac just days before winning the Battle of Gettysburg."
        },
        {
            "p": "Beginning in 1864, the new general-in-chief traveled with this general’s army and gave the main orders, while this general remained its commander and handled its day-to-day running. That awkward arrangement lasted through the Overland Campaign and the siege of Petersburg.",
            "r": "That general-in-chief was Ulysses S. Grant. For 10 points, name this commander of the Army of the Potomac, the winner at Gettysburg."
        },
        {
            "p": "In May 1864, this general angrily argued with his cavalry commander, Philip Sheridan, who boasted that he could beat J. E. B. Stuart if allowed to. Ulysses S. Grant let Sheridan go, and Stuart died after a battle at Yellow Tavern days later.",
            "r": "For 10 points, name this commander of the Army of the Potomac, who had won at Gettysburg the year before."
        },
        {
            "p": "In late 1863, this general called off a planned attack at Mine Run in Virginia because he decided the enemy’s defenses were too strong. Earlier that fall, he had maneuvered against Robert E. Lee in the Bristoe Campaign.",
            "r": "Months before, he had beaten Lee at the Battle of Gettysburg. For 10 points, name this commander of the Army of the Potomac."
        },
        {
            "p": "An Army post in Maryland that houses the headquarters of the National Security Agency is named for this general. A large statue of him on horseback stands on Cemetery Ridge, the line his army held in his most famous battle.",
            "r": "That battle was Gettysburg. For 10 points, name this Union general who replaced Joseph Hooker in 1863."
        },
        {
            "p": "During Reconstruction, this general commanded the military district that included Georgia, Alabama, and Florida. After the war, he also served as a commissioner of Philadelphia’s Fairmount Park, and he died in that city in 1872.",
            "r": "For 10 points, name this general who led the Union’s Army of the Potomac from just before Gettysburg until the end of the Civil War."
        },
        {
            "p": "On the first day of his most famous battle, this general sent Winfield Scott Hancock ahead to take charge after John Reynolds was killed. Hancock reported that the hills south of town were good ground for a fight.",
            "r": "This general then rushed the rest of his army there. For 10 points, name this Union general who won the Battle of Gettysburg."
        }
    ],
    "clues": [
        {
            "id": "gettysburg",
            "tier": "giveaway",
            "t": "Commanded the Union army that won the Battle of Gettysburg (July 1–3, 1863)",
            "k": ["gettysburg", "union army", "1863"],
            "n": 0,
            "rabbit": "Battle of Gettysburg"
        },
        {
            "id": "potomac",
            "tier": "giveaway",
            "t": "Led the Army of the Potomac from June 1863 to the end of the Civil War",
            "k": ["army of the potomac", "potomac"],
            "n": 0
        },
        {
            "id": "replaced-hooker",
            "tier": "giveaway",
            "t": "Replaced Joseph Hooker on June 28, 1863, just three days before Gettysburg",
            "k": ["joseph hooker", "hooker", "june 28", "three days"],
            "n": 0
        },
        {
            "id": "pennsylvanian",
            "tier": "giveaway",
            "t": "A Union general from Pennsylvania, raised in Philadelphia",
            "k": ["union general", "pennsylvania", "philadelphia"],
            "n": 0
        },
        {
            "id": "no-pursuit",
            "tier": "middle",
            "t": "Lincoln was frustrated that he let Robert E. Lee’s beaten army escape across the Potomac after Gettysburg",
            "k": ["robert e. lee", "escape", "lincoln", "potomac"],
            "n": 0
        },
        {
            "id": "grant",
            "tier": "middle",
            "t": "From 1864, Ulysses S. Grant traveled with his army and gave the main orders, while he stayed its commander",
            "k": ["ulysses s. grant", "grant", "1864"],
            "n": 0,
            "rabbit": "Ulysses S. Grant"
        },
        {
            "id": "overland",
            "tier": "middle",
            "t": "Led the army in the Overland Campaign and the siege of Petersburg, then chased Lee to Appomattox (1865)",
            "k": ["overland campaign", "petersburg", "appomattox"],
            "n": 0
        },
        {
            "id": "cadiz",
            "tier": "middle",
            "t": "Born in Cádiz, Spain, to American parents (1815)",
            "k": ["cádiz", "spain", "1815"],
            "n": 0
        },
        {
            "id": "engineer",
            "tier": "middle",
            "t": "Before the war, an army engineer who designed lighthouses",
            "k": ["engineer", "lighthouses"],
            "n": 0
        },
        {
            "id": "picketts-charge",
            "tier": "middle",
            "t": "His men turned back Pickett’s Charge on Cemetery Ridge (July 3, 1863)",
            "k": ["pickett’s charge", "cemetery ridge", "july 3"],
            "n": 0
        },
        {
            "id": "snapping-turtle",
            "tier": "middle",
            "t": "Nicknamed “Old Snapping Turtle” for his quick temper",
            "k": ["snapping turtle", "temper"],
            "n": 0
        },
        {
            "id": "west-point",
            "tier": "middle",
            "t": "West Point graduate (1835) who served under Zachary Taylor in the Mexican-American War",
            "k": ["west point", "zachary taylor", "mexican-american war"],
            "n": 0
        },
        {
            "id": "golden-opportunity",
            "tier": "power",
            "t": "Lincoln wrote him a letter, never sent, saying his “golden opportunity is gone”",
            "k": ["golden opportunity", "never sent", "letter"],
            "n": 0
        },
        {
            "id": "our-soil",
            "tier": "power",
            "t": "His order to drive the invader “from our soil” led Lincoln to complain, “The whole country is our soil”",
            "k": ["our soil", "whole country"],
            "n": 0
        },
        {
            "id": "arrested",
            "tier": "power",
            "t": "When a messenger woke him on June 28, 1863, he thought he was being arrested",
            "k": ["arrested", "messenger", "woke"],
            "n": 0
        },
        {
            "id": "council",
            "tier": "power",
            "t": "Held a council of war on the night of July 2, 1863, and decided to stay and fight",
            "k": ["council of war", "july 2"],
            "n": 0
        },
        {
            "id": "hancock",
            "tier": "power",
            "t": "On July 1, sent Winfield Scott Hancock ahead to take charge after John Reynolds was killed",
            "k": ["winfield scott hancock", "hancock", "john reynolds"],
            "n": 0
        },
        {
            "id": "fredericksburg",
            "tier": "power",
            "t": "At Fredericksburg (December 1862), his division briefly broke through Stonewall Jackson’s line",
            "k": ["fredericksburg", "broke through", "stonewall jackson"],
            "n": 0
        },
        {
            "id": "glendale",
            "tier": "power",
            "t": "Badly wounded at Glendale in the Seven Days Battles (1862)",
            "k": ["glendale", "seven days"],
            "n": 0
        },
        {
            "id": "lighthouses",
            "tier": "power",
            "t": "Designed lighthouses at Barnegat and Absecon in New Jersey and others in Florida; later led a survey of the Great Lakes",
            "k": ["barnegat", "absecon", "great lakes"],
            "n": 0
        },
        {
            "id": "sickles",
            "tier": "power",
            "t": "Feuded with Daniel Sickles, who moved his corps to the Peach Orchard without orders and later told Congress he had planned to retreat",
            "k": ["daniel sickles", "sickles", "peach orchard"],
            "n": 0
        },
        {
            "id": "sheridan",
            "tier": "power",
            "t": "Clashed with cavalry chief Philip Sheridan (May 1864); Grant let Sheridan ride off, and J. E. B. Stuart died after Yellow Tavern",
            "k": ["philip sheridan", "sheridan", "yellow tavern"],
            "n": 0
        },
        {
            "id": "old-baldy",
            "tier": "power",
            "t": "His horse, Old Baldy, was wounded several times but lived for years after the war",
            "k": ["old baldy", "horse"],
            "n": 0
        },
        {
            "id": "mine-run",
            "tier": "power",
            "t": "Called off an attack at Mine Run (late 1863) because Lee’s defenses were too strong; earlier fought the Bristoe Campaign",
            "k": ["mine run", "bristoe"],
            "n": 0
        },
        {
            "id": "fort-namesake",
            "tier": "power",
            "t": "A Maryland Army post that houses the National Security Agency is named for him; his statue stands on Cemetery Ridge",
            "k": ["national security agency", "maryland", "statue"],
            "n": 0
        },
        {
            "id": "reconstruction",
            "tier": "power",
            "t": "Commanded the Reconstruction military district of Georgia, Alabama, and Florida; died in Philadelphia in 1872",
            "k": ["reconstruction", "georgia", "1872"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Which Union general?",
        "body": "Abraham Lincoln went through a string of generals in the East, and tossups about one often name the others. Irvin McDowell lost at First Bull Run, George McClellan fought at Antietam, John Pope lost at Second Bull Run, Ambrose Burnside lost at Fredericksburg, Joseph Hooker lost at Chancellorsville, and George Meade won at Gettysburg. From 1864, Ulysses S. Grant traveled with Meade’s army, so late-war clues can point to either man.",
        "fix": "Gettysburg, replacing Hooker, “Old Snapping Turtle,” lighthouses, and a birth in Spain mean Meade. If the clue is about the general-in-chief who gave the orders in 1864–1865 or accepted Lee’s surrender, answer Grant. Don’t mix him up with the anthropologist Margaret Mead.",
        "line": "Real answer line: George <b><u>Meade</u></b> (or George Gordon <b><u>Meade</u></b>)"
    },
    "tests": {
        "right": [
            "George Meade",
            "Meade",
            "George Gordon Meade",
            "General Meade",
            "George Mead",
            "Gen. George G. Meade"
        ],
        "prompt": [
            "George"
        ],
        "wrong": [
            "Joseph Hooker",
            "George McClellan",
            "Robert E. Lee",
            "Margaret Mead",
            "Fort Meade",
            "Ulysses S. Grant",
            "Daniel Sickles",
            "George Meany"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", data["id"])
