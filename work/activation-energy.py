import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "activation-energy",
    "name": "Activation energy",
    "mono": "EA",
    "category": "Chemistry",
    "qbCategory": "Science · Chemistry",
    "kicker": "The energy hill a reaction must climb · Why a match needs a strike",
    "dates": "Introduced by Svante Arrhenius, 1889",
    "briefing": "Wood and paper don’t burst into flames on their own, even though burning releases lots of energy. That’s because a reaction must first get over an energy “hill” called the activation energy. Striking a match supplies that push, and catalysts such as enzymes lower the hill so reactions run faster; Svante Arrhenius introduced the idea in 1889 to explain why heat speeds reactions up.",
    "answerHtml": "<b><u>Activation energy</u></b> (or <u>E<sub>a</sub></u>; accept <u>energy of activation</u>; prompt on <u>energy barrier</u>; do not accept “catalyst” or “transition state”)",
    "accept": [
        "activation energy",
        "activation energies",
        "energy of activation",
        "activation barrier",
        "ea",
        "e a",
        "e sub a"
    ],
    "prompt": [
        "energy barrier",
        "barrier",
        "threshold energy",
        "minimum energy",
        "activation",
        "energy"
    ],
    "reject": [
        "catalyst",
        "catalysts",
        "catalysis",
        "enzyme",
        "enzymes",
        "inhibitor",
        "inhibitors",
        "transition state",
        "transition states",
        "activated complex",
        "reaction rate",
        "reaction rates",
        "rate of reaction",
        "rate constant",
        "arrhenius equation",
        "arrhenius law",
        "frequency factor",
        "pre exponential factor",
        "collision theory",
        "enthalpy",
        "enthalpy change",
        "enthalpy of reaction",
        "heat of reaction",
        "delta h",
        "free energy",
        "gibbs free energy",
        "kinetic energy",
        "potential energy",
        "lattice energy",
        "ionization energy",
        "bond energy",
        "bond enthalpy",
        "bond dissociation energy",
        "internal energy",
        "entropy",
        "endothermic",
        "exothermic",
        "heat",
        "temperature"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Activation_energy",
    "qb": {
        "q": "activation energy",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "On an Arrhenius [“ar-RAY-nee-us”] plot, the natural logarithm of the rate constant is graphed against one over the absolute temperature, giving a straight line whose slope equals the negative of this quantity divided by the gas constant. Chemists use that plot to measure this quantity from experiments.",
            "r": "For 10 points, name this minimum amount of energy that reactants need in order to react, which catalysts lower."
        },
        {
            "p": "Henry Eyring’s [“EYE-ring”] transition state theory, published in 1935, relates a reaction’s speed to this quantity and to the short-lived, high-energy arrangement of atoms that forms partway through the reaction. That arrangement sits at the very top of the hump on a reaction’s energy diagram.",
            "r": "For 10 points, name this energy barrier that must be overcome for a reaction to occur, which catalysts lower."
        },
        {
            "p": "For a simple one-step reaction, this quantity for the reverse reaction equals this quantity for the forward reaction minus the enthalpy change. As a result, an exothermic reaction has a larger value of this quantity when it runs backward, because its products sit lower on the energy diagram.",
            "r": "This quantity is the height of the hump on that diagram. For 10 points, name this energy barrier that reactants must overcome."
        },
        {
            "p": "Diamond is actually less stable than graphite, but diamonds don’t turn into graphite at room temperature because this quantity for that change is enormous. Chemists call substances like diamond kinetically stable, because they react extremely slowly even when the reaction would release energy.",
            "r": "For 10 points, name this energy barrier that must be overcome before a reaction can start."
        },
        {
            "p": "On a Maxwell–Boltzmann graph of molecular energies, the area under the curve to the right of this quantity shows the fraction of molecules with enough energy to react. Raising the temperature stretches that curve toward higher energies, so a larger fraction of collisions can succeed.",
            "r": "For 10 points, name this minimum energy needed for a reaction to happen, which a catalyst lowers."
        },
        {
            "p": "The thermite reaction releases a huge amount of heat, but it needs so much of this quantity to get started that a burning strip of magnesium ribbon is often used to light it. Paper and wood can sit in air for years without catching fire for a similar reason.",
            "r": "Striking a match supplies this quantity. For 10 points, name this minimum energy needed to start a reaction."
        },
        {
            "p": "In the Arrhenius [“ar-RAY-nee-us”] equation, a reaction’s rate constant depends on the temperature, a frequency factor called A, and this quantity. Reactions with a larger value of this quantity run more slowly and speed up more sharply when heated.",
            "r": "For 10 points, name this energy barrier, the minimum energy needed for a reaction to occur."
        },
        {
            "p": "In a reaction with several steps, each step has its own value of this quantity, drawn as a separate hump on the energy diagram, and the step with the largest value is usually the slowest, rate-determining step. The valleys between those humps stand for reaction intermediates.",
            "r": "For 10 points, name this energy barrier that reactants must climb over, which catalysts and enzymes lower."
        },
        {
            "p": "A sugar cube sitting in air does not burn, even though its reaction with oxygen releases a lot of energy, because this quantity for that reaction is high. In cells, the same overall reaction happens at body temperature in many small steps, each with a much smaller value of this quantity.",
            "r": "Enzymes lower this quantity. For 10 points, name this energy barrier that must be overcome for a reaction to begin."
        },
        {
            "p": "A rule of thumb says that many reactions near room temperature roughly double in speed for every 10-degree Celsius rise, a result that follows from typical sizes of this quantity. Cooking food at a higher temperature speeds up its chemical reactions for the same reason.",
            "r": "For 10 points, name this minimum energy needed for a reaction to occur, which enzymes lower."
        },
        {
            "p": "In an endothermic reaction, this quantity must be at least as large as the reaction’s enthalpy change, because the products sit higher on the energy diagram than the reactants. On that diagram, this quantity is measured from the reactants up to the transition state.",
            "r": "Catalysts lower this quantity without changing the enthalpy change. For 10 points, name this energy barrier for a reaction."
        },
        {
            "p": "According to collision theory, colliding molecules react only if they are lined up in the right orientation and their collision energy exceeds this quantity. Crushing a solid into powder speeds up a reaction by causing more collisions, but it does not change this quantity.",
            "r": "For 10 points, name this minimum energy needed for a reaction, which catalysts lower by providing a different pathway."
        },
        {
            "p": "Svante Arrhenius [“ar-RAY-nee-us”], who won the 1903 Nobel Prize in Chemistry for explaining how salts break apart into ions, introduced this quantity in 1889 to explain why heating speeds up reactions. This quantity is usually measured in kilojoules per mole.",
            "r": "For 10 points, name this energy barrier, the minimum energy reactants need to react."
        },
        {
            "p": "A glow stick placed in a freezer glows more dimly but lasts much longer, because at low temperatures fewer molecules have enough energy to get over this barrier. For the same reason, milk spoils more slowly in a refrigerator.",
            "r": "A match needs a strike to supply this quantity. For 10 points, name this minimum energy that reactants need to get a reaction going."
        },
        {
            "p": "A mixture of hydrogen and chlorine gases can sit safely in the dark, but bright light can set it off, because light splits a few chlorine molecules and helps the reaction get over this barrier. Robert Bunsen and Henry Roscoe used that reaction to measure the brightness of light.",
            "r": "Catalysts such as enzymes lower this barrier. For 10 points, name this minimum energy needed to start a reaction."
        }
    ],
    "clues": [
        {
            "id": "definition",
            "tier": "giveaway",
            "t": "The minimum energy reactants need for a reaction to start",
            "k": ["minimum", "reactants", "start"],
            "n": 0
        },
        {
            "id": "catalysts-lower",
            "tier": "giveaway",
            "t": "Catalysts, including enzymes, speed up reactions by lowering it",
            "k": ["catalysts", "enzymes", "lowering"],
            "n": 0,
            "rabbit": "Catalysts"
        },
        {
            "id": "match",
            "tier": "giveaway",
            "t": "Striking a match supplies it, which is why matches don’t light by themselves in the box",
            "k": ["striking", "match", "box"],
            "n": 0
        },
        {
            "id": "barrier",
            "tier": "giveaway",
            "t": "Pictured as a hill or barrier that reactants must climb before they can become products",
            "k": ["hill", "barrier", "climb"],
            "n": 0
        },
        {
            "id": "hump",
            "tier": "middle",
            "t": "On an energy diagram, it is the height of the hump from the reactants up to the peak",
            "k": ["hump", "diagram", "peak"],
            "n": 0,
            "rabbit": "Potential energy"
        },
        {
            "id": "transition-state",
            "tier": "middle",
            "t": "The top of the hump is the transition state, also called the activated complex",
            "k": ["transition state", "activated complex", "top"],
            "n": 0
        },
        {
            "id": "arrhenius-1889",
            "tier": "middle",
            "t": "Svante Arrhenius introduced the idea in 1889 to explain why heating speeds up reactions",
            "k": ["arrhenius", "1889", "heating"],
            "n": 0
        },
        {
            "id": "arrhenius-equation",
            "tier": "middle",
            "t": "The Arrhenius equation links a rate constant to the temperature, a frequency factor A, and this quantity",
            "k": ["arrhenius equation", "rate constant", "frequency factor"],
            "n": 0,
            "rabbit": "Reaction rate"
        },
        {
            "id": "temperature",
            "tier": "middle",
            "t": "Heating speeds up reactions because more molecules have at least this much energy",
            "k": ["heating", "more molecules"],
            "n": 0
        },
        {
            "id": "collision-theory",
            "tier": "middle",
            "t": "Collision theory: molecules react only if they collide in the right orientation with enough energy; crushing a solid speeds collisions but doesn’t change it",
            "k": ["collision theory", "orientation", "collide"],
            "n": 0
        },
        {
            "id": "units",
            "tier": "middle",
            "t": "Usually measured in kilojoules per mole",
            "k": ["kilojoules per mole", "kilojoules"],
            "n": 0
        },
        {
            "id": "enthalpy",
            "tier": "middle",
            "t": "A catalyst lowers it but doesn’t change the reaction’s overall enthalpy change",
            "k": ["enthalpy", "overall"],
            "n": 0,
            "rabbit": "Enthalpy"
        },
        {
            "id": "maxwell-boltzmann",
            "tier": "middle",
            "t": "On a Maxwell–Boltzmann graph, the area to the right of it shows the fraction of molecules with enough energy to react",
            "k": ["maxwell–boltzmann", "fraction", "area"],
            "n": 0
        },
        {
            "id": "arrhenius-plot",
            "tier": "power",
            "t": "An Arrhenius plot of ln k against 1/T is a straight line whose slope is minus this quantity divided by the gas constant",
            "k": ["arrhenius plot", "slope", "gas constant"],
            "n": 0,
            "rabbit": "Gas constant"
        },
        {
            "id": "reverse",
            "tier": "power",
            "t": "For the reverse of a one-step reaction, it equals the forward value minus the enthalpy change, so exothermic reactions have a bigger value backward",
            "k": ["reverse", "exothermic", "backward"],
            "n": 0
        },
        {
            "id": "diamond",
            "tier": "power",
            "t": "Diamond is less stable than graphite but doesn’t turn into graphite, because this barrier is enormous (kinetic stability)",
            "k": ["diamond", "graphite", "kinetic stability"],
            "n": 0,
            "rabbit": "Diamond"
        },
        {
            "id": "eyring",
            "tier": "power",
            "t": "Henry Eyring’s transition state theory (1935) relates reaction speed to it and to the transition state",
            "k": ["eyring", "1935", "transition state theory"],
            "n": 0
        },
        {
            "id": "thermite",
            "tier": "power",
            "t": "Thermite needs so much of it that a burning magnesium ribbon is often used to start it",
            "k": ["thermite", "magnesium ribbon"],
            "n": 0
        },
        {
            "id": "ten-degrees",
            "tier": "power",
            "t": "Rule of thumb: many reactions roughly double in speed for every 10 °C rise, because of typical values of it",
            "k": ["rule of thumb", "double", "10 °c"],
            "n": 0
        },
        {
            "id": "multistep",
            "tier": "power",
            "t": "In a multistep reaction, the step with the biggest hump is usually the slowest, rate-determining step",
            "k": ["rate-determining", "slowest", "multistep"],
            "n": 0
        },
        {
            "id": "endothermic",
            "tier": "power",
            "t": "In an endothermic reaction, it must be at least as large as the enthalpy change",
            "k": ["endothermic", "at least"],
            "n": 0
        },
        {
            "id": "sugar",
            "tier": "power",
            "t": "A sugar cube doesn’t burn in air because this barrier is high; cells break sugar down in small, enzyme-assisted steps",
            "k": ["sugar cube", "enzyme-assisted", "cells"],
            "n": 0
        },
        {
            "id": "glow-stick",
            "tier": "power",
            "t": "A glow stick in a freezer lasts longer because fewer molecules can get over this barrier when cold",
            "k": ["glow stick", "freezer"],
            "n": 0
        },
        {
            "id": "hydrogen-chlorine",
            "tier": "power",
            "t": "Light helps a hydrogen–chlorine mixture get over this barrier and explode; Bunsen and Roscoe used that reaction to measure light",
            "k": ["hydrogen", "chlorine", "bunsen", "roscoe"],
            "n": 0,
            "rabbit": "Robert Bunsen"
        }
    ],
    "trap": {
        "title": "The barrier, not the helper",
        "body": "Catalysts and enzymes work by lowering activation energy, so clues about one sound like clues about the other. Players also mix it up with the transition state, which is the arrangement of atoms at the top of the hump, and with the enthalpy change, which is the overall energy difference between reactants and products.",
        "fix": "Listen for the question word. “This quantity,” “this energy,” or “this barrier,” measured in kilojoules per mole, means activation energy; “these substances” that are not used up means catalysts. The peak itself is the transition state, and reactants versus products is the enthalpy change.",
        "line": "Real answer line: <b><u>Activation energy</u></b> (or <u>E<sub>a</sub></u>; accept <u>energy of activation</u>; prompt on <u>energy barrier</u>; do not accept “catalyst” or “transition state”)"
    },
    "tests": {
        "right": [
            "Activation energy",
            "Ea",
            "Energy of activation",
            "Activaton energy",
            "the activation energy"
        ],
        "prompt": [
            "Energy barrier",
            "Energy"
        ],
        "wrong": [
            "Catalyst",
            "Transition state",
            "Activated complex",
            "Kinetic energy",
            "Reaction rate",
            "Enthalpy",
            "Potential energy",
            "Gibbs free energy"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
