import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "pulsars",
    "name": "Pulsars",
    "mono": "PSR",
    "category": "Astronomy",
    "qbCategory": "Science · Other Science (Astronomy)",
    "kicker": "Spinning neutron stars · Cosmic lighthouses that tick like clocks",
    "dates": "First found 1967",
    "briefing": "In 1967, graduate student Jocelyn Bell noticed a radio signal that ticked every 1.3 seconds, so regular that her team jokingly nicknamed it LGM-1, for “Little Green Men.” It was the first pulsar: a spinning neutron star that sweeps beams of radio waves across space like a lighthouse. Some pulsars spin hundreds of times a second and keep time so steadily that astronomers use them as cosmic clocks.",
    "answerHtml": "<b><u>Pulsars</u></b> (accept <u>pulsar</u>; prompt on <u>neutron star</u>s)",
    "accept": [
        "pulsar",
        "pulsars"
    ],
    "prompt": [
        "neutron star",
        "neutron stars",
        "rotating neutron star",
        "rotating neutron stars",
        "spinning neutron star",
        "spinning neutron stars"
    ],
    "reject": [
        "neutrons",
        "magnetar",
        "magnetars",
        "quasar",
        "quasars",
        "white dwarf",
        "white dwarfs",
        "cepheid",
        "cepheids",
        "cepheid variable",
        "cepheid variables",
        "blazar",
        "blazars"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Pulsar",
    "qb": {
        "q": "pulsar",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "While checking long paper charts from a radio telescope she had helped build, a Cambridge graduate student noticed a bit of “scruff” that turned out to be a signal repeating every 1.3 seconds. Her team jokingly labeled it LGM-1, for “Little Green Men.”",
            "r": "That student, Jocelyn Bell, had found the first of these objects. For 10 points, name these spinning neutron stars that give off regular pulses of radio waves."
        },
        {
            "p": "Antony Hewish shared the 1974 Nobel Prize in Physics, the first ever given for astronomy, for his role in the discovery of these objects, but his student who first noticed them was left out. In 2018, that student won a three-million-dollar Breakthrough Prize and gave all of it to fund physics scholarships.",
            "r": "For 10 points, name these rapidly spinning neutron stars, the first of which Jocelyn Bell found in 1967."
        },
        {
            "p": "Inside the Crab Nebula, the wreck of a star that Chinese astronomers saw explode in 1054 CE, one of these objects spins about 30 times every second. The energy it loses as it slowly spins down keeps the whole nebula glowing.",
            "r": "For 10 points, name these rotating neutron stars that sweep beams across space like lighthouses."
        },
        {
            "p": "In 1974, Russell Hulse and Joseph Taylor used the Arecibo [“air-uh-SEE-boh”] telescope to find one of these objects orbiting another neutron star. The pair’s slowly shrinking orbit matched Albert Einstein’s prediction of gravitational waves, earning a 1993 Nobel Prize.",
            "r": "For 10 points, name these spinning neutron stars that give off regular radio pulses."
        },
        {
            "p": "The plaques on Pioneer 10 and 11 and the covers of the Voyager Golden Records show where the Sun is by using a map of 14 of these objects, with each one’s rhythm written in binary code.",
            "r": "That map was meant to show any finders where the spacecraft came from. For 10 points, name these rapidly rotating neutron stars that act like cosmic lighthouses."
        },
        {
            "p": "Some of these objects are “recycled” when gas pulled from a partner star spins them up. As of 2025, the fastest known one, in the star cluster Terzan 5, spun 716 times every second.",
            "r": "Such fast spinners are called millisecond examples of these objects. For 10 points, name these spinning neutron stars that emit regular pulses."
        },
        {
            "p": "These objects send out beams from their magnetic poles, which are tilted away from the axis they spin around. In 1968, Thomas Gold explained how they work, and his idea was confirmed when one in the Crab Nebula was found to be slowly losing spin.",
            "r": "Each beam sweeps past Earth like a lighthouse’s. For 10 points, name these spinning neutron stars, the first of which Jocelyn Bell found in 1967."
        },
        {
            "p": "In 1992, Aleksander Wolszczan [“VOHL-shchahn”] and Dale Frail found the first confirmed planets outside the solar system orbiting one of these objects. Tiny changes in the timing of its pulses revealed the planets’ tugs.",
            "r": "These objects are left behind when massive stars explode as supernovae. For 10 points, name these rapidly spinning neutron stars."
        },
        {
            "p": "In 2023, the NANOGrav team announced evidence of a low hum of gravitational waves filling the universe, found by timing dozens of these objects for 15 years. The pulses of some of these objects arrive so steadily that they rival atomic clocks.",
            "r": "These objects are the leftover cores of exploded stars. For 10 points, name these spinning neutron stars, which act like cosmic lighthouses."
        },
        {
            "p": "The Vela supernova remnant holds one of these objects that spins about 11 times a second and sometimes suddenly speeds up in events called glitches. Those glitches may happen when a superfluid deep inside the star suddenly shifts.",
            "r": "For 10 points, name these rotating neutron stars that send out regular pulses of radio waves."
        },
        {
            "p": "The cover of Joy Division’s 1979 album _Unknown Pleasures_ shows dozens of stacked radio signals from the first of these objects ever found, CP 1919. That object’s pulses repeat about every 1.3 seconds.",
            "r": "It was found in 1967 by Jocelyn Bell. For 10 points, name these spinning neutron stars, which tick like cosmic clocks."
        },
        {
            "p": "“Black widow” examples of these objects blast their small partner stars with so much radiation and wind that they slowly evaporate them. Many such systems contain millisecond examples, which were spun up by gas they had earlier pulled from a partner.",
            "r": "These objects send out beams that sweep past Earth like a lighthouse’s. For 10 points, name these rapidly spinning neutron stars."
        },
        {
            "p": "Free electrons in space slow down the lower radio frequencies of these objects’ pulses, so astronomers use that delay, called dispersion, to estimate how far away each one is. Their catalog names begin with the letters PSR.",
            "r": "For 10 points, name these objects, rotating neutron stars that sweep beams of radio waves past Earth."
        },
        {
            "p": "Most of these objects slowly lose spin as they turn their rotational energy into radiation and fast-moving particles, so an older one usually turns more slowly than a young one. Eventually they spin too slowly for their beams to keep shining.",
            "r": "For 10 points, name these spinning neutron stars, the first of which was found in 1967."
        },
        {
            "p": "Centaurus X-3, the first of these objects found to tick in X-rays, was spotted by the Uhuru satellite in 1971. In 2017, an experiment on the International Space Station showed that X-ray signals from these objects could guide spacecraft, like a cosmic GPS.",
            "r": "Most of these objects are seen in radio waves. For 10 points, name these spinning neutron stars that pulse like lighthouses."
        }
    ],
    "clues": [
        {
            "id": "spinning-ns",
            "tier": "giveaway",
            "t": "Rapidly spinning neutron stars that give off regular pulses, usually of radio waves",
            "k": [
                "spinning neutron stars",
                "regular pulses",
                "radio waves"
            ],
            "n": 0,
            "rabbit": "Neutron stars"
        },
        {
            "id": "lighthouse",
            "tier": "giveaway",
            "t": "Their beams sweep past Earth like the light of a lighthouse",
            "k": [
                "lighthouse",
                "beams"
            ],
            "n": 0
        },
        {
            "id": "bell-1967",
            "tier": "giveaway",
            "t": "Jocelyn Bell found the first one in 1967 as a Cambridge graduate student",
            "k": [
                "jocelyn bell",
                "1967",
                "cambridge"
            ],
            "n": 0
        },
        {
            "id": "supernova",
            "tier": "giveaway",
            "t": "Left behind when massive stars explode as supernovae",
            "k": [
                "supernovae",
                "massive stars"
            ],
            "n": 0,
            "rabbit": "Supernovae"
        },
        {
            "id": "lgm-1",
            "tier": "middle",
            "t": "The first one’s signal, repeating every 1.3 seconds, was jokingly labeled LGM-1, for “Little Green Men”",
            "k": [
                "lgm-1",
                "little green men",
                "1.3 seconds"
            ],
            "n": 0
        },
        {
            "id": "hewish-nobel",
            "tier": "middle",
            "t": "Antony Hewish shared the 1974 Nobel Prize in Physics, the first for astronomy, but Bell was left out",
            "k": [
                "hewish",
                "1974",
                "left out"
            ],
            "n": 0
        },
        {
            "id": "crab",
            "tier": "middle",
            "t": "The one in the Crab Nebula (from a supernova seen in 1054 CE) spins about 30 times a second and powers the nebula’s glow",
            "k": [
                "crab nebula",
                "1054",
                "30 times"
            ],
            "n": 0,
            "rabbit": "Crab Nebula"
        },
        {
            "id": "magnetic-poles",
            "tier": "middle",
            "t": "Their beams come from magnetic poles that are tilted away from the spin axis",
            "k": [
                "magnetic poles",
                "spin axis"
            ],
            "n": 0
        },
        {
            "id": "millisecond",
            "tier": "middle",
            "t": "Millisecond ones are “recycled”: spun up by gas pulled from a partner star",
            "k": [
                "millisecond",
                "recycled",
                "partner star"
            ],
            "n": 0
        },
        {
            "id": "hulse-taylor",
            "tier": "middle",
            "t": "Russell Hulse and Joseph Taylor’s binary system (found 1974) matched Einstein’s gravitational waves, winning a 1993 Nobel Prize",
            "k": [
                "hulse",
                "taylor",
                "gravitational waves"
            ],
            "n": 0
        },
        {
            "id": "planets-1992",
            "tier": "middle",
            "t": "The first confirmed exoplanets (1992) orbit one; Aleksander Wolszczan and Dale Frail found them by pulse timing",
            "k": [
                "exoplanets",
                "wolszczan",
                "1992"
            ],
            "n": 0,
            "rabbit": "Exoplanets"
        },
        {
            "id": "gold-1968",
            "tier": "middle",
            "t": "Thomas Gold explained them in 1968; the slowing spin of the Crab Nebula’s one confirmed his idea",
            "k": [
                "thomas gold",
                "1968"
            ],
            "n": 0
        },
        {
            "id": "spin-down",
            "tier": "middle",
            "t": "They slowly spin down as they lose energy, so older ones turn more slowly; at last their beams fade out",
            "k": [
                "spin down",
                "older ones"
            ],
            "n": 0
        },
        {
            "id": "cosmic-clocks",
            "tier": "middle",
            "t": "Their pulses arrive so steadily that some rival atomic clocks",
            "k": [
                "atomic clocks",
                "steadily"
            ],
            "n": 0
        },
        {
            "id": "breakthrough",
            "tier": "power",
            "t": "Jocelyn Bell Burnell won a $3 million Breakthrough Prize in 2018 and gave it all to fund physics scholarships",
            "k": [
                "breakthrough prize",
                "scholarships",
                "2018"
            ],
            "n": 0
        },
        {
            "id": "scruff",
            "tier": "power",
            "t": "Bell first saw the signal as a bit of “scruff” on long paper charts from a radio telescope she helped build",
            "k": [
                "scruff",
                "paper charts"
            ],
            "n": 0
        },
        {
            "id": "pioneer-voyager-map",
            "tier": "power",
            "t": "Pioneer plaques and Voyager Golden Records show the Sun’s location with a map of 14 of them, written in binary code",
            "k": [
                "pioneer",
                "golden records",
                "binary code"
            ],
            "n": 0
        },
        {
            "id": "terzan-5",
            "tier": "power",
            "t": "As of 2025, the fastest known one spun 716 times a second, in the star cluster Terzan 5",
            "k": [
                "716",
                "terzan 5"
            ],
            "n": 0
        },
        {
            "id": "nanograv",
            "tier": "power",
            "t": "NANOGrav (2023) timed dozens of them for 15 years and found evidence of a background hum of gravitational waves",
            "k": [
                "nanograv",
                "2023",
                "hum"
            ],
            "n": 0
        },
        {
            "id": "vela-glitches",
            "tier": "power",
            "t": "The Vela one spins about 11 times a second; sudden speedups called glitches may come from a superfluid inside",
            "k": [
                "vela",
                "glitches",
                "superfluid"
            ],
            "n": 0
        },
        {
            "id": "unknown-pleasures",
            "tier": "power",
            "t": "Joy Division’s album _Unknown Pleasures_ (1979) shows stacked pulses from CP 1919, the first one found",
            "k": [
                "joy division",
                "unknown pleasures",
                "cp 1919"
            ],
            "n": 0
        },
        {
            "id": "black-widow",
            "tier": "power",
            "t": "“Black widow” ones slowly evaporate their small partner stars with radiation and wind",
            "k": [
                "black widow",
                "evaporate"
            ],
            "n": 0
        },
        {
            "id": "dispersion",
            "tier": "power",
            "t": "Dispersion: free electrons in space delay the lower radio frequencies, which reveals how far away one is",
            "k": [
                "dispersion",
                "free electrons"
            ],
            "n": 0
        },
        {
            "id": "psr",
            "tier": "power",
            "t": "Their catalog names begin with the letters PSR",
            "k": [
                "psr",
                "catalog names"
            ],
            "n": 0
        },
        {
            "id": "cen-x3",
            "tier": "power",
            "t": "Centaurus X-3, spotted by the Uhuru satellite in 1971, was the first found ticking in X-rays",
            "k": [
                "centaurus x-3",
                "uhuru",
                "x-rays"
            ],
            "n": 0
        },
        {
            "id": "x-ray-navigation",
            "tier": "power",
            "t": "In 2017, an experiment on the International Space Station showed that X-ray ones could guide spacecraft like a GPS",
            "k": [
                "space station",
                "gps",
                "guide spacecraft"
            ],
            "n": 0
        }
    ],
    "trap": {
        "title": "Pulsar, neutron star, or quasar?",
        "body": "Pulsars are spinning neutron stars, but not every neutron star is seen as a pulsar, and “Neutron stars” is a separate answer line. On a pulsar question, saying “neutron star” earns a prompt; on a neutron star question, saying “pulsar” is wrong. Quasars sound alike but are something else entirely: blazing disks of gas around supermassive black holes in faraway galaxies.",
        "fix": "Regular ticks, the lighthouse beam, LGM-1, the Crab’s 30 spins a second, millisecond timing, and the Hulse–Taylor binary mean pulsars. If the clues describe the whole family of super-dense collapsed stars (Baade and Zwicky, the Tolman–Oppenheimer–Volkoff limit), say neutron stars. Galaxy-outshining glows and black holes mean quasars.",
        "line": "Real answer line: <b><u>Pulsars</u></b> (accept <u>pulsar</u>; prompt on <u>neutron star</u>s)"
    },
    "tests": {
        "right": [
            "Pulsars",
            "pulsar",
            "Pulsers",
            "millisecond pulsars",
            "a pulsar"
        ],
        "prompt": [
            "Neutron stars",
            "neutron star",
            "rotating neutron star"
        ],
        "wrong": [
            "Quasars",
            "Magnetar",
            "White dwarf",
            "Neutrons",
            "Crab Nebula",
            "Black hole"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
