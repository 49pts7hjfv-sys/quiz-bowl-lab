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
    "id": "crispus-attucks",
    "name": "Crispus Attucks",
    "mono": "CRA",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "First to die in the Boston Massacre · Of African and Native American descent",
    "dates": "c. 1723–1770",
    "briefing": "On the night of March 5, 1770, a tall sailor named Crispus Attucks stood with an angry crowd facing British soldiers on King Street in Boston. When the soldiers fired, he was the first of five colonists to die. A man of African and Native American descent who had probably escaped slavery twenty years earlier, he was later honored by abolitionists as the first martyr of the American Revolution.",
    "answerHtml": "Crispus <b><u>Attucks</u></b> (prompt on <u>Crispus</u>)",
    "accept": [
        "crispus attucks",
        "attucks"
    ],
    "prompt": [
        "crispus"
    ],
    "reject": [
        "boston massacre",
        "samuel adams",
        "sam adams",
        "john adams",
        "paul revere",
        "thomas preston",
        "christopher seider",
        "christopher snider",
        "samuel gray",
        "james caldwell",
        "samuel maverick",
        "patrick carr",
        "peter salem",
        "salem poor",
        "prince hall",
        "phillis wheatley",
        "james armistead",
        "william cooper nell"
    ],
    "tests": {
        "right": [
            "Crispus Attucks",
            "Attucks",
            "Crispus Atucks",
            "crispus attuks"
        ],
        "prompt": [
            "Crispus"
        ],
        "wrong": [
            "Boston Massacre",
            "Paul Revere",
            "Peter Salem",
            "Samuel Adams",
            "Thomas Preston"
        ]
    },
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Crispus_Attucks",
    "qb": {
        "q": "Crispus Attucks",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        T("In 1750, William Brown of Framingham placed an advertisement in the _Boston Gazette_ offering a reward for an enslaved man who had run away, describing him as 6 feet 2 inches tall. Historians believe that runaway was this man, who spent much of the next twenty years working as a sailor.",
          "For 10 points, name this man of African and Native American descent, the first person killed in the Boston Massacre."),
        T("A Boston newspaper reported that this man had been born in Framingham but had lately come from New Providence in the Bahamas, and that he was in town waiting for a ship to North Carolina. He made his living as a sailor.",
          "For 10 points, name this man who was the first to die when British soldiers fired into a Boston crowd in 1770."),
        T("In his closing argument at the soldiers’ trial, John Adams said that this man had led the crowd that attacked them and was chiefly to blame for the bloodshed. Six of the eight soldiers were found not guilty, and two were convicted of manslaughter.",
          "For 10 points, name this sailor, the first of five colonists killed in the Boston Massacre."),
        T("John Boyle O’Reilly’s poem for the 1888 unveiling of a monument on Boston Common calls this man “the first to defy, and the first to die.” That monument honors this man and the other four victims of the same night.",
          "For 10 points, name this man of African and Native American ancestry who died in the Boston Massacre."),
        T("In 1998, the U.S. Mint issued a silver dollar honoring Black patriots of the Revolutionary War, with this man’s portrait on the front. Abolitionists of the 1850s pointed to this man to argue that Black Americans had fought for liberty since the Revolution began.",
          "He had been killed on King Street in 1770. For 10 points, name this first victim of the Boston Massacre."),
        T("Oscar Robertson led an Indianapolis high school named for this man to Indiana state basketball championships in 1955 and 1956. That school had opened in 1927 as a segregated school for Black students.",
          "Its namesake was a sailor of African and Native American descent. For 10 points, name this first person killed in the Boston Massacre."),
        T("In 1858, the Black abolitionist and historian William Cooper Nell began organizing yearly celebrations in Boston honoring this man on the anniversary of his death. Nell had earlier written about this man in a book about Black patriots of the American Revolution.",
          "He died on March 5, 1770. For 10 points, name this man, the first person killed in the Boston Massacre."),
        T("This man and the sailor James Caldwell were not from Boston, so their bodies lay in Faneuil [“FAN-yul”] Hall before a shared funeral for the victims. Thousands of mourners joined the procession through the town.",
          "He was buried with other victims in the Granary Burying Ground. For 10 points, name this sailor killed on King Street in 1770."),
        T("Below the picture in Paul Revere’s famous engraving, this man is named among the “unhappy Sufferers,” along with Samuel Gray, Samuel Maverick, James Caldwell, and Patrick Carr. Unlike Carr, who died days later, this man was killed on the spot.",
          "For 10 points, name this man, the first person to die in the Boston Massacre."),
        T("This man joined a crowd that gathered around Private Hugh White, a lone sentry outside the Custom House, after White struck a wigmaker’s apprentice with his musket. Captain Thomas Preston then marched seven soldiers to the sentry’s aid.",
          "When the soldiers fired, this man was the first to fall. For 10 points, name this man of African and Native American descent."),
        T("Samuel Maverick, a 17-year-old apprentice, and Samuel Gray, a rope maker, were also killed in the event in which this man died. Patrick Carr, an Irish immigrant who was shot the same night, died nine days later.",
          "This man was the first to die. For 10 points, name this sailor of African and Native American descent killed in the Boston Massacre."),
        T("This man was killed by soldiers of the 29th Regiment, one of the units sent to Boston in 1768 to protect customs officials collecting the Townshend duties. Colonists mocked those soldiers as “lobsterbacks” because of their red coats.",
          "Captain Thomas Preston commanded the soldiers who fired. For 10 points, name this man, the first person killed in the Boston Massacre."),
        T("A circle of cobblestones near the Old State House marks the site of the shooting in which this man was killed, on what was then called King Street. He was part of a crowd that threw snowballs, ice, and insults at British soldiers that night.",
          "For 10 points, name this man of African and Native American descent who was the first person killed in the Boston Massacre."),
        T("On the day of this man’s funeral, most of Boston’s shops closed, and church bells tolled in the town and in neighboring towns such as Charlestown and Roxbury. He was laid to rest in one vault with three other victims.",
          "He was one of five colonists killed when British soldiers fired on a crowd. For 10 points, name this man, the first to die in that 1770 event."),
        T("Three days before this man died, soldiers and rope makers brawled at John Gray’s ropewalk, a fight that began when a worker insulted a soldier who was looking for part-time work. Bad feelings between soldiers and workers spread across the town.",
          "This man died when soldiers fired on a crowd on King Street. For 10 points, name this sailor, the first person killed in the Boston Massacre.")
    ],
    "clues": [
        C("first-killed", "giveaway",
          "The first person killed in the Boston Massacre, when British soldiers fired into a crowd in Boston on March 5, 1770",
          ["boston massacre", "first person killed", "march 5, 1770", "1770"], "Boston Massacre"),
        C("ancestry", "giveaway",
          "A sailor of African and Native American descent (his Native ancestry is often given as Wampanoag or Natick)",
          ["african", "native american", "wampanoag", "natick", "sailor"]),
        C("first-martyr", "giveaway",
          "Remembered as the first martyr of the American Revolution",
          ["first martyr", "martyr", "american revolution"]),
        C("framingham", "middle",
          "Born around 1723 and enslaved in Framingham, Massachusetts; he escaped in 1750 and spent about 20 years as a sailor",
          ["framingham", "escaped", "1750"]),
        C("king-street", "middle",
          "Killed on King Street (now State Street) outside the Custom House; a circle of cobblestones near the Old State House marks the site",
          ["king street", "custom house", "cobblestones", "old state house"]),
        C("preston", "middle",
          "Killed by soldiers of the 29th Regiment, sent to Boston in 1768; their captain, Thomas Preston, was found not guilty",
          ["thomas preston", "preston", "29th regiment"]),
        C("snowballs", "middle",
          "He was in a crowd that threw snowballs, ice, and insults at the soldiers",
          ["snowballs", "insults"]),
        C("adams-trial", "middle",
          "At the soldiers’ trial, John Adams argued that he had led the crowd and was chiefly to blame for the violence",
          ["john adams", "trial", "led the crowd"], "John Adams"),
        C("nell", "middle",
          "Black abolitionist William Cooper Nell organized yearly celebrations in his honor, starting in 1858",
          ["william cooper nell", "nell", "1858", "abolitionist"]),
        C("monument", "middle",
          "Honored, with the other four victims, by a monument on Boston Common unveiled in 1888",
          ["boston common", "1888", "monument"]),
        C("brown-ad", "power",
          "In 1750, William Brown of Framingham advertised a reward for him in the _Boston Gazette_, describing him as 6 feet 2 inches tall",
          ["william brown", "reward", "boston gazette", "6 feet 2"]),
        C("new-providence", "power",
          "A 1770 newspaper said he had lately come from New Providence in the Bahamas and was waiting for a ship to North Carolina",
          ["new providence", "bahamas", "north carolina"]),
        C("faneuil-hall", "power",
          "Because he was not from Boston, his body lay in Faneuil Hall, with sailor James Caldwell’s, before the shared funeral",
          ["faneuil hall", "james caldwell", "funeral"]),
        C("granary", "power",
          "Buried in one vault with other victims in the Granary Burying Ground, near Paul Revere, Samuel Adams, and John Hancock",
          ["granary burying ground", "granary", "vault"]),
        C("bells", "power",
          "On the day of his funeral, Boston’s shops closed and bells tolled in Boston, Charlestown, and Roxbury",
          ["bells", "charlestown", "roxbury", "shops"]),
        C("revere-sufferers", "power",
          "Named among the “unhappy Sufferers” below Paul Revere’s engraving of the massacre",
          ["unhappy sufferers", "paul revere", "engraving"]),
        C("other-victims", "power",
          "The other victims: Samuel Gray (a rope maker), Samuel Maverick (a 17-year-old apprentice), James Caldwell, and Patrick Carr, who died nine days later",
          ["samuel gray", "samuel maverick", "maverick", "patrick carr"]),
        C("oreilly", "power",
          "John Boyle O’Reilly’s poem for the 1888 monument calls him “the first to defy, and the first to die”",
          ["john boyle o’reilly", "o’reilly", "first to defy"]),
        C("silver-dollar", "power",
          "Pictured on a 1998 U.S. silver dollar honoring Black patriots of the Revolutionary War",
          ["silver dollar", "1998", "black patriots"]),
        C("indianapolis", "power",
          "Namesake of an Indianapolis high school where Oscar Robertson won state basketball titles in 1955 and 1956",
          ["indianapolis", "oscar robertson", "basketball"]),
        C("hugh-white", "power",
          "The crowd he joined had gathered around sentry Hugh White, who had struck a wigmaker’s apprentice with his musket",
          ["hugh white", "wigmaker", "apprentice"]),
        C("ropewalk", "power",
          "Three days before his death, soldiers and rope makers brawled at John Gray’s ropewalk",
          ["ropewalk", "john gray", "rope makers"])
    ],
    "trap": {
        "title": "The man, not the massacre",
        "body": "Almost every clue about Crispus Attucks is also a clue about the Boston Massacre: King Street, the Custom House, Captain Thomas Preston, John Adams’s defense of the soldiers, and Paul Revere’s engraving. If the question says “this man” or “this sailor,” the answer is Attucks, not the event. Other Black patriots of the Revolution come up too, like Peter Salem and Salem Poor, who fought at Bunker Hill, and James Armistead, who spied on the British before Yorktown.",
        "fix": "Listen for the noun: “this event” wants the Boston Massacre, while “this man” wants Attucks. Attucks clues are about dying on King Street in 1770; clues about fighting at Bunker Hill (1775) or spying for Lafayette (1781) point to someone else.",
        "line": "Real answer line: Crispus <b><u>Attucks</u></b> (prompt on <u>Crispus</u>)"
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
