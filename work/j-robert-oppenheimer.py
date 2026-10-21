import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

data = {
    "id": "j-robert-oppenheimer",
    "name": "J. Robert Oppenheimer",
    "mono": "JRO",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Physicist who led Los Alamos · “Father of the atomic bomb”",
    "dates": "1904–1967",
    "briefing": "J. Robert Oppenheimer was a brilliant theoretical physicist who also loved poetry and learned Sanskrit to read Hindu scriptures. During World War II, he directed the secret Los Alamos laboratory that built the first atomic bombs, and he later recalled that the Trinity test of July 1945 brought to mind a line from the _Bhagavad Gita_: “Now I am become Death, the destroyer of worlds.” In 1954, the government took away his security clearance, a decision it reversed in 2022.",
    "answerHtml": "J. Robert <b><u>Oppenheimer</u></b> (or Julius Robert <u>Oppenheimer</u>; do not accept “Frank Oppenheimer”)",
    "accept": [
        "j robert oppenheimer",
        "robert oppenheimer",
        "oppenheimer",
        "julius robert oppenheimer",
        "j r oppenheimer",
        "julius oppenheimer"
    ],
    "prompt": [],
    "reject": [
        "frank oppenheimer",
        "kitty oppenheimer",
        "katherine oppenheimer",
        "born oppenheimer",
        "born oppenheimer approximation",
        "tolman oppenheimer volkoff",
        "tolman oppenheimer volkoff limit",
        "oppenheimer volkoff",
        "oppenheimer snyder",
        "enrico fermi",
        "fermi",
        "leslie groves",
        "groves",
        "edward teller",
        "teller",
        "albert einstein",
        "einstein",
        "niels bohr",
        "hans bethe",
        "richard feynman",
        "leo szilard",
        "lewis strauss",
        "ernest lawrence",
        "max born",
        "werner heisenberg",
        "harry truman",
        "manhattan project",
        "trinity",
        "trinity test",
        "los alamos"
    ],
    "tests": {
        "right": [
            "J. Robert Oppenheimer",
            "Robert Oppenheimer",
            "Oppenheimer",
            "Julius Robert Oppenheimer",
            "Oppenhiemer",
            "Dr. Oppenheimer"
        ],
        "prompt": [],
        "wrong": [
            "Enrico Fermi",
            "Leslie Groves",
            "Edward Teller",
            "Albert Einstein",
            "Frank Oppenheimer",
            "Manhattan Project",
            "Born-Oppenheimer approximation"
        ]
    },
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/J._Robert_Oppenheimer",
    "qb": {
        "q": "Oppenheimer",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "As a graduate student at Göttingen [“GUR-ting-en”], this man worked with his adviser Max Born on an approximation that treats the motion of atomic nuclei separately from the motion of electrons in molecules. Years later, he built a leading school of theoretical physics at Berkeley.",
            "r": "During World War II, he directed the Los Alamos laboratory. For 10 points, name this “father of the atomic bomb.”"
        },
        {
            "p": "In 1939, this physicist and his student Hartland Snyder described how a very massive star could collapse until not even light could escape, an early prediction of black holes. That same year, he and George Volkoff calculated the largest possible mass of a neutron star.",
            "r": "For 10 points, name this physicist who later led the Los Alamos laboratory during the Manhattan Project."
        },
        {
            "p": "This man learned Sanskrit at Berkeley so he could read Hindu scriptures in their original language. In a 1965 television interview, he said that while watching a famous explosion twenty years earlier, he had remembered words spoken by the god Vishnu.",
            "r": "That line from the _Bhagavad Gita_ is “Now I am become Death, the destroyer of worlds.” For 10 points, name this director of the Los Alamos laboratory."
        },
        {
            "p": "This man later said he chose the code name for a test after thinking of the poems of John Donne, including one that begins “Batter my heart, three-person’d God.” That test took place in the Jornada del Muerto [“hor-NAH-dah del MWAIR-toh”] desert.",
            "r": "That test, code-named Trinity, was the first nuclear explosion. For 10 points, name this director of the Los Alamos laboratory."
        },
        {
            "p": "General Leslie Groves surprised many people by choosing this Berkeley professor, who had never run a large project and had no Nobel Prize, to lead a top-secret weapons laboratory. This man suggested putting the lab on a New Mexico mesa he had visited on horseback trips.",
            "r": "That lab at Los Alamos designed the first atomic bombs. For 10 points, name this physicist."
        },
        {
            "p": "This man was the main scientific author of the 1946 Acheson–Lilienthal Report, which proposed placing atomic energy under international control. From 1947 to 1952, he chaired the General Advisory Committee of the Atomic Energy Commission.",
            "r": "Earlier, he had directed the laboratory at Los Alamos. For 10 points, name this physicist called the “father of the atomic bomb.”"
        },
        {
            "p": "In 1949, a committee this man chaired advised against a crash program to build the hydrogen bomb, a weapon championed by Edward Teller. Five years later, Teller testified at a hearing that ended with this man losing his security clearance.",
            "r": "For 10 points, name this physicist who had directed the Los Alamos laboratory during the Manhattan Project."
        },
        {
            "p": "Atomic Energy Commission chairman Lewis Strauss pushed for a 1954 hearing that led to this physicist losing his security clearance. In 2022, Secretary of Energy Jennifer Granholm reversed that decision, saying the process had been flawed.",
            "r": "For 10 points, name this scientist who led the Los Alamos laboratory during World War II."
        },
        {
            "p": "In December 1963, President Lyndon Johnson presented this man with the Enrico Fermi Award, which John F. Kennedy had planned to give him before Kennedy was assassinated. Nine years earlier, this man had lost his security clearance.",
            "r": "For 10 points, name this physicist who had led the Los Alamos laboratory, where the first atomic bombs were built."
        },
        {
            "p": "From 1947 to 1966, this man directed the Institute for Advanced Study in Princeton, New Jersey, where Albert Einstein was one of his colleagues. He died of throat cancer in Princeton in 1967.",
            "r": "For 10 points, name this physicist who had led the Los Alamos laboratory during the Manhattan Project."
        },
        {
            "p": "Kai Bird and Martin Sherwin won a Pulitzer Prize for _American Prometheus_, a 2005 biography of this man. That book was the basis for a 2023 film that won Best Picture, and Cillian Murphy won Best Actor for playing this man.",
            "r": "That film was directed by Christopher Nolan. For 10 points, name this “father of the atomic bomb.”"
        },
        {
            "p": "This man was born in New York City in 1904 and attended the city’s Ethical Culture School before finishing Harvard in just three years. He later earned his doctorate in Germany and taught at both Berkeley and Caltech.",
            "r": "For 10 points, name this physicist who directed the Los Alamos laboratory that built the first atomic bombs."
        },
        {
            "p": "In John Adams’s 2005 opera _Doctor Atomic_, this man waits through a stormy night before a famous test in the New Mexico desert. Peter Sellars built that opera’s libretto from real documents and poems.",
            "r": "That test was code-named Trinity. For 10 points, name this director of the Los Alamos laboratory."
        },
        {
            "p": "Friends called this physicist “Oppie,” and his younger brother Frank, also a physicist, founded San Francisco’s Exploratorium science museum in 1969. This man’s trademark look included a pipe and a porkpie hat.",
            "r": "For 10 points, name this physicist who led the Los Alamos laboratory and recalled the words “Now I am become Death.”"
        },
        {
            "p": "This man directed Project Y, a secret laboratory whose mail went to a post office box in Santa Fe, and he recruited scientists such as Hans Bethe and Richard Feynman to work there.",
            "r": "That lab, at Los Alamos, built the bombs dropped on Hiroshima and Nagasaki. For 10 points, name this “father of the atomic bomb.”"
        }
    ],
    "clues": [
        {
            "id": "los-alamos",
            "tier": "giveaway",
            "t": "Scientific director of the Los Alamos laboratory in New Mexico, where the first atomic bombs were designed",
            "k": ["los alamos", "new mexico", "director"],
            "n": 0
        },
        {
            "id": "father",
            "tier": "giveaway",
            "t": "Called the “father of the atomic bomb”",
            "k": ["father of the atomic bomb", "atomic bomb"],
            "n": 0
        },
        {
            "id": "manhattan-project",
            "tier": "giveaway",
            "t": "Led the scientists of the Manhattan Project, the secret World War II program to build the bomb",
            "k": ["manhattan project", "world war ii"],
            "n": 0,
            "rabbit": "Manhattan Project"
        },
        {
            "id": "gita",
            "tier": "giveaway",
            "t": "Recalled a line from the _Bhagavad Gita_: “Now I am become Death, the destroyer of worlds”",
            "k": ["bhagavad gita", "destroyer of worlds", "become death"],
            "n": 0
        },
        {
            "id": "trinity",
            "tier": "giveaway",
            "t": "Watched the Trinity test, the first nuclear explosion, on July 16, 1945",
            "k": ["trinity", "july 16, 1945", "first nuclear explosion"],
            "n": 0
        },
        {
            "id": "groves",
            "tier": "middle",
            "t": "General Leslie Groves chose him in 1942, though he had never run a large project and had no Nobel Prize",
            "k": ["leslie groves", "groves", "1942"],
            "n": 0
        },
        {
            "id": "clearance",
            "tier": "middle",
            "t": "Lost his security clearance after a 1954 Atomic Energy Commission hearing",
            "k": ["security clearance", "1954", "hearing"],
            "n": 0
        },
        {
            "id": "teller",
            "tier": "middle",
            "t": "Opposed a crash program for the hydrogen bomb (1949); Edward Teller testified against him in 1954",
            "k": ["edward teller", "teller", "hydrogen bomb"],
            "n": 0
        },
        {
            "id": "ias",
            "tier": "middle",
            "t": "Directed the Institute for Advanced Study in Princeton, New Jersey, from 1947 to 1966",
            "k": ["institute for advanced study", "princeton", "1947"],
            "n": 0
        },
        {
            "id": "fermi-award",
            "tier": "middle",
            "t": "Received the Enrico Fermi Award from Lyndon Johnson in December 1963",
            "k": ["fermi award", "1963", "lyndon johnson"],
            "n": 0,
            "rabbit": "Enrico Fermi"
        },
        {
            "id": "reversal-2022",
            "tier": "middle",
            "t": "In 2022, the Department of Energy reversed the 1954 decision, saying the process had been flawed",
            "k": ["2022", "department of energy", "reversed"],
            "n": 0
        },
        {
            "id": "nolan-film",
            "tier": "middle",
            "t": "Christopher Nolan’s 2023 film about him won Best Picture, and Cillian Murphy won Best Actor for playing him",
            "k": ["christopher nolan", "nolan", "cillian murphy", "best picture"],
            "n": 0
        },
        {
            "id": "american-prometheus",
            "tier": "middle",
            "t": "The Pulitzer-winning biography _American Prometheus_ (2005), by Kai Bird and Martin Sherwin, was the basis for that film",
            "k": ["american prometheus", "kai bird", "sherwin"],
            "n": 0
        },
        {
            "id": "donne",
            "tier": "power",
            "t": "Said he named the Trinity test after thinking of John Donne’s poems, such as “Batter my heart, three-person’d God”",
            "k": ["john donne", "donne", "batter my heart"],
            "n": 0
        },
        {
            "id": "vishnu",
            "tier": "power",
            "t": "Learned Sanskrit at Berkeley; in a 1965 TV interview he said the line he remembered was spoken by the god Vishnu",
            "k": ["sanskrit", "vishnu", "1965"],
            "n": 0
        },
        {
            "id": "max-born",
            "tier": "power",
            "t": "At Göttingen, worked with his adviser Max Born on an approximation (1927) that treats nuclei and electrons in molecules separately",
            "k": ["max born", "göttingen", "approximation"],
            "n": 0
        },
        {
            "id": "volkoff",
            "tier": "power",
            "t": "With George Volkoff, calculated the largest possible mass of a neutron star (1939)",
            "k": ["volkoff", "neutron star", "1939"],
            "n": 0
        },
        {
            "id": "snyder",
            "tier": "power",
            "t": "With his student Hartland Snyder, described the collapse of a massive star (1939), an early prediction of black holes",
            "k": ["hartland snyder", "snyder", "black holes"],
            "n": 0
        },
        {
            "id": "berkeley",
            "tier": "power",
            "t": "Built a leading school of theoretical physics at Berkeley and Caltech in the 1930s",
            "k": ["berkeley", "caltech", "theoretical physics"],
            "n": 0
        },
        {
            "id": "ethical-culture",
            "tier": "power",
            "t": "Born in New York City (1904); attended the Ethical Culture School and finished Harvard in three years",
            "k": ["ethical culture", "harvard", "new york city"],
            "n": 0
        },
        {
            "id": "acheson-lilienthal",
            "tier": "power",
            "t": "Main scientific author of the Acheson–Lilienthal Report (1946), which proposed international control of atomic energy",
            "k": ["acheson", "lilienthal", "international control"],
            "n": 0
        },
        {
            "id": "general-advisory",
            "tier": "power",
            "t": "Chaired the Atomic Energy Commission’s General Advisory Committee from 1947 to 1952",
            "k": ["general advisory committee", "1952"],
            "n": 0
        },
        {
            "id": "strauss",
            "tier": "power",
            "t": "Atomic Energy Commission chairman Lewis Strauss pushed for the 1954 hearing; Robert Downey Jr. played Strauss in the 2023 film",
            "k": ["lewis strauss", "strauss", "downey"],
            "n": 0
        },
        {
            "id": "project-y",
            "tier": "power",
            "t": "Directed Project Y, whose mail went to a post office box in Santa Fe; suggested the mesa site; recruited Hans Bethe and Richard Feynman",
            "k": ["project y", "santa fe", "hans bethe", "mesa"],
            "n": 0
        },
        {
            "id": "doctor-atomic",
            "tier": "power",
            "t": "Main character of John Adams’s 2005 opera _Doctor Atomic_, with a libretto by Peter Sellars",
            "k": ["doctor atomic", "opera", "peter sellars"],
            "n": 0
        },
        {
            "id": "oppie",
            "tier": "power",
            "t": "Nicknamed “Oppie”; his younger brother Frank founded San Francisco’s Exploratorium (1969); known for his pipe and porkpie hat",
            "k": ["oppie", "exploratorium", "porkpie"],
            "n": 0
        },
        {
            "id": "died-1967",
            "tier": "power",
            "t": "Died of throat cancer in Princeton in 1967",
            "k": ["throat cancer", "1967"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Not Fermi, Teller, or Groves",
        "body": "Many people worked on the atomic bomb, and several are answers of their own. General Leslie Groves ran the whole Manhattan Project; Enrico Fermi built the first nuclear reactor in Chicago; Edward Teller pushed for the hydrogen bomb and testified against this man in 1954; and Albert Einstein signed the 1939 letter warning Franklin Roosevelt but never worked on the bomb. A question about “this program” wants the Manhattan Project itself.",
        "fix": "Los Alamos, the _Bhagavad Gita_ line, the name “Trinity,” the 1954 security hearing, and the Institute for Advanced Study mean this man. Groves means the Army general who built the Pentagon; Fermi means Chicago Pile-1; Teller means the hydrogen bomb.",
        "line": "Real answer line: J. Robert <b><u>Oppenheimer</u></b> (or Julius Robert <u>Oppenheimer</u>)"
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
