import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "penicillin",
    "name": "Penicillin",
    "mono": "PEN",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Antibiotic Alexander Fleming found in a mold · Fights bacterial infections",
    "dates": "Discovered 1928",
    "briefing": "In 1928, Alexander Fleming came back from a summer vacation to his London lab and found a mold growing on one of his dishes of bacteria, with a clear, germ-free ring around it. The mold was making penicillin, which kills bacteria by stopping them from building their cell walls. Howard Florey and Ernst Chain later turned it into a real medicine, and it saved huge numbers of lives during World War II.",
    "answerHtml": "<b><u>Penicillin</u></b> (accept <u>penicillin G</u>, <u>penicillin V</u>, or <u>benzylpenicillin</u>; prompt on <u>antibiotics</u> or <u>beta-lactam antibiotics</u>; do not accept “Penicillium” or “amoxicillin”)",
    "accept": [
        "penicillin",
        "penicillins",
        "penicillin g",
        "penicillin v",
        "benzylpenicillin",
        "phenoxymethylpenicillin"
    ],
    "prompt": [
        "antibiotic",
        "antibiotics",
        "antibacterial",
        "antibacterials",
        "beta lactam",
        "beta lactams",
        "beta lactam antibiotic",
        "beta lactam antibiotics"
    ],
    "reject": [
        "penicillium",
        "penicillium mold",
        "penicillinase",
        "amoxicillin",
        "ampicillin",
        "methicillin",
        "cephalosporin",
        "cephalosporins",
        "streptomycin",
        "sulfa drugs",
        "lysozyme",
        "alexander fleming",
        "fleming",
        "mold",
        "mould",
        "fungus",
        "fungi"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Penicillin",
    "qb": {
        "q": "penicillin",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "A lab worker nicknamed “Moldy Mary” found an especially productive strain of the mold that makes this drug on a cantaloupe from a market in Peoria, Illinois. Scientists at a government lab in Peoria boosted production of this drug by growing that mold in deep tanks fed with corn steep liquor.",
            "r": "Howard Florey and Ernst Chain had already turned this drug into a medicine at Oxford. For 10 points, name this antibiotic discovered by Alexander Fleming in 1928."
        },
        {
            "p": "In 1945, Dorothy Crowfoot Hodgkin used X-ray crystallography to show that this drug contains a strained, four-membered ring called a beta-lactam [“BAY-tuh LAK-tam”] ring. Hodgkin later won the 1964 Nobel Prize in Chemistry for finding the structures of molecules, including this drug and vitamin B12.",
            "r": "It kills bacteria by blocking how they build their cell walls. For 10 points, name this antibiotic made by a mold, which Alexander Fleming discovered."
        },
        {
            "p": "This drug binds to enzymes called transpeptidases [“trans-PEP-tih-day-sez”] and stops them from cross-linking peptidoglycan [“pep-tih-doh-GLY-kan”], so a growing bacterium’s wall turns weak and the cell bursts. Human cells are not harmed by this drug because they have no cell walls.",
            "r": "For 10 points, name this antibiotic that Alexander Fleming discovered when a mold killed bacteria in one of his dishes."
        },
        {
            "p": "Some bacteria resist this drug by making beta-lactamase [“BAY-tuh LAK-tuh-mayss”] enzymes that break open its four-membered ring, which is why its relative amoxicillin is often combined with clavulanic [“klav-yoo-LAN-ik”] acid, a chemical that blocks those enzymes. MRSA is a staph bacterium that resists another relative of this drug, methicillin.",
            "r": "It was mass-produced for Allied troops during World War II. For 10 points, name this antibiotic produced by a mold and discovered by Alexander Fleming."
        },
        {
            "p": "Norman Heatley worked out how to extract this drug from mold broth at Oxford, where his team grew the mold in shallow containers that included hospital bedpans. Their team, led by Howard Florey with Ernst Chain, showed in 1940 that this drug could protect infected mice.",
            "r": "Florey, Chain, and Alexander Fleming shared the 1945 Nobel Prize for this drug. For 10 points, name this antibiotic made by a mold."
        },
        {
            "p": "In 1942, Anne Miller of New Haven, Connecticut, became one of the first patients in the United States to be treated successfully with this drug. By the D-Day invasion in 1944, American factories were making enough of this drug to treat wounded Allied soldiers.",
            "r": "For 10 points, name this antibiotic, which Alexander Fleming first noticed when a mold killed bacteria on one of his dishes."
        },
        {
            "p": "Before naming this substance, its discoverer called it “mould juice,” and he first described it in a 1929 paper. He had found it at St. Mary’s Hospital in London after returning from a summer vacation in 1928.",
            "r": "He saw that bacteria near a spot of mold on one of his dishes had been destroyed. For 10 points, name this antibiotic discovered by Alexander Fleming."
        },
        {
            "p": "One form of this drug, labeled with the letter G, is usually given as a shot because stomach acid breaks it down, while a form labeled V can be swallowed as a pill. Amoxicillin and ampicillin are partly man-made relatives of this drug.",
            "r": "For 10 points, name this antibiotic, discovered when Alexander Fleming saw a mold killing bacteria."
        },
        {
            "p": "This drug works best against Gram-positive bacteria, whose thick cell walls hold on to a purple stain, such as the bacteria that cause strep throat. It does nothing against viruses, so it cannot cure a cold or the flu.",
            "r": "For 10 points, name this antibiotic, first found in a mold by Alexander Fleming."
        },
        {
            "p": "In his 1945 Nobel Prize lecture, this drug’s discoverer warned that using too little of it could let bacteria become resistant to it. Ernst Chain, a German-born scientist who had moved to England in 1933, helped purify this drug with the Australian Howard Florey.",
            "r": "It was first noticed when a mold killed bacteria on a lab dish. For 10 points, name this antibiotic discovered by Alexander Fleming."
        },
        {
            "p": "Years before finding this drug, its Scottish discoverer found lysozyme [“LYE-soh-zime”], a germ-fighting enzyme in tears and mucus. That discoverer was born on a farm in Ayrshire, Scotland, and did his research at St. Mary’s Hospital in London.",
            "r": "In 1928, he noticed that a mold had killed bacteria on one of his culture plates. For 10 points, name this antibiotic discovered by Alexander Fleming."
        },
        {
            "p": "John Sheehan of MIT first made this drug entirely from simple chemicals in 1957, though it is still mostly produced by growing mold in huge tanks. Its molecule has a four-membered beta-lactam ring joined to a five-membered ring that contains sulfur.",
            "r": "It blocks bacteria from building their cell walls. For 10 points, name this antibiotic that Alexander Fleming discovered in 1928."
        },
        {
            "p": "The mold spore that led to this drug’s discovery may have drifted up from a mold research lab on the floor below its discoverer’s lab. He had left his dishes of staph bacteria stacked on a bench while he took a summer vacation.",
            "r": "When he returned in September 1928, he saw that the mold had killed bacteria near it. For 10 points, name this antibiotic discovered by Alexander Fleming."
        },
        {
            "p": "Early supplies of this drug were so scarce that doctors at Oxford recovered it from patients’ urine to use again, since the kidneys clear it from the blood quickly. Ernst Chain and Howard Florey led the Oxford team that first tested it on people, in 1941.",
            "r": "This drug was mass-produced in the United States during World War II. For 10 points, name this antibiotic first noticed by Alexander Fleming."
        },
        {
            "p": "Cephalosporins [“SEF-uh-loh-SPOR-inz”] share a four-membered beta-lactam ring with this drug, and like it, they were first found in a fungus. Both kinds of drugs kill bacteria by stopping them from building their cell walls.",
            "r": "For 10 points, name this antibiotic discovered by Alexander Fleming after a mold spoiled one of his dishes of bacteria."
        }
    ],
    "clues": [
        {
            "id": "fleming-1928",
            "tier": "giveaway",
            "t": "Discovered by Alexander Fleming in 1928, when a mold killed the bacteria growing near it on a dish",
            "k": ["fleming", "1928", "mold"],
            "n": 0,
            "rabbit": "Alexander Fleming"
        },
        {
            "id": "antibiotic",
            "tier": "giveaway",
            "t": "One of the first antibiotics, drugs that kill bacteria",
            "k": ["antibiotics", "bacteria"],
            "n": 0,
            "rabbit": "Bacteria"
        },
        {
            "id": "mold",
            "tier": "giveaway",
            "t": "Made naturally by a mold, a kind of fungus",
            "k": ["mold", "fungus"],
            "n": 0,
            "rabbit": "Fungi"
        },
        {
            "id": "nobel-1945",
            "tier": "giveaway",
            "t": "Fleming, Howard Florey, and Ernst Chain shared the 1945 Nobel Prize in medicine for it",
            "k": ["nobel prize", "1945", "florey", "chain"],
            "n": 0
        },
        {
            "id": "not-viruses",
            "tier": "giveaway",
            "t": "Works against bacteria, not viruses, so it can’t cure a cold or the flu",
            "k": ["viruses", "cold", "flu"],
            "n": 0,
            "rabbit": "Viruses"
        },
        {
            "id": "st-marys",
            "tier": "middle",
            "t": "Fleming found it at St. Mary’s Hospital in London, after a summer vacation",
            "k": ["london", "st. mary’s", "vacation"],
            "n": 0
        },
        {
            "id": "oxford",
            "tier": "middle",
            "t": "Howard Florey and Ernst Chain’s team at Oxford turned it into a usable medicine in 1940–1941",
            "k": ["oxford", "florey", "chain"],
            "n": 0
        },
        {
            "id": "cell-walls",
            "tier": "middle",
            "t": "Kills bacteria by stopping them from building their cell walls, so they burst",
            "k": ["cell walls", "burst"],
            "n": 0,
            "rabbit": "Cell wall"
        },
        {
            "id": "transpeptidase",
            "tier": "middle",
            "t": "Blocks transpeptidase enzymes that cross-link peptidoglycan in the bacterial wall",
            "k": ["transpeptidase", "peptidoglycan", "cross-link"],
            "n": 0
        },
        {
            "id": "human-cells",
            "tier": "middle",
            "t": "Human cells have no cell walls, so it leaves them unharmed",
            "k": ["human cells", "no cell walls"],
            "n": 0
        },
        {
            "id": "beta-lactam",
            "tier": "middle",
            "t": "Its key structure is a strained, four-membered beta-lactam ring",
            "k": ["beta-lactam", "four-membered"],
            "n": 0
        },
        {
            "id": "world-war-ii",
            "tier": "middle",
            "t": "Mass-produced in the United States during World War II; enough was ready to treat Allied soldiers by D-Day (1944)",
            "k": ["world war ii", "d-day", "1944"],
            "n": 0
        },
        {
            "id": "resistance",
            "tier": "middle",
            "t": "Some bacteria resist it with beta-lactamase enzymes; MRSA resists its relative methicillin",
            "k": ["beta-lactamase", "mrsa", "methicillin"],
            "n": 0
        },
        {
            "id": "relatives",
            "tier": "middle",
            "t": "Amoxicillin and ampicillin are partly man-made members of its family",
            "k": ["amoxicillin", "ampicillin"],
            "n": 0
        },
        {
            "id": "gram-positive",
            "tier": "middle",
            "t": "Works best on Gram-positive bacteria, like the ones that cause strep throat",
            "k": ["gram-positive", "strep throat"],
            "n": 0
        },
        {
            "id": "hodgkin",
            "tier": "power",
            "t": "Dorothy Crowfoot Hodgkin found its structure by X-ray crystallography in 1945; she won the 1964 Nobel Prize in Chemistry",
            "k": ["hodgkin", "crystallography", "1964"],
            "n": 0
        },
        {
            "id": "peoria",
            "tier": "power",
            "t": "In Peoria, Illinois, “Moldy Mary” found a high-yield mold strain on a cantaloupe, and corn steep liquor in deep tanks boosted production",
            "k": ["peoria", "cantaloupe", "moldy mary", "corn steep liquor"],
            "n": 0
        },
        {
            "id": "heatley",
            "tier": "power",
            "t": "Norman Heatley worked out how to extract it at Oxford, where the mold grew in containers that included bedpans",
            "k": ["heatley", "bedpans", "extract"],
            "n": 0
        },
        {
            "id": "mice-1940",
            "tier": "power",
            "t": "In 1940, Florey and Chain showed it could protect infected mice",
            "k": ["mice", "1940"],
            "n": 0
        },
        {
            "id": "mould-juice",
            "tier": "power",
            "t": "Fleming first called it “mould juice” and described it in a 1929 paper",
            "k": ["mould juice", "1929"],
            "n": 0
        },
        {
            "id": "lysozyme",
            "tier": "power",
            "t": "Years earlier, Fleming had discovered lysozyme, a germ-fighting enzyme in tears and mucus",
            "k": ["lysozyme", "tears"],
            "n": 0,
            "rabbit": "Enzymes"
        },
        {
            "id": "anne-miller",
            "tier": "power",
            "t": "In 1942, Anne Miller of New Haven, Connecticut, was one of the first U.S. patients treated successfully with it",
            "k": ["anne miller", "new haven", "1942"],
            "n": 0
        },
        {
            "id": "g-and-v",
            "tier": "power",
            "t": "The G form is usually given as a shot because stomach acid breaks it down; the V form can be swallowed",
            "k": ["stomach acid", "shot", "g form"],
            "n": 0
        },
        {
            "id": "nobel-lecture",
            "tier": "power",
            "t": "In his 1945 Nobel lecture, Fleming warned that using too little of it could let bacteria become resistant",
            "k": ["nobel lecture", "resistant"],
            "n": 0
        },
        {
            "id": "sheehan",
            "tier": "power",
            "t": "John Sheehan of MIT first made it from simple chemicals in 1957; its second ring has five members and contains sulfur",
            "k": ["sheehan", "1957", "sulfur"],
            "n": 0
        },
        {
            "id": "urine",
            "tier": "power",
            "t": "The kidneys clear it quickly, so early Oxford doctors recovered scarce doses from patients’ urine",
            "k": ["kidneys", "urine", "scarce"],
            "n": 0
        },
        {
            "id": "spore",
            "tier": "power",
            "t": "The mold spore behind the discovery may have drifted up from a mold lab on the floor below Fleming’s",
            "k": ["spore", "floor below"],
            "n": 0
        },
        {
            "id": "cephalosporins",
            "tier": "power",
            "t": "Cephalosporins share its beta-lactam ring, block cell walls the same way, and also come from a fungus",
            "k": ["cephalosporins"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Drug, mold, or scientist?",
        "body": "Penicillin tossups and Alexander Fleming tossups share many clues: the moldy dish, 1928, St. Mary’s Hospital, and the 1945 Nobel Prize. The mold itself belongs to the genus Penicillium, a different answer that a question may ask for as “this genus of fungi.” Relatives such as amoxicillin and methicillin have their own names, so naming one of them won’t count.",
        "fix": "Listen for the noun. “This drug,” “this antibiotic,” or “this compound” means penicillin; “this scientist” means Fleming (or Florey or Chain); “this genus” or “this fungus” means Penicillium. Saying only “antibiotics” earns a prompt, so be ready to name the drug.",
        "line": "Real answer line: <b><u>Penicillin</u></b> (accept penicillin G or penicillin V; prompt on <u>antibiotics</u>; do not accept “Penicillium”)"
    },
    "tests": {
        "right": [
            "Penicillin",
            "penicilin",
            "Penicillin G",
            "penicillins",
            "Benzylpenicillin"
        ],
        "prompt": [
            "Antibiotics",
            "beta-lactam antibiotic"
        ],
        "wrong": [
            "Penicillium",
            "Amoxicillin",
            "Methicillin",
            "Lysozyme",
            "Streptomycin",
            "Alexander Fleming"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
