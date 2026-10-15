# Non-social acquisition channels for developer tools: launches, communities, open source, newsletters, SEO and LLM search, marketplaces, paid (as of Oct 2026)

> Method note (Oct 15, 2026): During this session, WebFetch and direct curl were blocked by DNS and the proxy for almost every domain, including news.ycombinator.com, markepear.dev, tldr.tech, carbonads.net, ethicalads.io, supabase.com and arxiv.org. All findings below therefore come from web-search result summaries, not from full pages I read. Many of the sources are vendor or agency blogs (daily.dev business, idlen.io, Stackmatix, launch-service sites) that sell the thing they benchmark. Treat their numbers as directional. Prices are approximate unless they are marked as an official rate card.

## Q1. Hacker News (Show HN / Launch HN): mechanics, traffic, culture, case examples

### Takeaway
A front-page Show HN typically brings low thousands to roughly 12k visitors in a 24–48h spike. GitHub stars run at about 1.4 per upvote, and 92% of the star impact is over within 48h. The median Show HN scores 2 points, and odds of traction have fallen sharply in 2025–26. HN culture punishes marketing language, superlatives, signup walls, upvote-asking and (since 2026) LLM-written text. Supabase is the canonical breakout case.

### Cited Findings
**Odds and distribution**
- Daniel King analyzed 188,085 Show HN posts (2012 to Apr 2026). The median Show HN scores **2 points**. The best posting slot was **Monday 00:00 UTC (Sunday 7pm ET)**, with a 10.8% chance of scoring 50+ — [danfking.github.io, Apr 2026](https://danfking.github.io/blog/2026/04/23/show-hn-by-the-numbers/)
- Same study: about **1.4 GitHub stars per HN upvote within 48h**. The half-life of a Show HN is about 24h, and **92% of star impact is over after 48h**. HN score correlates with stars at only r = 0.29 (8% of variance), and comment count at r = 0.10. Caveat: the stargazer API capped at 1,000 stars per repo in the sample, and the sample skews to high-scoring posts — [danfking.github.io](https://danfking.github.io/blog/2026/04/23/show-hn-by-the-numbers/)
- Scoring 50 points puts a post in the **top 6%** of Show HN submissions — summarized via [danfking.github.io](https://danfking.github.io/blog/2026/04/23/show-hn-by-the-numbers/)
- An arXiv preprint (138 AI/LLM repos, 2024–25) found that repos gain an average of **121 stars in 24h, 189 in 48h and 289 in a week** after HN exposure. The "Show HN" tag showed **no statistical advantage** after controls — [arXiv 2511.04453](https://arxiv.org/abs/2511.04453)
- Traction is falling. An analysis of 70,894 Show HN posts found that 14.5% reached "real traction" in late 2024 versus **7.8% in H1 2026** ("twice the submissions, half the hits") — [DEV Community / pennyforgehq](https://dev.to/pennyforgehq/twice-the-submissions-half-the-hits-the-show-hn-middle-class-is-evaporating-1832); [DEV](https://dev.to/pennyforgehq/your-odds-of-getting-any-traction-on-show-hn-have-fallen-by-a-third-your-odds-of-getting-real-28eb)
- Show HN launches now often run on repos created days before posting, where it used to be months — [DEV Community](https://dev.to/pennyforgehq/show-hn-launches-now-run-on-repos-created-days-before-posting-it-used-to-be-months-3i90)

**Traffic and conversion anecdotes (self-reported)**
- A blog's top front-page post drew about **10,000 visitors**. Other front-page posts drew about 2,000 each — [Vincent Schmalbach](https://www.vincentschmalbach.com/analyzing-a-year-of-hacker-news-traffic/)
- A post that reached the top ranks drew **12,000 unique visitors** overnight and 100+ newsletter subscribers — [HackerNoon](https://hackernoon.com/what-happened-when-i-topped-hacker-news-and-pulled-in-12000-readers-overnight)
- LangFast: **6,000+ visits** on launch day, with about **3% visit-to-user** conversion — summarized in [Indie Hackers / Quaderno roundup](https://quaderno.io/blog/is-hacker-news-a-good-platform-to-launch-your-product/)
- Quaderno: **410 visitors, 19 signups (~5.3%), 5 qualified leads**. Signup rates reported for Basecamp and Groove via HN were about **0.1% and 0.3%**. The conclusion was that "HN is a forum… not a signup machine" — [Quaderno](https://quaderno.io/blog/is-hacker-news-a-good-platform-to-launch-your-product/)
- Linkdrop reached #2 for about half a day and got about **450 signups**, most of which faded — [Indie Hackers](https://www.indiehackers.com/post/very-successful-launch-on-hacker-news-then-nothing-6fdb27caf2)
- A front-page wearable startup got about 6k page views and **no direct conversions**. The traffic pattern was a "massive 24h spike → gentle decline → long tail" — [Indie Hackers](https://www.indiehackers.com/post/front-page-of-hn-the-full-postmortem-traffic-lessons-surprises-cbe9e0a7f6)
- A failed launch got 1 point, 0 comments and 0 signups, which the author partly blamed on holiday timing — [Indie Hackers](https://www.indiehackers.com/post/i-built-a-saas-in-9-days-for-200-launched-on-hn-to-zero-signups-heres-what-actually-happened-87c39638c6)
- Older data point: a 2014 Show HN tool had 3,858 visitors in a day, and 1,634 of them actively used the tool — [peterbe.com](https://www.peterbe.com/plog/html-tree-on-hacker-news)

**Culture and rules**
- dang (HN moderator) wrote in 2020, and reaffirmed in a Mar 28, 2026 edit: "Drop any language that sounds like marketing or sales. On HN, that is an instant turnoff." The 2026 edit also says he wants **no LLM-generated or LLM-edited text** — [HN item 22336638](https://news.ycombinator.com/item?id=22336638); quoted in [GTM Hacker guide](https://gtmhacker.ai/guides/hacker-news-launch-guide/)
- Launch HN instructions: "Don't use superlatives (fastest, biggest, first, best). Modest language is stronger." — via [syften](https://syften.com/blog/hacker-news-marketing/) / [welaunch.sh](https://www.welaunch.sh/blog/hacker-news-launch-guide-2026-how-to-post-on-show-hn-without-getting-flagged-or-2)
- Common guidance: use the title format "Show HN: [Name] – [plain description]". Don't ask for upvotes. Don't post a landing page instead of a usable product. Avoid brand-new accounts. Link the repo or demo. Treat the repo as the landing page — [Lucas F. Costa, Aug 2023](https://lucasfcosta.com/2023/08/21/hn-launch.html); [signals.sh title formulas (2026)](https://signals.sh/blog/show-hn-title-formulas)
- Slow load times or broken links attract downvotes, so plan capacity for the spike — [arXiv/HN roundups via search](https://www.indiehackers.com/post/front-page-of-hn-the-full-postmortem-traffic-lessons-surprises-cbe9e0a7f6)

**Case: Supabase**
- An early user posted Supabase to HN in 2020 before the planned launch. The post, titled "an open source Firebase alternative," drew **1.1K+ upvotes**. Hosted databases went from about 8 to 800 in three days after the tagline change ("the open-source Firebase alternative") — [Contrary Research](https://research.contrary.com/company/supabase). Secondary sources give "80→800 users"; the figures conflict — [Morgan Perry DevTools Brew](https://morganperry.substack.com/p/devtools-brew-23-supabase-journey)
- Alpha launch week (2020): **30,000+ new visitors and 1,400+ signups** — [Supabase alpha launch postmortem (via plushcap mirror)](https://www.plushcap.com/content/supabase/blog/supabase-alpha-launch-postmortem)
- Supabase turned launches into recurring "Launch Weeks" — [Product Hunt story: How we launch at Supabase](https://www.producthunt.com/stories/how-we-launch-at-supabase). It passed **50,000 GitHub stars in Aug 2023** — [Supabase LW8 highlights](https://supabase.com/blog/launch-week-8-community-highlights.md)

### Inferences
- Plan for about 2k–12k visitors and a few hundred stars (roughly 1.4 × points) per front-page hit. Visit-to-signup conversion can range from 0.1% to 5%. HN is a credibility and awareness channel more than a steady funnel.
- Because the payoff is concentrated in 48h, the repo or demo, docs and onboarding must be ready before posting. A self-serve, no-signup demo matters.
- Falling hit rates in 2026 (crowding from AI-built tools) make HN less dependable as a single launch bet. Repeated launches (Supabase-style launch weeks) and a strong positioning line ("open source X alternative") look more robust.

### Gaps
- I could not read news.ycombinator.com/showhn.html or Markepear's HN guide directly because of fetch failures. The rules above are paraphrased through secondary guides.
- I found no rigorous, recent study of HN visitor→signup→paid conversion for B2B dev tools.

## Q2. Product Hunt: relevance for dev tools in 2025–2026, traffic, conversion

### Takeaway
Product Hunt is still used heavily by dev tools: the dev-tools category was up 136% YoY in Q2 2026. But editorial "Featured" placement has become scarce (about 10% of launches, per late-2024 data), and results are bimodal. Top placements bring roughly 3k–8k visitors, while most launches see hundreds of users and few paying customers.

### Cited Findings
- Product Hunt's own Q2 2026 "State of Tech Discovery": the third-largest category (dev tools) was **up 136% YoY with 633 launches** in the quarter. AI had 1,111 launches (+46%) — [Product Hunt Q2 2026](https://www.producthunt.com/p/general/product-hunt-s-state-of-tech-discovery-q2-2026)
- Only about **10% of daily launches get Featured** (late-2024 data), down from 60–98% in 2020–2023 — [launchbuff.com analysis 2026](https://launchbuff.com/blog/product-hunt-launch-data-analysis-2026)
- A #1 Product of the Day gets an estimated **3,000–8,000 visitors in 24h**. The same source claims dev-tool trial-to-paid from PH is 20–40% higher than other sources (launch-services blog, unverified) — [launchbuff.com](https://launchbuff.com/blog/product-hunt-launch-data-analysis-2026)
- MySignature survey: 26.5% of launches got 500–1,000 users, 24.5% got 100–500, and only 10.2% got 2,000–5,000. 50% of founders saw some signup increase — [Usertour](https://www.usertour.io/blog/product-hunt-gain)
- Corbado (2024, dev tool) reached #1 Developer Tool of the Week, which brought **2x website traffic and 4x daily signups** on launch day and the days after. Dev tools are a minority of PH products — [Corbado](https://www.corbado.com/blog/launch-developer-tool-product-hunt)
- Tally reached #1 Product of the Month with **766 new users on launch day and 785 the next day** — [Tally blog](https://blog.tally.so/product-hunt-launch-results/)
- Weak case: 500 visitors on the day and 0 paying customers — [DEV Community](https://dev.to/holiney/is-product-hunt-dead-or-what-results-can-you-expect-from-product-hunt-launch-4j3d)
- Dev-only alternatives such as **DevHunt** (a GitHub-verified weekly board) have small but targeted audiences — [LaunchList](https://getlaunchlist.com/blog/product-hunt-alternatives)
- Carbon Ads claims Product Hunt charges about a **$40 CPM** for ads — [Carbon Ads](https://carbonads.net/more-info)

### Inferences
- For dev tools, PH is a secondary launch surface. It is useful for a badge, backlinks and an early-adopter spike, but it converts worse than HN or Reddit for technical buyers unless the product also appeals to non-developer "builders" (AI app builders, no-code).
- Because Featured placement is now rare, an unfeatured launch can produce very little. Treat PH as one item in a coordinated launch week, not the main event.

### Gaps
- I found no independent 2025–26 data on PH→paid conversion specifically for dev tools. The figures come from launch-service blogs or single founders.

## Q3. Reddit: subreddits, self-promotion rules, Reddit ads for developers

### Takeaway
Reddit can drive larger dev-tool spikes than PH. Single viral posts have reportedly driven tens of thousands of visits and lasting adoption. But each subreddit enforces its own strict promotion rules (Showoff Saturday on r/webdev, megathreads and "production ready" requirements on r/selfhosted). Reddit ads are the cheapest developer-targeted paid channel (subreddit targeting, roughly $0.20–$2 CPC, about $9 CPM), but most benchmarks come from vendors.

### Cited Findings
**Organic rules and norms**
- The "10% rule" (no more than about 10% of activity being self-promotion) is an informal norm, not written site policy. Some subs enforce closer to 99/1. Mods check user histories — [redship.io 2026 guide](https://redship.io/blog/reddit-self-promotion-rules-2026)
- Example of a written sub rule (r/cybersecurity): promotion must be under 10% of posts and comments and at most once per week per promoted entity — [r/cybersecurity wiki mirror](https://redlib.hbubli.cc/r/cybersecurity/wiki/rules/promotion)
- r/selfhosted reportedly requires promoted apps to be "production ready and have docs", and newer projects go into a megathread. **r/webdev allows projects only on "Showoff Saturday"** — [via search summary of syften/launchit.fast](https://launchit.fast/blog/where-to-promote-your-startup-on-reddit-2026)
- r/programming is described as "zero-tolerance" for promotion, and r/selfhosted as more open to OSS (unverified secondary) — [openskillindex devmarketing skill](https://openskillindex.com/skills/jonathimer-devmarketing-skills-reddit-engagement)
- Syften analyzed 12 devtool subreddits. Best windows by activity: r/selfhosted **Fri 14:00–17:00 UTC** and r/webdev **Sat 14:00–17:00 UTC**. Syften cautions this is not proof of conversion — [Syften 2026](https://syften.com/blog/best-time-to-post-on-reddit/)

**Results (mostly self-reported)**
- An anonymous blog reports that a Reddit front-page post on r/programming drew **47,000 visits, 2.1% conversion, 987 signups** (unverifiable) — [search summary, prowlo/teract](https://prowlo.com/blog/reddit-marketing-devtools)
- An r/selfhosted launch reportedly produced **500 stars and 200 active users in 48h** (secondhand) — [growreddit](https://www.growreddit.com/best-subreddits-for-devtools)
- A founder says Reddit drove most of his OSS adoption, and that a single viral post fuelled growth for months — [Indie Hackers: 0 to 1000 GitHub stars](https://www.indiehackers.com/post/0-to-1000-github-stars-for-your-open-source-dev-tools-db2efb62f1)
- AFFiNE (33k→60k stars) case studies credit Reddit, but the sources disagree: one says 2,000+ stars from Reddit in month 1, another says +500 from an r/SideProject post — [gingiris](https://gingiris.github.io/growth-tools/blog/2026/03/25/how-to-get-more-github-stars-the-definitive-guide-33k-stars-case-study/); [DEV](https://dev.to/iris1031/how-to-get-more-github-stars-the-definitive-guide-33k-stars-case-study-11h8)
- Counterexample: a self-hosted tool launched on PH and a Reddit megathread got **27 stars and 270 sessions in 3 weeks** — [DEV Community](https://dev.to/yaniv_zalevas_a91253c56bb/three-weeks-of-launching-an-open-source-product-27-stars-270-sessions-0-comments-2mk0)

**Reddit ads**
- Refine Labs Q1 2026 B2B awareness: Reddit **$9.33 CPM** (versus LinkedIn $42.29 CPM and $11.24 CPC) — [Refine Labs](https://www.refinelabs.com/blog/b2b-paid-awareness-benchmarks-q1-2026)
- Developer-focused benchmark: Reddit is "affordable (~$0.44 CPC)" but better for awareness than conversions — [daily.dev business benchmarks 2026](https://business.daily.dev/resources/developer-paid-media-benchmarks-2026-cpm-cpc-ctr-by-channel/)
- B2B SaaS on Reddit: **$0.50–$2.00 CPC and $80–$200 CPA**. Developer subreddits run about **$0.20–$1.50 CPC**. Tech startups targeting dev and IT communities see **$30–$80 CPA per MQL**. A meaningful test takes **$500–$1,500** — [Stackmatix](https://www.stackmatix.com/blog/reddit-ads-tech-startups-roi); [Stackmatix cost](https://www.stackmatix.com/blog/how-much-does-reddit-advertising-cost)
- Vendor-reported cases: a B2B dev tool spent $2,100 over 4 weeks for 42 demo requests (**$50/demo vs $180 on LinkedIn**). An observability startup got 340 MQLs at **$38 CPA vs $267 on LinkedIn** over 90 days (unverified) — [Stackmatix B2B](https://www.stackmatix.com/blog/reddit-ads-for-b2b)
- Targeting works by subreddit (for example r/rust, r/golang) or keyword. A suggested test is 3–5 ad sets per subreddit cluster — [Stackmatix](https://www.stackmatix.com/blog/reddit-ads-for-b2b)

### Inferences
- Organic Reddit rewards established, genuinely participating accounts posting in the sub's sanctioned format: Showoff Saturday, megathreads, "I built X because Y" stories with source code. Fit by niche matters more than size: r/selfhosted for self-hostable OSS, language subs for libraries, r/cursor-type subs for AI-coding add-ons.
- Reddit ads look like the best-value paid test for dev tools ($500–$1.5k budget, subreddit targeting), but every case study is vendor-reported.

### Gaps
- I could not verify the current written rules of r/programming, r/ExperiencedDevs, r/SideProject or r/cursor, because fetching was blocked. Check each sidebar or wiki.
- I found no Reddit-official benchmark for developer audiences.

## Q4. GitHub and open source as marketing: stars to users, README, awesome lists, Trending, open core

### Takeaway
Stars are a weak but real vanity and credibility signal. They correlate only modestly with launch scores, and intent-data vendors rank them as low-strength buying signals. No published, reliable stars→users or stars→revenue conversion rate exists. What works is a README built as a landing page, a concentrated launch that hits GitHub Trending, inclusion in awesome lists, and open-core or hosted monetization (the Supabase model).

### Cited Findings
- One founder argues "no amount of GitHub Stars are worth a single paying user". Stars mainly add credibility for a hosted business — [debugginggtm substack](https://debugginggtm.substack.com/p/github-stars)
- Stargazers can be enriched (company and role) for outbound. Stars **older than 3–6 months rarely convert** — [reo.dev substack: business value of a GitHub star](https://reodotdev.substack.com/p/what-is-the-business-value-of-a-github)
- Reo.dev rates a star on a complementary repo as a **low-strength** intent signal. Forks and PRs from contributors are stronger. Starring is a "low-intent discovery" action (vendor classification) — [reo.dev signals](https://www.reo.dev/signal/complementary-github-star); [reo.dev blog](https://www.reo.dev/blog/decoding-purchase-intent-for-developer-led-sales)
- An academic study (Borges & Valente, JSS 2018) clusters star growth into four patterns and surveyed 115 developers on what stars mean. It does not measure conversion — [JSS 2018 PDF](https://homepages.dcc.ufmg.br/~mtov/pub/2018-jss-github-stars.pdf)
- HN→stars: about 1.4 stars per upvote within 48h (see Q1) — [danfking](https://danfking.github.io/blog/2026/04/23/show-hn-by-the-numbers/)
- README as landing page: visitors decide whether to star "within about 20 seconds". Recommended elements are a hero image, a one-sentence value proposition and a demo GIF — [infrasity GitHub marketing](https://www.infrasity.com/blog/github-marketing-strategies)
- The biggest awesome lists have **100,000+ stars**, and inclusion "borrows their long-tail traffic" — [infrasity / rzlt](https://www.rzlt.io/blog/open-source-marketing-how-to-turn-a-github-repo-into-a-growth-engine)
- Recommended sequence: positioning → README landing page → one concentrated multi-channel launch day (HN, PH, Reddit, awesome lists) → retention plus a GEO/SEO long tail — [Marketing-for-Founders repo (ossinsight)](https://ossinsight.io/analyze/EdoStra/Marketing-for-Founders)
- GitHub Trending is a discovery surface but "doesn't tell you how much a project actually grew or whether the growth is real" (star inflation and fake stars are a concern) — [DEV Open Source Top 10](https://dev.to/_4a402f2d2e1b4119fd0db/open-source-top-10-this-week-sep-28-oct-4-ranked-by-verified-github-star-growth-35la)
- Case: ToolJet gained **20,000 stars and 400 contributors** — [DEV/ToolJet](https://dev.to/tooljet/how-tooljet-gained-20000-github-stars-and-400-contributors-4ee0). Case: a freeCodeCamp author reached **3,500+ stars in one week** — [freeCodeCamp/Medium](https://medium.com/free-code-camp/how-to-get-up-to-3500-github-stars-in-one-week-339102b62a8f)
- Case: Supabase passed **50k stars by Aug 2023** (top ~160 repos), with open source plus launch weeks as its core engine — [Supabase blog](https://supabase.com/blog/launch-week-8-community-highlights.md)
- Warning: "The GitHub repo with 40K stars that nobody uses in production" — [Medium](https://medium.com/lets-code-future/the-github-repo-with-40k-stars-that-nobody-uses-in-production-786ce6705439)
- Data-access caveat (2026): stargazer endpoints on major repos now return 401/404 for non-collaborators, so star-history datasets are becoming hard to build — [DEV Community](https://dev.to/pennyforgehq/show-hn-launches-now-run-on-repos-created-days-before-posting-it-used-to-be-months-3i90)

### Inferences
- Treat stars as a social-proof and top-of-funnel metric, and as an outbound and intent signal when enriched and acted on quickly (within 3 months). Don't treat them as a revenue proxy. Track "active installs" and "cloud signups from repo" instead.
- Open core or a hosted "open-source X alternative" gives OSS reach a monetization path. Supabase and PostHog-style companies are the pattern, but I found no PostHog-specific data.

### Gaps
- I found no reliable published stars→users or stars→paid conversion rate.
- I found no PostHog-specific data on stars or open-core marketing in this session.

## Q5. Developer newsletters and podcasts: sponsorship prices and CTRs

### Takeaway
Newsletter sponsorships are the largest paid "native" developer channel. Indicative prices: TLDR flagship primary about $16k–$24k per send, TLDR mid-size lists about $3k–$9k, Bytes premier $3,650 per issue, This Week in React €1,500 top slot, Changelog podcast $3,000/week. Tech/dev newsletters price at roughly a $40–$150 CPM. Most rate cards are private or "price on application," and I found no verified CTRs for specific newsletters.

### Cited Findings
**TLDR (tldr.tech)**
- TLDR publishes no public rate card. It sells Quick Links, Secondary and Primary placements at a flat rate per send — [sponsorships.ai](https://sponsorships.ai/blog/tldr-advertising-cost)
- Derived estimates (not quotes): mid-sized lists (Dev/Web Dev, Data, InfoSec, Marketing) **$3k–$9k per send**, TLDR AI **$11k–$17k**, TLDR Tech flagship primary **$16k–$24k**, based on about $10–$15 per 1,000 subscribers — [unanswered.io](https://unanswered.io/guide/tldr-newsletter-business-model-advertising)
- Other cited ranges: $6k–$24k per send, and about $2.7k–$18k from an earlier TLDR ad page. A Medium comparison put the TLDR primary at about $18k — [sponsorships.ai](https://sponsorships.ai/blog/tldr-advertising-cost); [Medium](https://medium.com/@thenewsletternewsletter/cost-of-sponsorships-across-various-newsletters-22fe80bb561a)
- TLDR has about 1.25M subscribers (third-party listing) — [hashnode](https://hashnode.com/blog/where-to-advertise-to-developers)

**Bytes (ui.dev)**
- About **216k subscribers** (another, older listing says 105k). Premier sponsor **$3,650 per issue**, "Spot the Bug" $1,225, "Cool Bit" link $920, jobs $210 — [draft.dev list / developernewsletters via search](https://draft.dev/learn/the-ultimate-list-of-developer-newsletters)

**Cooper Press (JavaScript Weekly etc.)**
- JavaScript Weekly has about 170k–180k subscribers. Pricing is POA, with rates in a Q1 2024 media kit — [draft.dev](https://draft.dev/learn/the-ultimate-list-of-developer-newsletters); Cooper Press says its newsletters reach **400,000+ developers** — [Cooper Press booking](https://booking.cooperpress.com/jobs)
- A third-party guide gives a Cooper Press **CPC of about $3–$7** for JS Weekly — [hashnode](https://hashnode.com/blog/where-to-advertise-to-developers)

**Others**
- Console.dev: about 22k+ subscribers, POA. Pointer.io: about 60k+ subscribers, rates not public — [search summary of draft.dev / readless](https://draft.dev/learn/the-ultimate-list-of-developer-newsletters)
- This Week in React: **€1,500 top placement** and €800 secondary, with bundles such as €5,000 for 4 top issues. React Digest **$1,000–$1,500**. Smashing newsletter **$2,500** per post — [daily.dev business: best developer newsletters to sponsor](https://business.daily.dev/resources/best-developer-newsletters-to-sponsor/)
- Pragmatic Engineer has a sponsor page; price not captured — [Pragmatic Engineer](https://blog.pragmaticengineer.com/sponsor/)

**Benchmarks**
- Tech and dev newsletters: about **$40–$100+ CPM** — [beehiiv](https://www.beehiiv.com/blog/newsletter-sponsorship-cost); about **$60–$150 CPM** for tech and dev tools — [sponsorgap 2026](https://sponsorgap.com/blog/newsletter-sponsorship-rates-2026); dev newsletters about **$35–$60 per 1,000 opens** — [daily.dev business](https://business.daily.dev/resources/developer-newsletter-advertising-reach-engineers-inbox/)
- Niche newsletters with 5k–100k subscribers charge about **$100–$2,000 per placement** — [daily.dev business](https://business.daily.dev/resources/developer-newsletter-advertising-reach-engineers-inbox/)
- Dedicated sends cost **2–4x** the primary placement. Bottom slots fell from about 0.7x to **0.4–0.6x** of mid-issue pricing — [newsletrix](https://newsletrix.com/blog/newsletter-sponsorship-rates-by-niche)

**Podcasts**
- **Changelog (official rate card):** The Changelog **$3,000/week** (2 episodes/week, 4-week minimum, estimated reach 200k–280k). Changelog News $1,500/week. Practical AI $1,200/episode. Fallthrough $200/episode — [changelog.com/sponsor/pricing](https://changelog.com/sponsor/pricing)
- Changelog and Software Engineering Daily: roughly **$1,200–$3,000 per episode** (vendor blog, unverified for SE Daily) — [daily.dev business podcast advertising](https://business.daily.dev/resources/developer-podcast-advertising-sponsorship-formats-costs-roi/)
- Host-read mid-roll **$25–$40 CPM** (Acast). Programmatic **$15–$30 CPM**. Tech podcasts are often priced at **$45–$65 CPM** — [creatorsagency / influencerfee summaries](https://creatorsagency.co/blog/podcast-sponsorship-rates-2026)

### Inferences
- For a seed-stage dev tool, niche newsletters (language or framework weeklies at $500–$3.5k per slot) are probably a better test than TLDR's $16k+ flagship slots. Buy 3–4 issue bundles, because single-slot attribution is noisy.
- Podcasts work for awareness and brand trust (host-read). Budget a 4-week minimum (Changelog = $12k).

### Gaps
- I found **no published CTRs** for TLDR, Bytes, JS Weekly, Console or Pointer. Syntax.fm and SE Daily rate cards were not found. daily.dev newsletter pricing was not found.
- The Markepear newsletter guide could not be accessed because of a fetch failure.

## Q6. SEO, content, docs-as-marketing, and AI/LLM search (2025–2026)

### Takeaway
Docs are the most important content asset. Developers rank documentation as their #1 learning resource (83.9%, Stack Overflow 2024) and evaluate by free trial and peers rather than marketing pages. Comparison and "alternatives" pages and programmatic SEO still work. In 2025–26, LLM answers became a major channel: Vercel reportedly saw ChatGPT go from about 1% to 10% of signups in roughly six months. llms.txt helps coding agents but shows no measured effect on chatbot citations.

### Cited Findings
**Docs-as-marketing**
- In Stack Overflow 2024, technical documentation was the top online learning resource at **83.9%**, ahead of Stack Overflow at 80.3% — [Cherryleaf summary](https://www.cherryleaf.com/2024/07/survey-shows-documentation-is-the-no-1-way-that-developers-learn-about-your-api/)
- Per SO 2024 (secondary): **75.2%** evaluate new tools via free trial, **72.5%** ask other developers, **61.3%** use communities, and only **31.2%** use review sites — [daily.dev business on G2](https://business.daily.dev/resources/developer-tools-g2-review-sites-matter/)
- Developers "prefer to research, try things, and read documentation" and look first at the free tier and docs — [InfoWorld](https://www.infoworld.com/article/4058058/software-developers-arent-buying-it.html)

**Programmatic and comparison SEO**
- Dynamic Mockups went from **67 to about 2,100 monthly signups in 10 months** with programmatic SEO, plus 220% organic traffic growth in Q1 2025 versus Q4 2024 (vendor case) — [Omnius](https://www.omnius.so/blog/programmatic-seo-case-study)
- Comparison and "X vs competitor" pages at scale (Pipedrive example) improved rankings — [thebcms programmatic SEO examples](https://www.thebcms.com/blog/programmatic-seo-examples/)

**LLM / AI search**
- Guillermo Rauch (Vercel CEO) reportedly said ChatGPT went from about **1% to 10% of Vercel signups within six months** (secondhand, via Product Hunt pages. The original statement and date are not found) — [Product Hunt @rna](https://www.producthunt.com/@rna). A Sequoia podcast describes ChatGPT as Vercel's "fastest-growing customer acquisition channel" — [Sequoia](https://sequoiacap.com/?p=20130)
- Attribution: LLM-driven sessions split across referral, later branded or organic search, and "direct" (when referrers are stripped). Recommended fixes are a custom GA4 channel for chatgpt.com, perplexity and gemini, plus self-reported "how did you hear about us" — [source.app](https://www.source.app/articles/llm-attribution-chatgpt-traffic); [Something Inc](https://somethinginc.com/blog/how-to-measure-llm-seo-attribution-ai-search-visibility/)
- Visibility trackers (Peec.ai, Ziptie, LLMrefs) measure mentions, not signups — [llmrefs](https://llmrefs.com/blog/chatgpt-seo-tools)
- llms.txt: generated by Mintlify, Fern, GitBook, and Vercel and Supabase docs. Read by Cursor, Continue, Cline and MCP servers when pointed at docs. A SERanking Nov 2025 study found **zero correlation** between llms.txt and citation rates in ChatGPT, Claude, Gemini and Perplexity. Google (May 2026) says llms.txt is **not needed** for AI Overviews or AI Mode. Chrome Lighthouse 13.3 added an "Agentic Browsing" audit that checks for it — [callmissed](https://www.callmissed.com/en/blog/ai-documentation-tools-2026); [getpassionfruit](https://www.getpassionfruit.com/blog/should-i-create-an-llms.txt-file-google-s-2026-guidance-explained); [dataforaisearch](https://dataforaisearch.com/learn/llms-txt-complete-guide)

### Inferences
- For dev tools, "docs + quickstart + free tier" is the conversion page. Content strategy should prioritize integration tutorials, migration guides ("moving from X to Y") and honest comparison pages that LLMs can cite.
- LLM visibility depends on being in the corpora LLMs draw on: docs, GitHub READMEs, Reddit/HN/SO threads, comparison pages. It also depends on AI app builders defaulting to your tool (see Q8). Add an "AI assistant" option to signup attribution surveys.

### Gaps
- I found no primary-source confirmation of the Vercel 10% figure. I found no independent study of dev-tool SEO traffic→signup rates or of docs traffic share.
- The Markepear, Lee Robinson and swyx primary writing on content and docs could not be fetched.

## Q7. Communities, DevRel programs, students, hackathons, conferences, meetups

### Takeaway
Community is a durable moat but hard to measure. Supabase reportedly has 200k+ Discord members and 10:1 community-to-company content. DevRel budgets were rising in 2024, but measurement remains the top pain point. Conferences are expensive: KubeCon packages run about $6k–$150k, with a 50% startup discount. Student programs (GitHub Student Developer Pack) are a low-cost seeding channel.

### Cited Findings
**Discord / Slack / champions**
- Supabase: a Discord of **200,000+ members**, with community-generated content exceeding company content **10:1** (secondary, unverified) — [idlen.io community-led growth](https://www.idlen.io/blog/community-led-growth-developer-tools/)
- Champions are identified by behavior: active in Slack or Discord, building plugins, submitting PRs, writing posts. Rewards include early access, private channels with engineering, and roadmap input — [daily.dev business Discord guide](https://business.daily.dev/resources/discord-community-marketing-developer-tools-server-setup-pipeline/); [Advocu](https://www.advocu.com/post/developer-champion-program-from-planning-to-execution)
- Failure mode: programs "ship the title without the lifecycle — no term, no renewal, no way out" — [samber developer-champions](https://www.skills.sh/samber/developer-relations-skills/developer-champions)

**State of DevRel (2024, 11th annual)**
- Programs with budgets under $100K fell to **16.7% (from 36.7% in 2023)**. **29%** saw budget increases (versus 16%). **60%** exclude staff salaries from program budgets — [stateofdeveloperrelations.com 2024](https://www.stateofdeveloperrelations.com/2024devrelreport)
- **36%** use product usage as the top community metric. **44%** use active users as a primary success measure. Only **18%** link to revenue influence — [devrel.agency key insights](https://www.devrel.agency/post/key-insights-from-the-11th-annual-state-of-developer-relations-report)
- Only 2 of 13 DevRel leaders interviewed could clearly link activities to strategic outcomes — [Chris Reddington](https://chrisreddington.com/blog/devrel-value-creation/)

**Students**
- GitHub Student Developer Pack: partners give free or discounted offers, each claimed on the partner's site. Examples: JetBrains (free all-IDEs, about $289/yr value), GitKraken (6 months free, then 80% off while a student), Appwrite (Education plan), 1Password (1 year free). GitHub Copilot student signups were reportedly **paused since April 2026** — [GitHub SDP partner FAQ](https://github.com/github-education-resources/Student-Developer-Pack-Current-Partners-FAQ/blob/main/README.md); [perkstack](https://perkstack.co/blog/github-student-pack-guide)

**Conferences**
- KubeCon + CloudNativeCon tiers (2026 prospectus): **$125k / $60k / $35k / $18k / $6k** member pricing and **$150k / $72k / $42k / $21.6k** non-member. Add-ons include $15k t-shirt sleeve, $10k lanyard and $10k co-located events. Extra lead-scanner licenses cost $249 — [Linux Foundation prospectus PDF](https://events.linuxfoundation.org/wp-content/uploads/2026/01/sponsor-kubecon-ch26-eg-1.pdf); [co-located guide](https://events.linuxfoundation.org/archive/2026/kubecon-cloudnativecon-europe/co-located-events/co-located-events-sponsor-guide/)
- CNCF startups get **50% off booth price** with a Startup Sponsorship — [CNCF startups](https://www.cncf.io/about/join/startups/)
- KubeCon NA 2026 (Nov 9–12, Salt Lake City) claims 10,000 developers, architects and technical leaders — [LF sponsor page](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/sponsor/)

### Inferences
- For early-stage tools, a Discord or Slack paired with a structured champion tier and launch weeks gives community leverage cheaply. Conferences mostly make sense post-PMF for enterprise pipeline. A startup booth at about $3k–$9k (after the 50% discount) plus talks or co-located events is the efficient entry.
- Measure community by product usage and activation, not member counts, in line with where DevRel is heading.

### Gaps
- I did not find MLH or hackathon sponsorship costs, meetup economics, the 2025 State of DevRel report, or PostHog's and Vercel's ambassador program details. Common Room data was not captured.

## Q8. Integrations and marketplaces: VS Code, JetBrains, Raycast, GitHub Marketplace, MCP registries, ChatGPT/Claude

### Takeaway
Marketplaces have become a primary distribution surface for AI-era dev tools. The official MCP Registry's monthly new publishers grew from 277 in Sep 2025 to 3,962 in Aug 2026. ChatGPT's app/plugin directory listed about 2,289 apps by Aug 2026, and Claude's connector directory about 1,375 by mid-2026. VS Code Marketplace plus Open VSX (for Cursor and Windsurf) is table stakes for editor tools. Discoverability inside saturated registries is the new problem.

### Cited Findings
- MCP Registry: monthly new publishers grew from **277 (Sep 2025, launch month) to 3,962 (Aug 2026)**. **81.2%** of the 18,676 servers listed before the Jul 28, 2026 spec revision have not published a new version since — [Oktopost](https://www.oktopost.com/blog/mcp-registry-legacy-servers/)
- 13,000+ MCP servers on npm and GitHub, with about 400% YoY growth in registrations (May 2026 tally, secondary) — [bex.co, Oct 14 2026](https://bex.co/blog/2026/10/14/ai-agents-listing-hand-reviewed-mcp-directory)
- GitHub MCP Registry: enterprise admins can set allow lists, which VS Code enforces automatically — [GitHub Blog](https://github.blog/ai-and-ml/generative-ai/how-to-find-install-and-manage-mcp-servers-with-the-github-mcp-registry/)
- Recommended MCP distribution: at least one package registry (npm/PyPI) plus the official MCP Registry, and Docker/DXT for production — [ChatForest](https://chatforest.com/guides/mcp-server-packaging-distribution/)
- ChatGPT: the app directory became the **Plugin Directory on Jul 9, 2026**. **2,289 apps from 2,007 developers** as of Aug 2026. Listing requires review — [usecarly](https://www.usecarly.com/blog/chatgpt-plugins/); [node8.ai](https://node8.ai/ai-connectors/chatgpt/)
- Claude connectors: about 369 (Jun 19 2026) → **1,375** (later census: 768 community, 598 partner, 9 Anthropic), with 584 added in July alone. **17.1%** of ChatGPT-listed products also ship a Claude connector — [nicolassitter census](https://www.nicolassitter.com/research/mcp-apps-census-2026); [node8.ai](https://node8.ai/ai-connectors/)
- VS Code Marketplace's publisher reporting hub tracks page views→installs (an acquisition funnel). Acquisition counts can exceed displayed installs because of uninstalls — [Microsoft DevBlogs](https://devblogs.microsoft.com/devops/extension-reporting-hub-for-marketplace-publishers/); [vscode-discussions #617](https://github.com/microsoft/vscode-discussions/discussions/617)
- Open VSX is the route to Cursor, Windsurf and other forks — [DEV](https://dev.to/diana_tang/complete-guide-publishing-vs-code-extensions-to-both-marketplaces-4d58). The VS Code Private Marketplace (GA Nov 2025) lets enterprises curate and rehost extensions — [VS Code blog](https://code.visualstudio.com/blogs/2025/11/18/PrivateMarketplace)

### Inferences
- An MCP server, a ChatGPT app and a Claude connector are now part of "distribution through integrations." They also act as LLM SEO, because the assistant can invoke the tool directly. Inclusion in enterprise allow lists (GitHub MCP Registry, VS Code Private Marketplace) is becoming a gate for enterprise adoption.
- Being listed is not enough: the registries hold thousands of mostly stale entries. Ratings, maintenance cadence and verified-publisher status differentiate.

### Gaps
- I found no install or acquisition numbers for Raycast Store, JetBrains Marketplace, GitHub Marketplace or specific VS Code extensions (Cline, Continue), and no conversion data from any registry listing to paid users.

## Q9. Paid acquisition benchmarks for developer audiences

### Takeaway
Paid channels for developers are costly and noisy. Google Search runs about $2–$8 CPC for general software terms and $12–$30+ for niche dev terms. LinkedIn is the most expensive ($42–$120 CPM, about $11 CPC). Reddit is the cheapest targeted option (about $9 CPM, $0.20–$2 CPC). X runs $25–$45 CPM. Developer-native networks: Carbon about $6 CPM (claimed), EthicalAds CPM with volume discounts, daily.dev with $1k–$5k minimums. Most benchmarks are vendor-sourced and contradictory.

### Cited Findings
- **Google Ads:** $2–$8 CPC for general SaaS and software terms. $12–$30 for niche terms. The same source also says $25–$80 for developer-specific keywords (it contradicts itself) — [daily.dev business 2026 benchmarks](https://business.daily.dev/resources/developer-paid-media-benchmarks-2026-cpm-cpc-ctr-by-channel/). Cross-industry median search CPC is **$4.66** and CTR **6.42%** (WordStream/LocalIQ) — [whatagraph](https://whatagraph.com/blog/articles/ppc-benchmarks). Display: $20–$40 CPM, 0.25–0.35% CTR — [same](https://business.daily.dev/resources/developer-paid-media-benchmarks-2026-cpm-cpc-ctr-by-channel/)
- **LinkedIn:** $60–$120 CPM for developer targeting — [daily.dev business](https://business.daily.dev/resources/developer-paid-media-benchmarks-2026-cpm-cpc-ctr-by-channel/). Refine Labs Q1 2026: **$42.29 CPM and $11.24 CPC** — [Refine Labs](https://www.refinelabs.com/blog/b2b-paid-awareness-benchmarks-q1-2026)
- **Reddit:** $9.33 CPM (Refine Labs). About $0.44 CPC (daily.dev). $0.20–$1.50 CPC in dev subs (Stackmatix). See Q3.
- **X:** **$25–$45 CPM, 0.8–1.2% CTR** (developer-focused vendor source only) — [daily.dev business](https://business.daily.dev/resources/developer-paid-media-benchmarks-2026-cpm-cpc-ctr-by-channel/)
- **Carbon Ads:** **$6 CPM** "Optimized ROW Blend" for Dev Focus and Creator Focus audiences. Up to 15% added value with committed terms. Carbon claims competitors charge "$40 CPM like Product Hunt, or $10 CPM like Stack Overflow" — [carbonads.net/more-info](https://carbonads.net/more-info). A third party instead calls Carbon CPC-based with a $5k–$10k/month starting budget (conflict) — [idlen.io playbook](https://www.idlen.io/blog/developer-ad-network-playbook/)
- **EthicalAds:** CPM pricing, **10% discount at $3,000 and 15% at $25,000+**. Price is fixed for campaigns of 3 months or less. Targeting is by country and page content only, with no tracking — [EthicalAds advertiser FAQ](https://www.ethicalads.io/advertisers/faq/)
- **daily.dev ads:** minimum spend cited inconsistently as **$1,000** or **$5,000**. CPM quoted as $2–$5, $4–$12 or $8–$20, with CPC $0.50–$2.50. 1M+ developers targetable by language and tool. Its own feed also serves Carbon and EthicalAds inventory — [daily.dev business ad networks](https://business.daily.dev/resources/best-ad-networks-targeting-developers/); [developer ads pricing](https://business.daily.dev/resources/developer-ads-pricing-options-best-channels/); [daily-monetization repo](https://beta.pkg.go.dev/github.com/dailydotdev/daily-monetization)
- Native ads on developer platforms: **$35–$60 CPM** (2026 benchmark) — [daily.dev business](https://business.daily.dev/resources/developer-paid-media-benchmarks-2026-cpm-cpc-ctr-by-channel/)
- In-IDE ads: **2.1% CTR** versus 0.3% for display (vendor that sells in-IDE ads) — [idlen.io benchmarks](https://www.idlen.io/blog/developer-advertising-benchmarks-2026/)
- New: ChatGPT self-serve ads (2026) — guides exist, but I captured no dev-specific benchmarks — [cloro.dev](https://cloro.dev/blog/how-to-advertise-on-chatgpt/)

### Inferences
- What reportedly works: Google Search on high-intent competitor, alternative and integration keywords. Reddit subreddit targeting for cheap tests. Developer-native contextual networks (Carbon, EthicalAds) for awareness among ad-blocker-heavy audiences. Newsletter sponsorships (Q5). LinkedIn mainly for enterprise and ABM retargeting, given its cost.
- With such wide and contradictory ranges, budget for a 60–90 day test across 2–3 channels and measure CAC by activated user, not CTR.

### Gaps
- I could not read official rate pages for Carbon, EthicalAds, daily.dev or Stack Overflow (fetch blocked). I found no independent, dev-specific Google or X ads benchmark. I found no data on what share of dev-tool CAC comes from paid versus organic.
