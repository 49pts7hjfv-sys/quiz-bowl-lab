import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "french-and-indian-war",
    "name": "French and Indian War",
    "mono": "FIW",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Britain vs. France for North America · Set the stage for the Revolution",
    "dates": "Fought 1754–1763",
    "briefing": "In 1754, a 22-year-old Virginia officer named George Washington led an attack that helped start a war over the Ohio River Valley. Britain and its American colonists fought France and its many Native American allies across North America until 1763. Britain won and took Canada, but its huge war debts led to new taxes on the colonies, which helped spark the American Revolution.",
    "answerHtml": "<b><u>French and Indian War</u></b> (prompt on <u>Seven Years’ War</u>; accept <u>Guerre de la Conquête</u>)",
    "accept": [
        "french and indian war",
        "french and indian wars",
        "french indian war",
        "the french and indian war",
        "french and indian",
        "fourth intercolonial war",
        "guerre de la conquete",
        "war of the conquest"
    ],
    "prompt": [
        "seven years war",
        "the seven years war",
        "7 years war"
    ],
    "reject": [
        "king georges war",
        "king williams war",
        "queen annes war",
        "king philips war",
        "pontiacs war",
        "pontiacs rebellion",
        "american revolution",
        "revolutionary war",
        "american revolutionary war",
        "war of 1812",
        "war of the austrian succession",
        "war of the spanish succession",
        "french revolution",
        "beaver wars",
        "fort necessity",
        "plains of abraham",
        "battle of the plains of abraham",
        "battle of quebec",
        "thirty years war",
        "hundred years war",
        "albany plan",
        "proclamation of 1763"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/French_and_Indian_War",
    "qb": {
        "q": "French and Indian War",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "The Seneca leader Tanacharison [“tan-uh-CHAR-ih-sun”], known as the Half King, guided Virginian soldiers to a French camp in a rocky glen in 1754, and the attack there helped start this war. The French officer Joseph Coulon de Villiers de Jumonville [“zhoo-mon-VEEL”] died in that attack.",
            "r": "Those Virginians were led by a young George Washington. For 10 points, name this war fought between Britain and France in North America from 1754 to 1763."
        },
        {
            "p": "Weeks after an ambush that helped start this war, a young officer surrendered a small, hastily built fort to Louis Coulon de Villiers [“koo-LOHN duh vee-YAY”] on July 3, 1754. The surrender papers, written in French, said the officer’s men had committed an “assassination” in that earlier ambush.",
            "r": "That officer, George Washington, had surrendered Fort Necessity. For 10 points, name this war in which Britain took Canada from France."
        },
        {
            "p": "Early in this war, a Pennsylvania newspaper printed a cartoon of a snake cut into eight pieces, each labeled with the name of a colony or region, above the words “Join, or Die.” Its creator proposed a plan at a meeting in Albany for the colonies to unite, but no colony approved it.",
            "r": "That creator was Benjamin Franklin. For 10 points, name this war in which Britain and its colonies fought France and its Native allies."
        },
        {
            "p": "In 1755, General Edward Braddock’s army was ambushed and badly defeated near the Monongahela [“muh-non-guh-HEE-luh”] River while marching to capture Fort Duquesne [“doo-KAYN”] during this war. Braddock died days later, and the young wagon driver Daniel Boone escaped from that battle.",
            "r": "A young George Washington helped lead the retreat. For 10 points, name this war that ended with the Treaty of Paris in 1763."
        },
        {
            "p": "William Johnson, a British official who worked closely with the Mohawk, defeated and captured the French general Baron Dieskau [“DEES-kow”] at the Battle of Lake George in 1755 during this war. The Mohawk leader Hendrick Theyanoguin [“thay-uh-NOH-gwin”] was killed fighting on the British side in that campaign.",
            "r": "Johnson’s Mohawk allies belonged to the Iroquois Confederacy. For 10 points, name this war, the North American part of the Seven Years’ War."
        },
        {
            "p": "During this war, British authorities forced thousands of French-speaking Acadians [“uh-KAY-dee-unz”] out of Nova Scotia, and many of them later settled in Louisiana, where their descendants are called Cajuns. Henry Wadsworth Longfellow’s poem _Evangeline_ tells of a young woman separated from her love during that expulsion.",
            "r": "This war ended with the Treaty of Paris of 1763. For 10 points, name this war in which Britain fought France for control of North America."
        },
        {
            "p": "The Marquis de Montcalm [“mont-KAHM”] captured Fort William Henry in 1757 during this war, and his Native allies then attacked the British soldiers and families who were leaving under a promise of safe passage. James Fenimore Cooper’s novel _The Last of the Mohicans_ is set during that siege.",
            "r": "Montcalm later died defending Quebec. For 10 points, name this war in which Britain and France fought for North America."
        },
        {
            "p": "In 1758, during this war, Montcalm’s much smaller French army defeated James Abercromby’s attack on Fort Carillon [“kah-ree-YOHN”], which stood between Lake George and Lake Champlain. The British captured that fort the next year and renamed it Fort Ticonderoga [“ty-kon-der-OH-guh”].",
            "r": "Ethan Allen captured that fort again in the American Revolution. For 10 points, name this war that ended with the Treaty of Paris in 1763."
        },
        {
            "p": "After British Secretary of State William Pitt poured money and troops into this war, John Forbes led an army across Pennsylvania in 1758. The French then blew up Fort Duquesne [“doo-KAYN”], which they had built at the Forks of the Ohio, rather than let Forbes capture it.",
            "r": "The British built Fort Pitt nearby, and the city of Pittsburgh grew around it. For 10 points, name this war fought over the Ohio River Valley."
        },
        {
            "p": "Jeffery Amherst and James Wolfe captured the French fortress of Louisbourg [“LOO-iss-burg”] on Cape Breton Island in 1758, during this war. New England soldiers had already taken Louisbourg once in an earlier war, but Britain gave it back to France in a 1748 treaty.",
            "r": "The next year, Wolfe won the Battle of Quebec. For 10 points, name this war that ended French rule in Canada."
        },
        {
            "p": "Benjamin West’s painting _The Death of General Wolfe_ shows a British commander dying after a battle in this war. In that 1759 battle, Wolfe’s soldiers climbed steep cliffs at night to reach the Plains of Abraham and defeated the Marquis de Montcalm, who also died.",
            "r": "That battle won Quebec City for Britain. For 10 points, name this war in which Britain conquered New France."
        },
        {
            "p": "The Marquis de Vaudreuil [“voh-DROY”], the last governor of New France, surrendered Montreal to Jeffery Amherst in 1760, ending most of the fighting in North America during this war. That surrender came a year after the fall of Quebec City.",
            "r": "Three years later, France gave up Canada in the Treaty of Paris. For 10 points, name this war fought from 1754 to 1763."
        },
        {
            "p": "In the treaty that ended this war, Britain chose to keep Canada and gave the sugar-rich island of Guadeloupe [“gwah-duh-LOOP”] back to France. Spain gave Florida to Britain in that 1763 treaty, after France had secretly handed Louisiana to Spain.",
            "r": "That treaty was signed in Paris. For 10 points, name this war that drove France out of mainland North America."
        },
        {
            "p": "Soon after this war ended, the Ottawa leader Pontiac led an uprising against British forts near the Great Lakes, and the Proclamation of 1763 banned colonists from settling west of the Appalachian Mountains. To pay this war’s debts, Parliament passed the Sugar Act and the Stamp Act.",
            "r": "For 10 points, name this war between Britain and France that ended in 1763 and helped lead to the American Revolution."
        },
        {
            "p": "Robert Rogers wrote a famous list of “Rules of Ranging” for his company of New England frontiersmen, who scouted and raided on snowshoes and in boats during this war. Rogers’ Rangers fought for the British around Lake George and Lake Champlain.",
            "r": "Their enemies were French soldiers and their Native allies. For 10 points, name this war fought in North America from 1754 to 1763."
        }
    ],
    "clues": [
        {
            "id": "britain-france",
            "tier": "giveaway",
            "t": "Britain and its American colonies vs. France and its Native American allies, 1754–1763",
            "k": ["britain", "france", "1754", "1763"],
            "n": 0
        },
        {
            "id": "ohio",
            "tier": "giveaway",
            "t": "Began as a fight over the Ohio River Valley",
            "k": ["ohio river valley", "ohio"],
            "n": 0
        },
        {
            "id": "washington",
            "tier": "giveaway",
            "t": "Young George Washington’s attack at Jumonville Glen helped start it; he then surrendered Fort Necessity (1754)",
            "k": ["george washington", "jumonville", "fort necessity"],
            "n": 0,
            "rabbit": "George Washington"
        },
        {
            "id": "treaty-paris",
            "tier": "giveaway",
            "t": "Treaty of Paris (1763): France lost Canada and its lands east of the Mississippi to Britain",
            "k": ["treaty of paris", "canada", "mississippi"],
            "n": 0
        },
        {
            "id": "seven-years",
            "tier": "giveaway",
            "t": "The North American part of the worldwide Seven Years’ War",
            "k": ["seven years", "worldwide"],
            "n": 0
        },
        {
            "id": "albany",
            "tier": "middle",
            "t": "Benjamin Franklin’s “Join, or Die” cartoon and Albany Plan of Union (1754); no colony approved the plan",
            "k": ["join, or die", "albany plan", "franklin"],
            "n": 0
        },
        {
            "id": "braddock",
            "tier": "middle",
            "t": "General Edward Braddock was defeated near the Monongahela River (1755) and died days later",
            "k": ["edward braddock", "braddock", "monongahela"],
            "n": 0
        },
        {
            "id": "wolfe-montcalm",
            "tier": "middle",
            "t": "Battle of the Plains of Abraham at Quebec (1759): James Wolfe beat the Marquis de Montcalm; both generals died",
            "k": ["plains of abraham", "wolfe", "montcalm", "quebec"],
            "n": 0
        },
        {
            "id": "pitt",
            "tier": "middle",
            "t": "William Pitt’s spending turned the war around; Pittsburgh grew from Fort Pitt, built near the ruins of Fort Duquesne",
            "k": ["william pitt", "fort pitt", "pittsburgh", "duquesne"],
            "n": 0
        },
        {
            "id": "aftermath",
            "tier": "middle",
            "t": "Afterward came Pontiac’s War, the Proclamation of 1763, and taxes like the Stamp Act to pay war debts",
            "k": ["proclamation of 1763", "pontiac", "stamp act", "debts"],
            "n": 0,
            "rabbit": "Stamp Act"
        },
        {
            "id": "iroquois",
            "tier": "middle",
            "t": "The Iroquois Confederacy, especially the Mohawk, mostly sided with Britain",
            "k": ["iroquois", "mohawk"],
            "n": 0
        },
        {
            "id": "mohicans",
            "tier": "middle",
            "t": "James Fenimore Cooper’s _The Last of the Mohicans_ is set during the siege of Fort William Henry (1757)",
            "k": ["last of the mohicans", "fenimore cooper", "fort william henry"],
            "n": 0
        },
        {
            "id": "tanacharison",
            "tier": "power",
            "t": "The Seneca leader Tanacharison (the Half King) guided Washington’s men to Jumonville’s camp",
            "k": ["tanacharison", "half king"],
            "n": 0
        },
        {
            "id": "coulon",
            "tier": "power",
            "t": "Washington surrendered Fort Necessity to Louis Coulon de Villiers and signed a French paper admitting an “assassination”",
            "k": ["coulon de villiers", "assassination"],
            "n": 0,
            "rabbit": "Fort Necessity"
        },
        {
            "id": "boone",
            "tier": "power",
            "t": "Daniel Boone was a wagon driver in Braddock’s army",
            "k": ["daniel boone", "wagon"],
            "n": 0
        },
        {
            "id": "lake-george",
            "tier": "power",
            "t": "William Johnson defeated and captured Baron Dieskau at Lake George (1755); the Mohawk leader Hendrick was killed fighting for Britain",
            "k": ["lake george", "dieskau", "hendrick", "william johnson"],
            "n": 0
        },
        {
            "id": "acadians",
            "tier": "power",
            "t": "Britain expelled the French-speaking Acadians from Nova Scotia; many became Louisiana’s Cajuns (Longfellow’s _Evangeline_)",
            "k": ["acadians", "cajuns", "evangeline", "nova scotia"],
            "n": 0
        },
        {
            "id": "carillon",
            "tier": "power",
            "t": "Montcalm beat James Abercromby at Fort Carillon (1758); the British later renamed it Fort Ticonderoga",
            "k": ["carillon", "abercromby", "ticonderoga"],
            "n": 0
        },
        {
            "id": "forbes",
            "tier": "power",
            "t": "John Forbes’s 1758 march made the French blow up Fort Duquesne at the Forks of the Ohio",
            "k": ["john forbes", "forbes", "forks of the ohio"],
            "n": 0
        },
        {
            "id": "louisbourg",
            "tier": "power",
            "t": "Amherst and Wolfe took Louisbourg on Cape Breton Island (1758); New Englanders had captured it once before",
            "k": ["louisbourg", "cape breton", "amherst"],
            "n": 0
        },
        {
            "id": "west-painting",
            "tier": "power",
            "t": "Benjamin West’s painting _The Death of General Wolfe_; Wolfe’s men climbed cliffs at night to reach the battlefield",
            "k": ["benjamin west", "death of general wolfe", "cliffs"],
            "n": 0
        },
        {
            "id": "vaudreuil",
            "tier": "power",
            "t": "Governor Vaudreuil surrendered Montreal to Jeffery Amherst (1760), ending New France",
            "k": ["vaudreuil", "montreal", "new france"],
            "n": 0
        },
        {
            "id": "guadeloupe",
            "tier": "power",
            "t": "In the 1763 treaty, Britain kept Canada over sugar-rich Guadeloupe; Spain gave Florida to Britain; France had secretly given Louisiana to Spain",
            "k": ["guadeloupe", "florida", "louisiana"],
            "n": 0
        },
        {
            "id": "rangers",
            "tier": "power",
            "t": "Robert Rogers wrote “Rules of Ranging”; Rogers’ Rangers scouted on snowshoes",
            "k": ["robert rogers", "rules of ranging", "snowshoes"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Which colonial war?",
        "body": "Britain and France fought four wars in North America, and this was the last and biggest. The first three were King William’s War, Queen Anne’s War, and King George’s War, and New Englanders even captured Louisbourg in King George’s War. Right after this war came Pontiac’s War (1763) and then the long road to the American Revolution, so clues about forts and Native alliances can point to several answers.",
        "fix": "This war’s clues: Washington at Fort Necessity, Braddock’s defeat, the Albany Plan, Montcalm and Wolfe at Quebec, and the 1763 Treaty of Paris. Some answer lines accept the Seven Years’ War, the name for the whole worldwide war, but others only prompt on it, so say “French and Indian War” when the clues are in North America.",
        "line": "Real answer line: <b><u>French and Indian War</u></b> (prompt on <u>Seven Years’ War</u>)"
    },
    "tests": {
        "right": [
            "French and Indian War",
            "French-Indian War",
            "the French and Indian War",
            "French and Indain War",
            "French and Indian Wars",
            "Guerre de la Conquête"
        ],
        "prompt": [
            "Seven Years’ War",
            "7 Years War"
        ],
        "wrong": [
            "King George’s War",
            "American Revolution",
            "Pontiac’s War",
            "War of 1812",
            "Queen Anne’s War",
            "Fort Necessity"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
