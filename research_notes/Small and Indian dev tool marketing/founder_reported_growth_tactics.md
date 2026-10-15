# Founder-reported growth tactics of small dev tools (first 100 → 1,000 → 10,000 users)

Research date: 2026-10-15. Method note for the report writer:
- **Page fetching was blocked.** Every WebFetch to indiehackers.com, dev.to, scrapingbee.com, requestly.com, starterstory.com and superframeworks.com failed with DNS errors (`getaddrinfo ENOTFOUND`). Every finding below comes from **search-result snippets and summaries**, not from reading the full primary pages. Exact figures should be spot-checked against the linked page before publication.
- **The web-search budget ran out** partway through. That cut short the searches on pricing-change stories, Indian LinkedIn and Peerlist examples, YouTube, Instagram and TikTok reels, AI directories, awesome-lists and "alternative to X" SEO. These are listed as Gaps.
- Labels used: **[FR]** = founder-reported (the founder's own post, tweet, HN comment or interview). **[3P]** = third-party write-up, case study or estimate. **[Vendor]** = a marketing blog from a company that sells launch, ads or newsletter services. Treat [Vendor] figures as rough.
- Scope: small and mid-size tools only. Larger names appear only as context. Dub.co, Postiz and SigNoz have since grown, but they are included for their early stage.

---

## 1. Which channels produced users, with reported numbers?

### Takeaway
For small dev tools, the founder-reported numbers favour **compounding, search-like channels**: Chrome Web Store or VS Code Marketplace search, SEO content, GitHub, and the founder's own X account. These beat one-day launch spikes. Show HN, Product Hunt and Reddit can produce thousands of visitors or 1,000+ GitHub stars in a day. Paid conversion from those spikes is usually tiny unless the audience is the actual buyer. Open-source tools turn HN, Reddit and PH spikes into stars far more reliably than closed SaaS turns them into revenue.

### Cited Findings

**Hacker News / Show HN (small tools)**
- ToolJet (Indian founder Navaneeth Padanna, open-source low-code): the beta launched on Product Hunt first, then on HN a few hours later, in June 2021. The repo gained **1,000+ GitHub stars in under 8 hours**. The PH post reached top 5 within minutes and finished **#1 Product of the Day** [FR, company blog/dev.to]. Later Show HN posts reported 5,000 stars and 100+ contributors at v1.0, then 16,000 stars and 300 contributors at v2.0 [FR] — [ToolJet dev.to: 0→10,000 stars](https://dev.to/tooljet/from-zero-to-10000-stars-and-160-contributors-on-github-3057); [Show HN: ToolJet 1.0](https://news.ycombinator.com/item?id=30257335); [Show HN: ToolJet 2.0](https://news.ycombinator.com/item?id=34323247)
- SigNoz (Indian founders Pranay Prateek and Ankit Nayan, YC W21): Launch HN in Feb 2021. A podcast summary says the launch got "200+ upvotes", which is unverified [3P]. The repo had about **600–700 stars by May 2021** and about **10,000 stars, 2,000+ Slack members and 100+ contributors two years after launch** [FR, podcast]. When SigNoz Cloud launched, it got **4 signups in the first week** [FR] — [Launch HN: SigNoz](https://news.ycombinator.com/item?id=26079389); [Scaling DevTools podcast](https://scalingdevtools.com/podcast/episodes/pranay-prateek); [SigNoz blog](https://signoz.io/blog/logs-to-life-building-at-signoz/)
- Aggregate HN effect: an arXiv study of **138 AI/LLM repo launches (2024–25)** found HN exposure added on average **+121 stars in 24h, +189 in 48h and +289 in a week**. This is an academic study, not founder-reported — [arXiv 2511.04453](https://arxiv.org/html/2511.04453v1)
- Show HN distribution: the **median Show HN scores about 2 points**, and **50 points puts a post in roughly the top 6%**. Another claim is about **1.4 GitHub stars per upvote** within 48h for OSS tools [Vendor] — [daily.dev HN guide](https://business.daily.dev/resources/hacker-news-marketing-developer-tools-show-hn-launch-day-sustained-coverage/). A 2026 HN thread argues that Show HN is "drowning" in volume — [HN: Is Show HN dead?](https://news.ycombinator.com/item?id=47045804)
- Front-page traffic: one blogger measured about **50 unique visitors per minute** while on the front page. That came to about 3,500–4,000 visitors in the first hours and about 8,000 over four days [FR, single post] — [marcotm.com](https://marcotm.com/articles/stats-of-being-on-the-hacker-news-front-page/)
- Reposting works: in an Ask HN thread, one founder said their first Show HN got 3 points. A repost **2.5 years later** with more features got **190 points and 80 comments**, and the app later passed 5M sessions [FR] — [Ask HN: What did your Show HN turn into?](https://news.ycombinator.com/item?id=12030863)

**Product Hunt (small dev tools)**
- Documenso (open-source e-signing, dev-led): the co-founder launched with no plan, on a weekend, and still reached **#1 Product of the Day and #9 of the Week**, with **about 2.5K unique visitors**. A launch for his other product, Specify, was planned for weeks, reached #2 of the Day, and got the **same ~2.5K visitors** [FR, quoted in guide]. Product Hunt says **60% of #1 Product of the Day winners were self-hunted** — [fmerian awesome-product-hunt launch guide](https://github.com/fmerian/awesome-product-hunt/blob/main/product-hunt-launch-guide.md)
- Corbado (passkey auth dev tool): finished **#4 Product of the Day and #1 Developer Tool of the Week**. That brought **2x website traffic and 4x usual daily signups** on launch day and the few days after [FR] — [Corbado on Medium](https://medium.com/@corbado_tech/how-to-launch-a-dev-tool-on-product-hunt-718a9a1049b7)
- Dub.co (open-source link management, then pre-seed/seed): **1,085 upvotes, #1 of the Day, Week and Month**, and **663 new signups in one day**. The founder answered all **210 launch-day comments** [3P/Vendor guide summarising the founder] — [daily.dev OSS launch guide](https://business.daily.dev/resources/promote-open-source-project-step-by-step-launch-guide/)
- Screen Studio (dev-adjacent Mac screen recorder): the founder posted on X that **4 Jan 2023 was the best sales day ever**, apart from a 50%-off promo day, and **higher than the Product Hunt launch day** [FR] — [Adam Pietrasiak on X](https://twitter.com/pie6k/status/1610782639841226752)

**Reddit**
- Litlyx (open-source analytics): the founder says a post on **r/selfhosted went viral and added about 100 GitHub stars**. That was on top of slower growth from **55 → 500 stars over two months** [FR] — [dev.to Litlyx post](https://dev.to/antoniofromlitlyx/i-built-an-open-source-analytics-dashboard-and-its-growing-fast-24l2) (via search summary)
- r/selfhosted rule change: as of October 2026, projects **under 3 months old must post in the weekly New Project Megathread**. A standalone new-project post is listed as a way to get banned [3P guide] — [saascity.io](https://saascity.io/where-to-promote-open-source-projects)
- Not a dev tool, but a useful tactic benchmark: a niche app founder got **60 of the first 100 users from Reddit**, with Discord and Indie Hackers next and **0 from HN**. Their advice is to post in a directly relevant niche subreddit with "I built…" or "I had X issue so I made…" framing, and to let people try the product without an account [FR] — [Indie Hackers](https://www.indiehackers.com/post/how-i-got-my-first-100-users-2fc9d71c34)
- Jukebox (open-source side project by skeptrune): launched on **HN plus several subreddits**. It got **7,112 visitors** and 2,685 songs played; the dev.to repost says 2,877. Only **6.7% of people who created a "box" used it with others** [FR] — [skeptrune.com](https://www.skeptrune.com/posts/jukebox-hacker-news/); [dev.to repost](https://dev.to/skeptrune/from-side-project-idea-to-hacker-news-front-page-a-7112-user-retrospective-2p3i)
- Reddit ads for dev tools: Markepear highlights Latitude's all-text Reddit ad, which sends readers to **GitHub instead of a signup page**. Zesty's Reddit ad got **33 upvotes and 30 comments** [3P] — [Markepear Reddit examples](https://www.markepear.dev/examples/reddit); [Markepear copy examples](https://www.markepear.dev/examples/copy)

**Multi-channel "launch weeks" (open source)**
- Postiz (Nevo David, open-source social scheduler, bootstrapped): a case study says it went from **3K → 14K GitHub stars in three months** through concentrated launch weeks across **HN, Reddit, Dev.to, Medium and Product Hunt**. Revenue reached **$17K MRR from 472 paying subscribers** [3P]. Nevo David had earlier taken Novu to about 30K stars. Postiz later repositioned as **agent-callable infrastructure (CLI, MCP server, API)**. TrustMRR now shows about **$270K MRR and 7,922 active subscriptions**. Third-party sources conflict, citing $170K and $221K at different dates — [superframeworks case study](https://superframeworks.com/case-study/postiz); [TrustMRR: Postiz](https://trustmrr.com/startup/postiz); [Dealroom news: $17K/month, 25K stars](https://app.dealroom.co/news/feed/open-source-saas-founder-grows-postiz-to-17k-month-with-25k-github-stars)

**X / Twitter (founder account)**
- Screen Studio: **about $30K revenue in its first month** after release (Dec 2022), said by the founder on HN [FR]. A 2026 teardown estimates about 320K monthly visits and says the **founder's personal X account drives most acquisition** [3P estimate] — [HN comment](https://news.ycombinator.com/item?id=33945843); [systemaic teardown](https://www.systemaic.com/teardowns/screen-studio)
- Tony Dinh (DevUtils, Black Magic, later TypingMind): started building in public on Twitter in **April 2021**. By **Aug 2021, DevUtils was at about $200 MRR and Black Magic at about $300 MRR** [3P profile]. A profile quotes him attributing **"99% of sales" to his Twitter audience**, but that refers to his products overall [3P quoting FR] — [onemilliongoal profile](https://www.onemilliongoal.com/p/tony-dinh-the-vietnamese-developer); [supabird](https://supabird.io/articles/tony-dinh-from-a-105k-developer-to-a-1-million-indie-hacking-marvel)
- Supermemory (Indian founder Dhravya Shah): Starter Story says one founder tweet went viral and added **about 1,000 GitHub stars when the repo had about 4,000**. The headline claims **6.5K users in 6 weeks**. This is unverified: no tweet link or date [3P]. The repo now shows about **31.2K stars**, and the company raised about **$3M seed** — [Starter Story breakdown](https://www.starterstory.com/supermemory-ai-breakdown); [GitHub profile](https://github.com/dhravya); [mystartupnews.in](https://mystartupnews.in/news/19-year-old-indian-founder-dhravya-shah-raises-dollar3-million-for-ai-startup-supermemory)

**Marketplaces and store search (Chrome Web Store, VS Code)**
- Requestly (Indian founder Sachin Jain, Chrome extension for redirecting and modifying HTTP requests): began as a personal tool. Growth was **"organic"**: the founder searched for people asking things like "redirect URLs" or "modify headers" and answered them, and shared use cases on Twitter, Reddit and blog posts. Reported scale: **80,000 users** (IH post title), then **100K+ developers**, then **200K+ downloads and 8,000+ companies** [FR]. It joined YC W22 and Peak XV Surge, so it was not bootstrapped throughout. BrowserStack acquired it in **May 2025** — [IH: Solving a problem for myself and 80,000 other users](https://www.indiehackers.com/post/solving-a-problem-for-myself-and-80-000-other-users-sN7LLQAgRQNpILXfl1bN); [Neon Fund](https://neon.fund/blog/how-requestly-became-a-developer-favourite/); [Requestly blog](https://requestly.com/blog/the-evolution-of-requestly/)
- Superpower ChatGPT (Chrome extension): the developer says most growth came from **Chrome Web Store search, reviews and word of mouth**, reaching **5-figure MRR** [FR] — [Indie Hackers](https://www.indiehackers.com/post/tech/building-a-free-chrome-extension-in-3-days-and-turning-it-into-a-5-figure-mrr-ecosystem-3rIbjigZxiFsrgqJjJYp)
- VS Code Marketplace: a developer with 12 published extensions says **search ranking weighs installs heavily**, so the first organic installs matter most [FR]. Another dev.to author reports **about $6,800/month from three niche extensions** [FR, unverified]. The Marketplace has **no built-in payments**, so developers use Stripe, Lemon Squeezy or Paddle plus license keys [3P] — [dev.to: 12 VS Code extensions](https://dev.to/miccho27/i-published-12-vs-code-extensions-heres-what-each-one-does-and-what-i-learned-333c); [dev.to: $6,800/month](https://dev.to/hopkins_jesse_cdb68cfa22c/how-i-make-6800month-selling-niche-vs-code-extensions-eji); [Dodo Payments](https://dodopayments.com/blogs/sell-vscode-extensions)
- Pika (Indian founder Rishi Mohan, screenshot beautifier, open source) also ships a **VS Code extension**, used as a distribution surface — [VS Code Marketplace: Pika](https://marketplace.visualstudio.com/items?itemName=RishiMohan.pika-vscode)
- An IH post is titled "Trust me! Market your SaaS as a VS Code extension. Best decision I ever made." Its body could not be fetched, so no numbers are available — [Indie Hackers](https://www.indiehackers.com/post/trust-me-market-your-saas-as-a-vs-code-extension-best-decision-i-ever-made-ca6fef2375)

**SEO / content**
- ScrapingBee (bootstrapped web-scraping API, founders Pierre de Wulf and Kevin Sahin): the founders' previous product, PricingBot, got its first paying customer in Jan 2019 but stalled because people wouldn't pay. ScrapingBee grew out of **Kevin's existing web-scraping blog content**. Kevin published posts on **HN and Reddit** to build an audience from day one, and the team later built an **SEO content engine** [FR + podcast summaries]. Reported milestones: **$500K ARR in under 2 years** (Indie Hackers, Aug 2021) and **$1M ARR in Nov 2021** [3P]. Accounts disagree on time to $1M ARR: the founders' post says "almost five years and multiple failed projects" counting earlier attempts, while podcasts say 2–3 years. Oxylabs later acquired it, and Kevin cites **2,500+ customers** — [ScrapingBee: journey to $1M ARR](https://www.scrapingbee.com/journey-to-one-million-arr/); [IH on X](https://x.com/IndieHackers/status/1425481417467863047); [ideaindex case study](https://www.ideaindex.so/case-studies/scrapingbee)

**Directories / launch boards**
- Peerlist Launchpad: weekly launches open on Monday, and the **top 3 each week get a badge plus newsletter and social features**. Ranking is reportedly randomised for the first 2 days. A **100% complete profile** is required. Peerlist claimed **230K builders** on X in July 2026 [3P guides / company claim] — [launchrepo](https://launchrepo.dev/directories/peerlist/); [Peerlist on X](https://x.com/Peerlist?lang=en); [dev.to India-based founder](https://dev.to/andriana_kodlo_b2d08a9bce/i-listed-my-saas-on-5-platforms-in-one-day-still-zero-users-what-am-i-missing-2fc8)
- BetaList: one founder report gives about **200 directly attributable visits plus 40–50 from other promotion, and 16 signups**. The source surfaced oddly, via a CB Insights company page for "Phiona", so reliability is low — [CB Insights](https://www.cbinsights.com/company/phiona)
- Microlaunch and Uneed: only testimonials ("a lot of traffic") and positioning claims (a calmer feed with longer visibility). No founder-reported numbers were found [3P] — [Microlaunch on PH](https://www.producthunt.com/products/microlaunch); [LaunchList ranking](https://getlaunchlist.com/blog/where-to-launch-your-startup)

**Newsletters (small paid placements)**
- A vendor case study: **$2,000 on a Hacker Newsletter sponsorship gave a 5.5% CTR, 55 clicks and 11 trials (about $180 per trial)** [Vendor]. Niche dev newsletters with **5K–100K subscribers typically charge $100–$2,000**. TLDR works out to about **$10–15 per 1,000 subscribers** [Vendor] — [daily.dev newsletter sponsorships](https://business.daily.dev/resources/newsletter-sponsorships-developer-products/); [sponsorships.ai: TLDR](https://sponsorships.ai/blog/tldr-advertising-cost)
- ScreenshotOne's founder (2026, on X) says he has **started paid ads**: "early to tell… but it is costly" [FR] — [Dmytro Krasun on X](https://x.com/DmytroKrasun/status/2104570564006277204)

**ChatGPT / Perplexity citations**
- No founder-reported share of dev-tool signups coming from ChatGPT or Perplexity was found. At the aggregate level, AI platforms drove **about 1% of web traffic** across 10 industries, and ChatGPT accounted for **87.4% of AI referrals** (Conductor data via Digiday, 2025) — [Digiday](https://digiday.com/media/in-graphic-detail-the-state-of-ai-referral-traffic-in-2025/). ChatGPT's share of AI referrals fell to **about 63% by spring 2026** in Goodie's study of 41 sites — [Goodie](https://higoodie.com/blog/ai-search-traffic-report-2026/)
- A dev.to cautionary case: one founder's funnel showed **206 "sign-in starts" from AI visitors and 0 completed signups** in 7 days. The figure is secondhand — [dev.to robin_geo](https://dev.to/robin_geo/206-sign-in-starts-0-signups-how-to-check-whether-ai-visitors-actually-convert-4m6i)
- Postiz's repositioning around a CLI, MCP server and API to be "the tool your agent reaches for" coincides with its reported MRR jump. That is correlation, and the figures conflict — [dev.to max_quimby](https://dev.to/max_quimby/the-real-moat-is-being-the-tool-your-agent-reaches-for-1n26)

### Inferences
- The launch stack that worked for open-source dev tools (ToolJet, Postiz, Dub) **clusters several launches** (PH, then HN the same day, or a launch week across HN, Reddit, dev.to and PH). Success is measured in **stars, contributors and signups**, not revenue.
- Store and marketplace search (Chrome Web Store, VS Code) and SEO compound. Founders who grew there (Requestly, Superpower ChatGPT, ScrapingBee) describe **answering existing search intent** ("redirect URLs", "modify headers", scraping how-tos) rather than launching.
- A rough **visitor-to-signup funnel** for a small tool's launch day, from the reports above: about 2.5K visitors from a #1–#2 PH finish, 3.5K–8K from an HN front page, and a few hundred from a niche directory. Signups ran from 16 (BetaList) to 663 (Dub), depending on whether the product is free or open source and whether the audience is the buyer.
- For a closed, paid small tool, an HN or PH spike is better treated as **feedback and backlink capture** than as revenue (see Q5).

### Gaps
- No founder-reported numbers were found for: **LinkedIn posts** for dev tools, **YouTube small-creator reviews**, **Instagram/TikTok reels**, **JetBrains, Raycast or Open VSX** installs, **AI directories** (There's An AI For That, Futurepedia), **AlternativeTo**, **awesome-list inclusion**, **cold DMs**, or **"alternative to X" SEO pages**. The search budget ran out before these could be covered.
- The full text of IH posts, Starter Story interviews and dev.to retrospectives could not be read (DNS-blocked), so per-post upvote and signup breakdowns are missing.
- No dev-tool founder was found reporting a percentage of signups from ChatGPT or Perplexity.

---

## 2. Which founder-led content patterns got likes and reach?

### Takeaway
The best-documented pattern is **long-running build-in-public revenue and milestone posting on X or Indie Hackers** by solo founders: ScreenshotOne, Pika, snappify and Tony Dinh. **Short demo clips** are the other strong pattern, with Screen Studio as the clearest example. **Open-sourcing the core or a side tool** works as a reach engine (Hoppscotch, Postiz, Supermemory, Pika). Hard engagement numbers (likes or impressions mapped to signups) are almost never published.

### Cited Findings
- **Build in public, revenue updates (ScreenshotOne, Dmytro Krasun, bootstrapped screenshot API):** **3 years to $10K MRR**, then 8 more months to **$20K** [3P profile]. The IH interview reports **800+ paying customers and $25K+ MRR**. A 2026 X post reports **about $36K MRR**, after a July post described a plateau around **$33K MRR** [FR]. Profiles credit daily X threads on roadmap, revenue and failures for social proof and backlinks, plus being helpful in dev communities for referrals. His stated lesson was to **downgrade ambition** to small, achievable steps — [Startup Founder Stories](https://startupfounderstories.com/stories/dmytro-krasun-screenshotone-20k-mrr); [IH interview](https://www.indiehackers.com/post/tech/hitting-25k-mrr-by-making-his-goals-less-ambitious-jQRZDnzwm8DFAaS4Xrq0); [Solo Unicorn](https://www.solounicorn.club/blog/day-32-screenshotone); [X post](https://x.com/DmytroKrasun/status/2104570564006277204)
- **Build in public (snappify, code-presentation tool, Dominik Sumer):** an IH milestone log shows **$0 → $500 MRR in about 16 months**, **1,000 accounts and about 40 paying customers ($250 MRR) by March 2022**, and **$1,000 MRR by Nov 2022**. Growth **slowed in May 2022** when the founder took a freelance gig and had less time for marketing [FR] — [snappify on IH](https://www.indiehackers.com/product/snappify/1000-mrr--NJ4NwCuCqLCcXGHND_W)
- **Build in public plus open source (Pika, Indian founder Rishi Mohan):** a Show HN reported **$90 MRR** [FR]. Startups.fyi showed **$2K MRR (Mar 2023)** [3P]. A Starter Story interview says "close to **$3,500 MRR**", with a headline of $3.8K/month. He credits sharing progress, features and milestones on Twitter, and also posted on LinkedIn with #buildinginpublic [FR] — [Show HN: Pika](https://news.ycombinator.com/item?id=30611657); [Starter Story](https://www.starterstory.com/stories/pika); [startups.fyi](https://www.startups.fyi/product/pika-style); [LinkedIn post](https://in.linkedin.com/posts/qaplen_sidehustle-buildinginpublic-webapp-activity-6921539228338176000-1amU?trk=public_profile_like_view); [GitHub repo](https://github.com/rishimohan/pika)
- **Revenue screenshots and milestone tweets (Screen Studio):** "best sales day ever… even on product hunt release day, it did not have such revenue" (Jan 2023) [FR] — [X](https://twitter.com/pie6k/status/1610782639841226752)
- **Open-sourcing as the growth engine (Hoppscotch, Indian founder Liyas Thomas):** built in **6 hours in 2019** because his laptop couldn't run Postman. It reached **100K users within a year** (Oct 2020), **25K stars by Dec 2020**, then 35K and 52K, and about **79K stars and 500K+ developers** by a 2026 profile. He said, "we haven't spent a single penny on advertising or marketing." The company later raised a **$3M seed (OSS Capital)** [FR + 3P] — [founderspec](https://founderspec.com/breakdowns/hoppscotch); [LinkedIn 52K stars](https://www.linkedin.com/posts/liyasthomas_hoppscotch-just-passed-52000-stars-on-github-activity-7077690930786414592-9vHN); [Medium 35K stars](https://liyasthomas.medium.com/hoppscotch-is-celebrating-35-000-github-stars-a603e2ba4fa4); [GitHub ReadME story](https://github.com/readme/stories/liyas-thomas)
- **Milestone celebration posts as content:** Hoppscotch's founder posted star-milestone articles on dev.to, Medium and LinkedIn (30K, 35K and 52K stars, plus "trending on GitHub") — [dev.to 30K](https://dev.to/liyasthomas/hoppscotch-is-celebrating-30-000-github-stars-1gg9); [LinkedIn trending](https://www.linkedin.com/posts/liyasthomas_hoppscotch-is-trending-on-github-activity-6867099447546007553-v0rA)
- **Engineering as marketing / free tools:** the only conversion figure found is an unsourced heuristic of **2–5% tool→signup when the free tool is adjacent to the paid product**, near zero when unrelated, with **30–90 days to see signal** [Vendor] — [boilerplatehub](https://boilerplatehub.com/blog/engineering-as-marketing-free-tools); [MicroConf](https://microconf.com/latest/engineering-as-marketing)
- **Comment-answering as a reach multiplier:** Dub's founder answered all 210 PH comments on launch day [3P] — [daily.dev](https://business.daily.dev/resources/promote-open-source-project-step-by-step-launch-guide/)

### Inferences
- Build in public is **slow**: ScreenshotOne took 3 years to $10K MRR, and snappify 16 months to $500 MRR. Its value is compounding trust and backlinks, not quick likes. Pausing it shows up in growth (snappify, May 2022).
- Demo-friendly, visual dev tools (Screen Studio, Pika, snappify) get an outsized lift from X because the output itself is shareable. A small marketer should favour **15–30s output-first demo clips** over text threads.
- Open-sourcing the product, or a useful side tool, is the most repeatable no-budget reach mechanism among Indian dev tools in this sample: Hoppscotch, ToolJet, SigNoz, Supermemory and Pika.

### Gaps
- No like, impression or signup data was found for specific X threads, "I quit my job" posts, memes, hot takes or comparison tests by small dev-tool founders. The few such numbers seen came from aggregators.
- No named example of a JSON-formatter or regex-tester-style free tool with published signup numbers was found.

---

## 3. Indian context: Peerlist, LinkedIn, r/developersIndia, Indian startup Twitter

### Takeaway
The best-documented Indian dev tools grew mainly through **global developer channels**: GitHub and open source, HN and PH launches, and Chrome Web Store search. India-specific channels played a smaller part. Hoppscotch, ToolJet, SigNoz, Requestly, Supermemory and Pika all fit this. India-specific levers in the record are **LinkedIn milestone posts**, **Indian FOSS events (IndiaFOSS, FOSS Hack)** and **India-focused accelerators (Peak XV Surge)**. No numbers-backed Peerlist or r/developersIndia case study was found.

### Cited Findings
- Hoppscotch (Kerala/Kochi): fully organic, open-source growth to 100K users in year 1, and about 79K stars and 500K+ developers by 2026. OSS Capital called it "the fastest-growing open-source ecosystem in India" (an investor characterisation) — [founderspec](https://founderspec.com/breakdowns/hoppscotch)
- ToolJet: PH plus HN on the same day in June 2021, with 1,000+ stars in under 8 hours. It "consistently participated in open source conferences like **IndiaFOSS** and **FOSS Hack** hackathons" [FR] — [ToolJet dev.to 20K stars](https://dev.to/tooljet/how-tooljet-gained-20000-github-stars-and-400-contributors-4ee0); [ToolJet GitHub stars guide](https://blog.tooljet.com/github-stars-guide/)
- SigNoz: Launch HN, then about 10K stars in 2 years, then a **$6.5M seed led by SignalFire** — [SignalFire](https://www.signalfire.com/blog/signoz-pioneers-open-source-observability-with-65m-led-by-signalfire)
- Requestly: Chrome Web Store plus answering search-intent questions, then 100K–200K+ users, YC W22, Peak XV Surge, and a BrowserStack acquisition in May 2025 — [IH](https://www.indiehackers.com/post/solving-a-problem-for-myself-and-80-000-other-users-sN7LLQAgRQNpILXfl1bN); [Requestly: Surge](https://requestly.com/blog/a-taste-of-sequoias-surge-program/)
- Supermemory (Mumbai): hackathon project (2024), then a viral X post (+~1K stars, unverified), then about 31K stars and a $3M seed — [Starter Story](https://www.starterstory.com/supermemory-ai-breakdown); [solofounders](https://solofounders.com/blog/he-sold-a-company-at-16-raised-3m-at-19-then-gave-his-ai-engine-away-for-free/)
- Pika (Rishi Mohan): build in public on Twitter and LinkedIn, open source, and a VS Code extension; about $3.5K MRR per Starter Story — [Starter Story](https://www.starterstory.com/stories/pika)
- r/developersIndia: the community's GitHub org describes it as **"India's largest developer community network with 900k+ developers"** — [developersIndia GitHub](https://github.com/developersIndia). No dev-tool launch post with reported numbers was surfaced.
- Peerlist: 230K builders (company claim, July 2026), with weekly Monday launches and a top-3 newsletter feature. A founder based in India listed a SaaS on 5 platforms including Peerlist and got **zero users**. A commenter noted that listing gives "distribution, not necessarily discovery" [FR] — [dev.to](https://dev.to/andriana_kodlo_b2d08a9bce/i-listed-my-saas-on-5-platforms-in-one-day-still-zero-users-what-am-i-missing-2fc8); [Peerlist on X](https://x.com/Peerlist?lang=en)

### Inferences
- For an Indian small dev tool, the copyable path is **global-first**: GitHub and open source, the HN/PH launch stack and store SEO. India-specific channels serve **credibility and hiring**: LinkedIn milestone posts, IndiaFOSS and FOSS Hack, Peerlist. Indian channels have not shown up as primary user-acquisition engines in the documented cases.
- LinkedIn appears in Indian founders' playbooks (Liyas Thomas and Rishi Mohan both post milestones there), but no signup attribution was published.

### Gaps
- No numbers-backed r/developersIndia launch post, Peerlist Project of the Week result, Indian-Twitter viral launch with signups, or LinkedIn-driven dev-tool signup data was found. The search budget ran out before targeted queries on this. A sibling note (`indian_creator_community_ecosystem.md` in the same folder) may cover parts of it.

---

## 4. Conversion: free-to-paid rates and pricing changes

### Takeaway
Founder-reported free-to-paid conversion for small dev tools is usually **low single digits or below**. snappify had about 40 paying customers from 1,000 accounts (about 4%). A Chrome extension reported 2.1% at its paywall. TimeYourWeb had 10 payers from 20K users (0.05%). Survey benchmarks put good freemium conversion at 3–5% and the overall median at about 8%. No founder-reported "pricing change → revenue up X%" story for a small dev tool was captured before the search budget ran out.

### Cited Findings
- snappify: **about 40 paying out of 1,000 registered accounts (about 4%) at $250 MRR, March 2022** [FR] — [IH](https://www.indiehackers.com/product/snappify/1000-mrr--NJ4NwCuCqLCcXGHND_W)
- TimeYourWeb (Chrome extension): **about 20,000 users, 10 paying customers, $60 MRR after 10 years** [FR] — [IH](https://www.indiehackers.com/post/i-built-a-chrome-extension-in-2-weeks-10-years-later-20-000-users-10-paying-customers-60-mrr-YaK5THoaKqXgTlgBjHgO)
- CookieJar (Chrome extension): **2.1% free→paid conversion on the paywall**, about **$22/month** revenue [FR] — [IH MRR update](https://www.indiehackers.com/post/mrr-update-22-month-from-chrome-extensions-0715acdd8b)
- A podcast-described solo Chrome extension: **$10K MRR, 8% free-tier conversion, priced per 1,000 actions, distribution entirely via Chrome Web Store search ranking**. This comes from an episode description and is unverified — [iHeart podcast](https://www.iheart.com/podcast/53-the-indie-hacker-podcast-wi-334456085/episode/how-a-solo-dev-hit-10k-338614911/)
- ScreenshotOne: **800+ paying customers at $25K+ MRR**, an implied ARPU of about $30/month [FR] — [IH](https://www.indiehackers.com/post/tech/hitting-25k-mrr-by-making-his-goals-less-ambitious-jQRZDnzwm8DFAaS4Xrq0)
- Postiz: **$17K MRR from 472 subscribers** (about $36 ARPU) at an earlier stage [3P] — [superframeworks](https://superframeworks.com/case-study/postiz)
- Benchmarks: ChartMogul's **2026 survey of 200 products** gives a **median free-to-paid conversion of 8%** within six months. For freemium self-serve, **3–5% is good and 8–12% is great** — [ChartMogul](https://chartmogul.com/reports/saas-conversion-report/). An older OpenView analysis found that companies selling to developers convert at about **5%** — [boldstart](https://boldstart.vc/devtoolkit/an-alternative-to-nps-for-dev-tools/). Indie blogs cite 2–5% for freemium — [dev.to whoffagents](https://dev.to/whoffagents/how-to-price-your-developer-tool-a-framework-that-maximizes-revenue-3d9h)
- Monetisation constraint: the VS Code Marketplace has no "Buy" button or paid-license API, so external payments plus license keys are required — [Dodo Payments](https://dodopayments.com/blogs/sell-vscode-extensions)
- SigNoz targeted **free use for individual developers and small teams** (MIT license). The paid hosted Cloud started at **4 signups in week 1** [FR] — [Launch HN](https://news.ycombinator.com/item?id=26079389); [SigNoz blog](https://signoz.io/blog/logs-to-life-building-at-signoz/)

### Inferences
- Usage-heavy, infrastructure-like dev tools (APIs such as ScreenshotOne and ScrapingBee) appear to monetise far better per user than browser-extension utilities. Extensions often show high installs and very low revenue.
- A small marketer should plan for **about 1–5% of active free users converting**, and model revenue on ARPU of about $15–40/month for indie dev tools, based on the ScreenshotOne, Postiz and Pika figures above.

### Gaps
- No founder-reported pricing-change experiments for small dev tools were found (raising prices, killing lifetime deals, moving to usage pricing). The search budget was exhausted before this query ran. Open Startup dashboards (Baremetrics, ProfitWell, TrustMRR) were not systematically mined for conversion data.

---

## 5. Failure stories: upvotes and likes without users or revenue

### Takeaway
The recurring failure mode is that **launch-day audiences are other makers, not buyers**. A #1 Product Hunt finish or an HN front page can mean thousands of visitors, dozens of signups and zero or one paying customer. Usage-based failure is also common: signups that never engage.

### Cited Findings
- A **#1 Product of the Day with 612 upvotes (Sept 2024) produced one paying customer**. The author says launch-day attention comes mostly from other founders and enthusiasts [3P newsletter] — [Rashi Umapathi, Substack](https://rashiumapathi.substack.com/p/product-hunt-wont-save-your-startup)
- A founder's PH launch brought **1,000+ visitors and "tens" of signups, zero payments**. Another indie hacker **emailed 3,830 users and got 2 paying customers at $5/month** [3P compiled] — [Syften PH guide](https://syften.com/blog/product-hunt-launch/)
- Another IH founder's PH launch got **5 upvotes, 0 new signups and $0 MRR**, and they switched to direct outreach to founders with 10–50 users [FR] — [Indie Hackers](https://www.indiehackers.com/post/product-hunt-is-done-i-have-1-sign-up-and-0-mrr-heres-how-i-m-thinking-about-finding-my-first-paying-customer-a057ad34dc)
- An HN front-page dev project: **about 1,000 visitors in 24h, 425 tried the demo, 382 completed it, 3 signups, 0 purchases** [FR] — [dev.to ddltodata](https://dev.to/ddltodata/how-my-first-hacker-news-launch-went-and-what-i-did-about-it-40k9)
- Groove (helpdesk, not a dev tool; included for the benchmark): **105,000 HN visits a month before a launch gave 97 signups and 14 paying customers** [3P] — [Medium krunchdata HN guide](https://medium.com/@krunchdataio/a-guide-to-launch-your-dev-tool-on-hacker-news-track-where-your-conversions-came-from-3b27dd855a77)
- Jukebox: 7,112 visitors from HN and Reddit, but only **6.7% of box creators used it collaboratively**, and the founder abandoned it [FR] — [skeptrune.com](https://www.skeptrune.com/posts/jukebox-hacker-news/)
- An India-based founder listed a product on **5 launch platforms in one day and got zero users** [FR] — [dev.to](https://dev.to/andriana_kodlo_b2d08a9bce/i-listed-my-saas-on-5-platforms-in-one-day-still-zero-users-what-am-i-missing-2fc8)
- ScrapingBee's founders' prior product, **PricingBot, got paying customers but stalled because people wouldn't pay**, and they pivoted to the area where Kevin already had content and an audience [FR] — [ScrapingBee](https://www.scrapingbee.com/journey-to-one-million-arr/)
- TimeYourWeb: 20K users and $60 MRR after 10 years. Installs without a monetisation path [FR] — [IH](https://www.indiehackers.com/post/i-built-a-chrome-extension-in-2-weeks-10-years-later-20-000-users-10-paying-customers-60-mrr-YaK5THoaKqXgTlgBjHgO)
- Documenso: unplanned vs. planned PH launches gave the **same ~2.5K visitors**, which suggests launch prep has limited upside on traffic [FR] — [fmerian guide](https://github.com/fmerian/awesome-product-hunt/blob/main/product-hunt-launch-guide.md)
- Paid ads for a small dev tool: ScreenshotOne's founder calls them "costly" with results unclear (2026) [FR] — [X](https://x.com/DmytroKrasun/status/2104570564006277204)
- One case study mentions a **"$12K SEO flop"** in Postiz's history. The details could not be read (page blocked) — [superframeworks](https://superframeworks.com/case-study/postiz) (unverified)

### Inferences
- Why the spikes failed, as the sources describe it: (1) an audience mismatch, with makers and voters rather than buyers; (2) a "try it" demo with no reason to return or pay; (3) signup friction or required accounts; (4) a single launch with no follow-up channel.
- Patterns a small-company marketer can copy, synthesised from Q1–Q5:
  1. **Pick one compounding channel first**: store or marketplace SEO, a content or SEO engine, or GitHub. Treat PH and HN as one-off amplifiers of it.
  2. **Stack the launch day**: PH in the morning and Show HN a few hours later (ToolJet), or a week-long multi-platform launch (Postiz). Answer every comment (Dub).
  3. **Repost to HN later** with meaningful new features. A 3-point post became a 190-point post 2.5 years later.
  4. **Answer existing intent** in forums, Stack Overflow-style queries and Reddit threads before promoting (Requestly). Post in the niche subreddit with "I built…" framing and no forced signup.
  5. **Build in public for years, not weeks**: weekly revenue and milestone posts on X, IH and LinkedIn (ScreenshotOne, snappify, Pika). Expect a 1–3 year curve to $10K MRR.
  6. **Make the output shareable** (screenshots, videos, code images) so every user post is an ad (Screen Studio, Pika, snappify).
  7. **Open-source the core or a side tool** to win stars and contributors. Monetise through a hosted cloud, and expect a slow start: SigNoz Cloud had 4 signups in week 1.
  8. **Instrument the funnel**: visitors → activation → paid. Spikes routinely show 0.1–1% visitor-to-paid conversion.
  9. **Become agent-callable** (MCP server, CLI, API) for AI-era distribution. Postiz and ScreenshotOne both did this in 2026; the evidence is early and correlational.

### Gaps
- No numbers-backed failure story was found specifically for X or LinkedIn viral posts (many likes, no signups), or for AI-directory listings.
- Most failure data is about general SaaS, not dev tools. Dev-tool-specific failure postmortems with numbers remain scarce in the accessible results.
