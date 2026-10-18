import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

data = {
    "id": "cosmic-microwave-background",
    "name": "Cosmic microwave background",
    "mono": "CMB",
    "category": "Astronomy",
    "qbCategory": "Science · Other Science (Astronomy)",
    "kicker": "Leftover glow of the Big Bang · Fills the whole sky at about 2.7 kelvins",
    "dates": "Predicted 1948; discovered 1964",
    "briefing": "The cosmic microwave background is the faint afterglow of the Big Bang: light released about 380,000 years after the universe began, since stretched into microwaves as the universe expanded. It fills the entire sky with a chill of about 2.7 degrees above absolute zero. Two Bell Labs scientists found it by accident in 1964 while trying to get rid of a mysterious hiss in their antenna, and at first they blamed pigeon droppings.",
    "answerHtml": "<b><u>Cosmic microwave background</u></b> radiation (accept <u>CMB</u> or <u>CMBR</u>; accept <u>cosmic background radiation</u>; prompt on <u>background radiation</u> or <u>microwave</u>s; do not accept “Big Bang” or “cosmic rays”)",
    "accept": [
        "cosmic microwave background",
        "cosmic microwave background radiation",
        "cmb",
        "cmbr",
        "cmb radiation",
        "cosmic background radiation",
        "cosmic background",
        "microwave background",
        "microwave background radiation",
        "relic radiation"
    ],
    "prompt": [
        "background radiation",
        "microwave radiation",
        "microwaves",
        "microwave",
        "radiation",
        "cosmic radiation",
        "cosmic microwave radiation",
        "blackbody radiation",
        "black body radiation",
        "big bang radiation",
        "afterglow of the big bang"
    ],
    "reject": [
        "big bang",
        "cosmic rays",
        "cosmic ray",
        "gamma rays",
        "gamma ray burst",
        "x rays",
        "radio waves",
        "infrared radiation",
        "hawking radiation",
        "dark energy",
        "dark matter",
        "cosmic neutrino background",
        "gravitational waves",
        "solar wind",
        "redshift",
        "hubbles law"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Cosmic_microwave_background",
    "qb": {
        "q": "microwave background",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "While hunting for the source of a stubborn hiss in their horn antenna in Holmdel, New Jersey, two scientists evicted nesting pigeons and cleaned out their droppings, but the hiss did not go away. The two later shared the 1978 Nobel Prize in Physics.",
            "r": "Those scientists, Arno Penzias and Robert Wilson, had found this faint radiation left over from the Big Bang. For 10 points, name this glow that fills the whole sky."
        },
        {
            "p": "In 1948, Ralph Alpher and Robert Herman predicted that this radiation should exist with a temperature of about 5 kelvins, but their prediction was largely forgotten for years. Their work grew out of George Gamow’s studies of how the first chemical elements formed.",
            "r": "This radiation was finally detected in 1964. For 10 points, name this afterglow of the Big Bang, which fills the sky."
        },
        {
            "p": "When Robert Dicke heard about a puzzling signal in a phone call, he reportedly told his Princeton team, “Boys, we’ve been scooped,” because they had been building an instrument to search for this radiation. His group, which included Jim Peebles, published a paper explaining the signal alongside the discoverers’ report in 1965.",
            "r": "The signal had been found by two scientists at Bell Labs. For 10 points, name this faint radiation left over from the Big Bang."
        },
        {
            "p": "In 1990, the FIRAS instrument on the COBE satellite showed that this radiation matches a perfect blackbody curve almost exactly, and COBE’s DMR instrument later found tiny hot and cold spots in it. John Mather and George Smoot shared the 2006 Nobel Prize in Physics for that work.",
            "r": "This radiation is the afterglow of the Big Bang. For 10 points, name this faint glow that fills the sky."
        },
        {
            "p": "Light from this radiation reaches us from a “surface of last scattering” and has been redshifted by a factor of about 1,100. It was released when the young universe cooled enough for electrons and protons to join into neutral atoms, an event called recombination.",
            "r": "That happened about 380,000 years after the Big Bang. For 10 points, name this afterglow that fills the whole sky."
        },
        {
            "p": "Because the Sun is moving relative to this radiation, one half of the sky looks very slightly warmer in it than the other, a pattern called the dipole. Apart from that, its temperature varies across the sky by only about one part in 100,000.",
            "r": "Its temperature is only about 2.7 kelvins. For 10 points, name this leftover radiation from the Big Bang."
        },
        {
            "p": "NASA named a spacecraft that mapped this radiation from 2001 to 2010 for David Wilkinson, and the European Space Agency’s Planck satellite mapped it in even finer detail starting in 2009. Those maps helped pin down the age of the universe at about 13.8 billion years.",
            "r": "It is the oldest light in the universe. For 10 points, name this faint afterglow of the Big Bang, which fills the entire sky."
        },
        {
            "p": "In the Sunyaev–Zeldovich effect, hot gas in galaxy clusters gives an energy boost to some of this radiation as it passes through. Photons of this radiation also lose a little energy as they climb out of clumps of matter, an effect named for Sachs and Wolfe.",
            "r": "This radiation was released about 380,000 years after the Big Bang. For 10 points, name this glow that fills the sky."
        },
        {
            "p": "In 2014, the BICEP2 team at the South Pole announced that swirling “B-mode” patterns in the polarization of this radiation showed signs of gravitational waves from the universe’s first moments. Within a year, a joint study with the Planck team showed that dust in the Milky Way could explain the signal.",
            "r": "For 10 points, name this radiation left over from the Big Bang, which has a temperature of about 2.7 kelvins."
        },
        {
            "p": "A small part of the snowy static on old analog television sets came from this radiation. Because it is so cold, its brightness peaks at a wavelength of about one millimeter, as Wien’s [“VEENZ”] law predicts.",
            "r": "It is the leftover glow from the Big Bang. For 10 points, name this radiation, discovered by Arno Penzias and Robert Wilson."
        },
        {
            "p": "WMAP images of this radiation revealed an unusually large “Cold Spot” in the direction of the constellation Eridanus. A graph of how strong its hot and cold spots are at each size shows peaks caused by sound waves that rippled through the young universe.",
            "r": "For 10 points, name this faint glow left over from the Big Bang, mapped in detail by the Planck satellite."
        },
        {
            "p": "The discovery of this radiation dealt a major blow to the Steady State theory of Fred Hoyle, Hermann Bondi, and Thomas Gold, which said the universe has always looked the same. Hoyle had coined the name of the rival theory that this radiation supports during a 1949 radio broadcast.",
            "r": "That rival theory is the Big Bang. For 10 points, name this afterglow, which has a temperature of about 2.7 kelvins."
        },
        {
            "p": "The 20-foot horn antenna that first detected this radiation had been built in New Jersey to receive signals bounced off Echo, a giant balloon satellite. Its discoverers measured an extra temperature of about 3.5 kelvins that they could not explain.",
            "r": "For 10 points, name this radiation that Arno Penzias and Robert Wilson discovered, the leftover glow of the Big Bang."
        },
        {
            "p": "Jim Peebles, who shared the 2019 Nobel Prize in Physics, helped explain how tiny ripples in this radiation trace the seeds that later grew into galaxies. The sizes of those ripples show that space is very nearly flat.",
            "r": "This radiation was discovered in 1964. For 10 points, name this faint afterglow of the Big Bang."
        },
        {
            "p": "When this radiation was released, it glowed at about 3,000 kelvins, like the surface of a cool star, but the universe’s expansion has since stretched its waves more than a thousand times longer. Its photons outnumber all the protons and neutrons in the universe by more than a billion to one.",
            "r": "Today it is only about 2.7 kelvins. For 10 points, name this faint radiation left over from the Big Bang."
        }
    ],
    "clues": [
        {
            "id": "big-bang-afterglow",
            "tier": "giveaway",
            "t": "The faint leftover glow of the Big Bang, the oldest light in the universe",
            "k": ["big bang", "oldest light", "leftover"],
            "n": 0,
            "rabbit": "Big Bang"
        },
        {
            "id": "penzias-wilson",
            "tier": "giveaway",
            "t": "Discovered by accident in 1964 by Arno Penzias and Robert Wilson of Bell Labs (1978 Nobel Prize)",
            "k": ["penzias", "wilson", "bell labs", "1964"],
            "n": 0
        },
        {
            "id": "temperature",
            "tier": "giveaway",
            "t": "Its temperature is only about 2.7 kelvins (2.725 K), just above absolute zero",
            "k": ["2.7 kelvins", "absolute zero"],
            "n": 0
        },
        {
            "id": "every-direction",
            "tier": "giveaway",
            "t": "Comes from every direction in the sky and looks almost exactly the same everywhere",
            "k": ["every direction", "same everywhere"],
            "n": 0
        },
        {
            "id": "pigeons",
            "tier": "middle",
            "t": "Its discoverers evicted nesting pigeons and cleaned out their droppings from their horn antenna in Holmdel, New Jersey, but the hiss stayed",
            "k": ["pigeon", "holmdel", "horn antenna"],
            "n": 0
        },
        {
            "id": "alpher-herman",
            "tier": "middle",
            "t": "Predicted in 1948 by Ralph Alpher and Robert Herman, who expected a temperature of about 5 kelvins",
            "k": ["alpher", "herman", "1948"],
            "n": 0
        },
        {
            "id": "dicke",
            "tier": "middle",
            "t": "Robert Dicke’s Princeton team was about to search for it when he learned it had been found: “Boys, we’ve been scooped”",
            "k": ["dicke", "princeton", "scooped"],
            "n": 0
        },
        {
            "id": "recombination",
            "tier": "middle",
            "t": "Released about 380,000 years after the Big Bang, when electrons and protons joined into neutral atoms (recombination)",
            "k": ["380,000", "recombination", "neutral atoms"],
            "n": 0
        },
        {
            "id": "cobe",
            "tier": "middle",
            "t": "The COBE satellite showed it is an almost perfect blackbody and found tiny ripples; John Mather and George Smoot won the 2006 Nobel Prize",
            "k": ["cobe", "blackbody", "mather", "smoot"],
            "n": 0
        },
        {
            "id": "wmap-planck",
            "tier": "middle",
            "t": "Mapped in detail by NASA’s WMAP (2001–2010) and Europe’s Planck satellite (launched 2009)",
            "k": ["wmap", "planck"],
            "n": 0
        },
        {
            "id": "one-part",
            "tier": "middle",
            "t": "Its tiny hot and cold spots differ by only about one part in 100,000",
            "k": ["one part in 100,000", "hot and cold spots"],
            "n": 0
        },
        {
            "id": "steady-state",
            "tier": "middle",
            "t": "Its discovery was a major blow to the Steady State theory of Fred Hoyle, Hermann Bondi, and Thomas Gold",
            "k": ["steady state", "hoyle"],
            "n": 0
        },
        {
            "id": "tv-static",
            "tier": "middle",
            "t": "A small part of the snowy static on old analog TV sets came from it; its brightness peaks at a wavelength of about one millimeter",
            "k": ["static", "analog", "one millimeter"],
            "n": 0
        },
        {
            "id": "stretched",
            "tier": "middle",
            "t": "Released at about 3,000 kelvins, its light has been stretched more than a thousand times by the expanding universe",
            "k": ["stretched", "3,000 kelvins"],
            "n": 0
        },
        {
            "id": "last-scattering",
            "tier": "power",
            "t": "It comes from the “surface of last scattering” and has been redshifted by a factor of about 1,100",
            "k": ["last scattering", "1,100"],
            "n": 0
        },
        {
            "id": "dipole",
            "tier": "power",
            "t": "The Sun’s motion makes one half of the sky look very slightly warmer in it, a pattern called the dipole",
            "k": ["dipole", "warmer"],
            "n": 0
        },
        {
            "id": "sunyaev-zeldovich",
            "tier": "power",
            "t": "Sunyaev–Zeldovich effect: hot gas in galaxy clusters gives some of its photons an energy boost",
            "k": ["sunyaev", "zeldovich", "galaxy clusters"],
            "n": 0
        },
        {
            "id": "sachs-wolfe",
            "tier": "power",
            "t": "Sachs–Wolfe effect: its photons lose a little energy climbing out of clumps of matter",
            "k": ["sachs", "wolfe", "clumps"],
            "n": 0
        },
        {
            "id": "bicep2",
            "tier": "power",
            "t": "In 2014, BICEP2 claimed signs of early gravitational waves in its polarization, but dust in the Milky Way explained the signal",
            "k": ["bicep2", "polarization", "dust"],
            "n": 0
        },
        {
            "id": "cold-spot",
            "tier": "power",
            "t": "WMAP revealed an unusually large “Cold Spot” in it, toward the constellation Eridanus",
            "k": ["cold spot", "eridanus"],
            "n": 0
        },
        {
            "id": "acoustic-peaks",
            "tier": "power",
            "t": "Peaks in a graph of its spot sizes come from sound waves in the young universe and show that space is nearly flat",
            "k": ["sound waves", "peaks", "flat"],
            "n": 0
        },
        {
            "id": "wilkinson",
            "tier": "power",
            "t": "WMAP was named for David Wilkinson; WMAP and Planck maps put the age of the universe at about 13.8 billion years",
            "k": ["wilkinson", "13.8 billion"],
            "n": 0
        },
        {
            "id": "echo",
            "tier": "power",
            "t": "The 20-foot horn antenna that found it, built for the Echo balloon satellite, picked up an unexplained extra 3.5 kelvins",
            "k": ["echo", "balloon", "3.5 kelvins"],
            "n": 0
        },
        {
            "id": "peebles",
            "tier": "power",
            "t": "Jim Peebles, a member of Dicke’s team, shared the 2019 Nobel Prize in Physics for work in cosmology",
            "k": ["peebles", "2019"],
            "n": 0
        },
        {
            "id": "gamow",
            "tier": "power",
            "t": "Alpher and Herman’s prediction grew out of George Gamow’s work on how the first chemical elements formed",
            "k": ["gamow", "chemical elements"],
            "n": 0
        },
        {
            "id": "billion-to-one",
            "tier": "power",
            "t": "Its photons outnumber all the protons and neutrons in the universe by more than a billion to one",
            "k": ["billion to one", "photons"],
            "n": 0
        },
        {
            "id": "hoyle-name",
            "tier": "power",
            "t": "Fred Hoyle coined the name of the rival theory it supports, the Big Bang, in a 1949 radio broadcast",
            "k": ["1949", "radio broadcast"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Radiation, not the Big Bang",
        "body": "Almost every tossup on this radiation ends by calling it the afterglow of the Big Bang, and players who hear “Big Bang” buzz with “Big Bang,” which is a different answer line. Others say “cosmic rays,” which are fast-moving particles, not light. Saying only “background radiation” or “microwaves” earns a prompt, so be ready to give the full name.",
        "fix": "If the question asks for “this radiation,” “this glow,” or the signal found by Penzias and Wilson, answer “cosmic microwave background” (or “CMB”). If it asks for “this theory” or “this event” at the start of the universe, the answer is the Big Bang.",
        "line": "Real answer line: <b><u>cosmic microwave background</u></b> radiation (accept <u>CMB</u> or <u>CMBR</u>; prompt on partial answers)"
    },
    "tests": {
        "right": [
            "Cosmic microwave background",
            "CMB",
            "cosmic microwave background radiation",
            "Cosmic microwave backround",
            "CMBR",
            "the cosmic microwave background"
        ],
        "prompt": [
            "background radiation",
            "microwaves"
        ],
        "wrong": [
            "Big Bang",
            "Cosmic rays",
            "Dark energy",
            "Hawking radiation",
            "Gamma rays"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
