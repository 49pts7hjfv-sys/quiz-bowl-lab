import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "battle-of-the-little-bighorn",
    "name": "Battle of the Little Bighorn",
    "mono": "LBH",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Lakota, Cheyenne, and Arapaho defeat Custer’s 7th Cavalry · Montana, June 1876",
    "dates": "June 25–26, 1876",
    "briefing": "On June 25, 1876, Lieutenant Colonel George Armstrong Custer led the U.S. 7th Cavalry in an attack on a huge camp of Lakota, Northern Cheyenne, and Arapaho people beside Montana’s Little Bighorn River. Warriors led by Crazy Horse, Gall, and others won a major victory, and Custer and every soldier in the five companies he led were killed. The Lakota and Cheyenne call it the Battle of the Greasy Grass; newspapers called it “Custer’s Last Stand.”",
    "answerHtml": "Battle of the <b><u>Little Bighorn</u></b> (accept Battle of the <u>Greasy Grass</u> or <u>Custer’s Last Stand</u>; prompt on <u>Great Sioux War</u>; do not accept “Wounded Knee”)",
    "accept": [
        "battle of the little bighorn",
        "battle of little bighorn",
        "little bighorn",
        "the little bighorn",
        "little big horn",
        "battle of the little big horn",
        "battle of little big horn",
        "little bighorn battle",
        "battle of the greasy grass",
        "battle of greasy grass",
        "greasy grass",
        "custers last stand"
    ],
    "prompt": [
        "great sioux war",
        "great sioux war of 1876",
        "sioux war of 1876",
        "black hills war",
        "bighorn",
        "big horn",
        "battle of bighorn",
        "battle of the bighorn",
        "battle of big horn",
        "battle of the big horn",
        "last stand"
    ],
    "reject": [
        "wounded knee",
        "wounded knee massacre",
        "battle of wounded knee",
        "rosebud",
        "battle of the rosebud",
        "battle of rosebud",
        "rosebud creek",
        "sand creek",
        "sand creek massacre",
        "washita",
        "battle of the washita",
        "battle of washita river",
        "fetterman fight",
        "fetterman massacre",
        "red clouds war",
        "slim buttes",
        "battle of slim buttes",
        "big hole",
        "battle of the big hole",
        "battle of big hole",
        "bear paw",
        "battle of bear paw",
        "george armstrong custer",
        "george custer",
        "george a custer",
        "sitting bull",
        "crazy horse",
        "marcus reno",
        "frederick benteen",
        "reno hill",
        "ghost dance",
        "battle of the alamo",
        "alamo",
        "trail of tears",
        "little big man"
    ],
    "mediaPending": True,
    "media": [],
    "wiki": "https://en.wikipedia.org/wiki/Battle_of_the_Little_Bighorn",
    "qb": {
        "q": "Little Bighorn",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In early June 1876, a Hunkpapa [“HUNK-pah-pah”] Lakota holy man took part in a Sun Dance and saw a vision of soldiers falling upside down into his people’s camp. About three weeks later, cavalry soldiers attacked that camp, beside a river in Montana, in this battle.",
            "r": "That holy man was Sitting Bull. For 10 points, name this battle in which Lakota and Cheyenne warriors defeated George Armstrong Custer."
        },
        {
            "p": "Mark Kellogg, a newspaper reporter for the _Bismarck Tribune_, was killed while riding with the soldiers in this battle. Word of this battle reached the eastern states in early July 1876, during celebrations of the nation’s 100th birthday.",
            "r": "For 10 points, name this June 1876 battle in Montana, where George Armstrong Custer and every soldier in his five companies were killed."
        },
        {
            "p": "After a grass fire swept across this battle’s site in 1983, archaeologists mapped bullets and cartridge cases left on the ground. Their work showed that many of the Native fighters here had repeating rifles, while the soldiers carried single-shot carbines.",
            "r": "For 10 points, name this 1876 battle in which Lakota, Cheyenne, and Arapaho warriors defeated George Armstrong Custer’s troops."
        },
        {
            "p": "Before this battle, one officer turned down an offer of Gatling guns because he thought they would slow his troops down. His regiment belonged to General Alfred Terry’s column, one of three Army forces sent in 1876 to force Lakota and Cheyenne bands onto reservations.",
            "r": "For 10 points, name this battle in Montana where that officer, George Armstrong Custer, was killed along with every soldier in his five companies."
        },
        {
            "p": "In 1879, Major Marcus Reno asked for a court of inquiry to answer critics who blamed him for this battle’s outcome. Reno had attacked the south end of a huge village, then retreated across the river to a hilltop.",
            "r": "Most of the soldiers with Reno and Frederick Benteen survived there. For 10 points, name this battle in which their commander, George Armstrong Custer, was killed."
        },
        {
            "p": "Bloody Knife, an Arikara [“uh-RIK-uh-ruh”] scout who was a longtime favorite of the commanding officer, was killed early in this battle during Major Marcus Reno’s attack on the village. Scouts had warned that the camp ahead was enormous.",
            "r": "For 10 points, name this 1876 battle in which warriors led by Crazy Horse and Gall defeated George Armstrong Custer."
        },
        {
            "p": "Captain Myles Keogh [“KEE-oh”] was killed with his entire company in this battle, but his badly wounded horse survived. The Army later ordered that the horse, Comanche, should never be ridden again, and it became a living symbol of this battle.",
            "r": "For 10 points, name this battle where George Armstrong Custer and his 7th Cavalry were defeated in June 1876."
        },
        {
            "p": "Captain Grant Marsh’s steamboat, the _Far West_, rushed wounded soldiers from this battle down the Yellowstone and Missouri Rivers to Bismarck in record time. Those soldiers had survived with Major Marcus Reno and Captain Frederick Benteen on a hilltop above the river.",
            "r": "For 10 points, name this 1876 battle in which George Armstrong Custer and every soldier in his five companies were killed."
        },
        {
            "p": "Two Moons led Northern Cheyenne warriors in this battle, and the Cheyenne leader Lame White Man was among the Native fighters killed in it. The warriors came from a camp of several thousand people that stretched along a river valley in Montana.",
            "r": "For 10 points, name this battle in which Lakota and Cheyenne warriors defeated George Armstrong Custer’s 7th Cavalry in June 1876."
        },
        {
            "p": "Henry Wadsworth Longfellow wrote about this battle in the poem “The Revenge of Rain-in-the-Face.” Within weeks of this battle, Walt Whitman published a poem honoring the commander who died in it, which he later retitled “From Far Dakota’s Cañons.”",
            "r": "That commander’s body was found on a ridge now called Last Stand Hill. For 10 points, name this 1876 battle where Lakota and Cheyenne warriors defeated George Armstrong Custer."
        },
        {
            "p": "In Thomas Berger’s novel _Little Big Man_, the narrator Jack Crabb claims to be the only white survivor of this battle, and Dustin Hoffman played Crabb in the 1970 film version. An earlier film, _They Died with Their Boots On_, climaxes with this battle.",
            "r": "For 10 points, name this 1876 battle in Montana where George Armstrong Custer was killed along with every soldier in his five companies."
        },
        {
            "p": "In 1991, Congress renamed the national monument at this battle’s site, which had been named for the U.S. officer killed there. In 2003, an Indian Memorial was dedicated nearby to honor the Native people who took part in this battle.",
            "r": "For 10 points, name this battle in which the Lakota leaders Sitting Bull and Crazy Horse won their most famous victory, over George Armstrong Custer."
        },
        {
            "p": "Eight days before this battle, warriors led by Crazy Horse fought General George Crook’s soldiers to a standstill at Rosebud Creek, so Crook’s column was not there to help. The camp then moved west to a river valley in Montana Territory.",
            "r": "For 10 points, name this June 1876 battle where George Armstrong Custer and every soldier in his five companies were killed."
        },
        {
            "p": "After gold was found in the Black Hills, land promised to the Lakota by the 1868 Treaty of Fort Laramie, the government ordered all Lakota bands to report to reservations by January 31, 1876. Many bands that ignored the order gathered in the huge camp attacked in this battle.",
            "r": "For 10 points, name this June 1876 battle in which Lakota and Cheyenne warriors defeated George Armstrong Custer."
        },
        {
            "p": "During this battle, trumpeter John Martin carried a hurried written message to Captain Frederick Benteen: “Come on. Big village. Be quick. Bring packs.” Benteen instead joined Major Marcus Reno’s soldiers on a hilltop, where most of them survived.",
            "r": "For 10 points, name this June 1876 battle where George Armstrong Custer and all the men with him were killed."
        }
    ],
    "clues": [
        {
            "id": "custer-killed",
            "tier": "giveaway",
            "t": "George Armstrong Custer and every soldier in the five companies he led were killed",
            "k": ["custer", "five companies", "killed"],
            "n": 0,
            "rabbit": "George Armstrong Custer"
        },
        {
            "id": "seventh-cavalry",
            "tier": "giveaway",
            "t": "Lakota, Northern Cheyenne, and Arapaho warriors defeated the U.S. 7th Cavalry",
            "k": ["7th cavalry", "lakota", "cheyenne", "arapaho"],
            "n": 0
        },
        {
            "id": "june-1876",
            "tier": "giveaway",
            "t": "Fought June 25–26, 1876, beside a river in southern Montana Territory",
            "k": ["june 25", "1876", "montana"],
            "n": 0
        },
        {
            "id": "native-leaders",
            "tier": "giveaway",
            "t": "Sitting Bull, a Hunkpapa Lakota holy man, was the camp’s most famous leader; Crazy Horse and Gall led warriors in the fighting",
            "k": ["sitting bull", "crazy horse", "gall", "hunkpapa"],
            "n": 0,
            "rabbit": "Sitting Bull"
        },
        {
            "id": "reno-benteen",
            "tier": "middle",
            "t": "Custer split his regiment: Major Marcus Reno attacked the south end of the village, and Captain Frederick Benteen scouted the hills to the south",
            "k": ["marcus reno", "reno", "benteen", "split"],
            "n": 0
        },
        {
            "id": "hilltop",
            "tier": "middle",
            "t": "Reno’s men retreated across the river to a hilltop, where Benteen joined them; most of their soldiers survived",
            "k": ["hilltop", "retreated", "survived"],
            "n": 0
        },
        {
            "id": "last-stand-hill",
            "tier": "middle",
            "t": "Custer’s body was found on a ridge now called Last Stand Hill; he was reburied at West Point in 1877",
            "k": ["last stand hill", "west point", "ridge"],
            "n": 0
        },
        {
            "id": "black-hills",
            "tier": "middle",
            "t": "Part of the Great Sioux War of 1876, which followed the discovery of gold in the Black Hills",
            "k": ["great sioux war", "black hills", "gold"],
            "n": 0,
            "rabbit": "Sioux"
        },
        {
            "id": "fort-laramie",
            "tier": "middle",
            "t": "The 1868 Treaty of Fort Laramie had promised the Black Hills to the Lakota; Custer’s 1874 expedition reported gold there",
            "k": ["fort laramie", "1868", "1874", "expedition"],
            "n": 0
        },
        {
            "id": "deadline",
            "tier": "middle",
            "t": "The government ordered all Lakota bands onto reservations by January 31, 1876; many who refused gathered in the great camp",
            "k": ["january 31", "reservations", "refused"],
            "n": 0
        },
        {
            "id": "sun-dance",
            "tier": "middle",
            "t": "Weeks earlier, Sitting Bull had a vision at a Sun Dance of soldiers falling upside down into the camp",
            "k": ["sun dance", "vision", "upside down"],
            "n": 0
        },
        {
            "id": "rosebud",
            "tier": "middle",
            "t": "Eight days earlier (June 17, 1876), Crazy Horse’s warriors fought General George Crook to a standstill at the Battle of the Rosebud",
            "k": ["rosebud", "crook", "june 17"],
            "n": 0
        },
        {
            "id": "comanche",
            "tier": "middle",
            "t": "Comanche, the horse of Captain Myles Keogh, survived; the Army ordered that he never be ridden again",
            "k": ["comanche", "keogh", "horse"],
            "n": 0
        },
        {
            "id": "monument-1991",
            "tier": "power",
            "t": "In 1991, Congress renamed the battlefield’s national monument, which had been named for Custer; an Indian Memorial was added in 2003",
            "k": ["1991", "renamed", "indian memorial", "2003"],
            "n": 0
        },
        {
            "id": "terry",
            "tier": "power",
            "t": "Custer’s regiment was part of General Alfred Terry’s column; Terry and Colonel John Gibbon reached the hilltop survivors on June 27",
            "k": ["alfred terry", "terry", "gibbon", "june 27"],
            "n": 0
        },
        {
            "id": "gatling",
            "tier": "power",
            "t": "Custer turned down an offer of Gatling guns, thinking they would slow his march",
            "k": ["gatling", "turned down"],
            "n": 0
        },
        {
            "id": "kellogg",
            "tier": "power",
            "t": "Reporter Mark Kellogg of the _Bismarck Tribune_ rode with Custer and was killed",
            "k": ["kellogg", "reporter", "bismarck tribune"],
            "n": 0
        },
        {
            "id": "centennial",
            "tier": "power",
            "t": "News of the defeat reached the eastern states in early July 1876, during the nation’s centennial (100th birthday) celebrations",
            "k": ["centennial", "100th birthday", "july 1876"],
            "n": 0
        },
        {
            "id": "far-west",
            "tier": "power",
            "t": "Captain Grant Marsh’s steamboat _Far West_ rushed the wounded to Bismarck in record time",
            "k": ["far west", "grant marsh", "steamboat"],
            "n": 0
        },
        {
            "id": "bloody-knife",
            "tier": "power",
            "t": "Custer’s favorite scout, the Arikara Bloody Knife, was killed during Reno’s attack",
            "k": ["bloody knife", "arikara", "scout"],
            "n": 0
        },
        {
            "id": "martin-message",
            "tier": "power",
            "t": "Trumpeter John Martin carried a note to Benteen: “Come on. Big village. Be quick. Bring packs.”",
            "k": ["john martin", "trumpeter", "big village", "bring packs"],
            "n": 0
        },
        {
            "id": "archaeology",
            "tier": "power",
            "t": "After a 1983 grass fire, archaeologists found that many warriors had repeating rifles; the soldiers carried single-shot carbines",
            "k": ["grass fire", "1983", "repeating rifles", "archaeologists"],
            "n": 0
        },
        {
            "id": "reno-inquiry",
            "tier": "power",
            "t": "Reno asked for an 1879 court of inquiry to answer critics who blamed him for the defeat",
            "k": ["court of inquiry", "1879"],
            "n": 0
        },
        {
            "id": "two-moons",
            "tier": "power",
            "t": "Two Moons led Northern Cheyenne warriors; the Cheyenne leader Lame White Man was killed",
            "k": ["two moons", "lame white man"],
            "n": 0
        },
        {
            "id": "poems",
            "tier": "power",
            "t": "Poems about it: Walt Whitman’s “From Far Dakota’s Cañons” and Longfellow’s “The Revenge of Rain-in-the-Face”",
            "k": ["whitman", "longfellow", "rain-in-the-face", "dakota"],
            "n": 0
        },
        {
            "id": "little-big-man",
            "tier": "power",
            "t": "Jack Crabb, narrator of Thomas Berger’s _Little Big Man_ (a 1970 film with Dustin Hoffman), claims to be its only white survivor",
            "k": ["little big man", "jack crabb", "dustin hoffman", "berger"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Battle, man, or massacre?",
        "body": "Little Bighorn questions are full of names that are answer lines of their own: George Armstrong Custer (the commander who died), Sitting Bull and Crazy Horse (Lakota leaders), and the Battle of the Rosebud (Crazy Horse’s fight with George Crook eight days earlier). The Wounded Knee Massacre (1890) involved the same 7th Cavalry regiment but happened 14 years later, in South Dakota.",
        "fix": "Listen for the noun: “this battle” wants the Little Bighorn, while “this man” or “this commander” wants Custer. Answer lines also accept the Lakota and Cheyenne name, the Battle of the Greasy Grass, and “Custer’s Last Stand.” December 1890, the Ghost Dance, and Spotted Elk (Big Foot) mean Wounded Knee.",
        "line": "Real answer line: Battle of the <b><u>Little Bighorn</u></b> (accept Battle of the <u>Greasy Grass</u> or <u>Custer’s Last Stand</u>; prompt on <u>Great Sioux War</u>; do not accept “Wounded Knee”)"
    },
    "tests": {
        "right": [
            "Battle of the Little Bighorn",
            "Little Bighorn",
            "Little Big Horn",
            "Battle of the Greasy Grass",
            "Custer's Last Stand",
            "Custer Last Stand",
            "Little Bighorne",
            "Battle of Little Bighorn"
        ],
        "prompt": [
            "Great Sioux War",
            "Bighorn"
        ],
        "wrong": [
            "Wounded Knee",
            "Battle of the Rosebud",
            "Sand Creek Massacre",
            "George Armstrong Custer",
            "Custer",
            "Sitting Bull",
            "Crazy Horse",
            "Washita",
            "Little Big Man"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", data["id"])
