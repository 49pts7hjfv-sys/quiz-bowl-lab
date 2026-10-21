import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "henry-knox",
    "name": "Henry Knox",
    "mono": "KNX",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Washington’s chief of artillery · First U.S. Secretary of War",
    "dates": "1750–1806",
    "briefing": "Henry Knox was a Boston bookseller who taught himself about cannons by reading military books in his own shop. In the winter of 1775–1776, he hauled about 60 tons of cannons from Fort Ticonderoga to Boston on ox-drawn sleds, a “noble train of artillery” that helped force the British out of the city. He became George Washington’s chief of artillery and later the first U.S. Secretary of War, and Fort Knox is named for him.",
    "answerHtml": "Henry <b><u>Knox</u></b> (prompt on <u>Henry</u>; do not accept “Fort Knox,” “Philander Knox,” or “Benjamin Lincoln”)",
    "accept": [
        "henry knox",
        "knox",
        "general knox",
        "general henry knox",
        "secretary knox",
        "h knox"
    ],
    "prompt": [
        "henry"
    ],
    "reject": [
        "fort knox",
        "fort knox kentucky",
        "philander knox",
        "philander c knox",
        "john knox",
        "frank knox",
        "lucy knox",
        "knoxville",
        "benjamin lincoln",
        "nathanael greene",
        "george washington",
        "ethan allen",
        "benedict arnold",
        "baron von steuben",
        "von steuben",
        "alexander hamilton",
        "anthony wayne",
        "daniel morgan",
        "timothy pickering",
        "james mchenry",
        "fort ticonderoga",
        "dorchester heights",
        "secretary of war",
        "john adams"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Henry_Knox",
    "qb": {
        "q": "Henry Knox",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "This man lost two fingers on his left hand when his gun exploded during a bird-hunting trip in 1773, and in many portraits he keeps that hand wrapped in a cloth. At the time, he ran a bookstore in Boston and read books about artillery.",
            "r": "He later hauled cannons from Fort Ticonderoga to Boston. For 10 points, name this general who became the first U.S. Secretary of War."
        },
        {
            "p": "In 1774, this man married Lucy Flucker, whose father was a high royal official in Massachusetts and whose family stayed loyal to Britain. The couple slipped out of Boston in 1775, and he soon joined the patriot army surrounding the city.",
            "r": "He later hauled about 60 tons of cannons from Fort Ticonderoga to Boston. For 10 points, name this artillery chief who became the first Secretary of War."
        },
        {
            "p": "This member of George Washington’s cabinet signed the 1790 Treaty of New York with the Creek leader Alexander McGillivray [“muh-GIL-uh-vray”], who traveled to New York City to negotiate. This man argued that the United States should gain Native lands by treaty and purchase rather than by conquest.",
            "r": "His cabinet post put him in charge of the Army. For 10 points, name this first Secretary of War."
        },
        {
            "p": "Until 1798, this man’s department oversaw the building of the first frigates of the U.S. Navy, including the USS _Constitution_, after Congress approved six new ships in 1794. Joshua Humphreys designed those frigates. This man left office at the end of 1794 and later retired to Maine.",
            "r": "This man had earlier been George Washington’s chief of artillery. For 10 points, name this first Secretary of War."
        },
        {
            "p": "After leaving government, this man built a grand mansion called Montpelier in Thomaston, in what was then the District of Maine, and he died there in 1806. A granite fort on Maine’s Penobscot River was later named for him.",
            "r": "A more famous Army post in Kentucky, which stores much of the nation’s gold, also bears his name. For 10 points, name this first Secretary of War."
        },
        {
            "p": "During the 1777 Battle of Germantown, this officer argued that the Americans should not leave British soldiers holding a stone mansion behind their lines, and the long attack on that house, owned by Benjamin Chew, slowed the Continental Army. Weeks earlier, he had fought at Brandywine.",
            "r": "He commanded George Washington’s artillery. For 10 points, name this general who later became the first Secretary of War."
        },
        {
            "p": "At Fraunces Tavern in New York City in December 1783, George Washington said farewell to his officers, and this general, standing nearest, was the first to take his hand. After Washington resigned his command that month, this general became the senior officer of the small army that remained.",
            "r": "He had served as Washington’s chief of artillery. For 10 points, name this man who became the first Secretary of War."
        },
        {
            "p": "This man drew up the plan for a society of Continental Army officers, founded in 1783 and named for a Roman leader who returned to his farm after saving Rome. A city in Ohio was later named for that society.",
            "r": "George Washington became that society’s first leader. For 10 points, name this general who served as Washington’s chief of artillery."
        },
        {
            "p": "In 1785, Congress under the Articles of Confederation chose this man to run its War Department, a job Benjamin Lincoln had held before him. Two years later, during Shays’ Rebellion, rebels tried to seize a federal arsenal at Springfield that this man’s department controlled.",
            "r": "He kept a similar job under the Constitution, becoming the first Secretary of War. For 10 points, name this former artillery chief."
        },
        {
            "p": "After Arthur St. Clair’s army suffered a crushing defeat in the Northwest Territory in 1791, this man helped organize a new force called the Legion of the United States. Anthony Wayne led that force to victory at Fallen Timbers in 1794, the year this man left office.",
            "r": "This man was the first Secretary of War. For 10 points, name this general whose name is on a famous Army post in Kentucky."
        },
        {
            "p": "In the winter of 1775–1776, this man’s convoy of ox-drawn sleds crossed the frozen Hudson River near Albany and struggled over the snowy Berkshire Mountains. He hired local farmers and their oxen and horses for the trip of nearly 300 miles.",
            "r": "He called that convoy a “noble train of artillery.” For 10 points, name this man who brought the cannons of Fort Ticonderoga to Boston."
        },
        {
            "p": "On the night of March 4, 1776, American troops secretly dragged cannons that this man had delivered onto Dorchester Heights, overlooking Boston Harbor. Within two weeks, General William Howe’s British army sailed away, and Boston’s county still marks that day, March 17, as Evacuation Day.",
            "r": "Those cannons had come from Fort Ticonderoga. For 10 points, name this Boston bookseller who became Washington’s chief of artillery."
        },
        {
            "p": "On Christmas night in 1776, this officer directed the boats that carried George Washington’s army across the icy Delaware River, and his cannons helped win the Battle of Trenton the next morning. Days later, he was promoted to brigadier general.",
            "r": "He had earlier hauled cannons from Fort Ticonderoga. For 10 points, name this general who became the first Secretary of War."
        },
        {
            "p": "At the 1781 siege of Yorktown, this man commanded the American cannons that pounded Lord Cornwallis’s defenses until the British surrendered. He was promoted to major general the next year, at the age of 31.",
            "r": "He had been George Washington’s chief of artillery since 1775. For 10 points, name this man, the first Secretary of War."
        },
        {
            "p": "Before the Revolution, this man ran the London Book Store in Boston, where he studied military books and talked with British officers who came to browse. A city in Tennessee was named for him in 1791.",
            "r": "He later became the first U.S. Secretary of War. For 10 points, name this artillery chief who brought cannons from Fort Ticonderoga to Boston."
        }
    ],
    "clues": [
        {
            "id": "secretary-of-war",
            "tier": "giveaway",
            "t": "First U.S. Secretary of War (1789–1794), under George Washington",
            "k": ["secretary of war", "first", "1789"],
            "n": 0,
            "rabbit": "Secretary of War"
        },
        {
            "id": "noble-train",
            "tier": "giveaway",
            "t": "Hauled the cannons of Fort Ticonderoga to Boston in the winter of 1775–1776, his “noble train of artillery”",
            "k": ["noble train", "fort ticonderoga", "ticonderoga", "cannons"],
            "n": 0,
            "rabbit": "Fort Ticonderoga"
        },
        {
            "id": "army-post",
            "tier": "giveaway",
            "t": "A famous Army post in Kentucky that stores much of the nation’s gold is named for him",
            "k": ["kentucky", "gold"],
            "n": 0
        },
        {
            "id": "artillery-chief",
            "tier": "giveaway",
            "t": "George Washington’s chief of artillery during the Revolutionary War",
            "k": ["chief of artillery", "artillery", "revolutionary war"],
            "n": 0,
            "rabbit": "American Revolutionary War"
        },
        {
            "id": "bookseller",
            "tier": "middle",
            "t": "A Boston bookseller (the London Book Store) who taught himself about artillery from books",
            "k": ["bookseller", "london book store", "taught himself"],
            "n": 0
        },
        {
            "id": "dorchester",
            "tier": "middle",
            "t": "His cannons went onto Dorchester Heights, and the British left Boston on March 17, 1776 (Evacuation Day)",
            "k": ["dorchester heights", "evacuation day", "march 17"],
            "n": 0
        },
        {
            "id": "route",
            "tier": "middle",
            "t": "His ox-drawn sleds carried about 60 tons of cannons across the frozen Hudson River and the Berkshire Mountains",
            "k": ["60 tons", "ox-drawn sleds", "berkshire", "hudson"],
            "n": 0
        },
        {
            "id": "delaware-trenton",
            "tier": "middle",
            "t": "Directed the crossing of the Delaware River on Christmas night, 1776, before the Battle of Trenton",
            "k": ["delaware", "trenton"],
            "n": 0
        },
        {
            "id": "yorktown",
            "tier": "middle",
            "t": "Commanded the American cannons at the siege of Yorktown (1781); promoted to major general in 1782",
            "k": ["yorktown", "major general", "1781"],
            "n": 0
        },
        {
            "id": "cincinnati",
            "tier": "middle",
            "t": "Planned the Society of the Cincinnati (1783), named for the Roman hero Cincinnatus; Cincinnati, Ohio, was named for the society",
            "k": ["society of the cincinnati", "cincinnatus", "1783"],
            "n": 0
        },
        {
            "id": "articles",
            "tier": "middle",
            "t": "Ran the War Department under the Articles of Confederation from 1785, a job Benjamin Lincoln had held before him",
            "k": ["articles of confederation", "benjamin lincoln", "1785"],
            "n": 0,
            "rabbit": "Articles of Confederation"
        },
        {
            "id": "tennessee-city",
            "tier": "middle",
            "t": "A city in Tennessee was named for him in 1791",
            "k": ["tennessee", "1791"],
            "n": 0
        },
        {
            "id": "fingers",
            "tier": "power",
            "t": "Lost two fingers on his left hand in a 1773 hunting accident; portraits often show that hand wrapped in a cloth",
            "k": ["two fingers", "hunting accident", "1773"],
            "n": 0
        },
        {
            "id": "lucy",
            "tier": "power",
            "t": "Married Lucy Flucker (1774), whose father was a Loyalist royal official in Massachusetts",
            "k": ["lucy flucker", "flucker", "loyalist", "1774"],
            "n": 0
        },
        {
            "id": "treaty-new-york",
            "tier": "power",
            "t": "Signed the Treaty of New York (1790) with the Creek leader Alexander McGillivray",
            "k": ["treaty of new york", "mcgillivray", "creek", "1790"],
            "n": 0
        },
        {
            "id": "native-policy",
            "tier": "power",
            "t": "Argued that the U.S. should gain Native lands by treaty and purchase rather than by conquest",
            "k": ["treaty and purchase", "conquest", "native lands"],
            "n": 0
        },
        {
            "id": "frigates",
            "tier": "power",
            "t": "His department oversaw building the Navy’s first six frigates, including the USS _Constitution_ (Naval Act of 1794)",
            "k": ["frigates", "uss constitution", "naval act", "1794"],
            "n": 0
        },
        {
            "id": "montpelier",
            "tier": "power",
            "t": "Retired to Montpelier, his mansion in Thomaston, Maine, where he died in 1806",
            "k": ["montpelier", "thomaston", "1806"],
            "n": 0
        },
        {
            "id": "germantown",
            "tier": "power",
            "t": "At Germantown (1777), he urged attacking the Chew House instead of leaving it behind the lines, which slowed the American attack",
            "k": ["germantown", "chew house", "1777"],
            "n": 0
        },
        {
            "id": "fraunces",
            "tier": "power",
            "t": "At Fraunces Tavern (December 1783), he was the first officer to take Washington’s hand in farewell, and then the army’s senior officer",
            "k": ["fraunces tavern", "farewell", "december 1783"],
            "n": 0,
            "rabbit": "George Washington"
        },
        {
            "id": "shays",
            "tier": "power",
            "t": "During Shays’ Rebellion (1787), rebels tried to seize the federal arsenal at Springfield, run by his department",
            "k": ["shays", "springfield", "arsenal", "1787"],
            "n": 0,
            "rabbit": "Shays’ Rebellion"
        },
        {
            "id": "legion",
            "tier": "power",
            "t": "After St. Clair’s defeat (1791), he helped organize the Legion of the United States, which won at Fallen Timbers (1794)",
            "k": ["legion of the united states", "fallen timbers", "st. clair"],
            "n": 0
        },
        {
            "id": "maine-fort",
            "tier": "power",
            "t": "A granite fort on Maine’s Penobscot River is also named for him",
            "k": ["penobscot", "maine"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Which Knox? Which secretary?",
        "body": "The gold vault at Fort Knox in Kentucky is named for this man, but if a question asks for a person, naming the fort is wrong, and Philander Knox, William Howard Taft’s Secretary of State, is a different man. Also, Benjamin Lincoln ran the War Department under the Articles of Confederation before this man did; this man was the first Secretary of War under the Constitution.",
        "fix": "“This man” or “this general” with Fort Ticonderoga, the “noble train of artillery,” Dorchester Heights, or Washington’s first cabinet means Henry Knox. Saying just “Knox” is fine, but don’t add “Fort.”",
        "line": "Real answer line: Henry <b><u>Knox</u></b> (do not accept “Fort Knox” or “Philander Knox”)"
    },
    "tests": {
        "right": [
            "Henry Knox",
            "Knox",
            "General Knox",
            "Henry Nox",
            "General Henry Knox"
        ],
        "prompt": [
            "Henry"
        ],
        "wrong": [
            "Fort Knox",
            "Philander Knox",
            "Benjamin Lincoln",
            "John Knox",
            "Ethan Allen",
            "Benedict Arnold",
            "Knoxville"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", data["id"])
