import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "polio",
    "name": "Polio",
    "mono": "POL",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "Viral disease that can cause paralysis · Nearly wiped out by vaccines",
    "dates": "Salk vaccine announced 1955",
    "briefing": "Polio is a contagious disease caused by a virus, and in a small share of infections it attacks the nerves that control muscles, causing paralysis. In the early 1950s, American parents dreaded summer outbreaks, until Jonas Salk’s vaccine was announced safe and effective in 1955; Albert Sabin’s oral vaccine followed. A worldwide campaign launched in 1988 has pushed wild polio out of almost every country on Earth.",
    "answerHtml": "<b><u>Polio</u></b> (accept <u>poliomyelitis</u>, <u>poliovirus</u>, or <u>infantile paralysis</u>; prompt on <u>enterovirus</u>; do not accept “smallpox”)",
    "accept": [
        "polio",
        "poliomyelitis",
        "poliovirus",
        "polioviruses",
        "polio virus",
        "infantile paralysis",
        "wild poliovirus",
        "acute poliomyelitis"
    ],
    "prompt": [
        "enterovirus",
        "enteroviruses"
    ],
    "reject": [
        "smallpox",
        "measles",
        "mumps",
        "rubella",
        "chickenpox",
        "rabies",
        "tetanus",
        "diphtheria",
        "whooping cough",
        "tuberculosis",
        "influenza",
        "polo",
        "jonas salk",
        "salk",
        "albert sabin",
        "sabin",
        "iron lung",
        "salk vaccine",
        "sabin vaccine"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Polio",
    "qb": {
        "q": "polio",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "Karl Landsteiner, who also discovered the ABO blood groups, and Erwin Popper showed that a virus causes this disease by passing it to monkeys. Decades later, John Enders, Thomas Weller, and Frederick Robbins won a Nobel Prize for growing that virus in tissue culture, which made it possible to mass-produce vaccines.",
            "r": "Most infections with its virus cause no symptoms at all. For 10 points, name this disease, prevented by Jonas Salk’s vaccine, that can cause paralysis."
        },
        {
            "p": "The “iron lung” built by Philip Drinker and Louis Agassiz Shaw in 1928 helped many patients with this disease who could not breathe on their own. During epidemics of this disease in the 1950s, some hospitals filled entire wards with those machines.",
            "r": "For 10 points, name this viral disease, which vaccines developed by Jonas Salk and Albert Sabin helped nearly wipe out."
        },
        {
            "p": "Australian nurse Sister Elizabeth Kenny treated patients with this disease using hot, moist packs and gentle exercise instead of the stiff splints most doctors used. Franklin Roosevelt founded a treatment center for people with this disease at Warm Springs, Georgia, where he swam in warm spring water.",
            "r": "For 10 points, name this viral disease that can cause paralysis, prevented by vaccines from Jonas Salk and Albert Sabin."
        },
        {
            "p": "Comedian Eddie Cantor coined the name “March of Dimes” when he urged Americans to mail dimes to the White House for a foundation that Franklin Roosevelt started in 1938 to fight this disease. Partly because of that campaign, Roosevelt’s face was put on the dime in 1946.",
            "r": "For 10 points, name this disease that Roosevelt was diagnosed with in 1921, which can cause paralysis."
        },
        {
            "p": "Thomas Francis Jr. led a 1954 field trial of a vaccine for this disease that involved more than a million schoolchildren. The results were announced on April 12, 1955, exactly ten years after the death of Franklin Roosevelt, who had been diagnosed with this disease.",
            "r": "That vaccine was created by Jonas Salk at the University of Pittsburgh. For 10 points, name this viral disease that can cause paralysis."
        },
        {
            "p": "In a 1955 television interview with Edward R. Murrow, the creator of a vaccine against this disease said that it had no patent, asking, “Could you patent the sun?” That vaccine used virus that had been killed with the chemical formaldehyde.",
            "r": "That creator was Jonas Salk. For 10 points, name this disease that once caused summer epidemics of paralysis."
        },
        {
            "p": "Huge trials in the Soviet Union in 1959 tested a vaccine for this disease made from live but weakened virus, which was often given to children on sugar cubes. Because that vaccine was swallowed instead of injected, it was cheap and easy to give in mass campaigns.",
            "r": "That vaccine was developed by Albert Sabin. For 10 points, name this viral disease, which Jonas Salk also made a vaccine against."
        },
        {
            "p": "This disease’s full medical name comes from Greek words for “gray” and “marrow,” because its virus attacks the gray matter of the spinal cord. There, the virus can destroy motor neurons, the nerve cells that tell muscles to move.",
            "r": "Most people infected show no symptoms, but some become paralyzed. For 10 points, name this disease prevented by the Salk and Sabin vaccines."
        },
        {
            "p": "Of the three types of wild virus that cause this disease, type 2 was declared eradicated in 2015 and type 3 in 2019. As of 2024, wild type 1 was still spreading in only two countries, Pakistan and Afghanistan.",
            "r": "A worldwide campaign has worked to wipe out this disease since 1988. For 10 points, name this viral disease that Jonas Salk developed a vaccine against."
        },
        {
            "p": "The last case of this disease caused by wild virus in the Americas came in Peru in 1991, and India recorded its last such case in 2011. Rotary International has made ending this disease its signature cause since the 1980s.",
            "r": "For 10 points, name this disease that Jonas Salk and Albert Sabin developed vaccines against."
        },
        {
            "p": "In 2020, Africa was certified free of the wild virus that causes this disease, four years after Nigeria recorded the continent’s last case. Nelson Mandela had helped launch a 1996 campaign to “kick” this disease out of Africa.",
            "r": "For 10 points, name this viral disease that can cause paralysis, which is prevented by an oral vaccine or a shot."
        },
        {
            "p": "The violinist Itzhak Perlman [“IT-zahk PURL-mun”] had this disease as a child. So did track star Wilma Rudolph, who wore a brace on her leg as a young girl but went on to win three gold medals at the 1960 Olympics in Rome.",
            "r": "For 10 points, name this disease that can cause paralysis, which Jonas Salk’s vaccine was made to prevent."
        },
        {
            "p": "Painter Frida Kahlo had this disease at age six, which left her right leg thinner than her left. Franklin Roosevelt was diagnosed with this disease at age 39, in 1921, while vacationing at his summer home on Campobello Island.",
            "r": "For 10 points, name this disease that can cause paralysis, which vaccines have nearly wiped out."
        },
        {
            "p": "In the early 1950s, many American parents kept their children away from swimming pools and movie theaters during the summer “season” of this disease, and 1952 brought the worst outbreak of it in U.S. history.",
            "r": "Its very contagious virus enters the body through the mouth and multiplies in the throat and intestines. For 10 points, name this disease prevented by Jonas Salk’s vaccine."
        },
        {
            "p": "Rarely, the weakened virus in one oral vaccine against this disease can change and spread in places where few people are vaccinated. In 1988, the World Health Organization, Rotary International, UNICEF, and the CDC launched a global effort to eradicate this disease.",
            "r": "Wiping it out would make it only the second human disease eradicated, after smallpox. For 10 points, name this disease that Jonas Salk and Albert Sabin made vaccines for."
        }
    ],
    "clues": [
        {
            "id": "salk",
            "tier": "giveaway",
            "t": "Jonas Salk, at the University of Pittsburgh, made the first successful vaccine against it, a shot of killed virus",
            "k": ["salk", "pittsburgh", "killed virus"],
            "n": 0,
            "rabbit": "Jonas Salk"
        },
        {
            "id": "sabin",
            "tier": "giveaway",
            "t": "Albert Sabin made an oral vaccine of live, weakened virus, often given on sugar cubes",
            "k": ["sabin", "oral", "sugar cubes"],
            "n": 0
        },
        {
            "id": "paralysis",
            "tier": "giveaway",
            "t": "A contagious viral disease that can cause paralysis, especially in young children",
            "k": ["paralysis", "contagious"],
            "n": 0
        },
        {
            "id": "fdr",
            "tier": "giveaway",
            "t": "Franklin D. Roosevelt was diagnosed with it in 1921, at age 39",
            "k": ["roosevelt", "1921"],
            "n": 0,
            "rabbit": "Franklin Delano Roosevelt"
        },
        {
            "id": "iron-lung",
            "tier": "giveaway",
            "t": "Iron lungs helped patients who could not breathe on their own",
            "k": ["iron lungs", "breathe"],
            "n": 0
        },
        {
            "id": "march-of-dimes",
            "tier": "middle",
            "t": "Eddie Cantor named FDR’s 1938 fundraising drive against it the “March of Dimes”; FDR went on the dime in 1946",
            "k": ["march of dimes", "eddie cantor", "dime"],
            "n": 0
        },
        {
            "id": "april-1955",
            "tier": "middle",
            "t": "Salk’s vaccine was announced safe and effective on April 12, 1955, ten years after FDR’s death",
            "k": ["april 12", "1955", "safe and effective"],
            "n": 0
        },
        {
            "id": "field-trial",
            "tier": "middle",
            "t": "Thomas Francis Jr. led the 1954 field trial of Salk’s vaccine, with more than a million schoolchildren",
            "k": ["thomas francis", "field trial", "1954"],
            "n": 0
        },
        {
            "id": "patent-sun",
            "tier": "middle",
            "t": "Asked by Edward R. Murrow about a patent, Salk replied, “Could you patent the sun?”",
            "k": ["murrow", "patent the sun"],
            "n": 0
        },
        {
            "id": "spinal-cord",
            "tier": "middle",
            "t": "Its virus attacks motor neurons in the spinal cord’s gray matter; its full name comes from Greek for “gray marrow”",
            "k": ["motor neurons", "spinal cord", "gray matter"],
            "n": 0
        },
        {
            "id": "enterovirus",
            "tier": "middle",
            "t": "Caused by an enterovirus that enters through the mouth; most infections cause no symptoms",
            "k": ["enterovirus", "mouth", "no symptoms"],
            "n": 0
        },
        {
            "id": "summer",
            "tier": "middle",
            "t": "Summer outbreaks kept 1950s children out of pools; 1952 was the worst year in U.S. history",
            "k": ["summer", "pools", "1952"],
            "n": 0
        },
        {
            "id": "eradication",
            "tier": "middle",
            "t": "A global eradication effort began in 1988 (WHO, Rotary, UNICEF, CDC); it would be the second human disease wiped out, after smallpox",
            "k": ["eradication", "1988", "smallpox"],
            "n": 0
        },
        {
            "id": "drinker-shaw",
            "tier": "power",
            "t": "Philip Drinker and Louis Agassiz Shaw built the iron lung in 1928",
            "k": ["drinker", "agassiz shaw", "1928"],
            "n": 0
        },
        {
            "id": "enders",
            "tier": "power",
            "t": "John Enders, Thomas Weller, and Frederick Robbins grew its virus in tissue culture (Nobel Prize, 1954)",
            "k": ["enders", "weller", "robbins", "tissue culture"],
            "n": 0
        },
        {
            "id": "landsteiner",
            "tier": "power",
            "t": "Karl Landsteiner (who also found the ABO blood groups) and Erwin Popper showed that a virus causes it",
            "k": ["landsteiner", "popper"],
            "n": 0,
            "rabbit": "Blood types"
        },
        {
            "id": "kenny",
            "tier": "power",
            "t": "Australian nurse Sister Elizabeth Kenny used hot packs and exercise instead of splints",
            "k": ["elizabeth kenny", "hot packs", "splints"],
            "n": 0
        },
        {
            "id": "warm-springs",
            "tier": "power",
            "t": "FDR founded a treatment center at Warm Springs, Georgia",
            "k": ["warm springs", "georgia"],
            "n": 0
        },
        {
            "id": "formaldehyde",
            "tier": "power",
            "t": "Salk’s vaccine used virus killed with formaldehyde",
            "k": ["formaldehyde"],
            "n": 0
        },
        {
            "id": "soviet-1959",
            "tier": "power",
            "t": "Sabin’s oral vaccine was tested on huge numbers of people in the Soviet Union in 1959",
            "k": ["soviet union", "1959"],
            "n": 0
        },
        {
            "id": "three-types",
            "tier": "power",
            "t": "Of three wild types, type 2 was declared eradicated in 2015 and type 3 in 2019",
            "k": ["type 2", "type 3", "2015", "2019"],
            "n": 0
        },
        {
            "id": "pakistan-afghanistan",
            "tier": "power",
            "t": "As of 2024, wild type 1 still spread only in Pakistan and Afghanistan",
            "k": ["pakistan", "afghanistan", "type 1"],
            "n": 0
        },
        {
            "id": "americas-india",
            "tier": "power",
            "t": "The last wild case in the Americas came in Peru (1991); India’s last came in 2011",
            "k": ["peru", "india", "1991", "2011"],
            "n": 0
        },
        {
            "id": "africa",
            "tier": "power",
            "t": "Africa was certified free of its wild virus in 2020; Nelson Mandela had helped launch a 1996 campaign to “kick” it out",
            "k": ["africa", "mandela", "2020", "nigeria"],
            "n": 0
        },
        {
            "id": "rudolph-perlman",
            "tier": "power",
            "t": "Track star Wilma Rudolph (three golds in 1960) and violinist Itzhak Perlman both had it as children",
            "k": ["wilma rudolph", "itzhak perlman", "1960"],
            "n": 0
        },
        {
            "id": "kahlo",
            "tier": "power",
            "t": "Painter Frida Kahlo had it at age six, which left her right leg thinner",
            "k": ["frida kahlo", "age six"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Disease or doctor?",
        "body": "Polio tossups and Jonas Salk tossups share many clues: the 1954 field trial, the April 1955 announcement, and “Could you patent the sun?” Players who hear those clues can blurt “Salk” when the question wants the disease, or “polio” when it asks for the scientist. Don’t confuse polio with smallpox either; smallpox is the only human disease already declared eradicated (in 1980).",
        "fix": "Listen for the noun: “this disease” or “this virus” means polio, while “this scientist” or “this man” means Salk or Sabin. Clues about Edward Jenner, cowpox, or eradication in 1980 point to smallpox instead.",
        "line": "Real answer line: <b><u>Polio</u></b> (accept <u>poliomyelitis</u>, <u>poliovirus</u>, or <u>infantile paralysis</u>; do not accept “smallpox”)"
    },
    "tests": {
        "right": [
            "Polio",
            "Poliomyelitis",
            "polio virus",
            "Infantile paralysis",
            "Pollio"
        ],
        "prompt": [
            "Enterovirus"
        ],
        "wrong": [
            "Smallpox",
            "Measles",
            "Jonas Salk",
            "Polo",
            "Rabies"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
