import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."


def C(cid, tier, t, k, rabbit=None):
    d = {"id": cid, "tier": tier, "t": t, "k": k, "n": 0}
    if rabbit:
        d["rabbit"] = rabbit
    return d


data = {
    "id": "gustav-kirchhoff",
    "name": "Gustav Kirchhoff",
    "mono": "GK",
    "category": "Physics",
    "qbCategory": "Science · Physics",
    "kicker": "German physicist · Circuit laws and the science of spectroscopy",
    "dates": "1824–1887",
    "briefing": "Gustav Kirchhoff was a German physicist who worked out two simple rules for electric circuits in 1845, while he was still a student. With the chemist Robert Bunsen, he showed that every element glows with its own pattern of colored lines, and the pair used that trick to discover cesium and rubidium and to learn what the Sun is made of. He also coined the term “black body” for a perfect absorber of light.",
    "answerHtml": "Gustav <b><u>Kirchhoff</u></b> (do not accept “Robert Bunsen”)",
    "accept": [
        "gustav kirchhoff",
        "kirchhoff",
        "gustav robert kirchhoff",
        "g r kirchhoff",
        "g kirchhoff"
    ],
    "prompt": [],
    "reject": [
        "robert bunsen",
        "bunsen",
        "bunsen burner",
        "kirchhoffs laws",
        "kirchhoffs law",
        "kirchhoff laws",
        "kirchhoff law",
        "kirchhoffs circuit laws",
        "kirchhoff circuit laws",
        "kirchhoffs rules",
        "kirchhoff rules",
        "kirchhoffs current law",
        "kirchhoff current law",
        "kirchhoffs voltage law",
        "kirchhoff voltage law",
        "kirchhoffs junction rule",
        "kirchhoffs loop rule",
        "kirchhoffs law of thermal radiation",
        "joseph von fraunhofer",
        "fraunhofer",
        "max planck",
        "planck",
        "georg ohm",
        "ohm",
        "ohms law",
        "hermann von helmholtz",
        "helmholtz",
        "franz neumann",
        "neumann",
        "wilhelm wien",
        "wien",
        "ludwig boltzmann",
        "boltzmann",
        "gustav hertz",
        "heinrich hertz",
        "hertz",
        "william crookes",
        "crookes",
        "black body radiation",
        "spectroscopy",
        "cesium",
        "caesium",
        "rubidium"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Gustav_Kirchhoff",
    "qb": {"q": "Kirchhoff", "found": 0, "tip": TIP},
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        {
            "p": "In 1857, this scientist calculated that an electric signal in a wire with no resistance would travel at about the speed of light. As a student at Königsberg [“KUR-nigs-bairg”], he had studied under Franz Neumann [“NOY-mahn”], and he later taught at Breslau, Heidelberg, and Berlin.",
            "r": "For 10 points, name this German physicist whose namesake circuit laws are the junction rule and the loop rule."
        },
        {
            "p": "This physicist coined the term “black body” for an object that absorbs all the light that falls on it. His law of thermal radiation says that, at the same temperature, a good absorber of light is also an equally good emitter of it.",
            "r": "For 10 points, name this German physicist who discovered cesium and rubidium with Robert Bunsen."
        },
        {
            "p": "In 1859, this scientist explained the dark Fraunhofer [“FROWN-hoh-fer”] lines in sunlight, showing that cooler gases absorb exactly the colors they give off when heated. He showed that sunlight passed through a sodium flame made the Sun’s dark D lines even darker.",
            "r": "For 10 points, name this German physicist who worked with Robert Bunsen and has namesake circuit laws."
        },
        {
            "p": "Max Planck succeeded this physicist as a professor of theoretical physics in Berlin and later solved his challenge to find how the glow of a black body depends on wavelength and temperature. This man had moved to Berlin in 1875 after about twenty years at Heidelberg.",
            "r": "For 10 points, name this German physicist known for both spectroscopy and electric circuit laws."
        },
        {
            "p": "In 1860, this scientist and a partner found a new element in mineral water from Dürkheim [“DUR-kime”] after spotting two blue lines in its spectrum, and they named it from the Latin for “sky blue.” A year later, they found a second element named from the Latin for “deep red.”",
            "r": "Those elements are cesium and rubidium. For 10 points, name this German physicist who worked with Robert Bunsen."
        },
        {
            "p": "In 1845, while still a university student, this scientist published two rules that extended Georg Ohm’s work to complicated networks. One rule follows from the conservation of electric charge, and the other follows from the conservation of energy.",
            "r": "For 10 points, name this German physicist whose namesake laws are used to analyze electric circuits."
        },
        {
            "p": "This physicist and his chemist partner passed the light from flames colored by different salts through a prism and found that each element always produces its own set of bright lines, whatever compound it is part of. They described that method of spectrum analysis in 1860.",
            "r": "That partner, Robert Bunsen, has a lab burner named for him. For 10 points, name this German physicist."
        },
        {
            "p": "This physicist found that many dark lines in sunlight line up exactly with bright lines given off by hot iron vapor, showing that the Sun contains iron. He mapped the Sun’s spectrum in great detail in the early 1860s.",
            "r": "He had earlier proved that the Sun contains sodium. For 10 points, name this German physicist who pioneered spectroscopy with Robert Bunsen."
        },
        {
            "p": "In 1877, this scientist and his longtime partner became the first two winners of the Royal Society’s Davy Medal. The two men had first met at the University of Breslau and later worked together for years at Heidelberg.",
            "r": "That partner was Robert Bunsen. For 10 points, name this German physicist known for laws of electric circuits."
        },
        {
            "p": "This physicist was born in 1824 in Königsberg [“KUR-nigs-bairg”], a Prussian city later renamed Kaliningrad, in Russia. He spent the last part of his career teaching theoretical physics in Berlin, where he died in 1887.",
            "r": "His junction rule says the current flowing into any point in a circuit equals the current flowing out. For 10 points, name this physicist."
        },
        {
            "p": "Using his law of thermal radiation, this physicist argued that the glow given off by a perfect absorber depends only on its temperature and the wavelength, not on what it is made of. Finding the exact formula for that glow became a famous challenge.",
            "r": "This physicist’s loop rule says the voltages around any closed loop in a circuit add up to zero. For 10 points, name this German physicist."
        },
        {
            "p": "According to this scientist’s three laws of spectroscopy, a hot, dense object gives off a continuous rainbow of colors, while a hot, thin gas gives off only bright lines. A cooler gas in front of a hot source makes dark lines instead.",
            "r": "For 10 points, name this German physicist whose other namesake laws describe electric circuits."
        },
        {
            "p": "This physicist’s diffraction formula put Christiaan Huygens’s [“HOY-gunz”] idea, that every point on a wave front acts as a source of new wavelets, on a firm mathematical footing. He also explained why the Sun’s spectrum has dark lines.",
            "r": "For 10 points, name this German physicist whose junction and loop rules help solve electric circuits."
        },
        {
            "p": "This physicist and his partner heated salts of lithium, sodium, potassium, calcium, and other metals in a hot, nearly colorless gas flame, recording the pattern of colored lines each one made. They found that even a tiny trace of sodium gives a bright yellow line.",
            "r": "The flame came from a burner named for his partner, Robert Bunsen. For 10 points, name this German physicist."
        },
        {
            "p": "The method of spectrum analysis that this physicist developed with a partner soon led others to new elements: William Crookes found thallium in 1861 by its bright green line, and astronomers spotted the yellow line of helium in sunlight in 1868.",
            "r": "For 10 points, name this German physicist who discovered cesium and rubidium with Robert Bunsen."
        }
    ],
    "clues": [
        C("circuit-laws", "giveaway", "Namesake circuit laws: the junction rule (current law) and the loop rule (voltage law)",
          ["circuit laws", "junction rule", "loop rule"], "Electric current"),
        C("bunsen", "giveaway", "Worked with the chemist Robert Bunsen to pioneer spectroscopy, identifying elements by their colored lines",
          ["robert bunsen", "spectroscopy", "colored lines"], "Robert Bunsen"),
        C("cesium-rubidium", "giveaway", "With Bunsen, discovered cesium (1860) and rubidium (1861)",
          ["cesium", "rubidium"]),
        C("german-physicist", "giveaway", "German physicist (1824–1887) known for both electric circuits and spectroscopy",
          ["german physicist", "1824"]),
        C("junction", "middle", "Junction rule: the current flowing into any point equals the current flowing out (conservation of charge)",
          ["junction", "conservation of charge"]),
        C("loop", "middle", "Loop rule: the voltages around any closed loop add up to zero (conservation of energy)",
          ["closed loop", "conservation of energy", "voltages"]),
        C("student-1845", "middle", "Published his circuit laws in 1845, while still a student, extending Ohm’s law to networks",
          ["1845", "student", "ohm’s law"]),
        C("fraunhofer", "middle", "In 1859, explained the Sun’s dark Fraunhofer lines: cooler gases absorb the same colors they give off when hot",
          ["fraunhofer", "1859", "cooler gases"]),
        C("sodium-sun", "middle", "Proved the Sun contains sodium: sunlight passed through a sodium flame made its dark D lines even darker",
          ["sodium flame", "d lines", "sodium"], "Sodium"),
        C("black-body", "middle", "Coined the term “black body” for an object that absorbs all the light that falls on it",
          ["black body", "absorbs all"], "Max Planck"),
        C("thermal-radiation", "middle", "His law of thermal radiation: at the same temperature, a good absorber is an equally good emitter",
          ["thermal radiation", "absorber", "emitter"]),
        C("three-laws", "middle", "Three laws of spectroscopy: hot, dense objects give continuous spectra; hot, thin gases give bright lines; cooler gas in front gives dark lines",
          ["three laws", "continuous", "bright lines"]),
        C("planck", "middle", "Max Planck succeeded him in Berlin and solved his black-body challenge in 1900",
          ["max planck", "berlin", "challenge"]),
        C("konigsberg", "power", "Born in 1824 in Königsberg, Prussia, a city later renamed Kaliningrad, in Russia",
          ["königsberg", "kaliningrad", "prussia"]),
        C("neumann", "power", "Studied under Franz Neumann at the University of Königsberg",
          ["franz neumann", "neumann"]),
        C("signal-speed", "power", "Calculated in 1857 that an electric signal in a wire with no resistance travels at about the speed of light",
          ["speed of light", "1857", "signal"]),
        C("universal-glow", "power", "Argued that a black body’s glow depends only on its temperature and the wavelength, not on what it is made of",
          ["temperature and the wavelength", "glow"]),
        C("spectrum-analysis", "power", "Spectrum analysis (1860): with Bunsen, showed each element always gives its own bright lines, whatever compound it is in",
          ["spectrum analysis", "compound", "1860"]),
        C("sky-blue", "power", "Cesium is named from the Latin for “sky blue” and rubidium from the Latin for “deep red,” after their spectral lines",
          ["sky blue", "deep red", "latin"]),
        C("davy-medal", "power", "He and Bunsen were the first winners of the Royal Society’s Davy Medal (1877)",
          ["davy medal", "1877", "royal society"]),
        C("heidelberg", "power", "Met Bunsen at Breslau, worked with him at Heidelberg (1854–1875), then moved to Berlin",
          ["breslau", "heidelberg", "1875"]),
        C("iron-sun", "power", "Matched many dark lines in sunlight to the bright lines of hot iron vapor, and mapped the Sun’s spectrum in the early 1860s",
          ["iron vapor", "iron", "early 1860s"]),
        C("new-elements", "power", "Spectrum analysis soon revealed thallium (Crookes, 1861) and helium in the Sun (1868), years before helium was found on Earth",
          ["thallium", "helium", "1868"], "Helium"),
        C("huygens", "power", "His diffraction formula put Huygens’s idea of wavelets on a firm mathematical footing",
          ["diffraction formula", "huygens", "wavelets"], "Diffraction"),
        C("flame-tests", "power", "Heated salts of lithium, sodium, potassium, and calcium in a nearly colorless flame; a tiny trace of sodium gives a bright yellow line",
          ["nearly colorless", "yellow line", "salts"])
    ],
    "trap": {
        "title": "The physicist, not Bunsen",
        "body": "Gustav Kirchhoff and the chemist Robert Bunsen worked as a team, so spectroscopy clues, the Sun’s dark lines, and the discovery of cesium and rubidium fit both men, and this page does not accept “Bunsen.” Kirchhoff’s circuit laws are also their own answer line, so if a question asks for “these laws,” say “Kirchhoff’s laws,” not just his name.",
        "fix": "Circuit laws, the junction and loop rules, black bodies, and the law of thermal radiation point to Kirchhoff; the gas burner, arsenic compounds, batteries, and geysers point to Bunsen. If the question asks for “this physicist,” give the person.",
        "line": "Real answer line: Gustav <b><u>Kirchhoff</u></b> (do not accept “Robert Bunsen”)"
    },
    "tests": {
        "right": [
            "Gustav Kirchhoff",
            "Kirchhoff",
            "Kirchoff",
            "Gustav Kirchhof",
            "Gustav Robert Kirchhoff"
        ],
        "prompt": [],
        "wrong": [
            "Robert Bunsen",
            "Kirchhoff's laws",
            "Joseph von Fraunhofer",
            "Georg Ohm",
            "Max Planck"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
