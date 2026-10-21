import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

data = {
    "id": "mohs-hardness-scale",
    "name": "Mohs hardness scale",
    "mono": "MHS",
    "category": "Earth Science",
    "qbCategory": "Science · Other Science (Earth Science)",
    "kicker": "Ranks minerals 1 to 10 by scratch resistance · Talc is 1, diamond is 10",
    "dates": "Created in 1812",
    "briefing": "The Mohs hardness scale ranks minerals by how well they resist scratching, from soft talc at 1 to diamond at 10. German mineralogist Friedrich Mohs created it in 1812 around a simple rule: a harder mineral scratches a softer one. Geologists test unknown minerals with a fingernail (about 2.5), a copper penny (about 3 to 3.5), or a steel knife (about 5.5), and the steps are uneven: diamond resists scratching nearly four times as well as corundum, ranked 9.",
    "answerHtml": "<b><u>Mohs</u></b> hardness scale (accept <u>Mohs scale</u> or <u>hardness</u>; prompt on <u>scratch test</u>; do not accept “Richter scale,” “Moho,” or other hardness tests such as “Rockwell” or “Vickers”)",
    "accept": [
        "mohs",
        "mohs scale",
        "mohs hardness",
        "mohs hardness scale",
        "mohs scale of hardness",
        "mohs scale of mineral hardness",
        "mohs mineral hardness scale",
        "hardness",
        "hardness scale",
        "mineral hardness",
        "scratch hardness",
        "relative hardness",
        "friedrich mohs"
    ],
    "prompt": [
        "scratch test",
        "scratch tests",
        "scratch resistance",
        "resistance to scratching"
    ],
    "reject": [
        "richter",
        "richter scale",
        "richter magnitude scale",
        "moment magnitude scale",
        "mercalli scale",
        "beaufort scale",
        "fujita scale",
        "enhanced fujita scale",
        "saffir simpson scale",
        "ph scale",
        "kelvin scale",
        "moho",
        "mohorovicic",
        "mohorovicic discontinuity",
        "rockwell",
        "rockwell scale",
        "vickers",
        "brinell",
        "knoop",
        "toughness",
        "tenacity",
        "streak",
        "luster",
        "lustre",
        "cleavage",
        "fracture",
        "specific gravity",
        "density",
        "talc",
        "gypsum",
        "calcite",
        "fluorite",
        "apatite",
        "orthoclase",
        "feldspar",
        "quartz",
        "topaz",
        "corundum",
        "diamond"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Mohs_scale",
    "qb": {"q": "hardness", "found": 0, "tip": TIP},
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        {
            "p": "Statisticians often use this scale as a textbook example of an ordinal scale, because its numbers show only rank order and not equal steps. In actual scratch resistance, the gap between its 9 and 10 is bigger than all of the other gaps put together.",
            "r": "It runs from talc at 1 to diamond at 10. For 10 points, name this scale that ranks minerals by how well they resist scratching."
        },
        {
            "p": "Scientists measuring scratch resistance with a sclerometer [“skleh-ROM-uh-ter”] found that corundum, ranked 9 on this scale, resists scratching about twice as well as topaz, ranked 8. The mineral ranked 10 does nearly four times as well as corundum.",
            "r": "That top mineral is diamond, and talc sits at the bottom. For 10 points, name this scale of mineral scratch resistance created by a German mineralogist in 1812."
        },
        {
            "p": "A German mineralogist created this scale in 1812, choosing ten readily available minerals as its reference points. It works on a simple rule: a mineral can scratch any mineral ranked below it, but not one ranked above it.",
            "r": "Quartz ranks 7 on this scale. For 10 points, name this scale that runs from talc at 1 to diamond at 10."
        },
        {
            "p": "Geologists in the field estimate where a mineral falls on this scale with simple tools: a fingernail rates about 2.5, a copper penny about 3 to 3.5, a steel knife or a piece of glass about 5.5, and a steel file about 6.5.",
            "r": "Talc, the softest mineral, sits at the bottom of this scale. For 10 points, name this scale that ranks minerals from 1 to 10 by how well they resist scratching."
        },
        {
            "p": "Jade is tough enough to resist breaking but ranks only about 6 to 7 on this scale, while some minerals that rank far higher can shatter if struck the right way. That difference shows that this scale measures resistance to scratching, not toughness.",
            "r": "Quartz ranks 7 and corundum ranks 9 on this scale. For 10 points, name this scale topped by diamond at 10."
        },
        {
            "p": "Unlike the Brinell and Vickers tests, which press a steel ball or a diamond point into metals and measure the dent, this scale simply asks which mineral scratches which. Its ten reference minerals were chosen in 1812 because they were easy to find.",
            "r": "Its softest mineral is talc and its top mineral is diamond. For 10 points, name this 1-to-10 scale used to identify minerals."
        },
        {
            "p": "Tooth enamel, made mostly of a form of apatite, ranks about 5 on this scale, the same spot as apatite itself. The mineral just below apatite on this scale, fluorite, gave its name to fluorescence because some samples glow under ultraviolet light.",
            "r": "Gypsum, which a fingernail can scratch, ranks 2 on this scale. For 10 points, name this scale that runs from talc to diamond."
        },
        {
            "p": "Orthoclase, a feldspar whose name means “straight break” in Greek, marks 6 on this scale, which makes it just able to scratch window glass. Plagioclase, the other main kind of feldspar, ranks about the same, at 6 to 6.5.",
            "r": "Quartz, one step above orthoclase, ranks 7. For 10 points, name this scale that ranks minerals by how well they resist scratching, topped by diamond."
        },
        {
            "p": "Jewelers warn that gems ranking below 7 on this scale can slowly be scratched by ordinary household dust, which contains tiny grains of a common mineral ranked 7. Topaz, the November birthstone, ranks 8, and emery, a dark rock rich in the mineral ranked 9, coats nail files and sandpaper.",
            "r": "That mineral, corundum, includes rubies and sapphires. For 10 points, name this scale of mineral scratch resistance topped by diamond."
        },
        {
            "p": "Soapstone, a soft carving stone, is made mostly of the mineral at the bottom of this scale, which feels greasy and is ground into a soft powder used in cosmetics. Gypsum, the next mineral up, is heated to make plaster of Paris and used in drywall.",
            "r": "That bottom mineral, talc, ranks 1, and diamond ranks 10. For 10 points, name this scale of mineral scratch resistance."
        },
        {
            "p": "Clear crystals of the mineral ranked 3 on this scale, called Iceland spar, make objects seen through them look doubled, and that mineral fizzes in weak acid. It can be scratched by a steel knife but not by a fingernail.",
            "r": "That mineral, calcite, sits between gypsum and fluorite on this scale. For 10 points, name this scale that runs from talc at 1 to diamond at 10."
        },
        {
            "p": "Students memorize the order of this scale’s ten minerals with sentences like “Tall Giraffes Can Find Alligators Or Quaint Tigers Chewing Dinner.” In that sentence, the words “Find” and “Alligators” stand for fluorite and apatite, ranked 4 and 5.",
            "r": "The first word stands for talc and the last for diamond. For 10 points, name this scale of mineral scratch resistance from 1 to 10."
        },
        {
            "p": "An unglazed porcelain streak plate ranks about 6.5 to 7 on this scale, so minerals that rank higher scratch the plate instead of leaving a colored streak. Along with streak, luster, and cleavage, a mineral’s place on this scale helps geologists identify it.",
            "r": "It ranks talc at 1 and diamond at 10. For 10 points, name this scale used to compare how easily minerals are scratched."
        },
        {
            "p": "Volcanic glass called obsidian rates about 5 to 5.5 on this scale, while olivine, known as the green gem peridot, rates about 6.5 to 7. Because ordinary glass rates about 5.5, minerals above that point can scratch a window.",
            "r": "Diamond, a form of pure carbon, sits at the top of this scale at 10. For 10 points, name this scale that ranks minerals by scratch resistance."
        },
        {
            "p": "The creator of this scale studied under Abraham Werner, the leader of the Neptunists, at Germany’s Freiberg Mining Academy. He picked ten minerals that were easy to get as its fixed points, but later measurements showed that the steps between them are very uneven.",
            "r": "It is sometimes confused with the Richter scale for earthquakes. For 10 points, name this scale that runs from talc at 1 to diamond at 10."
        }
    ],
    "clues": [
        {"id": "definition", "tier": "giveaway",
         "t": "Ranks minerals from 1 to 10 by how well they resist scratching",
         "k": ["1 to 10", "scratching", "minerals"], "n": 0},
        {"id": "talc-diamond", "tier": "giveaway",
         "t": "Talc, the softest, is 1, and diamond is 10, at the top",
         "k": ["talc", "diamond", "softest"], "n": 0, "rabbit": "Diamond"},
        {"id": "quartz-7", "tier": "giveaway",
         "t": "Quartz ranks 7, so it scratches glass",
         "k": ["quartz", "glass"], "n": 0, "rabbit": "Quartz"},
        {"id": "scratch-rule", "tier": "giveaway",
         "t": "Its rule: a mineral can scratch any mineral ranked below it, but not one ranked above it",
         "k": ["scratch", "ranked below"], "n": 0},
        {"id": "german-1812", "tier": "middle",
         "t": "Created in 1812 by a German mineralogist named Friedrich, its namesake",
         "k": ["1812", "german", "namesake"], "n": 0},
        {"id": "ten-minerals", "tier": "middle",
         "t": "Its ten minerals, in order: talc, gypsum, calcite, fluorite, apatite, orthoclase, quartz, topaz, corundum, diamond",
         "k": ["gypsum", "calcite", "fluorite", "apatite", "topaz"], "n": 0},
        {"id": "field-tests", "tier": "middle",
         "t": "Field tests: a fingernail is about 2.5, a copper penny about 3 to 3.5, a steel knife or glass about 5.5, a steel file about 6.5",
         "k": ["fingernail", "copper penny", "steel knife", "steel file"], "n": 0},
        {"id": "relative", "tier": "middle",
         "t": "Relative, not evenly spaced: diamond resists scratching nearly four times as well as corundum",
         "k": ["relative", "four times", "evenly"], "n": 0},
        {"id": "corundum-9", "tier": "middle",
         "t": "Corundum ranks 9; rubies and sapphires are forms of corundum",
         "k": ["corundum", "rubies", "sapphires"], "n": 0, "rabbit": "Aluminum"},
        {"id": "orthoclase-6", "tier": "middle",
         "t": "Orthoclase, a feldspar whose name means “straight break,” ranks 6 and can just scratch window glass",
         "k": ["orthoclase", "feldspar", "straight break"], "n": 0, "rabbit": "Feldspar"},
        {"id": "gypsum-2", "tier": "middle",
         "t": "Gypsum ranks 2, so a fingernail can scratch it; it is used in plaster of Paris and drywall",
         "k": ["gypsum", "plaster of paris", "drywall"], "n": 0},
        {"id": "calcite-3", "tier": "middle",
         "t": "Calcite ranks 3; it fizzes in weak acid, and its clear Iceland spar crystals make objects look doubled",
         "k": ["calcite", "fizzes", "iceland spar"], "n": 0, "rabbit": "Limestone"},
        {"id": "apatite-fluorite", "tier": "middle",
         "t": "Apatite ranks 5, about the same as tooth enamel; fluorite, at 4, gave fluorescence its name",
         "k": ["apatite", "tooth enamel", "fluorescence"], "n": 0},
        {"id": "not-toughness", "tier": "middle",
         "t": "It measures scratch resistance, not toughness: tough jade ranks only about 6 to 7",
         "k": ["toughness", "jade"], "n": 0},
        {"id": "mnemonic", "tier": "power",
         "t": "A mnemonic for its order: “Tall Giraffes Can Find Alligators Or Quaint Tigers Chewing Dinner”",
         "k": ["mnemonic", "giraffes"], "n": 0},
        {"id": "ordinal", "tier": "power",
         "t": "Statisticians use it as a classic ordinal scale; the gap between 9 and 10 is bigger than all the other gaps combined",
         "k": ["ordinal scale", "statisticians", "gap"], "n": 0},
        {"id": "sclerometer", "tier": "power",
         "t": "Sclerometer measurements show corundum resists scratching about twice as well as topaz, and diamond nearly four times as well as corundum",
         "k": ["sclerometer", "twice"], "n": 0},
        {"id": "brinell-vickers", "tier": "power",
         "t": "Unlike the Brinell and Vickers tests, which press a ball or diamond point into metal, it compares which mineral scratches which",
         "k": ["brinell", "vickers", "metal"], "n": 0},
        {"id": "streak-plate", "tier": "power",
         "t": "An unglazed porcelain streak plate rates about 6.5 to 7; higher-ranked minerals scratch it instead of leaving a streak",
         "k": ["streak plate", "porcelain", "unglazed"], "n": 0},
        {"id": "dust", "tier": "power",
         "t": "Household dust contains quartz grains, so gems ranked below 7 can slowly get scratched",
         "k": ["household dust", "gems"], "n": 0},
        {"id": "topaz-emery", "tier": "power",
         "t": "Topaz, the November birthstone, ranks 8; emery, a rock rich in corundum, coats nail files and sandpaper",
         "k": ["topaz", "november", "emery"], "n": 0},
        {"id": "soapstone", "tier": "power",
         "t": "Soapstone, a soft carving stone, is mostly talc, which feels greasy and is ground into powder",
         "k": ["soapstone", "greasy", "powder"], "n": 0},
        {"id": "obsidian-olivine", "tier": "power",
         "t": "Obsidian rates about 5 to 5.5 and olivine (the gem peridot) about 6.5 to 7; window glass is about 5.5",
         "k": ["obsidian", "olivine", "peridot"], "n": 0},
        {"id": "werner", "tier": "power",
         "t": "Its creator studied under Abraham Werner, leader of the Neptunists, at Germany’s Freiberg Mining Academy",
         "k": ["werner", "freiberg", "neptunists"], "n": 0}
    ],
    "trap": {
        "title": "Not Richter, not the Moho",
        "body": "This scale ranks minerals by how well they resist scratching, so it has nothing to do with earthquakes; the Richter scale measures earthquake size. The Moho, short for the Mohorovičić discontinuity, is the boundary between Earth’s crust and mantle. Some real tossups ask for the property, hardness, instead of the scale named for Friedrich Mohs, and both are accepted here.",
        "fix": "Talc to diamond, quartz at 7, fingernails and steel knives, and scratch tests mean the Mohs scale (or hardness). Earthquakes mean the Richter or moment magnitude scale, and a boundary deep beneath the crust means the Moho.",
        "line": "Real answer line: <b><u>Mohs</u></b> hardness scale (accept hardness or Mohs scale; do not accept “Richter scale”)"
    },
    "tests": {
        "right": ["Mohs hardness scale", "Mohs scale", "Moh's scale", "Hardness", "Mohs scale of mineral hardness", "Mos scale", "Friedrich Mohs"],
        "prompt": ["Scratch test", "Scratch resistance"],
        "wrong": ["Richter scale", "Moho", "Diamond", "Talc", "Rockwell hardness", "Streak", "Density"]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
