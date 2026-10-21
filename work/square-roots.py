import json

data = {
    "id": "square-roots",
    "name": "Square roots",
    "mono": "SQR",
    "category": "Math",
    "qbCategory": "Science · Other Science (Math)",
    "kicker": "The number that, times itself, gives x · Written with a radical sign",
    "dates": "Radical sign first printed by Christoph Rudolff, 1525",
    "briefing": "A square root of a number is a value that, multiplied by itself, gives that number: 5 is a square root of 25 because 5 × 5 = 25. Square roots are written with the radical sign, √, and every positive number actually has two of them, like 5 and −5. Some square roots, such as √2 ≈ 1.414, can never be written as fractions, a discovery credited to the followers of Pythagoras.",
    "answerHtml": "<b><u>square root</u></b>s (accept <u>principal square root</u>s; prompt on <u>root</u>s or <u>radical</u>s; do not accept “cube roots” or a specific value such as “the square root of 2”)",
    "accept": [
        "square root",
        "square roots",
        "principal square root",
        "principal square roots",
        "sqrt",
        "square rooting",
        "square root function",
        "square root operation"
    ],
    "prompt": [
        "root",
        "roots",
        "radical",
        "radicals",
        "radical sign",
        "radical symbol",
        "radix"
    ],
    "reject": [
        "cube root",
        "cube roots",
        "cubic root",
        "fourth root",
        "fourth roots",
        "nth root",
        "nth roots",
        "square root of 2",
        "square root of two",
        "square root of 3",
        "square root of three",
        "square root of negative one",
        "square root of negative 1",
        "square root of minus one",
        "square root of minus 1",
        "root mean square",
        "square foot",
        "square feet",
        "squares",
        "squaring",
        "perfect square",
        "perfect squares",
        "square number",
        "square numbers",
        "exponent",
        "exponents",
        "powers",
        "logarithm",
        "logarithms",
        "radicand",
        "i",
        "imaginary unit",
        "imaginary number",
        "imaginary numbers",
        "irrational number",
        "irrational numbers",
        "babylonian method",
        "herons method",
        "newtons method",
        "pythagorean theorem",
        "pythagoras constant",
        "golden ratio",
        "quadratic formula",
        "discriminant",
        "absolute value",
        "standard deviation",
        "variance",
        "roots of unity",
        "root of unity"
    ],
    "tests": {
        "right": [
            "square root",
            "Square roots",
            "principal square root",
            "sqaure root",
            "sqrt"
        ],
        "prompt": [
            "root",
            "radical"
        ],
        "wrong": [
            "cube root",
            "square root of 2",
            "squares",
            "exponents",
            "imaginary unit",
            "square foot"
        ]
    },
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Square_root",
    "qb": {
        "q": "square root",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "The Babylonian clay tablet YBC 7289 shows a square with its diagonals drawn in, along with a base-60 value for this function of 2 that is correct to about six digits. The tablet relies on the fact that the diagonal of a square is this function of 2 times as long as a side.",
            "r": "That value for 2 is about 1.414. For 10 points, name this operation that undoes squaring a number."
        },
        {
            "p": "Christoph Rudolff’s 1525 algebra book is credited with the first printed use of the symbol for this operation, which probably grew out of a lowercase r for the Latin word radix. René Descartes [“day-KART”] later added a bar over the top of that symbol to show which numbers fall under it.",
            "r": "For 10 points, name this operation, written with a radical sign, which gives 7 for the number 49."
        },
        {
            "p": "Plato’s dialogue _Theaetetus_ [“thee-ee-TEE-tus”] says that Theodorus of Cyrene [“sy-REE-nee”] proved that this function of 3, of 5, and of several other whole numbers up to 17 is irrational. A spiral named for Theodorus is built from right triangles whose longest sides equal this function of 2, 3, 4, and so on.",
            "r": "Perfect squares such as 25 have whole-number values. For 10 points, name this operation, which gives 5 for 25."
        },
        {
            "p": "Heron of Alexandria described a way to approximate this function: make a guess, average it with the original number divided by the guess, and repeat. That method, also named for the Babylonians, is a special case of Isaac Newton’s method for finding where a curve crosses zero.",
            "r": "For 10 points, name this operation, the opposite of squaring, which gives 9 for the number 81."
        },
        {
            "p": "Tradition credits Hippasus [“HIP-uh-sus”], a follower of Pythagoras, with discovering that this function of 2 cannot be written as a fraction. A classic proof assumes that it can, then shows that the top and bottom of that fraction would both have to be even numbers, which is impossible in lowest terms.",
            "r": "That value is about 1.414. For 10 points, name this operation, which gives 6 for the number 36."
        },
        {
            "p": "Sheets of A4 paper are this function of 2 times as long as they are wide, so cutting one in half makes two smaller sheets with exactly the same shape. That ratio, about 1.414, means each size in the series has exactly half the area of the one before it.",
            "r": "For 10 points, name this operation, written with a radical sign, which gives 4 for the number 16."
        },
        {
            "p": "The golden ratio equals 1 plus this function of 5, all divided by 2. In the quadratic formula, this function is applied to the discriminant, b squared minus 4ac, so a negative discriminant means an equation has no real solutions.",
            "r": "It undoes squaring. For 10 points, name this operation, which gives 10 for the number 100."
        },
        {
            "p": "Gerolamo Cardano [“kar-DAH-noh”] ran into this operation applied to negative numbers while solving cubic equations in his 1545 book _Ars Magna_. Leonhard Euler [“OY-ler”] later introduced the letter i for this function of negative 1, and René Descartes had called such numbers “imaginary.”",
            "r": "It is the opposite of squaring. For 10 points, name this operation, which gives 3 for the number 9."
        },
        {
            "p": "A math holiday named for this operation falls on dates such as May 5, 2025, when the month and the day both equal this function of the year’s last two digits. The next such holiday after that falls on June 6, 2036.",
            "r": "It undoes squaring a number. For 10 points, name this operation, which gives 8 for the number 64."
        },
        {
            "p": "For small swings, the time a pendulum takes to swing back and forth equals 2 pi times this function of the pendulum’s length divided by the strength of gravity. In statistics, the standard deviation of a set of data is this function of the variance.",
            "r": "Every positive number has two such values, one positive and one negative. For 10 points, name this operation that undoes squaring."
        },
        {
            "p": "The ancient Indian Baudhayana [“bow-DHAH-yuh-nuh”] Shulba Sutra gives an approximation of this function of 2 that equals 577 over 408. Ancient Chinese mathematicians described a step-by-step method for this operation in _The Nine Chapters on the Mathematical Art_.",
            "r": "It undoes squaring. For 10 points, name this operation, written with a radical sign, which gives 12 for 144."
        },
        {
            "p": "This operation makes any number between 0 and 1 larger, turning one-fourth into one-half. Its graph begins at the origin and looks like the top half of a parabola lying on its side.",
            "r": "Positive numbers have two of these values, like 11 and negative 11 for 121. For 10 points, name this operation."
        },
        {
            "p": "The number written under this operation’s symbol is called the radicand, from a Latin word that also gives English the word “radish.” This operation is the same as raising a number to the one-half power.",
            "r": "For 10 points, name this operation, which gives 2 for the number 4 and is the opposite of squaring."
        },
        {
            "p": "To simplify this function of 50, you can rewrite it as 5 times this function of 2, because 50 equals 25 times 2. For numbers that are not negative, this function of a product equals the product of this function applied to each factor.",
            "r": "Among whole numbers, it gives whole-number results only for perfect squares like 49. For 10 points, name this operation."
        },
        {
            "p": "The distance formula on a coordinate grid applies this operation to the sum of the squares of the differences between two points’ x- and y-coordinates. By the Pythagorean theorem, a right triangle with legs of 1 and 2 has a hypotenuse equal to this function of 5.",
            "r": "It undoes squaring. For 10 points, name this operation, written with a radical sign, which gives 13 for 169."
        }
    ],
    "clues": [
        {
            "id": "definition",
            "tier": "giveaway",
            "t": "A number that, multiplied by itself, gives the original number: 5 for 25, since 5 × 5 = 25",
            "k": ["multiplied by itself", "original number"],
            "n": 0
        },
        {
            "id": "symbol",
            "tier": "giveaway",
            "t": "Written with the radical sign, a check-mark-shaped symbol",
            "k": ["radical sign", "check-mark"],
            "n": 0
        },
        {
            "id": "undo-squaring",
            "tier": "giveaway",
            "t": "The opposite, or inverse, of squaring a number",
            "k": ["squaring", "inverse", "opposite"],
            "n": 0
        },
        {
            "id": "two-values",
            "tier": "giveaway",
            "t": "Every positive number has two, one positive and one negative (7 and −7 for 49); the positive one is called the principal one",
            "k": ["principal", "positive and one negative"],
            "n": 0
        },
        {
            "id": "perfect-squares",
            "tier": "giveaway",
            "t": "Perfect squares like 1, 4, 9, 16, and 25 have whole-number ones",
            "k": ["perfect squares", "whole-number"],
            "n": 0
        },
        {
            "id": "two-irrational",
            "tier": "middle",
            "t": "The value for 2 is about 1.414 and is irrational (it cannot be written as a fraction); a square’s diagonal is that many times its side",
            "k": ["1.414", "irrational", "diagonal"],
            "n": 0,
            "rabbit": "Pythagorean theorem"
        },
        {
            "id": "hippasus",
            "tier": "middle",
            "t": "Tradition credits Hippasus, a follower of Pythagoras, with discovering that the value for 2 is irrational",
            "k": ["hippasus", "pythagoras"],
            "n": 0
        },
        {
            "id": "proof",
            "tier": "middle",
            "t": "Classic proof by contradiction: if the value for 2 were a fraction in lowest terms, its top and bottom would both have to be even",
            "k": ["contradiction", "lowest terms", "even"],
            "n": 0
        },
        {
            "id": "imaginary",
            "tier": "middle",
            "t": "Euler’s letter i stands for this value of −1; Cardano met such values of negative numbers in _Ars Magna_ (1545)",
            "k": ["euler", "cardano", "ars magna", "1545"],
            "n": 0,
            "rabbit": "Complex numbers"
        },
        {
            "id": "quadratic",
            "tier": "middle",
            "t": "In the quadratic formula it is taken of the discriminant, b² − 4ac; a negative discriminant means no real solutions",
            "k": ["quadratic formula", "discriminant"],
            "n": 0
        },
        {
            "id": "golden-ratio",
            "tier": "middle",
            "t": "The golden ratio equals 1 plus this value of 5, all divided by 2 (about 1.618)",
            "k": ["golden ratio", "1.618"],
            "n": 0
        },
        {
            "id": "distance",
            "tier": "middle",
            "t": "The distance formula and the Pythagorean theorem use it: the hypotenuse is this value of a² + b²",
            "k": ["distance formula", "pythagorean theorem", "hypotenuse"],
            "n": 0
        },
        {
            "id": "half-power",
            "tier": "middle",
            "t": "The same as raising a number to the one-half power; it makes numbers between 0 and 1 bigger (one-fourth becomes one-half)",
            "k": ["one-half power", "between 0 and 1"],
            "n": 0
        },
        {
            "id": "ybc-7289",
            "tier": "power",
            "t": "The Babylonian tablet YBC 7289 shows a square with its diagonals and a base-60 value for 2 correct to about six digits",
            "k": ["ybc 7289", "babylonian", "base-60"],
            "n": 0
        },
        {
            "id": "heron",
            "tier": "power",
            "t": "Heron’s (or the Babylonian) method: average a guess with the number divided by the guess, and repeat; it is a case of Newton’s method",
            "k": ["heron", "average", "newton"],
            "n": 0
        },
        {
            "id": "rudolff",
            "tier": "power",
            "t": "Christoph Rudolff’s 1525 algebra book is credited with first printing its symbol, which probably grew out of a lowercase r for the Latin word radix",
            "k": ["rudolff", "1525", "radix"],
            "n": 0
        },
        {
            "id": "descartes",
            "tier": "power",
            "t": "René Descartes added the bar over the top of its symbol to show which numbers fall under it",
            "k": ["descartes", "bar"],
            "n": 0
        },
        {
            "id": "theodorus",
            "tier": "power",
            "t": "Plato’s _Theaetetus_ says Theodorus of Cyrene proved the values for 3, 5, and other non-square whole numbers up to 17 are irrational; the spiral of Theodorus uses them",
            "k": ["theodorus", "theaetetus", "spiral"],
            "n": 0
        },
        {
            "id": "a4-paper",
            "tier": "power",
            "t": "A4 paper is this value of 2 times as long as it is wide, so cutting a sheet in half keeps its shape",
            "k": ["a4 paper", "cutting", "shape"],
            "n": 0
        },
        {
            "id": "pendulum",
            "tier": "power",
            "t": "For small swings, a pendulum’s swing time is 2π times this value of (length ÷ gravity); a standard deviation is this value of the variance",
            "k": ["pendulum", "standard deviation", "variance"],
            "n": 0,
            "rabbit": "Standard deviation"
        },
        {
            "id": "holiday",
            "tier": "power",
            "t": "A math holiday named for it falls on dates like May 5, 2025 (5/5/25) and June 6, 2036 (6/6/36)",
            "k": ["holiday", "may 5, 2025", "june 6, 2036"],
            "n": 0
        },
        {
            "id": "baudhayana",
            "tier": "power",
            "t": "India’s Baudhayana Shulba Sutra approximates the value for 2 as 577/408; China’s _Nine Chapters_ gives a step-by-step method for finding it",
            "k": ["baudhayana", "577/408", "nine chapters"],
            "n": 0
        },
        {
            "id": "radicand",
            "tier": "power",
            "t": "The number under its symbol is the radicand, from a Latin word that also gives English the word “radish”",
            "k": ["radicand", "radish", "latin"],
            "n": 0
        },
        {
            "id": "simplify",
            "tier": "power",
            "t": "To simplify, split off perfect squares: this value of 50 equals 5 times this value of 2, because 50 = 25 × 2",
            "k": ["simplify", "50", "split off"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Square root or cube root?",
        "body": "Square roots undo squaring, but cube roots undo cubing (the cube root of 27 is 3), and nth roots undo any power; those are different answer lines. Some tossups want one famous value instead, like the square root of 2 (about 1.414) or the imaginary unit i, the square root of −1. Saying only “root” or “radical” earns a prompt.",
        "fix": "Listen for “times itself,” “undoes squaring,” the radical sign, or examples like 7 for 49: say “square root.” If the clues say “times itself three times” or give 3 for 27, say “cube root.” If every clue is about one number, such as 1.414 or i, name that number.",
        "line": "Real answer line: <b><u>square root</u></b>s (accept <u>principal square root</u>s; prompt on <u>root</u>s or <u>radical</u>s; do not accept “cube roots” or a specific value such as “the square root of 2”)"
    }
}

with open("topics/square-roots.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote topics/square-roots.json")
