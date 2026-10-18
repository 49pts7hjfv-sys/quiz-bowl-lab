import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "epinephrine-adrenaline",
    "name": "Epinephrine (adrenaline)",
    "mono": "EPI",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "The “fight-or-flight” hormone · Made by the adrenal glands above the kidneys",
    "dates": "Isolated by Jokichi Takamine in 1901",
    "briefing": "When something scares you, your adrenal glands, perched on top of your kidneys, flood your blood with epinephrine, better known as adrenaline. Within seconds your heart pounds, your airways and pupils widen, and your liver pours sugar into your blood, getting you ready for “fight or flight.” Doctors use the very same chemical in EpiPens to stop dangerous allergic reactions.",
    "answerHtml": "<b><u>Epinephrine</u></b> (accept <u>adrenaline</u> or <u>adrenalin</u>; prompt on <u>catecholamine</u>; do not accept “norepinephrine” or “noradrenaline”)",
    "accept": [
        "epinephrine",
        "epinephrin",
        "adrenaline",
        "adrenalin"
    ],
    "prompt": [
        "catecholamine",
        "catecholamines"
    ],
    "reject": [
        "norepinephrine",
        "nor epinephrine",
        "noradrenaline",
        "noradrenalin",
        "nor adrenaline",
        "adrenal",
        "adrenal gland",
        "adrenal glands",
        "adrenal medulla",
        "adrenal cortex",
        "cortisol",
        "dopamine",
        "acetylcholine",
        "ephedrine",
        "pseudoephedrine",
        "glucagon",
        "insulin",
        "serotonin",
        "histamine",
        "aldosterone",
        "thyroxine",
        "acth",
        "adrenocorticotropic hormone",
        "cyclic amp",
        "tyrosine",
        "l dopa",
        "levodopa"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Adrenaline",
    "qb": {
        "q": "epinephrine",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Earl Sutherland won a Nobel Prize after discovering the “second messenger” cyclic AMP while studying how this hormone makes liver cells break down glycogen. The receptors this hormone binds on cell surfaces are sorted into alpha and beta types.",
            "r": "This hormone makes the heart race during sudden danger. For 10 points, name this “fight-or-flight” hormone made by the adrenal glands."
        },
        {
            "p": "Japanese chemist Jokichi Takamine [“tah-kah-MEE-nay”], who later helped arrange Japan’s 1912 gift of cherry trees to Washington, D.C., isolated this compound in 1901. Its two common names come from Greek and Latin words meaning “on the kidney” and “near the kidneys.”",
            "r": "People with severe allergies carry EpiPens that inject it. For 10 points, name this “fight-or-flight” hormone."
        },
        {
            "p": "An enzyme abbreviated PNMT makes this compound by adding a methyl group to a closely related molecule, and cortisol from the gland’s outer layer boosts production of that enzyme. Like dopamine, this compound is a catecholamine.",
            "r": "The adrenal medulla releases it into the blood during stress. For 10 points, name this “fight-or-flight” hormone."
        },
        {
            "p": "Chromaffin cells store this compound in tiny granules and release it when sympathetic nerve fibers signal them with the neurotransmitter acetylcholine. Those cells sit in the inner part of a gland, while the gland’s outer layer makes cortisol instead.",
            "r": "That inner part is the adrenal medulla. For 10 points, name this “fight-or-flight” hormone made there."
        },
        {
            "p": "A rare tumor called pheochromocytoma [“fee-oh-kroh-moh-sye-TOH-muh”] can release too much of this compound, causing sudden bouts of headache, sweating, and a pounding heartbeat. Enzymes called MAO and COMT break this compound down after it is released.",
            "r": "It raises heart rate and blood sugar in emergencies. For 10 points, name this hormone made by the adrenal glands."
        },
        {
            "p": "Beta-blockers such as propranolol [“proh-PRAN-oh-lol”] slow the heart by blocking this compound’s effects. By acting on beta-2 receptors, this compound relaxes the smooth muscle wrapped around the airways, widening them so breathing is easier.",
            "r": "Auto-injectors called EpiPens deliver this drug during severe allergic reactions. For 10 points, name this hormone made by the adrenal glands."
        },
        {
            "p": "Dentists often mix this compound into numbing drugs like lidocaine, since it narrows nearby blood vessels and makes the numbness last longer. In an emergency, it narrows blood vessels in the skin and gut but widens those in skeletal muscle.",
            "r": "A sudden burst of it makes your heart pound. For 10 points, name this “fight-or-flight” hormone made by the adrenal glands."
        },
        {
            "p": "Physiologist Walter Cannon showed that fear and pain make the body release extra amounts of this substance into the blood. It raises blood sugar by making the liver break down glycogen, a process called glycogenolysis [“gly-koh-jeh-NOL-ih-sis”].",
            "r": "Cannon named the response it drives “fight or flight.” For 10 points, name this hormone made by the adrenal glands."
        },
        {
            "p": "Cells build this compound from the amino acid tyrosine in four steps, passing through L-DOPA and dopamine along the way. Its structure includes a catechol group, a benzene ring carrying two hydroxyl groups.",
            "r": "Its close relative norepinephrine differs from it by just one methyl group. For 10 points, name this “fight-or-flight” hormone."
        },
        {
            "p": "This hormone binds beta-1 receptors in the heart to make it beat faster and harder, and it binds alpha-1 receptors on blood vessels to narrow them and raise blood pressure. In the liver, it switches on the breakdown of glycogen.",
            "r": "For 10 points, name this hormone released by the adrenal glands during the “fight-or-flight” response."
        },
        {
            "p": "Emergency teams give repeated doses of this drug during CPR for cardiac arrest, to help get the heart beating again. Within the body, this compound widens the pupils and the airways when danger appears.",
            "r": "It is the drug inside EpiPens. For 10 points, name this hormone that the adrenal glands release in the “fight-or-flight” response."
        },
        {
            "p": "American pharmacologist John Jacob Abel gave this hormone its Greek-based name, which means “on the kidney.” Its Latin-based name means nearly the same thing and is the one more often used in Britain.",
            "r": "People describe feeling a “rush” of it when they are scared. For 10 points, name this “fight-or-flight” hormone."
        },
        {
            "p": "The cells that make this compound develop from the neural crest, the same embryo tissue that forms many nerve cells, so the tissue holding them works like a modified sympathetic ganglion.",
            "r": "That tissue, the adrenal medulla, releases this hormone during stress. For 10 points, name this “fight-or-flight” hormone that EpiPens inject."
        },
        {
            "p": "Doctors inject this drug into the muscle of the outer thigh as the first treatment for anaphylaxis [“an-uh-fuh-LAK-sis”], a severe allergic reaction that can swell the throat and drop blood pressure. It works with the sympathetic nervous system.",
            "r": "For 10 points, name this hormone, made by the adrenal glands, that triggers the “fight-or-flight” response."
        },
        {
            "p": "This hormone widens the pupils by tightening the spoke-like dilator muscle of each iris, and it slows down digestion. It also makes fat cells break down stored fat for fuel.",
            "r": "Its release makes the heart race. For 10 points, name this “fight-or-flight” hormone made by the adrenal glands, the drug in EpiPens."
        }
    ],
    "clues": [
        {
            "id": "fight-or-flight",
            "tier": "giveaway",
            "t": "The main hormone of the “fight-or-flight” response to danger or stress",
            "k": ["fight-or-flight", "fight or flight", "stress"],
            "n": 0
        },
        {
            "id": "adrenal-glands",
            "tier": "giveaway",
            "t": "Made mainly by the adrenal glands, which sit on top of the kidneys",
            "k": ["adrenal glands", "kidneys"],
            "n": 0,
            "rabbit": "Adrenal glands"
        },
        {
            "id": "epipen",
            "tier": "giveaway",
            "t": "The drug in EpiPens, auto-injectors that treat anaphylaxis, a severe allergic reaction",
            "k": ["epipens", "epipen", "anaphylaxis", "allergic reaction"],
            "n": 0
        },
        {
            "id": "rush",
            "tier": "giveaway",
            "t": "A sudden “rush” of it makes the heart pound, the airways open, and the pupils widen",
            "k": ["rush", "heart pound", "pupils"],
            "n": 0
        },
        {
            "id": "adrenal-medulla",
            "tier": "middle",
            "t": "Released by the adrenal medulla, the inner part of each adrenal gland; the outer cortex makes cortisol instead",
            "k": ["adrenal medulla", "medulla", "cortisol"],
            "n": 0
        },
        {
            "id": "sympathetic",
            "tier": "middle",
            "t": "Works hand in hand with the sympathetic nervous system, which revs the body up for action",
            "k": ["sympathetic nervous system", "sympathetic"],
            "n": 0
        },
        {
            "id": "catecholamine",
            "tier": "middle",
            "t": "A catecholamine, like dopamine and norepinephrine; built from the amino acid tyrosine by way of L-DOPA and dopamine",
            "k": ["catecholamine", "tyrosine", "l-dopa"],
            "n": 0
        },
        {
            "id": "methyl-relative",
            "tier": "middle",
            "t": "Its close relative norepinephrine (noradrenaline) differs from it by just one methyl group",
            "k": ["methyl group", "methyl"],
            "n": 0,
            "rabbit": "Norepinephrine"
        },
        {
            "id": "blood-sugar",
            "tier": "middle",
            "t": "Raises blood sugar by making the liver break down glycogen (glycogenolysis); also makes fat cells release fat",
            "k": ["glycogenolysis", "glycogen", "blood sugar"],
            "n": 0
        },
        {
            "id": "names",
            "tier": "middle",
            "t": "Its two names mean “on the kidney” (Greek) and “near the kidneys” (Latin); the Latin one is more common in Britain",
            "k": ["on the kidney", "greek", "latin", "britain"],
            "n": 0
        },
        {
            "id": "cardiac-arrest",
            "tier": "middle",
            "t": "Given in repeated doses during CPR for cardiac arrest",
            "k": ["cardiac arrest", "cpr"],
            "n": 0
        },
        {
            "id": "airways-beta-blockers",
            "tier": "middle",
            "t": "Widens the airways through beta-2 receptors; beta-blockers such as propranolol block its effects on the heart",
            "k": ["beta-blockers", "propranolol", "airways"],
            "n": 0
        },
        {
            "id": "sutherland",
            "tier": "power",
            "t": "Earl Sutherland won a Nobel Prize (1971) after finding the “second messenger” cyclic AMP while studying how it breaks down liver glycogen",
            "k": ["sutherland", "second messenger", "cyclic amp"],
            "n": 0
        },
        {
            "id": "takamine",
            "tier": "power",
            "t": "Japanese chemist Jokichi Takamine isolated it in 1901; he also helped arrange Japan’s 1912 gift of cherry trees to Washington, D.C.",
            "k": ["takamine", "1901", "cherry trees"],
            "n": 0
        },
        {
            "id": "abel",
            "tier": "power",
            "t": "American pharmacologist John Jacob Abel gave it its Greek-based name",
            "k": ["john jacob abel", "abel"],
            "n": 0
        },
        {
            "id": "pnmt",
            "tier": "power",
            "t": "The enzyme PNMT makes it by adding a methyl group to norepinephrine; cortisol boosts that enzyme",
            "k": ["pnmt", "enzyme"],
            "n": 0
        },
        {
            "id": "chromaffin",
            "tier": "power",
            "t": "Chromaffin cells store it in granules and release it when sympathetic nerves signal them with acetylcholine",
            "k": ["chromaffin", "acetylcholine", "granules"],
            "n": 0
        },
        {
            "id": "neural-crest",
            "tier": "power",
            "t": "Its source cells come from the neural crest, so the adrenal medulla works like a modified sympathetic ganglion",
            "k": ["neural crest", "ganglion"],
            "n": 0
        },
        {
            "id": "pheochromocytoma",
            "tier": "power",
            "t": "A rare tumor called pheochromocytoma can release too much of it, causing headaches, sweating, and a pounding heartbeat",
            "k": ["pheochromocytoma", "tumor"],
            "n": 0
        },
        {
            "id": "mao-comt",
            "tier": "power",
            "t": "Broken down after release by the enzymes MAO and COMT; its catechol group is a benzene ring with two hydroxyl groups",
            "k": ["comt", "catechol", "hydroxyl"],
            "n": 0
        },
        {
            "id": "lidocaine",
            "tier": "power",
            "t": "Mixed into numbing drugs like lidocaine to narrow nearby blood vessels so the numbness lasts longer",
            "k": ["lidocaine", "numbing"],
            "n": 0
        },
        {
            "id": "cannon",
            "tier": "power",
            "t": "Physiologist Walter Cannon showed that fear and pain increase its release, and named the “fight or flight” response",
            "k": ["walter cannon", "cannon"],
            "n": 0
        },
        {
            "id": "vessels",
            "tier": "power",
            "t": "Narrows blood vessels in the skin and gut but widens those in skeletal muscle",
            "k": ["skeletal muscle", "skin"],
            "n": 0
        },
        {
            "id": "receptors",
            "tier": "power",
            "t": "Binds alpha and beta receptors: beta-1 makes the heart beat faster and harder, alpha-1 narrows blood vessels",
            "k": ["beta-1", "alpha-1", "receptors"],
            "n": 0
        },
        {
            "id": "anaphylaxis-thigh",
            "tier": "power",
            "t": "For anaphylaxis, it is injected into the muscle of the outer thigh as the first treatment",
            "k": ["outer thigh", "thigh"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Epinephrine or norepinephrine?",
        "body": "Norepinephrine (also called noradrenaline) is this hormone’s near-twin: both are catecholamines, both come from the adrenal medulla, and both power the “fight-or-flight” response. Answering the wrong twin loses the tossup. Players also blurt “adrenal glands,” which names the organ rather than the chemical, or “cortisol,” the stress hormone from the gland’s outer layer.",
        "fix": "Norepinephrine is mainly the messenger released by sympathetic nerve endings and by brain cells in the locus coeruleus, so listen for those. EpiPens, anaphylaxis, PNMT, and Takamine mean epinephrine (or adrenaline). If the question asks for “this gland,” say adrenal glands.",
        "line": "Real answer line: <b><u>Epinephrine</u></b> (accept <u>adrenaline</u>; do not accept “norepinephrine” or “noradrenaline”)"
    },
    "tests": {
        "right": [
            "Epinephrine",
            "Adrenaline",
            "adrenalin",
            "Epinefrine",
            "Epinephrine (adrenaline)"
        ],
        "prompt": [
            "Catecholamine"
        ],
        "wrong": [
            "Norepinephrine",
            "Noradrenaline",
            "Adrenal glands",
            "Cortisol",
            "Ephedrine",
            "Dopamine"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
