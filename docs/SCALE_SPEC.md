# Scaling the site from 215 to ~1,700 topics

The coach's study list grew from 215 topics in 11 areas to 1,708 topics in 16 areas
(`data/manifest.json`). New topic pages are being written in batches; until a topic's
`topics/<id>.json` exists it ships as an "upcoming" stub ("Coming soon"). Today `build.py` inlines
every built topic's full content into one HTML file. That file is 3.4 MB with 215 built topics and
would pass 25 MB with all 1,708, which is too heavy for phones and over the 16 MB limit of the
claude.ai copy of the site. This rework splits the content out and loads it on demand.

## What not to touch
Other agents are writing `topics/<id>.json` files right now. Do **not** edit anything in `topics/`,
`data/`, `research/`, `tools/curation.py`, `tools/extend_manifest.py`, `TOPIC_SPEC.md` or
`validate.py`. Keep `build.problems_in` working exactly as it does (the validator imports it). Do not
change `QBCore` (the answer checker at the top of `app/app.js`) except to call it. Do not commit or
push; the lead does that.

## Build output (what `python3 build.py` must produce)
1. `index.html` at the repo root (served by GitHub Pages) and `dist/quiz-bowl-lab.html` (the
   claude.ai artifact page: same content without doctype/charset/viewport, as today). Both hold the
   app (CSS + JS) and a **lean index** of all 1,708 topics, built or not: `id`, `name`, `category`,
   `order`, `aka` (other spellings from the manifest, for search), `built` (bool), and for built
   topics whatever the rail, Home, Topics page, Buzz/Flashcard pickers and My Stats need without the
   full content (e.g. `mono`, `kicker`, `freq`, clue/tossup counts, `mediaPending`). Keep the inline
   JSON small: target under ~600 KB for 1,708 topics.
2. `content/<area-slug>-<n>.json` at the repo root: the full built topics, grouped by area in display
   order, about 12 topics per chunk (make the size a constant). The index maps each built topic id to
   its chunk file. Put a short content hash in each chunk's file name (e.g.
   `content/biology-03.4f2a9c.json`) so a rebuilt chunk is never served stale from a browser cache;
   delete chunk files the build no longer references. Keep the total number of chunk files under 200
   (the claude.ai copy can publish at most 255 files at once).
3. Keep printing the summary line (`built topics: N / 1708, tossups: …`) plus the index size and
   chunk count. `--anki` behaviour unchanged.
4. Optional but useful: `dist/quiz-bowl-lab-offline.html` with all content inlined, for local
   testing; the loader uses inlined content when present instead of fetching.

## App changes (`app/app.js`, `app/style.css`)
- A small loader: `loadTopics(ids)` returns full topic objects, fetching only the chunks it needs,
  sharing in-flight requests and caching results in memory. Relative URLs only (the page must work
  both at the GitHub Pages address and inside the claude.ai artifact, where `content/…` files are
  published next to the page).
- Topic page (`#topic-<id>`): show a quiet loading state, then render. If a fetch fails, show a
  friendly "Couldn't load this topic — check your connection" message with a Retry button.
- Buzz Mode: pools can be large ("All topics" = 1,700). Pick the next question's topic from the pool,
  load just its chunk, render; prefetch the next one so play feels instant.
- Flashcards: single topics and small pools work as today. For big pools, build the deck from a
  random sample of topics (e.g. up to 20 topics per session) and load only those chunks. Say so in
  one short line under the deck ("A mix from 20 of your 450 topics — reshuffle for more").
- Topics page: must stay instant with 1,708 rows. Render area sections collapsed (header with
  counts, ready/coming-soon numbers, Select all / Clear) and fill rows only when a section is opened
  or a search is typed, the way the rail already defers its area bodies. Search matches name and
  `aka` with `QBCore.norm`. 16 area filter chips must wrap nicely on a 360 px phone.
- Rail, Home, My Stats: work from the lean index (no full content needed). A team study list can
  hold 450+ topics; the rail must stay usable (collapsed areas, counts).
- Everything else stays: saved progress (localStorage key `qblab.v1`) must load unchanged; backup /
  restore codes; no student names anywhere; no `alert/confirm/prompt`, no downloads; `esc()` for every
  inserted string; `try/catch` around storage; look and feel (tokens, fonts, light/dark, the mobile
  drawer at <= 900 px, 16 px gutters, no horizontal scroll at 360 px).

## How to test
- `python3 build.py && node --check app/app.js && python3 validate.py --cross` (validate must still
  end with `Errors: 0`).
- Chunk fetches don't work over `file://`, so serve the repo root: `python3 -m http.server 8765`
  (run it in the background from the repo root) and open `http://localhost:8765/index.html`.
- Screenshots with the local Playwright (write the script in your own scratch dir):
  `PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers NODE_PATH=$(npm root -g) node shot.js` at 1280x900 and
  390x844, light and dark. Visit `#home`, `#topics` (open an area, type a search like "kennedy"),
  `#topic-john-adams` (built), `#topic-california` (upcoming), `#buzz` (start a round from "All
  topics" and answer two questions), `#cards` (flip a card from a big pool), `#stats`. Add a team study
  list and toggle a topic. Collect `pageerror` and console errors (ignore Google Fonts network
  failures). Measure time to render `#topics` and the first Buzz question. Look at the screenshots
  with the Read tool and fix anything broken or ugly.
- Old saved state: before load, put this into localStorage `qblab.v1` (mirror the real saved-state
  shape from the code) and confirm progress survives:
  `{"v":1,"xp":120,"topics":{"john-adams":{"steps":{"learn":true},"notes":"Atlas of Independence","unlocked":true}}}`
- Simulate a failed chunk fetch (e.g. route `content/*` to abort in Playwright) and check the topic
  page shows the retry message instead of breaking.

## When done
Reply briefly: what changed, the index size and chunk count, timings you measured, how you tested,
anything left undone. Don't paste code.
