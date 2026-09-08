# AI Italian Teacher — backend deployment

This folder is **not** part of the GitHub Pages site (nothing under
`worker/` is linked from any HTML page). It's the source for a
separate Cloudflare Worker that acts as a secure proxy between your
website and the Groq API — the only place your Groq API key lives.

Ported from the sibling English-course project's `worker/` (same
architecture: CORS, rate limiting, Groq call, course-catalog
grounding) — this is a **separate, independently deployed Worker**
with its own name, its own KV namespace, and its own Italian-teacher
system prompt/course catalog. It does not share state with the
English, Latin, Ancient Greek, or Spanish courses' Workers, and
deploying one has no effect on the others.

## Why a separate deployment?

GitHub Pages only serves static files — there's no way to keep a
secret out of the browser if the AI call happened directly from your
site's JavaScript. The Worker runs on Cloudflare's servers, holds the
key there, and your site's JS only ever talks to the Worker.

## One-time setup (about 15 minutes)

### 1. Create free accounts (no credit card required for either)
- **Groq**: [console.groq.com](https://console.groq.com) → sign up → **API Keys** → Create API Key. Copy it somewhere safe. (If you already deployed another course's Worker, you can reuse the same Groq account/key — Groq's free-tier quota is shared per-account either way, so keep that in mind when tuning `DAILY_LIMIT_PER_ANON` below.)
- **Cloudflare**: [dash.cloudflare.com/sign-up](https://dash.cloudflare.com/sign-up) → sign up, or reuse the account you already created for another course's Worker — a Cloudflare account can host multiple, independent Workers.

### 2. Install Wrangler (Cloudflare's deploy tool)
```bash
npm install -g wrangler
wrangler login
```
This opens a browser window to connect Wrangler to your Cloudflare account. Skip this if you already did it for another course's Worker — it's the same account/tool.

### 3. Create the KV namespace (used for rate-limit counters)
```bash
cd worker
wrangler kv namespace create AI_TEACHER_KV
```
This prints something like:
```
id = "abcd1234..."
```
Copy that `id` value into `wrangler.toml`, replacing `REPLACE_WITH_YOUR_KV_NAMESPACE_ID`. **Do not reuse another course's KV namespace id** — each course needs its own so their rate-limit counters (and daily quotas) stay independent.

### 4. Set your Groq API key as a secret (never committed to git)
```bash
wrangler secret put GROQ_API_KEY
```
Paste your Groq key when prompted (the same key as another course's Worker is fine, or a separate one). This stores it encrypted on Cloudflare's side — it is never written to any file in this repo.

### 5. Confirm the allowed origin
Open `worker.js` and check the top of the file:
```js
const ALLOWED_ORIGIN = "https://renangrossi.github.io";
```
This is just the scheme+host of GitHub Pages — the same value works for every repo/project page under that account, so it's already correct for `lezionidiitaliano`. Update it only if the site moves to a custom domain.

### 6. Deploy
```bash
wrangler deploy
```
This prints your live Worker URL, something like:
```
https://ai-teacher-it.<your-account-subdomain>.workers.dev
```
Note the worker is named `ai-teacher-it` (see `wrangler.toml`) specifically so it doesn't collide with the other courses' Workers if all are deployed under the same Cloudflare account.

### 7. Point the website at your Worker
Update `AI_TEACHER_WORKER_URL` in `scripts/site_chrome.py` (near the top of the file, alongside `AI_TEACHER_ENABLED`) to the real URL printed in Step 6, then flip:
```python
AI_TEACHER_ENABLED = True
```
Then rebuild the whole site so every page picks up both changes:
```bash
python3 scripts/build_all.py
```
Commit and push as usual — the chat widget will now appear on every page and reach your live Worker.

## Adjusting limits

At the top of `worker.js`:
- `DAILY_LIMIT_PER_ANON` — questions per browser per day (default 20).
- `BURST_LIMIT_PER_IP` / `BURST_WINDOW_SECONDS` — short-term abuse brake (default 8 requests/60s per IP).
- `MAX_MESSAGE_LENGTH` — longest question accepted (keep in sync with the `maxlength` on the textarea rendered by `scripts/site_chrome.py`, if you change it).

## Course catalog (`course-catalog.json`)

So the AI Teacher can recommend a *real* lesson link instead of
guessing one, `worker.js` imports `course-catalog.json` — a list of
every real course page (the 6 level overview pages, all 56 lesson
pages, the 6 per-level "Mettiti alla Prova" cumulative-review pages,
and the site-wide utility pages like Dictionary/Exercises/Placement
Test) with their real on-site URLs. At request time the Worker does a
lightweight, deterministic keyword match between the student's
message (plus recent conversation) and this catalog, and only ever
hands the model URLs that come out of that match — the model is
instructed to never output a URL that wasn't supplied to it that
turn, so it's structurally unable to invent one.

**Generated once by scraping the real `<h1>`/`href`s out of `levels/*/​*.html`, then not auto-rebuilt.** If you add, rename, or move a lesson/level page, update `course-catalog.json` by hand.

Each entry:
```json
{ "level": "A1", "title": "Aggettivi e Accordo", "url": "levels/a1/aggettivi-e-accordo.html", "type": "lesson" }
```
- `url` is site-root-relative (no leading slash, no domain) — the Worker resolves it against `SITE_BASE_URL` in `worker.js`.
- `type` is `"lesson"` (a level lesson page — grammar explanation AND its own exercises together), `"test"` (a level's "Mettiti alla Prova" cumulative review page), or `"page"` (site-wide utility pages: Esercizi, Dizionario, Test di Livello, Esami Simulati, Extra, Verbi Irregolari, Ripasso di Oggi, I Miei Progressi).
- `level` is the CEFR level code (`"A1"`–`"C2"`), or `null` for a `"page"`-type entry that isn't level-specific.
- Optional `aliases`: extra search terms (English/Portuguese synonyms) for topics where student phrasing doesn't share words with the on-site Italian title — none are pre-populated yet; add them by hand for topics you notice the keyword matcher missing in practice.

After editing the catalog, redeploy with `wrangler deploy` (it's bundled into the Worker at deploy time, not fetched at runtime).

## What data is sent/stored

- The student's message and the current conversation (kept in the browser tab's memory only, lost on reload) are sent to the Worker, then to Groq, to generate a reply.
- The Worker stores nothing except two small rate-limit counters in KV: an anonymous ID (a random string generated in the browser, no personal info) plus a request count, both auto-expiring after 24 hours or 60 seconds.
- Per Groq's terms (worth re-checking at console.groq.com before relying on it long-term), free-tier requests may be logged for abuse monitoring; nothing here is guaranteed private, so the frontend also tells students not to share personal information.

## Free-tier reality check

Groq's `openai/gpt-oss-120b` free tier is roughly 1,000 requests/day
**shared across every visitor to your site**, not per-student — and if
you're using the *same* Groq account/key across multiple courses,
that quota is shared across all of them too. The Worker automatically
falls back to the `openai/gpt-oss-20b` model (same ~1,000 requests/day,
but a separate quota pool) if the primary model's daily quota is
exhausted, so the feature keeps working at slightly lower quality
rather than going down entirely. The per-browser daily cap
(`DAILY_LIMIT_PER_ANON`) exists specifically to stop one visitor from
using up the whole day's shared quota.
