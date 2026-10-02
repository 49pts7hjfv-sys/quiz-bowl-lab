# Build log

## Status (2026-10-02)
- **Content:** 215 / 215 topics, 3,225 tossups, 4,859 clues. `validate.py --cross`: 0 errors.
- **Independent review:** every tossup and clue was re-read by reviewers who hadn't written them; 183 topics
  received fixes (about 1,400 substantive corrections: event order, attributions, dates, numbers, science,
  answer leaks, answer-checker bugs) plus style cleanup.
- **Videos:** 186 / 215 topics have 3–5 verified focus videos and a reading link. Every topic has a reading
  link. 29 topics are still short and show "more videos coming soon" (`"mediaPending": true`):
  - Literature: Les Misérables, Moby-Dick, The Adventures of Tom Sawyer, The Red Badge of Courage,
    The Waste Land, Ulysses
  - Mythology: Horus, Perseus, Quetzalcoatl, Ra, Shiva
  - Fine Arts: Fallingwater, Guernica, Nighthawks, St. Paul's Cathedral, The Birth of Venus,
    The Persistence of Memory
  - Philosophy: René Descartes, Socrates, The Prince · Social Science: Adam Smith, Anthropology,
    Margaret Mead
  - Biology: Cell wall, Nucleus, Ribosomes · Earth Science: Limestone, Quartz · Religion: Rastafarianism
- **Frequency ranks:** 195 topics show "#N on QBReader's <Area> frequency list" (lists in `research/freq/`,
  matched by `tools/freq_match.py`; ties share a rank). The other 20 aren't on their area's MS/EHS list.

## Rules the content follows
1. Original writing, fact-checked against real QBReader tossups; never copied.
2. Every tossup is power-marked with "For 10 points" in the giveaway and stays within `validate.py` limits.
3. Focus videos (3–5) must be mainly about the exact topic, from trustworthy educational channels, verified
   through noembed; exactly one kid-friendly reading link. Otherwise `"mediaPending": true` — never an
   unverified link.
4. No student names anywhere. No Anki output unless asked.
5. Sensitive history, religion, literature and science: factual, classroom-level, nothing graphic; living
   religions described neutrally ("adherents believe…").
6. Concept topics never use their own answer word in their own tossups or clues (the validator checks
   answers of 4+ letters; check short answers like DNA or Ra by hand).

## Workflow
- Topic ids and order come from `data/manifest.json`.
- Edit topics → `python3 validate.py --cross` → `python3 build.py` → commit and push.
- Video backfill: agents write `work/media/<id>.json`, check with `tools/check_media.py`, merge with
  `tools/merge_media.py`, so they never collide with content edits. Brief: `docs/MEDIA_BRIEF.md`.
- Content review brief: `docs/REVIEW_BRIEF.md`.
- QBReader's API: `/api/query` for tossups, `/api/frequency-list` for frequency lists (WebFetch only; the
  shell can't reach qbreader.org).
