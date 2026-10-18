import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "momentum",
    "name": "Momentum",
    "mono": "MV",
    "category": "Physics",
    "qbCategory": "Science · Physics",
    "kicker": "Mass times velocity · Conserved when objects collide",
    "dates": "Newton’s “quantity of motion,” 1687",
    "briefing": "Momentum is mass in motion: multiply an object’s mass by its velocity and you get its momentum, which is why a slow-rolling bowling ball is harder to stop than a speeding ping-pong ball. In a collision, the total momentum stays the same as long as no outside force interferes. That rule explains why a skater who throws a heavy ball rolls backward, and how rockets push themselves through empty space.",
    "answerHtml": "<b><u>Momentum</u></b> (accept <u>linear momentum</u>; prompt on <u>p</u>; do not accept “angular momentum”)",
    "accept": [
        "momentum",
        "momenta",
        "linear momentum",
        "conservation of momentum",
        "law of conservation of momentum",
        "conservation of linear momentum",
        "translational momentum"
    ],
    "prompt": [
        "p"
    ],
    "reject": [
        "angular momentum",
        "rotational momentum",
        "moment of momentum",
        "moment",
        "moment of inertia",
        "impulse",
        "inertia",
        "kinetic energy",
        "energy",
        "velocity",
        "mass",
        "force",
        "torque"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Momentum",
    "qb": {
        "q": "momentum",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In his 1924 thesis, Louis de Broglie [“duh BROY”] proposed that any particle has a wavelength equal to Planck’s constant divided by this quantity. Werner Heisenberg’s uncertainty principle says that this quantity and position cannot both be known exactly at the same time.",
            "r": "For 10 points, name this quantity, equal to mass times velocity, that is conserved in collisions."
        },
        {
            "p": "Arthur Compton won a Nobel Prize after showing in 1923 that X-ray photons bounce off electrons like billiard balls, handing over some of their energy and this quantity. In that Compton effect, the scattered X-rays come out with longer wavelengths.",
            "r": "It is conserved in collisions. For 10 points, name this quantity, equal to mass times velocity for everyday objects."
        },
        {
            "p": "Emmy Noether’s [“NUR-terz”] theorem shows that the conservation of this quantity comes from the fact that the laws of physics are the same everywhere in space. In Hamiltonian mechanics, this quantity is paired with position as its “conjugate” variable.",
            "r": "The total amount of it stays the same when two carts collide on a track. For 10 points, name this quantity, symbolized p, which equals mass times velocity."
        },
        {
            "p": "Konstantin Tsiolkovsky’s [“tsee-ul-KOF-skeez”] 1903 rocket equation comes from applying the conservation of this quantity to a rocket that throws exhaust out its back. Because of that conservation law, a rocket can speed up in empty space with nothing to push against.",
            "r": "For 10 points, name this quantity, mass times velocity, which is conserved in collisions."
        },
        {
            "p": "Japan’s IKAROS spacecraft, launched in 2010, became the first to travel between planets using a solar sail, which is pushed by the tiny amount of this quantity carried by sunlight. A photon’s value of this quantity equals its energy divided by the speed of light.",
            "r": "For 10 points, name this quantity, symbolized p, that equals mass times velocity for ordinary objects."
        },
        {
            "p": "René Descartes [“day-KART”] claimed in 1644 that the total “quantity of motion” in the universe never changes, but he ignored direction, a mistake Christiaan Huygens [“HY-gunz”] fixed while studying collisions. This quantity is a vector, so it points in the same direction as an object’s velocity.",
            "r": "Isaac Newton also used the name “quantity of motion” for it. For 10 points, name this quantity, equal to mass times velocity."
        },
        {
            "p": "Isaac Newton’s second law, in its general form, says that the net force on an object equals the rate at which this quantity changes. Airbags protect people in car crashes by stretching out the time it takes to change this quantity, which lowers the force.",
            "r": "For 10 points, name this quantity, mass times velocity, which is conserved when objects collide."
        },
        {
            "p": "In a Newton’s cradle, lifting and releasing one steel ball sends exactly one ball swinging out from the other end, because both this quantity and kinetic energy are conserved. Two ice skaters who push off each other glide apart with equal and opposite amounts of this quantity.",
            "r": "It is measured in kilogram meters per second. For 10 points, name this quantity, symbolized p, which equals mass times velocity."
        },
        {
            "p": "In a perfectly inelastic collision, such as two train cars that couple together, some kinetic energy turns into heat and sound, but this quantity is still conserved. The change in this quantity equals the impulse, which is force multiplied by time.",
            "r": "A slow bowling ball can have more of it than a fast ping-pong ball. For 10 points, name this quantity, equal to mass times velocity."
        },
        {
            "p": "When a moving cue ball hits a resting billiard ball of the same mass head-on, the cue ball stops dead and the other ball rolls off with all of this quantity. This quantity is conserved in collisions as long as no outside force acts.",
            "r": "It is measured in newton-seconds. For 10 points, name this vector quantity, symbolized p, equal to mass times velocity."
        },
        {
            "p": "Physicists find a charged particle’s value of this quantity from how tightly its track curves in a magnetic field, since a larger value makes a wider curve. In special relativity, this quantity equals the Lorentz factor times mass times velocity.",
            "r": "For 10 points, name this quantity, mass times velocity, that is conserved when two objects collide."
        },
        {
            "p": "In quantum mechanics, the operator for this quantity is minus i times h-bar times a derivative with respect to position. A particle’s wave function written in terms of this quantity is the Fourier [“FOOR-ee-ay”] transform of its position wave function.",
            "r": "For 10 points, name this quantity, symbolized p, which equals mass times velocity in everyday physics."
        },
        {
            "p": "When a firework shell bursts in midair, its pieces fly apart in all directions, but the total of this quantity just after the burst equals the total just before. A system’s center of mass keeps a steady velocity when this quantity is conserved.",
            "r": "A truck has more of it than a bicycle moving at the same speed. For 10 points, name this quantity, mass times velocity."
        },
        {
            "p": "If the push of this quantity carried by light drove a Crookes radiometer, its vanes would spin the opposite way; instead, warm gas molecules push them. A squid jets forward by squirting water backward because this quantity is conserved.",
            "r": "For 10 points, name this quantity, equal to mass times velocity, that is conserved when objects collide."
        },
        {
            "p": "Newton’s third law guarantees that this quantity is conserved, because when two objects push on each other, they change each other’s amounts of it equally and oppositely. This quantity is measured in kilogram meters per second, the same units as a newton-second.",
            "r": "A charging football player is hard to stop because he has a lot of it. For 10 points, name this quantity, symbolized p, equal to mass times velocity."
        }
    ],
    "clues": [
        {
            "id": "mass-velocity",
            "tier": "giveaway",
            "t": "Mass times velocity (p = mv)",
            "k": ["mass times velocity", "p = mv"],
            "n": 0
        },
        {
            "id": "collisions",
            "tier": "giveaway",
            "t": "Conserved in collisions as long as no outside force acts",
            "k": ["collisions", "conserved", "outside force"],
            "n": 0
        },
        {
            "id": "symbol-units",
            "tier": "giveaway",
            "t": "Symbolized p; measured in kilogram meters per second (the same as newton-seconds)",
            "k": ["kilogram meters per second", "newton-seconds"],
            "n": 0
        },
        {
            "id": "truck-bike",
            "tier": "giveaway",
            "t": "A heavy truck has far more than a bicycle moving at the same speed",
            "k": ["truck", "bicycle"],
            "n": 0
        },
        {
            "id": "vector",
            "tier": "middle",
            "t": "A vector: it points in the same direction as the velocity",
            "k": ["vector", "direction"],
            "n": 0
        },
        {
            "id": "impulse",
            "tier": "middle",
            "t": "Impulse (force multiplied by time) equals its change",
            "k": ["impulse", "force", "time"],
            "n": 0
        },
        {
            "id": "airbags",
            "tier": "middle",
            "t": "Airbags stretch out the time it takes to change it, which lowers the force on people in a crash",
            "k": ["airbags", "lowers the force"],
            "n": 0
        },
        {
            "id": "newtons-cradle",
            "tier": "middle",
            "t": "Newton’s cradle: one ball in, one ball out, conserving it along with kinetic energy",
            "k": ["newton’s cradle", "cradle"],
            "n": 0
        },
        {
            "id": "inelastic",
            "tier": "middle",
            "t": "Conserved even in perfectly inelastic collisions, where some kinetic energy is lost",
            "k": ["inelastic", "kinetic energy"],
            "n": 0,
            "rabbit": "Kinetic Energy"
        },
        {
            "id": "second-law",
            "tier": "middle",
            "t": "Newton’s second law, in its general form: net force equals its rate of change",
            "k": ["second law", "rate of change"],
            "n": 0,
            "rabbit": "Newton’s laws of motion"
        },
        {
            "id": "rockets",
            "tier": "middle",
            "t": "Rockets and squids move forward by pushing exhaust or water backward",
            "k": ["rockets", "squids", "exhaust"],
            "n": 0
        },
        {
            "id": "skaters",
            "tier": "middle",
            "t": "Two skaters who push off each other get equal and opposite amounts",
            "k": ["skaters", "equal and opposite"],
            "n": 0
        },
        {
            "id": "billiards",
            "tier": "middle",
            "t": "A cue ball hitting an equal ball head-on stops and passes on all of it",
            "k": ["cue ball", "head-on"],
            "n": 0
        },
        {
            "id": "third-law",
            "tier": "middle",
            "t": "Newton’s third law guarantees its conservation: pushes between two objects change their amounts equally and oppositely",
            "k": ["third law", "equally and oppositely"],
            "n": 0
        },
        {
            "id": "de-broglie",
            "tier": "power",
            "t": "Louis de Broglie (1924): a particle’s wavelength equals Planck’s constant divided by it",
            "k": ["de broglie", "wavelength", "1924"],
            "n": 0
        },
        {
            "id": "heisenberg",
            "tier": "power",
            "t": "Heisenberg’s uncertainty principle: it and position cannot both be known exactly",
            "k": ["heisenberg", "uncertainty", "position"],
            "n": 0,
            "rabbit": "Uncertainty principle"
        },
        {
            "id": "compton",
            "tier": "power",
            "t": "Compton effect (1923): X-ray photons hand some of it to electrons and come out with longer wavelengths",
            "k": ["compton", "x-ray", "1923"],
            "n": 0
        },
        {
            "id": "noether",
            "tier": "power",
            "t": "Noether’s theorem: its conservation comes from the laws of physics being the same everywhere in space",
            "k": ["noether", "everywhere in space"],
            "n": 0
        },
        {
            "id": "hamiltonian",
            "tier": "power",
            "t": "In Hamiltonian mechanics, it is the “conjugate” variable paired with position",
            "k": ["hamiltonian", "conjugate"],
            "n": 0
        },
        {
            "id": "tsiolkovsky",
            "tier": "power",
            "t": "Konstantin Tsiolkovsky’s 1903 rocket equation comes from its conservation",
            "k": ["tsiolkovsky", "rocket equation", "1903"],
            "n": 0
        },
        {
            "id": "light",
            "tier": "power",
            "t": "Light carries it even though photons have no mass (energy divided by the speed of light), so it can push solar sails like Japan’s IKAROS (2010)",
            "k": ["solar sails", "ikaros", "photons"],
            "n": 0
        },
        {
            "id": "descartes",
            "tier": "power",
            "t": "Descartes (1644) said the “quantity of motion” is conserved but ignored direction; Huygens fixed this, and Newton used the same name",
            "k": ["descartes", "quantity of motion", "huygens"],
            "n": 0
        },
        {
            "id": "track-curvature",
            "tier": "power",
            "t": "Found from how tightly a charged particle’s track curves in a magnetic field",
            "k": ["track", "magnetic field", "curves"],
            "n": 0
        },
        {
            "id": "relativity",
            "tier": "power",
            "t": "In special relativity, it equals the Lorentz factor times mass times velocity",
            "k": ["lorentz factor", "special relativity"],
            "n": 0
        },
        {
            "id": "operator",
            "tier": "power",
            "t": "Its quantum operator is minus i times h-bar times a derivative with respect to position",
            "k": ["operator", "h-bar", "derivative"],
            "n": 0
        },
        {
            "id": "radiometer",
            "tier": "power",
            "t": "A Crookes radiometer spins the opposite way from what light’s push would cause; warm gas really drives it",
            "k": ["crookes radiometer", "radiometer"],
            "n": 0
        },
        {
            "id": "firework",
            "tier": "power",
            "t": "A bursting firework shell’s pieces have the same total just after the burst as just before",
            "k": ["firework", "burst"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Linear, not angular",
        "body": "Momentum (mass times velocity) and angular momentum (the spinning version) are separate answer lines, so “angular momentum” is wrong on a collision question. Players also confuse momentum with impulse, which is the change in momentum, and with kinetic energy, which is not conserved in inelastic collisions.",
        "fix": "Collisions, p = mv, impulse, airbags, rockets, Newton’s cradle, and de Broglie wavelengths mean momentum. Spinning skaters, torque, orbits, Kepler’s equal areas, and L mean angular momentum. If a question asks for the quantity that an impulse changes, the answer is momentum, not impulse.",
        "line": "Real answer line: <b><u>Momentum</u></b> (accept <u>linear momentum</u>; prompt on <u>p</u>; do not accept “angular momentum”)"
    },
    "tests": {
        "right": [
            "Momentum",
            "momentum",
            "Momentem",
            "Linear momentum",
            "Conservation of momentum"
        ],
        "prompt": [
            "p"
        ],
        "wrong": [
            "Angular momentum",
            "Impulse",
            "Inertia",
            "Kinetic energy",
            "Moment",
            "Conservation of angular momentum"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
