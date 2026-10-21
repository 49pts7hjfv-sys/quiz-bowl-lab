import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "alveoli",
    "name": "Alveoli",
    "mono": "ALV",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Tiny air sacs of the lungs · Where oxygen enters the blood",
    "dates": "About 300 million in an adult’s lungs",
    "briefing": "Alveoli are tiny, balloon-like air sacs at the ends of your smallest airways, clustered like bunches of grapes. An adult’s lungs hold roughly 300 million of them, and each is wrapped in capillaries, so oxygen can slip into the blood while carbon dioxide slips out. A soapy coating called surfactant keeps them from collapsing, which is why babies born very early can have trouble breathing.",
    "answerHtml": "<b><u>Alveoli</u></b> (accept <u>alveolus</u> or <u>alveolar sacs</u>; prompt on <u>air sacs</u>; do not accept “bronchioles” or “lungs”)",
    "accept": [
        "alveoli",
        "alveolus",
        "alveolar sacs",
        "alveolar sac",
        "pulmonary alveoli",
        "pulmonary alveolus"
    ],
    "prompt": [
        "air sacs",
        "air sac",
        "sacs"
    ],
    "reject": [
        "lungs",
        "lung",
        "bronchioles",
        "bronchiole",
        "bronchi",
        "bronchus",
        "trachea",
        "alveolar ducts",
        "alveolar duct",
        "capillaries",
        "capillary",
        "diaphragm",
        "pleura",
        "larynx",
        "pharynx",
        "villi",
        "nephrons",
        "air capillaries",
        "parabronchi",
        "gills",
        "spiracles",
        "surfactant",
        "pneumocytes",
        "macrophages",
        "dust cells",
        "red blood cells"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Pulmonary_alveolus",
    "qb": {
        "q": "alveoli",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In 1959, Mary Ellen Avery and Jere Mead showed that premature babies with a serious breathing disorder lacked a substance that normally coats the inside of these structures. That soapy substance, surfactant, lowers surface tension so these structures do not collapse when a person breathes out.",
            "r": "For 10 points, name these tiny air sacs in the lungs where gas exchange takes place."
        },
        {
            "p": "In 1980, Tetsuro Fujiwara successfully treated premature babies by putting replacement surfactant into their lungs to keep these structures open. Babies born too early may not yet make enough surfactant, which can lead to respiratory distress syndrome, also called hyaline [“HY-uh-lin”] membrane disease.",
            "r": "For 10 points, name these tiny air sacs, wrapped in capillaries, where oxygen enters the blood."
        },
        {
            "p": "The law of Laplace [“luh-PLAHSS”] explains why, without surfactant, smaller examples of these structures would collapse and empty into larger ones. Small openings called the pores of Kohn connect neighboring examples of these structures, so air can pass between them.",
            "r": "Their walls are only one cell thick. For 10 points, name these tiny sacs at the ends of the bronchioles where gas exchange happens."
        },
        {
            "p": "Birds lack these structures; instead, air flows one way through tubes called parabronchi, which are lined with tiny air capillaries. In humans, the air left in the trachea and bronchi that never reaches these structures is called anatomical dead space.",
            "r": "These structures are grouped in clusters like bunches of grapes. For 10 points, name these tiny air sacs in the lungs."
        },
        {
            "p": "Macrophages nicknamed “dust cells” crawl along the inner surfaces of these structures, swallowing dust and germs that get past the mucus in the airways. Coal dust that builds up in these structures over many years can scar the lungs, causing black lung disease.",
            "r": "Networks of capillaries surround them. For 10 points, name these tiny air sacs where oxygen passes into the blood."
        },
        {
            "p": "An inherited shortage of the protein alpha-1 antitrypsin [“an-tee-TRIP-sin”] lets enzymes break down the walls of these structures, causing emphysema earlier in life than usual. More often, emphysema is caused by smoking, which destroys these structures and leaves fewer, larger spaces with less surface area.",
            "r": "For 10 points, name these air sacs of the lungs, which are wrapped in capillaries."
        },
        {
            "p": "Thin, flat type I cells cover most of the inner surface of these structures, while rounder type II cells secrete surfactant and can divide to replace damaged type I cells. Elastic fibers in their walls help these structures spring back as a person breathes out.",
            "r": "For 10 points, name these tiny sacs in the lungs, where oxygen and carbon dioxide are exchanged."
        },
        {
            "p": "Oxygen’s partial pressure is about 100 millimeters of mercury inside these structures but only about 40 in the blood arriving from the body, so oxygen diffuses into the blood. At high altitude, lower air pressure leaves less oxygen inside these structures, so less oxygen crosses into the blood.",
            "r": "Each one is wrapped in capillaries. For 10 points, name these tiny air sacs at the ends of the bronchioles."
        },
        {
            "p": "These structures take their name from a Latin word for a “small cavity,” which is also used for the sockets that hold teeth in the jawbone. The bony ridge behind the upper front teeth, used to make sounds like t and d, is named with the same Latin word.",
            "r": "Each one is wrapped in capillaries. For 10 points, name these tiny air sacs in the lungs, where gas exchange occurs."
        },
        {
            "p": "The barrier between the air inside these structures and the blood in the surrounding capillaries is only about half a micrometer thick. An adult’s lungs contain roughly 300 million of these structures, giving them a surface area for gas exchange dozens of times larger than the skin’s.",
            "r": "Oxygen diffuses from them into the blood. For 10 points, name these tiny air sacs at the ends of the smallest airways."
        },
        {
            "p": "In pulmonary fibrosis, scar tissue thickens the walls of these structures, making it harder for oxygen to pass through them. In pneumonia, an infection makes these structures fill with fluid, so less oxygen can reach the blood.",
            "r": "They sit at the ends of the bronchioles. For 10 points, name these tiny sacs in the lungs where oxygen enters the blood."
        },
        {
            "p": "In 1929, Kurt von Neergaard showed that lungs filled with liquid are easier to inflate than lungs filled with air, because surface tension inside these structures resists stretching. The phospholipid DPPC is the main ingredient of the substance that lowers that surface tension inside these structures.",
            "r": "That substance is surfactant. For 10 points, name these tiny air sacs at the ends of the bronchioles."
        },
        {
            "p": "A newborn baby has only a fraction of the adult number of these structures, which keep forming for years after birth. Before birth, these structures are filled with fluid instead of air, and a baby’s first breaths help clear that fluid.",
            "r": "Each is wrapped in capillaries. For 10 points, name these tiny air sacs where oxygen passes into the blood."
        },
        {
            "p": "After surgery, patients often use a device called an incentive spirometer to take slow, deep breaths that help keep these structures from collapsing, a problem called atelectasis [“at-uh-LEK-tuh-sis”]. Without enough surfactant, these structures also tend to collapse.",
            "r": "They are clustered at the ends of the bronchioles. For 10 points, name these tiny air sacs in the lungs, where gas exchange happens."
        },
        {
            "p": "Oxygen leaving these structures crosses a thin respiratory membrane made of their wall, a shared basement membrane, and the wall of a capillary. Asthma narrows the bronchioles that lead to these structures, but unlike emphysema, it does not destroy these structures themselves.",
            "r": "Red blood cells pick up the oxygen that leaves them. For 10 points, name these tiny air sacs in the lungs."
        }
    ],
    "clues": [
        {
            "id": "air-sacs",
            "tier": "giveaway",
            "t": "Tiny, balloon-like air sacs at the ends of the smallest airways in the lungs",
            "k": ["air sacs", "lungs"],
            "n": 0,
            "rabbit": "Lungs"
        },
        {
            "id": "gas-exchange",
            "tier": "giveaway",
            "t": "Where oxygen diffuses into the blood and carbon dioxide diffuses out",
            "k": ["oxygen", "carbon dioxide", "diffuses"],
            "n": 0,
            "rabbit": "Diffusion"
        },
        {
            "id": "capillary-net",
            "tier": "giveaway",
            "t": "Each one is wrapped in a net of capillaries",
            "k": ["capillaries", "net"],
            "n": 0,
            "rabbit": "Capillaries"
        },
        {
            "id": "airway-path",
            "tier": "giveaway",
            "t": "Air reaches them through the trachea, the bronchi, and then the tiny bronchioles",
            "k": ["bronchioles", "trachea", "bronchi"],
            "n": 0
        },
        {
            "id": "grapes",
            "tier": "giveaway",
            "t": "Grouped in clusters that look like bunches of grapes",
            "k": ["grapes", "clusters"],
            "n": 0
        },
        {
            "id": "300-million",
            "tier": "middle",
            "t": "An adult’s lungs hold roughly 300 million of them, giving a surface area dozens of times larger than the skin’s",
            "k": ["300 million", "surface area"],
            "n": 0
        },
        {
            "id": "surfactant",
            "tier": "middle",
            "t": "Surfactant, a soapy mixture made by type II cells, lowers surface tension so they don’t collapse",
            "k": ["surfactant", "surface tension", "type ii"],
            "n": 0
        },
        {
            "id": "type-cells",
            "tier": "middle",
            "t": "Thin, flat type I cells cover most of their inner surface; rounder type II cells make surfactant and can divide to replace them",
            "k": ["type i", "flat", "divide"],
            "n": 0
        },
        {
            "id": "dust-cells",
            "tier": "middle",
            "t": "Macrophages nicknamed “dust cells” crawl inside them, eating dust and germs",
            "k": ["dust cells", "macrophages"],
            "n": 0
        },
        {
            "id": "emphysema",
            "tier": "middle",
            "t": "Emphysema, usually caused by smoking, destroys their walls, leaving fewer, larger spaces with less surface area",
            "k": ["emphysema", "smoking"],
            "n": 0
        },
        {
            "id": "respiratory-distress",
            "tier": "middle",
            "t": "Premature babies without enough surfactant can develop respiratory distress syndrome (hyaline membrane disease)",
            "k": ["respiratory distress syndrome", "hyaline membrane", "premature"],
            "n": 0
        },
        {
            "id": "pneumonia-fibrosis",
            "tier": "middle",
            "t": "In pneumonia, an infection fills them with fluid; in pulmonary fibrosis, scar tissue thickens their walls",
            "k": ["pneumonia", "pulmonary fibrosis"],
            "n": 0
        },
        {
            "id": "elastic-fibers",
            "tier": "middle",
            "t": "Elastic fibers in their walls help them spring back as you breathe out",
            "k": ["elastic fibers"],
            "n": 0
        },
        {
            "id": "avery",
            "tier": "power",
            "t": "In 1959, Mary Ellen Avery and Jere Mead showed that premature babies with a serious breathing disorder lacked surfactant",
            "k": ["mary ellen avery", "1959"],
            "n": 0
        },
        {
            "id": "fujiwara",
            "tier": "power",
            "t": "Tetsuro Fujiwara first successfully treated premature babies with replacement surfactant in 1980",
            "k": ["fujiwara", "1980", "replacement surfactant"],
            "n": 0
        },
        {
            "id": "von-neergaard",
            "tier": "power",
            "t": "In 1929, Kurt von Neergaard showed that surface tension makes air-filled lungs harder to inflate than liquid-filled ones",
            "k": ["von neergaard", "1929"],
            "n": 0
        },
        {
            "id": "dppc",
            "tier": "power",
            "t": "The main ingredient of surfactant is the phospholipid DPPC",
            "k": ["dppc", "phospholipid"],
            "n": 0,
            "rabbit": "Lipids"
        },
        {
            "id": "laplace",
            "tier": "power",
            "t": "The law of Laplace explains why, without surfactant, small sacs would collapse and empty into bigger ones",
            "k": ["law of laplace"],
            "n": 0
        },
        {
            "id": "pores-of-kohn",
            "tier": "power",
            "t": "Small openings called the pores of Kohn let air pass between neighboring ones",
            "k": ["pores of kohn"],
            "n": 0
        },
        {
            "id": "birds",
            "tier": "power",
            "t": "Birds lack them; air flows one way through parabronchi lined with tiny air capillaries",
            "k": ["parabronchi", "air capillaries", "birds"],
            "n": 0,
            "rabbit": "Birds"
        },
        {
            "id": "dead-space",
            "tier": "power",
            "t": "Air in the airways that never reaches them is called anatomical dead space",
            "k": ["anatomical dead space", "dead space"],
            "n": 0
        },
        {
            "id": "partial-pressure",
            "tier": "power",
            "t": "Oxygen’s partial pressure is about 100 mmHg inside them but about 40 mmHg in blood returning from the body",
            "k": ["partial pressure", "100 mmhg"],
            "n": 0
        },
        {
            "id": "latin-name",
            "tier": "power",
            "t": "Their name is Latin for “small cavities,” the same word used for tooth sockets and the ridge behind the upper front teeth",
            "k": ["small cavities", "tooth sockets", "ridge"],
            "n": 0
        },
        {
            "id": "alpha-1",
            "tier": "power",
            "t": "An inherited lack of the protein alpha-1 antitrypsin lets enzymes destroy their walls, causing emphysema early in life",
            "k": ["alpha-1 antitrypsin"],
            "n": 0
        },
        {
            "id": "black-lung",
            "tier": "power",
            "t": "Coal dust that builds up in them over many years can scar the lungs, causing black lung disease",
            "k": ["black lung", "coal dust"],
            "n": 0
        },
        {
            "id": "atelectasis",
            "tier": "power",
            "t": "Their collapse is called atelectasis; after surgery, patients use incentive spirometers to take deep breaths that help prevent it",
            "k": ["atelectasis", "incentive spirometers"],
            "n": 0
        },
        {
            "id": "respiratory-membrane",
            "tier": "power",
            "t": "Oxygen crosses a respiratory membrane (their wall, a shared basement membrane, and a capillary wall) only about half a micrometer thick",
            "k": ["respiratory membrane", "half a micrometer"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Sacs, not tubes",
        "body": "Lung tossups move through a chain of answers: the trachea, bronchi, bronchioles, alveoli, and the capillaries around them, plus the lungs as a whole. Alveoli are the dead-end sacs where gas exchange happens; bronchioles are the tiny tubes that lead to them. Saying just “air sacs” earns a prompt, and birds have different “air sacs” that do not exchange gases at all.",
        "fix": "“Surfactant,” “type I and type II cells,” “dust cells,” “300 million,” and “emphysema destroys their walls” mean alveoli. Smooth muscle that tightens during an asthma attack means bronchioles, vessels one cell thick mean capillaries, and “these paired organs” means the lungs.",
        "line": "Real answer line: <b><u>Alveoli</u></b> (accept alveolus; prompt on <u>air sacs</u>; do not accept “bronchioles”)"
    },
    "tests": {
        "right": [
            "Alveoli",
            "alveolus",
            "Alveolar sacs",
            "Alvioli",
            "Pulmonary alveoli"
        ],
        "prompt": [
            "Air sacs"
        ],
        "wrong": [
            "Bronchioles",
            "Lungs",
            "Capillaries",
            "Bronchi",
            "Trachea",
            "Villi"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
