import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "solubility",
    "name": "Solubility",
    "mono": "SLB",
    "category": "Chemistry",
    "qbCategory": "Science · Chemistry",
    "kicker": "How much of a substance can dissolve · Why salt vanishes but sand doesn’t",
    "dates": "Henry’s law for dissolved gases stated in 1803",
    "briefing": "Stir salt into a glass of water and it vanishes, but keep adding more and eventually grains pile up at the bottom: you have reached salt’s solubility, the most of it that can dissolve in that much water. Chemists’ rule of thumb is “like dissolves like,” which is why salt dissolves in water but oil doesn’t. Most solids dissolve better in hot water, yet warm soda goes flat faster, because gases dissolve better in cold liquids.",
    "answerHtml": "<b><u>Solubility</u></b> (accept word forms like <u>soluble</u>; prompt on <u>dissolving</u> or <u>miscibility</u>; do not accept “solubility product” or “Henry’s law”)",
    "accept": [
        "solubility",
        "solubilities",
        "soluble",
        "molar solubility"
    ],
    "prompt": [
        "dissolving",
        "dissolution",
        "dissolve",
        "dissolves",
        "miscibility",
        "miscible",
        "solubility rules",
        "solubility curve",
        "solubility curves"
    ],
    "reject": [
        "solubility product",
        "solubility product constant",
        "solubility constant",
        "ksp",
        "k sp",
        "solution",
        "solutions",
        "solute",
        "solutes",
        "solvent",
        "solvents",
        "solvation",
        "saturation",
        "saturated",
        "saturated solution",
        "unsaturated",
        "supersaturated",
        "supersaturation",
        "insoluble",
        "insolubility",
        "henrys law",
        "henry law",
        "concentration",
        "molarity",
        "precipitation",
        "precipitate",
        "hydration",
        "dilution",
        "diffusion",
        "osmosis",
        "polarity",
        "colloid",
        "suspension",
        "electrolyte"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Solubility",
    "qb": {
        "q": "solubility",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "For cerium(III) sulfate, an unusual ionic solid, this property decreases as the water gets warmer, so its curve slopes downward on a graph of this property against temperature. On the same kind of graph, the curve for sodium chloride is nearly flat, while the curve for potassium nitrate rises steeply.",
            "r": "This property is often given in grams of solute per 100 grams of water. For 10 points, name this property, the maximum amount of a substance that can dissolve in a solvent."
        },
        {
            "p": "Adding table salt to a saturated solution of silver chloride lowers this property of silver chloride, an example of the common-ion effect. For a salt that barely dissolves, chemists can calculate this property from a constant called K-sub-s-p, a product of the dissolved ions’ concentrations.",
            "r": "A saturated solution holds as much solute as this property allows. For 10 points, name this property, which tells how much of a solute can dissolve in a solvent."
        },
        {
            "p": "Doctors can safely have patients swallow barium sulfate before X-rays of the digestive system, because this property is extremely low for that compound, even though dissolved barium ions are poisonous. Calcium hydroxide, the compound dissolved in limewater, has a lower value of this property in hot water than in cold water.",
            "r": "Stirring or crushing a solid makes it dissolve faster, but neither one changes this property. For 10 points, name this property, the greatest amount of solute that can dissolve at a given temperature."
        },
        {
            "p": "Nutritionists group vitamins A, D, E, and K together because of this property in fats, which lets the body store them in the liver and fatty tissue. Vitamin C and the B vitamins are instead grouped by their high values of this property in water.",
            "r": "Substances with high values of this property in water are called hydrophilic, or “water-loving.” For 10 points, name this property, a measure of how well a substance dissolves."
        },
        {
            "p": "In the “golden rain” demonstration, yellow lead(II) iodide is dissolved in hot water, and glittering golden crystals appear as the water cools, because this property of that compound falls with temperature. That compound first forms as a solid when solutions of lead(II) nitrate and potassium iodide are mixed.",
            "r": "For most solids, this property rises in hotter water. For 10 points, name this property, the most solute that can dissolve in a given amount of solvent."
        },
        {
            "p": "Henry’s law says that this property for a gas is proportional to the partial pressure of that gas above the liquid. For that reason, soft drinks are bottled under a high pressure of carbon dioxide, which comes fizzing out when the cap is opened.",
            "r": "Unlike most solids, gases have a lower value of this property in warm water, so warm soda goes flat faster. For 10 points, name this property, a measure of how much of a substance can dissolve."
        },
        {
            "p": "Reusable hand warmers contain a sodium acetate solution holding more solute than this property normally allows, so clicking a metal disc inside makes the extra solute crystallize suddenly and give off heat. Rock candy grows from a sugar solution in that same supersaturated state.",
            "r": "A solution holding exactly as much solute as this property allows is called saturated. For 10 points, name this property, the maximum amount of solute that a solvent can hold."
        },
        {
            "p": "Rules for this property in water say that every nitrate, and every compound of sodium, potassium, or ammonium, dissolves easily, while most carbonates and phosphates barely dissolve at all. Chemists use those rules to predict whether mixing two salt solutions will make a cloudy solid.",
            "r": "Such a solid, called a precipitate, forms when a compound can’t stay dissolved. For 10 points, name this property, which describes how much of a substance can dissolve in a solvent."
        },
        {
            "p": "Silver nitrate is used to test for chloride ions, because silver chloride has such a low value of this property that a white solid appears. Rules for this property say that most chlorides dissolve in water, but the chlorides of silver, lead(II), and mercury(I) are exceptions.",
            "r": "Because so many substances have high values of this property in water, water is called the “universal solvent.” For 10 points, name this property that measures how much of a solute can dissolve."
        },
        {
            "p": "Gray-black iodine crystals barely dissolve in water but dissolve readily in hexane, because iodine and hexane are both nonpolar. For a similar reason, dry cleaners remove greasy stains with nonpolar liquids instead of plain water.",
            "r": "This property follows the rule of thumb “like dissolves like.” For 10 points, name this property, which describes how much of a substance can dissolve in a solvent."
        },
        {
            "p": "To dissolve an ionic solid, water must overcome its lattice energy, which holds the crystal together, and the hydration energy released as water molecules surround the freed ions helps pay that cost. In those surrounding shells, water molecules point their partially negative oxygen atoms toward the positive ions.",
            "r": "Water can surround ions because its molecules are polar. For 10 points, name this property, a measure of how much of a solute can dissolve in a solvent."
        },
        {
            "p": "Liquids that mix together in any amounts, such as ethanol and water, are called miscible, meaning each has an unlimited value of this property in the other. Hexane and water are immiscible, so they separate into two layers when poured together.",
            "r": "Oil and water don’t mix because oil has a very low value of this property in water. For 10 points, name this property, which describes how well a substance dissolves."
        },
        {
            "p": "Power plants that release warm water into rivers can harm fish, because this property of oxygen drops as the water warms up. That same drop explains why tiny bubbles of air appear on the inside of a pot of water long before the water boils.",
            "r": "Unlike gases, most solid solutes have higher values of this property in hot water. For 10 points, name this property, the most of a substance that can dissolve in a solvent."
        },
        {
            "p": "Chemists purify a solid by recrystallization, dissolving it in a small amount of hot solvent and letting pure crystals form as the solution cools, while most impurities stay dissolved. That method works because this property usually rises with temperature.",
            "r": "On a graph of this property against temperature, points below the curve stand for unsaturated solutions. For 10 points, name this property, the maximum amount of solute that can dissolve."
        },
        {
            "p": "A mixture of salt and sand can be separated by adding water, filtering out the sand, and then evaporating the water, because only the salt has a high value of this property in water. At room temperature, several times more sugar than table salt can dissolve in the same amount of water.",
            "r": "Adding solute past this property’s limit just leaves crystals at the bottom. For 10 points, name this property, a measure of how much of a solute can dissolve."
        }
    ],
    "clues": [
        {
            "id": "definition",
            "tier": "giveaway",
            "t": "The maximum amount of a solute that can dissolve in a given amount of solvent at a given temperature",
            "k": ["maximum amount", "solute", "solvent"],
            "n": 0
        },
        {
            "id": "like-dissolves-like",
            "tier": "giveaway",
            "t": "Rule of thumb: “like dissolves like,” so polar water dissolves ionic and polar substances such as salt and sugar, but not oil",
            "k": ["like dissolves like", "polar", "oil"],
            "n": 0
        },
        {
            "id": "units",
            "tier": "giveaway",
            "t": "Often measured in grams of solute per 100 grams of water",
            "k": ["grams", "100 grams of water"],
            "n": 0
        },
        {
            "id": "saturated",
            "tier": "giveaway",
            "t": "A saturated solution holds as much solute as it can; an unsaturated one can still dissolve more",
            "k": ["saturated", "unsaturated"],
            "n": 0
        },
        {
            "id": "universal-solvent",
            "tier": "giveaway",
            "t": "Water dissolves so many substances that it is called the “universal solvent”",
            "k": ["universal solvent", "water"],
            "n": 0,
            "rabbit": "Water"
        },
        {
            "id": "solids-temperature",
            "tier": "middle",
            "t": "Most solids dissolve better in hot water than in cold water",
            "k": ["solids", "hot water"],
            "n": 0
        },
        {
            "id": "gases-temperature",
            "tier": "middle",
            "t": "Gases dissolve better in cold water, so warm soda goes flat faster",
            "k": ["gases", "cold water", "flat"],
            "n": 0
        },
        {
            "id": "henrys-law",
            "tier": "middle",
            "t": "Henry’s law: the amount of a gas that dissolves is proportional to that gas’s partial pressure above the liquid",
            "k": ["henry’s law", "partial pressure"],
            "n": 0,
            "rabbit": "Henry’s law"
        },
        {
            "id": "rate-not-amount",
            "tier": "middle",
            "t": "Stirring and crushing make a solid dissolve faster, but they don’t change how much can dissolve",
            "k": ["stirring", "crushing", "faster"],
            "n": 0
        },
        {
            "id": "supersaturated",
            "tier": "middle",
            "t": "A supersaturated solution holds more than the limit; a seed crystal or a jolt makes the extra crystallize, as in rock candy and sodium acetate hand warmers",
            "k": ["supersaturated", "rock candy", "hand warmers"],
            "n": 0
        },
        {
            "id": "curves",
            "tier": "middle",
            "t": "On a graph against temperature, points above the curve are supersaturated, points on it are saturated, and points below it are unsaturated",
            "k": ["curve", "above", "below"],
            "n": 0
        },
        {
            "id": "precipitate",
            "tier": "middle",
            "t": "Mixing two solutions can form a solid that barely dissolves, called a precipitate",
            "k": ["precipitate", "mixing"],
            "n": 0
        },
        {
            "id": "miscible",
            "tier": "middle",
            "t": "Liquids that mix in any amounts, like ethanol and water, are miscible; oil and water are immiscible",
            "k": ["miscible", "immiscible", "ethanol"],
            "n": 0
        },
        {
            "id": "vitamins",
            "tier": "middle",
            "t": "Vitamins A, D, E, and K dissolve in fat and are stored in the body; vitamin C and the B vitamins dissolve in water",
            "k": ["vitamins", "fat", "stored"],
            "n": 0
        },
        {
            "id": "hydrophilic",
            "tier": "middle",
            "t": "Water-loving substances are hydrophilic; water-fearing ones are hydrophobic",
            "k": ["hydrophilic", "hydrophobic"],
            "n": 0
        },
        {
            "id": "ksp",
            "tier": "power",
            "t": "For salts that barely dissolve, it is found from a constant called K-sub-s-p, a product of the dissolved ions’ concentrations",
            "k": ["k-sub-s-p", "product", "concentrations"],
            "n": 0
        },
        {
            "id": "common-ion",
            "tier": "power",
            "t": "Common-ion effect: adding table salt lowers how much silver chloride can dissolve",
            "k": ["common-ion effect", "silver chloride"],
            "n": 0,
            "rabbit": "Chemical equilibrium"
        },
        {
            "id": "cerium-sulfate",
            "tier": "power",
            "t": "Cerium(III) sulfate is unusual: it dissolves less as water gets warmer",
            "k": ["cerium", "warmer"],
            "n": 0
        },
        {
            "id": "salt-nitrate-curves",
            "tier": "power",
            "t": "On temperature graphs, the curve for sodium chloride is nearly flat, but the curve for potassium nitrate rises steeply",
            "k": ["sodium chloride", "potassium nitrate", "flat"],
            "n": 0
        },
        {
            "id": "calcium-hydroxide",
            "tier": "power",
            "t": "Calcium hydroxide, the compound dissolved in limewater, dissolves less in hot water than in cold water",
            "k": ["calcium hydroxide", "limewater"],
            "n": 0
        },
        {
            "id": "barium-sulfate",
            "tier": "power",
            "t": "Barium sulfate barely dissolves, so patients can safely swallow it before X-rays of the digestive system",
            "k": ["barium sulfate", "x-rays"],
            "n": 0
        },
        {
            "id": "rules",
            "tier": "power",
            "t": "Rules: all nitrates and all sodium, potassium, and ammonium compounds dissolve in water; most carbonates and phosphates barely do",
            "k": ["nitrates", "ammonium", "carbonates", "phosphates"],
            "n": 0
        },
        {
            "id": "chloride-test",
            "tier": "power",
            "t": "Most chlorides dissolve, except those of silver, lead(II), and mercury(I); silver nitrate tests for chloride by forming white silver chloride",
            "k": ["silver nitrate", "chlorides", "white"],
            "n": 0
        },
        {
            "id": "golden-rain",
            "tier": "power",
            "t": "“Golden rain”: lead(II) iodide dissolves in hot water and forms glittering yellow crystals as the water cools",
            "k": ["golden rain", "glittering", "iodide"],
            "n": 0
        },
        {
            "id": "recrystallization",
            "tier": "power",
            "t": "Recrystallization purifies a solid by dissolving it in hot solvent and letting pure crystals form as it cools",
            "k": ["recrystallization", "purifies"],
            "n": 0
        },
        {
            "id": "lattice-vs-hydration",
            "tier": "power",
            "t": "To dissolve an ionic solid, water must overcome its lattice energy; the hydration energy released as water surrounds the ions helps pay for it",
            "k": ["lattice energy", "hydration energy", "overcome"],
            "n": 0,
            "rabbit": "Lattice energy"
        },
        {
            "id": "iodine-hexane",
            "tier": "power",
            "t": "Nonpolar iodine barely dissolves in water but dissolves readily in nonpolar hexane",
            "k": ["iodine", "hexane"],
            "n": 0
        },
        {
            "id": "thermal-pollution",
            "tier": "power",
            "t": "Warm water released by power plants holds less dissolved oxygen, which can harm fish",
            "k": ["power plants", "oxygen", "fish"],
            "n": 0
        }
    ],
    "trap": {
        "title": "The property, not its laws",
        "body": "Tossups on this property are full of related answer lines: Henry’s law for gases, the solubility product K-sub-s-p for salts that barely dissolve, and saturated or supersaturated solutions. A player who hears “partial pressure” and blurts “Henry’s law,” or hears K-sub-s-p and says “solubility product,” loses the tossup when the question wants the property itself. Also remember that stirring and crushing change how fast something dissolves, not how much.",
        "fix": "Listen for “this property” or “this quantity.” Answer with the property unless the question says “this law” (Henry’s law) or “this constant” (the solubility product).",
        "line": "Real answer line: <b><u>Solubility</u></b> (accept word forms like <u>soluble</u>; prompt on <u>dissolving</u>; do not accept “solubility product” or “Henry’s law”)"
    },
    "tests": {
        "right": [
            "Solubility",
            "solubilty",
            "Soluble",
            "Molar solubility",
            "Solubilities"
        ],
        "prompt": [
            "Dissolving",
            "Miscibility"
        ],
        "wrong": [
            "Solubility product",
            "Solution",
            "Henry’s law",
            "Saturation",
            "Insoluble",
            "Solvent",
            "Concentration",
            "Ksp"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
