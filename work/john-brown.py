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
    "id": "john-brown",
    "name": "John Brown",
    "mono": "JB",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Radical abolitionist · Led the 1859 raid on Harpers Ferry",
    "dates": "1800–1859",
    "briefing": "John Brown was a white abolitionist who believed that only force could end slavery. In 1856, during the fighting known as “Bleeding Kansas,” he and his followers killed five proslavery settlers, and in 1859 he led a raid on the federal armory at Harpers Ferry, Virginia, hoping to arm enslaved people. U.S. Marines led by Robert E. Lee captured him, and his raid and execution pushed the North and South closer to civil war.",
    "answerHtml": "<b><u>John Brown</u></b> (prompt on <u>Brown</u>)",
    "accept": [
        "john brown",
        "captain john brown"
    ],
    "prompt": [
        "brown",
        "old brown",
        "captain brown",
        "osawatomie brown",
        "old osawatomie brown"
    ],
    "reject": [
        "harpers ferry",
        "harpers ferry raid",
        "raid on harpers ferry",
        "john browns raid",
        "john browns body",
        "john brown jr",
        "john brown junior",
        "john brown gordon",
        "owen brown",
        "frederick brown",
        "frederick douglass",
        "douglass",
        "harriet tubman",
        "nat turner",
        "denmark vesey",
        "gabriel prosser",
        "robert e lee",
        "jeb stuart",
        "j e b stuart",
        "john wilkes booth",
        "brown v board of education",
        "brown v board",
        "james brown",
        "gordon brown",
        "henry box brown",
        "william wells brown"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/John_Brown_(abolitionist)",
    "qb": {
        "q": "John Brown",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        T("At a convention in Chatham, in what is now Ontario, this man presented a “Provisional Constitution” for a government he planned to set up after freeing enslaved people. A group of Northern backers called the Secret Six quietly paid for his plans.",
          "In 1859, he led a raid on the federal armory at Harpers Ferry. For 10 points, name this abolitionist."),
        T("Three days after proslavery forces raided the town of Lawrence in 1856, and two days after Senator Charles Sumner was attacked on the Senate floor, this man and his followers killed five proslavery settlers along Pottawatomie Creek.",
          "That attack deepened the violence known as “Bleeding Kansas.” For 10 points, name this abolitionist who later raided Harpers Ferry."),
        T("John Steuart Curry’s mural _Tragic Prelude_ in the Kansas State Capitol shows this man with his arms stretched wide, holding a Bible in one hand and a rifle in the other, as a tornado and a prairie fire rage behind him.",
          "This man led a raid on Harpers Ferry and was executed in 1859. For 10 points, name this abolitionist."),
        T("This man’s raiders took Lewis Washington, a great-grandnephew of George Washington, as a hostage, along with a sword said to have belonged to the first president. The first person killed in the raid was Heyward Shepherd, a free Black railroad worker.",
          "U.S. Marines led by Robert E. Lee captured him at Harpers Ferry. For 10 points, name this abolitionist."),
        T("Henry David Thoreau gave a lecture in Concord defending this man, and Ralph Waldo Emerson also spoke in his praise. Both writers had met him when he visited Concord to raise money for his fight against slavery.",
          "Weeks after Thoreau’s lecture, this man was executed for his raid on Harpers Ferry. For 10 points, name this abolitionist."),
        T("Julia Ward Howe wrote new words to the tune of a Union marching song which said that this man’s body “lies a-mouldering in the grave.” Her new version of that song became the “Battle Hymn of the Republic.”",
          "For 10 points, name this abolitionist who was executed after leading a raid on Harpers Ferry in 1859."),
        T("Frederick Douglass met this man at a stone quarry near Chambersburg, Pennsylvania, and refused to join his plan, warning that it would fail. This man also called Harriet Tubman “General Tubman,” though she did not take part in his attack.",
          "That attack targeted the federal armory at Harpers Ferry. For 10 points, name this abolitionist."),
        T("On the day of his execution, this man handed a guard a note predicting that “the crimes of this guilty land will never be purged away but with blood.” He had been convicted of treason against the state of Virginia.",
          "For 10 points, name this abolitionist who led a raid on Harpers Ferry in 1859."),
        T("In December 1858, this man led a raid into Missouri that freed 11 enslaved people, then guided them more than a thousand miles to freedom in Canada. Two years earlier, a battle at the Kansas town of Osawatomie had given him a nickname.",
          "He later attacked the federal armory at Harpers Ferry. For 10 points, name this abolitionist."),
        T("While running a wool business in Springfield, Massachusetts, this man organized Black residents into the League of Gileadites to resist the Fugitive Slave Act of 1850. His family’s farm was in North Elba, New York, where Gerrit Smith had given land to Black farmers.",
          "He is buried on that farm. For 10 points, name this abolitionist who raided Harpers Ferry in 1859."),
        T("In his 1860 Cooper Union speech, Abraham Lincoln insisted that this man was not a Republican and that no Republican had joined his attack. Many Southerners still blamed that attack on Republicans and other Northern opponents of slavery.",
          "That attack was the 1859 raid on Harpers Ferry. For 10 points, name this abolitionist."),
        T("In June 1856, this man’s fighters captured the proslavery militia leader Henry Clay Pate at the Battle of Black Jack. That August, his son Frederick was killed at Osawatomie, and two more of his sons later died in a raid he led.",
          "That raid targeted the federal armory at Harpers Ferry in 1859. For 10 points, name this abolitionist."),
        T("John Wilkes Booth joined a Virginia militia unit so he could watch this man’s execution in Charles Town. Cadets from the Virginia Military Institute also stood guard that day, led in part by a professor named Thomas Jackson, who later earned the nickname “Stonewall.”",
          "That execution followed this man’s 1859 raid on Harpers Ferry. For 10 points, name this abolitionist."),
        T("Stephen Vincent Benét won a Pulitzer Prize for a book-length Civil War poem whose title comes from a marching song about this man. James McBride’s novel _The Good Lord Bird_ is narrated by a boy who travels with this man through Kansas.",
          "In 1859, he led a famous raid on Harpers Ferry. For 10 points, name this abolitionist."),
        T("Thomas Jefferson wrote that the view where the Potomac and Shenandoah rivers meet was “worth a voyage across the Atlantic.” In 1906, W. E. B. Du Bois’s Niagara Movement met at that spot and honored this man, whose raid had made the town famous.",
          "That town is Harpers Ferry. For 10 points, name this abolitionist who led an 1859 raid on its armory."),
    ],
    "clues": [
        C("harpers-ferry", "giveaway", "Led a raid on the federal armory at Harpers Ferry, Virginia (now West Virginia), in October 1859", ["harpers ferry", "armory", "1859"]),
        C("abolitionist", "giveaway", "A white abolitionist who believed violence was justified to end slavery", ["abolitionist", "violence", "slavery"], "Abolitionism"),
        C("lee-marines", "giveaway", "U.S. Marines led by Colonel Robert E. Lee captured him in the armory’s engine house", ["marines", "engine house", "lee"], "Robert E. Lee"),
        C("executed", "giveaway", "Captured, tried, and executed in December 1859 after his raid failed", ["executed", "december 1859", "tried"]),
        C("bleeding-kansas", "giveaway", "Fought proslavery settlers during “Bleeding Kansas” in the 1850s", ["bleeding kansas", "kansas", "proslavery"], "Kansas–Nebraska Act"),
        C("pottawatomie", "middle", "Pottawatomie Creek (May 1856): he and his followers killed five proslavery settlers, days after proslavery forces raided Lawrence", ["pottawatomie", "lawrence", "five"]),
        C("treason", "middle", "Convicted of treason against the state of Virginia, not the United States, and executed in Charles Town", ["treason", "charles town", "virginia"]),
        C("song", "middle", "Union soldiers sang that his body “lies a-mouldering in the grave”; Julia Ward Howe used the tune for the “Battle Hymn of the Republic”", ["a-mouldering", "battle hymn", "julia ward howe"]),
        C("douglass", "middle", "Frederick Douglass met him at a stone quarry near Chambersburg, Pennsylvania, but refused to join the raid", ["frederick douglass", "douglass", "quarry", "chambersburg"], "Frederick Douglass"),
        C("tubman", "middle", "Called Harriet Tubman “General Tubman”; she did not take part in the raid", ["tubman", "general tubman"], "Harriet Tubman"),
        C("secret-six", "middle", "The “Secret Six,” including Gerrit Smith and Thomas Wentworth Higginson, paid for his plans", ["secret six", "gerrit smith", "higginson"]),
        C("osawatomie", "middle", "A battle at Osawatomie, Kansas (1856), where his son Frederick was killed, gave him a nickname", ["osawatomie", "frederick", "1856"]),
        C("cooper-union", "middle", "In his Cooper Union speech (1860), Abraham Lincoln insisted that no Republican had joined his raid", ["cooper union", "lincoln", "republican"], "Abraham Lincoln"),
        C("chatham", "power", "At a convention in Chatham, Canada (1858), presented a “Provisional Constitution” for a new government", ["chatham", "provisional constitution", "canada"]),
        C("missouri-raid", "power", "Freed 11 enslaved people in a Missouri raid (December 1858) and led them to Canada", ["missouri", "canada", "1858"]),
        C("gileadites", "power", "Formed the League of Gileadites in Springfield, Massachusetts (1851), to resist the Fugitive Slave Act", ["gileadites", "springfield", "fugitive slave act"]),
        C("last-note", "power", "His last note: “the crimes of this guilty land will never be purged away but with blood”", ["guilty land", "purged", "crimes"]),
        C("thoreau", "power", "Henry David Thoreau gave an 1859 lecture in Concord defending him; Ralph Waldo Emerson praised him too", ["thoreau", "concord", "emerson"]),
        C("curry", "power", "John Steuart Curry’s mural _Tragic Prelude_ in the Kansas State Capitol shows him holding a Bible and a rifle", ["tragic prelude", "curry", "kansas state capitol"]),
        C("north-elba", "power", "His family’s farm was in North Elba, New York, near Lake Placid, where he is buried", ["north elba", "lake placid", "buried"]),
        C("shepherd", "power", "The first person killed in the raid was Heyward Shepherd, a free Black railroad worker", ["heyward shepherd", "shepherd", "railroad"]),
        C("lewis-washington", "power", "His raiders took Lewis Washington, George Washington’s great-grandnephew, as a hostage", ["lewis washington", "hostage", "great-grandnephew"]),
        C("black-jack", "power", "Captured the proslavery leader Henry Clay Pate at the Battle of Black Jack (June 1856)", ["black jack", "henry clay pate", "pate"]),
        C("benet-mcbride", "power", "Stephen Vincent Benét’s Pulitzer-winning poem takes its title from the song about him; he also appears in James McBride’s novel _The Good Lord Bird_", ["benét", "pulitzer", "good lord bird", "mcbride"]),
        C("booth", "power", "John Wilkes Booth joined a militia unit to watch his execution; VMI cadets, partly led by Thomas “Stonewall” Jackson, stood guard", ["wilkes booth", "booth", "militia", "stonewall"], "John Wilkes Booth"),
        C("du-bois", "power", "W. E. B. Du Bois wrote a biography of him (1909); Du Bois’s Niagara Movement honored him at Harpers Ferry in 1906", ["du bois", "niagara", "1909", "1906"]),
        C("jefferson-view", "power", "Thomas Jefferson said the view at Harpers Ferry, where the Potomac and Shenandoah rivers meet, was “worth a voyage across the Atlantic”", ["potomac", "shenandoah", "voyage across the atlantic"]),
    ],
    "trap": {
        "title": "The man, not the town",
        "body": "Many tossups ask for Harpers Ferry, the town he attacked, or for his raid, instead of the man himself. Clues like the federal armory, Robert E. Lee’s Marines, and the engine house show up in both kinds of questions, so a quick buzz with the wrong one loses the tossup. “Brown” alone only earns a prompt, because other Browns (like the _Brown v. Board of Education_ case) come up too.",
        "fix": "Listen for the noun. “This man” or “this abolitionist” wants John Brown. “This town” or “this place,” where the Potomac and Shenandoah rivers meet, wants Harpers Ferry, and “this event” wants John Brown’s raid on Harpers Ferry. Say the full name, “John Brown.”",
        "line": "Real answer lines: <b><u>John Brown</u></b> (prompt on <u>Brown</u>) and, for the town, <b><u>Harpers Ferry</u></b>"
    },
    "tests": {
        "right": [
            "John Brown",
            "Captain John Brown",
            "Jon Brown",
            "John Brown the abolitionist",
            "john brwon"
        ],
        "prompt": [
            "Brown",
            "Osawatomie Brown"
        ],
        "wrong": [
            "Harpers Ferry",
            "Frederick Douglass",
            "Nat Turner",
            "John Brown Gordon",
            "Brown v. Board of Education",
            "Robert E. Lee",
            "John Wilkes Booth"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
