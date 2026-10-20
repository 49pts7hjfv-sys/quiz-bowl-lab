import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "cuba",
    "name": "Cuba",
    "mono": "CU",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Caribbean island 90 miles from Florida · Center of a 1962 nuclear standoff",
    "dates": "Spanish colony until 1898 · Republic since 1902",
    "briefing": "Cuba, the largest island in the Caribbean, lies only about 90 miles from Key West, Florida, and its history has been tangled up with that of the United States for more than 150 years. The explosion of the USS _Maine_ in Havana Harbor helped start the Spanish-American War in 1898, and after Fidel Castro’s revolution in 1959, Cuba became the center of the Cold War’s most dangerous standoff, the Cuban Missile Crisis of 1962.",
    "answerHtml": "<b><u>Cuba</u></b> (accept Republic of <u>Cuba</u>; do not accept “Spanish-American War,” “Cuban Missile Crisis,” or “Bay of Pigs”)",
    "accept": [
        "cuba",
        "republic of cuba",
        "the republic of cuba",
        "island of cuba"
    ],
    "prompt": [],
    "reject": [
        "havana",
        "puerto rico",
        "hispaniola",
        "haiti",
        "dominican republic",
        "jamaica",
        "bahamas",
        "florida",
        "key west",
        "philippines",
        "guam",
        "spain",
        "mexico",
        "panama",
        "grenada",
        "nicaragua",
        "venezuela",
        "soviet union",
        "ussr",
        "guantanamo bay",
        "guantanamo",
        "spanish american war",
        "cuban missile crisis",
        "missile crisis",
        "bay of pigs",
        "bay of pigs invasion",
        "cuban revolution",
        "mariel boatlift",
        "platt amendment",
        "teller amendment"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Cuba",
    "qb": {
        "q": "Cuba",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In the Ostend Manifesto of 1854, three American diplomats, including future president James Buchanan, urged the United States to offer Spain up to $120 million for this island and suggested taking it by force if Spain refused. Many Southern leaders hoped to add this island as a new slave state.",
            "r": "Christopher Columbus had landed there in 1492. For 10 points, name this Caribbean island whose capital is Havana."
        },
        {
            "p": "Carlos Manuel de Céspedes [“SEHS-peh-dess”] freed the enslaved workers on his sugar plantation in 1868 and began this island’s Ten Years’ War against Spain. During that war, Spanish forces captured the ship _Virginius_ and executed dozens of its crew and passengers, including Americans.",
            "r": "Thirty years later, the USS _Maine_ exploded in its main harbor. For 10 points, name this Caribbean island, home to the city of Havana."
        },
        {
            "p": "This island’s national hero wrote the poems of _Versos Sencillos_ (“Simple Verses”), some of which became the words of the song “Guantanamera.” That poet, José Martí [“mar-TEE”], organized a revolutionary party while living in New York and was killed in battle in 1895.",
            "r": "Three years later, the United States went to war with Spain over this island. For 10 points, name this island nation."
        },
        {
            "p": "Franklin Roosevelt’s Good Neighbor Policy led to a 1934 treaty that canceled most of an amendment this island had been forced to add to its constitution in 1901. That amendment, named for Senator Orville Platt, had let the United States intervene in this island’s affairs.",
            "r": "The U.S. kept its lease on a naval base at Guantánamo [“gwahn-TAH-nuh-moh”] Bay. For 10 points, name this island south of Florida."
        },
        {
            "p": "William Howard Taft briefly served as this island’s provisional governor in 1906, after Theodore Roosevelt sent troops back to restore order following a disputed election. In 1898, the Teller Amendment had promised that the United States would not annex this island.",
            "r": "That year, Roosevelt’s Rough Riders fought at San Juan Hill near its city of Santiago. For 10 points, name this island."
        },
        {
            "p": "On July 26, 1953, a young lawyer led a failed attack on the Moncada [“mohn-KAH-dah”] Barracks in this country, and at his trial he declared, “History will absolve me.” His movement, named for the date of that attack, later overthrew the dictator Fulgencio Batista [“bah-TEES-tah”].",
            "r": "That lawyer, Fidel Castro, took power in 1959. For 10 points, name this island nation that he ruled for nearly 50 years."
        },
        {
            "p": "In December 1956, 82 rebels sailed from Mexico to this island aboard the overcrowded yacht _Granma_, and the few survivors of their landing hid in the Sierra Maestra [“my-ES-truh”] mountains. An Argentine doctor, Che Guevara [“CHAY gheh-VAR-uh”], became one of their top commanders.",
            "r": "For 10 points, name this country where those rebels, led by Fidel Castro, took power in 1959."
        },
        {
            "p": "Most members of Brigade 2506 were captured within days of landing at Playa Girón [“hee-ROHN”] on this island’s southern coast in April 1961, and they were released the next year in exchange for food and medicine. That brigade of about 1,400 exiles had been trained by the CIA.",
            "r": "Their failed invasion is known as the Bay of Pigs. For 10 points, name this island nation led by Fidel Castro."
        },
        {
            "p": "On October 27, 1962, Major Rudolf Anderson was killed when his U-2 spy plane was shot down over this island during a tense standoff. To help end that standoff, the United States secretly agreed to remove its own Jupiter missiles from Turkey.",
            "r": "U-2 photos had revealed Soviet nuclear missile sites here. For 10 points, name this island at the center of a thirteen-day crisis between John F. Kennedy and Nikita Khrushchev [“KROOSH-chef”]."
        },
        {
            "p": "The Helms-Burton Act of 1996 tightened a U.S. trade embargo on this country after its air force shot down two small planes flown by the Miami exile group Brothers to the Rescue. That embargo had been made nearly total by John F. Kennedy in 1962.",
            "r": "Its leader at the time was Fidel Castro. For 10 points, name this island nation whose capital is Havana."
        },
        {
            "p": "In April 1980, more than 10,000 people crowded into the Peruvian embassy in this country’s capital, asking to leave. Soon after, its government opened the port of Mariel [“mah-ree-EL”], and about 125,000 people sailed to Florida in a boatlift.",
            "r": "Jimmy Carter was the U.S. president at the time. For 10 points, name this island nation about 90 miles south of Key West."
        },
        {
            "p": "In November 1999, fishermen rescued five-year-old Elián González [“el-YAHN gon-SAH-less”] at sea after the boat carrying him and his mother sank. After a long custody fight with relatives in Miami, he returned home with his father in June 2000.",
            "r": "For 10 points, name the island nation he came from, which was then led by Fidel Castro."
        },
        {
            "p": "Canada hosted secret talks and Pope Francis encouraged a deal that led the United States to restore diplomatic relations with this country in 2015. In March 2016, Barack Obama became the first sitting U.S. president to visit this country since Calvin Coolidge in 1928.",
            "r": "Its leader then was Raúl Castro, Fidel’s younger brother. For 10 points, name this island nation, whose capital is Havana."
        },
        {
            "p": "In 1881, a doctor from this island, Carlos Finlay, suggested that mosquitoes spread yellow fever, and Walter Reed’s team proved him right there in 1900. Reed’s work was backed by Leonard Wood, who ran the U.S. military government on this island from 1899 to 1902.",
            "r": "This island then became an independent republic. For 10 points, name this island, which Spain lost in the Spanish-American War."
        },
        {
            "p": "After the Soviet Union collapsed in 1991, this country lost most of its foreign aid and fell into an economic crisis its government called the “Special Period.” In 1994, thousands of its people, called balseros [“bahl-SAIR-ohs”], tried to reach Florida on homemade rafts.",
            "r": "Fidel Castro still ruled it at the time. For 10 points, name this communist island nation south of Florida."
        }
    ],
    "clues": [
        {
            "id": "havana",
            "tier": "giveaway",
            "t": "Largest island in the Caribbean, about 90 miles south of Key West, Florida; capital: Havana",
            "k": ["havana", "caribbean", "key west", "90 miles"],
            "n": 0
        },
        {
            "id": "fidel-castro",
            "tier": "giveaway",
            "t": "Fidel Castro took power in a revolution in 1959 and ruled for nearly 50 years",
            "k": ["fidel castro", "castro", "1959"],
            "n": 0
        },
        {
            "id": "missile-crisis",
            "tier": "giveaway",
            "t": "Soviet nuclear missiles there led to a thirteen-day standoff in October 1962 between John F. Kennedy and Nikita Khrushchev",
            "k": ["missiles", "thirteen-day", "october 1962", "khrushchev"],
            "n": 0,
            "rabbit": "John F. Kennedy"
        },
        {
            "id": "bay-of-pigs",
            "tier": "giveaway",
            "t": "Bay of Pigs invasion (April 1961): about 1,400 CIA-trained exiles landed and were defeated within days",
            "k": ["bay of pigs", "1961"],
            "n": 0
        },
        {
            "id": "maine",
            "tier": "giveaway",
            "t": "The USS _Maine_ exploded in Havana Harbor (February 1898), helping start the Spanish-American War",
            "k": ["maine", "spanish-american war", "1898"],
            "n": 0,
            "rabbit": "Spanish-American War"
        },
        {
            "id": "platt",
            "tier": "middle",
            "t": "The Platt Amendment (1901) let the U.S. intervene there and lease a naval base at Guantánamo Bay",
            "k": ["platt", "guantánamo", "guantanamo", "naval base"],
            "n": 0
        },
        {
            "id": "teller",
            "tier": "middle",
            "t": "The Teller Amendment (1898) promised the U.S. would not annex it; it became an independent republic in 1902",
            "k": ["teller", "annex", "1902"],
            "n": 0
        },
        {
            "id": "jose-marti",
            "tier": "middle",
            "t": "Poet José Martí, its national hero, was killed in battle in 1895 fighting for independence from Spain",
            "k": ["josé martí", "martí", "poet", "1895"],
            "n": 0
        },
        {
            "id": "batista",
            "tier": "middle",
            "t": "Castro’s 26th of July Movement overthrew the dictator Fulgencio Batista, who fled on January 1, 1959",
            "k": ["batista", "26th of july", "dictator"],
            "n": 0
        },
        {
            "id": "che",
            "tier": "middle",
            "t": "Argentine-born doctor Che Guevara was one of the revolution’s top commanders",
            "k": ["che guevara", "guevara", "argentine"],
            "n": 0
        },
        {
            "id": "embargo",
            "tier": "middle",
            "t": "U.S. trade embargo: begun in 1960 and made nearly total by John F. Kennedy in 1962",
            "k": ["embargo", "trade"],
            "n": 0
        },
        {
            "id": "mariel",
            "tier": "middle",
            "t": "Mariel boatlift (1980): about 125,000 people sailed to Florida while Jimmy Carter was president",
            "k": ["mariel", "boatlift", "125,000"],
            "n": 0
        },
        {
            "id": "elian",
            "tier": "middle",
            "t": "Elián González (1999–2000): a rescued boy returned to his father there after a custody fight with relatives in Miami",
            "k": ["elián gonzález", "elián", "custody", "miami"],
            "n": 0
        },
        {
            "id": "obama",
            "tier": "middle",
            "t": "Diplomatic relations restored in 2015; Barack Obama visited in 2016, the first sitting president to go since Calvin Coolidge (1928)",
            "k": ["obama", "2015", "coolidge", "1928"],
            "n": 0,
            "rabbit": "Barack Obama"
        },
        {
            "id": "columbus",
            "tier": "middle",
            "t": "Christopher Columbus landed there on his first voyage (1492); it stayed a Spanish colony until 1898",
            "k": ["columbus", "1492", "spanish colony"],
            "n": 0
        },
        {
            "id": "ostend",
            "tier": "power",
            "t": "Ostend Manifesto (1854): U.S. diplomats, including James Buchanan, urged offering Spain up to $120 million for it",
            "k": ["ostend", "buchanan", "$120 million"],
            "n": 0
        },
        {
            "id": "ten-years-war",
            "tier": "power",
            "t": "Ten Years’ War (1868–1878), begun by Carlos Manuel de Céspedes; in the _Virginius_ Affair (1873), Spain executed dozens aboard a captured ship, including Americans",
            "k": ["ten years’ war", "céspedes", "virginius"],
            "n": 0
        },
        {
            "id": "versos",
            "tier": "power",
            "t": "Martí wrote _Versos Sencillos_ (“Simple Verses”), the source of the song “Guantanamera,” and organized a revolutionary party in New York",
            "k": ["versos sencillos", "guantanamera", "simple verses"],
            "n": 0
        },
        {
            "id": "good-neighbor",
            "tier": "power",
            "t": "Franklin Roosevelt’s Good Neighbor Policy: a 1934 treaty canceled most of the Platt Amendment, but the U.S. kept Guantánamo Bay",
            "k": ["good neighbor", "1934"],
            "n": 0
        },
        {
            "id": "taft-1906",
            "tier": "power",
            "t": "After a disputed election, Theodore Roosevelt sent troops back in 1906, and William Howard Taft briefly served as provisional governor",
            "k": ["taft", "1906", "provisional governor"],
            "n": 0
        },
        {
            "id": "finlay",
            "tier": "power",
            "t": "Its doctor Carlos Finlay suggested mosquitoes spread yellow fever; Walter Reed proved it there (1900) under military governor Leonard Wood",
            "k": ["carlos finlay", "finlay", "walter reed", "yellow fever", "leonard wood"],
            "n": 0
        },
        {
            "id": "moncada",
            "tier": "power",
            "t": "Castro led a failed attack on the Moncada Barracks (July 26, 1953) and told his trial, “History will absolve me”",
            "k": ["moncada", "history will absolve me", "absolve"],
            "n": 0
        },
        {
            "id": "granma",
            "tier": "power",
            "t": "82 rebels sailed from Mexico on the yacht _Granma_ (1956); the survivors hid in the Sierra Maestra mountains",
            "k": ["granma", "sierra maestra", "yacht"],
            "n": 0
        },
        {
            "id": "brigade-2506",
            "tier": "power",
            "t": "Brigade 2506 landed at Playa Girón; the captured exiles were freed in 1962 in exchange for food and medicine",
            "k": ["brigade 2506", "playa girón", "medicine"],
            "n": 0
        },
        {
            "id": "rudolf-anderson",
            "tier": "power",
            "t": "Major Rudolf Anderson’s U-2 spy plane was shot down there on October 27, 1962",
            "k": ["rudolf anderson", "anderson", "u-2"],
            "n": 0
        },
        {
            "id": "helms-burton",
            "tier": "power",
            "t": "The Helms-Burton Act (1996) tightened the embargo after its air force shot down two Brothers to the Rescue planes",
            "k": ["helms-burton", "brothers to the rescue"],
            "n": 0
        },
        {
            "id": "peruvian-embassy",
            "tier": "power",
            "t": "Before the Mariel boatlift, more than 10,000 people crowded into the Peruvian embassy in Havana, asking to leave (April 1980)",
            "k": ["peruvian embassy", "peruvian", "10,000"],
            "n": 0
        },
        {
            "id": "special-period",
            "tier": "power",
            "t": "The “Special Period”: an economic crisis after the Soviet Union collapsed (1991); thousands of rafters called balseros fled in 1994",
            "k": ["special period", "balseros", "rafters"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Island, war, or crisis?",
        "body": "Many famous answer lines happen on this island, and real tossups often want the event instead. The Spanish-American War (1898), the Bay of Pigs invasion (1961), and the Cuban Missile Crisis (1962) share clues like Havana, Fidel Castro, and John F. Kennedy. Naming the island when the question wants one of those events is wrong, and so is naming an event when it asks for “this country.”",
        "fix": "Listen for the noun: “this island,” “this country,” or “this nation” wants Cuba, while “this war,” “this invasion,” or “this crisis” wants the event. Saying “Havana,” the capital city, is also wrong when the question asks for the country.",
        "line": "Real answer line: <b><u>Cuba</u></b> (accept Republic of <u>Cuba</u>; do not accept “Spanish-American War,” “Cuban Missile Crisis,” or “Bay of Pigs”)"
    },
    "tests": {
        "right": [
            "Cuba",
            "Republic of Cuba",
            "the island of Cuba",
            "Republic of Cubaa"
        ],
        "prompt": [],
        "wrong": [
            "Havana",
            "Puerto Rico",
            "Spanish-American War",
            "Cuban Missile Crisis",
            "Bay of Pigs",
            "Haiti",
            "Guantanamo Bay"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
