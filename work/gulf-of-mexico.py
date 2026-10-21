import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "gulf-of-mexico",
    "name": "Gulf of Mexico",
    "mono": "GOM",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Ocean basin bordered by the U.S., Mexico, and Cuba · Where the Mississippi ends",
    "dates": "Mapped by Spain in 1519",
    "briefing": "The Gulf of Mexico is a huge ocean basin ringed by the U.S. Gulf Coast from Florida to Texas, by Mexico, and by Cuba. The Mississippi River empties into it, hurricanes like Katrina have roared across its warm waters, and in 2010 the _Deepwater Horizon_ oil spill fouled its coast. In January 2025, an executive order renamed it the “Gulf of America” for U.S. government use, while many other countries and organizations kept the old name.",
    "answerHtml": "<b><u>Gulf of Mexico</u></b> (or <b><u>Gulf of America</u></b>; prompt on <u>Gulf</u>; do not accept “Caribbean Sea” or “Gulf of California”)",
    "accept": [
        "gulf of mexico",
        "the gulf of mexico",
        "gulf of america",
        "the gulf of america",
        "golfo de mexico",
        "el golfo de mexico"
    ],
    "prompt": [
        "gulf",
        "the gulf",
        "gulf coast",
        "the gulf coast"
    ],
    "reject": [
        "caribbean sea",
        "caribbean",
        "gulf of california",
        "sea of cortez",
        "gulf of alaska",
        "gulf of maine",
        "gulf of st lawrence",
        "gulf of saint lawrence",
        "gulf of honduras",
        "gulf of panama",
        "persian gulf",
        "gulf of aden",
        "gulf of guinea",
        "gulf of thailand",
        "gulf of tonkin",
        "gulf stream",
        "loop current",
        "florida current",
        "bay of campeche",
        "campeche",
        "sargasso sea",
        "atlantic ocean",
        "atlantic",
        "pacific ocean",
        "mississippi river",
        "mississippi river delta",
        "rio grande",
        "chesapeake bay",
        "galveston bay",
        "tampa bay",
        "mobile bay",
        "hudson bay",
        "yucatan channel",
        "straits of florida",
        "florida straits",
        "chicxulub crater",
        "hurricane katrina",
        "deepwater horizon",
        "dead zone"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Gulf_of_Mexico",
    "qb": {
        "q": "Gulf of Mexico",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "About half of the Chicxulub [“CHEEK-shoo-loob”] crater lies beneath this body of water, with the rest buried under the Yucatán [“yoo-kuh-TAN”] Peninsula. Most scientists think the asteroid that made that crater about 66 million years ago helped wipe out the dinosaurs.",
            "r": "The Mississippi River flows into this body of water. For 10 points, name this arm of the Atlantic Ocean bordered by Texas, Florida, Mexico, and Cuba."
        },
        {
            "p": "Warm water enters this body of water through the Yucatán [“yoo-kuh-TAN”] Channel and forms the Loop Current, which swings north and then exits through the Straits of Florida. Hurricanes that pass over that warm current can quickly grow stronger.",
            "r": "That current then feeds the Gulf Stream. For 10 points, name this body of water bordered by Mexico, Cuba, and the southern United States."
        },
        {
            "p": "On April 20, 2010, an explosion on an oil-drilling rig above BP’s Macondo well killed 11 workers in this body of water. Oil gushed from the broken well for 87 days before it was capped, in the largest marine oil spill in U.S. history.",
            "r": "That rig was the _Deepwater Horizon_. For 10 points, name this body of water off the coasts of Louisiana, Texas, and Mexico."
        },
        {
            "p": "In 1979, the Mexican oil well Ixtoc I blew out in this body of water’s Bay of Campeche [“kahm-PAY-chay”] and spilled oil for about nine months. Mexico’s state oil company, Pemex, had drilled that well. The spill reached beaches as far away as Texas.",
            "r": "Thirty-one years later, the _Deepwater Horizon_ disaster spilled even more oil into it. For 10 points, name this body of water bordered by Mexico and the United States."
        },
        {
            "p": "Each summer, fertilizer carried down a huge river feeds blooms of algae off the coast of Louisiana, and bacteria that break down the dead algae use up the oxygen in the water. That leaves a “dead zone” in this body of water where little sea life can survive.",
            "r": "That river, the Mississippi, ends in a delta here. For 10 points, name this body of water that borders Texas and Florida."
        },
        {
            "p": "The Kemp’s ridley, the smallest and most endangered sea turtle, nests mainly on this body of water’s beaches in the Mexican state of Tamaulipas [“tah-mow-LEE-pahs”] and on Texas’s Padre Island. Padre Island is often called the longest barrier island in the world.",
            "r": "For 10 points, name this body of water south of Texas, which a 2025 executive order renamed for U.S. federal use."
        },
        {
            "p": "In 1519, the Spanish captain Alonso Álvarez de Pineda [“pih-NAY-duh”] sailed along this body of water’s northern coast and drew the first known map of it. That same year, Hernán Cortés landed on its western shore and founded Veracruz [“vair-uh-KROOZ”] before marching inland against the Aztecs.",
            "r": "For 10 points, name this body of water whose U.S. coast runs from Texas to Florida."
        },
        {
            "p": "Álvar Núñez Cabeza de Vaca [“kuh-BAY-zuh duh VAH-kuh”] survived a 1528 shipwreck on this body of water’s coast, probably near Galveston Island, and then spent eight years wandering across Texas and northern Mexico. He was one of only four survivors of the Narváez [“nar-VAH-ez”] expedition.",
            "r": "For 10 points, name this body of water into which the Mississippi River and the Rio Grande both empty."
        },
        {
            "p": "A 1900 hurricane that struck Galveston, Texas, from this body of water killed at least 6,000 people, making it the deadliest natural disaster in U.S. history. Afterward, Galveston built a huge seawall and raised the ground level of much of the city.",
            "r": "For 10 points, name this body of water off the coast of Texas, whose warm waters also fed Hurricane Katrina."
        },
        {
            "p": "In late August 2005, a hurricane strengthened over this body of water’s warm Loop Current before striking Louisiana and Mississippi. Levee failures after that storm flooded about 80 percent of New Orleans, and its storm surge wrecked towns on the Mississippi coast, such as Biloxi.",
            "r": "That storm was Hurricane Katrina. For 10 points, name this body of water into which the Mississippi River flows."
        },
        {
            "p": "The deepest point in this body of water, more than two miles down, is named for Charles Sigsbee, who measured its depths in the 1870s. Sigsbee later commanded the USS _Maine_ when it exploded in Havana Harbor in 1898.",
            "r": "Cuba lies at this body of water’s southeastern edge. For 10 points, name this body of water bordered by Florida, Texas, and Mexico."
        },
        {
            "p": "Dr. Samuel Mudd, who treated John Wilkes Booth’s broken leg, was imprisoned at Fort Jefferson, a brick fort in the Dry Tortugas [“tor-TOO-guhz”] at the edge of this body of water. Those small islands lie west of Key West, Florida.",
            "r": "For 10 points, name this body of water that lies between Florida, Texas, and Mexico’s Yucatán Peninsula."
        },
        {
            "p": "The Flower Garden Banks, a national marine sanctuary about 100 miles off the coasts of Texas and Louisiana, protects coral reefs growing on top of salt domes in this body of water. Many oil and gas platforms also stand in its northern waters.",
            "r": "For 10 points, name this body of water bordered by Texas, Louisiana, Mississippi, Alabama, and Florida."
        },
        {
            "p": "Spanish treasure fleets loaded silver at Veracruz [“vair-uh-KROOZ”], on this body of water’s western shore, then sailed to Havana before crossing the Atlantic to Spain. In 1914, U.S. forces occupied Veracruz for seven months during the Mexican Revolution.",
            "r": "For 10 points, name this body of water bordered by Mexico, Cuba, and five U.S. states."
        },
        {
            "p": "Blooms of the microscopic alga Karenia brevis cause “red tides” that kill fish along Florida’s western coast, near cities such as Tampa and Naples. Mobile Bay, Galveston Bay, and Tampa Bay are all inlets of this body of water.",
            "r": "In 2025, an executive order gave it a new name for U.S. federal use, but many other countries kept its old name. For 10 points, name this body of water."
        }
    ],
    "clues": [
        {
            "id": "borders",
            "tier": "giveaway",
            "t": "Bordered by five U.S. states from Texas to Florida, plus Mexico and Cuba",
            "k": ["texas", "florida", "cuba", "five u.s. states"],
            "n": 0
        },
        {
            "id": "mississippi",
            "tier": "giveaway",
            "t": "The Mississippi River empties into it through a delta below New Orleans",
            "k": ["mississippi river", "delta", "new orleans"],
            "n": 0,
            "rabbit": "Mississippi River"
        },
        {
            "id": "renamed-2025",
            "tier": "giveaway",
            "t": "A January 2025 executive order gave it a new name for U.S. federal use, ending “of America”; many other countries and groups kept the old name",
            "k": ["executive order", "2025", "federal use"],
            "n": 0
        },
        {
            "id": "deepwater",
            "tier": "giveaway",
            "t": "The _Deepwater Horizon_ oil spill (2010), the largest marine oil spill in U.S. history, happened here",
            "k": ["deepwater horizon", "oil spill", "2010"],
            "n": 0
        },
        {
            "id": "katrina",
            "tier": "giveaway",
            "t": "Hurricane Katrina (2005) crossed it before striking Louisiana and Mississippi",
            "k": ["katrina", "hurricane", "2005"],
            "n": 0,
            "rabbit": "Hurricane Katrina"
        },
        {
            "id": "chicxulub",
            "tier": "middle",
            "t": "Part of the Chicxulub crater lies under it; most scientists think that asteroid impact helped wipe out the dinosaurs",
            "k": ["chicxulub", "asteroid", "dinosaurs"],
            "n": 0,
            "rabbit": "Asteroids"
        },
        {
            "id": "loop-current",
            "tier": "middle",
            "t": "Its warm Loop Current enters through the Yucatán Channel and exits through the Straits of Florida as the Florida Current",
            "k": ["loop current", "yucatán channel", "straits of florida"],
            "n": 0,
            "rabbit": "Ocean currents"
        },
        {
            "id": "dead-zone",
            "tier": "middle",
            "t": "Fertilizer carried by the Mississippi feeds algae that leave a low-oxygen “dead zone” off Louisiana each summer",
            "k": ["dead zone", "fertilizer", "algae", "oxygen"],
            "n": 0
        },
        {
            "id": "deepwater-details",
            "tier": "middle",
            "t": "The _Deepwater Horizon_ explosion (April 20, 2010) killed 11 workers, and oil gushed from BP’s well for 87 days",
            "k": ["11 workers", "87 days", "explosion"],
            "n": 0
        },
        {
            "id": "galveston",
            "tier": "middle",
            "t": "The 1900 Galveston hurricane, the deadliest natural disaster in U.S. history, killed at least 6,000 people",
            "k": ["galveston", "1900", "6,000"],
            "n": 0
        },
        {
            "id": "rio-grande",
            "tier": "middle",
            "t": "The Rio Grande also empties into it, at the border of Texas and Mexico",
            "k": ["rio grande", "border"],
            "n": 0
        },
        {
            "id": "ports",
            "tier": "middle",
            "t": "Big ports on its shores include Houston, New Orleans, Tampa, and Mexico’s Veracruz",
            "k": ["houston", "tampa", "ports"],
            "n": 0
        },
        {
            "id": "cortes",
            "tier": "middle",
            "t": "Hernán Cortés landed on its shore and founded Veracruz in 1519",
            "k": ["cortés", "veracruz", "1519"],
            "n": 0
        },
        {
            "id": "katrina-levees",
            "tier": "middle",
            "t": "Levee failures after Katrina flooded about 80 percent of New Orleans",
            "k": ["levee", "80 percent"],
            "n": 0
        },
        {
            "id": "bays",
            "tier": "middle",
            "t": "Its inlets include Mobile Bay, Galveston Bay, Tampa Bay, and Mexico’s Bay of Campeche",
            "k": ["mobile bay", "galveston bay", "tampa bay", "bay of campeche"],
            "n": 0
        },
        {
            "id": "pineda",
            "tier": "power",
            "t": "Alonso Álvarez de Pineda drew the first known map of its coast in 1519",
            "k": ["pineda", "first known map", "1519"],
            "n": 0
        },
        {
            "id": "cabeza-de-vaca",
            "tier": "power",
            "t": "Cabeza de Vaca, one of four survivors of the Narváez expedition, was shipwrecked on its Texas coast in 1528",
            "k": ["cabeza de vaca", "narváez", "1528"],
            "n": 0
        },
        {
            "id": "ixtoc",
            "tier": "power",
            "t": "The Ixtoc I blowout (1979) in the Bay of Campeche spilled oil for about nine months",
            "k": ["ixtoc", "1979", "blowout"],
            "n": 0
        },
        {
            "id": "kemps-ridley",
            "tier": "power",
            "t": "The Kemp’s ridley, the most endangered sea turtle, nests mainly on its beaches in Tamaulipas, Mexico, and on Texas’s Padre Island",
            "k": ["kemp’s ridley", "kemps ridley", "padre island", "tamaulipas"],
            "n": 0
        },
        {
            "id": "sigsbee",
            "tier": "power",
            "t": "Its deepest point, the Sigsbee Deep, is named for Charles Sigsbee, later captain of the USS _Maine_",
            "k": ["sigsbee", "deepest point", "uss maine"],
            "n": 0
        },
        {
            "id": "dry-tortugas",
            "tier": "power",
            "t": "Dr. Samuel Mudd was imprisoned at Fort Jefferson in the Dry Tortugas, west of Key West",
            "k": ["dry tortugas", "fort jefferson", "samuel mudd"],
            "n": 0
        },
        {
            "id": "flower-garden",
            "tier": "power",
            "t": "The Flower Garden Banks sanctuary protects coral reefs on top of salt domes off Texas and Louisiana",
            "k": ["flower garden banks", "coral reefs", "salt domes"],
            "n": 0
        },
        {
            "id": "treasure-fleets",
            "tier": "power",
            "t": "Spanish treasure fleets loaded silver at Veracruz and sailed to Havana; U.S. forces occupied Veracruz in 1914",
            "k": ["treasure fleets", "silver", "havana", "1914"],
            "n": 0
        },
        {
            "id": "red-tide",
            "tier": "power",
            "t": "Red tides caused by the alga Karenia brevis kill fish along Florida’s western coast",
            "k": ["red tides", "karenia brevis", "karenia"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Gulf, sea, or stream?",
        "body": "The Caribbean Sea lies just to the southeast, beyond Cuba and the Yucatán Peninsula, and the Gulf of California (the Sea of Cortez) is on Mexico’s Pacific side, so both are wrong answers. The Gulf Stream is an ocean current, not a body of water, even though this gulf’s Loop Current feeds it. Since a January 2025 executive order, the U.S. government calls this body of water the Gulf of America, while many other countries and organizations kept the name Gulf of Mexico, and either name counts.",
        "fix": "The Mississippi delta, Texas, Louisiana, Veracruz, or _Deepwater Horizon_ point here; Jamaica, Puerto Rico, or the Lesser Antilles point to the Caribbean; Baja California points to the Gulf of California. Say “Gulf of Mexico” or “Gulf of America,” not just “the Gulf.”",
        "line": "Real answer line: <b><u>Gulf of Mexico</u></b> (or <b><u>Gulf of America</u></b>; prompt on <u>Gulf</u>; do not accept “Caribbean Sea” or “Gulf of California”)"
    },
    "tests": {
        "right": [
            "Gulf of Mexico",
            "Gulf of America",
            "the Gulf of Mexico",
            "Gulf of Mexcio",
            "Golfo de México"
        ],
        "prompt": [
            "Gulf",
            "the Gulf"
        ],
        "wrong": [
            "Caribbean Sea",
            "Gulf of California",
            "Gulf Stream",
            "Gulf of Alaska",
            "Persian Gulf",
            "Atlantic Ocean",
            "Sea of Cortez",
            "Bay of Campeche"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", data["id"])
