import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "gadsden-purchase",
    "name": "Gadsden Purchase",
    "mono": "GP",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "1853 land deal with Mexico · Bought for a southern railroad route",
    "dates": "Signed 1853; approved 1854",
    "briefing": "In the 1850s, Americans wanted a flat, snow-free route for a railroad across the South to California, and the best one ran through Mexico. In 1853, the American minister James Gadsden struck a deal with Mexico’s leader, Antonio López de Santa Anna, who needed money for his army: for $10 million, the United States got a strip of land south of the Gila River that became southern Arizona and southwestern New Mexico. It was the last big addition to the lower 48 states.",
    "answerHtml": "<b><u>Gadsden Purchase</u></b> (or <u>Venta de La Mesilla</u>; accept <u>Gadsden Treaty</u>; prompt on <u>Gadsden</u> alone; do not accept “Louisiana Purchase” or “Mexican Cession”)",
    "accept": [
        "gadsden purchase",
        "the gadsden purchase",
        "gadsden treaty",
        "the gadsden treaty",
        "venta de la mesilla",
        "la venta de la mesilla",
        "sale of la mesilla",
        "sale of mesilla",
        "treaty of la mesilla",
        "treaty of mesilla",
        "tratado de la mesilla",
        "mesilla treaty"
    ],
    "prompt": [
        "gadsden",
        "mesilla",
        "la mesilla"
    ],
    "reject": [
        "louisiana purchase",
        "alaska purchase",
        "purchase of alaska",
        "sewards folly",
        "treaty of guadalupe hidalgo",
        "guadalupe hidalgo",
        "mexican cession",
        "mexican american war",
        "mexican war",
        "texas annexation",
        "annexation of texas",
        "oregon treaty",
        "adams onis treaty",
        "florida purchase",
        "james gadsden",
        "christopher gadsden",
        "gadsden flag",
        "treaty of paris",
        "webster ashburton treaty",
        "missouri compromise",
        "compromise of 1850",
        "kansas nebraska act",
        "ostend manifesto",
        "gila river",
        "rio grande"
    ],
    "mediaPending": True,
    "media": [],
    "wiki": "https://en.wikipedia.org/wiki/Gadsden_Purchase",
    "qb": {
        "q": "Gadsden Purchase",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "This deal freed the United States from Article XI of an earlier treaty, which had required the United States to stop Native American raids across the border into Mexico. Mexico had demanded payment for damage caused by those raids.",
            "r": "That earlier treaty was the Treaty of Guadalupe Hidalgo. For 10 points, name this 1853 purchase of land from Mexico."
        },
        {
            "p": "Errors on John Disturnell’s map, which had been used to draw a border in 1848, led to a quarrel over who owned a fertile valley near the Rio Grande. That quarrel ended when this deal moved the border south.",
            "r": "For 10 points, name this treaty signed under President Franklin Pierce, which gave the United States southern Arizona and southwestern New Mexico."
        },
        {
            "p": "Secretary of War Jefferson Davis pushed for this deal because surveys showed that the best route for a southern railroad to California ran south of the Gila [“HEE-luh”] River. Some Northern senators opposed it, worried that a southern railroad would strengthen the slave states.",
            "r": "For 10 points, name this 1853 land purchase from Mexico, which cost 10 million dollars and became part of Arizona and New Mexico."
        },
        {
            "p": "The U.S. Senate cut back this deal before approving it in 1854, shrinking both the amount of land and the price. The final version gave the United States about 30,000 square miles of desert and mountains.",
            "r": "Mexico’s leader, Antonio López de Santa Anna, sold the land for 10 million dollars. For 10 points, name this 1853 deal."
        },
        {
            "p": "The diplomat who negotiated this deal was a grandson of a South Carolina patriot whose yellow flag showed a coiled rattlesnake above the words “Don’t Tread on Me.” That diplomat had earlier run a railroad company in South Carolina.",
            "r": "For 10 points, name this 1853 land deal with Mexico that added southern Arizona to the United States."
        },
        {
            "p": "About twenty years before negotiating this deal, the same American diplomat had negotiated the Treaty of Payne’s Landing, which called for the Seminoles to move west from Florida. For this deal, he bargained with a Mexican leader who called himself “His Most Serene Highness.”",
            "r": "That leader was Antonio López de Santa Anna. For 10 points, name this purchase of land south of the Gila [“HEE-luh”] River."
        },
        {
            "p": "In the early 1880s, the Southern Pacific Railroad laid tracks across the land gained in this deal, helping to complete a second railroad route across the country. Those tracks passed through Tucson, which had been a Spanish and then a Mexican fort town.",
            "r": "For 10 points, name this 1853 purchase that the United States made to get a good southern route for a railroad."
        },
        {
            "p": "The silver-mining boomtown of Tombstone, where the Earp brothers and Doc Holliday fought the famous 1881 gunfight at the O.K. Corral, grew up on land gained in this deal. Much of that land lies in the Sonoran Desert, home of the giant saguaro [“suh-WAR-oh”] cactus.",
            "r": "For 10 points, name this 1853 purchase from Mexico, the last major addition to the lower 48 states."
        },
        {
            "p": "Anger over this deal helped turn many Mexicans against their leader, who was driven from power for the last time by the Revolution of Ayutla [“ah-YOOT-lah”] in 1855. That leader had used money from this deal to pay his army.",
            "r": "For 10 points, name this 10-million-dollar sale of land to the United States, approved in 1854."
        },
        {
            "p": "Many Americans had hoped this deal would include a port on the Gulf of California, but the final boundary left that gulf entirely in Mexico. The new border instead ran across the desert to the Colorado River.",
            "r": "For 10 points, name this 1853 purchase of land from Mexico, which set much of the border of southern Arizona."
        },
        {
            "p": "This deal was approved in 1854, the same year American diplomats wrote the Ostend Manifesto, which argued that the United States should buy Cuba from Spain or take it by force. Both efforts happened under President Franklin Pierce, who wanted to expand the country.",
            "r": "For 10 points, name this purchase of land from Mexico that became the southern edge of Arizona and New Mexico."
        },
        {
            "p": "In 1861, Confederate troops proclaimed a Confederate Territory of Arizona with its capital at Mesilla [“meh-SEE-yah”], a town the United States had gained in this deal. Union soldiers from California retook the area the next year.",
            "r": "For 10 points, name this 1853 deal in which Mexico sold land to the United States for a southern railroad route."
        },
        {
            "p": "Franklin Pierce sent a railroad promoter from South Carolina to Mexico City as the American minister, with orders to buy land for a southern rail line. That minister signed this deal on December 30, 1853.",
            "r": "For 10 points, name this land deal, named for that minister, which added southern Arizona and southwestern New Mexico to the United States."
        },
        {
            "p": "The border created by this deal split the homeland of the Tohono O’odham [“toh-HOH-noh AH-tum”] people between two countries, and it ran through lands where Apache bands lived and traveled. Neither group was consulted about the sale.",
            "r": "For 10 points, name this 1853 purchase of land south of the Gila [“HEE-luh”] River from Mexico."
        },
        {
            "p": "Beginning in 1858, Butterfield Overland Mail stagecoaches carried letters and passengers across the land gained in this deal, stopping at Tucson on the way to California. Its southern route avoided the snowy mountain passes farther north.",
            "r": "For 10 points, name this 1853 land deal with Antonio López de Santa Anna’s government, which cost the United States 10 million dollars."
        }
    ],
    "clues": [
        {
            "id": "ten-million",
            "tier": "giveaway",
            "t": "Bought from Mexico for $10 million",
            "k": ["$10 million", "10 million", "mexico"],
            "n": 0
        },
        {
            "id": "date-pierce",
            "tier": "giveaway",
            "t": "Signed in Mexico City in December 1853 and approved in 1854, under President Franklin Pierce",
            "k": ["1853", "franklin pierce", "pierce", "1854"],
            "n": 0
        },
        {
            "id": "land",
            "tier": "giveaway",
            "t": "The land became southern Arizona and southwestern New Mexico",
            "k": ["southern arizona", "new mexico", "arizona"],
            "n": 0
        },
        {
            "id": "railroad",
            "tier": "giveaway",
            "t": "Bought mainly to get a flat southern route for a railroad to California",
            "k": ["railroad", "southern route", "california"],
            "n": 0
        },
        {
            "id": "last-major",
            "tier": "giveaway",
            "t": "The last major addition of land to the contiguous United States (the lower 48)",
            "k": ["last major", "contiguous", "lower 48"],
            "n": 0
        },
        {
            "id": "negotiator",
            "tier": "middle",
            "t": "Negotiated by the U.S. minister to Mexico, a South Carolina railroad promoter whose name it bears",
            "k": ["railroad promoter", "south carolina", "minister"],
            "n": 0
        },
        {
            "id": "santa-anna",
            "tier": "middle",
            "t": "Sold by Antonio López de Santa Anna, who needed money to pay his army",
            "k": ["santa anna", "army", "money"],
            "n": 0,
            "rabbit": "Antonio López de Santa Anna"
        },
        {
            "id": "gila",
            "tier": "middle",
            "t": "The land lies south of the Gila River",
            "k": ["gila river", "gila"],
            "n": 0
        },
        {
            "id": "tucson",
            "tier": "middle",
            "t": "Included Tucson, a former Spanish and Mexican fort town",
            "k": ["tucson", "fort town"],
            "n": 0
        },
        {
            "id": "davis",
            "tier": "middle",
            "t": "Secretary of War Jefferson Davis pushed for it to get a southern railroad route",
            "k": ["jefferson davis", "secretary of war"],
            "n": 0
        },
        {
            "id": "guadalupe-hidalgo",
            "tier": "middle",
            "t": "Came five years after the Treaty of Guadalupe Hidalgo ended the Mexican-American War",
            "k": ["guadalupe hidalgo", "mexican-american war", "five years"],
            "n": 0,
            "rabbit": "Mexican-American War"
        },
        {
            "id": "mesilla",
            "tier": "middle",
            "t": "Mexicans named the deal after La Mesilla, a town and valley in present-day New Mexico",
            "k": ["la mesilla", "mesilla", "valley"],
            "n": 0
        },
        {
            "id": "smaller",
            "tier": "middle",
            "t": "The U.S. Senate cut back the deal before approving it, leaving about 30,000 square miles",
            "k": ["30,000 square miles", "senate", "cut back"],
            "n": 0
        },
        {
            "id": "article-xi",
            "tier": "power",
            "t": "Freed the U.S. from Article XI of the Treaty of Guadalupe Hidalgo, which required it to stop raids across the border into Mexico",
            "k": ["article xi", "raids"],
            "n": 0
        },
        {
            "id": "disturnell",
            "tier": "power",
            "t": "Settled a boundary dispute over the Mesilla Valley caused by errors on John Disturnell’s map",
            "k": ["disturnell", "boundary dispute", "map"],
            "n": 0
        },
        {
            "id": "flag",
            "tier": "power",
            "t": "Its negotiator was a grandson of the patriot whose yellow “Don’t Tread on Me” flag showed a rattlesnake",
            "k": ["rattlesnake", "tread on me", "grandson"],
            "n": 0
        },
        {
            "id": "paynes-landing",
            "tier": "power",
            "t": "Its negotiator had earlier negotiated the Treaty of Payne’s Landing (1832) with the Seminoles",
            "k": ["payne’s landing", "seminoles", "1832"],
            "n": 0
        },
        {
            "id": "ayutla",
            "tier": "power",
            "t": "Anger over the sale helped drive Santa Anna from power for good in the Revolution of Ayutla (1855)",
            "k": ["ayutla", "revolution", "1855"],
            "n": 0
        },
        {
            "id": "serene",
            "tier": "power",
            "t": "Santa Anna was ruling as a dictator who called himself “His Most Serene Highness”",
            "k": ["serene highness", "dictator"],
            "n": 0
        },
        {
            "id": "southern-pacific",
            "tier": "power",
            "t": "The Southern Pacific Railroad built across the land in the early 1880s, through Tucson",
            "k": ["southern pacific", "1880s"],
            "n": 0
        },
        {
            "id": "gulf-port",
            "tier": "power",
            "t": "Many Americans wanted a port on the Gulf of California, but the final border left the gulf in Mexico",
            "k": ["gulf of california", "port"],
            "n": 0
        },
        {
            "id": "tombstone",
            "tier": "power",
            "t": "Tombstone, site of the 1881 gunfight at the O.K. Corral, grew up on its land in the Sonoran Desert",
            "k": ["tombstone", "o.k. corral", "sonoran desert"],
            "n": 0
        },
        {
            "id": "ostend",
            "tier": "power",
            "t": "Approved in 1854, the same year as the Ostend Manifesto about getting Cuba; both came under Pierce",
            "k": ["ostend manifesto", "ostend", "cuba"],
            "n": 0
        },
        {
            "id": "tohono-oodham",
            "tier": "power",
            "t": "The new border split the homeland of the Tohono O’odham people; neither they nor the Apache were consulted",
            "k": ["tohono o’odham", "apache", "homeland"],
            "n": 0
        },
        {
            "id": "butterfield",
            "tier": "power",
            "t": "Butterfield Overland Mail stagecoaches crossed its land from 1858, stopping at Tucson",
            "k": ["butterfield", "stagecoaches", "1858"],
            "n": 0
        },
        {
            "id": "confederate-arizona",
            "tier": "power",
            "t": "In 1861, Confederates proclaimed a Confederate Territory of Arizona with its capital at Mesilla",
            "k": ["confederate territory", "1861", "capital"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Cession or Purchase?",
        "body": "Two deals five years apart took land from northern Mexico. The Mexican Cession came from the Treaty of Guadalupe Hidalgo (1848), which ended the Mexican-American War and handed over California and most of the Southwest for $15 million. The Gadsden Purchase (1853) was a much smaller strip south of the Gila River, bought for $10 million to make room for a railroad. The Louisiana Purchase (1803), bought from France, also cost about $15 million.",
        "fix": "A war, California, and 1848 mean the Mexican Cession or the Treaty of Guadalupe Hidalgo. A railroad route, the Gila River, Franklin Pierce, and 1853–1854 mean the Gadsden Purchase. Thomas Jefferson, Napoleon, and 1803 mean the Louisiana Purchase.",
        "line": "Real answer line: <b><u>Gadsden Purchase</u></b> (or <u>Venta de La Mesilla</u>; accept <u>Gadsden Treaty</u>; prompt on <u>Gadsden</u> alone)"
    },
    "tests": {
        "right": [
            "Gadsden Purchase",
            "the Gadsden Purchase",
            "Gadsen Purchase",
            "Venta de La Mesilla",
            "Gadsden Treaty",
            "Treaty of La Mesilla"
        ],
        "prompt": [
            "Gadsden",
            "Mesilla"
        ],
        "wrong": [
            "Louisiana Purchase",
            "Treaty of Guadalupe Hidalgo",
            "Mexican Cession",
            "James Gadsden",
            "Alaska Purchase",
            "Gadsden flag",
            "Mexican-American War"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", data["id"])
