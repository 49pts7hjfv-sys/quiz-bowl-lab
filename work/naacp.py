import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "naacp",
    "name": "NAACP",
    "mono": "NAA",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Civil rights organization founded in 1909 · Fought segregation in court",
    "dates": "Founded 1909",
    "briefing": "The National Association for the Advancement of Colored People was founded in 1909, on the 100th anniversary of Abraham Lincoln’s birth, by Black and white reformers including W. E. B. Du Bois, Ida B. Wells, and Mary White Ovington. Du Bois edited its magazine, _The Crisis_, and its lawyers, led by Thurgood Marshall, won _Brown v. Board of Education_ in 1954. Rosa Parks was secretary of its Montgomery branch, and Medgar Evers led its work in Mississippi.",
    "answerHtml": "<b><u>NAACP</u></b> (or <b><u>National Association for the Advancement of Colored People</u></b>)",
    "accept": [
        "naacp",
        "n a a c p",
        "n double a c p",
        "the naacp",
        "national association for the advancement of colored people",
        "national association for advancement of colored people"
    ],
    "prompt": [],
    "reject": [
        "sclc",
        "southern christian leadership conference",
        "sncc",
        "student nonviolent coordinating committee",
        "core",
        "congress of racial equality",
        "urban league",
        "national urban league",
        "niagara movement",
        "unia",
        "universal negro improvement association",
        "aclu",
        "american civil liberties union",
        "national association of colored women",
        "nacw",
        "black panther party",
        "black panthers",
        "nation of islam",
        "montgomery improvement association",
        "nafta"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/NAACP",
    "qb": {
        "q": "NAACP",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "After a deadly race riot in Springfield, Illinois, in 1908, William English Walling wrote an article called “The Race War in the North,” asking who would come to the aid of Black Americans. Mary White Ovington answered by meeting with Walling to plan this group.",
            "r": "It was founded the next year. For 10 points, name this civil rights organization that published _The Crisis_."
        },
        {
            "p": "Oswald Garrison Villard, a grandson of the abolitionist William Lloyd Garrison, wrote “the Call” that led to the founding of this group in New York. Villard owned the _New York Evening Post_ newspaper.",
            "r": "The Call came out on Lincoln’s 100th birthday, in 1909. For 10 points, name this civil rights organization whose lawyers later won _Brown v. Board of Education_."
        },
        {
            "p": "In 1921, this group’s monthly magazine, then edited for literature by Jessie Redmon Fauset [“FAW-set”], published Langston Hughes’s poem “The Negro Speaks of Rivers,” which Hughes had written as a teenager while riding a train to Mexico.",
            "r": "W. E. B. Du Bois edited that magazine, _The Crisis_, for more than twenty years. For 10 points, name this civil rights group founded in 1909."
        },
        {
            "p": "The biologist Ernest Everett Just received the first of this group’s top awards in 1915, a medal named for its leader Joel Spingarn. Later winners of that Spingarn Medal include Jackie Robinson and Martin Luther King Jr.",
            "r": "For 10 points, name this civil rights group, founded in 1909, whose lawyer Thurgood Marshall argued _Brown v. Board of Education_."
        },
        {
            "p": "This group’s first president, the Boston lawyer Moorfield Storey, had once been Senator Charles Sumner’s secretary. In 1917, Storey won _Buchanan v. Warley_, in which the Supreme Court struck down a Louisville law that kept Black and white families on separate blocks.",
            "r": "For 10 points, name this civil rights organization that W. E. B. Du Bois helped found in 1909."
        },
        {
            "p": "In July 1917, this group led thousands of people in a Silent Parade down New York’s Fifth Avenue to protest racial violence, including a deadly riot in East St. Louis. James Weldon Johnson, who helped organize that march, became this group’s first Black executive secretary in 1920.",
            "r": "For 10 points, name this organization whose magazine, _The Crisis_, was edited by W. E. B. Du Bois."
        },
        {
            "p": "In the 1920s and 1930s, this group flew a flag reading “A Man Was Lynched Yesterday” outside its New York office. Walter White, who later led the group, secretly investigated dozens of lynchings in the South.",
            "r": "It also pushed the Dyer anti-lynching bill, which passed the House in 1922. For 10 points, name this civil rights organization founded in 1909."
        },
        {
            "p": "Charles Hamilton Houston planned this group’s legal campaign against segregated schools, starting with lawsuits against all-white law and graduate schools in the 1930s. In 1940, his former student founded this group’s Legal Defense Fund.",
            "r": "That student, Thurgood Marshall, later won _Brown v. Board of Education_. For 10 points, name this civil rights group."
        },
        {
            "p": "In _Smith v. Allwright_, this group’s lawyers persuaded the Supreme Court in 1944 to strike down the all-white primary elections that Texas Democrats used to keep Black citizens from voting.",
            "r": "Thurgood Marshall argued that case. For 10 points, name this civil rights organization whose Legal Defense Fund later won _Brown v. Board of Education_."
        },
        {
            "p": "This group’s first field secretary in Mississippi investigated the 1955 murder of Emmett Till and organized boycotts before he was assassinated outside his home in Jackson in 1963. His widow, Myrlie Evers-Williams, chaired this group’s national board from 1995 to 1998.",
            "r": "That field secretary was Medgar Evers. For 10 points, name this civil rights organization founded in 1909."
        },
        {
            "p": "In 1956, Alabama banned this group from operating in the state and demanded its list of members, but in 1958 the Supreme Court ruled that the group did not have to hand over the names.",
            "r": "Rosa Parks had been secretary of its Montgomery branch. For 10 points, name this civil rights group."
        },
        {
            "p": "Daisy Bates, who led this group’s branches in Arkansas, advised the nine Black students who integrated Little Rock Central High School in 1957. In the 1940s, Ella Baker had traveled across the South as this group’s director of branches.",
            "r": "Its magazine was _The Crisis_. For 10 points, name this civil rights organization founded in 1909."
        },
        {
            "p": "In 1915, this group organized protests against D. W. Griffith’s film _The Birth of a Nation_, which glorified the Ku Klux Klan. That same year, it filed a brief in _Guinn v. United States_, in which the Supreme Court struck down Oklahoma’s “grandfather clause” for voting.",
            "r": "W. E. B. Du Bois was one of its founders. For 10 points, name this civil rights group founded six years earlier."
        },
        {
            "p": "At the 1963 March on Washington, this group’s leader, Roy Wilkins, announced that one of its founders had died in Ghana the night before. That founder had edited this group’s magazine for more than twenty years.",
            "r": "That founder was W. E. B. Du Bois. For 10 points, name this civil rights organization founded in 1909."
        },
        {
            "p": "The journalist Ida B. Wells, who exposed lynching in her pamphlet _Southern Horrors_, and the educator Mary Church Terrell were among the signers of the call to found this group. Each year, this group honors performers of color with its Image Awards.",
            "r": "For 10 points, name this civil rights organization whose lawyers won _Brown v. Board of Education_."
        }
    ],
    "clues": [
        {
            "id": "founded-1909",
            "tier": "giveaway",
            "t": "Civil rights organization founded in 1909, on the 100th anniversary of Abraham Lincoln’s birth",
            "k": ["1909", "civil rights", "lincoln"],
            "n": 0,
            "rabbit": "Abraham Lincoln"
        },
        {
            "id": "du-bois-crisis",
            "tier": "giveaway",
            "t": "W. E. B. Du Bois helped found it and edited its magazine, _The Crisis_, from 1910 to 1934",
            "k": ["du bois", "the crisis", "crisis"],
            "n": 0
        },
        {
            "id": "marshall-brown",
            "tier": "giveaway",
            "t": "Its lawyers, led by Thurgood Marshall, won _Brown v. Board of Education_ (1954)",
            "k": ["thurgood marshall", "marshall", "brown"],
            "n": 0,
            "rabbit": "Thurgood Marshall"
        },
        {
            "id": "rosa-parks",
            "tier": "giveaway",
            "t": "Rosa Parks was secretary of its Montgomery, Alabama, branch",
            "k": ["rosa parks", "secretary", "montgomery"],
            "n": 0,
            "rabbit": "Rosa Parks"
        },
        {
            "id": "founders",
            "tier": "middle",
            "t": "Founders included Ida B. Wells, Mary Church Terrell, Mary White Ovington, Oswald Garrison Villard, and William English Walling",
            "k": ["ovington", "terrell", "villard", "walling"],
            "n": 0
        },
        {
            "id": "springfield",
            "tier": "middle",
            "t": "A 1908 race riot in Springfield, Illinois, Lincoln’s hometown, led to its founding",
            "k": ["springfield", "race riot", "1908"],
            "n": 0
        },
        {
            "id": "spingarn",
            "tier": "middle",
            "t": "Gives the Spingarn Medal, first awarded in 1915 to the biologist Ernest Everett Just",
            "k": ["spingarn", "ernest everett just", "1915"],
            "n": 0
        },
        {
            "id": "ldf",
            "tier": "middle",
            "t": "Charles Hamilton Houston planned its legal fight against school segregation; Thurgood Marshall founded its Legal Defense Fund in 1940",
            "k": ["legal defense fund", "charles hamilton houston", "houston", "1940"],
            "n": 0
        },
        {
            "id": "evers",
            "tier": "middle",
            "t": "Medgar Evers, its first field secretary in Mississippi, was assassinated in Jackson in 1963",
            "k": ["medgar evers", "field secretary", "jackson"],
            "n": 0
        },
        {
            "id": "birth-of-a-nation",
            "tier": "middle",
            "t": "Protested D. W. Griffith’s film _The Birth of a Nation_ (1915), which glorified the Ku Klux Klan",
            "k": ["birth of a nation", "griffith", "ku klux klan"],
            "n": 0,
            "rabbit": "Ku Klux Klan"
        },
        {
            "id": "niagara",
            "tier": "middle",
            "t": "Many members of the Niagara Movement, founded in 1905 by Du Bois and William Monroe Trotter, joined it",
            "k": ["niagara movement", "trotter", "1905"],
            "n": 0
        },
        {
            "id": "image-awards",
            "tier": "middle",
            "t": "Honors performers of color each year with its Image Awards",
            "k": ["image awards"],
            "n": 0
        },
        {
            "id": "walling-article",
            "tier": "power",
            "t": "William English Walling’s article “The Race War in the North” (1908) asked who would come to the aid of Black Americans",
            "k": ["race war in the north", "walling"],
            "n": 0
        },
        {
            "id": "villard-call",
            "tier": "power",
            "t": "Oswald Garrison Villard, a grandson of William Lloyd Garrison, wrote “the Call,” released February 12, 1909",
            "k": ["villard", "the call", "william lloyd garrison"],
            "n": 0,
            "rabbit": "William Lloyd Garrison"
        },
        {
            "id": "storey",
            "tier": "power",
            "t": "First president: Boston lawyer Moorfield Storey, once Charles Sumner’s secretary; he won _Buchanan v. Warley_ (1917) against segregated city blocks",
            "k": ["moorfield storey", "storey", "buchanan", "sumner"],
            "n": 0
        },
        {
            "id": "guinn",
            "tier": "power",
            "t": "Filed a brief in _Guinn v. United States_ (1915), which struck down Oklahoma’s “grandfather clause” for voting",
            "k": ["grandfather clause", "guinn", "oklahoma"],
            "n": 0
        },
        {
            "id": "silent-parade",
            "tier": "power",
            "t": "Silent Parade (July 1917): thousands marched down New York’s Fifth Avenue to protest racial violence, including the East St. Louis riot",
            "k": ["silent parade", "fifth avenue", "1917"],
            "n": 0
        },
        {
            "id": "johnson",
            "tier": "power",
            "t": "James Weldon Johnson, author of “Lift Every Voice and Sing,” became its first Black executive secretary (1920)",
            "k": ["james weldon johnson", "lift every voice", "executive secretary"],
            "n": 0
        },
        {
            "id": "lynching-flag",
            "tier": "power",
            "t": "Flew a flag reading “A Man Was Lynched Yesterday”; Walter White investigated lynchings, and it pushed the Dyer anti-lynching bill (1922)",
            "k": ["lynched yesterday", "walter white", "dyer"],
            "n": 0
        },
        {
            "id": "hughes",
            "tier": "power",
            "t": "_The Crisis_ first published Langston Hughes’s “The Negro Speaks of Rivers” (1921); Jessie Redmon Fauset was its literary editor",
            "k": ["langston hughes", "negro speaks of rivers", "fauset"],
            "n": 0
        },
        {
            "id": "smith-allwright",
            "tier": "power",
            "t": "_Smith v. Allwright_ (1944): Thurgood Marshall won the case that ended Texas’s all-white primary elections",
            "k": ["white primary", "allwright", "texas"],
            "n": 0
        },
        {
            "id": "alabama-ban",
            "tier": "power",
            "t": "Alabama banned it in 1956 and demanded its membership lists; the Supreme Court sided with the group in 1958",
            "k": ["membership lists", "banned", "1958"],
            "n": 0
        },
        {
            "id": "bates-baker",
            "tier": "power",
            "t": "Daisy Bates, its Arkansas leader, advised the Little Rock Nine (1957); Ella Baker was its director of branches in the 1940s",
            "k": ["daisy bates", "little rock nine", "ella baker"],
            "n": 0
        },
        {
            "id": "myrlie",
            "tier": "power",
            "t": "Myrlie Evers-Williams, Medgar Evers’s widow, chaired its national board from 1995 to 1998",
            "k": ["myrlie evers-williams", "widow", "1995"],
            "n": 0
        },
        {
            "id": "wilkins",
            "tier": "power",
            "t": "Roy Wilkins, its leader from 1955 to 1977, announced Du Bois’s death at the 1963 March on Washington",
            "k": ["roy wilkins", "march on washington", "wilkins"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Which civil rights group?",
        "body": "Several civil rights organizations show up as answers. The NAACP (1909) fought mostly through lawsuits and lobbying. The Southern Christian Leadership Conference (SCLC, 1957) was Martin Luther King Jr.’s group of Black ministers, the Student Nonviolent Coordinating Committee (SNCC, 1960) grew out of the sit-ins, and the Congress of Racial Equality (CORE, 1942) organized the 1961 Freedom Rides. The Niagara Movement (1905) came just before the NAACP, and many of its members joined it.",
        "fix": "NAACP clues: 1909, Lincoln’s 100th birthday, W. E. B. Du Bois and _The Crisis_, the Spingarn Medal, Thurgood Marshall and _Brown v. Board_, Medgar Evers, and Rosa Parks as a branch secretary. Saying “NAACP” is enough; you don’t need the full name.",
        "line": "Real answer line: <b><u>NAACP</u></b> (or <b><u>National Association for the Advancement of Colored People</u></b>)"
    },
    "tests": {
        "right": [
            "NAACP",
            "N.A.A.C.P.",
            "National Association for the Advancement of Colored People",
            "naacpp",
            "the NAACP",
            "National Assocation for the Advancement of Colored People"
        ],
        "prompt": [],
        "wrong": [
            "SCLC",
            "SNCC",
            "CORE",
            "Urban League",
            "Niagara Movement",
            "Congress of Racial Equality",
            "NAFTA",
            "Universal Negro Improvement Association"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
