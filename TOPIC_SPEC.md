# Quiz Bowl Lab: how to write one topic

You are writing study content for a middle-school Quiz Bowl team (6th–8th graders). Their coach's
method: learn the basics, search QBReader for real questions (Middle School + Easy High School,
answer search, tossups, power-marked only), write notes with easy clues at the top and hard clues at
the bottom with a "power line", then drill flashcards both ways. Each topic you write becomes one
page of the team's study website plus flashcards.

Your output for each topic is ONE file: `topics/<id>.json`. It must pass
`python3 validate.py --cross topics/<id>.json` with **0 errors**.
Do not edit any other file in the project (not the app, build, validator, manifest, or other topics).

Study these two finished topics before you start. Match their tone, depth, and format exactly:
- `topics/john-adams.json`
- `topics/jamestown.json`

The topic list is `data/manifest.json` (id, name, category, qbCategory for all 215
topics). Use the manifest's `id` exactly.

---------------------------------------------------------------------------------------------------
## Step 1. Research the real questions on QBReader (10 minutes)

Use WebFetch on the QBReader API. **Cache warning:** the fetch tool can return a stale cached result
for a different query on the same path, so every QBReader call must use a *different capitalization
of the path*. You are given your own list of path spellings (like `api/qUeRY`); use each one at most
once, in order. Never use plain `api/query`.

URL template (one line, URL-encode the query; spaces = `%20`):

    https://www.qbreader.org/<YOUR-PATH-SPELLING>?queryString=<QUERY>&questionType=tossup&searchType=answer&difficulties=1,2&powermarkOnly=true&maxReturnLength=30

Prompt to pass with it:

    Return the total tossup count and the queryString field. Then for EVERY tossup in the response: (1) the set name and year, (2) the full answer_sanitized line verbatim, (3) the full question_sanitized text verbatim including the (*) marker. Skip nothing.

Then:
- **Check the result is really yours** (the answers should match your topic). If it is clearly about
  something else, the cache gave a stale result: retry with your next path spelling.
- `queryString` = what the coach would type: the core answer words ("Henry VIII", "Bismarck",
  "Hamlet", "photosynthesis", "Shiva", "Diwali"). Short distinctive words find more answer lines.
- If the search mixes in other meanings (e.g. "Hundred Years" also finds the novel *One Hundred Years
  of Solitude*), add `&categories=History` (or Literature, Religion, Mythology, Science,
  Fine%20Arts, Philosophy, Social%20Science) on a retry, or just skip the off-topic results.
- If fewer than about 5 relevant tossups come back, run a second query with `difficulties=3`
  (Regular High School) and `maxReturnLength=12` using your next path spelling.
- Record: `qb.found` = the total count from the difficulties=1,2 search. The relevant real tossups
  you analyzed (MS/EHS plus any Regular HS) are your **sample**.
- Read every real answer line: its accept / prompt / "do not accept" rules become your `accept`,
  `prompt`, `reject` lists and often your Buzzer Trap.
- Count how many sample tossups use each clue. That count is each clue's `n`.

If QBReader is unreachable or returns nothing useful after 3 tries, write the topic from your own
knowledge plus Wikipedia, set `sample.n` to 0, all `n` to 0, `qb.found` to 0, and say so in `qb.tip`.

## Step 2. Write the content

Accuracy is the top priority. Kids will memorize every clue. Only state facts you are certain of.
Power clues should come from the real tossups you read (editors fact-checked them) or from things you
know well; when a real tossup has a fact you doubt, leave it out. Never invent quotes, dates or numbers.
Write ORIGINAL questions: do not copy sentences from the real tossups; reword and recombine.

Middle-school appropriate: no gore, no sexual content, no drug details, nothing graphic. Hard history
(the Holocaust, slavery, the Trail of Tears, wars) is stated plainly and respectfully. Religions are
described respectfully and accurately, the way a comparative-religion teacher would, with no judgment
and no horror-movie stereotypes (e.g. Vodou and Santería are real religions with West African roots).
Religious fasting is about faith and practice; never connect it to dieting or weight.

### Field by field

