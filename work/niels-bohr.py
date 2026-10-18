import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "niels-bohr",
    "name": "Niels Bohr",
    "mono": "BHR",
    "category": "Physics",
    "qbCategory": "Science · Physics",
    "kicker": "Danish father of the quantum atom · Electrons in fixed orbits",
    "dates": "1885–1962",
    "briefing": "Niels Bohr was a Danish physicist who, in 1913, pictured the atom as a tiny solar system in which electrons can travel only in certain fixed orbits, jumping between them by giving off or absorbing light. That idea explained the colors of light that glowing hydrogen gives off and helped win him the 1922 Nobel Prize in Physics. His institute in Copenhagen became a world center for the new science of quantum mechanics.",
    "answerHtml": "<b><u>Niels Bohr</u></b> (accept <u>Bohr</u>; do not accept “Aage Bohr”)",
    "accept": [
        "niels bohr",
        "bohr",
        "niels henrik david bohr",
        "niels h d bohr"
    ],
    "prompt": [],
    "reject": [
        "aage bohr",
        "christian bohr",
        "harald bohr",
        "bohr model",
        "bohr radius",
        "bohr effect",
        "bohr magneton",
        "bohrium",
        "werner heisenberg",
        "heisenberg",
        "ernest rutherford",
        "rutherford",
        "max planck",
        "max born",
        "arnold sommerfeld",
        "sommerfeld",
        "j j thomson",
        "albert einstein",
        "einstein",
        "erwin schrodinger",
        "schrodinger",
        "wolfgang pauli",
        "copenhagen interpretation"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Niels_Bohr",
    "qb": {
        "q": "Bohr",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "When this scientist received the Order of the Elephant in 1947, he chose a coat of arms showing the yin-yang symbol and the Latin motto “Contraria sunt complementa,” or “opposites are complementary.” That motto reflected his principle of complementarity.",
            "r": "For 10 points, name this Danish physicist whose 1913 model of the atom placed electrons in fixed orbits."
        },
        {
            "p": "This scientist’s theory of the periodic table predicted that element 72 would resemble zirconium rather than the rare earths, and in 1923 two researchers at his institute found it and named it hafnium, after the Latin name for his home city.",
            "r": "Element 107 is also named for him. For 10 points, name this Danish physicist who proposed a model of the hydrogen atom in 1913."
        },
        {
            "p": "In 1940, as German troops occupied Copenhagen, George de Hevesy [“HEV-eh-shee”] dissolved the gold Nobel Prize medals of Max von Laue and James Franck in aqua regia at this scientist’s institute to hide them from the Nazis. The gold was later recovered and the medals were recast.",
            "r": "For 10 points, name this Danish physicist who won the 1922 Nobel Prize for his model of the atom."
        },
        {
            "p": "In 1943, this scientist escaped from occupied Denmark to Sweden on a fishing boat, then flew to Britain in the bomb bay of a Mosquito airplane and passed out from lack of oxygen. He later advised the Manhattan Project under the false name “Nicholas Baker.”",
            "r": "His son Aage later won a Nobel Prize too. For 10 points, name this Danish physicist who modeled the atom with electrons in fixed orbits."
        },
        {
            "p": "In 1939, this scientist and John Wheeler explained nuclear fission with a liquid-drop model of the nucleus, and he realized that the rare isotope uranium-235 is the one that splits when hit by slow neutrons. Earlier that year, he had carried news of fission’s discovery to the United States.",
            "r": "For 10 points, name this Danish physicist whose 1913 atomic model put electrons in fixed energy levels."
        },
        {
            "p": "At a 1927 conference in Como, Italy, this scientist introduced complementarity, the idea that light and electrons show wave or particle behavior depending on the experiment, but never both at once. He and Werner Heisenberg developed the Copenhagen interpretation of quantum mechanics.",
            "r": "For 10 points, name this Danish physicist who won the 1922 Nobel Prize in Physics for his work on atomic structure."
        },
        {
            "p": "This scientist’s correspondence principle says that quantum physics must give the same answers as classical physics for very large quantum numbers, such as electrons in huge orbits. In his model, an electron’s angular momentum must be a whole-number multiple of Planck’s constant divided by two pi.",
            "r": "That model explained the lines in hydrogen’s spectrum. For 10 points, name this Danish physicist who proposed it in 1913."
        },
        {
            "p": "At the 1930 Solvay Conference, this scientist answered Albert Einstein’s “photon box” challenge to quantum mechanics by using Einstein’s own general relativity. This scientist also replied to a famous 1935 paper by Einstein, Podolsky, and Rosen.",
            "r": "For 10 points, name this Danish physicist whose 1913 model of the atom had electrons jumping between fixed orbits."
        },
        {
            "p": "After working with Ernest Rutherford in Manchester, this scientist published a three-part paper in 1913, often called his “trilogy,” in the journal _Philosophical Magazine_. That work explained the Balmer series of visible lines in hydrogen’s spectrum and the value of the Rydberg constant.",
            "r": "In his model, electrons give off light when they jump down between fixed orbits. For 10 points, name this Danish physicist."
        },
        {
            "p": "Michael Frayn’s 1998 play _Copenhagen_ imagines what this scientist and his former assistant Werner Heisenberg said during a mysterious 1941 meeting in German-occupied Denmark. The play’s third character is this scientist’s wife, Margrethe.",
            "r": "For 10 points, name this Danish physicist who won the 1922 Nobel Prize for his work on the structure of atoms."
        },
        {
            "p": "This scientist’s son Aage won the 1975 Nobel Prize in Physics for work on the structure of atomic nuclei, and his father, Christian, found that carbon dioxide helps blood release oxygen. His brother Harald was a mathematician who won an Olympic silver medal in soccer.",
            "r": "For 10 points, name this Danish physicist whose model of the atom had electrons in fixed orbits."
        },
        {
            "p": "The radius of the smallest electron orbit in this scientist’s model of hydrogen, about 0.053 nanometers, is named for him. Arnold Sommerfeld later improved this scientist’s model by allowing electrons to follow elliptical orbits.",
            "r": "His model could not explain atoms with more than one electron, such as helium. For 10 points, name this Danish physicist who proposed that model in 1913."
        },
        {
            "p": "In 1944, this scientist urged Winston Churchill and Franklin Roosevelt to tell the Soviet Union about the atomic bomb project to avoid an arms race, and in 1950 he wrote an open letter to the United Nations calling for an “open world.”",
            "r": "For 10 points, name this Danish physicist whose model of the atom had electrons jumping between fixed orbits."
        },
        {
            "p": "In 1921, this scientist opened an institute for theoretical physics at the University of Copenhagen, where young physicists like Werner Heisenberg and Wolfgang Pauli came to work. The institute was later renamed for him.",
            "r": "For 10 points, name this Danish physicist whose 1913 model of the hydrogen atom placed electrons in fixed orbits."
        },
        {
            "p": "This scientist’s Nobel Prize in Physics was announced at the same time as Albert Einstein’s delayed prize for 1921. This scientist had earlier worked with J. J. Thomson at Cambridge before moving to Manchester to work with Ernest Rutherford.",
            "r": "For 10 points, name this Danish physicist whose atomic model placed electrons in fixed, numbered energy levels."
        }
    ],
    "clues": [
        {
            "id": "model-1913",
            "tier": "giveaway",
            "t": "Proposed a 1913 model of the hydrogen atom with electrons in fixed orbits, or energy levels",
            "k": ["1913", "fixed orbits", "energy levels"],
            "n": 0,
            "rabbit": "Hydrogen"
        },
        {
            "id": "danish",
            "tier": "giveaway",
            "t": "Danish physicist (1885–1962) from Copenhagen",
            "k": ["danish", "copenhagen", "1885"],
            "n": 0,
            "rabbit": "Denmark"
        },
        {
            "id": "nobel-1922",
            "tier": "giveaway",
            "t": "Won the 1922 Nobel Prize in Physics for his work on the structure of atoms",
            "k": ["1922", "nobel prize", "structure of atoms"],
            "n": 0
        },
        {
            "id": "jumps",
            "tier": "giveaway",
            "t": "In his model, electrons give off or absorb light when they jump between orbits",
            "k": ["jump", "give off", "absorb light"],
            "n": 0
        },
        {
            "id": "element-107",
            "tier": "giveaway",
            "t": "Element 107 is named for him",
            "k": ["element 107"],
            "n": 0
        },
        {
            "id": "institute",
            "tier": "middle",
            "t": "Opened an institute for theoretical physics in Copenhagen in 1921, later named for him; Heisenberg and Pauli worked there",
            "k": ["institute", "1921", "heisenberg", "pauli"],
            "n": 0,
            "rabbit": "Pauli exclusion principle"
        },
        {
            "id": "copenhagen-interpretation",
            "tier": "middle",
            "t": "Developed the Copenhagen interpretation of quantum mechanics with Werner Heisenberg",
            "k": ["copenhagen interpretation", "werner heisenberg"],
            "n": 0,
            "rabbit": "Uncertainty principle"
        },
        {
            "id": "complementarity",
            "tier": "middle",
            "t": "Introduced complementarity at a 1927 conference in Como, Italy: wave or particle behavior, depending on the experiment, but never both at once",
            "k": ["complementarity", "como", "1927"],
            "n": 0
        },
        {
            "id": "correspondence",
            "tier": "middle",
            "t": "Correspondence principle: quantum physics must match classical physics for very large quantum numbers",
            "k": ["correspondence principle", "classical physics"],
            "n": 0
        },
        {
            "id": "angular-momentum",
            "tier": "middle",
            "t": "In his model, an electron’s angular momentum is a whole-number multiple of Planck’s constant divided by 2π",
            "k": ["angular momentum", "planck’s constant", "whole-number"],
            "n": 0,
            "rabbit": "Angular momentum"
        },
        {
            "id": "rutherford-thomson",
            "tier": "middle",
            "t": "Worked with J. J. Thomson at Cambridge and Ernest Rutherford at Manchester before his 1913 model",
            "k": ["rutherford", "manchester", "cambridge"],
            "n": 0
        },
        {
            "id": "balmer",
            "tier": "middle",
            "t": "His model explained the Balmer series of hydrogen’s spectral lines and the value of the Rydberg constant",
            "k": ["balmer series", "rydberg constant", "spectral lines"],
            "n": 0
        },
        {
            "id": "einstein-debates",
            "tier": "middle",
            "t": "Debated Albert Einstein about quantum mechanics for years, including at the Solvay conferences and in reply to a 1935 paper by Einstein, Podolsky, and Rosen",
            "k": ["einstein", "solvay", "podolsky"],
            "n": 0,
            "rabbit": "Albert Einstein"
        },
        {
            "id": "fission",
            "tier": "middle",
            "t": "With John Wheeler (1939), explained nuclear fission with a liquid-drop model; saw that uranium-235 splits with slow neutrons",
            "k": ["liquid-drop", "john wheeler", "uranium-235", "fission"],
            "n": 0
        },
        {
            "id": "escape",
            "tier": "middle",
            "t": "Escaped occupied Denmark to Sweden by fishing boat in 1943, then flew to Britain in a Mosquito’s bomb bay and passed out from lack of oxygen",
            "k": ["1943", "fishing boat", "mosquito", "sweden"],
            "n": 0
        },
        {
            "id": "coat-of-arms",
            "tier": "power",
            "t": "His 1947 coat of arms showed the yin-yang symbol and the motto “Contraria sunt complementa” (opposites are complementary)",
            "k": ["yin-yang", "contraria sunt complementa", "1947"],
            "n": 0
        },
        {
            "id": "hafnium",
            "tier": "power",
            "t": "Predicted that element 72 would resemble zirconium; found at his institute in 1923, it was named hafnium for Copenhagen’s Latin name",
            "k": ["hafnium", "element 72", "zirconium", "1923"],
            "n": 0
        },
        {
            "id": "de-hevesy",
            "tier": "power",
            "t": "At his institute in 1940, George de Hevesy dissolved the gold Nobel medals of Max von Laue and James Franck in aqua regia to hide them",
            "k": ["de hevesy", "von laue", "franck", "aqua regia"],
            "n": 0,
            "rabbit": "Acids"
        },
        {
            "id": "nicholas-baker",
            "tier": "power",
            "t": "Advised the Manhattan Project under the false name “Nicholas Baker”",
            "k": ["nicholas baker", "manhattan project"],
            "n": 0,
            "rabbit": "Manhattan Project"
        },
        {
            "id": "trilogy",
            "tier": "power",
            "t": "Published his model as a three-part 1913 “trilogy” in the journal _Philosophical Magazine_",
            "k": ["trilogy", "philosophical magazine"],
            "n": 0
        },
        {
            "id": "frayn",
            "tier": "power",
            "t": "Michael Frayn’s 1998 play _Copenhagen_ imagines his 1941 meeting with Heisenberg; his wife, Margrethe, is the third character",
            "k": ["michael frayn", "1941", "margrethe"],
            "n": 0
        },
        {
            "id": "family",
            "tier": "power",
            "t": "Son Aage won the 1975 Nobel Prize in Physics; father Christian studied how blood releases oxygen; brother Harald won an Olympic soccer silver",
            "k": ["aage", "christian", "harald", "1975"],
            "n": 0,
            "rabbit": "Hemoglobin"
        },
        {
            "id": "radius",
            "tier": "power",
            "t": "The radius of the smallest orbit in his hydrogen model, about 0.053 nanometers, is named for him",
            "k": ["radius", "0.053", "smallest orbit"],
            "n": 0
        },
        {
            "id": "sommerfeld",
            "tier": "power",
            "t": "Arnold Sommerfeld extended his model to elliptical orbits; the model failed for atoms with more than one electron, like helium",
            "k": ["sommerfeld", "elliptical", "helium"],
            "n": 0
        },
        {
            "id": "open-world",
            "tier": "power",
            "t": "In 1944 urged Churchill and Roosevelt to tell the Soviet Union about the atomic bomb project; wrote a 1950 open letter to the United Nations",
            "k": ["churchill", "roosevelt", "open letter", "1950"],
            "n": 0
        },
        {
            "id": "einstein-1921",
            "tier": "power",
            "t": "His Nobel Prize was announced at the same time as Einstein’s delayed prize for 1921",
            "k": ["delayed", "1921"],
            "n": 0
        },
        {
            "id": "photon-box",
            "tier": "power",
            "t": "At the 1930 Solvay Conference, answered Einstein’s “photon box” challenge using general relativity",
            "k": ["photon box", "1930", "general relativity"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Not Rutherford or Heisenberg",
        "body": "Several founders of atomic physics show up in the same tossups. Ernest Rutherford discovered the nucleus with his gold foil experiment, and this man then put the electrons into fixed orbits around it; Werner Heisenberg, his younger colleague, created matrix mechanics and the uncertainty principle. The family is a trap too: his son Aage won a Nobel Prize in 1975, and his father Christian’s name is on the Bohr effect in blood.",
        "fix": "Fixed orbits, energy levels, hydrogen’s spectrum, complementarity, Copenhagen, or element 107 mean this man. The gold foil experiment and the nucleus mean Rutherford; matrix mechanics and uncertainty mean Heisenberg; and a 1975 Nobel for work on atomic nuclei means his son Aage, so give the full name if you can.",
        "line": "Real answer line: <b><u>Niels Bohr</u></b> (accept <u>Bohr</u>; do not accept “Aage Bohr”)"
    },
    "tests": {
        "right": [
            "Niels Bohr",
            "Bohr",
            "Neils Bohr",
            "Nils Bohr",
            "Dr. Bohr"
        ],
        "prompt": [],
        "wrong": [
            "Aage Bohr",
            "Ernest Rutherford",
            "Werner Heisenberg",
            "Max Planck",
            "Bohr model"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
