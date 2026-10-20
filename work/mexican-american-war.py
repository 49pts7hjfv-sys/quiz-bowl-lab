import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "mexican-american-war",
    "name": "Mexican-American War",
    "mono": "MAW",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "U.S. war with Mexico, 1846–1848 · Won California and the Southwest",
    "dates": "Fought 1846–1848",
    "briefing": "In 1846, the United States and Mexico went to war over Texas’s southern border, and President James K. Polk also wanted California. American armies under Zachary Taylor and Winfield Scott won battle after battle, and Scott captured Mexico City in 1847. In the Treaty of Guadalupe Hidalgo, Mexico gave up California and most of the present-day Southwest, but arguments over whether slavery would spread there helped lead to the Civil War.",
    "answerHtml": "<b><u>Mexican-American War</u></b> (or <u>Mexican War</u> or <u>U.S.-Mexican War</u>; accept <u>Intervención Estadounidense en México</u>; do not accept “Spanish-American War”)",
    "accept": [
        "mexican american war",
        "mexican war",
        "us mexican war",
        "u s mexican war",
        "united states mexican war",
        "us mexico war",
        "u s mexico war",
        "war with mexico",
        "american mexican war",
        "intervencion estadounidense en mexico",
        "guerra de estados unidos mexico"
    ],
    "prompt": [],
    "reject": [
        "spanish american war",
        "mexican revolution",
        "texas revolution",
        "texan revolution",
        "texas war of independence",
        "mexican war of independence",
        "mexican independence",
        "franco mexican war",
        "french intervention in mexico",
        "pastry war",
        "war of 1812",
        "civil war",
        "american civil war",
        "battle of the alamo",
        "alamo",
        "punitive expedition",
        "mexican punitive expedition",
        "gadsden purchase",
        "treaty of guadalupe hidalgo",
        "mexican cession",
        "manifest destiny",
        "battle of san jacinto",
        "san jacinto"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Mexican%E2%80%93American_War",
    "qb": {
        "q": "Mexican-American War",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "This war began after Mexican cavalry attacked Captain Seth Thornton’s patrol of American soldiers in land claimed by both countries north of the Rio Grande. The American president then told Congress that the enemy had “shed American blood upon the American soil.”",
            "r": "That president was James K. Polk. For 10 points, name this war fought from 1846 to 1848 between the United States and its southern neighbor."
        },
        {
            "p": "Before this war, the Mexican government refused to meet with John Slidell, whom the American president had sent to offer millions of dollars for California and New Mexico. That president then ordered General Zachary Taylor to march his army to the Rio Grande, into land that both nations claimed.",
            "r": "For 10 points, name this war that President James K. Polk led against Mexico from 1846 to 1848."
        },
        {
            "p": "Early in this war, American cannons helped win the Battle of Palo Alto against Mariano Arista [“ah-REES-tuh”], and the Americans won again the next day at Resaca de la Palma [“reh-SAH-kuh day lah PAHL-muh”]. Nearby, an earthwork called Fort Texas was renamed for Major Jacob Brown, who died defending it.",
            "r": "Those victories were won by General Zachary Taylor. For 10 points, name this war that made Taylor a hero two years before he was elected president."
        },
        {
            "p": "Jefferson Davis led the Mississippi Rifles at the Battle of Buena Vista [“BWAY-nuh VEE-stuh”] in this war, where an American army held off a much larger force led by Antonio López de Santa Anna. Months earlier, the same American general had captured the city of Monterrey [“mon-teh-RAY”].",
            "r": "That general was Zachary Taylor, nicknamed “Old Rough and Ready.” For 10 points, name this war fought from 1846 to 1848."
        },
        {
            "p": "During this war, the U.S. Navy let an exiled general slip through its blockade and return home from Cuba, because the American president believed that general would help make peace. Instead, that general took command of his country’s army and fought against the United States.",
            "r": "That general was Antonio López de Santa Anna. For 10 points, name this war that ended with the Treaty of Guadalupe Hidalgo."
        },
        {
            "p": "In 1847, during this war, Winfield Scott landed thousands of soldiers on the beaches near Veracruz [“vair-uh-KROOZ”] in the first large-scale amphibious landing by U.S. forces. Scott then marched inland, roughly following the route that Hernán Cortés [“air-NAHN kor-TEZ”] had taken more than three centuries earlier.",
            "r": "Months later, Scott captured Mexico City. For 10 points, name this war fought under President James K. Polk."
        },
        {
            "p": "At the Battle of Cerro Gordo [“SAIR-oh GOR-doh”] in this war, an army engineer named Robert E. Lee found a path through rough ground that let American troops get around the enemy’s side. Ulysses S. Grant, George McClellan, and Thomas “Stonewall” Jackson also served as junior officers in this war.",
            "r": "Many of those officers later fought against each other in the Civil War. For 10 points, name this earlier war that the United States fought from 1846 to 1848."
        },
        {
            "p": "Mexico honors six young military cadets who died defending Chapultepec [“chah-POOL-teh-pek”] Castle in this war as the Niños Héroes [“NEEN-yohs AIR-oh-ays”], or “Boy Heroes.” U.S. Marines who stormed that castle are remembered in the line “From the Halls of Montezuma” in their hymn.",
            "r": "Right after that battle, American troops captured Mexico City. For 10 points, name this war that ended with the Treaty of Guadalupe Hidalgo."
        },
        {
            "p": "John Riley led the Saint Patrick’s Battalion, a unit of mostly Irish Catholic immigrants who left the U.S. Army and fought for the other side in this war. Many members of that battalion were captured at the Battle of Churubusco [“choo-roo-BOO-skoh”] near Mexico City.",
            "r": "They fought against the army of General Winfield Scott. For 10 points, name this war in which the United States won California and the Southwest."
        },
        {
            "p": "Early in this war, the Army of the West under Stephen Kearny [“KAR-nee”] marched from Fort Leavenworth and captured Santa Fe without a fight. Kearny then headed for California, where the explorer John C. Frémont had joined American settlers rising up against Mexican rule.",
            "r": "This war added California and New Mexico to the United States. For 10 points, name this war fought from 1846 to 1848."
        },
        {
            "p": "Pennsylvania congressman David Wilmot tried to ban slavery in any land the United States gained from this war. His proviso passed the House more than once but always failed in the Senate, and the fight over it split Northern and Southern lawmakers.",
            "r": "The argument over land won in this war led to the Compromise of 1850. For 10 points, name this war that ended in 1848."
        },
        {
            "p": "Henry David Thoreau spent a night in jail for refusing to pay a tax, partly to protest slavery and this war. He explained his actions in the essay “Resistance to Civil Government,” later known as “Civil Disobedience,” which inspired Mahatma Gandhi and Martin Luther King Jr.",
            "r": "For 10 points, name this war in which the United States gained a huge area from Mexico in 1848."
        },
        {
            "p": "A one-term Illinois congressman introduced the “Spot Resolutions,” demanding that the president name the exact spot where American blood had been shed on American soil to start this war. Many Whigs attacked this conflict as “Mr. Polk’s War.”",
            "r": "That congressman, Abraham Lincoln, later became president. For 10 points, name this war in which General Winfield Scott captured Mexico City."
        },
        {
            "p": "Nicholas Trist ignored orders calling him home and negotiated the treaty that ended this war. Under that treaty, the United States paid 15 million dollars for a vast area that included California, and the Rio Grande became the border of Texas.",
            "r": "That treaty was the Treaty of Guadalupe Hidalgo. For 10 points, name this war that ended in 1848."
        },
        {
            "p": "Ulysses S. Grant, who fought in this war as a young officer, later called it “one of the most unjust ever waged by a stronger against a weaker nation.” The poet James Russell Lowell attacked this war in _The Biglow Papers_, written in the voice of a New England farmer.",
            "r": "This war began after the United States annexed Texas. For 10 points, name this war fought from 1846 to 1848."
        }
    ],
    "clues": [
        {
            "id": "dates-sides",
            "tier": "giveaway",
            "t": "Fought from 1846 to 1848 between the United States and Mexico",
            "k": ["1846", "1848"],
            "n": 0
        },
        {
            "id": "polk",
            "tier": "giveaway",
            "t": "President James K. Polk led the U.S. into it, hoping to gain California",
            "k": ["james k. polk", "polk", "california"],
            "n": 0,
            "rabbit": "James K. Polk"
        },
        {
            "id": "guadalupe",
            "tier": "giveaway",
            "t": "Ended by the Treaty of Guadalupe Hidalgo (1848): Mexico gave up California and most of the Southwest (the Mexican Cession)",
            "k": ["guadalupe hidalgo", "mexican cession", "southwest"],
            "n": 0
        },
        {
            "id": "texas",
            "tier": "giveaway",
            "t": "Followed the U.S. annexation of Texas (1845) and a border dispute over the Rio Grande",
            "k": ["annexation", "texas", "rio grande"],
            "n": 0
        },
        {
            "id": "taylor",
            "tier": "middle",
            "t": "Zachary Taylor (“Old Rough and Ready”) won at Palo Alto, Monterrey, and Buena Vista, then was elected president (1848)",
            "k": ["zachary taylor", "rough and ready", "buena vista", "monterrey"],
            "n": 0
        },
        {
            "id": "scott",
            "tier": "middle",
            "t": "Winfield Scott landed at Veracruz and captured Mexico City (1847)",
            "k": ["winfield scott", "veracruz", "mexico city"],
            "n": 0
        },
        {
            "id": "santa-anna",
            "tier": "middle",
            "t": "Antonio López de Santa Anna led Mexico’s army",
            "k": ["santa anna"],
            "n": 0,
            "rabbit": "Antonio López de Santa Anna"
        },
        {
            "id": "wilmot",
            "tier": "middle",
            "t": "Wilmot Proviso (1846): tried to ban slavery in any land won from Mexico; passed the House but failed in the Senate",
            "k": ["wilmot proviso", "wilmot", "proviso"],
            "n": 0
        },
        {
            "id": "spot",
            "tier": "middle",
            "t": "Congressman Abraham Lincoln’s “Spot Resolutions” challenged Polk to name where the war began",
            "k": ["spot resolutions", "lincoln"],
            "n": 0,
            "rabbit": "Abraham Lincoln"
        },
        {
            "id": "american-blood",
            "tier": "middle",
            "t": "Polk told Congress that Mexico had “shed American blood upon the American soil”",
            "k": ["american blood", "american soil"],
            "n": 0
        },
        {
            "id": "chapultepec",
            "tier": "middle",
            "t": "Battle of Chapultepec (1847): Mexico honors its cadets as the Niños Héroes; the Marines’ Hymn recalls the “Halls of Montezuma”",
            "k": ["chapultepec", "niños héroes", "halls of montezuma"],
            "n": 0
        },
        {
            "id": "thornton",
            "tier": "power",
            "t": "Thornton Affair (April 1846): Mexican cavalry attacked Captain Seth Thornton’s patrol north of the Rio Grande",
            "k": ["thornton", "patrol"],
            "n": 0
        },
        {
            "id": "slidell",
            "tier": "power",
            "t": "Mexico refused to meet John Slidell, whom Polk sent to buy California and New Mexico",
            "k": ["john slidell", "slidell"],
            "n": 0
        },
        {
            "id": "palo-alto",
            "tier": "power",
            "t": "First battles: Palo Alto and Resaca de la Palma (1846) against Mariano Arista; Fort Texas was renamed Fort Brown",
            "k": ["palo alto", "resaca de la palma", "arista", "fort brown"],
            "n": 0
        },
        {
            "id": "davis",
            "tier": "power",
            "t": "Jefferson Davis led the Mississippi Rifles at Buena Vista",
            "k": ["jefferson davis", "mississippi rifles"],
            "n": 0
        },
        {
            "id": "blockade",
            "tier": "power",
            "t": "Polk let the exiled Santa Anna slip through the blockade from Cuba, hoping he would make peace",
            "k": ["blockade", "cuba", "exiled"],
            "n": 0
        },
        {
            "id": "cortes",
            "tier": "power",
            "t": "Scott’s landing at Veracruz was the first large-scale U.S. amphibious landing; his march roughly followed Hernán Cortés’s route",
            "k": ["amphibious", "cortés", "cortes"],
            "n": 0
        },
        {
            "id": "lee",
            "tier": "power",
            "t": "At Cerro Gordo, engineer Robert E. Lee found a path around the Mexican flank; Grant, McClellan, and Stonewall Jackson also served",
            "k": ["cerro gordo", "robert e. lee", "engineer"],
            "n": 0
        },
        {
            "id": "san-patricios",
            "tier": "power",
            "t": "John Riley’s Saint Patrick’s Battalion, mostly Irish Catholic immigrants, fought for Mexico; many were captured at Churubusco",
            "k": ["saint patrick’s battalion", "john riley", "churubusco"],
            "n": 0
        },
        {
            "id": "kearny",
            "tier": "power",
            "t": "Stephen Kearny’s Army of the West took Santa Fe without a fight; John C. Frémont joined the uprising in California",
            "k": ["kearny", "army of the west", "santa fe"],
            "n": 0
        },
        {
            "id": "thoreau",
            "tier": "power",
            "t": "Henry David Thoreau went to jail rather than pay a tax; he wrote “Resistance to Civil Government” (“Civil Disobedience”)",
            "k": ["thoreau", "civil disobedience", "resistance to civil government"],
            "n": 0
        },
        {
            "id": "trist",
            "tier": "power",
            "t": "Nicholas Trist ignored his recall and negotiated the treaty: $15 million, with the Rio Grande as Texas’s border",
            "k": ["nicholas trist", "trist", "15 million"],
            "n": 0
        },
        {
            "id": "grant-lowell",
            "tier": "power",
            "t": "Grant called it “one of the most unjust” wars; James Russell Lowell mocked it in _The Biglow Papers_",
            "k": ["unjust", "biglow papers", "james russell lowell"],
            "n": 0
        },
        {
            "id": "polks-war",
            "tier": "power",
            "t": "Many Whigs attacked it as “Mr. Polk’s War”",
            "k": ["polk’s war", "whigs"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Texas Revolution or this war?",
        "body": "Texas shows up in two different wars. The Texas Revolution (1835–1836) is when Texas broke away from Mexico, with the Alamo, Sam Houston, and the Battle of San Jacinto. This war came a decade later, after the United States annexed Texas in 1845, and Santa Anna led Mexico’s army in both. Players also mix this war up with the Spanish-American War of 1898.",
        "fix": "The Alamo, Sam Houston, or San Jacinto means the Texas Revolution. Polk, Zachary Taylor, Winfield Scott, the Wilmot Proviso, Chapultepec, or the Treaty of Guadalupe Hidalgo means the Mexican-American War. Cuba, the Philippines, and “Remember the Maine!” mean 1898.",
        "line": "Real answer line: <b><u>Mexican-American War</u></b> (or <u>Mexican War</u>; or <u>U.S.-Mexican War</u>)"
    },
    "tests": {
        "right": [
            "Mexican-American War",
            "Mexican War",
            "U.S.-Mexican War",
            "Mexican American War",
            "Mexican-Amercan War",
            "War with Mexico"
        ],
        "prompt": [],
        "wrong": [
            "Spanish-American War",
            "Texas Revolution",
            "Mexican Revolution",
            "War of 1812",
            "Mexican War of Independence",
            "Battle of the Alamo"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