```
{
  "id": "<manifest id>",
  "name": "<manifest name>",
  "mono": "<1-3 capital letters or digits for the topic's badge, e.g. GW, FDR, H8, DNA, ZB>",
  "category": "<manifest category>",
  "qbCategory": "<QBReader category · subcategory, e.g. 'History · European History', 'Literature · British Literature', 'Religion', 'Mythology · Norse Mythology', 'Fine Arts · Painting', 'Science · Biology'>",
  "kicker": "<one line, two parts joined by ' · ': who/what it is · why it matters. Max ~70 chars>",
  "dates": "<short: '1491–1547', 'Fought 1337–1453', 'Published 1851', 'First performed c. 1600', 'Celebrated in the fall', 'Discovered 1897'>",
  "briefing": "<2-3 sentences, 35-90 words. A vivid hook a 6th grader would enjoy, with 2-3 real facts. Titles in _underscores_.>",
  "answerHtml": "<the answer line, QB style, required part in <b><u>…</u></b>, e.g. '<b><u>Henry VIII</u></b> (prompt on <u>Henry</u>)'>",
  "accept": ["<normalized acceptable answers>"],
  "prompt": ["<normalized answers that earn a prompt ('more specific?')>"],
  "reject": ["<normalized wrong answers that look close: siblings, namesakes, related topics>"],
  "tests": {"right": [...], "prompt": [...], "wrong": [...]},
  "media": [ ...see Step 3... ],
  "wiki": "https://en.wikipedia.org/wiki/<Article>",
  "qb": {"q": "<the queryString you used>", "found": <int>, "tip": "<one sentence about the search results: what to skip, what to notice, or a pattern>"},
  "sample": {"n": <int>, "note": "<completes the sentence '“Stock” counts come from …', e.g. 'the 8 real QBReader tossups for this answer line (Middle School + Easy High School, power-marked)' or '12 real QBReader tossups (4 Middle School/Easy High School + 8 Regular High School, power-marked)'>"},
  "tossups": [ {"p": "...", "r": "..."} x 15 ],
  "clues": [ {"id": "...", "tier": "giveaway|middle|power", "t": "...", "k": [...], "n": <int>, "rabbit": "<optional>"} ],
  "trap": {"title": "...", "body": "...", "fix": "...", "line": "Real answer line: <b><u>…</u></b> (…)"}
}
```

