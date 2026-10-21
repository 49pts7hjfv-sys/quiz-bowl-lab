import json

data = {
    "id": "vectors",
    "name": "Vectors",
    "mono": "VEC",
    "category": "Math",
    "qbCategory": "Science · Other Science (Math)",
    "kicker": "Quantities with size and direction · Drawn as arrows, added tip to tail",
    "dates": "Named by William Rowan Hamilton in the 1840s",
    "briefing": "A vector is a quantity that has both a size, called its magnitude, and a direction, so it is drawn as an arrow. “Walk 3 blocks” is just a distance, but “walk 3 blocks north” is a vector. Velocity, force, and displacement are vectors, while plain amounts like mass or temperature are called scalars. To add two vectors, you place them tip to tail and draw one arrow from the very start to the very end.",
    "answerHtml": "<b><u>vector</u></b>s (or <u>vector quantit</u>ies; do not accept “scalars,” “matrices,” or “velocity”)",
    "accept": [
        "vectors",
        "vector",
        "vector quantity",
        "vector quantities",
        "euclidean vector",
        "euclidean vectors",
        "geometric vector",
        "geometric vectors",
        "spatial vector",
        "spatial vectors"
    ],
    "prompt": [],
    "reject": [
        "scalar",
        "scalars",
        "scalar quantity",
        "scalar quantities",
        "matrix",
        "matrices",
        "matrixes",
        "tensor",
        "tensors",
        "velocity",
        "speed",
        "displacement",
        "force",
        "forces",
        "acceleration",
        "momentum",
        "magnitude",
        "direction",
        "arrow",
        "arrows",
        "ray",
        "rays",
        "line segment",
        "line segments",
        "vector space",
        "vector spaces",
        "vector field",
        "vector fields",
        "vector calculus",
        "dot product",
        "cross product",
        "quaternion",
        "quaternions",
        "complex numbers",
        "parallelogram",
        "parallelograms"
    ],
    "tests": {
        "right": [
            "Vectors",
            "vector",
            "vecter",
            "vector quantity",
            "Euclidean vectors",
            "a vector"
        ],
        "prompt": [],
        "wrong": [
            "scalars",
            "matrix",
            "velocity",
            "tensor",
            "force",
            "dot product",
            "vector field"
        ]
    },
    "mediaPending": True,
    "media": [],
    "wiki": "https://en.wikipedia.org/wiki/Euclidean_vector",
    "qb": {
        "q": "vector",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "William Rowan Hamilton coined the names of these quantities and of scalars in the 1840s, as the two parts of a quaternion. Each quaternion combined a plain number with one of these quantities pointing in three-dimensional space.",
            "r": "For 10 points, name these quantities, such as force and velocity, that have both a magnitude and a direction."
        },
        {
            "p": "The length of the cross product of two of these quantities equals the area of the parallelogram they outline, and its direction is given by the right-hand rule. Their dot product equals the product of their lengths times the cosine of the angle between them.",
            "r": "They can be added tip to tail. For 10 points, name these quantities that have both size and direction, unlike scalars."
        },
        {
            "p": "The name of these quantities comes from the Latin word for “carrier,” which is why biologists use the same word for a mosquito that spreads malaria. Torque is the cross product of two of these quantities: the position where a force is applied, measured from a pivot, and the force itself.",
            "r": "They are drawn as arrows. For 10 points, name these quantities, such as velocity, that have both a magnitude and a direction."
        },
        {
            "p": "Taking the cross product of the unit examples of these quantities called i-hat and j-hat gives k-hat, but reversing the order gives negative k-hat. Those three unit examples point along the x-, y-, and z-axes, and each has a length of exactly 1.",
            "r": "For 10 points, name these quantities, such as force and displacement, that have both a magnitude and a direction."
        },
        {
            "p": "Pushing straight down on a box sliding across the floor does no work, because work is a dot product, and the dot product of two of these quantities is zero whenever they are perpendicular to each other.",
            "r": "Force and displacement are examples of them, while mass and temperature are not. For 10 points, name these quantities, often drawn as arrows."
        },
        {
            "p": "The dot product of two of these quantities with components 1 and 2 and components 3 and 4 is 11, since 1 times 3 plus 2 times 4 equals 11. If the dot product of two nonzero ones is zero, they are perpendicular.",
            "r": "To add two of these, place them tip to tail. For 10 points, name these quantities with a magnitude and a direction."
        },
        {
            "p": "Isaac Newton’s _Principia_ combined two forces using the parallelogram law, which says that two of these quantities drawn from the same point add up to the diagonal of the parallelogram they form. Multiplying one of them by negative 1 turns it to point the opposite way.",
            "r": "Velocity is one of these quantities, while speed is not. For 10 points, name these quantities that have both size and direction."
        },
        {
            "p": "A boat aimed straight across a river at 4 meters per second, pushed downstream by a current of 3 meters per second, actually moves at 5 meters per second, a result found by adding two of these quantities. Pilots do the same to correct for wind.",
            "r": "Unlike scalars, these quantities have a direction. For 10 points, name these quantities, drawn as arrows."
        },
        {
            "p": "A weather map that draws a small arrow at many places to show the wind’s speed and direction is showing a “field” of these quantities. The net force on an object is found by adding up all the forces on it as these quantities, so two equal pulls in opposite directions cancel out.",
            "r": "They are drawn as arrows. For 10 points, name these quantities, such as velocity, that have both a magnitude and a direction."
        },
        {
            "p": "These quantities are often printed in bold type or written with a small arrow over the letter, and the length of one named v is written with bars on both sides of the v. A matrix with just one column is often treated as one of these quantities.",
            "r": "The one pointing from the origin to the point (3, 4) has a length of 5. For 10 points, name these quantities that have both size and direction."
        },
        {
            "p": "A runner who finishes one full lap of a 400-meter track has run 400 meters but ends with a displacement of zero, since displacement measures only the straight arrow from start to finish. Walking 3 kilometers east and then 4 kilometers north gives a displacement of 5 kilometers.",
            "r": "Displacement is one of these quantities, while distance is not. For 10 points, name these quantities that have both a magnitude and a direction."
        },
        {
            "p": "In the 1880s, the Yale professor Josiah Willard Gibbs and the English engineer Oliver Heaviside separately created the modern system for calculating with these quantities, which physicists then used in place of quaternions. Each of these quantities can be split into components along the axes.",
            "r": "For 10 points, name these quantities, drawn as arrows, that have both size and direction."
        },
        {
            "p": "Two ice skaters at rest who push off each other have momenta equal in size but opposite in direction, so their total momentum stays zero, because momentum is one of these quantities, which cancel when they point opposite ways.",
            "r": "They can be added tip to tail. For 10 points, name these quantities, including velocity and force, that have both size and direction."
        },
        {
            "p": "Video game engines store each character’s position and motion as lists of numbers that stand for these quantities, and 3-D graphics use them to describe which way each surface faces, which controls how light bounces off it.",
            "r": "Unlike scalars, they have a direction. For 10 points, name these quantities, often drawn as arrows."
        },
        {
            "p": "Multiplying one of these quantities by 3 makes it three times as long without changing its direction, while multiplying it by 0 gives the zero one, which has a length of 0 and no particular direction.",
            "r": "They are added tip to tail. For 10 points, name these quantities, such as displacement, that have both a magnitude and a direction."
        }
    ],
    "clues": [
        {
            "id": "size-direction",
            "tier": "giveaway",
            "t": "A quantity with both a size, called its magnitude, and a direction",
            "k": ["magnitude", "direction", "size"],
            "n": 0
        },
        {
            "id": "arrows",
            "tier": "giveaway",
            "t": "Drawn as arrows: the arrow’s length shows the magnitude, and the arrowhead shows the direction",
            "k": ["arrows", "arrowhead", "length"],
            "n": 0
        },
        {
            "id": "examples",
            "tier": "giveaway",
            "t": "Velocity, force, acceleration, displacement, and momentum are examples",
            "k": ["velocity", "force", "displacement"],
            "n": 0,
            "rabbit": "Velocity"
        },
        {
            "id": "scalars",
            "tier": "giveaway",
            "t": "Contrasted with scalars, which have size only, like mass, temperature, speed, or distance",
            "k": ["scalars", "size only"],
            "n": 0
        },
        {
            "id": "tip-to-tail",
            "tier": "giveaway",
            "t": "Added tip to tail: the sum, called the resultant, runs from the start of the first arrow to the end of the last",
            "k": ["tip to tail", "resultant"],
            "n": 0
        },
        {
            "id": "components",
            "tier": "middle",
            "t": "Split into components along the axes; the arrow from the origin to (3, 4) has components 3 and 4",
            "k": ["components", "axes"],
            "n": 0
        },
        {
            "id": "length",
            "tier": "middle",
            "t": "Its length comes from the Pythagorean theorem: the one with components 3 and 4 has length √(9 + 16) = 5",
            "k": ["pythagorean theorem", "√(9 + 16)"],
            "n": 0,
            "rabbit": "Pythagorean theorem"
        },
        {
            "id": "unit",
            "tier": "middle",
            "t": "Unit ones have length 1; î, ĵ, and k̂ (“i-hat,” “j-hat,” “k-hat”) point along the x-, y-, and z-axes",
            "k": ["unit", "i-hat", "length 1"],
            "n": 0
        },
        {
            "id": "scalar-multiple",
            "tier": "middle",
            "t": "Multiplying by a scalar stretches or shrinks it; multiplying by −1 flips it to point the opposite way, and multiplying by 0 gives the zero one",
            "k": ["stretches", "opposite way", "zero"],
            "n": 0
        },
        {
            "id": "displacement",
            "tier": "middle",
            "t": "A full lap of a 400-meter track has a displacement of zero; walking 3 km east, then 4 km north, gives a displacement of 5 km",
            "k": ["full lap", "displacement", "400-meter"],
            "n": 0
        },
        {
            "id": "net-force",
            "tier": "middle",
            "t": "Forces and momenta add this way: equal pulls in opposite directions cancel, giving a net force of zero",
            "k": ["net force", "cancel", "momenta"],
            "n": 0
        },
        {
            "id": "river",
            "tier": "middle",
            "t": "A boat aimed across a river at 4 m/s in a 3 m/s current really moves at 5 m/s; pilots correct for wind the same way",
            "k": ["river", "current", "pilots"],
            "n": 0
        },
        {
            "id": "notation",
            "tier": "middle",
            "t": "Printed in bold or written with a small arrow over the letter; its length is written |v| or ‖v‖",
            "k": ["bold", "small arrow"],
            "n": 0
        },
        {
            "id": "latin",
            "tier": "middle",
            "t": "Its name is Latin for “carrier,” so biologists use the same word for a mosquito or tick that spreads disease",
            "k": ["carrier", "mosquito", "latin"],
            "n": 0
        },
        {
            "id": "hamilton",
            "tier": "power",
            "t": "William Rowan Hamilton named them, and scalars, in the 1840s as the two parts of his quaternions",
            "k": ["hamilton", "quaternions", "1840s"],
            "n": 0
        },
        {
            "id": "gibbs-heaviside",
            "tier": "power",
            "t": "Josiah Willard Gibbs (Yale) and Oliver Heaviside (England) separately built the modern system for calculating with them in the 1880s",
            "k": ["gibbs", "heaviside", "1880s"],
            "n": 0
        },
        {
            "id": "dot-product",
            "tier": "power",
            "t": "Dot product: multiply matching components and add, so (1, 2) and (3, 4) give 1×3 + 2×4 = 11, a plain number",
            "k": ["dot product", "matching components"],
            "n": 0
        },
        {
            "id": "perpendicular",
            "tier": "power",
            "t": "The dot product equals the two lengths times the cosine of the angle between them, so it is 0 for perpendicular ones",
            "k": ["cosine", "perpendicular"],
            "n": 0
        },
        {
            "id": "cross-product",
            "tier": "power",
            "t": "Cross product: two in 3-D give a new one perpendicular to both; î × ĵ = k̂, but ĵ × î = −k̂",
            "k": ["cross product", "î × ĵ = k̂"],
            "n": 0
        },
        {
            "id": "right-hand",
            "tier": "power",
            "t": "The right-hand rule gives a cross product’s direction; its length equals the area of the parallelogram the two outline",
            "k": ["right-hand rule", "area"],
            "n": 0
        },
        {
            "id": "torque",
            "tier": "power",
            "t": "Torque is the cross product of a force’s position (measured from the pivot) and the force",
            "k": ["torque", "pivot"],
            "n": 0
        },
        {
            "id": "work",
            "tier": "power",
            "t": "Work is the dot product of force and displacement, so pushing straight down on a sliding box does no work",
            "k": ["work", "sliding box"],
            "n": 0
        },
        {
            "id": "parallelogram-law",
            "tier": "power",
            "t": "Parallelogram law: two drawn from one point add up to the diagonal of the parallelogram they form; Newton’s _Principia_ (1687) combined forces this way",
            "k": ["parallelogram law", "diagonal", "principia"],
            "n": 0,
            "rabbit": "Parallelograms"
        },
        {
            "id": "matrix-column",
            "tier": "power",
            "t": "A matrix with a single column (or a single row) is often treated as one, written as a list of components",
            "k": ["single column", "matrix"],
            "n": 0,
            "rabbit": "Matrices"
        },
        {
            "id": "field",
            "tier": "power",
            "t": "A weather map with wind arrows at many points shows a “field” of them",
            "k": ["field", "weather map", "wind"],
            "n": 0
        },
        {
            "id": "graphics",
            "tier": "power",
            "t": "Video games store positions and velocities as them, and 3-D graphics use them to show which way each surface faces for lighting",
            "k": ["video games", "graphics", "surface faces"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Vector or one example?",
        "body": "Velocity, force, and displacement are all vectors, and each is also its own answer line, so a tossup about one specific quantity may want that quantity instead. Scalars (size only) and matrices (grids of numbers) are separate answer lines too, and since a matrix with one column is sometimes called a column vector, clues about the two can overlap.",
        "fix": "Listen for the noun: “these quantities” with both magnitude and direction, tip-to-tail adding, dot and cross products, or i-hat, j-hat, and k-hat means vectors. “This quantity,” defined as the rate of change of position, means velocity; “size only” means scalars.",
        "line": "Real answer line: <b><u>vector</u></b>s (or <u>vector quantit</u>ies; do not accept “scalars,” “matrices,” or “velocity”)"
    }
}

with open("topics/vectors.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote topics/vectors.json")
