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
    "id": "james-monroe",
    "name": "James Monroe",
    "mono": "JM5",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "5th U.S. President · Issued the Monroe Doctrine in 1823",
    "dates": "1758–1831",
    "briefing": "As an 18-year-old officer, James Monroe was badly wounded at the Battle of Trenton, and he went on to become the last Founding Father to serve as president. As the fifth president, he led the country during the “Era of Good Feelings,” acquired Florida from Spain, and warned Europe to stay out of the Americas with the Monroe Doctrine. He died on July 4, 1831, the third president to die on Independence Day.",
    "answerHtml": "James <b><u>Monroe</u></b> (do not accept or prompt on “Monroe Doctrine”)",
    "accept": [
        "james monroe",
        "monroe",
        "president james monroe"
    ],
    "prompt": [
        "james"
    ],
    "reject": [
        "monroe doctrine",
        "the monroe doctrine",
        "doctrine",
        "james madison",
        "madison",
        "james k polk",
        "james polk",
        "polk",
        "james buchanan",
        "james garfield",
        "marilyn monroe",
        "elizabeth monroe",
        "fort monroe",
        "monrovia",
        "john quincy adams",
        "quincy adams"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/James_Monroe",
    "qb": {
        "q": "James Monroe",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        T("While serving as minister to France, this man got Thomas Paine released from a Paris prison in 1794 and let Paine recover in his own home. George Washington later recalled this diplomat for failing to defend the Jay Treaty.",
          "For 10 points, name this man whose 1823 namesake doctrine warned European powers not to start new colonies in the Americas."),
        T("In Emanuel Leutze’s painting _Washington Crossing the Delaware_, the soldier holding the flag is traditionally identified as this man. As a young officer, he was badly wounded at the Battle of Trenton, which followed that crossing.",
          "He later became the fifth president. For 10 points, name this Virginian whose presidency was called the Era of Good Feelings."),
        T("This man argued against ratifying the Constitution at Virginia’s ratifying convention, and in 1789 he lost a race for the House of Representatives to James Madison. He later served as Madison’s Secretary of State before succeeding him as president.",
          "For 10 points, name this fifth president, who gave his name to an 1823 doctrine about the Western Hemisphere."),
        T("As governor of Virginia, this man called out the state militia in 1800 after learning of a planned revolt by enslaved people led by a blacksmith named Gabriel. He had earlier served as a U.S. senator and as minister to France.",
          "For 10 points, name this Virginian who became the fifth U.S. president and issued a famous doctrine in 1823."),
        T("This diplomat and William Pinkney signed an 1806 treaty with Britain that Thomas Jefferson refused to send to the Senate because it did not end impressment. Three years earlier, Jefferson had sent this man to Paris to help Robert Livingston buy New Orleans.",
          "Instead, they bought the whole Louisiana Territory. For 10 points, name this man who later became the fifth president."),
        T("After the British burned Washington in 1814, this man took over the War Department while still serving as Secretary of State, holding both jobs until the War of 1812 ended. He had joined James Madison’s cabinet as Secretary of State in 1811.",
          "He won the presidency in 1816. For 10 points, name this fifth president, whose 1823 doctrine warned Europe against new colonies in the Americas."),
        T("During this president’s 1817 goodwill tour of New England, the Boston newspaper _Columbian Centinel_ coined a famous phrase for the calm political mood of his time in office. During his presidency, the rival Federalist Party faded away.",
          "That phrase was “the Era of Good Feelings.” For 10 points, name this fifth president of the United States."),
        T("In the 1820 election, William Plumer of New Hampshire was the only elector to vote against this president, choosing John Quincy Adams instead. The Federalists had not even nominated a candidate to run against him.",
          "For 10 points, name this president whose name is on an 1823 doctrine warning Europe not to colonize the Americas."),
        T("This president’s administration signed the Rush–Bagot Agreement, which limited warships on the Great Lakes, and the Treaty of 1818, which set much of the border with British Canada at the 49th parallel. His Secretary of State was John Quincy Adams.",
          "For 10 points, name this fifth president, who presided over the Era of Good Feelings."),
        T("Luis de Onís [“oh-NEES”] negotiated an 1819 treaty with this president’s Secretary of State that drew a border with Spain’s lands all the way to the Pacific Ocean. Earlier, General Andrew Jackson had invaded Spanish Florida while chasing Seminole warriors.",
          "In that treaty, Spain gave Florida to the United States. For 10 points, name this fifth president."),
        T("This president vetoed a bill to collect tolls on the Cumberland Road, arguing that the Constitution did not let Congress run such projects. The Panic of 1819, the country’s first major economic depression, struck during his first term.",
          "He had won the presidency in 1816 as a Democratic-Republican. For 10 points, name this president of the Era of Good Feelings."),
        T("This president was nicknamed “the Last Cocked Hat” because he kept wearing the knee breeches and three-cornered hat of the Revolutionary era. He was the last of four early presidents from Virginia, a group called the Virginia Dynasty.",
          "For 10 points, name this fifth president, who issued an 1823 doctrine warning Europe to stop colonizing the Americas."),
        T("This president died in New York City on July 4, 1831, exactly five years after John Adams and Thomas Jefferson both died on the same holiday. He had studied law under Jefferson and later lived at Highland, a farm near Monticello.",
          "For 10 points, name this fifth president, whose doctrine warned European powers to stay out of the Western Hemisphere."),
        T("The Supreme Court decided _McCulloch v. Maryland_ during this man’s presidency, and the Tallmadge Amendment set off a bitter fight over slavery in Missouri. That fight ended when he signed the Missouri Compromise in 1820.",
          "Monrovia, the capital of Liberia, is named for him. For 10 points, name this fifth president."),
        T("Britain’s foreign secretary, George Canning, proposed that his country and the United States jointly warn other European powers away from Latin America. This president’s Secretary of State, John Quincy Adams, convinced him to make the statement alone instead.",
          "That statement, in an 1823 message to Congress, became this president’s namesake doctrine. For 10 points, name this fifth president."),
    ],
    "clues": [
        C("fifth", "giveaway", "5th President of the United States (1817–1825)", ["5th president", "1817", "1825"]),
        C("doctrine", "giveaway", "His namesake doctrine (1823) warned European powers not to start new colonies in the Western Hemisphere", ["doctrine", "western hemisphere", "1823", "colonies"]),
        C("good-feelings", "giveaway", "His presidency was called the “Era of Good Feelings”", ["era of good feelings", "good feelings"]),
        C("monrovia", "giveaway", "Monrovia, the capital of Liberia, is named for him", ["monrovia", "liberia"]),
        C("virginia", "giveaway", "A Virginian, the last of the “Virginia Dynasty” of presidents (Washington, Jefferson, Madison, and him)", ["virginia dynasty", "virginian"]),
        C("jqa", "middle", "His Secretary of State, John Quincy Adams, wrote much of his famous doctrine and negotiated the Adams–Onís Treaty", ["john quincy adams", "secretary of state"], "John Quincy Adams"),
        C("florida", "middle", "Got Florida from Spain in the Adams–Onís Treaty (1819), after Andrew Jackson invaded Spanish Florida", ["florida", "spain", "1819"]),
        C("missouri", "middle", "Signed the Missouri Compromise (1820) after the Tallmadge Amendment started a fight over slavery in Missouri", ["missouri compromise", "tallmadge", "1820"], "Missouri Compromise"),
        C("louisiana", "middle", "Sent to Paris to buy New Orleans, he helped Robert Livingston buy the whole Louisiana Territory instead (1803)", ["louisiana", "livingston", "new orleans", "1803"]),
        C("trenton", "middle", "Wounded at the Battle of Trenton (1776); traditionally said to be the flag-bearer in Leutze’s _Washington Crossing the Delaware_", ["trenton", "flag", "crossing the delaware", "leutze"]),
        C("war-secretary", "middle", "Served as Secretary of State and Secretary of War at the same time near the end of the War of 1812", ["secretary of war", "same time", "war of 1812"]),
        C("july-4", "middle", "Died July 4, 1831, the third president to die on the Fourth of July (after John Adams and Thomas Jefferson in 1826)", ["july 4", "1831", "fourth of july"]),
        C("paine", "power", "As minister to France, got Thomas Paine released from a Paris prison (1794); Washington later recalled him over the Jay Treaty", ["thomas paine", "paine", "jay treaty", "1794"]),
        C("madison-1789", "power", "Opposed ratifying the Constitution in Virginia, then lost a 1789 House race to James Madison", ["james madison", "1789", "ratifying"]),
        C("gabriel", "power", "As governor of Virginia, called out the militia against Gabriel’s planned revolt of enslaved people (1800)", ["gabriel", "governor", "militia", "1800"]),
        C("pinkney", "power", "His 1806 treaty with Britain, signed with William Pinkney, was rejected by Jefferson because it did not end impressment", ["pinkney", "impressment", "1806"]),
        C("plumer", "power", "Won the 1820 election almost unanimously; one elector, William Plumer, voted for John Quincy Adams instead", ["plumer", "1820", "elector"]),
        C("centinel", "power", "Boston’s _Columbian Centinel_ coined the phrase “Era of Good Feelings” during his 1817 tour of New England", ["columbian centinel", "centinel", "1817", "tour"]),
        C("rush-bagot", "power", "The Rush–Bagot Agreement (1817) limited warships on the Great Lakes", ["rush", "bagot", "great lakes"]),
        C("convention-1818", "power", "The Treaty of 1818 with Britain made the 49th parallel much of the Canadian border and shared Oregon", ["49th parallel", "oregon", "1818"]),
        C("cumberland", "power", "Vetoed a bill to collect tolls on the Cumberland Road (1822), saying Congress lacked that power", ["cumberland road", "tolls", "1822"]),
        C("panic-1819", "power", "The Panic of 1819, the first major U.S. depression, struck during his first term", ["panic of 1819", "depression"]),
        C("cocked-hat", "power", "Nicknamed “the Last Cocked Hat” for still wearing knee breeches and a three-cornered hat", ["last cocked hat", "cocked hat", "knee breeches"]),
        C("highland", "power", "Studied law under Thomas Jefferson; his farm, Highland, was near Monticello", ["highland", "monticello", "studied law"]),
        C("canning", "power", "Britain’s George Canning proposed a joint warning to Europe, but John Quincy Adams convinced him to act alone", ["george canning", "canning", "joint", "alone"]),
    ],
    "trap": {
        "title": "The man, not the doctrine",
        "body": "The Monroe Doctrine is its own common answer line, so it is easy to blurt out on a question about the man. On this answer line, “Monroe Doctrine” is wrong: the question wants the president himself. Players also mix him up with James Madison, the president just before him, since both were Virginians who served as Secretary of State before becoming president.",
        "fix": "Listen for the noun. “This president” or “this man” wants James Monroe; “this doctrine” or “this policy” wants the Monroe Doctrine. A John Quincy Adams tossup may mention the doctrine he wrote for his boss, and then the answer is Adams. Madison clues: “Father of the Constitution,” the Bill of Rights, and leading the country in the War of 1812; Monroe clues: the Era of Good Feelings, Florida, and the Missouri Compromise.",
        "line": "Real answer line: James <b><u>Monroe</u></b> (do not accept or prompt on “Monroe Doctrine”)"
    },
    "tests": {
        "right": [
            "James Monroe",
            "Monroe",
            "President Monroe",
            "James Monore"
        ],
        "prompt": [
            "James"
        ],
        "wrong": [
            "Monroe Doctrine",
            "James Madison",
            "Marilyn Monroe",
            "John Quincy Adams",
            "James K. Polk",
            "Monrovia"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
