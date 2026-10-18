import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

data = {
    "id": "galaxies",
    "name": "Galaxies",
    "mono": "GAL",
    "category": "Astronomy",
    "qbCategory": "Science · Other Science (Astronomy)",
    "kicker": "Huge systems of stars, gas, and dust · The Milky Way is one of billions",
    "dates": "Other galaxies proven to exist in 1924–25",
    "briefing": "A galaxy is a gigantic system of stars, gas, dust, and dark matter held together by gravity; our Sun is one of hundreds of billions of stars in the Milky Way. For centuries, other galaxies looked like faint, fuzzy clouds, until Edwin Hubble showed in the 1920s that the Andromeda “nebula” lay far outside our own. Galaxies come in shapes like pinwheel spirals, smooth ellipticals, and messy irregulars, and the universe holds billions of them.",
    "answerHtml": "<b><u>Galaxies</u></b> (accept <u>galaxy</u>; accept specific types such as <u>spiral galaxies</u> or <u>elliptical galaxies</u>; prompt on <u>island universes</u> or <u>spiral nebulae</u>; do not accept a single galaxy such as “Milky Way” or “Andromeda”)",
    "accept": [
        "galaxy",
        "galaxies",
        "galaxys",
        "spiral galaxy",
        "spiral galaxies",
        "elliptical galaxy",
        "elliptical galaxies",
        "barred spiral galaxy",
        "barred spiral galaxies",
        "irregular galaxy",
        "irregular galaxies",
        "lenticular galaxy",
        "lenticular galaxies",
        "dwarf galaxy",
        "dwarf galaxies"
    ],
    "prompt": [
        "island universe",
        "island universes",
        "spiral nebula",
        "spiral nebulae",
        "extragalactic nebula",
        "extragalactic nebulae"
    ],
    "reject": [
        "milky way",
        "milky way galaxy",
        "andromeda",
        "andromeda galaxy",
        "m31",
        "triangulum",
        "triangulum galaxy",
        "m33",
        "whirlpool",
        "whirlpool galaxy",
        "sombrero",
        "sombrero galaxy",
        "magellanic cloud",
        "magellanic clouds",
        "large magellanic cloud",
        "small magellanic cloud",
        "galaxy cluster",
        "galaxy clusters",
        "cluster of galaxies",
        "clusters of galaxies",
        "cluster",
        "clusters",
        "supercluster",
        "superclusters",
        "galaxy group",
        "galaxy groups",
        "local group",
        "star cluster",
        "star clusters",
        "globular cluster",
        "nebula",
        "nebulae",
        "quasar",
        "quasars",
        "solar system",
        "constellation",
        "constellations",
        "black hole"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Galaxy",
    "qb": {
        "q": "galaxies",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Edwin Hubble’s labels “early-type” and “late-type” for different shapes of these objects are still used, even though they do not describe ages. Hubble sorted these objects on a diagram shaped like a tuning fork, with E0 through E7 on its handle and two prongs for ordinary and barred spirals.",
            "r": "The Milky Way is a barred spiral example of these objects. For 10 points, name these huge systems of stars, gas, and dust."
        },
        {
            "p": "In the 1920 Great Debate, Heber Curtis argued that “spiral nebulae” were distant examples of these objects, while Harlow Shapley argued that they lay within our own star system. Curtis pointed to faint exploding stars, called novae, in those nebulae as evidence of their great distance.",
            "r": "Edwin Hubble settled the debate by finding Cepheid [“SEF-ee-id”] variable stars in Andromeda. For 10 points, name these vast systems of stars, such as the Milky Way."
        },
        {
            "p": "Vera Rubin and Kent Ford found that stars far from the centers of these objects orbit about as fast as stars closer in, producing flat rotation curves. That result was key evidence that these objects sit inside huge halos of dark matter.",
            "r": "For 10 points, name these huge systems of stars, gas, and dust, such as the Milky Way."
        },
        {
            "p": "In 1845, the Earl of Rosse used a giant telescope nicknamed the Leviathan of Parsonstown to sketch the first spiral arms ever seen in one of these objects, the Whirlpool. C. C. Lin and Frank Shu later explained such arms as density waves.",
            "r": "For 10 points, name these huge collections of stars, which come in spiral, elliptical, and irregular types."
        },
        {
            "p": "When the Hubble Space Telescope stared at a tiny, seemingly empty patch of sky near the Big Dipper for ten days in 1995, it found about 3,000 of these objects in the resulting Deep Field image. A later Ultra Deep Field image showed about 10,000 of them.",
            "r": "For 10 points, name these huge systems of stars, gas, and dust, one of which is the Milky Way."
        },
        {
            "p": "In 2014, R. Brent Tully’s team mapped a supercluster of these objects named Laniakea [“lah-nee-ah-KAY-uh”], meaning “immeasurable heaven” in Hawaiian. A smaller group of these objects, called the Local Group, includes Triangulum and the Large and Small Magellanic Clouds.",
            "r": "The Milky Way and Andromeda are the two biggest members of that group. For 10 points, name these huge systems of stars."
        },
        {
            "p": "One major type of these objects is shaped like a smooth, featureless egg, holds mostly old reddish stars, and has very little gas or dust left for making new stars. The largest examples of that type, such as M87 in the Virgo Cluster, sit at the centers of big clusters.",
            "r": "Those are the elliptical type. For 10 points, name these huge star systems, which also come in spiral and irregular shapes."
        },
        {
            "p": "In 1755, Immanuel Kant suggested that some fuzzy patches in the night sky were enormous disks of stars far beyond our own, an idea later nicknamed “island universes.” The English word for these objects comes from the Greek word for milk.",
            "r": "For 10 points, name these vast systems of stars, gas, and dust, such as the Milky Way."
        },
        {
            "p": "The Antennae are a pair of these objects that are colliding, flinging out long streams of stars that look like an insect’s feelers. Collisions between these objects can trigger “starbursts,” bursts of rapid star formation like the one in M82, the Cigar.",
            "r": "In billions of years, the Milky Way may merge with Andromeda. For 10 points, name these huge systems of stars."
        },
        {
            "p": "Antonio Pigafetta, who sailed on Ferdinand Magellan’s voyage around the world, described two of these objects that are easy to see from the Southern Hemisphere. Those two dwarf examples, which look like faint smudges of light, are now named for Magellan.",
            "r": "They are the Large and Small Magellanic Clouds, which orbit the Milky Way. For 10 points, name these systems of stars, gas, and dust held together by gravity."
        },
        {
            "p": "In 1943, Carl Seyfert [“SEE-fert”] described a group of these objects with unusually bright, compact centers, now known to be powered by black holes swallowing gas. Nearly every large one of these objects has a supermassive black hole at its heart, like Sagittarius A* [“A-star”].",
            "r": "For 10 points, name these huge systems of stars, gas, and dust, such as the Milky Way."
        },
        {
            "p": "In 1929, Edwin Hubble showed that the farther away one of these objects is, the faster it is moving away from us, as shown by the redshift of its light. That pattern, now called the Hubble–Lemaître [“luh-MET-ruh”] law, revealed that the universe is expanding.",
            "r": "For 10 points, name these huge systems of stars, such as the Milky Way and Andromeda."
        },
        {
            "p": "Lenticular examples of these objects, labeled S0, have a central bulge and a disk but no spiral arms. Hoag’s Object, found in 1950, is a rare ring-shaped one, with a yellow core surrounded by a separate ring of young blue stars.",
            "r": "Irregular examples have no regular shape at all. For 10 points, name these huge systems of stars, gas, and dust, which also come in spiral and elliptical shapes."
        },
        {
            "p": "Large examples of these objects grow by swallowing smaller ones, a process sometimes called cannibalism. The Sagittarius Dwarf, found in 1994, is a small one of these objects being slowly torn apart by a much larger neighbor.",
            "r": "That neighbor is the Milky Way. For 10 points, name these huge systems of stars, gas, and dust."
        },
        {
            "p": "The Tully–Fisher relation links how fast spiral examples of these objects spin to how bright they are, which lets astronomers estimate their distances. The Faber–Jackson relation does something similar for the elliptical kind, using the speeds of their stars.",
            "r": "For 10 points, name these huge systems of stars, gas, and dust, one of which is the Milky Way."
        }
    ],
    "clues": [
        {
            "id": "definition",
            "tier": "giveaway",
            "t": "Huge systems of stars, gas, dust, and dark matter held together by gravity",
            "k": ["stars", "dust", "gravity"],
            "n": 0
        },
        {
            "id": "milky-way",
            "tier": "giveaway",
            "t": "The Milky Way, home of our Sun, is a barred spiral one",
            "k": ["milky way", "barred spiral"],
            "n": 0
        },
        {
            "id": "andromeda",
            "tier": "giveaway",
            "t": "Andromeda is the nearest large one to the Milky Way",
            "k": ["andromeda", "nearest"],
            "n": 0,
            "rabbit": "Andromeda Galaxy"
        },
        {
            "id": "types",
            "tier": "giveaway",
            "t": "The main types are spiral, elliptical, and irregular",
            "k": ["spiral", "elliptical", "irregular"],
            "n": 0
        },
        {
            "id": "billions",
            "tier": "giveaway",
            "t": "The observable universe holds at least hundreds of billions of them",
            "k": ["hundreds of billions", "observable universe"],
            "n": 0
        },
        {
            "id": "hubble-proof",
            "tier": "middle",
            "t": "In the 1920s, Edwin Hubble used Cepheid variable stars in Andromeda to prove that others exist far beyond the Milky Way",
            "k": ["edwin hubble", "cepheid", "1920s"],
            "n": 0,
            "rabbit": "Edwin Hubble"
        },
        {
            "id": "great-debate",
            "tier": "middle",
            "t": "1920 Great Debate: Heber Curtis said “spiral nebulae” were separate ones far away; Harlow Shapley said they lay within our own",
            "k": ["great debate", "curtis", "shapley", "1920"],
            "n": 0
        },
        {
            "id": "tuning-fork",
            "tier": "middle",
            "t": "Hubble’s tuning-fork diagram sorts them: ellipticals E0 to E7 on the handle, ordinary and barred spirals on the two prongs",
            "k": ["tuning-fork", "e0", "barred spirals"],
            "n": 0
        },
        {
            "id": "ellipticals",
            "tier": "middle",
            "t": "Elliptical ones are smooth and egg-shaped, with mostly old reddish stars and little gas left for new stars",
            "k": ["egg-shaped", "reddish", "old"],
            "n": 0
        },
        {
            "id": "hubble-law",
            "tier": "middle",
            "t": "Hubble’s law (1929): the farther away one is, the faster it is moving away, which shows the universe is expanding",
            "k": ["1929", "moving away", "expanding"],
            "n": 0,
            "rabbit": "Big Bang"
        },
        {
            "id": "black-hole-centers",
            "tier": "middle",
            "t": "Nearly every large one has a supermassive black hole at its center, like Sagittarius A* in the Milky Way",
            "k": ["supermassive black hole", "sagittarius a"],
            "n": 0,
            "rabbit": "Black Holes"
        },
        {
            "id": "dark-matter",
            "tier": "middle",
            "t": "Flat rotation curves found by Vera Rubin and Kent Ford show they sit inside huge halos of dark matter",
            "k": ["rotation curves", "vera rubin", "dark matter"],
            "n": 0,
            "rabbit": "Dark matter"
        },
        {
            "id": "magellanic",
            "tier": "middle",
            "t": "The Large and Small Magellanic Clouds are dwarf ones that orbit the Milky Way",
            "k": ["magellanic clouds", "dwarf"],
            "n": 0
        },
        {
            "id": "local-group",
            "tier": "middle",
            "t": "The Milky Way, Andromeda, and Triangulum are the three big spirals of the Local Group",
            "k": ["local group", "triangulum"],
            "n": 0
        },
        {
            "id": "milk",
            "tier": "middle",
            "t": "Their English name comes from the Greek word for milk",
            "k": ["greek", "milk"],
            "n": 0
        },
        {
            "id": "early-late",
            "tier": "power",
            "t": "Hubble’s terms “early-type” (ellipticals) and “late-type” (spirals) are still used, though they don’t describe ages",
            "k": ["early-type", "late-type"],
            "n": 0
        },
        {
            "id": "lord-rosse",
            "tier": "power",
            "t": "In 1845, the Earl of Rosse saw the first spiral arms, in the Whirlpool (M51), with the Leviathan of Parsonstown",
            "k": ["rosse", "whirlpool", "1845", "leviathan"],
            "n": 0
        },
        {
            "id": "density-waves",
            "tier": "power",
            "t": "C. C. Lin and Frank Shu explained spiral arms as density waves",
            "k": ["density waves", "spiral arms"],
            "n": 0
        },
        {
            "id": "deep-field",
            "tier": "power",
            "t": "Hubble’s 1995 Deep Field found about 3,000 in a tiny patch of sky near the Big Dipper; the Ultra Deep Field showed about 10,000",
            "k": ["deep field", "3,000", "10,000"],
            "n": 0
        },
        {
            "id": "laniakea",
            "tier": "power",
            "t": "Laniakea, the supercluster mapped in 2014 that includes the Milky Way, means “immeasurable heaven” in Hawaiian",
            "k": ["laniakea", "immeasurable heaven", "2014"],
            "n": 0
        },
        {
            "id": "m87",
            "tier": "power",
            "t": "The largest ellipticals, like M87 in the Virgo Cluster, sit at the centers of big clusters",
            "k": ["m87", "virgo cluster"],
            "n": 0
        },
        {
            "id": "kant",
            "tier": "power",
            "t": "Immanuel Kant suggested in 1755 that fuzzy patches were distant disks of stars, later nicknamed “island universes”",
            "k": ["kant", "1755", "island universes"],
            "n": 0
        },
        {
            "id": "collisions",
            "tier": "power",
            "t": "Collisions, like the Antennae pair with its insect-feeler streams of stars, can trigger starbursts like the one in M82, the Cigar",
            "k": ["antennae", "starbursts", "m82"],
            "n": 0
        },
        {
            "id": "pigafetta",
            "tier": "power",
            "t": "Antonio Pigafetta, who sailed with Magellan, described the two Magellanic Clouds",
            "k": ["pigafetta"],
            "n": 0
        },
        {
            "id": "seyfert",
            "tier": "power",
            "t": "Carl Seyfert described ones with unusually bright, compact centers in 1943",
            "k": ["seyfert", "1943"],
            "n": 0,
            "rabbit": "Quasars"
        },
        {
            "id": "lenticular",
            "tier": "power",
            "t": "Lenticular ones (labeled S0) have a bulge and a disk but no spiral arms; Hoag’s Object, found in 1950, is a rare ring-shaped one",
            "k": ["lenticular", "hoag", "1950"],
            "n": 0
        },
        {
            "id": "cannibalism",
            "tier": "power",
            "t": "Big ones grow by swallowing small ones; the Sagittarius Dwarf, found in 1994, is being torn apart by the Milky Way",
            "k": ["cannibalism", "sagittarius dwarf", "1994"],
            "n": 0
        },
        {
            "id": "tully-fisher",
            "tier": "power",
            "t": "The Tully–Fisher (spirals) and Faber–Jackson (ellipticals) relations link spin or star speeds to brightness, giving distances",
            "k": ["tully", "fisher", "faber", "jackson"],
            "n": 0
        }
    ],
    "trap": {
        "title": "All of them, or just one?",
        "body": "Galaxy tossups are full of famous individual galaxies, like Andromeda, the Whirlpool, M87, and the Magellanic Clouds, and a player who recognizes one may blurt its name. But “Andromeda Galaxy” is its own answer line, and when the question asks for “these objects,” naming one example is wrong. The reverse trap happens too: a tossup that wants one specific kind, such as elliptical galaxies, may give only a prompt for plain “galaxies.”",
        "fix": "Plural wording (“these objects,” “these systems”) with clues about many examples means “galaxies.” If every clue describes one shape (E0 to E7, smooth and egg-shaped), add the type: “elliptical galaxies.” If the clues describe one object with its own distance, neighbors, or Messier number, name that galaxy.",
        "line": "Real answer line: <b><u>galaxies</u></b> (accept <u>galaxy</u>; accept specific types such as spiral or elliptical galaxies)"
    },
    "tests": {
        "right": [
            "Galaxies",
            "galaxy",
            "Galexies",
            "spiral galaxies",
            "elliptical galaxies",
            "a galaxy"
        ],
        "prompt": [
            "island universes",
            "spiral nebulae"
        ],
        "wrong": [
            "Milky Way",
            "Andromeda Galaxy",
            "Galaxy clusters",
            "Nebulae",
            "Star clusters",
            "Local Group"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
