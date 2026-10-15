# "Engineer reveals his setup" carousels: format, performance and rules for ZeroAI

> General information only, not legal advice. Current as of 15 Oct 2026. Method note: web search worked, but direct page fetches failed with DNS errors for every host tried (docs.x.com, developer.x.com, yahoo, substack, mindwiredai). So most findings below come from search-result summaries of the cited pages, not full reads. Primary texts (X Display Requirements, ASCI Code Chapter IV, Instagram's own announcement) should be opened and checked before publishing.

## 1. Examples of viral setup-reveal posts: who, engagement, structure, hooks, crediting

### Takeaway
The main example is Boris Cherny's (creator of Claude Code at Anthropic) X thread on his Claude Code workflow in January 2026. Third-party blogs report about 8 to 8.5M views. It was then repackaged on LinkedIn and in blogs under headlines like "Boris Cherny (Claude Code creator) just shared his personal Claude setup..." I found no verifiable engagement numbers for the repackaged carousels, and no sourced examples of "Google engineer VS Code setup" or "Meta engineer daily tools" posts.

### Cited Findings
- One guide says Cherny posted the thread on 31 Jan 2026 and reports 8.5M views, 49,000 likes and 6,400 reposts. A mindwiredai.com article dates the first post to 2 Jan 2026 with about 8M views and mentions a follow-up thread on 31 Jan. These may be two separate posts. All figures come from third parties, not X analytics. — [Jitendra Zaa blog](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/); [mindwiredai](https://mindwiredai.com/?p=1119)
- Content that recurs in summaries: he called his setup "surprisingly vanilla". He runs about 5 Claude instances in parallel in the terminal, starts complex work in Plan Mode, and uses a shared CLAUDE.md checked into the repo that the team updates several times a week. Custom slash commands and subagents also come up. — [Karo Zieminski Substack](https://karozieminski.substack.com/p/boris-cherny-claude-code-workflow); [mindwiredai](https://mindwiredai.com/?p=1119); [Push to Prod Substack](https://getpushtoprod.substack.com/p/how-the-creator-of-claude-code-actually)
- Summaries disagree on the details: one says tmux plus Neovim plus custom scripts, others say 5 parallel instances. Tip counts also differ (10, 13). Some repackagers clearly paraphrased loosely. — [Yahoo Tech](https://tech.yahoo.com/articles/claude-codes-creator-says-setup-091701435.html); [Push to Prod](https://getpushtoprod.substack.com/p/how-the-creator-of-claude-code-actually); [Jitendra Zaa](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/)
- Common LinkedIn hook templates, used almost word for word by many accounts: "Boris Cherny (Claude Code creator) just shared his personal Claude setup to get 10x better results 👇" and "Boris Cherny (creator of Claude Code) just shared how the Claude Code team actually uses it to get 10x productivity 👇". — [LinkedIn example 1](https://se.linkedin.com/in/zsolthalo); [LinkedIn example 2](https://fr.linkedin.com/in/martyguilhem); [LinkedIn example 3](https://pl.linkedin.com/in/nshmelyov)
- A spin-off headline from a forum or affiliate site: "The creator of Claude Code just revealed his workflow and developers are losing their minds". This is the clickbait end of the range. — [AffLift thread](https://afflift.com/f/threads/the-creator-of-claude-code-just-revealed-his-workflow-and-developers-are-losing-their-minds.16030/latest)
- A later follow-up: in a 4 May Sequoia Capital interview, Cherny reportedly said he runs a few thousand agents overnight and manages them mostly from his phone. — [mindwiredai](https://mindwiredai.com/?p=1119) (secondary)
- Adjacent LinkedIn "setup" posts use a numbered-layers structure: "Claude Code is a 4-layer system: CLAUDE.md, skills, hooks, sub-agents". Some are packaged as a one-page A4 cheatsheet. — [LinkedIn example](https://tw.linkedin.com/in/freddie-kuo-74a219a8)

### Inferences
- The structure that recurs, as inferred from the hooks and summaries: (1) a hook slide with name, role and company plus a promise ("10x"); (2) a credibility slide, usually the original post or a quote; (3) 5 to 13 slides with one concrete setting or habit each; (4) a recap or cheatsheet; (5) a CTA (save, follow).
- The format works because the original source is a credible insider (the tool's own creator), the content is concrete and copyable, and the setup is surprisingly simple ("vanilla"). Without those three things the format tends to slide into clickbait.
- Repackagers rarely add anything new, and many copied each other's hook word for word. That is the "unoriginal" pattern Instagram now demotes (see section 3).

### Gaps
- No verified like, comment or share counts for any LinkedIn or Instagram carousel repackaging Cherny's thread. Page fetches failed and search snippets gave no numbers.
- No sourced examples of "Google engineer's VS Code setup" or "Meta engineer's 3 daily tools" carousels. The search index did not surface them, so I can't say who posted them or how they performed.
- Not confirmed how repackagers credited the source (screenshot vs "via @bcherny" vs link). The original thread's exact URL and handle were not fetched.

## 2. Do these posts perform well with developers? Credible vs clickbait

### Takeaway
The Cherny thread shows clear demand: millions of views and wide reposting. But the credibility came from the first-party source and from specific, checkable details. Secondary summaries that inflate claims ("10x", "losing their minds") or get details wrong (tool lists, tip counts) are where trust drops.

### Cited Findings
- 8 to 8.5M reported views on the original thread, plus many LinkedIn reshares and blog breakdowns. — [Jitendra Zaa](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/); [LinkedIn reshares](https://eg.linkedin.com/in/r4gra)
- Search-result summaries flagged that some coverage carries promotional material or reads like AI-generated summaries, and that numbers should be checked against the original posts. — [mindwiredai](https://mindwiredai.com/?p=1119); [winzheng](https://www.winzheng.com/en/article/claude-code-father-workflow-secrets)
- Summaries contradict each other on what the setup actually was (tmux/Neovim vs 5 parallel Claudes). This shows how secondary carousels drift from the source. — [Yahoo Tech](https://tech.yahoo.com/articles/claude-codes-creator-says-setup-091701435.html); [Karo Zieminski](https://karozieminski.substack.com/p/boris-cherny-claude-code-workflow)

### Inferences
- Credibility checklist for ZeroAI:
  - Link the exact original post: date, handle, and the URL in the caption or first comment.
  - Show the original via an embed or link rather than a doctored screenshot.
  - Quote specific settings verbatim (e.g. "5 parallel sessions", "Plan Mode first", "CLAUDE.md in repo").
  - Use the person's own framing ("vanilla") rather than "10x".
  - Avoid generic titles ("Meta engineer") unless you can name the source. An anonymous "Meta engineer" with no link looks made up.
- Clickbait signals that developers punish: "losing their minds", "10x", made-up or unnamed engineers, wrong details, and a hard product pitch dressed up as the engineer's recommendation.

### Gaps
- No studies or platform data found that compare developer engagement on credible vs clickbait setup posts. The points above are inferences.

## 3. Rules and risks of using real names, handles, company names, screenshots and reposts

### Takeaway
Naming a person and company factually to say what they shared is generally low risk. The risks come from: (a) implying they endorse ZeroAI; (b) using logos or marks more than needed; (c) reposting screenshots as-is (copyright, X's rules, and Instagram's originality demotion); (d) in India, using a person's name or likeness in a way that suggests false endorsement (personality rights).

### Cited Findings
**Trademarks and nominative fair use (US doctrine, persuasive elsewhere)**
- The New Kids on the Block test has three parts: (1) the product can't be readily identified without the mark; (2) only as much of the mark is used as necessary; (3) nothing suggests sponsorship or endorsement. — [Hunton Andrews Kurth](https://www.hunton.com/hunton-retail-law-resource/district-court-finds-use-of-third-party-hashtags-created-implied-association)
- *Align Technology v. Strauss Diamond*: a court rejected nominative fair use where the ads used competitors' marks as hashtags. It found the marks were used more than needed and to refer to the advertiser's own product. A plainly worded caption naming the competitor's product was treated as acceptable. — [Hunton](https://www.hunton.com/hunton-retail-law-resource/district-court-finds-use-of-third-party-hashtags-created-implied-association); [Pattishall](https://www.pattishall.com/pdf/LL&P%20MAY%2019.pdf)
- Using a company name accurately for comparison or compatibility is generally allowed. Problems start when a post suggests affiliation or uses more of the mark than needed. — [National Law Review](https://natlawreview.com/node/7273/printable/pdf); [Martech Zone](https://martech.zone/know-fair-use-disclosure-ip)

**India trademark law**
- Section 30(1) of the Trade Marks Act 1999 allows use of a registered mark to identify goods or services if it follows honest practices. Section 29(8) makes an ad infringing if it takes unfair advantage, is contrary to honest practices, or harms the mark's reputation or distinctiveness. "Honest practices" is defined only through case law. — [iPleaders](https://blog.ipleaders.in/comparative-advertisements-india/); [BananaIP](https://www.bananaip.com/intellepedia/trademark-violations-comparative-advertising-india-legal-analysis/); [Mondaq, Beiersdorf v HUL](https://www.mondaq.com/india/advertising-marketing-branding/1470702/comparative-advertising-in-india-beiersdorf-ag-v-hindustan-unilever-limited)

**X/Twitter content**
- X's Display Requirements list prohibited uses, as summarised in search results: using X content to promote any product or service without explicit permission from the user; implying sponsorship or endorsement by X; modifying post text; mockups of posts that don't exist; adding other platforms' icons. X recommends official embeds, and its docs note that the creator's permission may also be needed because X doesn't grant rights to user content. — [X Display Requirements](https://docs.x.com/developer-terms/display-requirements); [X embedded posts FAQ](https://developer.x.com/en/docs/x-for-websites/embedded-tweets/faq)
- Caveat: the Display Requirements are developer terms for API and embed use. Whether they bind a brand posting a screenshot on Instagram is unclear. The "promote a product without the user's explicit permission" line is still a useful bright line.
- X's Terms of Service grant X (and its sublicensees) a broad license to user content, including AI training since 2024. This license does not let third parties such as brands reuse posts, so copyright stays with the author. — [CNN on X ToS change](https://us.cnn.com/2024/10/21/tech/x-twitter-terms-of-service); [ConductAtlas summary](https://conductatlas.com/platform/x/x-terms-of-service/broad-royalty-free-content-license)

**Instagram originality (2026)**
- Instagram extended its originality-based recommendation rules from Reels to photos and carousels. One trade report gives 30 Apr 2026 as the date, and Planoly (5 May 2026) says it rolled out "last week". — [Communicate Online](https://communicateonline.me/news/instagram-expands-crackdown-on-reposted-content-across-platform/); [Planoly](https://planoly.com/blog/instagram-updates-its-original-content-policy)
- Penalty: unoriginal posts still reach followers but are removed from recommendations to non-followers. To count as original, third-party material must be "materially transformed", for example by adding contextual on-screen text, original graphics with new information, or remix tools. — [Communicate Online](https://communicateonline.me/news/instagram-expands-crackdown-on-reposted-content-across-platform/); [Uppbeat](https://uppbeat.io/blog/creator-news/instagram-has-updated-its-algorithm-to-reward-original-content-heres-how-to-make-the-most-of-it)
- Sources conflict on credit: one says a credit tag doesn't make a repost original. Planoly says reposts will carry labels crediting the original creator. No official Meta post was found. — [Sociallyin](https://sociallyin.com/blog/instagram-algorithm-update-repost/); [Planoly](https://planoly.com/blog/instagram-updates-its-original-content-policy)

**India personality rights**
- In 2025 the Delhi High Court granted a string of interim injunctions against unauthorised commercial use of a person's name, image or likeness, including AI deepfakes and fake merchandise: Aishwarya Rai Bachchan (Sept 2025), Abhishek Bachchan (10 Sept 2025), Nagarjuna (25 Sept 2025), Jaya Bachchan (Nov 2025), R. Madhavan (22 Dec 2025). — [Ada Derana](https://www.adaderana.lk/news/112404/delhi-high-court-rules-against-unauthorised-use-of-aishwarya-rais-name-photos); [Storyboard18, Nagarjuna](https://www.storyboard18.com/brand-makers/delhi-hc-protects-actor-nagarjunas-personality-rights-81873.htm); [Storyboard18, Jaya Bachchan](https://www.storyboard18.com/brand-makers/delhi-hc-backs-jaya-bachchan-in-fight-against-ai-misuse-and-fake-merch-protects-personality-rights-83939.htm); [Hogan Lovells tracker, Madhavan](https://digital-client-solutions.hoganlovells.com/resources/ai-litigation-case-law-tracker/case/ranganathan-madhavan-v-g-filmz-studioz/decision/43)
- In the Nagarjuna order, the court reasoned that unauthorised use "could mislead the public into assuming false endorsement or affiliation". False endorsement is the core harm. — [Storyboard18](https://www.storyboard18.com/brand-makers/delhi-hc-protects-actor-nagarjunas-personality-rights-81873.htm)

**ASCI influencer and endorsement rules**
- ASCI's influencer guidelines (posts from 14 Jun 2021) require prominent, hard-to-miss labels such as Ad, Advertisement, Sponsored, Collaboration, Partnership or Employee. Instagram's own "Sponsored" tag alone may not be enough. — [Nishith Desai](https://nishithdesai.com/research-and-articles/hotline/media-hotline/social-media-vs-reality-check-ascis-new-influencer-guidelines-4713); [National Law Review](https://natlawreview.com/article/social-media-vs-reality-check-asci-s-new-influencer-guidelines)
- A reported 2026 update (one secondary source, unverified) bans hiding disclosures in end-of-caption hashtag clusters and using #collab or #partnership without #Ad, and adds AI-influencer disclosure. — [Sansa Legal](https://www.sansalegal.com/post/asci-influencer-advertising-guidelines-2026-disclosure-rules-for-paid-content-and-ai-influencers)

### Inferences
- Celebrity cases set the precedent, but a well-known tech figure such as Cherny has an identifiable persona too. The risk rises sharply if his photo is used, if the ZeroAI pitch sits next to his face, or if the copy says "Boris uses / recommends ZeroAI".
- Safer practice for ZeroAI:
  - Use names and companies as plain text only. No Anthropic or Meta logos, and no company brand colours in a way that suggests a co-brand.
  - Avoid the person's photo, or use it only inside an official embed or link of their own post.
  - Re-typeset the content in your own design with commentary ("why this matters", "how to try it") rather than a raw screenshot. This helps with copyright and Instagram originality.
  - Link the original in the caption: "Source: @handle on X, [date], link".
  - Do not use the person's name or company as hashtags (the Align case).
  - Do not alter quotes.
  - Ideally, ask the engineer by DM before using a screenshot.
- Because ZeroAI is promoting its own product, the post is a brand ad. Disclosure is about ZeroAI's own brand voice, not a paid influencer. If any creator is paid to post the carousel, ASCI #Ad rules apply.
- Suggested wording for the ZeroAI slide:
  - "Our pick, not his: if you're juggling [Reclaim/Motion]-style scheduling, ZeroAI is an alternative we build. [Name] and [Company] are not affiliated with ZeroAI and don't endorse it."
  - Put a visual break (a "From the ZeroAI team" header and different slide styling) between the engineer's content and the pitch.
  - Never say "the tool Anthropic engineers use".

### Gaps
- Could not fetch the X Display Requirements, the ASCI Code or Meta's announcement in full. Wording above is from search summaries.
- No Indian case found on a non-celebrity professional's personality rights in a social post, or on brands quoting an engineer's public post.
- No authoritative source on whether X's developer display terms apply to screenshots reposted on other platforms.

## 4. Comparison and "alternative to [Reclaim/Motion]" claims

### Takeaway
In India, both ASCI Chapter IV and the Trade Marks Act (s.30(1), "honest practices") allow naming a competitor in a comparison. The comparison must be factual and capable of substantiation, must not mislead, must not create an artificial advantage, and must not denigrate. "ZeroAI is an alternative to X" is low risk if it is true and neutral. Claims like "better than", "cheaper" or "10x faster" need evidence.

### Cited Findings
- ASCI Chapter IV allows ads that compare with or name competitors, provided the compared aspects are clearly stated, the comparison is factual, accurate and capable of substantiation, consumers are not misled, the comparison is not chosen to give an artificial advantage or suggest a better bargain than is actually offered, and the ad does not denigrate, attack or discredit competitors directly or by implication. — [Lakshmikumaran & Sridharan](https://lakshmisri.com/insights/articles/comparative-advertising-acceptable-competitive-behaviour-and-law-of-disparagement); [S.S. Rana](https://ssrana.in/articles/legality-comparative-advertisements-in-india/); [Lexforti](https://lexforti.com/legal-news/comparative-advertising-balancing-manufacturer-vis-a-vis-consumer-interest/)
- ASCI CEO Manisha Kapoor is quoted as saying advertisers may name competitors if the comparison is fair, factual, substantiable, and neither misleading nor disparaging. — [exchange4media](https://www.exchange4media.com/marketing-news/call-out-culture-in-advertising-the-new-marketing-shortcut-or-a-risky-gamble-158409.html)
- Indian courts allow puffery ("my product is the best") but not disparagement of a rival's product, judged by an average consumer who "can read between the lines" (PepsiCo v Hindustan Coca-Cola; Pepsodent v Colgate). — [iPleaders](https://blog.ipleaders.in/the-legality-of-comparative-advertisement-and-product-disparagement-in-india/); [Lexforti](https://lexforti.com/legal-news/comparative-advertising-balancing-manufacturer-vis-a-vis-consumer-interest/)
- In the US, accurate comparative and compatibility references to a competitor's mark are generally allowed under nominative fair use. Using a competitor's marks as hashtags to promote your own product has been held to go too far. — [National Law Review](https://natlawreview.com/node/7273/printable/pdf); [Hunton](https://www.hunton.com/hunton-retail-law-resource/district-court-finds-use-of-third-party-hashtags-created-implied-association)

### Inferences
- Safe pattern: "Use [Motion/Reclaim]? ZeroAI is an alternative for [specific job]. Compare: [feature A], [feature B], [price as of date]." Every stated fact should have a dated source on file. Use competitor names in text only, without logos.
- Avoid: "Motion is overpriced/bloated", "better than Reclaim" without test data, and any implication that the engineer swapped their tool for ZeroAI.
- The engineer may not have mentioned a productivity tool at all (Cherny's list is Claude Code, tmux and similar). Framing ZeroAI as an "alternative to the tool he uses" could then misstate facts. Only name a tool the source actually named.

### Gaps
- Full current ASCI Code Chapter IV text not fetched (ascionline.in not reached). The conditions above come from law-firm summaries, some dated (2015).
- No ASCI complaint decisions found on software or SaaS "alternative to" claims specifically.
