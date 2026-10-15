# Small and mid-size open-source dev tools outside India (2023–2026): how they went viral, built communities and made money

**Method and reliability note (read first).** Research date: 15 Oct 2026. The GitHub API, ungh.cc and shields.io were blocked from this environment ("GitHub access to this repository is not enabled" / proxy 403). Every WebFetch also failed with DNS errors, including for star-history.com, openstatus.dev, opencollective.com, bex.co, dokploy.com, orm.drizzle.team and substack. **All findings therefore come from search-result snippets.** No page was read in full, and no star count was checked live. The shared web-search budget ran out partway through, so a few candidates were not searched at all (Continue.dev, Zellij, tRPC, Directus, Windmill funding, Hacktoberfest). They are listed under Gaps.

Labels used below:
- **[R]** reported by a third party (tracker, blog or news site).
- **[S]** self-reported by the founder or company.
- **[E]** my own estimate or inference.

Nothing is labelled "verified", because no figure could be checked against GitHub directly. Hoppscotch and Bruno are Indian-founded, so they belong to the Indian-tools track and are left out here.

---

## 1. Star milestones, launch spikes and team size for each tool

### Takeaway
The fastest small-tool growth from 2023 to 2026 came from three sources:
- **Category substitution:** an "open-source X alternative" to a paid incumbent such as Vercel/Heroku, DocuSign, Bitly or Typeform.
- **A single founder visible on X, Hacker News and Product Hunt.**
- **Discrete spikes:** a Show HN, Product Hunt #1, GitHub Trending, or a competitor's collapse (Kilo Code after Roo Code shut down).

Teams were tiny at breakout: often 1–3 people (Coolify solo, Dokploy solo, OpenStatus 2, Drizzle 3 founders). Steady star growth then came from compounding word of mouth, not from paid acquisition.

### Cited findings

