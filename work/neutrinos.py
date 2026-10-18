import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "neutrinos",
    "name": "Neutrinos",
    "mono": "NU",
    "category": "Physics",
    "qbCategory": "Science · Physics",
    "kicker": "Nearly massless “ghost particles” · Trillions pass through you every second",
    "dates": "Proposed by Wolfgang Pauli, 1930; first detected 1956",
    "briefing": "Neutrinos are tiny particles with no electric charge and almost no mass, and they barely interact with anything, so trillions of them stream through your body every second without a trace. Wolfgang Pauli proposed them in 1930 to explain where energy seemed to vanish in radioactive beta decay, but they weren’t detected until 1956. Scientists catch them with giant tanks of water deep underground, or with a cubic kilometer of ice at the South Pole.",
    "answerHtml": "<b><u>neutrino</u></b>s (accept specific types like <u>electron neutrino</u>s or <u>antineutrino</u>s; prompt on <u>lepton</u>s; do not accept “neutrons”)",
    "accept": [
        "neutrinos",
        "neutrino",
        "antineutrino",
        "antineutrinos",
        "electron neutrino",
        "electron neutrinos",
        "muon neutrino",
        "muon neutrinos",
        "tau neutrino",
        "tau neutrinos",
        "electron antineutrino",
        "electron antineutrinos",
        "muon antineutrino",
        "muon antineutrinos",
        "tau antineutrino",
        "tau antineutrinos",
        "sterile neutrino",
        "sterile neutrinos",
        "solar neutrino",
        "solar neutrinos"
    ],
    "prompt": [
        "lepton",
        "leptons"
    ],
    "reject": [
        "neutron",
        "neutrons",
        "antineutron",
        "antineutrons",
        "neutralino",
        "neutralinos",
        "neutron star",
        "neutrino oscillation",
        "neutrino oscillations",
        "photon",
        "photons",
        "positron",
        "positrons",
        "dark matter",
        "quark",
        "quarks",
        "w boson",
        "z boson"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Neutrino",
    "qb": {
        "q": "neutrino",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In 2011, the OPERA experiment reported measurements suggesting that these particles traveled from CERN to a lab in Italy faster than light, but the result was traced to a loose fiber-optic cable. These particles come in three flavors: electron, muon, and tau.",
            "r": "For 10 points, name these nearly massless, electrically neutral particles first proposed by Wolfgang Pauli."
        },
        {
            "p": "Ray Davis used a huge tank of dry-cleaning fluid deep in a South Dakota gold mine to catch these particles from the Sun, but found only about a third as many as John Bahcall had predicted. That shortfall was explained when scientists learned these particles change type as they travel.",
            "r": "Trillions of them pass through your body every second. For 10 points, name these ghostly, nearly massless particles that stream out of the Sun."
        },
        {
            "p": "Clyde Cowan and Frederick Reines first detected these particles in 1956, using tanks of water placed near a nuclear reactor at the Savannah River plant in South Carolina. Reines shared the 1995 Nobel Prize in Physics for that discovery.",
            "r": "These particles barely interact with matter. For 10 points, name these tiny, electrically neutral particles given off in beta decay."
        },
        {
            "p": "Wolfgang Pauli first proposed these particles in a 1930 letter that began “Dear Radioactive Ladies and Gentlemen,” calling his idea a “desperate remedy” to save the conservation of energy. Enrico Fermi later gave these particles their name, Italian for “little neutral one.”",
            "r": "For 10 points, name these particles, which are given off along with electrons in beta decay."
        },
        {
            "p": "About two dozen of these particles from Supernova 1987A were caught by detectors in Japan, the United States, and the Soviet Union, arriving hours before the exploding star’s light was seen. Masatoshi Koshiba shared the 2002 Nobel Prize for detecting them.",
            "r": "For 10 points, name these nearly massless particles, which come in electron, muon, and tau flavors."
        },
        {
            "p": "In 1998, the Super-Kamiokande detector in Japan found that these particles, made when cosmic rays hit the atmosphere, change from one type to another, proving that they have mass. Takaaki Kajita and Arthur McDonald shared the 2015 Nobel Prize for discovering such changes.",
            "r": "For 10 points, name these elusive particles that interact only through gravity and the weak force."
        },
        {
            "p": "A detector filled with 1,000 metric tons of heavy water, two kilometers underground in a Canadian nickel mine, showed that these particles from the Sun change type on their way to Earth. Arthur McDonald led that project, called SNO.",
            "r": "For 10 points, name these tiny particles produced in huge numbers by fusion in the Sun’s core."
        },
        {
            "p": "The IceCube observatory uses a cubic kilometer of ice at the South Pole to detect flashes of light made when these particles strike atoms. In 2018, IceCube traced one of these particles back to a blazar, a distant galaxy with a jet pointed at Earth.",
            "r": "For 10 points, name these ghostly particles that can pass through the entire Earth without stopping."
        },
        {
            "p": "Leon Lederman, Melvin Schwartz, and Jack Steinberger won a Nobel Prize for showing in 1962 that these particles come in more than one type. The tau type of these particles was first seen directly in 2000 at Fermilab.",
            "r": "For 10 points, name these electrically neutral particles that Wolfgang Pauli proposed to save the conservation of energy."
        },
        {
            "p": "Physicists hunt for a rare double beta decay that releases two electrons but none of these particles, which would show that these particles are their own antiparticles. Ettore Majorana [“mah-yoh-RAH-nah”] first suggested that such particles could exist.",
            "r": "They have far less mass than an electron. For 10 points, name these nearly massless particles that stream from the Sun by the trillions."
        },
        {
            "p": "The KATRIN experiment in Germany measures the energies of electrons given off in the beta decay of tritium to find out how heavy these particles can be. These particles travel at nearly the speed of light.",
            "r": "They are given off in beta decay. For 10 points, name these particles, nicknamed “ghost particles,” that rarely interact with matter."
        },
        {
            "p": "Super-Kamiokande uses about 11,000 light sensors lining a giant tank of ultrapure water to spot rings of Cherenkov [“chuh-REN-kof”] light made when these particles strike the water. These particles are hard to catch because they feel only gravity and the weak force.",
            "r": "For 10 points, name these particles that also pour out of nuclear reactors and the Sun."
        },
        {
            "p": "About 99 percent of the energy released when a massive star’s core collapses in a supernova is carried away by these particles. Huge numbers of these particles are also made by fusion in the Sun’s core.",
            "r": "Trillions of them pass through you every second. For 10 points, name these particles, which have no electric charge and almost no mass."
        },
        {
            "p": "The MSW effect describes how traveling through dense matter, such as the inside of the Sun, changes the way these particles switch from one type to another. These particles feel only gravity and the weak force, so most pass straight through the whole Earth.",
            "r": "For 10 points, name these ghostly particles that come in electron, muon, and tau flavors and were first proposed by Wolfgang Pauli."
        },
        {
            "p": "Maurice Goldhaber’s team showed that these particles are always “left-handed,” spinning opposite to the direction they travel. Because these particles have no electric charge, they ignore electromagnetism and pass through matter almost untouched. Pions and muons give off these particles when they decay.",
            "r": "For 10 points, name these particles, which Enrico Fermi named with an Italian word meaning “little neutral one.”"
        }
    ],
    "clues": [
        {
            "id": "ghost",
            "tier": "giveaway",
            "t": "Nicknamed “ghost particles”: no electric charge, almost no mass, and they barely interact with matter",
            "k": ["ghost particles", "no electric charge", "almost no mass"],
            "n": 0
        },
        {
            "id": "trillions",
            "tier": "giveaway",
            "t": "Trillions from the Sun pass through your body every second without a trace",
            "k": ["trillions", "every second"],
            "n": 0
        },
        {
            "id": "beta-decay",
            "tier": "giveaway",
            "t": "Given off in radioactive beta decay, along with an electron",
            "k": ["beta decay", "electron"],
            "n": 0
        },
        {
            "id": "pauli-fermi",
            "tier": "giveaway",
            "t": "Proposed by Wolfgang Pauli (1930); named by Enrico Fermi, Italian for “little neutral one”",
            "k": ["wolfgang pauli", "enrico fermi", "little neutral one"],
            "n": 0,
            "rabbit": "Enrico Fermi"
        },
        {
            "id": "flavors",
            "tier": "giveaway",
            "t": "Come in three flavors: electron, muon, and tau",
            "k": ["three flavors", "muon", "tau"],
            "n": 0
        },
        {
            "id": "weak-gravity",
            "tier": "middle",
            "t": "Feel only the weak force and gravity, so most pass straight through the whole Earth",
            "k": ["weak force", "whole earth"],
            "n": 0,
            "rabbit": "Weak nuclear force"
        },
        {
            "id": "cowan-reines",
            "tier": "middle",
            "t": "First detected in 1956 by Clyde Cowan and Frederick Reines near a nuclear reactor",
            "k": ["cowan", "reines", "1956"],
            "n": 0
        },
        {
            "id": "sun",
            "tier": "middle",
            "t": "Made in huge numbers by fusion in the Sun’s core",
            "k": ["fusion", "sun’s core"],
            "n": 0,
            "rabbit": "The Sun"
        },
        {
            "id": "oscillation",
            "tier": "middle",
            "t": "They change flavor as they travel (oscillation), which shows that they have mass",
            "k": ["oscillation", "change flavor"],
            "n": 0
        },
        {
            "id": "detectors",
            "tier": "middle",
            "t": "Caught in giant underground tanks of water (Super-Kamiokande in Japan) or in ice at the South Pole (IceCube)",
            "k": ["super-kamiokande", "icecube", "south pole"],
            "n": 0
        },
        {
            "id": "sn-1987a",
            "tier": "middle",
            "t": "About two dozen from Supernova 1987A were detected, arriving hours before its light; Masatoshi Koshiba shared the 2002 Nobel Prize",
            "k": ["supernova 1987a", "two dozen", "koshiba"],
            "n": 0,
            "rabbit": "Supernovae"
        },
        {
            "id": "desperate-remedy",
            "tier": "middle",
            "t": "Pauli’s 1930 letter, opening “Dear Radioactive Ladies and Gentlemen,” called them a “desperate remedy” to save conservation of energy",
            "k": ["desperate remedy", "dear radioactive", "conservation of energy"],
            "n": 0
        },
        {
            "id": "leptons",
            "tier": "middle",
            "t": "They are leptons, the neutral partners of the electron, the muon, and the tau",
            "k": ["leptons", "neutral partners"],
            "n": 0
        },
        {
            "id": "speed",
            "tier": "middle",
            "t": "Travel at nearly the speed of light and have far less mass than an electron",
            "k": ["speed of light", "less mass"],
            "n": 0
        },
        {
            "id": "davis",
            "tier": "power",
            "t": "Ray Davis’s tank of dry-cleaning fluid in a South Dakota gold mine caught only about a third of the predicted solar ones",
            "k": ["ray davis", "dry-cleaning fluid", "gold mine"],
            "n": 0
        },
        {
            "id": "bahcall",
            "tier": "power",
            "t": "John Bahcall predicted how many should come from the Sun; the shortfall was called the “solar problem”",
            "k": ["bahcall", "shortfall"],
            "n": 0
        },
        {
            "id": "super-k-1998",
            "tier": "power",
            "t": "1998: Super-Kamiokande saw ones from the atmosphere change type; Kajita and McDonald won the 2015 Nobel Prize",
            "k": ["1998", "kajita", "mcdonald"],
            "n": 0
        },
        {
            "id": "sno",
            "tier": "power",
            "t": "SNO, a detector full of heavy water in a Canadian nickel mine, showed that solar ones change type on the way to Earth",
            "k": ["sno", "heavy water", "nickel mine"],
            "n": 0
        },
        {
            "id": "opera",
            "tier": "power",
            "t": "OPERA’s 2011 faster-than-light result was traced to a loose fiber-optic cable",
            "k": ["opera", "faster-than-light", "fiber-optic"],
            "n": 0
        },
        {
            "id": "lederman",
            "tier": "power",
            "t": "Lederman, Schwartz, and Steinberger found the muon type in 1962; the tau type was first seen at Fermilab in 2000",
            "k": ["lederman", "steinberger", "1962", "fermilab"],
            "n": 0
        },
        {
            "id": "majorana",
            "tier": "power",
            "t": "Searches for a double beta decay that gives off two electrons and nothing else test whether they are their own antiparticles (Majorana particles)",
            "k": ["majorana", "double beta decay", "antiparticles"],
            "n": 0,
            "rabbit": "Antimatter"
        },
        {
            "id": "katrin",
            "tier": "power",
            "t": "KATRIN, in Germany, measures the beta decay of tritium to find how heavy they can be",
            "k": ["katrin", "tritium"],
            "n": 0
        },
        {
            "id": "msw",
            "tier": "power",
            "t": "The MSW effect: traveling through dense matter changes how they switch types",
            "k": ["msw effect", "dense matter"],
            "n": 0
        },
        {
            "id": "blazar",
            "tier": "power",
            "t": "In 2018, IceCube traced one to a blazar, a distant galaxy with a jet pointed at Earth",
            "k": ["blazar", "2018"],
            "n": 0
        },
        {
            "id": "supernova-energy",
            "tier": "power",
            "t": "Carry away about 99 percent of the energy of a collapsing star’s core",
            "k": ["99 percent", "collapsing star"],
            "n": 0
        },
        {
            "id": "goldhaber",
            "tier": "power",
            "t": "Maurice Goldhaber’s team showed they are always “left-handed,” spinning opposite to their motion",
            "k": ["goldhaber", "left-handed"],
            "n": 0
        },
        {
            "id": "cherenkov",
            "tier": "power",
            "t": "Super-Kamiokande’s about 11,000 light sensors watch for rings of Cherenkov light",
            "k": ["cherenkov", "light sensors", "11,000"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Neutrino or neutron?",
        "body": "The names sound alike because Pauli first called his proposed particle a “neutron,” but Enrico Fermi renamed it the neutrino, or “little neutral one,” after James Chadwick discovered the much heavier neutron in 1932. Neutrons sit in the nucleus with protons and are about as heavy as a proton; neutrinos are almost massless and zip through matter at nearly the speed of light. Both have no electric charge, so “neutral” alone won’t tell you which one a tossup wants.",
        "fix": "Ghost particles, the missing energy in beta decay, the Sun, oscillation, Super-Kamiokande, or IceCube means neutrinos. The nucleus, Chadwick, neutron stars, or nuclear chain reactions means neutrons.",
        "line": "Real answer line: <b><u>neutrino</u></b>s (accept specific types like <u>electron neutrino</u>s; do not accept “neutrons”)"
    },
    "tests": {
        "right": [
            "Neutrinos",
            "neutrino",
            "Electron neutrino",
            "Antineutrinos",
            "Nuetrinos"
        ],
        "prompt": [
            "Leptons"
        ],
        "wrong": [
            "Neutrons",
            "Neutron",
            "Neutralino",
            "Photons",
            "Neutrino oscillation",
            "Electrons"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
