import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "stem-cells",
    "name": "Stem cells",
    "mono": "STC",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Cells that can become many other kinds · How bodies grow, heal, and renew",
    "dates": "First proved to exist in the early 1960s",
    "briefing": "Stem cells are the body’s blank slates: unspecialized cells that can copy themselves and also turn into specialized cells, such as blood, muscle, or nerve cells. The ones in your bone marrow make billions of new blood cells every day, and flatworms called planarians use theirs to regrow a whole body from a small piece. In 2006, Shinya Yamanaka discovered how to turn ordinary mouse skin cells into stem cells, work that won him a Nobel Prize.",
    "answerHtml": "<b><u>Stem cells</u></b> (accept <u>stem cell</u> or specific kinds, such as <u>embryonic stem cells</u> or <u>induced pluripotent stem cells</u>; prompt on <u>pluripotent cells</u> or <u>undifferentiated cells</u>)",
    "accept": [
        "stem cells",
        "stem cell",
        "ips cells",
        "ips cell",
        "ipscs",
        "ipsc"
    ],
    "prompt": [
        "pluripotent cells",
        "pluripotent cell",
        "pluripotent",
        "totipotent cells",
        "totipotent",
        "multipotent cells",
        "multipotent",
        "undifferentiated cells",
        "unspecialized cells"
    ],
    "reject": [
        "meristem",
        "meristems",
        "zygote",
        "zygotes",
        "blastocyst",
        "blastocysts",
        "germ cells",
        "gametes",
        "cancer cells",
        "red blood cells",
        "white blood cells",
        "blood cells",
        "platelets",
        "neurons",
        "cloning",
        "clones",
        "progenitor cells",
        "differentiation",
        "cell differentiation",
        "somatic cells",
        "skin cells",
        "fibroblasts",
        "sickle cell"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Stem_cell",
    "qb": {
        "q": "stem cells",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In the early 1960s, James Till and Ernest McCulloch proved that these cells exist by injecting mice with donor cells and counting the lumps of new blood cells that grew in their spleens. The kind they found, called hematopoietic [“hee-muh-toh-poy-ET-ik”], makes every type of blood cell.",
            "r": "For 10 points, name these unspecialized cells that can divide to copy themselves and can also turn into specialized cells."
        },
        {
            "p": "Four genes nicknamed the Yamanaka factors, including Oct4 and Sox2, can switch an adult skin cell back into one of these cells. Shinya Yamanaka shared a 2012 Nobel Prize for creating those “induced pluripotent” cells, first from mice and then from humans.",
            "r": "For 10 points, name these unspecialized cells that can develop into many different types of cells."
        },
        {
            "p": "In 1962, John Gurdon grew tadpoles from frog eggs whose own nuclei had been replaced with nuclei from a tadpole’s intestinal cells, showing that specialized cells still carry every gene needed to build a body. Gurdon later shared a Nobel Prize with a scientist who turned adult cells back into these cells.",
            "r": "For 10 points, name these unspecialized cells, which can be embryonic or adult, that can develop into many cell types."
        },
        {
            "p": "E. Donnall Thomas won a 1990 Nobel Prize for developing transplants that give patients a new supply of the blood-forming kind of these cells. Donors for those transplants are usually matched to patients using proteins called HLA markers found on the surfaces of cells.",
            "r": "Bone marrow transplants replace these cells in patients with blood cancers such as leukemia. For 10 points, name these unspecialized cells that can become many kinds of cells."
        },
        {
            "p": "In adult tissues, these cells live in niches, special neighborhoods of supporting cells and chemical signals that keep them from specializing too soon. When one of these cells divides asymmetrically, one daughter cell stays like its parent while the other goes on to become a different kind of cell.",
            "r": "For 10 points, name these cells, found in embryos and in many adult tissues, that can turn into other kinds of cells."
        },
        {
            "p": "In 1981, Martin Evans and Matthew Kaufman grew lines of these cells from mouse blastocysts, work that later helped Evans win a Nobel Prize. Seventeen years later, James Thomson’s team at the University of Wisconsin did the same with human blastocysts.",
            "r": "For 10 points, name these unspecialized cells that can become many different kinds of body cells."
        },
        {
            "p": "Hans Clevers’s lab grew tiny “mini-guts” called organoids from single cells of this kind marked by a protein named Lgr5. In the small intestine, cells of this kind tucked into pits called crypts replace the organ’s inner lining every few days.",
            "r": "For 10 points, name these unspecialized cells that divide to renew tissues and can become specialized cells."
        },
        {
            "p": "Flatworms called planarians [“pluh-NAIR-ee-unz”] can regrow an entire body from a small piece because cells of this kind, called neoblasts, are spread throughout their bodies. Scientists hope to use cells of this kind to replace damaged tissues, a field called regenerative medicine.",
            "r": "For 10 points, name these unspecialized cells that can divide and develop into many specialized cell types."
        },
        {
            "p": "A zygote is described as totipotent because it can give rise to every kind of cell, including those of the placenta. Cells of this kind described as pluripotent can become any cell of the body itself, while multipotent ones can form only a few related cell types.",
            "r": "For 10 points, name these unspecialized cells, which can be embryonic or adult, that turn into specialized cells such as blood or nerve cells."
        },
        {
            "p": "The mesenchymal [“muh-ZENG-kuh-mul”] kind of these cells can turn into bone, cartilage, or fat cells. A ring of these cells at the limbus, the edge of the cornea, keeps renewing the clear outer layer of the eye.",
            "r": "For 10 points, name these unspecialized cells that can copy themselves and develop into other kinds of cells."
        },
        {
            "p": "Umbilical cord blood, which families can donate or store after a baby is born, is rich in the blood-forming kind of these cells. That hematopoietic kind lives mainly in red bone marrow, where it makes red blood cells, white blood cells, and platelets.",
            "r": "Transplants of these cells treat blood cancers such as leukemia. For 10 points, name these unspecialized cells that can become many kinds of cells."
        },
        {
            "p": "Cells of this kind make up the inner cell mass of a blastocyst, a hollow ball of cells that forms a few days after fertilization. Those cells are pluripotent, meaning they can become any type of cell in the body.",
            "r": "Adult tissues, like bone marrow, also contain cells of this kind. For 10 points, name these unspecialized cells that can turn into specialized cells."
        },
        {
            "p": "A region of each hair follicle called the bulge holds a supply of these cells, which help regrow hair and repair the skin after a wound. Similar cells in the bottom layer of the epidermis keep replacing the dead skin cells that flake off the surface.",
            "r": "For 10 points, name these unspecialized cells, found in embryos and adult tissues, that divide to renew the body."
        },
        {
            "p": "Satellite cells, which lie along muscle fibers and wake up to repair them after an injury, are the muscle kind of these cells. Like many cells of this kind, they can form only a narrow range of cell types.",
            "r": "For 10 points, name these unspecialized cells, which come in embryonic and adult types, that can develop into specialized cells."
        },
        {
            "p": "In 2014, a team led by Masayo Takahashi in Japan performed the first transplant of eye tissue grown from reprogrammed cells of this kind, to treat a disease of the retina. Many plants keep growing their whole lives because regions called meristems hold a lasting supply of cells of this kind.",
            "r": "For 10 points, name these unspecialized cells, which can be embryonic or adult, that can develop into specialized cells."
        }
    ],
    "clues": [
        {
            "id": "unspecialized",
            "tier": "giveaway",
            "t": "Unspecialized cells that can divide again and again to make more of themselves (self-renewal)",
            "k": ["unspecialized", "self-renewal"],
            "n": 0
        },
        {
            "id": "differentiate",
            "tier": "giveaway",
            "t": "Can differentiate, or specialize, into other cell types such as blood, muscle, or nerve cells",
            "k": ["differentiate", "specialize"],
            "n": 0
        },
        {
            "id": "embryonic-adult",
            "tier": "giveaway",
            "t": "Come in two broad kinds: embryonic ones from early embryos and adult (tissue) ones found after birth",
            "k": ["embryonic", "adult", "tissue"],
            "n": 0
        },
        {
            "id": "marrow-transplants",
            "tier": "giveaway",
            "t": "Bone marrow transplants give patients new blood-forming ones to treat blood cancers such as leukemia",
            "k": ["bone marrow", "leukemia", "transplants"],
            "n": 0
        },
        {
            "id": "hematopoietic",
            "tier": "middle",
            "t": "Hematopoietic (blood-forming) ones in red bone marrow make red blood cells, white blood cells, and platelets",
            "k": ["hematopoietic", "blood-forming", "red bone marrow"],
            "n": 0,
            "rabbit": "Blood"
        },
        {
            "id": "totipotent",
            "tier": "middle",
            "t": "A zygote is totipotent: it can make every kind of cell, even those of the placenta",
            "k": ["totipotent", "zygote"],
            "n": 0
        },
        {
            "id": "pluripotent-multipotent",
            "tier": "middle",
            "t": "Pluripotent ones can become any cell of the body; multipotent ones (most adult kinds) can form only a few related types",
            "k": ["pluripotent", "multipotent"],
            "n": 0
        },
        {
            "id": "inner-cell-mass",
            "tier": "middle",
            "t": "Embryonic ones come from the inner cell mass of a blastocyst, a hollow ball of cells a few days old",
            "k": ["blastocyst", "hollow ball"],
            "n": 0
        },
        {
            "id": "yamanaka",
            "tier": "middle",
            "t": "Shinya Yamanaka turned adult mouse skin cells into “induced pluripotent” (iPS) ones in 2006; Nobel Prize, 2012",
            "k": ["yamanaka", "induced pluripotent", "2006"],
            "n": 0
        },
        {
            "id": "cord-blood",
            "tier": "middle",
            "t": "Umbilical cord blood, donated or stored after birth, is rich in blood-forming ones",
            "k": ["umbilical cord", "cord blood"],
            "n": 0
        },
        {
            "id": "regenerative-medicine",
            "tier": "middle",
            "t": "Scientists hope to use them to replace damaged tissue, a field called regenerative medicine",
            "k": ["regenerative medicine", "damaged tissue"],
            "n": 0
        },
        {
            "id": "meristems",
            "tier": "middle",
            "t": "In plants, they sit in meristems at the tips of shoots and roots, so many plants keep growing their whole lives",
            "k": ["meristems", "shoots"],
            "n": 0,
            "rabbit": "Plants"
        },
        {
            "id": "till-mcculloch",
            "tier": "power",
            "t": "James Till and Ernest McCulloch proved they exist in the early 1960s, using lumps of blood cells that grew in mouse spleens",
            "k": ["till", "mcculloch", "spleens"],
            "n": 0
        },
        {
            "id": "yamanaka-factors",
            "tier": "power",
            "t": "The Yamanaka factors: four genes, including Oct4 and Sox2, that can reprogram adult cells",
            "k": ["yamanaka factors", "oct4", "sox2"],
            "n": 0
        },
        {
            "id": "gurdon",
            "tier": "power",
            "t": "John Gurdon (1962) grew tadpoles from frog eggs given nuclei from intestinal cells; he shared the 2012 Nobel with Yamanaka",
            "k": ["gurdon", "tadpoles", "frog eggs"],
            "n": 0
        },
        {
            "id": "donnall-thomas",
            "tier": "power",
            "t": "E. Donnall Thomas won a 1990 Nobel Prize for bone marrow transplants; donors are matched by HLA markers",
            "k": ["donnall thomas", "1990", "hla markers"],
            "n": 0
        },
        {
            "id": "evans-thomson",
            "tier": "power",
            "t": "Martin Evans and Matthew Kaufman grew mouse embryonic ones in 1981; James Thomson’s team grew human ones in 1998",
            "k": ["martin evans", "kaufman", "james thomson", "1998"],
            "n": 0
        },
        {
            "id": "niche",
            "tier": "power",
            "t": "They live in niches: neighborhoods of support cells and signals that keep them from specializing too soon",
            "k": ["niches", "niche"],
            "n": 0
        },
        {
            "id": "asymmetric",
            "tier": "power",
            "t": "Asymmetric division: one daughter cell stays like its parent while the other specializes",
            "k": ["asymmetric", "daughter"],
            "n": 0
        },
        {
            "id": "crypts-organoids",
            "tier": "power",
            "t": "Intestinal ones in pits called crypts renew the gut lining every few days; Hans Clevers grew “mini-gut” organoids from single Lgr5 cells",
            "k": ["crypts", "organoids", "lgr5", "clevers"],
            "n": 0,
            "rabbit": "Small intestine"
        },
        {
            "id": "planarians",
            "tier": "power",
            "t": "Planarian flatworms regrow a whole body from a small piece using ones called neoblasts",
            "k": ["planarian", "neoblasts", "flatworms"],
            "n": 0
        },
        {
            "id": "mesenchymal",
            "tier": "power",
            "t": "Mesenchymal ones can become bone, cartilage, or fat cells",
            "k": ["mesenchymal", "cartilage"],
            "n": 0
        },
        {
            "id": "limbus",
            "tier": "power",
            "t": "A ring of them at the limbus, the edge of the cornea, renews the eye’s clear outer layer",
            "k": ["limbus", "cornea"],
            "n": 0
        },
        {
            "id": "bulge-epidermis",
            "tier": "power",
            "t": "The bulge of each hair follicle holds them; others in the bottom layer of the epidermis replace shed skin cells",
            "k": ["bulge", "hair follicle", "epidermis"],
            "n": 0
        },
        {
            "id": "satellite",
            "tier": "power",
            "t": "Satellite cells along muscle fibers are the muscle kind; they wake up to repair muscle after an injury",
            "k": ["satellite", "muscle fibers"],
            "n": 0
        },
        {
            "id": "takahashi",
            "tier": "power",
            "t": "Masayo Takahashi’s team (2014) did the first transplant of eye tissue grown from reprogrammed ones, to treat a retina disease",
            "k": ["takahashi", "retina", "2014"],
            "n": 0
        }
    ],
    "trap": {
        "title": "The cells, not the place",
        "body": "Many clues describe where these cells live or come from, such as bone marrow, umbilical cord blood, a blastocyst, or a plant’s meristems, so players blurt the place instead of the cells. Others hear “totipotent” and answer “zygote,” or hear John Gurdon’s frogs and answer “cloning.” Words like pluripotent and multipotent only describe how many cell types these cells can make, so they earn a prompt at best.",
        "fix": "If the question asks for “these cells” that can copy themselves and turn into other cell types, say “stem cells.” Specific kinds, like embryonic stem cells or induced pluripotent stem cells, are fine as long as the words “stem cells” are in your answer.",
        "line": "Real answer line: <b><u>Stem cells</u></b> (accept specific kinds, such as <u>embryonic stem cells</u> or <u>induced pluripotent stem cells</u>; prompt on <u>pluripotent cells</u>)"
    },
    "tests": {
        "right": [
            "Stem cells",
            "stem cell",
            "Embryonic stem cells",
            "Induced pluripotent stem cells",
            "Stem cels",
            "iPS cells"
        ],
        "prompt": [
            "Pluripotent cells",
            "Undifferentiated cells"
        ],
        "wrong": [
            "Bone marrow",
            "Zygote",
            "Meristem",
            "Red blood cells",
            "Progenitor cells",
            "Gametes"
        ]
    }
}

with open(ROOT / "topics" / "stem-cells.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote topics/stem-cells.json")
