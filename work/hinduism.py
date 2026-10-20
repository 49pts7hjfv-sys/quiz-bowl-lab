import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TIP = "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."

LINE = "<b><u>Hinduism</u></b> (or <u>Sanatana Dharma</u>; accept word forms like <u>Hindu</u>s)"

data = {
    "id": "hinduism",
    "name": "Hinduism",
    "mono": "OM",
    "category": "Religion",
    "qbCategory": "Religion",
    "kicker": "Major religion of India and Nepal · Vedas, karma, and the Trimurti",
    "dates": "Roots in the Vedic period, from c. 1500 BCE",
    "briefing": "Hinduism has no single founder and no single holy book, yet about 1.2 billion people follow it, most of them in India and Nepal. Many Hindus call it Sanatana Dharma, the “eternal way.” They honor gods such as Vishnu, Shiva, and Ganesha, revere ancient Sanskrit texts called the Vedas, and believe that karma shapes each soul’s journey through rebirth until it reaches moksha, or liberation.",
    "answerHtml": LINE,
    "accept": [
        "hinduism",
        "hindu",
        "hindus",
        "hindu religion",
        "hindu faith",
        "hindu dharma",
        "sanatana dharma",
        "sanatan dharma"
    ],
    "prompt": [],
    "reject": [
        "hindi",
        "hindu kush",
        "hindustan",
        "buddhism",
        "buddhist",
        "jainism",
        "jain",
        "sikhism",
        "sikh",
        "vedanta",
        "vedas",
        "vaishnavism",
        "shaivism",
        "vishnu",
        "shiva",
        "brahma",
        "brahman",
        "krishna"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Hinduism",
    "qb": {"q": "Hinduism", "found": 0, "tip": TIP},
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        {
            "p": "A hymn in this religion’s oldest scripture says that priests, warriors, merchants, and laborers came from the mouth, arms, thighs, and feet of a cosmic giant named Purusha [“POO-roo-shuh”]. Those four social classes are called varnas, and the priestly class is the Brahmins.",
            "r": "This religion’s gods include Vishnu and Shiva. For 10 points, name this major religion of India."
        },
        {
            "p": "The philosopher Adi Shankara [“AH-dee SHUN-kuh-ruh”] taught that the individual self, or atman, is the same as Brahman, the ultimate reality, in a school of this religion called Advaita [“ud-VY-tuh”] Vedanta. Shankara is also said to have founded four monasteries in the four corners of India.",
            "r": "Its sacred texts include the Vedas and the _Bhagavad Gita_. For 10 points, name this religion of most people in India and Nepal."
        },
        {
            "p": "In a text of this religion, the sage Uddalaka [“ood-DAH-luh-kuh”] asks his son Shvetaketu [“shvay-tuh-KAY-too”] to dissolve salt in water and then taste it, to show that an unseen essence fills everything. He repeats the lesson “tat tvam asi” [“tut TVUM uh-see”], or “you are that.”",
            "r": "That text is the Chandogya Upanishad. For 10 points, name this religion whose oldest scriptures are the four Vedas."
        },
        {
            "p": "In one text of this religion, a boy named Nachiketa [“nuh-chih-KAY-tuh”] waits three days at the house of Yama, the god of death, and is granted three wishes. For his last wish, Nachiketa asks what happens to a person after death, and Yama teaches him that the true self never dies.",
            "r": "That text is the Katha Upanishad. For 10 points, name this religion whose gods include Brahma, Vishnu, and Shiva."
        },
        {
            "p": "In a 700-verse poem sacred to this religion, the warrior Arjuna loses his nerve before a battle at Kurukshetra [“koo-roo-KSHAY-truh”], and his charioteer urges him to do his duty without worrying about the results. That charioteer reveals himself to be the god Krishna.",
            "r": "That poem, the _Bhagavad Gita_, is part of the epic _Mahabharata_. For 10 points, name this religion of India."
        },
        {
            "p": "One god of this religion is believed to have come to Earth as a fish named Matsya [“MUT-syuh”], a tortoise named Kurma, and a man-lion named Narasimha [“nuh-ruh-SIM-huh”], and believers expect a tenth such form, Kalki, to appear at the end of the present age. Those forms are called avatars.",
            "r": "Rama and Krishna are also avatars of that god, Vishnu. For 10 points, name this religion whose holy river is the Ganges."
        },
        {
            "p": "Tens of millions of followers of this religion gather for the Kumbh Mela [“KOOMB MAY-luh”], a festival of ritual bathing held in turn at four Indian cities. Its biggest gatherings are at Prayagraj [“pruh-YAHG-rahj”], where the Yamuna [“YUH-muh-nuh”] River joins a larger sacred river.",
            "r": "That river, the Ganges, also flows past the holy city of Varanasi. For 10 points, name this religion of India."
        },
        {
            "p": "The Khmer king Suryavarman II [“soor-yuh-VAR-mun”] built Angkor Wat in Cambodia as a temple to a god of this religion, though it later became a Buddhist shrine. On the Indonesian island of Bali, most people follow a local form of this religion.",
            "r": "That god was Vishnu. For 10 points, name this religion followed by most people in India and Nepal."
        },
        {
            "p": "Swami Vivekananda [“vih-VAY-kah-nun-duh”] introduced this religion to many Americans at the 1893 Parliament of the World’s Religions in Chicago, opening his first speech with “Sisters and brothers of America.” He later founded a mission named for his teacher, the mystic Ramakrishna.",
            "r": "This religion’s goddesses include Lakshmi and Durga. For 10 points, name this religion whose holy texts include the Vedas."
        },
        {
            "p": "The Laws of Manu, an ancient law book of this religion, describe four stages of life, called ashramas [“AHSH-ruh-muhz”]: student, householder, forest dweller, and wandering renouncer, or sannyasi [“sun-YAH-see”]. That book also lists the duties of each social class.",
            "r": "This religion’s gods include Shiva, Vishnu, and Ganesha, the elephant-headed remover of obstacles. For 10 points, name this religion."
        },
        {
            "p": "Many hymns in this religion’s oldest scripture praise Agni, the god of fire, and Indra, a thunder god who defeated the serpent Vritra [“VRIT-ruh”] to free the waters. That scripture also contains the Gayatri [“GAH-yuh-tree”] Mantra, a prayer to the sun that many believers recite every day.",
            "r": "That scripture is the Rig Veda. For 10 points, name this religion whose epics include the _Ramayana_."
        },
        {
            "p": "This religion names four goals of human life: dharma, or duty; artha, or wealth; kama, or enjoyment; and moksha, or liberation. The last of those goals means escaping samsara [“sum-SAH-ruh”], the cycle of death and rebirth that is driven by karma.",
            "r": "Its followers worship at temples called mandirs. For 10 points, name this religion in which Brahma, Vishnu, and Shiva form the Trimurti."
        },
        {
            "p": "On the night before one festival of this religion, people light bonfires to remember how the demoness Holika [“HOH-lih-kuh”] perished in a fire while her nephew Prahlad [“pruh-LAHD”], a devotee of Vishnu, walked out unharmed. Prahlad’s father, a demon king, was later defeated by Vishnu’s man-lion form.",
            "r": "The next day, during that festival of colors, Holi, people throw colored powder at each other. For 10 points, name this religion that also celebrates Diwali."
        },
        {
            "p": "The short Mandukya [“MAHN-doo-kyuh”] Upanishad explains that this religion’s most sacred syllable is made of three sounds, A, U, and M, followed by silence. That syllable is chanted at the start of many prayers and mantras, and its written symbol decorates many temples.",
            "r": "That syllable is Om. For 10 points, name this religion of India whose oldest scriptures are the Vedas."
        },
        {
            "p": "In 1828, Ram Mohan Roy founded the Brahmo Samaj [“BRAH-moh suh-MAHJ”] to reform this religion, and in 1875 Dayananda Saraswati [“dye-AH-nun-duh suh-RUSS-wuh-tee”] founded the Arya Samaj [“AR-yuh suh-MAHJ”]. Both reform groups rejected the worship of images. Roy also campaigned for women’s rights and modern education.",
            "r": "The Arya Samaj urged a return to this religion’s oldest texts, the Vedas. For 10 points, name this religion whose followers bathe in the sacred Ganges."
        }
    ],
    "clues": [
        {
            "id": "india-nepal",
            "tier": "giveaway",
            "t": "Major religion of India and Nepal, with about 1.2 billion followers, the world’s third-largest religion",
            "k": ["india", "nepal", "third-largest", "1.2 billion"],
            "n": 0
        },
        {
            "id": "trimurti",
            "tier": "giveaway",
            "t": "Gods include the Trimurti: Brahma the creator, Vishnu the preserver, and Shiva the destroyer",
            "k": ["trimurti", "brahma", "vishnu", "shiva"],
            "n": 0,
            "rabbit": "Vishnu"
        },
        {
            "id": "vedas",
            "tier": "giveaway",
            "t": "Its oldest scriptures are the four Vedas, written in Sanskrit; the Rig Veda is the oldest of them",
            "k": ["vedas", "sanskrit", "rig veda"],
            "n": 0
        },
        {
            "id": "karma-moksha",
            "tier": "giveaway",
            "t": "Teaches karma and samsara, the cycle of rebirth; the goal is moksha, liberation from that cycle",
            "k": ["karma", "samsara", "moksha", "rebirth"],
            "n": 0,
            "rabbit": "Karma"
        },
        {
            "id": "ganges",
            "tier": "giveaway",
            "t": "The Ganges River is sacred, and Varanasi, on its banks, is a holy city",
            "k": ["ganges", "varanasi"],
            "n": 0
        },
        {
            "id": "festivals",
            "tier": "giveaway",
            "t": "Festivals include Diwali, the festival of lights, and Holi, the festival of colors",
            "k": ["diwali", "holi"],
            "n": 0,
            "rabbit": "Diwali"
        },
        {
            "id": "bhagavad-gita",
            "tier": "middle",
            "t": "_Bhagavad Gita_: before the battle of Kurukshetra, the god Krishna, serving as Arjuna’s charioteer, urges him to do his duty",
            "k": ["bhagavad gita", "gita", "arjuna", "kurukshetra"],
            "n": 0,
            "rabbit": "Krishna"
        },
        {
            "id": "epics",
            "tier": "middle",
            "t": "Two great epics: the _Mahabharata_ (which contains the _Gita_) and the _Ramayana_, in which Prince Rama rescues Sita from Ravana",
            "k": ["mahabharata", "ramayana", "rama", "sita"],
            "n": 0,
            "rabbit": "Ramayana"
        },
        {
            "id": "brahman-atman",
            "tier": "middle",
            "t": "Brahman is the ultimate reality; the Upanishads teach that atman, the inner self, is one with Brahman",
            "k": ["brahman", "atman", "upanishads"],
            "n": 0
        },
        {
            "id": "avatars",
            "tier": "middle",
            "t": "Vishnu’s ten avatars include Matsya the fish, Narasimha the man-lion, Rama, Krishna, and Kalki, who is yet to come",
            "k": ["avatars", "matsya", "narasimha", "kalki"],
            "n": 0
        },
        {
            "id": "varnas",
            "tier": "middle",
            "t": "Four varnas (social classes): Brahmins (priests), Kshatriyas (warriors), Vaishyas (merchants), and Shudras (laborers)",
            "k": ["varnas", "brahmins", "kshatriyas", "caste"],
            "n": 0
        },
        {
            "id": "om",
            "tier": "middle",
            "t": "Om (Aum) is its most sacred syllable, chanted at the start of prayers and mantras",
            "k": ["om", "aum", "syllable", "mantras"],
            "n": 0
        },
        {
            "id": "puja",
            "tier": "middle",
            "t": "Worship called puja: offerings of flowers, food, and light to murtis (sacred images) at home or in a temple (mandir)",
            "k": ["puja", "murti", "mandir"],
            "n": 0
        },
        {
            "id": "no-founder",
            "tier": "middle",
            "t": "Has no single founder; its name comes from an old Persian word for the people of the Indus River region",
            "k": ["no single founder", "founder", "indus", "persian"],
            "n": 0
        },
        {
            "id": "ganesha-lakshmi",
            "tier": "middle",
            "t": "Other beloved deities: elephant-headed Ganesha, remover of obstacles, and Lakshmi, goddess of wealth",
            "k": ["ganesha", "lakshmi", "obstacles"],
            "n": 0,
            "rabbit": "Ganesha"
        },
        {
            "id": "purusha-sukta",
            "tier": "power",
            "t": "The Rig Veda’s Purusha Sukta says the four varnas came from the mouth, arms, thighs, and feet of the cosmic being Purusha",
            "k": ["purusha sukta", "purusha", "cosmic"],
            "n": 0
        },
        {
            "id": "rig-veda-gods",
            "tier": "power",
            "t": "Rig Veda hymns praise Agni (fire) and Indra, who defeated the serpent Vritra; it also contains the Gayatri Mantra",
            "k": ["agni", "indra", "vritra", "gayatri"],
            "n": 0
        },
        {
            "id": "tat-tvam-asi",
            "tier": "power",
            "t": "Chandogya Upanishad: Uddalaka teaches his son Shvetaketu “tat tvam asi” (“you are that”) using salt dissolved in water",
            "k": ["tat tvam asi", "chandogya", "shvetaketu", "salt"],
            "n": 0
        },
        {
            "id": "nachiketa",
            "tier": "power",
            "t": "Katha Upanishad: the boy Nachiketa waits three days for Yama, god of death, and asks him what happens after death",
            "k": ["nachiketa", "katha", "yama"],
            "n": 0
        },
        {
            "id": "shankara",
            "tier": "power",
            "t": "Adi Shankara founded Advaita (“non-dual”) Vedanta, teaching that atman and Brahman are the same",
            "k": ["shankara", "advaita", "vedanta", "non-dual"],
            "n": 0
        },
        {
            "id": "mandukya",
            "tier": "power",
            "t": "The Mandukya Upanishad explains Om as three sounds, A, U, and M, followed by silence",
            "k": ["mandukya", "silence"],
            "n": 0
        },
        {
            "id": "purusharthas",
            "tier": "power",
            "t": "Four goals of life (purusharthas): dharma (duty), artha (wealth), kama (enjoyment), and moksha (liberation)",
            "k": ["purusharthas", "dharma", "artha", "kama"],
            "n": 0
        },
        {
            "id": "ashramas",
            "tier": "power",
            "t": "Four stages of life (ashramas): student, householder, forest dweller, and renouncer (sannyasi), described in the Laws of Manu",
            "k": ["ashramas", "sannyasi", "laws of manu", "householder"],
            "n": 0
        },
        {
            "id": "kumbh-mela",
            "tier": "power",
            "t": "Kumbh Mela: a bathing festival held in turn at four cities; the biggest is at Prayagraj, where the Yamuna meets the Ganges",
            "k": ["kumbh mela", "prayagraj", "yamuna"],
            "n": 0
        },
        {
            "id": "angkor-bali",
            "tier": "power",
            "t": "Angkor Wat in Cambodia was built by Suryavarman II as a temple to Vishnu; most people on Bali, Indonesia, follow this faith",
            "k": ["angkor wat", "suryavarman", "bali"],
            "n": 0
        },
        {
            "id": "vivekananda",
            "tier": "power",
            "t": "Swami Vivekananda, a disciple of Ramakrishna, spoke at Chicago’s 1893 Parliament of the World’s Religions: “Sisters and brothers of America”",
            "k": ["vivekananda", "ramakrishna", "1893", "chicago"],
            "n": 0
        },
        {
            "id": "reformers",
            "tier": "power",
            "t": "Reform groups: Ram Mohan Roy’s Brahmo Samaj (1828) and Dayananda Saraswati’s Arya Samaj (1875), which urged a return to the Vedas",
            "k": ["brahmo samaj", "arya samaj", "ram mohan roy"],
            "n": 0
        },
        {
            "id": "holika",
            "tier": "power",
            "t": "Holi’s bonfires recall how the demoness Holika perished in a fire while her nephew Prahlad, a devotee of Vishnu, was unharmed",
            "k": ["holika", "prahlad", "bonfires"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Karma is not enough",
        "body": "Hinduism, Buddhism, Jainism, and Sikhism all began in South Asia, and all four teach karma, rebirth, and liberation (moksha or nirvana), so an early buzz on a karma or reincarnation clue can easily go wrong. Clues about one god can also tempt you to name that god, such as Vishnu or Shiva, when the question wants the whole religion.",
        "fix": "Wait for something only Hinduism has: the Vedas and Upanishads, the _Bhagavad Gita_, the Trimurti, Brahman and atman, or the four varnas. Siddhartha and the Four Noble Truths mean Buddhism; Mahavira and the 24 Tirthankaras mean Jainism; Guru Nanak means Sikhism.",
        "line": "Real answer line: " + LINE
    },
    "tests": {
        "right": [
            "Hinduism",
            "Hindu",
            "hindus",
            "Sanatana Dharma",
            "Hindusim",
            "the Hindu religion"
        ],
        "prompt": [],
        "wrong": [
            "Hindi",
            "Buddhism",
            "Jainism",
            "Sikhism",
            "Vedanta",
            "Vishnu"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
