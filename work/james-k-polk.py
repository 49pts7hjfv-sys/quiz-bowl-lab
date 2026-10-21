import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "james-k-polk",
    "name": "James K. Polk",
    "mono": "JKP",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "11th U.S. President · Led the nation in the Mexican-American War",
    "dates": "1795–1849",
    "briefing": "James K. Polk was such a surprise choice in 1844 that his Whig opponents mocked him by asking, “Who is James K. Polk?” He became the first “dark horse” president, set four big goals, and met every one of them. Under Polk, the United States settled the Oregon boundary with Britain and won California and the Southwest in the Mexican-American War. He kept his promise to serve only one term and died just over three months after leaving office.",
    "answerHtml": "James K. <b><u>Polk</u></b> (accept James Knox <u>Polk</u>; do not accept “Zachary Taylor” or “Franklin Pierce”)",
    "accept": [
        "james k polk",
        "polk",
        "james polk",
        "james knox polk",
        "president polk",
        "president james k polk",
        "j k polk"
    ],
    "prompt": [
        "young hickory"
    ],
    "reject": [
        "andrew jackson",
        "jackson",
        "old hickory",
        "zachary taylor",
        "taylor",
        "franklin pierce",
        "pierce",
        "john tyler",
        "tyler",
        "james buchanan",
        "buchanan",
        "martin van buren",
        "van buren",
        "henry clay",
        "james monroe",
        "james madison",
        "millard fillmore",
        "sarah polk",
        "sarah childress polk",
        "leonidas polk",
        "george m dallas",
        "george dallas",
        "robert j walker",
        "john slidell",
        "nicholas trist",
        "winfield scott",
        "santa anna",
        "antonio lopez de santa anna",
        "manifest destiny",
        "mexican american war",
        "oregon treaty"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/James_K._Polk",
    "qb": {
        "q": "Polk",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "This man is the only Speaker of the House who later became president; he held that post from 1835 to 1839. Before winning the White House, he also served a single term as governor of Tennessee.",
            "r": "As a loyal follower of Andrew Jackson, he was nicknamed “Young Hickory.” For 10 points, name this 11th president."
        },
        {
            "p": "At the 1844 Democratic convention in Baltimore, Martin Van Buren could not win the two-thirds vote he needed, partly because he opposed annexing Texas. On the ninth ballot, the delegates turned instead to this former Speaker of the House from Tennessee.",
            "r": "He became the first “dark horse” presidential nominee. For 10 points, name this man who then beat Henry Clay in the 1844 election."
        },
        {
            "p": "Treasury Secretary Robert J. Walker gave his name to a law this president signed in 1846 that lowered tariff rates. That same year, this president restored the Independent Treasury, which kept federal money in government hands instead of in private banks.",
            "r": "For 10 points, name this president who also settled the Oregon boundary and won California in the Mexican-American War."
        },
        {
            "p": "The Bidlack Treaty, signed during this president’s term, gave the United States the right to move people and goods across the Isthmus of Panama, then part of New Granada. In his first annual message to Congress, this president restated the Monroe Doctrine to warn European powers against meddling in North America.",
            "r": "For 10 points, name this president who believed in Manifest Destiny and led the nation in the Mexican-American War."
        },
        {
            "p": "After Mexico refused to receive his envoy John Slidell, this president ordered General Zachary Taylor to march to the Rio Grande. When Mexican troops attacked an American patrol there, this president told Congress that Mexico had “shed American blood upon the American soil.”",
            "r": "For 10 points, name this president who asked Congress to declare war on Mexico in 1846."
        },
        {
            "p": "David Wilmot tried to attach a ban on slavery in any land won from Mexico to a spending bill this president had requested. Whig critics named the war after this president, and a one-term Illinois congressman challenged him to name the exact “spot” where it began.",
            "r": "That congressman was Abraham Lincoln. For 10 points, name this president who led the U.S. in the Mexican-American War."
        },
        {
            "p": "Secretary of State James Buchanan and the British minister Richard Pakenham signed a treaty under this president that divided a disputed region of the Pacific Northwest along the 49th parallel. That 1846 treaty gave the United States land that includes the present-day states of Washington, Oregon, and Idaho.",
            "r": "Expansionists had demanded more with the cry “Fifty-four forty or fight!” For 10 points, name this president who settled the Oregon question."
        },
        {
            "p": "According to Navy Secretary George Bancroft, this president named four goals early in his term: lowering the tariff, restoring an independent treasury, settling the Oregon question, and acquiring California. He achieved all four and kept his promise to serve only one term.",
            "r": "For 10 points, name this president who led the nation during the Mexican-American War."
        },
        {
            "p": "Congress created the Smithsonian Institution under this president, using money left by the British scientist James Smithson, and his navy secretary founded the Naval Academy at Annapolis. On March 3, 1849, the day before his term ended, this president signed the law creating the Department of the Interior.",
            "r": "For 10 points, name this 11th president, a Democrat from Tennessee who served from 1845 to 1849."
        },
        {
            "p": "In his December 1848 message to Congress, this president confirmed reports of gold in newly acquired California, helping set off a rush of fortune seekers. Earlier that year, the Senate had approved the Treaty of Guadalupe Hidalgo, which ended the war he had led.",
            "r": "He served only one term. For 10 points, name this president who led the U.S. in the Mexican-American War."
        },
        {
            "p": "This president ordered his diplomat Nicholas Trist to come home, but Trist stayed in Mexico and negotiated a peace treaty anyway. Though angry at Trist, this president sent the treaty to the Senate because it gave him most of what he wanted, including California.",
            "r": "That treaty was the Treaty of Guadalupe Hidalgo. For 10 points, name this president who led the U.S. through the Mexican-American War."
        },
        {
            "p": "Just over three months after leaving office, this president died of cholera in Nashville, giving him the shortest retirement of any president. His tomb stands on the grounds of the Tennessee State Capitol.",
            "r": "He had promised to serve only one term, and he kept that promise. For 10 points, name this president who led the U.S. in the Mexican-American War."
        },
        {
            "p": "This man graduated from the University of North Carolina in 1818 and then studied law in Nashville under Felix Grundy. As chairman of the House Ways and Means Committee, he led Andrew Jackson’s fight against the Second Bank of the United States.",
            "r": "That loyalty earned him the nickname “Young Hickory.” For 10 points, name this man who became the 11th president."
        },
        {
            "p": "In 1844, this candidate narrowly carried New York, and with it the election, partly because the antislavery Liberty Party candidate James G. Birney drew votes away from his Whig opponent. Whigs had mocked this little-known candidate by asking who he was.",
            "r": "That Whig opponent was Henry Clay. For 10 points, name this Democrat who became the 11th president."
        },
        {
            "p": "This president’s vice president, George M. Dallas of Pennsylvania, broke a tie in the Senate to pass a lower tariff in 1846. Just before this president took office, John Tyler signed a joint resolution to annex Texas, which became a state in December 1845.",
            "r": "For 10 points, name this president who championed Manifest Destiny and led the nation in the Mexican-American War."
        }
    ],
    "clues": [
        {
            "id": "eleventh-president",
            "tier": "giveaway",
            "t": "11th President (1845–1849), a Democrat from Tennessee",
            "k": ["11th president", "tennessee", "democrat", "1845"],
            "n": 0
        },
        {
            "id": "mexican-war",
            "tier": "giveaway",
            "t": "Led the U.S. in the Mexican-American War (1846–1848), which won California and the Southwest",
            "k": ["mexican-american war", "california", "southwest"],
            "n": 0,
            "rabbit": "Mexican-American War"
        },
        {
            "id": "manifest-destiny",
            "tier": "giveaway",
            "t": "The president most tied to Manifest Destiny, the belief that the U.S. should stretch across North America",
            "k": ["manifest destiny", "north america"],
            "n": 0,
            "rabbit": "Manifest Destiny"
        },
        {
            "id": "young-hickory",
            "tier": "giveaway",
            "t": "Nicknamed “Young Hickory” as a follower of Andrew Jackson (“Old Hickory”)",
            "k": ["young hickory", "andrew jackson", "old hickory"],
            "n": 0,
            "rabbit": "Andrew Jackson"
        },
        {
            "id": "one-term",
            "tier": "giveaway",
            "t": "Promised to serve only one term, and kept that promise",
            "k": ["one term", "promised"],
            "n": 0
        },
        {
            "id": "dark-horse",
            "tier": "middle",
            "t": "First “dark horse” nominee: chosen on the ninth ballot in 1844, then beat the Whig Henry Clay",
            "k": ["dark horse", "ninth ballot", "henry clay"],
            "n": 0,
            "rabbit": "Henry Clay"
        },
        {
            "id": "speaker",
            "tier": "middle",
            "t": "The only Speaker of the House (1835–1839) who later became president",
            "k": ["speaker of the house", "speaker"],
            "n": 0,
            "rabbit": "Speaker of the House of Representatives"
        },
        {
            "id": "oregon-treaty",
            "tier": "middle",
            "t": "Oregon Treaty (1846): split the Oregon Country with Britain along the 49th parallel",
            "k": ["oregon treaty", "49th parallel", "britain"],
            "n": 0
        },
        {
            "id": "fifty-four-forty",
            "tier": "middle",
            "t": "Expansionists wanted all of Oregon up to 54°40′ north: “Fifty-four forty or fight!”",
            "k": ["fifty-four forty", "or fight"],
            "n": 0
        },
        {
            "id": "four-goals",
            "tier": "middle",
            "t": "Set four goals and met them all: a lower tariff, an independent treasury, Oregon, and California",
            "k": ["four goals", "lower tariff", "independent treasury"],
            "n": 0
        },
        {
            "id": "american-blood",
            "tier": "middle",
            "t": "Told Congress that Mexico had “shed American blood upon the American soil” (1846)",
            "k": ["american blood", "american soil"],
            "n": 0
        },
        {
            "id": "texas",
            "tier": "middle",
            "t": "Texas, annexed by a resolution John Tyler signed just before he took office, became a state in December 1845",
            "k": ["texas", "john tyler", "annexed"],
            "n": 0,
            "rabbit": "Republic of Texas"
        },
        {
            "id": "guadalupe-hidalgo",
            "tier": "middle",
            "t": "The Treaty of Guadalupe Hidalgo (1848) ended the war and gave the U.S. the Mexican Cession",
            "k": ["guadalupe hidalgo", "mexican cession"],
            "n": 0
        },
        {
            "id": "spot-resolutions",
            "tier": "middle",
            "t": "Whigs named the war after him; Congressman Abraham Lincoln’s “Spot Resolutions” challenged his account of how it began",
            "k": ["spot resolutions", "abraham lincoln", "whigs"],
            "n": 0,
            "rabbit": "Abraham Lincoln"
        },
        {
            "id": "walker-tariff",
            "tier": "power",
            "t": "The Walker Tariff (1846), named for Treasury Secretary Robert J. Walker, lowered rates; Vice President George M. Dallas broke the Senate tie",
            "k": ["walker tariff", "robert j. walker", "george m. dallas"],
            "n": 0
        },
        {
            "id": "bancroft",
            "tier": "power",
            "t": "Navy Secretary George Bancroft described the four goals and founded the Naval Academy at Annapolis (1845)",
            "k": ["george bancroft", "bancroft", "naval academy", "annapolis"],
            "n": 0
        },
        {
            "id": "slidell",
            "tier": "power",
            "t": "Sent John Slidell to buy California and New Mexico; Mexico refused to receive him",
            "k": ["john slidell", "slidell"],
            "n": 0
        },
        {
            "id": "wilmot",
            "tier": "power",
            "t": "The Wilmot Proviso (1846) tried to ban slavery in land won from Mexico; it was attached to a spending bill he requested",
            "k": ["wilmot proviso", "wilmot", "slavery"],
            "n": 0
        },
        {
            "id": "trist",
            "tier": "power",
            "t": "Nicholas Trist ignored his recall and negotiated the peace treaty; he angrily sent it to the Senate anyway",
            "k": ["nicholas trist", "trist", "recall"],
            "n": 0
        },
        {
            "id": "pakenham",
            "tier": "power",
            "t": "Secretary of State James Buchanan and British minister Richard Pakenham signed the Oregon Treaty",
            "k": ["richard pakenham", "pakenham", "james buchanan"],
            "n": 0
        },
        {
            "id": "bidlack",
            "tier": "power",
            "t": "The Bidlack Treaty (1846) with New Granada gave the U.S. the right to cross the Isthmus of Panama",
            "k": ["bidlack", "new granada", "panama"],
            "n": 0
        },
        {
            "id": "monroe-doctrine",
            "tier": "power",
            "t": "Restated the Monroe Doctrine in his first annual message (1845), warning Europe not to meddle in North America",
            "k": ["monroe doctrine", "annual message"],
            "n": 0
        },
        {
            "id": "smithsonian-interior",
            "tier": "power",
            "t": "Signed laws creating the Smithsonian Institution (1846) and the Department of the Interior (March 3, 1849)",
            "k": ["smithsonian", "department of the interior", "interior"],
            "n": 0,
            "rabbit": "Smithsonian Institution"
        },
        {
            "id": "gold-message",
            "tier": "power",
            "t": "Confirmed the California gold discovery in his December 1848 message to Congress",
            "k": ["gold", "december 1848"],
            "n": 0,
            "rabbit": "California gold rush"
        },
        {
            "id": "grundy",
            "tier": "power",
            "t": "Graduated from the University of North Carolina (1818) and studied law under Felix Grundy",
            "k": ["felix grundy", "grundy", "university of north carolina"],
            "n": 0
        },
        {
            "id": "bank-war",
            "tier": "power",
            "t": "As chairman of the Ways and Means Committee, led Jackson’s fight against the Second Bank of the United States",
            "k": ["ways and means", "second bank"],
            "n": 0
        },
        {
            "id": "birney",
            "tier": "power",
            "t": "Won New York in 1844 partly because Liberty Party candidate James G. Birney drew votes from Clay",
            "k": ["james g. birney", "birney", "liberty party"],
            "n": 0
        },
        {
            "id": "cholera",
            "tier": "power",
            "t": "Died of cholera in Nashville just over three months after leaving office, the shortest retirement of any president; buried at the Tennessee State Capitol",
            "k": ["cholera", "shortest retirement", "nashville"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Young Hickory, not Old",
        "body": "Polk was Andrew Jackson’s protégé, so his nickname “Young Hickory” sounds a lot like Jackson’s “Old Hickory.” Two other nearby presidents also share his clues: Zachary Taylor, the Mexican War general who became the next president in 1849, and Franklin Pierce, another “dark horse” nominee, who won in 1852 after serving in the same war. John Tyler signed the resolution to annex Texas just days before Polk took office.",
        "fix": "“Old Hickory,” the Battle of New Orleans, and the Indian Removal Act mean Jackson; Buena Vista and “Old Rough and Ready” mean Taylor; the Gadsden Purchase and the Kansas-Nebraska Act mean Pierce. The first dark horse, the four goals, the 49th parallel, and asking Congress to declare war on Mexico mean Polk.",
        "line": "Real answer line: James K. <b><u>Polk</u></b> (accept James Knox <u>Polk</u>)"
    },
    "tests": {
        "right": [
            "James K. Polk",
            "Polk",
            "James Polk",
            "James Knox Polk",
            "President Polk",
            "James K. Pok"
        ],
        "prompt": [
            "Young Hickory"
        ],
        "wrong": [
            "Andrew Jackson",
            "Zachary Taylor",
            "Franklin Pierce",
            "John Tyler",
            "Old Hickory",
            "Leonidas Polk",
            "James Buchanan",
            "Henry Clay"
        ]
    }
}

out = ROOT / "topics" / f"{data['id']}.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", out)
