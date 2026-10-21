import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "big-bang",
    "name": "Big Bang",
    "mono": "BB",
    "category": "Astronomy",
    "qbCategory": "Science · Other Science (Astronomy)",
    "kicker": "How the universe began, hot and dense · Expanding for about 13.8 billion years",
    "dates": "About 13.8 billion years ago; named in 1949",
    "briefing": "The Big Bang theory says that about 13.8 billion years ago, the whole universe was in an incredibly hot, dense state, and it has been expanding and cooling ever since. It was not an explosion at one spot in space but a stretching of space itself, everywhere at once. The astronomer Fred Hoyle, who preferred a rival theory, gave it its catchy name on BBC radio in 1949.",
    "answerHtml": "<b><u>Big Bang</u></b> theory (accept <u>Big Bang</u> model or cosmology; prompt on <u>primeval atom</u> or <u>expanding universe</u>; do not accept “cosmic microwave background,” “inflation,” or “Steady State theory”)",
    "accept": [
        "big bang",
        "the big bang",
        "big bang theory",
        "big bang model",
        "big bang cosmology",
        "big bang hypothesis",
        "hot big bang",
    ],
    "prompt": [
        "primeval atom",
        "primeval atom hypothesis",
        "hypothesis of the primeval atom",
        "cosmic egg",
        "expanding universe",
        "expansion of the universe",
    ],
    "reject": [
        "steady state",
        "steady state theory",
        "cosmic microwave background",
        "cosmic microwave background radiation",
        "cmb",
        "cmbr",
        "cosmic inflation",
        "inflation",
        "inflation theory",
        "big crunch",
        "big freeze",
        "big rip",
        "big bounce",
        "hubbles law",
        "hubble law",
        "hubble lemaitre law",
        "redshift",
        "dark energy",
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Big_Bang",
    "qb": {
        "q": "Big Bang",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it.",
    },
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        {
            "p": "When a Belgian priest showed him math suggesting that the universe might be expanding, Albert Einstein reportedly said the math was correct but the physics was “abominable.” That priest, Georges Lemaître [“luh-MET-ruh”], later said the universe began as a single “primeval atom.”",
            "r": "For 10 points, name this theory that the universe began about 13.8 billion years ago in a hot, dense state.",
        },
        {
            "p": "Hermann Bondi, Thomas Gold, and Fred Hoyle championed a rival to this theory, in which new matter is constantly created as the universe expands, so that the universe always looks the same. That rival model was called the Steady State theory.",
            "r": "Hoyle himself coined this theory’s name on BBC radio in 1949. For 10 points, name this theory that the universe expanded from an extremely hot, dense beginning.",
        },
        {
            "p": "As a pun on the first three letters of the Greek alphabet, George Gamow [“GAM-off”] added Hans Bethe’s name to a 1948 paper with Ralph Alpher about how the lightest elements formed. Alpher and Robert Herman also predicted that leftover radiation from this event should still fill space.",
            "r": "That radiation is the cosmic microwave background. For 10 points, name this event that began the universe about 13.8 billion years ago.",
        },
        {
            "p": "In the first few minutes after this event, protons and neutrons fused to make nearly all of the universe’s helium, which makes up about a quarter of all ordinary matter by mass, along with a tiny bit of lithium.",
            "r": "For 10 points, name this event that started the expansion of the universe about 13.8 billion years ago.",
        },
        {
            "p": "To explain why the universe looks so smooth in every direction and why space is so nearly flat, physicists propose that a split second after this event, the universe swelled enormously in a burst called inflation. Alan Guth first proposed that idea around 1980.",
            "r": "For 10 points, name this event, the hot, dense beginning of the universe about 13.8 billion years ago.",
        },
        {
            "p": "In 1922, Alexander Friedmann found solutions to Albert Einstein’s equations that describe an expanding universe, ideas that later fed into this theory. Einstein himself had at first preferred a universe that stays the same size.",
            "r": "Edwin Hubble’s 1929 discovery that distant galaxies are rushing away from us became key evidence for it. For 10 points, name this theory of the universe’s origin.",
        },
        {
            "p": "Olbers’ paradox asks why the night sky is dark if the universe is endless and filled with stars, and part of the answer comes from this theory: the universe has a limited age, so light from the most distant stars has not had time to reach us.",
            "r": "For 10 points, name this theory that the universe began about 13.8 billion years ago.",
        },
        {
            "p": "Robert Dicke’s team at Princeton was building an instrument to search for radiation left over from this event when they learned that two Bell Labs scientists had already found it by accident. That faint glow was released about 380,000 years after this event.",
            "r": "Arno Penzias and Robert Wilson discovered it in 1964. For 10 points, name this event that began the universe, named by Fred Hoyle.",
        },
        {
            "p": "Physicists call the first tiny sliver of time after this event, up to about 10 to the minus 43rd seconds, the Planck epoch. For the first several microseconds after this event, the universe was filled with a hot soup of quarks and gluons.",
            "r": "For 10 points, name this event, the hot, dense beginning of the universe.",
        },
        {
            "p": "Stephen Hawking and Roger Penrose argued that, if general relativity holds, this event must have started from a singularity, a point of infinite density. Hawking’s 1966 Cambridge thesis made an early version of that argument.",
            "r": "For 10 points, name this event that began the expansion of the universe about 13.8 billion years ago.",
        },
        {
            "p": "For about 380,000 years after this event, the universe was a glowing fog of plasma that light could not pass through, until it cooled enough for electrons and nuclei to join into neutral atoms. Most of those first atoms were hydrogen.",
            "r": "For 10 points, name this event, the beginning of the universe in a hot, dense state.",
        },
        {
            "p": "Cosmologists contrast this event with possible endings for the universe nicknamed the Big Freeze, the Big Rip, and the Big Crunch, which would be like this event run in reverse. In 1998, astronomers found that the expansion that began with this event is speeding up.",
            "r": "For 10 points, name this event that began the universe about 13.8 billion years ago.",
        },
        {
            "p": "Quasars, which are common far away but rare nearby, supported this theory because they show that the universe has changed over time. The discovery of those faraway objects in the 1960s was a blow to the rival Steady State theory.",
            "r": "For 10 points, name this theory, which says the universe expanded from a hot, dense state about 13.8 billion years ago.",
        },
        {
            "p": "In 1927, two years before Edwin Hubble’s famous paper, Georges Lemaître published his own estimate of how fast the universe is expanding, a key step toward this theory. In 2018, the International Astronomical Union voted to recommend renaming the law describing that expansion to honor both men.",
            "r": "For 10 points, name this theory of the universe’s origin, named by Fred Hoyle.",
        },
        {
            "p": "Unlike an ordinary explosion, this event did not happen at one spot in space; instead, space itself began stretching everywhere at once, so it has no center. A CBS sitcom about scientists at Caltech, which ran from 2007 to 2019, was named for this theory.",
            "r": "For 10 points, name this event, the beginning of the universe about 13.8 billion years ago.",
        },
    ],
    "clues": [
        {"id": "hot-dense", "tier": "giveaway", "t": "Theory that the universe began in an extremely hot, dense state and has been expanding and cooling ever since", "k": ["hot, dense", "expanding", "cooling"], "n": 0},
        {"id": "age", "tier": "giveaway", "t": "Happened about 13.8 billion years ago", "k": ["13.8 billion"], "n": 0},
        {"id": "hoyle", "tier": "giveaway", "t": "Named by Fred Hoyle in a 1949 BBC radio broadcast, even though he favored a rival theory", "k": ["fred hoyle", "1949", "bbc"], "n": 0},
        {"id": "cmb", "tier": "giveaway", "t": "Its leftover glow is the cosmic microwave background, found by Arno Penzias and Robert Wilson in 1964", "k": ["cosmic microwave background", "penzias", "wilson"], "n": 0, "rabbit": "Cosmic microwave background"},
        {"id": "hubble", "tier": "giveaway", "t": "Edwin Hubble’s 1929 discovery that distant galaxies are rushing away from us is key evidence for it", "k": ["edwin hubble", "1929", "rushing away"], "n": 0, "rabbit": "Edwin Hubble"},
        {"id": "lemaitre", "tier": "middle", "t": "First proposed by the Belgian priest Georges Lemaître, who said the universe began as a “primeval atom”", "k": ["lemaître", "primeval atom", "belgian"], "n": 0},
        {"id": "steady-state", "tier": "middle", "t": "Its old rival, the Steady State theory of Hoyle, Hermann Bondi, and Thomas Gold, said new matter is constantly created", "k": ["steady state", "bondi", "gold"], "n": 0},
        {"id": "nucleosynthesis", "tier": "middle", "t": "In its first few minutes, nearly all the universe’s helium formed (about a quarter of ordinary matter by mass), plus a little lithium", "k": ["helium", "few minutes", "lithium"], "n": 0, "rabbit": "Helium"},
        {"id": "recombination", "tier": "middle", "t": "For about 380,000 years the universe was a fog of plasma; then neutral atoms, mostly hydrogen, formed and set free the light we see as the CMB", "k": ["380,000", "neutral atoms", "plasma"], "n": 0},
        {"id": "inflation", "tier": "middle", "t": "Around 1980, Alan Guth proposed that the universe swelled enormously in a split second just after it, an idea called inflation", "k": ["alan guth", "inflation", "1980"], "n": 0},
        {"id": "no-center", "tier": "middle", "t": "Not an explosion at one spot in space: space itself began stretching everywhere at once, so there is no center", "k": ["no center", "stretching"], "n": 0},
        {"id": "alpher-gamow", "tier": "middle", "t": "George Gamow added Hans Bethe’s name to his 1948 paper with Ralph Alpher on the lightest elements, as a pun on alpha, beta, gamma", "k": ["gamow", "alpher", "1948"], "n": 0},
        {"id": "quasars", "tier": "middle", "t": "Quasars, common far away but rare nearby, show that the universe has changed over time, evidence against the Steady State theory", "k": ["quasars", "changed over time"], "n": 0, "rabbit": "Quasars"},
        {"id": "sitcom", "tier": "middle", "t": "A CBS sitcom about scientists at Caltech, which ran from 2007 to 2019, is named for it", "k": ["sitcom", "caltech"], "n": 0},
        {"id": "abominable", "tier": "power", "t": "Albert Einstein reportedly told Lemaître that his math was correct but his physics was “abominable”", "k": ["abominable", "einstein"], "n": 0},
        {"id": "friedmann", "tier": "power", "t": "Alexander Friedmann found expanding-universe solutions to Einstein’s equations in 1922; Einstein had at first preferred an unchanging universe", "k": ["friedmann", "1922"], "n": 0},
        {"id": "dicke", "tier": "power", "t": "Robert Dicke’s Princeton team was about to search for its leftover radiation when two Bell Labs scientists found it by accident", "k": ["dicke", "princeton", "bell labs"], "n": 0},
        {"id": "lemaitre-1927", "tier": "power", "t": "Lemaître estimated the expansion rate in 1927, two years before Hubble; in 2018, astronomers voted to recommend renaming the expansion law for both men", "k": ["1927", "2018", "renaming"], "n": 0},
        {"id": "herman", "tier": "power", "t": "Ralph Alpher and Robert Herman predicted in 1948 that its leftover radiation should still fill space, at about 5 kelvins", "k": ["robert herman", "5 kelvins"], "n": 0},
        {"id": "olbers", "tier": "power", "t": "It helps answer Olbers’ paradox (why is the night sky dark?): the universe has a limited age", "k": ["olbers", "night sky", "limited age"], "n": 0},
        {"id": "planck-epoch", "tier": "power", "t": "The first sliver of time after it, up to about 10⁻⁴³ seconds, is called the Planck epoch", "k": ["planck epoch"], "n": 0},
        {"id": "quark-gluon", "tier": "power", "t": "For its first several microseconds, the universe was filled with a hot soup of quarks and gluons", "k": ["quarks", "gluons", "microseconds"], "n": 0, "rabbit": "Quarks"},
        {"id": "singularity", "tier": "power", "t": "Stephen Hawking and Roger Penrose argued it began with a singularity; Hawking’s 1966 Cambridge thesis made an early version of the case", "k": ["singularity", "hawking", "penrose"], "n": 0, "rabbit": "Stephen Hawking"},
        {"id": "endings", "tier": "power", "t": "Possible endings of the universe contrasted with it: the Big Freeze, the Big Rip, and the Big Crunch (like it run in reverse)", "k": ["big crunch", "big rip", "big freeze"], "n": 0},
        {"id": "dark-energy", "tier": "power", "t": "In 1998, astronomers found that the expansion it began is speeding up, which is blamed on dark energy", "k": ["1998", "dark energy", "speeding up"], "n": 0},
        {"id": "smooth-flat", "tier": "power", "t": "Inflation helps explain why the universe looks so smooth in every direction and why space is so nearly flat", "k": ["smooth", "flat"], "n": 0},
    ],
    "trap": {
        "title": "Theory, glow, or inflation?",
        "body": "Tossups on the cosmic microwave background usually end by calling it the afterglow of this event, and tossups on this event mention that glow, so players mix up the two answer lines. Inflation, Alan Guth’s idea of a split-second growth spurt just after the beginning, is a separate answer line too, and so is Hubble’s law. The Steady State theory of Fred Hoyle, Hermann Bondi, and Thomas Gold was the rival idea.",
        "fix": "“This theory” or “this event” plus Lemaître’s primeval atom, Hoyle’s 1949 nickname, 13.8 billion years, or the first few minutes of element-making means the Big Bang. “This radiation” or “this glow” found by Penzias and Wilson means the cosmic microwave background. A brief period of extremely rapid expansion means inflation.",
        "line": "Real answer line: <b><u>Big Bang</u></b> theory (prompt on <u>primeval atom</u>; do not accept “cosmic microwave background” or “Steady State theory”)",
    },
    "tests": {
        "right": ["Big Bang", "big bang theory", "The Big Bang", "Bigbang", "Big Bnag theory"],
        "prompt": ["primeval atom", "cosmic egg"],
        "wrong": ["Steady State theory", "cosmic microwave background", "inflation", "Big Crunch", "Hubble's law", "dark energy"],
    },
}

out = ROOT / "topics" / f"{data['id']}.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("saved", out)
