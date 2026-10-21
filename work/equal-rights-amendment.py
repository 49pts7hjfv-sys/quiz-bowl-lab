import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

data = {
    "id": "equal-rights-amendment",
    "name": "Equal Rights Amendment",
    "mono": "ERA",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Proposed amendment for equal rights regardless of sex · Passed Congress in 1972",
    "dates": "Written 1923; passed by Congress 1972",
    "briefing": "Alice Paul, who had helped win women the right to vote, wrote the Equal Rights Amendment in 1923 to guarantee equal rights under the law regardless of sex. Congress passed it in 1972, but by its 1982 deadline only 35 of the 38 states needed had approved it, as opponents led by Phyllis Schlafly campaigned against it. Nevada, Illinois, and Virginia voted to ratify it decades later, and whether those late votes count has been debated in Congress and the courts.",
    "answerHtml": "<b><u>Equal Rights Amendment</u></b> (or <b><u>ERA</u></b>; accept <u>Lucretia Mott Amendment</u> or <u>Alice Paul Amendment</u>; prompt on <u>equal rights</u>; do not accept “Nineteenth Amendment” or “Fourteenth Amendment”)",
    "accept": [
        "equal rights amendment",
        "era",
        "e r a",
        "lucretia mott amendment",
        "alice paul amendment"
    ],
    "prompt": [
        "equal rights",
        "equal rights for women",
        "womens rights amendment"
    ],
    "reject": [
        "nineteenth amendment",
        "19th amendment",
        "amendment xix",
        "amendment 19",
        "susan b anthony amendment",
        "anthony amendment",
        "fourteenth amendment",
        "14th amendment",
        "amendment xiv",
        "amendment 14",
        "equal protection clause",
        "equal protection",
        "thirteenth amendment",
        "13th amendment",
        "fifteenth amendment",
        "15th amendment",
        "eighteenth amendment",
        "18th amendment",
        "twenty first amendment",
        "21st amendment",
        "twenty sixth amendment",
        "26th amendment",
        "twenty seventh amendment",
        "27th amendment",
        "equal pay act",
        "civil rights act",
        "title ix",
        "title vii",
        "voting rights act",
        "declaration of sentiments",
        "seneca falls convention",
        "womens suffrage",
        "suffrage",
        "national organization for women",
        "national womans party",
        "stop era",
        "eagle forum"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Equal_Rights_Amendment",
    "qb": {
        "q": "Equal Rights Amendment",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "In December 1923, Senator Charles Curtis, a future vice president, and Representative Daniel Anthony, a nephew of Susan B. Anthony, first introduced this proposal in Congress. Its author had announced it months earlier at Seneca Falls, New York.",
            "r": "That author, Alice Paul, led the National Woman’s Party. For 10 points, name this proposed amendment that Congress finally passed in 1972."
        },
        {
            "p": "In 1943, this proposal’s author rewrote it to sound like the amendment that had given women the vote, saying that “equality of rights under the law” could not be “denied or abridged” on account of sex. The proposal was then renamed for its author.",
            "r": "That author was Alice Paul. For 10 points, name this proposed amendment that was three states short of ratification when its 1982 deadline passed."
        },
        {
            "p": "In 1970, Michigan congresswoman Martha Griffiths used a discharge petition to force this proposal out of a House committee where it had been stuck for decades. After the House approved it again in 1971, the Senate followed in March 1972.",
            "r": "For 10 points, name this proposed amendment that would forbid denying rights under the law on account of sex."
        },
        {
            "p": "Hawaii approved this proposal within hours of its passage by Congress in March 1972. Congress placed a seven-year deadline for ratification in the resolution’s opening words rather than in the text of the amendment itself.",
            "r": "For 10 points, name this proposed amendment that only 35 states had ratified when its deadline arrived."
        },
        {
            "p": "Phyllis Schlafly led opposition to this proposal through a group whose name stood for “Stop Taking Our Privileges.” She argued that it could take away protections women had, such as being exempt from the military draft, while supporters said it would guarantee equal treatment under the law.",
            "r": "Alice Paul had first written it in 1923. For 10 points, name this proposed constitutional amendment, which Congress passed in 1972."
        },
        {
            "p": "After ratifications of this proposal stalled at 35 states in 1977, Congress voted the next year to extend its deadline from March 1979 to June 30, 1982. No more states approved it before the new deadline, and several states had voted to withdraw their earlier approvals.",
            "r": "For 10 points, name this proposed amendment, written by Alice Paul, that needed approval from 38 states to be ratified."
        },
        {
            "p": "In January 2020, Virginia became the 38th state to vote to ratify this proposal, following Nevada in 2017 and Illinois in 2018. Because those votes came long after the deadline Congress had set, the Archivist of the United States did not certify it.",
            "r": "For 10 points, name this proposed amendment, first written by Alice Paul in 1923 and passed by Congress in 1972."
        },
        {
            "p": "In January 2025, President Joe Biden said he considered this proposal part of the Constitution, but the Archivist of the United States said it could not be certified, citing earlier legal and court decisions about its deadline. Supporters and opponents had argued for years over whether late approvals counted.",
            "r": "For 10 points, name this proposed amendment that Congress passed in 1972 with a seven-year ratification deadline."
        },
        {
            "p": "This proposal’s author announced it in July 1923 at Seneca Falls, New York, during a celebration of the 75th anniversary of the first women’s rights convention held there. She named it for one of that convention’s organizers, Lucretia Mott.",
            "r": "That author was Alice Paul. For 10 points, name this proposed amendment that would ban denying rights on account of sex."
        },
        {
            "p": "The second section of this proposal lets Congress enforce it with laws, and the third says it would take effect two years after ratification. Its first section bars denying “equality of rights under the law” on account of sex.",
            "r": "Alice Paul first wrote it in 1923. For 10 points, name this proposed amendment that Congress passed in 1972."
        },
        {
            "p": "Opponents of this proposal brought loaves of homemade bread to state legislators, in a campaign led by the founder of the conservative group Eagle Forum. Many of those opponents described themselves as homemakers.",
            "r": "That founder was Phyllis Schlafly. For 10 points, name this proposed amendment that was not ratified by 38 states before its 1982 deadline."
        },
        {
            "p": "In July 1978, about 100,000 people marched in Washington, D.C., to ask Congress to give this proposal more time. The National Organization for Women had made winning its ratification one of the group’s top goals.",
            "r": "Congress agreed, extending the deadline to 1982. For 10 points, name this proposed amendment written by Alice Paul."
        },
        {
            "p": "Nebraska approved this proposal in 1972 and then voted in 1973 to take back its approval, the first of several states to do so. Whether a state may withdraw a ratification has been debated ever since.",
            "r": "For 10 points, name this proposed amendment, which Congress sent to the states in 1972."
        },
        {
            "p": "In 1940, the Republican Party became the first major party to support this proposal in its platform, and the Democrats followed four years later. Republicans removed that support from their platform in 1980.",
            "r": "For 10 points, name this proposed amendment, which Congress passed in 1972 and which Phyllis Schlafly campaigned against."
        },
        {
            "p": "For decades, some labor reformers opposed this proposal because they feared it would wipe out laws that limited women’s working hours and protected women in factories. Its supporters in the National Woman’s Party answered that such laws kept women out of many jobs.",
            "r": "Congress finally passed it in 1972. For 10 points, name this proposed amendment that Alice Paul wrote in 1923."
        }
    ],
    "clues": [
        {
            "id": "alice-paul",
            "tier": "giveaway",
            "t": "Written by Alice Paul of the National Woman’s Party in 1923",
            "k": ["alice paul", "national woman’s party", "1923"],
            "n": 0,
            "rabbit": "Women’s Suffrage"
        },
        {
            "id": "passed-1972",
            "tier": "giveaway",
            "t": "Passed by Congress in 1972 and sent to the states with a seven-year deadline",
            "k": ["1972", "seven-year", "deadline"],
            "n": 0
        },
        {
            "id": "three-short",
            "tier": "giveaway",
            "t": "Only 35 states had ratified by the deadline, three short of the 38 needed",
            "k": ["35 states", "three short", "38"],
            "n": 0
        },
        {
            "id": "schlafly",
            "tier": "giveaway",
            "t": "Phyllis Schlafly led the opposition through a campaign called STOP (“Stop Taking Our Privileges”)",
            "k": ["phyllis schlafly", "schlafly", "stop taking our privileges"],
            "n": 0
        },
        {
            "id": "section-1",
            "tier": "giveaway",
            "t": "Key words: “Equality of rights under the law shall not be denied or abridged … on account of sex”",
            "k": ["equality of rights", "on account of sex"],
            "n": 0
        },
        {
            "id": "extension",
            "tier": "middle",
            "t": "Congress extended the deadline from 1979 to June 30, 1982, but no more states ratified",
            "k": ["extended", "1982", "june 30"],
            "n": 0
        },
        {
            "id": "virginia",
            "tier": "middle",
            "t": "Virginia voted to ratify in January 2020 as the 38th state, after Nevada (2017) and Illinois (2018)",
            "k": ["virginia", "nevada", "illinois", "2020"],
            "n": 0
        },
        {
            "id": "archivist",
            "tier": "middle",
            "t": "The Archivist of the United States did not certify it, citing the expired deadline",
            "k": ["archivist", "certify"],
            "n": 0
        },
        {
            "id": "seneca-falls",
            "tier": "middle",
            "t": "Alice Paul announced it at Seneca Falls in 1923, on the 75th anniversary of the women’s rights convention there",
            "k": ["seneca falls", "75th anniversary"],
            "n": 0,
            "rabbit": "Seneca Falls Convention"
        },
        {
            "id": "lucretia-mott",
            "tier": "middle",
            "t": "Originally named for Lucretia Mott; reworded in 1943 and renamed for its author",
            "k": ["lucretia mott", "1943", "reworded"],
            "n": 0
        },
        {
            "id": "rescind",
            "tier": "middle",
            "t": "Several states, starting with Nebraska in 1973, voted to take back (rescind) their approvals",
            "k": ["rescind", "nebraska", "take back"],
            "n": 0
        },
        {
            "id": "draft-debate",
            "tier": "middle",
            "t": "Opponents argued it could end women’s exemption from the military draft; supporters said it would guarantee equal treatment",
            "k": ["military draft", "equal treatment"],
            "n": 0
        },
        {
            "id": "curtis-anthony",
            "tier": "power",
            "t": "First introduced in Congress in December 1923 by Senator Charles Curtis and Representative Daniel Anthony, Susan B. Anthony’s nephew",
            "k": ["charles curtis", "curtis", "daniel anthony", "nephew"],
            "n": 0,
            "rabbit": "Susan B. Anthony"
        },
        {
            "id": "griffiths",
            "tier": "power",
            "t": "Martha Griffiths of Michigan used a discharge petition (1970) to get it out of a House committee",
            "k": ["martha griffiths", "griffiths", "discharge petition"],
            "n": 0
        },
        {
            "id": "hawaii",
            "tier": "power",
            "t": "Hawaii was the first state to ratify, within hours of the Senate’s vote in March 1972",
            "k": ["hawaii", "within hours", "march 1972"],
            "n": 0
        },
        {
            "id": "opening-words",
            "tier": "power",
            "t": "The deadline was placed in the resolution’s opening words, not in the amendment’s text",
            "k": ["opening words", "resolution"],
            "n": 0
        },
        {
            "id": "indiana",
            "tier": "power",
            "t": "Indiana was the 35th state, in 1977; no other state voted to ratify until Nevada in 2017",
            "k": ["indiana", "1977", "2017"],
            "n": 0
        },
        {
            "id": "biden-2025",
            "tier": "power",
            "t": "In January 2025, President Joe Biden said he considered it part of the Constitution; the Archivist said it could not be certified",
            "k": ["joe biden", "january 2025", "could not be certified"],
            "n": 0
        },
        {
            "id": "sections-2-3",
            "tier": "power",
            "t": "Section 2 lets Congress enforce it; Section 3 says it takes effect two years after ratification",
            "k": ["section 2", "section 3", "two years"],
            "n": 0
        },
        {
            "id": "eagle-forum",
            "tier": "power",
            "t": "Schlafly founded the Eagle Forum (1975); opponents brought homemade bread to state legislators",
            "k": ["eagle forum", "bread", "homemade"],
            "n": 0
        },
        {
            "id": "march-1978",
            "tier": "power",
            "t": "About 100,000 people marched in Washington in July 1978 for more time; the National Organization for Women made it a top goal",
            "k": ["100,000", "national organization for women", "1978"],
            "n": 0
        },
        {
            "id": "platforms",
            "tier": "power",
            "t": "Republicans backed it in their platform from 1940 until 1980; Democrats backed it starting in 1944",
            "k": ["republicans", "platform", "1940", "1944"],
            "n": 0
        },
        {
            "id": "labor-opposition",
            "tier": "power",
            "t": "Some labor reformers opposed it for decades, fearing it would end laws that limited women’s working hours",
            "k": ["labor reformers", "working hours"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Which women’s amendment?",
        "body": "Two amendments about women come up constantly. The Nineteenth Amendment (1920), nicknamed the Susan B. Anthony Amendment, says the right to vote cannot be denied on account of sex; this proposal, written by Alice Paul in 1923, would bar denying equal rights under the law on account of sex. Because Alice Paul also led protests for the vote, early clues about her can fit either answer, and the Fourteenth Amendment’s Equal Protection Clause is a third trap.",
        "fix": "Voting, 1920, and the Silent Sentinels mean the Nineteenth Amendment. Phyllis Schlafly, 1972, a ratification deadline, 35 states, or Virginia in 2020 mean the Equal Rights Amendment, and “ERA” is fine. “Equal protection of the laws” and Reconstruction mean the Fourteenth.",
        "line": "Real answer line: <b><u>Equal Rights Amendment</u></b> (or <b><u>ERA</u></b>; do not accept “Nineteenth Amendment”)"
    },
    "tests": {
        "right": [
            "Equal Rights Amendment",
            "ERA",
            "the ERA",
            "Equal Right Amendment",
            "Lucretia Mott Amendment",
            "E.R.A."
        ],
        "prompt": [
            "equal rights"
        ],
        "wrong": [
            "Nineteenth Amendment",
            "19th Amendment",
            "Fourteenth Amendment",
            "Equal Protection Clause",
            "Equal Pay Act",
            "Title IX",
            "STOP ERA"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
