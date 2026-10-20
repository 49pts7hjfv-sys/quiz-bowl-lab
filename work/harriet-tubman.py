import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "harriet-tubman",
    "name": "Harriet Tubman",
    "mono": "HT",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Underground Railroad conductor · Union scout and spy in the Civil War",
    "dates": "c. 1822–1913",
    "briefing": "Born into slavery in Maryland around 1822, Harriet Tubman escaped to Philadelphia in 1849, then went back again and again to lead family members and others to freedom on the Underground Railroad. People called her “Moses.” During the Civil War she worked as a Union scout, nurse, and spy, and she helped guide the Combahee River Raid, which freed more than 700 enslaved people in South Carolina.",
    "answerHtml": "Harriet <b><u>Tubman</u></b> (accept Araminta Ross)",
    "accept": [
        "harriet tubman",
        "tubman",
        "araminta ross",
        "minty ross"
    ],
    "prompt": [],
    "reject": [
        "harriet beecher stowe",
        "beecher stowe",
        "stowe",
        "harriet jacobs",
        "sojourner truth",
        "frederick douglass",
        "john tubman",
        "underground railroad",
        "william still",
        "thomas garrett",
        "john brown",
        "nelson davis"
    ],
    "mediaPending": True,
    "media": [],
    "wiki": "https://en.wikipedia.org/wiki/Harriet_Tubman",
    "qb": {
        "q": "Harriet Tubman",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In June 1863, this woman helped guide Colonel James Montgomery’s Black Union soldiers up the Combahee [“KUM-bee”] River in South Carolina, after her scouts found where Confederates had placed underwater mines. Union gunboats in that raid carried more than 700 enslaved people to freedom.",
            "r": "She had worked for the Union Army as a scout, nurse, and spy. For 10 points, name this Underground Railroad conductor nicknamed “Moses.”"
        },
        {
            "p": "As a teenager, this woman was badly hurt when an overseer threw a heavy metal weight that struck her head, and for the rest of her life she had sudden sleeping spells and vivid dreams she believed came from God. She was born with the first name Araminta on Maryland’s Eastern Shore.",
            "r": "For 10 points, name this woman who escaped slavery in 1849 and then led others north on the Underground Railroad."
        },
        {
            "p": "The Quaker stationmaster Thomas Garrett often sheltered this woman and the freedom seekers she guided in Wilmington, Delaware, and William Still recorded their arrivals in Philadelphia. After the Fugitive Slave Act of 1850, this woman began leading groups all the way to St. Catharines in Canada.",
            "r": "She had escaped from slavery in Maryland in 1849. For 10 points, name this Underground Railroad conductor nicknamed “Moses.”"
        },
        {
            "p": "John Brown called this woman “General” and asked her to help recruit fighters for his 1859 raid on Harpers Ferry, though she did not take part in the attack. Brown met her in Canada, where she had settled after leading many freedom seekers there.",
            "r": "For 10 points, name this woman who escaped slavery in Maryland and became a famous conductor on the Underground Railroad."
        },
        {
            "p": "Senator William Seward sold this woman land in Auburn, New York, where she later opened a home for elderly African Americans. She was buried in Auburn with military honors in 1913, after spending decades asking the government for a pension for her own Civil War service.",
            "r": "Abolitionists called her “Moses.” For 10 points, name this woman who led enslaved people to freedom on the Underground Railroad."
        },
        {
            "p": "This woman once boasted, “I never ran my train off the track and I never lost a passenger.” She made about thirteen trips back to Maryland and led about seventy people to freedom, including her parents and several of her brothers.",
            "r": "She had escaped from slavery herself in 1849. For 10 points, name this most famous conductor on the Underground Railroad."
        },
        {
            "p": "Cynthia Erivo earned an Oscar nomination for playing this woman in a 2019 film. National historical parks honoring this woman were created in the 2010s on Maryland’s Eastern Shore, where she was born, and in Auburn, New York, where she died.",
            "r": "In 2016, the Treasury announced plans to put her on the front of the $20 bill, replacing Andrew Jackson. For 10 points, name this Underground Railroad conductor."
        },
        {
            "p": "During the Civil War, this woman worked in Beaufort [“BYOO-fert”], South Carolina, where she nursed sick soldiers and freedpeople and led a network of scouts who gathered information behind Confederate lines. Because she was rarely paid, she supported herself by selling pies and root beer that she made.",
            "r": "In 1863, she helped lead a raid up the Combahee River. For 10 points, name this former Underground Railroad conductor."
        },
        {
            "p": "This woman’s first husband, John, was a free Black man who stayed behind when she escaped, and when she returned for him in 1851, he had married another woman. After the Civil War, she married a younger Union veteran named Nelson Davis in Auburn, New York.",
            "r": "She had escaped slavery in Maryland in 1849. For 10 points, name this woman known as the “Moses” of her people."
        },
        {
            "p": "In 1857, this woman rescued her elderly parents, Ben and Rit, from Maryland after her father came under suspicion for helping freedom seekers. Over the Christmas holiday in 1854, she had led three of her brothers to freedom.",
            "r": "For 10 points, name this woman who escaped slavery in 1849 and became the Underground Railroad’s most famous conductor."
        },
        {
            "p": "In 1860, this woman helped a crowd in Troy, New York, free Charles Nalle, a man who had escaped slavery and was about to be sent back south under the Fugitive Slave Act. She had led many freedom seekers through New York to Canada.",
            "r": "Earlier, she had escaped from Maryland. For 10 points, name this conductor on the Underground Railroad, who was known as “Moses.”"
        },
        {
            "p": "When her enslaver, Edward Brodess, died in 1849, this woman feared she would be sold away from her family. Around the time she married in 1844, she had begun using her mother’s first name instead of the name Araminta.",
            "r": "Soon after Brodess died, she escaped to Philadelphia. For 10 points, name this woman who became the most famous conductor on the Underground Railroad."
        },
        {
            "p": "In an 1868 letter, Frederick Douglass told this woman that “the midnight sky and the silent stars” had been the witnesses of her devotion to freedom and her heroism. Douglass contrasted her secret, dangerous work at night with his own public work by day.",
            "r": "For 10 points, name this woman who escaped slavery and became famous as a conductor on the Underground Railroad."
        },
        {
            "p": "Sarah Bradford wrote two biographies of this woman, in 1869 and 1886, to raise money for her. In her later years, this woman traveled to Boston, New York, and Washington, D.C., to speak in favor of women’s right to vote.",
            "r": "Bradford’s second book called her “the Moses of her people.” For 10 points, name this Underground Railroad conductor."
        },
        {
            "p": "Between rescue missions, this woman worked as a cook and maid in Philadelphia and in hotels in Cape May, New Jersey, to save money for her trips back to Maryland. She guided her groups mostly at night, often following the North Star.",
            "r": "For 10 points, name this woman who led about seventy people out of slavery on the Underground Railroad."
        }
    ],
    "clues": [
        {
            "id": "underground-railroad",
            "tier": "giveaway",
            "t": "The most famous “conductor” on the Underground Railroad, guiding enslaved people north to freedom",
            "k": ["underground railroad", "conductor"],
            "n": 0,
            "rabbit": "Underground Railroad"
        },
        {
            "id": "moses",
            "tier": "giveaway",
            "t": "Nicknamed “Moses” for leading her people out of slavery",
            "k": ["moses"],
            "n": 0
        },
        {
            "id": "escaped-1849",
            "tier": "giveaway",
            "t": "Escaped from slavery in Maryland in 1849, reaching Philadelphia",
            "k": ["1849", "maryland", "philadelphia"],
            "n": 0
        },
        {
            "id": "civil-war",
            "tier": "giveaway",
            "t": "Served the Union Army as a scout, nurse, and spy during the Civil War",
            "k": ["scout", "spy", "nurse", "civil war"],
            "n": 0
        },
        {
            "id": "twenty",
            "tier": "giveaway",
            "t": "In 2016, the Treasury announced plans to put her on the front of the $20 bill, replacing Andrew Jackson",
            "k": ["$20 bill", "treasury", "andrew jackson"],
            "n": 0
        },
        {
            "id": "combahee",
            "tier": "middle",
            "t": "Combahee River Raid (June 1863): helped guide Union soldiers who freed more than 700 enslaved people in South Carolina",
            "k": ["combahee", "700", "south carolina"],
            "n": 0
        },
        {
            "id": "never-lost",
            "tier": "middle",
            "t": "Made about 13 trips and led about 70 people to freedom; said she “never lost a passenger”",
            "k": ["never lost a passenger", "13 trips", "70 people"],
            "n": 0
        },
        {
            "id": "araminta",
            "tier": "middle",
            "t": "Born with the name Araminta (“Minty”) around 1822 in Dorchester County, Maryland; later took her mother’s first name",
            "k": ["araminta", "minty", "dorchester county", "mother’s first name"],
            "n": 0
        },
        {
            "id": "john-brown",
            "tier": "middle",
            "t": "John Brown called her “General” and sought her help recruiting for his raid on Harpers Ferry (1859)",
            "k": ["john brown", "general", "harpers ferry"],
            "n": 0,
            "rabbit": "John Brown"
        },
        {
            "id": "auburn",
            "tier": "middle",
            "t": "Bought land in Auburn, New York, from William Seward; opened a home for elderly African Americans; died there in 1913",
            "k": ["auburn", "seward", "1913"],
            "n": 0
        },
        {
            "id": "canada",
            "tier": "middle",
            "t": "After the Fugitive Slave Act of 1850, led freedom seekers all the way to St. Catharines, Canada",
            "k": ["fugitive slave act", "st. catharines", "canada"],
            "n": 0
        },
        {
            "id": "head-injury",
            "tier": "middle",
            "t": "As a teen, a heavy weight thrown by an overseer struck her head, causing lifelong sleeping spells and visions",
            "k": ["overseer", "sleeping spells", "visions", "head"],
            "n": 0
        },
        {
            "id": "suffrage",
            "tier": "middle",
            "t": "In her later years, spoke in favor of women’s suffrage in Boston, New York, and Washington, D.C.",
            "k": ["suffrage", "boston", "washington"],
            "n": 0,
            "rabbit": "Women’s Suffrage"
        },
        {
            "id": "garrett-still",
            "tier": "power",
            "t": "Sheltered by Quaker stationmaster Thomas Garrett in Wilmington, Delaware; William Still recorded her arrivals in Philadelphia",
            "k": ["thomas garrett", "garrett", "william still", "wilmington"],
            "n": 0
        },
        {
            "id": "montgomery",
            "tier": "power",
            "t": "Guided Colonel James Montgomery’s Black soldiers on the Combahee raid; her scouts found the Confederates’ river mines",
            "k": ["james montgomery", "montgomery", "mines"],
            "n": 0
        },
        {
            "id": "beaufort",
            "tier": "power",
            "t": "Worked in Beaufort, South Carolina, nursing soldiers and leading scouts; sold pies and root beer to support herself",
            "k": ["beaufort", "scouts", "root beer"],
            "n": 0
        },
        {
            "id": "brodess",
            "tier": "power",
            "t": "Escaped after her enslaver, Edward Brodess, died in 1849 and she feared being sold",
            "k": ["edward brodess", "brodess", "sold"],
            "n": 0
        },
        {
            "id": "husbands",
            "tier": "power",
            "t": "Her first husband, John, a free Black man, had remarried when she came back for him (1851); she later married veteran Nelson Davis (1869)",
            "k": ["nelson davis", "free black man", "1851"],
            "n": 0
        },
        {
            "id": "family-rescues",
            "tier": "power",
            "t": "Led three brothers to freedom at Christmas 1854; rescued her elderly parents, Ben and Rit, in 1857",
            "k": ["parents", "brothers", "christmas", "1857"],
            "n": 0
        },
        {
            "id": "nalle",
            "tier": "power",
            "t": "Helped a crowd free Charles Nalle from federal custody in Troy, New York (1860)",
            "k": ["charles nalle", "nalle", "troy"],
            "n": 0
        },
        {
            "id": "bradford",
            "tier": "power",
            "t": "Sarah Bradford’s biographies (1869, 1886) raised money for her; the second called her “the Moses of her people”",
            "k": ["sarah bradford", "bradford", "biographies"],
            "n": 0
        },
        {
            "id": "douglass-letter",
            "tier": "power",
            "t": "Frederick Douglass wrote that “the midnight sky and the silent stars” had witnessed her heroism (1868)",
            "k": ["frederick douglass", "midnight sky", "silent stars"],
            "n": 0,
            "rabbit": "Frederick Douglass"
        },
        {
            "id": "erivo",
            "tier": "power",
            "t": "Played by Cynthia Erivo in a 2019 film; national historical parks honor her in Maryland and in Auburn, New York",
            "k": ["cynthia erivo", "erivo", "national historical parks"],
            "n": 0
        },
        {
            "id": "pension",
            "tier": "power",
            "t": "Asked the government for decades for a pension for her own war service; buried with military honors",
            "k": ["pension", "military honors"],
            "n": 0
        },
        {
            "id": "cape-may",
            "tier": "power",
            "t": "Worked as a cook and maid in Philadelphia and Cape May, New Jersey, to pay for her rescue trips",
            "k": ["cape may", "cook", "new jersey"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Tubman, Truth, or Stowe?",
        "body": "Three famous antislavery women get mixed up. Harriet Tubman escaped slavery and led others to freedom on the Underground Railroad. Sojourner Truth, born Isabella Baumfree in New York, was a speaker famous for her “Ain’t I a Woman?” speech. Harriet Beecher Stowe was a white author who wrote _Uncle Tom’s Cabin_. Players who hear “Harriet” and an antislavery clue sometimes blurt out the wrong one.",
        "fix": "Tubman clues: born Araminta in Maryland, “Moses,” the Combahee River Raid, John Brown’s “General,” Auburn, New York, and the $20 bill plan. Truth clues: her speech in Akron, Ohio, and her New York childhood. Stowe clues: _Uncle Tom’s Cabin_ and Little Eva. Saying just “Tubman” is enough.",
        "line": "Real answer line: Harriet <b><u>Tubman</u></b> (accept Araminta Ross)"
    },
    "tests": {
        "right": [
            "Harriet Tubman",
            "Tubman",
            "Araminta Ross",
            "Harriet Tubmen",
            "harriett tubman"
        ],
        "prompt": [],
        "wrong": [
            "Harriet Beecher Stowe",
            "Sojourner Truth",
            "Harriet Jacobs",
            "Frederick Douglass",
            "John Tubman",
            "Underground Railroad"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
