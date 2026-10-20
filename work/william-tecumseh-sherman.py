import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "william-tecumseh-sherman",
    "name": "William Tecumseh Sherman",
    "mono": "WTS",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Union general of the Civil War · Led the March to the Sea",
    "dates": "1820–1891",
    "briefing": "William Tecumseh Sherman, named after the Shawnee leader Tecumseh, was a Union general who captured Atlanta in 1864 and then marched more than 60,000 soldiers across Georgia to Savannah, wrecking railroads, farms, and factories along the way. His March to the Sea brought the war home to Southern civilians and helped end the Civil War. He is remembered for a blunt summary of fighting: “War is hell.”",
    "answerHtml": "William Tecumseh <b><u>Sherman</u></b> (do not accept “Tecumseh”)",
    "accept": [
        "sherman",
        "william tecumseh sherman",
        "general william tecumseh sherman",
        "gen william tecumseh sherman",
        "union general william tecumseh sherman",
        "general w tecumseh sherman",
        "tecumseh sherman",
        "w tecumseh sherman",
        "william t sherman",
        "w t sherman",
        "william sherman",
        "general sherman",
        "cump sherman"
    ],
    "prompt": [],
    "reject": [
        "tecumseh",
        "roger sherman",
        "john sherman",
        "james s sherman",
        "james sherman",
        "sherman antitrust act",
        "sherman act",
        "sherman silver purchase act",
        "sherman tank",
        "m4 sherman",
        "general sherman tree",
        "philip sheridan",
        "sheridan",
        "ulysses s grant",
        "grant",
        "george thomas",
        "john bell hood",
        "joseph e johnston"
    ],
    "mediaPending": True,
    "media": [],
    "wiki": "https://en.wikipedia.org/wiki/William_Tecumseh_Sherman",
    "qb": {
        "q": "Sherman",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Augustus Saint-Gaudens made a gilded statue of this general on horseback, led by a winged Victory, that stands near Central Park in New York City. When this man died in 1891, his old opponent Joseph E. Johnston stood bareheaded in the rain at his funeral.",
            "r": "Johnston caught pneumonia and died weeks later. For 10 points, name this Union general who led the March to the Sea."
        },
        {
            "p": "After meeting with Black ministers in Savannah, this general issued Special Field Orders No. 15, which set aside land along the coasts of South Carolina, Georgia, and Florida for freed families in plots of up to 40 acres. Andrew Johnson later returned most of that land to its former owners.",
            "r": "That order inspired the phrase “forty acres and a mule.” For 10 points, name this Union general who had just finished his March to the Sea."
        },
        {
            "p": "Before the Civil War, this man was the first superintendent of a Louisiana military school that later became Louisiana State University, but he resigned as Louisiana prepared to secede. Earlier, he had been a banker in San Francisco.",
            "r": "He later fought at Shiloh and Vicksburg. For 10 points, name this Union general who captured Atlanta in 1864."
        },
        {
            "p": "After his father died in 1829, this boy from Lancaster, Ohio, was raised by the family of Thomas Ewing, who later became a senator and the first secretary of the interior. He married Ewing’s daughter Ellen and graduated from West Point in 1840.",
            "r": "His family called him “Cump,” short for a middle name that honored a Shawnee leader. For 10 points, name this Union general who marched from Atlanta to Savannah."
        },
        {
            "p": "Early in the Civil War, newspapers called this general insane after he told the secretary of war that it would take 200,000 soldiers to win the war in the West, and he was sent home to rest. He recovered and commanded a division at Shiloh.",
            "r": "He later became Ulysses S. Grant’s most trusted general. For 10 points, name this man who led the March to the Sea."
        },
        {
            "p": "This general’s frontal assault at Kennesaw Mountain failed in June 1864, but he kept moving around Joseph E. Johnston’s army until Jefferson Davis replaced Johnston with John Bell Hood. Hood could not hold the city he was defending.",
            "r": "In September, this general telegraphed, “Atlanta is ours, and fairly won.” For 10 points, name this Union general."
        },
        {
            "p": "This general wrote to Mayor James Calhoun that “war is cruelty, and you cannot refine it” after ordering civilians to leave the city they lived in. He argued that the people who had brought on the war deserved the hardships it caused them.",
            "r": "He is also remembered for saying that “war is hell.” For 10 points, name this Union general who captured Atlanta."
        },
        {
            "p": "In December 1864, this general’s soldiers stormed Fort McAllister, opening a supply line to the sea. Days later, he telegraphed Abraham Lincoln to present a city as a “Christmas gift,” along with 150 heavy guns and about 25,000 bales of cotton.",
            "r": "That city was Savannah, the end of his March to the Sea. For 10 points, name this Union general."
        },
        {
            "p": "At Bennett Place near Durham, North Carolina, this general accepted the surrender of Joseph E. Johnston’s army in April 1865, the largest surrender of the Civil War. Edwin Stanton angrily rejected the generous peace terms this general had first offered Johnston.",
            "r": "Earlier, he had captured Atlanta and Savannah. For 10 points, name this Union general who had led the March to the Sea."
        },
        {
            "p": "In 1884, this retired general refused the Republican presidential nomination so firmly that a flat refusal to run for office became known by his name. His brother John, a senator from Ohio, sponsored a famous 1890 antitrust law.",
            "r": "Earlier, he had captured Atlanta in 1864. For 10 points, name this Union general famous for his March to the Sea."
        },
        {
            "p": "After the Civil War, this man served on a peace commission that signed the 1868 Treaty of Fort Laramie with the Lakota and other Plains nations. That same year, he signed a treaty that let the Navajo return to their homeland after the Long Walk.",
            "r": "He commanded the U.S. Army from 1869 to 1883. For 10 points, name this Union general who led the March to the Sea."
        },
        {
            "p": "This general’s soldiers heated railroad rails over bonfires and twisted them around trees, making what were nicknamed his “neckties.” Foragers from his army, called “bummers,” took food and livestock from farms across Georgia, and his army of about 60,000 men cut a path roughly 60 miles wide.",
            "r": "For 10 points, name this general who led the March to the Sea from Atlanta to Savannah."
        },
        {
            "p": "The M4 tank of World War II was named for this man, and so was a giant sequoia in California that is the largest single tree on Earth by volume. In 1875, he published two volumes of memoirs about his campaigns.",
            "r": "He served under Ulysses S. Grant in the Civil War. For 10 points, name this Union general who captured Atlanta and marched to Savannah."
        },
        {
            "p": "In February 1865, much of Columbia, South Carolina, burned after this general’s army entered the city, though historians disagree about who started the fires. A month later, his army defeated Joseph E. Johnston at Bentonville, North Carolina.",
            "r": "His army had captured Atlanta the year before. For 10 points, name this Union general whose March to the Sea had ended at Savannah."
        },
        {
            "p": "This general’s troops were caught by surprise on the first morning of the Battle of Shiloh, and he was wounded in the hand there. In 1864, he replaced Ulysses S. Grant as the top Union commander in the West when Grant went east.",
            "r": "For 10 points, name this general who captured Atlanta and led the March to the Sea."
        }
    ],
    "clues": [
        {
            "id": "march-to-sea",
            "tier": "giveaway",
            "t": "Led the March to the Sea from Atlanta to Savannah, Georgia (November–December 1864)",
            "k": ["march to the sea", "savannah", "georgia"],
            "n": 0
        },
        {
            "id": "atlanta",
            "tier": "giveaway",
            "t": "Captured Atlanta in September 1864, helping Abraham Lincoln win reelection",
            "k": ["atlanta", "1864", "reelection"],
            "n": 0,
            "rabbit": "Atlanta"
        },
        {
            "id": "war-is-hell",
            "tier": "giveaway",
            "t": "Famous for saying “war is hell”",
            "k": ["war is hell", "hell"],
            "n": 0
        },
        {
            "id": "union-general",
            "tier": "giveaway",
            "t": "Union general in the Civil War and Ulysses S. Grant’s most trusted partner",
            "k": ["union general", "grant", "civil war"],
            "n": 0,
            "rabbit": "Ulysses S. Grant"
        },
        {
            "id": "total-war",
            "tier": "giveaway",
            "t": "Waged “total war,” destroying railroads, farms, and supplies to break the South’s will to fight",
            "k": ["total war", "railroads", "farms"],
            "n": 0
        },
        {
            "id": "shawnee-name",
            "tier": "middle",
            "t": "His middle name honored the Shawnee leader Tecumseh; his family called him “Cump”",
            "k": ["shawnee", "cump", "middle name"],
            "n": 0,
            "rabbit": "Tecumseh"
        },
        {
            "id": "christmas-gift",
            "tier": "middle",
            "t": "Presented Savannah to Lincoln as a “Christmas gift” (December 1864)",
            "k": ["christmas gift", "christmas", "lincoln"],
            "n": 0
        },
        {
            "id": "field-orders",
            "tier": "middle",
            "t": "Special Field Orders No. 15 (1865) set aside coastal land for freed families: “forty acres and a mule”",
            "k": ["field orders no. 15", "forty acres", "mule"],
            "n": 0,
            "rabbit": "Reconstruction"
        },
        {
            "id": "atlanta-is-ours",
            "tier": "middle",
            "t": "Telegraphed “Atlanta is ours, and fairly won” (September 1864)",
            "k": ["atlanta is ours", "fairly won"],
            "n": 0
        },
        {
            "id": "neckties",
            "tier": "middle",
            "t": "His troops twisted heated rails around trees (his “neckties”); his foragers were called “bummers”",
            "k": ["neckties", "bummers", "rails"],
            "n": 0
        },
        {
            "id": "bennett-place",
            "tier": "middle",
            "t": "Accepted Joseph E. Johnston’s surrender at Bennett Place, North Carolina (April 1865), the largest of the war",
            "k": ["bennett place", "joseph e. johnston", "johnston"],
            "n": 0
        },
        {
            "id": "battles",
            "tier": "middle",
            "t": "Fought at First Bull Run, Shiloh (wounded in the hand), Vicksburg, and Chattanooga",
            "k": ["shiloh", "bull run", "vicksburg", "chattanooga"],
            "n": 0
        },
        {
            "id": "commanding-general",
            "tier": "middle",
            "t": "Commanding general of the U.S. Army (1869–1883), after Grant became president",
            "k": ["commanding general", "1869", "1883"],
            "n": 0
        },
        {
            "id": "refusal-1884",
            "tier": "power",
            "t": "Refused the 1884 Republican nomination so firmly that a flat refusal to run is named for him",
            "k": ["1884", "refused", "nomination"],
            "n": 0
        },
        {
            "id": "insane",
            "tier": "power",
            "t": "Newspapers called him insane in 1861 after he said it would take 200,000 soldiers to win in the West",
            "k": ["insane", "200,000", "newspapers"],
            "n": 0
        },
        {
            "id": "lsu",
            "tier": "power",
            "t": "First superintendent of the military school that became Louisiana State University (LSU)",
            "k": ["louisiana state university", "lsu", "superintendent"],
            "n": 0
        },
        {
            "id": "ewing",
            "tier": "power",
            "t": "Raised by Thomas Ewing’s family in Lancaster, Ohio; married Ellen Ewing; West Point class of 1840",
            "k": ["thomas ewing", "ewing", "lancaster", "west point"],
            "n": 0
        },
        {
            "id": "calhoun",
            "tier": "power",
            "t": "Told Atlanta’s mayor, James Calhoun, that “war is cruelty, and you cannot refine it”",
            "k": ["war is cruelty", "calhoun", "refine"],
            "n": 0
        },
        {
            "id": "kennesaw",
            "tier": "power",
            "t": "His frontal assault at Kennesaw Mountain failed (June 1864); Jefferson Davis replaced Johnston with John Bell Hood",
            "k": ["kennesaw mountain", "kennesaw", "john bell hood", "hood"],
            "n": 0
        },
        {
            "id": "columbia",
            "tier": "power",
            "t": "Columbia, South Carolina, burned after his army arrived during his Carolinas campaign (February 1865); won at Bentonville",
            "k": ["columbia", "bentonville", "carolinas"],
            "n": 0
        },
        {
            "id": "stanton",
            "tier": "power",
            "t": "Edwin Stanton rejected the generous surrender terms he first offered Johnston",
            "k": ["stanton", "generous", "terms"],
            "n": 0
        },
        {
            "id": "saint-gaudens",
            "tier": "power",
            "t": "Augustus Saint-Gaudens’s gilded statue of him, led by Victory, stands near Central Park in New York",
            "k": ["saint-gaudens", "central park", "victory"],
            "n": 0
        },
        {
            "id": "johnston-funeral",
            "tier": "power",
            "t": "Died in 1891; Joseph E. Johnston caught pneumonia after standing bareheaded at his funeral",
            "k": ["1891", "funeral", "pneumonia", "bareheaded"],
            "n": 0
        },
        {
            "id": "namesakes",
            "tier": "power",
            "t": "The M4 tank of World War II and a giant sequoia, the largest tree by volume, are named for him",
            "k": ["m4", "tank", "sequoia"],
            "n": 0
        },
        {
            "id": "fort-laramie",
            "tier": "power",
            "t": "Served on the peace commission for the Treaty of Fort Laramie (1868); signed the treaty letting the Navajo go home after the Long Walk",
            "k": ["fort laramie", "navajo", "peace commission", "long walk"],
            "n": 0
        },
        {
            "id": "brother-john",
            "tier": "power",
            "t": "His brother John, an Ohio senator, sponsored the 1890 antitrust act that bears their family name",
            "k": ["brother", "antitrust", "1890"],
            "n": 0,
            "rabbit": "Sherman Antitrust Act"
        },
        {
            "id": "mcallister",
            "tier": "power",
            "t": "His troops stormed Fort McAllister (December 1864) just before he took Savannah",
            "k": ["fort mcallister", "mcallister"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Which Sherman? Not Tecumseh!",
        "body": "Several famous answers share his name. Roger Sherman of Connecticut proposed the Connecticut Compromise and signed the Declaration of Independence, the Articles of Confederation, and the Constitution. John Sherman, the general’s younger brother, was the senator behind the Sherman Antitrust Act. And Tecumseh, the Shawnee leader he was named after, is a separate answer line, so saying just “Tecumseh” is wrong.",
        "fix": "William Tecumseh Sherman clues: Atlanta, the March to the Sea, Savannah as a “Christmas gift,” Special Field Orders No. 15, and “war is hell.” The Connecticut Compromise means Roger Sherman; antitrust or silver laws mean John Sherman; Prophetstown, Tippecanoe, and the War of 1812 mean Tecumseh. Saying “Sherman” is enough.",
        "line": "Real answer line: William Tecumseh <b><u>Sherman</u></b> (do not accept “Tecumseh”)"
    },
    "tests": {
        "right": [
            "William Tecumseh Sherman",
            "Sherman",
            "General William Tecumseh Sherman",
            "W. T. Sherman",
            "William T. Sherman",
            "Shermen"
        ],
        "prompt": [],
        "wrong": [
            "Tecumseh",
            "Roger Sherman",
            "John Sherman",
            "Sherman Antitrust Act",
            "Philip Sheridan",
            "Ulysses S. Grant"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
