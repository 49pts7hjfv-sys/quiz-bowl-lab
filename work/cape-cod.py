import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "cape-cod",
    "name": "Cape Cod",
    "mono": "CC",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Hook-shaped Massachusetts peninsula · The Pilgrims’ first landfall, 1620",
    "dates": "Named 1602; Pilgrims landed 1620",
    "briefing": "Cape Cod is a hook-shaped peninsula in Massachusetts that curls out into the Atlantic Ocean like a bent arm. In 1602, the English explorer Bartholomew Gosnold named it for the codfish his crew caught there, and in November 1620 the _Mayflower_ anchored at its tip, where the Pilgrims signed the Mayflower Compact before settling at Plymouth. Later it became home to Marconi’s wireless station, the Kennedy family’s summer houses, and a national seashore.",
    "answerHtml": "<b><u>Cape Cod</u></b> (prompt on <u>Cape</u>; do not accept “Massachusetts”)",
    "accept": [
        "cape cod",
        "cape cod peninsula",
        "the cape cod peninsula",
        "cape cod massachusetts",
        "cape cod ma"
    ],
    "prompt": [
        "cape",
        "the cape",
        "barnstable county"
    ],
    "reject": [
        "cape ann",
        "cape cod bay",
        "cape cod canal",
        "cape canaveral",
        "cape hatteras",
        "cape may",
        "cape horn",
        "cape of good hope",
        "cape henry",
        "cape fear",
        "cape charles",
        "marthas vineyard",
        "nantucket",
        "nantucket island",
        "elizabeth islands",
        "cuttyhunk",
        "plymouth",
        "plymouth rock",
        "plymouth colony",
        "provincetown",
        "hyannis",
        "hyannis port",
        "long island",
        "boston",
        "massachusetts bay",
        "massachusetts bay colony",
        "mayflower"
    ],
    "mediaPending": True,
    "media": [],
    "wiki": "https://en.wikipedia.org/wiki/Cape_Cod",
    "qb": {
        "q": "Cape Cod",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "On the same 1602 voyage on which he named this place, an English explorer built a short-lived trading post on Cuttyhunk Island and named nearby Martha’s Vineyard. Five years later, he died at Jamestown, a colony he had helped organize.",
            "r": "That explorer, Bartholomew Gosnold, named this place for the fish his crew caught there. For 10 points, name this hook-shaped Massachusetts peninsula."
        },
        {
            "p": "At a place later called Corn Hill, explorers took corn that Native people had stored in the ground. Weeks later, at a spot now called First Encounter Beach, those explorers had a brief clash with Nauset men in December 1620, but no one was killed.",
            "r": "Those explorers had arrived on the _Mayflower_. For 10 points, name this Massachusetts peninsula where the Pilgrims first landed in 1620."
        },
        {
            "p": "Theodore Roosevelt laid the cornerstone of a granite tower on this peninsula in 1907, and the tower was finished in 1910. That tower, the Pilgrim Monument, rises above the town of Provincetown at this peninsula’s tip.",
            "r": "It honors the Pilgrims, whose _Mayflower_ first anchored here in 1620. For 10 points, name this Massachusetts peninsula."
        },
        {
            "p": "Peregrine White, the first English child born in New England, was born aboard a ship anchored off this peninsula in November 1620. Days earlier, forty-one men had signed a famous agreement aboard that ship in the harbor at this peninsula’s tip.",
            "r": "That ship was the _Mayflower_. For 10 points, name this Massachusetts peninsula where the Pilgrims landed before settling at Plymouth."
        },
        {
            "p": "On January 18, 1903, Guglielmo Marconi’s wireless station at South Wellfleet on this peninsula sent a greeting from Theodore Roosevelt to King Edward VII. The king’s reply made it one of the first two-way wireless exchanges across the Atlantic.",
            "r": "That site later became part of a national seashore created by John F. Kennedy. For 10 points, name this hook-shaped Massachusetts peninsula."
        },
        {
            "p": "August Belmont Jr.’s company opened a canal across this peninsula’s base in 1914, and the federal government bought it in 1928. In 1935, the Bourne and Sagamore Bridges opened to carry cars over that canal.",
            "r": "That canal lets ships avoid sailing around its dangerous outer shore. For 10 points, name this Massachusetts peninsula, where the _Mayflower_ first anchored in 1620."
        },
        {
            "p": "In 1961, John F. Kennedy signed a law creating a national seashore that protects about forty miles of this peninsula’s beaches, dunes, and marshes. Kennedy’s family had long spent summers in a group of houses at Hyannis Port here.",
            "r": "For 10 points, name this Massachusetts peninsula, which the explorer Bartholomew Gosnold named for a fish."
        },
        {
            "p": "“A man may stand there and put all America behind him,” wrote Henry David Thoreau about the outer beach of this peninsula. Thoreau’s book about walking its shores was published in 1865, three years after his death.",
            "r": "That book shares its name with this place. For 10 points, name this Massachusetts peninsula, where the Pilgrims first landed."
        },
        {
            "p": "Henry Beston spent a year living in a small cottage on a beach in Eastham on this peninsula and described the seasons there in _The Outermost House_. A blizzard washed that cottage out to sea in 1978.",
            "r": "For 10 points, name this hook-shaped Massachusetts peninsula, home to a national seashore and the town of Provincetown."
        },
        {
            "p": "In 1984, divers led by Barry Clifford found the wreck of the _Whydah_, a pirate ship that sank in a storm off this peninsula in 1717. The ship’s captain, “Black Sam” Bellamy, died in the wreck along with most of his crew.",
            "r": "For 10 points, name this Massachusetts peninsula, at whose tip lies the town of Provincetown, where the Pilgrims first landed."
        },
        {
            "p": "In 2007, the Mashpee Wampanoag [“wahm-puh-NOH-ag”] Tribe of this peninsula was recognized as a tribe by the U.S. government. The Nauset, a related people, lived on the outer part of this peninsula when English settlers arrived.",
            "r": "For 10 points, name this Massachusetts peninsula where the _Mayflower_ anchored in 1620, before the Pilgrims settled at Plymouth."
        },
        {
            "p": "This landform was built from sand and gravel left behind by melting glaciers at the end of the last ice age. Its shape is often compared to a bent arm, with its “elbow” at Chatham and its “fist” at Provincetown.",
            "r": "For 10 points, name this Massachusetts peninsula, where the Pilgrims first anchored in 1620 aboard the _Mayflower_."
        },
        {
            "p": "Around 1816, Captain Henry Hall of the town of Dennis is said to have started growing cranberries as a crop on this peninsula. Its oldest town, Sandwich, was incorporated in 1639, when the area belonged to Plymouth Colony.",
            "r": "For 10 points, name this hook-shaped peninsula in Massachusetts, named for a fish that early explorers caught there."
        },
        {
            "p": "In 1916, the Provincetown Players staged Eugene O’Neill’s first play to be performed, _Bound East for Cardiff_, in a fishing-wharf theater on this peninsula. The painter Edward Hopper later spent decades of summers working at his studio in Truro here.",
            "r": "For 10 points, name this Massachusetts peninsula, where the Kennedy family kept summer homes at Hyannis Port."
        },
        {
            "p": "In 1952, four Coast Guardsmen in a small lifeboat from Chatham rescued 32 sailors from the tanker _Pendleton_, which had broken in two during a storm off this peninsula. That rescue is the subject of the 2016 film _The Finest Hours_.",
            "r": "For 10 points, name this Massachusetts peninsula, where the Pilgrims first landed in 1620 before moving on to Plymouth."
        }
    ],
    "clues": [
        {
            "id": "hook-peninsula",
            "tier": "giveaway",
            "t": "Hook-shaped peninsula in southeastern Massachusetts, curling into the Atlantic like a bent arm",
            "k": ["hook-shaped", "peninsula", "bent arm", "massachusetts"],
            "n": 0
        },
        {
            "id": "mayflower-1620",
            "tier": "giveaway",
            "t": "The _Mayflower_ anchored at its tip in November 1620, before the Pilgrims settled at Plymouth",
            "k": ["mayflower", "november 1620", "pilgrims", "plymouth"],
            "n": 0,
            "rabbit": "Mayflower"
        },
        {
            "id": "gosnold",
            "tier": "giveaway",
            "t": "Named in 1602 by English explorer Bartholomew Gosnold for the codfish his crew caught there",
            "k": ["bartholomew gosnold", "gosnold", "codfish", "1602"],
            "n": 0
        },
        {
            "id": "kennedys",
            "tier": "giveaway",
            "t": "The Kennedy family kept summer homes at Hyannis Port, John F. Kennedy’s “Summer White House”",
            "k": ["summer white house", "hyannis port", "kennedy"],
            "n": 0,
            "rabbit": "John F. Kennedy"
        },
        {
            "id": "compact",
            "tier": "middle",
            "t": "The Mayflower Compact was signed aboard ship in what is now Provincetown Harbor, at the very tip",
            "k": ["mayflower compact", "provincetown"],
            "n": 0,
            "rabbit": "Plymouth Colony"
        },
        {
            "id": "canal-1914",
            "tier": "middle",
            "t": "A canal opened across its base in 1914, so ships no longer had to sail around its dangerous outer shore",
            "k": ["canal", "1914", "outer shore"],
            "n": 0
        },
        {
            "id": "national-seashore",
            "tier": "middle",
            "t": "John F. Kennedy signed the law creating its national seashore in 1961",
            "k": ["national seashore", "1961"],
            "n": 0
        },
        {
            "id": "marconi",
            "tier": "middle",
            "t": "Guglielmo Marconi’s station at South Wellfleet exchanged wireless messages with Britain in 1903",
            "k": ["marconi", "wellfleet", "wireless", "1903"],
            "n": 0
        },
        {
            "id": "glaciers",
            "tier": "middle",
            "t": "Built from moraines and other sand and gravel left by melting glaciers at the end of the last ice age",
            "k": ["moraines", "glaciers", "ice age"],
            "n": 0,
            "rabbit": "Moraines"
        },
        {
            "id": "wampanoag",
            "tier": "middle",
            "t": "Homeland of Wampanoag peoples; the Nauset lived on the outer part, and the Mashpee Wampanoag Tribe won federal recognition in 2007",
            "k": ["mashpee", "wampanoag", "nauset", "2007"],
            "n": 0
        },
        {
            "id": "first-encounter",
            "tier": "middle",
            "t": "Pilgrim explorers took stored corn at Corn Hill and clashed with Nauset men at First Encounter Beach (December 1620)",
            "k": ["first encounter", "corn hill", "december 1620"],
            "n": 0
        },
        {
            "id": "thoreau",
            "tier": "middle",
            "t": "Henry David Thoreau wrote a book about walking its beaches (1865): “A man may stand there and put all America behind him”",
            "k": ["america behind him", "thoreau", "1865"],
            "n": 0
        },
        {
            "id": "cuttyhunk",
            "tier": "power",
            "t": "On his 1602 voyage, Gosnold also named Martha’s Vineyard and built a short-lived post on Cuttyhunk Island; he later died at Jamestown",
            "k": ["martha’s vineyard", "cuttyhunk", "jamestown"],
            "n": 0,
            "rabbit": "Jamestown"
        },
        {
            "id": "pilgrim-monument",
            "tier": "power",
            "t": "Theodore Roosevelt laid the cornerstone (1907) of the Pilgrim Monument, a granite tower in Provincetown finished in 1910",
            "k": ["pilgrim monument", "cornerstone", "1910", "1907"],
            "n": 0
        },
        {
            "id": "peregrine",
            "tier": "power",
            "t": "Peregrine White, the first English child born in New England, was born aboard the _Mayflower_ while it lay at anchor here",
            "k": ["peregrine white", "first english child", "peregrine"],
            "n": 0
        },
        {
            "id": "roosevelt-edward",
            "tier": "power",
            "t": "Marconi’s station sent Theodore Roosevelt’s greeting to King Edward VII on January 18, 1903",
            "k": ["edward vii", "january 18", "greeting"],
            "n": 0
        },
        {
            "id": "belmont-bridges",
            "tier": "power",
            "t": "August Belmont Jr.’s company built the canal; the government bought it in 1928, and the Bourne and Sagamore Bridges opened in 1935",
            "k": ["august belmont", "belmont", "sagamore", "bourne"],
            "n": 0
        },
        {
            "id": "outermost-house",
            "tier": "power",
            "t": "Henry Beston’s _The Outermost House_ describes a year in his beach cottage in Eastham; a 1978 blizzard washed the cottage away",
            "k": ["outermost house", "henry beston", "eastham", "1978"],
            "n": 0
        },
        {
            "id": "whydah",
            "tier": "power",
            "t": "The pirate ship _Whydah_ of “Black Sam” Bellamy sank off its coast in 1717; Barry Clifford’s divers found it in 1984",
            "k": ["whydah", "bellamy", "black sam", "1984"],
            "n": 0
        },
        {
            "id": "sandwich",
            "tier": "power",
            "t": "Its oldest town, Sandwich, was incorporated in 1639, when the area belonged to Plymouth Colony",
            "k": ["sandwich", "oldest town", "1639"],
            "n": 0
        },
        {
            "id": "cranberries",
            "tier": "power",
            "t": "Captain Henry Hall of Dennis is said to have begun growing cranberries as a crop here around 1816",
            "k": ["cranberries", "henry hall", "dennis", "1816"],
            "n": 0
        },
        {
            "id": "provincetown-players",
            "tier": "power",
            "t": "The Provincetown Players staged Eugene O’Neill’s _Bound East for Cardiff_ in a wharf theater in 1916",
            "k": ["provincetown players", "bound east for cardiff", "eugene o’neill", "1916"],
            "n": 0
        },
        {
            "id": "hopper",
            "tier": "power",
            "t": "Painter Edward Hopper spent decades of summers working at his studio in Truro",
            "k": ["edward hopper", "hopper", "truro"],
            "n": 0
        },
        {
            "id": "pendleton",
            "tier": "power",
            "t": "In 1952, four Coast Guardsmen from Chatham rescued 32 sailors from the broken tanker _Pendleton_ (_The Finest Hours_, 2016)",
            "k": ["pendleton", "finest hours", "chatham", "coast guardsmen"],
            "n": 0
        },
        {
            "id": "fifteen-towns",
            "tier": "power",
            "t": "Its fifteen towns make up Barnstable County",
            "k": ["barnstable county", "fifteen towns", "barnstable"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Peninsula, not state",
        "body": "Cape Cod questions are full of places that are answer lines of their own: Massachusetts (the state it belongs to), Plymouth Colony (where the Pilgrims settled after leaving the Cape), and the _Mayflower_ (their ship). Nearby islands such as Martha’s Vineyard and Nantucket, and other capes like Cape Ann and Cape Canaveral, are also wrong.",
        "fix": "If the question says “this peninsula” or “this cape,” answer Cape Cod, not Massachusetts or Plymouth. Where the _Mayflower_ first anchored, Provincetown, Hyannis Port, Wellfleet, and Bartholomew Gosnold’s codfish all point to Cape Cod. Saying only “the Cape” earns a prompt, so add “Cod.”",
        "line": "Real answer line: <b><u>Cape Cod</u></b> (prompt on <u>Cape</u>; do not accept “Massachusetts”)"
    },
    "tests": {
        "right": [
            "Cape Cod",
            "Cape Cod, Massachusetts",
            "Cape Codd",
            "Cape Cod Peninsula",
            "the Cape Cod peninsula"
        ],
        "prompt": [
            "the Cape",
            "Cape"
        ],
        "wrong": [
            "Massachusetts",
            "Plymouth",
            "Cape Ann",
            "Martha's Vineyard",
            "Nantucket",
            "Cape Canaveral",
            "Provincetown",
            "Long Island",
            "Cape Cod Canal"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", data["id"])
