import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

data = {
    "id": "frederick-douglass",
    "name": "Frederick Douglass",
    "mono": "FD",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Abolitionist who escaped slavery · Author, editor, and great orator",
    "dates": "c. 1818–1895",
    "briefing": "Frederick Douglass was born into slavery in Maryland and kept teaching himself to read after his lessons were forbidden. In 1838 he escaped by train and steamboat, disguised as a sailor, and soon became one of the most powerful speakers in America. His 1845 autobiography became a bestseller, and his Rochester newspaper, _The North Star_, demanded freedom for enslaved people and equal rights for women.",
    "answerHtml": "Frederick <b><u>Douglass</u></b> (accept Frederick Augustus Washington <u>Bailey</u>; do not accept “Stephen Douglas”)",
    "accept": [
        "frederick douglass",
        "douglass",
        "frederick douglas",
        "fred douglass",
        "frederick bailey",
        "frederick augustus washington bailey",
        "frederick augustus bailey",
        "frederick washington bailey"
    ],
    "prompt": [
        "frederick",
        "fred"
    ],
    "reject": [
        "stephen douglas",
        "stephen a douglas",
        "stephen arnold douglas",
        "douglas macarthur",
        "macarthur",
        "william lloyd garrison",
        "lloyd garrison",
        "garrison",
        "john brown",
        "harriet tubman",
        "tubman",
        "sojourner truth",
        "booker t washington",
        "booker washington",
        "w e b du bois",
        "web du bois",
        "du bois",
        "dubois",
        "nat turner",
        "dred scott",
        "crispus attucks",
        "frederick the great",
        "frederick law olmsted",
        "wendell phillips",
        "lewis douglass",
        "charles douglass",
        "anna murray douglass",
        "anna douglass",
        "anna murray",
        "helen pitts",
        "hugh auld",
        "thomas auld",
        "sophia auld",
        "edward covey",
        "covey",
        "solomon northup",
        "madison washington",
        "ida b wells"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Frederick_Douglass",
    "qb": {
        "q": "Frederick Douglass",
        "found": 0,
        "tip": TIP
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "As a boy in Baltimore, this man bought a copy of _The Columbian Orator_, a book of famous speeches, and traded bread to white boys in the street in exchange for reading lessons. Earlier, Sophia Auld had taught him the alphabet until her husband made her stop.",
            "r": "He later wrote about these lessons in his 1845 _Narrative_. For 10 points, name this abolitionist who founded the newspaper _The North Star_."
        },
        {
            "p": "In one autobiography, this man described fighting back against Edward Covey, a farmer known as a “slave breaker,” and wrote, “You have seen how a man was made a slave; you shall see how a slave was made a man.” Covey never tried to whip him again.",
            "r": "He later founded the newspaper _The North Star_. For 10 points, name this abolitionist who described that fight in his 1845 _Narrative_."
        },
        {
            "p": "In September 1838, this man escaped from Baltimore dressed as a sailor and carrying papers borrowed from a free Black seaman, traveling by train and steamboat to New York. Anna Murray, a free Black woman who had helped him plan the escape, soon joined him there, and they married.",
            "r": "For 10 points, name this man who became a famous abolitionist speaker and wrote an 1845 _Narrative_ of his life."
        },
        {
            "p": "After escaping slavery, this man settled in New Bedford, Massachusetts, where his host, Nathan Johnson, suggested a new last name taken from a character in Walter Scott’s poem _The Lady of the Lake_. He had been born with the last name Bailey.",
            "r": "He later wrote three autobiographies. For 10 points, name this abolitionist who published the antislavery newspaper _The North Star_."
        },
        {
            "p": "After this man spoke at an antislavery meeting on Nantucket in 1841, the Massachusetts Anti-Slavery Society hired him as a lecturer. He later broke with that society’s leader, William Lloyd Garrison, by arguing that the Constitution could be used to fight slavery.",
            "r": "Garrison had called the Constitution a proslavery document. For 10 points, name this former slave who founded _The North Star_ in Rochester, New York."
        },
        {
            "p": "Speaking to the Rochester Ladies’ Anti-Slavery Society on July 5, 1852, this man said that, to an enslaved person, the nation’s holiday celebration was “a sham.” He told the crowd, “You may rejoice, I must mourn.”",
            "r": "That speech asked, “What to the Slave Is the Fourth of July?” For 10 points, name this abolitionist who had escaped slavery in Maryland."
        },
        {
            "p": "This man’s newspaper used the motto “Right is of no sex, Truth is of no color.” In 1848, he spoke up for a resolution demanding women’s right to vote at the Seneca Falls Convention.",
            "r": "That newspaper, _The North Star_, was printed in Rochester, New York. For 10 points, name this abolitionist and former slave."
        },
        {
            "p": "Fearing recapture after his first autobiography made him famous, this man spent nearly two years lecturing in Britain and Ireland, where he met Daniel O’Connell. In 1846, British supporters raised money to buy his freedom legally.",
            "r": "For 10 points, name this abolitionist who wrote an 1845 _Narrative_ of his life and founded _The North Star_."
        },
        {
            "p": "In 1859, John Brown met this man at a stone quarry near Chambersburg, Pennsylvania, and asked him to join a raid on the federal arsenal at Harpers Ferry. This man refused, but after the raid he fled to Canada and then England to avoid arrest.",
            "r": "He had escaped slavery in Maryland in 1838. For 10 points, name this abolitionist who published _The North Star_."
        },
        {
            "p": "Two of this man’s sons, Lewis and Charles, joined the 54th Massachusetts Infantry Regiment after he helped recruit Black soldiers for it. In 1863, he met Abraham Lincoln at the White House to push for equal pay and fair treatment for Black troops.",
            "r": "His 1845 _Narrative_ had made him famous. For 10 points, name this abolitionist who had escaped slavery in 1838."
        },
        {
            "p": "From 1889 to 1891, this man served as the U.S. minister to Haiti, and at the 1893 World’s Columbian Exposition in Chicago he represented Haiti at its pavilion. With Ida B. Wells, he wrote a pamphlet protesting that Black Americans had been left out of that fair.",
            "r": "Decades earlier, he had escaped slavery in Maryland. For 10 points, name this famous abolitionist, who wrote an 1845 _Narrative_ of his life."
        },
        {
            "p": "This man’s only work of fiction, _The Heroic Slave_, tells the story of Madison Washington, who led a revolt of enslaved people aboard the ship _Creole_ in 1841. This man also wrote three autobiographies, including _My Bondage and My Freedom_.",
            "r": "He had escaped slavery by disguising himself as a sailor. For 10 points, name this abolitionist who published the newspaper _The North Star_."
        },
        {
            "p": "Rutherford B. Hayes appointed this man U.S. Marshal for the District of Columbia in 1877. This man spent his last years at Cedar Hill, his home in Washington’s Anacostia neighborhood, where he died in 1895, hours after attending a women’s rights meeting.",
            "r": "He had founded _The North Star_ decades earlier. For 10 points, name this abolitionist who had escaped slavery in Maryland."
        },
        {
            "p": "In 1872, without asking him, the Equal Rights Party nominated this man for vice president on a ticket with Victoria Woodhull. Years earlier, he had declared, “If there is no struggle, there is no progress.”",
            "r": "For 10 points, name this abolitionist and newspaper editor who wrote an 1845 _Narrative_ of his life."
        },
        {
            "p": "In 1876, this man gave the main speech when the Emancipation Memorial, a statue of Abraham Lincoln paid for by formerly enslaved people, was unveiled in Washington, D.C. Two years earlier, he had briefly led the Freedman’s Savings Bank just before it collapsed.",
            "r": "For 10 points, name this abolitionist whose famous speeches included “What to the Slave Is the Fourth of July?”"
        }
    ],
    "clues": [
        {
            "id": "abolitionist",
            "tier": "giveaway",
            "t": "Abolitionist who escaped slavery in Maryland and became one of America’s most famous speakers and writers",
            "k": ["abolitionist", "escaped slavery", "maryland"],
            "n": 0
        },
        {
            "id": "narrative",
            "tier": "giveaway",
            "t": "Wrote a best-selling 1845 _Narrative_ of his life, “Written by Himself”",
            "k": ["written by himself", "narrative", "1845"],
            "n": 0
        },
        {
            "id": "north-star",
            "tier": "giveaway",
            "t": "Founded the antislavery newspaper _The North Star_ in Rochester, New York (1847)",
            "k": ["north star", "rochester", "newspaper"],
            "n": 0
        },
        {
            "id": "fourth-of-july",
            "tier": "giveaway",
            "t": "Gave the 1852 speech “What to the Slave Is the Fourth of July?”",
            "k": ["fourth of july", "1852"],
            "n": 0
        },
        {
            "id": "sailor",
            "tier": "middle",
            "t": "Escaped from Baltimore in 1838 disguised as a sailor, using a free Black seaman’s papers",
            "k": ["sailor", "1838", "baltimore"],
            "n": 0
        },
        {
            "id": "auld",
            "tier": "middle",
            "t": "Sophia Auld taught him the alphabet in Baltimore until her husband, Hugh, forbade it",
            "k": ["sophia auld", "auld", "alphabet"],
            "n": 0
        },
        {
            "id": "covey",
            "tier": "middle",
            "t": "Fought back against the “slave breaker” Edward Covey: “You have seen how a man was made a slave; you shall see how a slave was made a man”",
            "k": ["edward covey", "covey", "slave breaker"],
            "n": 0
        },
        {
            "id": "garrison",
            "tier": "middle",
            "t": "William Lloyd Garrison’s antislavery society hired him after he spoke at Nantucket (1841); they later split over the Constitution",
            "k": ["garrison", "nantucket", "1841"],
            "n": 0,
            "rabbit": "William Lloyd Garrison"
        },
        {
            "id": "seneca-falls",
            "tier": "middle",
            "t": "Spoke for women’s right to vote at the Seneca Falls Convention (1848); his paper’s motto was “Right is of no sex”",
            "k": ["seneca falls", "right is of no sex", "1848"],
            "n": 0,
            "rabbit": "Seneca Falls Convention"
        },
        {
            "id": "fifty-fourth",
            "tier": "middle",
            "t": "Recruited Black soldiers for the 54th Massachusetts Regiment; his sons Lewis and Charles joined it",
            "k": ["54th massachusetts", "recruited", "lewis"],
            "n": 0
        },
        {
            "id": "lincoln",
            "tier": "middle",
            "t": "Met Abraham Lincoln at the White House (1863) to push for equal pay and treatment for Black soldiers",
            "k": ["lincoln", "white house", "equal pay"],
            "n": 0
        },
        {
            "id": "anna-murray",
            "tier": "middle",
            "t": "Anna Murray, a free Black woman in Baltimore, helped plan his escape; they married in New York (1838)",
            "k": ["anna murray", "married"],
            "n": 0
        },
        {
            "id": "haiti",
            "tier": "middle",
            "t": "U.S. minister to Haiti (1889–1891)",
            "k": ["haiti", "minister"],
            "n": 0
        },
        {
            "id": "name-change",
            "tier": "power",
            "t": "Born with the last name Bailey; in New Bedford, Nathan Johnson suggested his new name from Walter Scott’s _The Lady of the Lake_",
            "k": ["lady of the lake", "new bedford", "nathan johnson", "bailey"],
            "n": 0
        },
        {
            "id": "columbian-orator",
            "tier": "power",
            "t": "As a boy he bought _The Columbian Orator_, a book of speeches, and traded bread for reading lessons",
            "k": ["columbian orator", "bread"],
            "n": 0
        },
        {
            "id": "ireland",
            "tier": "power",
            "t": "Lectured in Britain and Ireland (1845–1847) and met Daniel O’Connell; British friends bought his freedom (1846)",
            "k": ["daniel o’connell", "ireland", "1846"],
            "n": 0
        },
        {
            "id": "heroic-slave",
            "tier": "power",
            "t": "His only fiction, _The Heroic Slave_, is about Madison Washington, who led the 1841 revolt on the ship _Creole_",
            "k": ["heroic slave", "madison washington", "creole"],
            "n": 0
        },
        {
            "id": "john-brown",
            "tier": "power",
            "t": "Refused to join John Brown’s raid on Harpers Ferry after meeting him at a quarry near Chambersburg (1859)",
            "k": ["john brown", "harpers ferry", "chambersburg"],
            "n": 0,
            "rabbit": "John Brown"
        },
        {
            "id": "autobiographies",
            "tier": "power",
            "t": "Later autobiographies: _My Bondage and My Freedom_ (1855) and _Life and Times_ (1881)",
            "k": ["my bondage and my freedom", "bondage", "life and times"],
            "n": 0
        },
        {
            "id": "cedar-hill",
            "tier": "power",
            "t": "U.S. Marshal for D.C. (1877, under Hayes); lived at Cedar Hill in Anacostia, where he died in 1895",
            "k": ["cedar hill", "anacostia", "marshal"],
            "n": 0
        },
        {
            "id": "woodhull",
            "tier": "power",
            "t": "Nominated without his consent for vice president on Victoria Woodhull’s Equal Rights Party ticket (1872)",
            "k": ["victoria woodhull", "woodhull", "equal rights party"],
            "n": 0
        },
        {
            "id": "struggle",
            "tier": "power",
            "t": "“If there is no struggle, there is no progress” (1857 speech)",
            "k": ["no struggle", "no progress", "1857"],
            "n": 0
        },
        {
            "id": "columbian-exposition",
            "tier": "power",
            "t": "With Ida B. Wells, protested the exclusion of Black Americans from the 1893 World’s Columbian Exposition in Chicago",
            "k": ["columbian exposition", "wells", "1893"],
            "n": 0
        },
        {
            "id": "emancipation-memorial",
            "tier": "power",
            "t": "Gave the main speech at the unveiling of the Emancipation Memorial to Lincoln (1876); briefly led the Freedman’s Savings Bank (1874)",
            "k": ["emancipation memorial", "freedman’s savings bank", "1876"],
            "n": 0
        },
        {
            "id": "tubman-letter",
            "tier": "power",
            "t": "Wrote to Harriet Tubman (1868) that “the midnight sky and the silent stars” had witnessed her heroism",
            "k": ["harriet tubman", "midnight sky", "silent stars"],
            "n": 0,
            "rabbit": "Harriet Tubman"
        }
    ],
    "trap": {
        "title": "Douglass, not Douglas",
        "body": "Two famous figures of the 1850s share almost the same name. Frederick Douglass (two s’s) was the abolitionist editor, while Stephen A. Douglas (one s) was the Illinois senator who debated Abraham Lincoln and wrote the Kansas-Nebraska Act. Players also buzz too early with other abolitionists: William Lloyd Garrison published _The Liberator_, and Harriet Tubman led people north on the Underground Railroad.",
        "fix": "_The North Star_, the 1845 _Narrative_, the sailor disguise, Edward Covey, and “What to the Slave Is the Fourth of July?” mean Frederick Douglass. The Lincoln-Douglas debates, popular sovereignty, and the “Little Giant” mean Stephen Douglas. Say “Frederick Douglass” in full if you have any doubt.",
        "line": "Real answer line: Frederick <b><u>Douglass</u></b> (accept Frederick Augustus Washington <u>Bailey</u>; do not accept “Stephen Douglas”)"
    },
    "tests": {
        "right": [
            "Frederick Douglass",
            "Douglass",
            "Frederick Douglas",
            "Fredrick Douglass",
            "Frederick Bailey"
        ],
        "prompt": [
            "Frederick"
        ],
        "wrong": [
            "Stephen Douglas",
            "William Lloyd Garrison",
            "Harriet Tubman",
            "Booker T. Washington",
            "Sojourner Truth",
            "John Brown",
            "Frederick the Great"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
