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
    "id": "free-soil-party",
    "name": "Free Soil Party",
    "mono": "FSL",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Antislavery third party · Fought the spread of slavery into the West",
    "dates": "1848–1854",
    "briefing": "In 1848, antislavery Democrats, Whigs, and Liberty Party members met in Buffalo, New York, and formed the Free Soil Party, whose slogan was “Free Soil, Free Speech, Free Labor, and Free Men.” The party did not call for ending slavery in the South, but it fought to keep slavery out of the western territories. Its candidate, former president Martin Van Buren, won no states, and by 1854 most Free Soilers had joined the new Republican Party.",
    "answerHtml": "<b><u>Free Soil</u></b> Party (accept <u>Free Soilers</u>; do not accept “Liberty Party” or “Republican Party”)",
    "accept": [
        "free soil party",
        "the free soil party",
        "free soil",
        "free soilers",
        "free soiler",
        "freesoil",
        "freesoil party",
        "freesoilers",
        "free soil movement"
    ],
    "prompt": [],
    "reject": [
        "liberty party",
        "the liberty party",
        "republican party",
        "the republican party",
        "democratic party",
        "whig party",
        "conscience whigs",
        "cotton whigs",
        "barnburners",
        "barnburner",
        "know nothing party",
        "know nothings",
        "american party",
        "free state party",
        "free staters",
        "free silver",
        "free silver party",
        "populist party",
        "abolitionist party",
        "wilmot proviso"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Free_Soil_Party",
    "qb": {
        "q": "Free Soil",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        T("This party was founded at an August 1848 convention in Buffalo, New York, which brought together New York’s “Barnburner” Democrats, Massachusetts’s “Conscience Whigs,” and most members of the Liberty Party, an earlier abolitionist party.",
          "It opposed the spread of slavery into the western territories. For 10 points, name this third party that nominated Martin Van Buren for president in 1848."),
        T("Charles Francis Adams, the son of John Quincy Adams, was this party’s candidate for vice president in 1848. That year, its presidential candidate split the Democratic vote in New York, which helped the Whig Zachary Taylor win the election.",
          "That candidate was former president Martin Van Buren. For 10 points, name this party that opposed spreading slavery to the West."),
        T("Senator John P. Hale of New Hampshire was this party’s candidate for president in 1852, with George Washington Julian of Indiana as his running mate. They won only about 5 percent of the popular vote.",
          "For 10 points, name this antislavery party whose 1848 candidate had been Martin Van Buren."),
        T("This party grew out of support for a failed 1846 proposal by Pennsylvania congressman David Wilmot to ban slavery in any land the United States won from Mexico. That proposal passed the House more than once but died in the Senate.",
          "For 10 points, name this party, formed in 1848, that fought to keep slavery out of the western territories."),
        T("In 1849, Ohio’s legislature elected Salmon P. Chase to the U.S. Senate with the help of this party’s members, who had made a deal with the Democrats. Chase later served as Abraham Lincoln’s Secretary of the Treasury.",
          "For 10 points, name this antislavery party that ran Martin Van Buren for president in 1848."),
        T("In 1851, a coalition of Democrats and members of this party in the Massachusetts legislature elected Charles Sumner to the U.S. Senate. Five years later, Sumner was attacked with a cane on the Senate floor by South Carolina congressman Preston Brooks.",
          "For 10 points, name this antislavery party of the late 1840s and early 1850s, whose members later joined the Republicans."),
        T("This party ran its last presidential campaign in 1852. Two years later, after the Kansas–Nebraska Act threatened to open new territories to slavery, most of its members joined antislavery Whigs and Democrats in forming a new party.",
          "That new party was the Republican Party. For 10 points, name this antislavery party whose first presidential candidate was Martin Van Buren."),
        T("This party drew many New York Democrats nicknamed “Barnburners,” after a story about a farmer who burned down his own barn to get rid of the rats. Their rivals in New York’s Democratic Party were called “Hunkers.”",
          "For 10 points, name this third party that nominated former president Martin Van Buren in 1848."),
        T("Most members of the Liberty Party, which had nominated James G. Birney for president in 1840 and 1844, joined this party in 1848. Unlike the Liberty Party, this party did not call for ending slavery where it already existed.",
          "For 10 points, name this party that opposed the spread of slavery into the western territories."),
        T("Historian Eric Foner took most of this party’s slogan for the title of his 1970 book about the ideas of the early Republican Party. That four-part slogan began with this party’s own name and went on to promise “Free Speech, Free Labor, and Free Men.”",
          "For 10 points, name this antislavery party that ran Martin Van Buren for president in 1848."),
        T("In 1848, this party won about 10 percent of the national popular vote but no electoral votes. Its presidential candidate finished ahead of the Democratic nominee, Lewis Cass, in New York, which helped Zachary Taylor carry that state.",
          "For 10 points, name this third party whose candidate that year was former president Martin Van Buren."),
        T("Antislavery Whigs from Massachusetts, nicknamed “Conscience Whigs,” left their party to help form this one after the Whigs nominated Zachary Taylor, a slaveholding general. Their opponents in the Whig Party were called “Cotton Whigs.”",
          "For 10 points, name this antislavery party founded in 1848, whose first presidential candidate was Martin Van Buren."),
        T("Many members of this party opposed the spread of slavery mainly because they wanted western land kept open for free white farmers and workers. The party also called for free land for western settlers, an idea later carried out by the Homestead Act.",
          "Its first candidate was Martin Van Buren. For 10 points, name this antislavery third party of 1848 to 1854."),
        T("This party’s first presidential candidate had been elected president in 1836 as a Democrat and lost reelection to William Henry Harrison in 1840. That candidate ran again in 1848 on this party’s platform against the spread of slavery into the West.",
          "That candidate was Martin Van Buren. For 10 points, name this third party formed in 1848."),
        T("The 1848 platform of this party answered Southern demands with the words “no more Slave States and no more Slave Territory.” Two years later, senators allied with it, such as Salmon Chase of Ohio, spoke out against the Compromise of 1850.",
          "For 10 points, name this antislavery third party that nominated Martin Van Buren in 1848.")
    ],
    "clues": [
        C("third-party", "giveaway", "Antislavery third party (1848–1854) that fought the spread of slavery into the western territories", ["third party", "spread of slavery", "territories"]),
        C("van-buren", "giveaway", "1848 presidential candidate: former president Martin Van Buren", ["martin van buren", "van buren", "1848"], "Martin Van Buren"),
        C("republicans", "giveaway", "Most members joined the new Republican Party after the Kansas–Nebraska Act (1854)", ["republican party", "kansas–nebraska act", "1854"], "Republican Party"),
        C("wilmot", "giveaway", "Grew out of support for the Wilmot Proviso (1846), which would have banned slavery in land won from Mexico", ["wilmot proviso", "wilmot", "mexico"]),
        C("slogan", "middle", "Slogan: its own name, then “Free Speech, Free Labor, and Free Men”", ["free speech", "free labor", "free men"]),
        C("adams", "middle", "1848 running mate: Charles Francis Adams, son of John Quincy Adams", ["charles francis adams", "john quincy adams"]),
        C("buffalo", "middle", "Founded at a convention in Buffalo, New York, in August 1848", ["buffalo", "convention"]),
        C("coalition", "middle", "Formed by Barnburner Democrats, Conscience Whigs, and most of the Liberty Party", ["barnburner", "conscience whigs", "liberty party"]),
        C("hale", "middle", "1852 presidential candidate: Senator John P. Hale of New Hampshire", ["john p. hale", "hale", "new hampshire"]),
        C("taylor", "middle", "Van Buren split New York’s Democratic vote in 1848, helping Whig Zachary Taylor beat Democrat Lewis Cass", ["zachary taylor", "lewis cass", "new york"]),
        C("ten-percent", "middle", "Won about 10 percent of the popular vote in 1848 but no electoral votes", ["10 percent", "electoral votes"]),
        C("no-abolition", "middle", "Unlike abolitionists, most members did not call for ending slavery where it already existed", ["abolitionists", "already existed"]),
        C("barnburners", "power", "“Barnburners” were named for a farmer who burned his own barn to get rid of the rats; their rivals were “Hunkers”", ["barnburners", "rats", "hunkers"]),
        C("conscience-whigs", "power", "Massachusetts “Conscience Whigs” quit the Whigs after they nominated slaveholding general Zachary Taylor; their foes were “Cotton Whigs”", ["conscience whigs", "cotton whigs"]),
        C("birney", "power", "The Liberty Party had nominated James G. Birney for president in 1840 and 1844", ["james g. birney", "birney"]),
        C("chase", "power", "Salmon P. Chase won a Senate seat from Ohio (1849) with its help; he was later Lincoln’s Secretary of the Treasury", ["salmon p. chase", "chase", "ohio"]),
        C("sumner", "power", "Charles Sumner was elected senator from Massachusetts (1851) by a coalition of its members and Democrats", ["charles sumner", "sumner", "1851"]),
        C("julian", "power", "George Washington Julian of Indiana was Hale’s running mate in 1852", ["george washington julian", "julian", "indiana"]),
        C("five-percent", "power", "Won only about 5 percent of the vote in 1852, its last presidential race", ["5 percent", "1852"]),
        C("foner", "power", "Historian Eric Foner used most of its slogan as the title of his 1970 book on early Republican ideas", ["eric foner", "foner"]),
        C("free-labor", "power", "Many members wanted western land kept for free white farmers and workers; its platform called for free land for settlers", ["white farmers", "free land", "settlers"]),
        C("platform", "power", "1848 platform: “no more Slave States and no more Slave Territory”", ["no more slave states", "slave territory"]),
        C("compromise-1850", "power", "Its allies in Congress, such as Salmon Chase, opposed the Compromise of 1850 and its Fugitive Slave Act", ["compromise of 1850", "fugitive slave act"], "Compromise of 1850"),
        C("van-buren-past", "power", "Van Buren had won the presidency as a Democrat in 1836 and lost to William Henry Harrison in 1840", ["1836", "william henry harrison", "harrison"])
    ],
    "trap": {
        "title": "Liberty, Free Soil, or Republican?",
        "body": "Three antislavery parties came one after another. The Liberty Party ran the abolitionist James G. Birney in 1840 and 1844; the Free Soil Party ran Martin Van Buren in 1848 and John P. Hale in 1852 to stop slavery’s spread west; and the Republican Party, founded in 1854, took in most Free Soilers and elected Abraham Lincoln in 1860. Their clues overlap because many of the same people moved from one party to the next.",
        "fix": "Birney and the early 1840s mean the Liberty Party. Van Buren, Charles Francis Adams, Hale, the Buffalo convention, and the slogan “Free Soil, Free Speech, Free Labor, and Free Men” mean the Free Soil Party. The Kansas–Nebraska Act, Ripon, Frémont, and Lincoln mean the Republicans. Kansas “Free-Staters” were antislavery settlers in Kansas, not this party.",
        "line": "Real answer line: <b><u>Free Soil</u></b> Party (accept <u>Free Soilers</u>; do not accept “Liberty Party” or “Republican Party”)"
    },
    "tests": {
        "right": [
            "Free Soil Party",
            "Free Soilers",
            "Free-Soil",
            "free soil pary",
            "Freesoil Party"
        ],
        "prompt": [],
        "wrong": [
            "Liberty Party",
            "Republican Party",
            "Whig Party",
            "Know-Nothing Party",
            "Free Silver",
            "Democratic Party"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
