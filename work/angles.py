import json

data = {
    "id": "angles",
    "name": "Angles",
    "mono": "ANG",
    "category": "Math",
    "qbCategory": "Science · Other Science (Math)",
    "kicker": "Two rays meeting at a vertex · Measured in degrees or radians",
    "dates": "Defined in Euclid’s _Elements_, c. 300 BCE",
    "briefing": "An angle forms wherever two rays meet at a point called the vertex, like the hands of a clock or the tip of a pizza slice. Angles are measured in degrees, with 360 in a full turn, a custom usually traced to the ancient Babylonians, or in radians, with 2π in a full turn. A right angle is exactly 90°, acute angles are smaller, obtuse angles fall between 90° and 180°, and the three angles inside any flat triangle add up to 180°.",
    "answerHtml": "<b><u>angle</u></b>s (accept specific kinds, such as <u>right angle</u>s; prompt on <u>corner</u>s; do not accept units such as “degrees” or “radians”)",
    "accept": [
        "angles",
        "angle",
        "plane angle",
        "plane angles",
        "angle measure",
        "angle measures"
    ],
    "prompt": [
        "corner",
        "corners"
    ],
    "reject": [
        "degrees",
        "degree",
        "radians",
        "radian",
        "gradians",
        "gradian",
        "steradians",
        "steradian",
        "arcminutes",
        "arcminute",
        "arcseconds",
        "arcsecond",
        "minutes of arc",
        "vertex",
        "vertices",
        "ray",
        "rays",
        "line segment",
        "line segments",
        "triangle",
        "triangles",
        "triangle sum theorem",
        "circle",
        "circles",
        "polygon",
        "polygons",
        "protractor",
        "protractors",
        "compass",
        "sextant",
        "theodolite",
        "trigonometry",
        "trigonometric functions",
        "angle bisector",
        "angle bisectors",
        "angle trisection",
        "angle side angle",
        "side angle side",
        "angular momentum",
        "angular velocity",
        "anglo saxons",
        "angles and saxons"
    ],
    "tests": {
        "right": [
            "Angles",
            "angle",
            "right angles",
            "Angls",
            "acute angle"
        ],
        "prompt": [
            "corners"
        ],
        "wrong": [
            "degrees",
            "radians",
            "vertex",
            "Triangles",
            "angle bisector",
            "protractor",
            "angels"
        ]
    },
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Angle",
    "qb": {
        "q": "angle",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In 1837, Pierre Wantzel proved that, in general, these figures cannot be split into three equal parts using only a compass and straightedge, even though splitting one in half is easy. Archimedes [“ar-kih-MEE-deez”] got around that rule by sliding a ruler marked with two points.",
            "r": "A protractor measures these figures in degrees. For 10 points, name these figures formed by two rays that share an endpoint called the vertex."
        },
        {
            "p": "Roger Cotes worked out the idea behind one unit for measuring these in the early 1700s, and James Thomson, the brother of Lord Kelvin, first printed that unit’s name in 1873. One of those units cuts off an arc exactly as long as a circle’s radius.",
            "r": "There are 360 degrees in a full turn. For 10 points, name these figures, such as right and acute ones, which can be measured in radians."
        },
        {
            "p": "A way of measuring these that splits each unit into 60 minutes, and each minute into 60 seconds, traces back to Babylonian astronomers, who counted in base 60. Latitude and longitude are often written in those units.",
            "r": "The Babylonians are usually credited with splitting a full turn into 360 of those units. For 10 points, name these figures, which can be acute, right, or obtuse."
        },
        {
            "p": "Many calculators offer a GRAD mode, which uses a unit introduced in France that splits a full turn into 400 parts. Surveyors measure these figures both side to side and up and down with a telescope-like instrument on a tripod called a theodolite [“thee-AH-duh-lyte”].",
            "r": "Right ones measure 90 degrees. For 10 points, name these figures, which can be measured in degrees using a protractor."
        },
        {
            "p": "Euclid’s _Elements_ defines a plane one of these as the inclination of two lines that meet each other but do not lie in a straight line. Two planes that meet along a line form a dihedral one of these figures.",
            "r": "Euclid’s fourth postulate says that all right ones are equal. For 10 points, name these figures, which are measured with a protractor."
        },
        {
            "p": "Each time a side is added to a polygon, the total of these figures inside it grows by half a turn. For any convex polygon, the exterior ones, taken one at each corner, always add up to exactly one full turn.",
            "r": "Each one inside a regular hexagon measures 120 degrees. For 10 points, name these figures, three of which add up to 180 degrees inside any triangle."
        },
        {
            "p": "When a transversal crosses two parallel lines, it creates pairs of these figures called corresponding and alternate interior, and each such pair is equal. The triangle congruence shortcuts ASA and SAS are named partly for these figures.",
            "r": "Same-side interior pairs add up to 180 degrees. For 10 points, name these figures, which are classified as acute, right, or obtuse."
        },
        {
            "p": "An inscribed one of these figures measures exactly half of the central one that cuts off the same arc of a circle. The early Greek thinker Thales [“THAY-leez”] is traditionally credited with proving that when two lines cross, the pairs of these across from each other are equal.",
            "r": "Those pairs are called vertical. For 10 points, name these figures, which are measured in degrees with a protractor."
        },
        {
            "p": "These figures are called reflex when they are bigger than a half turn but smaller than a full turn. Two of them are complementary if together they make a quarter turn and supplementary if together they make a half turn.",
            "r": "A straight one measures exactly 180 degrees. For 10 points, name these figures, which are called acute when they are smaller than 90 degrees."
        },
        {
            "p": "On the surface of a sphere, a triangle with one corner at the North Pole and two on the equator can have three of these that are each a quarter turn. On a flat surface, an exterior one of a triangle equals the sum of the two interior ones that are not next to it.",
            "r": "The three inside a flat triangle add up to 180 degrees. For 10 points, name these figures, which are measured with a protractor."
        },
        {
            "p": "The law of reflection says that the one of these at which light strikes a mirror equals the one at which it bounces off, with both measured from a line called the normal. Snell’s law relates two of these when light bends as it passes from air into water.",
            "r": "A protractor measures them. For 10 points, name these figures, such as right ones, which are measured in degrees."
        },
        {
            "p": "Sailors used a sextant to measure one of these between the horizon and the Sun or a star, which helped them work out their latitude. Surveyors also speak of the “elevation” and “depression” types of these figures, measured up or down from the horizontal.",
            "r": "A carpenter’s square checks for right ones. For 10 points, name these figures, which are formed by two rays that share an endpoint."
        },
        {
            "p": "The name of these figures comes from a Latin word meaning “corner.” In the coordinate plane, one of these is in standard position when its vertex sits at the origin and its starting side lies along the positive x-axis, and turning counterclockwise from there gives a positive measure.",
            "r": "Acute ones are smaller than 90 degrees. For 10 points, name these figures, which can be measured in degrees or radians."
        },
        {
            "p": "A three-dimensional version of these figures, measured in steradians, describes how large an object looks from a single point, and a whole sphere around that point measures 4 pi steradians. In two dimensions, the official SI unit for these figures is named for a circle’s radius.",
            "r": "For 10 points, name these figures, such as acute and obtuse ones, which are usually measured in degrees."
        },
        {
            "p": "The names of two kinds of these figures come from Latin words meaning “sharp” and “blunt.” Leaves and seeds on many plants, such as sunflowers, spiral outward separated by a “golden” one of these figures, which is linked to the golden ratio.",
            "r": "An obtuse triangle has one that measures more than 90 degrees. For 10 points, name these figures, which you can measure with a protractor."
        }
    ],
    "clues": [
        {
            "id": "definition",
            "tier": "giveaway",
            "t": "Formed by two rays that share an endpoint, called the vertex",
            "k": [
                "two rays",
                "vertex",
                "endpoint"
            ],
            "n": 0
        },
        {
            "id": "kinds",
            "tier": "giveaway",
            "t": "Acute ones are smaller than 90°, right ones are exactly 90°, and obtuse ones are between 90° and 180°",
            "k": [
                "acute",
                "obtuse",
                "right ones"
            ],
            "n": 0
        },
        {
            "id": "units",
            "tier": "giveaway",
            "t": "Measured in degrees (360 in a full turn) or radians (2π in a full turn)",
            "k": [
                "degrees",
                "radians",
                "full turn"
            ],
            "n": 0
        },
        {
            "id": "protractor",
            "tier": "giveaway",
            "t": "Measured with a protractor, a half-circle tool marked from 0° to 180°",
            "k": [
                "protractor",
                "half-circle"
            ],
            "n": 0
        },
        {
            "id": "triangle-sum",
            "tier": "giveaway",
            "t": "The three inside any triangle on a flat surface add up to 180°",
            "k": [
                "triangle",
                "flat surface",
                "180"
            ],
            "n": 0,
            "rabbit": "Triangles"
        },
        {
            "id": "babylonians",
            "tier": "middle",
            "t": "The 360-part full turn is usually traced to Babylonian astronomers, who counted in base 60; a degree has 60 minutes, and a minute has 60 seconds",
            "k": [
                "babylonian",
                "base 60",
                "minutes"
            ],
            "n": 0
        },
        {
            "id": "complementary",
            "tier": "middle",
            "t": "Complementary pairs add up to 90° (a quarter turn); supplementary pairs add up to 180° (a half turn)",
            "k": [
                "complementary",
                "supplementary"
            ],
            "n": 0
        },
        {
            "id": "straight-reflex",
            "tier": "middle",
            "t": "A straight one is exactly 180°; reflex ones are between 180° and 360°",
            "k": [
                "straight",
                "reflex"
            ],
            "n": 0
        },
        {
            "id": "transversal",
            "tier": "middle",
            "t": "A transversal crossing two parallel lines makes equal corresponding and alternate interior pairs; same-side interior pairs add up to 180°",
            "k": [
                "transversal",
                "corresponding",
                "alternate interior"
            ],
            "n": 0,
            "rabbit": "Parallel postulate"
        },
        {
            "id": "vertical",
            "tier": "middle",
            "t": "When two lines cross, the vertical pairs across from each other are equal; Thales is traditionally credited with proving it",
            "k": [
                "vertical",
                "thales",
                "cross"
            ],
            "n": 0
        },
        {
            "id": "polygon-sum",
            "tier": "middle",
            "t": "Inside an n-sided polygon they total (n − 2) × 180°, so each extra side adds a half turn; a convex polygon’s exterior ones total 360°",
            "k": [
                "polygon",
                "half turn",
                "exterior"
            ],
            "n": 0
        },
        {
            "id": "radian",
            "tier": "middle",
            "t": "One radian cuts off an arc as long as the radius; π radians equal 180°, so one radian is about 57.3°",
            "k": [
                "radian",
                "radius",
                "57.3"
            ],
            "n": 0,
            "rabbit": "Pi"
        },
        {
            "id": "inscribed",
            "tier": "middle",
            "t": "An inscribed one is half of the central one that cuts off the same arc of a circle",
            "k": [
                "inscribed",
                "central",
                "arc"
            ],
            "n": 0,
            "rabbit": "Circles"
        },
        {
            "id": "carpenter",
            "tier": "middle",
            "t": "A carpenter’s square, shaped like a capital L, checks that a corner forms a right one",
            "k": [
                "carpenter",
                "capital l"
            ],
            "n": 0
        },
        {
            "id": "wantzel",
            "tier": "power",
            "t": "Pierre Wantzel proved in 1837 that, in general, they cannot be trisected (split into three equal parts) with only a compass and straightedge; Archimedes got around this with a marked ruler",
            "k": [
                "wantzel",
                "1837",
                "trisected",
                "archimedes"
            ],
            "n": 0
        },
        {
            "id": "cotes-thomson",
            "tier": "power",
            "t": "Roger Cotes worked out the radian idea in the early 1700s; James Thomson, Lord Kelvin’s brother, first printed the name “radian” in 1873",
            "k": [
                "cotes",
                "james thomson",
                "1873",
                "kelvin"
            ],
            "n": 0
        },
        {
            "id": "gradian",
            "tier": "power",
            "t": "Calculators offer a GRAD mode: the gradian, introduced in France, splits a full turn into 400 parts",
            "k": [
                "gradian",
                "grad",
                "400",
                "france"
            ],
            "n": 0
        },
        {
            "id": "theodolite",
            "tier": "power",
            "t": "Surveyors measure them side to side and up and down with a theodolite, a telescope-like instrument on a tripod",
            "k": [
                "theodolite",
                "surveyors",
                "tripod"
            ],
            "n": 0
        },
        {
            "id": "sextant",
            "tier": "power",
            "t": "Sailors used a sextant to measure one between the horizon and the Sun or a star, to work out their latitude; surveyors use “elevation” and “depression” types",
            "k": [
                "sextant",
                "horizon",
                "latitude",
                "elevation"
            ],
            "n": 0
        },
        {
            "id": "euclid",
            "tier": "power",
            "t": "Euclid’s _Elements_ defines one as the inclination of two lines that meet; his fourth postulate says all right ones are equal",
            "k": [
                "euclid",
                "inclination",
                "fourth postulate"
            ],
            "n": 0,
            "rabbit": "Euclid"
        },
        {
            "id": "dihedral",
            "tier": "power",
            "t": "Two planes meeting along a line form a dihedral one",
            "k": [
                "dihedral",
                "planes"
            ],
            "n": 0
        },
        {
            "id": "latin",
            "tier": "power",
            "t": "Their name comes from a Latin word for “corner”; “acute” and “obtuse” come from Latin words for “sharp” and “blunt”",
            "k": [
                "latin",
                "corner",
                "sharp",
                "blunt"
            ],
            "n": 0
        },
        {
            "id": "standard-position",
            "tier": "power",
            "t": "In standard position, the vertex is at the origin and the starting side lies along the positive x-axis; counterclockwise turns are positive",
            "k": [
                "standard position",
                "origin",
                "counterclockwise"
            ],
            "n": 0
        },
        {
            "id": "steradian",
            "tier": "power",
            "t": "Solid (3D) ones are measured in steradians, and a whole sphere is 4π steradians; the SI unit for flat ones is named for a circle’s radius",
            "k": [
                "steradians",
                "solid",
                "si unit"
            ],
            "n": 0
        },
        {
            "id": "reflection",
            "tier": "power",
            "t": "Law of reflection: light leaves a mirror at the same one it arrived at, both measured from the normal; Snell’s law covers light bending into water",
            "k": [
                "reflection",
                "normal",
                "snell"
            ],
            "n": 0
        },
        {
            "id": "sphere",
            "tier": "power",
            "t": "On a sphere, a triangle with one corner at the North Pole and two on the equator can have three 90° ones",
            "k": [
                "sphere",
                "north pole",
                "equator"
            ],
            "n": 0,
            "rabbit": "Spheres"
        },
        {
            "id": "golden",
            "tier": "power",
            "t": "Seeds and leaves on many plants, such as sunflowers, spiral outward separated by a “golden” one linked to the golden ratio",
            "k": [
                "golden",
                "sunflowers",
                "seeds"
            ],
            "n": 0
        },
        {
            "id": "congruence",
            "tier": "power",
            "t": "The triangle congruence shortcuts ASA and SAS are named partly for them",
            "k": [
                "congruence",
                "asa",
                "sas"
            ],
            "n": 0
        }
    ],
    "trap": {
        "title": "Figure, unit, or tool?",
        "body": "Clues about angles often name things that are their own answer lines. Degrees and radians are units for measuring angles, a protractor is the tool that measures them, and the vertex is only the point where the two rays meet. Other tossups want one specific kind, such as a right angle, or ask about triangles, whose three angles add up to 180°.",
        "fix": "If the question asks for “these figures” formed by two rays, say “angles.” If it asks for “this unit” or “this tool,” answer degrees, radians, or protractor instead. Saying only “corners” earns a prompt.",
        "line": "Real answer line: <b><u>angle</u></b>s (accept specific kinds, such as <u>right angle</u>s; prompt on <u>corner</u>s; do not accept units such as “degrees” or “radians”)"
    }
}

with open("topics/angles.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote topics/angles.json")
