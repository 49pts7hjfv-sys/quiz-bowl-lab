# Review brief for the new topics (expanded list, October 2026)

You are an independent reviewer for a real quiz bowl study site built by a parent for his 6th-grade
son's team (readers are 11–12 years old). Other agents just wrote the topics assigned to you, from
their own knowledge (QBReader was not reachable, so every clue's `n` is 0 and `qb.found` is 0 — that
is expected; leave those fields alone). Kids will memorize every clue, so your job is to catch
anything wrong before they do. Schema and rules: `TOPIC_SPEC.md` (Steps 2 and 4) and
`docs/NEW_TOPICS_BRIEF.md` (house conventions, neutrality, age-appropriateness).

## What you may and may not change
- You MAY edit, in your assigned topics only: tossups (p/r), clues, briefing, kicker, dates, trap,
  accept/prompt/reject, answerHtml, tests, qb.tip, qb.q, mono.
- You must NOT touch: id, name, category, qbCategory, media, mediaPending, qb.found, sample, or any
  file outside your assignment (never the 215 original topics, app/, build.py, validate.py, tools/,
  data/, docs/). No git commands. No web calls of any kind (no WebFetch, no WebSearch).
- Edit with a small Python script that loads the JSON, changes only the specific strings, and saves
  with `json.dump(data, f, ensure_ascii=False, indent=2)` plus a trailing newline. Never retype a whole
  file. Make surgical fixes; don't restyle good writing.

## What to check, topic by topic (read every tossup and every clue)
1. **Facts.** Every date, name, number, title, quote, attribution and "first/only/largest" claim in
   the tossups, clues, briefing, kicker, dates and trap. Fix what you are confident is wrong. If you
   are unsure of a claim, remove or soften that one claim — never replace it with another guess.
   Watch especially for: invented-sounding quotes, precise numbers (populations, distances, counts of
   moons/works/years), "the first to…" claims, and mixed-up people with similar names.
2. **Internal consistency.** The same fact stated the same way everywhere in the topic.
3. **Consistency across topics.** Topics in your area overlap; shared facts must agree. Spot-check
   related topics elsewhere (grep `topics/*.json` for a name) and flag conflicts with files you don't
   own in your report rather than editing them.
4. **Answer lines.** accept/prompt/reject match answerHtml and the trap's "Real answer line"; nothing
   accepted gives credit for a different topic. Known judge pitfall: a bare short word in `reject` that
   is also inside one of your own accept phrases breaks typo tolerance — put it in `prompt` or leave it
   out.
5. **Tossup craft.** Hardest clue first, giveaway last; the power part holds harder clues; `r`
   contains exactly "For 10 points"; no answer leaks (check 2–3-letter answers by eye); clues are
   learnable at Middle School / Easy High School level — replace truly obscure trivia with a solid,
   commonly asked fact, or delete it.
6. **Age-appropriateness and neutrality** per `docs/NEW_TOPICS_BRIEF.md` sections 5–6. Fix anything
   graphic, sexual, sensational, or one-sided. No "currently/now/today" claims about living people or
   recent events.
7. **Polish.** BCE/CE (never BC/AD); kicker ≤ ~80 characters with a capital after " · "; Buzzer Trap
   title 2–5 words; briefing 2–3 sentences, 35–90 words; titles in `_underscores_`, short works in
   “curly quotes”; no straight double quotes; at least 20 clues and 8 answer-checker tests.

## Validate after every edited file
    python3 validate.py --cross topics/<id>.json
Fix every `!!` error and FAIL line until it says `Errors: 0`. At the end, run it once on all your
files together.

## Report (keep it short)
One line per topic: `<id>: ok` or `<id>: fixed — <what changed, briefly>`. Then a "Flagged" list
(anything you were unsure about, or conflicts with files you don't own: file + what). Then one line
with how many tossups/clues you changed in total.
