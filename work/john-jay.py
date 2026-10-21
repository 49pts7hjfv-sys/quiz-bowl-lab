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
    "id": "john-jay",
    "name": "John Jay",
    "mono": "JJ",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "First Chief Justice of the United States · Diplomat and Federalist author",
    "dates": "1745–1829",
    "briefing": "John Jay helped negotiate the 1783 Treaty of Paris that ended the American Revolution, wrote five of the _Federalist_ essays, and became the first Chief Justice of the United States in 1789. In 1794 he made a treaty with Britain that was so unpopular that crowds burned him in effigy. As governor of New York, he signed a 1799 law that slowly ended slavery in the state.",
    "answerHtml": "John <b><u>Jay</u></b> (do not accept “Jay’s Treaty” or “John Marshall”)",
    "accept": [
        "john jay",
        "jay",
        "chief justice john jay",
        "justice john jay",
        "justice jay",
        "governor john jay"
    ],
    "prompt": [],
    "reject": [
        "jays treaty",
        "jay treaty",
        "the jay treaty",
        "jay s treaty",
        "treaty of london",
        "treaty of amity commerce and navigation",
        "pinckneys treaty",
        "pinckney treaty",
        "treaty of san lorenzo",
        "treaty of paris",
        "john marshall",
        "marshall",
        "john rutledge",
        "rutledge",
        "oliver ellsworth",
        "ellsworth",
        "alexander hamilton",
        "hamilton",
        "james madison",
        "madison",
        "john adams",
        "adams",
        "john quincy adams",
        "benjamin franklin",
        "franklin",
        "thomas jefferson",
        "jefferson",
        "george washington",
        "washington",
        "george clinton",
        "clinton",
        "thomas pinckney",
        "charles pinckney",
        "robert livingston",
        "william livingston",
        "gouverneur morris",
        "henry laurens",
        "publius",
        "federalist papers",
        "the federalist papers",
        "the federalist",
        "chisholm v georgia",
        "jay gould",
        "jay gatsby",
        "william jay",
        "peter jay",
        "sarah jay",
        "sarah livingston jay",
        "john jay college",
        "john jay college of criminal justice"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/John_Jay",
    "qb": {
        "q": "John Jay",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {"n": 0, "note": "no real tossups checked yet"},
    "tossups": [
        T("In _Chisholm v. Georgia_, the Court led by this man ruled that a citizen of one state could sue another state in federal court, a decision that led directly to the Eleventh Amendment. That Court had first met in New York City in February 1790.",
          "For 10 points, name this man whom George Washington appointed as the first Chief Justice of the United States."),
        T("Late in 1800, John Adams nominated this man to return to a job he had once held, but he turned it down, writing that the Court lacked “energy, weight, and dignity.” Adams then gave that job to his secretary of state, John Marshall.",
          "For 10 points, name this New Yorker who had been the first Chief Justice of the United States."),
        T("In 1793, the Court led by this man refused to answer a list of questions from Secretary of State Thomas Jefferson about American neutrality in the war between Britain and France, setting the rule that federal courts do not give advisory opinions. This man also had to ride circuit, hearing cases around the country.",
          "He was appointed by George Washington in 1789. For 10 points, name this New Yorker, the first Chief Justice of the United States."),
        T("In 1792, this man won more votes for governor of New York than George Clinton, but officials threw out the ballots from Otsego and two other counties on technicalities, and Clinton kept his office. Three years later, this man was elected governor while he was away in England.",
          "He had gone to London to negotiate a treaty with Britain. For 10 points, name this man, then the first Chief Justice of the United States."),
        T("As governor, this man signed a 1799 law declaring that children born to enslaved mothers after that July 4 would become free at age 28 for males and 25 for females. Years earlier, he had been the first president of the New York Manumission Society, which opened the African Free School.",
          "For 10 points, name this New Yorker who also served as the first Chief Justice of the United States."),
        T("In 1786, this man negotiated with Spain’s envoy Diego de Gardoqui [“gar-DOH-kee”] on a trade treaty that would have closed the Mississippi River to American shipping for years, which outraged Southern and Western Americans. He had earlier spent more than two years as an American envoy in Madrid.",
          "He was then the secretary of foreign affairs under the Articles of Confederation. For 10 points, name this New Yorker who became the first Chief Justice."),
        T("Distrusting the French foreign minister Vergennes [“ver-ZHEN”], this diplomat persuaded his fellow commissioners to negotiate directly with Britain’s envoy Richard Oswald, even though Congress had told them to consult France first. With Benjamin Franklin and John Adams, he signed the resulting treaty in 1783.",
          "That Treaty of Paris ended the American Revolution. For 10 points, name this New Yorker who later became the first Chief Justice."),
        T("Illness limited this man to writing just five essays in a famous series: numbers 2 through 5, on the dangers of foreign force and influence, and number 64, on the Senate’s power to approve treaties. Like his two co-authors, he signed those essays “Publius.”",
          "His co-authors were Alexander Hamilton and James Madison. For 10 points, name this New Yorker who later became the first Chief Justice."),
        T("This man reportedly joked that he could travel the country at night by the light of his own burning effigies after he signed a 1794 agreement with Lord Grenville. That agreement got British soldiers out of their forts in the Northwest Territory but did nothing to stop the British from forcing American sailors into their navy.",
          "Democratic-Republicans hated that treaty, which bears his name. For 10 points, name this diplomat who was then serving as Chief Justice."),
        T("This descendant of French Huguenots [“HYOO-guh-nots”] graduated from King’s College, now Columbia University, in 1764 and married Sarah Livingston, a daughter of future New Jersey governor William Livingston. A college of criminal justice in New York City is named for him.",
          "For 10 points, name this Founding Father who served as the first Chief Justice of the United States."),
        T("This man was the main author of New York’s first state constitution in 1777, and he then became that state’s first chief justice. In late 1778, he was elected president of the Continental Congress, succeeding Henry Laurens of South Carolina.",
          "The next year, Congress sent him to Spain. For 10 points, name this New Yorker who later became the first Chief Justice of the United States."),
        T("The Senate approved a treaty negotiated by this man by a vote of 20 to 10, exactly the two-thirds it needed, after striking out an article that limited American trade with the British West Indies. In 1796, Fisher Ames gave a famous speech urging the House to pay for carrying out that treaty.",
          "That treaty with Britain, signed in 1794, bears this man’s name. For 10 points, name this first Chief Justice of the United States."),
        T("As a holdover from the Confederation government, this man kept running American foreign policy until Thomas Jefferson arrived in 1790 to lead the new State Department. In 1801, he retired to a farm near Bedford, New York, where he lived until 1829.",
          "George Washington had already named him the first Chief Justice. For 10 points, name this New Yorker."),
        T("A 1794 treaty negotiated by this man alarmed Spain, which feared an alliance between Britain and the United States and soon agreed to Pinckney’s Treaty, opening the Mississippi River to American trade. This man negotiated his own treaty in London while he was still serving as a judge.",
          "Thomas Pinckney negotiated the Spanish treaty in 1795. For 10 points, name this first Chief Justice of the United States."),
        T("Writing as “A Citizen of New-York,” this man published a 1788 pamphlet urging his state to ratify the Constitution. He then joined Alexander Hamilton at the state’s ratifying convention in Poughkeepsie [“puh-KIP-see”], where the Constitution passed by just three votes.",
          "He had also written five of _The Federalist_ essays. For 10 points, name this man who became the first Chief Justice of the United States.")
    ],
    "clues": [
        C("first-chief-justice", "giveaway", "First Chief Justice of the United States (1789–1795), appointed by George Washington",
          ["first chief justice", "chief justice", "george washington"], "U.S. Supreme Court"),
        C("treaty-1794", "giveaway", "Negotiated the 1794 treaty with Britain that bears his name, which Democratic-Republicans hated",
          ["1794", "britain", "democratic-republicans"]),
        C("federalist", "giveaway", "Wrote 5 of the 85 _Federalist_ essays with Alexander Hamilton and James Madison, all signed “Publius”",
          ["federalist", "publius", "hamilton", "madison"], "The Federalist Papers"),
        C("chisholm", "middle", "_Chisholm v. Georgia_ (1793): his Court let a citizen sue another state, which led to the 11th Amendment",
          ["chisholm", "11th amendment", "georgia"]),
        C("emancipation", "middle", "Signed New York’s 1799 gradual emancipation law: children of enslaved mothers freed at 28 (males) or 25 (females)",
          ["1799", "gradual emancipation", "emancipation"]),
        C("manumission", "middle", "First president of the New York Manumission Society (1785), which opened the African Free School",
          ["manumission", "african free school"]),
        C("effigies", "middle", "His British treaty was so unpopular that he joked he could travel by the light of his burning effigies",
          ["effigies", "burning"]),
        C("forts", "middle", "That treaty removed British troops from forts in the Northwest Territory but did not stop impressment of American sailors",
          ["forts", "northwest territory", "impressment"]),
        C("continental-congress", "middle", "President of the Continental Congress (1778–1779), after Henry Laurens",
          ["continental congress", "henry laurens"]),
        C("foreign-affairs", "middle", "Secretary of foreign affairs under the Articles of Confederation; stayed until Jefferson arrived in 1790",
          ["foreign affairs", "articles of confederation", "jefferson"], "Articles of Confederation"),
        C("declined", "middle", "Turned down John Adams’s offer to be Chief Justice again (1800), saying the Court lacked “energy, weight, and dignity”; Adams chose John Marshall",
          ["dignity", "john marshall", "turned down"], "John Marshall"),
        C("paris", "middle", "Helped negotiate the Treaty of Paris (1783) that ended the Revolution, with Benjamin Franklin and John Adams",
          ["treaty of paris", "1783", "franklin"], "Treaty of Paris"),
        C("governor", "middle", "Governor of New York (1795–1801), elected while he was negotiating in England",
          ["governor", "new york", "1795"]),
        C("gardoqui", "power", "Envoy to Spain (1779–1782); his 1786 talks with Diego de Gardoqui would have closed the Mississippi River to Americans for years",
          ["gardoqui", "mississippi", "spain"]),
        C("vergennes", "power", "Distrusted French minister Vergennes and pushed to negotiate directly with Britain’s Richard Oswald",
          ["vergennes", "oswald"]),
        C("federalist-64", "power", "Wrote _Federalist_ Nos. 2–5 (dangers from foreign force) and No. 64 (the Senate’s treaty power)",
          ["treaty power", "foreign force", "64"]),
        C("advisory", "power", "His Court refused Jefferson’s questions (1793), so federal courts give no advisory opinions",
          ["advisory opinions", "advisory"]),
        C("otsego", "power", "Lost the 1792 race for governor to George Clinton after Otsego County’s ballots were thrown out",
          ["otsego", "george clinton", "1792"]),
        C("ny-constitution", "power", "Main author of New York’s 1777 constitution, then the state’s first chief justice",
          ["1777", "constitution"]),
        C("grenville", "power", "Negotiated his 1794 treaty in London with Lord Grenville",
          ["grenville", "london"]),
        C("senate-vote", "power", "The Senate approved his treaty 20–10, exactly two-thirds, after cutting an article on British West Indies trade",
          ["two-thirds", "west indies", "20–10"]),
        C("ames", "power", "Fisher Ames’s 1796 speech urged the House to pay for carrying out the treaty",
          ["fisher ames", "ames"], "Federalist Party"),
        C("pinckney", "power", "Spain, fearing an Anglo-American alliance, agreed to Pinckney’s Treaty (1795)",
          ["pinckney", "anglo-american"]),
        C("huguenots", "power", "Descended from French Huguenots; graduated from King’s College (now Columbia) in 1764; married Sarah Livingston",
          ["huguenots", "columbia", "sarah livingston"]),
        C("citizen", "power", "Wrote a 1788 pamphlet as “A Citizen of New-York”; New York ratified the Constitution by just three votes",
          ["citizen of new-york", "1788", "three votes"]),
        C("bedford", "power", "Retired in 1801 to a farm near Bedford, New York; died in 1829",
          ["bedford", "1829"]),
        C("college", "power", "A New York City college of criminal justice is named for him",
          ["criminal justice", "college"])
    ],
    "trap": {
        "title": "The man or his treaty?",
        "body": "Some tossups ask for Jay’s Treaty, the 1794 agreement with Britain, instead of the man who negotiated it, and answering “John Jay” to “name this treaty” is wrong. Early buzzers also mix him up with John Marshall, the fourth Chief Justice, who wrote _Marbury v. Madison_, and with his _Federalist_ co-authors Alexander Hamilton and James Madison. Pinckney’s Treaty (1795, with Spain) and the Treaty of Paris (1783) are other treaty traps.",
        "fix": "“This man” or “this Chief Justice” wants John Jay; “this treaty” wants Jay’s Treaty. First Chief Justice, the Treaty of Paris, five _Federalist_ essays, and governor of New York mean Jay; _Marbury v. Madison_ and 34 years on the Court mean Marshall.",
        "line": "Real answer line: John <b><u>Jay</u></b> (do not accept “Jay’s Treaty”)"
    },
    "tests": {
        "right": [
            "John Jay",
            "Jay",
            "Jon Jay",
            "Chief Justice John Jay",
            "John Jey"
        ],
        "prompt": [],
        "wrong": [
            "Jay's Treaty",
            "John Marshall",
            "Alexander Hamilton",
            "James Madison",
            "Treaty of Paris",
            "Jay Gould",
            "John Adams"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
