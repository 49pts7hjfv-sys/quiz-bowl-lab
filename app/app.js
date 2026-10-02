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

  /* ---------- data ---------- */
  const DATA = JSON.parse(document.getElementById('qb-data').textContent);
  const TOPICS = DATA.topics;
  const BY_ID = Object.fromEntries(TOPICS.map(t => [t.id, t]));
  const UPCOMING = DATA.upcoming || [];
  const UP_BY_ID = Object.fromEntries(UPCOMING.map(u => [u.id, u]));
  const AREAS = DATA.areas || [];
  const LISTS = DATA.lists || [];
  const SHORT_BY_AREA = Object.fromEntries(AREAS.map(a => [a.name, a.short || a.name]));
  // A short monogram for a topic that has none yet (upcoming stubs don't carry one).
  const STOPWORDS = new Set(['the', 'a', 'an', 'of', 'and']);
  function genMono(name) {
    const words = String(name).replace(/[^\w\s'-]/g, '').split(/\s+/).filter(w => w && !STOPWORDS.has(w.toLowerCase()));
    const pick = (words.length ? words : String(name).split(/\s+/)).slice(0, 2);
    return (pick.map(w => w[0]).join('').toUpperCase() || '?').slice(0, 3);
  }
  // Every topic (built + upcoming), grouped by area in display order, each a light descriptor.
  // Built topics keep their full object in BY_ID; look that up when more than id/name/category is needed.
  const BY_AREA = {}, ALL_ENTRIES = [], ENTRY_BY_ID = {}, TOPICS_BY_AREA = {};
  AREAS.forEach(a => {
    TOPICS_BY_AREA[a.name] = TOPICS.filter(t => t.category === a.name).sort((x, y) => x.order - y.order);
    const list = [
      ...TOPICS.filter(t => t.category === a.name).map(t => ({ id: t.id, name: t.name, category: a.name, order: t.order, built: true, mono: t.mono })),
      ...UPCOMING.filter(u => u.category === a.name).map(u => ({ id: u.id, name: u.name, category: a.name, order: u.order, built: false, mono: genMono(u.name) }))
    ].sort((x, y) => x.order - y.order);
    list.forEach(e => { ENTRY_BY_ID[e.id] = e; });
    BY_AREA[a.name] = list;
    ALL_ENTRIES.push(...list);
  });
  const BUILT_AREAS = AREAS.map(a => a.name).filter(name => (TOPICS_BY_AREA[name] || []).length > 0);
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
    chev: '<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg>'
  };

  /* ---------- tiny utilities ---------- */
  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => [...root.querySelectorAll(sel)];
  const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const fmt = s => esc(s).replace(/_([^_]+)_/g, '<i>$1</i>').replace(/\[“([^”]+)”\]/g, '<span class="pg">[“$1”]</span>');
  const shuffle = a => { for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  const clamp = (v, lo, hi) => Math.max(lo, Math.min(hi, v));
  const plural = (n, w) => `${n} ${w}${n === 1 ? '' : 's'}`;
  const pct = x => Math.round(x * 100) + '%';
  const mono = t => `<span class="mono${t.mono.length > 2 ? ' m3' : ''}">${esc(t.mono)}</span>`;

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
  // Keeps saved state valid as the topic set grows: fills in defaults for every built topic, and
  // drops any "my topics" id that no longer exists (e.g. a manifest id that was renamed or removed).
  function normalizeState() {
    TOPICS.forEach(t => { S.topics[t.id] = deepMerge(topicDefaults(), S.topics[t.id] || {}); });
    if (!Array.isArray(S.my)) S.my = [];
    S.my = S.my.filter(id => ENTRY_BY_ID[id]);
    if (!S.ui || typeof S.ui !== 'object') S.ui = { railOpen: {} };
    if (!S.ui.railOpen || typeof S.ui.railOpen !== 'object') S.ui.railOpen = {};
  }
  normalizeState();
  const storageOK = (() => { try { localStorage.setItem(KEY + '.probe', '1'); localStorage.removeItem(KEY + '.probe'); return true; } catch (e) { return false; } })();
  function save() { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) { /* ignore */ } }
  let saveTimer = null;
  const saveSoon = () => { clearTimeout(saveTimer); saveTimer = setTimeout(save, 350); };
  const TS = id => S.topics[id] || (S.topics[id] = topicDefaults());

  /* ---------- my topics ---------- */
  const sanitizedMy = () => S.my.filter(id => ENTRY_BY_ID[id]);
  const myEntries = () => { const set = new Set(sanitizedMy()); return ALL_ENTRIES.filter(e => set.has(e.id)); };
  const myBuiltTopics = () => { const set = new Set(sanitizedMy()); return TOPICS.filter(t => set.has(t.id)); };
  function setMine(id, on) {
    const set = new Set(sanitizedMy());
    if (on) set.add(id); else set.delete(id);
    S.my = [...set]; save();
    updateMyCount(); renderRail();
  }
  function updateMyCount() { const el = $('#mySelCount'); if (el) el.textContent = plural(sanitizedMy().length, 'topic') + ' selected'; }
  function refreshTopicsChecks(ids) { ids.forEach(id => { const el = document.getElementById('chk-' + id); if (el) el.checked = S.my.includes(id); }); updateMyCount(); }

  /* ---------- buzz/flashcard pools: 'my' | 'all' | 'area:<name>' | '<topic id>' ---------- */
  function normalizePoolValue(v) {
    if (v === 'all') return 'all';
    if (v === 'my') return myBuiltTopics().length ? 'my' : 'all';
    if (typeof v === 'string' && v.startsWith('area:')) return BUILT_AREAS.includes(v.slice(5)) ? v : 'all';
    return BY_ID[v] ? v : 'all';
  }
  function idsForPool(v) {
    if (v === 'all') return TOPICS.map(t => t.id);
    if (v === 'my') { const ids = myBuiltTopics().map(t => t.id); return ids.length ? ids : TOPICS.map(t => t.id); }
    if (typeof v === 'string' && v.startsWith('area:')) return (TOPICS_BY_AREA[v.slice(5)] || []).map(t => t.id);
    return BY_ID[v] ? [v] : TOPICS.map(t => t.id);
  }
  const isMultiDeck = v => v === 'all' || v === 'my' || (typeof v === 'string' && v.startsWith('area:'));
  // Shared <option>/<optgroup> markup for the Buzz pool and Flashcards deck selects.
  function poolOptionsHtml(selected, opts) {
    const o = Object.assign({ myLabel: 'My topics (mixed)', allLabel: 'All topics (mixed)', areaLabel: n => `All ${n} (mixed)`, singleLabel: t => t.name }, opts || {});
    let html = '';
    if (myBuiltTopics().length) html += `<option value="my" ${selected === 'my' ? 'selected' : ''}>${esc(o.myLabel)}</option>`;
    html += `<option value="all" ${selected === 'all' ? 'selected' : ''}>${esc(o.allLabel)}</option>`;
    BUILT_AREAS.forEach(name => { html += `<option value="area:${esc(name)}" ${selected === 'area:' + name ? 'selected' : ''}>${esc(o.areaLabel(name))}</option>`; });
    BUILT_AREAS.forEach(name => {
      html += `<optgroup label="${esc(name)}">`;
      TOPICS_BY_AREA[name].forEach(t => { html += `<option value="${t.id}" ${selected === t.id ? 'selected' : ''}>${esc(o.singleLabel(t))}</option>`; });
      html += `</optgroup>`;
    });
    return html;
  }

  /* ---------- QBReader frequency list ---------- */
  const freqLine = t => t.freq ? `#${t.freq.rank} on QBReader’s ${esc(t.freq.list)} frequency list · ${plural(t.freq.count, 'tossup')} (Middle School + Easy High School)` : '';
  const freqBadge = t => t.freq ? `<span class="pill pill-freq" title="${esc(freqLine(t))}">#${t.freq.rank}</span>` : '';
  function fmtDate(iso) { try { return new Date(iso + 'T00:00:00').toLocaleDateString(undefined, { year: 'numeric', month: 'short', day: 'numeric' }); } catch (e) { return iso; } }

  /* ---------- XP, levels, streaks ---------- */
  const dayKey = (d = new Date()) => `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
  const daysBetween = (a, b) => Math.round((new Date(b + 'T12:00:00') - new Date(a + 'T12:00:00')) / 864e5);
  function touch(xp = 0) {
    const today = dayKey(), st = S.streak;
    if (st.last !== today) { st.count = st.last && daysBetween(st.last, today) === 1 ? st.count + 1 : 1; st.last = today; }
    const before = level(S.xp).n;
    if (xp > 0) S.xp += xp;
    save(); renderRail();
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

  /* ---------- per-topic progress ---------- */
  const cardKeys = t => t.clues.map(c => `${t.id}:${c.id}`).concat(`${t.id}:__recite`);
  const mastery = t => { const keys = cardKeys(t); return keys.filter(k => S.cards[k] && S.cards[k].m).length / keys.length; };
  function stepDone(t, k) {
    const ts = TS(t.id);
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
  let view = 'home';
  const main = () => $('#main');
  function go(h) { if (location.hash === '#' + h) route(); else location.hash = h; }
  function route() {
    stopBuzz(); hush(); if (saying) { saying.btn.classList.remove('on'); saying = null; }
    const h = (location.hash || '').replace(/^#/, '');
    if (h.startsWith('topic-')) {
      const id = h.slice(6);
      if (BY_ID[id]) return viewTopic(BY_ID[id]);
      if (UP_BY_ID[id]) return viewUpcoming(UP_BY_ID[id]);
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
    closeMenu(); renderRail();
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

  // Rail library: "my topics" grouped by area (open by default) when any are picked, else every
  // area (collapsed by default) so the rail stays browsable before a student has picked anything.
  // Collapsed areas render only their header; a toggle lazily fills in that one area's rows (see
  // the 'rail-toggle' action), so 215 topics never cost more than the areas actually opened.
  let railPending = {};
  function railRowHtml(e, curId) {
    if (e.built) {
      const t = BY_ID[e.id];
      return `<button class="lib-item ${curId === e.id ? 'is-active' : ''}" data-act="go" data-to="topic-${t.id}">
        ${mono(t)}
        <span class="lib-name">${esc(t.name)}<small>${stepsDone(t)} of 5 steps</small></span>
        ${ring(mastery(t))}
      </button>`;
    }
    return `<div class="lib-item is-upcoming">${mono(e)}<span class="lib-name">${esc(e.name)}<small>Not written yet</small></span><span class="tag-soon">Soon</span></div>`;
  }
  const railAreaItemsHtml = (entries, curId) => entries.map(e => railRowHtml(e, curId)).join('');
  function railGroups() {
    const mine = sanitizedMy();
    if (mine.length) {
      const set = new Set(mine);
      return AREAS.map(a => a.name).filter(name => (BY_AREA[name] || []).some(e => set.has(e.id)))
        .map(name => ({ area: name, entries: BY_AREA[name].filter(e => set.has(e.id)) }));
    }
    return AREAS.map(a => ({ area: a.name, entries: BY_AREA[a.name] || [] }));
  }
  function renderRail() {
    const rail = $('#rail'); if (!rail) return;
    const lv = level(S.xp), st = streakNow(), c = S.career;
    const curId = currentTopicId(), curArea = curId && ENTRY_BY_ID[curId] ? ENTRY_BY_ID[curId].category : null;
    const mineEmpty = !sanitizedMy().length;
    railPending = {};
    const groupsHtml = railGroups().map(g => {
      const stored = S.ui.railOpen[g.area], defOpen = !mineEmpty;
      const isOpen = g.area === curArea || (stored !== undefined ? stored : defOpen);
      if (!isOpen) railPending[g.area] = g.entries;
      return `<div class="lib-area">
        <button class="lib-area-h" data-act="rail-toggle" data-area="${esc(g.area)}" aria-expanded="${isOpen}" title="${esc(g.area)}">
          ${ICON.chev}<span class="lib-area-name">${esc(SHORT_BY_AREA[g.area] || g.area)}</span><span class="lib-area-count">${g.entries.length}</span>
        </button>
        <div class="lib-area-body" data-area="${esc(g.area)}" data-loaded="${isOpen ? '1' : '0'}" ${isOpen ? '' : 'hidden'}>${isOpen ? railAreaItemsHtml(g.entries, curId) : ''}</div>
      </div>`;
    }).join('');
    const pickHtml = mineEmpty ? `<div class="lib-empty"><p>Pick the topics you want to study.</p><button class="btn btn-sm btn-pen" data-act="go" data-to="topics">Pick your topics</button></div>` : '';
    rail.innerHTML = `
      <div class="brand"><span class="brand-eyebrow">Team</span><span class="brand-name">Quiz Bowl Lab</span><span class="brand-sub">Middle School · Easy High School</span></div>
      <div class="player">
        <div class="player-top"><span class="lv">Level ${lv.n}</span><span class="lv-title">${esc(lv.title)}</span></div>
        <div class="xpbar" role="progressbar" aria-label="Progress to the next level" aria-valuemin="0" aria-valuemax="100" aria-valuenow="${Math.round(lv.pct * 100)}"><span style="width:${(lv.pct * 100).toFixed(1)}%"></span></div>
        <div class="player-meta">${S.xp} XP${lv.to ? ` · ${lv.to - S.xp} to Level ${lv.n + 1}` : ' · top level!'}</div>
        <div class="player-stats">
          <span class="streak ${st ? 'on' : ''}" title="Days in a row with practice">${ICON.flame}${plural(st, 'day')}</span>
          <span class="pgn" title="Buzz Mode: powers / tens / negs"><b>${c.p}</b>/<b>${c.t}</b>/<b>${c.n}</b> <small>P/T/N</small></span>
        </div>
      </div>
      <nav class="nav" aria-label="Main">
        ${navBtn('home', 'Home', ICON.home)}${navBtn('topics', 'Topics', ICON.grid)}${navBtn('buzz', 'Buzz Mode', ICON.bell)}${navBtn('cards', 'Flashcards', ICON.cards)}${navBtn('stats', 'My Stats', ICON.chart)}
      </nav>
      ${pickHtml}
      <div class="library" aria-label="Topics">${groupsHtml}</div>
      <div class="rail-foot">
        <button class="theme-btn" data-act="theme">${themeLabel()}</button>
        ${storageOK ? '' : '<p class="rail-note">This browser is blocking saved data, so progress will reset when you close the page.</p>'}
      </div>`;
    const tb = $('#tbXp'); if (tb) tb.textContent = `Lv ${lv.n} · ${S.xp} XP`;
  }

  /* ---------- HOME ---------- */
  function libCard(t) {
    const d = stepsDone(t);
    return `<button class="lib-card" data-act="go" data-to="topic-${t.id}">
      <span class="lib-card-top">${mono(t)}<span><span class="lc-name">${esc(t.name)}</span><span class="kick">${esc(t.kicker)}</span></span></span>
      <span class="meter" aria-hidden="true"><span style="width:${(d / 5) * 100}%"></span></span>
      <span class="meta"><span>${d} of 5 steps</span><span>${pct(mastery(t))} cards mastered</span></span>
    </button>`;
  }
  function upcomingLibCard(e) {
    return `<div class="lib-card is-upcoming">
      <span class="lib-card-top">${mono(e)}<span><span class="lc-name">${esc(e.name)}</span><span class="kick">Coming soon</span></span></span>
      <span class="meter" aria-hidden="true"><span style="width:0%"></span></span>
      <span class="meta"><span class="tag-soon">Soon</span><span>&nbsp;</span></span>
    </div>`;
  }
  function viewHome() {
    const mine = sanitizedMy();
    const scopeBuilt = mine.length ? myBuiltTopics() : TOPICS;
    const next = scopeBuilt.find(t => !TS(t.id).unlocked);
    const pickHtml = mine.length ? '' : `<div class="pick-card card">
        <p class="eyebrow">First step</p><h2>Pick your topics</h2>
        <p>Choose your own on the Topics page, or add a teammate’s team study list — ${TOPICS.length === ALL_ENTRIES.length ? `all ${TOPICS.length} topics are ready.` : `${TOPICS.length} of ${ALL_ENTRIES.length} topics are ready now, and more are on the way.`}</p>
        <button class="btn btn-pen" data-act="go" data-to="topics">Pick your topics</button>
      </div>`;
    const nextHtml = next
      ? `<div class="next-card">${mono(next)}<div><p class="eyebrow">Up next</p><h2>${esc(next.name)}</h2><p>${esc(next.kicker)} · ${stepsDone(next)} of 5 steps done</p></div><button class="btn btn-buzz" data-act="go" data-to="topic-${next.id}">Start studying</button></div>`
      : scopeBuilt.length
        ? `<div class="next-card"><span class="mono">${ICON.bell}</span><div><p class="eyebrow">All notes done</p><h2>Time for a mixed round</h2><p>Every topic${mine.length ? ' in My topics' : ''} has notes. Now play Buzz Mode mixed, like a real match.</p></div><button class="btn btn-buzz" data-act="${mine.length ? 'buzz-my' : 'buzz-all'}">Play Buzz Mode</button></div>`
        : `<div class="next-card"><span class="mono">${ICON.bell}</span><div><p class="eyebrow">Coming soon</p><h2>Your topics aren’t built yet</h2><p>None of the topics you picked are ready yet. Check back soon, or study any topic that’s already built.</p></div><button class="btn btn-buzz" data-act="go" data-to="topics">Browse built topics</button></div>`;
    const areasMine = mine.length ? AREAS.filter(a => (BY_AREA[a.name] || []).some(e => mine.includes(e.id))) : [];
    const myCardsHtml = areasMine.map(a => `<section class="sec"><h2>${esc(a.name)}</h2><div class="lib-grid">${BY_AREA[a.name].filter(e => mine.includes(e.id)).map(e => e.built ? libCard(BY_ID[e.id]) : upcomingLibCard(e)).join('')}</div></section>`).join('');
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
      <p class="fineprint">${TOPICS.length} of ${ALL_ENTRIES.length} topics are built so far — ${TOPICS.length * 15} practice tossups, original questions written in QBReader format and checked against the real QBReader questions for each answer line. Built ${fmtDate(DATA.built)}. Keep using the real QBReader database too.</p>
    </div>`);
  }

  /* ---------- TOPICS PAGE ---------- */
  function listCard(l) {
    const built = l.ids.filter(id => BY_ID[id]).length;
    return `<div class="list-card">
      <div class="list-card-top"><span class="list-n">List ${l.n}</span></div>
      <p class="list-label">${esc(l.label)}</p>
      <p class="list-ready">${built} of ${l.ids.length} topics ready</p>
      <button class="btn btn-sm btn-pen" data-act="list-add" data-n="${l.n}">Add to my topics</button>
    </div>`;
  }
  function topicRowHtml(e) {
    const q = norm(e.name + ' ' + e.category);
    const checked = S.my.includes(e.id) ? 'checked' : '';
    if (e.built) {
      const t = BY_ID[e.id];
      return `<li class="topic-row" data-area="${esc(e.category)}" data-q="${esc(q)}">
        <input type="checkbox" class="my-check" id="chk-${t.id}" data-id="${t.id}" ${checked} aria-label="Add ${esc(t.name)} to my topics">
        ${mono(t)}
        <span class="trow-main"><a class="topic-row-name" href="#topic-${t.id}">${esc(t.name)}</a><span class="topic-row-status">${stepsDone(t)} of 5 steps${freqBadge(t)}</span></span>
      </li>`;
    }
    return `<li class="topic-row is-upcoming" data-area="${esc(e.category)}" data-q="${esc(q)}">
      <input type="checkbox" class="my-check" id="chk-${e.id}" data-id="${e.id}" ${checked} aria-label="Add ${esc(e.name)} to my topics">
      ${mono(e)}
      <span class="trow-main"><span class="topic-row-name">${esc(e.name)}</span><span class="topic-row-status">Coming soon</span></span>
    </li>`;
  }
  function areaSectionHtml(a) {
    const entries = BY_AREA[a.name] || [], built = entries.filter(e => e.built).length;
    return `<section class="topics-area" data-area="${esc(a.name)}">
      <div class="topics-area-h">
        <h3>${esc(a.name)} <span class="muted">${built} of ${entries.length} ready</span></h3>
        <div class="row"><button class="btn btn-sm" data-act="area-select-all" data-area="${esc(a.name)}">Select all</button><button class="btn btn-sm btn-ghost" data-act="area-clear" data-area="${esc(a.name)}">Clear</button></div>
      </div>
      <ul class="topic-rows">${entries.map(topicRowHtml).join('')}</ul>
    </section>`;
  }
  let topicsQuery = '', topicsAreaFilter = 'all';
  function applyTopicsFilter() {
    const q = norm(topicsQuery);
    $$('.topics-area').forEach(sec => {
      let any = false;
      const areaMatches = topicsAreaFilter === 'all' || sec.dataset.area === topicsAreaFilter;
      $$('.topic-row', sec).forEach(row => {
        const show = areaMatches && (!q || row.dataset.q.includes(q));
        row.hidden = !show; if (show) any = true;
      });
      sec.hidden = !any;
    });
  }
  function viewTopics() {
    topicsQuery = ''; topicsAreaFilter = 'all';
    show('topics', `<div class="page">
      <header class="topic-head">
        <p class="eyebrow">Build your set</p>
        <h1 class="display">Topics</h1>
        <p class="kicker">Pick any topics to study — your own, a teammate’s team study list, or browse everything. ${TOPICS.length === ALL_ENTRIES.length ? `All ${TOPICS.length} topics are ready.` : `${TOPICS.length} of ${ALL_ENTRIES.length} topics are ready now; more are coming.`}</p>
      </header>
      <section class="sec">
        <h2>Team study lists</h2>
        <p class="sec-note">Each list is one teammate’s assignment. Adding a list never removes topics you already picked.</p>
        <div class="list-grid">${LISTS.map(listCard).join('')}</div>
      </section>
      <section class="sec">
        <div class="my-bar card">
          <span id="mySelCount" class="my-count">${plural(sanitizedMy().length, 'topic')} selected</span>
          <div id="myClearBox" class="row"><button class="btn btn-sm btn-ghost" data-act="my-clear">Clear my topics</button></div>
        </div>
      </section>
      <section class="sec">
        <div class="topics-tools">
          <input type="search" id="topicsSearch" class="search" placeholder="Search topics…" aria-label="Search topics" autocomplete="off">
          <div class="chips" role="group" aria-label="Filter by area" id="areaChips">
            <button class="chip on" data-act="topics-area" data-area="all">All</button>
            ${AREAS.map(a => `<button class="chip" data-act="topics-area" data-area="${esc(a.name)}">${esc(a.short || a.name)}</button>`).join('')}
          </div>
        </div>
        <div id="topicsList">${AREAS.map(areaSectionHtml).join('')}</div>
      </section>
    </div>`);
  }
  function viewUpcoming(u) {
    const isMine = S.my.includes(u.id);
    show('topic', `<div class="page">
      <header class="topic-head">
        <p class="eyebrow">${esc(u.category)}</p>
        <h1 class="display">${esc(u.name)}</h1>
        <p class="kicker">This one’s coming soon — Coach’s team is still writing it.</p>
        <div class="row"><button class="btn ${isMine ? 'btn-pen' : ''}" data-act="my-toggle" data-id="${u.id}" aria-pressed="${isMine}">${isMine ? '✓ In my topics' : '+ My topics'}</button></div>
      </header>
      <section class="sec">
        <div class="locked">${ICON.lock}<div><p><b>Not written yet.</b> Check back soon, or study one of the ${TOPICS.length} topics that are already built.</p></div></div>
      </section>
      <div class="row"><button class="btn btn-pen" data-act="go" data-to="topics">Browse topics</button><button class="btn btn-ghost" data-act="go" data-to="home">Home</button></div>
    </div>`);
  }

  /* ---------- TOPIC PAGE ---------- */
  function stepsHtml(t) {
    return STEPS.map(([k, label, tip], i) => {
      const done = stepDone(t, k), auto = k === 'notes' || k === 'drill';
      const inner = `<span class="step-n">${done ? '✓' : i + 1}</span><span class="step-l">${label}</span>`;
      return `<li>${auto
        ? `<span class="step auto ${done ? 'done' : ''}" title="${esc(tip)} (checks itself)">${inner}</span>`
        : `<button class="step ${done ? 'done' : ''}" data-act="step" data-id="${t.id}" data-step="${k}" aria-pressed="${done}" title="${esc(tip)}">${inner}</button>`}</li>`;
    }).join('');
  }
  function refreshSteps(t) { const el = $('#steps'); if (el) el.innerHTML = stepsHtml(t); renderRail(); }
  function markStep(t, k) { const ts = TS(t.id); if (!ts.steps[k]) { ts.steps[k] = true; touch(0); refreshSteps(t); } }

  const kindLabel = { video: 'Video', article: 'Article', museum: 'Museum videos', wiki: 'Wikipedia' };
  const mediaCard = (t, m) => `<a class="media-card" href="${esc(m.url)}" target="_blank" rel="noopener" data-act="media" data-id="${t.id}">
        <span class="media-kind k-${m.kind}">${kindLabel[m.kind] || m.kind}</span>
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
    return `<article class="tu" id="tu-${t.id}-${i + 1}">
      <header class="tu-h"><span class="tu-n">Tossup ${i + 1}</span><span class="tu-meta">${esc(t.qbCategory)} · QB Lab practice set</span>
        <button class="tu-say" data-act="say" data-id="${t.id}" data-i="${i}" aria-label="Read tossup ${i + 1} aloud" title="Read aloud">${ICON.speaker}</button></header>
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
    const ts = TS(t.id), caught = Array.isArray(ts.caught) ? ts.caught : null;
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
    const ts = TS(t.id), b = ts.buzz, heard = b.p + b.t + b.n + b.miss;
    show('topic', `<div class="page">
      <header class="topic-head">
        <p class="eyebrow">${esc(t.category)}${t.qbCategory && !t.qbCategory.endsWith(t.category) ? ' · ' + esc(t.qbCategory) : ''}</p>
        <h1 class="display">${esc(t.name)}</h1>
        <p class="kicker">${esc(t.kicker)} · ${esc(t.dates)}</p>
        <div class="answer-chip"><span class="answer-tag">Answer line</span><span>${t.answerHtml}</span></div>
        <div class="row"><button class="btn btn-buzz" data-act="buzz-topic" data-id="${t.id}">${ICON.bell}Buzz these 15</button><button class="btn" data-act="cards-topic" data-id="${t.id}">${ICON.cards}Flashcards</button>
          <button class="btn ${S.my.includes(t.id) ? 'btn-pen' : ''}" data-act="my-toggle" data-id="${t.id}" aria-pressed="${S.my.includes(t.id)}">${S.my.includes(t.id) ? '✓ In my topics' : '+ My topics'}</button></div>
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
            <a class="btn btn-pen" href="https://www.qbreader.org/db/" target="_blank" rel="noopener" data-act="qb" data-id="${t.id}">Open QBReader ↗</a>
            <p class="qb-found">When we checked, this search found <b>${t.qb.found}</b> tossups.</p>
            ${t.freq ? `<p class="qb-freq">${freqLine(t)}</p>` : ''}
            <p class="qb-tip">${fmt(t.qb.tip)}</p>
          </div>
        </div>
      </section>

      <section class="sec" id="s-read">
        <p class="sec-eyebrow">Step 3 · Read</p>
        <h2>QBReader Simulation</h2>
        <p class="sec-note">15 original practice tossups in QBReader format. <b>Bold text is the power zone:</b> buzz before the (*) and a right answer is worth 15 points instead of 10. Tap the speaker to hear one read aloud.</p>
        <div class="tu-tools"><button class="btn btn-sm" data-act="toggle-answers" aria-pressed="false">Hide answer lines</button><button class="btn btn-sm" data-act="read-done" data-id="${t.id}">I read all 15</button></div>
        <div class="tu-list" id="tuList">${t.tossups.map((tu, i) => tuCard(t, tu, i)).join('')}</div>
      </section>

      <section class="sec" id="s-notes">
        <p class="sec-eyebrow">Step 4 · Notes</p>
        <h2>My Notes</h2>
        <p class="sec-note">Do it Coach’s way: one clue per line, easy clues at the top, hard clues at the bottom, and a line where the power clues start. Write at least 5 clues to unlock the Clue Breakdown. Notes save as you type.</p>
        <div class="notebook">
          <div class="nb-head"><span class="nb-title">${esc(t.name)}</span><span class="nb-count" id="nbCount">${plural(noteLines(ts.notes), 'clue')}</span></div>
          <textarea id="notes-${t.id}" class="nb-text" data-id="${t.id}" spellcheck="true" aria-label="My notes for ${esc(t.name)}" placeholder="One clue per line.&#10;Easy clues at the top...&#10;&#10;— power line —&#10;Hard clues at the bottom...">${esc(ts.notes)}</textarea>
        </div>
        <div class="row"><button class="btn btn-pen" data-act="check" data-id="${t.id}">Check my notes</button><button class="btn btn-ghost" data-act="paper" data-id="${t.id}">I wrote mine on paper</button></div>
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
            <button class="btn btn-buzz" data-act="buzz-topic" data-id="${t.id}">${ICON.bell}Buzz this topic</button></div>
          <div class="drill-card"><h3>Flashcards</h3><p>Fill-in-the-blank cards for every clue, plus a “recite every clue” card.</p>
            <p class="drill-stat">${pct(mastery(t))} mastered</p>
            <button class="btn" data-act="cards-topic" data-id="${t.id}">${ICON.cards}Study the cards</button></div>
        </div>
        <p class="sec-note">When you have a few topics done, play Buzz Mode with <b>All topics</b>. Mixed questions are harder, just like a real match.</p>
      </section>
    </div>`);
  }
  function checkNotes(t) {
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
  const BZ = { q: [], i: 0, cur: null, words: [], pEnd: 0, shown: 0, phase: 'idle', timers: new Set(), score: 0, p: 0, t: 0, n: 0, log: [], buzzAt: -1, power: false, interrupted: false, prompted: false, last: null, token: null };
  function later(fn, ms) { const id = setTimeout(() => { BZ.timers.delete(id); fn(); }, ms); BZ.timers.add(id); return id; }
  function every(fn, ms) { const id = setInterval(fn, ms); BZ.timers.add(id); return id; }
  function clearAll() { BZ.timers.forEach(id => { clearTimeout(id); clearInterval(id); }); BZ.timers.clear(); }
  function stopBuzz() { clearAll(); BZ.token = null; if (BZ.phase !== 'idle') hush(); BZ.phase = 'idle'; }

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
            <select id="bzPool">${poolOptionsHtml(s.pool, { singleLabel: t => `${t.name} only` })}</select></div>
          <div class="field"><label for="bzCount">How many</label>
            <select id="bzCount">${['5', '10', '15', '20', 'all'].map(v => `<option value="${v}" ${s.count === v ? 'selected' : ''}>${v === 'all' ? 'All of them' : v + ' tossups'}</option>`).join('')}</select></div>
          <div class="field"><span class="label">Reading</span>${seg('bz-speak', s.speak && canSpeak ? 1 : 0, canSpeak ? [[0, 'Words on screen'], [1, 'Read aloud too']] : [[0, 'Words on screen']])}</div>
          <div class="field"><label for="bzSpeed">Reading speed: <span id="bzSpeedLbl">${s.wpm}</span> words per minute</label>
            <input id="bzSpeed" type="range" min="120" max="360" step="10" value="${s.wpm}"><span class="hint">A real moderator reads about 180–220.</span></div>
          <div class="field"><span class="label">Buzzer sound</span>${seg('bz-sound', s.sound ? 1 : 0, [[1, 'On'], [0, 'Off']])}</div>
        </div>
        <div class="row"><button class="btn btn-buzz" data-act="bz-start">${ICON.bell}Start the round</button><span class="muted">Press <span class="kbd">Space</span> to buzz, <span class="kbd">Enter</span> to answer, <span class="kbd">N</span> for the next tossup.</span></div>
      </section>
      <section class="stage" id="bzStage" hidden></section>
    </div>`);
  }
  function buildQueue(ids, count) {
    const pool = [];
    ids.forEach(id => BY_ID[id].tossups.forEach((_, ix) => pool.push({ id, ix })));
    shuffle(pool);
    const pri = x => { const r = S.tu[x.id + ':' + x.ix]; if (!r) return 0; return r.last === 'neg' || r.last === 'miss' || r.last === 'dead' ? 1 : 2; };
    pool.sort((a, b) => pri(a) - pri(b));
    const n = count === 'all' ? pool.length : Math.min(parseInt(count, 10) || 10, pool.length);
    return pool.slice(0, n);
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
    const s = S.settings;
    const ids = idsForPool(s.pool);
    stopBuzz();
    BZ.q = buildQueue(ids, s.count); BZ.i = 0; BZ.score = 0; BZ.p = BZ.t = BZ.n = 0; BZ.log = [];
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
  function loadQuestion() {
    clearAll(); hush(); BZ.token = null;
    if (BZ.i >= BZ.q.length) return finishBuzz(false);
    const { id, ix } = BZ.q[BZ.i], t = BY_ID[id], tu = t.tossups[ix];
    BZ.cur = { t, tu, id, ix };
    const pw = words(tu.p), rw = words(tu.r);
    BZ.words = pw.concat(rw); BZ.pEnd = pw.length; BZ.shown = 0;
    BZ.buzzAt = -1; BZ.power = false; BZ.interrupted = false; BZ.prompted = false; BZ.last = null;
    const stage = $('#bzStage'); if (!stage) return;
    stage.classList.remove('buzzed');
    paintScore();
    $('#bzLabel').textContent = `Tossup ${BZ.i + 1}`;
    $('#bzText').textContent = '';
    $('#bzCursor').hidden = false;
    const z = $('#bzZone'); z.className = 'zone'; z.textContent = 'Get ready…';
    $('#bzDead').hidden = true; $('#bzAnswerRow').hidden = true; $('#bzPrompt').hidden = true; $('#bzVerdict').hidden = true;
    $('#bzBuzzZone').hidden = false; $('#bzBuzzer').disabled = false;
    BZ.phase = 'countdown';
    later(() => {
      if (BZ.phase !== 'countdown') return;
      BZ.phase = 'reading'; updateZone();
      if (S.settings.speak && speechAvailable()) speakAll(); else readWords();
    }, 1000);
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
    touch(Math.max(0, pts));
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
      const hit = TOPICS.find(o => o.id !== t.id && judge(L.given, o) === 'right');
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
    clearAll(); BZ.token = null; hush();
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
      ${missedTopics.length ? `<section class="sec"><h3 class="h3">Study these next</h3><ul class="missed">${missedTopics.map(id => { const tp = BY_ID[id], k = missed.filter(x => x.id === id).length; return `<li><span><b>${esc(tp.name)}</b> <span class="muted">· missed ${plural(k, 'tossup')}</span></span><button class="btn btn-sm" data-act="go" data-to="topic-${id}">Study</button></li>`; }).join('')}</ul></section>` : (played ? '<p class="check-result">You got every tossup in this round. Try a faster reading speed or more questions.</p>' : '')}
      <div class="row"><button class="btn btn-buzz" data-act="bz-again">${ICON.bell}Play again</button><button class="btn" data-act="bz-setup">Change settings</button><button class="btn btn-ghost" data-act="go" data-to="home">Home</button></div>`;
    renderRail();
  }

  /* ---------- FLASHCARDS ---------- */
  const FC = { deck: [], i: 0, flipped: false, got: 0, missed: 0 };
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
          <select id="fcDeck">${poolOptionsHtml(s.deck)}</select></div>
        <div class="field"><span class="label">Card type</span>${seg('fc-mode', s.cardMode, MODES)}<span class="hint" id="fcModeNote">${modeNote()}</span></div>
        <div class="field"><span class="label">Mastered cards</span>${seg('fc-mastered', s.withMastered ? 1 : 0, [[0, 'Skip them'], [1, 'Include them']])}</div>
      </div>
      <div class="fc-wrap" id="fcWrap"></div>
    </div>`);
    newDeck();
  }
  function modeNote() {
    const m = resolvedMode();
    return { name: 'See a clue, name the answer line.', fill: 'Fill in the missing word in each clue.', recite: 'See the answer line, recite every clue you know.', mixed: 'A mix of all three.' }[m];
  }
  function deckFor() {
    const s = S.settings, ids = idsForPool(s.deck), mode = resolvedMode(), cards = [];
    ids.forEach(id => {
      const t = BY_ID[id];
      if (mode !== 'recite') t.clues.forEach(c => cards.push({ id, cid: c.id, type: mode === 'mixed' ? (Math.random() < 0.5 ? 'name' : 'fill') : mode }));
      if (mode === 'recite' || mode === 'mixed') cards.push({ id, cid: '__recite', type: 'recite' });
    });
    return shuffle(s.withMastered ? cards : cards.filter(c => !(S.cards[c.id + ':' + c.cid] || {}).m));
  }
  function newDeck() { FC.deck = deckFor(); FC.i = 0; FC.flipped = false; FC.got = 0; FC.missed = 0; paintCard(); }
  const tierPill = tier => `<span class="pill pill-tier t-${tier}">${TIER[tier].short}</span>`;
  function faces(card) {
    const t = BY_ID[card.id];
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
    if (!FC.deck.length) {
      w.innerHTML = `<div class="empty"><h3>Every card in this deck is mastered.</h3><p class="muted">Include mastered cards to review them, or pick another deck.</p><button class="btn btn-pen" data-act="fc-mastered" data-v="1">Review mastered cards</button></div>`;
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
    if (FC.i >= FC.deck.length) return;
    if (!FC.flipped) { flip(); return; }
    const card = FC.deck[FC.i], key = card.id + ':' + card.cid;
    const r = S.cards[key] || (S.cards[key] = { m: false, n: 0 });
    r.n++; r.t = Date.now();
    TS(card.id).steps.drill = true;
    if (got) { r.m = true; FC.got++; touch(2); }
    else { r.m = false; FC.missed++; FC.deck.splice(Math.min(FC.deck.length, FC.i + 4), 0, Object.assign({}, card)); save(); }
    FC.i++; FC.flipped = false;
    paintCard();
  }

  /* ---------- STATS ---------- */
  const toB64 = s => { const bytes = new TextEncoder().encode(s); let bin = ''; bytes.forEach(b => { bin += String.fromCharCode(b); }); return btoa(bin); };
  const fromB64 = s => { const bin = atob(String(s).replace(/\s+/g, '')); return new TextDecoder().decode(Uint8Array.from(bin, ch => ch.charCodeAt(0))); };
  function statsRow(t) {
    const ts = TS(t.id), b = ts.buzz, heard = b.p + b.t + b.n + b.miss;
    const caught = Array.isArray(ts.caught) ? `${ts.caught.length} of ${t.clues.length}` : ts.paper ? 'On paper' : '—';
    return `<tr><td><b>${esc(t.name)}</b></td><td>${stepsDone(t)} of 5</td><td>${caught}</td><td>${pct(mastery(t))}</td><td>${b.p}/${b.t}/${b.n}</td><td>${heard ? Math.round(((b.p + b.t) / heard) * 100) + '%' : '—'}</td></tr>`;
  }
  function viewStats() {
    const lv = level(S.xp), c = S.career;
    const gets = c.p + c.t, acc = c.heard ? Math.round((gets / c.heard) * 100) : 0;
    const mine = myBuiltTopics(), scope = mine.length ? mine : TOPICS;
    const scopeIds = new Set(scope.map(t => t.id));
    const areasShown = AREAS.filter(a => TOPICS_BY_AREA[a.name].some(t => scopeIds.has(t.id)));
    const statsSections = areasShown.map(a => `<div class="stats-area"><h3 class="h3">${esc(a.name)}</h3>
        <div class="table-wrap"><table><thead><tr><th>Topic</th><th>Steps</th><th>Clues in notes</th><th>Cards mastered</th><th>P/T/N</th><th>Correct</th></tr></thead>
        <tbody>${TOPICS_BY_AREA[a.name].filter(t => scopeIds.has(t.id)).map(statsRow).join('')}</tbody></table></div>
      </div>`).join('');
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
        <p class="sec-note">${mine.length ? 'My topics' : 'Every built topic'}, grouped by area.</p>
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
  document.addEventListener('click', e => {
    const el = e.target.closest('[data-act]'); if (!el) return;
    const act = el.dataset.act, id = el.dataset.id, t = id ? BY_ID[id] : null;
    switch (act) {
      case 'go': go(el.dataset.to); break;
      case 'menu': $('#app').classList.toggle('menu-open'); break;
      case 'menu-close': closeMenu(); break;
      case 'theme': cycleTheme(); break;
      case 'step': { const ts = TS(t.id), k = el.dataset.step; ts.steps[k] = !ts.steps[k]; if (ts.steps[k]) touch(0); else save(); refreshSteps(t); break; }
      case 'media': markStep(t, 'learn'); break;
      case 'qb': markStep(t, 'search'); break;
      case 'read-done': markStep(t, 'read'); toast('Step 3 done. Now write your notes.'); { const n = $('#s-notes'); if (n) n.scrollIntoView({ behavior: 'smooth', block: 'start' }); } break;
      case 'toggle-answers': { const list = $('#tuList'); if (!list) break; const on = list.classList.toggle('hide-answers'); el.textContent = on ? 'Show answer lines' : 'Hide answer lines'; el.setAttribute('aria-pressed', String(on)); break; }
      case 'say': sayTossup(t, parseInt(el.dataset.i, 10), el); break;
      case 'check': checkNotes(t); break;
      case 'paper': paperUnlock(t); break;
      case 'buzz-topic': S.settings.pool = id; S.settings.count = '15'; save(); go('buzz'); break;
      case 'buzz-all': S.settings.pool = 'all'; save(); go('buzz'); break;
      case 'buzz-my': S.settings.pool = 'my'; save(); go('buzz'); break;
      case 'cards-topic': S.settings.deck = id; S.settings.cardMode = 'auto'; save(); go('cards'); break;
      case 'my-toggle': { const on = !S.my.includes(id); setMine(id, on); el.textContent = on ? '✓ In my topics' : '+ My topics'; el.classList.toggle('btn-pen', on); el.setAttribute('aria-pressed', String(on)); break; }
      case 'list-add': {
        const list = LISTS.find(l => String(l.n) === el.dataset.n); if (!list) break;
        const before = new Set(sanitizedMy()), set = new Set(before);
        list.ids.forEach(x => set.add(x));
        S.my = [...set]; save();
        const added = set.size - before.size;
        toast(added ? `Added ${plural(added, 'topic')} to My topics.` : 'Those topics are already in My topics.');
        if (view === 'topics') refreshTopicsChecks(list.ids);
        renderRail();
        break;
      }
      case 'area-select-all': { const ids = (BY_AREA[el.dataset.area] || []).map(e => e.id), set = new Set(sanitizedMy()); ids.forEach(x => set.add(x)); S.my = [...set]; save(); refreshTopicsChecks(ids); renderRail(); break; }
      case 'area-clear': { const ids = (BY_AREA[el.dataset.area] || []).map(e => e.id), set = new Set(sanitizedMy()); ids.forEach(x => set.delete(x)); S.my = [...set]; save(); refreshTopicsChecks(ids); renderRail(); break; }
      case 'my-clear': { const box = $('#myClearBox'); if (box) box.innerHTML = `<div class="confirm"><span>Clear all ${sanitizedMy().length} topics from My topics?</span><button class="btn btn-sm btn-buzz" data-act="my-clear-yes">Yes, clear</button><button class="btn btn-sm btn-ghost" data-act="my-clear-no">Cancel</button></div>`; break; }
      case 'my-clear-yes': { const ids = sanitizedMy(); S.my = []; save(); toast('Cleared My topics.'); const box = $('#myClearBox'); if (box) box.innerHTML = '<button class="btn btn-sm btn-ghost" data-act="my-clear">Clear my topics</button>'; refreshTopicsChecks(ids); renderRail(); break; }
      case 'my-clear-no': { const box = $('#myClearBox'); if (box) box.innerHTML = '<button class="btn btn-sm btn-ghost" data-act="my-clear">Clear my topics</button>'; break; }
      case 'topics-area': { topicsAreaFilter = el.dataset.area; $$('#areaChips .chip').forEach(b => b.classList.toggle('on', b === el)); applyTopicsFilter(); break; }
      case 'rail-toggle': {
        const area = el.dataset.area, nowOpen = el.getAttribute('aria-expanded') !== 'true';
        S.ui.railOpen[area] = nowOpen; save();
        el.setAttribute('aria-expanded', String(nowOpen));
        const body = $$('.lib-area-body').find(b => b.dataset.area === area);
        if (body) {
          body.hidden = !nowOpen;
          if (nowOpen && body.dataset.loaded !== '1') { body.innerHTML = railAreaItemsHtml(railPending[area] || [], currentTopicId()); body.dataset.loaded = '1'; }
        }
        break;
      }
      case 'bz-start': case 'bz-again': startBuzz(); break;
      case 'bz-setup': viewBuzz(); break;
      case 'bz-buzz': buzz(); break;
      case 'bz-submit': submitAnswer(false); break;
      case 'bz-next': nextQuestion(); break;
      case 'bz-right': overrideRight(); break;
      case 'bz-quit': finishBuzz(true); break;
      case 'bz-speak': S.settings.speak = el.dataset.v === '1'; save(); el.parentNode.querySelectorAll('button').forEach(b => { const on = b === el; b.classList.toggle('on', on); b.setAttribute('aria-pressed', String(on)); }); break;
      case 'bz-sound': S.settings.sound = el.dataset.v === '1'; save(); el.parentNode.querySelectorAll('button').forEach(b => { const on = b === el; b.classList.toggle('on', on); b.setAttribute('aria-pressed', String(on)); }); if (S.settings.sound) beep('good'); break;
      case 'fc-flip': flip(); break;
      case 'fc-rate': rateCard(el.dataset.v === '1'); break;
      case 'fc-new': newDeck(); break;
      case 'fc-mode': S.settings.cardMode = el.dataset.v; save(); el.parentNode.querySelectorAll('button').forEach(b => { const on = b === el; b.classList.toggle('on', on); b.setAttribute('aria-pressed', String(on)); }); newDeck(); break;
      case 'fc-mastered': S.settings.withMastered = el.dataset.v === '1'; save(); if (view === 'cards') viewCards(); break;
      case 'copy-notes': {
        const text = TOPICS.filter(x => (TS(x.id).notes || '').trim()).map(x => `${x.name.toUpperCase()}\n${TS(x.id).notes.trim()}\n`).join('\n');
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
          box.innerHTML = `<div class="confirm"><span>This replaces the progress on this device with the backup (${obj.xp} XP). Continue?</span><button class="btn btn-sm btn-pen" data-act="restore-yes">Yes, restore</button><button class="btn btn-sm btn-ghost" data-act="restore-no">Cancel</button></div>`;
        } catch (err) { box.innerHTML = '<p class="check-result warn">That code didn’t work. Copy the whole backup code again and paste it here.</p>'; }
        break;
      }
      case 'restore-yes': if (pendingRestore) { S = deepMerge(fresh(), pendingRestore); normalizeState(); pendingRestore = null; save(); applyTheme(); toast('Progress restored.'); viewStats(); } break;
      case 'restore-no': pendingRestore = null; { const box = $('#restoreMsg'); if (box) box.innerHTML = ''; } break;
      case 'reset': { const box = $('#resetBox'); box.innerHTML = '<div class="confirm"><span>Erase everything on this device? This can’t be undone.</span><button class="btn btn-sm btn-buzz" data-act="reset-yes">Yes, erase it</button><button class="btn btn-sm btn-ghost" data-act="reset-no">Keep my progress</button></div>'; break; }
      case 'reset-yes': { const theme = S.settings.theme, touched = S.settings.themeTouched; S = fresh(); S.settings.theme = theme; S.settings.themeTouched = touched; normalizeState(); save(); toast('Progress erased.'); viewStats(); break; }
      case 'reset-no': { const box = $('#resetBox'); box.innerHTML = '<button class="btn" data-act="reset">Erase my progress…</button>'; break; }
      default: break;
    }
  });
  document.addEventListener('change', e => {
    const el = e.target;
    if (el.id === 'bzPool') { S.settings.pool = el.value; save(); }
    else if (el.id === 'bzCount') { S.settings.count = el.value; save(); }
    else if (el.id === 'fcDeck') { S.settings.deck = el.value; save(); newDeck(); }
    else if (el.classList && el.classList.contains('my-check')) { setMine(el.dataset.id, el.checked); }
  });
  document.addEventListener('input', e => {
    const el = e.target;
    if (el.id === 'bzSpeed') { S.settings.wpm = parseInt(el.value, 10) || 200; const l = $('#bzSpeedLbl'); if (l) l.textContent = S.settings.wpm; saveSoon(); }
    else if (el.classList && el.classList.contains('nb-text')) {
      const ts = TS(el.dataset.id); ts.notes = el.value; saveSoon();
      const cnt = $('#nbCount'); if (cnt) cnt.textContent = plural(noteLines(el.value), 'clue');
    }
    else if (el.id === 'topicsSearch') { topicsQuery = el.value; applyTopicsFilter(); }
  });
  document.addEventListener('keydown', e => {
    const tag = (e.target.tagName || '').toLowerCase();
    const typing = tag === 'input' || tag === 'textarea' || tag === 'select' || e.target.isContentEditable;
    if (view === 'buzz') {
      if ((e.code === 'Space' || e.key === ' ') && !typing && (BZ.phase === 'reading' || BZ.phase === 'dead')) { e.preventDefault(); buzz(); return; }
      if (e.key === 'Enter' && e.target.id === 'bzAnswer' && BZ.phase === 'answering') { e.preventDefault(); submitAnswer(false); return; }
      if ((e.key === 'n' || e.key === 'N') && !typing && BZ.phase === 'judged') { e.preventDefault(); nextQuestion(); return; }
      if ((e.code === 'Space' || e.key === ' ') && !typing && tag !== 'button' && (BZ.phase === 'answering' || BZ.phase === 'judged' || BZ.phase === 'countdown')) e.preventDefault();
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
