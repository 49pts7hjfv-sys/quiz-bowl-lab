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
    "id": "millikan-oil-drop-experiment",
    "name": "Millikan oil drop experiment",
    "mono": "OD",
    "category": "Physics",
    "qbCategory": "Science · Physics",
    "kicker": "The 1909 measurement of the electron’s charge · Proved charge comes in units",
    "dates": "First performed 1909",
    "briefing": "In 1909, Robert Millikan and his student Harvey Fletcher sprayed a fine mist of oil between two metal plates at the University of Chicago. By adjusting the voltage on the plates until a charged droplet hung still in midair, they could work out the electric charge it carried. Every charge they measured was a whole-number multiple of one tiny amount, about 1.6 × 10⁻¹⁹ coulombs: the charge of a single electron.",
    "answerHtml": "<b><u>Millikan oil drop</u></b> experiment (accept <u>oil drop</u> experiment; prompt on <u>Millikan</u>; do not accept “cathode ray tube” or “J. J. Thomson”)",
    "accept": [
        "millikan oil drop experiment",
        "millikans oil drop experiment",
        "millikan oil drop",
        "millikans oil drop",
        "oil drop experiment",
        "oil drop experiments",
        "oil drop",
        "oil drops",
        "oil droplet experiment",
        "millikan oil droplet experiment"
    ],
    "prompt": [
        "millikan",
        "millikans",
        "robert millikan",
        "millikan experiment",
        "millikans experiment"
    ],
    "reject": [
        "cathode ray tube",
        "cathode ray tubes",
        "cathode ray",
        "cathode rays",
        "cathode ray experiment",
        "crt",
        "j j thomson",
        "jj thomson",
        "thomson",
        "thomson experiment",
        "thomsons experiment",
        "plum pudding model",
        "gold foil experiment",
        "rutherford gold foil experiment",
        "geiger marsden experiment",
        "michelson morley experiment",
        "michelson morley",
        "cavendish experiment",
        "double slit experiment",
        "photoelectric effect",
        "photoelectric experiment",
        "stern gerlach experiment",
        "franck hertz experiment",
        "cloud chamber",
        "wilson cloud chamber",
        "electron",
        "electrons",
        "electric charge",
        "elementary charge",
        "charge",
        "electric field",
        "stokes law",
        "harvey fletcher",
        "fletcher",
        "faraday",
        "faradays ice pail experiment",
        "leyden jar",
        "van de graaff generator",
        "coulombs law",
        "electroscope"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Oil_drop_experiment",
    "qb": {"q": "oil drop", "found": 0, "tip": TIP},
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        {
            "p": "Felix Ehrenhaft [“AIR-en-hahft”] of Vienna disputed this experiment’s results, claiming to find “subelectrons” with even smaller charges. Decades later, historians studying the lab notebooks of this experiment’s leader found that he had left out many measurements from his famous 1913 paper.",
            "r": "For 10 points, name this experiment that measured the charge of the electron using tiny charged droplets."
        },
        {
            "p": "In a 1974 speech, Richard Feynman described how later measurements of the value found in this experiment crept upward only slowly, because scientists hesitated to report numbers far from it. Its value came out slightly low because it used a wrong value for the viscosity of air.",
            "r": "For 10 points, name this 1909 experiment that measured the electron’s charge by suspending charged droplets between two metal plates."
        },
        {
            "p": "To find the weight of each droplet in this experiment, its scientists timed how fast the droplet fell with the voltage on the plates switched off and then used Stokes’ law to work out its size from that speed.",
            "r": "For 10 points, name this experiment that showed electric charge comes in whole-number multiples of the electron’s charge."
        },
        {
            "p": "Before this experiment, J. J. Thomson, John Townsend, and H. A. Wilson had estimated the electron’s charge by timing how fast whole clouds of tiny water droplets fell, but those droplets evaporated too quickly.",
            "r": "This experiment instead watched single droplets one at a time. For 10 points, name this 1909 experiment that measured the charge of the electron."
        },
        {
            "p": "Harvey Fletcher worked on this experiment as a graduate student, but the key 1910 paper on its results listed only his professor as the author. Fletcher’s own account of their work was published in 1982, after his death.",
            "r": "For 10 points, name this experiment, performed at the University of Chicago, that measured the charge of a single electron."
        },
        {
            "p": "When X-rays struck the air inside this experiment’s chamber, a droplet could gain or lose charge, and its speed then changed by a whole step, never by part of a step.",
            "r": "That showed that charge is quantized. For 10 points, name this experiment whose result, about 1.6 times ten to the minus nineteen coulombs, is the charge of one electron."
        },
        {
            "p": "Inside this experiment’s apparatus, an atomizer sprayed a fine mist, and a few droplets drifted down through a tiny hole into the space below. A bright light made the droplets look like tiny stars against a dark background.",
            "r": "For 10 points, name this experiment that balanced charged droplets in an electric field to find the charge of the electron."
        },
        {
            "p": "Combining this experiment’s result with J. J. Thomson’s charge-to-mass ratio let scientists calculate the mass of the electron. Combining it with the Faraday constant gave a much better value of Avogadro’s number.",
            "r": "For 10 points, name this 1909 experiment that measured the elementary charge using tiny charged droplets between two plates."
        },
        {
            "p": "The scientist who led this experiment won the 1923 Nobel Prize in Physics, partly for this work and partly for testing Albert Einstein’s equation for the photoelectric effect. He had expected those tests to prove Einstein wrong.",
            "r": "For 10 points, name this experiment that measured the charge of the electron by balancing tiny charged droplets."
        },
        {
            "p": "Physicists have run automated versions of this experiment on huge numbers of droplets, searching for free particles with one-third of the usual charge, such as lone quarks, without finding any. Quarks carry one-third or two-thirds of the electron’s charge.",
            "r": "For 10 points, name this 1909 experiment that first precisely measured the charge of a single electron."
        },
        {
            "p": "The leader of this experiment later headed the California Institute of Technology and popularized the name “cosmic rays” for high-energy radiation from space. He moved there from the University of Chicago in 1921.",
            "r": "For 10 points, name this experiment that measured the charge of the electron by watching tiny charged droplets."
        },
        {
            "p": "This experiment’s 1913 paper reported that every charge it measured was a whole-number multiple of one basic unit, named in the paper’s title as the “elementary electrical charge.”",
            "r": "That unit is the charge of one electron. For 10 points, name this experiment that balanced tiny charged droplets between two metal plates."
        },
        {
            "p": "In its full form, this experiment timed each droplet twice: falling under gravity with the field off, and rising with the field switched on and pulling it upward.",
            "r": "In the simpler textbook version, a droplet hangs still when the electric force balances its weight. For 10 points, name this experiment that measured the electron’s charge."
        },
        {
            "p": "Each droplet in this experiment quickly stopped speeding up as it fell, once the push of the air balanced its weight, so its scientists could time its steady speed with a stopwatch. That steady speed is called terminal velocity.",
            "r": "For 10 points, name this experiment that showed electric charge comes in units of about 1.6 times ten to the minus nineteen coulombs."
        },
        {
            "p": "This experiment’s leader first tried water, but the tiny water droplets evaporated too quickly to be timed for long, so he switched to a liquid that evaporates very slowly.",
            "r": "For 10 points, name this experiment that measured the charge of the electron, performed at the University of Chicago in 1909."
        }
    ],
    "clues": [
        C("electron-charge", "giveaway", "Measured the charge of a single electron, about 1.6 × 10⁻¹⁹ coulombs",
          ["charge", "electron", "coulombs"], "Electric charge"),
        C("chicago-1909", "giveaway", "Performed in 1909 at the University of Chicago by Robert Millikan and his student Harvey Fletcher",
          ["1909", "university of chicago", "harvey fletcher"]),
        C("balance", "giveaway", "Balanced tiny charged droplets between two metal plates by adjusting the voltage (the electric field)",
          ["balanced", "metal plates", "voltage"], "Electric field"),
        C("quantized", "giveaway", "Showed that charge comes only in whole-number multiples of one basic unit: charge is quantized",
          ["whole-number multiples", "quantized"]),
        C("weight-balance", "middle", "A droplet hangs still when the upward electric force equals its weight (charge = weight ÷ field)",
          ["upward electric force", "weight"]),
        C("atomizer", "middle", "An atomizer sprayed a fine mist; a few droplets drifted through a tiny hole into the space below",
          ["atomizer", "mist", "tiny hole"]),
        C("x-rays", "middle", "X-rays changed a droplet’s charge, and its speed changed by whole steps, never by part of a step",
          ["x-rays", "whole steps"]),
        C("terminal", "middle", "Each falling droplet quickly reached a steady speed (terminal velocity), timed with a stopwatch",
          ["terminal velocity", "stopwatch"], "Drag (physics)"),
        C("stokes", "middle", "Stokes’ law turned a droplet’s steady falling speed into its size and weight",
          ["stokes’ law", "falling speed"], "Viscosity"),
        C("nobel-1923", "middle", "Its leader won the 1923 Nobel Prize in Physics, partly for it and partly for testing Einstein’s photoelectric equation",
          ["1923", "nobel prize", "photoelectric"]),
        C("thomson-mass", "middle", "With J. J. Thomson’s charge-to-mass ratio (1897), its result gave the electron’s mass",
          ["charge-to-mass ratio", "thomson"], "Electrons"),
        C("avogadro", "power", "With the Faraday constant, its result gave a much better value of Avogadro’s number",
          ["faraday constant", "avogadro’s number"], "Avogadro’s number"),
        C("slow-evaporating", "power", "Water droplets evaporated too fast, so its leader switched to a slowly evaporating liquid",
          ["evaporated", "slowly evaporating", "water droplets"]),
        C("clouds", "power", "Earlier, Thomson, John Townsend, and H. A. Wilson timed whole falling clouds of water droplets",
          ["clouds", "townsend", "h. a. wilson"]),
        C("ehrenhaft", "power", "Felix Ehrenhaft of Vienna disputed it, claiming to find smaller “subelectrons”",
          ["ehrenhaft", "subelectrons", "vienna"]),
        C("notebooks", "power", "Historians studying its leader’s notebooks found he left many measurements out of his 1913 paper",
          ["notebooks", "1913", "measurements"]),
        C("feynman", "power", "Richard Feynman’s 1974 “cargo cult science” speech told how later values crept up only slowly from its result",
          ["feynman", "cargo cult", "1974"], "Richard Feynman"),
        C("viscosity-air", "power", "Its value came out slightly low because it used a wrong value for the viscosity of air",
          ["viscosity of air", "slightly low"]),
        C("fletcher-1982", "power", "Fletcher’s own account was published in 1982, after his death; the key 1910 paper listed only his professor",
          ["1982", "account", "1910"]),
        C("stars", "power", "Lit by a bright lamp, the droplets looked like tiny stars against a dark background",
          ["stars", "dark background"]),
        C("rise-fall", "power", "Its full method timed each droplet falling with the field off and rising with the field on",
          ["rising", "field off"]),
        C("quarks", "power", "Automated versions have searched huge numbers of droplets for one-third charges, like lone quarks, without finding any",
          ["quarks", "one-third", "automated"], "Quarks"),
        C("caltech", "power", "Its leader later headed Caltech and popularized the name “cosmic rays”",
          ["caltech", "cosmic rays"]),
        C("elementary", "power", "Its 1913 paper’s title calls the basic unit the “elementary electrical charge”",
          ["elementary electrical charge"])
    ],
    "trap": {
        "title": "The experiment, not the particle",
        "body": "Tossups on this experiment are full of clues about electrons and electric charge, which are separate answer lines. J. J. Thomson’s cathode ray tube is a different famous experiment: it discovered the electron in 1897, while this one measured the electron’s charge. The Michelson–Morley experiment is another famous American experiment whose name starts with “Mi-.”",
        "fix": "Droplets, an atomizer, two charged plates, hovering, and 1.6 × 10⁻¹⁹ coulombs point to this experiment. A glowing beam bent by magnets and the charge-to-mass ratio point to Thomson; light beams and the aether point to Michelson–Morley. Saying just “Millikan” earns a prompt, so add “oil drop experiment.”",
        "line": "Real answer line: <b><u>Millikan oil drop</u></b> experiment (accept <u>oil drop</u> experiment; prompt on <u>Millikan</u>; do not accept “cathode ray tube” or “J. J. Thomson”)"
    },
    "tests": {
        "right": [
            "Millikan oil drop experiment",
            "Oil drop experiment",
            "Millikan's oil drop experiment",
            "Milikan oil drop experiment",
            "oil drop"
        ],
        "prompt": [
            "Millikan",
            "Robert Millikan"
        ],
        "wrong": [
            "Cathode ray tube",
            "J. J. Thomson",
            "Michelson-Morley experiment",
            "Gold foil experiment",
            "Electron"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
