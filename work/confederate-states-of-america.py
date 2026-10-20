import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "confederate-states-of-america",
    "name": "Confederate States of America",
    "mono": "CSA",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Breakaway nation of 11 Southern states · Fought the Union in the Civil War",
    "dates": "1861–1865",
    "briefing": "In February 1861, delegates from Deep South states that had seceded after Abraham Lincoln’s election met in Montgomery, Alabama, and formed the Confederate States of America, with Jefferson Davis as president. Its leaders said openly that they were protecting slavery. Four more states joined after the attack on Fort Sumter, the capital moved to Richmond, Virginia, and the Confederacy collapsed in 1865 when its armies surrendered.",
    "answerHtml": "<b><u>Confederate States</u></b> of America (or the <b><u>Confederacy</u></b>; accept <u>CSA</u>; prompt on <u>the South</u>)",
    "accept": [
        "confederate states of america",
        "confederate states",
        "the confederate states",
        "confederacy",
        "the confederacy",
        "southern confederacy",
        "csa",
        "c s a"
    ],
    "prompt": [
        "the south",
        "south",
        "southern states",
        "the southern states",
        "confederate",
        "confederates",
        "the confederates",
        "dixie",
        "rebels",
        "the rebels"
    ],
    "reject": [
        "union",
        "the union",
        "united states",
        "united states of america",
        "usa",
        "the north",
        "north",
        "northern states",
        "articles of confederation",
        "confederation",
        "iroquois confederacy",
        "haudenosaunee confederacy",
        "powhatan confederacy",
        "confederate army",
        "confederate states army",
        "confederate navy",
        "confederate states navy",
        "confederate congress",
        "confederate constitution",
        "army of northern virginia",
        "jefferson davis",
        "robert e lee",
        "alexander stephens",
        "border states",
        "south carolina",
        "west virginia",
        "secession",
        "civil war",
        "american civil war",
        "republic of texas"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Confederate_States_of_America",
    "qb": {
        "q": "Confederate States of America",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In a March 1861 speech in Savannah, Georgia, this nation’s vice president declared that its “cornerstone” rested on slavery and on the belief that Black people were not equal to white people. That speaker, Alexander Stephens, had served in the U.S. House of Representatives from 1843 to 1859.",
            "r": "For 10 points, name this nation formed by Southern states that seceded from the Union, led by Jefferson Davis."
        },
        {
            "p": "On February 18, 1861, a former Mississippi senator took the oath of office as this nation’s provisional president on the portico of the Alabama State Capitol in Montgomery. Delegates meeting in that city had written a temporary constitution for this nation earlier that month.",
            "r": "Its capital later moved to Richmond, Virginia. For 10 points, name this nation led by Jefferson Davis."
        },
        {
            "p": "Four states of the Upper South, starting with Virginia, joined this nation after Abraham Lincoln called for 75,000 volunteers to put down the rebellion in April 1861. Western counties of Virginia rejected that choice and later formed a new state loyal to the Union.",
            "r": "For 10 points, name this nation of eleven states that fought the Civil War under President Jefferson Davis."
        },
        {
            "p": "This nation’s constitution, adopted in March 1861, gave its president a single six-year term and let him veto individual items in spending bills. Unlike the U.S. Constitution of that time, it openly used the word “slaves” and protected slavery in any new territories.",
            "r": "Its vice president was Alexander Stephens. For 10 points, name this nation whose only president was Jefferson Davis."
        },
        {
            "p": "In April 1863, hundreds of women broke into shops in this nation’s capital to protest food shortages and soaring prices, in what became known as the Bread Riot. This nation’s leaders had hoped that Britain’s need for Southern cotton would win them foreign support, but no country ever officially recognized this nation.",
            "r": "Its capital was Richmond, Virginia. For 10 points, name this nation that fought the Union in the Civil War."
        },
        {
            "p": "In November 1861, U.S. Navy captain Charles Wilkes stopped the British mail ship _Trent_ and seized James Mason and John Slidell, two diplomats this nation was sending to Europe. Britain was furious, and Abraham Lincoln’s government released the two men to avoid a war.",
            "r": "Its president, Jefferson Davis, had sent those diplomats. For 10 points, name this Southern nation that fought the Union in the Civil War."
        },
        {
            "p": "In April 1862, this government passed the first national draft law in American history. Later that year, it excused one white man from service on each plantation with 20 or more enslaved people, which led many poorer soldiers to complain of “a rich man’s war and a poor man’s fight.”",
            "r": "Its best-known general was Robert E. Lee. For 10 points, name this government led by Jefferson Davis during the Civil War."
        },
        {
            "p": "This nation’s navy raised the burned frigate USS _Merrimack_ and rebuilt it as an ironclad, which fought the USS _Monitor_ at Hampton Roads in March 1862. Its submarine _H. L. Hunley_ later became the first submarine to sink an enemy warship.",
            "r": "For 10 points, name this nation whose generals included Robert E. Lee and Stonewall Jackson."
        },
        {
            "p": "The Cherokee leader Stand Watie was the last general in this nation’s army to surrender on land, in June 1865. Its commerce raider _Shenandoah_ kept sailing until November of that year, when its crew finally gave up in Liverpool, England.",
            "r": "Most of its soldiers had surrendered after Robert E. Lee gave up at Appomattox Court House. For 10 points, name this nation that lost the Civil War."
        },
        {
            "p": "In March 1865, with its armies near collapse, this nation’s congress voted to let enslaved men serve as soldiers, but the war ended before many could fight. About a year earlier, General Patrick Cleburne had proposed the same idea, and his proposal was hushed up.",
            "r": "Robert E. Lee led its most famous army. For 10 points, name this Southern nation that fought the Union from 1861 to 1865."
        },
        {
            "p": "This nation’s battle flag showed 13 stars, counting Kentucky and Missouri, where rival pro-Southern governments declared secession even though both states stayed in the Union. Maryland and Delaware were the other slave states that never joined this nation.",
            "r": "For 10 points, name this nation of eleven Southern states that fought the Union from 1861 to 1865."
        },
        {
            "p": "This nation’s first national flag, nicknamed the “Stars and Bars,” looked so much like the U.S. flag that soldiers had trouble telling them apart at the First Battle of Bull Run. Afterward, its generals adopted a separate battle flag with a blue X-shaped cross.",
            "r": "Its capital moved to Richmond, Virginia, in 1861. For 10 points, name this nation led by Jefferson Davis."
        },
        {
            "p": "Several states that formed this nation issued declarations explaining why they left the Union, and Mississippi’s said its position was “thoroughly identified with the institution of slavery.” South Carolina had been the first state to leave, in December 1860, soon after Abraham Lincoln was elected.",
            "r": "For 10 points, name this nation formed by seceding Southern states, which fought the Union in the Civil War."
        },
        {
            "p": "Judah P. Benjamin served this nation as attorney general, secretary of war, and secretary of state, and he escaped to England when it collapsed. Union general Winfield Scott’s Anaconda Plan aimed to squeeze this nation with a naval blockade and control of the Mississippi River.",
            "r": "Its most famous general was Robert E. Lee. For 10 points, name this nation whose president, Jefferson Davis, governed from Richmond."
        },
        {
            "p": "After fleeing its capital by train on the night of April 2, 1865, this nation’s government spent about a week in Danville, Virginia, before moving on to North Carolina. Its president was captured near Irwinville, Georgia, the next month.",
            "r": "Robert E. Lee had surrendered at Appomattox Court House on April 9. For 10 points, name this nation that lost the Civil War."
        }
    ],
    "clues": [
        {
            "id": "civil-war",
            "tier": "giveaway",
            "t": "Nation formed by Southern states that seceded from the Union; it fought and lost the Civil War (1861–1865)",
            "k": ["seceded", "civil war", "southern"],
            "n": 0,
            "rabbit": "American Civil War"
        },
        {
            "id": "jefferson-davis",
            "tier": "giveaway",
            "t": "Its only president was Jefferson Davis, a former U.S. senator from Mississippi",
            "k": ["jefferson davis", "davis", "mississippi"],
            "n": 0,
            "rabbit": "Jefferson Davis"
        },
        {
            "id": "robert-e-lee",
            "tier": "giveaway",
            "t": "Robert E. Lee led its most famous army and surrendered at Appomattox Court House (April 9, 1865)",
            "k": ["robert e. lee", "appomattox", "lee"],
            "n": 0,
            "rabbit": "Robert E. Lee"
        },
        {
            "id": "fort-sumter",
            "tier": "giveaway",
            "t": "Its troops fired on Fort Sumter in Charleston Harbor (April 12, 1861), starting the Civil War",
            "k": ["fort sumter", "sumter", "charleston"],
            "n": 0,
            "rabbit": "Fort Sumter"
        },
        {
            "id": "richmond",
            "tier": "middle",
            "t": "Capital: first Montgomery, Alabama, then Richmond, Virginia, from 1861",
            "k": ["richmond", "montgomery"],
            "n": 0
        },
        {
            "id": "montgomery-1861",
            "tier": "middle",
            "t": "Formed in February 1861 by delegates meeting in Montgomery, Alabama; Davis took the oath there on February 18",
            "k": ["february 1861", "delegates", "oath"],
            "n": 0,
            "rabbit": "Montgomery, Alabama"
        },
        {
            "id": "cornerstone",
            "tier": "middle",
            "t": "Cornerstone Speech (March 1861): Vice President Alexander Stephens said its “cornerstone” was slavery and the belief that Black people were not equal to white people",
            "k": ["cornerstone", "alexander stephens", "stephens", "savannah"],
            "n": 0
        },
        {
            "id": "eleven-states",
            "tier": "middle",
            "t": "Eleven states: seven from the Deep South, then four more, led by Virginia, after Lincoln called for 75,000 volunteers",
            "k": ["eleven", "75,000", "volunteers", "virginia"],
            "n": 0
        },
        {
            "id": "south-carolina",
            "tier": "middle",
            "t": "South Carolina seceded first (December 20, 1860), soon after Abraham Lincoln was elected",
            "k": ["south carolina", "december 20", "lincoln"],
            "n": 0
        },
        {
            "id": "constitution",
            "tier": "middle",
            "t": "Its constitution openly protected slavery and gave the president a single six-year term and a line-item veto",
            "k": ["six-year", "line-item", "constitution"],
            "n": 0
        },
        {
            "id": "anaconda",
            "tier": "middle",
            "t": "The Union’s Anaconda Plan aimed to squeeze it with a naval blockade and control of the Mississippi River",
            "k": ["anaconda", "blockade", "mississippi river"],
            "n": 0,
            "rabbit": "Anaconda Plan"
        },
        {
            "id": "king-cotton",
            "tier": "middle",
            "t": "Its leaders hoped Britain’s need for cotton (“King Cotton”) would win support, but no foreign country ever officially recognized it",
            "k": ["king cotton", "cotton", "britain", "recognized"],
            "n": 0
        },
        {
            "id": "border-states",
            "tier": "middle",
            "t": "Slave states that stayed in the Union: Maryland, Delaware, Kentucky, and Missouri; western Virginia broke away as West Virginia (1863)",
            "k": ["west virginia", "maryland", "delaware", "border"],
            "n": 0
        },
        {
            "id": "bread-riot",
            "tier": "power",
            "t": "Richmond Bread Riot (April 1863): hundreds of women protested food shortages and soaring prices",
            "k": ["bread riot", "bread", "food shortages"],
            "n": 0
        },
        {
            "id": "trent",
            "tier": "power",
            "t": "Trent Affair (1861): U.S. Navy captain Charles Wilkes seized its diplomats James Mason and John Slidell from a British ship",
            "k": ["trent", "mason", "slidell", "wilkes"],
            "n": 0
        },
        {
            "id": "draft",
            "tier": "power",
            "t": "Passed the first national draft in American history (April 1862); a plantation exemption led to complaints of “a rich man’s war and a poor man’s fight”",
            "k": ["draft", "rich man’s war", "1862"],
            "n": 0,
            "rabbit": "Military draft"
        },
        {
            "id": "merrimack",
            "tier": "power",
            "t": "Rebuilt the USS _Merrimack_ as an ironclad, which fought the USS _Monitor_ at Hampton Roads (March 1862)",
            "k": ["merrimack", "monitor", "hampton roads", "ironclad"],
            "n": 0,
            "rabbit": "Ironclads"
        },
        {
            "id": "hunley",
            "tier": "power",
            "t": "Its _H. L. Hunley_ was the first submarine to sink an enemy warship (1864)",
            "k": ["hunley", "submarine"],
            "n": 0
        },
        {
            "id": "last-surrender",
            "tier": "power",
            "t": "Last to give up: Cherokee general Stand Watie on land (June 1865) and the raider _Shenandoah_ at Liverpool, England (November 1865)",
            "k": ["stand watie", "shenandoah", "liverpool"],
            "n": 0
        },
        {
            "id": "enslaved-soldiers",
            "tier": "power",
            "t": "In March 1865, its congress voted to let enslaved men serve as soldiers; Patrick Cleburne’s similar proposal a year earlier had been hushed up",
            "k": ["cleburne", "march 1865", "soldiers"],
            "n": 0
        },
        {
            "id": "thirteen-stars",
            "tier": "power",
            "t": "Its battle flag had 13 stars, counting Kentucky and Missouri, which never actually left the Union",
            "k": ["13 stars", "battle flag", "kentucky", "missouri"],
            "n": 0
        },
        {
            "id": "stars-and-bars",
            "tier": "power",
            "t": "Its first national flag, the “Stars and Bars,” looked so much like the U.S. flag that it caused confusion at the First Battle of Bull Run",
            "k": ["stars and bars", "bull run"],
            "n": 0
        },
        {
            "id": "mississippi-declaration",
            "tier": "power",
            "t": "Mississippi’s declaration of the causes of secession said its position was “thoroughly identified with the institution of slavery”",
            "k": ["thoroughly identified", "institution of slavery", "declaration"],
            "n": 0
        },
        {
            "id": "judah-benjamin",
            "tier": "power",
            "t": "Judah P. Benjamin served as its attorney general, secretary of war, and secretary of state, then escaped to England",
            "k": ["judah p. benjamin", "benjamin"],
            "n": 0
        },
        {
            "id": "danville",
            "tier": "power",
            "t": "Its government fled Richmond by train on April 2, 1865, and stopped for about a week in Danville, Virginia; Davis was captured near Irwinville, Georgia, in May",
            "k": ["danville", "irwinville", "april 2"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Confederacy or Confederation?",
        "body": "The Articles of Confederation were the first U.S. plan of government, used from 1781 to 1789, long before the Civil War; the Confederate States of America was the nation of seceded Southern states (1861–1865). The names sound alike, so a quick buzz can grab the wrong one. Also, “the South” only earns a prompt, and clues about Jefferson Davis or Robert E. Lee can tempt you to name the man instead of the nation.",
        "fix": "Check the date and the noun: “this nation” or “this government” in the 1860s means the Confederate States (or “the Confederacy”), while a 1780s “document” or “plan of government” means the Articles of Confederation. If you are prompted after saying “the South,” say “Confederate States of America.”",
        "line": "Real answer line: <b><u>Confederate States</u></b> of America (or the <b><u>Confederacy</u></b>; accept <u>CSA</u>; prompt on <u>the South</u>)"
    },
    "tests": {
        "right": [
            "Confederate States of America",
            "the Confederacy",
            "CSA",
            "Confederate States",
            "Confedracy",
            "Southern Confederacy"
        ],
        "prompt": [
            "the South",
            "Confederate"
        ],
        "wrong": [
            "Union",
            "Articles of Confederation",
            "United States",
            "Jefferson Davis",
            "Iroquois Confederacy",
            "Confederate Army",
            "Border states"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
