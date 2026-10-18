/* ===== QBCORE: pure helpers (no DOM). Kept separate so they can be tested on their own. ===== */
const QBCore = (() => {
  const norm = s => String(s == null ? '' : s).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '')
    .replace(/&/g, ' and ').replace(/[’'`]/g, '').replace(/[^a-z0-9$]+/g, ' ').trim().replace(/\s+/g, ' ');

  const lev = (a, b) => {
    if (a === b) return 0;
    const m = a.length, n = b.length;
    if (!m) return n; if (!n) return m;
    let prev = new Array(n + 1), cur = new Array(n + 1);
    for (let j = 0; j <= n; j++) prev[j] = j;
    for (let i = 1; i <= m; i++) {
      cur[0] = i;
      for (let j = 1; j <= n; j++) {
        const cost = a.charCodeAt(i - 1) === b.charCodeAt(j - 1) ? 0 : 1;
        cur[j] = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + cost);
      }
      [prev, cur] = [cur, prev];
    }
    return prev[n];
  };

  // How many typos we forgive, by length of the official answer.
  const tol = len => (len <= 4 ? 0 : len <= 7 ? 1 : len <= 12 ? 2 : 3);
  const TITLES = /^(?:(?:the|a|an|president|pres|general|gen|captain|capt|admiral|mr|mrs|ms|dr|doctor|sir|dame|lady|lord|king|queen|emperor|empress|prince|princess|archduke|duke|kaiser|tsar|czar|chancellor|pope|saint|st|prophet|chief)\s+)+/;
  const hasPhrase = (hay, needle) => (' ' + hay + ' ').includes(' ' + needle + ' ');
  const LISTS = new WeakMap();
  const lists = topic => {
    let L = LISTS.get(topic);
    if (!L) { L = { acc: topic.accept.map(norm), pr: topic.prompt.map(norm), rej: topic.reject.map(norm) }; LISTS.set(topic, L); }
    return L;
  };

  // One pass over a normalized answer. `hard` marks an explicit do-not-accept match.
  function verdict(a, { acc, pr, rej }) {
    if (rej.includes(a)) return { kind: 'wrong', hard: true };
    if (acc.includes(a)) return { kind: 'right' };
    if (pr.includes(a)) return { kind: 'prompt' };
    if (rej.some(r => r.length > 3 && hasPhrase(a, r))) return { kind: 'wrong', hard: true };
    if (acc.some(x => x.length > 3 && hasPhrase(a, x))) return { kind: 'right' };
    let best = null;
    const consider = (list, kind) => list.forEach(x => {
      const t = tol(x.length);
      if (!t || Math.abs(x.length - a.length) > t) return;
      const d = lev(a, x);
      if (d <= t && (!best || d < best.d)) best = { d, kind };
    });
    consider(rej, 'wrong'); consider(acc, 'right'); consider(pr, 'prompt');
    return best ? { kind: best.kind, hard: best.kind === 'wrong' } : { kind: 'wrong' };
  }
  const RANK = { wrong: 0, prompt: 1, right: 2 };

  // Returns 'right', 'prompt', or 'wrong' for an answer typed against one answer line.
  // The answer is checked as typed and again without a leading title ("King", "Saint", "the"...).
  function judge(input, topic) {
    const raw = norm(input);
    if (!raw) return 'wrong';
    const L = lists(topic), a = verdict(raw, L);
    if (a.hard) return 'wrong';
    const bare = raw.replace(TITLES, '').trim();
    if (!bare || bare === raw) return a.kind;
    const b = verdict(bare, L);
    if (b.hard) return a.kind === 'right' ? 'right' : 'wrong';
    return RANK[a.kind] >= RANK[b.kind] ? a.kind : b.kind;
  }

  // Strip pronunciation guides and italics markers for reading aloud / word-by-word display.
  const plain = s => String(s).replace(/\s*\[“[^”]*”\]/g, '').replace(/_/g, '');
  const words = s => plain(s).split(/\s+/).filter(Boolean);

  // Fill-in-the-blank: hide the longest note keyword that appears in the clue text.
  function cloze(clue) {
    const text = clue.t.replace(/_/g, '');
    let best = null;
    for (const k of clue.k) {
      if (k.length < 4) continue;
      const re = new RegExp('(^|[^A-Za-z0-9])(' + k.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')(?![A-Za-z0-9])', 'i');
      const m = re.exec(text);
      if (m && (!best || m[2].length > best.term.length)) best = { index: m.index + m[1].length, term: m[2] };
    }
    if (!best) return null;
    return { before: text.slice(0, best.index), term: best.term, after: text.slice(best.index + best.term.length) };
  }

  // Which clues from the breakdown appear in a player's notes.
  function catches(notes, topic) {
    const N = ' ' + norm(notes) + ' ';
    return topic.clues.filter(c => c.k.some(k => { const nk = norm(k); return nk && N.includes(nk); })).map(c => c.id);
  }

  return { norm, lev, judge, plain, words, cloze, catches };
})();
/* ===== END QBCORE ===== */