**Answer-line lists** (`accept`, `prompt`, `reject`) hold *normalized* strings: lowercase, accents
removed, apostrophes removed, other punctuation turned into spaces, single spaces. ("Hundred Years'
War" → `hundred years war`; "Bahá’í" → `bahai`; "Cú Chulainn" → `cu chulainn`.)
- The checker accepts typos by edit distance (1 typo for 5-7 letters, 2 for 8-12, 3 for longer), so
  anything *close but wrong* MUST be in `reject`: "henry vii" for Henry VIII, "napoleon iii" for
  Napoleon, "andrew jackson" for Andrew Johnson, "mitosis" for meiosis, "kinetic energy" for energy,
  "martin luther king" for Martin Luther, "lincoln memorial" for Abraham Lincoln.
- Accept the common forms and spellings (number forms like "henry 8", "henry the eighth"; last names
  for people when QB does; English and original-language titles for works, e.g. "les miserables"
  and "the miserable ones"; Roman/Greek equivalents only if real answer lines accept them).
- A reject entry also blocks any answer that *contains* it as a phrase, and an accept entry accepts any
  answer containing it, so think about overlaps (accepting `energy` would accept "kinetic energy" unless
  `kinetic energy` is in reject).
- `tests`: at least 4 `right` (incl. a typo and a title like "King …" if natural), 1+ `prompt` (if
  prompts exist), and 4+ `wrong` (the near-misses above), written the way a kid would type them.
  Run the validator: every test must pass, and no other topic's name in the manifest may be accepted
  on your line (`--cross`).

**Tossups** (15). Each is one QBReader-style tossup split at the power mark:
- `p` = the bold power portion (before the (*)); `r` = everything after, ending with the giveaway
  sentence, which must contain the exact words **For 10 points** ("For 10 points, name this …").
- 3-5 sentences, 50-85 words total; the power portion is about 55-75% of the words.
- Pyramidal: hardest clue first, then easier clues, giveaway last. Never name the answer anywhere in
  the text ("this king", "this war", "this novel", "this deity", "this organelle", "this force").
  Also avoid words that give it away (don't say "this eighth Henry").
- Use the real stock clues often (like real packets do), spread all your clue-breakdown facts across
  the set, and start the 15 questions with different lead-in clues. Giveaways may repeat with varied wording.
- Pronunciation guides for hard names go right after the word in this exact form:
  `Talleyrand [“TAL-ee-rand”]`. Titles of works in `_underscores_` (italics).
- Plain text only: no HTML, no "(*)" (the app adds it), no straight double quotes (use “ ” and ’).
- Difficulty: Middle School / Easy High School. Power clues should be learnable facts that appear in
  real MS/EHS (or regular HS) questions, not obscure trivia.

**Clue breakdown** (20-28 clues) = the coach's notebook page: easy at the top, hard at the bottom.
- Order: all `giveaway` (3-6), then `middle` (5-10), then `power` (8-14).
- `giveaway` = what appears in "For 10 points" lines. `middle` = after the power mark. `power` = before it.
- `t`: one short note (max ~30 words) with the key fact, written so a kid could copy it into a
  notebook. Must NOT contain the answer itself (the flashcard shows it as the question). Titles in _underscores_.
- `k`: 2-5 lowercase keywords or short phrases a kid would write in notes for this clue. At least one
  keyword of 4+ letters must appear word-for-word in `t` (it becomes the fill-in-the-blank). Never use
  words from the answer itself.
- `n`: how many of your sample's real tossups used this clue (0 if none). Be honest; the site shows
  "Stock · 5 of 8 real" badges from this.
- `rabbit` (optional): a related answer line worth studying next (e.g. "Anne Boleyn", "Joan of Arc").
- `id`: short kebab-case, unique in the topic (e.g. "act-of-supremacy").

**Buzzer Trap**: the single most likely way to lose this tossup.
- `title`: 2-5 words. `body`: 2-4 sentences on the confusion (namesakes, related answer lines,
  prompts, "do not accept" rules, early-buzz traps). `fix`: 1-3 sentences on how to tell them apart
  or what to say. `line`: "Real answer line: " + the answer line in HTML.

## Step 3. Videos and a reading link (verify every link)

`media` is a list of link objects, in the order a kid should use them:

```
{"group": "focus" | "background" | "read", "kind": "video" | "article", "title": "...", "source": "<channel or site>", "url": "...", "note": "<one short line, '<length> · <what it covers>'>"}
```

- **focus: 3 to 5 videos mainly ABOUT THIS EXACT TOPIC** (not just its era or field). The parent who
  runs this site insists on this. Shortest/easiest first; try to include one 1-6 minute video.
- **background: 0-2 optional** bigger-picture videos (the era, the whole field).
- **read: exactly 1** quick kid-friendly article: Ducksters, Britannica Kids, Kiddle, National
  Geographic Kids, BBC Bitesize, Khan Academy, NASA Space Place, Smarthistory, SparkNotes or LitCharts
  (literature), etc.
- Do not add the Wikipedia link to `media`; it goes in `wiki` and the app shows it automatically.

Good channels: TED-Ed, Crash Course (US History, European/World History, Literature, Philosophy,
Psychology, Economics, Sociology, Physics, Biology, Astronomy, Religions), PBS / PBS Learning, PBS Eons,
Smithsonian Channel, BBC Teach / Bitesize, Horrible Histories (official), Khan Academy, Smarthistory
(art and architecture), Amoeba Sisters (biology), SciShow / SciShow Kids, National Geographic, NASA,
Kurzgesagt, Veritasium, MinutePhysics, History Matters, Simple History, Extra History, OverSimplified,
Epic History, Kings and Generals, Biography (Mini Bio), HISTORY, Overly Sarcastic Productions
(mythology, literature), SparkNotes, museums and historic sites. Avoid tiny unknown channels,
unofficial re-uploads, AI-voiced slideshows, advocacy/proselytizing content, and anything graphic.

How to find and verify (the shell cannot reach YouTube):
1. Find candidates with **WebSearch** using `allowed_domains: ["youtube.com"]` (mode "standard").
2. Verify **every** video with WebFetch on
   `https://noembed.com/embed?url=https://www.youtube.com/watch?v=VIDEO_ID`
   (prompt: "Return the title and author_name fields exactly, or quote the error."). Keep it only if it
   returns a real title and channel you expect. Drop anything with an error.
3. Video URLs must be exactly `https://www.youtube.com/watch?v=VIDEO_ID` (11-character id; no
   shorts/, youtu.be, playlists, or timestamps).
4. Find the article with WebSearch (restrict to the site's domain) and use a URL from the results.
   Only WebFetch URLs that came from search results; fetching other URLs can hang on a permission check.
5. Notes: only state a length you actually saw; otherwise "Short", "Short clip", or no length.
   Mention "battle scenes" etc. when relevant.
Budget: about 6 searches and 8 verifications per topic. Don't chase perfection.

**If WebSearch is unavailable** (the session's search limit is used up), do not try to get around it
with other search engines or by fetching search-results pages. Instead:
- Reuse verified videos that already exist in other topic files when they are mainly about your topic
  (`grep -l <video id or keyword> topics/*.json`), and the list in
  `research/verified_videos.json` if it exists.
- Try videos you know exist on reputable channels (e.g. a TED-Ed, Crash Course, or Amoeba Sisters video
  on exactly this topic) and verify each with noembed as above; keep only exact matches.
- If you end up with fewer than 3 verified focus videos, keep what you have (even 0), add
  `"mediaPending": true` to the topic, and leave out the read link if you could not verify one. The
  site shows "more videos coming soon", and videos are added later. Never include an unverified link.

## Step 4. Assemble, validate, fix

Write each topic with a small Python script (safest for quotes and Unicode), e.g.
`work/<id>.py` that builds the dict and saves it with
`json.dump(data, f, ensure_ascii=False, indent=2)` to `topics/<id>.json`.
Then run:

    python3 validate.py --cross topics/<id>.json

Fix every `!!` error and every FAIL line, then run it again until it says `Errors: 0`. Read the `..`
warnings too (e.g. too few stock clues). Finally re-read your 15 tossups once for facts, giveaways
hidden in the power text, and answer leaks.

## Your final answer (keep it short)

One line per topic: `<id>: done | found <qb.found> | sample <n> | focus videos <k> | <anything the
reviewer should know, e.g. "only 2 real tossups, used Regular HS", "no Ducksters page, used Kiddle">`.
Do not paste the JSON.
