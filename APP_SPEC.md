# App rework: from one student's site to the whole team's site

The Quiz Bowl Lab is a single-page study app (vanilla JS, no frameworks) built by `build.py` into
`dist/quiz-bowl-lab-offline.html` (full document) and `dist/quiz-bowl-lab.html` (published as a
claude.ai artifact). Code: `app/app.js` (QBCore helpers at the top, then the app IIFE),
`app/style.css`. Topic content lives in `topics/<id>.json` and `data/manifest.json`; other agents are
writing new topic files right now, so **do not edit anything in `topics/`, `data/`, `tools/`,
`validate.py`, or `TOPIC_SPEC.md`**, and do not change `QBCore` (answer checking) except to call it.

It started as one 6th grader's site with 5 topics. It is becoming the whole team's site: 215 topics in
11 content areas, built up over time. Different students are assigned different topics. The parent who
runs it wants: **no student names anywhere on the site**, and every student can **pick their own
topics**.

## Data you get (already produced by build.py)
`DATA = JSON.parse(#qb-data)` now has:
- `topics`: the built topics (full content), already in display order, each with `category` and `order`.
- `upcoming`: stubs `{id, name, category, order}` for topics not written yet ("coming soon").
- `areas`: `[{name, qb, short, count}]` in display order (American History, European History,
  Literature, Mythology, Religion, Philosophy, Social Science, Fine Arts, Physics, Biology, Earth Science).
- `lists`: anonymous team study lists `[{n, label, ids}]`, e.g. `{n: 1, label: "American History (20) + Religion (20)", ids: [...]}`.
  Each matches one student's assignment, described only by its contents.
- `built`: build date.
Older fields like `batch` may be missing; don't show "Batch N" anywhere.

## Requirements
1. **No names.** Remove every student's name (UI text, home eyebrow, comments). Brand = "Quiz Bowl Lab".
2. **My topics.** New saved field `S.my` (array of topic ids, may include upcoming ids). Saved progress
   from the current version (localStorage key `qblab.v1`) must keep working: add new fields with defaults,
   never reset existing progress. Include `my` in the backup/restore code.
3. **Topics page** (`#topics`), one page for picking and browsing:
   - "Team study lists": a card per list ("List 3", its label, topic count, how many are ready) with an
     "Add to my topics" button (adds; never silently replaces). A "Clear my topics" button that needs a
     second tap to confirm (inline, no browser dialogs).
   - Search box (match with `QBCore.norm`) and area filter chips.
   - All 215 topics grouped by area. Each row: a checkbox/toggle for My topics, the monogram, the name
     (a link to the topic page if built), and status: progress for built topics, "Coming soon" for
     upcoming ones. Per-area "Select all" / "Clear". A live count of selected topics.
4. **Rail (sidebar)** must stay usable with 200+ topics: nav (Home, Topics, Buzz Mode, Flashcards, My
   Stats) then My topics grouped by area with collapsible area headers (`aria-expanded`, counts, remember
   which are open in `S.ui`). If My topics is empty, show a short "Pick your topics" button and the
   areas collapsed (all topics inside). Upcoming topics appear dimmed with a "Soon" tag and are not links.
   The area of the topic being viewed is open.
5. **Home**: if My topics is empty, a clear first step: "Pick your topics" (link to `#topics`, mention
   the team study lists). "Up next" = the first built topic in My topics (or all topics if empty) that
   isn't unlocked yet. Then My topics as cards by area (upcoming cards dimmed, "Coming soon"). Keep
   Coach's routine, the mode tiles, and an updated fine print (counts of built topics/tossups, build date).
6. **Topic page**: eyebrow shows `category · qbCategory` (no batch). Add a toggle button "+ My topics" /
   "✓ In my topics". A route to an upcoming topic (`#topic-<id>`) shows a friendly "Coming soon" page.
7. **Buzz Mode and Flashcards** pools: `<select>` with "My topics (mixed)" (default when My topics has
   built topics), "All topics (mixed)", one "All <Area> (mixed)" per area that has built topics, then
   single topics in `<optgroup label="<Area>">` groups. Store values like `my`, `all`, `area:<name>`,
   `<id>`; validate stored values on load. Flashcards' "Auto" card type: name-it for multi-topic decks,
   fill-in for single topics.
8. **My Stats**: group by area; show My topics first (or all built topics if none chosen).
9. Keep the look and feel (tokens, fonts, light/dark, mobile drawer at <=900px, 16px gutters, no
   horizontal scroll at 360px). No `alert/confirm/prompt`, no downloads, no `print()`. Use the existing
   `data-act` event delegation, `esc()` for every inserted string, and `try/catch` around storage.
10. Performance: rendering the rail or Topics page with 215 rows must feel instant.
11. **Frequency list.** Some topics will carry `freq: {rank, count, list}` (from QBReader's frequency list,
    Middle School + Easy High School). When present, show it in the topic's QBReader section, e.g.
    “#6 on QBReader’s European History frequency list · 7 tossups (Middle School + Easy High School)”,
    and on the Topics page rows as a small “#6” badge. Absent = show nothing.

## How to test
- `cd . && python3 build.py && node --check app/app.js`
  (build.py skips topic files that are mid-write or invalid; that's expected while others work).
- Answer checker: `node tools/judge_check.js topics/george-washington.json topics/john-adams.json`.
- Screenshots with the local Playwright (the Playwright MCP tool can't open local files):
  write a script in your scratch dir and run
  `PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers NODE_PATH=$(npm root -g) node shot.js`, opening
  `file://dist/quiz-bowl-lab-offline.html#home` (and `#topics`, `#topic-john-adams`,
  `#topic-<an upcoming id>`, `#buzz`, `#cards`, `#stats`) at 1280x900 and 390x844, light and dark
  (`colorScheme`). Click through: add a team list, toggle a topic, collapse an area, start a Buzz round
  from "My topics", flip a flashcard. Collect `pageerror` and console errors (ignore Google Fonts
  network failures). Look at the screenshots with the Read tool and fix anything ugly or broken.
- Also simulate an old saved state: before load, put this in localStorage key `qblab.v1`
  (`page.addInitScript`) and confirm the page loads with that progress intact:
  `{"v":1,"xp":120,"topics":{"john-adams":{"steps":{"learn":true},"notes":"Atlas of Independence","unlocked":true}}}`
  (read the current code first to see the real saved-state shape and mirror it).

## When done
Reply with a short summary: what changed, how you tested, anything left undone. Don't paste code.
