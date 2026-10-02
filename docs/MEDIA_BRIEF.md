# Video + read-link backfill brief (shared by all media agents)

You are filling in missing study videos for a real Quiz Bowl study site at ., built by a
parent for his 6th-grade son's team (11-12 year olds). 215 topics are written; your assigned topics are
missing their verified videos and/or their kid-friendly read link. Content (tossups, clues) is NOT your job
and other agents are editing it right now — so you must NEVER write to topics/.
You only READ topics/<id>.json and WRITE work/media/<id>.json.

## Read first
- TOPIC_SPEC.md, the section "Step 3. Videos and a reading link" (rules, good channels,
  how to verify). Those rules apply, with the changes below.
- A finished example of the house style: the "media" list in topics/george-washington.json
  and topics/martin-luther.json.

## Output: one file per topic, work/media/<id>.json
{"id": "<id>", "media": [ ...the COMPLETE final list... ], "mediaPending": false, "report": "<one line>"}
- Start from the topic's CURRENT media in topics/<id>.json: keep every existing item (they were verified
  earlier) unless it breaks a rule, and add what is missing. Order: focus videos (shortest/easiest first),
  then 0-2 background videos, then exactly 1 read article last.
- Each item: {"group": "focus"|"background"|"read", "kind": "video"|"article", "title": "<real title as
  noembed returned it, lightly cleaned>", "source": "<channel or site name>", "url": "...", "note": "<one short
  line: '<length> · <what it covers>'>"}. You cannot see video lengths (noembed has none), so only give a
  length if a search result title states it; otherwise just say what it covers, e.g. "Animated retelling of
  the twelve labors". Use curly quotes “ ” ’ in titles/notes, never straight double quotes.
- mediaPending is false only when you have 3-5 focus videos AND 1 read link; otherwise true (keep what you
  verified, even if 0-2 videos).
- Check every file:  python3 tools/check_media.py work/media/<id>.json
  Fix every "!!" line until it says Errors: 0. Read the ".." warnings (a video reused from another topic is
  fine only if it is MAINLY about your topic too).

## Finding videos — STRICT SEARCH BUDGET
WebSearch was just renewed for this session and is shared by ~15 agents working at once. Your hard cap is
given in your assignment (about one search per topic). Do not exceed it. Spend it well:
- Always use WebSearch with allowed_domains: ["youtube.com"] and mode "standard". That returns ~9 YouTube
  links per query. A good query names the topic plus a strong channel, e.g. "Hamlet TED-Ed Crash Course",
  "Mona Lisa Smarthistory", "volcanoes National Geographic SciShow". Ignore playlist/channel links.
- One series-level query can serve several of your topics at once (e.g. "TED-Ed why should you read",
  "Crash Course Philosophy", "Amoeba Sisters cell organelles", "Smarthistory Renaissance painting"). Do a
  couple of these first, then spend the rest per topic on whatever is still missing.
- Before searching for a topic, grep for reusable verified videos: other topics/*.json files and
  research/verified_videos.json (only reuse when the video is mainly about YOUR topic).
- If WebSearch starts failing (limit used up), stop searching, finish with what you verified, and set
  mediaPending true where you are short. Never search through other engines or fetch search-result pages.

## Verifying — every single video
WebFetch https://noembed.com/embed?url=https://www.youtube.com/watch?v=VIDEO_ID with the prompt
"Return the title and author_name fields exactly, or quote the error." Keep a video only if noembed returns
a real title and a channel you'd trust. Never WebFetch youtube.com pages themselves (YouTube rate-limits the
fetch service). If a noembed call errors or rate-limits, don't hammer it — move on and retry that one later
once. Video urls must be exactly https://www.youtube.com/watch?v=ID (11-char id; no shorts/, youtu.be,
playlists, &t=, &list=). Avoid YouTube Shorts entirely.

## Choosing videos (the parent is strict about this)
- focus = 3-5 videos MAINLY ABOUT THIS EXACT TOPIC, not just its era/field/author. A video about Picasso's
  whole career is background for Guernica, not focus. Try to include one short (1-6 min) video.
- Trustworthy educational channels only (TED-Ed, Crash Course, Smarthistory, Khan Academy, PBS, Amoeba
  Sisters, SciShow/SciShow Kids, National Geographic, NASA, Kurzgesagt, Overly Sarcastic Productions,
  SparkNotes, BBC, museums, historic sites, the channels listed in TOPIC_SPEC.md). No tiny unknown channels,
  unofficial re-uploads, AI-voiced slideshows, movie clips/trailers, advocacy, or proselytizing.
- Age-appropriate for an 11-year-old: no graphic violence/gore, nothing sexual. For mature literature or
  dark history, prefer plot-summary/analysis channels that handle it at a classroom level, and say in the
  note if a video has battle scenes or mature themes.

## Read link (exactly 1) — prefer NOT to spend searches on it
Use, in this order of preference: Ducksters, Britannica Kids, Kiddle, National Geographic Kids, NASA Space
Place, BBC Bitesize, Smarthistory (art), SparkNotes or LitCharts (literature). These match the 64 finished
topics. You may WebFetch a page on these sites directly to verify it (e.g. Kiddle mirrors Wikipedia titles:
https://kids.kiddle.co/<Wikipedia_Title> — take the title from the topic's "wiki" field; SparkNotes:
https://www.sparknotes.com/lit/<slug>/ ; LitCharts: https://www.litcharts.com/lit/<slug> ; Ducksters has
subject index pages you can fetch to find the right article). Keep it only if the fetched page is really
about the topic and readable by a kid. Source names exactly: "Ducksters", "Britannica Kids", "Kiddle",
"National Geographic Kids", "NASA Space Place", "BBC Bitesize", "Smarthistory", "SparkNotes", "LitCharts".
If a domain hangs or errors, try another site rather than retrying.

## When done
Reply with one line per topic and nothing else:
<id>: focus <k> | background <b> | read <source or none> | pending <true/false> | <anything worth knowing>
then a last line: "searches used: N of CAP".
