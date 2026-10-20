import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."


def C(cid, tier, t, k, rabbit=None):
    d = {"id": cid, "tier": tier, "t": t, "k": k, "n": 0}
    if rabbit:
        d["rabbit"] = rabbit
    return d


LINE = "<b><u>simple machines</u></b> (accept <u>simple machine</u>; prompt on <u>machines</u>; do not accept a single machine such as “lever” or “pulley”)"

data = {
    "id": "simple-machines",
    "name": "Simple machines",
    "mono": "SM",
    "category": "Physics",
    "qbCategory": "Science · Physics",
    "kicker": "Six basic devices that multiply force · Levers, pulleys, ramps, and more",
    "dates": "Five listed by Hero of Alexandria, 1st century CE",
    "briefing": "Simple machines are the six basic devices that make work easier: the lever, wheel and axle, pulley, inclined plane, wedge, and screw. None of them gives you free energy; instead, they trade force for distance, letting you lift a heavy load with a small push over a longer path. The Greek scientist Archimedes studied levers and pulleys and is said to have boasted, “Give me a place to stand, and I will move the Earth.”",
    "answerHtml": LINE,
    "accept": [
        "simple machines",
        "simple machine",
        "six simple machines",
        "classical simple machines",
        "classical simple machine",
        "the simple machines"
    ],
    "prompt": [
        "machines",
        "machine",
        "basic machines",
        "mechanical devices"
    ],
    "reject": [
        "lever",
        "levers",
        "pulley",
        "pulleys",
        "inclined plane",
        "inclined planes",
        "ramp",
        "ramps",
        "wedge",
        "wedges",
        "screw",
        "screws",
        "wheel and axle",
        "wheels and axles",
        "compound machine",
        "compound machines",
        "complex machine",
        "complex machines",
        "mechanical advantage",
        "fulcrum",
        "torque",
        "work",
        "gear",
        "gears",
        "block and tackle",
        "archimedes screw",
        "turing machine",
        "perpetual motion machine",
        "rube goldberg machine"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Simple_machine",
    "qb": {"q": "simple machines", "found": 0, "tip": TIP},
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        {
            "p": "Hero of Alexandria listed five of these devices in his _Mechanics_, and Renaissance scientists later added a sixth to make the classic set. Archimedes [“ar-kih-MEE-deez”] is said to have boasted about one of them, “Give me a place to stand, and I will move the Earth.”",
            "r": "For 10 points, name these basic devices, such as the lever and the pulley, that change the size or direction of a force."
        },
        {
            "p": "Simon Stevin [“STAY-vin”] explained one of these devices by imagining a loop of beads draped over a triangular block, a picture called the “wreath of spheres.” Another of these devices is just a sloping surface wrapped around a cylinder, and a third is two sloping surfaces placed back to back.",
            "r": "For 10 points, name these six devices, which include the screw, the wedge, and the inclined plane."
        },
        {
            "p": "According to Plutarch, Archimedes used a combination of one kind of these devices to move a fully loaded ship all by himself. A block and tackle, built from several of that same kind of device, has an ideal mechanical advantage equal to the number of rope segments holding up the load.",
            "r": "For 10 points, name these devices, including the lever and the pulley, that make work easier."
        },
        {
            "p": "The shaduf [“shah-DOOF”], used to lift irrigation water in ancient Egypt, is a pole with a counterweight that acts as one of these devices. That device comes in three classes, depending on whether the fulcrum, the load, or the effort sits in the middle.",
            "r": "For 10 points, name these basic devices, which also include the wheel and axle and the inclined plane."
        },
        {
            "p": "The ideal mechanical advantage of one of these devices equals the radius of its wheel divided by the radius of its axle, and for another, it equals the length of a ramp divided by its height. In both cases, that ratio tells how many times the device multiplies the force you apply.",
            "r": "For 10 points, name these six devices, such as levers and pulleys, that trade force for distance."
        },
        {
            "p": "A spiral inside a tube, named for Archimedes, raises water when it is turned, and Archimedes also worked out a law describing how one of these devices balances. Mechanical advantage, the output force divided by the input force, measures how much one of these devices multiplies a force.",
            "r": "For 10 points, name these basic devices, including the wedge, the screw, and the lever."
        },
        {
            "p": "The distance between neighboring threads on one of these devices is called its pitch, and finer threads give that device a greater mechanical advantage. Another of these devices splits wood or holds a door open and is really two ramps placed back to back.",
            "r": "For 10 points, name these six devices, which also include the pulley and the lever."
        },
        {
            "p": "A single fixed version of one of these devices changes only the direction of a force, while a single movable version of it cuts the force needed to lift a load in half. Flagpoles use the fixed version to raise a flag by pulling down on a rope.",
            "r": "For 10 points, name these devices, such as the pulley, the lever, and the inclined plane."
        },
        {
            "p": "Your forearm acts as a third-class version of one of these devices, with the elbow as the pivot and the biceps pulling in between. Seesaws, wheelbarrows, and tweezers are examples of that same device, each of a different class.",
            "r": "For 10 points, name these six basic devices, which include the lever and the screw."
        },
        {
            "p": "A hand-held can opener combines several of these devices, using a turning handle and a sharp cutting wheel. Scissors are two of one kind of these devices joined at a pivot, with blades that act as another kind.",
            "r": "For 10 points, name these basic devices, such as the lever and the wedge, that make work easier."
        },
        {
            "p": "The ideal mechanical advantage of any of these devices equals the distance the effort moves divided by the distance the load moves. The efficiency of one of these devices is its useful work output divided by its work input, and friction keeps every real one below 100 percent.",
            "r": "For 10 points, name these six devices, including the pulley and the wheel and axle."
        },
        {
            "p": "A windlass, which winds up a rope to raise a bucket from a well, is one of these devices, as are a doorknob and a screwdriver handle. In that device, a large turning part multiplies the force on a smaller rod at its center.",
            "r": "For 10 points, name these six basic devices, which include the wheel and axle and the pulley."
        },
        {
            "p": "The ancient Egyptians are thought to have used long ramps, one of these devices, to drag heavy stone blocks up the pyramids. A longer, gentler ramp needs less force to push a load up, but the load must travel farther.",
            "r": "For 10 points, name these six devices, including the inclined plane, the lever, and the screw."
        },
        {
            "p": "For one of these devices, the ideal mechanical advantage equals the length of the effort arm divided by the length of the load arm, a rule worked out by Archimedes. Moving the pivot of that device closer to the load makes the load easier to lift.",
            "r": "For 10 points, name these basic devices, such as the lever, that make work easier."
        },
        {
            "p": "A zipper’s slider uses small versions of one of these devices to push its teeth together and pry them apart. Axes, knives, and chisels are also examples of that device, which has two sloping sides that meet at a sharp edge.",
            "r": "For 10 points, name these six devices, including the wedge and the pulley, that change the size or direction of a force."
        }
    ],
    "clues": [
        C("six", "giveaway", "The six classic ones: lever, wheel and axle, pulley, inclined plane, wedge, and screw", ["lever", "pulley", "inclined plane", "wedge", "screw"]),
        C("force", "giveaway", "Make work easier by changing the size or direction of a force", ["size or direction", "force"]),
        C("trade", "giveaway", "They trade force for distance; they never reduce the total work needed for a job", ["force for distance", "total work"], "Work (physics)"),
        C("compound", "giveaway", "Two or more working together form a compound machine, such as a bicycle, scissors, or a can opener", ["compound machine", "bicycle", "scissors"]),
        C("ma", "middle", "Mechanical advantage = output force ÷ input force: how many times a device multiplies your force", ["mechanical advantage", "output force"]),
        C("lever-classes", "middle", "Levers come in three classes, depending on whether the fulcrum, the load, or the effort is in the middle", ["three classes", "fulcrum"], "Torque"),
        C("lever-examples", "middle", "First class: a seesaw; second class: a wheelbarrow; third class: tweezers or your forearm (the biceps pulls between elbow and hand)", ["seesaw", "wheelbarrow", "tweezers", "forearm"]),
        C("screw-wedge", "middle", "A screw is an inclined plane wrapped around a cylinder; a wedge is two inclined planes placed back to back", ["wrapped around", "back to back"]),
        C("pulleys", "middle", "A single fixed pulley only changes a force’s direction (as on a flagpole); a single movable pulley cuts the force needed in half", ["fixed pulley", "movable pulley", "flagpole"]),
        C("efficiency", "middle", "Efficiency = work output ÷ work input; friction keeps every real one below 100 percent", ["efficiency", "friction", "100 percent"], "Friction"),
        C("archimedes-quote", "middle", "Archimedes is said to have boasted, “Give me a place to stand, and I will move the Earth”", ["archimedes", "place to stand"]),
        C("wheel-axle", "middle", "A doorknob, a screwdriver handle, a steering wheel, and a windlass are all wheels and axles", ["doorknob", "windlass", "steering wheel"]),
        C("wedge-examples", "middle", "Axes, knives, chisels, and doorstops are all wedges", ["axes", "chisels", "doorstops"]),
        C("ramp", "middle", "A longer, gentler ramp needs less force to push a load up, but the load travels farther", ["gentler ramp", "farther"]),
        C("hero", "power", "Hero (or Heron) of Alexandria listed five in his _Mechanics_: the lever, windlass, pulley, wedge, and screw", ["hero of alexandria", "heron", "windlass"]),
        C("renaissance", "power", "Renaissance scientists added the inclined plane to Hero’s five, making the classic six", ["renaissance", "classic six"]),
        C("plutarch", "power", "According to Plutarch, Archimedes used linked pulleys to move a fully loaded ship by himself", ["plutarch", "ship"]),
        C("block-tackle", "power", "A block and tackle’s ideal mechanical advantage equals the number of rope segments holding up the load", ["block and tackle", "rope segments"]),
        C("stevin", "power", "Simon Stevin explained the inclined plane with a loop of beads draped over a triangular block, the “wreath of spheres”", ["stevin", "wreath of spheres"]),
        C("shaduf", "power", "The shaduf, a pole with a counterweight that works as a lever, lifted irrigation water in ancient Egypt", ["shaduf", "shadoof", "irrigation"]),
        C("ima-wheel", "power", "Ideal mechanical advantage of a wheel and axle = the wheel’s radius ÷ the axle’s radius", ["radius", "wheel and axle"]),
        C("ima-ramp", "power", "Ideal mechanical advantage of an inclined plane = the ramp’s length ÷ its height", ["length", "height"]),
        C("ima-distance", "power", "Ideal mechanical advantage of any of them = the distance the effort moves ÷ the distance the load moves", ["effort moves", "load moves"]),
        C("ima-lever", "power", "For a lever, ideal mechanical advantage = effort arm ÷ load arm, so moving the pivot closer to the load makes lifting easier", ["effort arm", "load arm"]),
        C("pitch", "power", "The distance between a screw’s threads is its pitch; finer threads give a greater mechanical advantage", ["pitch", "threads"]),
        C("archimedes-screw", "power", "The Archimedes screw, a spiral inside a tube, raises water when it is turned", ["archimedes screw", "spiral"]),
        C("law-of-lever", "power", "Archimedes worked out the law of the lever, which tells how a lever balances", ["law of the lever", "balances"]),
        C("pyramids", "power", "The ancient Egyptians are thought to have used long ramps to drag stone blocks up the pyramids", ["pyramids", "egyptians"]),
        C("zipper", "power", "A zipper’s slider uses small wedges to push its teeth together and pry them apart", ["zipper", "slider"])
    ],
    "trap": {
        "title": "The group, not one",
        "body": "These tossups ask for the whole group, so naming one member, like “lever” or “pulley,” is wrong even if the clue you buzzed on was about that one device. Real quiz bowl also writes separate tossups on single machines (the lever, the pulley, the screw, the inclined plane), so the giveaway decides: “these six devices” means the group, while “this device” wants just one. Torque and mechanical advantage are related answers too.",
        "fix": "If the question says “these devices” or lists several (lever, pulley, wedge…), say “simple machines.” If it says “this device” with a fulcrum or three classes, say “lever”; a rope over a grooved wheel, “pulley”; a ramp, “inclined plane”; threads and pitch, “screw.” For “output force divided by input force,” say “mechanical advantage.”",
        "line": "Real answer line: " + LINE
    },
    "tests": {
        "right": [
            "Simple machines",
            "simple machine",
            "Simpel machines",
            "The six simple machines"
        ],
        "prompt": [
            "Machines",
            "machine"
        ],
        "wrong": [
            "Lever",
            "Pulley",
            "Inclined plane",
            "Compound machine",
            "Mechanical advantage",
            "Torque"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
