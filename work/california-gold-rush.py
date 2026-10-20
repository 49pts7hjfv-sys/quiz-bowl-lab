import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "california-gold-rush",
    "name": "California gold rush",
    "mono": "49",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Gold found at Sutter’s Mill in 1848 · Brought the forty-niners west",
    "dates": "1848–1855",
    "briefing": "In January 1848, a carpenter named James Marshall spotted shiny flakes in the water channel of a sawmill in the Sierra Nevada foothills. Within a year, word had spread around the world, and an estimated 300,000 people eventually rushed to California, most of them men who became known as “forty-niners.” A few struck it rich, more made money selling them supplies, and California’s Native peoples suffered terrible losses.",
    "answerHtml": "<b><u>California gold rush</u></b> (accept <u>Gold Rush of 1849</u>; prompt on <u>gold rush</u>; do not accept “California” alone or “Klondike Gold Rush”)",
    "accept": [
        "california gold rush",
        "the california gold rush",
        "california gold rush of 1849",
        "gold rush of 1849",
        "gold rush of 1848",
        "1849 gold rush",
        "1848 gold rush",
        "gold rush of 49"
    ],
    "prompt": [
        "gold rush",
        "the gold rush",
        "sutters mill",
        "discovery of gold",
        "discovery of gold in california",
        "gold discovery"
    ],
    "reject": [
        "klondike gold rush",
        "klondike",
        "yukon gold rush",
        "alaska gold rush",
        "georgia gold rush",
        "dahlonega gold rush",
        "pikes peak gold rush",
        "colorado gold rush",
        "black hills gold rush",
        "australian gold rush",
        "victorian gold rush",
        "fraser canyon gold rush",
        "comstock lode",
        "silver rush",
        "oklahoma land rush",
        "land rush",
        "oregon trail",
        "donner party",
        "manifest destiny",
        "mexican cession",
        "mexican american war",
        "compromise of 1850",
        "transcontinental railroad",
        "first transcontinental railroad",
        "pony express",
        "sutters fort"
    ],
    "mediaPending": True,
    "media": [],
    "wiki": "https://en.wikipedia.org/wiki/California_gold_rush",
    "qb": {
        "q": "gold rush",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In 1850, California’s legislature passed a Foreign Miners’ Tax that charged non-citizens $20 a month, driving away many Mexican and other Latin American miners during this event. A later version of the tax fell mostly on Chinese immigrants, who called California “Gold Mountain.”",
            "r": "For 10 points, name this event that began after James Marshall found gold at Sutter’s Mill in 1848."
        },
        {
            "p": "People who took part in this event described the hardships of the journey, and the letdown of finding little, as “seeing the elephant.” Many of them reached the Pacific coast by sailing around Cape Horn or by crossing the Isthmus of Panama.",
            "r": "For 10 points, name this event that drew the “forty-niners” west after gold was found at Sutter’s Mill."
        },
        {
            "p": "Participants in this event were nicknamed “Argonauts,” after the Greek heroes who sailed with Jason in search of the Golden Fleece. Many of them sang new words to Stephen Foster’s song “Oh! Susanna” as they headed west.",
            "r": "For 10 points, name this event that drew tens of thousands of “forty-niners” west after 1848."
        },
        {
            "p": "This event began when a carpenter noticed shiny flakes in the tailrace of a sawmill on the South Fork of the American River. Nine days later, the Treaty of Guadalupe Hidalgo was signed by negotiators who had no idea that the discovery had been made.",
            "r": "That carpenter was James Marshall. For 10 points, name this event that began at Sutter’s Mill in January 1848."
        },
        {
            "p": "The merchant Sam Brannan helped set off this event by running through the streets of San Francisco waving a bottle of gold dust, after stocking his store with picks and pans. Brannan grew rich by selling supplies to the people who joined this event.",
            "r": "It began after James Marshall found gold at Sutter’s Mill. For 10 points, name this event that brought the “forty-niners” to California."
        },
        {
            "p": "President James K. Polk set off a frenzy in December 1848 when he confirmed the discovery that started this event in his annual message to Congress. Soon, tens of thousands of fortune seekers were heading west by land and by sea.",
            "r": "They were called “forty-niners.” For 10 points, name this event that began when gold was found at Sutter’s Mill."
        },
        {
            "p": "During this event, a Bavarian-born merchant named Levi Strauss opened a dry-goods business in San Francisco. In 1873, he and the tailor Jacob Davis patented denim work pants that were strengthened with copper rivets.",
            "r": "Those pants became blue jeans. For 10 points, name this event that brought thousands of miners to California after 1848."
        },
        {
            "p": "In 2019, California’s governor formally apologized to Native Californians for the violence that came with this event, calling it a genocide. An 1850 state law let settlers force Native people, including children, into unpaid labor, and the Native population fell from an estimated 150,000 to about 30,000 by 1870.",
            "r": "For 10 points, name this event that began when James Marshall found gold at Sutter’s Mill in 1848."
        },
        {
            "p": "After this event began, the Land Act of 1851 forced Californios, Spanish-speaking landowners of Mexican descent, to prove their land titles in American courts, and many lost their ranches. Delegates at Monterey had already written a state constitution that banned slavery.",
            "r": "California became a state in 1850. For 10 points, name this event, which brought tens of thousands of “forty-niners” west."
        },
        {
            "p": "The richest diggings of this event lay along a belt of gold-bearing rock in the Sierra Nevada foothills called the Mother Lode. Miners there swirled gravel in pans or rocked it in wooden cradles to wash away dirt and leave the heavy flakes behind.",
            "r": "Those miners were called “forty-niners.” For 10 points, name this event that began at Sutter’s Mill in 1848."
        },
        {
            "p": "Late in this event, miners began blasting hillsides with high-pressure jets of water, a method called hydraulic mining that choked rivers downstream with mud. Earlier, miners had used shallow pans and long wooden troughs called sluices.",
            "r": "For 10 points, name this event that began when James Marshall found gold at Sutter’s Mill in 1848."
        },
        {
            "p": "Henry Wells and William Fargo founded a company in 1852 to provide banking and to ship gold, money, and mail during this event. San Francisco grew from a village of under 1,000 people into a booming city during this event, and abandoned ships crowded its harbor.",
            "r": "That company was Wells Fargo. For 10 points, name this event that brought the “forty-niners” west after 1848."
        },
        {
            "p": "Bret Harte’s story “The Luck of Roaring Camp” and Mark Twain’s “The Celebrated Jumping Frog of Calaveras County” are set in mining camps that grew up during this event.",
            "r": "The song “Oh My Darling, Clementine” is about a “miner, forty-niner.” For 10 points, name this event that began in 1848."
        },
        {
            "p": "A statue of one man stands over his grave at Coloma, pointing toward the spot where he made the discovery that started this event. That man’s employer, the Swiss-born John Sutter, lost his workers and most of his land to the fortune seekers who swarmed in.",
            "r": "For 10 points, name this event, which began when James Marshall found gold at Sutter’s Mill in 1848."
        },
        {
            "p": "An estimated 300,000 people came west during this event, many of them over the California Trail across the Sierra Nevada. The population boom allowed a new state to skip the territory stage and join the Union in 1850.",
            "r": "California’s motto, “Eureka” (“I have found it”), is said to refer to this event. For 10 points, name this event that brought the “forty-niners” west."
        }
    ],
    "clues": [
        {
            "id": "sutters-mill",
            "tier": "giveaway",
            "t": "Began when gold was found at Sutter’s Mill, a sawmill at Coloma, on January 24, 1848",
            "k": ["sutter’s mill", "sutters mill", "coloma", "january 24"],
            "n": 0
        },
        {
            "id": "forty-niners",
            "tier": "giveaway",
            "t": "Gold seekers who poured in during 1849 were called “forty-niners”; San Francisco’s NFL team is named for them",
            "k": ["forty-niners", "forty niners", "49ers", "1849"],
            "n": 0
        },
        {
            "id": "marshall",
            "tier": "giveaway",
            "t": "The carpenter James Marshall spotted the first flakes while building the sawmill",
            "k": ["james marshall", "marshall", "carpenter"],
            "n": 0
        },
        {
            "id": "statehood",
            "tier": "giveaway",
            "t": "Helped California become the 31st state in 1850, as a free state under the Compromise of 1850",
            "k": ["31st state", "compromise of 1850", "free state", "1850"],
            "n": 0,
            "rabbit": "California"
        },
        {
            "id": "sutter",
            "tier": "middle",
            "t": "John Sutter, a Swiss-born settler, owned the mill; fortune seekers overran his land and he went broke",
            "k": ["john sutter", "sutter", "swiss", "went broke"],
            "n": 0
        },
        {
            "id": "brannan",
            "tier": "middle",
            "t": "Merchant Sam Brannan waved a bottle of gold dust in the streets of San Francisco, then got rich selling supplies",
            "k": ["sam brannan", "brannan", "bottle", "supplies"],
            "n": 0
        },
        {
            "id": "polk",
            "tier": "middle",
            "t": "President James K. Polk confirmed the discovery in his December 1848 message to Congress",
            "k": ["james k. polk", "polk", "december 1848"],
            "n": 0,
            "rabbit": "James K. Polk"
        },
        {
            "id": "levi-strauss",
            "tier": "middle",
            "t": "Levi Strauss sold dry goods in San Francisco; in 1873 he and tailor Jacob Davis patented riveted denim pants (blue jeans)",
            "k": ["levi strauss", "jacob davis", "blue jeans", "1873"],
            "n": 0
        },
        {
            "id": "routes",
            "tier": "middle",
            "t": "Routes west: overland on the California Trail, by ship around Cape Horn, or across the Isthmus of Panama",
            "k": ["cape horn", "panama", "california trail", "isthmus"],
            "n": 0
        },
        {
            "id": "native-californians",
            "tier": "middle",
            "t": "Disease, starvation, and attacks by miners and state-backed militias cut California’s Native population from about 150,000 to about 30,000 by 1870",
            "k": ["native", "150,000", "30,000", "militias"],
            "n": 0
        },
        {
            "id": "san-francisco",
            "tier": "middle",
            "t": "San Francisco boomed from a village of under 1,000 people into a city; abandoned ships crowded its harbor",
            "k": ["san francisco", "abandoned ships", "harbor"],
            "n": 0
        },
        {
            "id": "panning",
            "tier": "middle",
            "t": "Miners washed stream gravel in pans, rocking cradles, and wooden troughs called sluices",
            "k": ["pans", "panning", "cradles", "sluices"],
            "n": 0
        },
        {
            "id": "eureka",
            "tier": "middle",
            "t": "California’s motto, “Eureka” (“I have found it”), is said to refer to it; the state’s nickname is the Golden State",
            "k": ["eureka", "i have found it", "golden state"],
            "n": 0
        },
        {
            "id": "chinese",
            "tier": "middle",
            "t": "Chinese immigrants who came during it called California “Gold Mountain”",
            "k": ["chinese", "mountain", "immigrants"],
            "n": 0
        },
        {
            "id": "foreign-miners-tax",
            "tier": "power",
            "t": "The Foreign Miners’ Tax (1850) charged non-citizens $20 a month, driving off many Mexican and Latin American miners; a later version hit the Chinese",
            "k": ["foreign miners", "$20", "non-citizens", "mexican"],
            "n": 0
        },
        {
            "id": "seeing-elephant",
            "tier": "power",
            "t": "Forty-niners called the hard trip and its disappointments “seeing the elephant”",
            "k": ["seeing the elephant", "elephant"],
            "n": 0
        },
        {
            "id": "argonauts",
            "tier": "power",
            "t": "Forty-niners were nicknamed “Argonauts,” after the heroes who sailed with Jason for the Golden Fleece",
            "k": ["argonauts", "jason", "golden fleece"],
            "n": 0
        },
        {
            "id": "oh-susanna",
            "tier": "power",
            "t": "Forty-niners sang new words to Stephen Foster’s “Oh! Susanna” on the way west",
            "k": ["oh! susanna", "oh susanna", "stephen foster", "susanna"],
            "n": 0
        },
        {
            "id": "mother-lode",
            "tier": "power",
            "t": "The richest gold belt, in the Sierra Nevada foothills, was called the Mother Lode",
            "k": ["mother lode", "sierra nevada", "foothills"],
            "n": 0
        },
        {
            "id": "tailrace",
            "tier": "power",
            "t": "Marshall found the flakes in the mill’s tailrace on the South Fork of the American River, nine days before the Treaty of Guadalupe Hidalgo",
            "k": ["tailrace", "american river", "guadalupe hidalgo", "nine days"],
            "n": 0
        },
        {
            "id": "hydraulic",
            "tier": "power",
            "t": "Later, hydraulic mining blasted hillsides with high-pressure water and choked rivers with mud",
            "k": ["hydraulic", "high-pressure water", "mud"],
            "n": 0
        },
        {
            "id": "wells-fargo",
            "tier": "power",
            "t": "Henry Wells and William Fargo founded Wells Fargo (1852) for banking and for shipping gold, money, and mail",
            "k": ["wells fargo", "henry wells", "william fargo", "1852"],
            "n": 0
        },
        {
            "id": "clementine",
            "tier": "power",
            "t": "The folk song “Oh My Darling, Clementine” is about a “miner, forty-niner” and his daughter",
            "k": ["clementine", "darling", "folk song"],
            "n": 0
        },
        {
            "id": "twain-harte",
            "tier": "power",
            "t": "Mining-camp stories: Bret Harte’s “The Luck of Roaring Camp” and Mark Twain’s “The Celebrated Jumping Frog of Calaveras County”",
            "k": ["bret harte", "roaring camp", "jumping frog", "calaveras"],
            "n": 0
        },
        {
            "id": "land-act",
            "tier": "power",
            "t": "The Land Act of 1851 made Californios (Spanish-speaking landowners) prove their land titles in court; many lost their ranches",
            "k": ["land act", "californios", "1851", "titles"],
            "n": 0
        },
        {
            "id": "apology-1850-law",
            "tier": "power",
            "t": "An 1850 state law let settlers force Native people, including children, into unpaid labor; in 2019 Governor Gavin Newsom apologized, calling the violence a genocide",
            "k": ["1850 state law", "unpaid labor", "gavin newsom", "2019", "genocide"],
            "n": 0
        },
        {
            "id": "marshall-statue",
            "tier": "power",
            "t": "A statue of Marshall at Coloma stands over his grave, pointing toward the discovery spot; Sutter’s Fort grew into Sacramento",
            "k": ["statue", "grave", "sacramento"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Which gold rush?",
        "body": "Several gold rushes show up in quiz bowl. The California gold rush began at Sutter’s Mill in 1848 and peaked with the forty-niners in 1849. The Klondike Gold Rush (1896–1899) took place in Canada’s Yukon, reached through Alaska, and Georgia’s 1829 rush near Dahlonega helped push the Cherokee off their land. Charlie Chaplin’s famous 1925 film _The Gold Rush_ is set in the Klondike, not California.",
        "fix": "Sutter’s Mill, James Marshall, Coloma, Sam Brannan, forty-niners, and Levi Strauss mean California. Skagway, Dawson City, and the Yukon mean the Klondike. Saying just “California” names the state, not the event, and a plain “gold rush” earns only a prompt.",
        "line": "Real answer line: <b><u>California gold rush</u></b> (accept <u>Gold Rush of 1849</u>; prompt on <u>gold rush</u>; do not accept “California” alone)"
    },
    "tests": {
        "right": [
            "California Gold Rush",
            "Gold Rush of 1849",
            "the California gold rush",
            "Califonia gold rush",
            "1849 gold rush"
        ],
        "prompt": [
            "gold rush",
            "Sutter's Mill"
        ],
        "wrong": [
            "California",
            "Klondike Gold Rush",
            "Oregon Trail",
            "Donner Party",
            "Comstock Lode",
            "Sutter's Fort",
            "Manifest Destiny"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
