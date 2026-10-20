import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "california",
    "name": "California",
    "mono": "CAL",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Pacific Coast state, admitted in 1850 · Missions, gold rush, and Hollywood",
    "dates": "Statehood 1850 (31st state)",
    "briefing": "California got its name from a make-believe island in a Spanish adventure story, and its real history is just as dramatic. Spanish priests built a chain of 21 missions along its coast, American settlers raised a grizzly-bear flag in 1846, and the discovery of gold at Sutter’s Mill in 1848 set off a rush that helped it become the 31st state in 1850.",
    "answerHtml": "<b><u>California</u></b> (accept <u>Alta California</u>; do not accept “Baja California”)",
    "accept": [
        "california",
        "state of california",
        "alta california",
        "upper california",
        "california republic"
    ],
    "prompt": [
        "bear flag republic"
    ],
    "reject": [
        "baja california",
        "baja california sur",
        "lower california",
        "california gold rush",
        "gold rush",
        "mexican cession",
        "mexico",
        "nevada",
        "oregon",
        "arizona",
        "new mexico",
        "texas",
        "hawaii",
        "los angeles",
        "san francisco",
        "san diego",
        "sacramento"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/California",
    "qb": {
        "q": "California",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "This state’s name comes from a fictional island ruled by Queen Calafia [“kuh-LAH-fee-uh”] in a Spanish adventure story written in the early 1500s by Garci Rodríguez de Montalvo [“mon-TAHL-voh”]. For many years, European mapmakers wrongly drew this region as a giant island.",
            "r": "This state’s nickname is the Golden State, and its motto is “Eureka.” For 10 points, name this Pacific Coast state, home to Hollywood and Los Angeles."
        },
        {
            "p": "In 1542, Juan Rodríguez Cabrillo [“kah-BREE-yoh”] sailed into San Diego Bay, becoming the first European to explore this region’s coast. Decades later, Francis Drake landed somewhere on this coast during his voyage around the world and claimed the land for England as “Nova Albion.”",
            "r": "In 1846, the Donner Party was trapped by snow in this state’s Sierra Nevada. For 10 points, name this Pacific Coast state whose capital is Sacramento."
        },
        {
            "p": "Father Junípero Serra [“hoo-NEE-puh-roh SAIR-uh”] founded the first of this region’s 21 Spanish missions at San Diego in 1769, and the last one was built at Sonoma in 1823. Those missions were linked by a road called El Camino Real [“el kuh-MEE-noh ray-AHL”], or “the Royal Road.”",
            "r": "The cities of San Diego and San Francisco share their names with two of those missions. For 10 points, name this state where gold was found in 1848."
        },
        {
            "p": "In 1812, the Russian-American Company built Fort Ross on this region’s northern coast, partly to hunt sea otters and to grow food for Russian settlements in Alaska. Russia sold that fort in 1841 to John Sutter, a Swiss settler whose own fort stood where this state’s capital later grew.",
            "r": "Gold was found at Sutter’s sawmill in 1848. For 10 points, name this state where the “forty-niners” rushed to find gold."
        },
        {
            "p": "In June 1846, American settlers in Sonoma took the Mexican general Mariano Vallejo [“vuh-YAY-hoh”] prisoner and declared an independent republic. Their homemade flag showed a grizzly bear and a red star, and the explorer John C. Frémont [“FREE-mont”] soon took charge of their revolt.",
            "r": "A version of that bear flag became this state’s flag. For 10 points, name this state, which joined the Union in 1850."
        },
        {
            "p": "Andrés Pico’s lancers clashed with soldiers under Stephen Kearny [“KAR-nee”] at the Battle of San Pasqual [“pahs-KWAHL”] in this region in late 1846. A few weeks later, Pico signed the Treaty of Cahuenga [“kuh-WENG-guh”] with John C. Frémont, ending the fighting here during the Mexican-American War.",
            "r": "In 1848, Mexico gave up this land in the Treaty of Guadalupe Hidalgo. For 10 points, name this state where gold was discovered that same year."
        },
        {
            "p": "On January 24, 1848, the carpenter James W. Marshall spotted shiny flakes in the water channel of a sawmill he was building at Coloma. Just nine days later, Mexico signed away this land in the Treaty of Guadalupe Hidalgo, though neither side knew about Marshall’s find.",
            "r": "The next year, thousands of “forty-niners” rushed there. For 10 points, name this state where gold was found at Sutter’s Mill."
        },
        {
            "p": "Delegates meeting at Monterey in 1849 wrote a constitution that banned slavery in this region, and they asked to join the Union without first becoming a territory. Henry Clay’s Compromise of 1850 admitted this state as a free state, upsetting the balance of free and slave states in the Senate.",
            "r": "It became the 31st state that year. For 10 points, name this state, which had grown quickly during a gold rush."
        },
        {
            "p": "Charles Crocker hired thousands of Chinese workers to blast tunnels through the Sierra Nevada for a railroad company based in this state’s capital. Leland Stanford, one of that company’s “Big Four” leaders, took part in the golden spike ceremony at Promontory Summit in 1869 and later founded a university here.",
            "r": "That company was the Central Pacific. For 10 points, name this state at the western end of the first transcontinental railroad."
        },
        {
            "p": "From 1910 to 1940, many Chinese immigrants were held for weeks or months at an immigration station on Angel Island, where some carved poems into the barrack walls. That island lies in a bay in this state, where the labor leader Denis Kearney had led an anti-Chinese movement with the slogan “The Chinese must go!”",
            "r": "Earlier, Chinese immigrants had called this land “Gold Mountain.” For 10 points, name this state whose largest city is Los Angeles."
        },
        {
            "p": "After a 1906 disaster, the banker Amadeo Giannini [“jah-NEE-nee”] saved his bank’s money in a produce wagon and lent it out to help rebuild a city in this state; his Bank of Italy later became Bank of America. That disaster began with an April earthquake along the San Andreas Fault, followed by days of fires.",
            "r": "More than half of San Francisco’s people lost their homes. For 10 points, name this state, home to Los Angeles and Hollywood."
        },
        {
            "p": "In 1864, Abraham Lincoln signed the Yosemite Grant, which set aside a valley and a grove of giant sequoias in this state for public use. The Scottish-born naturalist John Muir later fought to protect that area and co-founded the Sierra Club in this state in 1892.",
            "r": "This state’s Sierra Nevada also includes Mount Whitney, the highest peak in the lower 48 states. For 10 points, name this state, which also contains Death Valley."
        },
        {
            "p": "During World War II, the U.S. government forced about 10,000 Japanese Americans to live at Manzanar, a camp in this state’s Owens Valley. Fred Korematsu, who was born in this state’s city of Oakland, challenged that forced removal in a famous Supreme Court case.",
            "r": "That removal followed Executive Order 9066 in 1942. For 10 points, name this West Coast state whose capital is Sacramento."
        },
        {
            "p": "In 1965, Filipino American farmworkers led by Larry Itliong [“IT-lee-ong”] went on strike against grape growers near Delano [“duh-LAY-noh”] in this state, and Cesar Chavez’s union soon joined them. Chavez and Dolores Huerta [“WAIR-tuh”] then led a nationwide boycott of table grapes.",
            "r": "Their union became the United Farm Workers. For 10 points, name this state, home to the farm-rich Central Valley and the city of Los Angeles."
        },
        {
            "p": "Earl Warren was elected this state’s governor three times before becoming Chief Justice of the United States in 1953. Ronald Reagan, a former actor, was governor of this state from 1967 to 1975, and Richard Nixon is the only U.S. president born in this state.",
            "r": "Both Reagan and Nixon have presidential libraries here. For 10 points, name this state, home to Hollywood."
        }
    ],
    "clues": [
        {
            "id": "golden-state",
            "tier": "giveaway",
            "t": "Nicknamed the Golden State; its motto is “Eureka” (“I have found it”)",
            "k": ["golden state", "eureka"],
            "n": 0
        },
        {
            "id": "gold-rush",
            "tier": "giveaway",
            "t": "Gold was found at Sutter’s Mill in 1848, and the “forty-niners” poured in during the gold rush of 1849",
            "k": ["sutter’s mill", "forty-niners", "gold rush", "1848"],
            "n": 0,
            "rabbit": "California gold rush"
        },
        {
            "id": "cities",
            "tier": "giveaway",
            "t": "Capital: Sacramento; largest city: Los Angeles, home of Hollywood",
            "k": ["sacramento", "los angeles", "hollywood"],
            "n": 0
        },
        {
            "id": "statehood",
            "tier": "giveaway",
            "t": "Became the 31st state in 1850, as a free state under the Compromise of 1850",
            "k": ["31st", "free state", "compromise of 1850"],
            "n": 0,
            "rabbit": "Compromise of 1850"
        },
        {
            "id": "missions",
            "tier": "middle",
            "t": "Father Junípero Serra founded the first of 21 Spanish missions (San Diego, 1769); El Camino Real linked them, and many Native people were forced to live and work there",
            "k": ["junípero serra", "serra", "missions", "el camino real"],
            "n": 0
        },
        {
            "id": "bear-flag",
            "tier": "middle",
            "t": "Bear Flag Revolt (1846): settlers at Sonoma declared a republic under a grizzly-bear flag, which became the state flag",
            "k": ["bear flag", "sonoma", "grizzly"],
            "n": 0
        },
        {
            "id": "mexican-war",
            "tier": "middle",
            "t": "Won in the Mexican-American War; Mexico signed it away in the Treaty of Guadalupe Hidalgo (1848)",
            "k": ["guadalupe hidalgo", "mexican-american war", "mexico"],
            "n": 0,
            "rabbit": "Mexican-American War"
        },
        {
            "id": "railroad",
            "tier": "middle",
            "t": "Central Pacific Railroad: built east from Sacramento by thousands of Chinese workers; its “Big Four” leaders included Leland Stanford",
            "k": ["central pacific", "big four", "leland stanford", "chinese workers"],
            "n": 0
        },
        {
            "id": "earthquake",
            "tier": "middle",
            "t": "The 1906 San Francisco earthquake (San Andreas Fault) and fires left more than half the city homeless",
            "k": ["1906", "san andreas", "earthquake", "san francisco"],
            "n": 0
        },
        {
            "id": "yosemite",
            "tier": "middle",
            "t": "Lincoln signed the Yosemite Grant (1864); Scottish-born John Muir co-founded the Sierra Club (1892)",
            "k": ["yosemite", "john muir", "sierra club"],
            "n": 0
        },
        {
            "id": "extremes",
            "tier": "middle",
            "t": "Has Mount Whitney, the highest peak in the lower 48 states, and Death Valley, the lowest point in North America",
            "k": ["mount whitney", "death valley"],
            "n": 0
        },
        {
            "id": "donner",
            "tier": "middle",
            "t": "The Donner Party was trapped by snow in the Sierra Nevada (1846–1847) while heading there",
            "k": ["donner party", "donner", "sierra nevada"],
            "n": 0,
            "rabbit": "Donner Party"
        },
        {
            "id": "gold-mountain",
            "tier": "middle",
            "t": "Chinese immigrants called it “Gold Mountain”",
            "k": ["gold mountain"],
            "n": 0
        },
        {
            "id": "calafia",
            "tier": "power",
            "t": "Named for a make-believe island ruled by Queen Calafia in a 1500s Spanish story by Garci Rodríguez de Montalvo; old maps drew it as an island",
            "k": ["calafia", "montalvo", "island"],
            "n": 0
        },
        {
            "id": "cabrillo",
            "tier": "power",
            "t": "Juan Rodríguez Cabrillo explored its coast (1542); Francis Drake claimed “Nova Albion” for England (1579)",
            "k": ["cabrillo", "francis drake", "nova albion"],
            "n": 0
        },
        {
            "id": "fort-ross",
            "tier": "power",
            "t": "Fort Ross (1812): a Russian outpost for hunting sea otters, sold to John Sutter in 1841",
            "k": ["fort ross", "russian", "sea otters"],
            "n": 0
        },
        {
            "id": "vallejo",
            "tier": "power",
            "t": "Bear Flaggers took Mexican general Mariano Vallejo prisoner; John C. Frémont soon took charge of the revolt",
            "k": ["vallejo", "frémont", "fremont"],
            "n": 0
        },
        {
            "id": "cahuenga",
            "tier": "power",
            "t": "Andrés Pico fought Stephen Kearny at San Pasqual (1846), then signed the Treaty of Cahuenga with Frémont (1847)",
            "k": ["cahuenga", "san pasqual", "andrés pico", "kearny"],
            "n": 0
        },
        {
            "id": "marshall",
            "tier": "power",
            "t": "James W. Marshall found gold at the sawmill in Coloma, nine days before the Treaty of Guadalupe Hidalgo",
            "k": ["james w. marshall", "marshall", "coloma", "nine days"],
            "n": 0
        },
        {
            "id": "monterey",
            "tier": "power",
            "t": "Its 1849 constitution, written at Monterey, banned slavery; it was never a U.S. territory",
            "k": ["monterey", "1849", "territory"],
            "n": 0
        },
        {
            "id": "crocker",
            "tier": "power",
            "t": "Charles Crocker’s Chinese crews blasted tunnels through the Sierra Nevada; Stanford joined the golden spike ceremony at Promontory Summit (1869)",
            "k": ["crocker", "promontory", "golden spike"],
            "n": 0
        },
        {
            "id": "angel-island",
            "tier": "power",
            "t": "Angel Island (1910–1940): Chinese immigrants were held there and carved poems into the walls; Denis Kearney’s slogan was “The Chinese must go!”",
            "k": ["angel island", "poems", "denis kearney"],
            "n": 0
        },
        {
            "id": "giannini",
            "tier": "power",
            "t": "After the 1906 earthquake, A. P. Giannini lent money from his Bank of Italy (later Bank of America) to help San Francisco rebuild",
            "k": ["giannini", "bank of italy", "bank of america"],
            "n": 0
        },
        {
            "id": "manzanar",
            "tier": "power",
            "t": "Manzanar held about 10,000 Japanese Americans after Executive Order 9066 (1942); Oakland-born Fred Korematsu challenged the removal",
            "k": ["manzanar", "korematsu", "9066"],
            "n": 0
        },
        {
            "id": "farmworkers",
            "tier": "power",
            "t": "Delano grape strike (1965): Larry Itliong and Cesar Chavez; Dolores Huerta helped lead the grape boycott (United Farm Workers)",
            "k": ["delano", "cesar chavez", "dolores huerta", "itliong", "united farm workers"],
            "n": 0
        },
        {
            "id": "governors",
            "tier": "power",
            "t": "Earl Warren (governor, then Chief Justice) and Ronald Reagan (governor 1967–1975); Richard Nixon is the only president born there",
            "k": ["earl warren", "reagan", "nixon"],
            "n": 0
        }
    ],
    "trap": {
        "title": "State or gold rush?",
        "body": "Many clues for this state, like Sutter’s Mill, James Marshall, and the forty-niners, also lead tossups whose answer is the California gold rush, an event with its own answer line. If the question asks for “this event,” naming only the state is not enough. And Baja (Lower) California is a different place: a peninsula that belongs to Mexico.",
        "fix": "Listen for the noun: “this state” wants California, while “this event” or “this rush” wants “California gold rush.” The Spanish called the U.S. part Alta (Upper) California, so “Alta California” is fine, but never say “Baja.”",
        "line": "Real answer line: <b><u>California</u></b> (accept <u>Alta California</u>; do not accept “Baja California”)"
    },
    "tests": {
        "right": [
            "California",
            "Califronia",
            "State of California",
            "Alta California",
            "Upper California"
        ],
        "prompt": [
            "Bear Flag Republic"
        ],
        "wrong": [
            "Baja California",
            "California Gold Rush",
            "Nevada",
            "Los Angeles",
            "Oregon",
            "Mexican Cession"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
