import json

data = {
    "id": "inequalities",
    "name": "Inequalities",
    "mono": "INQ",
    "category": "Math",
    "qbCategory": "Science · Other Science (Math)",
    "kicker": "Comparisons using < or > · Flip the sign when multiplying by a negative",
    "dates": "Symbols < and > first printed in Thomas Harriot’s book, 1631",
    "briefing": "An inequality is a math statement saying that two amounts may not be equal, using signs such as < (“less than”), > (“greater than”), ≤, and ≥. Solving one is a lot like solving an equation, with one big twist: when you multiply or divide both sides by a negative number, the sign flips direction. The symbols < and > first appeared in a 1631 book by the English mathematician Thomas Harriot, published after his death.",
    "answerHtml": "<b><u>inequalities</u></b> (or <u>inequality</u>; accept <u>inequality sign</u>s; prompt on <u>less than</u> or <u>greater than</u>; do not accept “equations” or a specific inequality such as the “triangle inequality”)",
    "accept": [
        "inequalities",
        "inequality",
        "mathematical inequality",
        "mathematical inequalities",
        "inequality sign",
        "inequality signs",
        "inequality symbol",
        "inequality symbols",
        "linear inequality",
        "linear inequalities",
        "inequation",
        "inequations"
    ],
    "prompt": [
        "less than",
        "greater than",
        "less than or equal to",
        "greater than or equal to",
        "comparison",
        "comparisons",
        "not equal",
        "not equal to"
    ],
    "reject": [
        "equations",
        "equation",
        "equality",
        "equalities",
        "equal sign",
        "equals sign",
        "equals",
        "linear equations",
        "linear equation",
        "systems of linear equations",
        "system of linear equations",
        "triangle inequality",
        "am gm inequality",
        "arithmetic geometric mean inequality",
        "inequality of arithmetic and geometric means",
        "cauchy schwarz inequality",
        "chebyshevs inequality",
        "markovs inequality",
        "bells inequality",
        "bell inequality",
        "isoperimetric inequality",
        "bernoullis inequality",
        "jensens inequality",
        "income inequality",
        "economic inequality",
        "social inequality",
        "wealth inequality",
        "gini coefficient",
        "interval notation",
        "absolute value",
        "linear programming",
        "number line",
        "uncertainty principle"
    ],
    "tests": {
        "right": [
            "inequalities",
            "Inequality",
            "inequality signs",
            "inequalites",
            "linear inequalities"
        ],
        "prompt": [
            "less than",
            "greater than"
        ],
        "wrong": [
            "equations",
            "equality",
            "triangle inequality",
            "systems of linear equations",
            "income inequality",
            "absolute value"
        ]
    },
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Inequality_(mathematics)",
    "qb": {
        "q": "inequality",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "The symbols used for the two strict kinds of these statements first appeared in print in a 1631 book by Thomas Harriot, published ten years after his death. Harriot had earlier sailed to Roanoke and written _A Briefe and True Report of the New Found Land of Virginia_.",
            "r": "For 10 points, name these statements that compare two amounts using signs that mean “less than” or “greater than.”"
        },
        {
            "p": "The trichotomy property says that for any two real numbers, either the numbers are equal or exactly one of the two strict kinds of these statements is true. Multiplying or dividing both sides of one of these statements by a negative number reverses its direction.",
            "r": "For 10 points, name these mathematical statements, such as x is greater than 3, that compare two amounts."
        },
        {
            "p": "One of these statements says that the average of two positive numbers is always at least the square root of their product, with equality only when the two numbers are the same. That result compares the arithmetic mean with the geometric mean.",
            "r": "For 10 points, name these statements, written with symbols such as “greater than or equal to,” that compare two amounts."
        },
        {
            "p": "Augustin-Louis Cauchy [“koh-SHEE”], Viktor Bunyakovsky [“boon-yuh-KOF-skee”], and Hermann Schwarz [“SHWARTS”] name one of these statements, which says that the size of the dot product of two vectors is never more than the product of their lengths. That one can be proved using the fact that no real number squared is below zero.",
            "r": "They compare two amounts. For 10 points, name these statements, which use symbols meaning “less than” or “greater than.”"
        },
        {
            "p": "Pafnuty Chebyshev [“cheh-bih-SHOFF”] names one of these statements guaranteeing that, in any set of data, at least three-fourths of the values lie within two standard deviations of the mean. His student Andrey Markov names a related one of these statements.",
            "r": "For 10 points, name these statements that compare two amounts using signs such as “less than.”"
        },
        {
            "p": "Werner Heisenberg’s [“HY-zen-burgz”] uncertainty principle is one of these statements: the uncertainty in a particle’s position times the uncertainty in its momentum is at least a tiny fixed amount. The second law of thermodynamics can also be written as one of these, saying that the total entropy of an isolated system never decreases.",
            "r": "They compare amounts. For 10 points, name these statements, which use signs such as “greater than or equal to.”"
        },
        {
            "p": "In 1964, John Stewart Bell derived one of these statements that must hold if particles carry hidden instructions set in advance, and experiments on entangled particles have broken it. Alain Aspect, John Clauser, and Anton Zeilinger [“TSY-ling-er”] shared the 2022 Nobel Prize in Physics for such experiments.",
            "r": "Solving one gives a range of answers. For 10 points, name these statements that compare amounts using signs like “less than.”"
        },
        {
            "p": "According to legend, Queen Dido [“DY-doh”] founded Carthage on as much land as she could surround with strips cut from one oxhide, a story linked to the isoperimetric one of these statements. That statement says that, of all shapes with a given perimeter, the circle encloses the most area.",
            "r": "For 10 points, name these mathematical statements that compare two amounts using signs like “less than” instead of an equals sign."
        },
        {
            "p": "In 1939, Leonid Kantorovich [“kahn-tuh-ROH-vich”] began studying how to find the best outcome when choices are limited by a set of these statements, and in 1947 George Dantzig [“DANT-sig”] invented the simplex method to solve such problems. That field is called linear programming.",
            "r": "Students picture each sign as an alligator mouth eating the bigger number. For 10 points, name these statements that use signs like “greater than.”"
        },
        {
            "p": "G. H. Hardy, J. E. Littlewood, and George Pólya [“POH-yuh”] wrote a famous 1934 book whose one-word title names these statements. A compound one of these statements can describe all the numbers between 2 and 5.",
            "r": "For 10 points, name these statements, written with signs like “less than,” that compare two amounts."
        },
        {
            "p": "The complex numbers cannot be put in order in a way that works with multiplication, so these statements are not used to compare two complex numbers. For real numbers, squaring both sides of one of these statements can change whether it is true.",
            "r": "For 10 points, name these statements, such as 3 is less than 5, which compare two amounts."
        },
        {
            "p": "Many programming languages type the non-strict versions of these statements as two characters, ending with an equals sign. In a program, each such comparison evaluates to either true or false.",
            "r": "Each one compares two amounts. For 10 points, name these statements, which use the symbols for “less than” and “greater than.”"
        },
        {
            "p": "When graphing one of these statements in the coordinate plane, you draw a dashed boundary line if points on the line are not included and a solid line if they are, then shade one side. On a number line, an open circle shows that an endpoint is not included.",
            "r": "Solving one usually gives a whole range of answers. For 10 points, name these statements, which use signs such as “greater than.”"
        },
        {
            "p": "The triangle version of these statements says that any two sides of a triangle add up to more than the third side. For absolute values, that same statement says that the absolute value of a sum is never more than the sum of the absolute values.",
            "r": "For 10 points, name these statements, which compare two amounts using signs like “less than” or “greater than.”"
        },
        {
            "p": "An English astronomer who drew the Moon through a telescope in 1609, months before Galileo did, also introduced the modern symbols for the two strict kinds of these statements. That man, Thomas Harriot, served as a scientific adviser to Sir Walter Raleigh.",
            "r": "For 10 points, name these statements, which compare two amounts using symbols for “less than” and “greater than.”"
        }
    ],
    "clues": [
        {
            "id": "definition",
            "tier": "giveaway",
            "t": "Math statements that compare two amounts that may not be equal, using signs like < (less than) and > (greater than)",
            "k": ["compare", "less than", "greater than"],
            "n": 0
        },
        {
            "id": "signs",
            "tier": "giveaway",
            "t": "Four main signs: <, >, ≤ (less than or equal to), and ≥ (greater than or equal to)",
            "k": ["or equal to", "four main signs"],
            "n": 0
        },
        {
            "id": "alligator",
            "tier": "giveaway",
            "t": "Memory trick: each sign is an alligator mouth that eats the bigger number",
            "k": ["alligator", "bigger number"],
            "n": 0
        },
        {
            "id": "flip",
            "tier": "middle",
            "t": "Multiplying or dividing both sides by a negative number flips the sign",
            "k": ["flips", "negative number", "dividing"],
            "n": 0,
            "rabbit": "Negative numbers"
        },
        {
            "id": "harriot",
            "tier": "middle",
            "t": "Thomas Harriot’s symbols < and > first appeared in print in 1631, ten years after his death",
            "k": ["harriot", "1631"],
            "n": 0
        },
        {
            "id": "number-line",
            "tier": "middle",
            "t": "On a number line, an open circle means the endpoint is not included (< or >), and a closed circle means it is (≤ or ≥)",
            "k": ["open circle", "closed circle", "number line"],
            "n": 0
        },
        {
            "id": "graphing",
            "tier": "middle",
            "t": "In the coordinate plane, draw a dashed boundary for < or >, a solid one for ≤ or ≥, then shade one side",
            "k": ["dashed", "solid", "shade"],
            "n": 0
        },
        {
            "id": "triangle",
            "tier": "middle",
            "t": "The triangle version: any two sides of a triangle add up to more than the third; for absolute values, |a + b| ≤ |a| + |b|",
            "k": ["triangle", "third", "absolute values"],
            "n": 0,
            "rabbit": "Triangles"
        },
        {
            "id": "compound",
            "tier": "middle",
            "t": "A compound one, like 2 < x < 5, describes all the numbers between two values",
            "k": ["compound", "between"],
            "n": 0
        },
        {
            "id": "trichotomy",
            "tier": "middle",
            "t": "Trichotomy: for any two real numbers a and b, exactly one of a < b, a = b, or a > b is true",
            "k": ["trichotomy", "exactly one"],
            "n": 0
        },
        {
            "id": "range",
            "tier": "middle",
            "t": "Solving one usually gives a whole range of answers, often written in interval notation",
            "k": ["range", "interval notation"],
            "n": 0
        },
        {
            "id": "roanoke",
            "tier": "power",
            "t": "Harriot sailed to Roanoke and wrote _A Briefe and True Report of the New Found Land of Virginia_",
            "k": ["roanoke", "briefe and true report"],
            "n": 0
        },
        {
            "id": "moon",
            "tier": "power",
            "t": "Harriot drew the Moon through a telescope in 1609, months before Galileo, and advised Sir Walter Raleigh",
            "k": ["moon", "telescope", "raleigh"],
            "n": 0
        },
        {
            "id": "am-gm",
            "tier": "power",
            "t": "AM–GM: the average of two positive numbers is at least the square root of their product, with equality only when the numbers are the same",
            "k": ["am–gm", "average", "geometric"],
            "n": 0
        },
        {
            "id": "cauchy-schwarz",
            "tier": "power",
            "t": "Cauchy, Bunyakovsky, and Schwarz name one: the size of a dot product is never more than the product of the two vectors’ lengths",
            "k": ["cauchy", "schwarz", "dot product"],
            "n": 0,
            "rabbit": "Augustin-Louis Cauchy"
        },
        {
            "id": "chebyshev",
            "tier": "power",
            "t": "Chebyshev’s: in any data set, at least 3/4 of the values lie within two standard deviations of the mean; his student Andrey Markov names another",
            "k": ["chebyshev", "standard deviations", "markov"],
            "n": 0,
            "rabbit": "Standard deviation"
        },
        {
            "id": "heisenberg",
            "tier": "power",
            "t": "Heisenberg’s uncertainty principle: the uncertainty in position times the uncertainty in momentum is at least h-bar over 2",
            "k": ["heisenberg", "uncertainty principle", "momentum"],
            "n": 0,
            "rabbit": "Uncertainty principle"
        },
        {
            "id": "entropy",
            "tier": "power",
            "t": "The second law of thermodynamics: the total entropy of an isolated system never decreases",
            "k": ["second law", "entropy"],
            "n": 0,
            "rabbit": "Entropy"
        },
        {
            "id": "bell",
            "tier": "power",
            "t": "John Stewart Bell’s (1964) one is broken by experiments on entangled particles; Aspect, Clauser, and Zeilinger shared the 2022 Nobel Prize in Physics",
            "k": ["bell", "1964", "entangled", "2022"],
            "n": 0
        },
        {
            "id": "isoperimetric",
            "tier": "power",
            "t": "Isoperimetric: for a given perimeter, a circle encloses the most area; it is linked to the legend of Queen Dido founding Carthage",
            "k": ["isoperimetric", "dido", "carthage"],
            "n": 0
        },
        {
            "id": "linear-programming",
            "tier": "power",
            "t": "Linear programming finds the best choice under a set of them: Leonid Kantorovich began it in 1939, and George Dantzig invented the simplex method in 1947",
            "k": ["linear programming", "kantorovich", "dantzig", "simplex"],
            "n": 0
        },
        {
            "id": "hardy",
            "tier": "power",
            "t": "G. H. Hardy, J. E. Littlewood, and George Pólya wrote a famous 1934 book with a one-word title naming them",
            "k": ["hardy", "littlewood", "1934"],
            "n": 0
        },
        {
            "id": "complex",
            "tier": "power",
            "t": "Complex numbers can’t be ordered in a way that works with multiplication, so these aren’t used to compare them",
            "k": ["complex numbers", "ordered"],
            "n": 0,
            "rabbit": "Complex numbers"
        },
        {
            "id": "programming",
            "tier": "power",
            "t": "Programming languages type the non-strict ones as two characters, like <= and >=, and each comparison gives true or false",
            "k": ["programming", "true or false"],
            "n": 0
        },
        {
            "id": "squaring",
            "tier": "power",
            "t": "Squaring both sides can change whether one is true: −3 < 2, but 9 > 4",
            "k": ["squaring", "both sides"],
            "n": 0
        }
    ],
    "trap": {
        "title": "General idea or famous example?",
        "body": "Many tossups on inequalities use famous examples as clues, such as the triangle inequality or Chebyshev’s inequality, and each of those can be its own answer line; naming one of them when the question asks for the general idea is wrong. Equations, which use an equals sign, are a different answer line, and “income inequality” is a social-science topic, not a math one.",
        "fix": "If the question asks for “these statements” that compare amounts with <, >, ≤, or ≥, say “inequalities.” If every clue describes one named result, like the sides of a triangle, name that result. Saying only “less than” or “greater than” earns a prompt.",
        "line": "Real answer line: <b><u>inequalities</u></b> (or <u>inequality</u>; accept <u>inequality sign</u>s; prompt on <u>less than</u> or <u>greater than</u>; do not accept “equations” or a specific inequality such as the “triangle inequality”)"
    }
}

with open("topics/inequalities.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote topics/inequalities.json")
