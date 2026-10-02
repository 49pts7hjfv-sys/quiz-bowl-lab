// Answer-checker tests for topic files.
// usage: node tools/judge_check.js [--cross] [topics/<id>.json ...]
//   With no files, checks every topics/*.json.
//   Each topic may carry "tests": {"right": [...], "prompt": [...], "wrong": [...]}.
//   --cross also checks that no other topic's name is accepted on this topic's answer line.
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
const src = fs.readFileSync(path.join(ROOT, 'app', 'app.js'), 'utf8').split('/* ===== END QBCORE ===== */')[0];
const QBCore = new Function(src + '\nreturn QBCore;')();

const args = process.argv.slice(2);
const cross = args.includes('--cross');
let files = args.filter(a => !a.startsWith('--'));
const all = fs.readdirSync(path.join(ROOT, 'topics')).filter(f => f.endsWith('.json')).map(f => path.join(ROOT, 'topics', f));
if (!files.length) files = all;
const load = f => { try { return JSON.parse(fs.readFileSync(f, 'utf8')); } catch (e) { return null; } };
const manifest = JSON.parse(fs.readFileSync(path.join(ROOT, 'data', 'manifest.json'), 'utf8'));
const NAME = Object.fromEntries(manifest.topics.map(t => [t.id, t.name]));

let bad = 0;
const fail = msg => { bad++; console.log('FAIL ' + msg); };
const mine = files.map(f => [f, load(f)]);
for (const [f, t] of mine) {
  if (!t) { fail(`${path.basename(f)}: not valid JSON`); continue; }
  const tests = t.tests || {};
  let n = 0;
  for (const want of ['right', 'prompt', 'wrong']) {
    for (const input of tests[want] || []) {
      n++;
      const got = QBCore.judge(input, t);
      if (got !== want) fail(`${t.id}: judge(${JSON.stringify(input)}) = ${got}, want ${want}`);
    }
  }
  if (n < 8) fail(`${t.id}: only ${n} answer-checker tests (want 8+: right, prompt and wrong cases)`);
  const own = QBCore.judge(NAME[t.id] || t.name, t);
  if (own !== 'right') fail(`${t.id}: its own name "${NAME[t.id] || t.name}" is judged ${own}`);
}
if (cross) {
  // Compare against every other topic name in the manifest (built or not), so conflicts are found early.
  for (const [f, t] of mine) {
    if (!t) continue;
    for (const o of manifest.topics) {
      if (o.id === t.id) continue;
      const got = QBCore.judge(o.name, t);
      if (got === 'right') fail(`${t.id}: another topic's name "${o.name}" is accepted (add it to "reject")`);
    }
  }
}
console.log(bad ? `judge_check: ${bad} problem(s)` : `judge_check: OK (${mine.length} file(s)${cross ? ', cross-topic' : ''})`);
process.exit(bad ? 1 : 0);
