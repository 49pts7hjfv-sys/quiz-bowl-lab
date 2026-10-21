import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."


def C(cid, tier, t, k, rabbit=None):
    d = {"id": cid, "tier": tier, "t": t, "k": k, "n": 0}
    if rabbit:
        d["rabbit"] = rabbit
    return d


LINE = "<b><u>antimatter</u></b> (accept <u>antiparticle</u>s; prompt on specific antiparticles such as <u>positron</u>s or <u>antiproton</u>s; do not accept “dark matter”)"

data = {
    "id": "antimatter",
    "name": "Antimatter",
    "mono": "AM",
    "category": "Physics",
    "qbCategory": "Science · Physics",
    "kicker": "Particles with opposite charge · Vanish in a flash when they meet matter",
    "dates": "Dirac’s equation, 1928; positron found by Carl Anderson, 1932",
    "briefing": "Almost every kind of particle has an opposite twin with the same mass but the opposite electric charge, and those twins make up antimatter. When a particle meets its twin, both vanish in a burst of pure energy. Paul Dirac’s equations predicted antimatter, Carl Anderson found the first piece of it, the positron, in 1932, and hospitals use positrons in PET scans to see inside the body.",
    "answerHtml": LINE,
    "accept": [
        "antimatter",
        "anti matter",
        "antiparticle",
        "antiparticles",
        "anti particle",
        "anti particles"
    ],
    "prompt": [
        "positron",
        "positrons",
        "antielectron",
        "antielectrons",
        "anti electron",
        "anti electrons",
        "antiproton",
        "antiprotons",
        "anti proton",
        "anti protons",
        "antineutron",
        "antineutrons",
        "antihydrogen",
        "anti hydrogen",
        "antiatom",
        "antiatoms"
    ],
    "reject": [
        "dark matter",
        "dark energy",
        "ordinary matter",
        "normal matter",
        "baryonic matter",
        "negative mass",
        "exotic matter",
        "positronium",
        "annihilation",
        "pair production",
        "gamma rays",
        "gamma ray",
        "black hole",
        "black holes",
        "cosmic rays",
        "plasma",
        "nuclear fusion",
        "electrons",
        "protons",
        "neutrons",
        "neutrinos",
        "quarks"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Antimatter",
    "qb": {"q": "antimatter", "found": 0, "tip": TIP},
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        {
            "p": "Paul Dirac’s 1928 equation for the electron had puzzling extra solutions, which he first tried to explain as protons before predicting in 1931 a new particle with the electron’s mass and the opposite charge. That particle was the first known example of this substance.",
            "r": "For 10 points, name this kind of matter made of particles such as positrons, which annihilate when they meet ordinary matter."
        },
        {
            "p": "In 1932, Carl Anderson photographed cosmic-ray tracks in a cloud chamber with a lead plate across its middle and found a particle that curved the opposite way from an electron in a magnetic field. He shared the 1936 Nobel Prize in Physics for finding that first known particle of this kind.",
            "r": "For 10 points, name this kind of matter whose particles have the same mass as ordinary particles but opposite charge."
        },
        {
            "p": "In PET scans, a patient is given a sugar tagged with radioactive fluorine-18, which gives off particles of this kind; when each one meets an electron, the pair turns into two gamma rays flying off in opposite directions. Detectors around the body catch those gamma rays to map where the sugar collects.",
            "r": "It annihilates when it touches ordinary matter. For 10 points, name this kind of matter made of particles like positrons."
        },
        {
            "p": "In 1995, a team at CERN made the first nine atoms of hydrogen built from this substance, each lasting only a tiny fraction of a second. In 2023, CERN’s ALPHA experiment showed that such atoms fall downward under gravity, as ordinary matter does.",
            "r": "For 10 points, name this kind of matter, made of particles like the positron, that annihilates when it touches ordinary matter."
        },
        {
            "p": "In beta-plus decay, a proton inside an unstable nucleus turns into a neutron and gives off a neutrino along with a particle of this kind. Physics labs often use sodium-22, which decays this way, as a handy source of such particles.",
            "r": "Bananas give off a tiny number of these particles too. For 10 points, name this kind of matter that includes the positron."
        },
        {
            "p": "In 1967, Andrei Sakharov [“SAH-kuh-rof”] listed three conditions the early universe needed to meet to end up with far more ordinary matter than this substance. One of those conditions, a slight difference in how particles and their opposites behave, called CP violation, was first seen in 1964 in particles called kaons.",
            "r": "Why the Big Bang left so little of this substance is an unsolved puzzle. For 10 points, name this kind of matter made of particles like positrons."
        },
        {
            "p": "Richard Feynman described a particle of this kind as an ordinary particle traveling backward in time, an idea also proposed by Ernst Stueckelberg [“SHTOO-kel-bairg”]. In Feynman diagrams, such particles are drawn with arrows pointing the opposite way from the direction of time.",
            "r": "For 10 points, name this kind of matter, which releases energy when it annihilates with ordinary matter."
        },
        {
            "p": "In 1955, Emilio Segrè [“seh-GRAY”] and Owen Chamberlain used the Bevatron accelerator at Berkeley to create a negatively charged twin of the proton, and a neutral twin of the neutron was found there the next year. Those discoveries showed that heavy particles, not just electrons, have opposites belonging to this kind of matter.",
            "r": "For 10 points, name this kind of matter whose particles are mirror-image partners of ordinary particles, such as the positron."
        },
        {
            "p": "A gamma ray with enough energy passing near an atomic nucleus can turn into an electron and a particle of this kind, a process called pair production. The reverse process releases all of the particles’ mass as energy, following Einstein’s equation E equals m c squared.",
            "r": "For 10 points, name this kind of matter whose version of the electron is called the positron."
        },
        {
            "p": "In 2011, NASA announced that its Fermi Gamma-ray Space Telescope had caught thunderstorms hurling beams of particles of this kind out into space. Those particles were made when powerful bursts of gamma rays above the storms turned into electrons paired with these opposites.",
            "r": "For 10 points, name this kind of matter that includes the positron, the electron’s opposite."
        },
        {
            "p": "In Dan Brown’s novel _Angels & Demons_, a canister of this substance stolen from CERN threatens to destroy Vatican City. In _Star Trek_, the starship _Enterprise_ gets the power for its warp drive by combining ordinary matter with this substance.",
            "r": "For 10 points, name this real kind of matter made of particles like positrons, which annihilate with ordinary matter."
        },
        {
            "p": "The Alpha Magnetic Spectrometer, installed on the International Space Station in 2011 by the final flight of the space shuttle _Endeavour_, searches cosmic rays for helium nuclei made of this substance. Finding even one would hint that large regions of the universe are made of it.",
            "r": "It annihilates with ordinary matter. For 10 points, name this kind of matter, made of particles such as the positron."
        },
        {
            "p": "An electron and the particle of this kind that matches it can briefly orbit each other as an exotic “atom” called positronium before they annihilate. A photon, the particle of light, has no separate partner of this kind, because it is its own opposite.",
            "r": "For 10 points, name this kind of matter whose particles have the same mass but opposite electric charge as their ordinary partners."
        },
        {
            "p": "Combining just one gram of this substance with one gram of ordinary matter would release about 180 trillion joules, since all of the mass turns into energy. Because it is so hard to make and store, only tiny amounts of this substance have ever been produced.",
            "r": "For 10 points, name this kind of matter that annihilates on contact with ordinary matter, made of particles like positrons."
        },
        {
            "p": "At CERN, a machine called a decelerator slows down particles of this kind so that experiments can catch them in Penning traps, which hold charged particles with electric and magnetic fields instead of walls. In 2010, the ALPHA experiment first trapped whole atoms of hydrogen made of this substance.",
            "r": "It was first found in cosmic rays. For 10 points, name this kind of matter made of particles like positrons."
        }
    ],
    "clues": [
        C("definition", "giveaway", "Made of particles with the same mass as ordinary particles but the opposite electric charge", ["same mass", "opposite electric charge"]),
        C("positron", "giveaway", "The positron, the electron’s positively charged opposite, is the best-known example", ["positron", "positively charged"], "Electrons"),
        C("annihilate", "giveaway", "When it meets ordinary matter, both annihilate, turning all of their mass into energy such as gamma rays", ["annihilate", "gamma rays"]),
        C("emc2", "giveaway", "The energy released follows Einstein’s equation E = mc²", ["einstein", "e = mc²"], "Albert Einstein"),
        C("pet", "giveaway", "PET (positron emission tomography) scans detect the gamma rays made when it meets electrons in the body", ["positron emission tomography", "pet"]),
        C("dirac", "middle", "Paul Dirac’s 1928 equation for the electron led him to predict, in 1931, a particle with the electron’s mass and opposite charge", ["dirac", "1928", "1931"]),
        C("anderson", "middle", "Carl Anderson found the positron in cosmic rays with a cloud chamber (1932) and shared the 1936 Nobel Prize", ["anderson", "cloud chamber", "1932"]),
        C("cern-1995", "middle", "CERN made the first atoms of hydrogen out of it in 1995", ["cern", "1995", "hydrogen"]),
        C("asymmetry", "middle", "The Big Bang should have made equal amounts of it and ordinary matter; why ordinary matter won out is unsolved", ["big bang", "equal amounts", "unsolved"]),
        C("pair-production", "middle", "Pair production: a high-energy gamma ray near a nucleus can turn into an electron and a positron", ["pair production"]),
        C("bevatron", "middle", "Emilio Segrè and Owen Chamberlain made the proton’s negatively charged twin at Berkeley’s Bevatron (1955); the neutron’s twin followed in 1956", ["segrè", "chamberlain", "bevatron"]),
        C("fiction", "middle", "In _Angels & Demons_, a canister of it stolen from CERN threatens Vatican City; in _Star Trek_, it powers the warp drive", ["angels & demons", "star trek", "warp drive"]),
        C("traps", "middle", "Penning traps hold its charged particles with electric and magnetic fields, since touching container walls would destroy them", ["penning traps", "walls"]),
        C("cloud-chamber", "power", "Anderson’s track curved the opposite way from an electron’s, and a lead plate across the chamber showed which way it was moving", ["lead plate", "curved"]),
        C("feynman", "power", "Richard Feynman (and Ernst Stueckelberg) pictured its particles as ordinary particles moving backward in time", ["feynman", "backward in time"], "Richard Feynman"),
        C("sakharov", "power", "Andrei Sakharov’s 1967 conditions explain how the universe ended up with more matter; one is CP violation, first seen in kaons in 1964", ["sakharov", "cp violation", "kaons"]),
        C("alpha-2010", "power", "CERN’s ALPHA experiment first trapped whole atoms of hydrogen made of it in 2010", ["alpha experiment", "2010"]),
        C("alpha-gravity", "power", "In 2023, ALPHA showed that hydrogen made of it falls downward under gravity, as ordinary matter does", ["2023", "falls downward"]),
        C("fermi-storms", "power", "NASA’s Fermi telescope caught thunderstorms hurling beams of positrons into space (announced 2011)", ["fermi", "thunderstorms"]),
        C("bananas", "power", "Bananas give off a tiny number of positrons, thanks to radioactive potassium-40", ["bananas", "potassium-40"]),
        C("beta-plus", "power", "Beta-plus decay: a proton in a nucleus becomes a neutron, giving off a positron and a neutrino; sodium-22 is a common lab source", ["beta-plus", "sodium-22", "neutrino"]),
        C("positronium", "power", "An electron and a positron can briefly orbit each other as an exotic atom called positronium", ["positronium"]),
        C("photon", "power", "The photon is its own opposite, so it has no separate partner", ["photon", "own opposite"]),
        C("ams", "power", "The Alpha Magnetic Spectrometer on the space station (installed 2011 by _Endeavour_) hunts for helium nuclei made of it", ["alpha magnetic spectrometer", "endeavour", "helium"]),
        C("one-gram", "power", "One gram of it meeting one gram of ordinary matter would release about 180 trillion joules", ["180 trillion", "one gram"])
    ],
    "trap": {
        "title": "Anti, not dark",
        "body": "Antimatter and dark matter sound alike but are completely different. Antimatter is real material made of particles like positrons and antiprotons, which physicists create at CERN and hospitals use in PET scans; dark matter is unseen material that astronomers detect only through its gravity. A tossup about the positron or Carl Anderson may also tempt you to name just that one particle, which earns only a prompt here.",
        "fix": "Opposite charge, positrons, Dirac, Anderson, annihilation, PET scans, and CERN’s antihydrogen mean antimatter. Spinning galaxies, gravitational lensing, and WIMPs mean dark matter. If the giveaway says “this particle,” name the positron; if it says “this kind of matter” or “this substance,” say antimatter.",
        "line": "Real answer line: " + LINE
    },
    "tests": {
        "right": [
            "Antimatter",
            "anti-matter",
            "Antiparticles",
            "Antimater",
            "Antiparticle"
        ],
        "prompt": [
            "Positrons",
            "Antiprotons",
            "Antihydrogen"
        ],
        "wrong": [
            "Dark matter",
            "Matter",
            "Dark energy",
            "Electrons",
            "Protons",
            "Annihilation",
            "Positronium",
            "Neutrinos"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
