import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "anaconda-plan",
    "name": "Anaconda Plan",
    "mono": "AP",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Winfield Scott’s 1861 Union strategy · Blockade the coast, seize the Mississippi",
    "dates": "Proposed 1861",
    "briefing": "In 1861, the 74-year-old Union general Winfield Scott proposed a slow squeeze: blockade the Confederacy’s coastline and send gunboats and troops down the Mississippi River to split the South in two. Impatient Northerners wanted a quick march on Richmond instead, and critics mocked his idea by naming it after a giant snake that crushes its prey. The war took four years, and the Union ended up doing much of what Scott had planned.",
    "answerHtml": "<b><u>Anaconda</u></b> Plan (prompt on the Union <u>blockade</u> of the South or <u>Scott’s Great Snake</u>)",
    "accept": [
        "anaconda plan",
        "anaconda",
        "the anaconda plan",
        "anaconda strategy",
        "scotts anaconda",
        "scotts anaconda plan"
    ],
    "prompt": [
        "blockade",
        "union blockade",
        "naval blockade",
        "blockade of the south",
        "blockade of southern ports",
        "scotts plan",
        "winfield scotts plan",
        "scotts great snake",
        "great snake"
    ],
    "reject": [
        "mississippi river",
        "mississippi",
        "american civil war",
        "civil war",
        "siege of vicksburg",
        "vicksburg",
        "port hudson",
        "march to the sea",
        "shermans march to the sea",
        "total war",
        "marshall plan",
        "schlieffen plan",
        "virginia plan",
        "new jersey plan",
        "ten percent plan",
        "winfield scott",
        "king cotton",
        "cotton diplomacy",
        "monroe doctrine",
        "containment",
        "snakes"
    ],
    "mediaPending": True,
    "media": [],
    "wiki": "https://en.wikipedia.org/wiki/Anaconda_Plan",
    "qb": {
        "q": "Anaconda",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "After two victories completed this plan’s goal on one river, Abraham Lincoln wrote in a letter to James Conkling that “the Father of Waters again goes unvexed to the sea.” Those victories were the captures of Vicksburg, Mississippi, and Port Hudson, Louisiana, in July 1863.",
            "r": "For 10 points, name this plan by Winfield Scott to blockade the South and seize the Mississippi River, named for a snake."
        },
        {
            "p": "In the 1863 _Prize Cases_, the Supreme Court ruled 5–4 that the president could order one part of this plan without a declaration of war from Congress. Abraham Lincoln had proclaimed that part on April 19, 1861, a week after the attack on Fort Sumter.",
            "r": "That part was a naval blockade of Southern ports. For 10 points, name this Union strategy proposed by Winfield Scott."
        },
        {
            "p": "The capture of Fort Fisher in January 1865 closed Wilmington, North Carolina, the last major Confederate port still used by ships slipping past one part of this plan. Those low, fast steamers often carried cotton out to Nassau or Bermuda and brought weapons back.",
            "r": "Those ships were called blockade runners. For 10 points, name this Union strategy of Winfield Scott, named for a snake that squeezes its prey."
        },
        {
            "p": "In Margaret Mitchell’s novel _Gone with the Wind_, Rhett Butler makes a fortune by sneaking ships past one part of this plan. Many real ships that did the same thing sailed from Nassau in the Bahamas.",
            "r": "That part of this plan was a naval blockade of Southern ports. For 10 points, name this strategy proposed by Winfield Scott in 1861."
        },
        {
            "p": "Northern newspapers led by Horace Greeley’s _New-York Tribune_ rejected this slow plan and demanded a quick march on Richmond. That pressure helped push the Union army into the First Battle of Bull Run, where it suffered a stunning defeat in July 1861.",
            "r": "For 10 points, name this plan by General Winfield Scott to squeeze the South with a blockade and control of the Mississippi River."
        },
        {
            "p": "In letters to George McClellan in May 1861, this plan’s author predicted that it would bring the South to terms with less bloodshed than any other strategy. That author, then 74 years old, was too old and ill to lead an army in the field.",
            "r": "That author was Winfield Scott, nicknamed “Old Fuss and Feathers.” For 10 points, name this plan to blockade the South and control the Mississippi."
        },
        {
            "p": "In August 1864, David Farragut led a fleet past underwater mines, then called “torpedoes,” to close Mobile Bay, Alabama, one of the last Gulf ports used by ships slipping past one part of this plan. Two years earlier, Farragut had captured New Orleans.",
            "r": "An 1861 cartoon map called this plan “Scott’s Great Snake.” For 10 points, name this Union strategy to blockade the South and take the Mississippi River."
        },
        {
            "p": "To carry out the river half of this plan, engineer James Eads built a fleet of ironclad gunboats, including the USS _Cairo_, which a mine sank in the Yazoo River in December 1862. The _Cairo_ was raised a century later and put on display at Vicksburg.",
            "r": "For 10 points, name this Union strategy, proposed by Winfield Scott, to control the Mississippi River and blockade the South."
        },
        {
            "p": "In April 1862, John Pope’s army and Andrew Foote’s gunboats captured the Confederate defenses on Island No. 10, opening more of one river for this plan. Weeks later, David Farragut’s fleet ran past Forts Jackson and St. Philip and captured New Orleans.",
            "r": "For 10 points, name this Union strategy to take control of the Mississippi River and blockade the Confederacy, named for a giant snake."
        },
        {
            "p": "Nathaniel Banks’s army besieged Port Hudson, Louisiana, for about seven weeks, and its surrender in July 1863 completed one goal of this plan. Five days earlier, John Pemberton had surrendered Vicksburg to Ulysses S. Grant.",
            "r": "Those victories split the Confederacy in two. For 10 points, name this plan by Winfield Scott to control the Mississippi River and blockade Southern ports."
        },
        {
            "p": "In November 1861, a fleet under Samuel Du Pont captured Port Royal Sound in South Carolina so that ships enforcing one part of this plan would have a base for coal and supplies. Navy Secretary Gideon Welles divided those ships into squadrons along the Atlantic and Gulf coasts.",
            "r": "For 10 points, name this Union strategy to blockade the Confederacy and seize the Mississippi River, named for a snake."
        },
        {
            "p": "On March 8, 1862, the ironclad CSS _Virginia_ tried to break one part of this plan at Hampton Roads by sinking the USS _Cumberland_ and destroying the USS _Congress_. The next day, the USS _Monitor_ arrived and fought the _Virginia_ to a draw.",
            "r": "That part of this plan was the Union’s naval blockade of the South. For 10 points, name this strategy proposed by Winfield Scott."
        },
        {
            "p": "One goal of this plan was to cut off Texas, Arkansas, and Louisiana west of the river from the rest of the Confederacy, along with the cattle and supplies those lands sent east. Ulysses S. Grant’s capture of Vicksburg in 1863 was a key step toward that goal.",
            "r": "For 10 points, name this plan by Winfield Scott to blockade the South and control the Mississippi River."
        },
        {
            "p": "In 1861, Southern leaders held back their own cotton, hoping a shortage would force Britain to help them, but one part of this plan soon made shipping cotton overseas much harder anyway. As that part tightened, prices of salt, coffee, and other goods soared across the Confederacy.",
            "r": "For 10 points, name this Union strategy of Winfield Scott, which combined a naval blockade with a campaign down the Mississippi River."
        },
        {
            "p": "The author of this plan, a Virginian who stayed loyal to the Union, had commanded the brigade that won the Battle of Chippawa in the War of 1812 and led the army that captured Mexico City in 1847. He retired in November 1861, and George McClellan replaced him.",
            "r": "That general was Winfield Scott. For 10 points, name his plan to defeat the Confederacy by blockading its coast and seizing the Mississippi River."
        }
    ],
    "clues": [
        {
            "id": "scott",
            "tier": "giveaway",
            "t": "Proposed in 1861 by Winfield Scott, the Union army’s 74-year-old general-in-chief",
            "k": ["winfield scott", "scott", "general-in-chief", "1861"],
            "n": 0
        },
        {
            "id": "blockade",
            "tier": "giveaway",
            "t": "Part one: a naval blockade of Southern ports along the Atlantic and Gulf coasts",
            "k": ["blockade", "naval", "southern ports"],
            "n": 0
        },
        {
            "id": "mississippi",
            "tier": "giveaway",
            "t": "Part two: gunboats and troops would take control of the Mississippi River and split the Confederacy in two",
            "k": ["mississippi river", "mississippi", "split", "gunboats"],
            "n": 0,
            "rabbit": "Mississippi River"
        },
        {
            "id": "snake",
            "tier": "giveaway",
            "t": "Named after a giant South American snake that squeezes its prey",
            "k": ["snake", "squeezes", "south american"],
            "n": 0
        },
        {
            "id": "civil-war",
            "tier": "giveaway",
            "t": "A Union strategy for winning the American Civil War (1861–1865)",
            "k": ["civil war", "union", "strategy"],
            "n": 0,
            "rabbit": "American Civil War"
        },
        {
            "id": "vicksburg",
            "tier": "middle",
            "t": "Ulysses S. Grant’s capture of Vicksburg, Mississippi (July 4, 1863), was the key victory on the river",
            "k": ["vicksburg", "ulysses s. grant", "july 4"],
            "n": 0,
            "rabbit": "Siege of Vicksburg"
        },
        {
            "id": "port-hudson",
            "tier": "middle",
            "t": "Port Hudson, Louisiana, surrendered five days after Vicksburg (July 9, 1863), giving the Union the whole river",
            "k": ["port hudson", "louisiana", "july 9"],
            "n": 0
        },
        {
            "id": "father-of-waters",
            "tier": "middle",
            "t": "Lincoln then wrote that “the Father of Waters again goes unvexed to the sea”",
            "k": ["father of waters", "unvexed"],
            "n": 0
        },
        {
            "id": "mocked",
            "tier": "middle",
            "t": "Critics mocked it as too slow; newspapers like Horace Greeley’s _New-York Tribune_ demanded a quick march on Richmond",
            "k": ["mocked", "richmond", "greeley", "tribune"],
            "n": 0
        },
        {
            "id": "bull-run",
            "tier": "middle",
            "t": "Pressure for fast action helped lead to the Union defeat at the First Battle of Bull Run (July 1861)",
            "k": ["bull run", "july 1861", "defeat"],
            "n": 0,
            "rabbit": "First Battle of Bull Run"
        },
        {
            "id": "new-orleans",
            "tier": "middle",
            "t": "David Farragut’s fleet captured New Orleans (April 1862) after running past Forts Jackson and St. Philip",
            "k": ["farragut", "new orleans", "forts jackson"],
            "n": 0,
            "rabbit": "New Orleans"
        },
        {
            "id": "blockade-runners",
            "tier": "middle",
            "t": "Fast “blockade runners” slipped through, often via Nassau or Bermuda; Rhett Butler is one in _Gone with the Wind_",
            "k": ["blockade runners", "nassau", "bermuda", "rhett butler"],
            "n": 0
        },
        {
            "id": "proclamation",
            "tier": "middle",
            "t": "Abraham Lincoln proclaimed the blockade on April 19, 1861, a week after the attack on Fort Sumter",
            "k": ["april 19", "proclaimed", "fort sumter"],
            "n": 0
        },
        {
            "id": "old-fuss",
            "tier": "middle",
            "t": "Scott, nicknamed “Old Fuss and Feathers,” won at Chippawa (1814) and captured Mexico City (1847); he retired in November 1861",
            "k": ["old fuss and feathers", "mexico city", "chippawa", "retired"],
            "n": 0
        },
        {
            "id": "great-snake",
            "tier": "middle",
            "t": "An 1861 cartoon map, “Scott’s Great Snake,” showed a giant serpent wrapped around the Confederacy",
            "k": ["great snake", "cartoon", "serpent"],
            "n": 0
        },
        {
            "id": "mcclellan-letters",
            "tier": "power",
            "t": "Scott described the plan in letters to George McClellan (May 1861), predicting less bloodshed than any other strategy; McClellan replaced him",
            "k": ["mcclellan", "letters", "bloodshed"],
            "n": 0
        },
        {
            "id": "prize-cases",
            "tier": "power",
            "t": "The _Prize Cases_ (1863): the Supreme Court upheld Lincoln’s blockade, 5–4, even without a declaration of war",
            "k": ["prize cases", "supreme court", "declaration of war"],
            "n": 0
        },
        {
            "id": "fort-fisher",
            "tier": "power",
            "t": "Fort Fisher fell in January 1865, closing Wilmington, North Carolina, the last major port for blockade runners",
            "k": ["fort fisher", "wilmington", "january 1865"],
            "n": 0
        },
        {
            "id": "island-10",
            "tier": "power",
            "t": "John Pope’s army and Andrew Foote’s gunboats captured Island No. 10 on the Mississippi (April 1862)",
            "k": ["island no. 10", "andrew foote", "john pope"],
            "n": 0
        },
        {
            "id": "eads-cairo",
            "tier": "power",
            "t": "James Eads built ironclad river gunboats like the USS _Cairo_, sunk by a mine in the Yazoo River (1862) and raised in 1964",
            "k": ["james eads", "eads", "cairo", "yazoo"],
            "n": 0
        },
        {
            "id": "banks",
            "tier": "power",
            "t": "Nathaniel Banks besieged Port Hudson for about seven weeks before it surrendered",
            "k": ["nathaniel banks", "banks", "seven weeks"],
            "n": 0
        },
        {
            "id": "port-royal",
            "tier": "power",
            "t": "Samuel Du Pont captured Port Royal Sound, South Carolina (November 1861), as a base for the blockade fleet",
            "k": ["port royal", "du pont", "base"],
            "n": 0
        },
        {
            "id": "welles",
            "tier": "power",
            "t": "Navy Secretary Gideon Welles divided the blockade fleet into squadrons along the Atlantic and Gulf coasts",
            "k": ["gideon welles", "welles", "squadrons"],
            "n": 0
        },
        {
            "id": "hampton-roads",
            "tier": "power",
            "t": "The CSS _Virginia_ sank the USS _Cumberland_ and destroyed the USS _Congress_ at Hampton Roads (March 8, 1862) before fighting the _Monitor_",
            "k": ["hampton roads", "cumberland", "monitor"],
            "n": 0
        },
        {
            "id": "trans-mississippi",
            "tier": "power",
            "t": "Taking the river cut off Texas, Arkansas, and Louisiana west of the river from the rest of the Confederacy",
            "k": ["texas", "arkansas", "cut off"],
            "n": 0
        },
        {
            "id": "mobile-bay",
            "tier": "power",
            "t": "David Farragut closed Mobile Bay, Alabama (August 1864), steaming past underwater mines then called “torpedoes”",
            "k": ["mobile bay", "torpedoes", "august 1864"],
            "n": 0
        },
        {
            "id": "king-cotton",
            "tier": "power",
            "t": "In 1861 the South held back cotton to pressure Britain (“King Cotton”); the blockade later caused shortages of salt and coffee",
            "k": ["king cotton", "cotton", "salt", "coffee"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Plan, river, or siege?",
        "body": "This plan’s two halves lead to other answer lines: the Mississippi River, and battles on it like the Siege of Vicksburg. If a question asks for “this river,” “this siege,” or “this war,” naming the plan is wrong, and naming the river when it asks for “this plan” or “this strategy” is wrong too. Players also mix it up with the Marshall Plan, a different “plan” answer, or with Sherman’s “total war” March to the Sea.",
        "fix": "Listen for the noun: “this plan” or “this strategy” wants the Anaconda Plan. Winfield Scott, a blockade, a snake, or squeezing the South means the plan; Grant, John Pemberton, and a six-week siege mean Vicksburg. If you just say “the blockade,” expect a prompt, so add the plan’s name.",
        "line": "Real answer line: <b><u>Anaconda</u></b> Plan (prompt on the Union <u>blockade</u> of the South)"
    },
    "tests": {
        "right": [
            "Anaconda Plan",
            "Anaconda",
            "the Anaconda Plan",
            "Anaconda strategy",
            "Anacoda Plan"
        ],
        "prompt": [
            "blockade",
            "Union blockade",
            "Scott's Great Snake"
        ],
        "wrong": [
            "Mississippi River",
            "American Civil War",
            "Siege of Vicksburg",
            "Marshall Plan",
            "Winfield Scott",
            "March to the Sea"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", data["id"])
