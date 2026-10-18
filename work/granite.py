import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "granite",
    "name": "Granite",
    "mono": "GRN",
    "category": "Earth Science",
    "qbCategory": "Science · Other Science (Earth Science)",
    "kicker": "Coarse-grained igneous rock · Made mostly of quartz and feldspar",
    "dates": "Forms as magma cools slowly deep underground",
    "briefing": "Granite is the speckled rock of kitchen countertops, gravestones, and Mount Rushmore’s four faces. It forms when thick, silica-rich magma cools slowly deep underground, giving its crystals of quartz, feldspar, and mica time to grow big enough to see. Much of the continents’ crust is made of granite and rocks like it, and New Hampshire is so proud of its granite that it calls itself “the Granite State.”",
    "answerHtml": "<b><u>Granite</u></b> (accept <u>granitic</u> rock; prompt on <u>igneous rock</u>, <u>intrusive rock</u>, <u>plutonic rock</u>, or <u>felsic rock</u>; do not accept “rhyolite,” “granodiorite,” or “gneiss”)",
    "accept": [
        "granite",
        "granites",
        "granitic rock",
        "granitic rocks",
        "granite rock",
        "granite rocks"
    ],
    "prompt": [
        "igneous rock",
        "igneous rocks",
        "intrusive rock",
        "intrusive rocks",
        "intrusive igneous rock",
        "intrusive igneous rocks",
        "plutonic rock",
        "plutonic rocks",
        "plutonic igneous rock",
        "felsic rock",
        "felsic rocks",
        "felsic igneous rock",
        "granitoid",
        "granitoids"
    ],
    "reject": [
        "rhyolite",
        "granodiorite",
        "gneiss",
        "granite gneiss",
        "diorite",
        "gabbro",
        "basalt",
        "andesite",
        "syenite",
        "pegmatite",
        "pegmatites",
        "aplite",
        "quartzite",
        "quartz",
        "feldspar",
        "feldspars",
        "mica",
        "marble",
        "obsidian",
        "pumice",
        "sandstone",
        "limestone",
        "magma",
        "batholith",
        "batholiths"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Granite",
    "qb": {
        "q": "granite",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In 1785, James Hutton found veins of this rock cutting through older rock layers at Glen Tilt in Scotland, evidence that it had once forced its way in as a hot, molten liquid. That discovery helped Hutton argue that heat inside Earth, not an ancient ocean, produced this rock.",
            "r": "Its fine-grained volcanic twin, made from the same kind of magma, is rhyolite. For 10 points, name this coarse-grained igneous rock made mostly of quartz and feldspar."
        },
        {
            "p": "Many curling stones are cut from this rock quarried on Ailsa Craig, a tiny island off the coast of Scotland. The Scottish city of Aberdeen built so many of its buildings from a gray kind of this rock that it is nicknamed for it.",
            "r": "Mount Rushmore’s four presidential faces are carved into this rock. For 10 points, name this hard, coarse-grained rock that makes up much of the continental crust."
        },
        {
            "p": "Ancient Egyptians quarried a red kind of this rock at Aswan to carve obelisks such as Cleopatra’s Needles, and they lined the King’s Chamber inside the Great Pyramid with giant blocks of it. A huge unfinished obelisk still lies in one of those Aswan quarries.",
            "r": "Geologists call this rock felsic, a word blending “feldspar” and “silica.” For 10 points, name this coarse-grained igneous rock made mostly of quartz and feldspar."
        },
        {
            "p": "In 1974, Australian geologists Bruce Chappell and Allan White sorted examples of this rock into “I-type” and “S-type,” depending on whether melted igneous rock or melted sedimentary rock produced them. Traces of uranium in this rock slowly decay into radioactive radon gas.",
            "r": "Giant underground bodies of this rock, like the one at the heart of California’s Sierra Nevada, are called batholiths. For 10 points, name this light-colored rock made mostly of quartz and feldspar."
        },
        {
            "p": "Blocky towers of this rock called tors crown the hilltops of Dartmoor in southwestern England, where rain and frost slowly widened cracks in it. That moorland sits on part of a huge buried body of this rock that stretches west through Cornwall.",
            "r": "When its feldspar weathers into clay, its hard quartz grains are left behind as sand. For 10 points, name this coarse-grained igneous rock often used for kitchen countertops."
        },
        {
            "p": "Tiny zircon crystals inside this rock are often dated by measuring how much of their uranium has decayed into lead. That same trace uranium makes some samples of this rock give off small amounts of radon, a radioactive gas that can seep into basements.",
            "r": "Continental crust rich in this rock is lighter than the basalt of the ocean floor, so continents ride higher. For 10 points, name this coarse-grained rock made mostly of quartz and feldspar."
        },
        {
            "p": "Rock climbers scale El Capitan, a sheer cliff of this rock in Yosemite National Park, and curved sheets peel off nearby domes of it in a process called exfoliation. Those sheets crack loose because rock that formed deep underground expands once the rock above it wears away.",
            "r": "Huge underground bodies of this rock, called batholiths, can stretch for hundreds of kilometers. For 10 points, name this coarse-grained igneous rock made mostly of quartz and feldspar."
        },
        {
            "p": "The Texas State Capitol in Austin was built from “sunset red” blocks of this rock quarried near Marble Falls. Enchanted Rock, a giant pink dome of this rock in the Texas Hill Country, is said to creak and groan as it cools at night.",
            "r": "This rock’s pink color usually comes from crystals of potassium feldspar. For 10 points, name this coarse-grained igneous rock often used for countertops and gravestones."
        },
        {
            "p": "The Old Man of the Mountain, a face-shaped profile formed by cliff ledges of this rock in Franconia Notch, appeared on a state quarter in 2000 and collapsed in 2003. Plymouth Rock, a boulder dropped by an ice-age glacier, is also made of it.",
            "r": "New Hampshire’s nickname comes from this rock. For 10 points, name this coarse-grained igneous rock made mostly of quartz and feldspar."
        },
        {
            "p": "This rock’s name comes from the Latin word granum, meaning “grain.” Curved outer sheets peel off domes of this rock in Yosemite National Park and on Texas’s Enchanted Rock, a weathering process called exfoliation that is driven partly by the release of pressure.",
            "r": "Its minerals are among the last to crystallize in Bowen’s reaction series. For 10 points, name this coarse-grained igneous rock made mostly of quartz and feldspar."
        },
        {
            "p": "Pegmatites, igneous rocks whose crystals can grow longer than a person is tall, usually share this rock’s chemistry. A “graphic” variety of this rock has angular crystals growing through each other in patterns that look like ancient cuneiform writing.",
            "r": "Heat and pressure can transform this rock into banded gneiss [“NICE”]. For 10 points, name this rock that makes up much of the continental crust."
        },
        {
            "p": "Scotland’s third-largest city, Aberdeen, is nicknamed for this rock because so many of its buildings were made from a sparkling gray kind of it quarried nearby. Many curling stones are also cut from this rock on the Scottish island of Ailsa Craig.",
            "r": "Continental crust rich in this rock is less dense than the ocean floor’s basalt, so it resists sinking at subduction zones. For 10 points, name this light-colored rock used for many kitchen countertops."
        },
        {
            "p": "Plymouth Rock, which marks where the Pilgrims are said to have stepped ashore in 1620, is a boulder of this rock that an ice-age glacier carried and dropped. Geologists date this rock by measuring how much uranium in its tiny zircon crystals has turned into lead.",
            "r": "Its fine-grained volcanic cousin is rhyolite. For 10 points, name this coarse-grained igneous rock made mostly of quartz and feldspar."
        },
        {
            "p": "Followers of Abraham Werner, called Neptunists, believed this rock was the oldest of all, crystallized out of a vast ocean that once covered Earth. Modern geologists instead sort it into “I-type” and “S-type” kinds based on which rocks melted to form its magma.",
            "r": "Its potassium feldspar can tint it pink, while specks of biotite mica make dark spots. For 10 points, name this coarse-grained rock that makes up much of the continental crust."
        },
        {
            "p": "This rock is built from some of the last minerals to crystallize in Bowen’s reaction series, such as potassium feldspar and muscovite mica. Heat and pressure can metamorphose this rock into a banded rock called gneiss [“NICE”].",
            "r": "New Hampshire’s nickname comes from this rock. For 10 points, name this coarse-grained igneous rock found in many kitchen countertops and gravestones."
        }
    ],
    "clues": [
        {
            "id": "coarse-intrusive",
            "tier": "giveaway",
            "t": "A coarse-grained intrusive igneous rock that forms when silica-rich magma cools slowly deep underground",
            "k": ["coarse-grained", "intrusive", "cools slowly"],
            "n": 0,
            "rabbit": "Igneous rocks"
        },
        {
            "id": "quartz-feldspar",
            "tier": "giveaway",
            "t": "Made mostly of quartz and feldspar, usually with a little mica or hornblende",
            "k": ["quartz", "feldspar", "mica"],
            "n": 0,
            "rabbit": "Feldspar"
        },
        {
            "id": "countertops",
            "tier": "giveaway",
            "t": "A hard, light-colored rock used for kitchen countertops, gravestones, and monuments",
            "k": ["countertops", "gravestones", "light-colored"],
            "n": 0
        },
        {
            "id": "continental-crust",
            "tier": "giveaway",
            "t": "Along with similar rocks, it makes up much of the continental crust",
            "k": ["continental crust"],
            "n": 0
        },
        {
            "id": "rhyolite",
            "tier": "middle",
            "t": "Rhyolite is its fine-grained volcanic twin, made from the same kind of magma erupting at the surface",
            "k": ["rhyolite", "fine-grained", "volcanic twin"],
            "n": 0
        },
        {
            "id": "gneiss",
            "tier": "middle",
            "t": "Heat and pressure can metamorphose it into banded gneiss [“NICE”]",
            "k": ["gneiss", "banded", "metamorphose"],
            "n": 0
        },
        {
            "id": "felsic",
            "tier": "middle",
            "t": "Called felsic, a word blending “feldspar” and “silica,” because it is rich in both",
            "k": ["felsic", "silica"],
            "n": 0
        },
        {
            "id": "bowen",
            "tier": "middle",
            "t": "Its minerals are among the last to crystallize in Bowen’s reaction series, like potassium feldspar, muscovite, and quartz",
            "k": ["bowen’s reaction series", "bowens reaction series", "muscovite", "crystallize"],
            "n": 0,
            "rabbit": "Bowen’s reaction series"
        },
        {
            "id": "pink-specks",
            "tier": "middle",
            "t": "Potassium feldspar can tint it pink, while biotite mica or hornblende makes its dark specks",
            "k": ["pink", "biotite", "hornblende", "potassium feldspar"],
            "n": 0
        },
        {
            "id": "rushmore",
            "tier": "middle",
            "t": "Mount Rushmore’s four presidential faces are carved into it",
            "k": ["mount rushmore", "rushmore"],
            "n": 0,
            "rabbit": "Mount Rushmore"
        },
        {
            "id": "new-hampshire",
            "tier": "middle",
            "t": "New Hampshire’s nickname comes from it, and it is that state’s official state rock",
            "k": ["new hampshire", "nickname", "state rock"],
            "n": 0
        },
        {
            "id": "weathering",
            "tier": "middle",
            "t": "When its feldspar weathers into clay, its hard quartz grains are left behind as sand",
            "k": ["clay", "sand", "weathers"],
            "n": 0,
            "rabbit": "Sand"
        },
        {
            "id": "less-dense",
            "tier": "middle",
            "t": "Less dense than the ocean floor’s basalt, so continental crust rich in it rides higher and resists sinking at subduction zones",
            "k": ["less dense", "basalt", "subduction"],
            "n": 0,
            "rabbit": "Basalt"
        },
        {
            "id": "batholiths",
            "tier": "middle",
            "t": "Huge underground bodies of it are called batholiths, like the one at the heart of California’s Sierra Nevada",
            "k": ["batholiths", "sierra nevada"],
            "n": 0
        },
        {
            "id": "hutton",
            "tier": "power",
            "t": "In 1785, James Hutton found veins of it cutting into older rock at Glen Tilt, Scotland, showing it had once been molten",
            "k": ["hutton", "glen tilt", "veins"],
            "n": 0
        },
        {
            "id": "neptunists",
            "tier": "power",
            "t": "Abraham Werner’s Neptunists wrongly thought it was the oldest rock, crystallized out of a worldwide ocean",
            "k": ["neptunists", "werner"],
            "n": 0
        },
        {
            "id": "ailsa-craig",
            "tier": "power",
            "t": "Many curling stones are cut from it on Ailsa Craig, a tiny island off Scotland’s coast",
            "k": ["curling stones", "ailsa craig", "curling"],
            "n": 0
        },
        {
            "id": "aberdeen",
            "tier": "power",
            "t": "Aberdeen, Scotland’s third-largest city, is nicknamed for the sparkling gray kind used in many of its buildings",
            "k": ["aberdeen"],
            "n": 0
        },
        {
            "id": "aswan",
            "tier": "power",
            "t": "Egyptians quarried a red kind at Aswan for obelisks like Cleopatra’s Needles and for the Great Pyramid’s King’s Chamber",
            "k": ["aswan", "obelisks", "cleopatra’s needles", "king’s chamber"],
            "n": 0
        },
        {
            "id": "chappell-white",
            "tier": "power",
            "t": "In 1974, Bruce Chappell and Allan White sorted it into I-type and S-type, by whether igneous or sedimentary rock melted to make it",
            "k": ["i-type", "s-type", "chappell", "allan white"],
            "n": 0
        },
        {
            "id": "dartmoor",
            "tier": "power",
            "t": "Weathering carved blocky towers of it called tors on England’s Dartmoor, part of a huge buried body stretching through Cornwall",
            "k": ["tors", "dartmoor", "cornwall"],
            "n": 0
        },
        {
            "id": "uranium",
            "tier": "power",
            "t": "Traces of uranium in it decay into radioactive radon gas, and its zircon crystals are dated by uranium turning into lead",
            "k": ["uranium", "radon", "zircon"],
            "n": 0
        },
        {
            "id": "latin-grain",
            "tier": "power",
            "t": "Its name comes from the Latin word granum, meaning “grain”",
            "k": ["latin", "granum", "grain"],
            "n": 0
        },
        {
            "id": "el-capitan",
            "tier": "power",
            "t": "Climbers scale El Capitan, a giant cliff of it in Yosemite; curved sheets peel off its domes in a process called exfoliation",
            "k": ["el capitan", "yosemite", "exfoliation"],
            "n": 0
        },
        {
            "id": "texas",
            "tier": "power",
            "t": "The Texas State Capitol is built of “sunset red” blocks of it from near Marble Falls; Enchanted Rock is a giant pink dome of it",
            "k": ["texas state capitol", "enchanted rock", "marble falls"],
            "n": 0
        },
        {
            "id": "old-man",
            "tier": "power",
            "t": "New Hampshire’s Old Man of the Mountain, a face-shaped profile of its cliff ledges, was on a 2000 state quarter and collapsed in 2003",
            "k": ["old man of the mountain", "franconia notch", "2003"],
            "n": 0
        },
        {
            "id": "plymouth-rock",
            "tier": "power",
            "t": "Plymouth Rock is a boulder of it that an ice-age glacier carried and dropped",
            "k": ["plymouth rock", "glacier", "boulder"],
            "n": 0
        },
        {
            "id": "pegmatite-graphic",
            "tier": "power",
            "t": "Pegmatites, whose crystals can grow taller than a person, usually share its chemistry; its “graphic” variety looks like cuneiform writing",
            "k": ["pegmatites", "graphic", "cuneiform"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Granite, rhyolite, or gneiss?",
        "body": "Rhyolite has the same minerals as granite but cooled fast at the surface, so its crystals are too small to see. Gneiss [“NICE”] is what granite can become after heat and pressure squeeze it into bands, and granodiorite is a close cousin with more plagioclase feldspar; all three are different answer lines. Players also mix up granite with basalt, the dark rock of the ocean floor, or answer with one of granite’s minerals, quartz or feldspar.",
        "fix": "Coarse-grained, intrusive, light-colored, continental crust, countertops, and Mount Rushmore mean granite. Fine-grained and volcanic means rhyolite; banded and metamorphic means gneiss; dark, fine-grained, and ocean floor means basalt. Saying only “igneous rock” gets a prompt, so name the rock.",
        "line": "Real answer line: <b><u>Granite</u></b> (prompt on igneous rock or plutonic rock; do not accept “rhyolite,” “granodiorite,” or “gneiss”)"
    },
    "tests": {
        "right": ["Granite", "granites", "Granit", "pink granite", "granitic rock"],
        "prompt": ["igneous rock", "plutonic rock"],
        "wrong": ["Rhyolite", "Gneiss", "Basalt", "Granodiorite", "Quartz", "Feldspar"]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
