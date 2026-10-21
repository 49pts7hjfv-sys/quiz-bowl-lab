import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "birmingham-alabama",
    "name": "Birmingham, Alabama",
    "mono": "BHM",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Iron and steel city in Alabama · Site of the 1963 civil rights campaign",
    "dates": "Founded 1871",
    "briefing": "Birmingham, Alabama, was founded in 1871 where two railroads crossed near deposits of iron ore, coal, and limestone, and it grew so fast into a steel-making center that it was nicknamed the “Magic City.” In 1963, it became the scene of a major civil rights campaign, when police turned fire hoses and dogs on young marchers and Martin Luther King Jr. wrote a letter from its jail. That September, a bomb planted by Ku Klux Klan members at the 16th Street Baptist Church killed four Black girls.",
    "answerHtml": "<b><u>Birmingham</u></b>, Alabama (do not accept “Alabama” or “Montgomery”)",
    "accept": [
        "birmingham",
        "birmingham alabama",
        "birmingham al",
        "birmingham ala",
        "city of birmingham"
    ],
    "prompt": [],
    "reject": [
        "montgomery",
        "montgomery alabama",
        "selma",
        "selma alabama",
        "tuscaloosa",
        "huntsville",
        "mobile",
        "anniston",
        "atlanta",
        "memphis",
        "jackson mississippi",
        "little rock",
        "nashville",
        "greensboro",
        "albany georgia",
        "birmingham england",
        "birmingham uk",
        "birmingham united kingdom",
        "pittsburgh",
        "st louis",
        "state of alabama",
        "16th street baptist church",
        "sixteenth street baptist church",
        "kelly ingram park",
        "bethel baptist church",
        "dexter avenue baptist church"
    ],
    "mediaPending": True,
    "media": [],
    "wiki": "https://en.wikipedia.org/wiki/Birmingham,_Alabama",
    "qb": {
        "q": "Birmingham",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Giuseppe Moretti designed a cast-iron statue of the Roman god of the forge for the 1904 World’s Fair in St. Louis to show off this city’s iron industry. That statue of Vulcan, the largest cast-iron statue in the world, stands on Red Mountain overlooking this city.",
            "r": "For 10 points, name this Alabama city where Martin Luther King Jr. wrote a famous letter from jail in 1963."
        },
        {
            "p": "Sloss Furnaces, which made iron from 1882 until 1971, has become a museum in this city. In 1907, U.S. Steel took over the Tennessee Coal, Iron and Railroad Company, the biggest steelmaker in this city.",
            "r": "This city grew up around coal, iron ore, and limestone mined nearby. For 10 points, name this Alabama city nicknamed the “Pittsburgh of the South.”"
        },
        {
            "p": "This city was founded in 1871 at the spot where two railroads crossed, and it was named after an industrial city in England. It grew so quickly that people nicknamed it the “Magic City.”",
            "r": "For 10 points, name this steel-making center in Alabama where civil rights marchers faced fire hoses and police dogs in 1963."
        },
        {
            "p": "On Christmas night in 1956, a bomb badly damaged the parsonage of Bethel Baptist Church in this city, but its pastor survived. That pastor, Fred Shuttlesworth, had founded the Alabama Christian Movement for Human Rights after the state banned the NAACP.",
            "r": "In 1963, Shuttlesworth invited Martin Luther King Jr. to lead protests here. For 10 points, name this Alabama city."
        },
        {
            "p": "On Mother’s Day in 1961, a mob attacked a busload of Freedom Riders at this city’s Trailways station while the city’s police stayed away. Public Safety Commissioner Bull Connor claimed few officers were on duty because it was Mother’s Day.",
            "r": "For 10 points, name this Alabama city where Connor later used fire hoses on civil rights marchers in 1963."
        },
        {
            "p": "Organizers called this city’s 1963 protest campaign Project C, with the C standing for “confrontation.” On Good Friday that year, police arrested a minister here for leading a march that a court order had banned.",
            "r": "That minister, Martin Luther King Jr., then wrote a famous letter from this city’s jail. For 10 points, name this Alabama city."
        },
        {
            "p": "Eight white clergymen published a statement called “A Call for Unity,” urging Black residents of this city to stop protesting and to wait for the courts. A jailed minister answered them in a letter declaring that “injustice anywhere is a threat to justice everywhere.”",
            "r": "For 10 points, name this Alabama city whose jail gave its name to Martin Luther King Jr.’s 1963 letter."
        },
        {
            "p": "James Bevel helped organize a “Children’s Crusade” in this city, in which thousands of students skipped school to march in May 1963. So many young marchers were arrested that the city’s jails quickly filled.",
            "r": "Public Safety Commissioner Bull Connor then turned fire hoses and police dogs on the marchers. For 10 points, name this Alabama city."
        },
        {
            "p": "Kelly Ingram Park, where young protesters gathered in 1963, is part of a national monument in this city that Barack Obama created in 2017. Across the street stand the city’s Civil Rights Institute, opened in 1992, and a famous Baptist church.",
            "r": "A bomb planted by Ku Klux Klan members killed four girls at that church in September 1963. For 10 points, name this Alabama city."
        },
        {
            "p": "Businessman A. G. Gaston’s motel served as headquarters for a 1963 civil rights campaign in this city, and it was bombed that May, a day after the campaign’s leaders announced a deal to desegregate stores. The deal promised to open lunch counters and fitting rooms to Black customers.",
            "r": "For 10 points, name this Alabama city where Martin Luther King Jr. wrote a letter from jail in 1963."
        },
        {
            "p": "In 2013, Addie Mae Collins, Cynthia Wesley, Carole Robertson, and Denise McNair were honored with the Congressional Gold Medal, fifty years after their deaths in this city. Three of them were fourteen years old, and Denise McNair was eleven.",
            "r": "They were killed when a bomb exploded at the 16th Street Baptist Church. For 10 points, name this Alabama city."
        },
        {
            "p": "In 1977, Robert Chambliss was convicted of a 1963 bombing in this city, and Thomas Blanton Jr. and Bobby Frank Cherry were convicted of the same crime decades later. All three men were members of the Ku Klux Klan.",
            "r": "Their bomb killed four girls at the 16th Street Baptist Church. For 10 points, name this Alabama city."
        },
        {
            "p": "Dudley Randall’s poem about a tragedy in this city tells of a mother who sends her daughter to church because she thinks it is safer than a freedom march. John Coltrane recorded the jazz piece “Alabama” in response to that same 1963 event.",
            "r": "Spike Lee’s documentary _4 Little Girls_ is about it too. For 10 points, name this Alabama city where a church bombing killed four girls."
        },
        {
            "p": "In a Christopher Paul Curtis novel, the young narrator Kenny and his family drive from Flint, Michigan, to visit his grandmother in this city in 1963. His parents plan to leave his troublemaking older brother, Byron, there with their strict grandmother.",
            "r": "While they are there, Kenny’s little sister Joetta is nearly caught in a church bombing. For 10 points, name this Alabama city named in the novel’s title."
        },
        {
            "p": "Willie Mays began his professional career with this city’s Black Barons, who played at Rickwood Field, the oldest professional ballpark in the United States. Condoleezza Rice was born here, and Richard Arrington Jr. became its first Black mayor in 1979.",
            "r": "For 10 points, name this Alabama city, home of the Vulcan statue and the 16th Street Baptist Church."
        }
    ],
    "clues": [
        {
            "id": "letter-jail",
            "tier": "giveaway",
            "t": "Martin Luther King Jr. was jailed here in April 1963 and wrote a famous letter answering eight white clergymen",
            "k": ["clergymen", "letter", "jail", "april 1963"],
            "n": 0,
            "rabbit": "Martin Luther King Jr."
        },
        {
            "id": "church-bombing",
            "tier": "giveaway",
            "t": "September 15, 1963: Ku Klux Klan members bombed the 16th Street Baptist Church, killing four Black girls",
            "k": ["16th street baptist church", "four black girls", "bombed", "1963"],
            "n": 0,
            "rabbit": "Ku Klux Klan"
        },
        {
            "id": "bull-connor",
            "tier": "giveaway",
            "t": "Public Safety Commissioner Bull Connor turned fire hoses and police dogs on young marchers in May 1963",
            "k": ["bull connor", "fire hoses", "police dogs", "connor"],
            "n": 0
        },
        {
            "id": "steel",
            "tier": "giveaway",
            "t": "Alabama’s great iron and steel city, called the “Pittsburgh of the South”",
            "k": ["pittsburgh of the south", "steel", "iron"],
            "n": 0
        },
        {
            "id": "founded-1871",
            "tier": "middle",
            "t": "Founded in 1871 where two railroads crossed and named for England’s industrial city; it grew so fast it was called the “Magic City”",
            "k": ["magic city", "1871", "railroads"],
            "n": 0
        },
        {
            "id": "vulcan",
            "tier": "middle",
            "t": "A giant cast-iron statue of Vulcan, Roman god of the forge, stands on Red Mountain above the city",
            "k": ["vulcan", "red mountain", "forge"],
            "n": 0
        },
        {
            "id": "raw-materials",
            "tier": "middle",
            "t": "Iron ore, coal, and limestone, the raw materials for making iron and steel, were all found nearby",
            "k": ["iron ore", "limestone", "coal"],
            "n": 0
        },
        {
            "id": "childrens-crusade",
            "tier": "middle",
            "t": "The Children’s Crusade (May 1963): thousands of students marched, organized by James Bevel",
            "k": ["children’s crusade", "james bevel", "bevel", "students"],
            "n": 0
        },
        {
            "id": "shuttlesworth",
            "tier": "middle",
            "t": "Pastor Fred Shuttlesworth led the city’s civil rights movement and invited King and the SCLC in 1963; its airport is named for him",
            "k": ["fred shuttlesworth", "shuttlesworth", "airport"],
            "n": 0
        },
        {
            "id": "kelly-ingram",
            "tier": "middle",
            "t": "Young marchers gathered in Kelly Ingram Park, across from the 16th Street Baptist Church",
            "k": ["kelly ingram park", "kelly ingram", "park"],
            "n": 0
        },
        {
            "id": "bombingham",
            "tier": "middle",
            "t": "Nicknamed “Bombingham” for the many bombings of Black homes and churches in the 1950s and 1960s",
            "k": ["bombingham", "bombings"],
            "n": 0
        },
        {
            "id": "project-c",
            "tier": "middle",
            "t": "The 1963 campaign, run with the Southern Christian Leadership Conference (SCLC), was called Project C, for “confrontation”",
            "k": ["project c", "confrontation", "southern christian leadership"],
            "n": 0
        },
        {
            "id": "watsons",
            "tier": "middle",
            "t": "Christopher Paul Curtis’s novel about the Watson family’s 1963 trip from Flint, Michigan, is set partly here",
            "k": ["christopher paul curtis", "watson", "flint"],
            "n": 0
        },
        {
            "id": "sloss",
            "tier": "power",
            "t": "Sloss Furnaces, which made iron from 1882 to 1971, has become a museum and National Historic Landmark",
            "k": ["sloss furnaces", "sloss", "1971"],
            "n": 0
        },
        {
            "id": "moretti",
            "tier": "power",
            "t": "Giuseppe Moretti’s Vulcan, the world’s largest cast-iron statue, was made for the 1904 World’s Fair in St. Louis",
            "k": ["giuseppe moretti", "moretti", "1904", "st. louis"],
            "n": 0
        },
        {
            "id": "us-steel",
            "tier": "power",
            "t": "U.S. Steel took over the Tennessee Coal, Iron and Railroad Company, the city’s biggest steelmaker, in 1907",
            "k": ["tennessee coal", "u.s. steel", "1907"],
            "n": 0
        },
        {
            "id": "christmas-bombing",
            "tier": "power",
            "t": "Shuttlesworth founded the Alabama Christian Movement for Human Rights (1956) after the state banned the NAACP; his parsonage was bombed that Christmas night",
            "k": ["alabama christian movement", "naacp", "christmas", "parsonage"],
            "n": 0
        },
        {
            "id": "freedom-riders",
            "tier": "power",
            "t": "On Mother’s Day 1961, a mob attacked Freedom Riders at the Trailways bus station while police stayed away",
            "k": ["freedom riders", "mother’s day", "trailways", "1961"],
            "n": 0
        },
        {
            "id": "gaston-motel",
            "tier": "power",
            "t": "The A. G. Gaston Motel was the 1963 campaign’s headquarters; it was bombed in May, a day after a deal to desegregate stores",
            "k": ["gaston motel", "gaston", "headquarters"],
            "n": 0
        },
        {
            "id": "good-friday",
            "tier": "power",
            "t": "King was arrested on Good Friday, April 12, 1963, for leading a march banned by a court order",
            "k": ["good friday", "april 12", "court order"],
            "n": 0
        },
        {
            "id": "call-for-unity",
            "tier": "power",
            "t": "King’s letter answered “A Call for Unity” by eight white clergymen: “Injustice anywhere is a threat to justice everywhere”",
            "k": ["call for unity", "injustice anywhere", "clergymen"],
            "n": 0
        },
        {
            "id": "chambliss",
            "tier": "power",
            "t": "Klansmen Robert Chambliss (1977), Thomas Blanton Jr. (2001), and Bobby Frank Cherry (2002) were convicted of the church bombing",
            "k": ["chambliss", "bobby frank cherry", "blanton", "cherry"],
            "n": 0
        },
        {
            "id": "four-girls",
            "tier": "power",
            "t": "The girls killed were Addie Mae Collins, Cynthia Wesley, Carole Robertson, and Denise McNair; they received the Congressional Gold Medal in 2013",
            "k": ["addie mae collins", "denise mcnair", "congressional gold medal", "2013"],
            "n": 0
        },
        {
            "id": "art-response",
            "tier": "power",
            "t": "Responses to the bombing include John Coltrane’s “Alabama” (1963), a ballad by poet Dudley Randall, and Spike Lee’s documentary _4 Little Girls_ (1997)",
            "k": ["dudley randall", "coltrane", "4 little girls", "spike lee"],
            "n": 0
        },
        {
            "id": "civil-rights-institute",
            "tier": "power",
            "t": "Its Civil Rights Institute opened across from the church in 1992; Barack Obama made the district a national monument in 2017",
            "k": ["civil rights institute", "national monument", "1992", "2017"],
            "n": 0
        },
        {
            "id": "rickwood",
            "tier": "power",
            "t": "Willie Mays began his pro career with its Black Barons at Rickwood Field (1910), the oldest professional ballpark in the U.S.",
            "k": ["rickwood field", "black barons", "willie mays"],
            "n": 0
        },
        {
            "id": "rice-arrington",
            "tier": "power",
            "t": "Birthplace of Condoleezza Rice (1954); Richard Arrington Jr. became its first Black mayor in 1979",
            "k": ["condoleezza rice", "arrington", "1979"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Which Alabama city?",
        "body": "Alabama civil rights clues come from several cities. The Montgomery Bus Boycott (1955–1956) and Rosa Parks belong to Montgomery, the state capital; the 1965 voting rights march began in Selma; and George Wallace’s “stand in the schoolhouse door” happened in Tuscaloosa. Birmingham owns the 1963 campaign: King’s letter from jail, the Children’s Crusade, Bull Connor’s fire hoses, and the 16th Street Baptist Church bombing.",
        "fix": "Listen for 1963, Bull Connor, Fred Shuttlesworth, the Children’s Crusade, and the 16th Street Baptist Church: that is Birmingham. Steel, the “Magic City,” and the Vulcan statue also mean Birmingham. Saying only “Alabama” is wrong when the question asks for “this city.”",
        "line": "Real answer line: <b><u>Birmingham</u></b>, Alabama (do not accept “Alabama” or “Montgomery”)"
    },
    "tests": {
        "right": [
            "Birmingham",
            "Birmingham, Alabama",
            "Birmingham, AL",
            "Birmingam",
            "the city of Birmingham"
        ],
        "prompt": [],
        "wrong": [
            "Alabama",
            "Montgomery",
            "Montgomery, Alabama",
            "Selma",
            "Tuscaloosa",
            "Birmingham, England",
            "Atlanta",
            "16th Street Baptist Church"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", data["id"])
