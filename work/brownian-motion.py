import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

data = {
    "id": "brownian-motion",
    "name": "Brownian motion",
    "mono": "BM",
    "category": "Physics",
    "qbCategory": "Science · Physics",
    "kicker": "Random jiggling of tiny specks in a fluid · Proof that molecules exist",
    "dates": "Observed by Robert Brown, 1827; explained by Einstein, 1905",
    "briefing": "In 1827, botanist Robert Brown peered through his microscope at tiny particles from pollen grains floating in water and saw them jiggling nonstop, as if alive. That random dance, Brownian motion, happens because invisible water molecules keep slamming into the particles from every side. In 1905 Albert Einstein worked out the math, and Jean Perrin’s experiments that followed helped convince doubters that atoms and molecules are real.",
    "answerHtml": "<b><u>Brownian</u></b> motion (accept <u>Brownian</u> movement or <u>pedesis</u>; prompt on <u>random walk</u>; do not accept “diffusion”)",
    "accept": [
        "brownian motion",
        "brownian motions",
        "brownian movement",
        "brownian movements",
        "brownian",
        "pedesis",
        "wiener process"
    ],
    "prompt": [
        "random walk",
        "random walks",
        "random motion",
        "random movement"
    ],
    "reject": [
        "diffusion",
        "osmosis",
        "convection",
        "effusion",
        "robert brown",
        "brown",
        "browning",
        "robert browning",
        "brownian ratchet",
        "brownian noise",
        "brown noise",
        "thermal motion",
        "kinetic theory",
        "kinetic molecular theory",
        "kinetic theory of gases",
        "colloid",
        "colloids",
        "colloidal suspension",
        "tyndall effect",
        "pollen",
        "avogadros number",
        "viscosity",
        "heat",
        "random",
        "stokes law"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Brownian_motion",
    "qb": {
        "q": "Brownian motion",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In his 1900 thesis, Louis Bachelier [“bah-shel-YAY”] used a mathematical version of this phenomenon to model the ups and downs of prices on the Paris stock exchange. In that model, prices take a random walk, moving up or down by chance at each step.",
            "r": "For 10 points, name this random jiggling of tiny particles suspended in a fluid, named for a Scottish botanist."
        },
        {
            "p": "In _On the Nature of Things_, the Roman poet Lucretius [“loo-KREE-shus”] described dust specks dancing in a sunbeam as evidence that unseen atoms were pushing them, an early description often linked to this phenomenon. Jean Perrin’s measurements of this phenomenon later helped convince doubters that atoms really exist.",
            "r": "For 10 points, name this random jiggling of particles in a fluid, which Robert Brown saw under a microscope in 1827."
        },
        {
            "p": "In 1785, the Dutch scientist Jan Ingenhousz [“ING-en-howss”], better known for showing that plants need light to make oxygen, described coal dust jittering on the surface of alcohol, an early sighting of this phenomenon. Smaller particles show more of this motion than larger ones.",
            "r": "For 10 points, name this random movement of particles suspended in a fluid, named for the botanist Robert Brown."
        },
        {
            "p": "Paul Langevin [“lahn-zhuh-VAN”] described this phenomenon in 1908 with an equation that combines a drag force that slows a particle with a rapidly changing random force. This phenomenon grows more vigorous as the surrounding fluid gets warmer.",
            "r": "For 10 points, name this random jiggling of particles from pollen grains and other specks in water, which Robert Brown studied in 1827."
        },
        {
            "p": "Jean Perrin [“zhahn peh-RAN”] tracked tiny grains of a yellow resin called gamboge [“gam-BOHJ”] to test a theory of this phenomenon, work that earned him the 1926 Nobel Prize in Physics. He used his results to calculate Avogadro’s number.",
            "r": "Albert Einstein had explained this phenomenon in 1905. For 10 points, name this random jiggling of small particles in a fluid."
        },
        {
            "p": "A particle undergoing this phenomenon wanders a typical distance from its starting point that grows only with the square root of time, so drifting twice as far takes four times as long. Measuring this phenomenon gave scientists a way to find Avogadro’s number.",
            "r": "Albert Einstein explained it in 1905. For 10 points, name this random jiggling of tiny particles in a fluid, named for Robert Brown."
        },
        {
            "p": "In a common school experiment, a microscope aimed into a small glass cell full of smoke shows bright specks wobbling unpredictably because of this phenomenon. The specks keep moving this way for as long as anyone watches; the motion never runs down.",
            "r": "It happens because invisible air molecules keep crashing into the specks. For 10 points, name this random jiggling named for botanist Robert Brown."
        },
        {
            "p": "This phenomenon’s namesake sailed to Australia with Matthew Flinders as the naturalist aboard HMS _Investigator_ and later named the cell nucleus. He showed that this phenomenon was not a sign of life by seeing it in specks of ground glass and rock.",
            "r": "For 10 points, name this random jiggling of tiny particles in water, studied by a Scottish botanist in 1827."
        },
        {
            "p": "This phenomenon is named for a botanist who saw it while studying pollen from the wildflower _Clarkia pulchella_ [“KLAR-kee-uh pul-KEL-uh”], and who at first wondered if the moving particles were alive. Those particles came from inside the pollen grains.",
            "r": "For 10 points, name this random jiggling of tiny particles in a fluid, named for Robert Brown."
        },
        {
            "p": "Another name for this phenomenon comes from a Greek word meaning “leaping.” The Stokes–Einstein equation says that this phenomenon spreads particles faster at higher temperatures and more slowly in thicker, more viscous liquids.",
            "r": "For 10 points, name this random zigzag motion of small particles in a fluid, named for Robert Brown."
        },
        {
            "p": "Marian Smoluchowski [“smoh-loo-KOF-skee”] explained this phenomenon in 1906, separately from a more famous physicist, with an equation linking how fast the particles spread to their mobility and the temperature. Whole pollen grains are too big to show this phenomenon clearly, but tiny particles released from inside them do.",
            "r": "For 10 points, name this random jiggling of tiny particles in a fluid, which Robert Brown studied in 1827."
        },
        {
            "p": "Norbert Wiener [“WEE-ner”] gave the first rigorous mathematical description of this phenomenon, so mathematicians name their model of it for him. In that model, a particle’s position after a set time follows a bell-shaped normal distribution.",
            "r": "For 10 points, name this random jiggling of tiny particles suspended in a fluid, named for a Scottish botanist."
        },
        {
            "p": "A particle undergoing this phenomenon is just as likely to move one way as any other, yet over time it wanders farther and farther from where it started. This phenomenon is the microscopic process behind diffusion, the spreading of particles from crowded areas to less crowded ones.",
            "r": "For 10 points, name this random jiggling of tiny particles in a fluid, caused by collisions with molecules."
        },
        {
            "p": "Richard Feynman’s ratchet-and-pawl thought experiment showed that a tiny one-way gear cannot turn this phenomenon into useful work when everything is at the same temperature. Particles undergoing this phenomenon wander farther in thin liquids like water than in thick ones like honey.",
            "r": "For 10 points, name this random jiggling of small particles in a fluid, which Albert Einstein explained in 1905."
        },
        {
            "p": "Under a microscope, droplets of fat in diluted milk jitter back and forth because of this phenomenon, which helps keep the tiny particles in many colloids from settling out. Larger particles show less of it, because the random pushes they get from all sides nearly cancel out.",
            "r": "For 10 points, name this random jiggling of small particles in a fluid, named for the Scottish botanist Robert Brown."
        }
    ],
    "clues": [
        {
            "id": "definition",
            "tier": "giveaway",
            "t": "The random jiggling of tiny particles suspended in a liquid or a gas",
            "k": ["random jiggling", "suspended", "particles"],
            "n": 0
        },
        {
            "id": "robert-brown",
            "tier": "giveaway",
            "t": "Named for Scottish botanist Robert Brown, who saw it in water under a microscope in 1827",
            "k": ["robert brown", "botanist", "1827"],
            "n": 0
        },
        {
            "id": "pollen",
            "tier": "giveaway",
            "t": "Brown was watching tiny particles from pollen grains floating in water",
            "k": ["pollen", "grains"],
            "n": 0,
            "rabbit": "Pollen"
        },
        {
            "id": "molecules",
            "tier": "giveaway",
            "t": "Caused by fast-moving molecules of the fluid crashing into the particles unevenly",
            "k": ["molecules", "crashing"],
            "n": 0
        },
        {
            "id": "einstein-1905",
            "tier": "giveaway",
            "t": "Albert Einstein explained it in one of his 1905 “miracle year” papers",
            "k": ["einstein", "1905", "miracle year"],
            "n": 0,
            "rabbit": "Albert Einstein"
        },
        {
            "id": "perrin",
            "tier": "middle",
            "t": "Jean Perrin tested Einstein’s theory with grains of gamboge resin, winning the 1926 Nobel Prize in Physics",
            "k": ["jean perrin", "gamboge", "1926"],
            "n": 0
        },
        {
            "id": "atoms-real",
            "tier": "middle",
            "t": "Perrin’s measurements helped convince doubters that atoms and molecules really exist",
            "k": ["atoms", "really exist", "doubters"],
            "n": 0
        },
        {
            "id": "avogadro",
            "tier": "middle",
            "t": "Measuring it gave scientists a way to find Avogadro’s number",
            "k": ["avogadro’s number", "avogadro"],
            "n": 0,
            "rabbit": "Avogadro’s number"
        },
        {
            "id": "warmer-smaller",
            "tier": "middle",
            "t": "More vigorous in warmer fluids and for smaller particles; larger particles show less",
            "k": ["warmer", "smaller particles", "vigorous"],
            "n": 0
        },
        {
            "id": "square-root",
            "tier": "middle",
            "t": "A particle’s typical distance from its start grows with the square root of time, so going twice as far takes four times as long",
            "k": ["square root", "four times"],
            "n": 0
        },
        {
            "id": "not-alive",
            "tier": "middle",
            "t": "Brown first wondered if the particles were alive, then saw the same motion in specks of ground glass and rock",
            "k": ["ground glass", "alive", "rock"],
            "n": 0
        },
        {
            "id": "diffusion",
            "tier": "middle",
            "t": "The microscopic process behind diffusion, the spreading of particles from crowded areas to less crowded ones",
            "k": ["diffusion", "spreading"],
            "n": 0,
            "rabbit": "Diffusion"
        },
        {
            "id": "smoke-cell",
            "tier": "middle",
            "t": "A school “smoke cell” experiment shows bright specks of smoke jiggling in air under a microscope",
            "k": ["smoke cell", "smoke"],
            "n": 0
        },
        {
            "id": "colloids",
            "tier": "middle",
            "t": "Keeps tiny particles in colloids, like fat droplets in milk, jiggling instead of settling out",
            "k": ["colloids", "milk", "settling"],
            "n": 0,
            "rabbit": "Colloids"
        },
        {
            "id": "random-walk",
            "tier": "middle",
            "t": "Can be modeled as a random walk: a path of steps taken in random directions",
            "k": ["random walk", "random directions"],
            "n": 0
        },
        {
            "id": "lucretius",
            "tier": "power",
            "t": "Lucretius’s _On the Nature of Things_ described dust dancing in a sunbeam as evidence of atoms",
            "k": ["lucretius", "on the nature of things", "sunbeam"],
            "n": 0
        },
        {
            "id": "ingenhousz",
            "tier": "power",
            "t": "Jan Ingenhousz described coal dust jittering on the surface of alcohol in 1785",
            "k": ["ingenhousz", "coal dust", "1785"],
            "n": 0
        },
        {
            "id": "bachelier",
            "tier": "power",
            "t": "Louis Bachelier’s 1900 thesis used a math version of it to model prices on the Paris stock exchange",
            "k": ["bachelier", "stock exchange", "1900"],
            "n": 0
        },
        {
            "id": "wiener",
            "tier": "power",
            "t": "Norbert Wiener gave the first rigorous math description; mathematicians name their model of it for him",
            "k": ["norbert wiener", "wiener", "rigorous"],
            "n": 0
        },
        {
            "id": "langevin",
            "tier": "power",
            "t": "Paul Langevin’s 1908 equation combines a slowing drag force with a rapidly changing random force",
            "k": ["langevin", "1908", "random force"],
            "n": 0
        },
        {
            "id": "smoluchowski",
            "tier": "power",
            "t": "Marian Smoluchowski explained it separately from Einstein (1906), linking how fast particles spread to their mobility and temperature",
            "k": ["smoluchowski", "mobility", "1906"],
            "n": 0
        },
        {
            "id": "stokes-einstein",
            "tier": "power",
            "t": "Stokes–Einstein equation: particles spread faster at high temperature and more slowly in viscous liquids, like honey",
            "k": ["stokes–einstein", "viscous", "honey"],
            "n": 0,
            "rabbit": "Viscosity"
        },
        {
            "id": "leaping",
            "tier": "power",
            "t": "Another name for it comes from a Greek word meaning “leaping”",
            "k": ["greek", "leaping"],
            "n": 0
        },
        {
            "id": "clarkia",
            "tier": "power",
            "t": "Brown was studying pollen from the wildflower _Clarkia pulchella_",
            "k": ["clarkia pulchella", "clarkia", "wildflower"],
            "n": 0
        },
        {
            "id": "inside-grains",
            "tier": "power",
            "t": "Whole pollen grains are too big to show it clearly; Brown saw particles released from inside them",
            "k": ["too big", "inside"],
            "n": 0
        },
        {
            "id": "investigator",
            "tier": "power",
            "t": "Robert Brown sailed to Australia with Matthew Flinders on HMS _Investigator_ and named the cell nucleus",
            "k": ["matthew flinders", "investigator", "nucleus"],
            "n": 0,
            "rabbit": "Nucleus"
        },
        {
            "id": "feynman-ratchet",
            "tier": "power",
            "t": "Richard Feynman’s ratchet-and-pawl thought experiment: a tiny one-way gear can’t turn it into useful work at one temperature",
            "k": ["feynman", "ratchet", "one-way gear"],
            "n": 0,
            "rabbit": "Richard Feynman"
        },
        {
            "id": "normal-distribution",
            "tier": "power",
            "t": "In the math model, a particle’s position after a set time follows a bell-shaped normal distribution",
            "k": ["normal distribution", "bell-shaped"],
            "n": 0
        }
    ],
    "trap": {
        "title": "The motion, not diffusion",
        "body": "This jiggling of single particles and diffusion, the overall spreading of a substance, are separate answer lines, and diffusion tossups even mention this motion. Robert Brown is the man, not the answer, and the pollen grains themselves are a separate biology answer line. Saying only “random walk” earns a prompt.",
        "fix": "One speck zigzagging under a microscope, Robert Brown in 1827, Einstein’s 1905 paper, Perrin, gamboge, Langevin, or Bachelier means Brownian motion. A substance spreading from high to low concentration, or Fick’s laws, means diffusion. Finish the answer with “motion.”",
        "line": "Real answer line: <b><u>Brownian</u></b> motion (accept <u>Brownian</u> movement or <u>pedesis</u>; prompt on <u>random walk</u>; do not accept “diffusion”)"
    },
    "tests": {
        "right": [
            "Brownian motion",
            "brownian motion",
            "Brownian movement",
            "Brownian",
            "Brownain motion",
            "Pedesis"
        ],
        "prompt": [
            "Random walk"
        ],
        "wrong": [
            "Diffusion",
            "Robert Brown",
            "Osmosis",
            "Convection",
            "Thermal motion",
            "Colloids",
            "Browning"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
