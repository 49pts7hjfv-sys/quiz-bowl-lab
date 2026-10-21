import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "arlington-national-cemetery",
    "name": "Arlington National Cemetery",
    "mono": "ANC",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Military cemetery on Robert E. Lee’s old estate · Tomb of the Unknown Soldier",
    "dates": "Established 1864",
    "briefing": "Arlington National Cemetery covers a Virginia hillside that once belonged to Robert E. Lee’s family, across the Potomac River from Washington, D.C. During the Civil War, Union Quartermaster General Montgomery Meigs began burying soldiers there in 1864. More than 400,000 people rest there, including President John F. Kennedy beneath an eternal flame, and soldiers of the Old Guard watch over the Tomb of the Unknown Soldier day and night.",
    "answerHtml": "<b><u>Arlington National Cemetery</u></b> (accept <u>Arlington Cemetery</u>; prompt on <u>Arlington</u> or <u>Arlington County</u>; do not accept “Arlington House”)",
    "accept": [
        "arlington national cemetery",
        "the arlington national cemetery",
        "arlington cemetery",
        "arlington national cemetery virginia"
    ],
    "prompt": [
        "arlington",
        "arlington county",
        "arlington virginia",
        "arlington va",
        "arlington county virginia",
        "arlington county va"
    ],
    "reject": [
        "arlington house",
        "custis lee mansion",
        "lee mansion",
        "robert e lee memorial",
        "tomb of the unknown soldier",
        "tomb of the unknown soldiers",
        "tomb of the unknowns",
        "tomb of the unknown",
        "marine corps war memorial",
        "iwo jima memorial",
        "gettysburg national cemetery",
        "soldiers national cemetery",
        "andersonville",
        "national memorial cemetery of the pacific",
        "arlington memorial bridge",
        "memorial bridge",
        "memorial amphitheater",
        "pentagon",
        "the pentagon",
        "mount vernon",
        "lincoln memorial",
        "edwin arlington robinson",
        "arlington texas",
        "arlington massachusetts"
    ],
    "mediaPending": True,
    "media": [],
    "wiki": "https://en.wikipedia.org/wiki/Arlington_National_Cemetery",
    "qb": {
        "q": "Arlington",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "George Washington Parke Custis, the grandson of Martha Washington, built a Greek Revival mansion on this site partly as a memorial to George Washington. In 1831, Custis’s daughter Mary married a young army officer in that house, and the couple made it their home for about thirty years.",
            "r": "That officer was Robert E. Lee. For 10 points, name this national cemetery created on Lee’s estate in Virginia."
        },
        {
            "p": "Private William Christman of the 67th Pennsylvania Infantry became the first soldier buried at this site, on May 13, 1864. About a month later, Secretary of War Edwin Stanton approved Quartermaster General Montgomery Meigs’s plan to turn the land into a military cemetery.",
            "r": "For 10 points, name this cemetery in Virginia, where the Tomb of the Unknown Soldier stands."
        },
        {
            "p": "Montgomery Meigs had graves dug close to a mansion on this site, even in its rose garden, reportedly so that the family who had lived there could never move back. Meigs, who was born in Georgia but stayed loyal to the Union, was later buried here himself.",
            "r": "That mansion had been the home of Robert E. Lee. For 10 points, name this military cemetery across the Potomac River from Washington, D.C."
        },
        {
            "p": "In the 1882 case _United States v. Lee_, the Supreme Court ruled that the federal government had taken this site illegally during the Civil War. The next year, the government paid 150,000 dollars to the family’s eldest son, who had brought the suit, so that it could keep the land.",
            "r": "That son’s father was Robert E. Lee. For 10 points, name this national cemetery on Lee’s former estate."
        },
        {
            "p": "In 1863, the government set up Freedman’s Village on this estate as a community for formerly enslaved people who had escaped to Union lines. Thousands of freedpeople, along with soldiers of the U.S. Colored Troops, were later buried here.",
            "r": "For 10 points, name this cemetery in Virginia, where President John F. Kennedy is buried under an eternal flame."
        },
        {
            "p": "In 1921, Sergeant Edward Younger walked among four identical caskets in a French city hall and placed white roses on one of them. The soldier in that casket was buried at this site on November 11, 1921, in a ceremony led by President Warren G. Harding.",
            "r": "That soldier lies in the Tomb of the Unknown Soldier. For 10 points, name this cemetery across the Potomac River from Washington, D.C."
        },
        {
            "p": "In 1998, DNA tests identified the remains in one crypt at this site as those of Air Force pilot Michael Blassie, who had been shot down in Vietnam, and that crypt has been left empty ever since.",
            "r": "Unknowns from World War II and Korea had been placed at the Tomb of the Unknown Soldier in 1958. For 10 points, name this national cemetery in Virginia."
        },
        {
            "p": "Soldiers from the 3rd U.S. Infantry Regiment, nicknamed “The Old Guard,” keep watch over a memorial at this site, as they have every hour of every day since 1937. Each sentinel takes 21 steps and then pauses for 21 seconds, recalling a 21-gun salute.",
            "r": "That memorial is the Tomb of the Unknown Soldier. For 10 points, name this cemetery on Robert E. Lee’s former estate."
        },
        {
            "p": "The marble for a famous tomb at this site, finished in 1932, came from the same Colorado quarry that supplied the marble for the Lincoln Memorial. One side of that tomb reads “Here rests in honored glory an American soldier known but to God.”",
            "r": "That tomb holds the Unknown Soldier from World War I. For 10 points, name this national cemetery in Virginia."
        },
        {
            "p": "Only two U.S. presidents are buried at this site. One of them, William Howard Taft, is the only person to have served as both president and Chief Justice of the United States.",
            "r": "The other, John F. Kennedy, lies beneath an eternal flame that his widow lit at his 1963 funeral. For 10 points, name this cemetery."
        },
        {
            "p": "In 1909, the remains of Pierre L’Enfant [“lahn-FAHN”] were moved to this site and reburied on a hillside overlooking the capital city he had planned. L’Enfant had been fired in 1792 and died poor.",
            "r": "For 10 points, name this cemetery in Virginia, home of the Tomb of the Unknown Soldier and the grave of John F. Kennedy."
        },
        {
            "p": "Abraham Lincoln’s son Robert Todd Lincoln is buried at this site rather than with his parents in Springfield, Illinois. Boxing champion Joe Louis and civil rights leader Medgar Evers, both World War II veterans, are also buried here.",
            "r": "For 10 points, name this military cemetery where John F. Kennedy is buried under an eternal flame."
        },
        {
            "p": "A bridge opened in 1932 across the Potomac River links the Lincoln Memorial to this site, symbolizing the North and South reunited after the Civil War. The Women in Military Service for America Memorial, dedicated in 1997, stands at this site’s ceremonial entrance.",
            "r": "For 10 points, name this cemetery on Robert E. Lee’s former estate, home of the Tomb of the Unknown Soldier."
        },
        {
            "p": "Memorials at this site honor the crews lost aboard the space shuttles _Challenger_ in 1986 and _Columbia_ in 2003. The mast of the battleship USS _Maine_, which sank in Havana harbor in 1898, also stands here.",
            "r": "For 10 points, name this national cemetery in Virginia, where the Tomb of the Unknown Soldier stands."
        },
        {
            "p": "Unlike most national cemeteries, which are run by the Department of Veterans Affairs, this one is run by the U.S. Army. More than 400,000 people are buried at this site, and military funerals are held here almost every weekday.",
            "r": "For 10 points, name this cemetery across the Potomac River from Washington, D.C., where John F. Kennedy is buried."
        }
    ],
    "clues": [
        {
            "id": "lee-estate",
            "tier": "giveaway",
            "t": "Built on the Virginia estate of Robert E. Lee’s family, across the Potomac River from Washington, D.C.",
            "k": ["robert e. lee", "potomac", "estate"],
            "n": 0,
            "rabbit": "Robert E. Lee"
        },
        {
            "id": "unknown-soldier",
            "tier": "giveaway",
            "t": "Home of the Tomb of the Unknown Soldier, guarded every hour of every day",
            "k": ["tomb of the unknown soldier", "unknown soldier", "guarded"],
            "n": 0
        },
        {
            "id": "jfk",
            "tier": "giveaway",
            "t": "President John F. Kennedy is buried there under an eternal flame",
            "k": ["john f. kennedy", "kennedy", "eternal flame"],
            "n": 0,
            "rabbit": "John F. Kennedy"
        },
        {
            "id": "meigs",
            "tier": "middle",
            "t": "Union Quartermaster General Montgomery Meigs began burying soldiers there in 1864",
            "k": ["montgomery meigs", "meigs", "1864", "quartermaster"],
            "n": 0
        },
        {
            "id": "military",
            "tier": "middle",
            "t": "The best-known U.S. military cemetery: more than 400,000 people are buried there, most of them veterans and their families",
            "k": ["military cemetery", "400,000", "veterans"],
            "n": 0
        },
        {
            "id": "old-guard",
            "tier": "middle",
            "t": "Tomb guards come from the 3rd U.S. Infantry Regiment, “The Old Guard”",
            "k": ["old guard", "3rd u.s. infantry", "infantry"],
            "n": 0
        },
        {
            "id": "armistice-day",
            "tier": "middle",
            "t": "An unidentified World War I soldier was buried there on Armistice Day, November 11, 1921",
            "k": ["armistice day", "1921", "world war i"],
            "n": 0
        },
        {
            "id": "21-steps",
            "tier": "middle",
            "t": "Each tomb guard takes 21 steps and pauses 21 seconds, recalling a 21-gun salute",
            "k": ["21 steps", "21 seconds", "21-gun salute"],
            "n": 0
        },
        {
            "id": "known-but-to-god",
            "tier": "middle",
            "t": "The tomb reads “Here rests in honored glory an American soldier known but to God”",
            "k": ["known but to god", "honored glory"],
            "n": 0
        },
        {
            "id": "taft",
            "tier": "middle",
            "t": "Only two presidents are buried there: William Howard Taft and John F. Kennedy",
            "k": ["william howard taft", "taft", "two presidents"],
            "n": 0
        },
        {
            "id": "lenfant",
            "tier": "middle",
            "t": "Pierre L’Enfant, who planned Washington, D.C., was reburied there in 1909, on a hillside overlooking the city",
            "k": ["l’enfant", "1909", "reburied"],
            "n": 0,
            "rabbit": "Washington, D.C."
        },
        {
            "id": "custis",
            "tier": "power",
            "t": "George Washington Parke Custis, Martha Washington’s grandson, built its mansion; his daughter Mary married Robert E. Lee there in 1831",
            "k": ["george washington parke custis", "custis", "martha washington", "1831"],
            "n": 0
        },
        {
            "id": "rose-garden",
            "tier": "power",
            "t": "Meigs had graves dug near the mansion, even in its rose garden, reportedly so the Lees could never return",
            "k": ["rose garden", "never return", "graves"],
            "n": 0
        },
        {
            "id": "us-v-lee",
            "tier": "power",
            "t": "_United States v. Lee_ (1882): the Supreme Court ruled the land was taken illegally; the government paid Lee’s son $150,000 (1883)",
            "k": ["united states v. lee", "1882", "150,000", "supreme court"],
            "n": 0
        },
        {
            "id": "christman",
            "tier": "power",
            "t": "Private William Christman of Pennsylvania was the first soldier buried there (May 13, 1864)",
            "k": ["william christman", "christman", "may 13"],
            "n": 0
        },
        {
            "id": "freedmans-village",
            "tier": "power",
            "t": "Freedman’s Village, a community for formerly enslaved people, was set up on the estate in 1863",
            "k": ["freedman’s village", "freedman", "formerly enslaved", "1863"],
            "n": 0
        },
        {
            "id": "younger",
            "tier": "power",
            "t": "Sergeant Edward Younger chose the World War I Unknown in France by placing white roses on one of four caskets; Warren G. Harding led the burial",
            "k": ["edward younger", "younger", "white roses", "harding"],
            "n": 0
        },
        {
            "id": "blassie",
            "tier": "power",
            "t": "The Vietnam Unknown was identified by DNA in 1998 as Air Force pilot Michael Blassie; that crypt stays empty",
            "k": ["michael blassie", "blassie", "dna", "1998"],
            "n": 0
        },
        {
            "id": "since-1937",
            "tier": "power",
            "t": "Sentinels have guarded the tomb around the clock since 1937; Unknowns from World War II and Korea were added in 1958",
            "k": ["1937", "around the clock", "1958"],
            "n": 0
        },
        {
            "id": "memorial-bridge",
            "tier": "power",
            "t": "A bridge across the Potomac (1932) links it to the Lincoln Memorial, a symbol of North and South reunited",
            "k": ["lincoln memorial", "1932", "bridge"],
            "n": 0,
            "rabbit": "Lincoln Memorial"
        },
        {
            "id": "notable-graves",
            "tier": "power",
            "t": "Also buried there: Robert Todd Lincoln, boxer Joe Louis, civil rights leader Medgar Evers, and Justice Thurgood Marshall",
            "k": ["robert todd lincoln", "joe louis", "medgar evers", "thurgood marshall"],
            "n": 0
        },
        {
            "id": "shuttles",
            "tier": "power",
            "t": "Memorials honor the crews of the space shuttles _Challenger_ (1986) and _Columbia_ (2003) and the battleship USS _Maine_ (1898)",
            "k": ["challenger", "columbia", "space shuttles", "maine"],
            "n": 0
        },
        {
            "id": "army-run",
            "tier": "power",
            "t": "Run by the U.S. Army, while most national cemeteries are run by the Department of Veterans Affairs",
            "k": ["u.s. army", "veterans affairs", "army"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Cemetery, house, or county?",
        "body": "Several answers share the name Arlington. Arlington House is the Lee family’s mansion on the cemetery grounds, Arlington County is the Virginia county around it (home of the Pentagon), and the Tomb of the Unknown Soldier is one memorial inside the cemetery. On this answer line, plain “Arlington” or “Arlington County” earns only a prompt, and “Arlington House” or the Tomb alone is wrong.",
        "fix": "When a tossup says “this cemetery,” answer “Arlington National Cemetery.” If it asks for “this mansion” (Custis, Lee, Greek Revival columns), say Arlington House; if it asks for “this memorial” guarded by the Old Guard, say the Tomb of the Unknown Soldier.",
        "line": "Real answer line: <b><u>Arlington National Cemetery</u></b> (accept <u>Arlington Cemetery</u>; prompt on <u>Arlington</u> or <u>Arlington County</u>; do not accept “Arlington House”)"
    },
    "tests": {
        "right": [
            "Arlington National Cemetery",
            "Arlington Cemetery",
            "Arlington National Cemetary",
            "Arlingtn National Cemetery"
        ],
        "prompt": [
            "Arlington",
            "Arlington County",
            "Arlington, Virginia"
        ],
        "wrong": [
            "Arlington House",
            "Tomb of the Unknown Soldier",
            "Gettysburg National Cemetery",
            "Pentagon",
            "Mount Vernon",
            "Edwin Arlington Robinson"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", data["id"])
