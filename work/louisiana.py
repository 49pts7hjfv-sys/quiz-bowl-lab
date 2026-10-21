import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def T(p, r):
    return {"p": p, "r": r}


def C(cid, tier, t, k, rabbit=None):
    c = {"id": cid, "tier": tier, "t": t, "k": k, "n": 0}
    if rabbit:
        c["rabbit"] = rabbit
    return c


data = {
    "id": "louisiana",
    "name": "Louisiana",
    "mono": "LA",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Pelican State on the Gulf Coast · French, Spanish, Cajun, and Creole roots",
    "dates": "French claim 1682 · Statehood 1812",
    "briefing": "Louisiana is the only U.S. state divided into parishes instead of counties, and its laws on property and families still follow the civil-law tradition of France and Spain. Named for the French king Louis XIV, it passed from France to Spain and back again before the United States bought it in 1803. Cajuns, Creoles, Mardi Gras, jazz, and gumbo give it a culture unlike any other state’s, centered on the port city of New Orleans.",
    "answerHtml": "<b><u>Louisiana</u></b> (accept <u>La Louisiane</u>; do not accept “Louisiana Purchase,” “Louisiana Territory,” or “New Orleans”)",
    "accept": [
        "louisiana",
        "state of louisiana",
        "la louisiane",
        "louisiane",
        "louisiana state",
        "french louisiana",
        "spanish louisiana",
        "colony of louisiana",
        "louisiana colony"
    ],
    "prompt": [],
    "reject": [
        "louisiana purchase",
        "the louisiana purchase",
        "louisiana territory",
        "territory of louisiana",
        "territory of orleans",
        "orleans territory",
        "new orleans",
        "battle of new orleans",
        "orleans",
        "baton rouge",
        "lafayette",
        "shreveport",
        "acadiana",
        "acadia",
        "nova scotia",
        "mississippi",
        "mississippi river",
        "alabama",
        "arkansas",
        "texas",
        "florida",
        "georgia",
        "louisiana state university",
        "lsu",
        "st louis",
        "saint louis",
        "louis xiv",
        "louisville",
        "missouri",
        "hurricane katrina",
        "katrina",
        "mardi gras",
        "cajun",
        "cajuns",
        "creole",
        "plessy v ferguson"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Louisiana",
    "qb": {
        "q": "Louisiana",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        T("In April 1682, René-Robert Cavelier, Sieur de La Salle, reached the mouth of the Mississippi River and claimed its entire basin for France. Later, the brothers Iberville [“EE-ber-vil”] and Bienville [“BYEN-vil”] founded the first French settlements on this colony’s Gulf Coast.",
          "La Salle named the region for King Louis XIV. For 10 points, name this French colony whose name was later given to a U.S. state."),
        T("Louis Juchereau de St. Denis founded Natchitoches [“NAK-uh-tish”] in 1714, making it the oldest permanent European settlement in this state. Four years later, Jean-Baptiste Le Moyne de Bienville founded the city that became this state’s largest, naming it for the Duke of Orléans [“or-lay-AHN”].",
          "That city is New Orleans. For 10 points, name this state, whose capital is Baton Rouge."),
        T("After France secretly handed this colony to Spain in the 1762 Treaty of Fontainebleau [“FON-tin-bloh”], French colonists drove out the Spanish governor Antonio de Ulloa [“oo-YOH-uh”] in 1768. Alejandro O’Reilly crushed that revolt the next year, and a later Spanish governor, Bernardo de Gálvez [“GAHL-vess”], captured British forts during the American Revolution.",
          "For 10 points, name this colony, which later became the U.S. state whose largest city is New Orleans."),
        T("This state was admitted on April 30, 1812, exactly nine years after the signing of the treaty that sold its land to the United States, making it the first state carved out of that land. Before statehood, it had been called the Territory of Orleans.",
          "Its admission came just weeks before the War of 1812 began. For 10 points, name this 18th state, whose capital is Baton Rouge."),
        T("Elected bodies called police juries govern many of the 64 parishes in this state, which uses that word instead of “counties.” Its laws on property, contracts, and families are unusual too, following the civil-law tradition of France and Spain instead of English common law.",
          "For 10 points, name this Gulf Coast state, nicknamed the Pelican State, whose capital is Baton Rouge."),
        T("Part of Henry Wadsworth Longfellow’s poem _Evangeline_ takes place in this state, where thousands of French-speaking Acadians [“uh-KAY-dee-unz”] settled after Britain began forcing them out of Nova Scotia in 1755. Their part of this state is called Acadiana.",
          "Their descendants are called Cajuns. For 10 points, name this state whose largest city is New Orleans."),
        T("The Krewe of Comus held the first modern parade of its kind in this state’s largest city in 1857, and in 1872 the Rex organization chose that celebration’s official colors: purple, green, and gold. During the celebration, riders on floats throw beads to crowds, and bakeries sell king cakes.",
          "That celebration is Mardi Gras, or “Fat Tuesday.” For 10 points, name this state, home of New Orleans."),
        T("Enslaved and free people of African descent gathered on Sundays to drum and dance at Congo Square, in this state’s largest city. Cornet player Buddy Bolden and pianist Jelly Roll Morton later helped create a new kind of music there.",
          "That music was jazz. For 10 points, name this state whose largest city, New Orleans, was Louis Armstrong’s hometown."),
        T("The 34-story capitol of this state, the tallest in the nation, was built at the urging of a governor who was shot inside it in 1935, while serving as a U.S. senator. That man, nicknamed “the Kingfish,” promised “Every Man a King” and proposed a “Share Our Wealth” plan.",
          "That man was Huey Long. For 10 points, name this state, whose capital, Baton Rouge, is home to that building."),
        T("Less than a month after a far deadlier storm, Hurricane Rita struck this state’s western coast in September 2005. During that earlier hurricane, thousands of people sheltered in the Superdome, and the government’s slow response was widely criticized.",
          "That earlier storm, Hurricane Katrina, caused levee failures that flooded about 80 percent of New Orleans. For 10 points, name this state."),
        T("This state’s flag shows a mother pelican feeding her young above a ribbon with the motto “Union, Justice, Confidence.” That bird had vanished from this state’s coast by the early 1960s, so wildlife officials brought brown pelicans back from Florida.",
          "For 10 points, name this Gulf Coast state, called the Pelican State and the Bayou State."),
        T("The Lake Pontchartrain [“PON-chur-train”] Causeway, which runs about 24 miles across a lake in this state, is often called the world’s longest continuous bridge over water. This state also holds the Atchafalaya [“uh-chaf-uh-LIE-uh”] Basin, the largest river swamp in the United States.",
          "For 10 points, name this state, where the Mississippi River flows past Baton Rouge and New Orleans to the Gulf."),
        T("In January 1811, Charles Deslondes [“day-LOHND”] led hundreds of enslaved people in the German Coast Uprising, the largest slave revolt in U.S. history, along the Mississippi River upstream from this future state’s largest city. Militias and U.S. troops put down the revolt within days.",
          "The next year, this territory became a state. For 10 points, name this state, home of New Orleans and the Cajuns."),
        T("In 1960, six-year-old Ruby Bridges integrated William Frantz Elementary School in this state, walking past angry crowds with federal marshals, a scene Norman Rockwell later painted. Decades earlier, Homer Plessy had been arrested in this state for sitting in a railroad car reserved for white passengers.",
          "For 10 points, name this state, whose segregation law the Supreme Court upheld in _Plessy v. Ferguson_."),
        T("Tabasco sauce has been made since 1868 on Avery Island, which sits on top of a huge salt dome in this state. Accordion player Clifton Chenier, called the “King of Zydeco” [“ZY-duh-koh”], made this state’s Creole dance music famous.",
          "Gumbo and jambalaya are also famous dishes from this state. For 10 points, name this state, whose capital is Baton Rouge.")
    ],
    "clues": [
        C("new-orleans", "giveaway", "Its largest city is New Orleans; its capital is Baton Rouge (“red stick” in French)",
          ["new orleans", "baton rouge", "red stick"]),
        C("pelican", "giveaway", "Nicknamed the Pelican State (also the Bayou State)",
          ["pelican state", "pelican", "bayou state"]),
        C("mardi-gras", "giveaway", "Famous for Mardi Gras, jazz, and foods like gumbo and jambalaya",
          ["mardi gras", "jazz", "gumbo", "jambalaya"]),
        C("katrina", "giveaway", "Hurricane Katrina (2005) caused levee failures that flooded about 80 percent of New Orleans",
          ["katrina", "levee", "2005"], "Hurricane Katrina"),
        C("purchase", "middle", "Its land was part of the 1803 purchase from France, and it was the first state carved from that land",
          ["1803", "purchase", "france"], "Louisiana Purchase"),
        C("la-salle", "middle", "La Salle claimed the Mississippi basin for France in 1682 and named it for King Louis XIV",
          ["la salle", "louis xiv", "1682"]),
        C("bienville", "middle", "Brothers Iberville and Bienville founded the first French settlements (1699); Bienville founded New Orleans (1718), naming it for the Duke of Orléans",
          ["bienville", "iberville", "1718", "duke of orléans"]),
        C("statehood", "middle", "Became the 18th state on April 30, 1812, after being the Territory of Orleans",
          ["18th state", "1812", "territory of orleans"]),
        C("parishes", "middle", "Divided into 64 parishes instead of counties",
          ["64 parishes", "parishes", "counties"]),
        C("civil-law", "middle", "Its laws on property, contracts, and families follow the civil-law tradition of France and Spain, not English common law",
          ["civil-law", "common law", "civil law"]),
        C("cajuns", "middle", "Cajuns descend from French-speaking Acadians expelled from Nova Scotia by Britain beginning in 1755",
          ["cajuns", "acadians", "nova scotia"]),
        C("huey-long", "middle", "Governor and senator Huey Long (“Every Man a King,” “Share Our Wealth,” “the Kingfish”) was assassinated in 1935",
          ["huey long", "every man a king", "share our wealth", "kingfish"]),
        C("jazz", "middle", "Jazz was born in New Orleans; Louis Armstrong was born there in 1901",
          ["louis armstrong", "armstrong", "jazz"]),
        C("spain", "middle", "Spain ruled it from the 1760s until it secretly returned it to France in 1800 (Treaty of San Ildefonso)",
          ["spain", "san ildefonso", "1800"]),
        C("natchitoches", "power", "Natchitoches (1714) is its oldest permanent European settlement",
          ["natchitoches", "1714"]),
        C("fontainebleau", "power", "France secretly gave it to Spain in the Treaty of Fontainebleau (1762)",
          ["fontainebleau", "1762"]),
        C("ulloa", "power", "Colonists drove out Spanish governor Antonio de Ulloa (1768); later governor Bernardo de Gálvez captured British forts in the Revolution",
          ["ulloa", "gálvez", "1768"]),
        C("police-juries", "power", "Many of its parishes are governed by elected police juries",
          ["police juries", "police jury"]),
        C("evangeline", "power", "Longfellow’s _Evangeline_ is partly set here; the Cajun region is called Acadiana",
          ["evangeline", "longfellow", "acadiana"]),
        C("comus-rex", "power", "The Krewe of Comus held the first modern Mardi Gras parade (1857); Rex chose purple, green, and gold (1872)",
          ["comus", "rex", "purple, green, and gold"]),
        C("congo-square", "power", "People of African descent drummed and danced at Congo Square; Buddy Bolden and Jelly Roll Morton were early jazz musicians",
          ["congo square", "buddy bolden", "jelly roll morton"]),
        C("capitol", "power", "Huey Long had its 34-story capitol built, the nation’s tallest; he was shot there in 1935",
          ["capitol", "34-story", "tallest"]),
        C("flag", "power", "Its flag shows a pelican feeding her young with the motto “Union, Justice, Confidence”; brown pelicans were brought back from Florida",
          ["union, justice, confidence", "motto", "florida"]),
        C("causeway", "power", "The Lake Pontchartrain Causeway (about 24 miles) is often called the world’s longest continuous bridge over water",
          ["pontchartrain", "causeway"]),
        C("atchafalaya", "power", "The Atchafalaya Basin is the largest river swamp in the United States",
          ["atchafalaya", "swamp"]),
        C("german-coast", "power", "German Coast Uprising (1811), led by Charles Deslondes: the largest slave revolt in U.S. history",
          ["german coast", "deslondes", "1811"]),
        C("bridges", "power", "Ruby Bridges integrated William Frantz Elementary in New Orleans (1960); Homer Plessy was arrested here (1892)",
          ["ruby bridges", "plessy", "william frantz"], "Plessy v. Ferguson"),
        C("tabasco", "power", "Tabasco sauce comes from Avery Island; Clifton Chenier was the “King of Zydeco”",
          ["tabasco", "avery island", "zydeco"])
    ],
    "trap": {
        "title": "State, purchase, or city?",
        "body": "Three answer lines share the same clues. The Louisiana Purchase was the 1803 land deal with France, which covered all or part of 15 states; the state of Louisiana is only its southern corner. New Orleans, its largest city, gets its own tossups about jazz, Mardi Gras, and Hurricane Katrina. Answering “New Orleans” when the question says “this state” is wrong, and plain “Louisiana” only earns a prompt when the question wants the purchase.",
        "fix": "Listen for the noun: “this state” or “this colony” wants Louisiana; “this land deal” or “this purchase” wants the Louisiana Purchase; “this city” wants New Orleans. Parishes, Baton Rouge, Huey Long, and the Cajuns usually mean the state.",
        "line": "Real answer line: <b><u>Louisiana</u></b> (do not accept “Louisiana Purchase” or “New Orleans”)"
    },
    "tests": {
        "right": [
            "Louisiana",
            "La Louisiane",
            "Lousiana",
            "State of Louisiana",
            "Louisianna"
        ],
        "prompt": [],
        "wrong": [
            "Louisiana Purchase",
            "New Orleans",
            "Mississippi",
            "Louisiana Territory",
            "Baton Rouge",
            "Acadiana",
            "Hurricane Katrina"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
