import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

data = {
    "id": "gravitational-lensing",
    "name": "Gravitational lensing",
    "mono": "GL",
    "category": "Astronomy",
    "qbCategory": "Science · Other Science (Astronomy)",
    "kicker": "Gravity bending and magnifying light · Predicted by Einstein’s relativity",
    "dates": "Predicted by general relativity, 1915; first lens found 1979",
    "briefing": "Gravity can bend light. When a massive galaxy or cluster of galaxies sits between Earth and a more distant object, its gravity bends and magnifies that object’s light, smearing it into arcs, extra copies, or even a full circle called an Einstein ring. Albert Einstein’s general relativity predicted this bending, and a 1919 solar eclipse first confirmed it. Astronomers use these natural “magnifying glasses” to map dark matter, spot faraway galaxies, and even find hidden planets.",
    "answerHtml": "<b><u>gravitational lensing</u></b> (accept <u>gravitational lens</u>es; accept <u>microlensing</u>, <u>strong lensing</u>, or <u>weak lensing</u>; accept descriptions of gravity bending light; prompt on <u>lensing</u> or “bending of light”; do not accept “refraction,” “redshift,” or “dark matter”)",
    "accept": [
        "gravitational lensing",
        "gravitational lens",
        "gravitational lenses",
        "gravitational microlensing",
        "microlensing",
        "micro lensing",
        "strong lensing",
        "weak lensing",
        "strong gravitational lensing",
        "weak gravitational lensing",
        "gravity lensing",
        "lensing by gravity",
        "bending of light by gravity",
        "light bending by gravity",
        "gravitational bending of light",
        "gravitational deflection of light",
        "deflection of light by gravity",
        "gravitational light bending"
    ],
    "prompt": [
        "lensing",
        "lens",
        "lenses",
        "bending of light",
        "light bending",
        "bending light",
        "deflection of light",
        "light deflection",
        "gravitational deflection"
    ],
    "reject": [
        "redshift",
        "red shift",
        "gravitational redshift",
        "blueshift",
        "refraction",
        "diffraction",
        "reflection",
        "dispersion",
        "dark matter",
        "dark energy",
        "einstein ring",
        "einstein rings",
        "einstein cross",
        "chwolson ring",
        "relativity",
        "general relativity",
        "theory of relativity",
        "special relativity",
        "gravitational waves",
        "gravitational wave",
        "frame dragging",
        "time dilation",
        "doppler effect",
        "doppler shift",
        "shapiro delay",
        "mirage",
        "black hole",
        "black holes",
        "event horizon",
        "curved spacetime",
        "spacetime curvature",
        "bullet cluster",
        "twin quasar",
        "quasar",
        "quasars",
        "exoplanet",
        "exoplanets"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Gravitational_lens",
    "qb": {
        "q": "lensing",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In 1801, Johann von Soldner [“ZOLD-ner”] used Newton’s laws to estimate how much the Sun’s gravity should deflect a passing ray of starlight. Albert Einstein’s general relativity later predicted twice that amount, about 1.75 arcseconds for light that just grazes the Sun.",
            "r": "For 10 points, name this effect in which a massive object’s gravity bends and magnifies light like a lens."
        },
        {
            "p": "For the total solar eclipse of May 29, 1919, Arthur Eddington sailed to the island of Príncipe [“PREEN-see-peh”] off West Africa, while a second team observed from Sobral in Brazil, to photograph stars near the darkened Sun.",
            "r": "Their measurements showed starlight bending around the Sun, as Einstein predicted. For 10 points, name this effect, in which gravity bends light from a distant source."
        },
        {
            "p": "Prodded by an amateur scientist named Rudi Mandl, Albert Einstein published a short 1936 paper on this effect but doubted that it could ever be seen for stars. In 1937, Fritz Zwicky [“TSVIK-ee”] argued that whole galaxies could cause it, giving astronomers a way to weigh them.",
            "r": "For 10 points, name this effect in which gravity bends and magnifies light from distant objects."
        },
        {
            "p": "Orest Chwolson [“KHVOL-sun”] pointed out in 1924 that a star lined up perfectly behind another star could appear as a glowing ring, an idea that Albert Einstein explored independently in 1936. Radio astronomers led by Jacqueline Hewitt found the first known ring of this kind in 1988.",
            "r": "Such rings are named for Einstein. For 10 points, name this effect in which gravity bends light from a distant source."
        },
        {
            "p": "In 1979, Dennis Walsh, Robert Carswell, and Ray Weymann found two images of the same quasar sitting side by side, with nearly identical spectra. Those twin images were the first known example of this effect, caused by a galaxy lying between the quasar and Earth.",
            "r": "For 10 points, name this effect, in which a massive object’s gravity bends light like a magnifying glass."
        },
        {
            "p": "The Einstein Cross, found in 1985, shows a single distant quasar as four separate points of light arranged around a much closer galaxy. That foreground galaxy is nicknamed Huchra’s Lens, after the astronomer John Huchra.",
            "r": "For 10 points, name this effect, in which gravity bends the light of a background object into multiple images."
        },
        {
            "p": "In 1986 and 1987, astronomers found a giant glowing arc in the galaxy cluster Abell 370, which turned out to be the stretched-out image of a single galaxy far behind the cluster. Hubble images of clusters like Abell 2218 show dozens of such arcs.",
            "r": "For 10 points, name this effect, in which the gravity of massive objects bends light from more distant ones."
        },
        {
            "p": "When two galaxy clusters collided to form the Bullet Cluster, X-ray telescopes showed their hot gas piling up in the middle. But mass maps made with this effect showed that most of the clusters’ mass had passed right through, strong evidence for dark matter.",
            "r": "For 10 points, name this effect, in which mass bends light coming from more distant objects."
        },
        {
            "p": "In 2006, astronomers announced a cold planet about five and a half times Earth’s mass, found when its star passed in front of a more distant star and briefly brightened it. That “micro” version of this effect can even reveal rogue planets drifting with no star at all.",
            "r": "For 10 points, name this effect, in which gravity bends and focuses light the way a lens does."
        },
        {
            "p": "Surveys called MACHO, EROS, and OGLE watched millions of stars in the Magellanic Clouds and toward the Milky Way’s center for brief, symmetrical brightenings caused by this effect. Those surveys found too few massive compact objects to explain most of the dark matter.",
            "r": "For 10 points, name this effect, in which a massive object bends the light of something behind it."
        },
        {
            "p": "In 1964, Sjur Refsdal [“SHOOR REFS-dahl”] proposed that the time delays between multiple images of one exploding star could reveal how fast the universe is expanding. A supernova named for him appeared in 2014 as four images, and another image showed up in 2015, as predicted.",
            "r": "For 10 points, name this effect, in which gravity bends light into arcs, rings, and multiple images."
        },
        {
            "p": "In 2022, Hubble astronomers announced Earendel [“AIR-en-del”], the most distant single star seen up to that time, whose light left it when the universe was less than a billion years old. Its name comes from an Old English word meaning “morning star.”",
            "r": "A galaxy cluster magnified that star through this effect. For 10 points, name this effect, in which gravity bends and brightens light."
        },
        {
            "p": "In July 2022, President Joe Biden unveiled the first full-color image from the James Webb Space Telescope, Webb’s First Deep Field, which showed the galaxy cluster SMACS 0723 surrounded by stretched, glowing arcs of light.",
            "r": "Those arcs are distant galaxies magnified by the cluster’s gravity. For 10 points, name this effect, which Einstein’s general relativity predicts."
        },
        {
            "p": "Unlike a glass lens, this effect bends every color of light by the same amount, so it never splits light into a rainbow. It also has no single focal point, because light passing closer to the massive object is bent more sharply.",
            "r": "For 10 points, name this effect predicted by general relativity, in which gravity bends light from distant objects."
        },
        {
            "p": "Weak forms of this effect slightly stretch the shapes of millions of faraway galaxies, a pattern called cosmic shear that lets astronomers map invisible mass. The European Space Agency launched its Euclid telescope in 2023 partly to measure that stretching across about a third of the sky.",
            "r": "For 10 points, name this effect, in which gravity bends light the way a lens does."
        }
    ],
    "clues": [
        {
            "id": "bends-light",
            "tier": "giveaway",
            "t": "Gravity from a massive object, like a galaxy, bends and magnifies light from a more distant object behind it",
            "k": ["bends", "magnifies", "massive object"],
            "n": 0
        },
        {
            "id": "relativity",
            "tier": "giveaway",
            "t": "Predicted by Albert Einstein’s general theory of relativity",
            "k": ["general theory of relativity", "einstein"],
            "n": 0,
            "rabbit": "Theory of relativity"
        },
        {
            "id": "einstein-ring",
            "tier": "giveaway",
            "t": "Perfect alignment can stretch the light into a circle called an Einstein ring",
            "k": ["einstein ring", "circle"],
            "n": 0,
            "rabbit": "Albert Einstein"
        },
        {
            "id": "eddington",
            "tier": "giveaway",
            "t": "First seen in starlight bending around the Sun during Arthur Eddington’s 1919 eclipse expedition",
            "k": ["eddington", "1919", "eclipse"],
            "n": 0
        },
        {
            "id": "dark-matter-map",
            "tier": "giveaway",
            "t": "Used to map invisible dark matter, which has gravity but gives off no light",
            "k": ["dark matter", "map"],
            "n": 0,
            "rabbit": "Dark matter"
        },
        {
            "id": "arcs-images",
            "tier": "middle",
            "t": "Can make several images of one object or stretch galaxies into glowing arcs",
            "k": ["several images", "arcs"],
            "n": 0
        },
        {
            "id": "magnify",
            "tier": "middle",
            "t": "Massive galaxy clusters act as natural magnifying glasses, letting telescopes see very distant galaxies",
            "k": ["magnifying glasses", "galaxy clusters"],
            "n": 0
        },
        {
            "id": "bullet-cluster",
            "tier": "middle",
            "t": "In the Bullet Cluster (2006), it showed that most of the mass had moved apart from the hot X-ray gas, evidence for dark matter",
            "k": ["bullet cluster", "2006"],
            "n": 0
        },
        {
            "id": "twin-quasar",
            "tier": "middle",
            "t": "The first known example, the Twin Quasar, was found in 1979 by Dennis Walsh and colleagues",
            "k": ["twin quasar", "1979", "walsh"],
            "n": 0,
            "rabbit": "Quasars"
        },
        {
            "id": "einstein-cross",
            "tier": "middle",
            "t": "The Einstein Cross (found in 1985) is one quasar split into four images around a nearer galaxy",
            "k": ["einstein cross", "four images"],
            "n": 0
        },
        {
            "id": "exoplanets",
            "tier": "middle",
            "t": "Its “micro” version reveals planets, even rogue ones with no star, when a star briefly brightens a more distant star",
            "k": ["planets", "rogue", "brightens"],
            "n": 0,
            "rabbit": "Exoplanets"
        },
        {
            "id": "webb-deep-field",
            "tier": "middle",
            "t": "Webb’s First Deep Field (July 2022) showed arcs around the galaxy cluster SMACS 0723",
            "k": ["smacs 0723", "first deep field", "2022"],
            "n": 0
        },
        {
            "id": "twice-newton",
            "tier": "middle",
            "t": "General relativity predicts twice the bending that Newton’s laws give: about 1.75 arcseconds for light grazing the Sun",
            "k": ["1.75 arcseconds", "twice"],
            "n": 0
        },
        {
            "id": "sobral-principe",
            "tier": "middle",
            "t": "The 1919 eclipse teams observed from the island of Príncipe and from Sobral, Brazil",
            "k": ["príncipe", "sobral"],
            "n": 0
        },
        {
            "id": "soldner",
            "tier": "power",
            "t": "Johann von Soldner used Newton’s laws in 1801 to estimate how much the Sun bends starlight",
            "k": ["soldner", "1801"],
            "n": 0
        },
        {
            "id": "mandl-1936",
            "tier": "power",
            "t": "Einstein’s 1936 paper on it, urged by amateur scientist Rudi Mandl, doubted that it could be seen for stars",
            "k": ["rudi mandl", "1936"],
            "n": 0
        },
        {
            "id": "zwicky",
            "tier": "power",
            "t": "Fritz Zwicky argued in 1937 that whole galaxies could cause it and that it could weigh them",
            "k": ["zwicky", "1937", "weigh"],
            "n": 0
        },
        {
            "id": "chwolson",
            "tier": "power",
            "t": "Orest Chwolson described the ring image in 1924; Jacqueline Hewitt’s team found the first known ring with radio telescopes in 1988",
            "k": ["chwolson", "1924", "hewitt", "1988"],
            "n": 0
        },
        {
            "id": "abell",
            "tier": "power",
            "t": "A giant arc in the cluster Abell 370 (found 1986–87) turned out to be one distant galaxy; Abell 2218 shows dozens of arcs",
            "k": ["abell 370", "abell 2218", "giant arc"],
            "n": 0
        },
        {
            "id": "huchra",
            "tier": "power",
            "t": "The galaxy in the middle of the Einstein Cross is nicknamed Huchra’s Lens, after John Huchra",
            "k": ["huchra"],
            "n": 0
        },
        {
            "id": "macho-surveys",
            "tier": "power",
            "t": "The MACHO, EROS, and OGLE surveys watched for brief brightenings and found too few MACHOs to explain dark matter",
            "k": ["macho", "ogle", "eros"],
            "n": 0
        },
        {
            "id": "ogle-planet",
            "tier": "power",
            "t": "A cold planet about 5.5 times Earth’s mass, announced in 2006, was found this way",
            "k": ["cold planet", "2006", "5.5 times"],
            "n": 0
        },
        {
            "id": "refsdal",
            "tier": "power",
            "t": "Sjur Refsdal (1964) proposed using time delays between images to measure the universe’s expansion; Supernova Refsdal reappeared on schedule in 2015",
            "k": ["refsdal", "time delays", "1964"],
            "n": 0
        },
        {
            "id": "earendel",
            "tier": "power",
            "t": "Earendel, announced in 2022 as the most distant single star seen up to then, was magnified this way; its name is Old English for “morning star”",
            "k": ["earendel", "morning star"],
            "n": 0
        },
        {
            "id": "achromatic",
            "tier": "power",
            "t": "It is achromatic: unlike a glass lens, it bends all colors equally, so it never makes a rainbow",
            "k": ["achromatic", "all colors", "rainbow"],
            "n": 0
        },
        {
            "id": "cosmic-shear",
            "tier": "power",
            "t": "Weak versions slightly stretch the shapes of faraway galaxies (cosmic shear); ESA’s Euclid telescope, launched in 2023, measures this",
            "k": ["cosmic shear", "euclid", "2023"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Effect, ring, or matter?",
        "body": "Tossups on this effect are packed with things it reveals, and several are answer lines of their own: dark matter in the Bullet Cluster, distant quasars like the Twin Quasar, and exoplanets found by its “micro” version. Players also confuse it with refraction, the bending of light as it passes from one material into another, and with redshift, a change in the color of light rather than its direction.",
        "fix": "If the clues describe gravity bending or magnifying light (Eddington’s eclipse, Einstein rings and crosses, arcs around galaxy clusters), answer “gravitational lensing.” Invisible mass holding clusters together is dark matter; light bending as it enters water or glass is refraction. Saying only “lensing” earns a prompt, so add “gravitational.”",
        "line": "Real answer line: <b><u>gravitational lensing</u></b> (accept <u>gravitational lens</u>es; prompt on <u>lensing</u>)"
    },
    "tests": {
        "right": [
            "Gravitational lensing",
            "gravitational lens",
            "Gravitational lenseing",
            "microlensing",
            "weak lensing",
            "bending of light by gravity"
        ],
        "prompt": [
            "lensing",
            "bending of light"
        ],
        "wrong": [
            "Refraction",
            "Redshift",
            "Dark matter",
            "Einstein ring",
            "General relativity",
            "Gravity",
            "Gravitational waves"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
