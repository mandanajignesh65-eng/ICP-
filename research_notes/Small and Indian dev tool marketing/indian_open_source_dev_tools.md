# How small-to-mid-size Indian open-source and SaaS developer tools built reach, community and revenue

Research method note (Oct 15, 2026): Every direct page fetch failed with DNS errors (plane.so, opensource.com, company.hoppscotch.io, marmelab.com all returned ENOTFOUND), and the GitHub API was blocked for this session. Everything below comes from web-search result snippets and summaries of the cited pages, so it was not read from the pages in full. Labels used: **[verified]** means a primary or first-party source (company blog, founder post, HN comment by the founder, press release); **[reported]** means secondary press; **[estimate]** means a third-party aggregator such as Latka, Prospeo, or directory sites. Star counts from aggregators are often a few months out of date.

## Which tools qualify, and tool-by-tool snapshots

### Takeaway
The clearest Indian-founded, non-AI-first, productivity-type developer tools with good public growth data are Hoppscotch, Bruno, Plane, ToolJet, SigNoz, Requestly, Chatwoot, Keploy, Devtron, Middleware, Hyperswitch and listmonk. Appsmith is the upper bound. Infisical, Mintlify and FlowiseAI could not be confirmed as Indian-founded and should be left out or flagged.

### Cited Findings

