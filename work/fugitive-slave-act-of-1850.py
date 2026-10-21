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
    "id": "fugitive-slave-act-of-1850",
    "name": "Fugitive Slave Act of 1850",
    "mono": "FSA",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Part of the Compromise of 1850 · Forced free states to return freedom seekers",
    "dates": "Signed September 18, 1850; repealed 1864",
    "briefing": "The Fugitive Slave Act of 1850, part of the Compromise of 1850, made officials and even ordinary citizens in the free states help capture people who had escaped slavery. Accused people could not testify or have a jury trial, and a federal commissioner earned $10 for sending someone south but only $5 for setting someone free. The law turned many Northerners against slavery, drove thousands of Black Americans to Canada, and helped inspire _Uncle Tom’s Cabin_.",
    "answerHtml": "<b><u>Fugitive Slave Act</u></b> of 1850 (accept <u>Fugitive Slave Law</u>; do not accept “Compromise of 1850” or “Kansas–Nebraska Act”)",
    "accept": [
        "fugitive slave act",
        "fugitive slave act of 1850",
        "the fugitive slave act",
        "fugitive slave law",
        "fugitive slave law of 1850",
        "the fugitive slave law",
        "fugitive slave bill",
        "1850 fugitive slave act",
        "1850 fugitive slave law",
        "fugitive slave acts",
        "fugitive slave laws"
    ],
    "prompt": [
        "fugitive slave"
    ],
    "reject": [
        "compromise of 1850",
        "the compromise of 1850",
        "compromise",
        "kansas nebraska act",
        "kansas nebraska",
        "missouri compromise",
        "fugitive slave act of 1793",
        "fugitive slave law of 1793",
        "1793",
        "fugitive slave clause",
        "dred scott",
        "dred scott v sandford",
        "underground railroad",
        "uncle toms cabin",
        "personal liberty laws",
        "personal liberty law",
        "prigg v pennsylvania",
        "ableman v booth",
        "wilmot proviso",
        "black codes",
        "slave codes",
        "gag rule",
        "emancipation proclamation",
        "omnibus bill"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Fugitive_Slave_Act_of_1850",
    "qb": {
        "q": "Fugitive Slave Act",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        T("Senator James Mason of Virginia wrote this law, which paid federal commissioners ten dollars when they sent an accused person south but only five dollars when they set the person free. Critics said that difference was a bribe.",
          "It passed as part of the Compromise of 1850. For 10 points, name this law that forced Northerners to help return people who had escaped slavery."),
        T("Southern leaders demanded this law after the Supreme Court ruled in _Prigg v. Pennsylvania_ that state officials did not have to help capture people who had escaped slavery. Several Northern states had then passed “personal liberty laws” that barred their officials and jails from helping.",
          "For 10 points, name this 1850 law that made it a federal job to return freedom seekers to their enslavers."),
        T("In February 1851, a group of Black abolitionists including Lewis Hayden rushed into a Boston courtroom and freed Shadrach Minkins, a waiter who had been arrested under this law. They helped Minkins escape to Canada.",
          "For 10 points, name this law, part of the Compromise of 1850, that required the return of people who had escaped slavery."),
        T("In 1854, President Franklin Pierce sent federal troops to Boston to make sure that Anthony Burns was returned to slavery in Virginia under this law. Thousands of protesters lined the streets as soldiers marched Burns to a ship.",
          "For 10 points, name this law passed in 1850 to force the return of people who had escaped slavery."),
        T("Ralph Waldo Emerson wrote in his journal that this law was a “filthy enactment” that he would not obey. In 1854, Henry David Thoreau attacked it in a Fourth of July speech called “Slavery in Massachusetts.”",
          "For 10 points, name this law that required Northerners to help capture people who had escaped slavery."),
        T("A novel first published in installments in the antislavery newspaper _The National Era_ was written partly in response to this law. In that novel, the enslaved mother Eliza escapes with her young son by crossing the icy Ohio River.",
          "That novel was Harriet Beecher Stowe’s _Uncle Tom’s Cabin_. For 10 points, name this law passed as part of the Compromise of 1850."),
        T("In _Ableman v. Booth_, the Supreme Court ruled that Wisconsin could not overrule this law, after newspaper editor Sherman Booth helped free Joshua Glover from a jail in Milwaukee. Wisconsin’s own supreme court had declared this law unconstitutional.",
          "For 10 points, name this 1850 law that required free states to return people who had escaped slavery."),
        T("Under this law, a person accused of escaping slavery was denied a jury trial and was not allowed to testify in his or her own defense. A sworn statement from the person claiming ownership was enough to send the accused south.",
          "For 10 points, name this law signed by Millard Fillmore as part of the Compromise of 1850."),
        T("This law threatened anyone who helped a person escape slavery with a fine of up to $1,000 and six months in jail. It also let federal marshals order ordinary citizens to help catch people who had escaped.",
          "For 10 points, name this 1850 law that led many freedom seekers to flee all the way to Canada."),
        T("Millard Fillmore signed this law in September 1850, about two months after Zachary Taylor’s death made him president. Stephen Douglas helped steer it through Congress as one of several separate bills, after Henry Clay’s “Omnibus Bill” fell apart.",
          "For 10 points, name this law about people who had escaped slavery, part of the Compromise of 1850."),
        T("William and Ellen Craft had escaped from Georgia in 1848, with Ellen disguised as a white man and William posing as her servant. Two years later, they fled from Boston to England after slave catchers came to seize them under this law.",
          "For 10 points, name this law that forced free states to help return people who had escaped slavery."),
        T("In the Jerry Rescue of 1851, abolitionists in Syracuse, New York, broke into the building where William Henry was being held under this law and helped him reach Canada. The rescue happened while the Liberty Party was meeting in the city.",
          "For 10 points, name this 1850 law that required the return of people who had escaped slavery."),
        T("Early in the Civil War, General Benjamin Butler refused to return three men who had escaped to Fort Monroe, calling them “contraband of war” instead of following this law. Congress finally repealed this law in June 1864.",
          "For 10 points, name this law from 1850 that required Northerners to help return people who had escaped slavery."),
        T("In 1860, Harriet Tubman helped a crowd in Troy, New York, free Charles Nalle, who was about to be sent back south under this law. After this law passed, Tubman began guiding freedom seekers all the way to St. Catharines in Canada.",
          "For 10 points, name this law, part of the Compromise of 1850, that forced free states to return freedom seekers."),
        T("John Greenleaf Whittier’s poem “Ichabod” attacked Daniel Webster for supporting this law in his Seventh of March speech. In that speech, Webster said he spoke “not as a Massachusetts man, nor as a Northern man, but as an American.”",
          "For 10 points, name this law that required the return of people who had escaped slavery, passed in 1850.")
    ],
    "clues": [
        C("compromise-1850", "giveaway", "Part of the Compromise of 1850, proposed by Henry Clay", ["compromise of 1850", "henry clay"], "Compromise of 1850"),
        C("return", "giveaway", "Required officials and citizens in the free states to help return people who had escaped slavery", ["escaped slavery", "return", "free states"]),
        C("canada", "giveaway", "Drove many freedom seekers and free Black Americans to flee to Canada; the Underground Railroad grew busier", ["canada", "underground railroad"], "Underground Railroad"),
        C("fillmore", "giveaway", "Signed by President Millard Fillmore on September 18, 1850", ["millard fillmore", "fillmore", "september 18, 1850"]),
        C("jury", "middle", "Accused people got no jury trial and could not testify for themselves", ["jury trial", "testify"]),
        C("commissioners", "middle", "Federal commissioners got $10 for sending an accused person south but only $5 for setting the person free", ["commissioners", "$10", "$5"]),
        C("penalties", "middle", "Helping a freedom seeker could bring a $1,000 fine and six months in jail; marshals could order bystanders to help", ["$1,000", "six months", "bystanders"]),
        C("uncle-tom", "middle", "Helped inspire Harriet Beecher Stowe to write _Uncle Tom’s Cabin_ (1852)", ["uncle tom’s cabin", "stowe", "harriet beecher stowe"], "Uncle Tom’s Cabin"),
        C("personal-liberty", "middle", "Northern states passed “personal liberty laws” to block it", ["personal liberty laws", "personal liberty"]),
        C("burns", "middle", "Anthony Burns (1854): federal troops marched him through Boston to a ship back to slavery in Virginia", ["anthony burns", "burns", "boston"]),
        C("minkins", "middle", "Shadrach Minkins (1851): rescued from a Boston courtroom and taken to Canada", ["shadrach minkins", "minkins"]),
        C("webster", "middle", "Daniel Webster backed it in his Seventh of March speech (1850)", ["daniel webster", "seventh of march"], "Daniel Webster"),
        C("tubman", "middle", "After it passed, Harriet Tubman led freedom seekers all the way to St. Catharines, Canada", ["harriet tubman", "st. catharines"], "Harriet Tubman"),
        C("mason", "power", "Written by Senator James Mason of Virginia", ["james mason", "mason"]),
        C("prigg", "power", "Came after _Prigg v. Pennsylvania_ (1842) ruled that state officials did not have to help capture freedom seekers", ["prigg", "1842"]),
        C("law-1793", "power", "Strengthened a weaker 1793 law, signed by George Washington, that carried out a clause in Article IV of the Constitution", ["1793", "george washington", "article iv"]),
        C("ableman", "power", "_Ableman v. Booth_ (1859): the Supreme Court said Wisconsin could not overrule it; Sherman Booth had helped free Joshua Glover", ["ableman", "sherman booth", "joshua glover"]),
        C("jerry", "power", "Jerry Rescue (1851): abolitionists in Syracuse, New York, freed William “Jerry” Henry", ["jerry rescue", "syracuse"]),
        C("crafts", "power", "William and Ellen Craft fled from Boston to England when slave catchers came for them (1850)", ["ellen craft", "england"]),
        C("emerson-thoreau", "power", "Emerson called it a “filthy enactment”; Thoreau attacked it in the speech “Slavery in Massachusetts” (1854)", ["filthy enactment", "thoreau", "slavery in massachusetts"]),
        C("ichabod", "power", "Whittier’s poem “Ichabod” attacked Webster for supporting it", ["ichabod", "whittier"]),
        C("gileadites", "power", "John Brown formed the League of Gileadites in Springfield, Massachusetts (1851), to resist it", ["gileadites", "springfield"], "John Brown"),
        C("nalle", "power", "Harriet Tubman helped a crowd free Charles Nalle in Troy, New York (1860)", ["charles nalle", "nalle", "troy"]),
        C("contraband", "power", "General Benjamin Butler called escaped men “contraband of war” (1861); Congress repealed it in June 1864", ["contraband", "1864", "butler"]),
        C("sims", "power", "Thomas Sims (1851) was sent back from Boston to slavery in Georgia", ["thomas sims", "sims"])
    ],
    "trap": {
        "title": "One law or the whole deal?",
        "body": "The Fugitive Slave Act was one of five laws in the Compromise of 1850, so the two answer lines share clues such as Henry Clay, Stephen Douglas, Daniel Webster, and Millard Fillmore. Saying “Compromise of 1850” when the question wants this one law is wrong, and so is the Kansas–Nebraska Act of 1854, which repealed the Missouri Compromise line and led to “Bleeding Kansas.” An older Fugitive Slave Act, signed by George Washington, dates from 1793.",
        "fix": "If the question asks for “this law” and mentions commissioners’ fees, jury trials, Shadrach Minkins, Anthony Burns, or personal liberty laws, say “Fugitive Slave Act.” If it asks for “this set of laws” or “this compromise” and mentions California’s statehood or the slave trade in Washington, D.C., say “Compromise of 1850.”",
        "line": "Real answer line: <b><u>Fugitive Slave Act</u></b> of 1850 (accept <u>Fugitive Slave Law</u>; do not accept “Compromise of 1850” or “Kansas–Nebraska Act”)"
    },
    "tests": {
        "right": [
            "Fugitive Slave Act",
            "Fugitive Slave Law",
            "Fugitive Slave Act of 1850",
            "Fugative Slave Act",
            "the Fugitive Slave Law"
        ],
        "prompt": [
            "Fugitive Slave"
        ],
        "wrong": [
            "Compromise of 1850",
            "Kansas-Nebraska Act",
            "Fugitive Slave Act of 1793",
            "Missouri Compromise",
            "Underground Railroad",
            "Uncle Tom's Cabin"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
