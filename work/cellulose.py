import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "cellulose",
    "name": "Cellulose",
    "mono": "CEL",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Glucose chains in plant cell walls · Most abundant organic compound",
    "dates": "Discovered 1838",
    "briefing": "Cellulose is the tough material that gives plants their strength: long chains of thousands of glucose units, bundled into fibers that build plant cell walls. It is the most abundant organic compound on Earth and makes up most of cotton and paper and much of wood. Humans cannot digest it, so it passes through us as fiber, but cows and termites rely on tiny microbes in their guts to break it down.",
    "answerHtml": "<b><u>Cellulose</u></b> (prompt on <u>fiber</u> or <u>polysaccharide</u>; do not accept “cellulase,” “starch,” or “chitin”)",
    "accept": [
        "cellulose",
        "celluloses",
        "cellulose fiber",
        "cellulose fibers",
        "cellulose fibre",
        "cellulose fibres"
    ],
    "prompt": [
        "fiber",
        "fibre",
        "dietary fiber",
        "dietary fibre",
        "insoluble fiber",
        "roughage",
        "polysaccharide",
        "polysaccharides",
        "carbohydrate",
        "carbohydrates",
        "glucose polymer"
    ],
    "reject": [
        "cellulase",
        "cellulases",
        "celluloid",
        "cellobiose",
        "cellulose acetate",
        "cellulose nitrate",
        "cellulose synthase",
        "nitrocellulose",
        "hemicellulose",
        "hemicelluloses",
        "methylcellulose",
        "starch",
        "amylose",
        "amylopectin",
        "glycogen",
        "chitin",
        "lignin",
        "pectin",
        "cell wall",
        "cell walls",
        "glucose",
        "sucrose",
        "cellophane",
        "rayon",
        "cotton",
        "paper",
        "wood",
        "peptidoglycan",
        "keratin",
        "collagen"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Cellulose",
    "qb": {
        "q": "cellulose",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "French chemist Anselme Payen [“pah-YAN”] isolated this substance from plant material in 1838 and worked out its chemical formula. Unlike starch, which is built from the same sugar, this substance cannot be broken down by the enzymes in the human gut.",
            "r": "So it passes through the body as dietary fiber. For 10 points, name this polysaccharide that forms plant cell walls."
        },
        {
            "p": "Christian Schönbein [“SHURN-bine”] invented an explosive called guncotton by treating this substance with nitric acid. Other chemical treatments turn this substance into fabrics such as rayon, which was first sold as “artificial silk.”",
            "r": "Cotton is mostly made of this substance. For 10 points, name this polysaccharide that builds plant cell walls."
        },
        {
            "p": "John Wesley Hyatt mixed a nitric acid–treated form of this substance with camphor to make an early plastic meant to replace ivory in billiard balls. That plastic was later used for photographic film and movie film.",
            "r": "This substance itself is a chain of glucose units that forms plant cell walls. For 10 points, name this most abundant organic compound on Earth."
        },
        {
            "p": "Sea squirts, also called tunicates, are the only animals known to make this substance, which forms their tough outer coat, or tunic. Animals such as cows and termites can digest this substance only with help from microbes living in their guts.",
            "r": "For 10 points, name this polysaccharide, made of glucose, that forms the cell walls of plants."
        },
        {
            "p": "Water molds, or oomycetes [“oh-uh-MY-seets”], have cell walls made of this substance instead of chitin, which is one way to tell them apart from true fungi. In plants, chains of this substance bundle into strands called microfibrils.",
            "r": "For 10 points, name this glucose polymer that makes up most of the cell walls of plants."
        },
        {
            "p": "In plants, rosette-shaped enzyme complexes sitting in the cell membrane spin out long chains of this substance, which bundle into microfibrils held together by hydrogen bonds. Each glucose unit in this substance’s chains is flipped relative to its neighbors, keeping the chains straight.",
            "r": "For 10 points, name this polysaccharide that is the main component of plant cell walls."
        },
        {
            "p": "The rubbery mat that forms on top of kombucha and the chewy dessert nata de coco are both made of a pure form of this substance produced by bacteria. Unlike starch, this substance links its glucose units with beta-1,4 bonds.",
            "r": "For 10 points, name this polysaccharide that forms plant cell walls and that humans cannot digest."
        },
        {
            "p": "Many termites depend on protists in their guts, such as _Trichonympha_ [“trik-oh-NIM-fuh”], to break down this substance in the wood they eat. Cows also rely on microbes, which ferment this substance in the rumen, the first chamber of a cow’s stomach.",
            "r": "For 10 points, name this polysaccharide that forms plant cell walls and passes through humans as dietary fiber."
        },
        {
            "p": "Schweizer’s [“SHVY-tserz”] reagent, a deep-blue solution of copper and ammonia, is one of the few liquids that can dissolve this substance. Because hydrogen bonds pack its chains tightly together, this substance does not dissolve in water.",
            "r": "For 10 points, name this polysaccharide that makes up plant cell walls, cotton, and paper."
        },
        {
            "p": "Horses and rabbits ferment this substance in an enlarged pouch called the cecum [“SEE-kum”], where gut microbes break it down. Iodine turns starch blue-black, but it does not stain this other chain of glucose the same way.",
            "r": "For 10 points, name this polysaccharide, the main building material of plant cell walls."
        },
        {
            "p": "Unlike the coiled chains of starch, which use alpha bonds, the glucose units in this substance are linked by beta-1,4 glycosidic [“gly-koh-SID-ik”] bonds into long, straight chains. In wood, fibers of this substance are glued together by a tough polymer called lignin.",
            "r": "For 10 points, name this most abundant organic compound on Earth, which forms plant cell walls."
        },
        {
            "p": "In the kraft process, wood chips are cooked with sodium hydroxide and sodium sulfide to dissolve the lignin and free this substance’s fibers. Every other glucose unit in a chain of this substance is flipped upside down, so the chains stay straight.",
            "r": "This substance is the main ingredient of paper. For 10 points, name this polysaccharide that forms plant cell walls."
        },
        {
            "p": "Count Hilaire de Chardonnet [“shar-doh-NAY”] made an “artificial silk” from this substance in the 1880s. Cows break down this substance by fermenting it in the rumen, the first chamber of the stomach, and by chewing their cud.",
            "r": "For 10 points, name this polysaccharide that forms plant cell walls and makes up most of cotton."
        },
        {
            "p": "Food companies add a powdered form of this substance to shredded cheese to keep the shreds from clumping together. This substance is also the largest single part of wood, where its fibers are bound together by lignin.",
            "r": "For 10 points, name this polysaccharide that is the main part of plant cell walls, cotton, and paper."
        },
        {
            "p": "Chitin, found in insect exoskeletons, has nearly the same structure as this substance, except that each of chitin’s sugars carries a nitrogen-containing group. Both chitin and this substance are tough building materials made of long chains of sugars.",
            "r": "This substance passes through the human body as dietary fiber. For 10 points, name this polysaccharide that builds plant cell walls."
        }
    ],
    "clues": [
        {
            "id": "cell-walls",
            "tier": "giveaway",
            "t": "The main building material of plant cell walls",
            "k": ["cell walls", "building material"],
            "n": 0,
            "rabbit": "Cell wall"
        },
        {
            "id": "glucose-chains",
            "tier": "giveaway",
            "t": "A polysaccharide: a long, unbranched chain of thousands of glucose units",
            "k": ["polysaccharide", "glucose", "unbranched"],
            "n": 0,
            "rabbit": "Glucose"
        },
        {
            "id": "most-abundant",
            "tier": "giveaway",
            "t": "The most abundant organic compound on Earth",
            "k": ["most abundant", "organic compound"],
            "n": 0
        },
        {
            "id": "dietary-fiber",
            "tier": "giveaway",
            "t": "Humans cannot digest it, so it passes through the body as dietary fiber (roughage)",
            "k": ["dietary fiber", "roughage", "digest"],
            "n": 0
        },
        {
            "id": "cotton-paper",
            "tier": "giveaway",
            "t": "Cotton is about 90 percent this substance, and it is the main ingredient of paper",
            "k": ["cotton", "paper", "90 percent"],
            "n": 0,
            "rabbit": "Cotton"
        },
        {
            "id": "beta-bonds",
            "tier": "middle",
            "t": "Its glucose units are joined by beta-1,4 glycosidic bonds; starch uses alpha bonds instead",
            "k": ["beta-1,4", "glycosidic", "alpha"],
            "n": 0
        },
        {
            "id": "flipped",
            "tier": "middle",
            "t": "Every other glucose unit in the chain is flipped upside down, so the chain stays straight",
            "k": ["flipped", "straight"],
            "n": 0
        },
        {
            "id": "microfibrils",
            "tier": "middle",
            "t": "Hydrogen bonds hold neighboring chains together into strong microfibrils that do not dissolve in water",
            "k": ["hydrogen bonds", "microfibrils", "dissolve"],
            "n": 0,
            "rabbit": "Hydrogen bonds"
        },
        {
            "id": "gut-microbes",
            "tier": "middle",
            "t": "Cows, termites, and other plant-eaters digest it only with help from microbes living in their guts",
            "k": ["gut microbes", "microbes", "termites"],
            "n": 0
        },
        {
            "id": "rumen",
            "tier": "middle",
            "t": "Cows ferment it in the rumen, the first chamber of their stomach, and chew their cud",
            "k": ["rumen", "cud"],
            "n": 0,
            "rabbit": "Stomach"
        },
        {
            "id": "lignin",
            "tier": "middle",
            "t": "In wood, its fibers are glued together by a tough polymer called lignin",
            "k": ["lignin", "wood"],
            "n": 0,
            "rabbit": "Trees"
        },
        {
            "id": "rayon-cellophane",
            "tier": "middle",
            "t": "Treated with chemicals, it can be turned into rayon fabric and clear cellophane wrap",
            "k": ["rayon", "cellophane"],
            "n": 0
        },
        {
            "id": "starch-iodine",
            "tier": "middle",
            "t": "Plants store glucose as starch but build with this; iodine turns starch blue-black but not this",
            "k": ["starch", "iodine"],
            "n": 0
        },
        {
            "id": "chitin",
            "tier": "middle",
            "t": "Fungi and insects build with chitin, a similar chain whose sugars carry a nitrogen-containing group",
            "k": ["chitin", "nitrogen"],
            "n": 0,
            "rabbit": "Fungi"
        },
        {
            "id": "payen",
            "tier": "power",
            "t": "French chemist Anselme Payen isolated it from plant material in 1838",
            "k": ["anselme payen", "payen", "1838"],
            "n": 0
        },
        {
            "id": "guncotton",
            "tier": "power",
            "t": "Christian Schönbein made the explosive guncotton by treating it with nitric acid",
            "k": ["guncotton", "schönbein", "nitric acid"],
            "n": 0
        },
        {
            "id": "hyatt",
            "tier": "power",
            "t": "John Wesley Hyatt mixed a nitrated form with camphor to make an early plastic for billiard balls, later used for film",
            "k": ["hyatt", "camphor", "billiard balls"],
            "n": 0
        },
        {
            "id": "chardonnet",
            "tier": "power",
            "t": "Count Hilaire de Chardonnet made an “artificial silk” from it in the 1880s",
            "k": ["chardonnet", "artificial silk"],
            "n": 0
        },
        {
            "id": "tunicates",
            "tier": "power",
            "t": "Tunicates (sea squirts) are the only animals known to make it, in their tough outer tunic",
            "k": ["tunicates", "sea squirts", "tunic"],
            "n": 0,
            "rabbit": "Chordates"
        },
        {
            "id": "oomycetes",
            "tier": "power",
            "t": "Water molds (oomycetes) have walls of it instead of chitin, one way to tell them from true fungi",
            "k": ["oomycetes", "water molds"],
            "n": 0
        },
        {
            "id": "rosettes",
            "tier": "power",
            "t": "Rosette-shaped enzyme complexes in the cell membrane spin out its chains",
            "k": ["rosette-shaped", "rosette", "cell membrane"],
            "n": 0,
            "rabbit": "Cell membrane"
        },
        {
            "id": "kombucha",
            "tier": "power",
            "t": "Bacteria make a pure form of it: the rubbery mat on kombucha and the dessert nata de coco",
            "k": ["kombucha", "nata de coco"],
            "n": 0
        },
        {
            "id": "trichonympha",
            "tier": "power",
            "t": "Termites depend on gut protists such as _Trichonympha_ to break it down",
            "k": ["trichonympha", "protists"],
            "n": 0
        },
        {
            "id": "schweizer",
            "tier": "power",
            "t": "Schweizer’s reagent, a deep-blue copper and ammonia solution, can dissolve it",
            "k": ["schweizer", "copper", "ammonia"],
            "n": 0
        },
        {
            "id": "cecum",
            "tier": "power",
            "t": "Horses and rabbits ferment it in an enlarged pouch of the gut called the cecum",
            "k": ["cecum", "horses", "rabbits"],
            "n": 0
        },
        {
            "id": "kraft",
            "tier": "power",
            "t": "The kraft process cooks wood chips with sodium hydroxide and sodium sulfide to free its fibers from lignin for pulp",
            "k": ["kraft process", "kraft", "pulp"],
            "n": 0
        },
        {
            "id": "cheese",
            "tier": "power",
            "t": "A powdered form is added to shredded cheese to keep the shreds from clumping",
            "k": ["shredded cheese", "clumping"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Cellulose, not cellulase",
        "body": "Cellulose is the fiber itself, while cellulase (ending in “-ase,” like most enzymes) is the enzyme that breaks it down, and a one-letter slip changes the answer. Starch and glycogen are the other traps: they are also chains of glucose, but they are energy stores that our bodies can digest, while cellulose is a building material we cannot digest. Chitin is the look-alike building material of fungi and insect shells.",
        "fix": "Plant cell walls, fiber, cotton, paper, wood, termites, and beta bonds mean cellulose. Food storage in potatoes and seeds means starch; storage in liver and muscle means glycogen; exoskeletons and mushrooms mean chitin. Spell and say it with “-ose,” the ending for sugars.",
        "line": "Real answer line: <b><u>Cellulose</u></b> (prompt on <u>fiber</u> or <u>polysaccharide</u>; do not accept “cellulase”)"
    },
    "tests": {
        "right": [
            "Cellulose",
            "cellulose",
            "Celulose",
            "Cellulose fibers",
            "Cellulos"
        ],
        "prompt": [
            "Fiber",
            "Polysaccharide"
        ],
        "wrong": [
            "Cellulase",
            "Starch",
            "Chitin",
            "Lignin",
            "Glycogen",
            "Celluloid"
        ]
    }
}

out = ROOT / "topics" / "cellulose.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", out)
