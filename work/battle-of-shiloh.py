import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "battle-of-shiloh",
    "name": "Battle of Shiloh",
    "mono": "SHI",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Grant’s costly 1862 win in Tennessee · Its huge losses shocked the nation",
    "dates": "Fought April 6–7, 1862",
    "briefing": "Early on April 6, 1862, Confederate troops burst out of the woods near a little log church in southwestern Tennessee and caught Ulysses S. Grant’s army by surprise. Their commander, Albert Sidney Johnston, was killed that afternoon, and the next day Union reinforcements helped Grant drive the Confederates away. With nearly 24,000 men killed, wounded, captured, or missing, Shiloh was the bloodiest battle in American history up to that time.",
    "answerHtml": "Battle of <b><u>Shiloh</u></b> (or Battle of <b><u>Pittsburg Landing</u></b>)",
    "accept": [
        "shiloh",
        "battle of shiloh",
        "pittsburg landing",
        "battle of pittsburg landing",
        "pittsburgh landing",
        "battle of pittsburgh landing"
    ],
    "prompt": [],
    "reject": [
        "fort donelson",
        "battle of fort donelson",
        "fort henry",
        "battle of fort henry",
        "corinth",
        "siege of corinth",
        "battle of corinth",
        "vicksburg",
        "siege of vicksburg",
        "antietam",
        "battle of antietam",
        "gettysburg",
        "battle of gettysburg",
        "chickamauga",
        "stones river",
        "perryville",
        "pea ridge",
        "chattanooga",
        "bull run",
        "first battle of bull run",
        "fort sumter",
        "hornets nest",
        "the hornets nest",
        "sunken road"
    ],
    "mediaPending": True,
    "media": [],
    "wiki": "https://en.wikipedia.org/wiki/Battle_of_Shiloh",
    "qb": {
        "q": "Shiloh",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "The Welsh-born journalist Henry Morton Stanley, who later tracked down the missionary David Livingstone in Africa, fought for the Confederacy in this battle and was taken prisoner. The Union soldier Ambrose Bierce later wrote a vivid memoir essay about what he saw in this battle.",
            "r": "For 10 points, name this April 1862 battle in Tennessee, where Albert Sidney Johnston’s army surprised Ulysses S. Grant’s."
        },
        {
            "p": "After this battle, Henry Halleck took personal command in the field and moved so slowly toward Corinth, Mississippi, that the Confederates simply abandoned the town in late May. Meanwhile, newspapers blamed the general who had won this battle for letting his army be caught by surprise.",
            "r": "That general was Ulysses S. Grant. For 10 points, name this April 1862 battle in Tennessee."
        },
        {
            "p": "In a Ray Bradbury short story, a general comforts a frightened young drummer named Joby on the night before this battle. Herman Melville wrote a short requiem for this battle’s dead, describing swallows that skim low over its “forest-field.”",
            "r": "For 10 points, name this April 1862 battle in Tennessee, where Confederate general Albert Sidney Johnston was killed."
        },
        {
            "p": "Daniel Ruggles gathered dozens of Confederate cannons to pound a stubborn Union position during this battle. Union troops had held that position, nicknamed the “Hornet’s Nest” for the buzzing of bullets, until Benjamin Prentiss surrendered more than 2,000 men there late in the day.",
            "r": "For 10 points, name this April 1862 battle in Tennessee, a hard-won victory for Ulysses S. Grant."
        },
        {
            "p": "When this battle began, the Union commander was at his headquarters in Savannah, Tennessee, several miles downriver, and he rushed to the fighting by steamboat. A patrol sent out by Benjamin Prentiss had run into the Confederate army just before dawn.",
            "r": "For 10 points, name this April 1862 battle, where Albert Sidney Johnston’s Confederates surprised Ulysses S. Grant’s army."
        },
        {
            "p": "One commander in this battle was shot in the leg near a peach orchard and died within an hour, making him the highest-ranking officer on either side killed in the Civil War. His second-in-command, P. G. T. Beauregard [“BOH-ruh-gard”], called off the attack at nightfall.",
            "r": "That commander was Albert Sidney Johnston. For 10 points, name this April 1862 battle in Tennessee."
        },
        {
            "p": "A Union division under Lew Wallace marched on the wrong road during the first day of this battle and arrived only as night fell, angering the commanding general. Wallace later became famous as the author of the novel _Ben-Hur_.",
            "r": "Reinforcements under Don Carlos Buell also began arriving that evening. For 10 points, name this battle that Ulysses S. Grant won on April 7, 1862."
        },
        {
            "p": "In his memoirs, the winning general of this battle wrote that afterward he “gave up all idea of saving the Union except by complete conquest.” On the rainy night after its first day, that general told William Tecumseh Sherman, “Lick ’em tomorrow, though.”",
            "r": "For 10 points, name this April 1862 battle in Tennessee, won by Ulysses S. Grant."
        },
        {
            "p": "During the night after this battle’s first day, the Union gunboats _Tyler_ and _Lexington_ fired shells toward the Confederate lines to keep the enemy from resting. By then, the Union army had been pushed back to a steamboat landing on the Tennessee River.",
            "r": "For 10 points, name this April 1862 battle, where Ulysses S. Grant’s army was surprised by Albert Sidney Johnston."
        },
        {
            "p": "John Wesley Powell, who later led a famous boat expedition through the Grand Canyon, lost his right arm while commanding artillery in this battle. In this battle, Union troops held out for hours along a sunken road before they were surrounded.",
            "r": "That position was nicknamed the Hornet’s Nest. For 10 points, name this April 1862 battle in Tennessee won by Ulysses S. Grant."
        },
        {
            "p": "Before this battle, Confederate forces gathered at the railroad junction of Corinth, Mississippi, after losing Forts Henry and Donelson earlier that year. They marched north from Corinth to strike the enemy before Don Carlos Buell’s army could arrive.",
            "r": "For 10 points, name this battle in which Albert Sidney Johnston was killed while attacking Ulysses S. Grant’s army in April 1862."
        },
        {
            "p": "After this battle, Abraham Lincoln supposedly defended its winning general against critics by saying, “I can’t spare this man; he fights.” This battle’s nearly 24,000 casualties made it the bloodiest battle in American history up to that time.",
            "r": "That general was Ulysses S. Grant. For 10 points, name this April 1862 battle in Tennessee."
        },
        {
            "p": "Shelby Foote, later known for his storytelling in Ken Burns’s documentary _The Civil War_, wrote a 1952 novel named for this battle. Southerners named this battle for a small log church whose Hebrew name is often translated as “place of peace.”",
            "r": "Northerners named it for a nearby steamboat landing. For 10 points, name this April 1862 battle in Tennessee."
        },
        {
            "p": "On the first morning of this battle, William Tecumseh Sherman’s division was caught by surprise near a log church, and Sherman was wounded in the hand. Sherman had dismissed warnings that a large Confederate army was nearby.",
            "r": "For 10 points, name this April 1862 battle where Confederates under Albert Sidney Johnston surprised Ulysses S. Grant’s army."
        },
        {
            "p": "On the second day of this battle, fresh troops from Don Carlos Buell’s Army of the Ohio joined a Union counterattack that drove the Confederates back toward Corinth. The night before, P. G. T. Beauregard [“BOH-ruh-gard”] had sent a message to Richmond claiming a complete victory.",
            "r": "For 10 points, name this April 1862 battle in Tennessee, where Ulysses S. Grant’s army recovered from a surprise attack."
        }
    ],
    "clues": [
        {
            "id": "april-1862",
            "tier": "giveaway",
            "t": "Fought April 6–7, 1862, in southwestern Tennessee, beside the Tennessee River",
            "k": ["april 1862", "tennessee", "1862"],
            "n": 0
        },
        {
            "id": "grant",
            "tier": "giveaway",
            "t": "Ulysses S. Grant’s Union army was surprised on the first day but won on the second",
            "k": ["ulysses s. grant", "grant", "surprised"],
            "n": 0,
            "rabbit": "Ulysses S. Grant"
        },
        {
            "id": "johnston",
            "tier": "giveaway",
            "t": "Confederate commander Albert Sidney Johnston was killed, the highest-ranking officer on either side to die in the war",
            "k": ["albert sidney johnston", "johnston", "highest-ranking"],
            "n": 0
        },
        {
            "id": "two-names",
            "tier": "middle",
            "t": "Southerners named it for a log church (a Hebrew name often translated “place of peace”); Northerners named it for a steamboat landing",
            "k": ["log church", "place of peace", "steamboat landing", "church"],
            "n": 0
        },
        {
            "id": "hornets-nest",
            "tier": "middle",
            "t": "Union troops held the “Hornet’s Nest” along a sunken road for hours, until Benjamin Prentiss surrendered more than 2,000 men",
            "k": ["hornet’s nest", "hornets nest", "sunken road", "prentiss"],
            "n": 0
        },
        {
            "id": "beauregard",
            "tier": "middle",
            "t": "P. G. T. Beauregard took over after Johnston died and halted the attack at nightfall",
            "k": ["beauregard", "nightfall", "took over"],
            "n": 0
        },
        {
            "id": "buell",
            "tier": "middle",
            "t": "Don Carlos Buell’s Army of the Ohio arrived that evening and overnight, and helped Grant win on April 7",
            "k": ["don carlos buell", "buell", "army of the ohio"],
            "n": 0
        },
        {
            "id": "casualties",
            "tier": "middle",
            "t": "Nearly 24,000 casualties: the bloodiest battle in American history up to that time",
            "k": ["24,000", "bloodiest", "casualties"],
            "n": 0
        },
        {
            "id": "sherman",
            "tier": "middle",
            "t": "William Tecumseh Sherman’s division was surprised near the church; Sherman was wounded in the hand",
            "k": ["william tecumseh sherman", "sherman", "wounded in the hand"],
            "n": 0,
            "rabbit": "William Tecumseh Sherman"
        },
        {
            "id": "corinth",
            "tier": "middle",
            "t": "The Confederates marched from the railroad junction of Corinth, Mississippi, and retreated there afterward",
            "k": ["corinth", "mississippi", "railroad junction"],
            "n": 0
        },
        {
            "id": "ben-hur",
            "tier": "power",
            "t": "Lew Wallace’s division took the wrong road and arrived as night fell; Wallace later wrote the novel _Ben-Hur_",
            "k": ["lew wallace", "ben-hur", "wrong road"],
            "n": 0
        },
        {
            "id": "lick-em",
            "tier": "power",
            "t": "On the rainy first night, Grant told Sherman, “Lick ’em tomorrow, though”",
            "k": ["lick ’em tomorrow", "lick em", "tomorrow"],
            "n": 0
        },
        {
            "id": "complete-conquest",
            "tier": "power",
            "t": "Grant’s memoirs: afterward he “gave up all idea of saving the Union except by complete conquest”",
            "k": ["complete conquest", "memoirs", "conquest"],
            "n": 0
        },
        {
            "id": "peach-orchard",
            "tier": "power",
            "t": "Johnston was shot in the leg near a peach orchard and died within an hour",
            "k": ["peach orchard", "peach", "leg"],
            "n": 0
        },
        {
            "id": "gunboats",
            "tier": "power",
            "t": "The Union gunboats _Tyler_ and _Lexington_ fired shells toward the Confederate lines through the night",
            "k": ["gunboats", "tyler", "lexington"],
            "n": 0
        },
        {
            "id": "ruggles",
            "tier": "power",
            "t": "Daniel Ruggles gathered dozens of Confederate cannons to pound the Hornet’s Nest",
            "k": ["ruggles", "cannons", "dozens"],
            "n": 0
        },
        {
            "id": "savannah",
            "tier": "power",
            "t": "Grant was at his headquarters in Savannah, Tennessee, when it began; a patrol from Prentiss’s division found the Confederates before dawn",
            "k": ["savannah", "headquarters", "patrol"],
            "n": 0
        },
        {
            "id": "halleck",
            "tier": "power",
            "t": "Afterward, Henry Halleck took command and crept toward Corinth, which the Confederates abandoned in late May 1862",
            "k": ["halleck", "henry halleck", "late may"],
            "n": 0
        },
        {
            "id": "spare-this-man",
            "tier": "power",
            "t": "Lincoln supposedly defended Grant afterward: “I can’t spare this man; he fights”",
            "k": ["spare this man", "he fights", "lincoln"],
            "n": 0
        },
        {
            "id": "stanley",
            "tier": "power",
            "t": "Henry Morton Stanley, who later found David Livingstone in Africa, fought for the Confederacy and was captured",
            "k": ["henry morton stanley", "stanley", "livingstone"],
            "n": 0
        },
        {
            "id": "bierce",
            "tier": "power",
            "t": "Union soldier Ambrose Bierce later wrote a memoir essay about what he saw there",
            "k": ["ambrose bierce", "bierce", "memoir essay"],
            "n": 0
        },
        {
            "id": "powell",
            "tier": "power",
            "t": "John Wesley Powell, later famous for exploring the Grand Canyon by boat, lost his right arm there",
            "k": ["john wesley powell", "powell", "grand canyon"],
            "n": 0
        },
        {
            "id": "bradbury",
            "tier": "power",
            "t": "Ray Bradbury’s short story about a young drummer named Joby takes place the night before it",
            "k": ["ray bradbury", "bradbury", "drummer", "joby"],
            "n": 0
        },
        {
            "id": "melville-foote",
            "tier": "power",
            "t": "Herman Melville wrote a requiem poem for its dead (swallows over the “forest-field”); Shelby Foote wrote a 1952 novel about it",
            "k": ["melville", "requiem", "shelby foote", "swallows"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Same names, different battles",
        "body": "Shiloh had a Sunken Road and a Peach Orchard, but so did other famous battles: Antietam’s Sunken Road became “Bloody Lane,” and Gettysburg had its own Peach Orchard. Shiloh also gets mixed up with Ulysses S. Grant’s other Western victories, Fort Donelson (February 1862), where he demanded “unconditional surrender,” and the Siege of Vicksburg (1863). The two sides even used different names for this battle.",
        "fix": "Listen for April 1862, Tennessee, a log church, the Hornet’s Nest, Albert Sidney Johnston’s death, Beauregard, Buell, and Lew Wallace. Both names, Shiloh (the Southern name, after the church) and Pittsburg Landing (the Northern name, after the steamboat landing), are correct.",
        "line": "Real answer line: Battle of <b><u>Shiloh</u></b> (or Battle of <b><u>Pittsburg Landing</u></b>)"
    },
    "tests": {
        "right": [
            "Shiloh",
            "Battle of Shiloh",
            "Pittsburg Landing",
            "Battle of Pittsburgh Landing",
            "Shilo",
            "Shiloh Church"
        ],
        "prompt": [],
        "wrong": [
            "Fort Donelson",
            "Antietam",
            "Vicksburg",
            "Corinth",
            "Gettysburg",
            "Chickamauga",
            "Hornet's Nest"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
