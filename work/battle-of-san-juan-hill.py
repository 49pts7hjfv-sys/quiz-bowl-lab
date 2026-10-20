import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "battle-of-san-juan-hill",
    "name": "Battle of San Juan Hill",
    "mono": "SJH",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "The Rough Riders’ 1898 charge in Cuba · Made Theodore Roosevelt a hero",
    "dates": "Fought July 1, 1898",
    "briefing": "On July 1, 1898, American soldiers charged up a ridge of hills outside Santiago, Cuba, straight into fire from Spanish rifles. Theodore Roosevelt led his volunteer Rough Riders up nearby Kettle Hill beside the Black troopers known as Buffalo Soldiers, then joined the attack on San Juan Hill. The victory trapped Spain’s army and fleet at Santiago and made Roosevelt so famous that New York elected him governor that fall.",
    "answerHtml": "Battle of <b><u>San Juan Hill</u></b> (or Battle of <b><u>San Juan Heights</u></b>; prompt on <u>Kettle Hill</u>; do not accept “Spanish-American War”)",
    "accept": [
        "san juan hill",
        "battle of san juan hill",
        "battle for san juan hill",
        "san juan heights",
        "battle of san juan heights",
        "battle of the san juan heights"
    ],
    "prompt": [
        "kettle hill",
        "battle of kettle hill",
        "san juan",
        "battle of san juan",
        "santiago campaign"
    ],
    "reject": [
        "el caney",
        "battle of el caney",
        "las guasimas",
        "battle of las guasimas",
        "santiago de cuba",
        "battle of santiago de cuba",
        "manila bay",
        "battle of manila bay",
        "spanish american war",
        "rough riders",
        "buffalo soldiers",
        "bunker hill",
        "battle of bunker hill",
        "san jacinto",
        "battle of san jacinto",
        "puerto rico"
    ],
    "mediaPending": True,
    "media": [],
    "wiki": "https://en.wikipedia.org/wiki/Battle_of_San_Juan_Hill",
    "qb": {
        "q": "San Juan Hill",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "During this battle, an Army Signal Corps observation balloon was towed along a jungle trail above the advancing soldiers. The balloon showed Spanish riflemen exactly where the Americans were, and many soldiers were hit while crowded together at a river crossing below it.",
            "r": "Theodore Roosevelt’s Rough Riders also fought in this battle. For 10 points, name this July 1, 1898, battle outside Santiago, Cuba."
        },
        {
            "p": "Soldiers named one hill in this battle for a huge iron sugar-making pot that they found on its top. Black cavalrymen of the 9th and 10th Cavalry, nicknamed Buffalo Soldiers, helped capture that hill before joining the attack on a ridge topped by a Spanish blockhouse.",
            "r": "Theodore Roosevelt’s Rough Riders charged up that first hill. For 10 points, name this 1898 battle near Santiago, Cuba."
        },
        {
            "p": "Lieutenant John Parker earned the nickname “Gatling Gun” Parker after his detachment of hand-cranked rapid-fire guns raked the Spanish trenches during this battle. That covering fire helped American infantry under Jacob Kent climb to a blockhouse at the top of the main ridge.",
            "r": "Theodore Roosevelt’s Rough Riders fought nearby. For 10 points, name this 1898 battle fought outside Santiago, Cuba."
        },
        {
            "p": "Frederic Remington painted soldiers in this battle charging forward on foot behind a lone officer on horseback. That officer had resigned as Assistant Secretary of the Navy to help raise a volunteer regiment for this battle’s war.",
            "r": "That regiment was the Rough Riders. For 10 points, name this battle that made Theodore Roosevelt a national hero."
        },
        {
            "p": "In 2001, President Bill Clinton gave a posthumous Medal of Honor for this battle to a man who had been turned down soon after it was fought, possibly because he had angered the War Department by signing a letter urging that sick soldiers be brought home.",
            "r": "That man had led the Rough Riders up Kettle Hill. For 10 points, name this battle that made Theodore Roosevelt a hero."
        },
        {
            "p": "Days before this battle, General William Shafter’s Fifth Army Corps landed at Daiquirí [“dye-kee-REE”], and a cavalry division under the former Confederate general Joseph Wheeler won a skirmish at Las Guásimas [“GWAH-see-mahs”]. Shafter then ordered this attack on the heights guarding the city of Santiago.",
            "r": "For 10 points, name this July 1, 1898, battle in which Theodore Roosevelt led the Rough Riders up Kettle Hill."
        },
        {
            "p": "John J. Pershing, who later commanded American forces in World War I, fought in this battle as an officer of the 10th Cavalry. That regiment and the 9th Cavalry, Black units nicknamed Buffalo Soldiers, helped capture Kettle Hill during this battle.",
            "r": "For 10 points, name this 1898 battle near Santiago, Cuba, where Theodore Roosevelt led the Rough Riders."
        },
        {
            "p": "During this battle, one officer rode his horse, Little Texas, partway up a slope until a wire fence forced him to continue on foot. That officer’s regiment of cowboys, college athletes, and Native Americans had trained in San Antonio, Texas.",
            "r": "That regiment was the Rough Riders. For 10 points, name this battle of the Spanish-American War that made Theodore Roosevelt famous."
        },
        {
            "p": "Spanish General Arsenio Linares [“lee-NAH-rays”] was wounded in this battle, whose outnumbered Spanish defenders fired Mauser rifles that used smokeless powder. Many American volunteers carried older rifles, and their clouds of black-powder smoke gave away their positions.",
            "r": "For 10 points, name this July 1, 1898, battle in Cuba where the Rough Riders charged alongside the Buffalo Soldiers."
        },
        {
            "p": "The humorist Finley Peter Dunne had his character Mr. Dooley joke that one officer’s memoir of this battle’s campaign should have been titled _Alone in Cuba_, because the author wrote so much about himself.",
            "r": "That 1899 memoir was Theodore Roosevelt’s _The Rough Riders_. For 10 points, name this 1898 battle in which Roosevelt led a famous charge."
        },
        {
            "p": "On the same day as this battle, Henry Lawton’s division needed hours to capture the nearby village of El Caney [“kah-NAY”], where the Spanish general Joaquín Vara del Rey was killed. Lawton had been expected to take that village quickly and then join this attack on the heights east of Santiago.",
            "r": "For 10 points, name this July 1, 1898, battle in Cuba in which Theodore Roosevelt led the Rough Riders."
        },
        {
            "p": "One man honored for his actions in this battle and his oldest son, honored for leading troops ashore at Utah Beach on D-Day, are one of only two father-and-son pairs to receive the Medal of Honor. The other pair is Arthur and Douglas MacArthur.",
            "r": "The father had led the Rough Riders. For 10 points, name this 1898 battle in which Theodore Roosevelt charged up Kettle Hill."
        },
        {
            "p": "Glowing newspaper reports by the correspondent Richard Harding Davis made one volunteer officer the best-known American hero of this battle. That officer was elected governor of New York about four months later.",
            "r": "He had led the Rough Riders up Kettle Hill. For 10 points, name this 1898 battle in Cuba that made Theodore Roosevelt a national hero."
        },
        {
            "p": "Shortly before this battle, Colonel Leonard Wood was promoted to lead a brigade, leaving his second-in-command in charge of their regiment, officially the 1st U.S. Volunteer Cavalry. Most of that regiment fought on foot, because there had been no room on the ships for most of their horses.",
            "r": "That regiment was the Rough Riders. For 10 points, name this battle near Santiago, Cuba, where Theodore Roosevelt led a charge."
        },
        {
            "p": "Two days after this battle, Admiral Pascual Cervera’s Spanish fleet tried to escape from Santiago Harbor and was destroyed by American warships. This battle had given the Americans high ground overlooking that city, which surrendered on July 17.",
            "r": "For 10 points, name this July 1, 1898, battle of the Spanish-American War, where Theodore Roosevelt’s Rough Riders charged."
        }
    ],
    "clues": [
        {
            "id": "rough-riders",
            "tier": "giveaway",
            "t": "Theodore Roosevelt’s volunteer cavalry regiment, the Rough Riders, made a famous charge here",
            "k": ["rough riders", "theodore roosevelt", "roosevelt", "teddy"],
            "n": 0,
            "rabbit": "Theodore Roosevelt"
        },
        {
            "id": "spanish-american-war",
            "tier": "giveaway",
            "t": "An American victory over Spain in the Spanish-American War (1898)",
            "k": ["spanish-american war", "spanish american", "1898", "spain"],
            "n": 0,
            "rabbit": "Spanish-American War"
        },
        {
            "id": "santiago",
            "tier": "giveaway",
            "t": "Fought on July 1, 1898, on the heights just east of Santiago, Cuba",
            "k": ["santiago", "cuba", "july 1"],
            "n": 0
        },
        {
            "id": "kettle",
            "tier": "middle",
            "t": "The Rough Riders actually charged up nearby Kettle Hill first, then joined the attack on the main ridge",
            "k": ["kettle", "nearby", "main ridge"],
            "n": 0
        },
        {
            "id": "buffalo-soldiers",
            "tier": "middle",
            "t": "The 9th and 10th Cavalry, Black regiments nicknamed Buffalo Soldiers, fought beside the Rough Riders",
            "k": ["buffalo soldiers", "buffalo", "9th", "10th cavalry"],
            "n": 0,
            "rabbit": "Buffalo Soldiers"
        },
        {
            "id": "gatling",
            "tier": "middle",
            "t": "Lieutenant John Parker’s Gatling guns gave covering fire (“Gatling Gun” Parker)",
            "k": ["gatling", "parker", "covering fire"],
            "n": 0
        },
        {
            "id": "remington",
            "tier": "middle",
            "t": "Frederic Remington painted the charge: soldiers on foot behind a lone officer on horseback",
            "k": ["remington", "frederic remington", "painted"],
            "n": 0
        },
        {
            "id": "medal-2001",
            "tier": "middle",
            "t": "Roosevelt got the Medal of Honor for it in 2001 (from Bill Clinton), the only president ever to receive it",
            "k": ["medal of honor", "2001", "clinton"],
            "n": 0
        },
        {
            "id": "on-foot",
            "tier": "middle",
            "t": "The Rough Riders (officially the 1st U.S. Volunteer Cavalry) fought on foot; most of their horses stayed behind in Florida",
            "k": ["on foot", "florida", "volunteer cavalry", "horses"],
            "n": 0
        },
        {
            "id": "governor",
            "tier": "middle",
            "t": "Made Roosevelt a national hero; New York elected him governor about four months later",
            "k": ["governor", "new york", "hero"],
            "n": 0
        },
        {
            "id": "siege-santiago",
            "tier": "middle",
            "t": "Led to the siege of Santiago: Cervera’s fleet was destroyed trying to escape (July 3), and the city surrendered July 17",
            "k": ["siege", "cervera", "july 17", "surrendered"],
            "n": 0
        },
        {
            "id": "kettle-name",
            "tier": "power",
            "t": "Kettle Hill was named for a huge iron pot used in making sugar, found on its top",
            "k": ["iron pot", "sugar", "pot"],
            "n": 0
        },
        {
            "id": "balloon",
            "tier": "power",
            "t": "An Army Signal Corps observation balloon above the troops showed Spanish riflemen where to aim",
            "k": ["balloon", "signal corps", "observation"],
            "n": 0
        },
        {
            "id": "shafter",
            "tier": "power",
            "t": "General William Shafter’s Fifth Army Corps had landed at Daiquirí days earlier",
            "k": ["shafter", "fifth army corps", "daiquiri"],
            "n": 0
        },
        {
            "id": "wheeler",
            "tier": "power",
            "t": "Former Confederate general Joseph Wheeler’s cavalry won a skirmish at Las Guásimas a week earlier (June 24)",
            "k": ["wheeler", "las guasimas", "confederate"],
            "n": 0
        },
        {
            "id": "kent",
            "tier": "power",
            "t": "Jacob Kent’s infantry division stormed the main ridge, which was topped by a Spanish blockhouse",
            "k": ["jacob kent", "blockhouse", "infantry"],
            "n": 0
        },
        {
            "id": "linares",
            "tier": "power",
            "t": "Spanish general Arsenio Linares was wounded; his outnumbered men had Mauser rifles with smokeless powder",
            "k": ["linares", "mauser", "smokeless"],
            "n": 0
        },
        {
            "id": "pershing",
            "tier": "power",
            "t": "John J. Pershing, later the U.S. commander in World War I, fought here with the 10th Cavalry",
            "k": ["pershing", "world war i", "10th cavalry"],
            "n": 0,
            "rabbit": "John J. Pershing"
        },
        {
            "id": "little-texas",
            "tier": "power",
            "t": "Roosevelt rode his horse, Little Texas, up the slope until a wire fence stopped him",
            "k": ["little texas", "wire fence", "horse"],
            "n": 0
        },
        {
            "id": "leonard-wood",
            "tier": "power",
            "t": "Leonard Wood was promoted to lead a brigade, leaving Roosevelt in command; the regiment had trained in San Antonio",
            "k": ["leonard wood", "san antonio", "brigade"],
            "n": 0
        },
        {
            "id": "dooley",
            "tier": "power",
            "t": "Mr. Dooley (Finley Peter Dunne) joked that Roosevelt’s memoir _The Rough Riders_ (1899) should be called _Alone in Cuba_",
            "k": ["alone in cuba", "dooley", "finley peter dunne"],
            "n": 0
        },
        {
            "id": "el-caney",
            "tier": "power",
            "t": "Same day: Henry Lawton’s men took the village of El Caney, where Spain’s General Vara del Rey was killed",
            "k": ["el caney", "lawton", "vara del rey"],
            "n": 0
        },
        {
            "id": "father-son",
            "tier": "power",
            "t": "Roosevelt and his son Ted Jr. (Utah Beach, D-Day) are one of two father-son Medal of Honor pairs; the MacArthurs are the other",
            "k": ["utah beach", "macarthur", "father", "d-day"],
            "n": 0,
            "rabbit": "Douglas MacArthur"
        },
        {
            "id": "round-robin",
            "tier": "power",
            "t": "Roosevelt was turned down for the medal in 1898, possibly for angering the War Department with a letter urging that sick troops be sent home",
            "k": ["war department", "sick troops", "letter", "round robin"],
            "n": 0
        },
        {
            "id": "davis",
            "tier": "power",
            "t": "Correspondent Richard Harding Davis’s glowing reports made Roosevelt the battle’s best-known hero",
            "k": ["richard harding davis", "davis", "correspondent"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Kettle Hill or San Juan?",
        "body": "The Rough Riders’ famous charge was really up Kettle Hill, a smaller hill nearby, before they joined the attack on San Juan Hill itself, so Kettle Hill clues often appear in tossups on this battle. Two other fights get mixed in: Henry Lawton’s attack on El Caney the same day, and the naval Battle of Santiago de Cuba two days later, when Admiral Cervera’s fleet was destroyed. “Spanish-American War” names the whole war, not this battle.",
        "fix": "If the question says “this battle” and mentions July 1, 1898, the Rough Riders, the Buffalo Soldiers, or Gatling guns, answer San Juan Hill. Kettle Hill was part of the same attack (the Battle of the San Juan Heights), so it earns only a prompt; El Caney means Lawton’s village fight, and Cervera’s ships mean the July 3 sea battle.",
        "line": "Real answer line: Battle of <b><u>San Juan Hill</u></b> (or Battle of <b><u>San Juan Heights</u></b>; prompt on <u>Kettle Hill</u>)"
    },
    "tests": {
        "right": [
            "San Juan Hill",
            "Battle of San Juan Hill",
            "San Juan Heights",
            "San Juan Hil",
            "the charge up San Juan Hill"
        ],
        "prompt": [
            "Kettle Hill",
            "San Juan"
        ],
        "wrong": [
            "El Caney",
            "Spanish-American War",
            "Rough Riders",
            "Bunker Hill",
            "Battle of Santiago de Cuba",
            "Manila Bay"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
