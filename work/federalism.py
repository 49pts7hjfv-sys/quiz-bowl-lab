import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "federalism",
    "name": "Federalism",
    "mono": "FDL",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Sharing power between the nation and the states · Built into the Constitution",
    "dates": "Built into the Constitution, 1787",
    "briefing": "Who makes the rules where you live: your state or the national government? Under federalism, the answer is both. The Constitution gives some powers, like coining money and declaring war, to the national government and leaves many others, like running schools, mostly to the states, and the Tenth Amendment reserves to the states or the people the powers not given to the nation. When state and national laws clash, the Supremacy Clause says national law wins.",
    "answerHtml": "<b><u>federalism</u></b> (accept <u>federal system</u>; accept dual, cooperative, or New <u>federalism</u>; prompt on <u>division of powers</u>; do not accept “Federalist Party,” “Federalist Papers,” “checks and balances,” or “separation of powers”)",
    "accept": [
        "federalism",
        "federal system",
        "federal system of government",
        "american federalism",
        "federalism in the united states",
        "dual federalism",
        "cooperative federalism",
        "new federalism",
        "fiscal federalism"
    ],
    "prompt": [
        "division of powers",
        "division of power",
        "dual sovereignty",
        "federation",
        "shared powers",
        "shared power",
        "power sharing"
    ],
    "reject": [
        "federalist",
        "federalists",
        "federalist party",
        "federalist papers",
        "the federalist papers",
        "anti federalist",
        "anti federalists",
        "antifederalist",
        "antifederalists",
        "anti federalism",
        "antifederalism",
        "federalist society",
        "checks and balances",
        "separation of powers",
        "separation of power",
        "confederation",
        "confederacy",
        "confederalism",
        "articles of confederation",
        "unitary system",
        "unitary government",
        "unitary state",
        "states rights",
        "nullification",
        "popular sovereignty",
        "republicanism",
        "feudalism",
        "federal government",
        "tenth amendment",
        "10th amendment",
        "supremacy clause",
        "commerce clause",
        "necessary and proper clause",
        "elastic clause",
        "mcculloch v maryland",
        "federal reserve",
        "federal reserve system",
        "federal bureau of investigation",
        "nationalism",
        "democracy",
        "divided government",
        "limited government",
        "bill of rights"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Federalism_in_the_United_States",
    "qb": {
        "q": "federalism",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Dissenting in _New State Ice Co. v. Liebmann_ in 1932, Louis Brandeis wrote that “a single courageous State may, if its citizens choose, serve as a laboratory” and try “novel social and economic experiments without risk to the rest of the country.”",
            "r": "That idea is summed up as “laboratories of democracy.” For 10 points, name this system of sharing power between the national government and the states."
        },
        {
            "p": "James Madison wrote that in “the compound republic of America,” power is first divided between “two distinct governments” and then split among separate branches, so that “a double security arises to the rights of the people.”",
            "r": "Those two levels are the national and state governments. For 10 points, name this principle of dividing power between them."
        },
        {
            "p": "In _Federalist_ No. 45, James Madison promised that the powers given to the new national government would be “few and defined,” while those left to the states would be “numerous and indefinite.”",
            "r": "For 10 points, name this system, protected by the Tenth Amendment, that divides power between the nation and the states."
        },
        {
            "p": "Political scientist Morton Grodzins compared one form of this principle to a marble cake, in which national, state, and local governments mix their work together, unlike an older “layer cake” model in which each level kept to its own jobs.",
            "r": "For 10 points, name this system that divides power between the national government and the states."
        },
        {
            "p": "Richard Nixon’s revenue-sharing program and Ronald Reagan’s block grants were part of a “new” version of this principle, which aimed to shift money and decision-making from Washington to state and local governments.",
            "r": "For 10 points, name this system of dividing power between the national government and the states, protected by the Tenth Amendment."
        },
        {
            "p": "In an 1819 case about a tax on the Second Bank of the United States, John Marshall ruled that the national government is supreme within its own sphere and that “the power to tax involves the power to destroy,” so a state could not tax the bank.",
            "r": "That case, _McCulloch v. Maryland_, helped define this division of power. For 10 points, name this principle of sharing power between the nation and the states."
        },
        {
            "p": "In _New York v. United States_ (1992), Sandra Day O’Connor wrote for the Supreme Court that Congress could not force states to take ownership of radioactive waste, because the national government may not simply order state governments to carry out its programs.",
            "r": "That ruling relied on the Tenth Amendment. For 10 points, name this system that divides power between the national government and the states."
        },
        {
            "p": "In _United States v. Lopez_ (1995), the Supreme Court ruled for the first time in nearly sixty years that Congress had gone beyond its power to regulate commerce among the states, striking down a law that banned guns near schools.",
            "r": "Rulings like that one shape this system. For 10 points, name this division of power between the national and state governments."
        },
        {
            "p": "Under the doctrine of preemption, a valid act of Congress overrides a conflicting state law, and judges in every state must follow it. That rule comes from a clause in Article VI of the Constitution.",
            "r": "That Supremacy Clause makes national law “the supreme Law of the Land.” For 10 points, name this system of sharing power between the nation and the states."
        },
        {
            "p": "Under the Articles of Confederation, the states kept most power, and the national Congress could not collect taxes or regulate trade. At the Constitutional Convention of 1787, the framers created a stronger national government while keeping the states, a balance at the heart of this principle.",
            "r": "For 10 points, name this system that divides power between the national government and the states."
        },
        {
            "p": "Powers held by both levels of government in this system, such as taxing and borrowing money, are called concurrent powers. Powers given only to the national government, such as coining money and declaring war, are called delegated or enumerated powers.",
            "r": "Powers kept by the states are called reserved powers. For 10 points, name this system of dividing power between the nation and the states."
        },
        {
            "p": "John C. Calhoun argued that a state could nullify a national law it judged unconstitutional, and in 1832 South Carolina declared the tariffs of 1828 and 1832 void. Andrew Jackson answered with the Force Bill, and a compromise tariff ended the crisis in 1833.",
            "r": "For 10 points, name this system of sharing power between the nation and the states, which that Nullification Crisis tested."
        },
        {
            "p": "Thomas Jefferson and James Madison secretly wrote the Kentucky and Virginia Resolutions of 1798, arguing that states could judge whether national laws such as the Alien and Sedition Acts went beyond the powers the Constitution granted.",
            "r": "Those resolutions argued for the states’ side of this system. For 10 points, name this division of power between the national government and the states."
        },
        {
            "p": "In _South Dakota v. Dole_ (1987), the Supreme Court let Congress withhold some highway money from states that kept their drinking age below 21. Such conditions on grants of money are one way the national government shapes state policy in this system.",
            "r": "For 10 points, name this system that divides power between the national and state governments."
        },
        {
            "p": "In _Hammer v. Dagenhart_ (1918), the Supreme Court struck down a national law against child labor, ruling that factory work was for the states, not Congress, to regulate. That decision reflected a strict “layer cake” view of this system that lasted until the New Deal.",
            "r": "For 10 points, name this system of dividing power between the national government and the states."
        }
    ],
    "clues": [
        {
            "id": "definition",
            "tier": "giveaway",
            "t": "The division of power between the national government and the state governments",
            "k": ["national government", "state governments", "division"],
            "n": 0
        },
        {
            "id": "tenth-amendment",
            "tier": "giveaway",
            "t": "The Tenth Amendment reserves powers not given to the national government to the states or the people",
            "k": ["tenth amendment", "reserves"],
            "n": 0,
            "rabbit": "Bill of Rights"
        },
        {
            "id": "supremacy",
            "tier": "giveaway",
            "t": "Article VI’s Supremacy Clause: national law wins when it conflicts with state law",
            "k": ["supremacy clause", "article vi"],
            "n": 0
        },
        {
            "id": "articles",
            "tier": "middle",
            "t": "Replaced the weak national government of the Articles of Confederation with a new balance in the 1787 Constitution",
            "k": ["articles of confederation", "1787"],
            "n": 0,
            "rabbit": "Articles of Confederation"
        },
        {
            "id": "powers-types",
            "tier": "middle",
            "t": "Delegated (enumerated) powers belong to the nation, reserved powers to the states, and concurrent powers, like taxing, to both",
            "k": ["delegated", "reserved", "concurrent", "enumerated"],
            "n": 0
        },
        {
            "id": "laboratories",
            "tier": "middle",
            "t": "Louis Brandeis (1932): a state may “serve as a laboratory” for new ideas, the source of the phrase “laboratories of democracy”",
            "k": ["brandeis", "laboratory", "laboratories of democracy"],
            "n": 0
        },
        {
            "id": "cakes",
            "tier": "middle",
            "t": "“Layer cake” (dual) model vs. “marble cake” (cooperative) model, a comparison made by Morton Grodzins",
            "k": ["layer cake", "marble cake", "grodzins"],
            "n": 0
        },
        {
            "id": "mcculloch",
            "tier": "middle",
            "t": "_McCulloch v. Maryland_ (1819): a state cannot tax the national bank; “the power to tax involves the power to destroy”",
            "k": ["mcculloch", "maryland", "power to tax"],
            "n": 0,
            "rabbit": "McCulloch v. Maryland"
        },
        {
            "id": "federalist-45",
            "tier": "middle",
            "t": "_Federalist_ No. 45 (Madison): national powers are “few and defined,” state powers “numerous and indefinite”",
            "k": ["few and defined", "numerous and indefinite", "no. 45"],
            "n": 0,
            "rabbit": "The Federalist Papers"
        },
        {
            "id": "nullification",
            "tier": "middle",
            "t": "John C. Calhoun’s idea of nullification and South Carolina’s Nullification Crisis (1832–1833) tested it",
            "k": ["nullification", "calhoun", "south carolina"],
            "n": 0
        },
        {
            "id": "new-version",
            "tier": "middle",
            "t": "Nixon’s revenue sharing and Reagan’s block grants tried to shift money and power back to the states",
            "k": ["revenue sharing", "block grants", "reagan"],
            "n": 0
        },
        {
            "id": "unitary-contrast",
            "tier": "middle",
            "t": "Differs from a unitary system, where the central government holds most power, and a confederation, where the states do",
            "k": ["unitary", "confederation", "central government"],
            "n": 0
        },
        {
            "id": "federalist-51",
            "tier": "power",
            "t": "_Federalist_ No. 51: the “compound republic” divides power between “two distinct governments,” a “double security” for rights",
            "k": ["compound republic", "double security", "two distinct governments"],
            "n": 0
        },
        {
            "id": "new-state-ice",
            "tier": "power",
            "t": "Brandeis’s line came from his dissent in _New State Ice Co. v. Liebmann_ (1932)",
            "k": ["new state ice", "liebmann", "dissent"],
            "n": 0
        },
        {
            "id": "ny-v-us",
            "tier": "power",
            "t": "_New York v. United States_ (1992): Congress may not force states to take ownership of radioactive waste",
            "k": ["radioactive waste", "1992", "ownership"],
            "n": 0
        },
        {
            "id": "lopez",
            "tier": "power",
            "t": "_United States v. Lopez_ (1995): the first limit on Congress’s commerce power in nearly 60 years",
            "k": ["lopez", "commerce", "1995"],
            "n": 0
        },
        {
            "id": "dole",
            "tier": "power",
            "t": "_South Dakota v. Dole_ (1987): Congress may withhold highway money from states with a drinking age under 21",
            "k": ["south dakota", "highway money", "drinking age"],
            "n": 0
        },
        {
            "id": "hammer",
            "tier": "power",
            "t": "_Hammer v. Dagenhart_ (1918): struck down a national child-labor law as a matter for the states",
            "k": ["hammer", "dagenhart", "child-labor", "1918"],
            "n": 0
        },
        {
            "id": "ky-va",
            "tier": "power",
            "t": "The Kentucky and Virginia Resolutions (1798), by Jefferson and Madison, said states could judge national laws",
            "k": ["kentucky", "virginia resolutions", "1798"],
            "n": 0
        },
        {
            "id": "force-bill",
            "tier": "power",
            "t": "Andrew Jackson’s Force Bill and the Compromise Tariff of 1833 ended the Nullification Crisis",
            "k": ["force bill", "compromise tariff", "1833"],
            "n": 0
        },
        {
            "id": "grants-in-aid",
            "tier": "power",
            "t": "Grants-in-aid: national money given to states, often with conditions (“strings attached”)",
            "k": ["grants-in-aid", "strings attached", "conditions"],
            "n": 0
        },
        {
            "id": "commandeering",
            "tier": "power",
            "t": "The “anti-commandeering” rule: the national government cannot force state officials to carry out its programs",
            "k": ["anti-commandeering", "commandeering", "state officials"],
            "n": 0
        },
        {
            "id": "preemption",
            "tier": "power",
            "t": "Preemption: a valid act of Congress overrides a conflicting state law",
            "k": ["preemption", "overrides"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Not the Federalists",
        "body": "Several answer lines sound like this one. The Federalist Party was the party of Alexander Hamilton and John Adams in the 1790s, and _The Federalist Papers_ were 85 essays defending the Constitution, so saying either one for this principle is wrong. It is also easy to confuse with the separation of powers and checks and balances, which divide power among the three branches, not between levels of government.",
        "fix": "If the clue is about the nation versus the states (the Tenth Amendment, the Supremacy Clause, _McCulloch v. Maryland_, layer and marble cakes, or “laboratories of democracy”), say “federalism.” If it is about the president, Congress, and the courts limiting one another, think checks and balances or the separation of powers.",
        "line": "Real answer line: <b><u>federalism</u></b> (accept <u>federal system</u>; do not accept “Federalist Party,” “checks and balances,” or “separation of powers”)"
    },
    "tests": {
        "right": [
            "federalism",
            "Federalism",
            "federal system",
            "cooperative federalism",
            "fedralism"
        ],
        "prompt": [
            "division of powers",
            "federation"
        ],
        "wrong": [
            "Federalist Party",
            "The Federalist Papers",
            "checks and balances",
            "separation of powers",
            "Federalist",
            "confederation",
            "states' rights",
            "Tenth Amendment"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
