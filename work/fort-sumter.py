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
    "id": "fort-sumter",
    "name": "Fort Sumter",
    "mono": "FTS",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Charleston Harbor fort · Where the Civil War began in April 1861",
    "dates": "Attacked April 12–13, 1861",
    "briefing": "Fort Sumter stood on a man-made island guarding the harbor of Charleston, South Carolina. After South Carolina left the Union, Major Robert Anderson and fewer than a hundred U.S. soldiers held the unfinished fort. At 4:30 a.m. on April 12, 1861, Confederate cannons opened fire, and after 34 hours Anderson surrendered. Nobody was killed by the bombardment itself, but it started the Civil War.",
    "answerHtml": "Fort <b><u>Sumter</u></b> (accept Battle of Fort <u>Sumter</u>; prompt on <u>Charleston</u> Harbor)",
    "accept": [
        "fort sumter",
        "sumter",
        "battle of fort sumter",
        "fort sumpter",
        "ft sumter"
    ],
    "prompt": [
        "charleston",
        "charleston harbor",
        "charleston south carolina"
    ],
    "reject": [
        "fort moultrie",
        "moultrie",
        "fort mchenry",
        "fort pickens",
        "fort wagner",
        "battery wagner",
        "fort pulaski",
        "fort monroe",
        "fort ticonderoga",
        "fort necessity",
        "fort sumner",
        "sumner",
        "charles sumner",
        "thomas sumter",
        "fort johnson",
        "castle pinckney",
        "fort donelson",
        "fort henry",
        "fort fisher",
        "first battle of bull run",
        "bull run",
        "the citadel",
        "star of the west",
        "sumer",
        "sumerians",
        "summer"
    ],
    "tests": {
        "right": [
            "Fort Sumter",
            "Sumter",
            "Fort Sumpter",
            "Battle of Fort Sumter",
            "Ft. Sumter"
        ],
        "prompt": [
            "Charleston",
            "Charleston Harbor"
        ],
        "wrong": [
            "Fort Moultrie",
            "Fort McHenry",
            "Fort Sumner",
            "Fort Pickens",
            "Charles Sumner",
            "Fort Wagner"
        ]
    },
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Fort_Sumter",
    "qb": {
        "q": "Sumter",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        T("Construction of this fort began in 1829 on a man-made island built from tons of granite and other rock, and it was still unfinished more than thirty years later. Its walls were designed to hold more than a hundred cannons.",
          "Robert Anderson commanded this fort in 1861. For 10 points, name this fort in Charleston Harbor where the Civil War began."),
        T("This fort was named for a South Carolina general of the Revolutionary War nicknamed “the Carolina Gamecock.” It was built after the War of 1812 to guard the entrance to an important Southern harbor.",
          "Confederate guns attacked it on April 12, 1861. For 10 points, name this fort in Charleston Harbor."),
        T("Six days after South Carolina seceded, the commander of the U.S. Army post there secretly moved his men to this fort from Fort Moultrie [“MOOL-tree”], which could easily be attacked from land. He moved them at night, on December 26, 1860.",
          "That commander was Major Robert Anderson. For 10 points, name this fort where the Civil War began."),
        T("In January 1861, cadets from The Citadel fired on the _Star of the West_, an unarmed merchant ship carrying soldiers and supplies to this fort, and the ship turned back. President James Buchanan had sent that ship.",
          "Three months later, Confederate cannons fired on this fort. For 10 points, name this fort in Charleston Harbor."),
        T("In April 1861, President Lincoln informed South Carolina governor Francis Pickens that he would send only food, not soldiers or weapons, to this fort’s hungry garrison. Confederate leaders decided to attack before the supplies arrived.",
          "General P. G. T. Beauregard [“BOH-ruh-gard”] then ordered the bombardment. For 10 points, name this fort where the Civil War began."),
        T("Gustavus Fox led a relief fleet that arrived outside the harbor during the attack on this fort, but it could not reach the fort in time to help. Fox later became assistant secretary of the navy.",
          "For 10 points, name this fort in Charleston Harbor where the Civil War began in April 1861."),
        T("The Confederate general who ordered the attack on this fort had once studied artillery at West Point under the Union officer defending it, and later served as his assistant there. That Union officer was a Kentucky native.",
          "Those men were P. G. T. Beauregard [“BOH-ruh-gard”] and Robert Anderson. For 10 points, name this fort where the Civil War began."),
        T("At 4:30 a.m., a signal shell fired from Fort Johnson burst over this fort, starting a bombardment. The Virginia secessionist Edmund Ruffin is often said to have fired one of the first shots that followed.",
          "For 10 points, name this fort attacked on April 12, 1861, at the start of the Civil War."),
        T("Mary Chesnut wrote in her diary that she knelt and prayed when the guns began firing at this fort, then watched from a rooftop in the nearby city. Her husband, James, was one of the aides who carried the demand that the fort surrender.",
          "For 10 points, name this fort in Charleston Harbor whose bombardment began the Civil War."),
        T("Captain Abner Doubleday, who was later wrongly credited with inventing baseball, aimed the first shot fired back by the defenders of this fort. The garrison was running out of food and could use only some of its cannons.",
          "For 10 points, name this fort that surrendered after a 34-hour bombardment in April 1861."),
        T("During a salute to the U.S. flag after this fort surrendered, a pile of cartridges blew up by accident, killing Private Daniel Hough. Not one person had died during the 34-hour bombardment before the surrender.",
          "Hough is often called the first soldier to die in the Civil War. For 10 points, name this fort in Charleston Harbor."),
        T("Three days after the attack on this fort began, Abraham Lincoln called for 75,000 volunteers to put down the rebellion. That call led Virginia, Arkansas, North Carolina, and Tennessee to leave the Union.",
          "For 10 points, name this fort in Charleston Harbor that Confederates captured at the start of the Civil War."),
        T("In April 1863, Union ironclads under Samuel Du Pont failed to capture this fort, and later Union guns pounded it into rubble. Confederates held it until February 1865, when they abandoned the nearby city as William Tecumseh Sherman’s army marched through South Carolina.",
          "For 10 points, name this fort where the Civil War had begun almost four years earlier."),
        T("On April 14, 1865, Henry Ward Beecher gave a speech as this fort’s former commander raised over it the same flag he had lowered exactly four years earlier. That night, Abraham Lincoln was shot at Ford’s Theatre.",
          "That commander was Robert Anderson. For 10 points, name this fort in Charleston Harbor."),
        T("The day after U.S. troops secretly moved into this fort, South Carolina militia seized Castle Pinckney and the abandoned Fort Moultrie [“MOOL-tree”] nearby. Over the next months, Southern troops built gun batteries around the harbor aimed at this fort.",
          "For 10 points, name this fort in Charleston Harbor where the first shots of the Civil War were fired.")
    ],
    "clues": [
        C("first-shots", "giveaway",
          "Where the first shots of the Civil War were fired, on April 12, 1861",
          ["first shots", "civil war", "april 12, 1861"], "American Civil War"),
        C("charleston", "giveaway",
          "A fort on a man-made island in the harbor of Charleston, South Carolina",
          ["charleston", "south carolina", "harbor", "island"]),
        C("anderson", "giveaway",
          "Major Robert Anderson commanded its U.S. garrison and surrendered on April 13, 1861",
          ["robert anderson", "anderson", "surrendered", "april 13"]),
        C("beauregard", "giveaway",
          "Confederate General P. G. T. Beauregard ordered the bombardment",
          ["beauregard", "bombardment"]),
        C("moultrie", "middle",
          "On December 26, 1860, six days after South Carolina seceded, Anderson secretly moved his men there from Fort Moultrie",
          ["fort moultrie", "moultrie", "december 26"]),
        C("star-of-the-west", "middle",
          "In January 1861, cadets from The Citadel fired on the _Star of the West_, a supply ship sent by President James Buchanan",
          ["star of the west", "citadel", "buchanan"]),
        C("34-hours", "middle",
          "The bombardment lasted 34 hours, and no one was killed by enemy fire",
          ["34 hours", "enemy fire"]),
        C("volunteers", "middle",
          "Three days after the attack began, Lincoln called for 75,000 volunteers, and four more states seceded",
          ["75,000", "volunteers", "four more states"]),
        C("gamecock", "middle",
          "Named for a Revolutionary War general nicknamed “the Carolina Gamecock”",
          ["carolina gamecock", "gamecock", "revolutionary war"]),
        C("pickens", "middle",
          "Lincoln told South Carolina governor Francis Pickens he would send only food; Confederate leaders chose to attack first",
          ["francis pickens", "pickens", "food"]),
        C("flag-1865", "middle",
          "Anderson raised the same flag over it on April 14, 1865, the day Lincoln was shot",
          ["same flag", "april 14, 1865", "flag"]),
        C("construction", "power",
          "Construction began in 1829 on a man-made island of granite and other rock; it was still unfinished in 1861",
          ["1829", "granite", "unfinished"]),
        C("fox", "power",
          "Gustavus Fox’s relief fleet arrived during the attack but could not reach the fort",
          ["gustavus fox", "fox", "relief fleet"]),
        C("west-point", "power",
          "Beauregard had studied artillery under Anderson at West Point and later served as his assistant",
          ["west point", "artillery", "assistant"]),
        C("fort-johnson", "power",
          "The attack began at 4:30 a.m. with a signal shell fired from Fort Johnson",
          ["fort johnson", "signal shell", "4:30"]),
        C("ruffin", "power",
          "Virginia secessionist Edmund Ruffin is often said to have fired one of the first shots",
          ["edmund ruffin", "ruffin"]),
        C("chesnut", "power",
          "Mary Chesnut described the bombardment in her diary; her husband, James, helped carry the surrender demand",
          ["mary chesnut", "chesnut", "diary"]),
        C("doubleday", "power",
          "Captain Abner Doubleday, wrongly credited with inventing baseball, aimed the first shot fired back",
          ["abner doubleday", "doubleday", "baseball"]),
        C("hough", "power",
          "Private Daniel Hough died in an accidental explosion during a salute after the surrender",
          ["daniel hough", "hough", "salute"]),
        C("du-pont", "power",
          "Union ironclads under Samuel Du Pont failed to retake it in April 1863",
          ["du pont", "ironclads", "april 1863"]),
        C("rubble", "power",
          "Union guns pounded it into rubble, but Confederates held it until February 1865",
          ["rubble", "february 1865"]),
        C("beecher", "power",
          "Henry Ward Beecher gave the speech at the April 1865 flag-raising ceremony",
          ["henry ward beecher", "beecher"]),
        C("castle-pinckney", "power",
          "The day after Anderson moved in, South Carolina militia seized Castle Pinckney and Fort Moultrie",
          ["castle pinckney", "militia"])
    ],
    "trap": {
        "title": "Sumter, not Moultrie or McHenry",
        "body": "Charleston Harbor had several forts. Robert Anderson’s men started out at Fort Moultrie and moved to Fort Sumter in December 1860, and Confederate guns at Moultrie and Fort Johnson later fired on Sumter. Players also mix up Fort Sumter (1861, the Civil War) with Fort McHenry (1814, the War of 1812 and “The Star-Spangled Banner”) and with Fort Sumner in New Mexico, where Navajo people were held after the Long Walk.",
        "fix": "The Civil War, April 1861, Anderson, and Beauregard mean Sumter. The War of 1812 and the national anthem mean McHenry. If a clue says troops moved out of a fort in December 1860, that fort was Moultrie; the fort they moved into is Sumter.",
        "line": "Real answer line: Fort <b><u>Sumter</u></b> (accept Battle of Fort <u>Sumter</u>; prompt on <u>Charleston</u> Harbor)"
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
