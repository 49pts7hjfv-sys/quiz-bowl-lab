import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "diffraction",
    "name": "Diffraction",
    "mono": "DFR",
    "category": "Physics",
    "qbCategory": "Science · Physics",
    "kicker": "Waves spreading around edges · Why you can hear around corners",
    "dates": "Named by Francesco Maria Grimaldi in 1665",
    "briefing": "Diffraction is the spreading of a wave as it squeezes through a gap or bends around the edge of an obstacle. It is why you can hear a friend talking around a corner even when you cannot see them: sound waves are long enough to bend around the wall, but light waves are much too short. Shining light through tiny slits makes striped patterns that helped prove light is a wave.",
    "answerHtml": "<b><u>diffraction</u></b> (accept word forms like <u>diffract</u>ing; accept specific types such as <u>X-ray diffraction</u>, <u>electron diffraction</u>, or <u>single-slit diffraction</u>; do not accept “refraction” or “interference”)",
    "accept": [
        "diffraction",
        "diffractions",
        "diffract",
        "diffracts",
        "diffracting",
        "diffracted",
        "diffraction of light",
        "diffraction of waves",
        "x ray diffraction",
        "xray diffraction",
        "electron diffraction",
        "neutron diffraction",
        "single slit diffraction",
        "double slit diffraction",
        "fraunhofer diffraction",
        "fresnel diffraction",
        "bragg diffraction",
        "diffraction pattern",
        "diffraction patterns"
    ],
    "prompt": [],
    "reject": [
        "refraction",
        "refractions",
        "refracting",
        "reflection",
        "reflecting",
        "interference",
        "wave interference",
        "constructive interference",
        "destructive interference",
        "thin film interference",
        "dispersion",
        "scattering",
        "rayleigh scattering",
        "diffusion",
        "polarization",
        "rarefaction",
        "braggs law",
        "bragg law",
        "huygens principle",
        "doppler effect"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Diffraction",
    "qb": {
        "q": "diffraction",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "When Augustin-Jean Fresnel [“fray-NEL”] entered a contest on this effect in 1818, Siméon Denis Poisson [“pwah-SOHN”] argued that Fresnel’s wave theory predicted an absurd result: a bright spot in the center of a round object’s shadow. François Arago [“ah-rah-GOH”] then found that spot.",
            "r": "For 10 points, name this spreading of a wave as it passes the edge of an obstacle or goes through a narrow opening."
        },
        {
            "p": "The Jesuit priest Francesco Maria Grimaldi named this effect after the Latin for “breaking into pieces,” in a book published in 1665, after he saw that light passing a thin rod made a shadow edged with colored bands.",
            "r": "Waves spread out the most when an opening is about as wide as their wavelength. For 10 points, name this bending of waves around obstacles."
        },
        {
            "p": "A principle named for Jacques Babinet [“bah-bee-NAY”] says that a thin hair and a slit of the same width produce nearly the same pattern from this effect, so a laser shining past a hair can measure its thickness. Narrowing a slit makes the pattern of light and dark bands spread out wider.",
            "r": "For 10 points, name this effect in which waves spread out after passing through a narrow opening or around an edge."
        },
        {
            "p": "Light passing through a round opening makes a bright central spot called an Airy disk, surrounded by faint rings. According to the Rayleigh criterion, two stars can just be told apart when the center of one’s spot falls on the first dark ring of the other’s.",
            "r": "This effect sets a limit on how sharp a telescope’s images can be. For 10 points, name this spreading of waves around edges and through openings."
        },
        {
            "p": "William Lawrence Bragg was 25 when he and his father shared the 1915 Nobel Prize in Physics; his law, n lambda equals 2 d sine theta, uses this effect to find the spacing between layers of atoms in a crystal.",
            "r": "For 10 points, name this effect, used in X-ray crystallography, in which waves spread out as they pass edges or narrow gaps."
        },
        {
            "p": "In 1912, Max von Laue [“LOW-uh”] showed that a crystal could act on X-rays the way a fine grid of slits acts on light, proving that X-rays are waves and that crystals are made of regularly spaced atoms. The resulting patterns of spots let scientists work out where atoms sit.",
            "r": "For 10 points, name this spreading of waves as they pass through narrow openings or around edges."
        },
        {
            "p": "In 1927, Clinton Davisson and Lester Germer fired electrons at a nickel crystal and saw the kind of pattern only waves make, confirming an idea of Louis de Broglie [“duh BROY”] that particles act like waves. George Paget Thomson saw the same effect with electrons passing through thin metal foil.",
            "r": "For 10 points, name this effect, in which waves spread out after passing through a narrow opening or around an edge."
        },
        {
            "p": "Rosalind Franklin’s “Photo 51,” made by sending X-rays through fibers of DNA, showed an X-shaped pattern from this effect that revealed the molecule’s helical shape. X-rays work for this because their wavelengths are about as small as the spaces between atoms.",
            "r": "For 10 points, name this effect, the spreading of waves around obstacles and through small gaps."
        },
        {
            "p": "Ernst Abbe [“AH-buh”] showed that this effect keeps ordinary light microscopes from seeing details much smaller than about half the wavelength of light. Eric Betzig, Stefan Hell, and William Moerner shared the 2014 Nobel Prize in Chemistry for microscopes that get around that limit.",
            "r": "Electron microscopes suffer less from it because electrons have much shorter wavelengths. For 10 points, name this spreading of waves around obstacles."
        },
        {
            "p": "A small, colorful ring called a corona that sometimes surrounds the Moon is caused by this effect in tiny water droplets, unlike the much larger 22-degree halo, which comes from light bending through ice crystals. Iridescent clouds get their colors in a similar way.",
            "r": "For 10 points, name this spreading of light waves around small obstacles and through narrow gaps."
        },
        {
            "p": "David Rittenhouse made an early grating for this effect in 1785 by stretching hairs between two fine screws. The rainbow colors on the back of a CD appear because its tightly packed rows of pits act as a grating, sending each color off at a different angle.",
            "r": "Spectroscopes use gratings that rely on this effect. For 10 points, name this spreading of waves through narrow slits."
        },
        {
            "p": "AM radio signals, whose waves are hundreds of meters long, curve around hills and tall buildings much better than FM signals because of this effect. Ocean waves fan out in the same way after passing through a narrow harbor entrance.",
            "r": "This effect lets you hear someone talking around a corner. For 10 points, name this spreading of waves around obstacles."
        },
        {
            "p": "The spikes seen around bright stars in many telescope photos come from this effect, as starlight passes the thin struts that hold a telescope’s second mirror. The bigger a telescope’s opening, the less this effect blurs its images.",
            "r": "For 10 points, name this spreading of light as it passes the edge of an object or goes through a narrow slit."
        },
        {
            "p": "The Huygens–Fresnel [“HOY-gunz fray-NEL”] principle explains this effect by treating every point on a wave’s front as the source of tiny new wavelets that spread out and overlap. Far from an opening, the simpler Fraunhofer [“FROWN-hoh-fer”] form of this effect applies.",
            "r": "In a single-slit pattern, the central bright band is twice as wide as the others. For 10 points, name this spreading of waves through openings."
        },
        {
            "p": "In the early 1800s, Thomas Young sent light through two narrow slits and saw stripes of light and dark, evidence that light is a wave. Each slit spreads the light out because of this effect, and the overlapping waves then interfere.",
            "r": "For 10 points, name this bending of waves around obstacles, which is different from refraction and interference."
        }
    ],
    "clues": [
        {
            "id": "spreading",
            "tier": "giveaway",
            "t": "The spreading of a wave as it passes through a narrow opening or around the edge of an obstacle",
            "k": ["spreading", "narrow opening", "edge"],
            "n": 0,
            "rabbit": "Waves"
        },
        {
            "id": "corners",
            "tier": "giveaway",
            "t": "Why you can hear someone talking around a corner but can’t see them: sound waves are long, and light waves are very short",
            "k": ["around a corner", "sound waves"],
            "n": 0
        },
        {
            "id": "slits",
            "tier": "giveaway",
            "t": "Light sent through very narrow slits makes patterns of bright and dark bands",
            "k": ["slits", "bright and dark bands"],
            "n": 0
        },
        {
            "id": "gratings",
            "tier": "giveaway",
            "t": "A grating, with thousands of tiny slits or lines, uses it to spread light into a rainbow of colors",
            "k": ["grating", "rainbow"],
            "n": 0
        },
        {
            "id": "wavelength-size",
            "tier": "middle",
            "t": "Waves spread out the most when an opening is about as wide as their wavelength",
            "k": ["wavelength", "as wide as"],
            "n": 0
        },
        {
            "id": "cd",
            "tier": "middle",
            "t": "The rainbow colors on the back of a CD come from its rows of pits acting as a grating",
            "k": ["rows of pits", "cd"],
            "n": 0
        },
        {
            "id": "harbor",
            "tier": "middle",
            "t": "Ocean waves fan out after passing through a narrow harbor entrance",
            "k": ["harbor", "ocean waves", "fan out"],
            "n": 0
        },
        {
            "id": "am-radio",
            "tier": "middle",
            "t": "AM radio waves, hundreds of meters long, curve around hills and buildings much better than FM waves",
            "k": ["am radio", "hills", "fm"],
            "n": 0,
            "rabbit": "Radio waves"
        },
        {
            "id": "crystallography",
            "tier": "middle",
            "t": "X-ray crystallography uses it to find where atoms sit, since X-ray wavelengths are about the size of the gaps between atoms",
            "k": ["x-ray crystallography", "atoms", "gaps"],
            "n": 0,
            "rabbit": "X-rays"
        },
        {
            "id": "photo-51",
            "tier": "middle",
            "t": "Rosalind Franklin’s “Photo 51,” made this way with X-rays, showed an X-shaped pattern that revealed DNA’s helical shape",
            "k": ["photo 51", "rosalind franklin", "dna"],
            "n": 0,
            "rabbit": "DNA"
        },
        {
            "id": "young",
            "tier": "middle",
            "t": "Thomas Young’s two-slit experiment (early 1800s) showed light is a wave: each slit spreads the light, and the waves then interfere",
            "k": ["thomas young", "two-slit", "interfere"],
            "n": 0
        },
        {
            "id": "sharpness-limit",
            "tier": "middle",
            "t": "Limits how sharp a telescope’s images can be; a bigger opening blurs less",
            "k": ["telescope", "bigger opening", "sharp"],
            "n": 0
        },
        {
            "id": "slit-width",
            "tier": "middle",
            "t": "Narrowing a slit makes the pattern spread out wider; the central bright band is twice as wide as the others",
            "k": ["narrowing", "twice as wide", "central bright band"],
            "n": 0,
            "rabbit": "Uncertainty principle"
        },
        {
            "id": "electron-microscopes",
            "tier": "middle",
            "t": "Electron microscopes suffer less from it because electrons have much shorter wavelengths than visible light",
            "k": ["electron microscopes", "shorter wavelengths"],
            "n": 0
        },
        {
            "id": "arago-spot",
            "tier": "power",
            "t": "Poisson said Fresnel’s wave theory predicted an absurd bright spot in the center of a round object’s shadow; François Arago found it",
            "k": ["poisson", "arago", "bright spot"],
            "n": 0
        },
        {
            "id": "grimaldi",
            "tier": "power",
            "t": "Francesco Maria Grimaldi named it from the Latin for “breaking into pieces,” in a book published in 1665",
            "k": ["grimaldi", "1665", "breaking into pieces"],
            "n": 0
        },
        {
            "id": "babinet",
            "tier": "power",
            "t": "Babinet’s principle: a hair and a slit of the same width make nearly the same pattern, so a laser can measure a hair’s thickness",
            "k": ["babinet", "hair", "laser"],
            "n": 0
        },
        {
            "id": "airy-rayleigh",
            "tier": "power",
            "t": "Round openings make an Airy disk with faint rings; by the Rayleigh criterion, two stars can just be told apart when one’s spot sits on the other’s first dark ring",
            "k": ["airy disk", "rayleigh criterion", "first dark ring"],
            "n": 0,
            "rabbit": "Lord Rayleigh"
        },
        {
            "id": "bragg",
            "tier": "power",
            "t": "William Lawrence Bragg, age 25, shared the 1915 Nobel Prize with his father; Bragg’s law is n lambda = 2 d sine theta",
            "k": ["bragg", "1915", "n lambda"],
            "n": 0
        },
        {
            "id": "von-laue",
            "tier": "power",
            "t": "In 1912, Max von Laue showed that crystals act on X-rays like a fine grid of slits, proving X-rays are waves",
            "k": ["von laue", "1912", "crystals"],
            "n": 0
        },
        {
            "id": "davisson-germer",
            "tier": "power",
            "t": "In 1927, Davisson and Germer aimed electrons at a nickel crystal and saw wave patterns, confirming de Broglie’s matter waves",
            "k": ["davisson", "germer", "nickel", "de broglie"],
            "n": 0,
            "rabbit": "Electrons"
        },
        {
            "id": "gp-thomson",
            "tier": "power",
            "t": "George Paget Thomson saw it with electrons passing through thin metal foil; his father, J. J. Thomson, had shown that electrons are particles",
            "k": ["george paget thomson", "metal foil", "j. j. thomson"],
            "n": 0
        },
        {
            "id": "abbe-limit",
            "tier": "power",
            "t": "Ernst Abbe’s limit: light microscopes can’t see details much smaller than about half a wavelength; a 2014 Chemistry Nobel went to Betzig, Hell, and Moerner for beating it",
            "k": ["ernst abbe", "half a wavelength", "2014"],
            "n": 0
        },
        {
            "id": "corona",
            "tier": "power",
            "t": "A small colorful corona around the Moon comes from it in tiny water droplets, unlike the 22-degree halo made by refraction in ice crystals",
            "k": ["corona", "water droplets", "22-degree halo"],
            "n": 0,
            "rabbit": "Refraction"
        },
        {
            "id": "spikes",
            "tier": "power",
            "t": "The spikes around bright stars in telescope photos come from starlight passing the thin struts that hold the second mirror",
            "k": ["spikes", "struts", "second mirror"],
            "n": 0
        },
        {
            "id": "rittenhouse",
            "tier": "power",
            "t": "David Rittenhouse made an early grating in 1785 by stretching hairs between two fine screws",
            "k": ["rittenhouse", "1785", "hairs"],
            "n": 0
        },
        {
            "id": "huygens-fresnel",
            "tier": "power",
            "t": "The Huygens–Fresnel principle treats every point on a wave’s front as the source of tiny new wavelets",
            "k": ["huygens–fresnel", "wavelets", "wave’s front"],
            "n": 0
        },
        {
            "id": "fraunhofer",
            "tier": "power",
            "t": "Far from the opening, the simpler Fraunhofer form applies; close to it, the Fresnel form",
            "k": ["fraunhofer", "fresnel form"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Not refraction or interference",
        "body": "Diffraction, refraction, and interference all show up in optics tossups, and real answer lines keep them apart. Refraction is bending when a wave crosses into a new material and changes speed. Interference is what happens when overlapping waves add up or cancel out, and in a two-slit experiment both effects happen at once: each slit spreads the light by diffraction, and the spreading waves then interfere.",
        "fix": "Edges, narrow gaps, gratings, X-ray crystals, Bragg’s law, Airy disks, or sound bending around corners mean diffraction. A straw that looks bent, lenses, or Snell’s law mean refraction; if a question stresses two waves adding up or canceling, as in soap bubbles or noise-canceling headphones, the answer may be interference.",
        "line": "Real answer line: <b><u>diffraction</u></b> (accept word forms like <u>diffract</u>ing; accept specific types such as <u>X-ray diffraction</u>, <u>electron diffraction</u>, or <u>single-slit diffraction</u>; do not accept “refraction” or “interference”)"
    },
    "tests": {
        "right": [
            "Diffraction",
            "diffracting",
            "X-ray diffraction",
            "Electron diffraction",
            "Difraction"
        ],
        "prompt": [],
        "wrong": [
            "Refraction",
            "Reflection",
            "Interference",
            "Diffusion",
            "Dispersion"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
