import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "ph",
    "name": "pH",
    "mono": "PH7",
    "category": "Chemistry",
    "qbCategory": "Science · Chemistry",
    "kicker": "How acidic or basic a solution is · Neutral is 7, like pure water",
    "dates": "Introduced by Søren Sørensen, 1909",
    "briefing": "pH is the number chemists use to say how acidic or basic a solution is: 7 is neutral, like pure water, lower numbers are acidic, like lemon juice at about 2, and higher numbers are basic, like bleach. Each step on the scale means ten times more or fewer hydrogen ions, so lemon juice has about 100,000 times more than pure water. Danish chemist Søren Sørensen invented the scale in 1909 at a brewery’s laboratory in Copenhagen.",
    "answerHtml": "<b><u>pH</u></b> (accept <u>potential of hydrogen</u> or <u>power of hydrogen</u>; prompt on <u>acidity</u> or <u>hydrogen ion concentration</u>; do not accept “pOH” or “pKa”)",
    "accept": [
        "ph",
        "p h",
        "ph scale",
        "ph value",
        "ph level",
        "ph number",
        "potential of hydrogen",
        "power of hydrogen",
        "potential hydrogen",
        "power hydrogen"
    ],
    "prompt": [
        "acidity",
        "basicity",
        "hydrogen ion concentration",
        "hydronium concentration",
        "hydronium ion concentration"
    ],
    "reject": [
        "poh",
        "pka",
        "pkb",
        "pkw",
        "ka",
        "kb",
        "kw",
        "acid",
        "acids",
        "base",
        "bases",
        "alkali",
        "litmus",
        "litmus paper",
        "indicator",
        "indicators",
        "universal indicator",
        "phenolphthalein",
        "titration",
        "buffer",
        "buffers",
        "neutralization",
        "molarity",
        "logarithm",
        "log",
        "hammett acidity function",
        "acid dissociation constant",
        "dissociation constant",
        "equilibrium constant",
        "ph meter"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/PH",
    "qb": {
        "q": "pH",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In 1934, Arnold Beckman invented an electronic meter to measure this quantity in lemon juice for a group of California citrus growers, and his company grew into a major maker of lab instruments. Such meters work by sensing the voltage across a thin glass bulb.",
            "r": "For 10 points, name this number that tells how acidic or basic a solution is, on a scale where 7 is neutral."
        },
        {
            "p": "Søren Sørensen [“SUR-en-sen”] introduced this measure in 1909 while studying proteins and enzymes at the Carlsberg Laboratory, a research lab in Copenhagen founded by a brewer. He defined it using the negative logarithm of a concentration.",
            "r": "Pure water has a value of 7 on this measure. For 10 points, name this scale that tells how acidic or basic a solution is."
        },
        {
            "p": "The Henderson–Hasselbalch [“HAH-sul-bahlk”] equation says that for a buffer, this quantity equals the pKa of the weak acid plus the logarithm of the ratio of base to acid. When a buffer holds equal amounts of a weak acid and its conjugate base, this quantity equals the pKa.",
            "r": "For 10 points, name this measure of how acidic a solution is, which is 7 for pure water."
        },
        {
            "p": "Halfway to the equivalence point, when a weak acid is being titrated with a strong base, this quantity equals the acid’s pKa. During a titration, this quantity jumps sharply near the equivalence point, giving an S-shaped curve.",
            "r": "For 10 points, name this logarithmic measure of acidity, which runs from about 0 to 14."
        },
        {
            "p": "Hot pure water is still neutral even though its value of this quantity is lower than that of cold pure water, because water splits into more hydrogen and hydroxide ions as it heats up. At 25 degrees Celsius, the ion product of water is 1.0 times 10 to the negative 14th.",
            "r": "For 10 points, name this number, 7 for pure water at room temperature, that tells how acidic a solution is."
        },
        {
            "p": "Very concentrated solutions of strong acids can have values of this quantity below zero, and car battery acid, a sulfuric acid solution, has a value near zero. For superacids, which are even stronger, chemists use the Hammett acidity function instead of this quantity.",
            "r": "For 10 points, name this logarithmic measure of acidity, on which pure water scores a 7."
        },
        {
            "p": "As the oceans absorb carbon dioxide from the air, the average value of this quantity for surface seawater has fallen from about 8.2 to about 8.1 since the 1700s, a change called ocean acidification. That small drop makes seawater roughly 30 percent more acidic.",
            "r": "For 10 points, name this measure of how acidic or basic a solution is, which is 7 for pure water."
        },
        {
            "p": "Some hydrangea [“hy-DRAIN-juh”] flowers turn blue when grown in soil with a low value of this quantity and pink when the value is high. Gardeners spread lime on soil to raise this quantity and sulfur to lower it.",
            "r": "For 10 points, name this measure of acidity, on a scale where 7 is neutral and lower numbers are more acidic."
        },
        {
            "p": "A buffer made of carbonic acid and bicarbonate keeps this quantity in human blood between about 7.35 and 7.45. If this quantity in blood falls below that range, a person develops acidosis; if it rises above it, alkalosis.",
            "r": "For 10 points, name this scale, on which 7 is neutral, used to measure how acidic a solution is."
        },
        {
            "p": "Ordinary rain has a value of this quantity of about 5.6, because carbon dioxide dissolves in it to form carbonic acid. Rain with an even lower value, caused mostly by sulfur and nitrogen oxides from burning fuels, is called acid rain.",
            "r": "For 10 points, name this number that tells how acidic a solution is, which is 7 for pure water."
        },
        {
            "p": "Red cabbage juice turns red or pink at low values of this quantity and green or yellow at high values, so it can be used to estimate it. Universal indicator shows a whole rainbow of colors as this quantity changes, from red through green to purple.",
            "r": "For 10 points, name this scale, on which acids score below 7 and bases score above 7, that measures acidity."
        },
        {
            "p": "At 25 degrees Celsius, this quantity and a similar measure based on hydroxide ions always add up to 14. Phenolphthalein [“fee-nol-THAY-leen”] changes from colorless to pink as this quantity rises past about 8.",
            "r": "Each one-unit drop in this quantity means ten times more hydrogen ions. For 10 points, name this measure of acidity."
        },
        {
            "p": "Every amino acid has a value of this quantity called its isoelectric point, at which the molecule carries no overall electric charge. Biochemists separate proteins in a gel by differences in that value, a technique called isoelectric focusing.",
            "r": "For 10 points, name this measure of how acidic or basic a solution is, which is 7 when the solution is neutral."
        },
        {
            "p": "Pepsin, a protein-digesting enzyme in the stomach, works best when this quantity is about 2, while enzymes inside lysosomes work best near 5. Stomach acid gets its low value of this quantity from hydrochloric acid.",
            "r": "For 10 points, name this scale that runs from 0 to 14 and measures how acidic a solution is."
        },
        {
            "p": "In 1909, Fritz Haber and Zygmunt Klemensiewicz [“kleh-men-SHEH-vich”] built an early glass electrode, the kind of sensor still used to measure this quantity. The lowercase first letter of this quantity’s name is often said to stand for “power” or “potential.”",
            "r": "For 10 points, name this logarithmic measure of hydrogen ion concentration, which is 7 for pure water."
        }
    ],
    "clues": [
        {
            "id": "zero-fourteen",
            "tier": "giveaway",
            "t": "A scale, usually running from 0 to 14, that measures how acidic or basic a solution is",
            "k": ["0 to 14", "acidic", "basic", "scale"],
            "n": 0
        },
        {
            "id": "seven-neutral",
            "tier": "giveaway",
            "t": "A value of 7 is neutral, as in pure water; lower values are acidic and higher values are basic",
            "k": ["neutral", "pure water", "acidic"],
            "n": 0,
            "rabbit": "Water"
        },
        {
            "id": "hydrogen-ions",
            "tier": "giveaway",
            "t": "It measures the concentration of hydrogen (hydronium) ions in a solution",
            "k": ["hydrogen", "hydronium", "concentration"],
            "n": 0,
            "rabbit": "Ions"
        },
        {
            "id": "tenfold",
            "tier": "giveaway",
            "t": "The scale is logarithmic: each one-unit change means ten times more or fewer hydrogen ions",
            "k": ["logarithmic", "ten times"],
            "n": 0
        },
        {
            "id": "sorensen",
            "tier": "middle",
            "t": "Søren Sørensen introduced it in 1909 at the Carlsberg Laboratory in Copenhagen",
            "k": ["sørensen", "carlsberg", "1909", "copenhagen"],
            "n": 0
        },
        {
            "id": "negative-log",
            "tier": "middle",
            "t": "Defined as the negative logarithm (base 10) of the hydrogen ion concentration",
            "k": ["negative logarithm", "base 10"],
            "n": 0
        },
        {
            "id": "examples",
            "tier": "middle",
            "t": "Stomach acid and lemon juice are about 2, pure water is 7, blood is about 7.4, and bleach is about 13",
            "k": ["stomach acid", "lemon juice", "blood", "bleach"],
            "n": 0
        },
        {
            "id": "litmus",
            "tier": "middle",
            "t": "Litmus paper turns red in acids (low values) and blue in bases (high values)",
            "k": ["litmus", "red", "blue"],
            "n": 0,
            "rabbit": "Acids"
        },
        {
            "id": "indicators",
            "tier": "middle",
            "t": "Red cabbage juice, phenolphthalein, and universal indicator change color as it changes",
            "k": ["red cabbage", "phenolphthalein", "universal indicator"],
            "n": 0
        },
        {
            "id": "meter",
            "tier": "middle",
            "t": "Measured precisely by an electronic meter with a glass electrode",
            "k": ["meter", "glass electrode"],
            "n": 0
        },
        {
            "id": "sum-14",
            "tier": "middle",
            "t": "At 25 °C, it plus the matching measure for hydroxide ions always equals 14",
            "k": ["hydroxide", "equals 14"],
            "n": 0
        },
        {
            "id": "blood",
            "tier": "middle",
            "t": "A carbonic acid–bicarbonate buffer keeps blood between about 7.35 and 7.45; lower is acidosis, higher is alkalosis",
            "k": ["bicarbonate", "7.35", "acidosis", "alkalosis"],
            "n": 0,
            "rabbit": "Blood"
        },
        {
            "id": "acid-rain",
            "tier": "middle",
            "t": "Normal rain is about 5.6 because of dissolved carbon dioxide; acid rain is lower",
            "k": ["acid rain", "5.6", "carbon dioxide"],
            "n": 0,
            "rabbit": "Carbon dioxide"
        },
        {
            "id": "beckman",
            "tier": "power",
            "t": "Arnold Beckman invented an electronic meter for it in 1934 to test lemon juice for California citrus growers",
            "k": ["beckman", "1934", "citrus"],
            "n": 0
        },
        {
            "id": "haber-klemensiewicz",
            "tier": "power",
            "t": "Fritz Haber and Zygmunt Klemensiewicz built an early glass electrode in 1909",
            "k": ["klemensiewicz", "haber", "glass electrode"],
            "n": 0
        },
        {
            "id": "henderson",
            "tier": "power",
            "t": "Henderson–Hasselbalch equation: for a buffer, it equals the pKa plus the log of the base-to-acid ratio",
            "k": ["henderson", "hasselbalch", "pka", "buffer"],
            "n": 0
        },
        {
            "id": "half-equivalence",
            "tier": "power",
            "t": "Halfway to the equivalence point of a weak acid titration, it equals the acid’s pKa; it jumps sharply near the equivalence point",
            "k": ["halfway", "equivalence point", "titration"],
            "n": 0,
            "rabbit": "Titration"
        },
        {
            "id": "hot-water",
            "tier": "power",
            "t": "Hot pure water is still neutral but reads lower than 7, because water splits into more ions when heated",
            "k": ["hot", "neutral", "more ions"],
            "n": 0
        },
        {
            "id": "below-zero",
            "tier": "power",
            "t": "Very concentrated strong acids can go below zero; superacids are compared with the Hammett acidity function instead",
            "k": ["below zero", "hammett", "superacids"],
            "n": 0
        },
        {
            "id": "ocean",
            "tier": "power",
            "t": "Surface seawater has dropped from about 8.2 to about 8.1 since the 1700s as oceans absorb carbon dioxide (ocean acidification)",
            "k": ["ocean acidification", "8.2", "8.1"],
            "n": 0
        },
        {
            "id": "hydrangeas",
            "tier": "power",
            "t": "Hydrangeas bloom blue in acidic soil and pink in alkaline soil; lime raises soil values and sulfur lowers them",
            "k": ["hydrangeas", "lime", "sulfur"],
            "n": 0,
            "rabbit": "Soil"
        },
        {
            "id": "isoelectric",
            "tier": "power",
            "t": "An amino acid’s isoelectric point is the value at which it has no overall charge, used in isoelectric focusing",
            "k": ["isoelectric point", "amino acid", "no overall charge"],
            "n": 0,
            "rabbit": "Amino acids"
        },
        {
            "id": "pepsin",
            "tier": "power",
            "t": "Pepsin works best near 2 and lysosome enzymes near 5",
            "k": ["pepsin", "lysosome"],
            "n": 0,
            "rabbit": "Enzymes"
        },
        {
            "id": "letter-p",
            "tier": "power",
            "t": "Its lowercase first letter is often said to stand for “power” or “potential”",
            "k": ["power", "potential", "lowercase"],
            "n": 0
        },
        {
            "id": "kw",
            "tier": "power",
            "t": "At 25 °C, water’s ion product, Kw, is 1.0 × 10⁻¹⁴",
            "k": ["ion product", "kw"],
            "n": 0
        }
    ],
    "trap": {
        "title": "The scale, not the acid",
        "body": "Nearly every pH clue mentions acids, bases, litmus, indicators, or hydrogen ions, so players blurt “acids” or “hydrogen ions” instead of the measurement itself. Others confuse pH with its cousins pOH, which is based on hydroxide ions, and pKa, which measures how strong an acid is; those are different answers.",
        "fix": "If the question asks for “this number,” “this quantity,” or “this scale,” answer pH. Even when a clue says the value plus a hydroxide-based measure equals 14, the answer is still pH, not pOH.",
        "line": "Real answer line: <b><u>pH</u></b> (accept <u>potential of hydrogen</u> or <u>power of hydrogen</u>; prompt on <u>acidity</u> or <u>hydrogen ion concentration</u>; do not accept “pOH” or “pKa”)"
    },
    "tests": {
        "right": [
            "pH",
            "PH",
            "p.H.",
            "Potential of hydrogen",
            "Power of hydrogen",
            "pH scale"
        ],
        "prompt": [
            "Acidity",
            "Hydrogen ion concentration"
        ],
        "wrong": [
            "pOH",
            "pKa",
            "Acids",
            "Litmus",
            "Ka",
            "Molarity",
            "Titration",
            "Indicator"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
