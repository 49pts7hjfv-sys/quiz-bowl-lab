import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

LINE = "<b><u>karma</u></b> (or <u>kamma</u>; do not accept “dharma,” “samsara,” or “reincarnation”)"

data = {
    "id": "karma",
    "name": "Karma",
    "mono": "KAR",
    "category": "Religion",
    "qbCategory": "Religion",
    "kicker": "Law that actions bring results · Shared by Hindus, Buddhists, Jains, and Sikhs",
    "dates": "Taught in India for more than 2,500 years",
    "briefing": "Karma is a Sanskrit word meaning “action,” and it names the idea that every deed, good or bad, brings results for the person who does it, in this life or a future one. Hindus, Buddhists, Jains, and Sikhs all teach it, though in different ways: Jains picture it as sticky particles clinging to the soul, while Buddhists say what counts most is a person’s intention.",
    "answerHtml": LINE,
    "accept": [
        "karma",
        "kamma",
        "karmic"
    ],
    "prompt": [],
    "reject": [
        "dharma",
        "dhamma",
        "samsara",
        "reincarnation",
        "rebirth",
        "transmigration",
        "moksha",
        "nirvana",
        "ahimsa",
        "atman",
        "brahman",
        "maya",
        "kama",
        "karna",
        "yoga",
        "jnana",
        "bhakti",
        "punya",
        "merit",
        "fate",
        "destiny",
        "gamma",
        "kurma",
        "parma",
        "arma",
        "karl marx"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Karma",
    "qb": {"q": "karma", "found": 0, "tip": TIP},
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        {
            "p": "In the _Brihadaranyaka Upanishad_ [“brih-hud-AR-un-yuh-kuh oo-PAN-ih-shud”], the sage Yajnavalkya [“yahj-nyah-VAHL-kyah”] teaches that a person becomes good through good deeds and bad through bad deeds. He adds that desire shapes a person’s will, will shapes deeds, and deeds shape what that person becomes.",
            "r": "For 10 points, name this principle of cause and effect, from a Sanskrit word meaning “action.”"
        },
        {
            "p": "In the _Bhagavad Gita_, Krishna tells Arjuna he has a right to his actions but never to their fruits, and teaches a path of selfless action named for this concept. Krishna presents that path alongside the paths of devotion, or bhakti, and of knowledge, or jnana [“GYAH-nuh”].",
            "r": "For 10 points, name this idea, found in Hinduism and Buddhism, that every deed brings consequences."
        },
        {
            "p": "Some Hindu teachers divide this concept into three kinds: sanchita [“SUN-chih-tuh”], the store built up over past lives; prarabdha [“pruh-RAHB-duh”], the portion that bears fruit in this life; and agami [“AH-gah-mee”], the portion being created by present actions.",
            "r": "Hindus believe it binds the soul to the cycle of rebirth until it reaches moksha. For 10 points, name this law of moral cause and effect."
        },
        {
            "p": "The Buddha declared that this concept is really intention, or cetana [“CHAY-tuh-nuh”], so only deliberate acts of body, speech, and mind produce it. Buddhists call its results vipaka [“vih-PAH-kuh”], meaning “ripening,” and compare them to fruit that grows from a planted seed.",
            "r": "For 10 points, name this principle that good and bad actions bring good and bad results."
        },
        {
            "p": "During the second watch of the night of his enlightenment, the Buddha is said to have seen countless beings dying and being born again in better or worse states according to this principle. In the first watch of that night, he had remembered his own past lives.",
            "r": "For 10 points, name this law of cause and effect, a Sanskrit word for “action” or “deed.”"
        },
        {
            "p": "One religion sorts this force into eight main types and calls its inflow into the soul asrava [“AHS-ruh-vuh”] and its shedding nirjara [“nir-JAH-ruh”]. That religion teaches that this force is made of tiny particles of matter that stick to the soul, or jiva [“JEE-vuh”], like dust on an oily cloth.",
            "r": "Jains try to shed all of it to free the soul. For 10 points, name this concept, from a Sanskrit word meaning “action.”"
        },
        {
            "p": "Guru Nanak’s Japji [“JUP-jee”] teaches that people reap what they themselves have sown, and that this force decides the kind of body a soul is born into. Yet Sikhs believe that liberation comes only through God’s grace, called nadar [“NUH-dur”].",
            "r": "For 10 points, name this law of cause and effect that Sikhs share with Hindus, Buddhists, and Jains."
        },
        {
            "p": "Hindus and Jains often speak of two kinds of this force: punya [“POON-yuh”], or merit, and papa [“PAH-puh”], or demerit. Buddhists in Thailand and Laos make merit by placing food in the bowls of monks on their morning alms rounds, hoping to improve this force.",
            "r": "Good and bad deeds are thought to shape a person’s next life. For 10 points, name this principle that deeds bring matching results."
        },
        {
            "p": "In the earliest Vedas, this word mostly meant the correct performance of sacrifices and other rituals, a meaning stressed by the Mimamsa [“mee-MAHM-suh”] school of Hindu philosophy. Later texts turned it into a moral law that helps explain samsara [“sum-SAH-ruh”], the cycle of rebirth.",
            "r": "Hindus, Buddhists, Jains, and Sikhs all teach versions of it. For 10 points, name this Sanskrit word meaning “action” or “deed.”"
        },
        {
            "p": "In the Tibetan Wheel of Life, a ring around the center shows people rising on a white half and falling on a black half, to stand for good and bad forms of this force. The whole wheel is gripped by Yama [“YAH-muh”], the lord of death.",
            "r": "Buddhists believe this force helps decide where beings are reborn. For 10 points, name this principle of cause and effect."
        },
        {
            "p": "The opening verse of the _Dhammapada_ [“DAH-muh-PAH-duh”] says that suffering follows a person who speaks or acts with an impure mind, just as a cart’s wheel follows the foot of the ox that pulls it. Buddhists see that verse as a lesson about this force.",
            "r": "Its name comes from a Sanskrit word meaning “action.” For 10 points, name this law that good and bad deeds bring matching results."
        },
        {
            "p": "In Hindu tradition, the scribe Chitragupta [“chit-ruh-GOOP-tuh”] records the good and bad deeds that make up each person’s store of this force, so that Yama, the god of death, can judge each soul. Many Hindus believe this force decides what kind of life a soul enters next.",
            "r": "Its name means “action” in Sanskrit. For 10 points, name this law of moral cause and effect."
        },
        {
            "p": "Swami Vivekananda [“vih-VAY-kah-NUN-duh”] turned lectures he had given in New York into a book about a yoga named for this concept, teaching that work done without selfish motives frees the soul. He drew that teaching from the _Bhagavad Gita_.",
            "r": "For 10 points, name this concept, which teaches that every action has consequences in this life and the next."
        },
        {
            "p": "Jains teach that the Tirthankaras [“teer-TUN-kuh-ruz”] reached perfect knowledge only after destroying the four most harmful types of this, which cloud the soul’s knowledge, perception, bliss, and energy. Jain monks keep strict vows to stop new amounts of it from flowing in, and they fast to burn away what has already built up.",
            "r": "For 10 points, name this principle that Jains picture as a sticky substance clinging to the soul."
        },
        {
            "p": "John Lennon’s 1970 hit single put the word “Instant” in front of this concept, and Culture Club’s 1983 number-one song paired it with a color-changing lizard. In the late 1800s, the Theosophical Society helped spread this idea, along with belief in past lives, to Europeans and Americans.",
            "r": "Its name is a Sanskrit word for “action.” For 10 points, name this concept, often summed up as “what goes around comes around.”"
        }
    ],
    "clues": [
        {
            "id": "action",
            "tier": "giveaway",
            "t": "From a Sanskrit word meaning “action” or “deed”: the law that every action brings a result",
            "k": ["action", "deed", "sanskrit"],
            "n": 0
        },
        {
            "id": "religions",
            "tier": "giveaway",
            "t": "Taught in Hinduism, Buddhism, Jainism, and Sikhism",
            "k": ["hinduism", "buddhism", "jainism", "sikhism"],
            "n": 0
        },
        {
            "id": "rebirth",
            "tier": "giveaway",
            "t": "Good and bad deeds shape a person’s future, including the next life in the cycle of rebirth (samsara)",
            "k": ["samsara", "rebirth", "next life"],
            "n": 0,
            "rabbit": "Reincarnation"
        },
        {
            "id": "goes-around",
            "tier": "giveaway",
            "t": "In everyday English, it means “what goes around comes around”",
            "k": ["what goes around", "comes around"],
            "n": 0
        },
        {
            "id": "gita",
            "tier": "middle",
            "t": "In the _Bhagavad Gita_, Krishna teaches the yoga of selfless action: do your duty without attachment to its fruits",
            "k": ["bhagavad gita", "krishna", "selfless action", "fruits"],
            "n": 0,
            "rabbit": "Krishna"
        },
        {
            "id": "three-paths",
            "tier": "middle",
            "t": "The _Gita_’s three paths: selfless action, jnana (knowledge), and bhakti (devotion)",
            "k": ["jnana", "bhakti", "knowledge", "devotion"],
            "n": 0
        },
        {
            "id": "jain-matter",
            "tier": "middle",
            "t": "Jains see it as sticky, invisible particles of matter that cling to the soul (jiva); shedding them all frees the soul",
            "k": ["sticky", "jiva", "particles", "matter"],
            "n": 0,
            "rabbit": "Jainism"
        },
        {
            "id": "liberation",
            "tier": "middle",
            "t": "Escaping its hold brings moksha (in Hinduism and Jainism) or nirvana (in Buddhism)",
            "k": ["moksha", "nirvana", "escaping"],
            "n": 0,
            "rabbit": "Nirvana"
        },
        {
            "id": "intention",
            "tier": "middle",
            "t": "In Buddhism, the Buddha said it is really intention (cetana), so only deliberate acts count",
            "k": ["intention", "cetana", "deliberate"],
            "n": 0
        },
        {
            "id": "merit",
            "tier": "middle",
            "t": "Good deeds bring merit (punya) and bad deeds bring demerit (papa); Buddhists make merit by giving food to monks",
            "k": ["merit", "punya", "papa", "monks"],
            "n": 0
        },
        {
            "id": "sikh-grace",
            "tier": "middle",
            "t": "In Sikhism, it decides the body a soul is born into, but liberation comes through God’s grace (nadar)",
            "k": ["grace", "nadar", "liberation"],
            "n": 0,
            "rabbit": "Sikhism"
        },
        {
            "id": "yajnavalkya",
            "tier": "power",
            "t": "In the _Brihadaranyaka Upanishad_, the sage Yajnavalkya says one becomes good by good deeds and bad by bad deeds",
            "k": ["yajnavalkya", "brihadaranyaka", "upanishad"],
            "n": 0
        },
        {
            "id": "three-kinds",
            "tier": "power",
            "t": "Three kinds in Hindu teaching: sanchita (stored up), prarabdha (ripening now), and agami (being made now)",
            "k": ["sanchita", "prarabdha", "agami"],
            "n": 0
        },
        {
            "id": "vipaka",
            "tier": "power",
            "t": "Buddhists call its results vipaka (“ripening”), like fruit growing from a seed",
            "k": ["vipaka", "ripening", "seed"],
            "n": 0
        },
        {
            "id": "second-watch",
            "tier": "power",
            "t": "In the second watch of his enlightenment night, the Buddha saw beings reborn according to their deeds",
            "k": ["second watch", "enlightenment"],
            "n": 0
        },
        {
            "id": "asrava",
            "tier": "power",
            "t": "Jain terms: asrava (inflow), bandha (bondage), samvara (stopping), and nirjara (shedding)",
            "k": ["asrava", "nirjara", "samvara", "bandha"],
            "n": 0
        },
        {
            "id": "eight-types",
            "tier": "power",
            "t": "Jains name eight main types; the Tirthankaras destroyed the four most harmful ones before reaching perfect knowledge",
            "k": ["eight main types", "tirthankaras", "perfect knowledge"],
            "n": 0
        },
        {
            "id": "sow",
            "tier": "power",
            "t": "Guru Nanak’s Japji says people reap what they themselves have sown",
            "k": ["japji", "sown", "reap"],
            "n": 0
        },
        {
            "id": "mimamsa",
            "tier": "power",
            "t": "In the earliest Vedas it mostly meant correct ritual action; the Mimamsa school stressed that meaning",
            "k": ["vedas", "ritual", "mimamsa"],
            "n": 0
        },
        {
            "id": "wheel-of-life",
            "tier": "power",
            "t": "Tibetan Wheel of Life: a ring shows beings rising on a white half and falling on a black half; Yama grips the wheel",
            "k": ["wheel of life", "white half", "yama"],
            "n": 0
        },
        {
            "id": "dhammapada",
            "tier": "power",
            "t": "The _Dhammapada_’s first verse: suffering follows an impure mind as a cart’s wheel follows the ox",
            "k": ["dhammapada", "cart", "ox"],
            "n": 0
        },
        {
            "id": "chitragupta",
            "tier": "power",
            "t": "In Hindu tradition, the scribe Chitragupta records each person’s deeds for Yama, the god of death",
            "k": ["chitragupta", "scribe", "records"],
            "n": 0
        },
        {
            "id": "vivekananda",
            "tier": "power",
            "t": "Swami Vivekananda’s book of New York lectures explained the yoga of selfless work",
            "k": ["vivekananda", "new york", "lectures"],
            "n": 0
        },
        {
            "id": "west",
            "tier": "power",
            "t": "The Theosophical Society spread it in the West in the late 1800s; songs by John Lennon (1970) and Culture Club (1983) used the word",
            "k": ["theosophical", "lennon", "culture club"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Action, not the cycle",
        "body": "Karma, dharma, samsara, and moksha all turn up in the same Hindu and Buddhist tossups, and they sound alike. Karma is the force of a person’s actions; samsara is the cycle of birth, death, and rebirth that karma keeps turning; dharma is duty or the Buddha’s teaching; and moksha or nirvana is the escape. Reincarnation is the rebirth itself, not the law that shapes it, so “reincarnation” is wrong here.",
        "fix": "Listen for deeds, fruits, merit, or cause and effect: that is karma. “This cycle” or “this wheel” means samsara, “this duty” means dharma, and “this liberation” means moksha or nirvana. The Pali form, kamma, is accepted.",
        "line": "Real answer line: " + LINE
    },
    "tests": {
        "right": [
            "karma",
            "Karma",
            "kamma",
            "the law of karma",
            "karmma",
            "karmic law"
        ],
        "prompt": [],
        "wrong": [
            "dharma",
            "samsara",
            "reincarnation",
            "moksha",
            "nirvana",
            "kama",
            "Karna"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
