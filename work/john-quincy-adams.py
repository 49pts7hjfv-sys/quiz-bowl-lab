"""Build topics/john-quincy-adams.json (American History). QBReader mode OFF: written from known stock clues."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "john-quincy-adams",
    "name": "John Quincy Adams",
    "mono": "JQA",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "6th U.S. President · Son of John Adams and “Old Man Eloquent” in Congress",
    "dates": "1767–1848",
    "briefing": (
        "John Quincy Adams watched the Battle of Bunker Hill from a hilltop when he was seven, and he spent the rest "
        "of his life serving his country. The son of John Adams, he helped end the War of 1812, wrote most of the "
        "Monroe Doctrine, and won a disputed election in 1824 to become the 6th president. After losing to Andrew "
        "Jackson, he served 17 years in the House of Representatives, where he fought a “gag rule” that blocked "
        "antislavery petitions."
    ),
    "answerHtml": "<b><u>John Quincy Adams</u></b> (or <b><u>JQA</u></b>; prompt on <u>Adams</u>; do not accept “John Adams”)",
    "accept": [
        "john quincy adams",
        "jqa",
        "j q a",
        "quincy adams",
        "john q adams",
        "j q adams",
        "president john quincy adams",
    ],
    "prompt": [
        "adams",
        "president adams",
        "john quincy",
        "quincy",
    ],
    "reject": [
        "john adams",
        "president john adams",
        "samuel adams",
        "sam adams",
        "abigail adams",
        "abigail",
        "louisa adams",
        "louisa catherine adams",
        "louisa catherine johnson",
        "charles francis adams",
        "henry adams",
        "andrew jackson",
        "jackson",
        "henry clay",
        "clay",
        "james monroe",
        "monroe",
        "monroe doctrine",
        "john c calhoun",
        "calhoun",
        "william crawford",
        "crawford",
    ],
    "tests": {
        "right": [
            "John Quincy Adams",
            "JQA",
            "J.Q. Adams",
            "John Q. Adams",
            "Jon Quincy Adams",
            "President John Quincy Adams",
        ],
        "prompt": [
            "Adams",
            "John Quincy",
        ],
        "wrong": [
            "John Adams",
            "Samuel Adams",
            "Abigail Adams",
            "Andrew Jackson",
            "Henry Clay",
            "Louisa Adams",
            "James Monroe",
        ],
    },
    "mediaPending": True,
    "media": [],
    "wiki": "https://en.wikipedia.org/wiki/John_Quincy_Adams",
    "qb": {
        "q": "John Quincy Adams",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it.",
    },
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        {
            "p": "In his first annual message to Congress, this president called for a national university and astronomical observatories, which he called “lighthouses of the skies.” He also asked for federal spending on roads and canals and a naval academy, but critics mocked his plans.",
            "r": "He had won the presidency in the House of Representatives after the election of 1824. For 10 points, name this sixth president.",
        },
        {
            "p": "While serving as minister to Russia, this man turned down a seat on the Supreme Court after James Madison nominated him. Years earlier, at age 14, he had traveled to St. Petersburg as a secretary for the American diplomat Francis Dana.",
            "r": "For 10 points, name this son of John and Abigail Adams who became the sixth president of the United States.",
        },
        {
            "p": "As a seven-year-old, this future president watched the Battle of Bunker Hill from a hilltop with his mother. He later taught rhetoric and oratory as a professor at Harvard while also serving as a U.S. senator.",
            "r": "He was the first president whose father had also been president. For 10 points, name this sixth president.",
        },
        {
            "p": "In 1841, this former president argued before the Supreme Court on behalf of Africans who had taken over the Spanish ship _La Amistad_, and the Court ruled that they should go free. Anthony Hopkins played him in a 1997 Steven Spielberg film about the case.",
            "r": "For 10 points, name this sixth president, who served in Congress after leaving the White House.",
        },
        {
            "p": "For eight years, this congressman fought the “gag rule,” which automatically tabled antislavery petitions sent to the House, until it was finally repealed in 1844. His speeches in Congress earned him the nickname “Old Man Eloquent.”",
            "r": "For 10 points, name this former president who served in the House after leaving the White House.",
        },
        {
            "p": "This congressman collapsed at his desk in the House of Representatives in 1848 and died two days later in the Capitol, reportedly saying, “This is the last of earth. I am content.” A young Illinois congressman named Abraham Lincoln was serving in the House at the time.",
            "r": "For 10 points, name this man who had been the sixth president, the son of the second.",
        },
        {
            "p": "In a four-way presidential race that also included William Crawford and Henry Clay, this man finished second in both popular and electoral votes, but no candidate won a majority of electoral votes. Under the Twelfth Amendment, the House had to choose among the top three finishers, which left Clay out.",
            "r": "The House chose this man over Andrew Jackson, who called the result a “corrupt bargain.” For 10 points, name this winner of the election of 1824.",
        },
        {
            "p": "As Secretary of State, this man convinced James Monroe to issue a warning to Europe on America’s own, rather than jointly with Britain, as British foreign secretary George Canning had proposed. He held that cabinet job for all eight years of Monroe’s presidency.",
            "r": "For 10 points, name this man who wrote most of the Monroe Doctrine and later became the sixth president.",
        },
        {
            "p": "This diplomat negotiated the Transcontinental Treaty with Spain’s minister Luis de Onís [“oh-NEES”], which gave Florida to the United States and drew a border with Spanish lands all the way to the Pacific. He also defended Andrew Jackson’s invasion of Florida when other cabinet members wanted Jackson punished.",
            "r": "For 10 points, name this Secretary of State under James Monroe who later became the sixth president.",
        },
        {
            "p": "This diplomat led the American team, which also included Henry Clay and Albert Gallatin, that negotiated a Christmas Eve treaty in what is now Belgium. He later served as minister to Great Britain, a post his father had held.",
            "r": "That treaty ended the War of 1812. For 10 points, name this son of the second president who became the sixth president.",
        },
        {
            "p": "Southerners called a tariff this president signed in 1828 the “Tariff of Abominations,” and his own vice president, John C. Calhoun, secretly wrote a protest against it. That protest was called the “South Carolina Exposition and Protest.”",
            "r": "Later that year, this president lost his bid for reelection to Andrew Jackson. For 10 points, name this sixth president.",
        },
        {
            "p": "This congressman led a long fight to make sure that money left to the United States by the British scientist James Smithson was used, as Smithson’s will asked, for “the increase and diffusion of knowledge.” Some members of Congress had wanted to refuse the gift.",
            "r": "That gift founded the Smithsonian Institution. For 10 points, name this former president who later served in the House.",
        },
        {
            "p": "This president’s wife, Louisa Catherine, was born in London, making her the first First Lady born outside the United States. He refused to attend the inauguration of the man who defeated him.",
            "r": "His father had done the same in 1801. For 10 points, name this sixth president, the son of John and Abigail Adams.",
        },
        {
            "p": "Elected to the Senate as a Federalist from Massachusetts, this man angered his party by supporting Thomas Jefferson’s Embargo Act, and he resigned his seat in 1808. He had earlier served as minister to the Netherlands and to Prussia.",
            "r": "For 10 points, name this man who later became the sixth president, following in his father’s footsteps.",
        },
        {
            "p": "This president often began his day with a swim in the Potomac River, and the diary he kept for more than sixty years is a famous record of early American politics. He is buried in a Massachusetts church nicknamed the “Church of the Presidents.”",
            "r": "His parents are buried there too. For 10 points, name this sixth president, the son of John Adams.",
        },
    ],
    "clues": [
        {
            "id": "sixth-president",
            "tier": "giveaway",
            "t": "6th President (1825–1829)",
            "k": ["6th president", "sixth", "1825"],
            "n": 0,
        },
        {
            "id": "son-of",
            "tier": "giveaway",
            "t": "Son of John Adams, the 2nd president, and Abigail Adams",
            "k": ["2nd president", "second president", "abigail"],
            "n": 0,
            "rabbit": "John Adams",
        },
        {
            "id": "corrupt-bargain",
            "tier": "giveaway",
            "t": "Won the election of 1824 in the House; Andrew Jackson called it a “corrupt bargain” with Henry Clay",
            "k": ["corrupt bargain", "1824", "henry clay", "andrew jackson"],
            "n": 0,
            "rabbit": "Andrew Jackson",
        },
        {
            "id": "monroe-doctrine",
            "tier": "giveaway",
            "t": "As James Monroe’s Secretary of State, wrote most of the Monroe Doctrine (1823)",
            "k": ["monroe doctrine", "secretary of state", "1823"],
            "n": 0,
            "rabbit": "James Monroe",
        },
        {
            "id": "lost-1828",
            "tier": "middle",
            "t": "Lost the 1828 election to Andrew Jackson and, like his father, skipped his successor’s inauguration",
            "k": ["1828", "inauguration", "jackson"],
            "n": 0,
        },
        {
            "id": "amistad",
            "tier": "middle",
            "t": "Argued the _Amistad_ case (1841) before the Supreme Court, winning freedom for Africans who had taken over the ship",
            "k": ["amistad", "supreme court", "1841"],
            "n": 0,
        },
        {
            "id": "gag-rule",
            "tier": "middle",
            "t": "In the House, fought the “gag rule” blocking antislavery petitions until it was repealed in 1844",
            "k": ["gag rule", "petitions", "1844"],
            "n": 0,
        },
        {
            "id": "house-years",
            "tier": "middle",
            "t": "Served 17 years in the House of Representatives after his presidency (1831–1848)",
            "k": ["house of representatives", "17 years", "1831"],
            "n": 0,
        },
        {
            "id": "old-man-eloquent",
            "tier": "middle",
            "t": "Nicknamed “Old Man Eloquent” for his speeches in Congress",
            "k": ["old man eloquent", "eloquent"],
            "n": 0,
        },
        {
            "id": "collapse",
            "tier": "middle",
            "t": "Collapsed at his desk in the House in 1848 and died two days later: “This is the last of earth. I am content.”",
            "k": ["collapsed", "last of earth", "1848"],
            "n": 0,
        },
        {
            "id": "ghent",
            "tier": "middle",
            "t": "Led the Americans who negotiated the Treaty of Ghent (1814), ending the War of 1812",
            "k": ["treaty of ghent", "ghent", "war of 1812"],
            "n": 0,
            "rabbit": "War of 1812",
        },
        {
            "id": "tariff-abominations",
            "tier": "middle",
            "t": "Signed the Tariff of 1828, which Southerners called the “Tariff of Abominations”",
            "k": ["tariff of abominations", "abominations", "tariff of 1828"],
            "n": 0,
        },
        {
            "id": "bunker-hill",
            "tier": "middle",
            "t": "As a seven-year-old, watched the Battle of Bunker Hill (1775) with his mother",
            "k": ["bunker hill", "1775", "seven-year-old"],
            "n": 0,
        },
        {
            "id": "lighthouses",
            "tier": "power",
            "t": "His first annual message (1825) asked for a national university and observatories, “lighthouses of the skies”",
            "k": ["lighthouses of the skies", "lighthouses", "observatories", "national university"],
            "n": 0,
        },
        {
            "id": "russia",
            "tier": "power",
            "t": "At 14, went to Russia as secretary to diplomat Francis Dana; later U.S. minister to Russia",
            "k": ["russia", "francis dana", "dana"],
            "n": 0,
        },
        {
            "id": "supreme-court",
            "tier": "power",
            "t": "Turned down a seat on the Supreme Court after James Madison nominated him (1811)",
            "k": ["turned down", "madison", "1811"],
            "n": 0,
        },
        {
            "id": "transcontinental",
            "tier": "power",
            "t": "Negotiated the Transcontinental Treaty with Spain’s Luis de Onís (1819), which gave Florida to the United States",
            "k": ["transcontinental", "luis de onís", "onís", "florida"],
            "n": 0,
        },
        {
            "id": "defended-jackson",
            "tier": "power",
            "t": "In Monroe’s cabinet, defended Andrew Jackson’s 1818 invasion of Spanish Florida",
            "k": ["spanish florida", "defended", "1818"],
            "n": 0,
        },
        {
            "id": "twelfth-amendment",
            "tier": "power",
            "t": "In 1824, the 12th Amendment sent the race to the House, which chose among the top three; fourth-place Henry Clay was left out",
            "k": ["12th amendment", "twelfth", "top three"],
            "n": 0,
        },
        {
            "id": "smithsonian",
            "tier": "power",
            "t": "Fought to use James Smithson’s gift for its intended purpose, founding the Smithsonian Institution",
            "k": ["smithsonian", "smithson"],
            "n": 0,
        },
        {
            "id": "harvard",
            "tier": "power",
            "t": "Taught rhetoric and oratory as a Harvard professor while also serving in the Senate",
            "k": ["harvard", "rhetoric", "oratory"],
            "n": 0,
        },
        {
            "id": "louisa",
            "tier": "power",
            "t": "His wife, Louisa Catherine, born in London, was the first First Lady born outside the United States",
            "k": ["louisa", "london", "born outside"],
            "n": 0,
        },
        {
            "id": "embargo",
            "tier": "power",
            "t": "As a Federalist senator from Massachusetts, backed Jefferson’s Embargo Act and resigned his seat in 1808",
            "k": ["embargo", "federalist", "1808"],
            "n": 0,
        },
        {
            "id": "calhoun",
            "tier": "power",
            "t": "Vice President John C. Calhoun secretly wrote the “South Carolina Exposition and Protest” against his 1828 tariff",
            "k": ["calhoun", "exposition and protest", "south carolina"],
            "n": 0,
        },
        {
            "id": "amistad-film",
            "tier": "power",
            "t": "Played by Anthony Hopkins in Steven Spielberg’s film _Amistad_ (1997)",
            "k": ["anthony hopkins", "hopkins", "spielberg"],
            "n": 0,
        },
        {
            "id": "diary",
            "tier": "power",
            "t": "Kept a diary for more than sixty years and liked morning swims in the Potomac; buried in Massachusetts’s “Church of the Presidents”",
            "k": ["diary", "potomac", "church of the presidents"],
            "n": 0,
        },
        {
            "id": "diplomat-posts",
            "tier": "power",
            "t": "Minister to the Netherlands (named by Washington) and Prussia (named by his father); later minister to Great Britain",
            "k": ["netherlands", "prussia", "great britain"],
            "n": 0,
        },
    ],
    "trap": {
        "title": "Father or son?",
        "body": "John Quincy Adams (6th president) and his father, John Adams (2nd president), were both Massachusetts diplomats who served one term as president and skipped the next president’s inauguration. Real answer lines say “do not accept John Adams,” so leaving out “Quincy” loses the tossup, and saying only “Adams” earns just a prompt. Samuel Adams, John Adams’s cousin, is a third Adams to avoid.",
        "fix": "Son clues: the Treaty of Ghent, the Monroe Doctrine, the “corrupt bargain” of 1824, the Tariff of Abominations, the gag rule, the Amistad case, and dying in the Capitol in 1848. Father clues: the Boston Massacre trial, the XYZ Affair, the Alien and Sedition Acts, and dying on July 4, 1826. When prompted, say “John Quincy Adams.”",
        "line": "Real answer line: <b><u>John Quincy Adams</u></b> (or <b><u>JQA</u></b>; prompt on <u>Adams</u>; do not accept or prompt on “John Adams”)",
    },
}

out = ROOT / "topics" / f"{data['id']}.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", out)
