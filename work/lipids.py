import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "lipids",
    "name": "Lipids",
    "mono": "LIP",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Fats, oils, waxes, and steroids · Store energy and build cell membranes",
    "dates": "Pack about 9 Calories per gram",
    "briefing": "Lipids are the greasy, water-fearing molecules of life: fats, oils, waxes, and steroids such as cholesterol. Because they are nonpolar, they don’t dissolve in water, which is why oil-and-vinegar salad dressing separates. Fats pack about 9 Calories per gram, more than twice as much as carbohydrates or proteins, and phospholipids form the double layer that wraps every cell.",
    "answerHtml": "<b><u>Lipids</u></b> (accept <u>fats</u> or <u>lipid</u>; prompt on <u>triglycerides</u> or <u>oils</u>; do not accept “fatty acids” or “carbohydrates”)",
    "accept": [
        "lipids",
        "lipid",
        "fats",
        "fat"
    ],
    "prompt": [
        "triglycerides",
        "triglyceride",
        "triacylglycerols",
        "triacylglycerol",
        "oils",
        "oil"
    ],
    "reject": [
        "fatty acids",
        "fatty acid",
        "carbohydrates",
        "carbohydrate",
        "proteins",
        "protein",
        "nucleic acids",
        "nucleic acid",
        "phospholipids",
        "phospholipid",
        "lipid bilayer",
        "lipid bilayers",
        "lipid rafts",
        "steroids",
        "steroid",
        "cholesterol",
        "waxes",
        "wax",
        "glycerol",
        "lipase",
        "lipases",
        "lipoproteins",
        "lipoprotein",
        "glycolipids",
        "sugars",
        "starch",
        "cellulose",
        "hydrocarbons"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Lipid",
    "qb": {
        "q": "lipids",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In the early 1800s, French chemist Michel Chevreul [“shuh-VRUHL”] showed that soap-making splits animal versions of these substances into glycerol and acids. That reaction, in which these substances are boiled with lye, is called saponification [“suh-pon-ih-fih-KAY-shun”].",
            "r": "They store about 9 Calories per gram. For 10 points, name this class of water-fearing biomolecules that includes oils, waxes, and steroids."
        },
        {
            "p": "Omega-3 molecules of this kind, found in fish such as salmon, have their first carbon-carbon double bond three carbons from the tail end of the chain. Linoleic [“lin-uh-LEE-ik”] acid, another one, is called “essential” because the body cannot make it and must get it from food.",
            "r": "For 10 points, name this class of biomolecules that includes triglycerides and steroids and does not dissolve in water."
        },
        {
            "p": "Lecithin [“LESS-ih-thin”] from egg yolks keeps mayonnaise from separating, since each of its molecules has a water-loving head and two water-fearing tails. Molecules with that shape, one type of these substances, are called amphipathic [“am-fih-PATH-ik”].",
            "r": "That type forms the double layer of every cell membrane. For 10 points, name this class of biomolecules that also includes oils and waxes."
        },
        {
            "p": "Bubbling hydrogen gas through liquid plant-based examples of these substances turns some of their carbon-carbon double bonds into single bonds, making solid spreads like margarine. That partial hydrogenation also creates “trans” versions of these molecules, which are linked to heart disease.",
            "r": "Saturated ones, like butter, have no double bonds and are solid at room temperature. For 10 points, name these biomolecules that include triglycerides."
        },
        {
            "p": "In the emulsion test for these substances, a food sample is shaken with ethanol and then poured into water, where these substances turn the mixture cloudy white. The dye Sudan III [“soo-DAN three”] stains these substances red.",
            "r": "Rubbing them on brown paper leaves a see-through spot. For 10 points, name these biomolecules that include oils and waxes."
        },
        {
            "p": "After digestion, these molecules are packed into particles called chylomicrons [“kye-loh-MY-kronz”] and absorbed into lacteals, tiny lymph vessels inside the villi of the small intestine. Before that, bile salts help gather them into tiny clusters called micelles [“my-SELZ”].",
            "r": "Enzymes called lipases break them down. For 10 points, name these energy-rich biomolecules that do not dissolve in water."
        },
        {
            "p": "Brown adipose tissue burns stored molecules of this kind to make heat instead of ATP, using a protein called thermogenin inside its mitochondria. White adipose tissue stores these molecules and also cushions organs and insulates the body.",
            "r": "For 10 points, name these biomolecules, including triglycerides, that store about 9 Calories of energy per gram."
        },
        {
            "p": "Three ester bonds form when a glycerol molecule joins three long acid chains in a dehydration synthesis that releases three molecules of water. The molecule built that way, a triglyceride [“try-GLISS-er-ide”], is the most common kind of these substances in food.",
            "r": "For 10 points, name this class of biomolecules that includes oils, waxes, and steroids such as cholesterol."
        },
        {
            "p": "The myelin sheaths that insulate nerve fibers are made mostly of these substances, which is one reason the brain is so rich in them. One group of these substances, which includes testosterone and estrogen, is built from four fused carbon rings.",
            "r": "That group, the steroids, includes cholesterol. For 10 points, name this class of water-fearing biomolecules."
        },
        {
            "p": "Cells that make large amounts of these substances, such as those in the adrenal glands, are packed with smooth endoplasmic reticulum, the organelle that builds them. Vitamins A, D, E, and K dissolve in these substances rather than in water, so the body can store them.",
            "r": "They do not mix with water. For 10 points, name this class of biomolecules that includes oils, waxes, and cholesterol."
        },
        {
            "p": "When food rich in these substances reaches the small intestine, the gut releases cholecystokinin [“koh-luh-sis-toh-KY-nin”], which makes the gallbladder squeeze out bile. Bile then breaks these substances into tiny droplets so enzymes can reach them, a process called emulsification.",
            "r": "Pancreatic lipase then breaks them into fatty acids and glycerol. For 10 points, name these biomolecules that do not dissolve in water."
        },
        {
            "p": "Chips and nuts go rancid when oxygen attacks the double bonds in these molecules, so companies add antioxidants such as vitamin E to slow the damage. Unsaturated versions of these molecules have kinks at those double bonds, which keep them liquid at room temperature.",
            "r": "For 10 points, name this class of biomolecules, including oils and waxes, that stores long-term energy."
        },
        {
            "p": "A camel’s hump is not a water tank but a store of these substances, which the camel can break down for energy when food is scarce. Whales and seals stay warm in icy water thanks to blubber, a thick layer of these substances under the skin.",
            "r": "Butter and olive oil are rich in them. For 10 points, name this class of biomolecules that includes triglycerides, oils, and waxes."
        },
        {
            "p": "Soap cleans greasy dishes because each soap molecule has a long nonpolar tail that dissolves in these substances and a charged head that dissolves in water. Bile salts work in a similar way, coating tiny droplets of these substances in the small intestine.",
            "r": "These substances are nonpolar, so they don’t mix with water. For 10 points, name this class of biomolecules."
        },
        {
            "p": "Fish that live in icy water build their cell membranes with extra unsaturated molecules of this kind, whose kinked tails keep the membranes from stiffening in the cold. Saturated molecules of this kind have straight tails that pack tightly together.",
            "r": "That is why butter is solid at room temperature. For 10 points, name this class of biomolecules that includes oils and waxes."
        }
    ],
    "clues": [
        {
            "id": "nonpolar",
            "tier": "giveaway",
            "t": "Biomolecules that do not dissolve in water because they are nonpolar (hydrophobic, or “water-fearing”)",
            "k": ["nonpolar", "hydrophobic", "water-fearing"],
            "n": 0
        },
        {
            "id": "members",
            "tier": "giveaway",
            "t": "Include oils, waxes, and steroids such as cholesterol",
            "k": ["oils", "waxes", "steroids"],
            "n": 0,
            "rabbit": "Cholesterol"
        },
        {
            "id": "energy",
            "tier": "giveaway",
            "t": "Store energy: about 9 Calories per gram, more than twice as much as carbohydrates or proteins",
            "k": ["9 calories", "energy", "per gram"],
            "n": 0
        },
        {
            "id": "membranes",
            "tier": "giveaway",
            "t": "Molecules with a phosphate head and two tails form the double layer (bilayer) of every cell membrane",
            "k": ["bilayer", "cell membrane", "phosphate"],
            "n": 0,
            "rabbit": "Cell membrane"
        },
        {
            "id": "four-biomolecules",
            "tier": "giveaway",
            "t": "One of the four main kinds of biomolecules, along with carbohydrates, proteins, and nucleic acids",
            "k": ["biomolecules", "carbohydrates", "nucleic acids"],
            "n": 0,
            "rabbit": "Proteins"
        },
        {
            "id": "triglycerides",
            "tier": "middle",
            "t": "Triglycerides: three fatty acids attached to one glycerol, the most common kind in food",
            "k": ["triglycerides", "glycerol"],
            "n": 0
        },
        {
            "id": "saturated",
            "tier": "middle",
            "t": "Saturated ones have no carbon-carbon double bonds and are solid at room temperature, like butter; unsaturated ones have kinks and stay liquid",
            "k": ["saturated", "unsaturated", "double bonds", "butter"],
            "n": 0
        },
        {
            "id": "bile",
            "tier": "middle",
            "t": "Bile, made by the liver and stored in the gallbladder, breaks them into tiny droplets (emulsification)",
            "k": ["bile", "emulsification", "gallbladder"],
            "n": 0
        },
        {
            "id": "lipases",
            "tier": "middle",
            "t": "Enzymes called lipases, mostly from the pancreas, break them into fatty acids and glycerol",
            "k": ["lipases", "pancreas"],
            "n": 0,
            "rabbit": "Pancreas"
        },
        {
            "id": "food-tests",
            "tier": "middle",
            "t": "Food tests: Sudan III dye stains them red, and they leave a see-through grease spot on brown paper",
            "k": ["sudan", "grease spot", "brown paper"],
            "n": 0
        },
        {
            "id": "smooth-er",
            "tier": "middle",
            "t": "Built by the smooth endoplasmic reticulum, which is plentiful in cells like those of the adrenal glands",
            "k": ["smooth endoplasmic reticulum", "adrenal"],
            "n": 0,
            "rabbit": "Endoplasmic reticulum"
        },
        {
            "id": "adipose",
            "tier": "middle",
            "t": "Stored in adipose tissue, which cushions organs and insulates the body; whale blubber and camel humps are big stores of them",
            "k": ["adipose", "blubber", "camel"],
            "n": 0
        },
        {
            "id": "vitamins",
            "tier": "middle",
            "t": "Vitamins A, D, E, and K dissolve in them instead of in water, so the body can store those vitamins",
            "k": ["vitamins", "dissolve"],
            "n": 0
        },
        {
            "id": "waxes",
            "tier": "middle",
            "t": "Waxes, like beeswax and the cuticle that coats leaves, keep water out",
            "k": ["beeswax", "cuticle"],
            "n": 0
        },
        {
            "id": "steroid-rings",
            "tier": "middle",
            "t": "Steroids, such as cholesterol, testosterone, and estrogen, are built from four fused carbon rings",
            "k": ["four fused", "carbon rings", "testosterone"],
            "n": 0
        },
        {
            "id": "ester-bonds",
            "tier": "power",
            "t": "Glycerol joins its three acid chains by ester bonds in a dehydration synthesis that releases water",
            "k": ["ester bonds", "dehydration synthesis"],
            "n": 0
        },
        {
            "id": "hydrogenation",
            "tier": "power",
            "t": "Hydrogenation turns liquid plant oils into solid spreads like margarine; partial hydrogenation creates “trans” versions linked to heart disease",
            "k": ["hydrogenation", "margarine", "trans"],
            "n": 0
        },
        {
            "id": "omega-essential",
            "tier": "power",
            "t": "Omega-3 ones (in fish like salmon) have their first double bond three carbons from the tail end; linoleic acid is “essential,” so it must come from food",
            "k": ["omega-3", "linoleic", "essential"],
            "n": 0
        },
        {
            "id": "chevreul",
            "tier": "power",
            "t": "Michel Chevreul showed in the early 1800s that soap-making splits animal ones into glycerol and acids",
            "k": ["chevreul", "1800s"],
            "n": 0
        },
        {
            "id": "saponification",
            "tier": "power",
            "t": "Boiling them with lye, a strong base, makes soap and glycerol, a reaction called saponification",
            "k": ["saponification", "lye", "soap"],
            "n": 0
        },
        {
            "id": "emulsion-test",
            "tier": "power",
            "t": "Emulsion test: shake a sample with ethanol, pour it into water, and these turn the mixture cloudy white",
            "k": ["emulsion test", "ethanol", "cloudy white"],
            "n": 0
        },
        {
            "id": "lacteals",
            "tier": "power",
            "t": "Bile salts gather them into micelles; then they are packed into chylomicrons and absorbed by lacteals in the villi",
            "k": ["chylomicrons", "lacteals", "micelles"],
            "n": 0,
            "rabbit": "Small intestine"
        },
        {
            "id": "lecithin",
            "tier": "power",
            "t": "Lecithin from egg yolks keeps mayonnaise from separating; its molecules are amphipathic, with a water-loving head and two water-fearing tails",
            "k": ["lecithin", "mayonnaise", "amphipathic"],
            "n": 0
        },
        {
            "id": "brown-adipose",
            "tier": "power",
            "t": "Brown adipose tissue burns them to make heat, using thermogenin in its mitochondria",
            "k": ["brown adipose", "thermogenin"],
            "n": 0,
            "rabbit": "Mitochondria"
        },
        {
            "id": "myelin",
            "tier": "power",
            "t": "Myelin sheaths around nerve fibers are made mostly of them, so the brain is rich in them",
            "k": ["myelin", "nerve fibers"],
            "n": 0
        },
        {
            "id": "soap",
            "tier": "power",
            "t": "Soap cleans grease because each soap molecule has a nonpolar tail that dissolves in these and a charged head that dissolves in water",
            "k": ["charged head", "nonpolar tail"],
            "n": 0
        },
        {
            "id": "rancid",
            "tier": "power",
            "t": "They go rancid when oxygen attacks their double bonds, so antioxidants such as vitamin E are added to foods",
            "k": ["rancid", "antioxidants"],
            "n": 0
        },
        {
            "id": "cold-fish",
            "tier": "power",
            "t": "Fish in icy water put extra unsaturated ones in their cell membranes, since kinked tails keep membranes from stiffening",
            "k": ["icy water", "stiffening"],
            "n": 0
        }
    ],
    "trap": {
        "title": "The family, not one member",
        "body": "Lipid tossups name many family members, such as triglycerides, phospholipids, cholesterol, and waxes, and many parts, such as fatty acids and glycerol, so players blurt one of those instead of the whole class. “Triglycerides” or “oils” earns only a prompt, and “fatty acids” is wrong because fatty acids are just building blocks. Players also confuse lipids with carbohydrates, since both store energy and are made mostly of carbon, hydrogen, and oxygen.",
        "fix": "If the question asks for the whole class, including steroids, waxes, or membrane molecules, say “lipids” (or “fats”). Water-fearing, nonpolar, 9 Calories per gram, Sudan III, or bile mean lipids; sugars, starch, 4 Calories per gram, or Benedict’s and iodine tests mean carbohydrates.",
        "line": "Real answer line: <b><u>Lipids</u></b> (accept <u>fats</u>; prompt on <u>triglycerides</u> or <u>oils</u>; do not accept “fatty acids”)"
    },
    "tests": {
        "right": [
            "Lipids",
            "lipid",
            "Fats",
            "fat",
            "Lipds"
        ],
        "prompt": [
            "Triglycerides",
            "Oils"
        ],
        "wrong": [
            "Fatty acids",
            "Carbohydrates",
            "Proteins",
            "Cholesterol",
            "Phospholipids",
            "Lipid bilayer"
        ]
    }
}

with open(ROOT / "topics" / "lipids.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote topics/lipids.json")
