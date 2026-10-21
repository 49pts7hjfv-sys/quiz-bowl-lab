import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "first-battle-of-bull-run",
    "name": "First Battle of Bull Run",
    "mono": "BR1",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "First major land battle of the Civil War · Where “Stonewall” got his name",
    "dates": "Fought July 21, 1861",
    "briefing": "On July 21, 1861, two armies made up mostly of untrained volunteers clashed along a Virginia stream called Bull Run, near the railroad town of Manassas Junction. Congressmen and other sightseers rode out from Washington, D.C., to watch, but Confederate reinforcements arriving by train turned the battle into a panicked Union retreat. It was the first major land battle of the Civil War, and it gave Thomas Jackson his famous nickname, “Stonewall.”",
    "answerHtml": "<b><u>First</u></b> Battle of <b><u>Bull Run</u></b> (or <b><u>First</u></b> Battle of <b><u>Manassas</u></b>; prompt on <u>Bull Run</u> or <u>Manassas</u> alone; do not accept “Second Bull Run” or “Second Manassas”)",
    "accept": [
        "first battle of bull run",
        "first bull run",
        "1st bull run",
        "1st battle of bull run",
        "battle of first bull run",
        "first battle of manassas",
        "first manassas",
        "1st manassas",
        "1st battle of manassas",
        "battle of first manassas"
    ],
    "prompt": [
        "bull run",
        "battle of bull run",
        "the battle of bull run",
        "manassas",
        "battle of manassas",
        "the battle of manassas"
    ],
    "reject": [
        "second battle of bull run",
        "second bull run",
        "2nd bull run",
        "2nd battle of bull run",
        "bull run 2",
        "bull run ii",
        "second battle of manassas",
        "second manassas",
        "2nd manassas",
        "2nd battle of manassas",
        "manassas 2",
        "manassas ii",
        "battle of antietam",
        "antietam",
        "sharpsburg",
        "battle of fort sumter",
        "fort sumter",
        "battle of gettysburg",
        "gettysburg",
        "battle of shiloh",
        "shiloh",
        "fredericksburg",
        "chancellorsville",
        "balls bluff",
        "battle of balls bluff",
        "wilsons creek",
        "battle of wilsons creek",
        "big bethel",
        "battle of big bethel",
        "blackburns ford",
        "battle of blackburns ford",
        "henry house hill",
        "peninsula campaign",
        "seven days battles",
        "american civil war",
        "civil war"
    ],
    "mediaPending": True,
    "media": [],
    "wiki": "https://en.wikipedia.org/wiki/First_Battle_of_Bull_Run",
    "qb": {
        "q": "Bull Run",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Abraham Lincoln told the Union commander in this battle, “You are green, it is true, but they are green also; you are all green alike,” when that general worried that his volunteers were not ready to fight. Northern newspapers had been demanding a quick march on Richmond.",
            "r": "That general, Irvin McDowell, lost this battle. For 10 points, name this July 1861 Confederate victory, the first major land battle of the Civil War."
        },
        {
            "p": "Union general Robert Patterson was supposed to keep Joseph E. Johnston’s army pinned down in the Shenandoah Valley, but Johnston slipped away and sent most of his men to this battle by railroad. Those troops arrived in time to help turn this battle into a Confederate victory.",
            "r": "For 10 points, name this July 1861 battle near Manassas Junction, Virginia, where Thomas Jackson earned the nickname “Stonewall.”"
        },
        {
            "p": "South Carolina general Barnard Bee was mortally wounded in this battle soon after rallying his men by pointing to a Virginia brigade that was holding firm on Henry House Hill. That brigade’s commander had taught at the Virginia Military Institute before the war.",
            "r": "Bee reportedly said that commander was “standing like a stone wall,” giving Thomas Jackson his nickname. For 10 points, name this first major land battle of the Civil War."
        },
        {
            "p": "New York congressman Alfred Ely was captured by Confederate soldiers and held in Richmond for months after he rode out from Washington to watch this battle. During the Union retreat, a Confederate shell overturned a wagon on a bridge over Cub Run, blocking the road back to Washington.",
            "r": "Sightseers who had come to watch, some with picnic baskets, were caught in the panic. For 10 points, name this July 1861 Union defeat near Manassas, Virginia."
        },
        {
            "p": "Before this battle, the Washington socialite Rose O’Neal Greenhow sent secret messages to Confederate general P. G. T. Beauregard [“BOH-ruh-gard”] warning him that the Union army was about to march toward his position. Detective Allan Pinkerton arrested her about a month after this battle.",
            "r": "Beauregard won this battle on July 21, 1861. For 10 points, name this first major land battle of the Civil War, fought near Manassas Junction, Virginia."
        },
        {
            "p": "One week before this battle, Major Sullivan Ballou of the 2nd Rhode Island wrote a loving farewell letter to his wife, Sarah. Ballou died of wounds he received in this battle, and his letter became famous when it was read in Ken Burns’s documentary _The Civil War_.",
            "r": "For 10 points, name this July 1861 battle, where Irvin McDowell’s Union army was defeated near Manassas, Virginia."
        },
        {
            "p": "Three days before this battle, a Union shell crashed into the kitchen of Wilmer McLean’s farmhouse, which a Confederate general was using as his headquarters. McLean later moved his family to a quiet village called Appomattox Court House, where Robert E. Lee surrendered in his parlor in 1865.",
            "r": "For 10 points, name this first major land battle of the Civil War, fought in July 1861 along a stream in northern Virginia."
        },
        {
            "p": "Judith Henry, an elderly widow who was too sick to leave her bed, became the only civilian killed in this battle when artillery fire struck her house. Her family’s farm sat on a hilltop where Confederate troops regrouped and held their ground during the afternoon.",
            "r": "On that hill, Thomas Jackson earned the nickname “Stonewall.” For 10 points, name this July 1861 battle, the first major land battle of the Civil War."
        },
        {
            "p": "Future generals William Tecumseh Sherman and Ambrose Burnside each led a Union brigade in this battle. While some Union troops staged a fake attack at the Stone Bridge, others marched around to cross the stream at Sudley Springs and strike the Confederate left flank.",
            "r": "That attack went well at first but failed when Confederate reinforcements arrived. For 10 points, name this July 1861 battle, a Union defeat near Manassas Junction, Virginia."
        },
        {
            "p": "Many Union soldiers in this battle had signed up for only 90 days, and the 4th Pennsylvania Infantry headed home on the eve of this battle because its time was up. Their commander felt pushed to attack before more of his volunteers’ terms ran out.",
            "r": "That commander was Irvin McDowell. For 10 points, name this July 1861 battle where Thomas Jackson earned the nickname “Stonewall.”"
        },
        {
            "p": "In this battle, J. E. B. Stuart’s cavalry charged the 11th New York Fire Zouaves, a regiment made up largely of New York City firefighters. Nearby, Union gunners held their fire against an approaching Virginia regiment that they mistook for friendly troops, then lost their cannons.",
            "r": "Soldiers on both sides wore many different uniforms in this early battle. For 10 points, name this first major land battle of the Civil War, which ended with a Union retreat toward Washington."
        },
        {
            "p": "Confederate president Jefferson Davis took a train from Richmond and reached the field as this battle was ending. Afterward, Confederate generals designed a separate battle flag, because their first national flag, the “Stars and Bars,” had looked too much like the U.S. flag in the smoke of this battle.",
            "r": "For 10 points, name this battle of July 21, 1861, where Irvin McDowell’s Union army was routed near Manassas Junction."
        },
        {
            "p": "Horace Greeley’s _New-York Tribune_ printed the slogan “Forward to Richmond!” day after day, demanding that the Union army capture the Confederate capital before the Confederate Congress could meet there on July 20. That pressure helped push the Union army south into this battle.",
            "r": "For 10 points, name this July 1861 battle along a Virginia stream, the first major land battle of the Civil War."
        },
        {
            "p": "The day after this battle, Abraham Lincoln summoned George McClellan to Washington to take command of the beaten army, which McClellan rebuilt as the Army of the Potomac. Northerners who had expected a short war began preparing for a long one.",
            "r": "McClellan replaced Irvin McDowell, who had lost this battle. For 10 points, name this July 1861 battle near Manassas, Virginia."
        },
        {
            "p": "On July 18, 1861, Union troops probing the Confederate defenses were driven back in a skirmish at Blackburn’s Ford. That setback convinced the Union commander to send his main force on a long march around the Confederate left flank in this larger battle three days later.",
            "r": "Nearly 5,000 soldiers were killed, wounded, captured, or missing in this battle. For 10 points, name this July 1861 Confederate victory near Manassas Junction, Virginia."
        }
    ],
    "clues": [
        {
            "id": "first-major",
            "tier": "giveaway",
            "t": "The first major land battle of the Civil War, fought on July 21, 1861",
            "k": ["first major", "july 21, 1861", "land battle", "1861"],
            "n": 0
        },
        {
            "id": "manassas",
            "tier": "giveaway",
            "t": "Fought along a stream near Manassas Junction, Virginia; Confederates named it for the railroad town",
            "k": ["manassas junction", "manassas", "virginia", "stream"],
            "n": 0
        },
        {
            "id": "stonewall",
            "tier": "giveaway",
            "t": "Thomas Jackson earned the nickname “Stonewall” there",
            "k": ["stonewall", "thomas jackson", "jackson"],
            "n": 0,
            "rabbit": "Stonewall Jackson"
        },
        {
            "id": "confederate-victory",
            "tier": "giveaway",
            "t": "A Confederate victory; the Union army fled in a disorderly retreat toward Washington, D.C.",
            "k": ["confederate victory", "retreat", "washington"],
            "n": 0
        },
        {
            "id": "mcdowell",
            "tier": "middle",
            "t": "Union commander Irvin McDowell lost and was soon replaced by George McClellan, who built the Army of the Potomac",
            "k": ["irvin mcdowell", "mcdowell", "mcclellan", "army of the potomac"],
            "n": 0,
            "rabbit": "George McClellan"
        },
        {
            "id": "beauregard-johnston",
            "tier": "middle",
            "t": "Confederate commanders: P. G. T. Beauregard and Joseph E. Johnston",
            "k": ["beauregard", "joseph e. johnston", "johnston"],
            "n": 0
        },
        {
            "id": "railroad",
            "tier": "middle",
            "t": "Johnston’s troops came from the Shenandoah Valley by railroad and arrived in time to help win",
            "k": ["railroad", "shenandoah valley", "shenandoah", "train"],
            "n": 0
        },
        {
            "id": "sightseers",
            "tier": "middle",
            "t": "Congressmen and other sightseers rode out from Washington to watch, some with picnic baskets, and got caught in the retreat",
            "k": ["sightseers", "picnic", "congressmen", "spectators"],
            "n": 0
        },
        {
            "id": "bee",
            "tier": "middle",
            "t": "General Barnard Bee reportedly said Jackson was “standing like a stone wall” on Henry House Hill",
            "k": ["barnard bee", "stone wall", "henry house hill", "henry house"],
            "n": 0
        },
        {
            "id": "green-troops",
            "tier": "middle",
            "t": "Most soldiers on both sides were new, untrained volunteers wearing many different uniforms",
            "k": ["untrained", "volunteers", "uniforms"],
            "n": 0
        },
        {
            "id": "forward-to-richmond",
            "tier": "middle",
            "t": "Northern newspapers demanded “Forward to Richmond!”, pressuring the Union army to attack early",
            "k": ["forward to richmond", "richmond", "newspapers"],
            "n": 0
        },
        {
            "id": "long-war",
            "tier": "middle",
            "t": "Nearly 5,000 soldiers were killed, wounded, captured, or missing, and both sides realized the war would be long",
            "k": ["5,000", "long", "casualties"],
            "n": 0
        },
        {
            "id": "second-battle",
            "tier": "middle",
            "t": "A second battle was fought on the same ground in August 1862, when Robert E. Lee beat John Pope",
            "k": ["august 1862", "john pope", "second"],
            "n": 0,
            "rabbit": "Second Battle of Bull Run"
        },
        {
            "id": "green-alike",
            "tier": "power",
            "t": "Lincoln told McDowell, “You are green, it is true, but they are green also; you are all green alike”",
            "k": ["green alike", "green", "lincoln"],
            "n": 0
        },
        {
            "id": "patterson",
            "tier": "power",
            "t": "Union general Robert Patterson failed to keep Johnston pinned down in the Shenandoah Valley",
            "k": ["robert patterson", "patterson", "pinned down"],
            "n": 0
        },
        {
            "id": "greenhow",
            "tier": "power",
            "t": "The spy Rose O’Neal Greenhow sent Beauregard secret messages about the Union army’s plans; Allan Pinkerton later arrested her",
            "k": ["rose o’neal greenhow", "greenhow", "pinkerton", "spy"],
            "n": 0
        },
        {
            "id": "ballou",
            "tier": "power",
            "t": "Major Sullivan Ballou wrote a famous farewell letter to his wife, Sarah, a week before he died of wounds received there",
            "k": ["sullivan ballou", "ballou", "letter"],
            "n": 0
        },
        {
            "id": "mclean",
            "tier": "power",
            "t": "Three days before, a Union shell hit Wilmer McLean’s farmhouse, a Confederate headquarters; Lee later surrendered in McLean’s parlor at Appomattox",
            "k": ["wilmer mclean", "mclean", "appomattox"],
            "n": 0
        },
        {
            "id": "judith-henry",
            "tier": "power",
            "t": "Judith Henry, an elderly widow, was the only civilian killed, when artillery fire struck her house on Henry House Hill",
            "k": ["judith henry", "civilian", "widow"],
            "n": 0
        },
        {
            "id": "ely",
            "tier": "power",
            "t": "Congressman Alfred Ely of New York, who came to watch, was captured and held in Richmond for months",
            "k": ["alfred ely", "captured"],
            "n": 0
        },
        {
            "id": "sherman-burnside",
            "tier": "power",
            "t": "William Tecumseh Sherman and Ambrose Burnside each commanded a Union brigade",
            "k": ["sherman", "burnside", "brigade"],
            "n": 0
        },
        {
            "id": "flank-march",
            "tier": "power",
            "t": "Union troops faked an attack at the Stone Bridge while others crossed at Sudley Springs to hit the Confederate left flank",
            "k": ["stone bridge", "sudley springs", "flank"],
            "n": 0
        },
        {
            "id": "blackburns-ford",
            "tier": "power",
            "t": "A skirmish at Blackburn’s Ford on July 18 turned back a Union probe, so McDowell planned a flank march instead",
            "k": ["blackburn’s ford", "blackburns ford", "july 18"],
            "n": 0
        },
        {
            "id": "enlistments",
            "tier": "power",
            "t": "Many Union troops had 90-day enlistments; the 4th Pennsylvania went home on the eve of the battle",
            "k": ["90-day", "4th pennsylvania", "enlistments"],
            "n": 0
        },
        {
            "id": "stuart-zouaves",
            "tier": "power",
            "t": "J. E. B. Stuart’s cavalry charged the 11th New York Fire Zouaves; Union gunners lost their cannons after mistaking Virginians for friends",
            "k": ["fire zouaves", "zouaves", "j. e. b. stuart", "stuart"],
            "n": 0
        },
        {
            "id": "davis-flag",
            "tier": "power",
            "t": "Jefferson Davis arrived by train as the fighting ended; confusion between the “Stars and Bars” and the U.S. flag led to a separate Confederate battle flag",
            "k": ["jefferson davis", "stars and bars", "battle flag"],
            "n": 0
        }
    ],
    "trap": {
        "title": "First or Second?",
        "body": "Two big battles were fought along the same Virginia stream near Manassas Junction: the first in July 1861, and the second in August 1862, when Robert E. Lee and Stonewall Jackson beat John Pope. Union armies usually named battles after streams and Confederates after towns, so each battle has two names, Bull Run and Manassas. Saying just “Bull Run” or “Manassas” earns a prompt, and “Second Bull Run” is wrong.",
        "fix": "Listen for the year and the generals: 1861, Irvin McDowell, sightseers from Washington, and the “Stonewall” nickname mean the first battle; 1862, John Pope, and Lee’s army mean the second. Always say “First” in front of Bull Run or Manassas.",
        "line": "Real answer line: <b><u>First</u></b> Battle of <b><u>Bull Run</u></b> (or <b><u>First</u></b> Battle of <b><u>Manassas</u></b>; prompt on <u>Bull Run</u> or <u>Manassas</u> alone; do not accept “Second Bull Run”)"
    },
    "tests": {
        "right": [
            "First Battle of Bull Run",
            "First Bull Run",
            "the first battle of bull run",
            "First Manassas",
            "First Battle of Manassas",
            "1st Bull Run",
            "First Batle of Bull Run"
        ],
        "prompt": [
            "Bull Run",
            "Manassas",
            "Battle of Bull Run",
            "the Battle of Manassas"
        ],
        "wrong": [
            "Second Battle of Bull Run",
            "Second Manassas",
            "2nd Bull Run",
            "Antietam",
            "Fort Sumter",
            "Gettysburg",
            "Shiloh",
            "Ball's Bluff"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", data["id"])
