# Content review brief (shared by all reviewer agents)

You are an independent reviewer for a real Quiz Bowl study site at ., built by a parent for
his 6th-grade son's team (readers are 11-12 years old). All 215 topics are written; other agents wrote them.
The parent asked for a review "to make sure everything was captured and is consistent". You review one
content area (your assignment lists the topic ids). Each topic is topics/<id>.json.
Schema and rules: TOPIC_SPEC.md (read Steps 2 and 4 and the tossup/clue rules).

## What you may and may not change
- You MAY edit, in your own topics only: tossups (p/r), clues, briefing, kicker, dates, trap, accept/prompt/
  reject, answerHtml, tests, qb.tip, sample.note, wiki (only if the link is plainly wrong).
- You must NOT touch: id, name, category, qbCategory, mono, media, mediaPending, qb.found, sample.n, or any
  file outside your assignment. Never edit app/, build.py, validate.py, tools/, data/.
- Edit with a small Python script that loads the JSON, changes only the specific strings, and saves with
  json.dump(data, f, ensure_ascii=False, indent=2) plus a trailing newline. Never retype a whole file.
- Make surgical fixes. Don't rewrite things that are already fine, and don't restyle good writing.

## What to check, topic by topic (read every tossup and clue)
1. Facts. Every date, name, number, title, quote and attribution in the tossups, clues, briefing, kicker,
   dates and trap. Fix anything you are confident is wrong. If you're unsure, either remove/soften that one
   claim or leave it and flag it — never replace it with another guess. You may WebFetch the topic's own
   Wikipedia page (its "wiki" field) to settle a doubt, but at most 5 fetches in total: the session shares a
   limited page-fetch budget.
2. Internal consistency. The same fact must be stated the same way across briefing, kicker, dates, tossups,
   clues and trap (e.g. a year in a clue vs. a tossup).
3. Consistency across topics. Topics in your area overlap (e.g. Napoleon and Waterloo). Make sure shared facts
   agree. work/cross_area_links.json lists topics in OTHER areas whose names appear in
   yours (ignore obvious false positives such as "heart" used as an ordinary word); spot-check that shared
   facts agree with those files too (read them; don't edit them — flag a conflict in your report instead).
4. Answer lines. accept/prompt/reject should match the answerHtml and the trap's "Real answer line". Nothing in
   accept should give credit for a different topic's answer. Known judge pitfall: a bare short word in
   "reject" that is also inside one of your own accept phrases breaks typo-tolerance (reject-containment is
   checked first) — put such words in "prompt" or leave them out.
5. Tossup craft. Power text (p) holds harder clues; the giveaway is at the end of r; r contains exactly
   "For 10 points"; no answer leak (the validator checks); pyramidal order makes sense.
6. Age-appropriateness for 11-year-olds: no graphic violence or sexual content; mature literary/historical
   themes at a classroom level. Fix anything that crosses the line.
7. Consistency polish (apply to every topic in your area):
   - Buzzer Trap title: 2-5 words is the house style (6 at most). Shorten longer ones, keeping the meaning.
   - Briefing: 2-3 sentences, 35-90 words.
   - At least 20 clues and at least 3 answer-checker tests per topic. If a topic has 19 clues, add one
     accurate clue (choose its tier so tier limits still hold: giveaway 3-6, middle 5-11, power 8-15; give
     it a kebab-case id, lowercase cloze keywords "k" that appear in the text, and n = 0 unless real tossups
     use it). If a topic has only 2 tests, add one (copy the shape of the existing tests, e.g. a sensible
     misspelling that should be accepted, or a near-miss that should be rejected) and make sure
     node tools/judge_check.js passes.
   - Curly quotes “ ” ‘ ’ in text, never straight double quotes.

## Validate after every edited file
    cd . && python3 validate.py --cross topics/<id>.json
Fix every "!!" error and FAIL line until it says Errors: 0. At the end, run it once on all your files
together.

## Report (keep it short)
One line per topic: "<id>: ok" or "<id>: fixed — <what changed, briefly>". Then a "Flagged for the parent"
list with anything you were unsure about or conflicts you found in other areas' files (file + what). Then a
final line with how many tossups/clues you changed in total.
