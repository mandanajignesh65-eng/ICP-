# Classic (non-AI-native) devtool and developer-platform GTM playbooks: tool-by-tool fact base

Research date: 2026-10-15. Method note: web fetch of primary pages (posthog.com, supabase.com, accel.com, etc.) was blocked by the session's network proxy, so findings below come from search-result extracts of those pages plus secondary coverage. Every metric is dated. "FACT (company-reported)" means the company or founder said it; "ESTIMATE" means a third party (Sacra, StartupHub, review sites) modeled it; neither is audited unless stated.

## Q1. Primary acquisition channels and launch story, per tool (HN, Product Hunt, waitlist, invite-only, OSS stars)

### Takeaway
Nearly every winner had one sharp launch moment on a developer-native venue (Hacker News, Product Hunt, PyCon lightning talk, Chrome Web Store/Stack Overflow, GitHub), then kept launching repeatedly. After that, growth came mostly from word of mouth driven by the product. Productivity apps (Arc, Fig, Linear) leaned on waitlists and invite gates. Infrastructure platforms (Supabase, PostHog, Docker, Bun, Sentry) leaned on open-source repos and HN.

### Cited Findings

**Raycast (Mac launcher, productivity)**
- Founded 2020 by ex-Facebook engineers Thomas Paul Mann and Petr Nikolaev. YC W20. Built v1 in about 3 months. Team grew from 2 to 5 by end of 2020, then to 10 — [Changelog #587 / search extract](https://changelog.com/podcast/587); [UKTN](https://www.uktech.news/funding/raycast-funding-public-beta-20211130)
- Product Hunt cadence: Raycast 1.0 (Oct 2020), Ray.so (Feb 2021), Raycast API + Store (Nov 2021). An observer counted "15 launches in 6 years". The Windows PH page says it was the 16th Raycast launch — [fmerian on X](https://x.com/fmerian/status/2074818307207856216); [Product Hunt](https://www.producthunt.com/products/raycast?launch=product-hunt-for-raycast)
- Mann: extensions were "the stepping stone that really enabled us to grow, and brought in this amazing community." DAUs grew from 130 (Oct 2020) to over 11,000 (Nov 2021), per funding coverage of the $15M round. FACT (company-reported) — [UKTN, Nov 2021](https://www.uktech.news/funding/raycast-funding-public-beta-20211130)
- The API/Store public beta (late 2021) let developers build an extension "in less than 30 minutes" and share it with their team or the community — [UKTN](https://www.uktech.news/funding/raycast-funding-public-beta-20211130)

**Linear (issue tracking, productivity)**
- Founded 2019 by Karri Saarinen, Tuomas Artman and Jori Lallo (ex-Uber, Airbnb, Coinbase) — [The Hub](https://thehub.io/startups/linear-1)
- Growth was mostly word of mouth. The product was designed to be screenshot-worthy, so "when users screenshot Linear in tweets, blog posts, or Slack messages, the product markets itself." In the first two years the team focused on fit with early-stage startups — [Eleken case study](https://eleken.co/blog-posts/linear-app-case-study); [IdeaPlan](https://www.ideaplan.io/blog/how-linear-grew-to-1-billion-with-35k-marketing-spend)
- Lifetime marketing spend of about $35k, which secondary sources say Saarinen shared publicly. Secondary source; the primary quote was not retrieved — [IdeaPlan](https://www.ideaplan.io/blog/how-linear-grew-to-1-billion-with-35k-marketing-spend)

**Arc browser (The Browser Company)**
- Invite-only on Mac for a long period. Opened to everyone with the 1.0 release in July 2023, when it dropped a waitlist reported at over 1 million people. The waitlist figure varies across outlets — [9to5Mac, Jul 2023](https://9to5mac.com/2023/07/25/arc-browser-no-waitlist/); [TechCrunch](https://techcrunch.com/2023/12/11/arc-browser-launches-its-windows-client-in-beta/)
- Windows: more than 500,000 on the waitlist in Dec 2023 when beta onboarding began. GA in 2024 followed a beta with over 150,000 testers — [TechCrunch Dec 2023](https://techcrunch.com/2023/12/11/arc-browser-launches-its-windows-client-in-beta/); [AlternativeTo May 2024](https://alternativeto.net/news/2024/5/the-browser-company-finally-launches-the-windows-version-of-the-arc-web-browser/)
- The company later pivoted to Dia (an AI browser) and gated it behind a waitlist, with Arc users getting priority beta access. Commentators criticized this as abandoning Arc's devoted base — [Subscription Insider](https://www.subscriptioninsider.com/?p=124388)

**Fig (terminal autocomplete)**
- YC S20, founded by Brendan Falk and Matt Schrage. $2.2M seed — [TechCrunch](https://techcrunch.com/?p=2193972); [YC](https://www.ycombinator.com/companies/fig)
- Mac-only beta behind a waitlist. One user waited about 2 weeks. The waitlist email said people who "really wanted" instant access could ask, and users got in by contacting the team on Twitter or by email (a hand-onboarding tactic) — [travis.media](https://www.travis.media/im-off-the-fig-waitlist/)
- Product Hunt launches: 7 Jul 2020 (visual apps/shortcuts), 25 May 2021 (autocomplete). General availability reported 17 Sep 2021 — [hunted.space](https://hunted.space/dashboard/fig/launches/fig-5); [Product Hunt](https://www.producthunt.com/products/fig/launches/fig-6)
- Acquired by AWS (Aug 2023, terms undisclosed). Paid features made free for existing users, then the standalone product was sunset. The technology was folded into Amazon Q Developer, and the closed-source successor frustrated users — [TechCrunch](https://techcrunch.com/?p=2591683); [GeekWire](https://www.geekwire.com/tag/fig/); [GitHub issue](https://fr.github.com/withfig/autocomplete/issues/2068)

**Obsidian (notes, productivity)**
- About 1 million users (company estimate, 2023, based on download counts because the app has no analytics). Discord had over 110,000 members. Team of under a dozen people (2023) — [MacStories](https://www.macstories.net/news/obsidians-popularity-explained/); [Wikipedia](https://en.wikipedia.org/wiki/Obsidian_(software))
- Community plugin ecosystem of more than 1,800–2,000 plugins (2026 sources). Distribution runs through the community: Discord, forum, YouTube/PKM creators — [Obsidian stats hub](https://publish.obsidian.md/hub/04+-+Guides%2C+Workflows%2C+%26+Courses/Guides/Obsidian+ecosystem+statistics); [Wikipedia](https://en.wikipedia.org/wiki/Obsidian_(software))
- "100% user-supported", no VC funding — [Steph Ango (CEO)](https://stephango.com/vcware)

**Notion (developer adoption)**
- Growth came from templates, the ambassador program (started 2019; over 300 ambassadors in 30+ countries by 2023), creators on YouTube and TikTok, and team referrals. Early Product Hunt presence helped. Secondary sources only — [Synergy Startup](https://synergystartup.substack.com/p/notion-growth-strategy-behind-100m); [IdeaPlan](https://www.ideaplan.io/blog/how-notion-built-a-product-led-growth-engine)
- Developer/API adoption numbers are not public — [Toolfinder](https://toolfinder.com/lists/notion-in-statistics)

**Supabase**
- The planned launch was pre-empted when an early user posted the site on Hacker News. It stayed on the HN front page for several days, bringing about 30,000 visitors and over 1,400 signups in 7 days (alpha, 2020). FACT (company postmortem, via summary) — [Supabase "How we launch"](https://supabase.com/blog/supabase-how-we-launch); [Plushcap summary of alpha postmortem](https://plushcap.com/analysis/supabase/alpha-launch-postmortem)
- "Launch Day" became "Launch Week" in the last week of March 2021: 7 major features shipped and an "immediate uptick in growth rate." Supabase credits the format as part of a product-led growth strategy — [Supabase blog](https://supabase.com/blog/supabase-how-we-launch); [Product Hunt Stories repost (attributed to Ant Wilson)](https://www.producthunt.com/stories/how-we-launch-at-supabase)

**PostHog**
- YC W20. Hacker News launch about 4 weeks after the first line of code: 300+ self-hosted deployments within days and 1,500 GitHub stars two weeks later. PostHog claims it was "the most successful B2B software launch on HN since 2012" (company claim) — [History of PostHog](https://posthog.com/hogpedia/history-of-posthog); [Morgan Perry DevTools Brew #64](https://morganperry.substack.com/p/devtools-brew-64-posthog-reaching)
- Older recruiting profile: 97% of growth from word of mouth; no outbound sales team (PLG) — [Wellfound](https://wellfound.com/company/posthoghq)

**Resend**
- YC company. Launched on Product Hunt (reached #2 on launch day per Resend's LinkedIn; date not shown in the snippet) — [Resend LinkedIn](https://www.linkedin.com/posts/resend_resend-email-for-developers-product-hunt-activity-7100116159252819968-XuyX?trk=public_profile_like_view); [YC](https://www.ycombinator.com/companies/resend)
- The open-source React Email library is the top-of-funnel. Stars: 5.1k (early, YC page), 15,509 (React Email 4.0), 17,041 (React Email 5.0), about 19.7k (13 Sep 2026). React Email 6.0 launched on PH 18 Apr 2026 (#7, 139 upvotes) — [YC](https://www.ycombinator.com/companies/resend); [Resend blog: React Email 4](https://resend.com/blog/react-email-4); [React Email 5](https://resend.com/blog/react-email-5); [Star History](https://www.star-history.com/resend/react-email/); [hunted.space](https://hunted.space/dashboard/react-email-6-0-resend)
- Founder Zeno Rocha was previously VP Developer Experience at WorkOS — [Crunchbase](https://crunchbase.com/organization/resend)

**Postman**
- Abhinav Asthana built it as a side project while interning at Yahoo Bangalore and released it free on the Chrome Web Store. The first public announcement was a Stack Overflow answer/post. It reached nearly 500k users while still only a Chrome extension, many of them non-developers — [eChai GTM teardown](https://echai.ventures/gtm/gtm-teardowns/what-did-postman-do-differently-to-get-developers-to-adopt-before-it-ever-sold-anything); [Contrary Research](https://research.contrary.com/company/postman)

**Docker**
- Solomon Hykes first demoed Docker publicly in a 5-minute PyCon lightning talk on 15 Mar 2013 (cut off by the timekeeper). It was open-sourced the same month, and early adopters came via conferences such as OSCON 2013 — [Docker blog](https://www.docker.com/blog/tag/docker/page/17/?page=1); [Snyk 10-year retrospective](https://snyk.io/blog/the-docker-project-turns-10/); [ActiveState](https://www.activestate.com/?p=5167)
- Docker Captains program: community experts who share knowledge (start date not found) — [Docker blog](https://www.docker.com/blog/tag/docker/page/17/?page=1)

**Bun**
- Initial release 14 Sep 2021; 1.0 on 8 Sep 2023. Origin: Jarred Sumner was frustrated by a 45-second edit-reload loop while building a browser game. Oven raised $7M (24 Aug 2022). About 40k GitHub stars by June 2023; over 82k by Dec 2025 — [Wikipedia](https://en.wikipedia.org/wiki/Bun_(software)); [InfoWorld interview](https://www.infoworld.com/article/3700870/interview-with-jarred-sumner-buns-creator-talks-tech-funding-and-startups.html)
- Acquired by Anthropic (announced 2–3 Dec 2025, undisclosed price). Stays MIT-licensed — [Gigazine](https://gigazine.net/gsc_news/en/20251203-anthropic-acquired-bun)

**Netlify**
- Popularized "Jamstack" as a category term and community: a conference, the Jamstack Community Discord, and an ecosystem of startups such as Gatsby. Origin of the term is disputed: a defining blog post appears backdated to 2015, and Biilmann said it was "maybe not even me" who coined it. Netlify later closed the Jamstack Discord over declining engagement and shifted to "composable web" framing — [The New Stack](https://thenewstack.io/is-jamstack-toast-some-developers-say-yes-netlify-says-no/); [Heavybit Jamstack Radio ep 2](https://www.heavybit.com/library/podcasts/jamstack-radio/ep-2-the-jamstack-origin-story/); [The New Stack on Gatsby](https://thenewstack.io/netlify-acquires-gatsby-its-struggling-jamstack-competitor/)

**Railway**
- Grew to about 2 million developers "without marketing" before its $100M Series B (TQ Ventures lead, Jan 2026). About 30 employees. The new funds go to the company's "first organized go-to-market strategy" — [Crypto Briefing](https://cryptobriefing.com/railway-secures-100-m-expand-ai-ready-cloud-platform/?rand=59535); [Preqin](https://www.preqin.com/data/profile/asset/railway-corporation/456313)

**Tailscale**
- Word of mouth from the free personal plan sells corporate plans. The CEO wrote that each product-quality improvement raised the growth rate "that same day." The company invested early in its subreddit, including building a moderator team — [Tailscale "free plan" blog](https://tailscale.com/blog/free-plan); [Foundation Inc Reddit teardown](https://foundationinc.co/lab/tailscale-reddit-strategy)

**Neon**
- Open-source (Apache 2.0) serverless Postgres. By GA, 30% of databases were created by AI agents; by May 2025 the share was over 80% (Databricks-reported telemetry). Acquired by Databricks for about $1B (May 2025) — [Databricks blog](https://www.databricks.com/blog/databricks-neon); [Yahoo Finance/TechCrunch](https://au.finance.yahoo.com/news/databricks-buy-open-source-database-120751104.html)

### Inferences
- HN was decisive for open-source infrastructure (Supabase, PostHog, Bun). Product Hunt was decisive for Mac and productivity apps (Raycast, Fig, Resend), and those companies treated PH as a repeatable channel (Raycast's 15–16 launches) rather than a one-time event.
- Waitlist/invite-only worked for consumer-grade productivity tools with high switching costs (Arc, Fig, early Linear). It builds scarcity and lets the team onboard by hand, but none of them published waitlist-to-active conversion.
- Agent-created workloads (Neon over 80%, Supabase over 60%; see Q4) are now an acquisition channel in their own right for database platforms. That breaks the classic human-developer funnel.

### Gaps
- Linear's 2019–2020 waitlist/private beta size: no source found (the First Round podcast covers it, but the content wasn't retrieved).
- Fig and Bun HN launch thread metrics: not found.
- Raycast total user count: not disclosed. TechCrunch (Sep 2024) says Mann declined to share Pro subscriber numbers.
- GitLab and HashiCorp early launch details were not researched in depth (time budget).

## Q2. Signature tactics (launch weeks, handbook/brand, design-led, extension store, founder-led X, blog, OSS flywheel, sponsorships, free-to-enterprise)

### Takeaway
Each winner had one signature, repeatable "media" mechanic it owned. Supabase had Launch Weeks plus hackathons. PostHog had brand, writing and weird ads. Linear had craft and design as the marketing. Raycast had an extension store plus PH cadence. Vercel had Next.js. Sentry had developer podcasts (it bought Syntax) and OSS funding. Clerk had creator integrations rather than scripted ads. Postman had free-to-team collaboration.

### Cited Findings

**Supabase: Launch Weeks**
- Origin was March 2021 (7 features in one week). Launch Weeks recur at irregular intervals, not strictly quarterly: LW6 Dec 2022, LW12 Aug 2024, LW13 Dec 2024, LW14 Mar 2025, LW15 Jul 2025 — [Supabase blog](https://supabase.com/blog/supabase-how-we-launch); [Paul Copplestone author page](https://supabase.com/blog/authors/paul_copplestone); [releases.sh](https://releases.sh/release/rel_RHsJJY4yCEXXFJ69ICsZo)
- Each LW is paired with a community hackathon. LW15: a 10-day build window (18–27 Jul 2025), teams of up to 4, limited-edition swag and a "Hackathon Hall of Fame" — [dev.to Supabase](https://dev.to/supabase/supabase-launch-week-15-hackathon-2ajk)
- Company claim: databases managed grew 47% month-on-month for 18 months, credited partly to the launch-week format — [Supabase blog](https://supabase.com/blog/supabase-how-we-launch)
- GitHub stars: 25k (Nov 2021 LW recap), over 50k (Aug 2023, LW8) — [LW Nov 2021 recap mirror](https://git.gay/root/supabase.supabase/src/branch/master/apps/www/_blog/2021-12-15-beta-november-2021-launch-week-recap.mdx); [Plushcap LW8](https://plushcap.com/analysis/supabase/supabase-launch-week-8-community-highlights)

**PostHog: transparent handbook, quirky brand, content**
- The paid-ads handbook says ads exist to "generate sales leads and convert high-intent engineers into signups", not for general brand awareness. Channels: Google Search, Bing, LinkedIn. Conversion tracking runs through PostHog, BigQuery, Clay, Clearbit and Census rather than third-party pixels. Paid ads for a product only after it is GA with pricing — [PostHog handbook: Paid ads](https://posthog.com/handbook/marketing/paid)
- Out-of-home and guerrilla tactics: SF billboards (Jan 2025, an X post joking about cost and offering merch for photos); Muni bus ads saying "you may be entitled to PostHog", which parodied the pain of SaaS sales calls (2025); a lemonade stand in SF handing out early-access invites — [PostHog on X](https://x.com/posthog/status/1879740868447395848); [SF Standard](https://sfstandard.com/2026/09/15/promiscuous-claude-stuns-new-ai-billboard/); [Nate Matherson on X](https://x.com/NateMatherson/status/1923809756625445255); [uglyGTM](https://www.uglygtm.com/blog/guerrilla-marketing-examples)
- Wynter workshop title: "$45,000 a month for weird ideas: how PostHog does marketing." The page content wasn't retrieved, so the budget's scope is unverified — [Wynter](https://wynter.com/posthog-weird-ideas-marketing-workshop)
- "Product for Engineers" Substack newsletter, deliberately not about PostHog: grew from about 38k to over 100k subscribers in 2025 (company-reported year-end recap) — [Best of Product for Engineers 2025](https://newsletter.posthog.com/p/the-best-of-product-for-engineers); [Subscribe page](https://newsletter.posthog.com/subscribe)
- MKT1 cites PostHog as the archetype of "bold, memorable, opinionated creative" that makes billboards work — [MKT1 newsletter](https://newsletter.mkt1.co/p/sf-billboard-drive-by-1)

**Linear: design-led, "quality" positioning**
- The product is meant to be so good that people talk about it. Users screenshot it in tweets, blogs and Slack, so the craft itself is the distribution. Built out of frustration with slow, cluttered tools (implicitly Jira) — [Eleken](https://eleken.co/blog-posts/linear-app-case-study); [The Hub](https://thehub.io/startups/linear-1); [First Round Review podcast](https://review.firstround.com/podcast/inside-linear-why-craft-and-focus-still-win-in-product-building/)
- The founders deliberately avoided the hyper-growth playbook they had seen at prior employers — [Accel Early Stage podcast](https://accel.com/podcast-episodes/how-linears-karri-saarinen-is-redefining-what-scale-looks-like)

**Raycast: extension store + free core + Pro**
- The free tier includes all Store extensions (about 1,000 in 2024; reports of 2,000–3,000+ in 2025–26). Pro adds AI, cloud sync and themes — [Raycast blog: Introducing Raycast Pro](https://raycast.com/blog/introducing-raycast-pro); [tech-insider review 2026](https://tech-insider.org/raycast-vs-alfred-2026/)
- Pro "unlocked the fundraise" for the Series B (Mann, Sep 2024) — [TechCrunch](https://techcrunch.com/2024/09/25/raycast-raises-30m-to-bring-its-mac-productivity-app-to-windows-and-ios/)
- Side-product launches (Ray.so code screenshots) serve as additional PH and social surface area — [fmerian on X](https://x.com/fmerian/status/2074818307207856216)

**Vercel: Next.js open-source flywheel**
- Next.js is Vercel's flagship OSS product. It brings developers into the ecosystem, and Vercel's hosting converts them. Acquisitions extended the framework footprint into Vue/Nuxt. v0 (an AI app generator) re-accelerated growth from 2024 — [Sacra Vercel](https://sacra.com/c/vercel); [ValueAdd VC](https://valueaddvc.com/blog/how-does-vercel-make-money-usage-based-hosting-enterprise-and-the-3-2b-valuation-breakdown)
- Theo (t3.gg) was formerly Vercel-sponsored and has since moved away — [rosetta.to summary](https://rosetta.to/u/t3dotgg/breaking-up-with-vercel)

**Sentry: developer-first, podcasts, OSS funding**
- Sponsored the Syntax.fm podcast, then bought it. Sent about $100k in free gifts to developers. Launched the Open Source Pledge ($500k to OSS maintainers) — [Software Huddle interview with David Cramer](https://softwarehuddle.substack.com/p/building-evolving-sentrys-architecture)
- Ad offer example: a 2018 Syntax episode carried a Sentry read with a coupon for 2 free months — [Syntax #100](https://www.syntax.fm/100)
- Blog claim: first company near 100% coverage of fundable dependencies via GitHub Sponsors; separate posts on giving $260,028 and $500,000 to maintainers (different years) — [Sentry blog $500k](https://blog.sentry.io/we-just-gave-500-000-dollars-to-open-source-maintainers); [Sentry blog $260k](https://blog.sentry.io/we-just-gave-260-028-dollars-to-open-source-maintainers)

**Clerk: creator sponsorships (Theo etc.)**
- SponsorRadar detected 14–16 Clerk-sponsored videos on Theo's channel (about 500k subs). These counts are inferred from video content and the two pages disagree — [SponsorRadar Clerk](https://sponsorradar.com/brands/clerk); [SponsorRadar t3dotgg](https://sponsorradar.com/channels/t3dotgg)
- Clerk's team (talk summary): it approached creators by asking them to try the product rather than buying transactional reads, and said "long-form sponsored videos focused on the product alone didn't really work" — [Newslepear #86](https://newslepear.beehiiv.com/p/86-masterclass-into-youtube-influencers-last-sign-up-step-idea-and-more-learnings-on-great-docs)
- Theo claims over 3M views a month and an audience of experienced developers (self-reported) — [t3.gg sponsor page](https://t3.gg/sponsor-me)
- Menlo's positioning: a component-first approach (drop-in React/Next.js UI) cuts implementation "from weeks to hours" — [Menlo VC](https://menlovc.com/perspective/for-the-love-of-the-developer-clerks-series-c/)

**Resend: founder-led, developer-experience brand**
- React Email OSS plus a polished DX brand; versioned releases are launched on PH and the blog — [Resend blog](https://resend.com/blog/react-email-5); [hunted.space](https://hunted.space/dashboard/react-email-6-0-resend)

**Tailscale: blog, free plan, Reddit**
- A long-form founder blog explains both the economics ("how our free plan stays free": low scaling costs, users aren't the product) and the strategy, which is that free personal use creates word of mouth that sells corporate plans — [Tailscale blog](https://tailscale.com/blog/free-plan); [Plushcap summary](https://www.plushcap.com/content/tailscale/blog/tailscale-how-our-free-plan-stays-free)
- Subreddit community and moderator investment — [Foundation Inc](https://foundationinc.co/lab/tailscale-reddit-strategy)

**Postman: free-to-enterprise**
- Ran a customer success team instead of a sales team (bottom-up). Opening collaboration features to free trial users "produced a large jump in conversions" — [eChai teardown](https://echai.ventures/gtm/gtm-teardowns/what-did-postman-do-differently-to-get-developers-to-adopt-before-it-ever-sold-anything)
- Investors: Nexus at seed; CRV and Insight came in once usage was established — [VCBeast](https://vcbeast.com/companies/postman)

**GitLab: public handbook + buyer-based open core**
- The public handbook documents "buyer-based open core" pricing. The likely buyer sets the tier (Free = individual contributor, Premium = manager/director, Ultimate = executive). OSS features drive popularity, and higher tiers capture ARR. The CEO owns pricing — [GitLab handbook: tiering](https://handbook.gitlab.com/handbook/product/tiering-guidance-for-features/); [GitLab pricing tiers handbook](https://handbook.gitlab.com/handbook/marketing/brand-and-product-marketing/product-and-solution-marketing/pricing-tiers/)
- In 2020 GitLab open-sourced 18 previously paid features ("if a feature can be moved down, do it quickly") — [DevClass](https://devclass.com/2020/03/31/gitlab-asks-customers-to-help-it-open-source-a-raft-of-features)
- PostHog cites GitLab as a company that shaped PostHog, the likely lineage of PostHog's public handbook — [PostHog newsletter](https://posthog.com/newsletter/the-companies-that-shaped-posthog.md)

**Notion: templates + ambassadors + creators**
- See Q1. The loop: more users bring more creators, which brings more content and then more users — [Synergy Startup](https://synergystartup.substack.com/p/notion-growth-strategy-behind-100m)

### Inferences
- The common thread is owning a recurring "news event" that the company controls. Examples are Supabase LWs, Raycast PH launches, PostHog stunts and Resend React Email versions. This replaces paid reach with earned reach.
- Creator sponsorships work when the creator is genuinely a user and integrates the product into real builds (Clerk's lesson). Scripted product-only long-form videos underperform.
- A public handbook (GitLab, then PostHog) acts as recruiting, trust-building and SEO content at the same time.

### Gaps
- Primary-source detail on PostHog's $45k/month "weird ideas" budget (page unreachable).
- Resend: no retrievable data on Zeno Rocha's X posting cadence or signups attributable to X.
- Sentry's Syntax acquisition price/date is confirmed only via the interview summary.

## Q3. Pricing models and free-to-paid / bottom-up-to-enterprise conversion

### Takeaway
The dominant pattern is a generous free tier (often with no credit card) plus a paid trigger at the moment of team collaboration or commercial use. Infrastructure platforms meter usage (PostHog, Vercel, Netlify, Supabase, Neon). Productivity tools charge per seat (Linear) or sell a flat Pro add-on (Raycast). Open-core projects tier features by buyer (GitLab). Several companies tightened free tiers after establishing ubiquity (Docker 2021, Postman 2026, HashiCorp BSL 2023), with real backlash risk.

### Cited Findings
- **PostHog:** every product has a free tier with no credit card: 1M analytics events, 5k session recordings and 1M flag requests per month. Pay-as-you-go with a $0 base, no per-seat fees, billing limits, and no sales call needed. Over 90% of companies use PostHog for free (company docs). Boost $250/mo and Scale $750/mo platform packages; Enterprise is contact-sales — [PostHog pricing](https://posthog.com/pricing.md); [PostHog docs](https://posthog.com/docs/product-analytics/pricing.md); [Cube review](https://cubeapm.com/blog/posthog-pricing-and-review/)
- Sacra: usage-based self-serve is a distribution advantage over Amplitude and LaunchDarkly, which route larger plans through sales. An engineer installs a snippet and teams expand product by product — [Sacra](https://sacra.com/chat/h/06f0c870-7a2a-4150-8cb7-09b60079aa04/)
- **Raycast:** free core includes all store extensions. Pro is $10/mo monthly or $8/mo annual (AI, cloud sync, themes). Advanced AI add-on brings the total to about $16–18/mo. Teams $12/user/mo annually — [Raycast Pro blog](https://raycast.com/blog/introducing-raycast-pro); [Toolradar](https://toolradar.com/tools/raycast/pricing)
- **Tailscale:** the free plan expanded from 1 to 3 users (Apr 2023, pricing v3). Personal use is "free forever". Corporate control features are what companies pay for — [Tailscale pricing v3](https://tailscale.com/blog/pricing-v3); [Tailscale FAQ](https://tailscale.com/docs/reference/faq/pricing)
- **Sentry:** free Developer plan (1 user, 5k errors/mo), Team $26/mo, Business $80/mo, Enterprise by quote (aggregator data). Self-hosted option is free. Sacra: self-serve is about 70% of revenue — [Sacra Sentry](https://sacra.com/c/sentry/); [Toolradar](https://toolradar.com/tools/sentry/pricing)
- **Vercel:** Hobby is free but non-commercial only (about 100GB bandwidth; hard limits, no overage). Pro is $20/user/mo with usage credits. Enterprise is usage-based. The commercial-use clause is the conversion trigger — [Orb](https://withorb.com/blog/vercel-pricing); [ValueAdd VC](https://valueaddvc.com/blog/how-does-vercel-make-money-usage-based-hosting-enterprise-and-the-3-2b-valuation-breakdown)
- **Netlify:** moved to credit-based pricing in Sep 2025. Free gets 300 credits/mo (sites pause when depleted). Personal $9/mo (1,000 credits); Pro $20/member — [Makerstack review](https://makerstack.co/reviews/netlify-review/); [CostBench](https://costbench.com/software/cloud-infrastructure/netlify/free-plan/)
- **Neon:** after the Databricks deal, storage dropped to about $0.35/GB-month, compute fell 15–25%, and free-tier compute doubled. Sources conflict on the exact free-tier limits — [SaaS Price Pulse](https://www.saaspricepulse.com/tools/neon); [agentdeals](https://agentdeals.dev/vendor/neon)
- **Postman:** in March 2026 the free plan became single-user (no team workspaces). New tiers: Solo $9/mo, Team $19/user/mo, Enterprise $49/user/mo (annual). Previously up to 3 users could collaborate free (third-party claim). One tracker dates the change to 24 Apr 2026 — [Postman docs: about plans](https://learning.postman.com/latest-v-12/docs/billing/about-plans.md); [Apidog](https://apidog.com/de/blog/postman-free-vs-paid-comparison); [CostBench](https://costbench.com/changelog/postman-plans-renamed-2026-04/)
- **Docker:** on 31 Aug 2021, Docker Desktop became paid for companies with over 250 employees or over $10M revenue. It stayed free for small business, personal, education and non-commercial OSS (about half the user base, per the company). Grace period ran to 31 Jan 2022. Before this, revenue came from Docker Hub add-ons. In Oct 2022 Team went from $84 to $108/user/yr, Business from $252 to $288, and Team was capped at 100 users — [InfoWorld](https://www.infoworld.com/article/2268969/docker-desktop-is-no-longer-free-for-enterprise-users.html); [DevClass](https://devclass.com/2022/10/20/docker-quietly-raises-prices-limits-team-accounts); [Sacra Docker](https://sacra.com/c/docker/)
- **HashiCorp:** moved Terraform and Vault from MPL to BSL in Aug 2023. This triggered the OpenTofu fork (Linux Foundation) and OpenBao (Vault fork). Revenue growth was already slowing beforehand. IBM acquired HashiCorp for about $6.4B ($35/share), closing 27 Feb 2025 — [The Register](https://www.theregister.com/2025/02/28/ibm_hashicorp_deal_closing/); [DevOps.com](https://devops.com/ibm-confirms-its-buying-hashicorp/); [Fierce Network](https://www.fierce-network.com/cloud/analysts-sound-ibms-64b-hashicorp-acquisition)
- **GitLab:** buyer-based open core with Free, Premium and Ultimate tiers mapped to IC, manager and exec buyers. Almost all revenue comes from paid-tier subscriptions — [GitLab handbook](https://handbook.gitlab.com/handbook/product/tiering-guidance-for-features/); [GitLab stewardship](https://handbook.gitlab.com/handbook/company/stewardship/)
- **Obsidian:** free core. Paid add-ons are Sync ($4/user/mo), Publish ($8/site/mo), and Catalyst (one-time $25+ supporter tier with early betas and badges). The commercial license ($50/user/yr) became optional in Feb 2025, when the app became free for all uses including commercial. Sources conflict, so check the live page — [Obsidian pricing](https://obsidian.md/pricing); [Obsidian license](https://www.obsidian.md/license)
- **Fig:** planned to fund itself via team subscriptions on top of an app ecosystem — [TechCrunch](https://techcrunch.com/?p=2193972)
- **Supabase:** ARPC (average revenue per customer) stayed roughly flat at about $700/yr while paying customers grew from 100k to over 250k in 7 months (Sacra estimate, 2026). Growth is volume-driven — [Sacra](https://sacra.com/research/supabase-170m-year-growing-221-yoy/)
- **Linear:** per-seat SaaS. Net revenue retention of 177% reported alongside its 2026 tender. This is secondary press; primary not retrieved — [Pulse 2.0](https://pulse2.com/linear-completes-99-million-tender-at-2-5-billion-valuation-as-arr-tops-100-million-and-net-retention-hits-177/)

### Inferences
- Conversion triggers cluster into four types: (1) a second user or team collaboration (Postman, Tailscale, Sentry, Linear), (2) commercial use (Vercel Hobby, Docker Desktop, Obsidian historically), (3) usage thresholds (PostHog, Netlify, Neon, Supabase), and (4) premium or AI features on a free core (Raycast Pro).
- Restricting the free tier after reaching dominance raises revenue (Docker reached about $207M ARR by 2024 per Sacra), but forks and backlash are the risk (HashiCorp's OpenTofu). Postman's 2026 single-user free plan is a live test of the same move.
- A 177% NRR (Linear) and a flat ~$700 ARPC (Supabase) show two different engines. Linear expands seats within accounts. Supabase acquires new accounts at high volume.

### Gaps
- No company in scope published an explicit free-to-paid conversion rate. The closest figure is PostHog's "over 90% of companies use it for free".
- Supabase's current free-tier limits were not verified this session.
- GitLab IPO-era revenue and conversion metrics were not retrieved.

## Q4. Published metrics (users, ARR, valuation, stars, launch signups), dated, facts vs estimates

### Takeaway
Hard company-reported numbers are rare. Most ARR figures are Sacra estimates. The most reliable figures are funding rounds, company-stated user and customer counts, and GitHub stars.

### Cited Findings
| Company | Metric | Date | Type | Source |
|---|---|---|---|---|
| Supabase | ~$170M ARR, +221% YoY; $101M end-2025; $70M Aug 2025; $30M end-2024 | May 2026 | ESTIMATE (Sacra) | [Sacra](https://sacra.com/research/supabase-170m-year-growing-221-yoy/); [Sacra $70M](https://sacra.com/research/supabase-at-70m-arr-growing-250-yoy/) |
| Supabase | Registered developers 4M to ~10M and paying customers 100k to 250k+ in 7 months; database launches +600% YoY; over 60% of new DBs launched by AI tools | to Jun 2026 | ESTIMATE/derived (Sacra) | [Sacra](https://sacra.com/c/supabase/) |
| Supabase | $500M Series F at $10.5B post, led by GIC | Jun 2026 | Reported (Sacra) | [Sacra](https://sacra.com/c/supabase/) |
| Supabase | 1,400+ signups, 30k visitors in 7 days from HN (alpha) | 2020 | FACT (company) | [Plushcap/Supabase](https://plushcap.com/analysis/supabase/alpha-launch-postmortem) |
| PostHog | ~$58M ARR, +112% YoY | Feb 2026 | ESTIMATE (Sacra) | [Sacra](https://sacra.com/research/58m-year-hedgehog-of-product-analytics/) |
| PostHog | 70,000+ teams; ~$1.4B valuation after $75M Series E (Peak XV), Oct 2025; $70M Series D led by Stripe, Jun 2025 | 2025 | FACT (company/press) | [Morgan Perry](https://morganperry.substack.com/p/devtools-brew-64-posthog-reaching); [Summify](https://summify.io/discover/from-pivot-hell-to-1-4-billion-unicorn-5WN8bf/) |
| PostHog | 300+ self-hosted deploys in days; 1,500 stars at 2 weeks | Feb 2020 | FACT (company) | [History of PostHog](https://posthog.com/hogpedia/history-of-posthog) |
| Vercel | ~$340M ARR (Feb 2026), $305M end-2025, $172M Feb 2025, ~$96M end-2023 | 2026 | ESTIMATE (Sacra) | [Sacra](https://sacra.com/c/vercel); [Sacra $172M](https://sacra.com/research/172m-year-heroku-of-vibe-coding/) |
| Linear | ARR over $100M; 40,000+ paying business customers; NRR 177%; $99M tender at $2.5B | 2026 | Press (secondary) | [Pulse 2.0](https://pulse2.com/linear-completes-99-million-tender-at-2-5-billion-valuation-as-arr-tops-100-million-and-net-retention-hits-177/) |
| Linear | $82M Series C at $1.25B (Accel lead); 15,000+ customers; profits up 280% the prior year | Jun 2025 | FACT (press) | [Built In SF](https://www.builtinsf.com/articles/linear-raises-82m-series-c-1b-valuation-20250611) |
| Linear | ~$35k lifetime marketing spend | ~2023 | Secondary, attributed to Saarinen | [IdeaPlan](https://www.ideaplan.io/blog/how-linear-grew-to-1-billion-with-35k-marketing-spend) |
| Raycast | DAU 130 to 11,000+ | Oct 2020 to Nov 2021 | FACT (company) | [UKTN](https://www.uktech.news/funding/raycast-funding-public-beta-20211130) |
| Raycast | $30M Series B (Atomico), total raised over $45M; 22,000-member developer community | Sep 2024 | FACT (press) | [TechCrunch](https://techcrunch.com/2024/09/25/raycast-raises-30m-to-bring-its-mac-productivity-app-to-windows-and-ios/); [Tech Funding News](https://techfundingnews.com/raycast-raises-30m-to-expand-mac-productivity-app-to-windows-and-ios/) |
| Tailscale | ~$160M Series C (Accel) at ~$1.45–1.5B; 10,000+ paying business customers; ARR growing over 100% YoY (undisclosed absolute) | Apr 2025 | FACT (company/press) | [BetaKit](https://betakit.com/corporate-vpn-startup-tailscale-secures-230-million-cad-series-c-on-back-of-surprising-growth/); [Verdict](https://www.verdict.co.uk/tailscale-160m-series-c-round/) |
| Tailscale | 5,000+ paying customers; hundreds of thousands of free MAU | Mar 2024 | FACT (company) | [Tailscale blog](https://tailscale.com/blog/5000-customers) |
| Tailscale | ~$18.5M 2023 revenue | 2023 | UNVERIFIED (Substack) | [devcuration](https://devcuration.substack.com/p/tailscale-series-c-160m) |
| Sentry | $100M ARR, valued over $3B | ~2024 | Investor description (Accel) | [Accel podcast](https://accel.com/podcast-episodes/how-sentrys-david-cramer-turned-an-open-source-side-project-into-a-3b-business) |
| Sentry | ~$128M ARR, ~50k customers, +30% YoY; self-serve ~70% of revenue | end-2023 | ESTIMATE (Sacra), conflicts with Accel's ~$100M | [Sacra](https://sacra.com/c/sentry/) |
| Postman | Revenue $313M (+82% YoY) | 2024 | Secondary estimate | [Value for Startups](https://valueforstartups.in/postman_report) |
| Postman | 40M+ developers, 500k companies; $5.6B valuation (2021) | ~2025 | Company-style claim via profile | [VCBeast](https://vcbeast.com/companies/postman) |
| Docker | ~$207M ARR (2024), ~$165M prior year | 2024 | ESTIMATE (Sacra) | [Sacra](https://sacra.com/c/docker/) |
| HashiCorp | ~$164M last public quarterly revenue (+15% YoY; cloud +42%); IBM $6.4B | 2024–25 | FACT (public filings via secondary) | [Salesmotion](https://salesmotion.io/company-intelligence/hashicorp); [The Register](https://www.theregister.com/2025/02/28/ibm_hashicorp_deal_closing/) |
| Netlify | Revenue $46.3M (2024) vs $33M (2023); 50M+ sites | 2024 | Secondary estimate | [Makerstack](https://makerstack.co/reviews/netlify-review/) |
| Neon | Acquired for ~$1B; over 80% of DBs created by agents | May 2025 | FACT (Databricks) | [Databricks blog](https://www.databricks.com/blog/databricks-neon) |
| Railway | ~2M developers, ~30 employees, $100M Series B, no marketing to date | Jan 2026 | Company claim via press | [Crypto Briefing](https://cryptobriefing.com/railway-secures-100-m-expand-ai-ready-cloud-platform/?rand=59535) |
| Clerk | $50M Series C (Menlo + Anthology Fund); 200M+ users managed across 15,000+ applications | 2025 (date conflicts: Jun/Jul/Oct) | FACT (company) | [Clerk blog](https://clerk.com/blog/series-c.md); [Menlo](https://menlovc.com/perspective/for-the-love-of-the-developer-clerks-series-c/) |
| Resend | $18M Series A (a16z); 200,000+ developers signed up; millions of emails/day | Dec 2024 | FACT (company) | [Resend blog](https://resend.com/blog/series-a); [EveryDev](https://www.everydev.ai/developers/resend) |
| Resend | ~$7.7M annual revenue | 2025–26 | ESTIMATE (27% confidence, modeled) | [StartupHub](https://www.startuphub.ai/startups/resend) |
| Bun | ~40k stars (Jun 2023) to 82k+ (Dec 2025); $7M raised (Aug 2022) | — | FACT | [InfoWorld](https://www.infoworld.com/article/3700870/interview-with-jarred-sumner-buns-creator-talks-tech-funding-and-startups.html); [Wikipedia](https://en.wikipedia.org/wiki/Bun_(software)) |
| Arc | 1M+ Mac waitlist at public launch; 500k+ Windows waitlist; $50M raise at $550M | Jul 2023; Dec 2023; Mar 2024 | FACT (press) | [9to5Mac](https://9to5mac.com/2023/07/25/arc-browser-no-waitlist/); [TechCrunch](https://techcrunch.com/2024/03/21/the-browser-company-raises-50-million-at-550-million-valuation) |
| Obsidian | ~1M users; 110k+ Discord; under 12 staff; no VC | 2023 | FACT (company estimate) | [MacStories](https://www.macstories.net/news/obsidians-popularity-explained/) |
| Notion | ~100M users; ~4M paying (secondary) | 2024 | Secondary | [Synergy Startup](https://synergystartup.substack.com/p/notion-growth-strategy-behind-100m) |
| Fig | $2.2M seed; acquired by AWS | 2020; Aug 2023 | FACT | [TechCrunch](https://techcrunch.com/?p=2591683) |

### Inferences
- The fastest 2025–26 growers (Supabase, Vercel, Neon, Railway) had their classic developer-first GTM supercharged by AI coding agents and vibe-coding tools acting as a new distribution layer. Sacra attributes Supabase's and Vercel's re-acceleration to this, and Databricks attributes Neon's.
- The classic productivity tools (Linear, Raycast, Obsidian) reached scale with tiny marketing spend and teams. Linear reported over $100M ARR on about $35k of lifetime marketing (if both figures hold).

### Gaps
- No primary ARR disclosures for Raycast, Resend, Clerk, Tailscale (absolute), Obsidian, Railway, Arc or Notion's developer segment.
- The Linear 2026 ARR/NRR figure comes from a single secondary outlet. The 2025 "$100M ARR" Latka figure conflicts with it.
- Sentry ARR conflicts: Accel says about $100M; Sacra estimates about $128M at end-2023.

## Q5. Who spent on paid ads, and what kind

### Takeaway
Paid spend among these companies is mostly developer-native: podcast and YouTube creator sponsorships (Sentry, Clerk, Vercel), high-intent search and LinkedIn (PostHog), and a few brand-as-meme out-of-home campaigns (PostHog billboards and bus ads). Linear, Railway and Obsidian say or are reported to have spent almost nothing.

### Cited Findings
- **PostHog:** Google Search, Bing and LinkedIn ads for high-intent engineers, explicitly not for awareness. SF billboards (Jan 2025) and Muni bus ads (2025) with humor-led creative. Guerrilla events (lemonade stand). A "$45k/month for weird ideas" marketing budget was reported (Wynter workshop title) — [PostHog handbook](https://posthog.com/handbook/marketing/paid); [PostHog X](https://x.com/posthog/status/1879740868447395848); [SF Standard](https://sfstandard.com/2026/09/15/promiscuous-claude-stuns-new-ai-billboard/); [Wynter](https://wynter.com/posthog-weird-ideas-marketing-workshop)
- **Sentry:** developer podcast sponsorship (Syntax), later buying Syntax outright. Coupon-code offers. $100k in developer gifts — [Software Huddle](https://softwarehuddle.substack.com/p/building-evolving-sentrys-architecture); [Syntax #100](https://www.syntax.fm/100); [Sentry Syntax post](https://blog.sentry.io/syntax-sentry-mmxxiii/)
- **Clerk:** YouTube creator sponsorships (Theo/t3.gg 14–16 videos per SponsorRadar), built around real product use rather than scripted reads — [SponsorRadar](https://sponsorradar.com/brands/clerk); [Newslepear](https://newslepear.beehiiv.com/p/86-masterclass-into-youtube-influencers-last-sign-up-step-idea-and-more-learnings-on-great-docs)
- **Vercel:** previously sponsored Theo — [rosetta.to](https://rosetta.to/u/t3dotgg/breaking-up-with-vercel)
- **WorkOS** (Clerk competitor) also appears as a creator-sponsorship buyer — [SponsorRadar WorkOS](https://sponsorradar.com/brands/workos)
- **Linear:** about $35k lifetime marketing spend (secondary) — [IdeaPlan](https://www.ideaplan.io/blog/how-linear-grew-to-1-billion-with-35k-marketing-spend)
- **Railway:** reached about 2M developers "without marketing" by Jan 2026 and plans its first organized GTM — [Crypto Briefing](https://cryptobriefing.com/railway-secures-100-m-expand-ai-ready-cloud-platform/?rand=59535)
- **SF billboard context:** by 2026 SF's 101 corridor was saturated with cryptic startup billboards (NPR, SF Standard), which reduces the novelty value — [NPR Mar 2026](https://www.npr.org/2026/03/19/nx-s1-5746115-e1/billboard-ads-for-tech-startups-in-san-francisco-are-cryptic-on-purpose); [SF Standard Feb 2026](https://sfstandard.com/2026/02/06/confusing-101-billboards-san-francisco/)

### Inferences
- Paid spend works for devtools when it is (a) bottom-of-funnel search, (b) borrowed trust from a creator or podcast developers already follow, or (c) shareable brand stunts whose real reach comes from social photos (PostHog explicitly asked for photos in exchange for merch).
- For productivity tools aimed at individual developers, the evidence (Linear, Raycast, Obsidian) favors near-zero paid spend, with the product, launch cadence and community as the channel.

### Gaps
- No dollar figures for Sentry, Clerk or Vercel sponsorship budgets, and no attributed signups from any sponsorship.
- No evidence found on paid-ad use by Raycast, Supabase, Tailscale, Resend, Bun, Arc or Obsidian (absence of evidence, not confirmed zero spend).
- Pre-2020 paid strategies at GitLab, HashiCorp and Docker were not researched in depth.
