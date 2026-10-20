import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "diabetes",
    "name": "Diabetes",
    "mono": "DM",
    "category": "Biology",
    "qbCategory": "Science · Biology",
    "kicker": "A disease of high blood sugar · Linked to the hormone insulin",
    "dates": "Insulin treatment began in 1922",
    "briefing": "Diabetes is a disease in which the level of sugar in the blood stays too high, because the pancreas makes too little insulin or the body’s cells don’t respond to it well. In type 1, the immune system destroys the cells that make insulin; in type 2, the most common form, cells resist insulin’s signal. People with diabetes check their blood sugar and may take insulin by pen, shot, or pump, a treatment first used in 1922.",
    "answerHtml": "<b><u>Diabetes</u></b> mellitus (accept <u>type 1</u> or <u>type 2 diabetes</u>; prompt on <u>hyperglycemia</u> or <u>high blood sugar</u>; do not accept “diabetes insipidus”)",
    "accept": [
        "diabetes",
        "diabetes mellitus",
        "type 1 diabetes",
        "type 2 diabetes",
        "type one diabetes",
        "type two diabetes",
        "type i diabetes",
        "type ii diabetes",
        "juvenile diabetes",
        "sugar diabetes"
    ],
    "prompt": [
        "hyperglycemia",
        "hyperglycaemia",
        "high blood sugar"
    ],
    "reject": [
        "diabetes insipidus",
        "insipidus",
        "pre diabetes",
        "prediabetes",
        "prediabetic",
        "diabetic ketoacidosis",
        "ketoacidosis",
        "hypoglycemia",
        "hypoglycaemia",
        "low blood sugar",
        "insulin",
        "insulin resistance",
        "glucose",
        "glucagon",
        "pancreas",
        "beta cells",
        "islets of langerhans",
        "obesity",
        "hypertension",
        "high blood pressure",
        "kidney disease",
        "gout",
        "anemia",
        "celiac disease",
        "cystic fibrosis",
        "hypothyroidism",
        "hyperthyroidism",
        "metabolic syndrome"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Diabetes",
    "qb": {
        "q": "diabetes",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In 1675, English doctor Thomas Willis added a Latin word meaning “honey-sweet” to this disease’s name, because the urine of people with it was sweet with sugar. The Greek-based first word of that name means “to pass through,” because people with it urinate often.",
            "r": "People with this disease check their blood sugar and may take insulin. For 10 points, name this disease in which blood sugar runs too high."
        },
        {
            "p": "Ancient Indian doctors called this disease madhumeha [“MUH-dhoo-MAY-hah”], or “honey urine,” after noticing that ants were drawn to the urine of people who had it. The Greek doctor Aretaeus [“air-uh-TEE-us”] of Cappadocia also wrote a famous early description of it.",
            "r": "Many people with it use insulin pens or pumps. For 10 points, name this disease marked by high blood sugar."
        },
        {
            "p": "In 1889, Oskar Minkowski and Joseph von Mering found that dogs whose pancreas had been removed developed this disease. Twenty years earlier, Paul Langerhans had described small clusters of cells in that organ, later named for him.",
            "r": "In type 1 of this disease, the immune system destroys the pancreas’s insulin-making beta cells. For 10 points, name this disease."
        },
        {
            "p": "Elizabeth Hughes, daughter of U.S. Secretary of State Charles Evans Hughes, was one of the earliest patients treated with a new hormone for this disease in 1922. That January, a teenage boy named Leonard Thompson had become the first person given that hormone, at Toronto General Hospital.",
            "r": "That hormone was insulin, which people with type 1 of this disease need every day. For 10 points, name this disease marked by high blood sugar."
        },
        {
            "p": "Metformin, a common medicine for one form of this disease, was developed from galegine [“GAL-uh-jeen”], a chemical in goat’s rue, a flowering plant also called French lilac. Doctors in Europe began prescribing it in the late 1950s.",
            "r": "In that form, called type 2, the body’s cells respond poorly to insulin. For 10 points, name this disease marked by high blood sugar."
        },
        {
            "p": "If people with this disease have too little of a certain hormone, their bodies burn fat and make acids called ketones, which can build up dangerously and give the breath a fruity smell. That emergency is called ketoacidosis [“kee-toh-ass-ih-DOH-sis”].",
            "r": "It happens most often in type 1 of this disease, in which the body makes almost no insulin. For 10 points, name this disease marked by high blood sugar."
        },
        {
            "p": "Frederick Banting got the idea for his research on this disease in October 1920, after reading an article about what happens when the pancreas’s ducts get blocked. He later carried out that research with Charles Best in J. J. R. Macleod’s lab.",
            "r": "Their work produced insulin, which people with type 1 of this disease need. For 10 points, name this disease."
        },
        {
            "p": "The United Nations officially recognized this disease’s worldwide awareness day in 2006; it falls on November 14, the birthday of a Canadian scientist. The day’s symbol is a blue circle.",
            "r": "That scientist, Frederick Banting, helped discover insulin. For 10 points, name this disease in which blood sugar runs too high."
        },
        {
            "p": "In London, Ontario, a “Flame of Hope” burns near the house where Frederick Banting lived when he got his big idea, and it is meant to be put out only when a cure for this disease is found.",
            "r": "People with this disease may use insulin pumps. For 10 points, name this disease marked by high blood sugar."
        },
        {
            "p": "Doctors call three classic warning signs of this disease the “three P’s”: polyuria [“pah-lee-YOOR-ee-uh”], or frequent urination; polydipsia [“pah-lee-DIP-see-uh”], or extreme thirst; and polyphagia [“pah-lee-FAY-jee-uh”], or extreme hunger. Many people also feel very tired or notice blurry vision.",
            "r": "For 10 points, name this disease in which the body makes too little insulin or uses it poorly."
        },
        {
            "p": "In the most common form of this disease, muscle and fat cells fail to move enough GLUT4 transporter proteins to their surfaces when a certain hormone signals them. That form makes up about 90 to 95 percent of all cases.",
            "r": "That form, type 2, is marked by insulin resistance. For 10 points, name this disease marked by high blood sugar."
        },
        {
            "p": "Sonia Sotomayor, who joined the U.S. Supreme Court in 2009, learned she had this disease at age seven. Her picture book _Just Ask!_ features a girl named Sonia who lives with it.",
            "r": "She has type 1, in which the body makes almost no insulin. For 10 points, name this disease marked by high blood sugar."
        },
        {
            "p": "Doctors track this disease with the A1C test, which measures glycated [“GLY-kay-ted”] hemoglobin inside red blood cells and reflects average levels over the past two to three months. Glycated means that sugar molecules have stuck to the protein.",
            "r": "Some people with this disease link a glucose sensor to an insulin pump to make an “artificial pancreas.” For 10 points, name this disease."
        },
        {
            "p": "Eye doctors look for damage that this disease can cause to the tiny blood vessels of the retina, and over many years it can also harm the kidneys and the nerves in the feet.",
            "r": "That damage happens when blood sugar stays too high for a long time. For 10 points, name this disease treated with insulin."
        },
        {
            "p": "A rare condition linked to the hormone ADH, also called vasopressin, shares the first word of this disease’s name, but its Latin second word means “tasteless,” because the large amounts of urine it causes contain no sugar.",
            "r": "This disease, by contrast, is marked by high blood sugar. For 10 points, name this disease whose type 1 and type 2 forms involve insulin."
        }
    ],
    "clues": [
        {
            "id": "high-blood-sugar",
            "tier": "giveaway",
            "t": "A disease in which blood sugar (glucose) stays too high",
            "k": ["blood sugar", "glucose"],
            "n": 0,
            "rabbit": "Glucose"
        },
        {
            "id": "insulin",
            "tier": "giveaway",
            "t": "Caused by too little insulin or by cells that respond poorly to it; many people with it take insulin",
            "k": ["insulin"],
            "n": 0,
            "rabbit": "Insulin"
        },
        {
            "id": "two-types",
            "tier": "giveaway",
            "t": "Two main types: type 1 (the immune system destroys insulin-making cells) and type 2 (cells respond poorly to insulin)",
            "k": ["type 1", "type 2"],
            "n": 0
        },
        {
            "id": "pancreas",
            "tier": "giveaway",
            "t": "The pancreas’s beta cells make the insulin that keeps blood sugar in check",
            "k": ["pancreas", "beta cells"],
            "n": 0,
            "rabbit": "Pancreas"
        },
        {
            "id": "monitoring",
            "tier": "giveaway",
            "t": "People with it check their blood sugar with finger-prick meters or sensors and may use insulin pens or pumps",
            "k": ["finger-prick", "sensors", "pumps"],
            "n": 0
        },
        {
            "id": "autoimmune",
            "tier": "middle",
            "t": "Type 1 is autoimmune and often starts in childhood; it was once called “juvenile”",
            "k": ["autoimmune", "juvenile"],
            "n": 0
        },
        {
            "id": "type-2-common",
            "tier": "middle",
            "t": "Type 2 makes up about 90 to 95 percent of cases and often runs in families",
            "k": ["90 to 95 percent", "runs in families"],
            "n": 0
        },
        {
            "id": "three-ps",
            "tier": "middle",
            "t": "Classic warning signs, the “three P’s”: frequent urination, extreme thirst, and extreme hunger",
            "k": ["frequent urination", "extreme thirst", "three p"],
            "n": 0
        },
        {
            "id": "a1c",
            "tier": "middle",
            "t": "The A1C test measures sugar stuck to hemoglobin over the past two to three months",
            "k": ["hemoglobin", "a1c"],
            "n": 0,
            "rabbit": "Hemoglobin"
        },
        {
            "id": "banting-best",
            "tier": "middle",
            "t": "Frederick Banting and Charles Best discovered insulin in Toronto in 1921, giving people with it a treatment",
            "k": ["banting", "best", "toronto", "1921"],
            "n": 0
        },
        {
            "id": "name-meaning",
            "tier": "middle",
            "t": "Its Greek name means “to pass through”; its full name adds a Latin word meaning “honey-sweet”",
            "k": ["pass through", "honey-sweet"],
            "n": 0
        },
        {
            "id": "complications",
            "tier": "middle",
            "t": "Over many years, high blood sugar can damage the retina, the kidneys, and the nerves",
            "k": ["retina", "kidneys", "nerves"],
            "n": 0,
            "rabbit": "Retina"
        },
        {
            "id": "insipidus",
            "tier": "middle",
            "t": "Not the same as the “insipidus” condition, a rare water-balance problem linked to the hormone ADH (vasopressin)",
            "k": ["insipidus", "vasopressin", "adh"],
            "n": 0
        },
        {
            "id": "artificial-pancreas",
            "tier": "middle",
            "t": "An “artificial pancreas” links a glucose sensor to an insulin pump",
            "k": ["artificial pancreas", "sensor"],
            "n": 0
        },
        {
            "id": "willis",
            "tier": "power",
            "t": "English doctor Thomas Willis added the Latin “honey-sweet” part of its name in 1675",
            "k": ["thomas willis", "1675"],
            "n": 0
        },
        {
            "id": "madhumeha",
            "tier": "power",
            "t": "Ancient Indian doctors called it madhumeha, “honey urine,” noticing that ants were drawn to patients’ urine",
            "k": ["madhumeha", "honey urine", "ants"],
            "n": 0
        },
        {
            "id": "aretaeus",
            "tier": "power",
            "t": "The Greek doctor Aretaeus of Cappadocia wrote a famous early description of it",
            "k": ["aretaeus", "cappadocia"],
            "n": 0
        },
        {
            "id": "minkowski",
            "tier": "power",
            "t": "Oskar Minkowski and Joseph von Mering (1889) found that dogs whose pancreas was removed developed it",
            "k": ["minkowski", "von mering", "1889"],
            "n": 0
        },
        {
            "id": "early-patients",
            "tier": "power",
            "t": "Leonard Thompson, a teenage boy, was the first person treated with insulin (Toronto General Hospital, January 1922); Elizabeth Hughes was another early patient",
            "k": ["leonard thompson", "elizabeth hughes", "1922"],
            "n": 0
        },
        {
            "id": "metformin",
            "tier": "power",
            "t": "Metformin, a common type 2 medicine, was developed from galegine, a chemical in goat’s rue (French lilac)",
            "k": ["metformin", "galegine", "french lilac"],
            "n": 0
        },
        {
            "id": "ketoacidosis",
            "tier": "power",
            "t": "With too little insulin, the body makes ketones that can build up dangerously (ketoacidosis), sometimes with fruity-smelling breath",
            "k": ["ketoacidosis", "ketones", "fruity"],
            "n": 0
        },
        {
            "id": "banting-idea",
            "tier": "power",
            "t": "Banting got his idea in October 1920 after reading about blocked pancreatic ducts; he worked in J. J. R. Macleod’s lab",
            "k": ["october 1920", "macleod", "ducts"],
            "n": 0
        },
        {
            "id": "awareness-day",
            "tier": "power",
            "t": "Its awareness day, November 14, is Frederick Banting’s birthday; the UN recognized the day in 2006, and its symbol is a blue circle",
            "k": ["november 14", "blue circle", "2006"],
            "n": 0
        },
        {
            "id": "flame-of-hope",
            "tier": "power",
            "t": "A “Flame of Hope” in London, Ontario, near Banting’s house, is meant to burn until a cure is found",
            "k": ["flame of hope", "london"],
            "n": 0
        },
        {
            "id": "glut4",
            "tier": "power",
            "t": "In type 2, muscle and fat cells fail to move enough GLUT4 transporters to their surfaces, part of insulin resistance",
            "k": ["insulin resistance", "glut4"],
            "n": 0
        },
        {
            "id": "sotomayor",
            "tier": "power",
            "t": "Sonia Sotomayor, who joined the Supreme Court in 2009, learned she had type 1 at age seven; her picture book _Just Ask!_ features a girl who lives with it",
            "k": ["sotomayor", "just ask"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Mellitus or insipidus?",
        "body": "Two different conditions share the word “diabetes,” from the Greek for “to pass through,” because both make people urinate a lot. Diabetes mellitus (“honey-sweet”) is about blood sugar and insulin. Diabetes insipidus (“tasteless”) is a rare water-balance problem involving the hormone ADH, and a question about the sugar disease won’t accept it. Others buzz with “insulin” or “pancreas,” the hormone or the organ, instead of the disease.",
        "fix": "Insulin, beta cells, glucose, the A1C test, or Banting and Best mean diabetes mellitus (plain “diabetes” is fine). ADH, vasopressin, or urine with no sugar mean diabetes insipidus. If the question asks for “this hormone” or “this organ,” answer insulin or pancreas instead.",
        "line": "Real answer line: <b><u>Diabetes</u></b> mellitus (accept <u>type 1</u> or <u>type 2 diabetes</u>; do not accept “diabetes insipidus”)"
    },
    "tests": {
        "right": [
            "Diabetes",
            "Diabetes mellitus",
            "Type 1 diabetes",
            "Type 2 diabetes",
            "Diabetis"
        ],
        "prompt": [
            "Hyperglycemia",
            "High blood sugar"
        ],
        "wrong": [
            "Diabetes insipidus",
            "Insulin",
            "Hypoglycemia",
            "Pancreas",
            "Prediabetes",
            "Glucose"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
