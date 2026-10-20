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
    "id": "emancipation-proclamation",
    "name": "Emancipation Proclamation",
    "mono": "EP",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Lincoln’s order freeing enslaved people · Took effect January 1, 1863",
    "dates": "Took effect January 1, 1863",
    "briefing": "On New Year’s Day 1863, Abraham Lincoln signed an order declaring that enslaved people in the states rebelling against the Union “are, and henceforward shall be free.” Because it applied only to areas the Confederacy controlled, freedom often arrived only when Union soldiers did. The order also let Black men join the Union Army and Navy, and nearly 200,000 served before the war ended.",
    "answerHtml": "<b><u>Emancipation Proclamation</u></b> (prompt on <u>emancipation</u> or <u>proclamation</u>; do not accept “Thirteenth Amendment”)",
    "accept": [
        "emancipation proclamation",
        "the emancipation proclamation",
        "preliminary emancipation proclamation",
        "final emancipation proclamation"
    ],
    "prompt": [
        "emancipation",
        "proclamation",
        "the proclamation",
        "emancipation order",
        "lincolns proclamation"
    ],
    "reject": [
        "thirteenth amendment",
        "13th amendment",
        "fourteenth amendment",
        "14th amendment",
        "gettysburg address",
        "juneteenth",
        "general order no 3",
        "general order number 3",
        "general order 3",
        "confiscation act",
        "confiscation acts",
        "second confiscation act",
        "emancipation manifesto",
        "emancipation edict",
        "emancipation reform",
        "emancipation of the serfs",
        "emancipation act",
        "slavery abolition act",
        "compensated emancipation act",
        "proclamation of 1763",
        "proclamation of neutrality",
        "neutrality proclamation",
        "proclamation of amnesty and reconstruction",
        "ten percent plan",
        "wade davis bill",
        "declaration of independence",
        "freedmens bureau",
        "civil rights act of 1866"
    ],
    "tests": {
        "right": [
            "Emancipation Proclamation",
            "the Emancipation Proclamation",
            "Emancipation Proclomation",
            "Preliminary Emancipation Proclamation"
        ],
        "prompt": [
            "Emancipation",
            "Proclamation"
        ],
        "wrong": [
            "Thirteenth Amendment",
            "13th Amendment",
            "Gettysburg Address",
            "Juneteenth",
            "Emancipation Manifesto",
            "Confiscation Act"
        ]
    },
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Emancipation_Proclamation",
    "qb": {
        "q": "Emancipation Proclamation",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        T("On July 22, 1862, the President read a draft of this document to his cabinet, and Secretary of State William Seward advised waiting to issue it until the Union won a major victory. That victory came two months later in Maryland.",
          "Five days after the Battle of Antietam, Abraham Lincoln announced this order. For 10 points, name this document that took effect on January 1, 1863."),
        T("A month before announcing this order, its author replied to Horace Greeley’s editorial “The Prayer of Twenty Millions” by writing, “If I could save the Union without freeing any slave I would do it.” He had already drafted this order by then.",
          "For 10 points, name this order by Abraham Lincoln that declared enslaved people in the rebelling states to be free."),
        T("Francis Bicknell Carpenter spent six months at the White House painting the President and his cabinet at the first reading of this document. That 1864 painting hangs in the U.S. Capitol, and Carpenter later wrote a book about his stay.",
          "For 10 points, name this order, issued by Abraham Lincoln, that took effect on January 1, 1863."),
        T("On December 31, 1862, many Black churches held “Watch Night” services, staying up past midnight in prayer and celebration. In Boston, Frederick Douglass waited with a crowd at Tremont Temple for word from Washington.",
          "They were waiting for this order to take effect. For 10 points, name this order by Abraham Lincoln that freed enslaved people in the rebelling states."),
        T("In 1861 and 1862, the President overruled generals John C. Frémont [“FREE-mont”] and David Hunter, who had each declared enslaved people free in areas under their command. He later issued his own order as a war measure, using his powers as commander in chief.",
          "For 10 points, name this order that Abraham Lincoln issued after the Battle of Antietam."),
        T("In April 1862, Congress freed enslaved people in Washington, D.C., and paid their owners, months before the President issued this broader order. That summer, the Second Confiscation Act declared free any enslaved people of rebel owners who escaped to Union lines.",
          "For 10 points, name this order, announced in September 1862, that took effect on January 1, 1863."),
        T("After shaking hands for hours at a White House reception, the President worried that his tired hand would make his signature on this document look shaky. As he signed, he reportedly said, “If my name ever goes into history it will be for this act.”",
          "It applied only to areas in rebellion. For 10 points, name this order that Abraham Lincoln signed on January 1, 1863."),
        T("The original of this document, five pages long, is kept at the National Archives in Washington, D.C. Because light can damage it, it is shown to the public for only a few days each year.",
          "For 10 points, name this 1863 order by Abraham Lincoln that freed enslaved people in Confederate-held areas."),
        T("This order exempted Tennessee, the 48 counties that became West Virginia, and Union-held parts of Louisiana and Virginia, including New Orleans and Norfolk. Its preliminary version had given the rebelling states about 100 days to rejoin the Union.",
          "It also did not apply in the border states. For 10 points, name this 1863 order by Abraham Lincoln."),
        T("This order ends by calling itself “an act of justice, warranted by the Constitution, upon military necessity,” and asks for “the considerate judgment of mankind, and the gracious favor of Almighty God.”",
          "Abraham Lincoln issued it as a war measure. For 10 points, name this order that took effect on January 1, 1863."),
        T("After this order took effect, Frederick Douglass published the call “Men of Color, To Arms!” and helped recruit soldiers for the 54th Massachusetts, in which two of his sons served.",
          "This order let Black men join the Union Army and Navy. For 10 points, name this order issued by Abraham Lincoln."),
        T("On June 19, 1865, Union general Gordon Granger arrived in Galveston, Texas, and issued General Order No. 3, announcing that all enslaved people in Texas were free under this earlier order. That day is remembered as Juneteenth.",
          "Juneteenth became a federal holiday in 2021. For 10 points, name this order by Abraham Lincoln that took effect on January 1, 1863."),
        T("Cotton workers in Manchester, England, sent the President a letter praising this order even though a cotton shortage caused by the war had left many of them out of work. He wrote back to thank them.",
          "This order made Britain and France less likely to back the Confederacy. For 10 points, name this order announced after the Battle of Antietam."),
        T("The preliminary version of this order warned that enslaved people in any state still rebelling on a set date “shall be then, thenceforward, and forever free.” It also repeated the President’s offer of money to loyal states that chose to end slavery themselves.",
          "That version came five days after the Battle of Antietam. For 10 points, name this order by Abraham Lincoln."),
        T("The final version of this order declared that enslaved people in the listed areas “are, and henceforward shall be free,” and that freed men would be received into the armed service of the United States to garrison forts and to man ships.",
          "Nearly 200,000 Black men served in the Union Army and Navy by the war’s end. For 10 points, name this order signed by Abraham Lincoln on January 1, 1863.")
    ],
    "clues": [
        C("lincoln-order", "giveaway",
          "Abraham Lincoln’s order declaring enslaved people in the rebelling Confederate states free",
          ["abraham lincoln", "lincoln", "rebelling", "free"], "Abraham Lincoln"),
        C("jan-1-1863", "giveaway",
          "Took effect on January 1, 1863",
          ["january 1, 1863", "january 1", "1863"]),
        C("antietam", "giveaway",
          "Announced in preliminary form on September 22, 1862, five days after the Battle of Antietam",
          ["antietam", "september 22", "preliminary"], "Battle of Antietam"),
        C("confederate-only", "giveaway",
          "Applied only to areas in rebellion, not to the loyal border states such as Kentucky and Maryland",
          ["border states", "rebellion", "kentucky", "maryland"]),
        C("war-measure", "middle",
          "Issued as a “war measure” under Lincoln’s power as commander in chief",
          ["war measure", "commander in chief"]),
        C("black-soldiers", "middle",
          "Let Black men join the Union Army and Navy; nearly 200,000 served by the war’s end",
          ["black men", "army and navy", "200,000"]),
        C("thirteenth", "middle",
          "Did not end slavery everywhere; the 13th Amendment (ratified December 1865) did",
          ["13th amendment", "thirteenth", "december 1865"]),
        C("juneteenth", "middle",
          "Juneteenth: on June 19, 1865, General Gordon Granger announced in Galveston that all enslaved people in Texas were free",
          ["juneteenth", "gordon granger", "galveston", "june 19"]),
        C("britain-france", "middle",
          "Made the war a fight against slavery, so Britain and France were less likely to back the Confederacy",
          ["britain", "france", "against slavery"]),
        C("seward", "middle",
          "Secretary of State William Seward advised waiting for a Union victory before announcing it",
          ["william seward", "seward", "victory"]),
        C("july-22", "power",
          "Lincoln first read a draft to his cabinet on July 22, 1862",
          ["july 22", "cabinet", "draft"]),
        C("greeley", "power",
          "Lincoln answered Horace Greeley’s “The Prayer of Twenty Millions”: “If I could save the Union without freeing any slave I would do it”",
          ["horace greeley", "greeley", "prayer of twenty millions"]),
        C("carpenter", "power",
          "Francis Bicknell Carpenter’s 1864 painting of the first reading hangs in the U.S. Capitol",
          ["carpenter", "painting", "capitol"]),
        C("watch-night", "power",
          "Black churches held “Watch Night” services on December 31, 1862; Frederick Douglass waited at Boston’s Tremont Temple",
          ["watch night", "tremont temple", "december 31"]),
        C("fremont-hunter", "power",
          "Lincoln had overruled freedom orders by generals John C. Frémont (1861) and David Hunter (1862)",
          ["frémont", "david hunter", "hunter"]),
        C("dc-confiscation", "power",
          "Came after Congress freed enslaved people in Washington, D.C. (April 1862) and passed the Second Confiscation Act (July 1862)",
          ["confiscation act", "washington, d.c.", "april 1862"]),
        C("history-quote", "power",
          "As Lincoln signed it, he reportedly said, “If my name ever goes into history it will be for this act”",
          ["goes into history", "signed", "history"]),
        C("archives", "power",
          "The five-page original is kept at the National Archives and shown only a few days a year",
          ["national archives", "five-page"]),
        C("considerate", "power",
          "Ends: “I invoke the considerate judgment of mankind, and the gracious favor of Almighty God”",
          ["considerate judgment", "almighty god"]),
        C("henceforward", "power",
          "Declared enslaved people in the listed areas “are, and henceforward shall be free”; the preliminary said “thenceforward, and forever free”",
          ["henceforward", "thenceforward", "forever free"]),
        C("exemptions", "power",
          "Exempted Tennessee, the counties that became West Virginia, and Union-held parts of Louisiana and Virginia",
          ["tennessee", "west virginia", "exempted"]),
        C("hundred-days", "power",
          "The preliminary version gave the rebelling states about 100 days to rejoin the Union",
          ["100 days", "rejoin"]),
        C("manchester", "power",
          "Lincoln thanked the cotton workers of Manchester, England, who supported it even though the cotton shortage cost many their jobs",
          ["manchester", "cotton workers", "cotton"]),
        C("douglass", "power",
          "Frederick Douglass urged “Men of Color, To Arms!” and recruited for the 54th Massachusetts, where two of his sons served",
          ["men of color", "54th massachusetts", "frederick douglass"], "Frederick Douglass")
    ],
    "trap": {
        "title": "Proclamation or amendment?",
        "body": "The Emancipation Proclamation (1863) was a wartime order by Lincoln that freed enslaved people only in areas still in rebellion. The Thirteenth Amendment (ratified 1865) abolished slavery everywhere in the United States, so naming one for the other loses the tossup. Juneteenth, the Gettysburg Address, and the Confiscation Acts share clues with it too, and Russia’s 1861 Emancipation Manifesto freed serfs, not enslaved Americans.",
        "fix": "Listen for the type of thing: “this order,” “this proclamation,” or “this document” issued by Lincoln in 1862 or 1863 means the Emancipation Proclamation; “this amendment” ratified in 1865 means the Thirteenth Amendment. A date of June 19, 1865, means Juneteenth.",
        "line": "Real answer line: <b><u>Emancipation Proclamation</u></b> (prompt on <u>emancipation</u> or <u>proclamation</u>; do not accept “Thirteenth Amendment”)"
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