**Coolify** (self-hostable PaaS; founder Andras Bacsai, Hungary; solo for most of its history)
- **Origin and job exit:** Coolify was the side project that made him "leave a stable job at a multinational company in the middle of the pandemic." It launched on Product Hunt with #buildinpublic, hunted by Csaba Kissi [S]. — [X post](https://x.com/heyandras/status/1509066653912363008)
- **Full-time timeline:** he quit his job in July 2022 with savings for "several months, even 1–2 years" [S]. — [blog](https://blog.andrasbacsai.com/im-leaving-my-job-again-but-its-different-now)
  - In July 2023 he stopped freelancing to work on Coolify full-time [S]. — [newsletter](https://newsletter.coollabs.io/)
  - A late-2023 newsletter says v4 was in beta, around beta 120 [S]. — [newsletter](https://newsletter.coollabs.io/)
- **Show HN for v2 (2022):** he described Coolify as a curiosity project that grew into the reason he quit [S]. — [Show HN: Coolify v2](https://news.ycombinator.com/item?id=30854912)
- **Ask HN, October 2022:** he said he had "turned down 30+ investors" and was "funded by the community" [S]. — [HN comment](https://news.ycombinator.com/item?id=33077979)
- **Star counts (all [R], undated or loosely dated):**
  - more than 47,000 (undated guide) — [selfhostyourself](https://selfhostyourself.com/guides/how-to-self-host-coolify)
  - 53.9k — [Trendshift](https://trendshift.io/repositories/634)
  - about 55,900 at v4.1.0 (May 2026) — [n6cloud](https://n6cloud.com/?p=13547)
  - about 57,300 (June 2026) and 63.0k (GitHub page, via search snippet) — [GitHub](https://github.com/coollabsio/coolify)
  - 59,698 (July 2026, GitHub API per a bex.co article) — [bex.co](https://bex.co/blog/2026/07/27/dokploy-caprover-github-stars-docker-compose-ux)
- **YouTube amplification:** Coolify's docs list a Fireship video alongside a Syntax walkthrough (1.5 h), WebDevCody (6 min) and MelkeyDev. The Fireship video's date and its exact effect on star growth could not be confirmed. — [Coolify docs, videos page](https://coolify.io/docs/videos)

**Dokploy** (self-hostable PaaS; founder Mauricio Siu, "Siumauricio")
- **Created April 2024.** It passed CapRover's star count in about 2 years, where CapRover took about 9 years [R]. — [bex.co](https://bex.co/blog/2026/07/27/dokploy-caprover-github-stars-docker-compose-ux)
- **Stars:** 36,124 in July 2026 (GitHub API per bex.co) [R]. — [bex.co](https://bex.co/blog/2026/07/27/dokploy-caprover-github-stars-docker-compose-ux)
  - Star-history: 37.2k, 401 contributors, +158 stars that week [R]. — [star-history](https://www.star-history.com/dokploy/dokploy/)
  - Dokploy's own site still says "over 26.0k" (stale) [S]. — [dokploy.com](https://dokploy.com/)
- **Founder:** Mauricio Siu founded it. His GitHub Sponsors page asks for help "to cover server costs." — [Rivo blog](https://rivo.gg/blog/preview-deployment-vulnerability-in-dokploy); [GitHub Sponsors](https://github.com/sponsors/Siumauricio)

**OpenStatus** (status pages and uptime monitoring; Thibault Le Ouay and Maximilian Kaske; team of 2)
- **Show HN launch (October 2023):** it had about 2,000 stars at the time [S/R]. — [Show HN](https://news.ycombinator.com/item?id=37740870)
- **First year:** more than 6,000 stars and 5,000 users, with "a small team of two" [S]. — [OpenStatus blog](https://www.openstatus.dev/blog/reflecting-1-year-building-openstatus)
- **Later counts:**
  - about 7,000 stars cited in the May 2026 retrospective [S] — [blog](https://www.openstatus.dev/blog/a-year-of-openstatus-may-2026)
  - 9.1k stars, 120 contributors, +42 that week (13 Sep 2026) [R] — [star-history](https://www.star-history.com/openstatushq/openstatus/)
- **Product Hunt entries** dated 18 Oct 2025 and 30 May 2026 [R]. — [Product Hunt](https://www.producthunt.com/products/openstatus-2)

**Drizzle ORM** (TypeScript ORM; founders Andrii Sherman, Alex Blokh and Dan Kochetov; based in Dnipro, Ukraine)
- **Positioning:** framed as a bootstrapped underdog against a competitor that had raised $61M (Prisma).
- **Traction:** about 30,900 stars and 2.4M weekly npm downloads "without any VC funding" [R]. — [Underdog Founders Substack](https://underdogfounders.substack.com/p/the-story-of-building-drizzle-orm)

**Unkey** (API key management; co-founder and CEO James Perkins)
- 1.2k stars and 13M+ key verifications at the November 2023 pre-seed [S]. — [Unkey blog](https://www.unkey.com/blog/unkey-raises-1-5-million)
- "Almost 3K stars" around 2024 [R]. — [OSS Startup Podcast E147](https://podcast24.co.uk/episodes/the-oss-startup-podcast/e147-the-over-complication-of-api-management-what-went-wrong-UP8TbwDEVdY)

**Documenso** (open DocuSign alternative; Timur Ercan; Germany, 2023)
- Stars: 14,000+ (August 2026) and 15,418 [R]. — [gappsy](https://www.gappsy.com/tools/documenso/); [OpenAlternative](https://openalternative.co/documenso)

**Formbricks** (open Qualtrics/Typeform alternative; Johannes Dancker and others)
- About 13.1k stars on GitHub; 12.8k in an August 2026 snapshot [R]. — [GitHub](https://github.com/formbricks/formbricks); [OpenTechHub](https://www.opentechhub.io/formbricks/)

**Trigger.dev** (background jobs; YC-backed)
- More than 4,000 stars at the $3M seed (around 2023) [S]. — [seed post](https://trigger.dev/blog/3m-dollar-seed-round)
- 16.5k stars in 2026 [R/S]. — [GitHub](https://github.com/triggerdotdev/trigger.dev)

**Novu** (notifications infrastructure; growth led by Nevo David)
- Grew from 2k to more than 20k stars in about a year [S/R]. — [DEV interview](https://dev.to/crowddotdev/how-to-grow-a-github-project-to-20k-stars-with-nevo-david-novu-3i81)
- Later passed 31k stars and was Product Hunt Product of the Day [S]. — [Indie Hackers](https://www.indiehackers.com/post/growing-open-source-novu-to-31k-stars-and-product-of-the-day-adaa2ec01b)

**Cal.com** (early contrast case; began as "Calendso")
- The side project "nearly broke Product Hunt" and became Product of the Month plus a Maker Grant.
- Within a few months it had about 9,000 stars, more than 800 forks, a 1,200+ member Slack and 10k weekly users.
- Team: 8 core members, about a dozen freelancers and 76+ community contributors. All of this is [S], from the seed post (translated pages). — [Cal.com seed blog (IT)](https://cal.com/it/blog/seed); [DE](https://cal.com/de/blog/seed)

**Dub** (open Bitly alternative; Steven Tey)
- Started in October 2022 while Tey was at Vercel. It passed 14k stars, later "almost 18K" [R].
- A top Hacker News post drove early momentum. Product Hunt launch on 21 March 2024 won #1 Product of the Month [S/R]. — [OSS Startup Podcast ep. 152](https://ossstartuppodcast.substack.com/p/episode-152-taking-on-bitly-with); [oss.beehiiv](https://oss.beehiiv.com/p/dub); [Tey profile](https://foss.read.cv/steven)
- His earlier side project, Novel, reached 2.6K stars in 3 days [R]. — [oss.beehiiv](https://oss.beehiiv.com/p/dub)

**Atuin** (shell history; Ellie Huxtable)
- About 31.9k stars [R]. Around 70M lines of history on the sync server [S]. — [Changelog #579](https://changelog.com/podcast/579); [ellie.wtf](https://ellie.wtf/projects/atuin/)
- Annual "atuin wrapped" feature (v18.4, December 2024) used as a shareable release moment. — [X post](https://x.com/ellie_huxtable/status/1872697379029434852)

**Lazygit / lazydocker** (Jesse Duffield; Melbourne)
- Stars as of about March 2025: lazygit 58,202 and lazydocker 43,228 [R]. — [sponsors.ecosyste.ms](https://sponsors.ecosyste.ms/accounts/jesseduffield)

**Hono** (Yusuke Wada, Senior Developer Advocate at Cloudflare)
- Released 15 December 2021. About 30.9k–32.5k stars as of October 2026 [R].
- Wada claims Hono passed NestJS and Fastify in npm downloads, is chasing Express, and is used inside Cloudflare KV, R2 and Workers AI [S]. — [X post](https://x.com/yusukebe/status/2045037650093232176); [GitHub](https://github.com/honojs/hono); [tech-insider](https://tech-insider.org/hono-vs-express-vs-fastify-2026/)

**Excalidraw**
- Created 1 January 2020 by Christopher "Vjeux" Chedeau, then at Meta. Run by Excalidraw s.r.o. in Brno, Czech Republic.
- Team of 6 [R]. Third-party reviews cite around 120K stars [R]. — [Wikipedia](https://en.wikipedia.org/wiki/Excalidraw); [CheckThat](https://checkthat.ai/brands/excalidraw); [doolpa](https://doolpa.com/article/excalidraw)

**AI coding agents** (a fast-moving cohort)
- **Cline:** about 58K stars in early 2026, 69,653 on 1 October 2026 [R]. — [wetheflywheel](https://wetheflywheel.com/en/guides/open-source-ai-coding-agents-2026/)
- **Roo Code** (a Cline fork): final release 15 May 2026; repo is now read-only and points users to Cline [R]. — [wetheflywheel](https://wetheflywheel.com/en/comparisons/opencode-vs-roo-code-vs-cline/); [bodegaone](https://www.bodegaone.ai/blog/roo-code-shutdown-alternatives)
- **Kilo Code** (a Roo fork): about 19,200 stars in May 2026, "growth driven almost entirely by one event: Roo Code's shutdown announcement." It reached 27,460 by 1 October 2026 [R]. — [wetheflywheel](https://wetheflywheel.com/en/comparisons/opencode-vs-roo-code-vs-cline/)
- **Aider** (Paul Gauthier, former founding CTO of Inktomi): 40k+, 41.6k (March 2026) and about 47.1k (mid-2026) [R]. — [promptquorum](https://www.promptquorum.com/power-local-llm/aider-review); [self.md](https://self.md/people/paul-gauthier-aider/)

**Maybe Finance**
- When the company open-sourced its code after its first shutdown, the repo was "#1 trending repo on GitHub…for the entire week" [S]. Stars were frozen at about 54,351 when it was archived in July 2025 [R]. — [Josh Pigford on X](https://x.com/Shpigford/status/2038774838475805081); [Failory](https://newsletter.failory.com/p/3-reasons-maybe-failed)

**Workflow tools**
- **Kestra:** 26K stars cited at its $25M Series A (31 March 2026) [S/R]. — [Axios](https://www.axios.com/pro/enterprise-software-deals/2026/03/31/workflow-orchestration-kestra-enterprise)
- **Activepieces:** about 22,001 stars [R]. — [OpenAlternative compare](https://openalternative.co/compare/activepieces/vs/windmill)
- **Windmill:** about 16,381 stars [R]. — [OpenAlternative compare](https://openalternative.co/compare/activepieces/vs/windmill)
- **n8n** (contrast, now large): 46,000+ stars in March 2026, from a weak source [R]. — [Automation Atlas](https://automationatlas.io/answers/n8n-series-c-valuation-2025/)

**Payload CMS**
- Weekly npm downloads grew from about 2,000 (beta, 2021) to about 90,000 (end of 2024) [S, Mikrut via Crain's]. — [Crain's Grand Rapids](https://www.crainsgrandrapids.com/news/technology/grand-rapids-tech-firm-acquired-by-san-francisco-web-designer)

### Summary table

Stars are reported, not verified.

| Tool | Founded / OSS launch | Team at breakout | Latest stars [R] | Key spike event |
|---|---|---|---|---|
| Coolify | 2021 | 1 (solo) | ~57k–63k (mid-2026) | Product Hunt launch with build-in-public; Show HN v2 (2022); YouTube (Fireship, Syntax) |
| Dokploy | Apr 2024 | 1 (solo) | ~36k–37.8k (Jul–Sep 2026) | Coolify-alternative positioning; Docker Compose UX |
| OpenStatus | 2023 | 2 | ~9.1k (Sep 2026) | Show HN (Oct 2023, ~2k stars) |
| Drizzle | ~2022 | 3 founders | ~30.9k | X memes, "Wall of Hate" |
| Unkey | 2023 | small | ~3k (2024) | build in public, pre-seed |
| Novu | 2021–22 | small | 31k+ | DEV.to articles plus Reddit-triggered GitHub Trending |
| Dub | Oct 2022 | 1 → small | ~18k | top HN post; Product Hunt #1 Product of the Month (Mar 2024) |
| Kilo Code | 2025 | small | 27.5k (Oct 2026) | Roo Code shutdown |
| Maybe | open-sourced ~Jan 2024 | company | 54k (frozen) | #1 GitHub Trending for a week |

### Inferences
- [E] "Open-source alternative to {expensive SaaS}" is the dominant launch frame. Coolify (Vercel/Heroku/Netlify), Dokploy (Vercel/Netlify/Heroku), Documenso (DocuSign), Formbricks (Qualtrics) and Dub (Bitly) all use it in their repo taglines. It makes the HN or Product Hunt pitch self-explanatory.
- [E] Followers can be second movers in a category. Dokploy outgrew a nine-year incumbent (CapRover) in two years by improving UX in a category Coolify had already proven.
- [E] Events can produce discontinuous spikes: an incumbent's death (Roo → Kilo) or a dramatic story (Maybe's shutdown and open-sourcing). These can rival years of organic growth.

### Gaps
- No live star counts or star-history curves could be pulled because the GitHub API and star-history.com were blocked. Milestone dates (for example, when Coolify crossed 10k, 25k and 50k) are unavailable.
- Not researched due to the exhausted search budget: Zellij, tRPC, Zod star history, Biome stars, oxc stars, Ghostty stars and 1.0 date, Continue.dev, Directus, Infisical stars, Payload stars, Excalidraw milestone dates.
- No dated source for the Fireship video on Coolify or its star impact.

---

## 2. Community-building tactics

### Takeaway
The documented small-team tactics are:
- **Paid micro-bounties via Algora:** modest totals, from about $1.4k at Coolify to $15k at Cal.com.
- **Contributor gamification during launch weeks:** Formbricks.
- **Large bounties for a specific technical goal:** the Prettier/Biome $20k+ challenge.
- **Corporate fellowships:** Clerk paying Zod's author.
- **Open-company transparency:** Cal.com's "Open Startup."

Discord sizes and good-first-issue programs could not be sourced.

### Cited findings
- **Algora bounties at Coolify:** $1,402 total awarded across 27 bounties and 1 tip, with 16 solvers. Payouts ranged from $15 to $100; the top earner made $565 [R, snapshot]. — [Algora/Coolify](https://algora.io/coollabsio/bounties/community)
- **Algora at Cal.com:** $15,014 awarded across 132 bounties and 53 tips; completed bounties include a $500 fix [R]. — [Algora/Cal.com](https://algora.io/cal/home)
- **Algora fees (sources conflict):** "0% fee for devs" per one listing, versus about 25% take rate per an older HN comment. — [awesome-bounties](https://github.com/JuanM94/awesome-bounties); [HN](https://news.ycombinator.com/item?id=40682632)
- **Bounty competition:** new Algora bounties reportedly attract 8–158 competing PRs within hours (anecdotal, 2026). In August 2026 the global board at algora.io/bounties returned 404, while per-org pages still worked. — [DEV.to](https://dev.to/aion_autonomous_org/i-measured-the-open-source-bounty-market-before-entering-it-then-i-didnt-enter-93n)
- **Biome and the Prettier bounty:**
  - Prettier offered $10k for a Rust formatter passing 95% of its tests. Vercel's Guillermo Rauch matched it to $20k, and napi.rs added $2.5k ($22.5k total). — [Prettier blog](https://prettier.io/blog/2023/11/27/20k-bounty-was-claimed/); [Wikipedia](https://en.wikipedia.org/wiki/Open-source_bounty)
  - Biome, a fork of Rome (abandoned October 2023), won in November 2023 with v1.4.0. — [Biome blog](https://www.biomejs.cn/en/blog/biome-wins-prettier-challenge/)
  - Biome split the money: 50% to direct challenge contributors, 25% to external contributors, 25% to the team. — [Biome blog](https://www.biomejs.cn/en/blog/biome-wins-prettier-challenge/); [GitHub issue #720](https://github.com/biomejs/biome/issues/720)
  - The bounty gave a brand-new fork a public, newsworthy win.
- **Formbricks launch-week community project:** day two of a launch week introduced a project "to gamify open source contributions" [S]. — [Dancker LinkedIn](https://www.linkedin.com/posts/johannes-dancker_saas-productstrategy-opensourcesoftware-activity-7051965455577550848-Fxz8); [Open Pioneers](https://www.openpioneers.com/p/formbricks)
- **Cal.com "Open Startup":** "operates fully transparent and shares its salaries and core metrics." It used a 1,200+ member Slack and 76+ contributors early. — [cal.com/open](https://www.cal.com/open); [seed blog](https://cal.com/de/blog/seed)
- **Contributor scale:** Dokploy has 401 contributors and OpenStatus 120 [R]. — [star-history Dokploy](https://www.star-history.com/dokploy/dokploy/); [star-history OpenStatus](https://www.star-history.com/openstatushq/openstatus/)
- **Novu:** stars brought "more contributors, more PRs, more signups, more visibility" [S]. — [DEV interview](https://dev.to/crowddotdev/how-to-grow-a-github-project-to-20k-stars-with-nevo-david-novu-3i81)
- **Atuin:** release posts publicly thank contributors ("thank you so much to everyone who contributed, you're the best!"), and features like `atuin wrapped` were suggested by the community. — [X v18.1](https://x.com/ellie_huxtable/status/1767236949822091335); [Bluesky](https://thoughts.waylonwalker.com/post/475)

### Inferences
- [E] Algora bounties at small projects are marketing and onboarding tools more than real labour markets. Coolify paid only about $1.4k in total, at $15–$100 each.
- [E] The many-PRs-per-bounty dynamic suggests bounties can create review burden.
- [E] A big, externally funded bounty such as Prettier's gave a small project a credibility event far beyond its cash value.

### Gaps
- Discord member counts for any of these tools: not found (searches did not reach it).
- Hacktoberfest results and spam experience for Formbricks, Novu and others: search budget exhausted.
- Swag, office hours and public roadmaps: no sourced data gathered.

---

## 3. Marketing on X, build in public and launch weeks

### Takeaway
The standout X tactic is personality-driven, irreverent brand voice:
- **Drizzle** displays hateful tweets as a "Wall of Hate" on its homepage instead of testimonials.
- **Founder-led build in public** (Coolify, Unkey, Dub): transparent revenue posts and ship-logs.
- **Content-led star campaigns** (Novu's DEV.to posts).
- **Launch weeks** run by small teams (Trigger.dev, Formbricks): concentrate announcements into a newsworthy window.

### Cited findings
- **Drizzle's "Wall of Hate":** instead of testimonials, the team gathered critical tweets and displayed them as a joke. Developers replied "I made it into the reviews!"
  - The Substack credits Drizzle with "spoke the language of the community they served, including controversy, humor, and irony" [R]. — [Underdog Founders](https://underdogfounders.substack.com/p/the-story-of-building-drizzle-orm); [orm.drizzle.team](https://orm.drizzle.team/)
  - The homepage feed was divisive: one GitHub discussion calls it "hilarious," another asks for a filter because of "several bad tweets bashing Drizzle." — [Discussion #2407](https://github.com/drizzle-team/drizzle-orm/discussions/2407); [Discussion #2164](https://github.com/drizzle-team/drizzle-orm/discussions/2164)
  - The @DrizzleORM voice is self-deprecating: it said they "never rushed the hype train" on benchmarks. Sponsor shout-outs use "Make TypeScript SQL great again!" — [X post](https://x.com/DrizzleORM/status/1653652968426688513); [X](https://x.com/DrizzleORM)
  - Some users said that if it was a marketing joke, "it is not a good marketing strategy" (mixed reception). — [search summary of X](https://twitter.com/DrizzleORM/status/1759679595735847348)
- **Coolify founder posting:**
  - Bacsai publishes income openly. February (2025) gross was $15,700 (Cloud about $10.5k, donations about $5.2k), expenses $2,800 and net $12,900.
  - He added, "for comparison, my last 9-5 job paid $1,700/m."
  - He posts frequent "still working on…" updates. — [X post](https://x.com/heyandras/status/1901894087604916396); [X](https://x.com/heyandras/status/1881625735405961381)
  - Some secondary sources mis-date the income snapshot to March 2025. — [bex.co](https://bex.co/blog/2026/08/16/coolify-bootstrapped-vs-vc-repricing-treadmill)
- **Unkey:** open source "from the start"; "if we were gonna build something, we wanted to build it with open source in mind" [S]. — [APIs You Won't Hate podcast](https://apisyouwonthate.com/podcast/unkey-globally-distributed-api-key-generation-with-cofounder-james-perkins/)
- **Novu playbook** (Nevo David):
  - Write DEV.to articles that are *not* about Novu but about the notifications space, with several "star the repo" calls to action.
  - Get "a lot of stars from multiple sources in a short period of time" to reach GitHub Trending; Reddit moved them from TypeScript-trending to global Trending.
  - Influencers bring a mostly junior audience but heavy traffic.
  - He claims "99%" of customers said a friend told them. — [DEV.to (Novu)](https://dev.to/novu/we-are-trending-on-github-this-is-how-we-did-it-kab); [DEV interview](https://dev.to/crowddotdev/how-to-grow-a-github-project-to-20k-stars-with-nevo-david-novu-3i81); [star-history blog](https://www.star-history.com/blog/do-github-stars-equal-money/)
- **Launch weeks:**
  - Trigger.dev's blog has multiple "Launch week" posts (August and December) [R]. — [trigger.dev/blog](https://trigger.dev/blog)
  - Formbricks ran a launch week (its date is unclear; the LinkedIn post is about 3.5 years old, so around April 2023). — [LinkedIn](https://www.linkedin.com/posts/johannes-dancker_saas-productstrategy-opensourcesoftware-activity-7051965455577550848-Fxz8)
  - No OpenStatus launch week could be confirmed.
- **Dub:** a top HN post plus Product Hunt #1 Product of the Month (21 March 2024). — [OSS Startup Podcast](https://ossstartuppodcast.substack.com/p/episode-152-taking-on-bitly-with); [Tey profile](https://foss.read.cv/steven)
- **Cal.com:** a Product Hunt launch that "nearly broke Product Hunt." — [seed blog](https://cal.com/it/blog/seed)
- **Hono:** distributed through the creator's DevRel role at Cloudflare and conference talks (GitNation). — [gitnation](https://gitnation.com/person/yusuke_wada); [GitHub](https://github.com/yusukebe)
- **Atuin:** podcast circuit (Changelog #579, RustShip) and Mastodon/Bluesky/X release posts. — [Changelog](https://changelog.com/podcast/579); [Hachyderm](https://hachyderm.io/@ellie)

### Inferences
- [E] Drizzle's meme voice works because it is self-deprecating and community-inclusive: users become part of the joke. It carries some brand risk; a minority found the hate wall off-putting.
- [E] Transparent revenue posts, like Coolify's "$12.9k net vs my $1,700 salary," are themselves viral content. They signal sustainability, which reassures self-hosters who fear abandonment.
- [E] Novu's DEV.to-plus-Reddit-plus-Trending approach is effective, but it optimises stars, which leads to the "stars ≠ users" problem in section 5.

### Gaps
- Quantified X engagement or follower growth for Drizzle, Coolify, Unkey or Dub: not found.
- OpenStatus launch-week details: not confirmed.
- Exact dates and contents of Trigger.dev's launch weeks: not confirmed.

---

## 4. Monetization: sponsors, hosted cloud, open core, enterprise licences, funding

### Takeaway
Three sustainable models appear among small tools:
- **Solo or bootstrapped: donations plus a cheap hosted cloud.** Coolify makes about $15k+/month, with no VC.
- **Bootstrapped team: sponsorship plus a corporate patron.** Drizzle's team was hired by PlanetScale in March 2026.
- **VC-backed open core or cloud:** Unkey $1.5M pre-seed then $4.5M seed; Trigger.dev $3M seed then $16M Series A; Infisical $16M Series A; Kestra $25M Series A; Cline $32M; Kilo $8M seed.

A late-stage route is licence tightening (tldraw, Open WebUI, Dokploy's open-core addition). It works commercially but triggers backlash. Acquisitions (Payload → Figma; VoidZero → Cloudflare) are another exit.

### Cited findings

**Bootstrapped or donation-led**
- **Coolify:**
  - Open Collective page lists hosted-service MRR of about $15K+, 3,000+ Cloud users, GitHub Sponsors about $4,500/month and Open Collective about $1,200/month [S]. — [Open Collective](https://opencollective.com/coollabsio)
  - Coolify Cloud costs $5/month for 2 servers, plus $3 for each additional server. — [bex.co](https://bex.co/blog/2026/08/16/coolify-bootstrapped-vs-vc-repricing-treadmill); [DEV teardown](https://dev.to/beton/coolify-pricing-teardown-2026-5675)
  - Infrastructure sponsors include Hetzner and Hostinger. — [GitHub](https://github.com/coollabsio/coolify)
  - Turned down 30+ investors [S]. — [HN](https://news.ycombinator.com/item?id=33077979)
- **Drizzle:**
  - GitHub Sponsors brought about $122,703 from April 2023 [R, Open Collective page; layout ambiguous]. Sponsor tiers run from $5 to $1,000/month; Platinum gets a README logo. — [Open Collective](https://opencollective.com/drizzle-orm)
  - Declined VC offers and "reached profitability in 2024" [R]. — [Underdog Founders](https://underdogfounders.substack.com/p/the-story-of-building-drizzle-orm)
  - June 2025: the team is "self-sustainable" [S]. — [Discussion #4616](https://github.com/drizzle-team/drizzle-orm/discussions/4616)
  - March 2026: "PlanetScale hired the entire Drizzle core team and became the biggest backer"; 100+ sponsors over the years [S]. — [Sustainability page](https://orm.drizzle.team/docs/sustainability)
  - Embeddable Drizzle Studio is licensed commercially, priced by platform size, with discounts for sponsors [S]. — [drizzle-studio-npm](https://github.com/drizzle-team/drizzle-studio-npm)
- **Excalidraw:**
  - Described as "bootstrapped and revenue-funded" versus Miro's $476M raised [R, opinion]. — [Jason Bosco on X](https://x.com/jasonbosco/status/1793647996598370776)
  - Excalidraw+ costs $6/user/month; the core stays MIT. Revenue is undisclosed. — [gappsy](https://www.gappsy.com/tools/excalidraw/); [CheckThat](https://checkthat.ai/brands/excalidraw)
- **Lazygit (Jesse Duffield):**
  - 122 current and 364 past sponsors, $5 minimum (around March 2025) [R]. — [sponsors.ecosyste.ms](https://sponsors.ecosyste.ms/accounts/jesseduffield)
  - He writes that he has "less time (aka motivation)" with each passing day [S]. — [sponsors.ecosyste.ms](https://sponsors.ecosyste.ms/accounts/jesseduffield)
  - Also received an Appwrite OSS Fund grant. — [DEV/Appwrite](https://dev.to/appwrite/appwrite-oss-fund-sponsors-lazygit-2no9)
- **Zod (Colin McDonnell):**
  - Clerk's first OSS Fellowship (announced 11 June 2024): 12 weeks at "a full-time, entry-level-engineer-style wage" to build Zod 4.
  - In return, Clerk gets branding in docs, README, RFCs and X profile, plus right of first refusal on a six-month "diamond tier" sponsor slot. — [Zod blog](https://zod.dev/blog/clerk-fellowship); [Clerk blog](https://clerk.com/blog/zod-fellowship)
  - Zod 4 is now stable. — [zod.dev](https://zod.dev/)
- **Ghostty** (contrast: a well-known founder, not money-seeking):
  - Fiscally sponsored by Hack Club, a 501(c)(3), as of 3 December 2025. Trademarks and IP moved to Hack Club; 7% of donations go to Hack Club.
  - A non-profit was intended "since the beginning… 2023 and the private beta days" [S]. — [mitchellh.com](https://mitchellh.com/writing/ghostty-non-profit)
  - The $150K personal donation is single-source and unverified. — [ascii.co.uk](https://ascii.co.uk/news/article/news-20251204-0eddfa93/ghostty-terminal-emulator-becomes-fiscally-sponsored-non-pro)
- **Aider:** Apache 2.0, with no paid tiers; users bring their own LLM keys. Whether an "Aider AI LLC" exists or any funding was raised is unverified and sources conflict. — [promptquorum](https://www.promptquorum.com/power-local-llm/aider-review); [grokipedia](https://grokipedia.com/page/Aider)

**VC-backed open core or cloud**
- **Unkey:** $1.5M pre-seed (November 2023, led by Essence VC; Sunflower and The Normal Fund) and $4.5M seed (23 April 2026, led by Uncork Capital). Seed money goes to the open-source core, SDKs and "a deeper free tier." — [pre-seed](https://www.unkey.com/blog/unkey-raises-1-5-million); [seed](https://www.unkey.com/blog/unkey-raises-seed)
- **Trigger.dev:** $3M seed (at about 4k stars), then a $16M Series A on 17 December 2025 led by Standard Capital with YC. Apache 2.0 and self-hostable. — [seed](https://trigger.dev/blog/3m-dollar-seed-round); [Series A](https://trigger.dev/blog/series-a)
- **Infisical:** YC Winter 2023, initially *closed source*, then switched to open source (MIT core). $16M Series A led by Elad Gil (June 2025). 40M+ downloads in a year. — [Fortune](https://fortune.com/2025/06/06/infisical-raises-16-million-series-a-led-by-elad-gil-to-safeguard-secrets)
- **Documenso:** about $2.2M early funding [R]. Managed plans from about $25–30/month; self-hosted and hosted share one codebase (AGPL). — [gappsy](https://www.gappsy.com/tools/documenso/); [Zapier](https://zapier.com/blog/docusign-alternatives/)
- **Formbricks:** pre-seed led by OSS Capital; also Flex Capital, Peer Richelsen and GitHub Accelerator (inaugural cohort). Amounts undisclosed. — [Crunchbase](https://www.crunchbase.com/organization/formbricks); [Formbricks About](https://formbricks.com/about)
- **Cal.com:** $7.4M seed led by Joseph Jacks (OSS Capital, December 2021), then a $25M Series A (April 2022, 776). — [seed blog](https://cal.com/es/blog/seed); [Preqin](https://www.preqin.com/data/profile/asset/cal-com--inc-/476838)
- **tldraw:**
  - Insiders' extension of $2M (November 2023), then a $10M Series A (Lux and Definition) after a first year of $1M licence revenue from ClickUp, Padlet and others.
  - Commercial licence reported at $6,000/year per team. — [tldraw Series A](https://tldraw.dev/blog/announcing-tldraw-series-a); [BigGo](https://biggo.com/news/202509190115_tldraw_SDK_4.0_Licensing_Debate)
- **AI agents:**
  - Cline: $32M seed plus Series A (31 July 2025; Emergence and Pace).
  - Kilo Code: $8M seed [R]. — [wetheflywheel](https://wetheflywheel.com/en/comparisons/opencode-vs-roo-code-vs-cline/)
- **Kestra:** $25M Series A led by RTP Global (31 March 2026). — [Axios](https://www.axios.com/pro/enterprise-software-deals/2026/03/31/workflow-orchestration-kestra-enterprise)
- **Activepieces:** YC $0.5M convertible note (September 2022); no later round found. — [Seedtable](https://seedtable.com/companies/activepieces/funding-rounds/seed-2022-08)
- **Dokploy:**
  - Cloud runs about $4.50 per server per month; Startup tier from $15/month [R, conflicting aggregators]. — [toolradar](https://toolradar.com/tools/dokploy/pricing); [noizz](https://noizz.io/insights/dokploy-year-progress)
  - 21 January 2026: moved the existing code to standard Apache 2.0 and added a *source-available enterprise licence for future paid features*. It promised to "never" move existing OSS functionality to the paid licence (open core). — [Dokploy blog](https://dokploy.com/blog/we-are-updating-dokploys-open-source-license)

**Exits and larger contrasts**
- **Payload:** acquired by Figma, announced 17 June 2025, terms undisclosed. Figma first approached about a Series A. The repo is said to stay MIT. — [Crain's](https://www.crainsgrandrapids.com/news/technology/grand-rapids-tech-firm-acquired-by-san-francisco-web-designer); [CMSWire](https://www.cmswire.com/digital-experience/when-cms-meets-ux-design-what-figmas-payload-deal-really-means); [UI Things](https://uithings.com/?p=766)
- **VoidZero (Vite, Oxc, Rolldown):**
  - $12.5M Series A (Accel, 30 October 2025).
  - Reportedly acquired by, or joined, Cloudflare in June 2026, with projects staying MIT. Not confirmed from a primary source. — [DealStreetAsia](https://www.dealstreetasia.com/stories/voidzero-accel-461657); [Dealroom](https://dealroom.co/companies/voidzero/)
- **n8n (contrast, no longer small):** $180M Series C at a $2.5B valuation (October 2025, Accel), then SAP investment at a reported $5.2B (May 2026). — [Sifted](https://sifted.eu/articles/n8n-hits-2-5bn-valuation); [itechguides](https://www.itechguides.com/?p=554068)

### How they avoided angering the community (evidence)
- **Dokploy:** an explicit written promise never to relicense existing features; only *new* paid features are source-available. — [Dokploy blog](https://dokploy.com/blog/we-are-updating-dokploys-open-source-license)
- **Coolify:** the self-hosted product is fully free; Cloud is priced very low ($5); no VC (so no pressure to reprice). — [bex.co](https://bex.co/blog/2026/08/16/coolify-bootstrapped-vs-vc-repricing-treadmill)
- **Drizzle:** sponsor-funded and later a corporate patron (PlanetScale) rather than relicensing; the project stays open source. — [Makerkit](https://makerkit.dev/blog/tutorials/drizzle-vs-prisma)
- **Zod:** a disclosed sponsor-for-branding trade (Clerk) instead of paywalling. — [Zod blog](https://zod.dev/blog/clerk-fellowship)
- **Ghostty:** non-profit structure removes any monetization suspicion. — [mitchellh.com](https://mitchellh.com/writing/ghostty-non-profit)

### Inferences
- [E] For solo developer-infrastructure tools, "free self-host plus a cheap managed control plane plus visible donations" can reach about $15–20k/month (Coolify). That is enough for one person, but not a VC-scale business.
- [E] The bootstrapped library model (Drizzle, Zod) tends to end in corporate patronage: PlanetScale, Clerk, Cloudflare for Hono and VoidZero.
- [E] VC-backed small open-source companies raise when stars are modest: Unkey at 1.2k, Trigger.dev at about 4k, Cal.com at about 9k. Investors (Essence, OSS Capital, YC) treat early stars plus usage as the signal.

### Gaps
- No ARR figures found for Unkey, Trigger.dev, Documenso, Formbricks, OpenStatus, Dub, Dokploy or Infisical.
- No sponsor income totals for Atuin, Zellij, Hono, Biome or Oxc.
- Whether Atuin raised venture funding: not found (unverified recollection that Atuin raised a seed in 2024; treat as unconfirmed).
- Continue.dev funding: search budget exhausted.

---

## 5. What did NOT work

### Takeaway
Documented failure modes:
- **Stars without users or revenue:** OpenStatus admitting it "chased stars"; Maybe's 54k stars on a dead company.
- **Fake-star inflation**, which helps for less than 2 months and then becomes a liability.
- **Licence tightening backlash:** Open WebUI, tldraw 4.0.
- **Fork volatility in AI tools:** Roo Code shut down after forking Cline.
- **Maintainer fatigue on sponsor-only funding:** lazygit.

### Cited findings
- **OpenStatus retrospective (May 2026):** the team admits it was "chasing stars instead of talking to the people actually using the product." Self-hosting "was hard, even for them," and the "open source" marketing was "partly cope." It dropped synthetic monitoring as the headline product and rebuilt the dashboard [S]. — [OpenStatus blog](https://www.openstatus.dev/blog/a-year-of-openstatus-may-2026)
- **Maybe Finance:**
  - Viral open-sourcing (#1 GitHub Trending for a week; about 54k stars) did not save the business.
  - July 2025 pivot to B2B: "about 6,000 paying customers short of breaking even, with only around 200 paying customers."
  - The company was later shut down and its assets, including 40+ repos, liquidated. — [Pigford pivot post](https://x.com/Shpigford/status/1947725345244709240); [shutdown post](https://x.com/Shpigford/status/2038774838475805081); [Failory](https://newsletter.failory.com/p/3-reasons-maybe-failed)
  - A community fork, "Sure," continues. — [Econumo](https://econumo.com/docs/comparison/econumo-vs-maybe-finance/)
- **Fake stars:**
  - The CMU, NC State and Socket "StarScout" study found about 6M suspected fake stars across 18,617 repos from about 301k accounts (2019–2024). The early version reported 4.5M across 15,835 repos.
  - Fake-star activity surged in 2024. Fake stars "only have a promotion effect in the short term (i.e., less than two months) and become a liability in the long term."
  - Accepted at ICSE 2026. — [arXiv 2412.13459](https://arxiv.org/abs/2412.13459); [ICSE 2026](https://conf.researchr.org/details/icse-2026/icse-2026-research-track/14/Six-Million-Suspected-Fake-Stars-on-GitHub-A-Growing-Spiral-of-Popularity-Contests); [Computing](https://www.computing.co.uk/news/2025/security/fake-github-stars-inflating-malicious-repositories)
- **Open WebUI licence changes:**
  - January 2025: BSD-3 plus an anti-endorsement clause, citing impersonation scams. — [GitHub Discussion #8467](https://github.com/open-webui/open-webui/discussions/8467)
  - v0.6.6 (19 April 2025): a custom "Open WebUI License" with a CLA and a branding-retention clause above 50 users unless an Enterprise licence is bought. — [Lobsters](https://lobste.rs/s/lyzca7/open_webui_changed_its_license_open_webui); [promptquorum](https://www.promptquorum.com/local-llms/open-webui-review); [opsily](https://opsily.com/hosting/open-webui/open-webui-enterprise-license)
  - Backlash: non-OSI concerns and fork talk on HN (59 comments). — [BigGo Finance](https://finance.biggo.com/news/202511041923_open-webui-license-change-backlash)
- **tldraw:**
  - December 2023 licence: free for non-commercial use only. — [isitreallyfoss](https://isitreallyfoss.com/projects/tldraw/)
  - SDK 4.0 (September 2025): production use requires a trial, commercial or hobby licence. A $6,000/year per team cost sparked "heated discussions" over accessibility for small startups. — [tldraw SDK 4.0](https://tldraw.dev/blog/tldraw-sdk-4-0); [HN](https://news.ycombinator.com/item?id=45293839); [BigGo](https://biggo.com/news/202509190115_tldraw_SDK_4.0_Licensing_Debate)
  - It still produced $1M first-year licence revenue and a $10M Series A, so the commercial outcome was positive despite the backlash. — [tldraw Series A](https://tldraw.dev/blog/announcing-tldraw-series-a)
- **Rome to Biome:** Rome (VC-backed) was abandoned. The community fork Biome continued and won the Prettier bounty. This shows a funded company can die while the community carries the project on. — [Biome blog](https://www.biomejs.cn/en/blog/biome-wins-prettier-challenge/)
- **AI-agent fork churn:** Roo Code (a Cline fork) shut down in May 2026; Kilo (a Roo fork) absorbed its users. — [wetheflywheel](https://wetheflywheel.com/en/comparisons/opencode-vs-roo-code-vs-cline/)
- **Maintainer fatigue:** Jesse Duffield (lazygit, 58k stars, 122 sponsors) writes that he has "less time (aka motivation)" to contribute with each passing day. — [sponsors.ecosyste.ms](https://sponsors.ecosyste.ms/accounts/jesseduffield)
- **Bounty dynamics:** Algora bounties draw 8–158 competing PRs, and the global board went 404 in August 2026, suggesting contraction. — [DEV.to](https://dev.to/aion_autonomous_org/i-measured-the-open-source-bounty-market-before-entering-it-then-i-didnt-enter-93n)
- **Influencer traffic skews junior,** per Novu's growth lead. — [DEV interview](https://dev.to/crowddotdev/how-to-grow-a-github-project-to-20k-stars-with-nevo-david-novu-3i81)

### Inferences
- [E] Stars are a fundraising and distribution signal, not a revenue signal. Maybe (54k stars, 200 paying customers) and OpenStatus (9k stars, admitted star-chasing) are the clearest cautionary cases.
- [E] Changing a licence after people have adopted the tool causes the most backlash (Open WebUI, tldraw). Dokploy's "new features only, never retroactive" framing is the least risky way to do it.
- [E] Forks of a hot project gain stars fast, but they depend on the parent's momentum and on their own funding. In AI tooling this period showed consolidation (Roo → Cline; Kilo absorbing Roo's users).

### Gaps
- Specific cases of contributor churn (contributors who leave) at small tools: no sourced data.
- Direct community reaction to Dokploy's January 2026 licence change: not found.
- Hacktoberfest spam and maintainer burden: search budget exhausted.
- n8n's Sustainable Use Licence backlash history: not covered in the search results.
