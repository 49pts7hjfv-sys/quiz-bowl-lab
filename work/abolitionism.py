import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "abolitionism",
    "name": "Abolitionism",
    "mono": "AB",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "The movement to end slavery · Grew into a national crusade in the 1830s",
    "dates": "Roots in the 1700s; a national movement from the 1830s to 1865",
    "briefing": "Abolitionism was the movement to end slavery. In the 1830s it grew from a few small groups into a national crusade, led by people like William Lloyd Garrison, who demanded immediate emancipation in _The Liberator_, and Frederick Douglass, who had escaped slavery himself. Abolitionists gave speeches, flooded Congress with petitions, and spread books such as _Uncle Tom’s Cabin_. Many faced angry mobs, and in 1837 a mob in Illinois killed the editor Elijah Lovejoy.",
    "answerHtml": "<b><u>abolition</u></b>ism (or <u>abolition</u>ist movement; accept <u>antislavery movement</u>; prompt on <u>emancipation</u>; do not accept “Underground Railroad,” “Emancipation Proclamation,” or “Free Soil Party”)",
    "accept": [
        "abolitionism",
        "abolition",
        "abolitionist movement",
        "abolition movement",
        "abolitionists",
        "abolitionist",
        "abolition of slavery",
        "antislavery movement",
        "anti slavery movement",
        "movement to end slavery",
        "movement to abolish slavery"
    ],
    "prompt": [
        "antislavery",
        "anti slavery",
        "emancipation",
        "ending slavery",
        "freeing the slaves",
        "freeing slaves"
    ],
    "reject": [
        "underground railroad",
        "emancipation proclamation",
        "free soil party",
        "free soil",
        "free soilers",
        "liberty party",
        "william lloyd garrison",
        "garrison",
        "frederick douglass",
        "harriet tubman",
        "sojourner truth",
        "harriet beecher stowe",
        "uncle toms cabin",
        "john brown",
        "thirteenth amendment",
        "13th amendment",
        "american anti slavery society",
        "american colonization society",
        "colonization",
        "colonization movement",
        "womens suffrage",
        "suffrage",
        "womens rights movement",
        "temperance",
        "temperance movement",
        "prohibition",
        "republican party",
        "civil rights movement",
        "reconstruction",
        "second great awakening",
        "great awakening",
        "fugitive slave act",
        "gag rule",
        "slave rebellions"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Abolitionism_in_the_United_States",
    "qb": {
        "q": "abolitionism",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In November 1837, a proslavery mob in Alton, Illinois, killed the newspaper editor Elijah Lovejoy while he defended his printing press. Weeks later, the young lawyer Wendell Phillips gave his first famous speech for this cause at Boston’s Faneuil Hall, protesting that killing.",
            "r": "For 10 points, name this movement, led by William Lloyd Garrison and Frederick Douglass, that demanded freedom for all enslaved people."
        },
        {
            "p": "Raised in a slaveholding family in Charleston, South Carolina, two sisters moved north and became speakers for this cause. In 1838, the younger sister, Angelina Grimké, became the first woman to address an American legislative body.",
            "r": "She spoke to a committee of the Massachusetts legislature. For 10 points, name this movement that fought to end slavery in the United States."
        },
        {
            "p": "An antislavery weekly in Washington, D.C., called _The National Era_ first printed a novel in installments in 1851 and 1852, and the book version sold hundreds of thousands of copies. That novel’s characters include Eliza, who escapes across the frozen Ohio River.",
            "r": "That novel, Harriet Beecher Stowe’s _Uncle Tom’s Cabin_, won many Northerners over to this cause. For 10 points, name this movement against slavery."
        },
        {
            "p": "The wealthy New York merchants Arthur and Lewis Tappan helped pay for a national organization founded in Philadelphia in December 1833 to advance this cause. Its Declaration of Sentiments promised to work without violence.",
            "r": "That group was the American Anti-Slavery Society. For 10 points, name this movement, whose leaders included William Lloyd Garrison."
        },
        {
            "p": "James G. Birney, a former slaveholder, ran for president in 1840 and 1844 as the candidate of the Liberty Party, the first political party built around this cause. In 1844, Birney’s votes in New York may have cost Henry Clay the election.",
            "r": "For 10 points, name this movement, which William Lloyd Garrison led through his newspaper _The Liberator_."
        },
        {
            "p": "Born Isabella Baumfree in New York, one leader of this cause walked away from slavery in 1826 with her baby daughter and later won a court case to get back her young son, who had been illegally sold to an owner in Alabama.",
            "r": "She later took the name Sojourner Truth. For 10 points, name this movement against slavery."
        },
        {
            "p": "From 1836 to 1844, the House of Representatives used a “gag rule” to table, without debate, the flood of petitions sent by supporters of this cause. Former president John Quincy Adams fought the rule for years until it was finally repealed.",
            "r": "For 10 points, name this movement that worked to end slavery, led by figures like William Lloyd Garrison."
        },
        {
            "p": "In 1835, supporters of this cause mailed huge numbers of pamphlets to Southern towns, and a mob in Charleston broke into the post office and burned them. Andrew Jackson’s postmaster general allowed Southern postmasters to refuse to deliver such mail.",
            "r": "Its national society organized that mailing campaign. For 10 points, name this movement, which demanded an immediate end to slavery."
        },
        {
            "p": "In 1829, David Walker, a free Black man in Boston, published an _Appeal_ urging enslaved people to resist, and in 1843 Henry Highland Garnet told a convention, “Let your motto be resistance!” Both men were radical voices in this movement.",
            "r": "For 10 points, name this movement against slavery, whose best-known newspaper was William Lloyd Garrison’s _The Liberator_."
        },
        {
            "p": "In 1834, students at Lane Seminary in Cincinnati held more than two weeks of debates on slavery, and many left for Oberlin College after the school tried to silence them. Their leader, Theodore Weld, later wrote _American Slavery As It Is_ to support this cause.",
            "r": "For 10 points, name this movement that demanded the freeing of all enslaved people."
        },
        {
            "p": "In 1688, four Quakers in Germantown, Pennsylvania, signed one of the earliest written protests against slavery in the colonies. Later Quakers such as John Woolman and Anthony Benezet [“BEN-uh-zet”] carried on this cause, and Benjamin Franklin led a Pennsylvania society devoted to it.",
            "r": "The cause grew into a national movement in the 1830s. For 10 points, name this movement against slavery."
        },
        {
            "p": "Josiah Wedgwood’s factory made a medallion showing a kneeling, chained man who asks, “Am I Not a Man and a Brother?” It became a symbol of this cause, which in Britain was led by William Wilberforce and won an 1833 law ending slavery in most of the empire.",
            "r": "In the United States, its leaders included Frederick Douglass. For 10 points, name this movement against slavery."
        },
        {
            "p": "When women delegates were shut out of a world convention for this cause in London in 1840, Lucretia Mott and Elizabeth Cady Stanton met and decided that women needed their own movement. Eight years later, they organized the Seneca Falls Convention.",
            "r": "For 10 points, name this movement against slavery that helped launch the fight for women’s rights."
        },
        {
            "p": "Lewis Tappan organized a committee to defend the Africans who had seized the Spanish schooner _Amistad_ in 1839, and former president John Quincy Adams argued their case before the Supreme Court, which freed them in 1841.",
            "r": "Tappan also helped found the American Anti-Slavery Society. For 10 points, name this movement against slavery led by people like William Lloyd Garrison."
        },
        {
            "p": "Founded in Philadelphia in 1833, the national society of this movement voted to disband in 1870, after the Fifteenth Amendment protected Black men’s right to vote. Wendell Phillips had led that society for its last five years.",
            "r": "Its most famous newspaper had stopped printing in 1865, once the Thirteenth Amendment ended slavery. For 10 points, name this movement led by William Lloyd Garrison and Frederick Douglass."
        }
    ],
    "clues": [
        {
            "id": "definition",
            "tier": "giveaway",
            "t": "The reform movement that fought to free all enslaved people; it became a national crusade in the 1830s",
            "k": ["reform movement", "enslaved", "1830s"],
            "n": 0
        },
        {
            "id": "garrison",
            "tier": "giveaway",
            "t": "William Lloyd Garrison’s newspaper _The Liberator_ (1831) demanded immediate emancipation",
            "k": ["william lloyd garrison", "garrison", "the liberator", "immediate emancipation"],
            "n": 0,
            "rabbit": "William Lloyd Garrison"
        },
        {
            "id": "douglass",
            "tier": "giveaway",
            "t": "Frederick Douglass, who escaped slavery, became its greatest speaker and founded _The North Star_",
            "k": ["frederick douglass", "douglass", "north star"],
            "n": 0,
            "rabbit": "Frederick Douglass"
        },
        {
            "id": "thirteenth",
            "tier": "giveaway",
            "t": "Its main goal was reached when the 13th Amendment ended slavery (1865)",
            "k": ["13th amendment", "1865"],
            "n": 0
        },
        {
            "id": "aass",
            "tier": "giveaway",
            "t": "The American Anti-Slavery Society, founded in Philadelphia in 1833, was its main national group",
            "k": ["american anti-slavery society", "1833"],
            "n": 0
        },
        {
            "id": "tubman",
            "tier": "middle",
            "t": "Harriet Tubman and others led people north on the Underground Railroad",
            "k": ["harriet tubman", "tubman", "underground railroad"],
            "n": 0,
            "rabbit": "Underground Railroad"
        },
        {
            "id": "sojourner",
            "tier": "middle",
            "t": "Sojourner Truth, born Isabella Baumfree, spoke for it and for women’s rights; her 1851 Akron speech is remembered as “Ain’t I a Woman?”",
            "k": ["sojourner truth", "isabella baumfree", "ain’t i a woman"],
            "n": 0
        },
        {
            "id": "grimke",
            "tier": "middle",
            "t": "Sarah and Angelina Grimké, sisters from a Charleston slaveholding family, spoke for it",
            "k": ["grimké", "angelina", "charleston"],
            "n": 0
        },
        {
            "id": "uncle-tom",
            "tier": "middle",
            "t": "Harriet Beecher Stowe’s _Uncle Tom’s Cabin_ (1852) won many Northerners to the cause",
            "k": ["uncle tom’s cabin", "harriet beecher stowe", "stowe"],
            "n": 0,
            "rabbit": "Uncle Tom’s Cabin"
        },
        {
            "id": "lovejoy",
            "tier": "middle",
            "t": "A proslavery mob killed the editor Elijah Lovejoy in Alton, Illinois (1837)",
            "k": ["elijah lovejoy", "lovejoy", "alton"],
            "n": 0
        },
        {
            "id": "liberty-party",
            "tier": "middle",
            "t": "The Liberty Party ran James G. Birney for president (1840, 1844); his 1844 New York votes may have cost Henry Clay; it later merged into the Free Soil Party",
            "k": ["liberty party", "james g. birney", "birney", "henry clay"],
            "n": 0
        },
        {
            "id": "gag-rule",
            "tier": "middle",
            "t": "The House “gag rule” (1836–1844) tabled its petitions; John Quincy Adams fought it",
            "k": ["gag rule", "petitions", "john quincy adams"],
            "n": 0
        },
        {
            "id": "london-1840",
            "tier": "middle",
            "t": "Women shut out of the 1840 World Anti-Slavery Convention in London, like Lucretia Mott and Elizabeth Cady Stanton, went on to organize Seneca Falls",
            "k": ["world anti-slavery convention", "lucretia mott", "seneca falls", "1840"],
            "n": 0,
            "rabbit": "Seneca Falls Convention"
        },
        {
            "id": "phillips",
            "tier": "power",
            "t": "Weeks after Lovejoy’s death, Wendell Phillips gave his first famous speech for the cause at Faneuil Hall",
            "k": ["wendell phillips", "faneuil hall"],
            "n": 0
        },
        {
            "id": "angelina-legislature",
            "tier": "power",
            "t": "Angelina Grimké became the first woman to address an American legislative body (Massachusetts, 1838)",
            "k": ["legislative body", "massachusetts", "1838"],
            "n": 0
        },
        {
            "id": "national-era",
            "tier": "power",
            "t": "_Uncle Tom’s Cabin_ first ran in installments in _The National Era_, an antislavery paper in Washington, D.C.",
            "k": ["national era", "installments"],
            "n": 0
        },
        {
            "id": "tappans",
            "tier": "power",
            "t": "New York merchants Arthur and Lewis Tappan paid for much of the work; Arthur was the first president of the American Anti-Slavery Society",
            "k": ["arthur tappan", "lewis tappan", "tappan"],
            "n": 0
        },
        {
            "id": "truth-court-case",
            "tier": "power",
            "t": "Sojourner Truth walked away from slavery in 1826 and won a court case to get back her son, illegally sold to an owner in Alabama",
            "k": ["court case", "1826", "alabama"],
            "n": 0
        },
        {
            "id": "postal-campaign",
            "tier": "power",
            "t": "1835 postal campaign: a Charleston mob burned its pamphlets, and Postmaster General Amos Kendall let Southern postmasters block them",
            "k": ["pamphlets", "amos kendall", "1835"],
            "n": 0
        },
        {
            "id": "walker",
            "tier": "power",
            "t": "David Walker, a free Black man in Boston, published an _Appeal_ (1829) urging enslaved people to resist",
            "k": ["david walker", "appeal", "1829"],
            "n": 0
        },
        {
            "id": "garnet",
            "tier": "power",
            "t": "Henry Highland Garnet told an 1843 convention, “Let your motto be resistance!”",
            "k": ["henry highland garnet", "garnet", "motto be resistance"],
            "n": 0
        },
        {
            "id": "lane-seminary",
            "tier": "power",
            "t": "Lane Seminary debates in Cincinnati (1834); many students left for Oberlin; their leader Theodore Weld wrote _American Slavery As It Is_ (1839)",
            "k": ["lane seminary", "oberlin", "theodore weld", "american slavery as it is"],
            "n": 0
        },
        {
            "id": "quakers",
            "tier": "power",
            "t": "Quakers led early protests: the Germantown protest (1688), John Woolman, and Anthony Benezet; Benjamin Franklin later led a Pennsylvania society for the cause",
            "k": ["germantown", "john woolman", "benezet", "quakers"],
            "n": 0,
            "rabbit": "Quakers"
        },
        {
            "id": "wedgwood",
            "tier": "power",
            "t": "Josiah Wedgwood’s medallion “Am I Not a Man and a Brother?” became its symbol; in Britain, William Wilberforce led the cause",
            "k": ["wedgwood", "am i not a man and a brother", "wilberforce"],
            "n": 0
        },
        {
            "id": "amistad",
            "tier": "power",
            "t": "Lewis Tappan’s committee defended the _Amistad_ Africans, whom the Supreme Court freed in 1841",
            "k": ["amistad", "1841"],
            "n": 0
        },
        {
            "id": "disband",
            "tier": "power",
            "t": "The American Anti-Slavery Society disbanded in 1870, after the 15th Amendment protected Black men’s right to vote",
            "k": ["disbanded", "1870", "15th amendment"],
            "n": 0
        }
    ],
    "trap": {
        "title": "The movement, not a person",
        "body": "Tossups on this movement are full of names, and William Lloyd Garrison, Frederick Douglass, Harriet Tubman, and Sojourner Truth all have their own answer lines, so naming one of them is wrong when the question asks for “this movement.” The Underground Railroad (the escape network), the Emancipation Proclamation (Lincoln’s 1863 order), and the Free Soil Party (an 1848 party against spreading slavery west) are separate answers too.",
        "fix": "Listen for the noun. “This movement,” “this cause,” or “this crusade” wants abolitionism (“abolition” is fine). “This network” means the Underground Railroad, “this party” could mean the Liberty or Free Soil Party, and “this man” or “this woman” wants a person.",
        "line": "Real answer line: <b><u>abolition</u></b>ism (or <u>abolition</u>ist movement; accept <u>antislavery movement</u>; prompt on <u>emancipation</u>; do not accept “Underground Railroad” or “Emancipation Proclamation”)"
    },
    "tests": {
        "right": [
            "Abolitionism",
            "abolition",
            "abolitionist movement",
            "the abolitionists",
            "anti-slavery movement",
            "abolitionsim",
            "abolishion"
        ],
        "prompt": [
            "antislavery",
            "emancipation"
        ],
        "wrong": [
            "Underground Railroad",
            "Emancipation Proclamation",
            "Free Soil Party",
            "William Lloyd Garrison",
            "Thirteenth Amendment",
            "Women’s suffrage",
            "Temperance movement",
            "Uncle Tom’s Cabin"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("wrote", data["id"])
