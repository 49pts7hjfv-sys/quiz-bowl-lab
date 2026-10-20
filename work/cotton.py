import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

data = {
    "id": "cotton",
    "name": "Cotton",
    "mono": "CTN",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Fiber crop that ruled the antebellum South · Whitney’s gin and “King Cotton”",
    "dates": "Gin invented 1793",
    "briefing": "In 1793, Eli Whitney built a simple machine, the cotton gin, that pulled the sticky seeds out of cotton fibers far faster than hands could. Growing cotton suddenly paid huge profits, and planters forced enslaved people to clear and work new fields from Georgia to Texas; by 1860, nearly 4 million people were enslaved in the United States. Southerners boasted that “Cotton is King,” and the crop fed textile mills from Massachusetts to England.",
    "answerHtml": "<b><u>Cotton</u></b> (accept <u>Gossypium</u>; prompt on “cash crop”; do not accept “cotton gin”)",
    "accept": [
        "cotton",
        "cotton plant",
        "cotton plants",
        "cotton crop",
        "raw cotton",
        "cotton fiber",
        "king cotton",
        "gossypium"
    ],
    "prompt": [
        "cash crop",
        "fiber",
        "fibre",
        "plant fiber"
    ],
    "reject": [
        "cotton gin",
        "gin",
        "cotton mill",
        "cotton mills",
        "cotton mather",
        "cotton club",
        "cotton candy",
        "cottonmouth",
        "tobacco",
        "indigo",
        "rice",
        "sugar",
        "sugarcane",
        "sugar cane",
        "hemp",
        "flax",
        "linen",
        "wool",
        "silk",
        "jute",
        "corn",
        "wheat",
        "peanuts",
        "peanut",
        "cellulose",
        "boll weevil",
        "eli whitney",
        "whitney",
        "kapok"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Cotton",
    "qb": {
        "q": "cotton",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "At Mulberry Grove, a Georgia plantation owned by Catharine Greene, a young Yale graduate built a machine whose wire teeth pulled the fibers of this plant through slots too narrow for its seeds. Planters across the South soon copied that 1793 invention, so its inventor earned little from it.",
            "r": "That machine was Eli Whitney’s gin. For 10 points, name this fiber crop that became the South’s most valuable export."
        },
        {
            "p": "In an 1858 speech, Senator James Henry Hammond of South Carolina warned Northerners, “You dare not make war” on this crop, claiming that no power on earth would dare to. His speech helped popularize a famous slogan of the antebellum South.",
            "r": "That slogan declared this crop “King.” For 10 points, name this crop whose seeds were removed by Eli Whitney’s gin."
        },
        {
            "p": "During the American Civil War, textile mills in Lancashire, England, ran so short of this raw material that hundreds of thousands of workers lost their jobs or had their hours cut. In 1863, Abraham Lincoln wrote to the workingmen of Manchester to thank them for supporting the Union despite their hardship.",
            "r": "Britain found new supplies in Egypt and India. For 10 points, name this crop that the Confederacy hoped would force Britain to support it."
        },
        {
            "p": "In 1919, the town of Enterprise, Alabama, put up a monument to a pest that had destroyed so much of this crop that local farmers switched to growing peanuts. That beetle had crossed from Mexico into Texas in the 1890s.",
            "r": "That pest was the boll weevil. For 10 points, name this crop that enslaved people were forced to plant and pick across the Deep South."
        },
        {
            "p": "Samuel Slater memorized the designs of British spinning machines and built a water-powered mill in Pawtucket, Rhode Island, to spin this fiber into thread. Decades later, the Boston Associates built huge mills in Lowell, Massachusetts, where young “mill girls” wove it into cloth.",
            "r": "For 10 points, name this fiber, picked by enslaved workers in the South and spun in Northern textile mills."
        },
        {
            "p": "In the 1840s, Massachusetts Whigs split between “Conscience Whigs,” who opposed slavery, and a faction close to factory owners, nicknamed for the raw material their mills bought from Southern plantations. Conscience Whigs said that faction put business ties with the South ahead of opposing slavery.",
            "r": "Charles Sumner was a Conscience Whig. For 10 points, name this crop, whose seeds were removed by Eli Whitney’s gin."
        },
        {
            "p": "Edgar Degas [“day-GAH”] painted his uncle’s New Orleans business in 1873, showing men in top hats reading a newspaper and examining samples of this white fiber spread on a table. New Orleans was a leading port for shipping this crop to mills in Europe.",
            "r": "Eli Whitney’s gin removed its seeds. For 10 points, name this crop, the South’s most valuable export before the Civil War."
        },
        {
            "p": "Mohandas Gandhi urged Indians to spin their own thread on a spinning wheel called a charkha [“CHAR-kuh”] and to wear homespun khadi [“KAH-dee”] cloth instead of cloth woven from this fiber in British mills. Much of the raw material for those British mills had come from the American South.",
            "r": "Its fluffy fibers grow in a boll around the seeds. For 10 points, name this crop cleaned by Eli Whitney’s 1793 gin."
        },
        {
            "p": "Soviet planners diverted the rivers that fed the Aral Sea to irrigate huge fields of this thirsty crop in Central Asia, and the sea shrank to a fraction of its former size. The Indus Valley civilization wove some of the oldest known cloth from this plant.",
            "r": "In the United States, it was the leading crop of the Deep South. For 10 points, name this fiber cleaned by Eli Whitney’s gin."
        },
        {
            "p": "Solomon Northup described how enslaved workers on Edwin Epps’s Louisiana plantation had to pick this crop from dawn to dark and were punished if their baskets weighed too little. Northup told that story in his 1853 memoir _Twelve Years a Slave_.",
            "r": "For 10 points, name this crop whose spread after the invention of Eli Whitney’s gin made slavery grow across the Deep South."
        },
        {
            "p": "James Hargreaves’s spinning jenny and Richard Arkwright’s water frame were used to spin thread from this fiber, helping to start the Industrial Revolution in Britain. Manchester, England, became the world’s leading center for turning it into cloth.",
            "r": "Much of Manchester’s raw supply came from the American South. For 10 points, name this crop cleaned by Eli Whitney’s gin."
        },
        {
            "p": "In 1861, many Southerners refused to ship this crop to Europe, hoping that shortages would pressure Britain and France into recognizing the Confederacy. That plan failed, partly because British warehouses already held large supplies from earlier bumper harvests.",
            "r": "Southerners had boasted that this crop was “King.” For 10 points, name this crop that dominated the economy of the antebellum South."
        },
        {
            "p": "George Washington Carver taught Southern farmers to rotate this soil-exhausting crop with peanuts and sweet potatoes. After the Civil War, many sharecroppers grew this crop and fell deep into debt under the crop-lien system.",
            "r": "For 10 points, name this crop picked by hand across the Deep South, whose seeds were removed by Eli Whitney’s gin."
        },
        {
            "p": "By 1860, this crop made up more than half of all U.S. exports by value. Its fields had spread west from South Carolina and Georgia across Alabama and Mississippi all the way to Texas, with some of the richest land in the Mississippi Delta.",
            "r": "Nearly four million people were enslaved in the South by then. For 10 points, name this cash crop, whose seeds were removed by Eli Whitney’s gin."
        },
        {
            "p": "Long-staple varieties of this plant grew well on the Sea Islands off Georgia and South Carolina, but short-staple upland varieties had sticky green seeds that were very hard to remove by hand. This shrub belongs to the mallow family, and its fibers are about 90 percent cellulose.",
            "r": "For 10 points, name this crop, whose fibers grow inside a boll and were cleaned by Eli Whitney’s gin."
        }
    ],
    "clues": [
        {
            "id": "gin",
            "tier": "giveaway",
            "t": "Eli Whitney’s gin (1793) quickly pulled the seeds out of its fibers",
            "k": ["eli whitney", "seeds", "1793", "gin"],
            "n": 0,
            "rabbit": "Eli Whitney"
        },
        {
            "id": "slavery",
            "tier": "giveaway",
            "t": "Its spread across the Deep South made slavery grow; nearly 4 million people were enslaved by 1860",
            "k": ["slavery", "enslaved", "deep south", "4 million"],
            "n": 0
        },
        {
            "id": "cash-crop",
            "tier": "giveaway",
            "t": "The South’s main cash crop; its fluffy white fibers grow in a boll around the seeds",
            "k": ["cash crop", "boll", "fibers"],
            "n": 0
        },
        {
            "id": "king",
            "tier": "giveaway",
            "t": "Southerners boasted that it was “King” of the antebellum economy",
            "k": ["king", "slogan"],
            "n": 0
        },
        {
            "id": "mills",
            "tier": "giveaway",
            "t": "Spun and woven into cloth in textile mills in New England and Britain",
            "k": ["textile mills", "cloth", "new england"],
            "n": 0
        },
        {
            "id": "boll-weevil",
            "tier": "middle",
            "t": "The boll weevil, a beetle from Mexico, reached Texas in the 1890s and ruined crops across the South",
            "k": ["boll weevil", "weevil", "beetle"],
            "n": 0
        },
        {
            "id": "lowell",
            "tier": "middle",
            "t": "Lowell, Massachusetts: young “mill girls” worked in its textile mills and published the _Lowell Offering_",
            "k": ["lowell offering", "mill girls", "lowell"],
            "n": 0
        },
        {
            "id": "slater",
            "tier": "middle",
            "t": "Samuel Slater, “Father of the American Industrial Revolution,” built a spinning mill in Pawtucket, Rhode Island",
            "k": ["samuel slater", "slater", "pawtucket"],
            "n": 0
        },
        {
            "id": "diplomacy",
            "tier": "middle",
            "t": "The Confederacy held it back in 1861 to win British support, but Britain had stockpiles and found new sources in Egypt and India",
            "k": ["confederacy", "stockpiles", "egypt", "india"],
            "n": 0
        },
        {
            "id": "carver",
            "tier": "middle",
            "t": "George Washington Carver taught farmers to rotate it with peanuts and sweet potatoes to restore the soil",
            "k": ["george washington carver", "carver", "peanuts", "sweet potatoes"],
            "n": 0
        },
        {
            "id": "sharecropping",
            "tier": "middle",
            "t": "After the Civil War, many sharecroppers grew it and fell into debt under the crop-lien system",
            "k": ["sharecroppers", "crop-lien", "debt"],
            "n": 0
        },
        {
            "id": "staple-types",
            "tier": "middle",
            "t": "The gin made short-staple “upland” types profitable; long-staple types grew on the Sea Islands",
            "k": ["short-staple", "upland", "sea islands", "long-staple"],
            "n": 0
        },
        {
            "id": "hammond",
            "tier": "middle",
            "t": "Senator James Henry Hammond (1858): “You dare not make war” on it, because it “is king”",
            "k": ["hammond", "make war", "1858"],
            "n": 0
        },
        {
            "id": "lancashire",
            "tier": "power",
            "t": "Lancashire “famine” (1861–1865): British mills ran short during the Civil War; Lincoln thanked the workingmen of Manchester (1863)",
            "k": ["lancashire", "workingmen", "famine"],
            "n": 0
        },
        {
            "id": "enterprise",
            "tier": "power",
            "t": "Enterprise, Alabama, built a monument to the boll weevil (1919) for pushing farmers to grow peanuts",
            "k": ["enterprise", "monument", "1919"],
            "n": 0
        },
        {
            "id": "mallow",
            "tier": "power",
            "t": "A shrub in the mallow family; its fibers are about 90 percent cellulose",
            "k": ["mallow", "cellulose", "shrub"],
            "n": 0,
            "rabbit": "Cellulose"
        },
        {
            "id": "mulberry-grove",
            "tier": "power",
            "t": "Whitney built the gin at Mulberry Grove, the Georgia plantation of Catharine Greene, widow of General Nathanael Greene",
            "k": ["mulberry grove", "catharine greene", "nathanael greene"],
            "n": 0
        },
        {
            "id": "mechanism",
            "tier": "power",
            "t": "The gin’s wire teeth pulled fibers through slots too narrow for the seeds; Whitney earned little because planters copied it",
            "k": ["wire teeth", "slots", "copied"],
            "n": 0
        },
        {
            "id": "exports",
            "tier": "power",
            "t": "By 1860 it made up more than half of all U.S. exports by value",
            "k": ["exports", "half", "1860"],
            "n": 0
        },
        {
            "id": "whigs",
            "tier": "power",
            "t": "In the 1840s, Massachusetts Whigs tied to the mills, nicknamed for this crop, split from the antislavery “Conscience Whigs” like Charles Sumner",
            "k": ["conscience whigs", "whigs", "sumner"],
            "n": 0
        },
        {
            "id": "degas",
            "tier": "power",
            "t": "Edgar Degas painted his uncle’s New Orleans office, where buyers examined samples of it (1873)",
            "k": ["degas", "new orleans", "office"],
            "n": 0
        },
        {
            "id": "gandhi",
            "tier": "power",
            "t": "Mohandas Gandhi spun thread on a charkha and wore homespun khadi to protest cloth made in British mills",
            "k": ["gandhi", "khadi", "charkha"],
            "n": 0
        },
        {
            "id": "aral-sea",
            "tier": "power",
            "t": "Soviet irrigation of Central Asian fields of it drained much of the Aral Sea",
            "k": ["aral sea", "soviet", "central asian"],
            "n": 0
        },
        {
            "id": "northup",
            "tier": "power",
            "t": "Solomon Northup described picking it on Edwin Epps’s Louisiana plantation in _Twelve Years a Slave_ (1853)",
            "k": ["solomon northup", "twelve years a slave", "epps"],
            "n": 0
        },
        {
            "id": "inventions",
            "tier": "power",
            "t": "Britain’s spinning jenny (Hargreaves) and water frame (Arkwright) spun it into thread; Manchester led the world in weaving it",
            "k": ["spinning jenny", "water frame", "arkwright", "manchester"],
            "n": 0
        },
        {
            "id": "indus",
            "tier": "power",
            "t": "The Indus Valley civilization wove some of the oldest known cloth from it",
            "k": ["indus valley", "indus"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Crop, machine, or inventor?",
        "body": "Tossups on cotton, on Eli Whitney, and on the cotton gin share the same clues: Mulberry Grove, wire teeth, sticky seeds, and the spread of slavery. If the question asks for “this crop” or “this plant,” answering “cotton gin” is wrong. Other Southern cash crops can trick you too: tobacco saved Jamestown, Eliza Lucas Pinckney grew indigo in South Carolina, and rice and sugar grew in the Carolinas and Louisiana.",
        "fix": "Listen for the noun: “this crop,” “this fiber,” or “this plant” wants cotton; “this machine” or “this device” wants the cotton gin; “this inventor” wants Eli Whitney. Boll weevils, “King,” the Lowell mills, and Lancashire all point to cotton.",
        "line": "Real answer line: <b><u>Cotton</u></b> (accept <u>Gossypium</u>; prompt on “cash crop”; do not accept “cotton gin”)"
    },
    "tests": {
        "right": [
            "Cotton",
            "cotton plant",
            "Gossypium",
            "King Cotton",
            "coton"
        ],
        "prompt": [
            "cash crop"
        ],
        "wrong": [
            "cotton gin",
            "tobacco",
            "indigo",
            "Cotton Mather",
            "rice",
            "cellulose",
            "Eli Whitney"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
