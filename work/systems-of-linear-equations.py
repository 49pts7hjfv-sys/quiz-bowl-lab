import json

data = {
    "id": "systems-of-linear-equations",
    "name": "Systems of linear equations",
    "mono": "SLE",
    "category": "Math",
    "qbCategory": "Science · Other Science (Math)",
    "kicker": "Equations solved together · The solution is where the lines cross",
    "dates": "Solved in China’s _Nine Chapters on the Mathematical Art_, about 2,000 years ago",
    "briefing": "A system of linear equations is two or more equations, such as x + y = 10 and x − y = 4, that must all be true at the same time. Graph each one as a line, and the solution is where the lines cross, here at x = 7 and y = 3; parallel lines never cross, so their system has no solution. Chinese mathematicians solved problems like this with counting rods about 2,000 years ago.",
    "answerHtml": "<b><u>system</u></b>s of <b><u>linear equation</u></b>s (accept <u>linear system</u>s or <u>simultaneous linear equations</u>; prompt on <u>system of equations</u>, <u>simultaneous equations</u>, or <u>linear equations</u>; do not accept “matrices” or “systems of inequalities”)",
    "accept": [
        "systems of linear equations",
        "system of linear equations",
        "linear system",
        "linear systems",
        "linear system of equations",
        "linear systems of equations",
        "linear equation system",
        "linear equation systems",
        "simultaneous linear equations",
        "set of linear equations",
        "sets of linear equations"
    ],
    "prompt": [
        "system of equations",
        "systems of equations",
        "simultaneous equations",
        "simultaneous equation",
        "linear equations",
        "linear equation",
        "equation system",
        "equation systems"
    ],
    "reject": [
        "nonlinear",
        "non linear",
        "inequalities",
        "inequality",
        "system of inequalities",
        "systems of inequalities",
        "linear inequalities",
        "linear inequality",
        "linear programming",
        "linear algebra",
        "linear function",
        "linear functions",
        "quadratic equations",
        "quadratic equation",
        "quadratic formula",
        "quadratics",
        "differential equations",
        "differential equation",
        "matrices",
        "matrix",
        "matrixes",
        "augmented matrix",
        "coefficient matrix",
        "determinant",
        "determinants",
        "cramers rule",
        "cramer rule",
        "gaussian elimination",
        "gauss jordan elimination",
        "row reduction",
        "elimination",
        "substitution",
        "graphing",
        "vectors",
        "vector",
        "polynomials",
        "polynomial"
    ],
    "tests": {
        "right": [
            "systems of linear equations",
            "System of linear equations",
            "linear system",
            "simultaneous linear equations",
            "sytems of linear equations",
            "a system of linear equations"
        ],
        "prompt": [
            "system of equations",
            "linear equations",
            "simultaneous equations"
        ],
        "wrong": [
            "matrices",
            "systems of inequalities",
            "linear inequalities",
            "quadratic equations",
            "system of nonlinear equations",
            "non-linear system",
            "Gaussian elimination",
            "determinant",
            "linear algebra"
        ]
    },
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/System_of_linear_equations",
    "qb": {
        "q": "linear equations",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "The eighth chapter of the Chinese classic _The Nine Chapters on the Mathematical Art_ opens with one of these about bundles of three grades of grain, solved by moving counting rods on a board. That chapter’s title, “fangcheng” [“fahng-CHUNG”], is the modern Chinese word for “equation.”",
            "r": "Graphing one of these shows its solution where the lines cross. For 10 points, name these groups of equations, which can be solved by substitution or elimination."
        },
        {
            "p": "Gabriel Cramer of Geneva published a rule in 1750 that solves one of these by dividing two determinants, one of them found after replacing a column of coefficients with the constants from the right-hand side. That rule works only when the determinant of the coefficient matrix is not zero.",
            "r": "For 10 points, name these sets of equations, such as x + y = 10 and x − y = 4, that must all be true at once."
        },
        {
            "p": "An ancient Chinese puzzle in the _Sunzi Suanjing_ [“SOON-dzuh SWAHN-jing”] asks how many pheasants and rabbits share a cage holding 35 heads and 94 feet. The answer is 23 pheasants and 12 rabbits, since 23 plus 12 is 35 and their feet add up to 46 plus 48, or 94.",
            "r": "One way to solve it is to double the heads equation and subtract it from the feet equation, a method called elimination. For 10 points, name these groups of equations solved together."
        },
        {
            "p": "Seki Takakazu [“SEH-kee tah-kah-KAH-zoo”] in Japan and Gottfried Leibniz [“LYBE-nits”] in Germany each discovered determinants in the late 1600s while studying how to solve these. In 1750, Gabriel Cramer published a rule that solves them using ratios of determinants.",
            "r": "For 10 points, name these collections of equations, such as 2x + y = 7 and x − y = 2, that are solved together."
        },
        {
            "p": "The TOP500 list ranks the world’s fastest supercomputers by how quickly they solve one gigantic one of these, a test called the LINPACK benchmark. Computers often solve these using Gaussian elimination, a step-by-step method of row operations on a grid of numbers.",
            "r": "For 10 points, name these groups of equations that share the same unknowns and must all be true at the same time."
        },
        {
            "p": "The Rouché–Capelli [“roo-SHAY kuh-PEL-ee”] theorem says that one of these has a solution exactly when two matrices built from it have the same rank. One of those matrices, called the augmented matrix, adds a column of constants to the grid of coefficients.",
            "r": "If its two equations graph as the same line, it has infinitely many solutions. For 10 points, name these sets of equations solved together."
        },
        {
            "p": "If every constant on the right side of one of these is 0, it is called homogeneous and always has the “trivial” solution, in which every unknown equals 0. Any one of these has no solution, exactly one solution, or infinitely many solutions, but never exactly two.",
            "r": "For 10 points, name these sets of equations, which can be solved by graphing their lines and finding where they cross."
        },
        {
            "p": "Applying Kirchhoff’s [“KEER-kofs”] laws to an electric circuit with several loops produces one of these, and balancing a chemical equation can be done by solving one. When one of these is written as A x equals b and matrix A has an inverse, its solution is that inverse times b.",
            "r": "For 10 points, name these sets of two or more equations, solved by graphing, substitution, or elimination."
        },
        {
            "p": "One of these is called overdetermined when it has more equations than unknowns. When such a case has no exact solution, the method of least squares, published by Adrien-Marie Legendre [“luh-ZHAHN-druh”] in 1805, finds the closest possible answer.",
            "r": "One of these with no solution at all is called inconsistent. For 10 points, name these groups of equations, whose solution is where their graphed lines intersect."
        },
        {
            "p": "The Jacobi [“yah-KOH-bee”] and Gauss–Seidel [“GOWSS ZY-dul”] methods solve large examples of these by starting with a guess and improving it over and over. Writing a square matrix as a lower triangular matrix times an upper triangular one, called LU decomposition, speeds up solving many of these that share the same coefficients.",
            "r": "Substitution solves one equation for one unknown and plugs the result into the others. For 10 points, name these groups of equations, such as y = 2x and x + y = 12."
        },
        {
            "p": "Wassily Leontief’s [“vah-SEE-lee lee-ON-tee-efs”] input–output model, which won the 1973 Nobel Prize in economics, finds how much each industry must produce by solving a giant one of these. Economists find the price at which supply equals demand by solving a small one of these.",
            "r": "For 10 points, name these sets of equations that share unknowns and must all be true at once."
        },
        {
            "p": "Gauss–Jordan elimination solves one of these by row-reducing a grid of its numbers until every unknown can be read off directly. When one of these has three unknowns, each equation describes a flat plane, and a single solution is the point where three planes meet.",
            "r": "For 10 points, name these sets of equations solved together, often by substitution or elimination."
        },
        {
            "p": "In the _Nine Chapters on the Mathematical Art_, red counting rods stood for positive numbers and black rods for negative numbers while solving these. Liu Hui [“lyoh HWAY”] explained that method in a commentary written in 263 CE, about 1,500 years before Carl Friedrich Gauss was born.",
            "r": "Graphing one shows where its lines cross. For 10 points, name these groups of equations, solved by substitution or elimination."
        },
        {
            "p": "One of these is called underdetermined if it has fewer equations than unknowns, and such a case can never have exactly one solution. A company’s break-even point, where its cost line meets its revenue line, can be found by solving one of these.",
            "r": "Subtracting 2x − y = 1 from 2x + 3y = 13 leaves 4y = 12. For 10 points, name these sets of equations that must all be true at once."
        },
        {
            "p": "Gaussian elimination turns one of these into a staircase-shaped “row echelon form,” and then back substitution finds the unknowns one at a time, starting from the bottom row. If elimination produces a false statement such as 0 = 5, there is no solution.",
            "r": "For 10 points, name these sets of equations whose graphed lines cross at the solution, unless the lines are parallel."
        }
    ],
    "clues": [
        {
            "id": "definition",
            "tier": "giveaway",
            "t": "Two or more equations with the same unknowns that must all be true at the same time",
            "k": ["same unknowns", "true at the same time", "two or more"],
            "n": 0
        },
        {
            "id": "lines-cross",
            "tier": "giveaway",
            "t": "Graph each equation as a line: the solution is the point where the lines cross",
            "k": ["lines cross", "graph", "point"],
            "n": 0
        },
        {
            "id": "methods",
            "tier": "giveaway",
            "t": "Solved by three classroom methods: graphing, substitution, and elimination",
            "k": ["graphing", "substitution", "elimination"],
            "n": 0
        },
        {
            "id": "example",
            "tier": "giveaway",
            "t": "Example: x + y = 10 and x − y = 4; adding them gives 2x = 14, so x = 7 and y = 3",
            "k": ["adding", "2x = 14", "x = 7"],
            "n": 0
        },
        {
            "id": "parallel",
            "tier": "middle",
            "t": "Parallel lines (same slope, different y-intercepts) never cross, so that pair has no solution and is called inconsistent",
            "k": ["parallel", "no solution", "inconsistent"],
            "n": 0
        },
        {
            "id": "same-line",
            "tier": "middle",
            "t": "If both equations describe the same line, there are infinitely many solutions",
            "k": ["same line", "infinitely many"],
            "n": 0
        },
        {
            "id": "never-two",
            "tier": "middle",
            "t": "It always has no solution, exactly one, or infinitely many, but never exactly two",
            "k": ["never exactly two", "exactly one"],
            "n": 0
        },
        {
            "id": "substitution",
            "tier": "middle",
            "t": "Substitution: solve one equation for one unknown and plug it into the other; y = 2x and x + y = 12 give x = 4, y = 8",
            "k": ["substitution", "plug"],
            "n": 0
        },
        {
            "id": "elimination",
            "tier": "middle",
            "t": "Elimination: add or subtract the equations to cancel an unknown; 2x + 3y = 13 minus 2x − y = 1 leaves 4y = 12",
            "k": ["elimination", "cancel", "4y = 12"],
            "n": 0
        },
        {
            "id": "false-statement",
            "tier": "middle",
            "t": "If elimination produces a false statement like 0 = 5, there is no solution; 0 = 0 means infinitely many",
            "k": ["false statement", "0 = 5", "0 = 0"],
            "n": 0
        },
        {
            "id": "gaussian",
            "tier": "middle",
            "t": "Gaussian elimination (for Carl Friedrich Gauss) row-reduces to row echelon form, then uses back substitution; Gauss–Jordan elimination goes on to reduced row echelon form",
            "k": ["gaussian elimination", "row echelon", "back substitution"],
            "n": 0,
            "rabbit": "Carl Friedrich Gauss"
        },
        {
            "id": "matrix-form",
            "tier": "middle",
            "t": "Written in matrix form as Ax = b; if A has an inverse, x = A⁻¹b. The augmented matrix adds the column of constants",
            "k": ["augmented matrix", "inverse", "ax = b"],
            "n": 0,
            "rabbit": "Matrices"
        },
        {
            "id": "three-planes",
            "tier": "middle",
            "t": "With three unknowns, each equation is a flat plane, and a single solution is the point where three planes meet",
            "k": ["three planes", "plane", "three unknowns"],
            "n": 0
        },
        {
            "id": "nine-chapters",
            "tier": "power",
            "t": "China’s _Nine Chapters on the Mathematical Art_ (about 2,000 years old) solved them with counting rods on a board, the same idea as Gaussian elimination",
            "k": ["nine chapters", "counting rods", "board"],
            "n": 0
        },
        {
            "id": "fangcheng",
            "tier": "power",
            "t": "Its eighth chapter, “Fangcheng” (the modern Chinese word for “equation”), opens with a problem about bundles of three grades of grain",
            "k": ["fangcheng", "eighth chapter", "grain"],
            "n": 0
        },
        {
            "id": "red-black-rods",
            "tier": "power",
            "t": "In the _Nine Chapters_ method, red rods stood for positive numbers and black rods for negative ones; Liu Hui explained it in a commentary in 263 CE",
            "k": ["red rods", "black rods", "liu hui", "263"],
            "n": 0,
            "rabbit": "Negative numbers"
        },
        {
            "id": "pheasants-rabbits",
            "tier": "power",
            "t": "Puzzle from the ancient Chinese _Sunzi Suanjing_: 35 heads and 94 feet in one cage means 23 pheasants and 12 rabbits",
            "k": ["pheasants", "rabbits", "94 feet", "sunzi"],
            "n": 0
        },
        {
            "id": "cramer",
            "tier": "power",
            "t": "Cramer’s rule (Gabriel Cramer of Geneva, 1750) finds each unknown as a ratio of two determinants; it needs a determinant that is not zero",
            "k": ["cramer", "1750", "geneva", "determinants"],
            "n": 0,
            "rabbit": "Determinant"
        },
        {
            "id": "seki-leibniz",
            "tier": "power",
            "t": "Seki Takakazu in Japan and Gottfried Leibniz in Germany each discovered determinants in the late 1600s while studying them",
            "k": ["seki", "leibniz", "late 1600s"],
            "n": 0
        },
        {
            "id": "rouche-capelli",
            "tier": "power",
            "t": "Rouché–Capelli theorem: a solution exists exactly when the coefficient matrix and the augmented matrix have the same rank",
            "k": ["rouché–capelli", "same rank", "rank"],
            "n": 0
        },
        {
            "id": "homogeneous",
            "tier": "power",
            "t": "A homogeneous one has every constant equal to 0, so it always has the “trivial” solution with every unknown equal to 0",
            "k": ["homogeneous", "trivial"],
            "n": 0
        },
        {
            "id": "least-squares",
            "tier": "power",
            "t": "Overdetermined ones have more equations than unknowns (Legendre’s least squares, 1805, finds the closest answer); underdetermined ones have fewer and never exactly one solution",
            "k": ["overdetermined", "underdetermined", "least squares", "legendre"],
            "n": 0
        },
        {
            "id": "iterative",
            "tier": "power",
            "t": "The Jacobi and Gauss–Seidel methods solve big ones by improving a guess over and over; LU decomposition (lower × upper triangular) speeds up solving many that share coefficients",
            "k": ["jacobi", "gauss–seidel", "lu decomposition", "guess"],
            "n": 0
        },
        {
            "id": "linpack",
            "tier": "power",
            "t": "The TOP500 list ranks supercomputers by how fast they solve one gigantic one (the LINPACK benchmark)",
            "k": ["top500", "linpack", "supercomputers"],
            "n": 0
        },
        {
            "id": "kirchhoff-chemistry",
            "tier": "power",
            "t": "Kirchhoff’s laws for electric circuits and balancing chemical equations both lead to them",
            "k": ["kirchhoff", "circuits", "chemical"],
            "n": 0
        },
        {
            "id": "leontief",
            "tier": "power",
            "t": "Wassily Leontief’s input–output model (1973 economics Nobel) solves a giant one to find how much each industry must produce",
            "k": ["leontief", "input–output", "industry"],
            "n": 0
        },
        {
            "id": "break-even",
            "tier": "power",
            "t": "A company’s break-even point (where the cost line meets the revenue line) and a market’s supply-and-demand price both come from solving one",
            "k": ["break-even", "revenue", "supply"],
            "n": 0
        }
    ],
    "trap": {
        "title": "System, matrix, or inequality?",
        "body": "Many clues for this answer line, like Gaussian elimination, Cramer’s rule, and augmented matrices, also show up in tossups on matrices and determinants, which are different answer lines. Systems of inequalities, whose solutions are shaded regions instead of points, are a different answer line too. Saying only “linear equations” or “system of equations” earns a prompt, so be ready to say the whole thing.",
        "fix": "Listen for the noun. “These sets of equations” or “these groups of equations solved together” means systems of linear equations; “these arrays of numbers” means matrices; “this number computed from a square matrix” means the determinant. Clues about shading or “greater than” point to inequalities.",
        "line": "Real answer line: <b><u>system</u></b>s of <b><u>linear equation</u></b>s (accept <u>linear system</u>s or <u>simultaneous linear equations</u>; prompt on <u>system of equations</u> or <u>linear equations</u>; do not accept “matrices”)"
    }
}

with open("topics/systems-of-linear-equations.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote topics/systems-of-linear-equations.json")
