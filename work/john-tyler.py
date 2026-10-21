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
    "id": "john-tyler",
    "name": "John Tyler",
    "mono": "TY",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "10th U.S. President · First VP to become president when a president died",
    "dates": "1790–1862",
    "briefing": "John Tyler became president in 1841 when William Henry Harrison died after just one month in office, and he insisted he was the real president, not a stand-in, even as critics mocked him as “His Accidency.” His own Whig Party threw him out after he vetoed its bank bills. He signed the resolution to annex Texas, fathered 15 children, and was elected to the Confederate Congress but died in 1862 before he could serve.",
    "answerHtml": "John <b><u>Tyler</u></b> (do not accept “William Henry Harrison” or “Zachary Taylor”)",
    "accept": [
        "john tyler",
        "tyler",
        "president tyler",
        "president john tyler"
    ],
    "prompt": [],
    "reject": [
        "william henry harrison",
        "william harrison",
        "harrison",
        "benjamin harrison",
        "tippecanoe",
        "old tippecanoe",
        "tippecanoe and tyler too",
        "zachary taylor",
        "daniel webster",
        "webster",
        "henry clay",
        "clay",
        "james k polk",
        "james polk",
        "polk",
        "john c calhoun",
        "calhoun",
        "abel upshur",
        "upshur",
        "millard fillmore",
        "fillmore",
        "martin van buren",
        "van buren",
        "andrew jackson",
        "jackson",
        "jefferson davis",
        "john minor botts",
        "botts",
        "julia tyler",
        "julia gardiner tyler",
        "julia gardiner",
        "letitia tyler",
        "letitia christian tyler",
        "john tyler sr",
        "john tyler senior",
        "lyon gardiner tyler",
        "tyler precedent",
        "tyler doctrine",
        "wat tyler",
        "tyler perry",
        "steven tyler",
        "anne tyler",
        "royall tyler",
        "liv tyler",
        "tyler texas"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/John_Tyler",
    "qb": {
        "q": "Tyler",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        T("In 1833, this man cast the only vote in the Senate against the Force Bill, which let Andrew Jackson use the army against South Carolina during the nullification crisis. Three years later, he resigned from the Senate rather than obey Virginia’s instructions to help erase the Senate’s censure of Jackson.",
          "He later joined the Whigs. For 10 points, name this Virginian who became president in 1841 after William Henry Harrison died."),
        T("Fletcher Webster, the son of the Secretary of State, traveled overnight to Williamsburg, Virginia, in April 1841 to bring this man some unexpected news. The next day, Judge William Cranch swore him in at a hotel in Washington, D.C.",
          "The news was that William Henry Harrison had died. For 10 points, name this man who became the 10th president."),
        T("This man reportedly sent back unopened any letters addressed to the “Acting President,” insisting that he held the office with all of its powers. His view, which became known as the precedent named after him, was finally written into the Constitution by the Twenty-fifth Amendment in 1967.",
          "Critics still mocked him as “His Accidency.” For 10 points, name this first vice president to become president after a president’s death."),
        T("In September 1841, every member of this president’s cabinet except Daniel Webster resigned after he vetoed a second bill to create a national bank, a plan pushed by Henry Clay. Days later, a meeting of his own party’s members of Congress expelled him from the party.",
          "That left him a president without a party. For 10 points, name this president who succeeded William Henry Harrison."),
        T("In 1843, Virginia congressman John Minor Botts introduced a resolution to impeach this man, the first such attempt against any president, but the House voted it down. Months earlier, a House committee led by John Quincy Adams had condemned this president’s use of the veto.",
          "His opponents were angry about his vetoes of bank bills. For 10 points, name this president who succeeded William Henry Harrison."),
        T("On this president’s last full day in office in 1845, Congress overrode his veto of a bill about revenue cutters, small armed ships that enforced customs laws, the first time it had ever overridden a presidential veto. That same day, March 3, Florida became a state.",
          "Three days earlier, he had signed a resolution to annex Texas. For 10 points, name this 10th president."),
        T("In 1844, a huge new cannon nicknamed the “Peacemaker” exploded during a demonstration aboard the USS _Princeton_, killing Secretary of State Abel Upshur and Navy Secretary Thomas Gilmer. This president, who was below deck at the time, was unhurt.",
          "For 10 points, name this president, who had taken office in 1841 after William Henry Harrison died."),
        T("Four months after the USS _Princeton_ disaster killed her father, Julia Gardiner married this man in New York City, making him the first president to marry while in office. His first wife, Letitia, had been the first First Lady to die in the White House.",
          "He had 15 children, more than any other president. For 10 points, name this 10th president."),
        T("In 1842, this president applied the Monroe Doctrine to the Hawaiian Islands, warning European powers not to take them over. Two years later, his envoy Caleb Cushing signed the Treaty of Wanghia [“wahng-SHYAH”], the first treaty between the United States and China.",
          "For 10 points, name this president who also signed the joint resolution to annex Texas."),
        T("During this president’s term, the Webster–Ashburton Treaty settled the long-disputed border between Maine and the British colony of New Brunswick. The Second Seminole War in Florida also came to an end in 1842, the same year that treaty was signed.",
          "For 10 points, name this president, the first vice president to take over after a president died."),
        T("After the Senate rejected an annexation treaty negotiated by Secretary of State John C. Calhoun, this president asked Congress to act by joint resolution, which needed only a simple majority in each house. He signed that resolution on March 1, 1845, just days before leaving office.",
          "For 10 points, name this president who began the process of adding Texas to the Union."),
        T("This man named his Virginia plantation Sherwood Forest, comparing himself to the outlaw Robin Hood after his party cast him out. In February 1861, he presided over a peace conference in Washington that tried and failed to prevent the Civil War.",
          "Two decades earlier, he had succeeded William Henry Harrison. For 10 points, name this former president."),
        T("This man was elected to the Confederate House of Representatives but died in Richmond in January 1862 before he could take his seat. Because he had sided with the Confederacy, the federal government held no official mourning for this former president.",
          "For 10 points, name this 10th president, who had taken office after William Henry Harrison died."),
        T("Two grandsons of this president, born in the 1920s, lived into the 21st century, because both he and one of his sons became fathers late in life. This man had 15 children with his two wives, more than any other president.",
          "For 10 points, name this president, mocked as “His Accidency” after he succeeded William Henry Harrison."),
        T("This man, whose father had also been governor of Virginia, graduated from the College of William & Mary at 17. As president, he served his entire term without a vice president, because the Constitution then had no way to fill an empty vice presidency.",
          "For 10 points, name this Virginian who became president when William Henry Harrison died in 1841.")
    ],
    "clues": [
        C("tenth", "giveaway", "10th President (1841–1845); the first vice president to become president when a president died",
          ["10th president", "vice president", "1841"]),
        C("harrison", "giveaway", "Took over when William Henry Harrison died one month into his term (April 1841)",
          ["william henry harrison", "harrison", "one month"], "William Henry Harrison"),
        C("accidency", "giveaway", "Critics mocked him as “His Accidency”",
          ["accidency", "his accidency"]),
        C("texas", "giveaway", "Signed the joint resolution to annex Texas on March 1, 1845",
          ["texas", "annex", "joint resolution"], "Republic of Texas"),
        C("tippecanoe", "giveaway", "Harrison’s running mate in 1840, under a Whig slogan that paired his name with Harrison’s nickname, “Tippecanoe”",
          ["tippecanoe", "running mate", "1840"]),
        C("precedent", "middle", "Insisted he was fully president, not “Acting President”; the 25th Amendment (1967) later wrote his view into the Constitution",
          ["acting president", "25th amendment", "precedent"], "Vice President of the United States"),
        C("expelled", "middle", "Vetoed Henry Clay’s national bank bills (1841); his cabinet quit except Daniel Webster, and the Whigs expelled him",
          ["national bank", "expelled", "daniel webster", "whigs"], "Daniel Webster"),
        C("fifteen", "middle", "Had 15 children with two wives, the most of any president",
          ["15 children", "children"]),
        C("princeton", "middle", "The USS _Princeton_’s “Peacemaker” cannon exploded (1844), killing Secretary of State Abel Upshur and Navy Secretary Thomas Gilmer",
          ["princeton", "peacemaker", "upshur"]),
        C("julia", "middle", "Married Julia Gardiner (1844), the first president to marry in office; his first wife, Letitia, died in the White House (1842)",
          ["julia gardiner", "letitia", "married"]),
        C("confederate", "middle", "Elected to the Confederate Congress but died in Richmond (January 1862) before taking his seat; Washington held no official mourning",
          ["confederate", "richmond", "1862", "mourning"]),
        C("peace-conference", "middle", "Presided over the failed Washington Peace Conference (February 1861)",
          ["peace conference", "1861"]),
        C("webster-ashburton", "middle", "The Webster–Ashburton Treaty (1842) settled the Maine–New Brunswick border",
          ["webster–ashburton", "maine", "new brunswick"]),
        C("force-bill", "power", "Cast the only Senate vote against the Force Bill (1833)",
          ["force bill", "1833"]),
        C("censure", "power", "Resigned from the Senate (1836) rather than vote to erase Andrew Jackson’s censure",
          ["censure", "resigned", "1836"]),
        C("fletcher-webster", "power", "Fletcher Webster brought him the news in Williamsburg; Judge William Cranch swore him in",
          ["fletcher webster", "williamsburg", "cranch"]),
        C("botts", "power", "John Minor Botts introduced the first resolution to impeach a president (1843); it failed",
          ["botts", "impeach"]),
        C("override", "power", "Congress overrode his veto of a revenue cutter bill on March 3, 1845, the first override ever",
          ["overrode", "override", "revenue cutter"]),
        C("hawaii", "power", "Extended the Monroe Doctrine to Hawaii (1842)",
          ["hawaii", "monroe doctrine"]),
        C("wanghia", "power", "Treaty of Wanghia (1844), the first U.S. treaty with China, negotiated by Caleb Cushing",
          ["wanghia", "caleb cushing", "china"]),
        C("seminole", "power", "The Second Seminole War ended during his term (1842)",
          ["second seminole war", "seminole"]),
        C("calhoun", "power", "The Senate rejected John C. Calhoun’s Texas annexation treaty (1844), so he used a joint resolution needing only simple majorities",
          ["calhoun", "simple majorities", "treaty"]),
        C("florida", "power", "Florida became a state on March 3, 1845, his last full day in office",
          ["florida", "march 3"]),
        C("sherwood", "power", "Named his plantation Sherwood Forest, comparing himself to the outlaw Robin Hood",
          ["sherwood forest", "robin hood", "outlaw"]),
        C("grandsons", "power", "Two of his grandsons, born in the 1920s, lived into the 21st century",
          ["grandsons", "21st century"]),
        C("no-vp", "power", "Served his entire term without a vice president",
          ["without a vice president", "entire term"]),
        C("governor", "power", "Governor of Virginia (1825–1827), like his father; graduated from William & Mary at 17",
          ["governor of virginia", "william & mary", "father"])
    ],
    "trap": {
        "title": "Tyler, Harrison, or Taylor?",
        "body": "Tyler tossups lean on William Henry Harrison: the 1840 slogan “Tippecanoe and Tyler Too,” Harrison’s one-month presidency, and the Whig Party they both led. Buzzing “Harrison” on those clues is wrong when the question wants the man who replaced him. Zachary Taylor, the 12th president, has a similar-sounding name and was also a Whig, but he was a general who won the 1848 election and then died in office himself.",
        "fix": "Anything after April 4, 1841, like “His Accidency,” the bank vetoes, the cabinet resigning, the USS _Princeton_, and the Texas annexation resolution, means Tyler. Tippecanoe, Tecumseh, and the long inaugural speech mean Harrison; the Mexican War general “Old Rough and Ready” means Taylor.",
        "line": "Real answer line: John <b><u>Tyler</u></b> (do not accept “William Henry Harrison”)"
    },
    "tests": {
        "right": [
            "John Tyler",
            "Tyler",
            "President Tyler",
            "Jon Tyler",
            "Tylor"
        ],
        "prompt": [],
        "wrong": [
            "William Henry Harrison",
            "Zachary Taylor",
            "Daniel Webster",
            "James K. Polk",
            "Tyler Perry",
            "Julia Tyler",
            "Harrison"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
