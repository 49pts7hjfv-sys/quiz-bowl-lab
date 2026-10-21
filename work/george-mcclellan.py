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
    "id": "george-mcclellan",
    "name": "George McClellan",
    "mono": "GBM",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Union general nicknamed the “Young Napoleon” · Lost to Lincoln in 1864",
    "dates": "1826–1885",
    "briefing": "George McClellan was skilled at building an army: after the Union defeat at Bull Run in 1861, he turned thousands of raw recruits into the well-trained Army of the Potomac, and his soldiers loved him. But he was so cautious that Abraham Lincoln complained he had “the slows.” After McClellan failed to chase Robert E. Lee’s army following Antietam, Lincoln removed him, and in 1864 McClellan ran against Lincoln for president and lost.",
    "answerHtml": "George B. <b><u>McClellan</u></b> (accept George Brinton <u>McClellan</u>; prompt on “Little Mac”)",
    "accept": [
        "george mcclellan",
        "george b mcclellan",
        "george brinton mcclellan",
        "mcclellan",
        "general mcclellan",
        "general george mcclellan",
        "george mcclellan sr",
        "george b mcclellan sr"
    ],
    "prompt": [
        "little mac",
        "young napoleon"
    ],
    "reject": [
        "george b mcclellan jr",
        "george mcclellan jr",
        "mcclellan jr",
        "george meade",
        "meade",
        "ambrose burnside",
        "burnside",
        "joseph hooker",
        "hooker",
        "john pope",
        "irvin mcdowell",
        "mcdowell",
        "winfield scott",
        "henry halleck",
        "halleck",
        "ulysses s grant",
        "robert e lee",
        "abraham lincoln",
        "george pendleton",
        "pendleton",
        "allan pinkerton",
        "pinkerton",
        "fitz john porter",
        "j e b stuart",
        "jeb stuart",
        "stonewall jackson",
        "joseph johnston",
        "john mcclernand",
        "mcclernand",
        "george armstrong custer",
        "george custer",
        "napoleon bonaparte"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/George_B._McClellan",
    "qb": {
        "q": "McClellan",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        T("After observing the Crimean War as part of a U.S. Army commission, this man designed a saddle that the American cavalry used for decades. He left the Army in 1857 to work for the Illinois Central Railroad.",
          "For 10 points, name this Union general who commanded the Army of the Potomac at Antietam."),
        T("Small victories in western Virginia, such as the Battle of Rich Mountain, helped this man win command of Union forces around Washington after the First Battle of Bull Run. That November, he replaced the aging Winfield Scott as general-in-chief.",
          "His soldiers called him “Little Mac.” For 10 points, name this Union general nicknamed the “Young Napoleon.”"),
        T("Confederate general John Magruder fooled this man by marching the same troops back and forth near Yorktown, helping convince him to begin a month-long siege in 1862. This man had moved his army by boat to the Virginia Peninsula to attack Richmond from the east.",
          "This general’s soldiers called him “Little Mac.” For 10 points, name this commander of the Army of the Potomac."),
        T("During this man’s campaign against Richmond, Confederate general Joseph Johnston was wounded at the Battle of Seven Pines, and Robert E. Lee took command of the army facing him. Lee then drove this man away from Richmond in the Seven Days Battles.",
          "For 10 points, name this Union general who later fought Lee again at Antietam."),
        T("Detective Allan Pinkerton ran this general’s spy service and gave him reports that greatly overestimated the size of the Confederate army. Those reports made this general, who already moved slowly, even more cautious.",
          "For 10 points, name this Union general who was removed from command of the Army of the Potomac in November 1862."),
        T("Days before one battle, Union soldiers found a copy of Robert E. Lee’s plans, Special Order 191, wrapped around three cigars, and passed it to this general. Even with that “Lost Order,” this general moved slowly, giving Lee time to gather his scattered army.",
          "He then fought Lee at Antietam. For 10 points, name this commander of the Army of the Potomac."),
        T("During the bloodiest single day in American history, this general kept thousands of soldiers in reserve, including Fitz John Porter’s corps. Afterward, he let Robert E. Lee’s army retreat across the Potomac River into Virginia without chasing it.",
          "For 10 points, name this Union commander at the Battle of Antietam, whom Lincoln removed weeks later."),
        T("When this general complained that his cavalry horses were tired and had sore tongues, Abraham Lincoln asked by telegram what the horses had done since Antietam “that fatigue anything.” Lincoln also complained that this general had “the slows.”",
          "Lincoln removed him from command in November 1862. For 10 points, name this general."),
        T("Confederate cavalry leader J. E. B. Stuart twice led his horsemen in a complete circle around this general’s army, once during the Peninsula Campaign and again weeks after Antietam. The second ride took Stuart as far north as Chambersburg, Pennsylvania.",
          "For 10 points, name this Union general who commanded the Army of the Potomac in 1862."),
        T("In his Harrison’s Landing letter of July 1862, this general advised Abraham Lincoln not to turn the war into a fight to end slavery. Months earlier, he had gone to bed rather than meet Lincoln, who had been waiting at his house.",
          "For 10 points, name this Union general who later ran against Lincoln for president."),
        T("This man ran for president with George Pendleton of Ohio on a platform that called the war a failure, but he rejected that “peace plank” in his letter accepting the nomination. He won only Kentucky, Delaware, and New Jersey.",
          "For 10 points, name this Democrat who lost the 1864 election to Abraham Lincoln."),
        T("This man served as governor of New Jersey from 1878 to 1881, and his son of the same name later served as mayor of New York City. Earlier, the fall of Atlanta in September 1864 hurt this man’s chances of winning the presidency.",
          "For 10 points, name this former Union general who lost to Abraham Lincoln in 1864."),
        T("This man finished second in his West Point class of 1846 and served as an engineer under Winfield Scott in the Mexican-American War. In the 1850s, he helped survey possible routes for a railroad to the Pacific.",
          "For 10 points, name this general who led the Union’s Army of the Potomac in 1861 and 1862."),
        T("This general was criticized for slowly sending help to John Pope before the Second Battle of Bull Run in 1862. After Pope’s defeat, Abraham Lincoln put this general back in charge of the armies around Washington.",
          "For 10 points, name this general who weeks later fought Robert E. Lee at Antietam."),
        T("This general turned the beaten army from First Bull Run into a well-drilled force and was deeply loved by his soldiers. When Abraham Lincoln removed him in November 1862, Ambrose Burnside took his place.",
          "For 10 points, name this first commander of the Army of the Potomac, nicknamed “Little Mac.”")
    ],
    "clues": [
        C("army-of-potomac", "giveaway", "Organized and commanded the Union’s Army of the Potomac early in the Civil War", ["army of the potomac", "potomac"]),
        C("antietam", "giveaway", "Fought Robert E. Lee at Antietam (September 17, 1862)", ["antietam", "robert e. lee"], "Battle of Antietam"),
        C("election-1864", "giveaway", "Democratic nominee who lost the 1864 election to Abraham Lincoln", ["1864", "democratic", "abraham lincoln"], "Abraham Lincoln"),
        C("removed", "giveaway", "Lincoln removed him in November 1862 for being too slow and cautious", ["removed", "november 1862", "cautious"]),
        C("nicknames", "middle", "Nicknamed the “Young Napoleon” and, by his soldiers, “Little Mac”", ["young napoleon", "little mac"]),
        C("peninsula", "middle", "Peninsula Campaign (1862): moved his army by boat toward Richmond, but Lee drove him back in the Seven Days Battles", ["peninsula", "seven days", "richmond"]),
        C("general-in-chief", "middle", "Replaced Winfield Scott as general-in-chief of the Union armies (November 1861)", ["winfield scott", "general-in-chief"]),
        C("slows", "middle", "Lincoln complained that he had “the slows”", ["the slows", "slows"]),
        C("lost-order", "middle", "Received Lee’s “Lost Order” (Special Order 191) before Antietam but still moved slowly", ["lost order", "special order 191"]),
        C("reserves", "middle", "At Antietam, held back thousands of reserve troops and let Lee retreat into Virginia", ["reserve", "retreat"]),
        C("burnside", "middle", "Replaced by Ambrose Burnside, who then lost at Fredericksburg (December 1862)", ["ambrose burnside", "burnside", "fredericksburg"]),
        C("new-jersey", "middle", "Governor of New Jersey (1878–1881)", ["new jersey", "governor"]),
        C("peace-plank", "middle", "1864 running mate: George Pendleton; he rejected his party’s “peace plank,” which called the war a failure", ["pendleton", "peace plank"]),
        C("saddle", "power", "Designed a cavalry saddle, named for him, after observing the Crimean War", ["saddle", "crimean war"]),
        C("railroad", "power", "Left the Army in 1857 to work for the Illinois Central Railroad", ["illinois central", "railroad"]),
        C("west-point", "power", "Second in his West Point class (1846); an engineer in the Mexican-American War", ["west point", "1846", "mexican-american war"], "Mexican-American War"),
        C("pinkerton", "power", "Detective Allan Pinkerton’s spies greatly overestimated Confederate numbers for him", ["allan pinkerton", "pinkerton"]),
        C("magruder", "power", "John Magruder fooled him at Yorktown (1862) by marching troops back and forth", ["magruder", "yorktown"]),
        C("seven-pines", "power", "Joseph Johnston was wounded at Seven Pines (1862), so Robert E. Lee took command of the army facing him", ["seven pines", "joseph johnston"], "Robert E. Lee"),
        C("harrisons-landing", "power", "Harrison’s Landing letter (July 1862): advised Lincoln not to make the war a fight to end slavery", ["harrison’s landing", "letter"]),
        C("stuart", "power", "J. E. B. Stuart rode completely around his army twice in 1862", ["j. e. b. stuart", "stuart"]),
        C("horses", "power", "Lincoln’s telegram asked what his horses had done since Antietam “that fatigue anything”", ["horses", "fatigue", "telegram"]),
        C("snub", "power", "Went to bed rather than meet Lincoln, who was waiting at his house (November 1861)", ["went to bed", "waiting"]),
        C("three-states", "power", "Won only Kentucky, Delaware, and New Jersey in the 1864 election", ["kentucky", "delaware"]),
        C("rich-mountain", "power", "Won small victories in western Virginia, such as Rich Mountain (1861), before taking command in Washington", ["rich mountain", "western virginia"]),
        C("son-mayor", "power", "His son of the same name was mayor of New York City (1904–1909)", ["mayor", "new york city"]),
        C("pope", "power", "Was slow to send help to John Pope before Second Bull Run (1862)", ["john pope", "second bull run"])
    ],
    "trap": {
        "title": "Which Union general?",
        "body": "Abraham Lincoln went through several top generals in the East, and their clues blur together. Irvin McDowell lost at First Bull Run; McClellan led the Peninsula Campaign and fought at Antietam; John Pope lost at Second Bull Run; Ambrose Burnside lost at Fredericksburg; Joseph Hooker lost at Chancellorsville; and George Meade won at Gettysburg.",
        "fix": "“The slows,” the Peninsula Campaign, Pinkerton, the Lost Order, Antietam, and the 1864 Democratic nomination mean McClellan. Fredericksburg means Burnside, Chancellorsville means Hooker, and Gettysburg means Meade. His son, George B. McClellan Jr., a mayor of New York City, is a different person.",
        "line": "Real answer line: George B. <b><u>McClellan</u></b> (accept George Brinton <u>McClellan</u>)"
    },
    "tests": {
        "right": [
            "George McClellan",
            "McClellan",
            "George B. McClellan",
            "General McClellan",
            "George McClelland"
        ],
        "prompt": [
            "Little Mac"
        ],
        "wrong": [
            "George Meade",
            "Ambrose Burnside",
            "Joseph Hooker",
            "Ulysses S. Grant",
            "George McClellan Jr.",
            "Robert E. Lee"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
