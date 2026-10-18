# Writing the new topics (expanded list, October 2026)

The site grew from 215 to 1,708 topics in 16 areas (`data/manifest.json`). You are writing some of
the 1,493 new ones. **Follow `TOPIC_SPEC.md` exactly**, with the changes and additions below. Where
this brief and the spec disagree, this brief wins.

## 1. Match the house style
Before writing, read `topics/john-adams.json` and `topics/jamestown.json`, plus the example(s) for your
area below. Match their tone, depth, length and format.

| Area | Also read |
| --- | --- |
| American History | `abraham-lincoln`, `trail-of-tears` |
| European History | `henry-viii`, `hundred-years-war` |
| Literature | `hamlet`, `the-great-gatsby` (works); for an author, follow `plato`'s person format with literature clues |
| Mythology | `odin`, `achilles` |
| Religion | `sikhism`, `moses` |
| Philosophy | `plato`, `existentialism` |
| Social Science | `sigmund-freud`, `inflation` |
| Fine Arts | `mona-lisa`, `the-thinker` (works); for an artist, follow `albert-einstein`'s person format with art clues |
| Music | `albert-einstein` (person format) and `the-night-watch` (how works are clued) |
| Physics, Chemistry, Astronomy, Math, Computer Science | `friction`, `albert-einstein`, `black-holes` |
| Biology, Earth Science | `mitochondria`, `photosynthesis`, `volcanoes` |

`qbCategory`: QBReader category · subcategory, e.g. `History · American History`,
`Literature · Classical Literature`, `Fine Arts · Auditory Fine Arts` (Music), `Science · Chemistry`,
`Science · Other Science (Astronomy)`, `Science · Other Science (Math)`,
`Science · Other Science (Computer Science)`, `Social Science · Psychology`.

## 2. No videos or links this round
Do **not** use WebSearch (the session's search allowance is saved for a later video pass). Set
`"mediaPending": true` and `"media": []`. Videos and the reading link are added later. Never add an
unverified link.

## 3. QBReader research (your prompt says which mode you are in)
- **QBReader ON:** use Step 1 of the spec with the path spellings you are given (one per request, in
  order, never plain `api/query`). If a request fails twice in a row with a permission/provenance
  error or a timeout, switch to OFF for the rest of your batch.
- **QBReader OFF:** do not call WebFetch or WebSearch at all (each blocked request pops up a
  permission prompt for the parent). Use the spec's fallback: write from your own solid knowledge of
  how quiz bowl clues this answer line at the Middle School / Easy High School level (stock clues
  first in the giveaway/middle tiers, deeper but still learnable facts as power clues); `qb.found` 0,
  `sample.n` 0, every clue `n` 0, `sample.note` = "no real tossups checked yet", and `qb.tip` =
  "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
  Keep `qb.q` = the query string a kid should type.

## 4. Accuracy, dates, living people
- Kids memorize every clue. Only state facts you are certain of; when unsure, leave it out. No
  invented quotes, numbers or dates.
- Facts are as of mid-2025 at the latest. For living people and recent events never write
  "currently", "now", "today", "the current", "most recent" or "latest"; give roles with dates
  ("Speaker of the House from 2007 to 2011 and 2019 to 2023").
- Two 2025 renamings: by a 2025 executive order the U.S. government calls Denali "Mount McKinley"
  and the Gulf of Mexico the "Gulf of America". Mention neutrally only if relevant, and accept both
  names on the answer line.

## 5. Neutral on politics
Politicians, parties, elections and court cases on contested issues (e.g. Roe v. Wade, Same-sex
marriage, Affirmative action, the Affordable Care Act, Don't Ask, Don't Tell, Second Amendment):
write like a civics textbook. Who, what, when, the legal question and the outcome; no praise or
blame words, no opinions, no predictions. If sides are described, describe them evenly.

## 6. Age-appropriate (11–12-year-olds)
The spec's rules apply (factual, classroom-level, nothing graphic). In particular:
- **Violence and tragedy** (attacks, shootings, massacres, assassinations, the Holocaust, internment,
  the KKK, Jim Crow, disasters, the Donner Party, slave rebellions): state what happened plainly and
  respectfully; no descriptions of wounds, gore, or methods. The Donner Party's survival by
  cannibalism may be stated once, plainly, without detail.
- **Gangsters and outlaws**: what they did and how they were caught, without glamorizing.
- **Mature literature** (e.g. A Clockwork Orange, Death in Venice, The Color Purple, The Handmaid's
  Tale, Tess of the d'Urbervilles, Lysistrata, Satyricon, The Golden Ass, Catullus, Sappho, To His Coy
  Mistress, The Bell Jar, Madame Bovary, Anna Karenina): clue it the way a classroom would — author,
  characters, setting, structure, famous non-explicit lines, themes named plainly ("deals with abuse").
  No sexual content, no violent detail, no explicit quotations. (Lysistrata: the women "go on strike"
  to force the men to end the war. Death in Venice: Aschenbach's artistic crisis, Venice, the cholera
  outbreak, and the boy Tadzio only as an ideal of beauty he watches from afar.)
- **Myths**: plain statements are fine ("Cronus swallowed his children", "Medea killed her children
  for revenge"); no sexual detail (say "fell in love with", "carried off").
- **Health and the body** (autism, Down syndrome, schizophrenia, Alzheimer's, HIV, cancer, diabetes,
  testosterone, placenta, etc.): accurate, respectful, person-first, no stigma, no medical advice;
  autism described as a developmental difference across a spectrum. Reproduction-related biology at
  textbook level only.
- **Religions** (e.g. Scientology): neutral and factual ("adherents believe…"); no ridicule.
- **Alcohols (chemistry)**: chemistry only. **Tobacco**: history of the cash crop.

## 7. Answer lines across 1,708 topics
`python3 validate.py --cross topics/<id>.json` now checks your answer line against all 1,708 topic
names (built or not). Add near-misses to `reject` (e.g. "Venus (planet)" must reject
"birth of venus"; "Electric field" must reject "magnetic field"). If your topic genuinely shares one
real answer line with another topic (e.g. the history topic "Republic of Ireland" and the existing
mythology topic "Ireland" are both answered "Ireland"), don't contort it: say so in your final
report and the lead will record the exception. A topic's manifest name must itself be judged right
(e.g. "Venus (planet)" → accept "venus").

## 8. Concept topics
Never use the answer word (or its plural/singular) anywhere in the tossups or clue text; the
validator checks phrases of 4+ letters, so check short answers (pH, ATP, RNA, CPU, Pi, Set, Pan, Ra)
by eye. Accept both singular and plural forms.

## 9. Monograms and house conventions
- Choose a distinctive 1–3 character `mono`; the lead resolves duplicates across 1,708 topics later.
- Site-wide conventions: BCE/CE (never BC/AD); kicker ≤ ~80 characters, two parts joined by " · "
  with a capital letter after the dot; Buzzer Trap title 2–5 words; titles of books, plays, long
  poems, albums, paintings and ships in `_underscores_`; short poems, stories, songs and essays in
  “curly quotes”; at least 20 clues; at least 8 answer-checker tests.

## 10. Your files only
Write each topic with `work/<id>.py` → `topics/<id>.json`. Don't edit any other file (not the app,
build, validator, manifest, spec, briefs or other topics). Don't run git commands.
