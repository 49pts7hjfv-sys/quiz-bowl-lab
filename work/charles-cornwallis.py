import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

data = {
    "id": "charles-cornwallis",
    "name": "Charles Cornwallis",
    "mono": "CC",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "British general who surrendered at Yorktown · Later Governor-General of India",
    "dates": "1738–1805",
    "briefing": "Charles Cornwallis led British armies through much of the American Revolution, crushing Horatio Gates at Camden in 1780 and beating Nathanael Greene at Guilford Courthouse in 1781, though at a heavy cost. That October, trapped at Yorktown, Virginia, by George Washington’s army, French troops, and a French fleet, he surrendered his whole army, which effectively ended the war. His career survived: he later governed British India and served as Lord Lieutenant of Ireland.",
    "answerHtml": "Charles <b><u>Cornwallis</u></b> (or Lord <b><u>Cornwallis</u></b>; do not accept “Henry Clinton” or “John Burgoyne”)",
    "accept": [
        "charles cornwallis",
        "cornwallis",
        "lord cornwallis",
        "lord charles cornwallis",
        "general cornwallis",
        "earl cornwallis",
        "marquess cornwallis"
    ],
    "prompt": [],
    "reject": [
        "henry clinton",
        "sir henry clinton",
        "clinton",
        "william howe",
        "howe",
        "john burgoyne",
        "burgoyne",
        "banastre tarleton",
        "tarleton",
        "charles ohara",
        "ohara",
        "thomas gage",
        "guy carleton",
        "patrick ferguson",
        "benedict arnold",
        "george iii",
        "king george iii",
        "lord north",
        "william cornwallis",
        "admiral cornwallis",
        "nathanael greene",
        "horatio gates",
        "benjamin lincoln",
        "rochambeau",
        "comte de rochambeau",
        "george washington",
        "battle of yorktown",
        "siege of yorktown",
        "yorktown",
        "charles james fox",
        "tipu sultan"
    ],
    "tests": {
        "right": [
            "Charles Cornwallis",
            "Cornwallis",
            "Lord Cornwallis",
            "General Cornwallis",
            "Cornwalis",
            "Charles Cornwalis",
            "Marquess Cornwallis",
            "Lord Charles Cornwallis"
        ],
        "prompt": [],
        "wrong": [
            "Henry Clinton",
            "William Howe",
            "John Burgoyne",
            "Banastre Tarleton",
            "Charles O'Hara",
            "William Cornwallis",
            "Battle of Yorktown",
            "George Washington"
        ]
    },
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Charles_Cornwallis,_1st_Marquess_Cornwallis",
    "qb": {
        "q": "Cornwallis",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "The German-born general Baron de Kalb was mortally wounded while fighting this general’s army in August 1780. In that battle, at Camden, South Carolina, this general’s troops sent American militiamen running and their commander, Horatio Gates, fleeing on horseback.",
            "r": "In October 1781, this general surrendered to George Washington at Yorktown, Virginia. For 10 points, name this British commander."
        },
        {
            "p": "To chase Nathanael Greene’s army faster in early 1781, this general burned his own baggage wagons, but Greene escaped across the Dan River into Virginia. After this general later beat Greene in a costly battle, the politician Charles James Fox declared that another such victory would ruin the British army.",
            "r": "That battle was fought at Guilford Courthouse. For 10 points, name this British general who surrendered at Yorktown later that year."
        },
        {
            "p": "In January 1777, this general pinned George Washington’s army against a creek at Trenton and planned to finish the fight in the morning. During the night, Washington’s men slipped away, leaving campfires burning to fool the British, and defeated a British force at Princeton.",
            "r": "This general later won at Camden and surrendered at Yorktown. For 10 points, name this British commander."
        },
        {
            "p": "Claiming to be ill, this commander skipped a surrender ceremony and sent his deputy, Charles O’Hara, who first tried to hand his sword to the Comte de Rochambeau [“roh-sham-BOH”]. Rochambeau pointed O’Hara toward the American commander, who had his own second-in-command, Benjamin Lincoln, accept the sword.",
            "r": "For 10 points, name this British general whose army surrendered at Yorktown on October 19, 1781."
        },
        {
            "p": "In 1792, this man forced Tipu Sultan of Mysore [“my-SOR”] to give up about half of his kingdom and to hand over two of his sons as hostages, and he was made a marquess that year. In 1793, he fixed the land taxes of Bengal in a plan called the Permanent Settlement.",
            "r": "As a general, he had surrendered at Yorktown in 1781. For 10 points, name this British Governor-General of India."
        },
        {
            "p": "A small French invasion force surrendered to this man’s army at Ballinamuck in 1798, as a rebellion by the United Irishmen was ending. As Lord Lieutenant of Ireland, he then helped pass the Act of Union, but he resigned in 1801 when King George III refused to allow Catholic emancipation.",
            "r": "Twenty years earlier, he had surrendered his own army at Yorktown. For 10 points, name this British general."
        },
        {
            "p": "This man signed the 1802 Treaty of Amiens for Britain, bringing a short-lived peace with Napoleon’s France. Three years later, he died at Ghazipur soon after returning to India for a second term as its Governor-General.",
            "r": "Decades earlier, this general had won at Camden before being trapped at Yorktown. For 10 points, name this British commander in the American Revolution."
        },
        {
            "p": "The destruction of Patrick Ferguson’s Loyalist force at Kings Mountain in October 1780 forced this general to give up his first invasion of North Carolina. Three months later, his cavalry commander, Banastre Tarleton, was badly beaten by Daniel Morgan at the Battle of Cowpens.",
            "r": "For 10 points, name this British general who surrendered to George Washington at Yorktown in 1781."
        },
        {
            "p": "In May 1781, this general marched north into Virginia and took command of the British troops there, including soldiers who had been led by the turncoat Benedict Arnold. Weeks later, his cavalry raided Charlottesville and nearly captured Thomas Jefferson at his home, Monticello.",
            "r": "That October, this general surrendered his army at Yorktown, Virginia. For 10 points, name this British commander in the American Revolution."
        },
        {
            "p": "In November 1776, this general crossed the Hudson River to capture Fort Lee and then chased George Washington’s retreating army across New Jersey. The next September, he led a long flanking march around Washington’s right side that helped the British win the Battle of Brandywine.",
            "r": "He later commanded the British army in the South. For 10 points, name this British general who surrendered at Yorktown in 1781."
        },
        {
            "p": "This general was traded in a prisoner exchange for Henry Laurens, a former president of the Continental Congress who had been held in the Tower of London. After the war, this general and his former commander, Henry Clinton, published pamphlets blaming each other for a disastrous defeat.",
            "r": "That defeat came at Yorktown in 1781. For 10 points, name this British general who surrendered there."
        },
        {
            "p": "On the night of October 16, 1781, this commander tried to ferry his troops across a river to Gloucester Point, but a sudden storm scattered his boats. Two days earlier, he had lost two key redoubts to night attacks by French troops and by Americans led by Alexander Hamilton.",
            "r": "Days later, trapped by American and French forces, he surrendered his army at Yorktown. For 10 points, name this British general."
        },
        {
            "p": "This general does not appear in John Trumbull’s painting of his own army’s surrender, which hangs in the U.S. Capitol Rotunda and shows Benjamin Lincoln on a white horse. According to legend, a British band played “The World Turned Upside Down” as this general’s troops laid down their weapons.",
            "r": "For 10 points, name this British general whose 1781 surrender at Yorktown effectively ended the American Revolution."
        },
        {
            "p": "Henry Clinton ordered this general to set up a fortified base for the Royal Navy on the Chesapeake Bay, but a French fleet under the Comte de Grasse [“GRAHSS”] drove off the British ships sent to help him. A relief fleet from New York arrived days too late to save this general’s army.",
            "r": "For 10 points, name this British general who surrendered to George Washington at Yorktown, Virginia, in October 1781."
        },
        {
            "p": "After helping Henry Clinton capture Charleston in 1780, this general was left in command of the British army in the South. In March 1781, he won the Battle of Guilford Courthouse in North Carolina but lost about a quarter of his men.",
            "r": "He then marched his weakened army to Wilmington and on into Virginia. For 10 points, name this British general who surrendered at Yorktown later that year."
        }
    ],
    "clues": [
        {
            "id": "yorktown",
            "tier": "giveaway",
            "t": "Surrendered his army at Yorktown, Virginia, on October 19, 1781, which effectively ended the American Revolution",
            "k": ["yorktown", "october 19", "1781", "surrendered"],
            "n": 0,
            "rabbit": "Battle of Yorktown"
        },
        {
            "id": "trapped",
            "tier": "giveaway",
            "t": "Was trapped at Yorktown by George Washington’s army, the Comte de Rochambeau’s French troops, and a French fleet under the Comte de Grasse",
            "k": ["george washington", "rochambeau", "de grasse", "french fleet"],
            "n": 0,
            "rabbit": "George Washington"
        },
        {
            "id": "british-general",
            "tier": "giveaway",
            "t": "British general who commanded Britain’s army in the South during the American Revolution",
            "k": ["british general", "south"],
            "n": 0
        },
        {
            "id": "lord",
            "tier": "giveaway",
            "t": "Usually called “Lord” because he was an earl; he was made a marquess in 1792",
            "k": ["earl", "marquess", "lord"],
            "n": 0
        },
        {
            "id": "camden",
            "tier": "middle",
            "t": "Crushed Horatio Gates’s army at the Battle of Camden, South Carolina (August 1780); Baron de Kalb was mortally wounded",
            "k": ["camden", "horatio gates", "de kalb"],
            "n": 0
        },
        {
            "id": "guilford",
            "tier": "middle",
            "t": "Beat Nathanael Greene at Guilford Courthouse, North Carolina (March 1781), but lost about a quarter of his men",
            "k": ["guilford courthouse", "nathanael greene", "quarter"],
            "n": 0
        },
        {
            "id": "charleston",
            "tier": "middle",
            "t": "Helped Henry Clinton capture Charleston (1780), then was left in command of the British army in the South",
            "k": ["charleston", "1780", "command"],
            "n": 0
        },
        {
            "id": "princeton",
            "tier": "middle",
            "t": "Trapped Washington at Trenton in January 1777, but Washington slipped away overnight and won at Princeton",
            "k": ["princeton", "trenton", "slipped away"],
            "n": 0
        },
        {
            "id": "ohara",
            "tier": "middle",
            "t": "Claimed illness and skipped the surrender; his deputy Charles O’Hara offered the sword to Rochambeau, and Benjamin Lincoln accepted it",
            "k": ["charles o’hara", "o’hara", "benjamin lincoln", "sword"],
            "n": 0
        },
        {
            "id": "clinton",
            "tier": "middle",
            "t": "Served under commander-in-chief Henry Clinton, who ordered him to build a naval base on the Chesapeake; the two later blamed each other in pamphlets",
            "k": ["henry clinton", "chesapeake", "pamphlets"],
            "n": 0
        },
        {
            "id": "india",
            "tier": "middle",
            "t": "Governor-General of India (1786–1793), and again briefly in 1805",
            "k": ["governor-general", "india"],
            "n": 0
        },
        {
            "id": "ireland",
            "tier": "middle",
            "t": "Lord Lieutenant of Ireland (1798–1801), during and after the Irish Rebellion of 1798",
            "k": ["lord lieutenant", "ireland", "1798"],
            "n": 0
        },
        {
            "id": "upside-down",
            "tier": "middle",
            "t": "Legend says a band played “The World Turned Upside Down” at his surrender; John Trumbull’s painting of it shows Benjamin Lincoln, not him",
            "k": ["world turned upside down", "upside down", "john trumbull", "trumbull"],
            "n": 0
        },
        {
            "id": "cowpens",
            "tier": "middle",
            "t": "His cavalry commander, Banastre Tarleton, was beaten by Daniel Morgan at Cowpens (January 1781)",
            "k": ["banastre tarleton", "tarleton", "cowpens", "daniel morgan"],
            "n": 0
        },
        {
            "id": "kings-mountain",
            "tier": "power",
            "t": "The defeat of Patrick Ferguson’s Loyalists at Kings Mountain (October 1780) ended his first invasion of North Carolina",
            "k": ["kings mountain", "patrick ferguson", "loyalists"],
            "n": 0
        },
        {
            "id": "race-to-the-dan",
            "tier": "power",
            "t": "Burned his own baggage to chase Nathanael Greene, who escaped across the Dan River into Virginia (1781)",
            "k": ["dan river", "baggage", "burned"],
            "n": 0
        },
        {
            "id": "fox",
            "tier": "power",
            "t": "After Guilford Courthouse, Charles James Fox declared that another such victory would ruin the British army",
            "k": ["charles james fox", "another such victory", "ruin"],
            "n": 0
        },
        {
            "id": "fort-lee",
            "tier": "power",
            "t": "Captured Fort Lee and chased Washington’s army across New Jersey (November 1776)",
            "k": ["fort lee", "new jersey", "1776"],
            "n": 0
        },
        {
            "id": "brandywine",
            "tier": "power",
            "t": "Led the flanking march that helped the British win the Battle of Brandywine (September 1777)",
            "k": ["brandywine", "flanking", "1777"],
            "n": 0
        },
        {
            "id": "virginia-1781",
            "tier": "power",
            "t": "In Virginia (May 1781), took over troops once led by Benedict Arnold; his cavalry nearly captured Thomas Jefferson near Charlottesville",
            "k": ["benedict arnold", "charlottesville", "thomas jefferson"],
            "n": 0
        },
        {
            "id": "gloucester",
            "tier": "power",
            "t": "Tried to escape across the York River to Gloucester Point, but a storm scattered his boats (October 16–17, 1781)",
            "k": ["gloucester point", "storm", "york river"],
            "n": 0
        },
        {
            "id": "laurens",
            "tier": "power",
            "t": "Was exchanged for Henry Laurens, a former president of the Continental Congress held in the Tower of London",
            "k": ["henry laurens", "laurens", "tower of london"],
            "n": 0
        },
        {
            "id": "tipu",
            "tier": "power",
            "t": "Defeated Tipu Sultan of Mysore, who gave up about half his kingdom and two sons as hostages (1792)",
            "k": ["tipu sultan", "mysore", "hostages"],
            "n": 0
        },
        {
            "id": "permanent-settlement",
            "tier": "power",
            "t": "His Permanent Settlement (1793) fixed the land taxes of Bengal",
            "k": ["permanent settlement", "bengal", "1793"],
            "n": 0
        },
        {
            "id": "ballinamuck",
            "tier": "power",
            "t": "A small French invasion force surrendered to his army at Ballinamuck, Ireland (1798)",
            "k": ["ballinamuck", "french invasion"],
            "n": 0
        },
        {
            "id": "act-of-union",
            "tier": "power",
            "t": "Helped pass the Act of Union joining Britain and Ireland; resigned in 1801 when George III refused Catholic emancipation",
            "k": ["act of union", "catholic emancipation", "george iii"],
            "n": 0
        },
        {
            "id": "amiens",
            "tier": "power",
            "t": "Signed the Treaty of Amiens (1802), a short-lived peace between Britain and Napoleon’s France",
            "k": ["treaty of amiens", "amiens", "1802"],
            "n": 0
        },
        {
            "id": "ghazipur",
            "tier": "power",
            "t": "Died at Ghazipur, India, in 1805, soon after returning for a second term as Governor-General",
            "k": ["ghazipur", "1805"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Which British general?",
        "body": "Several British generals show up in Revolutionary War tossups. John Burgoyne surrendered at Saratoga in 1777; William Howe captured New York and Philadelphia; Henry Clinton was Cornwallis’s commander-in-chief, based in New York; and Banastre Tarleton was Cornwallis’s cavalry leader, beaten at Cowpens. Cornwallis also skipped his own surrender ceremony, so clues about Charles O’Hara handing over the sword still want Cornwallis.",
        "fix": "Camden, Guilford Courthouse, Yorktown, India, and Ireland mean Cornwallis. Saratoga means Burgoyne; Bunker Hill and the capture of Philadelphia mean Howe; Cowpens and cavalry raids mean Tarleton. If you only remember “Lord ___,” say “Cornwallis.”",
        "line": "Real answer line: Charles <b><u>Cornwallis</u></b> (or Lord <b><u>Cornwallis</u></b>; do not accept “Henry Clinton” or “John Burgoyne”)"
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
