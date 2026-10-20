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
    "id": "dred-scott-v-sandford",
    "name": "Dred Scott v. Sandford",
    "mono": "DS",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "1857 Supreme Court slavery case · Struck down the Missouri Compromise",
    "dates": "Decided March 6, 1857",
    "briefing": "Dred Scott was an enslaved man whose owner had taken him to live in places where slavery was banned, so he and his wife, Harriet, sued for their freedom. In 1857, the Supreme Court ruled 7–2 against him. Chief Justice Roger Taney wrote that Black Americans could not be citizens and that Congress could not ban slavery in the territories, so the Missouri Compromise was unconstitutional. The ruling deepened the split between North and South.",
    "answerHtml": "<b><u>Dred Scott</u></b> v. Sandford (accept <u>Scott v. Sandford</u> or the spelling “Sanford”; prompt on <u>Scott</u>)",
    "accept": [
        "dred scott v sandford",
        "dred scott v sanford",
        "dred scott",
        "scott v sandford",
        "scott v sanford",
        "scott vs sandford",
        "scott vs sanford",
        "scott versus sandford",
        "scott versus sanford"
    ],
    "prompt": [
        "scott",
        "sandford",
        "sanford"
    ],
    "reject": [
        "plessy v ferguson",
        "plessy",
        "brown v board of education",
        "brown v board",
        "marbury v madison",
        "mcculloch v maryland",
        "gibbons v ogden",
        "worcester v georgia",
        "prigg v pennsylvania",
        "ableman v booth",
        "united states v the amistad",
        "amistad",
        "roger taney",
        "taney",
        "missouri compromise",
        "kansas nebraska act",
        "fugitive slave act",
        "compromise of 1850",
        "freeport doctrine",
        "lincoln douglas debates",
        "fourteenth amendment",
        "14th amendment",
        "thirteenth amendment",
        "13th amendment",
        "harriet scott",
        "winfield scott"
    ],
    "tests": {
        "right": [
            "Dred Scott v. Sandford",
            "Dred Scott",
            "Scott v. Sanford",
            "Dred Scott decision",
            "Dred Scot v Sandford"
        ],
        "prompt": [
            "Scott"
        ],
        "wrong": [
            "Plessy v. Ferguson",
            "Marbury v. Madison",
            "Roger Taney",
            "Missouri Compromise",
            "Brown v. Board of Education"
        ]
    },
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Dred_Scott_v._Sandford",
    "qb": {
        "q": "Dred Scott",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        T("About two months after this case was decided, Taylor Blow, the son of the plaintiff’s first owner, freed the plaintiff and his family. The plaintiff died of tuberculosis in St. Louis the following year.",
          "For 10 points, name this 1857 Supreme Court case in which Roger Taney [“TAW-nee”] ruled that Black Americans could not be citizens."),
        T("Newspapers embarrassed Calvin Chaffee, an antislavery congressman from Massachusetts, by pointing out that his wife was the widow of John Emerson, who had owned the plaintiff in this case. Emerson, an army surgeon, had taken the plaintiff to Illinois and to Fort Snelling.",
          "For 10 points, name this 1857 case that ruled Congress could not ban slavery in the territories."),
        T("Shortly before this case was decided, President-elect James Buchanan privately urged Justice Robert Grier, a fellow Pennsylvanian, to join the majority. In his inaugural address two days before the ruling, Buchanan said that the Supreme Court would soon settle the question of slavery in the territories.",
          "It ruled that Black Americans could not be citizens. For 10 points, name this case decided by Roger Taney’s [“TAW-neez”] court in March 1857."),
        T("In a dissent, Justice Benjamin Curtis pointed out that free Black men could vote in five of the original states when the nation was founded. John McLean also dissented, and Curtis resigned from the Court later that year.",
          "For 10 points, name this 7–2 decision by Chief Justice Roger Taney [“TAW-nee”] that struck down the Missouri Compromise."),
        T("Montgomery Blair, who later served as Abraham Lincoln’s postmaster general, argued the plaintiff’s side when this case reached the Supreme Court. The justices heard arguments twice, in February and December 1856.",
          "For 10 points, name this 1857 case in which the Court ruled against an enslaved man who sued for his freedom."),
        T("A court clerk misspelled the name of this case’s defendant, John Sanford, the brother of army surgeon John Emerson’s widow. The plaintiff sued Sanford in federal court because Sanford lived in another state, New York.",
          "For 10 points, name this 1857 case in which Chief Justice Roger Taney [“TAW-nee”] ruled against the enslaved plaintiff."),
        T("The plaintiff in this case married Harriet Robinson at Fort Snelling, in what is now Minnesota, where the Missouri Compromise had banned slavery. His owner, army surgeon John Emerson, had also taken him to live in the free state of Illinois.",
          "For 10 points, name this 1857 Supreme Court case in which the plaintiff lost his bid for freedom."),
        T("In 1850, a jury in St. Louis decided that the plaintiff in this case and his wife were free, but the Missouri Supreme Court reversed that ruling two years later. The couple had first sued for their freedom in 1846 at St. Louis’s Old Courthouse.",
          "For 10 points, name this case that the U.S. Supreme Court decided against the plaintiff in 1857."),
        T("In his “House Divided” speech, Abraham Lincoln suggested that four men he called “Stephen, Franklin, Roger, and James” had worked together to spread slavery, pointing to this case as evidence. “Roger” was the Chief Justice who wrote this case’s majority opinion.",
          "For 10 points, name this 1857 decision that Lincoln and Stephen Douglas argued over during their 1858 debates."),
        T("At Freeport, Illinois, Stephen Douglas argued that settlers could still keep slavery out of a territory by refusing to pass laws protecting it, despite this ruling. That answer to Abraham Lincoln’s question cost Douglas support among Southern Democrats.",
          "For 10 points, name this 1857 Supreme Court case that declared the Missouri Compromise unconstitutional."),
        T("In 2012, a bronze statue of the plaintiff in this case and his wife, Harriet, was unveiled outside the Old Courthouse in St. Louis, where their fight for freedom began. That courthouse is part of Gateway Arch National Park.",
          "For 10 points, name this 1857 case in which the Supreme Court ruled that Black Americans could not be citizens."),
        T("This ruling was only the second time the Supreme Court had struck down a federal law, more than fifty years after _Marbury v. Madison_. The law it struck down had already been repealed by the Kansas–Nebraska Act of 1854.",
          "That law was the Missouri Compromise. For 10 points, name this 1857 case decided by Roger Taney’s [“TAW-neez”] court."),
        T("This ruling’s majority opinion said that enslaved people were property protected by the Fifth Amendment’s due process clause, so Congress could not stop settlers from bringing them into a western territory.",
          "The ruling also said Black Americans could not be citizens. For 10 points, name this 1857 Supreme Court case."),
        T("The Fourteenth Amendment, ratified in 1868, overturned part of this ruling by declaring that all persons born or naturalized in the United States are citizens. The Thirteenth Amendment had already ended slavery three years earlier.",
          "For 10 points, name this 1857 case in which Chief Justice Roger Taney [“TAW-nee”] said Black Americans could not be citizens."),
        T("The author of this ruling’s majority opinion had been named Chief Justice by Andrew Jackson after John Marshall died. That justice was also the brother-in-law of Francis Scott Key, who wrote the words of “The Star-Spangled Banner.”",
          "That justice was Roger Taney [“TAW-nee”]. For 10 points, name this 1857 case that declared the Missouri Compromise unconstitutional.")
    ],
    "clues": [
        C("ruling-1857", "giveaway",
          "1857 Supreme Court case in which an enslaved man lost his lawsuit for freedom",
          ["1857", "supreme court", "lawsuit", "enslaved"]),
        C("taney", "giveaway",
          "Chief Justice Roger Taney wrote the majority opinion",
          ["roger taney", "taney", "chief justice"]),
        C("citizens", "giveaway",
          "Ruled that Black Americans, enslaved or free, could not be U.S. citizens, so they could not sue in federal court",
          ["citizens", "federal court", "sue"]),
        C("missouri-compromise", "giveaway",
          "Ruled that Congress could not ban slavery in the territories, so the Missouri Compromise was unconstitutional",
          ["missouri compromise", "territories", "unconstitutional"], "Missouri Compromise"),
        C("vote-7-2", "middle",
          "Decided 7–2 on March 6, 1857, two days after James Buchanan became president",
          ["march 6", "buchanan", "7–2"]),
        C("emerson", "middle",
          "The plaintiff’s owner, army surgeon John Emerson, took him to the free state of Illinois and to Fort Snelling (in today’s Minnesota)",
          ["john emerson", "emerson", "illinois", "fort snelling"]),
        C("harriet", "middle",
          "His wife, Harriet Robinson, whom he married at Fort Snelling, also sued for her freedom",
          ["harriet", "robinson", "wife"]),
        C("fifth-amendment", "middle",
          "Taney said enslaved people were property protected by the Fifth Amendment’s due process clause",
          ["fifth amendment", "property", "due process"]),
        C("fourteenth", "middle",
          "The Fourteenth Amendment (1868) overturned its citizenship ruling: everyone born in the United States is a citizen",
          ["fourteenth amendment", "1868", "born"]),
        C("freeport", "middle",
          "At Freeport (1858), Stephen Douglas said territories could still keep slavery out by not passing laws to protect it",
          ["freeport", "stephen douglas", "douglas"], "Stephen A. Douglas"),
        C("st-louis", "middle",
          "The lawsuit began in 1846 at St. Louis’s Old Courthouse; a jury freed the couple in 1850, but the Missouri Supreme Court reversed it in 1852",
          ["st. louis", "old courthouse", "1846", "missouri supreme court"]),
        C("blow-freed", "power",
          "Taylor Blow, son of the plaintiff’s first owner, freed the family in May 1857; the plaintiff died of tuberculosis in 1858",
          ["taylor blow", "blow", "tuberculosis", "1858"]),
        C("chaffee", "power",
          "Emerson’s widow had married Calvin Chaffee, an antislavery congressman from Massachusetts, who was embarrassed by the case",
          ["calvin chaffee", "chaffee"]),
        C("grier", "power",
          "Buchanan privately urged Justice Robert Grier to join the majority; his inaugural address said the Court would soon settle the territorial question",
          ["robert grier", "grier", "inaugural"]),
        C("curtis", "power",
          "Benjamin Curtis and John McLean dissented; Curtis noted free Black men could vote in five original states, then resigned",
          ["benjamin curtis", "curtis", "john mclean", "mclean"]),
        C("blair", "power",
          "Montgomery Blair, later Lincoln’s postmaster general, argued the plaintiff’s side; the case was argued twice in 1856",
          ["montgomery blair", "blair", "postmaster general"]),
        C("sanford", "power",
          "The defendant, John Sanford of New York, was Mrs. Emerson’s brother; a court clerk misspelled his name in the case’s official title",
          ["john sanford", "misspelled", "clerk"]),
        C("house-divided", "power",
          "Lincoln’s “House Divided” speech suggested that “Stephen, Franklin, Roger, and James” had plotted to spread slavery",
          ["house divided", "plotted", "stephen, franklin, roger, and james"]),
        C("marbury", "power",
          "Only the second time the Supreme Court struck down a federal law, after _Marbury v. Madison_ (1803)",
          ["marbury", "second time", "1803"], "Marbury v. Madison"),
        C("kansas-nebraska", "power",
          "The Missouri Compromise had already been repealed by the Kansas–Nebraska Act (1854)",
          ["kansas–nebraska", "repealed", "1854"], "Kansas–Nebraska Act"),
        C("statue", "power",
          "A 2012 statue of the couple stands outside the Old Courthouse, part of Gateway Arch National Park",
          ["statue", "2012", "gateway arch"]),
        C("taney-key", "power",
          "Taney had been named Chief Justice by Andrew Jackson and was Francis Scott Key’s brother-in-law",
          ["andrew jackson", "brother-in-law", "francis scott key"], "Francis Scott Key")
    ],
    "trap": {
        "title": "Not Plessy, not Taney",
        "body": "Several famous Supreme Court cases about race get mixed up. _Dred Scott v. Sandford_ (1857) said Black Americans could not be citizens and struck down the Missouri Compromise; _Plessy v. Ferguson_ (1896) allowed “separate but equal” segregation; and _Brown v. Board of Education_ (1954) overturned Plessy for public schools. Some tossups instead ask for the man who wrote the opinion, Roger Taney, or for the law the case struck down, the Missouri Compromise.",
        "fix": "Listen for the date and the noun: 1857 and “this case” or “this decision” mean Dred Scott, while “this Chief Justice” means Taney and “this law” or “this agreement” means the Missouri Compromise. The defendant’s name is often spelled “Sanford,” and both spellings are accepted.",
        "line": "Real answer line: <b><u>Dred Scott</u></b> v. Sandford (accept <u>Scott v. Sandford</u> or the spelling “Sanford”; prompt on <u>Scott</u>)"
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
