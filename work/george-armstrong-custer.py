import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def T(p, r):
    return {"p": p, "r": r}


def C(cid, tier, t, k, rabbit=None):
    c = {"id": cid, "tier": tier, "t": t, "k": k, "n": 0}
    if rabbit:
        c["rabbit"] = rabbit
    return c


data = {
    "id": "george-armstrong-custer",
    "name": "George Armstrong Custer",
    "mono": "GAC",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Union cavalry general · Killed at the Battle of the Little Bighorn",
    "dates": "1839–1876",
    "briefing": "George Armstrong Custer finished last in his West Point class, then became a Union general at just 23, famous for his long golden hair and daring cavalry charges. After the Civil War he led the 7th Cavalry on the Great Plains. On June 25, 1876, he attacked a huge camp of Lakota and Cheyenne people along Montana’s Little Bighorn River, and warriors led by Crazy Horse and others defeated his troops; he and every soldier in his part of the regiment were killed.",
    "answerHtml": "George Armstrong <b><u>Custer</u></b>",
    "accept": [
        "george armstrong custer",
        "george custer",
        "custer",
        "george a custer",
        "g a custer",
        "general custer",
        "general george custer"
    ],
    "prompt": [],
    "reject": [
        "elizabeth custer",
        "libbie custer",
        "elizabeth bacon custer",
        "tom custer",
        "thomas custer",
        "boston custer",
        "custers last stand",
        "custer battlefield",
        "little bighorn",
        "battle of the little bighorn",
        "battle of little bighorn",
        "little big horn",
        "greasy grass",
        "sitting bull",
        "crazy horse",
        "marcus reno",
        "frederick benteen",
        "alfred terry",
        "george crook",
        "philip sheridan",
        "nelson miles",
        "jeb stuart",
        "j e b stuart",
        "george meade",
        "george mcclellan",
        "george pickett",
        "john buford",
        "black kettle",
        "wounded knee",
        "wounded knee massacre",
        "sand creek",
        "washita"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/George_Armstrong_Custer",
    "qb": {
        "q": "Custer",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        T("This man graduated last in his West Point class of 1861, but two years later, at only 23, he was promoted to brigadier general, making him one of the youngest generals in the Union army.",
          "Newspapers called him the “Boy General.” For 10 points, name this cavalry officer who was killed at the Battle of the Little Bighorn."),
        T("On the last day of the Battle of Gettysburg, this man’s Michigan cavalry brigade helped stop J. E. B. Stuart’s Confederate horsemen in a fight east of town. He led his men into battle with the cry “Come on, you Wolverines!”",
          "For 10 points, name this Union cavalry general who later died fighting the Lakota and Cheyenne in 1876."),
        T("General Philip Sheridan bought the small table on which Ulysses S. Grant wrote out the terms of Robert E. Lee’s surrender and gave it to this man’s wife, Elizabeth. This man’s cavalry had helped block Lee’s escape in the final days of the war.",
          "He later led the 7th Cavalry. For 10 points, name this commander who died at the Little Bighorn in 1876."),
        T("In 1867, this officer was court-martialed for leaving his post without permission to visit his wife, and he was suspended from the Army for a year without pay. Philip Sheridan called him back early to lead a winter campaign on the southern Plains.",
          "For 10 points, name this lieutenant colonel of the 7th Cavalry who was killed at the Little Bighorn."),
        T("In November 1868, this man’s soldiers attacked a Cheyenne village on the Washita [“WOSH-ih-taw”] River in what is now Oklahoma, killing the peace-seeking chief Black Kettle and many other people. Black Kettle had survived the Sand Creek Massacre four years earlier.",
          "For 10 points, name this commander of the 7th Cavalry, who was defeated at the Little Bighorn eight years later."),
        T("In 1874, this man led an Army expedition into the Black Hills, land promised to the Lakota by the 1868 Treaty of Fort Laramie. Reports of gold from that trip set off a rush of miners onto the land.",
          "For 10 points, name this officer whose 7th Cavalry was defeated at the Little Bighorn two years later."),
        T("In 1876, this man angered President Ulysses S. Grant by testifying to Congress about corruption linked to Secretary of War William Belknap. Grant at first refused to let this man go on that summer’s campaign against the Lakota.",
          "Grant relented, and this man led the 7th Cavalry into Montana. For 10 points, name this officer killed at the Little Bighorn."),
        T("A horse named Comanche, ridden by Captain Myles Keogh [“KEE-oh”], was found badly hurt but alive after this man’s final battle and became a famous symbol of that fight. Comanche’s preserved body is displayed at the University of Kansas.",
          "For 10 points, name this commander of the 7th Cavalry, who died at the Little Bighorn in 1876."),
        T("This man’s younger brother Tom, who had won two Medals of Honor during the Civil War, died alongside him in 1876. Another brother, Boston, a teenage nephew, and his brother-in-law James Calhoun were also killed in that battle.",
          "For 10 points, name this 7th Cavalry commander who was defeated at the Little Bighorn."),
        T("Before his final battle, this man split his regiment, sending Major Marcus Reno to attack one end of a huge village and Captain Frederick Benteen to scout the hills to the south. Most of the soldiers with Reno and Benteen survived on a hilltop.",
          "For 10 points, name this commander who was killed with every soldier in his own part of the 7th Cavalry at the Little Bighorn."),
        T("Eight days before this man’s death, warriors led by Crazy Horse fought General George Crook’s column to a standstill at the Battle of the Rosebud in Montana Territory. Crook’s men pulled back to resupply and took no part in the fighting that followed.",
          "For 10 points, name this 7th Cavalry commander defeated by Lakota and Cheyenne warriors at the Little Bighorn."),
        T("This man’s regiment adopted the Irish tune “Garryowen” as its marching song. His last message, carried by trumpeter John Martin, told Captain Frederick Benteen: “Come on. Big village. Be quick. Bring packs.”",
          "He led the 7th Cavalry. For 10 points, name this commander killed with all the soldiers under his direct command at the Little Bighorn in 1876."),
        T("This man wrote the memoir _My Life on the Plains_, and after his death his widow, Elizabeth, spent decades defending his reputation in books such as _Boots and Saddles_. She also wrote _Tenting on the Plains_ and _Following the Guidon_.",
          "For 10 points, name this cavalry officer who died at the Battle of the Little Bighorn."),
        T("In 1991, Congress renamed a national monument in Montana that had been named for this man. In 2003, an Indian Memorial was added there to honor the Native people who fought and died in the battle.",
          "For 10 points, name this commander of the 7th Cavalry, whose “Last Stand” took place in June 1876."),
        T("Weeks before this man’s death, the Hunkpapa [“HUNK-pah-pah”] Lakota leader Sitting Bull had a vision at a Sun Dance of soldiers falling into his people’s camp. The Lakota and Cheyenne call the battle that followed the Battle of the Greasy Grass.",
          "For 10 points, name this U.S. cavalry commander who was killed in that battle, the Little Bighorn.")
    ],
    "clues": [
        C("little-bighorn", "giveaway", "Killed with all the soldiers under his direct command at the Battle of the Little Bighorn (June 25, 1876), his “Last Stand”", ["little bighorn", "last stand", "june 25, 1876"], "Battle of the Little Bighorn"),
        C("seventh-cavalry", "giveaway", "Commanded the U.S. 7th Cavalry on the Great Plains", ["7th cavalry", "great plains"]),
        C("lakota-cheyenne", "giveaway", "Defeated by Lakota and Cheyenne warriors; Sitting Bull and Crazy Horse were their best-known leaders", ["sitting bull", "crazy horse", "lakota", "cheyenne"], "Sitting Bull"),
        C("boy-general", "giveaway", "Union cavalry general in the Civil War, nicknamed the “Boy General”", ["boy general", "civil war"]),
        C("west-point", "middle", "Graduated last in his West Point class of 1861", ["west point", "1861", "last"]),
        C("gettysburg", "middle", "At Gettysburg (July 3, 1863), his Michigan brigade helped stop J. E. B. Stuart’s cavalry", ["gettysburg", "michigan", "stuart"], "Battle of Gettysburg"),
        C("wolverines", "middle", "His battle cry: “Come on, you Wolverines!”", ["wolverines", "come on"]),
        C("black-hills", "middle", "Led the 1874 Black Hills Expedition, which found gold on land promised to the Lakota by the 1868 Treaty of Fort Laramie", ["black hills", "gold", "fort laramie"]),
        C("washita", "middle", "His troops attacked Black Kettle’s Cheyenne village on the Washita River (1868)", ["washita", "black kettle"]),
        C("reno-benteen", "middle", "Split his regiment, sending Major Marcus Reno and Captain Frederick Benteen in other directions; most of their men survived", ["marcus reno", "reno", "frederick benteen", "benteen"]),
        C("elizabeth", "middle", "His wife, Elizabeth (“Libbie”), defended his memory in books like _Boots and Saddles_", ["elizabeth", "libbie", "boots and saddles"]),
        C("appomattox", "middle", "His cavalry helped block Lee’s retreat; Sheridan gave his wife the table on which Grant wrote the surrender terms", ["appomattox", "table", "sheridan"]),
        C("brigadier", "power", "Promoted to brigadier general at 23, days before Gettysburg (June 1863)", ["brigadier general", "june 1863"]),
        C("court-martial", "power", "Court-martialed in 1867 for leaving his post to visit his wife; suspended for a year without pay", ["court-martialed", "1867", "suspended"]),
        C("my-life", "power", "Wrote the memoir _My Life on the Plains_ (1874)", ["my life on the plains"]),
        C("belknap", "power", "Angered President Grant by testifying (1876) about corruption tied to Secretary of War William Belknap", ["belknap", "grant", "testifying"]),
        C("brothers", "power", "His brothers Tom (two Medals of Honor) and Boston died with him, along with a nephew and his brother-in-law", ["medals of honor", "tom", "boston"]),
        C("comanche", "power", "Comanche, Captain Myles Keogh’s horse, survived the battle; it is preserved at the University of Kansas", ["comanche", "keogh", "university of kansas"]),
        C("rosebud", "power", "Eight days earlier, Crazy Horse fought George Crook to a standstill at the Rosebud (June 17, 1876)", ["rosebud", "george crook", "crook"]),
        C("garryowen", "power", "His regiment’s marching tune was the Irish song “Garryowen”", ["garryowen"]),
        C("last-message", "power", "His last message, carried by trumpeter John Martin: “Benteen. Come on. Big village. Be quick. Bring packs.”", ["john martin", "big village", "bring packs"]),
        C("sun-dance", "power", "Sitting Bull’s Sun Dance vision showed soldiers falling into the camp", ["sun dance", "vision", "falling"]),
        C("greasy-grass", "power", "The Lakota and Cheyenne call the battle the Greasy Grass", ["greasy grass"]),
        C("monument", "power", "The battlefield monument once named for him was renamed in 1991; an Indian Memorial was added in 2003", ["renamed", "1991", "indian memorial"]),
        C("west-point-grave", "power", "Reburied at West Point in 1877; Errol Flynn played him in _They Died with Their Boots On_ (1941)", ["reburied", "errol flynn", "boots on"])
    ],
    "trap": {
        "title": "The man or the battle?",
        "body": "Many tossups ask for the Battle of the Little Bighorn instead of the man, and they share clues such as Sitting Bull, Crazy Horse, Reno, Benteen, Comanche, and the Greasy Grass. If the question says “this battle,” answering with his name is wrong. The Wounded Knee Massacre (1890) involved his old regiment, the 7th Cavalry, but happened 14 years after he died.",
        "fix": "Listen for the noun: “this man,” “this officer,” or “this commander” means Custer; “this battle” or “this fight” means the Little Bighorn. West Point, Gettysburg, the Wolverines, the Washita, and the Black Hills Expedition are clues about his career. Lakota leaders such as Sitting Bull and Crazy Horse are their own answer lines.",
        "line": "Real answer line: George Armstrong <b><u>Custer</u></b>"
    },
    "tests": {
        "right": [
            "George Armstrong Custer",
            "Custer",
            "General Custer",
            "George Custar",
            "George A. Custer"
        ],
        "prompt": [],
        "wrong": [
            "Sitting Bull",
            "Crazy Horse",
            "Tom Custer",
            "Marcus Reno",
            "Battle of the Little Bighorn",
            "George Meade"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
