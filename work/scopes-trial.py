import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "scopes-trial",
    "name": "Scopes Trial",
    "mono": "SMT",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "1925 Tennessee trial over teaching evolution · Darrow versus Bryan",
    "dates": "July 10–21, 1925",
    "briefing": "In the summer of 1925, the small town of Dayton, Tennessee, hosted one of the most famous trials in American history. A young teacher named John Scopes was charged with breaking the Butler Act, a new state law that banned teaching that humans descended from other animals. The famous lawyer Clarence Darrow defended him and William Jennings Bryan helped prosecute him; Scopes was found guilty and fined $100, though the verdict was later thrown out on a technicality.",
    "answerHtml": "<b><u>Scopes</u></b> Monkey <b><u>Trial</u></b> (accept <u>Monkey Trial</u> or <u>State of Tennessee v. John Thomas Scopes</u>; prompt on <u>Scopes</u> alone)",
    "accept": [
        "scopes trial",
        "scopes monkey trial",
        "monkey trial",
        "scopes case",
        "scopes evolution trial",
        "trial of john scopes",
        "tennessee v scopes",
        "state of tennessee v scopes",
        "tennessee v john scopes",
        "tennessee v john t scopes",
        "state of tennessee v john thomas scopes",
        "scopes v state",
        "scopes v tennessee",
        "state v scopes"
    ],
    "prompt": [
        "scopes",
        "john scopes",
        "john t scopes",
        "john thomas scopes",
        "scopes monkey"
    ],
    "reject": [
        "butler act",
        "inherit the wind",
        "clarence darrow",
        "darrow",
        "william jennings bryan",
        "bryan",
        "evolution",
        "human evolution",
        "charles darwin",
        "darwin",
        "epperson v arkansas",
        "kitzmiller v dover",
        "dayton",
        "salem witch trials",
        "leopold and loeb"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Scopes_trial",
    "qb": {
        "q": "Scopes",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In 1927, the Tennessee Supreme Court threw out the verdict in this case on a technicality: the judge, not the jury, had set the $100 fine, even though the state constitution required a jury to set any fine over $50.",
            "r": "The court still upheld the Butler Act. For 10 points, name this 1925 trial in Dayton, Tennessee, over the teaching of evolution."
        },
        {
            "p": "Worried that the crowded courtroom floor might give way in the summer heat, the judge in this case moved the proceedings onto the courthouse lawn. There, the defense called a lawyer for the other side to the witness stand as an expert on the Bible.",
            "r": "That expert, William Jennings Bryan, was questioned by Clarence Darrow. For 10 points, name this 1925 trial of a Tennessee teacher."
        },
        {
            "p": "At Robinson’s Drug Store, local businessman George Rappleyea and others planned this case, hoping it would put their small town on the map. They persuaded a 24-year-old science teacher and football coach to serve as the defendant, though he was not even sure he had taught the lesson in question.",
            "r": "The American Civil Liberties Union had offered to defend any teacher who challenged the law. For 10 points, name this 1925 trial in Dayton, Tennessee."
        },
        {
            "p": "The defendant in this case was accused of teaching from George William Hunter’s textbook _A Civic Biology_, which the state itself had approved for its schools. The case was brought under a law that banned teaching that humans had descended from “a lower order of animals.”",
            "r": "That law was the Butler Act. For 10 points, name this 1925 trial in which Clarence Darrow defended a Tennessee teacher."
        },
        {
            "p": "In a play based on this event, Henry Drummond defends the teacher Bertram Cates against the famous orator Matthew Harrison Brady, while a sharp-tongued reporter named E. K. Hornbeck looks on. Spencer Tracy and Fredric March starred in the 1960 film version of that play.",
            "r": "That play is _Inherit the Wind_. For 10 points, name this real 1925 trial in Dayton, Tennessee."
        },
        {
            "p": "A Tennessee college founded in 1930 honors a man who died just five days after this case ended. That man, a three-time presidential nominee, argued that voters and taxpayers had the right to decide what their public schools taught.",
            "r": "That man, William Jennings Bryan, helped prosecute this case. For 10 points, name this 1925 trial over teaching evolution in Tennessee."
        },
        {
            "p": "Chicago radio station WGN broadcast this case live, though its defendant never took the witness stand. H. L. Mencken covered this case for the _Baltimore Sun_, one of many reporters who crowded into the small town where it took place.",
            "r": "Clarence Darrow led the defense. For 10 points, name this 1925 trial of a Tennessee teacher charged with teaching evolution."
        },
        {
            "p": "At the end of this case, the defense lawyer asked the jury to find his own client guilty so that the case could be appealed to a higher court. The jury took only about nine minutes to reach its verdict, and the judge fined the defendant $100.",
            "r": "For 10 points, name this 1925 trial in Dayton, Tennessee, in which Clarence Darrow defended a teacher accused of teaching evolution."
        },
        {
            "p": "The law at the center of this case stayed on the books until 1967. A farmer and Tennessee lawmaker named John Washington Butler wrote that law, which made it illegal for public school teachers to teach any theory that denied the Bible’s account of the creation of humans.",
            "r": "For 10 points, name this 1925 trial in Dayton in which Clarence Darrow faced William Jennings Bryan."
        },
        {
            "p": "In 1968, the U.S. Supreme Court ruled in _Epperson v. Arkansas_ that a state ban on teaching evolution violated the First Amendment’s ban on establishing a religion. Tennessee had repealed the law tested in this case just one year earlier.",
            "r": "That law was the Butler Act. For 10 points, name this 1925 trial in which Clarence Darrow defended a teacher in Dayton, Tennessee."
        },
        {
            "p": "Dudley Field Malone and Arthur Garfield Hays joined the defense in this case, while local prosecutor Tom Stewart had help from a famous politician and his son. Judge John Raulston refused to let the defense’s expert scientists testify before the jury.",
            "r": "For 10 points, name this 1925 trial in which Clarence Darrow faced William Jennings Bryan."
        },
        {
            "p": "The defendant in this case later studied geology and worked in the oil industry, and he told his side of the story in a 1967 memoir called _Center of the Storm_. During the trial itself, he never took the witness stand.",
            "r": "For 10 points, name this 1925 trial of a Tennessee teacher, in which Clarence Darrow faced William Jennings Bryan."
        },
        {
            "p": "The day after a witness in this case said that the “days” of creation might have been long periods of time, the judge ordered that witness’s testimony struck from the record. That witness had been asked whether a whale had really swallowed Jonah and whether Joshua had made the sun stand still.",
            "r": "That witness was William Jennings Bryan, questioned by Clarence Darrow. For 10 points, name this 1925 trial in Dayton, Tennessee."
        },
        {
            "p": "This case was heard at the Rhea [“RAY”] County Courthouse, which became a National Historic Landmark with a museum about this case. In this case, one side argued that voters had the right to decide what public schools taught, while the other side argued for teachers’ freedom to teach science.",
            "r": "Clarence Darrow led the defense. For 10 points, name this 1925 trial in Dayton, Tennessee, over the teaching of evolution."
        },
        {
            "p": "One lawyer in this case had earlier defended the labor leader Eugene V. Debs after the Pullman Strike. In this case, that lawyer objected to opening each day’s session with a prayer, and he was cited for contempt of court, though the judge forgave him after he apologized.",
            "r": "That lawyer, Clarence Darrow, defended a Tennessee teacher. For 10 points, name this 1925 trial over the teaching of evolution."
        }
    ],
    "clues": [
        {
            "id": "evolution-1925",
            "tier": "giveaway",
            "t": "1925 trial of a Tennessee teacher charged with teaching human evolution",
            "k": ["1925", "evolution", "teacher"],
            "n": 0,
            "rabbit": "Evolution"
        },
        {
            "id": "darrow-bryan",
            "tier": "giveaway",
            "t": "Clarence Darrow led the defense; William Jennings Bryan helped the prosecution",
            "k": ["clarence darrow", "darrow", "william jennings bryan", "bryan"],
            "n": 0,
            "rabbit": "William Jennings Bryan"
        },
        {
            "id": "dayton",
            "tier": "giveaway",
            "t": "Held in the small town of Dayton, Tennessee",
            "k": ["dayton", "tennessee"],
            "n": 0
        },
        {
            "id": "defendant",
            "tier": "middle",
            "t": "The defendant was a 24-year-old high school science teacher and football coach",
            "k": ["defendant", "24-year-old", "coach"],
            "n": 0
        },
        {
            "id": "butler-act",
            "tier": "middle",
            "t": "Tested the Butler Act, which banned teaching that humans descended from “a lower order of animals”",
            "k": ["butler act", "butler", "lower order"],
            "n": 0
        },
        {
            "id": "aclu",
            "tier": "middle",
            "t": "The American Civil Liberties Union (ACLU) offered to defend any teacher who challenged the law",
            "k": ["american civil liberties union", "aclu"],
            "n": 0
        },
        {
            "id": "two-sides",
            "tier": "middle",
            "t": "One side said voters should decide what public schools teach; the other argued for teachers’ freedom to teach science",
            "k": ["voters", "freedom", "public schools"],
            "n": 0
        },
        {
            "id": "bible-expert",
            "tier": "middle",
            "t": "Darrow called Bryan to the witness stand as an expert on the Bible and asked about stories like Jonah and the whale",
            "k": ["bible", "jonah", "witness stand"],
            "n": 0
        },
        {
            "id": "guilty-fine",
            "tier": "middle",
            "t": "The jury found the teacher guilty, and he was fined $100",
            "k": ["guilty", "$100", "fined"],
            "n": 0
        },
        {
            "id": "inherit-the-wind",
            "tier": "middle",
            "t": "Retold in the play _Inherit the Wind_ (1955), with Henry Drummond (Darrow) and Matthew Harrison Brady (Bryan)",
            "k": ["inherit the wind", "drummond", "brady"],
            "n": 0,
            "rabbit": "Inherit the Wind"
        },
        {
            "id": "bryan-death",
            "tier": "middle",
            "t": "Bryan died in Dayton five days after the trial ended; Bryan College (founded 1930) honors him",
            "k": ["five days", "bryan college", "1930"],
            "n": 0
        },
        {
            "id": "appeal-1927",
            "tier": "middle",
            "t": "In 1927, the Tennessee Supreme Court threw out the verdict on a technicality (the judge, not the jury, set the fine) but upheld the law",
            "k": ["1927", "technicality", "tennessee supreme court"],
            "n": 0
        },
        {
            "id": "mencken",
            "tier": "middle",
            "t": "Journalist H. L. Mencken covered the trial for the _Baltimore Sun_",
            "k": ["mencken", "baltimore sun"],
            "n": 0
        },
        {
            "id": "civic-biology",
            "tier": "power",
            "t": "The teacher used George William Hunter’s state-approved textbook _A Civic Biology_",
            "k": ["civic biology", "hunter", "textbook"],
            "n": 0
        },
        {
            "id": "rappleyea",
            "tier": "power",
            "t": "Planned at Robinson’s Drug Store by George Rappleyea and other businessmen who wanted publicity for Dayton",
            "k": ["rappleyea", "drug store", "publicity"],
            "n": 0
        },
        {
            "id": "lawn",
            "tier": "power",
            "t": "Moved outdoors to the courthouse lawn, where Darrow questioned Bryan; the judge then struck that testimony from the record",
            "k": ["lawn", "outdoors", "struck"],
            "n": 0
        },
        {
            "id": "days-of-creation",
            "tier": "power",
            "t": "Asked about Joshua making the sun stand still, Bryan said the “days” of creation might have been long periods of time",
            "k": ["joshua", "long periods", "creation"],
            "n": 0
        },
        {
            "id": "nine-minutes",
            "tier": "power",
            "t": "Darrow asked the jury to find his client guilty so he could appeal; the jury took about nine minutes",
            "k": ["nine minutes", "appeal"],
            "n": 0
        },
        {
            "id": "john-butler",
            "tier": "power",
            "t": "The law was written by farmer and lawmaker John Washington Butler, signed by Governor Austin Peay, and repealed in 1967",
            "k": ["john washington butler", "austin peay", "peay", "1967"],
            "n": 0
        },
        {
            "id": "epperson",
            "tier": "power",
            "t": "_Epperson v. Arkansas_ (1968): the U.S. Supreme Court struck down a state ban on teaching evolution",
            "k": ["epperson", "1968", "arkansas"],
            "n": 0
        },
        {
            "id": "lawyers",
            "tier": "power",
            "t": "Dudley Field Malone and Arthur Garfield Hays helped the defense; Tom Stewart and William Jennings Bryan Jr. helped prosecute",
            "k": ["dudley field malone", "malone", "hays", "tom stewart"],
            "n": 0
        },
        {
            "id": "raulston",
            "tier": "power",
            "t": "Judge John Raulston kept the defense’s expert scientists from testifying before the jury",
            "k": ["raulston", "expert", "scientists"],
            "n": 0
        },
        {
            "id": "wgn",
            "tier": "power",
            "t": "Chicago radio station WGN broadcast the trial live",
            "k": ["wgn", "radio", "broadcast"],
            "n": 0
        },
        {
            "id": "center-storm",
            "tier": "power",
            "t": "The teacher never testified; he later worked as an oil geologist and wrote the memoir _Center of the Storm_ (1967)",
            "k": ["center of the storm", "geologist", "testified"],
            "n": 0
        },
        {
            "id": "debs-contempt",
            "tier": "power",
            "t": "Darrow, who had defended labor leader Eugene V. Debs, objected to opening prayers and was cited for contempt",
            "k": ["debs", "contempt", "prayers"],
            "n": 0
        },
        {
            "id": "film-1960",
            "tier": "power",
            "t": "Spencer Tracy and Fredric March starred in the 1960 film of _Inherit the Wind_; reporter E. K. Hornbeck is based on Mencken",
            "k": ["spencer tracy", "fredric march", "hornbeck"],
            "n": 0
        },
        {
            "id": "courthouse",
            "tier": "power",
            "t": "Held at the Rhea County Courthouse, later a National Historic Landmark with a museum about the trial",
            "k": ["rhea county", "courthouse", "national historic landmark"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Trial, teacher, or lawyer?",
        "body": "This trial turns up inside tossups on several other answers. John Scopes was the teacher on trial, Clarence Darrow was his defense lawyer, William Jennings Bryan helped the prosecution, the Butler Act was the law being tested, and _Inherit the Wind_ is the play based on the trial, with the names changed.",
        "fix": "Listen for the noun: “this trial” or “this case” wants the Scopes Trial; “this teacher” wants Scopes; “this lawyer” or “this orator” wants Darrow or Bryan; “this law” wants the Butler Act; “this play” wants _Inherit the Wind_. Saying only “Scopes” on a question about the trial gets a prompt, so add “Trial.”",
        "line": "Real answer line: <b><u>Scopes</u></b> Monkey <b><u>Trial</u></b> (accept <u>Monkey Trial</u> or <u>State of Tennessee v. John Thomas Scopes</u>; prompt on <u>Scopes</u>)"
    },
    "tests": {
        "right": [
            "Scopes Trial",
            "Scopes Monkey Trial",
            "the Monkey Trial",
            "Tennessee v. Scopes",
            "Scopes Trail"
        ],
        "prompt": [
            "Scopes",
            "John Scopes"
        ],
        "wrong": [
            "Butler Act",
            "Inherit the Wind",
            "Clarence Darrow",
            "William Jennings Bryan",
            "Epperson v. Arkansas",
            "Salem witch trials"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
