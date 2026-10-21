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
    "id": "fourteen-points",
    "name": "Fourteen Points",
    "mono": "14P",
    "category": "American History",
    "qbCategory": "History · American History",
    "kicker": "Woodrow Wilson’s plan for peace · Its last point called for a League of Nations",
    "dates": "Delivered January 8, 1918",
    "briefing": "On January 8, 1918, with World War I still being fought, President Woodrow Wilson told Congress his plan for a fair and lasting peace in fourteen numbered points. He called for an end to secret treaties, freedom of the seas, lower trade barriers, smaller armies, borders drawn along lines of nationality, and, in the last point, a League of Nations. Germany asked for peace on these terms, but the Treaty of Versailles left out many of them, and the U.S. Senate rejected that treaty.",
    "answerHtml": "<b><u>Fourteen Points</u></b> (accept <u>14 Points</u>; prompt on <u>Points</u> alone; do not accept “League of Nations” or “Treaty of Versailles”)",
    "accept": [
        "fourteen points",
        "the fourteen points",
        "14 points",
        "the 14 points",
        "wilsons fourteen points",
        "wilsons 14 points",
        "fourteen points speech",
        "fourteen point",
        "14 point"
    ],
    "prompt": [
        "points",
        "fourteen",
        "14",
        "wilsons plan",
        "wilsons peace plan"
    ],
    "reject": [
        "league of nations",
        "the league of nations",
        "treaty of versailles",
        "versailles treaty",
        "versailles",
        "paris peace conference",
        "covenant of the league of nations",
        "league covenant",
        "peace without victory",
        "four freedoms",
        "atlantic charter",
        "zimmermann telegram",
        "new freedom",
        "lodge reservations",
        "treaty of brest litovsk",
        "brest litovsk",
        "armistice",
        "fourteenth amendment",
        "14th amendment",
        "monroe doctrine",
        "truman doctrine",
        "big four"
    ],
    "media": [],
    "mediaPending": True,
    "wiki": "https://en.wikipedia.org/wiki/Fourteen_Points",
    "qb": {
        "q": "Fourteen Points",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        T("Colonel Edward House’s team of experts, known as “The Inquiry,” helped prepare this program, and the journalist Walter Lippmann helped draft it. Its author hoped it would answer the Bolsheviks [“BOHL-shuh-viks”], who had embarrassed the Allies by publishing their secret treaties.",
          "For 10 points, name this January 1918 plan for peace after World War I, presented by Woodrow Wilson."),
        T("Before the Allies accepted these proposals as the basis for an armistice, Britain rejected their call for “freedom of the seas,” and France insisted that Germany pay for damage done to civilians. Germany’s new chancellor, Prince Max of Baden, had asked for peace on these terms in October 1918.",
          "For 10 points, name this peace program that Woodrow Wilson announced to Congress in January 1918."),
        T("The thirteenth item of this program called for an independent Polish state with “free and secure access to the sea.” That demand led the peacemakers at Paris to give Poland a strip of land called the Polish Corridor, which cut East Prussia off from the rest of Germany.",
          "Its last item called for a League of Nations. For 10 points, name this January 1918 peace plan of Woodrow Wilson."),
        T("This program demanded that Belgium be evacuated and restored, that all French territory be freed, and that “the wrong done to France by Prussia in 1871” over Alsace-Lorraine be righted. It also called for Romania, Serbia, and Montenegro to be evacuated.",
          "The Treaty of Versailles later returned Alsace-Lorraine to France. For 10 points, name this list of war aims announced by Woodrow Wilson in January 1918."),
        T("The first item of this program called for “open covenants of peace, openly arrived at,” so that diplomacy would “proceed always frankly and in the public view.” Its second item called for “absolute freedom of navigation upon the seas.”",
          "For 10 points, name this set of proposals that Woodrow Wilson made for ending World War I."),
        T("Senator Henry Cabot Lodge, who chaired the Foreign Relations Committee, demanded changes called “reservations” before he would accept a treaty that was partly based on this program. The Senate rejected that treaty in 1919 and again in 1920.",
          "For 10 points, name this peace plan by Woodrow Wilson whose last item called for a League of Nations."),
        T("William Borah and other senators nicknamed the “Irreconcilables” opposed in any form the organization called for in the last item of this program. Many senators feared that Article X of that organization’s Covenant could drag the United States into foreign wars.",
          "That organization was the League of Nations. For 10 points, name this plan for peace presented by Woodrow Wilson in 1918."),
        T("This program called for the Dardanelles [“dar-duh-NELZ”] to be permanently opened as a free passage for the ships of all nations. It also promised that the non-Turkish peoples of the Ottoman Empire would have the chance for “autonomous development.”",
          "For 10 points, name this list of peace terms that Woodrow Wilson gave Congress in January 1918."),
        T("This program said that the peoples of Austria-Hungary should have “the freest opportunity to autonomous development,” and it called for Serbia to be given access to the sea. After the war, new countries such as Czechoslovakia formed from Austria-Hungary’s lands.",
          "For 10 points, name this plan for peace, built on the idea of self-determination, that Woodrow Wilson announced in 1918."),
        T("One item of this program said that Italy’s borders should be redrawn “along clearly recognizable lines of nationality.” At the Paris Peace Conference, Italy’s Vittorio Orlando walked out for a time when Woodrow Wilson refused to give Italy the port of Fiume [“fee-OO-may”].",
          "For 10 points, name this plan for peace that Wilson had announced to Congress during World War I."),
        T("While Russia’s new Bolshevik government was negotiating with Germany at Brest-Litovsk [“BREST lih-TOFSK”], this program called for all Russian territory to be evacuated. It also promised Russia “a sincere welcome into the society of free nations under institutions of her own choosing.”",
          "For 10 points, name this peace program that Woodrow Wilson presented to Congress in January 1918."),
        T("This program called for an “impartial adjustment of all colonial claims,” in which the interests of the colonized peoples would have “equal weight” with the claims of governments. It also called for national armaments to be reduced as far as domestic safety allows.",
          "For 10 points, name this plan for peace whose last item called for a League of Nations."),
        T("Almost a year before giving this speech, its author had told the Senate that the world needed a “peace without victory.” He gave this speech about nine months after the United States entered World War I, in an address to a joint session of Congress.",
          "For 10 points, name this January 1918 speech by Woodrow Wilson that listed his goals for peace."),
        T("This program’s author won the Nobel Peace Prize for 1919, mostly for his work creating the organization proposed in its final item. That item called for “a general association of nations” to protect the independence of “great and small states alike.”",
          "For 10 points, name this plan for peace presented by Woodrow Wilson in January 1918."),
        T("At the Paris Peace Conference, French premier Georges Clemenceau [“KLEM-un-soh”] demanded harsher terms for Germany than this program had promised, including large reparations payments. Clemenceau, Britain’s David Lloyd George, and Italy’s Vittorio Orlando joined this program’s author as the “Big Four.”",
          "The Treaty of Versailles left out many of this program’s ideas. For 10 points, name this peace plan announced by Woodrow Wilson in January 1918.")
    ],
    "clues": [
        C("wilson-1918", "giveaway", "Woodrow Wilson’s plan for peace after World War I, given to Congress on January 8, 1918", ["woodrow wilson", "january 8, 1918", "congress"], "Woodrow Wilson"),
        C("league", "giveaway", "Its last item called for “a general association of nations,” which became the League of Nations", ["league of nations", "general association"], "League of Nations"),
        C("self-determination", "giveaway", "Built on the idea of self-determination: peoples should choose their own governments", ["self-determination"]),
        C("versailles", "giveaway", "The Treaty of Versailles (1919) left out many of its ideas, and the U.S. Senate rejected that treaty", ["treaty of versailles", "versailles", "senate"], "Treaty of Versailles"),
        C("open-covenants", "middle", "First item: “open covenants of peace, openly arrived at” (no more secret treaties)", ["open covenants", "openly arrived at", "secret treaties"]),
        C("freedom-of-seas", "middle", "Second item: freedom of the seas, which Britain would not accept", ["freedom of the seas", "britain"]),
        C("trade-arms", "middle", "Called for removing trade barriers and reducing armaments", ["trade barriers", "armaments"]),
        C("poland", "middle", "Called for an independent Poland with “free and secure access to the sea”", ["poland", "access to the sea"]),
        C("alsace-lorraine", "middle", "France should get back Alsace-Lorraine, taken by Prussia in 1871; Belgium should be evacuated and restored", ["alsace-lorraine", "belgium", "1871"]),
        C("lodge", "middle", "Senator Henry Cabot Lodge led the fight against the treaty, demanding changes called “reservations”", ["henry cabot lodge", "lodge", "reservations"]),
        C("armistice", "middle", "Germany asked for an armistice based on it in October 1918; the fighting ended on November 11, 1918", ["armistice", "november 11", "october 1918"], "World War I"),
        C("nobel", "middle", "Wilson won the Nobel Peace Prize for 1919 for his work creating the League", ["nobel peace prize", "nobel"]),
        C("inquiry", "power", "Colonel Edward House’s team of experts, “The Inquiry,” helped prepare it; Walter Lippmann helped draft it", ["edward house", "inquiry", "walter lippmann", "lippmann"]),
        C("bolsheviks", "power", "Partly an answer to the Bolsheviks, who had published the Allies’ secret treaties in late 1917", ["bolsheviks", "published"]),
        C("russia", "power", "Sixth item: Russian territory evacuated and Russia welcomed into “the society of free nations” (during the Brest-Litovsk talks)", ["russia", "society of free nations", "brest-litovsk"]),
        C("colonial", "power", "Fifth item: an “impartial adjustment of all colonial claims”", ["colonial claims", "impartial"]),
        C("austria-hungary", "power", "Tenth item: “autonomous development” for the peoples of Austria-Hungary", ["austria-hungary", "autonomous development"]),
        C("dardanelles", "power", "Twelfth item: the Dardanelles opened to the ships of all nations; autonomy for the non-Turkish peoples of the Ottoman Empire", ["dardanelles", "ottoman"]),
        C("italy", "power", "Ninth item: Italy’s borders “along clearly recognizable lines of nationality”; Italy’s Orlando later walked out over Fiume", ["italy", "lines of nationality", "fiume"]),
        C("serbia", "power", "Eleventh item: Romania, Serbia, and Montenegro evacuated; Serbia given access to the sea", ["serbia", "montenegro", "romania"]),
        C("prince-max", "power", "Prince Max of Baden, Germany’s new chancellor, asked Wilson for an armistice on its terms (October 1918)", ["prince max", "max of baden", "chancellor"]),
        C("damage", "power", "Before accepting it as the basis for peace, France insisted that Germany pay for damage done to civilians", ["damage", "civilians"]),
        C("irreconcilables", "power", "William Borah’s “Irreconcilables” opposed the League in any form; Article X of its Covenant was the biggest fight", ["irreconcilables", "borah", "article x"]),
        C("peace-without-victory", "power", "Almost a year earlier (January 1917), Wilson had called for a “peace without victory”", ["peace without victory"]),
        C("polish-corridor", "power", "Led to the Polish Corridor, which cut East Prussia off from the rest of Germany", ["polish corridor", "east prussia"]),
        C("clemenceau", "power", "France’s Georges Clemenceau demanded harsher terms for Germany at the Paris Peace Conference", ["clemenceau", "paris peace conference"])
    ],
    "trap": {
        "title": "Speech, treaty, or league?",
        "body": "Three answer lines share Woodrow Wilson, Henry Cabot Lodge, and the Senate fight of 1919–1920. The Fourteen Points were Wilson’s January 1918 speech listing his goals for peace; the League of Nations was the organization his last point called for; and the Treaty of Versailles was the 1919 peace treaty with Germany that created the League. Answering “League of Nations” or “Versailles” here is wrong, and so is mixing it up with the Fourteenth Amendment.",
        "fix": "Listen for the noun. “This speech,” “this plan,” or “these proposals,” with numbered items such as freedom of the seas or an independent Poland, means the Fourteen Points. “This organization,” Geneva, or Article X means the League; “this treaty,” the war guilt clause, or the Hall of Mirrors means Versailles.",
        "line": "Real answer line: <b><u>Fourteen Points</u></b> (accept <u>14 Points</u>; do not accept “League of Nations” or “Treaty of Versailles”)"
    },
    "tests": {
        "right": [
            "Fourteen Points",
            "14 Points",
            "Wilson's Fourteen Points",
            "Fourten Points",
            "the Fourteen Points"
        ],
        "prompt": [
            "Points"
        ],
        "wrong": [
            "League of Nations",
            "Treaty of Versailles",
            "Fourteenth Amendment",
            "Peace without victory",
            "Woodrow Wilson"
        ]
    }
}

with open(ROOT / "topics" / f"{data['id']}.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", data["id"])
