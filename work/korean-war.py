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
    "id": "korean-war",
    "name": "Korean War",
    "mono": "KW",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Cold War fight on the Korean Peninsula · Ended by a 1953 armistice",
    "dates": "Fought 1950–1953",
    "briefing": "On June 25, 1950, North Korean troops crossed the 38th parallel into South Korea, and the United Nations sent an army, led mostly by Americans, to stop them. After a surprise landing at Inchon, a huge Chinese counterattack, and two more years of grinding battles near the old border, an armistice in July 1953 stopped the fighting. No peace treaty was ever signed, and Americans often call it the “Forgotten War.”",
    "answerHtml": "<b><u>Korean War</u></b> (accept <u>Korean Conflict</u> or <u>6–25 War</u>; prompt on <u>Korea</u> or “police action”; do not accept “Vietnam War”)",
    "accept": [
        "korean war",
        "the korean war",
        "korean conflict",
        "the korean conflict",
        "korea war",
        "war in korea",
        "korean war of 1950",
        "6 25 war",
        "625 war",
        "six two five war",
        "fatherland liberation war",
        "war to resist america and aid korea",
        "war to resist us aggression and aid korea"
    ],
    "prompt": [
        "korea",
        "police action",
        "korean police action",
        "forgotten war",
        "the forgotten war"
    ],
    "reject": [
        "vietnam war",
        "vietnam",
        "second indochina war",
        "first indochina war",
        "indochina war",
        "cold war",
        "world war ii",
        "world war 2",
        "second world war",
        "world war i",
        "world war 1",
        "first world war",
        "chinese civil war",
        "gulf war",
        "persian gulf war",
        "war of 1812",
        "spanish american war",
        "mexican american war",
        "battle of inchon",
        "inchon",
        "inchon landing",
        "incheon",
        "operation chromite",
        "battle of chosin reservoir",
        "chosin reservoir",
        "chosin",
        "pusan perimeter",
        "battle of pork chop hill",
        "pork chop hill",
        "heartbreak ridge",
        "38th parallel",
        "korean demilitarized zone",
        "demilitarized zone",
        "dmz",
        "panmunjom",
        "korean armistice agreement",
        "armistice",
        "north korea",
        "south korea",
        "douglas macarthur",
        "macarthur",
        "harry truman",
        "harry s truman",
        "truman",
        "dwight eisenhower",
        "dwight d eisenhower",
        "eisenhower",
        "kim il sung",
        "syngman rhee",
        "mash",
        "m a s h"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Korean_War",
    "qb": {
        "q": "Korean War",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        T("In August 1945, two American colonels, Dean Rusk and Charles Bonesteel, used a National Geographic map to choose a line dividing a peninsula into American and Soviet occupation zones. Five years later, troops from the northern zone crossed that line, starting this war.",
          "That line was the 38th parallel. For 10 points, name this war that began in June 1950."),
        T("The Soviet Union could not veto a key Security Council vote at the start of this war because it was boycotting the council to protest Taiwan’s government holding China’s seat. Sixteen countries eventually sent combat troops to fight under the United Nations flag in this war.",
          "For 10 points, name this war in which UN forces defended South Korea from 1950 to 1953."),
        T("The first American ground troops to fight in this war, a small unit called Task Force Smith, were overrun at Osan in July 1950. By August, the defenders had been pushed into a small corner around the port of Pusan [“POO-sahn”], where they held a line called the Pusan Perimeter.",
          "The invaders had come from North Korea that June. For 10 points, name this war that lasted until 1953."),
        T("Some officers warned that one port’s enormous tides and high seawalls made it a terrible place for a landing, but Operation Chromite went ahead there on September 15, 1950. That surprise amphibious attack cut the invaders’ supply lines and led to the recapture of Seoul about two weeks later.",
          "Douglas MacArthur planned that landing at Inchon. For 10 points, name this war, fought from 1950 to 1953."),
        T("American F-86 Sabre jets battled Soviet-built MiG-15s over an area near the Yalu River nicknamed “MiG Alley” during this war. In October 1950, Chinese troops under Peng Dehuai [“PUNG duh-HWY”] secretly crossed that river and soon launched huge attacks on UN forces.",
          "For 10 points, name this war in which China fought on the side of North Korea."),
        T("U.S. Marines who fought their way out after Chinese troops surrounded them in bitter, below-zero cold in late 1950 became known as the “Chosin Few.” Afterward, ships carried about 100,000 soldiers and nearly as many civilians away from the port of Hungnam [“HOONG-nahm”].",
          "That fight was the Battle of Chosin Reservoir. For 10 points, name this war that ended in 1953."),
        T("In December 1950, Jesse L. Brown, the first African American pilot to complete the U.S. Navy’s flight training program, was shot down near the Chosin Reservoir and died. His wingman, Thomas Hudner, crash-landed his own plane in an attempt to rescue him and received the Medal of Honor.",
          "For 10 points, name this war in which UN forces fought North Korean and Chinese troops from 1950 to 1953."),
        T("House Republican leader Joseph Martin read aloud a letter in which a general in this war wrote that “there is no substitute for victory.” Days later, in April 1951, that general was removed from command for publicly challenging the president’s policy.",
          "That general was Douglas MacArthur, and the president who fired him was Harry Truman. For 10 points, name this war."),
        T("Omar Bradley warned that carrying this war into China itself would mean fighting “the wrong war, at the wrong place, at the wrong time, and with the wrong enemy.” Matthew Ridgway, who had taken over the Eighth Army, replaced the fired commander of UN forces in this war.",
          "That fired commander was Douglas MacArthur. For 10 points, name this war that began in June 1950 and ended in 1953."),
        T("Truce talks in this war began at Kaesong [“KAY-sung”] in July 1951 and later moved to Panmunjom [“pahn-moon-JUM”], where they dragged on for two years, mostly over whether prisoners of war could refuse to go home. Syngman Rhee [“SING-mun REE”], who wanted to keep fighting, refused to sign the agreement that finally stopped it.",
          "That armistice was signed on July 27, 1953. For 10 points, name this war, which ended without a peace treaty."),
        T("During the 1952 presidential campaign, Dwight Eisenhower promised to travel to the front lines of this war, a trip he made that December. After he took office and Joseph Stalin died in March 1953, negotiators finally reached a deal to stop the fighting.",
          "Eisenhower had told voters, “I shall go to Korea.” For 10 points, name this war, ended by an armistice in 1953."),
        T("Gregory Peck starred in a 1959 film about the fight for Pork Chop Hill, one of many costly battles over hilltops during this war’s last two years. Other hard-fought battles in this war took place at Heartbreak Ridge and Bloody Ridge, close to the old dividing line.",
          "That line was the 38th parallel. For 10 points, name this war that ended in 1953."),
        T("The final episode of a TV comedy set in this war, “Goodbye, Farewell and Amen,” became the most-watched broadcast in American television history up to that time when it aired in 1983. That series followed Hawkeye Pierce and other doctors at the 4077th Mobile Army Surgical Hospital.",
          "That show, _M*A*S*H_, ran for 11 seasons. For 10 points, name this war in which it was set."),
        T("A memorial on the National Mall, dedicated in 1995, shows 19 stainless steel soldiers in rain ponchos walking through a field, and a polished granite wall reflects them to make 38. Nearby, a line carved in stone reads “Freedom Is Not Free.”",
          "For 10 points, name this war, often called the “Forgotten War,” whose memorial stands near the Lincoln Memorial."),
        T("A small mare named Reckless carried ammunition for U.S. Marines in this war and was later promoted to staff sergeant. Soon after this war began, Harry Truman approved NSC-68, a secret plan calling for a huge military buildup to contain communism.",
          "During this war, the city of Seoul changed hands four times. For 10 points, name this war fought from 1950 to 1953.")
    ],
    "clues": [
        C("invasion", "giveaway", "Began on June 25, 1950, when North Korea invaded South Korea",
          ["june 25, 1950", "invaded", "north korea"]),
        C("parallel", "giveaway", "The 38th parallel divided North and South Korea; the fighting ended near it",
          ["38th parallel", "parallel"]),
        C("armistice", "giveaway", "Ended with an armistice on July 27, 1953, not a peace treaty",
          ["armistice", "july 27, 1953", "peace treaty"]),
        C("un", "giveaway", "United Nations (UN) forces, led mostly by the United States, defended South Korea",
          ["united nations", "un forces"]),
        C("forgotten", "giveaway", "Often nicknamed the “Forgotten War” in the United States",
          ["forgotten", "nicknamed"]),
        C("macarthur", "middle", "General Douglas MacArthur led UN forces until Harry Truman fired him in April 1951",
          ["douglas macarthur", "macarthur", "truman", "fired"], "Douglas MacArthur"),
        C("inchon", "middle", "MacArthur’s surprise landing at Inchon (September 15, 1950) turned the tide",
          ["inchon", "landing", "september 15"]),
        C("china", "middle", "China entered in late 1950 after UN forces neared the Yalu River border",
          ["china", "yalu river", "yalu"]),
        C("chosin", "middle", "Battle of Chosin Reservoir (late 1950): surrounded Marines fought their way out in bitter cold",
          ["chosin", "reservoir", "marines"]),
        C("pusan", "middle", "Early on, UN troops were pushed back into the Pusan Perimeter in the southeast",
          ["pusan perimeter", "pusan"]),
        C("leaders", "middle", "North Korea was led by Kim Il Sung; South Korea by Syngman Rhee, who refused to sign the armistice",
          ["kim il sung", "syngman rhee"]),
        C("eisenhower", "middle", "Dwight Eisenhower promised in 1952, “I shall go to Korea”; the armistice came in his first year as president",
          ["eisenhower", "i shall go", "1952"], "Dwight D. Eisenhower"),
        C("mash", "middle", "The TV comedy _M*A*S*H_ (1972–1983), about Hawkeye Pierce’s army hospital, was set in this war; its 1983 finale set viewing records",
          ["m*a*s*h", "hawkeye", "finale"]),
        C("police-action", "middle", "Truman agreed with a reporter who called it a “police action”; Congress never declared war",
          ["police action", "declared war"], "Harry S. Truman"),
        C("rusk", "power", "Dean Rusk and Charles Bonesteel picked the 38th parallel as the dividing line in 1945, using a National Geographic map",
          ["rusk", "bonesteel", "national geographic"]),
        C("boycott", "power", "The Soviet Union was boycotting the UN Security Council, so it could not veto sending troops",
          ["boycotting", "security council", "veto"]),
        C("sixteen", "power", "Sixteen nations sent combat troops under the UN flag",
          ["sixteen", "combat troops"]),
        C("task-force-smith", "power", "Task Force Smith, the first U.S. ground unit to fight, was overrun at Osan (July 1950)",
          ["task force smith", "osan"]),
        C("mig-alley", "power", "F-86 Sabres fought Soviet-built MiG-15s in “MiG Alley”; Peng Dehuai led the Chinese troops",
          ["mig alley", "sabres", "peng dehuai"]),
        C("hungnam", "power", "The Hungnam evacuation (December 1950) carried away about 100,000 troops and nearly as many civilians",
          ["hungnam", "evacuation"]),
        C("jesse-brown", "power", "Jesse L. Brown, the first African American to complete Navy flight training, was shot down and died; Thomas Hudner won the Medal of Honor trying to save him",
          ["hudner", "jesse brown", "medal of honor"]),
        C("no-substitute", "power", "MacArthur’s letter, read by Joseph Martin: “There is no substitute for victory”; his farewell: “Old soldiers never die”",
          ["no substitute for victory", "joseph martin", "old soldiers"]),
        C("bradley", "power", "Omar Bradley: war with China would be “the wrong war, at the wrong place, at the wrong time, and with the wrong enemy”",
          ["omar bradley", "bradley", "wrong enemy"]),
        C("ridgway", "power", "Matthew Ridgway took over the Eighth Army, then replaced MacArthur (1951)",
          ["ridgway", "eighth army"]),
        C("kaesong", "power", "Truce talks began at Kaesong (1951) and moved to Panmunjom; prisoners of war were the main dispute",
          ["kaesong", "prisoners of war"]),
        C("hills", "power", "Battles for hills: Pork Chop Hill (a 1959 Gregory Peck film), Heartbreak Ridge, and Bloody Ridge",
          ["pork chop hill", "heartbreak ridge", "gregory peck"]),
        C("memorial", "power", "Its memorial in Washington (1995): 19 steel soldiers in ponchos and the words “Freedom Is Not Free”",
          ["ponchos", "freedom is not free", "19"]),
        C("reckless", "power", "Reckless, a small mare that carried ammunition for the Marines, was promoted to staff sergeant",
          ["reckless", "staff sergeant"])
    ],
    "trap": {
        "title": "Korea, not Vietnam",
        "body": "The Korean War and the Vietnam War were both Cold War fights between a Communist north and a U.S.-backed south, so players mix them up. Many clues inside Korean War tossups, like Inchon, the Chosin Reservoir, and Douglas MacArthur, are answer lines of their own, and “name this battle” or “name this general” wants that answer instead. Calling it just “Korea” or a “police action” earns only a prompt.",
        "fix": "The 38th parallel, Inchon, Chosin, MacArthur’s firing, Panmunjom, and _M*A*S*H_ mean Korea (1950–1953). The 17th parallel, Ho Chi Minh, the Gulf of Tonkin, and the Tet Offensive mean Vietnam. Say “Korean War,” not just “Korea.”",
        "line": "Real answer line: <b><u>Korean War</u></b> (accept <u>Korean Conflict</u> or <u>6–25 War</u>; prompt on <u>Korea</u>)"
    },
    "tests": {
        "right": [
            "Korean War",
            "The Korean War",
            "Korean Conflict",
            "Koren War",
            "6-25 War"
        ],
        "prompt": [
            "Korea",
            "police action"
        ],
        "wrong": [
            "Vietnam War",
            "Cold War",
            "Battle of Inchon",
            "World War II",
            "Douglas MacArthur",
            "North Korea",
            "Chosin Reservoir"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
