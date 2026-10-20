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
    "id": "donner-party",
    "name": "Donner Party",
    "mono": "DP",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Pioneers trapped in the Sierra Nevada snow · The winter of 1846–47",
    "dates": "1846–1847",
    "briefing": "In 1846, the families of George and Jacob Donner and James Reed left Springfield, Illinois, for California, and others joined them along the way. They gambled on a “shortcut” that cost them weeks, and early blizzards trapped them in the Sierra Nevada beside a lake now called Donner Lake. Rescue parties struggled through deep snow all winter, but nearly half of the group died before the last survivor was brought out in April 1847.",
    "answerHtml": "<b><u>Donner Party</u></b> (accept <u>Donner–Reed Party</u>; prompt on <u>Donner</u>)",
    "accept": [
        "donner party",
        "the donner party",
        "donner reed party",
        "donner company",
        "donner wagon train",
        "donner expedition"
    ],
    "prompt": [
        "donner",
        "donners",
        "the donners",
        "donner family",
        "reed party"
    ],
    "reject": [
        "donner pass",
        "donner lake",
        "donner summit",
        "donner memorial state park",
        "oregon trail",
        "california trail",
        "mormon trail",
        "santa fe trail",
        "california gold rush",
        "gold rush",
        "forlorn hope",
        "hastings cutoff",
        "lansford hastings",
        "bidwell bartleson party",
        "stephens townsend murphy party",
        "lewis and clark expedition",
        "mormon pioneers",
        "sutters fort"
    ],
    "tests": {
        "right": [
            "Donner Party",
            "the Donner Party",
            "Doner Party",
            "Donner-Reed Party"
        ],
        "prompt": [
            "Donner",
            "the Donners"
        ],
        "wrong": [
            "Donner Pass",
            "Oregon Trail",
            "Forlorn Hope",
            "Hastings Cutoff",
            "California Gold Rush"
        ]
    },
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Donner_Party",
    "qb": {
        "q": "Donner Party",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        T("In 1847, Mormon pioneers led by Brigham Young followed a rough wagon road that this group had spent weeks cutting through the Wasatch [“WAH-satch”] Mountains the year before. Delays like that one left this group far behind schedule.",
          "For 10 points, name this group of pioneers who were trapped by snow in the Sierra Nevada in the winter of 1846 to 1847."),
        T("When this group reached Fort Bridger in 1846, they learned that the guide they had counted on had already gone ahead with another wagon train. They decided to follow his route anyway, south of the Great Salt Lake.",
          "That guide was Lansford Hastings. For 10 points, name this group that took the Hastings Cutoff and became trapped in the Sierra Nevada."),
        T("At Fort Laramie, the mountain man James Clyman warned one of this group’s leaders, an old friend, not to take a shortcut that had never been tried with wagons. That leader, James Reed, ignored the advice.",
          "For 10 points, name this group of California-bound emigrants who took the Hastings Cutoff and were trapped by snow in 1846."),
        T("This group was formed in July 1846 at the Little Sandy River, in what is now Wyoming, when the families who planned to take a new shortcut chose their own captain. Its leading families had started out from Springfield, Illinois, that April.",
          "For 10 points, name this wagon train, named for its captain, that was trapped in the Sierra Nevada."),
        T("James Reed’s family had to abandon their two-level wagon, later nicknamed the “Pioneer Palace Car,” after most of their oxen were lost crossing a salt desert that proved about twice as wide as promised.",
          "For 10 points, name this group of pioneers whose survivors reached California in 1847 after a winter trapped in the Sierra Nevada."),
        T("Eight-year-old Patty Reed hid a tiny wooden doll in her clothes throughout this group’s ordeal, and it is displayed at Sutter’s Fort in Sacramento. Her father led the second relief party to reach this group.",
          "For 10 points, name this group of pioneers trapped near a lake in the Sierra Nevada in 1846 and 1847."),
        T("Tamsen, the wife of this group’s elected captain, refused to leave her dying husband at their camp on Alder Creek, and she sent her young daughters out with rescuers instead. Neither she nor her husband survived.",
          "For 10 points, name this group of pioneers trapped by snow in the Sierra Nevada on the way to California."),
        T("Patrick Breen kept a diary through the winter that this group spent in crude cabins beside Truckee Lake. His entries record snowstorms, hunger, and prayers for rescue, and his whole family survived.",
          "For 10 points, name this group of pioneers whose winter camp was beside a lake later renamed for them."),
        T("Charles Stanton rode ahead to Sutter’s Fort and returned to this group with mules carrying food in October 1846. Two months later, he died in the mountains while trying to lead a party out on snowshoes.",
          "That party was the Forlorn Hope. For 10 points, name this group of pioneers trapped in the Sierra Nevada."),
        T("In April 1847, the fourth and last relief party found Lewis Keseberg alone at this group’s lake camp, the final survivor to be rescued. Months earlier, the Mexican-American War had pulled many men away from California’s settlements, slowing rescue efforts.",
          "For 10 points, name this group of emigrants trapped in the Sierra Nevada in the winter of 1846 to 1847."),
        T("In January 1847, William Eddy staggered into Johnson’s Ranch to call for help, the first to arrive of the only seven snowshoers who survived the trek out of the mountains. His group had left the lake camp a month earlier.",
          "That group was called the Forlorn Hope. For 10 points, name this group of pioneers trapped by snow in the Sierra Nevada."),
        T("In a May 1847 letter to her cousin, 13-year-old Virginia Reed wrote that she had not told half of their troubles, and she gave this advice: “Never take no cutoffs and hurry along as fast as you can.”",
          "For 10 points, name this group of pioneers whose disastrous shortcut left them trapped in the Sierra Nevada."),
        T("Along the Humboldt River, James Reed killed the teamster John Snyder in a fight, and the rest of this group banished Reed. He rode ahead to California, where he later organized a relief party to rescue his family.",
          "For 10 points, name this group of pioneers trapped by snow in the Sierra Nevada in 1846."),
        T("A statue of a pioneer family at a California state park stands on a base 22 feet tall, said to match the depth of the snow that buried this group’s camp. That park sits beside a lake once called Truckee Lake.",
          "For 10 points, name this group of pioneers trapped in the Sierra Nevada in 1846 and 1847."),
        T("The Central Pacific Railroad and, later, Interstate 80 crossed the Sierra Nevada near a pass named for this group. In 1844, the Stephens–Townsend–Murphy Party had become the first to bring wagons over that pass.",
          "For 10 points, name this group of pioneers who failed to cross the Sierra Nevada before winter snows trapped them in 1846.")
    ],
    "clues": [
        C("sierra-snow", "giveaway",
          "Pioneers trapped by early snow in the Sierra Nevada in the winter of 1846–1847",
          ["sierra nevada", "trapped", "1846"]),
        C("california", "giveaway",
          "A wagon train headed for California, led by the brothers George and Jacob and by James Reed",
          ["california", "wagon train", "james reed"]),
        C("survival", "giveaway",
          "Some of the starving survivors resorted to cannibalism",
          ["cannibalism", "starving"]),
        C("nearly-half", "giveaway",
          "Nearly half of the group died; the survivors reached California in 1847",
          ["nearly half", "1847"]),
        C("hastings-cutoff", "middle",
          "Took the Hastings Cutoff, a “shortcut” promoted by Lansford Hastings that cost them weeks",
          ["hastings cutoff", "lansford hastings", "shortcut"]),
        C("truckee-lake", "middle",
          "Camped in cabins at Truckee Lake, which was later renamed for them, as were a nearby pass and a state park",
          ["truckee lake", "truckee", "renamed"]),
        C("forlorn-hope", "middle",
          "The “Forlorn Hope” left on snowshoes in December 1846 to get help; only seven of the snowshoers made it out",
          ["forlorn hope", "snowshoes", "december 1846"]),
        C("reed-banished", "middle",
          "Along the Humboldt River, James Reed was banished after killing teamster John Snyder in a fight; he later led a relief party",
          ["banished", "john snyder", "humboldt"]),
        C("relief", "middle",
          "Four relief parties from Sutter’s Fort and other California settlements reached them between February and April 1847",
          ["relief parties", "relief", "sutter’s fort"]),
        C("salt-desert", "middle",
          "Lost many oxen crossing the Great Salt Lake Desert, about twice as wide as Hastings had claimed",
          ["great salt lake desert", "salt", "oxen"]),
        C("never-cutoffs", "middle",
          "Virginia Reed’s 1847 letter: “Never take no cutoffs and hurry along as fast as you can”",
          ["virginia reed", "never take no cutoffs", "cutoffs"]),
        C("springfield", "middle",
          "Its leading families left Springfield, Illinois, in April 1846",
          ["springfield", "illinois", "april 1846"]),
        C("wasatch", "power",
          "Spent weeks cutting a wagon road through the Wasatch Mountains; Mormon pioneers used it in 1847",
          ["wasatch", "mormon", "wagon road"]),
        C("fort-bridger", "power",
          "At Fort Bridger they learned that Hastings had already gone ahead with another wagon train",
          ["fort bridger", "bridger"]),
        C("clyman", "power",
          "Mountain man James Clyman warned James Reed at Fort Laramie not to take the cutoff",
          ["james clyman", "clyman", "fort laramie"]),
        C("little-sandy", "power",
          "Formed in July 1846 at the Little Sandy River (in today’s Wyoming), where George was elected captain",
          ["little sandy", "wyoming", "captain"]),
        C("palace-car", "power",
          "The Reeds abandoned their two-level wagon, nicknamed the “Pioneer Palace Car,” in the salt desert",
          ["pioneer palace car", "palace car", "two-level"]),
        C("patty-doll", "power",
          "Eight-year-old Patty Reed’s tiny wooden doll survived the journey and is displayed at Sutter’s Fort",
          ["patty reed", "doll"]),
        C("tamsen", "power",
          "Tamsen, the captain’s wife, stayed with her dying husband at Alder Creek instead of leaving with rescuers",
          ["tamsen", "alder creek"]),
        C("breen", "power",
          "Patrick Breen kept a diary at the lake camp; his whole family survived",
          ["patrick breen", "breen", "diary"]),
        C("stanton", "power",
          "Charles Stanton brought mules loaded with food from Sutter’s Fort, then died with the Forlorn Hope",
          ["charles stanton", "stanton", "mules"]),
        C("eddy", "power",
          "William Eddy reached Johnson’s Ranch in January 1847, the first of the Forlorn Hope survivors to get there",
          ["william eddy", "eddy", "johnson’s ranch"]),
        C("keseberg", "power",
          "Lewis Keseberg was the last survivor rescued, in April 1847; the Mexican-American War had slowed the rescues",
          ["keseberg", "april 1847", "mexican-american war"]),
        C("monument", "power",
          "A pioneer statue near the lake stands on a 22-foot base, the reported depth of that winter’s snow",
          ["22-foot", "pioneer", "statue"]),
        C("railroad", "power",
          "The Central Pacific Railroad and Interstate 80 later crossed the Sierra near the pass named for them",
          ["central pacific", "interstate 80", "pass"]),
        C("stephens-1844", "power",
          "The Stephens–Townsend–Murphy Party had first taken wagons over that pass in 1844",
          ["stephens–townsend–murphy", "1844", "wagons"])
    ],
    "trap": {
        "title": "Party, pass, or trail?",
        "body": "Several places are named for this group, including Donner Lake, Donner Pass, and Donner Memorial State Park, so make sure the question wants the people. Other questions about westward travel want the Oregon Trail or the California Trail, which the Donner Party was following before it took the Hastings Cutoff, and some ask for that “shortcut” itself or for the snowshoe group called the Forlorn Hope.",
        "fix": "“This group,” “this party,” or “these emigrants” means the Donner Party. “This pass” means Donner Pass, and “this route” or “this shortcut” may mean the Hastings Cutoff. Clues about Oregon’s Willamette Valley or the Whitman Mission point to the Oregon Trail.",
        "line": "Real answer line: <b><u>Donner Party</u></b> (accept <u>Donner–Reed Party</u>; prompt on <u>Donner</u>)"
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