(() => {
  'use strict';
  const { norm, judge, plain, words, cloze, catches } = QBCore;

  /* ---------- data: a lean index of every topic (full topics load on demand, see the loader) ---------- */
  const DATA = JSON.parse(document.getElementById('qb-data').textContent);
  const AREAS = DATA.areas || [];
  const CHUNKS = DATA.chunks || [];
  const SHORT_BY_AREA = Object.fromEntries(AREAS.map(a => [a.name, a.short || a.name]));
  // A short monogram for a topic that has none yet (upcoming stubs don't carry one).
  const STOPWORDS = new Set(['the', 'a', 'an', 'of', 'and']);
  function genMono(name) {
    const ws = String(name).replace(/[^\w\s'-]/g, '').split(/\s+/).filter(w => w && !STOPWORDS.has(w.toLowerCase()));
    const pick = (ws.length ? ws : String(name).split(/\s+/)).slice(0, 2);
    return (pick.map(w => w[0]).join('').toUpperCase() || '?').slice(0, 3);
  }
  // One light entry per topic, built or coming soon, in display order (area, then the coach's order).
  // Built entries carry what lists, pickers and stats show; the full topic comes from loadTopics().
  const ENTRIES = (DATA.topics || []).map(r => {
    const built = !!r.built && Number.isInteger(r.chunk) && r.chunk >= 0 && r.chunk < CHUNKS.length;
    return {
      id: String(r.id), name: String(r.name), category: r.category, order: r.order, aka: Array.isArray(r.aka) ? r.aka : [],
      built, mono: r.mono || genMono(r.name), kicker: r.kicker || '', clues: r.clues || 0, tossups: built ? r.tossups || 0 : 0,
      freq: Array.isArray(r.freq) ? { rank: r.freq[0], count: r.freq[1], list: r.freq[2] || r.category } : null,
      chunk: built ? r.chunk : -1, mediaPending: !!r.mediaPending
    };
  });
  const ENTRY_BY_ID = Object.fromEntries(ENTRIES.map(e => [e.id, e]));
  const BY_AREA = {}, BUILT_BY_AREA = {};
  AREAS.forEach(a => { BY_AREA[a.name] = []; BUILT_BY_AREA[a.name] = []; });
  ENTRIES.forEach(e => { if (BY_AREA[e.category]) { BY_AREA[e.category].push(e); if (e.built) BUILT_BY_AREA[e.category].push(e); } });
  const BUILT = ENTRIES.filter(e => e.built);
  const BUILT_AREAS = AREAS.map(a => a.name).filter(name => BUILT_BY_AREA[name].length > 0);
  const LISTS = (DATA.lists || []).map(l => ({ n: l.n, label: l.label, ids: (l.ix || []).map(i => ENTRIES[i] && ENTRIES[i].id).filter(Boolean) }));
  const TOTAL_TOSSUPS = BUILT.reduce((n, e) => n + e.tossups, 0);
  const TIER = {
    giveaway: { label: 'Giveaway (Easy)', short: 'Giveaway', blurb: 'the “For 10 points” clues at the very end' },
    middle: { label: 'Middle clues (10 points)', short: '10-point', blurb: 'after the power mark, before the giveaway' },
    power: { label: 'Power clues (Hard)', short: 'Power', blurb: 'bold text before the (*), worth 15' }
  };
  const TIER_ORDER = ['giveaway', 'middle', 'power'];
  const STEPS = [
    ['learn', 'Learn', 'Read the briefing and watch or read one link'],
    ['search', 'Search', 'Run Coach’s QBReader search'],
    ['read', 'Read', 'Read the 15 practice tossups'],
    ['notes', 'Notes', 'Write your clue notes and check them'],
    ['drill', 'Drill', 'Play Buzz Mode or study the flashcards']
  ];
  const LEVELS = [[0, 'Rookie'], [150, 'Clue Hunter'], [400, 'Stock-Clue Collector'], [800, 'Power Seeker'], [1400, 'Power Player'], [2200, 'Packet Master'], [3200, 'Nationals Contender'], [4500, 'National Champion']];
  const PTS = { power: 15, ten: 10, neg: -5, miss: 0, dead: 0 };
  // Sizes that keep 1,700 topics light: rail areas open on their own only for small "My topics",
  // Home shows a few cards per area, search shows the first rows per area, Flashcards sample big pools.
  const RAIL_AUTO_OPEN = 40, HOME_CARDS = 6, SEARCH_ROWS = 50, FC_SAMPLE = 20, FC_CHUNKS = 5, STATS_ALL = 60;

  const ICON = {
    home: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V21h14V9.5"/></svg>',
    bell: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/></svg>',
    cards: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="7" width="13" height="14" rx="2"/><path d="M8 3h11a2 2 0 0 1 2 2v12"/></svg>',
    chart: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 3v18h18"/><path d="M8 17v-6"/><path d="M13 17V7"/><path d="M18 17v-4"/></svg>',
    flame: '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2c1 3.5-1.5 5-1.5 7.5 0 1.4 1 2.5 2.3 2.5 1.6 0 2.2-1.6 1.7-3.4C17 10 19 12.6 19 15.5 19 19.1 15.9 22 12 22s-7-2.9-7-6.5C5 10.9 9.6 8.2 12 2z"/></svg>',
    speaker: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M11 5 6 9H2v6h4l5 4V5z"/><path d="M15.5 8.5a5 5 0 0 1 0 7"/><path d="M19 5a10 10 0 0 1 0 14"/></svg>',
    lock: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>',
    menu: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h16"/></svg>',
    grid: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="8" height="8" rx="1.5"/><rect x="13" y="3" width="8" height="8" rx="1.5"/><rect x="3" y="13" width="8" height="8" rx="1.5"/><rect x="13" y="13" width="8" height="8" rx="1.5"/></svg>',
    cloud: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M17.5 19H7a5 5 0 1 1 1.1-9.9A6 6 0 0 1 19.5 11a4 4 0 0 1-2 8z"/><path d="M4 4l16 16"/></svg>',
    chev: '<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg>'
  };

  /* ---------- tiny utilities ---------- */
  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => [...root.querySelectorAll(sel)];
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const fmt = s => esc(s).replace(/_([^_]+)_/g, '<i>$1</i>').replace(/\[“([^”]+)”\]/g, '<span class="pg">[“$1”]</span>');
  const shuffle = a => { for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  const clamp = (v, lo, hi) => Math.max(lo, Math.min(hi, v));
  const plural = (n, w, many) => `${n} ${n === 1 ? w : many || w + 's'}`;
  const pct = x => Math.round(x * 100) + '%';
  const mono = t => `<span class="mono${t.mono.length > 2 ? ' m3' : ''}">${esc(t.mono)}</span>`;
  const debounce = (fn, ms) => { let id = null; return (...args) => { clearTimeout(id); id = setTimeout(() => fn(...args), ms); }; };

  /* ---------- content loader ---------- */
  // Full topics live in content/<area>-<n>.<hash>.json (about a dozen per file), listed in DATA.chunks
  // and fetched by relative URL. loadTopics(ids) fetches only the chunks it needs, shares requests
  // already in flight, and keeps every topic it has loaded in memory. The offline build inlines each
  // chunk as <script type="application/json" data-chunk="<url>">, which is used instead of fetching.
  const FULL = new Map();
  const CHUNK_JOBS = new Map();
  const FETCH_TIMEOUT_MS = 20000;
  let inlineChunks = null;
  const loadError = (kind, msg) => Object.assign(new Error(msg), { kind }); // kind: 'network' | 'stale'
  function inlineChunk(url) {
    if (!inlineChunks) { inlineChunks = new Map(); $$('script[data-chunk]').forEach(s => inlineChunks.set(s.getAttribute('data-chunk'), s)); }
    const el = inlineChunks.get(url);
    return el ? el.textContent : null;
  }
  async function fetchChunk(url) {
    const inline = inlineChunk(url);
    if (inline != null) return JSON.parse(inline);
    const ctl = typeof AbortController === 'function' ? new AbortController() : null;
    const timer = ctl ? setTimeout(() => ctl.abort(), FETCH_TIMEOUT_MS) : null;
    try {
      let res;
      try { res = await fetch(url, ctl ? { signal: ctl.signal } : undefined); } catch (e) { throw loadError('network', 'fetch failed: ' + url); }
      if (res.status === 404 || res.status === 410) throw loadError('stale', 'gone: ' + url); // the site was rebuilt since this page loaded
      if (!res.ok) throw loadError('network', 'HTTP ' + res.status + ': ' + url);
      try { return await res.json(); } catch (e) { throw loadError('network', 'unreadable: ' + url); }
    } finally { if (timer) clearTimeout(timer); }
  }
  function loadChunk(ci) {
    let job = CHUNK_JOBS.get(ci);
    if (!job) {
      const url = CHUNKS[ci];
      job = (url ? fetchChunk(url) : Promise.reject(loadError('stale', 'no chunk ' + ci))).then(data => {
        (data && Array.isArray(data.topics) ? data.topics : []).forEach(t => { if (t && ENTRY_BY_ID[t.id]) FULL.set(t.id, t); });
      });
      CHUNK_JOBS.set(ci, job);
      job.catch(() => { if (CHUNK_JOBS.get(ci) === job) CHUNK_JOBS.delete(ci); }); // so Retry fetches again
    }
    return job;
  }
  // Resolves to the full topic objects for these (built) ids, in the same order.
  async function loadTopics(ids) {
    const need = new Set();
    ids.forEach(id => { const e = ENTRY_BY_ID[id]; if (e && e.built && !FULL.has(id)) need.add(e.chunk); });
    await Promise.all([...need].map(loadChunk));
    return ids.map(id => { const t = FULL.get(id); if (!t) throw loadError('stale', 'not in its chunk: ' + id); return t; });
  }
  const prefetch = ids => { loadTopics(ids).catch(() => { /* the view that needs it shows the error */ }); };
  function loadErrorHtml(err, what, retryAct, extra) {
    const stale = !!err && err.kind === 'stale';
    const head = stale ? `This ${what} was updated after you opened the page.` : `Couldn’t load this ${what} — check your connection.`;
    const sub = stale ? 'Reload the page to get the newest version. Your progress is saved.'
      : location.protocol === 'file:' ? 'Topics can’t load from a file saved on this computer. Open the site’s web address instead.'
        : 'Your progress is saved. Try again in a moment.';
    return `<div class="load-error" role="alert">${ICON.cloud}<div><p><b>${esc(head)}</b></p><p class="muted">${esc(sub)}</p>
      <div class="row">${stale ? '<button class="btn btn-pen" data-act="reload">Reload the page</button>' : ''}<button class="btn${stale ? '' : ' btn-pen'}" data-act="${esc(retryAct)}">Retry</button>${extra || ''}</div></div></div>`;
  }

  /* ---------- saved progress ---------- */
  const KEY = 'qblab.v1';
  const fresh = () => ({
    v: 1, xp: 0, streak: { count: 0, last: null }, topics: {}, cards: {}, tu: {}, my: [], ui: { railOpen: {} },
    career: { p: 0, t: 0, n: 0, heard: 0, sessions: 0, best: 0 },
    settings: { wpm: 200, speak: false, sound: true, count: '10', pool: 'my', deck: 'my', cardMode: 'auto', withMastered: false, theme: 'system', themeTouched: false }
  });
  const topicDefaults = () => ({ notes: '', unlocked: false, paper: false, caught: null, steps: {}, buzz: { p: 0, t: 0, n: 0, miss: 0 }, xpNotes: false });
  function deepMerge(base, add) {
    if (!add || typeof add !== 'object') return base;
    for (const k of Object.keys(add)) {
      const v = add[k];
      if (v && typeof v === 'object' && !Array.isArray(v) && base[k] && typeof base[k] === 'object' && !Array.isArray(base[k])) deepMerge(base[k], v);
      else base[k] = v;
    }
    return base;
  }
  function readSaved() { try { const raw = localStorage.getItem(KEY); if (raw) return deepMerge(fresh(), JSON.parse(raw)); } catch (e) { /* storage blocked */ } return fresh(); }
  let S = readSaved();
  // Mastered flashcards per topic, counted from S.cards keys "<topic id>:<clue id>" (rebuilt when cards change).
  let masteredIdx = null;
  function cardsChanged() { masteredIdx = null; }
  // Keeps saved state valid as the topic set grows. A topic's record is created the first time it is
  // studied (TS), so the save stays small with 1,700 topics; reads go through TSR, which never creates one.
  function normalizeState() {
    if (!S.topics || typeof S.topics !== 'object' || Array.isArray(S.topics)) S.topics = {};
    Object.keys(S.topics).forEach(id => { const v = S.topics[id]; S.topics[id] = deepMerge(topicDefaults(), v && typeof v === 'object' ? v : {}); });
    ['cards', 'tu'].forEach(k => { if (!S[k] || typeof S[k] !== 'object' || Array.isArray(S[k])) S[k] = {}; });
    if (!Array.isArray(S.my)) S.my = [];
    S.my = [...new Set(S.my.filter(id => ENTRY_BY_ID[id]))]; // drop ids that were renamed or removed
    if (!S.ui || typeof S.ui !== 'object') S.ui = { railOpen: {} };
    if (!S.ui.railOpen || typeof S.ui.railOpen !== 'object') S.ui.railOpen = {};
    cardsChanged();
  }
  normalizeState();
  const storageOK = (() => { try { localStorage.setItem(KEY + '.probe', '1'); localStorage.removeItem(KEY + '.probe'); return true; } catch (e) { return false; } })();
  function save() { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) { /* ignore */ } }
  let saveTimer = null;
  const saveSoon = () => { clearTimeout(saveTimer); saveTimer = setTimeout(save, 350); };
  const TS = id => S.topics[id] || (S.topics[id] = topicDefaults());
  const BLANK_TS = (() => { const b = topicDefaults(); Object.freeze(b.steps); Object.freeze(b.buzz); return Object.freeze(b); })();
  const TSR = id => S.topics[id] || BLANK_TS;

  /* ---------- my topics ---------- */
  const sanitizedMy = () => S.my.filter(id => ENTRY_BY_ID[id]);
  const mySet = () => new Set(sanitizedMy());
  const myBuiltEntries = () => { const set = mySet(); return BUILT.filter(e => set.has(e.id)); };
  const myBtnHtml = id => { const on = S.my.includes(id); return `<button class="btn ${on ? 'btn-pen' : ''}" data-act="my-toggle" data-id="${esc(id)}" aria-pressed="${on}">${on ? '✓ In my topics' : '+ My topics'}</button>`; };
  function setMine(id, on) {
    const set = mySet();
    if (on) set.add(id); else set.delete(id);
    S.my = [...set];
    afterMyChange([id]);
  }
  // After My topics changes: save, then repaint whatever shows it (Topics page checkboxes and counts, the rail).
  function afterMyChange(ids) {
    save();
    if (view === 'topics') { refreshTopicsChecks(ids); paintAreaMetas(); paintListCards(); updateMyCount(); }
    renderRail();
  }
  function updateMyCount() { const el = $('#mySelCount'); if (el) el.textContent = plural(sanitizedMy().length, 'topic') + ' selected'; }
  function refreshTopicsChecks(ids) { const set = mySet(); ids.forEach(id => { const el = document.getElementById('chk-' + id); if (el) el.checked = set.has(id); }); }

  /* ---------- buzz/flashcard pools: 'my' | 'all' | 'area:<name>' | '<topic id>' ---------- */
  function normalizePoolValue(v) {
    if (v === 'all') return 'all';
    if (v === 'my') return myBuiltEntries().length ? 'my' : 'all';
    if (typeof v === 'string' && v.startsWith('area:')) return BUILT_AREAS.includes(v.slice(5)) ? v : 'all';
    const e = ENTRY_BY_ID[v];
    return e && e.built ? v : 'all';
  }
  // Built topic ids in a pool (from the index; nothing is loaded here).
  function idsForPool(v) {
    if (v === 'my') { const ids = myBuiltEntries().map(e => e.id); if (ids.length) return ids; }
    else if (typeof v === 'string' && v.startsWith('area:')) { const list = BUILT_BY_AREA[v.slice(5)]; if (list && list.length) return list.map(e => e.id); }
    else if (v !== 'all') { const e = ENTRY_BY_ID[v]; if (e && e.built) return [e.id]; }
    return BUILT.map(e => e.id);
  }
  const isMultiDeck = v => v === 'all' || v === 'my' || (typeof v === 'string' && v.startsWith('area:'));
  // Shared <option>/<optgroup> markup for the Buzz pool and Flashcards deck selects.
  function poolOptionsHtml(selected, opts) {
    const o = Object.assign({ myLabel: 'My topics (mixed)', allLabel: 'All topics (mixed)', areaLabel: n => `All ${n} (mixed)`, singleLabel: e => e.name }, opts || {});
    const sel = v => (selected === v ? ' selected' : '');
    let html = '';
    if (myBuiltEntries().length) html += `<option value="my"${sel('my')}>${esc(o.myLabel)}</option>`;
    html += `<option value="all"${sel('all')}>${esc(o.allLabel)}</option>`;
    BUILT_AREAS.forEach(name => { html += `<option value="area:${esc(name)}"${sel('area:' + name)}>${esc(o.areaLabel(name))}</option>`; });
    BUILT_AREAS.forEach(name => {
      html += `<optgroup label="${esc(name)}">${BUILT_BY_AREA[name].map(e => `<option value="${esc(e.id)}"${sel(e.id)}>${esc(o.singleLabel(e))}</option>`).join('')}</optgroup>`;
    });
    return html;
  }

  /* ---------- QBReader frequency list ---------- */
  const freqLine = t => t.freq ? `#${t.freq.rank} on QBReader’s ${esc(t.freq.list)} frequency list · ${plural(t.freq.count, 'tossup')} (Middle School + Easy High School)` : '';
  const freqBadge = t => t.freq ? `<span class="pill pill-freq" title="${esc(freqLine(t))}">#${esc(t.freq.rank)}</span>` : '';
  function fmtDate(iso) { try { return new Date(iso + 'T00:00:00').toLocaleDateString(undefined, { year: 'numeric', month: 'short', day: 'numeric' }); } catch (e) { return iso; } }

  /* ---------- XP, levels, streaks ---------- */
  const dayKey = (d = new Date()) => `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
  const daysBetween = (a, b) => Math.round((new Date(b + 'T12:00:00') - new Date(a + 'T12:00:00')) / 864e5);
  function touch(xp = 0) {
    const today = dayKey(), st = S.streak;
    if (st.last !== today) { st.count = st.last && daysBetween(st.last, today) === 1 ? st.count + 1 : 1; st.last = today; }
    const before = level(S.xp).n;
    if (xp > 0) S.xp += xp;
    save(); paintPlayer();
    const after = level(S.xp);
    if (after.n > before) toast(`Level up! Level ${after.n}: ${after.title}`);
  }
  const streakNow = () => { const st = S.streak; if (!st.last) return 0; return daysBetween(st.last, dayKey()) <= 1 ? st.count : 0; };
  function level(xp) {
    let i = 0;
    while (i + 1 < LEVELS.length && xp >= LEVELS[i + 1][0]) i++;
    const [from, title] = LEVELS[i];
    const to = LEVELS[i + 1] ? LEVELS[i + 1][0] : null;
    return { n: i + 1, title, from, to, pct: to ? (xp - from) / (to - from) : 1 };
  }

  /* ---------- per-topic progress (works from an index entry or a full topic) ---------- */
  const cardKeys = t => t.clues.map(c => `${t.id}:${c.id}`).concat(`${t.id}:__recite`);
  function masteredCount(id) {
    if (!masteredIdx) {
      masteredIdx = {};
      Object.keys(S.cards).forEach(k => { const r = S.cards[k], cut = k.indexOf(':'); if (r && r.m && cut > 0) { const tid = k.slice(0, cut); masteredIdx[tid] = (masteredIdx[tid] || 0) + 1; } });
    }
    return masteredIdx[id] || 0;
  }
  // Share of a topic's flashcards marked "Got it": exact once the topic is loaded, else from the index's clue count.
  function mastery(t) {
    const full = FULL.get(t.id);
    if (full) { const keys = cardKeys(full); return keys.filter(k => S.cards[k] && S.cards[k].m).length / keys.length; }
    const e = ENTRY_BY_ID[t.id], total = e && e.built ? e.clues + 1 : 0;
    return total ? Math.min(1, masteredCount(t.id) / total) : 0;
  }
  function stepDone(t, k) {
    const ts = TSR(t.id);
    if (k === 'notes') return !!ts.unlocked;
    if (k === 'drill') { const b = ts.buzz; return !!ts.steps.drill || b.p + b.t + b.n + b.miss > 0; }
    return !!ts.steps[k];
  }
  const stepsDone = t => STEPS.filter(([k]) => stepDone(t, k)).length;

  /* ---------- toast ---------- */
  let toastTimer = null;
  function toast(msg) {
    const el = $('#toast'); if (!el) return;
    el.textContent = msg; el.classList.add('show');
    clearTimeout(toastTimer); toastTimer = setTimeout(() => el.classList.remove('show'), 2200);
  }

  /* ---------- theme ---------- */
  const THEMES = ['system', 'light', 'dark'];
  function applyTheme() {
    const th = S.settings.theme, root = document.documentElement;
    if (th === 'light' || th === 'dark') root.setAttribute('data-theme', th);
    else if (S.settings.themeTouched) root.removeAttribute('data-theme');
  }
  function cycleTheme() {
    const i = THEMES.indexOf(S.settings.theme);
    S.settings.theme = THEMES[(i + 1) % THEMES.length]; S.settings.themeTouched = true;
    applyTheme(); save(); renderRail();
  }
  const themeLabel = () => ({ system: 'Theme: match device', light: 'Theme: light', dark: 'Theme: dark' }[S.settings.theme] || 'Theme');

  /* ---------- sound + speech ---------- */
  let actx = null;
  function beep(kind) {
    if (!S.settings.sound) return;
    try {
      actx = actx || new (window.AudioContext || window.webkitAudioContext)();
      const o = actx.createOscillator(), g = actx.createGain(), now = actx.currentTime;
      o.type = 'square'; o.frequency.value = kind === 'good' ? 880 : kind === 'power' ? 1175 : kind === 'bad' ? 196 : 523;
      g.gain.setValueAtTime(0.0001, now); g.gain.exponentialRampToValueAtTime(0.07, now + 0.01); g.gain.exponentialRampToValueAtTime(0.0001, now + 0.2);
      o.connect(g); g.connect(actx.destination); o.start(now); o.stop(now + 0.22);
    } catch (e) { /* no audio */ }
  }
  const speechAvailable = () => 'speechSynthesis' in window && 'SpeechSynthesisUtterance' in window;
  function pickVoice() {
    try {
      const vs = speechSynthesis.getVoices().filter(v => /^en[-_]/i.test(v.lang) || v.lang === 'en');
      return vs.find(v => v.localService && /en[-_]US/i.test(v.lang)) || vs.find(v => /en[-_]US/i.test(v.lang)) || vs.find(v => v.localService) || vs[0] || null;
    } catch (e) { return null; }
  }
  function hush() { try { if (speechAvailable()) speechSynthesis.cancel(); } catch (e) { /* ignore */ } }
  if (speechAvailable()) { try { speechSynthesis.getVoices(); speechSynthesis.onvoiceschanged = () => speechSynthesis.getVoices(); } catch (e) { /* ignore */ } }

  let saying = null;
  function sayTossup(t, i, btn) {
    if (!speechAvailable()) { toast('Read-aloud isn’t available in this browser.'); return; }
    if (saying && saying.btn === btn) { hush(); btn.classList.remove('on'); saying = null; return; }
    hush(); if (saying) saying.btn.classList.remove('on');
    const tu = t.tossups[i];
    const text = plain(tu.p + ' ' + tu.r);
    const chunks = text.match(/[^.!?]+[.!?]+[”’")]*|[^.!?]+$/g) || [text];
    const v = pickVoice(), token = {};
    saying = { btn, token }; btn.classList.add('on');
    chunks.forEach((ch, k) => {
      const u = new SpeechSynthesisUtterance(ch.trim());
      if (v) { u.voice = v; u.lang = v.lang; } else u.lang = 'en-US';
      u.rate = clamp(S.settings.wpm / 175, 0.6, 2);
      if (k === chunks.length - 1) u.onend = () => { if (saying && saying.token === token) { btn.classList.remove('on'); saying = null; } };
      speechSynthesis.speak(u);
    });
  }

  /* ---------- routing ---------- */
  let view = 'home', routeSeq = 0;
  const main = () => $('#main');
  function go(h) { if (location.hash === '#' + h) route(); else location.hash = h; }
  function route() {
    const seq = ++routeSeq;
    stopBuzz(); FC.wait = null; hush(); if (saying) { saying.btn.classList.remove('on'); saying = null; }
    const h = (location.hash || '').replace(/^#/, '');
    if (h.startsWith('topic-')) {
      const e = ENTRY_BY_ID[h.slice(6)];
      if (e && e.built) return openTopic(e, seq);
      if (e) return viewUpcoming(e);
    }
    if (h === 'topics') return viewTopics();
    if (h === 'buzz') return viewBuzz();
    if (h === 'cards') return viewCards();
    if (h === 'stats') return viewStats();
    return viewHome();
  }
  function show(name, html) {
    view = name;
    const m = main(); m.innerHTML = html;
    window.scrollTo(0, 0); m.scrollTop = 0;
    closeMenu(); syncRail();
    if (name === 'topic') requestAnimationFrame(revealRailItem);
    try { m.focus({ preventScroll: true }); } catch (e) { /* ignore */ }
  }
  const closeMenu = () => $('#app').classList.remove('menu-open');

  /* ---------- rail ---------- */
  function ring(p) {
    const r = 9, C = 2 * Math.PI * r;
    const fg = p > 0 ? `<circle cx="12" cy="12" r="${r}" class="ring-fg" stroke-dasharray="${(C * p).toFixed(2)} ${C.toFixed(2)}" transform="rotate(-90 12 12)"/>` : '';
    return `<svg class="ring" viewBox="0 0 24 24" role="img" aria-label="${pct(p)} of flashcards mastered"><circle cx="12" cy="12" r="${r}" class="ring-bg"/>${fg}</svg>`;
  }
  const navBtn = (to, label, icon) => `<button class="nav-btn ${view === to ? 'is-active' : ''}" data-act="go" data-to="${to}">${icon}<span>${label}</span></button>`;
  const currentTopicId = () => { const h = (location.hash || '').replace(/^#/, ''); return h.startsWith('topic-') ? h.slice(6) : null; };

  // Rail library: "My topics" grouped by area when any are picked, else every area, each with a
  // collapsible header and a ready/total count. Areas start collapsed (except for a small My topics,
  // the area being viewed, or ones the student opened); a collapsed area renders only its header and
  // is filled in when opened. Inside an area, built topics come first and the ones not written yet
  // fold into a single "N coming soon" row, so a 450-topic list stays short.
  const railState = { groups: {}, soonOpen: {} };
  function railRowHtml(e, curId) {
    const id = esc(e.id), active = curId === e.id ? ' is-active' : '';
    if (e.built) {
      return `<button class="lib-item${active}" data-act="go" data-to="topic-${id}" data-id="${id}">
        ${mono(e)}<span class="lib-name">${esc(e.name)}<small>${stepsDone(e)} of 5 steps</small></span>${ring(mastery(e))}</button>`;
    }
    return `<div class="lib-item is-upcoming${active}" data-id="${id}">${mono(e)}<span class="lib-name">${esc(e.name)}<small>Not written yet</small></span><span class="tag-soon">Soon</span></div>`;
  }
  function railBodyHtml(area, curId) {
    const built = [], soon = [];
    (railState.groups[area] || []).forEach(e => (e.built ? built : soon).push(e));
    let html = built.map(e => railRowHtml(e, curId)).join('');
    if (soon.length) {
      const open = !!railState.soonOpen[area] || soon.some(e => e.id === curId);
      html += `<button class="lib-soon" data-act="rail-soon" data-area="${esc(area)}" aria-expanded="${open}">${ICON.chev}<span>${built.length ? `${soon.length} more coming soon` : `${plural(soon.length, 'topic')} coming soon`}</span></button>
        <div class="lib-soon-body" data-area="${esc(area)}"${open ? '' : ' hidden'}>${open ? soon.map(e => railRowHtml(e, curId)).join('') : ''}</div>`;
    }
    return html;
  }
  function railGroups() {
    const mine = mySet();
    if (mine.size) return AREAS.map(a => ({ area: a.name, entries: BY_AREA[a.name].filter(e => mine.has(e.id)) })).filter(g => g.entries.length);
    return AREAS.map(a => ({ area: a.name, entries: BY_AREA[a.name] }));
  }
  function playerHtml() {
    const lv = level(S.xp), st = streakNow(), c = S.career;
    return `<div class="player-top"><span class="lv">Level ${lv.n}</span><span class="lv-title">${esc(lv.title)}</span></div>
        <div class="xpbar" role="progressbar" aria-label="Progress to the next level" aria-valuemin="0" aria-valuemax="100" aria-valuenow="${Math.round(lv.pct * 100)}"><span style="width:${(lv.pct * 100).toFixed(1)}%"></span></div>
        <div class="player-meta">${S.xp} XP${lv.to ? ` · ${lv.to - S.xp} to Level ${lv.n + 1}` : ' · top level!'}</div>
        <div class="player-stats">
          <span class="streak ${st ? 'on' : ''}" title="Days in a row with practice">${ICON.flame}${plural(st, 'day')}</span>
          <span class="pgn" title="Buzz Mode: powers / tens / negs"><b>${c.p}</b>/<b>${c.t}</b>/<b>${c.n}</b> <small>P/T/N</small></span>
        </div>`;
  }
  function paintTopbar() { const lv = level(S.xp), tb = $('#tbXp'); if (tb) tb.textContent = `Lv ${lv.n} · ${S.xp} XP`; }
  function paintPlayer() { const el = $('#railPlayer'); if (el) el.innerHTML = playerHtml(); paintTopbar(); }
  // Repaints one topic's rail row (steps, mastery ring) without rebuilding the rail.
  function paintRailRow(id) {
    const e = ENTRY_BY_ID[id], el = $$('#rail .lib-item').find(x => x.dataset.id === id);
    if (e && el) el.outerHTML = railRowHtml(e, currentTopicId());
  }
  // Whether an area is open when it doesn't hold the topic being viewed: as the student left it, else
  // open only for a small My topics.
  function railOpenByDefault(area, mineCount) {
    const stored = S.ui.railOpen[area];
    return stored !== undefined ? !!stored : mineCount > 0 && mineCount <= RAIL_AUTO_OPEN;
  }
  const railAreaEls = area => [$$('#rail .lib-area-h').find(b => b.dataset.area === area), $$('#rail .lib-area-body').find(b => b.dataset.area === area)];
  function setRailArea(area, open) {
    const [h, body] = railAreaEls(area);
    if (!h || !body) return;
    h.setAttribute('aria-expanded', String(open));
    body.hidden = !open;
    if (open && body.dataset.loaded !== '1') { body.innerHTML = railBodyHtml(area, currentTopicId()); body.dataset.loaded = '1'; }
  }
  function setRailSoon(area, open) {
    const btn = $$('#rail .lib-soon').find(b => b.dataset.area === area), body = $$('#rail .lib-soon-body').find(b => b.dataset.area === area);
    if (!btn || !body) return;
    railState.soonOpen[area] = open;
    btn.setAttribute('aria-expanded', String(open));
    body.hidden = !open;
    if (open && !body.childElementCount) { const cur = currentTopicId(); body.innerHTML = (railState.groups[area] || []).filter(x => !x.built).map(x => railRowHtml(x, cur)).join(''); }
  }
  // After navigation: highlight the nav item and the topic being viewed, open its area (closing the one
  // opened for the previous topic), refresh the player card. The full rebuild (renderRail) runs only
  // when the rail's contents change (My topics, theme, restore), so moving between topics stays cheap.
  let railStale = true, railAuto = null;
  function syncRail() {
    const rail = $('#rail');
    if (!rail || railStale || !rail.childElementCount) return renderRail();
    $$('.nav-btn', rail).forEach(b => { const on = b.dataset.to === view; b.classList.toggle('is-active', on); });
    const curId = currentTopicId(), cur = curId ? ENTRY_BY_ID[curId] : null, curArea = cur ? cur.category : null;
    if (curArea !== railAuto) {
      if (railAuto && !railOpenByDefault(railAuto, sanitizedMy().length)) setRailArea(railAuto, false);
      if (curArea) setRailArea(curArea, true);
      railAuto = curArea;
    }
    $$('.lib-item.is-active', rail).forEach(x => { if (x.dataset.id !== curId) x.classList.remove('is-active'); });
    if (cur) {
      if (!cur.built) setRailSoon(curArea, true);
      const item = $$('.lib-item', rail).find(x => x.dataset.id === curId);
      if (item) item.classList.add('is-active');
    }
    paintPlayer();
  }
  function renderRail() {
    const rail = $('#rail'); if (!rail) return;
    const curId = currentTopicId(), cur = curId ? ENTRY_BY_ID[curId] : null, curArea = cur ? cur.category : null;
    const mine = sanitizedMy();
    railStale = false; railAuto = curArea;
    railState.groups = {};
    const groupsHtml = railGroups().map(g => {
      railState.groups[g.area] = g.entries;
      const isOpen = g.area === curArea || railOpenByDefault(g.area, mine.length);
      const total = g.entries.length, ready = g.entries.filter(e => e.built).length;
      return `<div class="lib-area">
        <button class="lib-area-h" data-act="rail-toggle" data-area="${esc(g.area)}" aria-expanded="${isOpen}" title="${esc(g.area)}: ${ready} of ${total} ready">
          ${ICON.chev}<span class="lib-area-name">${esc(SHORT_BY_AREA[g.area] || g.area)}</span><span class="lib-area-count">${ready === total ? total : `${ready}<span class="of">/${total}</span>`}</span>
        </button>
        <div class="lib-area-body" data-area="${esc(g.area)}" data-loaded="${isOpen ? '1' : '0'}"${isOpen ? '' : ' hidden'}>${isOpen ? railBodyHtml(g.area, curId) : ''}</div>
      </div>`;
    }).join('');
    const pickHtml = mine.length ? '' : `<div class="lib-empty"><p>Pick the topics you want to study.</p><button class="btn btn-sm btn-pen" data-act="go" data-to="topics">Pick your topics</button></div>`;
    rail.innerHTML = `
      <div class="brand"><span class="brand-eyebrow">Team</span><span class="brand-name">Quiz Bowl Lab</span><span class="brand-sub">Middle School · Easy High School</span></div>
      <div class="player" id="railPlayer">${playerHtml()}</div>
      <nav class="nav" aria-label="Main">
        ${navBtn('home', 'Home', ICON.home)}${navBtn('topics', 'Topics', ICON.grid)}${navBtn('buzz', 'Buzz Mode', ICON.bell)}${navBtn('cards', 'Flashcards', ICON.cards)}${navBtn('stats', 'My Stats', ICON.chart)}
      </nav>
      ${pickHtml}
      <div class="library" aria-label="${mine.length ? 'My topics' : 'All topics'}">${mine.length ? '<p class="lib-title">My topics</p>' : ''}${groupsHtml}</div>
      <div class="rail-foot">
        <button class="theme-btn" data-act="theme">${themeLabel()}</button>
        ${storageOK ? '' : '<p class="rail-note">This browser is blocking saved data, so progress will reset when you close the page.</p>'}
      </div>`;
    paintTopbar();
  }
  // Scrolls the rail (only the rail) so the topic being viewed is in sight. Skipped while the phone
  // drawer is closed (it runs again when the drawer opens).
  function revealRailItem() {
    const rail = $('#rail'), item = rail && rail.querySelector('.lib-item.is-active');
    if (!item || (window.matchMedia('(max-width: 900px)').matches && !$('#app').classList.contains('menu-open'))) return;
    const r = rail.getBoundingClientRect(), i = item.getBoundingClientRect();
    if (i.top < r.top + 8 || i.bottom > r.bottom - 8) rail.scrollTop += i.top - r.top - rail.clientHeight / 3;
  }

  /* ---------- HOME ---------- */
  function libCard(e) {
    const d = stepsDone(e);
    return `<button class="lib-card" data-act="go" data-to="topic-${esc(e.id)}">
      <span class="lib-card-top">${mono(e)}<span><span class="lc-name">${esc(e.name)}</span><span class="kick">${fmt(e.kicker)}</span></span></span>
      <span class="meter" aria-hidden="true"><span style="width:${(d / 5) * 100}%"></span></span>
      <span class="meta"><span>${d} of 5 steps</span><span>${pct(mastery(e))} cards mastered</span></span>
    </button>`;
  }
  // One area of My topics on Home: the first few ready topics as cards, then "more ready" and
  // "coming soon" tiles instead of hundreds of cards.
  const homeMore = {};
  function homeAreaHtml(area, set) {
    const mine = BY_AREA[area].filter(e => set.has(e.id)), built = mine.filter(e => e.built), soon = mine.length - built.length;
    const cap = homeMore[area] ? built.length : HOME_CARDS;
    const more = built.length > cap
      ? `<button class="lib-card tile-more" data-act="home-more" data-area="${esc(area)}"><span class="lc-name">+ ${built.length - cap} more ready</span><span class="kick">Show all ${built.length}</span></button>` : '';
    const soonTile = soon
      ? `<button class="lib-card tile-soon" data-act="browse-area" data-area="${esc(area)}"><span class="tag-soon">Soon</span><span class="lc-name">${built.length ? `${soon} more coming soon` : `${plural(soon, 'topic')} coming soon`}</span><span class="kick">See them on the Topics page</span></button>` : '';
    return `<section class="sec" data-home-area="${esc(area)}"><h2>${esc(area)} <span class="sec-count">${built.length} of ${mine.length} ready</span></h2>
      <div class="lib-grid">${built.slice(0, cap).map(libCard).join('')}${more}${soonTile}</div></section>`;
  }
  function viewHome() {
    const mine = sanitizedMy(), set = new Set(mine);
    const scopeBuilt = mine.length ? myBuiltEntries() : BUILT;
    const next = scopeBuilt.find(e => !TSR(e.id).unlocked);
    const pickHtml = mine.length ? '' : `<div class="pick-card card">
        <p class="eyebrow">First step</p><h2>Pick your topics</h2>
        <p>Choose your own on the Topics page, or add a teammate’s team study list — ${BUILT.length === ENTRIES.length ? `all ${BUILT.length} topics are ready.` : `${BUILT.length} of ${ENTRIES.length} topics are ready now, and more are on the way.`}</p>
        <button class="btn btn-pen" data-act="go" data-to="topics">Pick your topics</button>
      </div>`;
    const nextHtml = next
      ? `<div class="next-card">${mono(next)}<div><p class="eyebrow">Up next</p><h2>${esc(next.name)}</h2><p>${fmt(next.kicker)} · ${stepsDone(next)} of 5 steps done</p></div><button class="btn btn-buzz" data-act="go" data-to="topic-${esc(next.id)}">Start studying</button></div>`
      : scopeBuilt.length
        ? `<div class="next-card"><span class="mono">${ICON.bell}</span><div><p class="eyebrow">All notes done</p><h2>Time for a mixed round</h2><p>Every topic${mine.length ? ' in My topics' : ''} has notes. Now play Buzz Mode mixed, like a real match.</p></div><button class="btn btn-buzz" data-act="${mine.length ? 'buzz-my' : 'buzz-all'}">Play Buzz Mode</button></div>`
        : `<div class="next-card"><span class="mono">${ICON.bell}</span><div><p class="eyebrow">Coming soon</p><h2>Your topics aren’t built yet</h2><p>None of the topics you picked are ready yet. Check back soon, or study any topic that’s already built.</p></div><button class="btn btn-buzz" data-act="go" data-to="topics">Browse built topics</button></div>`;
    const myCardsHtml = mine.length ? AREAS.filter(a => BY_AREA[a.name].some(e => set.has(e.id))).map(a => homeAreaHtml(a.name, set)).join('') : '';
    show('home', `<div class="page">
      <header class="home-head">
        <p class="eyebrow">Team Quiz Bowl Lab</p>
        <h1 class="display">Ready to buzz?</h1>
        <p class="lede">Study every answer line the way Coach does it: learn the basics, read real-style tossups, take notes from easy clues to hard clues, then drill until you can power it.</p>
      </header>
      ${pickHtml}
      ${nextHtml}
      <section class="sec">
        <h2>Coach’s routine</h2>
        <ol class="routine">
          <li><b>Learn the basics</b>Read a short intro first so the clues make sense.</li>
          <li><b>Search QBReader</b>Middle School + Easy High School, answer only, tossups, power-marked.</li>
          <li><b>Take notes</b>Easy clues at the top, hard clues at the bottom, a line where power starts.</li>
          <li><b>Drill</b>Flashcards both ways: clue → answer, and answer → recite the clues.</li>
          <li><b>Show Coach</b>Bring your notes and your system to practice.</li>
        </ol>
        <p class="pace"><b>Coach’s pace:</b> 2 or 3 answer lines a day gets you through a 100–150 answer frequency list in about a month.</p>
      </section>
      ${myCardsHtml}
      <section class="modes">
        <button class="mode-tile" data-act="go" data-to="buzz"><span class="mode-icon">${ICON.bell}</span><span class="mt-name">Buzz Mode</span><span class="mt-text">Questions appear word by word or are read aloud. Buzz early for 15.</span></button>
        <button class="mode-tile cards" data-act="go" data-to="cards"><span class="mode-icon">${ICON.cards}</span><span class="mt-name">Flashcards</span><span class="mt-text">One clue per card, Coach’s way. Sort them into “Got it” and “Again.”</span></button>
      </section>
      <p class="fineprint">${BUILT.length} of ${ENTRIES.length} topics are built so far — ${TOTAL_TOSSUPS.toLocaleString()} practice tossups, original questions written in QBReader format and checked against the real QBReader questions for each answer line. Built ${fmtDate(DATA.built)}. Keep using the real QBReader database too.</p>
    </div>`);
  }

  /* ---------- TOPICS PAGE ---------- */
  // Kept for the session, so coming back from a topic finds the same search, filter and open areas.
  const TP = { q: '', area: 'all', open: {}, more: {}, listsOpen: null };
  const entryQ = e => e.q || (e.q = norm([e.name].concat(e.aka).join(' | ')));
  const searchQ = () => norm(TP.q);
  function listCard(l, set) {
    const built = l.ids.filter(id => ENTRY_BY_ID[id].built).length, all = l.ids.length > 0 && l.ids.every(id => set.has(id));
    return `<div class="list-card">
      <div class="list-card-top"><span class="list-n">List ${esc(l.n)}</span></div>
      <p class="list-label">${esc(l.label)}</p>
      <p class="list-ready">${built} of ${l.ids.length} topics ready</p>
      ${all ? `<button class="btn btn-sm is-in" data-act="list-add" data-n="${esc(l.n)}" aria-label="List ${esc(l.n)} is in My topics">✓ In my topics</button>` : `<button class="btn btn-sm btn-pen" data-act="list-add" data-n="${esc(l.n)}">Add to my topics</button>`}
    </div>`;
  }
  function paintListCards() { const g = $('#listGrid'); if (g) { const set = mySet(); g.innerHTML = LISTS.map(l => listCard(l, set)).join(''); } }
  function topicRowHtml(e, set, q) {
    const id = esc(e.id), checked = set.has(e.id) ? ' checked' : '';
    let also = '';
    if (q && !norm(e.name).includes(q)) { const hit = e.aka.find(a => norm(a).includes(q)); if (hit) also = `<span class="trow-aka">also “${esc(hit)}”</span>`; }
    const box = `<input type="checkbox" class="my-check" id="chk-${id}" data-id="${id}"${checked} aria-label="Add ${esc(e.name)} to my topics">${mono(e)}`;
    if (e.built) return `<li class="topic-row">${box}<span class="trow-main"><a class="topic-row-name" href="#topic-${id}">${esc(e.name)}</a><span class="topic-row-status">${stepsDone(e)} of 5 steps${freqBadge(e)}</span>${also}</span></li>`;
    return `<li class="topic-row is-upcoming">${box}<span class="trow-main"><span class="topic-row-name">${esc(e.name)}</span><span class="topic-row-status">Coming soon</span>${also}</span></li>`;
  }
  // Area sections render collapsed (header, counts, Select all / Clear); rows are filled in only when
  // the area is opened, picked with a chip, or has search matches.
  function areaSectionHtml(a, i) {
    const name = esc(a.name);
    return `<section class="topics-area" data-area="${name}">
      <div class="topics-area-h">
        <button class="ta-toggle" data-act="ta-toggle" data-area="${name}" aria-expanded="false" aria-controls="ta-rows-${i}">${ICON.chev}<span class="ta-name">${name}</span><span class="ta-meta"></span></button>
        <div class="ta-actions"><button class="btn btn-sm" data-act="area-select-all" data-area="${name}">Select all</button><button class="btn btn-sm btn-ghost" data-act="area-clear" data-area="${name}">Clear</button></div>
      </div>
      <ul class="topic-rows" id="ta-rows-${i}" hidden></ul>
    </section>`;
  }
  function areaMetaHtml(area, set, matches) {
    if (matches) return plural(matches.length, 'match', 'matches');
    const all = BY_AREA[area], ready = all.filter(e => e.built).length, sel = all.filter(e => set.has(e.id)).length;
    const base = ready === all.length ? plural(all.length, 'topic') : ready ? `${ready} ready · ${all.length - ready} coming soon` : `${all.length} coming soon`;
    return base + (sel ? ` · <b>${sel} selected</b>` : '');
  }
  function areaMatches(area, q) { return q ? BY_AREA[area].filter(e => entryQ(e).includes(q)) : null; }
  // Paints one area section for the current filter/search. `cap` limits rows per area while searching.
  function paintArea(sec, q, set, matches, cap) {
    const area = sec.dataset.area;
    if (matches === undefined) matches = areaMatches(area, q);
    const visible = (TP.area === 'all' || TP.area === area) && (!matches || matches.length > 0);
    const btn = $('.ta-toggle', sec), body = $('.topic-rows', sec), acts = $$('.ta-actions .btn', sec);
    sec.hidden = !visible;
    if (!visible) { if (body.childElementCount) body.innerHTML = ''; return 0; }
    const open = !!matches || TP.area === area || !!TP.open[area];
    sec.classList.toggle('is-open', open);
    btn.setAttribute('aria-expanded', String(open));
    btn.classList.toggle('locked-open', !!matches || TP.area === area);
    $('.ta-meta', sec).innerHTML = areaMetaHtml(area, set, matches);
    acts[0].textContent = matches ? 'Select matches' : 'Select all';
    acts[1].textContent = matches ? 'Clear matches' : 'Clear';
    if (open) {
      const list = matches || BY_AREA[area], lim = matches && !TP.more[area] ? cap || SEARCH_ROWS : list.length;
      body.innerHTML = list.slice(0, lim).map(e => topicRowHtml(e, set, q)).join('')
        + (list.length > lim ? `<li class="topic-more"><button class="btn btn-sm btn-ghost" data-act="ta-more" data-area="${esc(area)}">Show all ${list.length} matches</button></li>` : '');
      body.hidden = false;
    } else { body.innerHTML = ''; body.hidden = true; }
    return matches ? matches.length : 0;
  }
  function paintTopicsList() {
    const q = searchQ(), set = mySet(), secs = $$('#topicsList .topics-area');
    const all = secs.map(sec => areaMatches(sec.dataset.area, q));
    // A very broad search ("a") shows a few rows per area, each with "Show all", so it stays quick.
    const total = q ? all.reduce((n, m, i) => n + (TP.area === 'all' || TP.area === secs[i].dataset.area ? m.length : 0), 0) : 0;
    const cap = total > 200 ? 10 : SEARCH_ROWS;
    let found = 0;
    secs.forEach((sec, i) => { found += paintArea(sec, q, set, all[i], cap); });
    const st = $('#topicsStatus');
    if (st) {
      const where = TP.area === 'all' ? '' : ` in ${esc(SHORT_BY_AREA[TP.area] || TP.area)}`;
      st.innerHTML = !q ? '' : found ? `${plural(found, 'topic')} match “${esc(TP.q.trim())}”${where}.` : `No topics match “${esc(TP.q.trim())}”${where}. Check the spelling or try another name.`;
      st.hidden = !q;
    }
  }
  function paintAreaMetas() {
    const q = searchQ(), set = mySet();
    $$('#topicsList .topics-area').forEach(sec => { if (!sec.hidden) $('.ta-meta', sec).innerHTML = areaMetaHtml(sec.dataset.area, set, areaMatches(sec.dataset.area, q)); });
  }
  const paintSearchSoon = debounce(() => { if (view === 'topics') paintTopicsList(); }, 120);
  function viewTopics() {
    const set = mySet(), listsOpen = TP.listsOpen != null ? TP.listsOpen : !set.size;
    show('topics', `<div class="page">
      <header class="topic-head">
        <p class="eyebrow">Build your set</p>
        <h1 class="display">Topics</h1>
        <p class="kicker">Pick any topics to study — your own, a teammate’s team study list, or browse everything. ${BUILT.length === ENTRIES.length ? `All ${BUILT.length} topics are ready.` : `${BUILT.length} of ${ENTRIES.length.toLocaleString()} topics are ready now; more are coming.`}</p>
      </header>
      <section class="sec">
        <div class="sec-head"><h2>Team study lists</h2><button class="btn btn-sm btn-ghost" data-act="lists-toggle" aria-expanded="${listsOpen}" aria-controls="listGrid">${listsOpen ? 'Hide the lists' : `Show all ${LISTS.length}`}</button></div>
        <p class="sec-note">Each list is one teammate’s assignment. Adding a list never removes topics you already picked.</p>
        <div class="list-grid" id="listGrid"${listsOpen ? '' : ' hidden'}>${LISTS.map(l => listCard(l, set)).join('')}</div>
      </section>
      <section class="sec">
        <div class="my-bar card">
          <span id="mySelCount" class="my-count">${plural(set.size, 'topic')} selected</span>
          <div id="myClearBox" class="row"><button class="btn btn-sm btn-ghost" data-act="my-clear">Clear my topics</button></div>
        </div>
      </section>
      <section class="sec">
        <div class="topics-tools">
          <input type="search" id="topicsSearch" class="search" placeholder="Search all ${ENTRIES.length.toLocaleString()} topics…" aria-label="Search topics" autocomplete="off" value="${esc(TP.q)}">
          <div class="chips" role="group" aria-label="Filter by area" id="areaChips">
            <button class="chip${TP.area === 'all' ? ' on' : ''}" data-act="topics-area" data-area="all" aria-pressed="${TP.area === 'all'}">All</button>
            ${AREAS.map(a => `<button class="chip${TP.area === a.name ? ' on' : ''}" data-act="topics-area" data-area="${esc(a.name)}" aria-pressed="${TP.area === a.name}">${esc(a.short || a.name)}</button>`).join('')}
          </div>
        </div>
        <p class="topics-status" id="topicsStatus" role="status" hidden></p>
        <div id="topicsList">${AREAS.map(areaSectionHtml).join('')}</div>
      </section>
    </div>`);
    paintTopicsList();
  }
  function viewUpcoming(e) {
    show('topic', `<div class="page">
      <header class="topic-head">
        <p class="eyebrow">${esc(e.category)}</p>
        <h1 class="display">${esc(e.name)}</h1>
        <p class="kicker">This one’s coming soon — Coach’s team is still writing it.</p>
        <div class="row">${myBtnHtml(e.id)}</div>
      </header>
      <section class="sec">
        <div class="locked">${ICON.lock}<div><p><b>Not written yet.</b> Check back soon, or study one of the ${BUILT.length} topics that are already built.</p><p class="muted" id="upHint"${S.my.includes(e.id) ? ' hidden' : ''}>Add it to My topics now and it will show up there as soon as it’s ready.</p></div></div>
      </section>
      <div class="row"><button class="btn btn-pen" data-act="go" data-to="topics">Browse topics</button><button class="btn btn-ghost" data-act="go" data-to="home">Home</button></div>
    </div>`);
  }

  /* ---------- TOPIC PAGE ---------- */
  // Shown at once from the index while the full topic loads (and kept if loading fails).
  function topicHeadHtml(e) {
    const id = esc(e.id);
    return `<header class="topic-head">
        <p class="eyebrow">${esc(e.category)}</p>
        <h1 class="display">${esc(e.name)}</h1>
        ${e.kicker ? `<p class="kicker">${fmt(e.kicker)}</p>` : ''}
        <div class="row"><button class="btn btn-buzz" data-act="buzz-topic" data-id="${id}">${ICON.bell}Buzz these ${e.tossups || 15}</button><button class="btn" data-act="cards-topic" data-id="${id}">${ICON.cards}Flashcards</button>
          ${myBtnHtml(e.id)}</div>
      </header>`;
  }
  function openTopic(e, seq) {
    const t = FULL.get(e.id);
    if (t) return viewTopic(t);
    show('topic', `<div class="page" aria-busy="true">${topicHeadHtml(e)}
      <div class="loading" role="status"><span class="loading-dot" aria-hidden="true"></span>Loading this topic…</div>
      <div class="skeleton" aria-hidden="true"><span></span><span></span><span></span><span></span></div>
    </div>`);
    loadTopics([e.id]).then(([full]) => { if (seq === routeSeq) viewTopic(full); }, err => {
      if (seq !== routeSeq) return;
      show('topic', `<div class="page">${topicHeadHtml(e)}<section class="sec">${loadErrorHtml(err, 'topic', 'topic-retry', '<button class="btn btn-ghost" data-act="go" data-to="topics">Browse topics</button>')}</section></div>`);
    });
  }
  function stepsHtml(t) {
    return STEPS.map(([k, label, tip], i) => {
      const done = stepDone(t, k), auto = k === 'notes' || k === 'drill';
      const inner = `<span class="step-n">${done ? '✓' : i + 1}</span><span class="step-l">${label}</span>`;
      return `<li>${auto
        ? `<span class="step auto ${done ? 'done' : ''}" title="${esc(tip)} (checks itself)">${inner}</span>`
        : `<button class="step ${done ? 'done' : ''}" data-act="step" data-id="${esc(t.id)}" data-step="${k}" aria-pressed="${done}" title="${esc(tip)}">${inner}</button>`}</li>`;
    }).join('');
  }
  function refreshSteps(t) { const el = $('#steps'); if (el) el.innerHTML = stepsHtml(t); paintRailRow(t.id); }
  function markStep(t, k) { const ts = TS(t.id); if (!ts.steps[k]) { ts.steps[k] = true; touch(0); refreshSteps(t); } }

  const kindLabel = { video: 'Video', article: 'Article', museum: 'Museum videos', wiki: 'Wikipedia' };
  const mediaCard = (t, m) => `<a class="media-card" href="${esc(m.url)}" target="_blank" rel="noopener" data-act="media" data-id="${esc(t.id)}">
        <span class="media-kind k-${esc(m.kind)}">${esc(kindLabel[m.kind] || m.kind)}</span>
        <span class="media-title">${esc(m.title)}</span><span class="media-src">${esc(m.source)}</span><span class="media-note">${esc(m.note)}</span>
        <span class="media-go" aria-hidden="true">↗</span></a>`;
  const mediaGroup = (title, sub, cards, cls) => !cards.length ? '' : `<div class="media-group${cls ? ' ' + cls : ''}">
        <h3 class="h3 media-h">${title}${sub ? ` <small>${sub}</small>` : ''}</h3>
        <div class="media">${cards.join('')}</div></div>`;
  // Media is grouped: "focus" = 3 to 5 videos about this exact topic, "read" = short articles, "background" = bigger-picture extras.
  function mediaHtml(t) {
    const pick = g => t.media.filter(m => (m.group || 'focus') === g).map(m => mediaCard(t, m));
    const focus = pick('focus'), more = pick('background');
    const read = [mediaCard(t, { url: t.wiki, kind: 'wiki', title: 'Read the intro', source: 'Coach’s first step',
      note: 'The first 3 paragraphs are enough. Hover over words you don’t know.' }), ...pick('read')];
    const soon = t.mediaPending || focus.length < 3;
    const focusSub = focus.length ? `${focus.length} pick${focus.length === 1 ? '' : 's'}, all about this topic${soon ? ' · more coming soon' : ''}` : '';
    const pendingNote = !focus.length ? `<div class="media-group"><h3 class="h3 media-h">Videos about ${esc(t.name)} <small>Coming soon</small></h3><p class="sec-note">We’re still picking the best videos for this topic. Start with the Wikipedia intro below.</p></div>` : '';
    return pendingNote + mediaGroup(`Videos about ${esc(t.name)}`, focusSub, focus)
      + mediaGroup('Read', 'Quick and easy', read)
      + mediaGroup('More background', 'The bigger story around it. Good to have, not required.', more, 'media-more');
  }
  function tuCard(t, tu, i) {
    return `<article class="tu" id="tu-${esc(t.id)}-${i + 1}">
      <header class="tu-h"><span class="tu-n">Tossup ${i + 1}</span><span class="tu-meta">${esc(t.qbCategory)} · QB Lab practice set</span>
        <button class="tu-say" data-act="say" data-id="${esc(t.id)}" data-i="${i}" aria-label="Read tossup ${i + 1} aloud" title="Read aloud">${ICON.speaker}</button></header>
      <p class="tu-q"><b>${fmt(tu.p)} (*)</b> ${fmt(tu.r)}</p>
      <p class="tu-a"><span class="tu-a-tag">ANSWER:</span> ${t.answerHtml}</p>
    </article>`;
  }
  function stockPill(c, t) {
    if (!c.n) return '';
    return c.n >= 2
      ? `<span class="pill pill-stock" title="How many real QBReader tossups used this clue">Stock · ${c.n} of ${t.sample.n} real</span>`
      : `<span class="pill pill-once">In 1 of ${t.sample.n} real</span>`;
  }
  const rabbitPill = c => c.rabbit ? `<span class="pill pill-rabbit" title="This is its own answer line. Study it later!">★ Also an answer line: ${esc(c.rabbit)}</span>` : '';
  function breakdownHtml(t) {
    const ts = TSR(t.id), caught = Array.isArray(ts.caught) ? ts.caught : null;
    const parts = [];
    TIER_ORDER.forEach(tier => {
      const list = t.clues.filter(c => c.tier === tier);
      if (!list.length) return;
      if (tier === 'power') parts.push('<div class="powerline"><span>Power line · below here is worth 15</span></div>');
      parts.push(`<h3 class="bd-tier t-${tier}">${TIER[tier].label} <small>${TIER[tier].blurb}</small></h3>`);
      parts.push(`<ul class="bd-list">${list.map(c => {
        const state = caught ? (caught.includes(c.id) ? 'got' : 'miss') : '';
        const mark = state === 'got' ? '✓' : '';
        const label = state === 'got' ? 'In your notes' : state === 'miss' ? 'Not in your notes yet' : '';
        return `<li class="${state}"><span class="bd-mark" ${label ? `title="${label}" aria-label="${label}"` : 'aria-hidden="true"'}>${mark}</span><span class="bd-body"><span>${fmt(c.t)}</span><span class="bd-pills">${stockPill(c, t)}${rabbitPill(c)}</span></span></li>`;
      }).join('')}</ul>`);
    });
    return `<p class="sec-note">Easy on top, hard on the bottom, like Coach’s notebook. “Stock” counts come from ${esc(t.sample.note)}.</p><div class="bd">${parts.join('')}</div>`;
  }
  function lockedHtml(t) {
    const counts = TIER_ORDER.map(k => `${t.clues.filter(c => c.tier === k).length} ${TIER[k].short.toLowerCase()}`).join(', ');
    return `<div class="locked">${ICON.lock}<div><p><b>Locked until you write your notes.</b> Coach wants to see your own notes at practice, so make them first. Then check them here to see which clues you caught and which you missed.</p><p class="muted">${t.clues.length} clues waiting: ${counts}.</p></div></div>`;
  }
  const noteLines = s => String(s || '').split('\n').filter(l => l.replace(/[-—–_\s]/g, '').length > 1).length;
  function viewTopic(t) {
    const ts = TSR(t.id), b = ts.buzz, heard = b.p + b.t + b.n + b.miss, id = esc(t.id);
    show('topic', `<div class="page">
      <header class="topic-head">
        <p class="eyebrow">${esc(t.category)}${t.qbCategory && !t.qbCategory.endsWith(t.category) ? ' · ' + esc(t.qbCategory) : ''}</p>
        <h1 class="display">${esc(t.name)}</h1>
        <p class="kicker">${fmt(t.kicker)} · ${fmt(t.dates)}</p>
        <div class="answer-chip"><span class="answer-tag">Answer line</span><span>${t.answerHtml}</span></div>
        <div class="row"><button class="btn btn-buzz" data-act="buzz-topic" data-id="${id}">${ICON.bell}Buzz these ${t.tossups.length}</button><button class="btn" data-act="cards-topic" data-id="${id}">${ICON.cards}Flashcards</button>
          ${myBtnHtml(t.id)}</div>
      </header>
      <ol class="steps" id="steps" aria-label="Coach’s routine for this topic">${stepsHtml(t)}</ol>

      <section class="sec" id="s-learn">
        <p class="sec-eyebrow">Step 1 · Learn</p>
        <h2>The Briefing</h2>
        <p class="lead">${fmt(t.briefing)}</p>
        ${mediaHtml(t)}
      </section>

      <section class="sec" id="s-search">
        <p class="sec-eyebrow">Step 2 · Search</p>
        <h2>Coach’s QBReader search</h2>
        <div class="qbsearch">
          <dl class="qb-fields">
            <div><dt>Search for</dt><dd><code>${esc(t.qb.q)}</code></dd></div>
            <div><dt>Difficulty</dt><dd>Middle School + Easy High School</dd></div>
            <div><dt>Search in</dt><dd>Answer only</dd></div>
            <div><dt>Type</dt><dd>Tossups</dd></div>
            <div><dt>Filter</dt><dd>Power-marked tossups only</dd></div>
          </dl>
          <div class="qb-side">
            <a class="btn btn-pen" href="https://www.qbreader.org/db/" target="_blank" rel="noopener" data-act="qb" data-id="${id}">Open QBReader ↗</a>
            <p class="qb-found">When we checked, this search found <b>${esc(t.qb.found)}</b> tossups.</p>
            ${t.freq ? `<p class="qb-freq">${freqLine(t)}</p>` : ''}
            <p class="qb-tip">${fmt(t.qb.tip)}</p>
          </div>
        </div>
      </section>

      <section class="sec" id="s-read">
        <p class="sec-eyebrow">Step 3 · Read</p>
        <h2>QBReader Simulation</h2>
        <p class="sec-note">15 original practice tossups in QBReader format. <b>Bold text is the power zone:</b> buzz before the (*) and a right answer is worth 15 points instead of 10. Tap the speaker to hear one read aloud.</p>
        <div class="tu-tools"><button class="btn btn-sm" data-act="toggle-answers" aria-pressed="false">Hide answer lines</button><button class="btn btn-sm" data-act="read-done" data-id="${id}">I read all 15</button></div>
        <div class="tu-list" id="tuList">${t.tossups.map((tu, i) => tuCard(t, tu, i)).join('')}</div>
      </section>

      <section class="sec" id="s-notes">
        <p class="sec-eyebrow">Step 4 · Notes</p>
        <h2>My Notes</h2>
        <p class="sec-note">Do it Coach’s way: one clue per line, easy clues at the top, hard clues at the bottom, and a line where the power clues start. Write at least 5 clues to unlock the Clue Breakdown. Notes save as you type.</p>
        <div class="notebook">
          <div class="nb-head"><span class="nb-title">${esc(t.name)}</span><span class="nb-count" id="nbCount">${plural(noteLines(ts.notes), 'clue')}</span></div>
          <textarea id="notes-${id}" class="nb-text" data-id="${id}" spellcheck="true" aria-label="My notes for ${esc(t.name)}" placeholder="One clue per line.&#10;Easy clues at the top...&#10;&#10;— power line —&#10;Hard clues at the bottom...">${esc(ts.notes)}</textarea>
        </div>
        <div class="row"><button class="btn btn-pen" data-act="check" data-id="${id}">Check my notes</button><button class="btn btn-ghost" data-act="paper" data-id="${id}">I wrote mine on paper</button></div>
        <div id="checkResult"></div>
      </section>

      <section class="sec" id="s-check">
        <p class="sec-eyebrow">Check your notes</p>
        <h2>Clue Breakdown</h2>
        <div id="breakdown">${ts.unlocked ? breakdownHtml(t) : lockedHtml(t)}</div>
      </section>

      <section class="sec" id="s-trap">
        <p class="sec-eyebrow">Don’t get burned</p>
        <h2>Buzzer Trap</h2>
        <div class="trap"><div class="trap-band"><span>Buzzer trap</span></div>
          <div class="trap-body"><h3>${esc(t.trap.title)}</h3><p>${fmt(t.trap.body)}</p><p class="trap-fix"><b>How to beat it:</b> ${fmt(t.trap.fix)}</p><p class="trap-line">${t.trap.line}</p></div>
        </div>
      </section>

      <section class="sec" id="s-drill">
        <p class="sec-eyebrow">Step 5 · Drill</p>
        <h2>Drill it</h2>
        <div class="drill-grid">
          <div class="drill-card"><h3>Buzz Mode</h3><p>Play these 15 tossups like a match. Try to buzz inside the bold power zone.</p>
            <p class="drill-stat">${heard ? `Your record: ${b.p} powers, ${b.t} tens, ${b.n} negs` : 'No buzzes yet'}</p>
            <button class="btn btn-buzz" data-act="buzz-topic" data-id="${id}">${ICON.bell}Buzz this topic</button></div>
          <div class="drill-card"><h3>Flashcards</h3><p>Fill-in-the-blank cards for every clue, plus a “recite every clue” card.</p>
            <p class="drill-stat">${pct(mastery(t))} mastered</p>
            <button class="btn" data-act="cards-topic" data-id="${id}">${ICON.cards}Study the cards</button></div>
        </div>
        <p class="sec-note">When you have a few topics done, play Buzz Mode with <b>All topics</b>. Mixed questions are harder, just like a real match.</p>
      </section>
    </div>`);
  }
  function checkNotes(t) {
    if (!t || !t.clues) return;
    const ts = TS(t.id), box = $('#checkResult');
    const lines = noteLines(ts.notes);
    if (lines < 5) {
      if (box) box.innerHTML = `<p class="check-result warn">Write at least 5 clues first. You have ${lines} so far.</p>`;
      return;
    }
    const got = catches(ts.notes, t);
    const first = !ts.xpNotes;
    ts.caught = got; ts.unlocked = true; ts.paper = false; ts.xpNotes = true;
    touch(first ? 25 : 0);
    const bd = $('#breakdown'); if (bd) bd.innerHTML = breakdownHtml(t);
    refreshSteps(t);
    const miss = t.clues.length - got.length;
    if (box) box.innerHTML = `<p class="check-result">You caught <b>${got.length} of ${t.clues.length}</b> clues${first ? ' · +25 XP' : ''}. ${miss ? 'The clues with an empty circle are not in your notes yet. Add the ones you want, then check again.' : 'You got every single one!'}</p>`;
    beep('good');
    const target = $('#s-check'); if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
  function paperUnlock(t) {
    if (!t || !t.clues) return;
    const ts = TS(t.id), first = !ts.xpNotes;
    ts.unlocked = true; ts.paper = true; ts.caught = null; ts.xpNotes = true;
    touch(first ? 25 : 0);
    const bd = $('#breakdown'); if (bd) bd.innerHTML = breakdownHtml(t);
    refreshSteps(t);
    const box = $('#checkResult');
    if (box) box.innerHTML = `<p class="check-result">Breakdown unlocked${first ? ' · +25 XP' : ''}. Compare it with your notebook and add any clues you missed.</p>`;
    const target = $('#s-check'); if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  /* ---------- BUZZ MODE ---------- */
  // The round's queue is built from the index (topic id + tossup number); each question's topic is
  // loaded when it comes up, and the next one is fetched in the background so play feels instant.
  const BZ = { q: [], i: 0, cur: null, words: [], pEnd: 0, shown: 0, phase: 'idle', timers: new Set(), score: 0, p: 0, t: 0, n: 0, log: [], buzzAt: -1, power: false, interrupted: false, prompted: false, last: null, token: null, wait: null, pre: null };
  function later(fn, ms) { const id = setTimeout(() => { BZ.timers.delete(id); fn(); }, ms); BZ.timers.add(id); return id; }
  function every(fn, ms) { const id = setInterval(fn, ms); BZ.timers.add(id); return id; }
  function clearAll() { BZ.timers.forEach(id => { clearTimeout(id); clearInterval(id); }); BZ.timers.clear(); }
  function stopBuzz() { clearAll(); BZ.token = null; BZ.wait = null; if (BZ.phase !== 'idle') hush(); BZ.phase = 'idle'; }

  const seg = (act, value, opts) => `<div class="seg" role="group">${opts.map(([v, l]) => `<button class="${String(value) === String(v) ? 'on' : ''}" data-act="${act}" data-v="${v}" aria-pressed="${String(value) === String(v)}">${l}</button>`).join('')}</div>`;
  function viewBuzz() {
    const s = S.settings;
    s.pool = normalizePoolValue(s.pool);
    const canSpeak = speechAvailable();
    show('buzz', `<div class="page">
      <header class="topic-head">
        <p class="eyebrow">Practice match</p>
        <h1 class="display">Buzz Mode</h1>
        <p class="kicker">Each tossup appears one word at a time, like a moderator reading a packet. Buzz the moment you know it.</p>
      </header>
      <section class="sec" id="bzSetup">
        <div class="rules">
          <div class="rule r-power"><b>+15</b>Power: right answer during the bold text, before the (*)</div>
          <div class="rule r-ten"><b>+10</b>Right answer after the power mark</div>
          <div class="rule r-neg"><b>−5</b>Neg: wrong answer before the question ends</div>
        </div>
        <div class="setup card">
          <div class="field"><label for="bzPool">Questions from</label>
            <select id="bzPool">${poolOptionsHtml(s.pool, { singleLabel: e => `${e.name} only` })}</select></div>
          <div class="field"><label for="bzCount">How many</label>
            <select id="bzCount">${['5', '10', '15', '20', 'all'].map(v => `<option value="${v}" ${s.count === v ? 'selected' : ''}>${v === 'all' ? 'All of them' : v + ' tossups'}</option>`).join('')}</select></div>
          <div class="field"><span class="label">Reading</span>${seg('bz-speak', s.speak && canSpeak ? 1 : 0, canSpeak ? [[0, 'Words on screen'], [1, 'Read aloud too']] : [[0, 'Words on screen']])}</div>
          <div class="field"><label for="bzSpeed">Reading speed: <span id="bzSpeedLbl">${s.wpm}</span> words per minute</label>
            <input id="bzSpeed" type="range" min="120" max="360" step="10" value="${s.wpm}"><span class="hint">A real moderator reads about 180–220.</span></div>
          <div class="field"><span class="label">Buzzer sound</span>${seg('bz-sound', s.sound ? 1 : 0, [[1, 'On'], [0, 'Off']])}</div>
        </div>
        <div class="row"><button class="btn btn-buzz" data-act="bz-start"${BUILT.length ? '' : ' disabled'}>${ICON.bell}Start the round</button><span class="muted">Press <span class="kbd">Space</span> to buzz, <span class="kbd">Enter</span> to answer, <span class="kbd">N</span> for the next tossup.</span></div>
      </section>
      <section class="stage" id="bzStage" hidden></section>
    </div>`);
    prepareQueue();
  }
  // Every tossup in the pool as {id, ix}: never heard first, then ones missed last time, then the rest,
  // in random order within each group (tossup counts come from the index, so nothing loads here).
  function buildQueue(ids, count) {
    const groups = [[], [], []];
    ids.forEach(id => {
      const n = ENTRY_BY_ID[id].tossups;
      for (let ix = 0; ix < n; ix++) {
        const r = S.tu[id + ':' + ix];
        groups[!r ? 0 : r.last === 'neg' || r.last === 'miss' || r.last === 'dead' ? 1 : 2].push({ id, ix });
      }
    });
    const pool = [].concat(...groups.map(shuffle));
    const n = count === 'all' ? pool.length : Math.min(parseInt(count, 10) || 10, pool.length);
    return pool.slice(0, n);
  }
  // Builds the next round's queue ahead of time and fetches its first topic, so Start is instant.
  // (Only the first: on a slow connection a second download would slow it down. Each question
  // prefetches the one after it once it starts.)
  function prepareQueue() {
    const s = S.settings;
    BZ.pre = { pool: s.pool, count: s.count, q: buildQueue(idsForPool(s.pool), s.count) };
    if (BZ.pre.q.length) prefetch([BZ.pre.q[0].id]);
  }
  function stageHtml() {
    return `<div class="scorebar"><div class="sb-left"><span>Tossup</span><b id="bzNum" class="tnum">1 / 1</b></div><div class="sb-score" id="bzScore" aria-label="Score">0</div><div class="sb-right"><span id="bzPTN" title="Powers / tens / negs">0/0/0</span><span class="lamp" aria-hidden="true"></span></div></div>
      <div class="row between"><span class="zone" id="bzZone">Get ready…</span><button class="btn btn-sm btn-ghost" data-act="bz-quit">End round</button></div>
      <div class="reader" id="bzReader"><span class="tu-label" id="bzLabel"></span><span id="bzText"></span><span class="cursor" id="bzCursor" aria-hidden="true"></span></div>
      <div class="bar" id="bzDead" hidden><span></span></div>
      <div class="answer-row" id="bzAnswerRow" hidden>
        <label for="bzAnswer">Your answer</label>
        <p class="prompt-note" id="bzPrompt" hidden>Prompt: can you be more specific?</p>
        <div class="answer-input"><input id="bzAnswer" type="text" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="Type it, then press Enter"><button class="btn btn-pen" data-act="bz-submit">Submit</button></div>
        <div class="bar urgent" id="bzClock"><span></span></div>
      </div>
      <div class="buzz-zone" id="bzBuzzZone"><button class="buzzer" id="bzBuzzer" data-act="bz-buzz" aria-label="Buzz in">BUZZ</button>
        <div class="buzz-help"><span>Press <span class="kbd">Space</span> or tap the buzzer when you know it.</span><span>Bold text is worth 15. A wrong buzz before the end costs 5.</span></div></div>
      <div class="verdict" id="bzVerdict" hidden aria-live="polite"></div>`;
  }
  function runBar(el, ms) { if (!el) return; el.hidden = false; el.classList.remove('run'); void el.offsetWidth; el.style.setProperty('--dur', ms + 'ms'); el.classList.add('run'); }
  function startBuzz() {
    const s = S.settings, pre = BZ.pre;
    stopBuzz();
    BZ.q = pre && pre.pool === s.pool && pre.count === s.count ? pre.q : buildQueue(idsForPool(s.pool), s.count);
    BZ.pre = null;
    BZ.i = 0; BZ.score = 0; BZ.p = BZ.t = BZ.n = 0; BZ.log = [];
    const setup = $('#bzSetup'), stage = $('#bzStage');
    if (!stage) return;
    if (setup) setup.hidden = true;
    stage.hidden = false; stage.innerHTML = stageHtml();
    if (document.activeElement && document.activeElement.blur) document.activeElement.blur();
    stage.scrollIntoView({ behavior: 'smooth', block: 'start' });
    loadQuestion();
  }
  function paintScore() {
    const num = $('#bzNum'); if (num) num.textContent = `${Math.min(BZ.i + 1, BZ.q.length)} / ${BZ.q.length}`;
    const sc = $('#bzScore'); if (sc) sc.textContent = String(BZ.score).replace('-', '−');
    const ptn = $('#bzPTN'); if (ptn) ptn.textContent = `${BZ.p}/${BZ.t}/${BZ.n}`;
  }
  // Resets the stage for question BZ.i: label, empty reader, hidden answer/verdict panels.
  function resetStage(zoneText, zoneCls) {
    const stage = $('#bzStage'); if (!stage) return false;
    stage.classList.remove('buzzed');
    paintScore();
    $('#bzLabel').textContent = `Tossup ${BZ.i + 1}`;
    $('#bzText').textContent = '';
    const z = $('#bzZone'); z.className = 'zone' + (zoneCls ? ' ' + zoneCls : ''); z.textContent = zoneText;
    $('#bzDead').hidden = true; $('#bzAnswerRow').hidden = true; $('#bzPrompt').hidden = true; $('#bzVerdict').hidden = true;
    $('#bzBuzzZone').hidden = false;
    return true;
  }
  function loadQuestion() {
    clearAll(); hush(); BZ.token = null; BZ.wait = null;
    if (BZ.i >= BZ.q.length) return finishBuzz(false);
    const { id, ix } = BZ.q[BZ.i], t = FULL.get(id);
    if (!t) return waitForQuestion(id);
    const tu = t.tossups[ix];
    if (!tu) { BZ.i++; return loadQuestion(); } // the topic changed since the round was set up
    BZ.cur = { t, tu, id, ix };
    const pw = words(tu.p), rw = words(tu.r);
    BZ.words = pw.concat(rw); BZ.pEnd = pw.length; BZ.shown = 0;
    BZ.buzzAt = -1; BZ.power = false; BZ.interrupted = false; BZ.prompted = false; BZ.last = null;
    if (!resetStage('Get ready…')) return;
    $('#bzCursor').hidden = false;
    $('#bzBuzzer').disabled = false;
    BZ.phase = 'countdown';
    later(() => {
      if (BZ.phase !== 'countdown') return;
      BZ.phase = 'reading'; updateZone();
      if (S.settings.speak && speechAvailable()) speakAll(); else readWords();
    }, 1000);
    const next = BZ.q[BZ.i + 1];
    if (next && !FULL.has(next.id)) prefetch([next.id]);
  }
  function waitForQuestion(id) {
    const wait = BZ.wait = {};
    BZ.phase = 'loading';
    if (!resetStage('Loading the next tossup…', 'dead')) return;
    $('#bzCursor').hidden = true;
    $('#bzBuzzer').disabled = true;
    loadTopics([id]).then(() => { if (BZ.wait === wait) loadQuestion(); }, err => {
      if (BZ.wait !== wait) return;
      BZ.wait = null; BZ.phase = 'error';
      const z = $('#bzZone'); if (z) z.textContent = 'Tossup didn’t load';
      const v = $('#bzVerdict');
      v.className = 'verdict v-error';
      v.innerHTML = loadErrorHtml(err, 'tossup', 'bz-retry', '<button class="btn btn-ghost" data-act="bz-quit">End round</button>');
      v.hidden = false; $('#bzBuzzZone').hidden = true;
    });
  }
  function updateZone() {
    const z = $('#bzZone'); if (!z) return;
    const inPower = BZ.shown <= BZ.pEnd;
    z.className = 'zone' + (inPower ? '' : ' off');
    z.textContent = inPower ? 'Power zone · 15 points' : '10-point zone';
  }
  function revealTo(n) {
    n = Math.min(n, BZ.words.length);
    if (n <= BZ.shown) return;
    const box = $('#bzText'); if (!box) return;
    let add = '';
    for (let k = BZ.shown; k < n; k++) add += (k ? ' ' : '') + BZ.words[k];
    box.appendChild(document.createTextNode(add));
    BZ.shown = n;
    updateZone();
  }
  function readWords() {
    const ms = 60000 / S.settings.wpm;
    every(() => {
      if (BZ.phase !== 'reading') return;
      revealTo(BZ.shown + 1);
      if (BZ.shown >= BZ.words.length) questionDone();
    }, ms);
  }
  function speakAll() {
    hush();
    try { speechSynthesis.resume(); } catch (e) { /* ignore */ }
    const chunks = []; let a = 0;
    BZ.words.forEach((w, k) => { if (/[.!?][”’")]*$/.test(w) || k === BZ.words.length - 1) { chunks.push([a, k]); a = k + 1; } });
    const voice = pickVoice(), rate = clamp(S.settings.wpm / 175, 0.6, 2), msPer = 60000 / S.settings.wpm;
    const token = {}; BZ.token = token; let started = false;
    chunks.forEach(([s, e], ci) => {
      const ws = BZ.words.slice(s, e + 1);
      const u = new SpeechSynthesisUtterance(ws.join(' '));
      if (voice) { u.voice = voice; u.lang = voice.lang; } else u.lang = 'en-US';
      u.rate = rate;
      const offs = []; let c = 0; ws.forEach(w => { offs.push(c); c += w.length + 1; });
      let sub = null;
      const stopSub = () => { if (sub) { clearInterval(sub); BZ.timers.delete(sub); sub = null; } };
      u.onstart = () => {
        if (BZ.token !== token || BZ.phase !== 'reading') return;
        started = true; revealTo(s + 1);
        sub = every(() => { if (BZ.phase === 'reading' && BZ.shown < e) revealTo(BZ.shown + 1); }, msPer);
      };
      u.onboundary = ev => {
        if (BZ.token !== token || BZ.phase !== 'reading') return;
        if (ev.name && ev.name !== 'word') return;
        let k = 0; while (k + 1 < offs.length && offs[k + 1] <= ev.charIndex) k++;
        revealTo(s + k + 1);
      };
      u.onend = () => {
        stopSub();
        if (BZ.token !== token || BZ.phase !== 'reading') return;
        revealTo(e + 1);
        if (ci === chunks.length - 1) questionDone();
      };
      u.onerror = ev => {
        stopSub();
        if (BZ.token !== token || BZ.phase !== 'reading') return;
        if (ev && (ev.error === 'interrupted' || ev.error === 'canceled')) return;
        speechFallback();
      };
      speechSynthesis.speak(u);
    });
    later(() => { if (!started && BZ.token === token && BZ.phase === 'reading') speechFallback(); }, 2500);
  }
  function speechFallback() {
    BZ.token = null; hush();
    toast('Read-aloud isn’t working here, so the words will appear on screen.');
    readWords();
  }
  function questionDone() {
    if (BZ.phase !== 'reading') return;
    clearAll(); BZ.token = null;
    BZ.phase = 'dead';
    const z = $('#bzZone'); if (z) { z.className = 'zone dead'; z.textContent = 'Question over · buzz now for 10'; }
    const c = $('#bzCursor'); if (c) c.hidden = true;
    runBar($('#bzDead'), 5000);
    later(() => { if (BZ.phase === 'dead') noBuzz(); }, 5000);
  }
  function buzz() {
    if (BZ.phase !== 'reading' && BZ.phase !== 'dead') return;
    BZ.interrupted = BZ.phase === 'reading' && BZ.shown < BZ.words.length;
    BZ.power = BZ.phase === 'reading' && BZ.shown <= BZ.pEnd;
    BZ.buzzAt = BZ.shown;
    clearAll(); BZ.token = null; hush();
    BZ.phase = 'answering';
    beep('buzz');
    const stage = $('#bzStage'); stage.classList.add('buzzed');
    $('#bzBuzzer').disabled = true;
    $('#bzDead').hidden = true; $('#bzCursor').hidden = true;
    $('#bzAnswerRow').hidden = false;
    const inp = $('#bzAnswer'); inp.value = ''; inp.focus();
    startAnswerClock();
  }
  function startAnswerClock() {
    runBar($('#bzClock'), 15000);
    later(() => { if (BZ.phase === 'answering') submitAnswer(true); }, 15000);
  }
  function submitAnswer(fromClock) {
    if (BZ.phase !== 'answering') return;
    const inp = $('#bzAnswer'), val = inp ? inp.value : '';
    const v = judge(val, BZ.cur.t);
    if (v === 'prompt' && !BZ.prompted && !fromClock) {
      BZ.prompted = true; clearAll();
      $('#bzPrompt').hidden = false; inp.value = ''; inp.focus();
      startAnswerClock();
      return;
    }
    clearAll();
    const right = v === 'right';
    record(right ? (BZ.power ? 'power' : 'ten') : (BZ.interrupted ? 'neg' : 'miss'), val);
  }
  function noBuzz() { BZ.buzzAt = -1; BZ.power = false; BZ.interrupted = false; record('dead', ''); }
  function record(kind, given) {
    const pts = PTS[kind], { id, ix } = BZ.cur, ts = TS(id), c = S.career;
    BZ.score += pts;
    if (kind === 'power') { BZ.p++; c.p++; ts.buzz.p++; }
    else if (kind === 'ten') { BZ.t++; c.t++; ts.buzz.t++; }
    else if (kind === 'neg') { BZ.n++; c.n++; ts.buzz.n++; }
    else ts.buzz.miss++;
    c.heard++;
    const key = id + ':' + ix, r = S.tu[key] || (S.tu[key] = { seen: 0, last: null });
    r.seen++; r.last = kind;
    ts.steps.drill = true;
    BZ.last = { kind, given, pts };
    BZ.log.push({ id, ix, kind, buzzAt: BZ.buzzAt, total: BZ.words.length });
    BZ.phase = 'judged';
    beep(kind === 'power' ? 'power' : kind === 'ten' ? 'good' : kind === 'neg' ? 'bad' : '');
    touch(Math.max(0, pts)); paintRailRow(id);
    paintVerdict();
  }
  function overrideRight() {
    const L = BZ.last;
    if (BZ.phase !== 'judged' || !L || (L.kind !== 'neg' && L.kind !== 'miss')) return;
    const { id, ix } = BZ.cur, ts = TS(id), c = S.career;
    BZ.score -= PTS[L.kind];
    if (L.kind === 'neg') { BZ.n--; c.n--; ts.buzz.n--; } else ts.buzz.miss--;
    const kind = BZ.power ? 'power' : 'ten';
    BZ.score += PTS[kind];
    if (kind === 'power') { BZ.p++; c.p++; ts.buzz.p++; } else { BZ.t++; c.t++; ts.buzz.t++; }
    S.tu[id + ':' + ix].last = kind;
    BZ.log[BZ.log.length - 1].kind = kind;
    BZ.last = { kind, given: L.given, pts: PTS[kind], overridden: true };
    touch(PTS[kind]);
    paintVerdict();
  }
  // "Sam Adams" on a John Adams tossup: is it the answer to another topic? Loaded topics get the real
  // answer checker; the rest are matched on their name and other spellings from the index.
  let nameIdx = null;
  function otherAnswer(given, curId) {
    for (const o of FULL.values()) if (o.id !== curId && judge(given, o) === 'right') return ENTRY_BY_ID[o.id] || o;
    if (!nameIdx) { nameIdx = new Map(); BUILT.forEach(e => [e.name].concat(e.aka).forEach(n => { const k = norm(n); if (k && !nameIdx.has(k)) nameIdx.set(k, e); })); }
    const hit = nameIdx.get(norm(given));
    return hit && hit.id !== curId && !FULL.has(hit.id) ? hit : null;
  }
  function fullQuestionHtml() {
    let html = '';
    const N = BZ.words.length;
    for (let k = 0; k < N; k++) {
      if (k === BZ.buzzAt) html += '<span class="bz-mark">BUZZ</span> ';
      const w = esc(BZ.words[k]);
      html += k < BZ.pEnd ? `<b>${w}</b>` : w;
      if (k === BZ.pEnd - 1) html += ' <b>(*)</b>';
      html += ' ';
    }
    if (BZ.buzzAt >= N) html += '<span class="bz-mark">BUZZ</span>';
    return html;
  }
  function paintVerdict() {
    const { t } = BZ.cur, L = BZ.last;
    paintScore();
    const titles = { power: 'Power!', ten: 'Correct', neg: 'Neg', miss: 'Not quite', dead: 'No buzz' };
    const ptsTxt = L.pts > 0 ? '+' + L.pts : L.pts < 0 ? '−' + Math.abs(L.pts) : '0 points';
    let other = '';
    if ((L.kind === 'neg' || L.kind === 'miss') && L.given) {
      const hit = otherAnswer(L.given, t.id);
      if (hit) other = `<p class="other-hint">“${esc(L.given)}” is the answer to a different question in your library (${esc(hit.name)}). Listen for the clues that point here instead.</p>`;
    }
    const canOverride = (L.kind === 'neg' || L.kind === 'miss') && L.given && L.given.trim();
    const lastQ = BZ.i >= BZ.q.length - 1;
    const v = $('#bzVerdict');
    v.className = `verdict v-${L.kind}`;
    v.innerHTML = `<div class="verdict-head"><span class="verdict-title">${titles[L.kind]}</span><span class="verdict-pts">${ptsTxt}</span>${L.overridden ? '<span class="pill pill-once">Changed to correct</span>' : ''}</div>
      <p class="said">${L.kind === 'dead' ? 'You didn’t buzz on this one.' : `You said: <b>${esc(L.given || '(nothing)')}</b>`}</p>
      <p class="said">Answer: <span class="trap-line">${t.answerHtml}</span></p>
      ${other}
      <div class="full-q">${fullQuestionHtml()}</div>
      <div class="row">
        <button class="btn btn-pen" data-act="bz-next">${lastQ ? 'See results' : 'Next tossup'} <span class="kbd">N</span></button>
        ${canOverride ? '<button class="btn btn-ghost" data-act="bz-right">I was right</button>' : ''}
      </div>`;
    v.hidden = false;
    $('#bzAnswerRow').hidden = true; $('#bzDead').hidden = true; $('#bzBuzzZone').hidden = true;
    const z = $('#bzZone'); if (z) { z.className = 'zone dead'; z.textContent = 'Tossup over'; }
    const nb = v.querySelector('[data-act="bz-next"]');
    if (nb) { try { nb.focus({ preventScroll: true }); } catch (e) { nb.focus(); } }
  }
  function nextQuestion() { if (BZ.phase !== 'judged') return; BZ.i++; loadQuestion(); }
  function finishBuzz(early) {
    const played = BZ.log.length;
    clearAll(); BZ.token = null; BZ.wait = null; hush();
    BZ.phase = 'done';
    if (played) { S.career.sessions++; S.career.best = Math.max(S.career.best, BZ.score); save(); }
    const stage = $('#bzStage'); if (!stage) return;
    stage.classList.remove('buzzed');
    const gets = BZ.log.filter(x => x.kind === 'power' || x.kind === 'ten');
    const earliest = gets.length ? Math.min(...gets.map(x => x.buzzAt / x.total)) : null;
    const missed = BZ.log.filter(x => x.kind !== 'power' && x.kind !== 'ten');
    const missedTopics = [...new Set(missed.map(x => x.id))];
    stage.innerHTML = `<div class="summary-hero">
        <div><div class="lbl">${early ? 'Round ended early' : 'Final score'}</div><div class="big">${String(BZ.score).replace('-', '−')}</div></div>
        <div><div class="line">${plural(BZ.p, 'power')} · ${plural(BZ.t, 'ten')} · ${plural(BZ.n, 'neg')}</div>
          <div class="line">${gets.length} of ${played} correct${earliest != null ? ` · earliest correct buzz ${pct(earliest)} of the way in` : ''}</div>
          <div class="lbl">Best round so far: ${S.career.best}</div></div>
      </div>
      ${missedTopics.length ? `<section class="sec"><h3 class="h3">Study these next</h3><ul class="missed">${missedTopics.map(id => { const tp = ENTRY_BY_ID[id], k = missed.filter(x => x.id === id).length; return `<li><span><b>${esc(tp ? tp.name : id)}</b> <span class="muted">· missed ${plural(k, 'tossup')}</span></span><button class="btn btn-sm" data-act="go" data-to="topic-${esc(id)}">Study</button></li>`; }).join('')}</ul></section>` : (played ? '<p class="check-result">You got every tossup in this round. Try a faster reading speed or more questions.</p>' : '')}
      <div class="row"><button class="btn btn-buzz" data-act="bz-again">${ICON.bell}Play again</button><button class="btn" data-act="bz-setup">Change settings</button><button class="btn btn-ghost" data-act="go" data-to="home">Home</button></div>`;
    paintPlayer();
    prepareQueue();
  }

  /* ---------- FLASHCARDS ---------- */
  // Single topics and small pools use every topic. A big pool gets a sample of FC_SAMPLE topics drawn
  // from a few content chunks, so a deck never downloads hundreds of topics; "reshuffle" draws again.
  const FC = { deck: [], i: 0, flipped: false, got: 0, missed: 0, ids: [], pool: null, poolN: 0, wait: null };
  const MODES = [['auto', 'Auto'], ['name', 'Name it'], ['fill', 'Fill it in'], ['recite', 'Recite'], ['mixed', 'Mixed']];
  function resolvedMode() { const m = S.settings.cardMode; return m === 'auto' ? (isMultiDeck(S.settings.deck) ? 'name' : 'fill') : m; }
  function viewCards() {
    const s = S.settings;
    s.deck = normalizePoolValue(s.deck);
    show('cards', `<div class="page">
      <header class="topic-head">
        <p class="eyebrow">Coach’s flashcard method</p>
        <h1 class="display">Flashcards</h1>
        <p class="kicker">One clue per card. Flip it, then sort it: “Got it” cards leave the pile, “Again” cards come back in a few turns.</p>
      </header>
      <div class="setup card">
        <div class="field"><label for="fcDeck">Deck</label>
          <select id="fcDeck">${poolOptionsHtml(s.deck)}</select><span class="hint" id="fcSample" hidden></span></div>
        <div class="field"><span class="label">Card type</span>${seg('fc-mode', s.cardMode, MODES)}<span class="hint" id="fcModeNote">${modeNote()}</span></div>
        <div class="field"><span class="label">Mastered cards</span>${seg('fc-mastered', s.withMastered ? 1 : 0, [[0, 'Skip them'], [1, 'Include them']])}</div>
      </div>
      <div class="fc-wrap" id="fcWrap"></div>
    </div>`);
    newDeck(false);
  }
  function modeNote() {
    const m = resolvedMode();
    return { name: 'See a clue, name the answer line.', fill: 'Fill in the missing word in each clue.', recite: 'See the answer line, recite every clue you know.', mixed: 'A mix of all three.' }[m];
  }
  // Up to FC_SAMPLE ids from a big pool: shuffle, group by content chunk, take a few chunks at random
  // (more only if they hold too few topics), then pick round-robin so the mix is even.
  function sampleIds(pool) {
    const groups = new Map();
    shuffle(pool.slice()).forEach(id => { const c = ENTRY_BY_ID[id].chunk; if (!groups.has(c)) groups.set(c, []); groups.get(c).push(id); });
    const order = shuffle([...groups.values()]), use = [];
    let have = 0;
    for (const g of order) { if (use.length >= FC_CHUNKS && have >= FC_SAMPLE) break; use.push(g); have += g.length; }
    const picked = [];
    for (let r = 0; picked.length < FC_SAMPLE && use.some(g => r < g.length); r++) use.forEach(g => { if (r < g.length && picked.length < FC_SAMPLE) picked.push(g[r]); });
    return picked;
  }
  function deckFor(ids) {
    const s = S.settings, mode = resolvedMode(), cards = [];
    ids.forEach(id => {
      const t = FULL.get(id); if (!t) return;
      if (mode !== 'recite') t.clues.forEach(c => cards.push({ id, cid: c.id, type: mode === 'mixed' ? (Math.random() < 0.5 ? 'name' : 'fill') : mode }));
      if (mode === 'recite' || mode === 'mixed') cards.push({ id, cid: '__recite', type: 'recite' });
    });
    return shuffle(s.withMastered ? cards : cards.filter(c => !(S.cards[c.id + ':' + c.cid] || {}).m));
  }
  function paintSampleNote() {
    const el = $('#fcSample'); if (!el) return;
    const big = FC.poolN > FC.ids.length, d = S.settings.deck;
    el.hidden = !big;
    if (!big) { el.innerHTML = ''; return; }
    const of = d === 'my' ? `your ${FC.poolN} ready topics` : d.startsWith('area:') ? `the ${FC.poolN} ready ${esc(d.slice(5))} topics` : `all ${FC.poolN} ready topics`;
    el.innerHTML = `A mix from ${FC.ids.length} of ${of} — <button class="linkish" data-act="fc-reshuffle">reshuffle for more</button>`;
  }
  function newDeck(resample) {
    const s = S.settings, pool = idsForPool(s.deck), inPool = new Set(pool);
    const same = FC.pool === s.deck && FC.poolN === pool.length && FC.ids.length > 0 && FC.ids.every(id => inPool.has(id))
      && (pool.length > FC_SAMPLE || FC.ids.length === pool.length);
    if (resample || !same) { FC.ids = pool.length > FC_SAMPLE ? sampleIds(pool) : pool.slice(); FC.pool = s.deck; FC.poolN = pool.length; }
    paintSampleNote();
    FC.deck = []; FC.i = 0; FC.flipped = false; FC.got = 0; FC.missed = 0;
    const wait = FC.wait = {};
    const deal = () => { FC.wait = null; FC.deck = deckFor(FC.ids); paintCard(); };
    if (FC.ids.every(id => FULL.has(id))) return deal();
    const w = $('#fcWrap');
    if (w) w.innerHTML = `<div class="loading fc-loading" role="status"><span class="loading-dot" aria-hidden="true"></span>Shuffling the deck…</div>`;
    loadTopics(FC.ids).then(() => { if (FC.wait === wait) deal(); }, err => {
      if (FC.wait !== wait) return;
      FC.wait = null;
      const box = $('#fcWrap');
      if (box) box.innerHTML = loadErrorHtml(err, 'deck', 'fc-retry');
    });
  }
  const tierPill = tier => `<span class="pill pill-tier t-${tier}">${TIER[tier].short}</span>`;
  function faces(card) {
    const t = FULL.get(card.id);
    if (card.type === 'recite') {
      const list = TIER_ORDER.map(tier => `<li class="tierhead">${TIER[tier].label}</li>` + t.clues.filter(c => c.tier === tier).map(c => `<li>${fmt(c.t)}</li>`).join('')).join('');
      return {
        tall: true,
        front: `<p class="fc-kicker">Recite every clue you know</p><p class="fc-big">${esc(t.name)}</p><p class="fc-hint">Say them out loud, easy to hard, then flip and count how many you got.</p>`,
        back: `<p class="fc-kicker">${t.clues.length} clues · ${esc(t.name)}</p><ol class="fc-list">${list}</ol>`
      };
    }
    const c = t.clues.find(x => x.id === card.cid);
    if (card.type === 'fill') {
      const z = cloze(c);
      if (z) return {
        front: `<p class="fc-kicker">${tierPill(c.tier)} ${esc(t.name)}</p><p class="fc-clue">${esc(z.before)}<span class="blank" aria-hidden="true">${esc(z.term)}</span><span class="sr-only">blank</span>${esc(z.after)}</p><p class="fc-hint">Fill in the blank, then flip.</p>`,
        back: `<p class="fc-kicker">${tierPill(c.tier)} The missing word</p><p class="fc-big">${esc(z.term)}</p><p class="fc-clue small">${esc(z.before)}<b>${esc(z.term)}</b>${esc(z.after)}</p>`
      };
    }
    return {
      front: `<p class="fc-kicker">${tierPill(c.tier)} Which answer line?</p><p class="fc-clue">${fmt(c.t)}</p><p class="fc-hint">Say the answer, then flip.</p>`,
      back: `<p class="fc-kicker">${esc(t.category)}</p><p class="fc-big">${esc(t.name)}</p><p class="trap-line">${t.answerHtml}</p><p class="fc-clue small">${fmt(c.t)}</p>`
    };
  }
  function paintCard() {
    const w = $('#fcWrap'); if (!w) return;
    const note = $('#fcModeNote'); if (note) note.textContent = modeNote();
    const sampled = FC.poolN > FC.ids.length;
    if (!FC.deck.length) {
      w.innerHTML = `<div class="empty"><h3>Every card in this deck is mastered.</h3><p class="muted">Include mastered cards to review them${sampled ? ', reshuffle for other topics,' : ''} or pick another deck.</p><div class="row"><button class="btn btn-pen" data-act="fc-mastered" data-v="1">Review mastered cards</button>${sampled ? '<button class="btn" data-act="fc-reshuffle">Reshuffle</button>' : ''}</div></div>`;
      return;
    }
    if (FC.i >= FC.deck.length) {
      w.innerHTML = `<div class="empty"><h3>Pile cleared!</h3><p class="muted">${plural(FC.got, 'card')} marked “Got it” this time${FC.got ? ` · +${FC.got * 2} XP` : ''}.</p><div class="row"><button class="btn btn-pen" data-act="fc-new">New pile</button><button class="btn" data-act="go" data-to="buzz">Try Buzz Mode</button></div></div>`;
      return;
    }
    const card = FC.deck[FC.i], f = faces(card), left = FC.deck.length - FC.i;
    w.innerHTML = `<div class="fc-status"><span>${plural(left, 'card')} left in this pile</span><span>Got it: ${FC.got} · Again: ${FC.missed}</span></div>
      <div class="fc-scene"><div class="fc-card ${f.tall ? 'tall' : ''}" id="fcCard" data-act="fc-flip" role="button" tabindex="0" aria-label="Flashcard. Press Space to flip.">
        <div class="fc-face fc-front">${f.front}</div><div class="fc-face fc-back" aria-hidden="true">${f.back}</div></div></div>
      <div class="fc-actions"><button class="btn fc-again" data-act="fc-rate" data-v="0">Again <span class="kbd">1</span></button><button class="btn fc-flip" data-act="fc-flip">Flip <span class="kbd">Space</span></button><button class="btn fc-got" data-act="fc-rate" data-v="1">Got it <span class="kbd">2</span></button></div>`;
  }
  function flip() {
    const el = $('#fcCard'); if (!el) return;
    FC.flipped = !FC.flipped;
    el.classList.toggle('flipped', FC.flipped);
    const front = el.querySelector('.fc-front'), back = el.querySelector('.fc-back');
    if (front) front.setAttribute('aria-hidden', String(FC.flipped));
    if (back) back.setAttribute('aria-hidden', String(!FC.flipped));
  }
  function rateCard(got) {
    if (FC.wait || FC.i >= FC.deck.length) return;
    if (!FC.flipped) { flip(); return; }
    const card = FC.deck[FC.i], key = card.id + ':' + card.cid;
    const r = S.cards[key] || (S.cards[key] = { m: false, n: 0 });
    r.n++; r.t = Date.now();
    TS(card.id).steps.drill = true;
    if (got) { r.m = true; FC.got++; cardsChanged(); touch(2); }
    else { r.m = false; FC.missed++; cardsChanged(); FC.deck.splice(Math.min(FC.deck.length, FC.i + 4), 0, Object.assign({}, card)); save(); }
    paintRailRow(card.id);
    FC.i++; FC.flipped = false;
    paintCard();
  }

  /* ---------- STATS ---------- */
  const toB64 = s => { const bytes = new TextEncoder().encode(s); let bin = ''; bytes.forEach(b => { bin += String.fromCharCode(b); }); return btoa(bin); };
  const fromB64 = s => { const bin = atob(String(s).replace(/\s+/g, '')); return new TextDecoder().decode(Uint8Array.from(bin, ch => ch.charCodeAt(0))); };
  const started = e => stepsDone(e) > 0 || !!String(TSR(e.id).notes || '').trim();
  function statsRow(e) {
    const ts = TSR(e.id), b = ts.buzz, heard = b.p + b.t + b.n + b.miss;
    const caught = Array.isArray(ts.caught) ? `${ts.caught.length} of ${e.clues}` : ts.paper ? 'On paper' : '—';
    return `<tr><td><a class="stats-topic" href="#topic-${esc(e.id)}">${esc(e.name)}</a></td><td>${stepsDone(e)} of 5</td><td>${caught}</td><td>${pct(mastery(e))}</td><td>${b.p}/${b.t}/${b.n}</td><td>${heard ? Math.round(((b.p + b.t) / heard) * 100) + '%' : '—'}</td></tr>`;
  }
  function viewStats() {
    const lv = level(S.xp), c = S.career;
    const gets = c.p + c.t, acc = c.heard ? Math.round((gets / c.heard) * 100) : 0;
    const mine = myBuiltEntries(), scope = mine.length ? mine : BUILT;
    // Small sets list every topic; big ones (a 450-topic list, or every built topic) list the started ones.
    const listAll = scope.length <= STATS_ALL, scopeIds = new Set(scope.map(e => e.id));
    let shown = 0;
    const statsSections = AREAS.map(a => {
      const rows = BUILT_BY_AREA[a.name].filter(e => scopeIds.has(e.id) && (listAll || started(e)));
      shown += rows.length;
      return rows.length ? `<div class="stats-area"><h3 class="h3">${esc(a.name)}</h3>
        <div class="table-wrap"><table><thead><tr><th>Topic</th><th>Steps</th><th>Clues in notes</th><th>Cards mastered</th><th>P/T/N</th><th>Correct</th></tr></thead>
        <tbody>${rows.map(statsRow).join('')}</tbody></table></div>
      </div>` : '';
    }).join('');
    const what = mine.length ? 'My topics' : 'Every built topic';
    const note = listAll ? `${what}, grouped by area.`
      : shown ? `${what} that you’ve started, grouped by area. ${plural(scope.length - shown, 'more topic')} ${scope.length - shown === 1 ? 'hasn’t' : 'haven’t'} been started yet.`
        : `You haven’t started any of these ${scope.length} topics yet. Open one from Home or the Topics page to begin.`;
    show('stats', `<div class="page">
      <header class="topic-head"><p class="eyebrow">My scoresheet</p><h1 class="display">My Stats</h1><p class="kicker">Level ${lv.n} · ${esc(lv.title)} · ${S.xp} XP</p></header>
      <section class="sec"><div class="stat-grid">
        <div class="stat"><b>${streakNow()}</b><span>Day streak</span></div>
        <div class="stat"><b>${c.p}</b><span>Powers (15 points)</span></div>
        <div class="stat"><b>${c.t}</b><span>Tens (10 points)</span></div>
        <div class="stat"><b>${c.n}</b><span>Negs (−5 points)</span></div>
        <div class="stat"><b>${acc}%</b><span>Correct, of ${plural(c.heard, 'tossup')} heard</span></div>
        <div class="stat"><b>${c.best}</b><span>Best round score</span></div>
      </div></section>
      <section class="sec"><h2>By topic</h2>
        <p class="sec-note">${note}</p>
        ${statsSections}
      </section>
      <section class="sec"><h2>Notes for Coach</h2>
        <p class="sec-note">Coach wants to see your notes at practice. Copy all of them at once, then paste them into an email or a document. Or bring your notebook.</p>
        <div class="row"><button class="btn btn-pen" data-act="copy-notes">Copy all my notes</button></div>
        <textarea id="notesOut" class="code" readonly hidden aria-label="All my notes"></textarea>
      </section>
      <section class="sec"><h2>Back up your progress</h2>
        <p class="sec-note">Your progress lives in this browser on this device. To keep a backup or move to another device, copy your backup code and paste it under “Restore” there.</p>
        <div class="row"><button class="btn" data-act="backup">Copy my backup code</button></div>
        <textarea id="backupOut" class="code" readonly hidden aria-label="Backup code"></textarea>
        <div class="field"><label for="restoreIn">Restore from a backup code</label><textarea id="restoreIn" class="code" placeholder="Paste a backup code here"></textarea></div>
        <div class="row"><button class="btn" data-act="restore">Restore</button></div>
        <div id="restoreMsg"></div>
      </section>
      <section class="sec"><h2>Start over</h2>
        <p class="sec-note">Erase all XP, notes, flashcard piles, and Buzz Mode stats on this device.</p>
        <div id="resetBox"><button class="btn" data-act="reset">Erase my progress…</button></div>
      </section>
    </div>`);
  }
  async function copyOut(text, area, okMsg) {
    try { await navigator.clipboard.writeText(text); toast(okMsg); if (area) { area.hidden = false; area.value = text; } }
    catch (e) { if (area) { area.hidden = false; area.value = text; area.focus(); area.select(); } toast('Select the text and press Ctrl+C (or ⌘C) to copy.'); }
  }
  let pendingRestore = null;

  /* ---------- events ---------- */
  const confirmClearHtml = () => '<button class="btn btn-sm btn-ghost" data-act="my-clear">Clear my topics</button>';
  function selectIds(ids, on) {
    const set = mySet();
    ids.forEach(x => (on ? set.add(x) : set.delete(x)));
    S.my = [...set];
    afterMyChange(ids);
  }
  // Ids an area's Select all / Clear acts on: its search matches while searching, else the whole area.
  const areaTargetIds = area => (areaMatches(area, searchQ()) || BY_AREA[area] || []).map(e => e.id);
  document.addEventListener('click', e => {
    const el = e.target.closest('[data-act]'); if (!el) return;
    const act = el.dataset.act, id = el.dataset.id, t = id ? FULL.get(id) || ENTRY_BY_ID[id] || null : null;
    switch (act) {
      case 'go': go(el.dataset.to); break;
      case 'menu': if ($('#app').classList.toggle('menu-open')) requestAnimationFrame(revealRailItem); break;
      case 'menu-close': closeMenu(); break;
      case 'theme': cycleTheme(); break;
      case 'reload': location.reload(); break;
      case 'topic-retry': route(); break;
      case 'step': { if (!t) break; const ts = TS(t.id), k = el.dataset.step; ts.steps[k] = !ts.steps[k]; if (ts.steps[k]) touch(0); else save(); refreshSteps(t); break; }
      case 'media': if (t) markStep(t, 'learn'); break;
      case 'qb': if (t) markStep(t, 'search'); break;
      case 'read-done': if (!t) break; markStep(t, 'read'); toast('Step 3 done. Now write your notes.'); { const n = $('#s-notes'); if (n) n.scrollIntoView({ behavior: 'smooth', block: 'start' }); } break;
      case 'toggle-answers': { const list = $('#tuList'); if (!list) break; const on = list.classList.toggle('hide-answers'); el.textContent = on ? 'Show answer lines' : 'Hide answer lines'; el.setAttribute('aria-pressed', String(on)); break; }
      case 'say': if (t && t.tossups) sayTossup(t, parseInt(el.dataset.i, 10), el); break;
      case 'check': checkNotes(FULL.get(id)); break;
      case 'paper': paperUnlock(FULL.get(id)); break;
      case 'buzz-topic': S.settings.pool = id; S.settings.count = '15'; save(); go('buzz'); break;
      case 'buzz-all': S.settings.pool = 'all'; save(); go('buzz'); break;
      case 'buzz-my': S.settings.pool = 'my'; save(); go('buzz'); break;
      case 'cards-topic': S.settings.deck = id; S.settings.cardMode = 'auto'; save(); go('cards'); break;
      case 'my-toggle': {
        const on = !S.my.includes(id); setMine(id, on);
        el.textContent = on ? '✓ In my topics' : '+ My topics'; el.classList.toggle('btn-pen', on); el.setAttribute('aria-pressed', String(on));
        const hint = $('#upHint'); if (hint) hint.hidden = on;
        break;
      }
      case 'list-add': {
        const list = LISTS.find(l => String(l.n) === el.dataset.n); if (!list) break;
        const before = mySet().size;
        selectIds(list.ids, true);
        const added = mySet().size - before;
        toast(added ? `Added ${plural(added, 'topic')} to My topics.` : 'Those topics are already in My topics.');
        break;
      }
      case 'lists-toggle': {
        const grid = $('#listGrid'); if (!grid) break;
        TP.listsOpen = grid.hidden; grid.hidden = !TP.listsOpen;
        el.setAttribute('aria-expanded', String(TP.listsOpen)); el.textContent = TP.listsOpen ? 'Hide the lists' : `Show all ${LISTS.length}`;
        break;
      }
      case 'area-select-all': selectIds(areaTargetIds(el.dataset.area), true); break;
      case 'area-clear': selectIds(areaTargetIds(el.dataset.area), false); break;
      case 'my-clear': { const box = $('#myClearBox'); if (box) box.innerHTML = `<div class="confirm"><span>Clear all ${sanitizedMy().length} topics from My topics?</span><button class="btn btn-sm btn-buzz" data-act="my-clear-yes">Yes, clear</button><button class="btn btn-sm btn-ghost" data-act="my-clear-no">Cancel</button></div>`; break; }
      case 'my-clear-yes': { const ids = sanitizedMy(); S.my = []; afterMyChange(ids); toast('Cleared My topics.'); const box = $('#myClearBox'); if (box) box.innerHTML = confirmClearHtml(); break; }
      case 'my-clear-no': { const box = $('#myClearBox'); if (box) box.innerHTML = confirmClearHtml(); break; }
      case 'topics-area': { TP.area = el.dataset.area; $$('#areaChips .chip').forEach(b => { const on = b === el; b.classList.toggle('on', on); b.setAttribute('aria-pressed', String(on)); }); paintTopicsList(); break; }
      case 'ta-toggle': {
        const area = el.dataset.area, sec = el.closest('.topics-area');
        if (!sec || searchQ() || TP.area === area) break; // open while searching or filtered to this area
        TP.open[area] = !TP.open[area];
        paintArea(sec, '', mySet());
        break;
      }
      case 'ta-more': { const area = el.dataset.area, sec = el.closest('.topics-area'); TP.more[area] = true; if (sec) paintArea(sec, searchQ(), mySet()); break; }
      case 'browse-area': TP.area = el.dataset.area; TP.q = ''; go('topics'); break;
      case 'home-more': {
        const area = el.dataset.area, sec = $$('[data-home-area]').find(x => x.dataset.homeArea === area);
        homeMore[area] = true;
        if (sec) sec.outerHTML = homeAreaHtml(area, mySet());
        break;
      }
      case 'rail-toggle': {
        const area = el.dataset.area, nowOpen = el.getAttribute('aria-expanded') !== 'true';
        S.ui.railOpen[area] = nowOpen; save();
        el.setAttribute('aria-expanded', String(nowOpen));
        const body = $$('.lib-area-body').find(b => b.dataset.area === area);
        if (body) {
          body.hidden = !nowOpen;
          if (nowOpen && body.dataset.loaded !== '1') { body.innerHTML = railBodyHtml(area, currentTopicId()); body.dataset.loaded = '1'; }
        }
        break;
      }
      case 'rail-soon': setRailSoon(el.dataset.area, el.getAttribute('aria-expanded') !== 'true'); break;
      case 'bz-start': case 'bz-again': startBuzz(); break;
      case 'bz-setup': viewBuzz(); break;
      case 'bz-buzz': buzz(); break;
      case 'bz-submit': submitAnswer(false); break;
      case 'bz-next': nextQuestion(); break;
      case 'bz-right': overrideRight(); break;
      case 'bz-quit': finishBuzz(true); break;
      case 'bz-retry': if (BZ.phase === 'error') loadQuestion(); break;
      case 'bz-speak': S.settings.speak = el.dataset.v === '1'; save(); el.parentNode.querySelectorAll('button').forEach(b => { const on = b === el; b.classList.toggle('on', on); b.setAttribute('aria-pressed', String(on)); }); break;
      case 'bz-sound': S.settings.sound = el.dataset.v === '1'; save(); el.parentNode.querySelectorAll('button').forEach(b => { const on = b === el; b.classList.toggle('on', on); b.setAttribute('aria-pressed', String(on)); }); if (S.settings.sound) beep('good'); break;
      case 'fc-flip': flip(); break;
      case 'fc-rate': rateCard(el.dataset.v === '1'); break;
      case 'fc-new': newDeck(FC.poolN > FC.ids.length); break;
      case 'fc-reshuffle': newDeck(true); break;
      case 'fc-retry': newDeck(false); break;
      case 'fc-mode': S.settings.cardMode = el.dataset.v; save(); el.parentNode.querySelectorAll('button').forEach(b => { const on = b === el; b.classList.toggle('on', on); b.setAttribute('aria-pressed', String(on)); }); newDeck(false); break;
      case 'fc-mastered': S.settings.withMastered = el.dataset.v === '1'; save(); if (view === 'cards') viewCards(); break;
      case 'copy-notes': {
        const text = ENTRIES.filter(x => String(TSR(x.id).notes || '').trim()).map(x => `${x.name.toUpperCase()}\n${TSR(x.id).notes.trim()}\n`).join('\n');
        if (!text) { toast('No notes yet. Write some on a topic page first.'); break; }
        copyOut(text, $('#notesOut'), 'Notes copied. Paste them anywhere.'); break;
      }
      case 'backup': copyOut(toB64(JSON.stringify(S)), $('#backupOut'), 'Backup code copied.'); break;
      case 'restore': {
        const box = $('#restoreMsg'), raw = ($('#restoreIn') || {}).value || '';
        try {
          const obj = JSON.parse(fromB64(raw));
          if (!obj || obj.v !== 1 || typeof obj.xp !== 'number') throw new Error('bad');
          pendingRestore = obj;
          box.innerHTML = `<div class="confirm"><span>This replaces the progress on this device with the backup (${esc(obj.xp)} XP). Continue?</span><button class="btn btn-sm btn-pen" data-act="restore-yes">Yes, restore</button><button class="btn btn-sm btn-ghost" data-act="restore-no">Cancel</button></div>`;
        } catch (err) { box.innerHTML = '<p class="check-result warn">That code didn’t work. Copy the whole backup code again and paste it here.</p>'; }
        break;
      }
      case 'restore-yes': if (pendingRestore) { S = deepMerge(fresh(), pendingRestore); normalizeState(); pendingRestore = null; save(); applyTheme(); railStale = true; toast('Progress restored.'); viewStats(); } break;
      case 'restore-no': pendingRestore = null; { const box = $('#restoreMsg'); if (box) box.innerHTML = ''; } break;
      case 'reset': { const box = $('#resetBox'); box.innerHTML = '<div class="confirm"><span>Erase everything on this device? This can’t be undone.</span><button class="btn btn-sm btn-buzz" data-act="reset-yes">Yes, erase it</button><button class="btn btn-sm btn-ghost" data-act="reset-no">Keep my progress</button></div>'; break; }
      case 'reset-yes': { const theme = S.settings.theme, touched = S.settings.themeTouched; S = fresh(); S.settings.theme = theme; S.settings.themeTouched = touched; normalizeState(); save(); railStale = true; toast('Progress erased.'); viewStats(); break; }
      case 'reset-no': { const box = $('#resetBox'); box.innerHTML = '<button class="btn" data-act="reset">Erase my progress…</button>'; break; }
      default: break;
    }
  });
  document.addEventListener('change', e => {
    const el = e.target;
    if (el.id === 'bzPool') { S.settings.pool = el.value; save(); prepareQueue(); }
    else if (el.id === 'bzCount') { S.settings.count = el.value; save(); prepareQueue(); }
    else if (el.id === 'fcDeck') { S.settings.deck = el.value; save(); newDeck(true); }
    else if (el.classList && el.classList.contains('my-check')) { setMine(el.dataset.id, el.checked); }
  });
  document.addEventListener('input', e => {
    const el = e.target;
    if (el.id === 'bzSpeed') { S.settings.wpm = parseInt(el.value, 10) || 200; const l = $('#bzSpeedLbl'); if (l) l.textContent = S.settings.wpm; saveSoon(); }
    else if (el.classList && el.classList.contains('nb-text')) {
      const ts = TS(el.dataset.id); ts.notes = el.value; saveSoon();
      const cnt = $('#nbCount'); if (cnt) cnt.textContent = plural(noteLines(el.value), 'clue');
    }
    else if (el.id === 'topicsSearch') { TP.q = el.value; TP.more = {}; paintSearchSoon(); }
  });
  document.addEventListener('keydown', e => {
    const tag = (e.target.tagName || '').toLowerCase();
    const typing = tag === 'input' || tag === 'textarea' || tag === 'select' || e.target.isContentEditable;
    if (view === 'buzz') {
      if ((e.code === 'Space' || e.key === ' ') && !typing && (BZ.phase === 'reading' || BZ.phase === 'dead')) { e.preventDefault(); buzz(); return; }
      if (e.key === 'Enter' && e.target.id === 'bzAnswer' && BZ.phase === 'answering') { e.preventDefault(); submitAnswer(false); return; }
      if ((e.key === 'n' || e.key === 'N') && !typing && BZ.phase === 'judged') { e.preventDefault(); nextQuestion(); return; }
      if ((e.code === 'Space' || e.key === ' ') && !typing && tag !== 'button' && (BZ.phase === 'answering' || BZ.phase === 'judged' || BZ.phase === 'countdown' || BZ.phase === 'loading')) e.preventDefault();
    } else if (view === 'cards' && !typing) {
      if (e.code === 'Space' || e.key === ' ' || (e.key === 'Enter' && e.target.id === 'fcCard')) { e.preventDefault(); flip(); }
      else if (e.key === '1' || e.key === 'ArrowLeft') { e.preventDefault(); rateCard(false); }
      else if (e.key === '2' || e.key === 'ArrowRight') { e.preventDefault(); rateCard(true); }
    }
    if (e.key === 'Escape') closeMenu();
  });
  window.addEventListener('hashchange', route);
  window.addEventListener('pagehide', save);

  /* ---------- boot ---------- */
  const menuBtn = $('#menuBtn'); if (menuBtn) menuBtn.innerHTML = ICON.menu;
  applyTheme();
  route();
})();
