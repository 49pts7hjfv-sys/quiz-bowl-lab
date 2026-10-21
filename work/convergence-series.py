import json

data = {
    "id": "convergence-series",
    "name": "Convergence (series)",
    "mono": "CNV",
    "category": "Math",
    "qbCategory": "Science · Other Science (Math)",
    "kicker": "When an endless sum settles on a finite total · 1/2 + 1/4 + 1/8 + … = 1",
    "dates": "Made rigorous by Augustin-Louis Cauchy, 1821",
    "briefing": "An infinite series is a sum that never ends, like 1/2 + 1/4 + 1/8 + 1/16 + …, and it converges if its running totals, called partial sums, close in on one finite number. That example converges to exactly 1, like walking halfway to a wall, then half the remaining distance, again and again. But some endless sums grow forever: in the 1300s, Nicole Oresme proved that 1 + 1/2 + 1/3 + 1/4 + … diverges, even though its terms shrink toward zero.",
    "answerHtml": "<b><u>convergence</u></b> (accept word forms such as <u>convergent</u> series or <u>converge</u>s; prompt on <u>limit</u>; do not accept “divergence”)",
    "accept": [
        "convergence",
        "convergences",
        "convergent",
        "converge",
        "converges",
        "converging",
        "converged",
        "convergent series",
        "convergence of series",
        "convergence of a series",
        "series convergence"
    ],
    "prompt": [
        "limit",
        "limits",
        "finite limit",
        "finite sum"
    ],
    "reject": [
        "divergence",
        "divergent",
        "diverge",
        "diverges",
        "diverging",
        "diverged",
        "divergent series",
        "non convergence",
        "non convergent",
        "nonconvergence",
        "nonconvergent",
        "not convergent",
        "taylor series",
        "power series",
        "geometric series",
        "harmonic series",
        "infinite series",
        "fourier series",
        "partial sum",
        "partial sums",
        "infinity",
        "zeno",
        "zeno of elea",
        "zenos paradox",
        "zenos paradoxes",
        "ratio test",
        "root test",
        "comparison test",
        "integral test",
        "asymptote",
        "asymptotes",
        "continuity"
    ],
    "tests": {
        "right": [
            "convergence",
            "convergent series",
            "converges",
            "convergance",
            "absolute convergence",
            "converge"
        ],
        "prompt": [
            "limit"
        ],
        "wrong": [
            "divergence",
            "diverges",
            "Taylor series",
            "harmonic series",
            "geometric series",
            "Zeno’s paradox"
        ]
    },
    "mediaPending": True,
    "media": [],
    "wiki": "https://en.wikipedia.org/wiki/Convergent_series",
    "qb": {
        "q": "convergence",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Bernhard Riemann showed that if a series has this property only conditionally, its terms can be rearranged to add up to any number at all. A series has this property absolutely if it still has it after every negative term is made positive.",
            "r": "Its opposite is divergence. For 10 points, name this property of an infinite series whose partial sums approach a finite limit."
        },
        {
            "p": "Guido Grandi’s series, 1 minus 1 plus 1 minus 1 and so on forever, lacks this property because its partial sums keep bouncing between 1 and 0. The terms of any series with this property must shrink toward zero, though that alone does not guarantee it.",
            "r": "For 10 points, name this property of infinite series whose running totals settle on one finite number, the opposite of divergence."
        },
        {
            "p": "In the 1300s, Nicole Oresme [“oh-REM”] grouped the terms of 1 plus one-half plus one-third plus one-fourth and so on into chunks that are each worth at least one-half, proving that this sum lacks this property. That sum is called the harmonic series.",
            "r": "For 10 points, name this property of an infinite series whose partial sums approach a finite limit, as with one-half plus one-fourth plus one-eighth and so on, which approaches 1."
        },
        {
            "p": "Archimedes found the area of a slice of a parabola using the sum 1 plus one-fourth plus one-sixteenth and so on, which has this property and totals four-thirds. The comparison test says a series of positive terms has this property if its terms are smaller than those of a series that does.",
            "r": "For 10 points, name this property of infinite series, such as one-half plus one-fourth plus one-eighth and so on, the opposite of divergence."
        },
        {
            "p": "Augustin-Louis Cauchy [“koh-SHEE”] gave a careful definition of this property in his 1821 textbook _Cours d’analyse_ [“KOOR dah-nah-LEEZ”]. His criterion says a series has this property exactly when its partial sums eventually stay as close to one another as anyone could demand.",
            "r": "For 10 points, name this property of an infinite series that adds up to a finite total, the opposite of divergence."
        },
        {
            "p": "Leonhard Euler showed that 1 plus one-fourth plus one-ninth plus one-sixteenth and so on, a sum with this property, totals pi squared over 6. More generally, the sum of 1 over n to the p has this property exactly when p is greater than 1.",
            "r": "For 10 points, name this property of an infinite series whose partial sums approach a finite limit, unlike the harmonic series."
        },
        {
            "p": "The ratio test checks a series for this property by dividing the size of each term by the size of the term before it; if those ratios approach a number less than 1, the series has this property. If they approach exactly 1, the test gives no answer.",
            "r": "One-half plus one-fourth plus one-eighth and so on has this property, adding up to 1. For 10 points, name this property of infinite series."
        },
        {
            "p": "The alternating harmonic series, 1 minus one-half plus one-third minus one-fourth and so on, has this property and adds up to the natural log of 2, but only conditionally. Removing its minus signs gives the harmonic series, which lacks this property.",
            "r": "For 10 points, name this property of an infinite series whose partial sums approach a finite number."
        },
        {
            "p": "The Indian mathematician Madhava found that 1 minus one-third plus one-fifth minus one-seventh and so on equals pi over 4, though that series approaches its total very slowly. Gottfried Leibniz [“LYBE-nits”] names a test for this property in series whose terms alternate in sign and steadily shrink toward zero.",
            "r": "A series with this property has partial sums that approach one finite number. For 10 points, name this property of infinite series, the opposite of divergence."
        },
        {
            "p": "Zeno of Elea argued that Achilles could never catch a tortoise, since Achilles must first reach where the tortoise was, then where it moved next, and so on forever. Modern math answers Zeno by showing that an endless sum of shrinking time intervals can still have this property and total a finite time.",
            "r": "One-half plus one-fourth plus one-eighth and so on has this property, adding up to 1. For 10 points, name this property of an infinite series whose partial sums approach a finite limit."
        },
        {
            "p": "The repeating decimal 0.999… can be written as nine-tenths plus nine-hundredths plus nine-thousandths and so on, a geometric series with this property whose total is exactly 1. Likewise, 0.333… is a series with this property that adds up to one-third.",
            "r": "Its opposite is divergence. For 10 points, name this property of infinite series whose partial sums approach a finite limit."
        },
        {
            "p": "A power series has this property only for values of x within a certain distance, called a radius, from its center, though the series for e to the x has this property for every value of x. At the edge of that radius, a series may or may not have this property.",
            "r": "Its opposite is divergence. For 10 points, name this property of infinite series whose partial sums approach a finite limit."
        },
        {
            "p": "The integral test decides this property for a series of positive, shrinking terms by comparing the series with the area under a curve. The nth-term test says that if a series’s terms do not shrink toward zero, the series cannot have this property.",
            "r": "For 10 points, name this property of an infinite series, such as one-half plus one-fourth plus one-eighth and so on, whose sum is finite."
        },
        {
            "p": "Adding the reciprocals of the factorials, 1 plus 1 plus one-half plus one-sixth plus one twenty-fourth and so on, gives a series with this property whose total is the number e, about 2.718. The ratio test confirms it, since each term divided by the one before it shrinks toward zero.",
            "r": "Geometric series have this property when their common ratio is between negative 1 and 1. For 10 points, name this property of infinite series, the opposite of divergence."
        },
        {
            "p": "The sum of one over 1 times 2, plus one over 2 times 3, plus one over 3 times 4, and so on has this property and adds up to exactly 1, because nearly all of its pieces cancel in a “telescoping” pattern.",
            "r": "Its opposite is called divergence. For 10 points, name this property of infinite series whose partial sums approach a finite limit."
        }
    ],
    "clues": [
        {
            "id": "definition",
            "tier": "giveaway",
            "t": "An infinite series has it when its partial sums (running totals) approach one finite number",
            "k": ["partial sums", "running totals", "finite number"],
            "n": 0
        },
        {
            "id": "opposite",
            "tier": "giveaway",
            "t": "Its opposite is divergence: the partial sums grow without bound or never settle down",
            "k": ["divergence", "without bound"],
            "n": 0
        },
        {
            "id": "halves",
            "tier": "giveaway",
            "t": "1/2 + 1/4 + 1/8 + 1/16 + … has it, adding up to exactly 1",
            "k": ["exactly 1", "1/2 + 1/4"],
            "n": 0
        },
        {
            "id": "geometric",
            "tier": "middle",
            "t": "A geometric series a + ar + ar² + … has it exactly when r is between −1 and 1; its sum is then a ÷ (1 − r)",
            "k": ["geometric series", "a ÷ (1 − r)"],
            "n": 0
        },
        {
            "id": "harmonic",
            "tier": "middle",
            "t": "The harmonic series 1 + 1/2 + 1/3 + 1/4 + … lacks it: its terms shrink to 0, but its sum grows forever",
            "k": ["harmonic series", "grows forever"],
            "n": 0
        },
        {
            "id": "oresme",
            "tier": "middle",
            "t": "Nicole Oresme proved in the 1300s that the harmonic series lacks it, by grouping its terms into chunks each worth at least 1/2",
            "k": ["oresme", "1300s", "at least 1/2"],
            "n": 0
        },
        {
            "id": "nth-term",
            "tier": "middle",
            "t": "Its terms must shrink toward 0, but that alone is not enough (the nth-term test)",
            "k": ["nth-term test", "shrink toward 0"],
            "n": 0
        },
        {
            "id": "zeno",
            "tier": "middle",
            "t": "Zeno’s paradox of Achilles and the tortoise is answered by an endless sum of shrinking time intervals that totals a finite time",
            "k": ["zeno", "achilles", "tortoise"],
            "n": 0
        },
        {
            "id": "decimal",
            "tier": "middle",
            "t": "The repeating decimal 0.999… = 9/10 + 9/100 + 9/1000 + … has it and equals exactly 1; 0.333… adds up to 1/3",
            "k": ["repeating decimal", "0.999"],
            "n": 0
        },
        {
            "id": "ratio-test",
            "tier": "middle",
            "t": "Ratio test: if each term’s size divided by the size of the one before approaches a number less than 1, the series has it; exactly 1 tells nothing",
            "k": ["ratio test", "less than 1"],
            "n": 0
        },
        {
            "id": "comparison-test",
            "tier": "middle",
            "t": "Comparison test: a series of positive terms has it if its terms are smaller than those of a series that has it",
            "k": ["comparison test", "positive terms"],
            "n": 0
        },
        {
            "id": "alternating-harmonic",
            "tier": "middle",
            "t": "The alternating harmonic series 1 − 1/2 + 1/3 − 1/4 + … has it, adding up to ln 2 (about 0.693), but only conditionally",
            "k": ["alternating", "ln 2", "conditionally"],
            "n": 0
        },
        {
            "id": "riemann",
            "tier": "power",
            "t": "Bernhard Riemann showed that a series having it only conditionally can be rearranged to add up to any number at all",
            "k": ["riemann", "rearranged"],
            "n": 0,
            "rabbit": "Bernhard Riemann"
        },
        {
            "id": "absolute",
            "tier": "power",
            "t": "A series has it absolutely if it still has it after every negative term is made positive",
            "k": ["absolutely", "negative term"],
            "n": 0
        },
        {
            "id": "grandi",
            "tier": "power",
            "t": "Grandi’s series 1 − 1 + 1 − 1 + … lacks it: its partial sums bounce between 1 and 0 forever",
            "k": ["grandi", "bounce"],
            "n": 0
        },
        {
            "id": "archimedes",
            "tier": "power",
            "t": "Archimedes found the area of a slice of a parabola using 1 + 1/4 + 1/16 + … = 4/3",
            "k": ["archimedes", "parabola", "4/3"],
            "n": 0
        },
        {
            "id": "cauchy",
            "tier": "power",
            "t": "Augustin-Louis Cauchy defined it carefully in his 1821 _Cours d’analyse_; his criterion: the partial sums eventually stay as close together as you like",
            "k": ["cauchy", "1821", "criterion"],
            "n": 0,
            "rabbit": "Augustin-Louis Cauchy"
        },
        {
            "id": "basel",
            "tier": "power",
            "t": "Basel problem: Leonhard Euler showed that 1 + 1/4 + 1/9 + 1/16 + … has it and equals π²/6",
            "k": ["basel problem", "π²/6"],
            "n": 0,
            "rabbit": "Leonhard Euler"
        },
        {
            "id": "p-series",
            "tier": "power",
            "t": "A p-series, 1 + 1/2ᵖ + 1/3ᵖ + …, has it exactly when p is greater than 1",
            "k": ["p-series", "greater than 1"],
            "n": 0
        },
        {
            "id": "madhava-leibniz",
            "tier": "power",
            "t": "Madhava found 1 − 1/3 + 1/5 − 1/7 + … = π/4; Leibniz’s test covers series whose terms alternate in sign and steadily shrink to 0",
            "k": ["madhava", "π/4", "leibniz"],
            "n": 0,
            "rabbit": "Pi"
        },
        {
            "id": "radius",
            "tier": "power",
            "t": "A power series has it only within a certain distance, its radius, from the center; the series for eˣ has it for every x",
            "k": ["radius", "power series", "every x"],
            "n": 0,
            "rabbit": "Taylor series"
        },
        {
            "id": "integral-test",
            "tier": "power",
            "t": "The integral test compares a series of positive, shrinking terms with the area under a curve",
            "k": ["integral test", "area under a curve"],
            "n": 0,
            "rabbit": "Integrals"
        },
        {
            "id": "factorials",
            "tier": "power",
            "t": "Adding the reciprocals of the factorials, 1 + 1 + 1/2 + 1/6 + 1/24 + …, gives a series that has it and totals e, about 2.718",
            "k": ["factorials", "2.718"],
            "n": 0,
            "rabbit": "Factorial"
        },
        {
            "id": "telescoping",
            "tier": "power",
            "t": "1/(1×2) + 1/(2×3) + 1/(3×4) + … has it and totals exactly 1, because its pieces cancel in a “telescoping” pattern",
            "k": ["telescoping", "cancel"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Settles down or blows up?",
        "body": "Convergence and divergence are opposites that share many clues, like the harmonic series (which diverges) and geometric series (which converge when the ratio is between −1 and 1). A tossup describing a series that “grows without bound” or “never settles down” wants divergence. Other tossups want one specific series, such as a Taylor series or the harmonic series, as the answer.",
        "fix": "Ask whether the partial sums approach one finite number: if yes, say “convergence”; if they grow forever or keep bouncing around, say “divergence.” Saying just “limit” earns a prompt, because convergence means the partial sums have a finite limit.",
        "line": "Real answer line: <b><u>convergence</u></b> (accept word forms such as <u>convergent</u> series or <u>converge</u>s; prompt on <u>limit</u>; do not accept “divergence”)"
    }
}

with open("topics/convergence-series.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote topics/convergence-series.json")
