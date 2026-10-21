import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "william-mckinley",
    "name": "William McKinley",
    "mono": "WMK",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "25th U.S. President · Led the nation in the Spanish-American War; shot in 1901",
    "dates": "1843–1901",
    "briefing": "William McKinley was the last Civil War veteran to become president; at Antietam, the teenage sergeant carried hot coffee and food to soldiers under fire. As the 25th president, he won the 1896 election by campaigning from his front porch in Canton, Ohio, led the country through the Spanish-American War, and annexed Hawaii. In September 1901, the anarchist Leon Czolgosz shot him at the Pan-American Exposition in Buffalo, New York, and Theodore Roosevelt became president.",
    "answerHtml": "William <b><u>McKinley</u></b>",
    "accept": [
        "william mckinley",
        "mckinley",
        "president mckinley",
        "president william mckinley",
        "william mckinley jr",
        "mc kinley",
        "william mc kinley"
    ],
    "prompt": [
        "william"
    ],
    "reject": [
        "theodore roosevelt",
        "teddy roosevelt",
        "roosevelt",
        "william jennings bryan",
        "bryan",
        "mark hanna",
        "marcus hanna",
        "hanna",
        "garret hobart",
        "hobart",
        "leon czolgosz",
        "czolgosz",
        "mount mckinley",
        "mt mckinley",
        "denali",
        "mckinley tariff",
        "ida mckinley",
        "ida saxton",
        "rutherford b hayes",
        "rutherford hayes",
        "hayes",
        "benjamin harrison",
        "william henry harrison",
        "harrison",
        "grover cleveland",
        "cleveland",
        "william howard taft",
        "taft",
        "james garfield",
        "garfield",
        "john hay",
        "chester arthur",
        "spanish american war"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/William_McKinley",
    "qb": {
        "q": "William McKinley",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "During the Battle of Antietam, this teenage commissary sergeant drove a wagon of hot coffee and food to Ohio soldiers under fire, and a monument on the battlefield honors him. His regiment had been led for a time by another future president, Rutherford B. Hayes.",
            "r": "He later became the last Civil War veteran elected president. For 10 points, name this president who led the nation in the Spanish-American War."
        },
        {
            "p": "As chairman of the House Ways and Means Committee, this congressman wrote an 1890 law that sharply raised tariffs on imported goods, and he lost his House seat in elections later that year. He then served two terms as governor of Ohio.",
            "r": "For 10 points, name this Republican who won the presidency in 1896 by defeating William Jennings Bryan."
        },
        {
            "p": "While his opponent traveled about 18,000 miles by train giving speeches in favor of “free silver,” this candidate stayed home in Canton, Ohio. Trains brought hundreds of thousands of visitors to hear him speak from his front porch.",
            "r": "For 10 points, name this Republican who defeated William Jennings Bryan in the 1896 presidential election."
        },
        {
            "p": "The Cleveland industrialist Mark Hanna managed this man’s first presidential campaign, which defended the gold standard and raised huge sums from big businesses. Four years later, this man ran for reelection on the slogan “four more years of the full dinner pail.”",
            "r": "For 10 points, name this Republican president who defeated William Jennings Bryan in 1896 and 1900."
        },
        {
            "p": "Soon after taking office, this president called Congress into a special session that passed the Dingley Tariff, raising taxes on imports. In 1900, he signed the Gold Standard Act, which made gold the only standard for redeeming paper money.",
            "r": "For 10 points, name this Republican president who had defeated the free-silver champion William Jennings Bryan."
        },
        {
            "p": "The Spanish diplomat Enrique Dupuy de Lôme [“doo-PWEE duh LOHM”] resigned after a New York newspaper printed his stolen letter calling this president “weak.” Days later, the USS _Maine_ exploded in Havana Harbor.",
            "r": "In April 1898, this president asked Congress to declare war on Spain. For 10 points, name this president during the Spanish-American War."
        },
        {
            "p": "Mark Twain and Andrew Carnegie joined the Anti-Imperialist League to oppose this president’s decision to keep the Philippines. In 1899, the Senate approved his peace treaty with Spain by just one vote more than it needed.",
            "r": "That treaty gave the U.S. Puerto Rico, Guam, and the Philippines. For 10 points, name this president during the Spanish-American War."
        },
        {
            "p": "Five years after American businessmen and planters overthrew Queen Liliuokalani [“lih-lee-oo-oh-kuh-LAH-nee”], this president signed the Newlands Resolution, annexing the islands she had ruled. Grover Cleveland had withdrawn an earlier treaty to take over those islands.",
            "r": "For 10 points, name this president who annexed Hawaii in 1898, the same year he led the nation into war with Spain."
        },
        {
            "p": "On September 6, 1901, this president was greeting a line of visitors in the Temple of Music at the Pan-American Exposition in Buffalo, New York, when an anarchist shot him. He died eight days later.",
            "r": "The shooter was Leon Czolgosz [“CHOLE-gosh”], and Theodore Roosevelt became president. For 10 points, name this 25th president."
        },
        {
            "p": "The day before he was shot, this president told a huge crowd at a world’s fair that the United States could no longer stay isolated and should sign trade agreements with other nations. After his death, the Secret Service began protecting presidents full-time.",
            "r": "For 10 points, name this president who was assassinated in Buffalo, New York, in 1901."
        },
        {
            "p": "Ohio made the scarlet carnation its state flower in memory of this man, who often wore a red carnation for good luck. In the 1890s, a gold prospector named North America’s tallest peak after him.",
            "r": "That peak was renamed Denali in 2015, but a 2025 executive order restored his name to it for federal use. For 10 points, name this 25th president."
        },
        {
            "p": "This president’s first vice president, Garret Hobart, died in office in 1899. For the next election, the Republicans gave this president a new running mate: the governor of New York, who had become famous leading the Rough Riders in Cuba.",
            "r": "For 10 points, name this president whose second vice president, Theodore Roosevelt, succeeded him in 1901."
        },
        {
            "p": "This president’s secretary of state, John Hay, sent the Open Door Notes asking other powers to give all nations equal trading rights in China. In 1900, this president sent American troops to help end the Boxer Rebellion’s siege of foreign diplomats in Beijing.",
            "r": "For 10 points, name this president who led the nation in the Spanish-American War."
        },
        {
            "p": "This president’s portrait appeared on the $500 bill, and he is buried with his wife, Ida, and their two daughters, who died young, in a domed memorial in Canton, Ohio. He was born in Niles, Ohio, in 1843.",
            "r": "He was assassinated in 1901. For 10 points, name this Republican, the 25th president of the United States."
        },
        {
            "p": "In December 1898, this president issued a proclamation of “benevolent assimilation” for the Philippines. Weeks later, fighting broke out between American troops and Filipino forces led by Emilio Aguinaldo [“ah-ghee-NAHL-doh”], who wanted independence.",
            "r": "That conflict became the Philippine-American War. For 10 points, name this president who also annexed Hawaii and won the Spanish-American War."
        }
    ],
    "clues": [
        {
            "id": "twenty-fifth",
            "tier": "giveaway",
            "t": "25th President (1897–1901), a Republican from Ohio",
            "k": ["25th president", "ohio", "republican"],
            "n": 0
        },
        {
            "id": "assassinated",
            "tier": "giveaway",
            "t": "Shot by the anarchist Leon Czolgosz at the Pan-American Exposition in Buffalo, New York (September 1901)",
            "k": ["leon czolgosz", "czolgosz", "pan-american exposition", "buffalo"],
            "n": 0
        },
        {
            "id": "spanish-american-war",
            "tier": "giveaway",
            "t": "President during the Spanish-American War (1898)",
            "k": ["spanish-american war", "1898"],
            "n": 0,
            "rabbit": "Spanish-American War"
        },
        {
            "id": "bryan",
            "tier": "giveaway",
            "t": "Defeated William Jennings Bryan in 1896 and again in 1900",
            "k": ["william jennings bryan", "bryan", "1896", "1900"],
            "n": 0,
            "rabbit": "William Jennings Bryan"
        },
        {
            "id": "roosevelt",
            "tier": "giveaway",
            "t": "His vice president, Theodore Roosevelt, took over when he died in 1901",
            "k": ["theodore roosevelt", "roosevelt", "vice president"],
            "n": 0,
            "rabbit": "Theodore Roosevelt"
        },
        {
            "id": "front-porch",
            "tier": "middle",
            "t": "Ran a “front porch” campaign from his home in Canton, Ohio (1896), while Bryan toured by train",
            "k": ["front porch", "canton"],
            "n": 0
        },
        {
            "id": "hanna",
            "tier": "middle",
            "t": "Cleveland industrialist Mark Hanna ran his 1896 campaign, which defended the gold standard and raised huge sums",
            "k": ["mark hanna", "hanna", "gold standard"],
            "n": 0
        },
        {
            "id": "tariff",
            "tier": "middle",
            "t": "As chairman of the House Ways and Means Committee, wrote the tariff of 1890 named for him, which sharply raised taxes on imports",
            "k": ["tariff", "ways and means", "1890"],
            "n": 0
        },
        {
            "id": "gold-standard-act",
            "tier": "middle",
            "t": "Signed the Gold Standard Act (1900), making gold the only standard for redeeming paper money",
            "k": ["gold standard act", "paper money"],
            "n": 0
        },
        {
            "id": "hawaii",
            "tier": "middle",
            "t": "Annexed Hawaii with the Newlands Resolution (1898)",
            "k": ["hawaii", "newlands resolution", "newlands"],
            "n": 0
        },
        {
            "id": "maine",
            "tier": "middle",
            "t": "Asked Congress to declare war on Spain in April 1898, after the USS _Maine_ exploded in Havana Harbor",
            "k": ["maine", "havana", "april 1898"],
            "n": 0
        },
        {
            "id": "treaty-of-paris",
            "tier": "middle",
            "t": "The Treaty of Paris (1898) gave the U.S. Puerto Rico, Guam, and the Philippines",
            "k": ["treaty of paris", "philippines", "puerto rico", "guam"],
            "n": 0
        },
        {
            "id": "antietam",
            "tier": "middle",
            "t": "Last Civil War veteran to be president; at Antietam, as a teenage commissary sergeant, he brought coffee and food to soldiers under fire",
            "k": ["antietam", "coffee", "commissary sergeant"],
            "n": 0,
            "rabbit": "Battle of Antietam"
        },
        {
            "id": "mountain",
            "tier": "middle",
            "t": "North America’s tallest peak was named for him in the 1890s; it was renamed Denali in 2015, and a 2025 order restored his name for federal use",
            "k": ["denali", "tallest peak", "2015", "2025"],
            "n": 0,
            "rabbit": "Denali"
        },
        {
            "id": "temple-of-music",
            "tier": "power",
            "t": "Shot on September 6, 1901, while greeting visitors in the Temple of Music; died eight days later",
            "k": ["temple of music", "eight days", "september 6"],
            "n": 0
        },
        {
            "id": "secret-service",
            "tier": "power",
            "t": "After his death, the Secret Service began protecting presidents full-time",
            "k": ["secret service", "full-time"],
            "n": 0
        },
        {
            "id": "last-speech",
            "tier": "power",
            "t": "In his last speech, at the Buffalo fair the day before he was shot, said the U.S. could no longer stay isolated and urged trade agreements",
            "k": ["last speech", "isolated", "trade agreements"],
            "n": 0
        },
        {
            "id": "hayes",
            "tier": "power",
            "t": "Served in the 23rd Ohio regiment, once led by Rutherford B. Hayes; ended the war as a major",
            "k": ["rutherford b. hayes", "hayes", "23rd ohio", "major"],
            "n": 0
        },
        {
            "id": "governor",
            "tier": "power",
            "t": "Lost his House seat in 1890, then served two terms as governor of Ohio (1892–1896)",
            "k": ["governor of ohio", "governor", "two terms"],
            "n": 0
        },
        {
            "id": "dingley",
            "tier": "power",
            "t": "Called Congress into a special session that passed the Dingley Tariff (1897)",
            "k": ["dingley", "special session"],
            "n": 0
        },
        {
            "id": "de-lome",
            "tier": "power",
            "t": "Spanish diplomat Enrique Dupuy de Lôme’s stolen letter called him “weak” (February 1898)",
            "k": ["de lôme", "dupuy", "weak"],
            "n": 0
        },
        {
            "id": "hobart",
            "tier": "power",
            "t": "His first vice president, Garret Hobart, died in office (1899); Theodore Roosevelt joined the 1900 ticket",
            "k": ["garret hobart", "hobart", "1899"],
            "n": 0
        },
        {
            "id": "dinner-pail",
            "tier": "power",
            "t": "1900 reelection slogan: “Four more years of the full dinner pail”",
            "k": ["full dinner pail", "dinner pail"],
            "n": 0
        },
        {
            "id": "open-door",
            "tier": "power",
            "t": "Secretary of State John Hay sent the Open Door Notes about trade in China; U.S. troops helped end the Boxer Rebellion (1900)",
            "k": ["open door", "john hay", "boxer rebellion"],
            "n": 0
        },
        {
            "id": "benevolent-assimilation",
            "tier": "power",
            "t": "Proclaimed “benevolent assimilation” of the Philippines (1898); the Philippine-American War against Emilio Aguinaldo’s forces began in 1899",
            "k": ["benevolent assimilation", "aguinaldo", "philippine-american war"],
            "n": 0
        },
        {
            "id": "anti-imperialists",
            "tier": "power",
            "t": "The Anti-Imperialist League, including Mark Twain and Andrew Carnegie, opposed keeping the Philippines; the Senate passed the treaty by one vote (1899)",
            "k": ["anti-imperialist league", "mark twain", "andrew carnegie"],
            "n": 0
        },
        {
            "id": "carnation",
            "tier": "power",
            "t": "Wore a red carnation for luck; Ohio’s state flower, the scarlet carnation, honors him",
            "k": ["scarlet carnation", "carnation", "state flower"],
            "n": 0
        },
        {
            "id": "canton-memorial",
            "tier": "power",
            "t": "Born in Niles, Ohio (1843); buried in a domed memorial in Canton with his wife, Ida; pictured on the $500 bill",
            "k": ["niles", "$500 bill", "memorial"],
            "n": 0
        }
    ],
    "trap": {
        "title": "McKinley or Roosevelt?",
        "body": "Theodore Roosevelt was McKinley’s assistant secretary of the Navy, then his vice president, and he became president when McKinley was shot, so their clues overlap: 1898, Cuba, and 1901. Players also blurt out William Jennings Bryan, the man McKinley beat twice, or Benjamin Harrison, the president who signed the 1890 tariff that McKinley wrote.",
        "fix": "Who was shot in Buffalo, who campaigned from his front porch, and who asked Congress to declare war on Spain? McKinley. Who charged up San Juan Hill with the Rough Riders or took over in 1901? Roosevelt. Who gave the “Cross of Gold” speech and lost? Bryan.",
        "line": "Real answer line: William <b><u>McKinley</u></b>"
    },
    "tests": {
        "right": [
            "William McKinley",
            "McKinley",
            "President McKinley",
            "William McKinly",
            "Mckinely"
        ],
        "prompt": [
            "William"
        ],
        "wrong": [
            "Theodore Roosevelt",
            "William Jennings Bryan",
            "Mount McKinley",
            "Mark Hanna",
            "Leon Czolgosz",
            "Benjamin Harrison",
            "Grover Cleveland"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", data["id"])