**Hoppscotch** (API client; Kerala, founder Liyas Thomas)
- Started as "a personal tool for myself in August 2019." Thomas says he built the first version in about six hours and it "was an overnight success" [verified, founder interview]. — [FOSS United interview](https://fossunited.org/blog/interview/liyas-thomas); [GitHub ReadME story](https://github.com/readme/stories/liyas-thomas)
- Originally called "Postwoman." Its 2020 profile described it as a "web alternative to Postman" used by 65k+ developers [reported, 2020]. — [HackerNoon Noonie profile](https://sia.hackernoon.com/liyas-thomas-2020-noonie-nominee-is-the-creator-of-postwomanio-lz4g3u1o)
- It was renamed because a Postman-like name risked trademark trouble, and the team did not want to "hurt another project's goodwill." Ben Halpern of DEV.to suggested the name "Hoppscotch" [verified]. Sources disagree on when the rename happened (August vs. November 2020). — [DEV.to: Postwoman is changing name](https://dev.to/liyasthomas/postwoman-is-changing-name-igp); [GitHub discussion #5481](https://github.com/hoppscotch/hoppscotch/discussions/5481)
- Star milestones [verified]: 25,000 stars in Nov 2020, then 30k and 35k posts on DEV. — [DEV 25k](https://dev.to/liyasthomas/hoppscotch-celebrating-25-000-github-stars-5aao); [DEV 30k](https://dev.to/liyasthomas/hoppscotch-is-celebrating-30-000-github-stars-1gg9); [DEV 35k](https://dev.to/liyasthomas/hoppscotch-is-celebrating-35000-github-stars-42hj?comments_sort=latest)
- About 2 years after launch it had "300,000+ users and 30,000+ GitHub Stars," and Thomas said "all of the growth and reach is organic" [verified, GitHub ReadME podcast]. — [GitHub ReadME podcast](https://github.com/readme/podcast/liyas-thomas)
- Seed round: $3M led by OSS Capital (Joseph Jacks joined the board), with Automattic participating. Dated 1 Dec 2021, and the company cited a "500,000+ developers" community at the time [verified]. — [IndieHackers announcement](https://www.indiehackers.com/post/hoppscotch-raises-3m-in-seed-funding-to-build-open-source-api-development-ecosystem-3ab1ef9278); [startupintros](https://startupintros.com/news/2021-12-01-hoppscotch-seed)
- Trendshift says the repo first reached #1 on GitHub Trending on 24 Jul 2024 [reported]. — [Trendshift](https://trendshift.io/repositories/36)
- Current stars: about 65.8k to 80k depending on the snapshot; OSS Insight shows 79,546 (undated) [estimate]. Directory listings claim "~$2M ARR as of 2025" [estimate, unconfirmed]. PitchBook lists about 8 employees [estimate]. — [OSS Insight compare](https://ossinsight.io/compare/hoppscotch/hoppscotch/usebruno/bruno); [everydev.ai](https://www.everydev.ai/developers/hoppscotch); [PitchBook](https://pitchbook.com/profiles/company/489006-55)
- Thomas gave a GitHub Satellite talk titled "Journey of a project made in India: Hoppscotch" [verified]. — [GitHub Satellite](https://githubsatellite.com/sessions/journey-of-a-project-made-in-india-hoppscotch/)

**Bruno** (Git-native, offline API client; founder Anoop M D)
- Started in Dec 2021 to keep API collections in version control next to the code. It is named after Anoop's dog [reported]. Bruno gave a talk at IndiaFOSS 2024 (FOSS United CFP) [verified]. — [everydev.ai](https://www.everydev.ai/developers/usebruno); [FOSS United IndiaFOSS24 CFP](https://fossunited.org/c/indiafoss/indiafoss24/cfp/oas92icb9u)
- Marmelab reported it went from about 2k to about 18k stars in 5 months [reported, May 2024]. — [Marmelab](https://marmelab.com/blog/2024/05/03/we-dont-talk-about-bruno.html)
- Reached the top of HN on 9–10 Mar 2024 with "Bruno: Fast and Git-friendly open-source API client (Postman alternative)." In the thread Anoop wrote that they had "around 10 inbound reach outs from VCs… denied funding from all of them," were "fully bootstrapped," and sold the Golden Edition as a one-time $19 payment [verified, founder HN comment]. — [HN thread](https://news.ycombinator.com/item?id=39653718); [Anoop comment](https://news.ycombinator.com/item?id=39656680)
- 2024 recap: 1 million downloads and 700,000 new users in 2024 [verified, first-party]. 2025 recap: MAU went from about 250k (Jan 2025) to 600k+ (Dec 2025), stars from 26k to 40k, 78 releases, and the team grew from 6 to 23 [verified, first-party]. — [Bruno 2024 recap](https://blog.usebruno.com/building-momentum-reflecting-on-2024-and-aiming-higher); [Bruno 2025 recap](https://blog.usebruno.com/bruno-2025-from-idea-to-daily-driver)
- "The Funding Announcement We Never Made": Bruno says it quietly raised $3M about a year before the post and made previously paid features (gRPC, WebSocket) free [verified, first-party]. A third-party summary names Silverton Partners as the investor [reported]. — [Bruno blog](https://blog.usebruno.com/the-funding-announcement-we-never-made); [daily.dev](https://daily.dev/posts/the-funding-announcement-we-never-made-joknszzvh)
- In June 2025 a maintainer said they had stopped selling new Golden Edition licenses because it "wasn't a sustainable model." Bruno now sells Pro/Ultimate plans [verified]. — [GitHub discussion #269](https://github.com/usebruno/bruno/discussions/269)
- Stars: about 44k in May 2026 and about 47.4k on 10 Oct 2026 (Insomnia was about 40.0k on the same date) [estimate, comparison site]. — [Voiden comparison](https://voiden.md/blog/postman-vs-insomnia-vs-bruno-vs-hoppscotch-vs-voiden-2026-comparison); [iconpolls](https://iconpolls.com/blogs/bruno-api-client-review-2026-download-github-app-testing-mac-web-user-experience-and-faqs)

**Plane** (project management; brothers Vamsi Kurama (CEO) and Vihar Kurama (COO); Hyderabad / Delaware)
- Repo went onto GitHub on 19 Nov 2022 as a private, invite-only repo with 5 watchers. The team seeded it privately through their own network before making it public [verified, Plane blog]. — [Plane blog: 20k stars](https://plane.so/blog/how-we-got-to-20k-github-stars)
- "Hacker News was almost 3X more effective than all their previous efforts on Reddit and Twitter." A single HN post brought about 7,000 stars [verified, via search summary of Plane blog]. — [Plane blog](https://plane.so/blog/how-we-got-to-20k-github-stars)
- #1 open-source project-management tool on GitHub by Sep 2023 at 14k stars, 18k in Oct 2023, and 20k within about a year [verified]. — [Plane blog](https://plane.so/blog/how-we-got-to-20k-github-stars)
- Plane drew criticism for posting a star chart against unnamed competitors, and OpenSauced described its stars as the result of "deliberate growth hacking" [reported]. — [DEV/OpenSauced: Growth Hacking Killed GitHub Stars](https://dev.to/opensauced/growth-hacking-killed-github-stars-40on)
- $4M seed, funded "solely by OSS Capital," Nov 2023 (Caplight lists Apr 2024) [verified]. — [Plane seed blog](https://plane.so/blog/plane-raises-4m-seed); [Inc42](https://inc42.com/buzz/plane-bags-4-mn-to-offer-project-management-solutions-to-firms/)
- About 56k stars in Aug 2026 [estimate, ideaproof tracker]. No Series A found. — [ideaproof](https://ideaproof.io/open-source/project/plane)

**ToolJet** (internal-tool / low-code builder; founder Navaneeth PK, Kerala; earlier co-founded MobioPush, which Freshworks acqui-hired in 2015)
- First commit 31 Mar 2021. Repo made public and launched on 7 Jun 2021: Product Hunt first, then HN a few hours later. The HN post was #1 within about an hour, there were 1,000+ stars within 8 hours plus hundreds of cloud signups, and 2.4k stars after 3 days [verified, founder]. — [ToolJet blog: 10 to 2000 stars in 3 days](https://blog.tooljet.com/building-and-launching-tooljet/); [opensource.com](https://opensource.com/article/22/10/tooljet-open-source-journey)
- 4,000 stars and 100 contributors by end of 2021. About 5k stars at the Show HN for ToolJet 1.0 (Feb 2022). 10k stars in Jun 2022, exactly one year after open-sourcing. 16k at the 2.0 launch (Jan 2023). 17k+ in Feb 2023 per TechCrunch [verified/reported]. — [Show HN 1.0](https://news.ycombinator.com/item?id=30257335); [Show HN 2.0](https://news.ycombinator.com/item?id=34323247); [Zero to 10k](https://blog.tooljet.com/zero-to-10-000-stargazers-on-github/); [TechCrunch Feb 2023](https://techcrunch.com/2023/02/02/tooljet-an-open-source-low-code-app-builder-wants-to-help-companies-do-more-with-less/)
- 2-year mark (Mar 2023): 18.4k stars, 315 contributors, and 1,700+ Slack members [verified]. A later post covered about 20k stars and 400 contributors. About 41.1k stars in 2026 [estimate]. — [Two years of ToolJet](https://blog.tooljet.com/two-years-of-tooljet/); [DEV: 20k stars & 400 contributors](https://dev.to/tooljet/how-tooljet-gained-20000-github-stars-and-400-contributors-4ee0); [GitHub](https://github.com/ToolJet/ToolJet)
- Funding: $1.5M seed (Jan 2022) led by Nexus, with Ratio Ventures and Better Capital. An undisclosed round from Microsoft M12 and GitHub followed (Jul 2023) [reported]. — [Entrepreneur India](https://india.entrepreneur.com/?p=32752); [Inc42](https://inc42.com/buzz/open-source-low-code-platform-tooljet-secures-funding-from-microsofts-m12-fund-github-invest/)
- The GitHub README now positions it as "ToolJet AI – enterprise app generation platform… from Claude Code, Codex and Cursor over MCP," which shows a later pivot toward AI [verified, 2026]. — [GitHub](https://github.com/ToolJet/ToolJet)

**SigNoz** (observability; Pranay Prateek (ex-Microsoft, IIT Madras) and Ankit Nayan (IIT Delhi); YC W21)
- Positioned as an "open source alternative to DataDog/NewRelic," OpenTelemetry-native, and self-hostable for privacy-conscious companies [verified]. — [YC](https://www.ycombinator.com/companies/signoz); [TechCrunch Sep 2023](https://techcrunch.com/2023/09/28/open-source-datadog-rival-signoz-lands-on-the-cloud-with-6-5m-investment)
- HN front page: 480+ points and 100+ comments, mentioned alongside a "9000+ GitHub stars" update (2022) [verified]. — [SigNal 17](https://signoz.io/blog/community-update-17/); [Show HN](https://news.ycombinator.com/item?id=33049046)
- Community growth over time [verified, company]: 11k stars, 1,800 Slack members and 80 contributors (YC launch post); then 3,000 members and 5M downloads (Sep 2023); then 20k+ stars, 6,000+ Slack members and 150+ contributors (job post); then "over 22k stars" (2025 AMA). — [YC launch](https://www.ycombinator.com/launches/Hqn-signoz-open-source-alternative-to-datadog-new-relic); [BW Disrupt](https://bwdisrupt.com/article/signoz-raises-54mn-from-signalfire-others-493376); [YC jobs](https://www.ycombinator.com/companies/signoz/jobs); [Reddit r/devops](https://reddit.birdcat.cafe/r/devops/comments/1l8jrc2/comment/mx5bshc)
- Funding: $1.1M after YC, then $5.4M led by SignalFire (Sep 2023), totaling $6.5M seed [verified]. Revenue: Latka says $279K (2021) and Prospeo estimates about $3M [estimates, conflicting]. — [Entrackr](https://entrackr.com/2023/09/signoz-raises-5-4-mn-in-a-new-round); [SigNoz newsroom](https://signoz.io/newsroom/signoz-funding/); [Latka](https://getlatka.com/companies/signoz); [Prospeo](https://prospeo.io/c/signoz-revenue)
- The Scaling DevTools podcast episode is titled "How SigNoz grew to 12k GitHub stars." Its summary says growth came from technical content plus developer communities, and that buyers want to "run a tool, inspect it, ask a community" before talking to sales [reported]. — [Scaling DevTools](https://scalingdevtools.com/podcast/episodes/pranay-prateek)

**Requestly** (HTTP interception / API mocking; Sachin Jain and Sagar Soni; YC W22)
- Started as a Chrome extension and became an "open-source Postman alternative." 200,000+ active installs, users at Google and Amazon [verified, YC]. — [YC](https://www.ycombinator.com/companies/requestly); [YC launch](https://www.ycombinator.com/launches/MKD-requestly-open-source-api-mocking-testing-tool-for-developers)
- Jain described growth with no landing pages or marketing, driven by Stack Overflow answers and GitHub [reported, Baremetrics interview]. — [Baremetrics video](https://baremetrics.com/videos/accidentally-building-a-y-combinator-backed-startup-with); [Baremetrics founder chat](https://baremetrics.com/founder-chats/sachin-jain)
- Total funding about $125K (YC, Peak XV, Titan Capital, Neon Fund) [estimate]. BrowserStack acquired it in 2025 for an undisclosed amount, with 200k+ developers at 10k+ companies at the time [reported]. — [Inc42](https://inc42.com/?p=513025); [Entrepreneur India](https://india.entrepreneur.com/?p=80513)

**Chatwoot** (open-source Intercom/Zendesk alternative; Pranav Raj, Sojan Jose, Nithin David Thomas; Kerala/Bengaluru; YC W21)
- 10k stars announced in 2021. $1.6M seed (2021) from Goat Capital, Uncorrelated, YC and angels including Austen Allred [verified]. Stars now about 19k [estimate]. — [Chatwoot August update](https://www.chatwoot.com/blog/chatwoot-august-update); [startups.fm](https://startups.fm/startups/chatwoot)
- Revenue: about ₹2.2 Cr in FY25 (Inc42 datalabs) and about $370K as of Mar 2023 (The Company Check) [estimates]. — [Inc42](https://inc42.com/company/chatwoot/); [The Company Check](https://www.thecompanycheck.com/company/b/chatwoot/ps76meay46daqx480)

**Keploy** (API test generation from real traffic via eBPF; Shubham Jain and Neha Gupta; Bengaluru, Hybridk8s Pvt Ltd)
- Both founders have a GSoC/Outreachy mentoring background (XWiki, JenkinsX) [reported]. — [OSS EU 2024 speaker profile](https://osseu2024.sched.com/speaker/neha65)
- $1.3M seed (Mar 2022; Chiratae, Upsparks) [estimate]. Flipkart Ventures also backed it [reported]. — [neuronfeed](https://neuronfeed.com/startups/keploy); [f4.fund](https://f4.fund/firms/flipkart-ventures/activity)
- Aug 2024: "5.2K stars, 850+ contributors, 900 forks" [verified, Keploy]. A later undated profile claims 17k+ stars and 1,000+ contributors [estimate]. Keploy also runs an OSS fund of about $12,500 per developer per year [verified]. — [Keploy OSS Funds 2024](https://wp.keploy.io/?p=2571); [everydev.ai](https://www.everydev.ai/developers/keploy)

**Devtron** (Kubernetes DevOps platform; Prashant Ghildiyal, Nishant Kumar, Rajesh Razdan; 2019)
- $12M led by Insight Partners (Oct 2022), after an earlier round from Leo Capital. The CEO cited "thousands of nimble startups across the globe installing Devtron every month" [verified, press release]. No star data was found. — [Insight Partners](https://www.insightpartners.com/ideas/devops-modernization-platform-devtron-announces-12-million-in-funding-from-global-software-investor-insight-partners/)

**Middleware** (cloud observability; Laduram Vishnoi, previously founded Acquire.io)
- Founded 2022 with $500K of the founder's own money and 15 engineers. $6.5M seed led by 8VC (2023), with Guillermo Rauch participating [reported]. No ARR figure has been disclosed. — [YourStory](https://yourstory.com/2023/10/ai-startup-cloud-observability-middleware-developers-code-debugging); [VentureBeat](https://venturebeat.com/ai/middleware-raises-6-5m-to-simplify-cloud-monitoring-with-ai)

**Hyperswitch (Juspay)** (open-source payment orchestration, written in Rust)
- 14k+ stars at its US/EU expansion launch (Mar 2025) and "42K+" stars in 2025–26, with "150+ core engineers" [verified, company-reported]. This is corporate-backed open source, not a scrappy startup. — [Hyperswitch newsroom](https://hyperswitch.io/newsroom/juspay-hyperswitch-open-source-payments-platform-expands-to-us-europe-and-uk); [Hyperswitch about](https://hyperswitch.io/about)

**listmonk / Zerodha open source** (Kailash Nadh)
- listmonk is a self-hosted newsletter manager built partly so Zerodha could send bulk email cheaply. Nadh co-founded FOSS United (2020). Zerodha's FLOSS/Fund (Oct 2024) gives $1M a year in grants of $10k–$100k, applied for through a `funding.json` file [verified/reported]. — [Wikipedia: Kailash Nadh](https://en.wikipedia.org/wiki/Kailash_Nadh); [The Register](https://www.theregister.com/2024/10/17/zerodha_open_source_fund/); [Sustain podcast 257](https://podcast.sustainoss.org/257)

**Ente** (E2E-encrypted photos; Vishnu Mohandas, ex-Google). Not a developer tool, but a useful model for Indian open-source monetization.
- Profitable and funded by subscriptions, with 100k+ users. Plans: 10GB free, then $9.99/mo for 1TB [reported, TechCrunch Apr 2025]. Server code open-sourced in 2024. Ran the viral stunt site theyseeyourphotos.com (Dec 2024) [reported]. — [TechCrunch](https://techcrunch.com/2025/04/01/ente-wants-to-take-on-google-photos-with-its-privacy-first-photo-storage-service); [PetaPixel](https://petapixel.com/2024/12/03/this-website-reveals-what-googles-ai-can-learn-from-your-photos/)

**Dyte** (video SDK; Abhishek Kankani, Kushagra Vaish, Palash Golecha). This is SaaS, not open-source-first.
- $11.6M seed (Apr 2022) led by Sequoia Surge, Nexus and Unbound [verified]. Reported acquired by Cloudflare [reported, single source]. — [TechCrunch](https://techcrunch.com/2022/04/07/dyte-raises-11-6m-to-help-developers-build-better-video-calls/); [Venture Intelligence](https://news.ventureintelligence.com/private-equity/multimedia-integration-s'ware-maker-dyte-acquired-by-cloudflare)

**OpenObserve** (logs/observability, Rust; founder/CEO Prabhat Sharma)
- 18k+ stars (Apr 2026) and 20k+ (15 Jul 2026). 6,000 to 8,000+ organizations. $10M Series A (Apr/May 2026) led by Nexus and Dell Technologies Capital. Claims "140x lower storage cost than Elasticsearch" [verified, press release; vendor claim]. The company is US-headquartered, and Indian founding was not verified. — [Pulse 2.0](https://pulse2.com/openobserve-raises-10-million-series-a-to-accelerate-ai-native-observability-platform/); [Business Wire via StreetInsider](https://www.streetinsider.com/Business+Wire/OpenObserve+Surpasses+20%2C000+GitHub+Stars+as+Developers+Embrace+Open+Source+Observability/26773564.html)

**Appsmith** (upper bound; Abhishek Nayak, Arpit Mohan, Nikhil Nandagopal; 2019)
- $8M Series A (Oct 2021, Canaan) and $41M Series B (Jun 2022, Insight), about $51.5M in total. As of Jun 2022: 18k+ stars ("up 12x since 2021"), 10M+ downloads, 18k community members and 192 contributors. 30k stars in Mar 2024 [verified/reported]. — [Insight Partners](https://www.insightpartners.com/ideas/appsmith-raises-41-million-to-scale-open-source-platform/); [DevTools Brew](https://morganperry.substack.com/p/devtools-brew-66-building-appsmith)

**Not confirmed as Indian-founded / exclude**
- Infisical (CEO Vlad Matsiiako), Mintlify (Han Wang and Hahnbee Lee, who met at Cornell) and FlowiseAI (Henry Heng): the search results did not establish Indian founding. — [lemelson.org](https://www.lemelson.org/hahnbee-lee/); [seedtable Flowise](https://seedtable.com/companies/flowiseai)

### Inferences
- The cohort splits into two playbooks. **Grassroots, solo-founder tools** (Hoppscotch, Bruno, Requestly) began as personal itches, grew organically, and raised small rounds late or quietly. **Founder-led COSS startups** (Plane, ToolJet, SigNoz, Appsmith) planned a big launch moment (HN/PH) and raised institutional seed rounds soon after.
- OSS Capital is the recurring Indian dev-tool seed investor (Hoppscotch, Plane, Appsmith), and Nexus is the recurring Indian VC (ToolJet, Dyte, OpenObserve).

### Gaps
- No current (Oct 2026) GitHub-verified star counts, because the GitHub API was blocked. Treat the aggregator numbers above as approximate.
- Founding geography could not be confirmed for Bruno's legal entity (Bruno Software Inc. vs an Indian entity) or for OpenObserve, Infisical, Mintlify and Flowise.

## Launch stories: HN / Product Hunt / Reddit / GitHub Trending / FOSS United / Hacktoberfest

### Takeaway
Hacker News front-page moments did most of the work. ToolJet got 1k stars in 8 hours, Plane got about 7k stars from one HN post, SigNoz reached 480+ points, and Bruno was #1 in Mar 2024. Product Hunt was secondary, Reddit/Twitter were weaker, and GitHub Trending amplified the HN spike. Riding competitor backlash (Postman's forced login and Scratch Pad removal) gave Bruno and Hoppscotch durable, compounding demand.

### Cited Findings
- ToolJet sequence: PH launch first, then HN a few hours later. HN reached #1 within about an hour, and the founder reports 1,000+ stars in 8 hours and 2.4k in 3 days (Jun 2021) [verified]. ToolJet used a fresh "Show HN" for each major release: 1.0 in Feb 2022 at about 5k stars, 2.0 in Jan 2023 at 16k. — [ToolJet blog](https://blog.tooljet.com/building-and-launching-tooljet/); [Show HN 1.0](https://news.ycombinator.com/item?id=30257335); [Show HN 2.0](https://news.ycombinator.com/item?id=34323247)
- Plane: private invite-only repo, then a public launch; "HN was almost 3X more effective than all previous efforts on Reddit and Twitter," and one HN post brought about 7,000 stars [verified]. — [Plane blog](https://plane.so/blog/how-we-got-to-20k-github-stars)
- SigNoz: HN front page over a weekend with 480+ points and 100+ comments. The podcast summary cites a separate launch with 200+ upvotes, so these are likely different posts [verified/reported]. — [SigNoz SigNal 17](https://signoz.io/blog/community-update-17/); [Scaling DevTools](https://scalingdevtools.com/podcast/episodes/pranay-prateek)
- Bruno: top of HN on 9–10 Mar 2024. The top comments were about Postman's forced login ("As soon as Postman asked for a login I uninstalled it"). Marmelab reported 2k to about 18k stars in 5 months [verified/reported]. — [HN](https://news.ycombinator.com/item?id=39653718); [HN comment](https://news.ycombinator.com/item?id=39654210); [Marmelab](https://marmelab.com/blog/2024/05/03/we-dont-talk-about-bruno.html)
- Postman removed Scratch Pad (offline, no-login use) in v10.18, released 15 Sep 2023 [verified, per Postman docs/blog as summarised]. Bruno's star curve accelerated in the following months. — [Voiden comparison summarising Postman docs](https://voiden.md/blog/postman-vs-insomnia-vs-bruno-vs-hoppscotch-vs-voiden-2026-comparison)
- Hoppscotch: a podcast describes the start as "a single post and how that post got viral." Thomas says the growth was all organic. A second HN thread, "Hoppscotch: Open-source alternative to Postman" (2022), resurfaced it [verified]. It hit #1 on GitHub Trending on 24 Jul 2024 [reported]. — [Craft of Open Source podcast](https://www.flagsmith.com/podcast/hoppscotch); [HN 2020](https://news.ycombinator.com/item?id=24895218); [HN 2022](https://news.ycombinator.com/item?id=30498072); [Trendshift](https://trendshift.io/repositories/36)
- Hacktoberfest: ToolJet's first Hacktoberfest (2021) brought 72 new contributors from more than a dozen countries, using "good first issue" labels and Slack for help. It repeated in 2022 with a dedicated community call [verified]. SigNoz also took part in Hacktoberfest and launched a technical writer program [verified]. — [ToolJet Hacktoberfest recap](https://blog.tooljet.com/tooljets-first-hacktoberfest-it-turned-out-to-be-great/); [ToolJet HF 2022](https://blog.tooljet.com/hacktoberfest-2022/); [SigNoz HF](https://dev.to/signoz/signoz-is-taking-part-in-hacktoberfest-16fj); [SigNoz writer program](https://dev.to/signoz/launching-signoz-technical-writer-program-hmi)
- FOSS United / IndiaFOSS: IndiaFOSS 2024 had 1,500+ participants. IndiaFOSS 2025 (20–21 Sep 2025, Bengaluru plus online, 5th edition) had 18 sponsors, 11 of them open-source companies [verified]. Bruno spoke at IndiaFOSS 2024 [verified]. — [IndiaFOSS 2025 sponsorship deck](https://fossunited.org/files/IndiaFOSS%202025%20Sponsorship%20Deck.pdf); [FOSS United grants 2025](https://fossunited.org/blog/grants/2025-grants-recap); [Bruno CFP](https://fossunited.org/c/indiafoss/indiafoss24/cfp/oas92icb9u)
- Hoppscotch's CEO did an r/developersIndia AMA (8 Sep 2023) [verified]. — [r/developersIndia AMA](https://lr.us.psf.lt/r/developersIndia/s/gWcND0DcZY)

### Inferences
- The repeatable launch pattern is: build a small warm audience first (Plane's private repo), then do PH and HN on the same day (ToolJet), reply in the HN thread yourself (Anoop and Pranay both did), and point everyone to Slack or Discord.
- Re-launching each major version on HN (ToolJet 1.0 and 2.0) produced fresh spikes, so HN does not have to be a one-time event.
- For Indian tools, FOSS United, r/developersIndia AMAs and GitHub's "made in India" storytelling (GitHub Satellite) build domestic credibility and hiring pipelines. The star and user spikes, however, came from global channels (HN).

### Gaps
- No source found for Plane's or Hoppscotch's Product Hunt rank or date.
- Hoppscotch's original 2019 viral post (platform and numbers) was not found in snippets.
- Exact star-history curves were not retrievable (star-history.com and the GitHub API were blocked).

## Positioning tactics: "open-source alternative to X", offline/local-first, anti-bloat; value of competitor backlash

### Takeaway
Almost every tool in the set led with "open-source alternative to [incumbent]": Postman (Hoppscotch, Requestly, Bruno), Jira/Linear (Plane), Retool (ToolJet/Appsmith), Datadog (SigNoz/OpenObserve/Middleware) and Intercom (Chatwoot). That was combined with a privacy, self-host, offline or Git-native angle. Competitor backlash (Postman's login and cloud push) was the single biggest tailwind for Bruno and a lasting one for Hoppscotch.

### Cited Findings
- Hoppscotch began as "Postwoman," a "web alternative to Postman." It renamed to avoid trademark risk and later framed itself as having outgrown "just a Postman alternative." Thomas credits a minimalist UI and avoiding bloated features [verified]. — [DEV rename post](https://dev.to/liyasthomas/postwoman-is-changing-name-igp); [GitHub discussion #5481](https://github.com/hoppscotch/hoppscotch/discussions/5481); [GitHub ReadME](https://github.com/readme/stories/liyas-thomas)
- Bruno: "Git-friendly," with collections stored on the filesystem, local-first and no cloud account. HN commenters explicitly cited Postman's forced login [verified]. — [HN](https://news.ycombinator.com/item?id=39653718); [DEV comparison](https://dev.to/ctrix/hoppscotch-the-modern-lightweight-alternative-to-postman-and-bruno-3gkm)
- A weak-evidence blog claims Bruno adoption roughly tripled since Postman's pricing change, measured by .bru files in public repos [estimate]. — [Voiden](https://voiden.md/blog/postman-vs-insomnia-vs-bruno-vs-hoppscotch-vs-voiden-2026-comparison)
- Plane: "Open Source JIRA, Linear and Asana/Height alternative" [verified]. — [Plane blog](https://plane.so/blog/how-we-got-to-20k-github-stars); [ideaproof](https://ideaproof.io/open-source/project/plane)
- SigNoz: "open-core alternative to DataDog for companies that are security and privacy conscious" and do not want data leaving their infrastructure, plus OpenTelemetry-native [verified]. — [SigNoz blog](https://signoz.io/blog/open-source-datadog-alternative); [TechCrunch](https://techcrunch.com/2023/09/28/open-source-datadog-rival-signoz-lands-on-the-cloud-with-6-5m-investment)
- OpenObserve: cost positioning against Datadog, Splunk and Elasticsearch ("140x lower storage costs") [verified, vendor claim]. — [StreetInsider/Business Wire](https://www.streetinsider.com/Business+Wire/OpenObserve+Surpasses+20%2C000+GitHub+Stars+as+Developers+Embrace+Open+Source+Observability/26773564.html)
- Requestly: YC lists it as an "open-source Postman alternative," though it started as a Chrome extension for HTTP rewriting [verified]. — [YC](https://www.ycombinator.com/companies/requestly)
- Ente: privacy against Google Photos, plus an adversarial marketing stunt (theyseeyourphotos.com) that turned Google's own Vision AI against it [reported]. — [PetaPixel](https://petapixel.com/2024/12/03/this-website-reveals-what-googles-ai-can-learn-from-your-photos/)

### Inferences
- "Alternative to X" makes discovery cheap, because people already search for "X alternative." The risk is being defined by X (Hoppscotch's rename). The mature move is to later reposition as an "ecosystem" or "platform" (Hoppscotch, ToolJet → "ToolJet AI").
- Backlash only converts if the alternative fixes the exact grievance: Bruno's no-login, files-in-Git design directly answered Postman's forced login and the removal of offline Scratch Pad.

### Gaps
- No quantitative before/after star data around 15 Sep 2023 (Scratch Pad removal) was retrievable for Bruno or Hoppscotch.

## Community: Discord/Slack sizes, contributors, programs, Indian meetups, GSoC/Hacktoberfest, college outreach

### Takeaway
Slack, not Discord, was the default for the B2B-ish tools: ToolJet had 1.7k+ members, SigNoz grew from 1.8k to 6k+. Contributor counts were driven by Hacktoberfest and "good first issue" labelling (ToolJet reached 315 then 400 contributors, Keploy claims 850+). Founders from the GSoC mentor community (Keploy) used that network deliberately.

### Cited Findings
- ToolJet: 1,700+ Slack members, 315 contributors and 18.4k stars (Mar 2023). The "Zero to 10k" lesson was that "product-community fit is crucial." It committed to faster issue/PR turnaround, more tutorials and community calls [verified]. — [Two years of ToolJet](https://blog.tooljet.com/two-years-of-tooljet/); [Zero to 10k](https://blog.tooljet.com/zero-to-10-000-stargazers-on-github/)
- SigNoz: Slack grew from 1,800 (YC launch) to 3,000 (Sep 2023) to 6,000+ (job post). Contributors went from 80 to 150+ [verified, company]. The Show HN replies directed people to Slack. — [YC launch](https://www.ycombinator.com/launches/Hqn-signoz-open-source-alternative-to-datadog-new-relic); [BW Disrupt](https://bwdisrupt.com/article/signoz-raises-54mn-from-signalfire-others-493376); [YC jobs](https://www.ycombinator.com/companies/signoz/jobs); [SigNoz community docs](https://signoz.io/docs/community/)
- Appsmith: 18k community members and 192 contributors (Jun 2022) [verified]. — [Insight Partners](https://www.insightpartners.com/ideas/appsmith-raises-41-million-to-scale-open-source-platform/)
- Keploy: 850+ contributors with only 5.2k stars (Aug 2024), an unusually high contributor-to-star ratio that suggests heavy student/Hacktoberfest/GSoC funnelling. Its founders were GSoC/Outreachy mentors [verified/reported]. — [Keploy OSS Funds](https://wp.keploy.io/?p=2571); [OSS EU speaker](https://osseu2024.sched.com/speaker/neha65)
- Hyperswitch: "150+ core engineers" plus global contributors [verified, company]. — [Hyperswitch about](https://hyperswitch.io/about)
- FOSS United is the Indian community hub. Late-2025 meetup listings included Coimbatore, Hyderabad, Mumbai, Kolkata, Bihar, Chennai and Mangalore. IndiaFOSS had 1,500+ attendees (2024). FOSS United grants are co-sponsored by Zerodha (e.g., ₹9 lakh to Zasper) [verified]. — [FOSS United platform](https://platform.fossunited.org); [FOSS United grants 2025](https://fossunited.org/blog/grants/2025-grants-recap); [Zerodha 2025 OSS report](https://zerodha.com/open-source/2025-report/)
- Zerodha FLOSS/Fund: $1M a year. Since May 2025 it had disbursed $195k (Krita, OpenSSL, Weblate) as of Oct 2025 [reported]. — [OpenSourceForU](https://www.opensourceforu.com/2025/10/zerodha-announces-final-675000-tranche-for-global-open-source-projects-advocates-sovereign-foss-fund/)

### Inferences
- High contributor counts (Keploy 850+, ToolJet 400) are partly a function of Indian student demand for open-source credentials. That gives cheap reach on campus but a low share of core code; star-to-contributor ratios differ widely.
- Slack suits tools sold to companies (observability, internal tools), since buyers and engineers are already there. Discord is more common for consumer-dev tools, but no Discord sizes were found for Hoppscotch or Bruno.

### Gaps
- No Discord member counts found for Hoppscotch, Bruno or Plane.
- No evidence found of formal ambassador or campus programs (e.g., Hoppscotch/Plane campus ambassadors) or Bangalore/Pune company-run meetups with attendance numbers.
- Contributor counts for Hoppscotch, Bruno and Plane were not available (GitHub API blocked).

## Social media: X / LinkedIn / YouTube content, viral posts, Indian creators

### Takeaway
Public evidence of social tactics is thin. The documented pattern is founder-led milestone posts (DEV.to "celebrating N stars" posts, LinkedIn launch posts), first-party transparency blogs (Bruno's yearly recaps and "The Funding Announcement We Never Made"), and star-chart tweets that can backfire (Plane). Stunt microsites (Ente) are the standout viral tactic.

### Cited Findings
- Liyas Thomas published a series of milestone posts on DEV.to (25k, 30k, 35k stars) and LinkedIn launch posts, for example the Desktop App launch (Nov 2023) and engineering-team growth posts [verified]. — [DEV 25k](https://dev.to/liyasthomas/hoppscotch-celebrating-25-000-github-stars-5aao); [LinkedIn desktop launch](https://www.linkedin.com/posts/liyasthomas_today-were-launching-our-desktop-app-at-activity-7128082569539063808-Hlrj); [LinkedIn team post](https://in.linkedin.com/posts/liyasthomas_hoppscotchs-engineering-team-has-grown-quite-activity-6957729663175540736--o1q)
- ToolJet published "how we got N stars" posts on DEV.to and its blog (10k stars/160 contributors; 20k/400) [verified]. — [DEV 10k](https://dev.to/tooljet/from-zero-to-10000-stars-and-160-contributors-on-github-3057); [DEV 20k](https://dev.to/tooljet/how-tooljet-gained-20000-github-stars-and-400-contributors-4ee0)
- Plane's star-growth tweet and blog went viral, but drew criticism for comparing its chart against unnamed competitors [reported]. — [DEV/OpenSauced](https://dev.to/opensauced/growth-hacking-killed-github-stars-40on)
- Bruno's content is transparency-heavy: "State of Bruno" updates, yearly recaps with MAU and star numbers, and the funding post, which was syndicated on daily.dev [verified]. — [State of Bruno](https://blog.usebruno.com/bruno-update); [daily.dev](https://daily.dev/posts/the-funding-announcement-we-never-made-joknszzvh)
- Ente's theyseeyourphotos.com stunt got wide coverage (PetaPixel, Wired-derived reports) [reported]. — [PetaPixel](https://petapixel.com/2024/12/03/this-website-reveals-what-googles-ai-can-learn-from-your-photos/)

### Inferences
- "How we got N stars" posts work as content marketing in their own right. They get re-shared by other founders and are indexed long-term.
- Transparency posts (numbers, funding, pricing reversals) build trust with developer audiences who are wary of a "Postman-style rug pull."

### Gaps
- No data found on Instagram or YouTube strategy, Indian creator collaborations, or specific viral post view counts for any of these tools.

## Monetization: open core, cloud, enterprise, pricing, ARR/funding

### Takeaway
The dominant model is open core with cloud and enterprise tiers (SSO, audit logs, RBAC, team collaboration). Seeds are typically $1.5M–$6.5M and come once traction (10k+ stars) is proven. Revenue disclosures are rare; the public ARR/revenue figures are third-party estimates. Bruno's switch from a $19 perpetual license to subscriptions plus a quiet $3M raise is the clearest documented case of a bootstrapped model being revised.

### Cited Findings
- Hoppscotch: Free at $0; Organization at $6/user/month billed annually (admin dashboard, team collaboration); Enterprise custom (SSO, audit logs). Subscriptions for both SaaS and self-hosted. About $2M ARR in 2025 [estimate]. $3M seed (Dec 2021, OSS Capital and Automattic) [verified]. — [everydev.ai](https://www.everydev.ai/developers/hoppscotch); [IndieHackers](https://www.indiehackers.com/post/hoppscotch-raises-3m-in-seed-funding-to-build-open-source-api-development-ecosystem-3ab1ef9278)
- Bruno: Golden Edition at $19 one-time (2023–24), discontinued for new buyers by Jun 2025 as "not a sustainable model." Now Pro/Ultimate subscriptions. $3M raised and announced after the fact, after the founder had said "we will never take VC funding" in Mar 2024 [verified]. — [HN](https://news.ycombinator.com/item?id=39656680); [GitHub #269](https://github.com/usebruno/bruno/discussions/269); [Bruno funding post](https://blog.usebruno.com/the-funding-announcement-we-never-made)
- ToolJet: free community edition with no usage limits plus a paid enterprise edition. "Very large companies as paying customers," but the team "has not pushed monetization hard" (2022) [verified, founder]. — [opensource.com](https://opensource.com/article/22/10/tooljet-open-source-journey)
- SigNoz: usage-based cloud pricing plus self-host. $6.5M seed total. Revenue estimates conflict ($279K in 2021 vs about $3M) [estimate]. — [SignalFire](https://www.signalfire.com/blog/signoz-pioneers-open-source-observability-with-65m-led-by-signalfire); [Latka](https://getlatka.com/companies/signoz); [Prospeo](https://prospeo.io/c/signoz-revenue)
- Plane: $4M seed from OSS Capital (Nov 2023). No Series A found as of Oct 2026 [verified]. — [Plane seed](https://plane.so/blog/plane-raises-4m-seed)
- Chatwoot: $1.6M seed. Revenue about ₹2.2 Cr in FY25 [estimate]. — [Chatwoot](https://www.chatwoot.com/blog/chatwoot-august-update); [Inc42](https://inc42.com/company/chatwoot/)
- Requestly: about $125K raised, then an exit to BrowserStack (2025) [reported]. — [Inc42](https://inc42.com/?p=513025)
- Devtron $12M (Insight, 2022); Middleware $6.5M (8VC, 2023); Dyte $11.6M seed (2022); Appsmith $51.5M total; OpenObserve $10M Series A (2026) [verified/reported]. — [Insight/Devtron](https://www.insightpartners.com/ideas/devops-modernization-platform-devtron-announces-12-million-in-funding-from-global-software-investor-insight-partners/); [VentureBeat/Middleware](https://venturebeat.com/ai/middleware-raises-6-5m-to-simplify-cloud-monitoring-with-ai); [TechCrunch/Dyte](https://techcrunch.com/2022/04/07/dyte-raises-11-6m-to-help-developers-build-better-video-calls/); [Pulse2/OpenObserve](https://pulse2.com/openobserve-raises-10-million-series-a-to-accelerate-ai-native-observability-platform/)
- Ente: subscription-funded and profitable; 10GB free, then $9.99/mo for 1TB [reported]. — [TechCrunch](https://techcrunch.com/2025/04/01/ente-wants-to-take-on-google-photos-with-its-privacy-first-photo-storage-service)
- Frappe: "took more than a decade… from sustainability to profitability." Monetizes through a partner ecosystem and partner-run conferences [verified, Frappe site snippets]. — [Frappe Mauritius](https://frappe.io/blog/community/frappe-local-mauritius)

### Inferences
- Low per-seat pricing (Hoppscotch at $6/user) undercuts the incumbent and suits small teams. Enterprise SSO and audit logs are the real revenue gates.
- Star counts are monetization-lagging: Hoppscotch at about 70–80k stars is estimated at only about $2M ARR. Large open-source audiences do not translate linearly into revenue, and Indian tools often under-monetize early (ToolJet: "not pushed monetization hard").

### Gaps
- No primary-source ARR or revenue figure exists for any of Hoppscotch, Bruno, Plane, ToolJet, SigNoz or Keploy.
- Plane, ToolJet and SigNoz current pricing pages were not retrievable.

## Mistakes and lessons founders shared

### Takeaway
The documented lessons are: (1) product-community fit and fast issue response matter more than stars (ToolJet); (2) one-time licenses do not sustain a growing team, and anti-VC pledges can break (Bruno); (3) competitor-comparison star charts invite a backlash (Plane); (4) "alternative to X" names carry trademark and identity risk (Postwoman); (5) developer buyers want to self-evaluate through community before sales (SigNoz).

### Cited Findings
- ToolJet: "getting product-community fit is crucial for any open-source startup." Fixes included more Slack support, faster issue/PR turnaround, and more tutorials and events [verified]. — [Zero to 10k](https://blog.tooljet.com/zero-to-10-000-stargazers-on-github/)
- ToolJet's founder relied on writing about learnings and being active in developer communities instead of paid marketing [verified]. — [opensource.com](https://opensource.com/article/22/10/tooljet-open-source-journey)
- Bruno: the $19 perpetual license "could not support the usage volume." It stopped new Golden Edition sales (Jun 2025), raised $3M, and moved previously paid features to free [verified]. — [GitHub #269](https://github.com/usebruno/bruno/discussions/269); [Bruno funding post](https://blog.usebruno.com/the-funding-announcement-we-never-made)
- Plane: criticized for a star chart against unnamed competitors, with growth labelled "deliberate growth hacking" [reported]. — [DEV/OpenSauced](https://dev.to/opensauced/growth-hacking-killed-github-stars-40on)
- Hoppscotch: renamed from Postwoman over trademark risk and goodwill [verified]. — [DEV](https://dev.to/liyasthomas/postwoman-is-changing-name-igp)
- SigNoz: developers want to "run a tool, inspect it and ask a community" before a formal sales process, so content and community come before sales [reported, podcast summary]. — [Scaling DevTools](https://scalingdevtools.com/podcast/episodes/pranay-prateek)
- Requestly: grew with "no landing pages or marketing," answering Stack Overflow questions and using GitHub [reported]. — [Baremetrics](https://baremetrics.com/founder-chats/sachin-jain)
- Frappe: more than a decade from sustainability to profitability, a warning about how slowly pure-FOSS business models mature [verified]. — [Frappe](https://frappe.io/blog/community/frappe-local-mauritius)
- Stars are a fundraising signal and are open to inflation; there has been broader commentary on "GitHub's fake star economy" [reported]. — [Unicorn CTO #124](https://developerfirst.substack.com/p/issue-124); [Peerlist](https://peerlist.io/saxenashikhil/articles/inside-githubs-fake-star-economy)

### Inferences
- For a small Indian tool, the evidence favors: a narrow, pain-specific wedge ("Postman but offline/Git-native"); a single coordinated HN+PH launch with the founder answering in the thread; Slack/Discord and "good first issue" for Hacktoberfest; transparent milestone posts; and starting paid team/enterprise tiers earlier than ToolJet did.
- Pledges about funding or pricing ("never VC," lifetime licenses) become public liabilities. Bruno managed this by being transparent after the fact.

### Gaps
- No founder retrospectives found from Plane, Keploy or Devtron on specific mistakes.
- The Hoppscotch Craft of Open Source podcast and the SigNoz Scaling DevTools episode were not fetched in full, so detailed lessons from them are only partially captured.
