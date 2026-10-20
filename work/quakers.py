import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "quakers",
    "name": "Quakers",
    "mono": "QK",
    "category": "Religion",
    "qbCategory": "Religion",
    "kicker": "The Religious Society of Friends · Silent worship and a peace testimony",
    "dates": "Began in England in the 1650s",
    "briefing": "In a traditional Quaker meeting for worship, there is no minister, no music, and no sermon: people sit together in silence until someone feels moved to speak. The Religious Society of Friends began in England in the 1650s with George Fox, who taught that there is “that of God in every one.” Quakers became known for refusing to fight in wars, for William Penn’s colony of Pennsylvania, and for helping lead the fight against slavery.",
    "answerHtml": "<b><u>Quakers</u></b> (or Religious <b><u>Society of Friends</u></b>; accept word forms like <u>Quaker</u>ism or <u>Friends</u> Church; prompt on <u>Friends</u>; do not accept “Shakers”)",
    "accept": [
        "quakers",
        "quaker",
        "quakerism",
        "religious society of friends",
        "society of friends",
        "the society of friends",
        "friends church",
        "friends churches"
    ],
    "prompt": [
        "friends",
        "the friends"
    ],
    "reject": [
        "earthquakes",
        "earthquake",
        "quake",
        "quakes",
        "shakers",
        "shaker",
        "shaking quakers",
        "puritans",
        "puritan",
        "pilgrims",
        "separatists",
        "amish",
        "mennonites",
        "mennonite",
        "methodists",
        "methodism",
        "baptists",
        "anabaptists",
        "unitarians",
        "moravians",
        "anglicans",
        "presbyterians",
        "congregationalists"
    ],
    "tests": {
        "right": [
            "Quakers",
            "Quaker",
            "Religious Society of Friends",
            "Society of Friends",
            "Quackers",
            "Quakerism"
        ],
        "prompt": [
            "Friends"
        ],
        "wrong": [
            "Shakers",
            "Earthquakes",
            "Quakes",
            "Puritans",
            "Amish",
            "Mennonites",
            "Methodists"
        ]
    },
    "mediaPending": True,
    "media": [],
    "wiki": "https://en.wikipedia.org/wiki/Quakers",
    "qb": {
        "q": "Quakers",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In 1650, a judge in Derby named Gervase Bennet [“JER-vus BEN-it”] mocked this group with its best-known nickname after its founder told him to “tremble at the word of the Lord.” Early members of this group called themselves “Children of the Light.”",
            "r": "For 10 points, name this Christian group founded by George Fox, known for its silent meetings for worship."
        },
        {
            "p": "In 1652, this group’s founder climbed Pendle Hill in northern England and had a vision of “a great people to be gathered.” A few weeks later, he preached to about a thousand people on a hillside called Firbank Fell, an event often seen as this group’s true beginning.",
            "r": "That founder, George Fox, taught that there is “that of God in every one.” For 10 points, name this Christian group that worships in silence."
        },
        {
            "p": "Margaret Fell, often called this group’s “mother,” made her home, Swarthmoor [“SWORTH-moor”] Hall, a center for its early traveling preachers, and she later married its founder. She wrote a 1666 pamphlet, _Women’s Speaking Justified_, defending the right of women to preach.",
            "r": "Her husband, George Fox, founded this group. For 10 points, name this Christian denomination known for its silent meetings."
        },
        {
            "p": "Mary Dyer was hanged on Boston Common in 1660 for returning to Massachusetts Bay Colony after its Puritan leaders had banished her for belonging to this group. A statue of her stands outside the Massachusetts State House.",
            "r": "Puritans disliked this group’s belief that God speaks to every person directly. For 10 points, name this group founded by George Fox."
        },
        {
            "p": "While imprisoned in the Tower of London, a member of this group wrote _No Cross, No Crown_. In 1681, King Charles II paid off a debt owed to that writer’s father, an admiral, by granting the writer a huge tract of land in America.",
            "r": "That writer, William Penn, founded Pennsylvania as a “Holy Experiment” for this persecuted group. For 10 points, name this Christian group known for its silent worship."
        },
        {
            "p": "Benjamin West painted a member of this group making a treaty with the Lenape [“leh-NAH-pay”] people beneath a great elm tree at Shackamaxon [“shack-uh-MAX-un”]. That man named his new colony’s capital Philadelphia, from Greek words meaning “brotherly love.”",
            "r": "That man, William Penn, belonged to this group. For 10 points, name this Christian group known for refusing to swear oaths."
        },
        {
            "p": "In 1688, four members of this group in the settlement of Germantown signed one of the first written protests against slavery in the English colonies. In the next century, John Woolman traveled from meeting to meeting, urging fellow believers to free the people they enslaved.",
            "r": "This group became early leaders of the abolitionist movement. For 10 points, name this Christian group whose most famous colonist was William Penn."
        },
        {
            "p": "Levi Coffin, nicknamed the “President of the Underground Railroad,” and Thomas Garrett, who helped Harriet Tubman in Wilmington, Delaware, both belonged to this religious group. In the 1700s, its members became some of the first Americans to forbid slaveholding among themselves.",
            "r": "For 10 points, name this Christian group founded by George Fox, whose members worship in silent meetings."
        },
        {
            "p": "The minister Lucretia Mott, who helped organize the 1848 Seneca Falls Convention, belonged to this group, and Susan B. Anthony was raised in it. Alice Paul, who wrote the Equal Rights Amendment, also came from this group, which allowed women to preach from its earliest days.",
            "r": "For 10 points, name this religious group that William Penn joined as a young man."
        },
        {
            "p": "Elizabeth Fry, whose portrait appeared on the Bank of England’s five-pound note, worked to improve conditions for women prisoners at Newgate Prison as a member of this group. The families who founded the Cadbury and Rowntree chocolate companies also belonged to it.",
            "r": "For 10 points, name this Christian group founded in England by George Fox, known for its silent worship."
        },
        {
            "p": "In 1947, the Nobel Peace Prize went to two service committees, one based in London and one in Philadelphia, that represented this group. The American committee had been founded in 1917 so that conscientious objectors from this group could do relief work instead of fighting in World War I.",
            "r": "Members of this group follow a “peace testimony” against all war. For 10 points, name this Christian group founded by George Fox."
        },
        {
            "p": "Herbert Hoover was born into this religious group in West Branch, Iowa, and Richard Nixon graduated from a college it founded in Whittier, California. That college was named for the abolitionist poet John Greenleaf Whittier, who also belonged to this group.",
            "r": "For 10 points, name this religious group, whose member William Penn founded Pennsylvania as a refuge for it."
        },
        {
            "p": "This group’s founder dismissed church buildings as “steeplehouses,” and its members worship in plain meetinghouses with no altar. At business meetings, they make decisions without voting, as a member called the clerk waits for a shared “sense of the meeting.”",
            "r": "In many of its worship meetings, members sit in silence until someone feels moved to speak. For 10 points, name this Christian group founded by George Fox."
        },
        {
            "p": "Early members of this group refused to take off their hats for judges or nobles and called everyone “thee” and “thou” to show that all people are equal. They also refused to swear oaths, and they traditionally called Sunday “First Day” to avoid day names with pagan roots.",
            "r": "A famous oatmeal brand named for this group has no ties to it. For 10 points, name this Christian group founded by George Fox."
        },
        {
            "p": "Robert Barclay’s _Apology for the True Christian Divinity_ became the classic defense of this group’s beliefs, including the idea of an “Inward Light” in every person. In 1660, members of this group told King Charles II that they utterly rejected fighting “with outward weapons.”",
            "r": "Bayard Rustin, who organized the 1963 March on Washington, belonged to this pacifist group. For 10 points, name this Christian group founded by George Fox."
        }
    ],
    "clues": [
        {
            "id": "george-fox",
            "tier": "giveaway",
            "t": "Founded by George Fox in England in the mid-1600s",
            "k": ["george fox", "fox", "england"],
            "n": 0
        },
        {
            "id": "silent-worship",
            "tier": "giveaway",
            "t": "Known for silent worship: people sit quietly in a meetinghouse until someone feels moved to speak",
            "k": ["silent", "meetinghouse", "moved to speak"],
            "n": 0
        },
        {
            "id": "penn",
            "tier": "giveaway",
            "t": "William Penn, a member, founded Pennsylvania (1681) as a refuge for them, a “Holy Experiment”",
            "k": ["william penn", "pennsylvania", "holy experiment"],
            "n": 0,
            "rabbit": "Pennsylvania"
        },
        {
            "id": "pacifism",
            "tier": "giveaway",
            "t": "Pacifists: their “peace testimony” rejects all war, and many have been conscientious objectors",
            "k": ["peace testimony", "pacifists", "conscientious objectors"],
            "n": 0
        },
        {
            "id": "inner-light",
            "tier": "middle",
            "t": "Believe in an Inner (or Inward) Light, “that of God in every one,” so many meetings have no paid minister",
            "k": ["inner", "inward light", "that of god", "minister"],
            "n": 0
        },
        {
            "id": "abolition",
            "tier": "middle",
            "t": "Early leaders of abolition; Levi Coffin and Thomas Garrett helped freedom seekers on the Underground Railroad",
            "k": ["abolition", "underground railroad", "levi coffin", "thomas garrett"],
            "n": 0,
            "rabbit": "Underground Railroad"
        },
        {
            "id": "womens-rights",
            "tier": "middle",
            "t": "Women could preach from the start; Lucretia Mott helped organize Seneca Falls (1848), and Susan B. Anthony and Alice Paul grew up in the group",
            "k": ["lucretia mott", "seneca falls", "alice paul", "women"],
            "n": 0,
            "rabbit": "Seneca Falls Convention"
        },
        {
            "id": "nobel",
            "tier": "middle",
            "t": "1947 Nobel Peace Prize to its British and American service committees (the American one was founded in 1917)",
            "k": ["nobel peace prize", "1947", "service committees"],
            "n": 0
        },
        {
            "id": "plain-speech",
            "tier": "middle",
            "t": "Plain speech: “thee” and “thou” for everyone, no hat-raising for nobles, no oaths, and “First Day” for Sunday",
            "k": ["thee", "thou", "oaths", "first day"],
            "n": 0
        },
        {
            "id": "philadelphia",
            "tier": "middle",
            "t": "Penn named Philadelphia (“brotherly love”) and made a treaty with the Lenape, painted by Benjamin West",
            "k": ["philadelphia", "brotherly love", "lenape", "benjamin west"],
            "n": 0
        },
        {
            "id": "presidents",
            "tier": "middle",
            "t": "Presidents Herbert Hoover (born in West Branch, Iowa) and Richard Nixon (Whittier College) were raised in it",
            "k": ["herbert hoover", "richard nixon", "whittier"],
            "n": 0,
            "rabbit": "Herbert Hoover"
        },
        {
            "id": "oatmeal",
            "tier": "middle",
            "t": "A famous oatmeal brand is named for the group but has no ties to it",
            "k": ["oatmeal", "brand"],
            "n": 0
        },
        {
            "id": "tremble",
            "tier": "power",
            "t": "Nickname from Judge Gervase Bennet (1650), after Fox told him to “tremble at the word of the Lord”; early name: “Children of the Light”",
            "k": ["tremble", "gervase bennet", "children of the light"],
            "n": 0
        },
        {
            "id": "pendle-hill",
            "tier": "power",
            "t": "Fox’s 1652 vision on Pendle Hill of “a great people to be gathered”; he then preached at Firbank Fell",
            "k": ["pendle hill", "firbank fell", "1652"],
            "n": 0
        },
        {
            "id": "margaret-fell",
            "tier": "power",
            "t": "Margaret Fell, the movement’s “mother,” hosted preachers at Swarthmoor Hall, wrote _Women’s Speaking Justified_ (1666), and married Fox",
            "k": ["margaret fell", "swarthmoor", "speaking justified"],
            "n": 0
        },
        {
            "id": "mary-dyer",
            "tier": "power",
            "t": "Mary Dyer was hanged on Boston Common (1660) for returning to Puritan Massachusetts after being banished",
            "k": ["mary dyer", "boston common", "1660", "banished"],
            "n": 0
        },
        {
            "id": "no-cross",
            "tier": "power",
            "t": "Penn wrote _No Cross, No Crown_ in the Tower of London; Charles II granted him land to repay a debt to Penn’s father, an admiral",
            "k": ["no cross, no crown", "tower of london", "charles ii", "debt"],
            "n": 0
        },
        {
            "id": "germantown",
            "tier": "power",
            "t": "1688 Germantown petition: one of the first written protests against slavery in the English colonies",
            "k": ["germantown", "1688", "petition"],
            "n": 0
        },
        {
            "id": "woolman",
            "tier": "power",
            "t": "John Woolman traveled among meetings urging members to free the people they enslaved",
            "k": ["john woolman", "woolman"],
            "n": 0
        },
        {
            "id": "elizabeth-fry",
            "tier": "power",
            "t": "Elizabeth Fry improved conditions for women prisoners at Newgate Prison and appeared on the five-pound note",
            "k": ["elizabeth fry", "newgate", "five-pound note"],
            "n": 0
        },
        {
            "id": "chocolate",
            "tier": "power",
            "t": "The families who founded the Cadbury and Rowntree chocolate companies were members",
            "k": ["cadbury", "rowntree", "chocolate"],
            "n": 0
        },
        {
            "id": "steeplehouses",
            "tier": "power",
            "t": "Fox called churches “steeplehouses”; business meetings decide by the “sense of the meeting,” without voting, guided by a clerk",
            "k": ["steeplehouses", "sense of the meeting", "clerk"],
            "n": 0
        },
        {
            "id": "barclay",
            "tier": "power",
            "t": "Robert Barclay’s _Apology for the True Christian Divinity_ was the classic defense of its beliefs",
            "k": ["robert barclay", "barclay", "apology"],
            "n": 0
        },
        {
            "id": "outward-weapons",
            "tier": "power",
            "t": "A 1660 declaration to Charles II rejected fighting “with outward weapons,” the root of its peace testimony",
            "k": ["outward weapons", "declaration", "1660"],
            "n": 0
        },
        {
            "id": "rustin",
            "tier": "power",
            "t": "Bayard Rustin, who organized the 1963 March on Washington, was a member",
            "k": ["bayard rustin", "march on washington"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Quakers, not Shakers",
        "body": "Several Protestant groups from England and colonial America get mixed up. The Shakers began as an offshoot nicknamed the “Shaking Quakers” and became famous for celibate communities, simple furniture, and the song “Simple Gifts.” The Puritans were the group that banished and hanged Quakers in Massachusetts, and Pennsylvania clues can tempt players to name the Amish or Mennonites, German-speaking groups who also settled there.",
        "fix": "George Fox, William Penn, silent meetings, the Inner Light, “thee” and “thou,” and the 1947 Nobel Peace Prize mean the Quakers. Ann Lee and “Simple Gifts” mean the Shakers; Jakob Ammann and horse-drawn buggies mean the Amish; John Winthrop’s “city upon a hill” means the Puritans.",
        "line": "Real answer line: <b><u>Quakers</u></b> (or Religious <b><u>Society of Friends</u></b>; accept <u>Friends</u> Church; do not accept “Shakers”)"
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
