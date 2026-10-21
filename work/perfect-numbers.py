import json

data = {
    "id": "perfect-numbers",
    "name": "Perfect numbers",
    "mono": "28",
    "category": "Math",
    "qbCategory": "Science · Other Science (Math)",
    "kicker": "Equal to the sum of their proper divisors · The smallest are 6 and 28",
    "dates": "Euclid’s recipe for even ones, c. 300 BCE",
    "briefing": "A perfect number equals the sum of its proper divisors, the numbers that divide it evenly other than itself: 6 = 1 + 2 + 3, and 28 = 1 + 2 + 4 + 7 + 14. The ancient Greeks knew the first four, 6, 28, 496, and 8,128, and Euclid showed how to build them from special primes now named for Marin Mersenne. Every perfect number ever found is even, and nobody knows whether an odd one exists.",
    "answerHtml": "<b><u>perfect number</u></b>s (prompt on <u>perfect</u>; do not accept “prime numbers,” “Mersenne primes,” or “perfect squares”)",
    "accept": [
        "perfect numbers",
        "perfect number",
        "even perfect numbers",
        "even perfect number"
    ],
    "prompt": [
        "perfect"
    ],
    "reject": [
        "prime numbers",
        "prime number",
        "primes",
        "mersenne primes",
        "mersenne prime",
        "mersenne numbers",
        "mersenne number",
        "perfect squares",
        "perfect square",
        "perfect cubes",
        "perfect cube",
        "perfect powers",
        "perfect power",
        "odd perfect numbers",
        "odd perfect number",
        "multiply perfect numbers",
        "multiperfect numbers",
        "abundant numbers",
        "abundant number",
        "deficient numbers",
        "deficient number",
        "amicable numbers",
        "amicable number",
        "amicable pairs",
        "sociable numbers",
        "triangular numbers",
        "triangular number",
        "hexagonal numbers",
        "composite numbers",
        "even numbers",
        "even number",
        "factors",
        "divisors",
        "6",
        "six",
        "28",
        "twenty eight",
        "496",
        "8128"
    ],
    "tests": {
        "right": [
            "perfect numbers",
            "Perfect number",
            "even perfect numbers",
            "perfct numbers",
            "perfect nubmers"
        ],
        "prompt": [
            "perfect"
        ],
        "wrong": [
            "prime numbers",
            "Mersenne primes",
            "perfect squares",
            "amicable numbers",
            "abundant numbers",
            "triangular numbers",
            "odd perfect numbers"
        ]
    },
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Perfect_number",
    "qb": {
        "q": "perfect number",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Nicomachus [“nih-KOM-uh-kus”] of Gerasa listed the first four of these numbers around 100 CE and contrasted them with “deficient” and “abundant” numbers. A number is abundant if its smaller divisors add up to more than the number itself, as happens with 12.",
            "r": "For 10 points, name these numbers, such as 6 and 28, that equal the sum of their proper divisors."
        },
        {
            "p": "In Book IX of his _Elements_, Euclid showed how to build one of these numbers from any prime that is one less than a power of 2, as when 31 gives 496, which is 16 times 31. Leonhard Euler [“OY-ler”] later proved that every even one of these numbers comes from Euclid’s recipe.",
            "r": "Ancient Greeks knew four of them. For 10 points, name these numbers, like 6, that equal the sum of their proper divisors."
        },
        {
            "p": "Saint Augustine argued in _The City of God_ that the number of days of creation was chosen because that number is one of these, not the other way around. Every even one of these numbers ends in the digit 6 or 8.",
            "r": "For 10 points, name these numbers, like 28, that equal the sum of their proper divisors."
        },
        {
            "p": "Written in binary, every even one of these numbers is a string of 1s followed by a string of 0s, such as 111110000. Every even one after the first equals a sum of consecutive odd cubes, starting with 1 cubed plus 3 cubed.",
            "r": "For 10 points, name these numbers, including 6, 28, and 496, that equal the sum of their proper divisors."
        },
        {
            "p": "Every even one of these numbers is also a triangular number; the third one, for example, is the sum of all the whole numbers from 1 to 31. The fourth of these numbers, 8,128, equals 64 times the prime number 127.",
            "r": "For 10 points, name these numbers, the smallest of which is 6, that equal the sum of their proper divisors."
        },
        {
            "p": "Nobody knows whether any odd numbers belong to this class, and in 2012 researchers showed that an odd one would have to be larger than 10 to the 1500th power. That makes the existence of an odd example one of the oldest unsolved problems in mathematics.",
            "r": "For 10 points, name these numbers, like 6 and 28, that equal the sum of their proper divisors."
        },
        {
            "p": "Each new prime found by the volunteer GIMPS project, such as a record-setting one discovered in 2024, also produces a new even one of these numbers. Those primes, which have the form 2 to the n, minus 1, are named for the French friar Marin Mersenne [“mair-SEN”].",
            "r": "For 10 points, name these numbers, such as 6 and 28, which equal the sum of all their divisors except themselves."
        },
        {
            "p": "In Yoko Ogawa’s novel _The Housekeeper and the Professor_, a math professor treasures the uniform number of the baseball pitcher Yutaka Enatsu [“eh-NAHT-soo”] because it is one of these numbers. That novel also features amicable pairs, such as 220 and 284, in which each number’s proper divisors add up to the other.",
            "r": "Enatsu’s number was 28. For 10 points, name these numbers, such as 6, that equal the sum of their proper divisors."
        },
        {
            "p": "For each of these numbers, the reciprocals of all its divisors, including the number itself, add up to exactly 2. Equivalently, adding up all the divisors of one of these numbers, including itself, gives exactly twice the number.",
            "r": "For 10 points, name these numbers, like 28, that equal the sum of their proper divisors."
        },
        {
            "p": "If you keep adding up the digits of any even one of these numbers except the smallest, you always end up at 1; for example, 496 gives 19, then 10, then 1. The fifth of these numbers is 33,550,336.",
            "r": "For 10 points, name these numbers, whose smallest example, 6, equals 1 plus 2 plus 3."
        },
        {
            "p": "Numbers such as 120, whose divisors add up to exactly three times the number, are a generalization of these numbers. Searches for new examples of these numbers use the Lucas–Lehmer test to check whether a number of the form 2 to the p, minus 1, is prime.",
            "r": "For 10 points, name these numbers, like 6 and 28, that equal the sum of their proper divisors."
        },
        {
            "p": "Euclid’s recipe for these numbers needs a prime of the form 2 to the p, minus 1, and p itself must be prime, but that is not enough: 2 to the 11th power, minus 1, is 2,047, which equals 23 times 89.",
            "r": "The four smallest of these numbers are 6, 28, 496, and 8,128. For 10 points, name these numbers that equal the sum of their proper divisors."
        },
        {
            "p": "The fourth of these numbers, 8,128, equals 64 times the prime 127, and the third, 496, equals 16 times the prime 31. Each even one of these numbers has exactly one odd prime factor.",
            "r": "For 10 points, name these numbers, like 6 and 28, that equal the sum of the numbers that divide them, not counting themselves."
        },
        {
            "p": "Book VII of Euclid’s _Elements_ defines one of these as a number that is “equal to its own parts.” Every known example of these numbers is even, and each comes from a prime that is one less than a power of 2.",
            "r": "For 10 points, name these numbers, such as 28, which equals 1 plus 2 plus 4 plus 7 plus 14."
        },
        {
            "p": "Ancient writers wrongly guessed that the nth of these numbers always has exactly n digits, but the fifth one, 33,550,336, has eight. They also wrongly guessed that these numbers take turns ending in 6 and 8, but the fifth and sixth both end in 6.",
            "r": "Each equals the sum of its proper divisors. For 10 points, name these numbers, the first two of which are 6 and 28."
        }
    ],
    "clues": [
        {
            "id": "definition",
            "tier": "giveaway",
            "t": "A number equal to the sum of its proper divisors (all of its divisors except itself)",
            "k": ["sum", "proper divisors", "except itself"],
            "n": 0
        },
        {
            "id": "six",
            "tier": "giveaway",
            "t": "The smallest one is 6, because 1 + 2 + 3 = 6",
            "k": ["smallest", "1 + 2 + 3"],
            "n": 0
        },
        {
            "id": "twenty-eight",
            "tier": "giveaway",
            "t": "The second one is 28 = 1 + 2 + 4 + 7 + 14",
            "k": ["second", "28"],
            "n": 0
        },
        {
            "id": "first-four",
            "tier": "middle",
            "t": "The first four, 6, 28, 496, and 8,128, were known to the ancient Greeks",
            "k": ["first four", "496", "8,128", "ancient greeks"],
            "n": 0
        },
        {
            "id": "euclid",
            "tier": "middle",
            "t": "Book IX of Euclid’s _Elements_ shows how to build one from a prime that is one less than a power of 2: 31 gives 496 = 16 × 31",
            "k": ["euclid", "book ix", "power of 2"],
            "n": 0,
            "rabbit": "Euclid"
        },
        {
            "id": "euler",
            "tier": "middle",
            "t": "Leonhard Euler proved that every even one comes from Euclid’s recipe (the Euclid–Euler theorem)",
            "k": ["euler", "euclid–euler"],
            "n": 0,
            "rabbit": "Leonhard Euler"
        },
        {
            "id": "mersenne",
            "tier": "middle",
            "t": "Each Mersenne prime (2ⁿ − 1, named for the friar Marin Mersenne) gives exactly one even one; the GIMPS project found a record Mersenne prime in 2024",
            "k": ["mersenne", "gimps", "2024"],
            "n": 0,
            "rabbit": "Prime numbers"
        },
        {
            "id": "odd-unknown",
            "tier": "middle",
            "t": "No odd one is known, and whether one exists is one of the oldest unsolved problems in math",
            "k": ["odd", "unsolved"],
            "n": 0
        },
        {
            "id": "ends-6-8",
            "tier": "middle",
            "t": "Every even one ends in the digit 6 or 8",
            "k": ["digit 6 or 8", "ends"],
            "n": 0
        },
        {
            "id": "abundant-deficient",
            "tier": "middle",
            "t": "If a number’s proper divisors add up to more than it, it is abundant (12 is the smallest); if less, it is deficient (like 8, or any prime)",
            "k": ["abundant", "deficient", "12"],
            "n": 0
        },
        {
            "id": "nicomachus",
            "tier": "middle",
            "t": "Nicomachus of Gerasa listed the first four around 100 CE and contrasted them with abundant and deficient numbers",
            "k": ["nicomachus", "gerasa", "100 ce"],
            "n": 0
        },
        {
            "id": "augustine",
            "tier": "middle",
            "t": "Saint Augustine’s _The City of God_ says the six days of creation were chosen because 6 has this property, not the other way around",
            "k": ["augustine", "city of god", "creation"],
            "n": 0
        },
        {
            "id": "binary",
            "tier": "power",
            "t": "In binary, every even one is a run of 1s followed by 0s: 6 is 110, 28 is 11100, and 496 is 111110000",
            "k": ["binary", "111110000", "11100"],
            "n": 0,
            "rabbit": "Binary numbers"
        },
        {
            "id": "triangular",
            "tier": "power",
            "t": "Every even one is a triangular number: 496 is the sum of the whole numbers 1 through 31",
            "k": ["triangular", "1 through 31"],
            "n": 0
        },
        {
            "id": "odd-cubes",
            "tier": "power",
            "t": "Every even one after 6 is a sum of consecutive odd cubes, like 28 = 1³ + 3³",
            "k": ["odd cubes", "consecutive"],
            "n": 0
        },
        {
            "id": "reciprocals",
            "tier": "power",
            "t": "The reciprocals of all its divisors add up to 2, and all its divisors, including itself, add up to twice the number",
            "k": ["reciprocals", "twice"],
            "n": 0
        },
        {
            "id": "odd-bound",
            "tier": "power",
            "t": "In 2012, researchers showed that an odd one would have to be larger than 10 to the 1500th power",
            "k": ["2012", "1500th power"],
            "n": 0
        },
        {
            "id": "ogawa",
            "tier": "power",
            "t": "In Yoko Ogawa’s novel _The Housekeeper and the Professor_, the professor treasures pitcher Yutaka Enatsu’s uniform number, 28",
            "k": ["ogawa", "enatsu", "housekeeper"],
            "n": 0
        },
        {
            "id": "fifth",
            "tier": "power",
            "t": "The fifth one is 33,550,336, which is 4,096 × 8,191",
            "k": ["fifth", "33,550,336"],
            "n": 0
        },
        {
            "id": "digit-sum",
            "tier": "power",
            "t": "Repeatedly adding the digits of any even one except 6 ends at 1: 496 gives 19, then 10, then 1",
            "k": ["repeatedly", "digits"],
            "n": 0
        },
        {
            "id": "generalization",
            "tier": "power",
            "t": "Numbers like 120, whose divisors add up to three times the number, are a generalization of them",
            "k": ["120", "three times", "generalization"],
            "n": 0
        },
        {
            "id": "lucas-lehmer",
            "tier": "power",
            "t": "The Lucas–Lehmer test checks whether 2ᵖ − 1 is prime, so searches use it to find new ones",
            "k": ["lucas–lehmer", "test"],
            "n": 0
        },
        {
            "id": "exponent",
            "tier": "power",
            "t": "The exponent p must be prime, but that is not enough: 2¹¹ − 1 = 2,047 = 23 × 89",
            "k": ["exponent", "2,047"],
            "n": 0
        },
        {
            "id": "own-parts",
            "tier": "power",
            "t": "Book VII of Euclid’s _Elements_ defines one as a number “equal to its own parts”",
            "k": ["book vii", "own parts"],
            "n": 0
        },
        {
            "id": "wrong-guesses",
            "tier": "power",
            "t": "Ancient writers wrongly guessed that the nth one has n digits and that they take turns ending in 6 and 8",
            "k": ["wrongly guessed", "take turns"],
            "n": 0
        },
        {
            "id": "odd-prime-factor",
            "tier": "power",
            "t": "Each even one has exactly one odd prime factor: 8,128 = 64 × 127",
            "k": ["odd prime factor", "127"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Perfect or prime?",
        "body": "Perfect numbers are built from Mersenne primes, so tossups about them mention primes of the form 2ⁿ − 1, Euclid, Euler, and Marin Mersenne, and each of those can be its own answer line. A perfect number itself is never prime. Don’t confuse perfect numbers with perfect squares (like 25), or with abundant, deficient, or amicable numbers, which compare a number with its divisors in other ways.",
        "fix": "If the clues say a number equals the sum of its proper divisors, or name 6, 28, 496, or 8,128, say “perfect numbers.” If they only describe primes of the form 2ⁿ − 1, the answer may be Mersenne primes. Saying only “perfect” earns a prompt.",
        "line": "Real answer line: <b><u>perfect number</u></b>s (prompt on <u>perfect</u>; do not accept “prime numbers,” “Mersenne primes,” or “perfect squares”)"
    }
}

with open("topics/perfect-numbers.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote topics/perfect-numbers.json")
