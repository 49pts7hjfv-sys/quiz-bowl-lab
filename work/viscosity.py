import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "viscosity",
    "name": "Viscosity",
    "mono": "VIS",
    "category": "Physics",
    "qbCategory": "Science · Physics",
    "kicker": "A fluid’s resistance to flow · Why honey pours slower than water",
    "dates": "Newton’s law for it published in 1687",
    "briefing": "Viscosity is a fluid’s resistance to flowing: it is why honey oozes slowly off a spoon while water splashes right out of a glass. Most liquids get runnier as they warm up, which is why syrup pours faster after a turn in the microwave. Some strange fluids, like a cornstarch-and-water mix called oobleck, suddenly act thicker when you punch or squeeze them.",
    "answerHtml": "<b><u>Viscosity</u></b> (accept <u>dynamic</u> or <u>kinematic viscosity</u>; prompt on <u>thickness</u> or <u>internal friction</u>)",
    "accept": [
        "viscosity",
        "viscosities",
        "dynamic viscosity",
        "kinematic viscosity",
        "absolute viscosity",
        "shear viscosity"
    ],
    "prompt": [
        "thickness",
        "internal friction",
        "fluid friction",
        "resistance to flow"
    ],
    "reject": [
        "surface tension",
        "friction",
        "drag",
        "drag force",
        "density",
        "fluidity",
        "pressure",
        "buoyancy",
        "elasticity",
        "turbulence",
        "reynolds number",
        "viscoelasticity"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Viscosity",
    "qb": {
        "q": "viscosity",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "A funnel of tar pitch set up at the University of Queensland in 1927 had let only nine drops fall by 2014, because pitch has an enormous value of this property. Thomas Parnell started that experiment to show that a substance that shatters under a hammer can still slowly flow.",
            "r": "Honey has a higher value of this property than water. For 10 points, name this property, a fluid’s resistance to flow."
        },
        {
            "p": "James Clerk Maxwell surprised scientists by predicting that this property of a gas does not depend on the gas’s pressure, and he confirmed it using disks that twisted back and forth in gas. Unlike liquids, gases have more of this property when they get hotter.",
            "r": "For 10 points, name this property that measures how strongly a fluid resists flowing, which is high for honey and molasses."
        },
        {
            "p": "In 1937, Pyotr Kapitsa [“KAH-pee-tsuh”], and separately John Allen and Don Misener, found that liquid helium cooled below about 2 kelvins flows through tiny gaps with none of this property. Such a superfluid can even creep up and over the walls of its container.",
            "r": "For 10 points, name this property that describes how “thick” a fluid is, which makes honey flow slowly."
        },
        {
            "p": "Proving that the Navier–Stokes [“nahv-YAY STOHKS”] equations, which describe fluids that have this property, always have smooth solutions is one of the Clay Institute’s million-dollar Millennium Prize Problems. This property is the reason a stirred cup of tea eventually stops swirling.",
            "r": "For 10 points, name this property, a fluid’s internal resistance to flow, which is much higher for honey than for water."
        },
        {
            "p": "Jean Poiseuille [“pwah-ZOY”], a French doctor who studied blood flow, found that the flow through a narrow tube depends on the tube’s radius to the fourth power divided by this property. A unit of this property, the poise, is named after him.",
            "r": "For 10 points, name this property of fluids that is much higher for molasses than for water."
        },
        {
            "p": "Robert Millikan used Stokes’ law, which says the drag on a small falling sphere equals six pi times this property times the sphere’s radius and speed, to find the sizes of his oil drops. Students can measure this property by timing steel balls as they sink through tubes of oil.",
            "r": "For 10 points, name this property, measured in pascal-seconds, that describes how strongly a fluid resists flowing."
        },
        {
            "p": "The Reynolds number compares a fluid’s inertia to this property, and a low Reynolds number means smooth, layered flow instead of turbulence. Osborne Reynolds studied the switch between those kinds of flow by injecting a thin stream of dye into water flowing through a glass pipe.",
            "r": "For 10 points, name this property, a fluid’s resistance to flow, which is higher for syrup than for water."
        },
        {
            "p": "The Society of Automotive Engineers grades motor oils for this property using labels like 10W-30, where the W stands for “winter” and the first number describes how the oil behaves when cold.",
            "r": "Warming most liquids lowers this property. For 10 points, name this property, which is why honey pours more slowly than water."
        },
        {
            "p": "A mix of cornstarch and water called oobleck, named after the Dr. Seuss book _Bartholomew and the Oobleck_, suddenly gets more of this property when you punch or squeeze it. Ketchup does the opposite, losing some of this property when it is shaken, which is why it can suddenly rush out of the bottle.",
            "r": "For 10 points, name this property that stays constant for Newtonian fluids such as water, a measure of resistance to flow."
        },
        {
            "p": "Lava rich in silica has a high value of this property, so it traps gas and tends to erupt explosively, while runny basalt lava flows in rivers on Hawaii. In Earth’s mantle, solid rock with an enormous value of this property slowly flows over millions of years.",
            "r": "Molasses and honey have high values of this property. For 10 points, name this property, a fluid’s resistance to flow."
        },
        {
            "p": "A popular myth wrongly claims that old church windows are thicker at the bottom because glass slowly flows downward; in fact, glass at room temperature has far too high a value of this property to flow noticeably.",
            "r": "This property usually drops as a liquid is heated. For 10 points, name this property that makes honey and syrup pour slowly."
        },
        {
            "p": "Dividing this property by a fluid’s density gives a related quantity measured in units called stokes. Water at room temperature has about one centipoise of this property, which equals one-thousandth of a pascal-second.",
            "r": "Honey has thousands of times more of it than water does. For 10 points, name this property, a fluid’s resistance to flow."
        },
        {
            "p": "When a giant storage tank burst in Boston’s North End in January 1919, cold winter air raised this property of the spilled molasses, making rescue and cleanup much harder. Most liquids flow more easily as they warm up because heat lowers this property.",
            "r": "For 10 points, name this property that describes how thick and slow-flowing a fluid is."
        },
        {
            "p": "Ludwig Prandtl [“PRAHN-tul”] showed in 1904 that the effects of this property are concentrated in a thin “boundary layer” of fluid right next to a surface, such as an airplane wing, where the fluid touching the wing does not move relative to it.",
            "r": "Isaac Newton described fluids for which this property stays the same no matter how fast they are stirred. For 10 points, name this property, a fluid’s resistance to flow."
        },
        {
            "p": "The reciprocal of this property is called fluidity. Glycerin, a thick, sweet liquid whose molecules cling to each other through many hydrogen bonds, has a value of this property more than a thousand times that of water.",
            "r": "Motor oil is rated by it. For 10 points, name this property, which makes honey flow more slowly than water."
        }
    ],
    "clues": [
        {
            "id": "definition",
            "tier": "giveaway",
            "t": "A fluid’s resistance to flow, or how “thick” it is",
            "k": ["resistance to flow", "thick"],
            "n": 0
        },
        {
            "id": "honey",
            "tier": "giveaway",
            "t": "High for honey, syrup, and molasses; low for water",
            "k": ["honey", "molasses", "syrup"],
            "n": 0
        },
        {
            "id": "warming",
            "tier": "giveaway",
            "t": "Most liquids have less of it when heated, so warm syrup pours faster",
            "k": ["heated", "warm syrup"],
            "n": 0
        },
        {
            "id": "motor-oil",
            "tier": "giveaway",
            "t": "Motor oil is graded for it with labels like 10W-30 (the W means winter)",
            "k": ["motor oil", "10w-30", "winter"],
            "n": 0
        },
        {
            "id": "units",
            "tier": "middle",
            "t": "SI unit: the pascal-second; the older poise is named for Jean Poiseuille",
            "k": ["pascal-second", "poise", "poiseuille"],
            "n": 0
        },
        {
            "id": "stokes-law",
            "tier": "middle",
            "t": "Stokes’ law: the drag on a small sphere equals 6π times this property times the radius times the speed",
            "k": ["stokes", "sphere", "drag"],
            "n": 0,
            "rabbit": "Drag (physics)"
        },
        {
            "id": "falling-ball",
            "tier": "middle",
            "t": "Measured by timing a steel ball sinking through a tube of liquid",
            "k": ["sinking", "steel ball", "tube"],
            "n": 0
        },
        {
            "id": "reynolds",
            "tier": "middle",
            "t": "The Reynolds number compares inertia to it; low values mean smooth, layered (laminar) flow instead of turbulence",
            "k": ["reynolds number", "laminar", "turbulence"],
            "n": 0
        },
        {
            "id": "non-newtonian",
            "tier": "middle",
            "t": "Oobleck (cornstarch and water) gains it when squeezed; ketchup loses it when shaken",
            "k": ["oobleck", "ketchup", "cornstarch"],
            "n": 0
        },
        {
            "id": "newtonian",
            "tier": "middle",
            "t": "Newtonian fluids like water keep the same value no matter how fast they are stirred",
            "k": ["newtonian", "stirred"],
            "n": 0
        },
        {
            "id": "lava",
            "tier": "middle",
            "t": "High-silica lava has a lot of it and tends to erupt explosively; basalt lava is runny",
            "k": ["silica", "lava", "basalt"],
            "n": 0,
            "rabbit": "Magma"
        },
        {
            "id": "tea",
            "tier": "middle",
            "t": "It makes a stirred cup of tea eventually stop swirling",
            "k": ["tea", "swirling"],
            "n": 0
        },
        {
            "id": "pitch-drop",
            "tier": "power",
            "t": "Pitch drop experiment at the University of Queensland (begun 1927 by Thomas Parnell): only nine drops fell by 2014",
            "k": ["pitch drop", "queensland", "parnell"],
            "n": 0
        },
        {
            "id": "maxwell",
            "tier": "power",
            "t": "James Clerk Maxwell predicted a gas’s value does not depend on its pressure; gases gain it when heated",
            "k": ["maxwell", "pressure"],
            "n": 0
        },
        {
            "id": "superfluid",
            "tier": "power",
            "t": "Superfluid helium (found by Pyotr Kapitsa and by Allen and Misener, 1937) has none at all",
            "k": ["superfluid", "kapitsa", "helium"],
            "n": 0
        },
        {
            "id": "navier-stokes",
            "tier": "power",
            "t": "Navier–Stokes equations: proving they always have smooth solutions is a million-dollar Millennium Prize Problem",
            "k": ["navier", "millennium prize"],
            "n": 0
        },
        {
            "id": "poiseuille-law",
            "tier": "power",
            "t": "Poiseuille’s law: flow through a narrow tube depends on the radius to the fourth power divided by it",
            "k": ["fourth power", "narrow tube"],
            "n": 0
        },
        {
            "id": "millikan",
            "tier": "power",
            "t": "Robert Millikan used Stokes’ law to find the sizes of his oil drops",
            "k": ["millikan", "oil drops"],
            "n": 0,
            "rabbit": "Millikan oil drop experiment"
        },
        {
            "id": "kinematic",
            "tier": "power",
            "t": "Dividing it by a fluid’s density gives a related quantity measured in stokes",
            "k": ["dividing", "density"],
            "n": 0,
            "rabbit": "Density"
        },
        {
            "id": "water-value",
            "tier": "power",
            "t": "Water at room temperature: about 1 centipoise, or one-thousandth of a pascal-second",
            "k": ["centipoise", "one-thousandth"],
            "n": 0
        },
        {
            "id": "glass-myth",
            "tier": "power",
            "t": "Myth: old church windows are thicker at the bottom because glass flows; really, glass has far too much of it",
            "k": ["church windows", "glass", "myth"],
            "n": 0
        },
        {
            "id": "molasses-flood",
            "tier": "power",
            "t": "Boston’s Great Molasses Flood (January 1919): cold air made the spilled molasses thicker, slowing rescue and cleanup",
            "k": ["molasses flood", "boston", "1919"],
            "n": 0
        },
        {
            "id": "prandtl",
            "tier": "power",
            "t": "Ludwig Prandtl (1904): its effects are concentrated in a thin boundary layer next to a surface",
            "k": ["prandtl", "boundary layer", "1904"],
            "n": 0
        },
        {
            "id": "fluidity",
            "tier": "power",
            "t": "Its reciprocal is called fluidity",
            "k": ["reciprocal", "fluidity"],
            "n": 0
        },
        {
            "id": "glycerin",
            "tier": "power",
            "t": "Glycerin’s many hydrogen bonds give it more than a thousand times as much as water",
            "k": ["glycerin", "hydrogen bonds"],
            "n": 0,
            "rabbit": "Hydrogen bonds"
        },
        {
            "id": "mantle",
            "tier": "power",
            "t": "Earth’s solid mantle flows slowly over millions of years because it has an enormous value",
            "k": ["mantle", "millions of years"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Thick is not heavy",
        "body": "Viscosity is about how slowly a fluid flows, not how heavy it is. Cooking oil is more viscous than water but less dense, so it floats on top of water. Surface tension, the “skin” on a liquid that lets water striders walk on it, is a different property too.",
        "fix": "Honey, syrup, motor oil, Stokes’ law, poise, and the pitch drop mean viscosity. Floating, sinking, and mass per volume mean density; water striders, beading droplets, and capillary action mean surface tension.",
        "line": "Real answer line: <b><u>Viscosity</u></b> (accept <u>dynamic</u> or <u>kinematic viscosity</u>; prompt on <u>thickness</u> or <u>internal friction</u>)"
    },
    "tests": {
        "right": [
            "Viscosity",
            "viscosity",
            "Viscocity",
            "Dynamic viscosity",
            "Kinematic viscosity"
        ],
        "prompt": [
            "Thickness",
            "Internal friction"
        ],
        "wrong": [
            "Surface tension",
            "Density",
            "Friction",
            "Drag",
            "Fluidity",
            "Velocity"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
