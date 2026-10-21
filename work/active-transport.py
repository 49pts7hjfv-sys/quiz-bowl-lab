import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "active-transport",
    "name": "Active transport",
    "mono": "ATR",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Moving substances against a concentration gradient · Powered by ATP",
    "dates": "Sodium-potassium pump discovered 1957",
    "briefing": "Active transport is how a cell moves substances “uphill,” from where they are scarce to where they are already crowded. Because that goes against the natural spread of diffusion, it costs energy, usually ATP, and it is done by protein pumps in the cell membrane. A famous example is the sodium-potassium pump, which pushes three sodium ions out of a cell and brings two potassium ions in for each ATP it uses.",
    "answerHtml": "<b><u>Active transport</u></b> (accept <u>primary</u> or <u>secondary active transport</u>; prompt on <u>cotransport</u> or <u>pumping</u>; do not accept “passive transport,” “diffusion,” or “osmosis”)",
    "accept": [
        "active transport",
        "primary active transport",
        "secondary active transport",
        "active membrane transport",
        "active transportation",
        "active transport process"
    ],
    "prompt": [
        "cotransport",
        "co transport",
        "secondary transport",
        "symport",
        "antiport",
        "sodium potassium pump",
        "sodium potassium pumps",
        "proton pump",
        "ion pump",
        "ion pumps",
        "pump",
        "pumps",
        "pumping",
        "membrane transport",
        "transport",
        "carrier mediated transport"
    ],
    "reject": [
        "passive transport",
        "passive diffusion",
        "diffusion",
        "simple diffusion",
        "facilitated diffusion",
        "osmosis",
        "endocytosis",
        "exocytosis",
        "phagocytosis",
        "pinocytosis",
        "bulk transport",
        "vesicular transport",
        "filtration",
        "dialysis",
        "chemiosmosis",
        "electron transport chain",
        "electron transport",
        "axonal transport",
        "brownian motion"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Active_transport",
    "qb": {
        "q": "active transport",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Jens Christian Skou discovered an enzyme in crab nerve cells in 1957 that carries out this process, and he shared the 1997 Nobel Prize in Chemistry for that discovery. Heart drugs such as digoxin, which comes from foxglove plants, block that enzyme, and so does the poison ouabain [“WAH-bayn”].",
            "r": "That enzyme, the sodium-potassium pump, moves three sodium ions out and two potassium ions in. For 10 points, name this process that moves substances against their concentration gradient using energy."
        },
        {
            "p": "Salt-loving archaea use a light-powered protein called bacteriorhodopsin [“bak-teer-ee-oh-roh-DOP-sin”] to carry out this process, pushing hydrogen ions out of the cell. In mitochondria, protein complexes use energy taken from electrons to perform this process on hydrogen ions, building up a gradient.",
            "r": "For 10 points, name this process that uses energy to move substances from low to high concentration, unlike diffusion."
        },
        {
            "p": "Oral rehydration solution, a mix of salt and sugar in clean water, has saved many lives during cholera outbreaks because intestinal cells pull in sodium and glucose together, and water follows. That pairing relies on a sodium-glucose symporter called SGLT1, which uses the secondary form of this process.",
            "r": "Pumps powered by ATP also carry it out. For 10 points, name this process that uses energy to move substances against their concentration gradient."
        },
        {
            "p": "V-type pumps perform this process on hydrogen ions to keep lysosomes and plant vacuoles acidic. Cells in the stomach lining also perform it, pumping hydrogen ions into the stomach in exchange for potassium ions to make stomach acid, and drugs called proton pump inhibitors block those pumps.",
            "r": "The sodium-potassium pump is a famous example. For 10 points, name this energy-using process that moves substances against their concentration gradient."
        },
        {
            "p": "Thyroid cells use a sodium-iodide symporter to perform the secondary form of this process, gathering iodide until it is far more concentrated inside them than in the blood. That symporter is powered by a sodium gradient that another protein builds using ATP.",
            "r": "For 10 points, name this process in which cells use energy to move substances against their concentration gradient."
        },
        {
            "p": "Companion cells in a plant’s phloem use proton pumps to build up a gradient of hydrogen ions, which then helps them pull in sucrose by the secondary form of this process. Root hair cells, which are packed with mitochondria, use this process to absorb mineral ions like nitrate from the soil.",
            "r": "For 10 points, name this process in which cells spend energy, usually from ATP, to move substances against their concentration gradient."
        },
        {
            "p": "In the antiport kind of this process, two substances cross a membrane in opposite directions, as when heart muscle cells push calcium out while letting sodium in through a sodium-calcium exchanger. In the symport kind, two substances cross in the same direction.",
            "r": "Both kinds are forms of cotransport. For 10 points, name this process that moves molecules against their concentration gradient using energy."
        },
        {
            "p": "Calcium pumps that perform this process in muscle cells are P-type pumps, which change shape after ATP attaches a phosphate group to them. After a muscle contracts, those pumps pull calcium back into the sarcoplasmic reticulum [“sar-koh-PLAZ-mik reh-TIK-yoo-lum”] so the muscle can relax.",
            "r": "For 10 points, name this process, also carried out by the sodium-potassium pump, that uses energy to move substances against a concentration gradient."
        },
        {
            "p": "The main pump that carries out this process in animal cells is called electrogenic, because each cycle moves one more positive charge out of the cell than in. That pump helps keep the inside of a resting neuron at about −70 millivolts compared with the outside.",
            "r": "For 10 points, name this process, performed by the sodium-potassium pump, that moves substances against their concentration gradient."
        },
        {
            "p": "_E. coli_ bacteria bring lactose inside with lactose permease, which carries each sugar molecule in along with a hydrogen ion in a form of this process. That permease is made from a gene in the lac operon.",
            "r": "For 10 points, name this process that uses energy to move substances against their concentration gradient, unlike diffusion."
        },
        {
            "p": "Some cancer cells resist chemotherapy by making P-glycoprotein, a pump powered by ATP that performs this process to push drugs back out of the cell. P-glycoprotein belongs to a large family of pumps named for the ATP-binding cassette, or ABC, part of their structure.",
            "r": "For 10 points, name this process that uses energy to move substances across a membrane against their concentration gradient."
        },
        {
            "p": "Diabetes drugs called SGLT2 inhibitors block a kidney protein that performs this process, letting extra sugar leave the body in urine. Normally, cells lining the kidney’s proximal tubules use this process to reclaim nearly all of the glucose from the filtered fluid.",
            "r": "Protein pumps carry it out. For 10 points, name this process that moves substances from lower to higher concentration using energy."
        },
        {
            "p": "Thermodynamically, this process is endergonic, or “uphill,” so cells must couple it to an energy-releasing reaction such as the breakdown of ATP. Facilitated diffusion uses similar carrier proteins, but it can only move substances down their concentration gradients, without spending energy.",
            "r": "For 10 points, name this process, carried out by pumps, that moves substances against their concentration gradient."
        },
        {
            "p": "Saltwater fish use special “chloride cells” in their gills to pump extra salt out of their bodies, while freshwater fish use similar cells to pull in salt from the dilute water around them. Both jobs rely on this process.",
            "r": "For 10 points, name this process that moves ions against their concentration gradient using energy, usually from ATP."
        },
        {
            "p": "In the primary form of this process, a pump uses ATP directly, while in the secondary form, a substance flowing down its gradient, usually sodium or hydrogen ions, provides the energy to move another substance up its gradient.",
            "r": "Root hair cells use it to take up minerals. For 10 points, name this process that moves molecules against their concentration gradient, unlike diffusion and osmosis."
        }
    ],
    "clues": [
        {
            "id": "against-gradient",
            "tier": "giveaway",
            "t": "Moves molecules or ions across a membrane from low to high concentration, against their concentration gradient",
            "k": ["concentration gradient", "low to high"],
            "n": 0
        },
        {
            "id": "needs-energy",
            "tier": "giveaway",
            "t": "Requires energy, usually from ATP, unlike diffusion and osmosis",
            "k": ["energy", "atp", "diffusion"],
            "n": 0,
            "rabbit": "ATP"
        },
        {
            "id": "pumps",
            "tier": "giveaway",
            "t": "Carried out by membrane proteins called pumps",
            "k": ["pumps", "membrane proteins"],
            "n": 0,
            "rabbit": "Cell membrane"
        },
        {
            "id": "sodium-potassium-pump",
            "tier": "giveaway",
            "t": "The sodium-potassium pump moves 3 sodium ions out and 2 potassium ions in for each ATP it uses",
            "k": ["sodium-potassium pump", "sodium", "potassium"],
            "n": 0,
            "rabbit": "Potassium"
        },
        {
            "id": "root-hairs",
            "tier": "giveaway",
            "t": "Root hair cells use it to take in mineral ions, like nitrate, from soil that has fewer of them",
            "k": ["root hair", "mineral ions", "nitrate"],
            "n": 0,
            "rabbit": "Roots"
        },
        {
            "id": "primary-secondary",
            "tier": "middle",
            "t": "Primary forms use ATP directly; secondary forms (cotransport) use the energy of an ion gradient built by a primary pump",
            "k": ["primary", "secondary", "cotransport"],
            "n": 0
        },
        {
            "id": "symport-antiport",
            "tier": "middle",
            "t": "In symport, two substances cross in the same direction; in antiport, they cross in opposite directions",
            "k": ["symport", "antiport"],
            "n": 0
        },
        {
            "id": "sglt",
            "tier": "middle",
            "t": "Intestine and kidney cells pull in glucose together with sodium using sodium-glucose symporters (SGLTs)",
            "k": ["sodium-glucose", "sglts"],
            "n": 0
        },
        {
            "id": "stomach-acid",
            "tier": "middle",
            "t": "Stomach lining cells pump hydrogen ions into the stomach to make acid; drugs called proton pump inhibitors block them",
            "k": ["proton pump inhibitors", "hydrogen ions"],
            "n": 0,
            "rabbit": "Stomach"
        },
        {
            "id": "resting-potential",
            "tier": "middle",
            "t": "The sodium-potassium pump helps keep a resting neuron’s inside at about −70 millivolts",
            "k": ["70 millivolts", "resting"],
            "n": 0,
            "rabbit": "Neurons"
        },
        {
            "id": "calcium-pumps",
            "tier": "middle",
            "t": "Calcium pumps in the sarcoplasmic reticulum pull calcium back inside so muscles can relax",
            "k": ["calcium pumps", "sarcoplasmic reticulum"],
            "n": 0
        },
        {
            "id": "facilitated-diffusion",
            "tier": "middle",
            "t": "Unlike facilitated diffusion, which also uses carrier proteins, it can move substances “uphill”",
            "k": ["facilitated diffusion", "uphill"],
            "n": 0,
            "rabbit": "Diffusion"
        },
        {
            "id": "phloem-loading",
            "tier": "middle",
            "t": "Plants load sucrose into the phloem using hydrogen-ion gradients made by proton pumps",
            "k": ["sucrose", "phloem", "proton pumps"],
            "n": 0,
            "rabbit": "Phloem"
        },
        {
            "id": "endergonic",
            "tier": "middle",
            "t": "It is endergonic (“uphill”), so cells must couple it to an energy-releasing reaction such as ATP breakdown",
            "k": ["endergonic", "couple"],
            "n": 0
        },
        {
            "id": "skou",
            "tier": "power",
            "t": "Jens Christian Skou discovered the sodium-potassium pump in crab nerves in 1957 and shared the 1997 Nobel Prize in Chemistry",
            "k": ["skou", "crab nerves", "1997"],
            "n": 0
        },
        {
            "id": "digoxin-ouabain",
            "tier": "power",
            "t": "Digoxin, a heart drug from foxglove, and the poison ouabain both block the sodium-potassium pump",
            "k": ["digoxin", "foxglove", "ouabain"],
            "n": 0
        },
        {
            "id": "bacteriorhodopsin",
            "tier": "power",
            "t": "Salt-loving archaea use bacteriorhodopsin, a light-powered pump, to push hydrogen ions out of the cell",
            "k": ["bacteriorhodopsin", "archaea", "light-powered"],
            "n": 0
        },
        {
            "id": "mitochondrial-complexes",
            "tier": "power",
            "t": "In mitochondria, protein complexes use energy from electrons to pump hydrogen ions, building a gradient",
            "k": ["protein complexes", "electrons"],
            "n": 0,
            "rabbit": "Mitochondria"
        },
        {
            "id": "oral-rehydration",
            "tier": "power",
            "t": "Oral rehydration solution (salt and sugar in water) helps cholera patients because sodium and glucose are pulled in together and water follows",
            "k": ["oral rehydration", "cholera"],
            "n": 0,
            "rabbit": "Cholera"
        },
        {
            "id": "iodide-symporter",
            "tier": "power",
            "t": "Thyroid cells gather iodide using a sodium-iodide symporter",
            "k": ["sodium-iodide symporter", "thyroid", "iodide"],
            "n": 0,
            "rabbit": "Thyroid gland"
        },
        {
            "id": "v-type",
            "tier": "power",
            "t": "V-type pumps keep lysosomes and plant vacuoles acidic by pumping in hydrogen ions",
            "k": ["v-type", "lysosomes", "vacuoles"],
            "n": 0,
            "rabbit": "Lysosomes"
        },
        {
            "id": "sodium-calcium-exchanger",
            "tier": "power",
            "t": "Heart muscle cells use a sodium-calcium exchanger, an antiport, to push calcium out while sodium flows in",
            "k": ["sodium-calcium exchanger"],
            "n": 0
        },
        {
            "id": "p-type",
            "tier": "power",
            "t": "The sodium-potassium and calcium pumps are P-type pumps: ATP attaches a phosphate to the pump, changing its shape",
            "k": ["p-type", "phosphate"],
            "n": 0
        },
        {
            "id": "electrogenic",
            "tier": "power",
            "t": "The sodium-potassium pump is electrogenic, moving one more positive charge out than in during each cycle",
            "k": ["electrogenic", "positive charge"],
            "n": 0
        },
        {
            "id": "lactose-permease",
            "tier": "power",
            "t": "_E. coli_’s lactose permease, made from a lac operon gene, brings in lactose along with a hydrogen ion",
            "k": ["lactose permease", "lac operon"],
            "n": 0,
            "rabbit": "Lac operon"
        },
        {
            "id": "p-glycoprotein",
            "tier": "power",
            "t": "Some cancer cells resist chemotherapy with P-glycoprotein, an ATP-binding cassette (ABC) pump that pushes drugs out",
            "k": ["p-glycoprotein", "chemotherapy"],
            "n": 0
        },
        {
            "id": "sglt2",
            "tier": "power",
            "t": "Diabetes drugs called SGLT2 inhibitors block glucose reabsorption in the kidneys, so extra sugar leaves in urine",
            "k": ["sglt2 inhibitors", "kidneys"],
            "n": 0,
            "rabbit": "Diabetes"
        },
        {
            "id": "chloride-cells",
            "tier": "power",
            "t": "Saltwater fish pump extra salt out through “chloride cells” in their gills; freshwater fish use them to pull salt in",
            "k": ["chloride cells", "gills"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Active or passive?",
        "body": "Diffusion, facilitated diffusion, and osmosis are passive: substances move down their concentration gradient, and the cell spends no energy. Active transport is the opposite, using energy, usually ATP, to push substances up their gradient. Facilitated diffusion is the sneaky one, because it also uses membrane proteins, but it never moves anything against the gradient.",
        "fix": "“Against the gradient,” “uphill,” “pump,” “ATP,” “sodium-potassium pump,” or “cotransport” means active transport. “Down the gradient,” “no energy,” or “channel proteins” means diffusion or facilitated diffusion, and water crossing a membrane means osmosis. Endocytosis and exocytosis, which wrap material in vesicles, are separate answers.",
        "line": "Real answer line: <b><u>Active transport</u></b> (accept primary or secondary active transport; prompt on <u>cotransport</u>; do not accept “passive transport” or “diffusion”)"
    },
    "tests": {
        "right": [
            "Active transport",
            "Primary active transport",
            "secondary active transport",
            "Active transprt",
            "active transportation"
        ],
        "prompt": [
            "Cotransport",
            "Sodium-potassium pump"
        ],
        "wrong": [
            "Passive transport",
            "Diffusion",
            "Facilitated diffusion",
            "Osmosis",
            "Endocytosis",
            "Exocytosis"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
