# Senior / famous engineers who publicly revealed their daily dev + productivity stack (2024–2026)

Research date: 2026-10-15. Labels used below:
- **VERIFIED**: I fetched the primary page myself and the quote is copied from it word for word.
- **REPORTED**: The claim comes from secondary coverage or a search snippet. The primary page was blocked or not fetched. Check it before quoting on a slide.

## Who has publicly named a calendar/focus/time-blocking/productivity tool alongside their dev tools?

### Takeaway
Out of the many people checked, 6 strong candidates remain and 2 weaker ones. The best fits for the carousel are **Mitchell Hashimoto** (Ghostty + Claude Code + a time-blocking habit), **Kent C. Dodds** (Cursor + Raycast + Notion Calendar), **Cassidy Williams** (Notion Calendar + Sukha focus app; she works at GitHub), **DHH** (Neovim/LazyVim + Omarchy + HEY Calendar), **Zack Proser** (Claude Code + Wispr Flow + Granola) and **Andrej Karpathy** (Cursor + Claude Code/Codex + one Apple Notes note). I found no current Meta, Google, Stripe, Netflix or Shopify IC engineer who publicly named a calendar or time-blocking app.

### Cited Findings

**1. Mitchell Hashimoto: co-founder of HashiCorp, creator of Ghostty (VERIFIED). Best fit.**
- Post "My AI Adoption Journey", dated **February 5, 2026** — [mitchellh.com](https://mitchellh.com/writing/my-ai-adoption-journey)
- Tool 1, Ghostty (his own terminal): "The command palette that ships for macOS in Ghostty…" He also uses examples from Ghostty throughout the post — [source](https://mitchellh.com/writing/my-ai-adoption-journey)
- Tool 2, Claude Code (and Amp): "The next phase on my journey I tried Claude Code. I'll cut to the chase: I initially wasn't impressed." He later mentions "Amp's deep mode (which is basically just GPT-5.2-Codex)" and "Modern coding models like Opus and Codex" — [source](https://mitchellh.com/writing/my-ai-adoption-journey)
- Tool 3 is a habit, not an app. It is time-blocking plus turning off notifications:
  - "Step 3: End-of-Day Agents … block out the last 30 minutes of every day to kick off one or more agents." — [source](https://mitchellh.com/writing/my-ai-adoption-journey)
  - "Very important at this stage: turn off agent desktop notifications. Context switching is very expensive. … Don't let the agent notify you." — [source](https://mitchellh.com/writing/my-ai-adoption-journey)
  - He also refers to working "in my own, normal, pre-AI deep thinking mode". — [source](https://mitchellh.com/writing/my-ai-adoption-journey)
- Disclosure in the post: "I don't work for, invest in, or advise any AI companies." — [source](https://mitchellh.com/writing/my-ai-adoption-journey)
- ZeroAI angle: he blocks deep-work time and the agent window by hand. ZeroAI books those blocks on Google Calendar automatically.

**2. Kent C. Dodds: ex-PayPal engineer, creator of EpicWeb/Testing JavaScript (VERIFIED). Page is undated.**
- His /uses page ("The tools Kent C. Dodds uses", kcd.im/uses). It has no date; I fetched it in Oct 2026, and it now lists Cursor, so it was updated in 2024 or later — [kentcdodds.com/uses](https://kentcdodds.com/uses)
- Tool 1, Cursor: "Cursor - My preferred editor." — [source](https://kentcdodds.com/uses)
- Tool 2, Raycast and Wispr Flow (the page lists "Raycast", "ScriptKit" and "Wispr Flow - Voice to text (AI)") — [source](https://kentcdodds.com/uses)
- Tool 3, Notion Calendar: "Notion Calendar - My calendar app and it allows me to share my availability with specific blocks of time." — [source](https://kentcdodds.com/uses)
- Caveat: he is now an independent educator, so a "senior engineer at [big company]" framing would mean using "ex-PayPal".

**3. Cassidy Williams: GitHub (VERIFIED quotes; job title REPORTED)**
- Post "The Productivity apps I use in 2024", dated **Jul 1, 2024** — [cassidoo.co](https://cassidoo.co/post/producivity-apps-2024/)
- Notion Calendar: "Notion Calendar is a keyboard shortcut-powered calendar app. I've been using it for a couple years now… It lets you quickly use keyboard commands to see your teammate's calendars, share availability, view multiple timezones, and create events." — [source](https://cassidoo.co/post/producivity-apps-2024/)
- Sukha, formerly Centered (a focus app): "when I use Sukha, I get more work done, simply put… Sukha is a flow state to-do app." — [source](https://cassidoo.co/post/producivity-apps-2024/)
- Obsidian: "I'm alllllll in on Obsidian." — [source](https://cassidoo.co/post/producivity-apps-2024/)
- Habit quote: "If something is scheduled on my calendar, whether it's flow time or dedicated time to one specific task, I follow it." — [source](https://cassidoo.co/post/producivity-apps-2024/)
- Caveat: the post leaves out dev tools on purpose ("This post will not cover my code editor(s), terminals, or other developer tools"). Tools 1 and 2 would need another source, for example her GitHub/VS Code content. — [source](https://cassidoo.co/post/producivity-apps-2024/)
- The 2023 version names "Cron" (now Notion Calendar) as "my current favorite" calendar, and Centered for focus. It also says she used Vimcal in the past — [cassidoo.co 2023](https://cassidoo.co/post/producivity-apps-2023/)
- She published a newer post, "best-ai-tools-sept-2026" (Sep 17, 2026). Its whole body is "It depends!", so it names no tools — [source](https://cassidoo.co/post/best-ai-tools-sept-2026/)
- Her role as Senior Director of Developer Advocacy at GitHub comes from my background knowledge, not from a page I fetched. Verify it on LinkedIn.

**4. DHH (David Heinemeier Hansson): creator of Ruby on Rails, CTO of 37signals (VERIFIED from his Omarchy manual)**
- His Omarchy manual says: "Omarchy ships with a complete Neovim setup that's been lovingly tuned… It's called LazyVim" — [Omarchy Manual: Neovim](https://learn.omacom.io/2/the-omarchy-manual/56/neovim)
- Default hotkeys in his distro: "Super + Shift + N — Neovim", "Super + Shift + C — Calendar (HEY)", "Super + Shift + E — Email (HEY)". There is also a `tdl <ai>` command to "Create dev layout with editor, AI, and terminal" — [Omarchy hotkeys](https://learn.omacom.io/2/the-omarchy-manual/53/hotkeys)
- The editor menu also offers VSCode, Cursor, Zed, Sublime and Helix — [Omarchy Dev Tools](https://learn.omacom.io/books/2/pages/62)
- HEY Calendar features include "Sometime this week" tasks, habit tracking, time tracking and a Journal — [hey.com/calendar](https://www.hey.com/calendar/)
- Caveat: this is the manual for his own Linux distro, and HEY is his own company's product. It is not a "my daily tools" interview. Frame it as "the setup DHH ships to developers". HEY Calendar being 37signals' product is a weak spot for a "switch to ZeroAI" pitch.

**5. Zack Proser: AI engineer and developer educator (VERIFIED quotes; employer not verified)**
- Post "My 2026 AI Engineer Setup", published **Feb 22, 2026** — [zackproser.com](https://zackproser.com/blog/2026-ai-engineer-setup)
- "The short version: Claude Code replaced Cursor. Granola replaced manual meeting notes. WisprFlow still runs everything." — [source](https://zackproser.com/blog/2026-ai-engineer-setup)
- Habit: "launch Claude Code agents on a task before leaving my desk, step outside, check agent progress on my phone…" — [source](https://zackproser.com/blog/2026-ai-engineer-setup)
- Caveat: the page has affiliate links for Wispr Flow and Granola. Granola is a meeting-notes tool, not a calendar tool. His employer is not stated on the page.

**6. Andrej Karpathy: OpenAI co-founder, ex-Tesla AI director (REPORTED; the primary pages were blocked)**
- In August 2025 he described a tiered workflow. Cursor tab-complete handles about 75% of his coding, followed by Claude Code and Codex for larger chunks, with GPT-5 Pro as "the last line of defense". This comes from secondary coverage of his X post, and I did not see the original tweet — [Analytics Vidhya](https://www.analyticsvidhya.com/blog/2025/08/llm-workflow-for-developers/); [Genbeta](https://www.genbeta.com/inteligencia-artificial/cofundador-openai-alucina-que-esta-pasando-programacion-ia-futuro-sera-tab-tab-tab)
- Productivity tool: his post "The append-and-review note" (about March 2025, date not verified) describes keeping one single note called "notes" in Apple Notes. New items go on top and he scrolls down to review. Cloudflare blocked the page, so this is from the search summary — [karpathy.bearblog.dev](https://karpathy.bearblog.dev/the-append-and-review-note/)
- Caveat: copy exact wording from the original X post and blog before quoting. Apple Notes is a to-do/notes system, not a calendar.

**7. Wes Bos: Syntax.fm co-host and educator (VERIFIED, but the page is old)**
- "I've always been a huge Alfred fan … but have recently switched over to Raycast which is even better!" — [wesbos.com/uses](https://wesbos.com/uses)
- "I use Things App with a GTD mindset for managing my tasks." — [source](https://wesbos.com/uses)
- Dev tools: VS Code and the Warp terminal ("I currently use Warp for my terminal") — [source](https://wesbos.com/uses)
- Caveat: the page is dated December 12, 2019 and is a "living document". It is not clearly from 2024–2026, and he does not work at a big company.

**8. Boris Cherny: creator of Claude Code at Anthropic (REPORTED; useful as a benchmark, but there is no tool 3)**
- He runs about 5 parallel Claude Code sessions in numbered terminal tabs, uses system notifications to know when a session needs input, and keeps a shared CLAUDE.md file. He called his setup "surprisingly vanilla" — [getpushtoprod](https://getpushtoprod.substack.com/p/how-the-creator-of-claude-code-actually); [karozieminski](https://karozieminski.substack.com/p/boris-cherny-claude-code-workflow)
- Note: he relies on notifications, which is the opposite of Mitchell Hashimoto's advice to turn them off. That disagreement could make a good contrast slide.

### Inferences
- The most authentic "tool 3" stories are **habits**: Mitchell's 30-minute end-of-day block with notifications off, and Cassidy's "If something is scheduled on my calendar… I follow it". ZeroAI automates exactly this, so a slide like "He blocks it by hand → ZeroAI books it for you" is honest framing.
- **Notion Calendar** is the calendar app that comes up most often among well-known developers (Kent C. Dodds, Cassidy Williams, and Miriam Suzanne on usesthis). It is the natural "tool 3" to position ZeroAI against. ZeroAI turns Slack/Jira/Linear asks into calendar blocks, and Notion Calendar does not do that.
- Ranking for carousels: (1) Hashimoto, (2) Kent C. Dodds, (3) Cassidy Williams, (4) DHH, (5) Zack Proser, (6) Karpathy, only after checking the originals. Wes Bos is a backup.
- Wording: "senior engineer at [company]" fits only some of them. Use "HashiCorp co-founder", "GitHub's Cassidy Williams", "ex-PayPal engineer Kent C. Dodds", "Rails creator DHH" and "OpenAI co-founder Karpathy" rather than inventing a title.

### Gaps
- I found no public statement from a current **Meta, Google, Stripe, Netflix, Shopify, Linear or Notion** individual-contributor engineer that names a calendar or time-blocking app such as Reclaim, Motion, Sunsama or Akiflow. One targeted search (Lenny's "How I AI" plus Reclaim/Motion/Granola) turned up nothing relevant.
- **Guillermo Rauch** (Vercel): no source found naming his calendar or productivity apps.
- I did not research **Pieter Levels, ThePrimeagen or Simon Willison** in depth because of time limits. None of them is known to name a calendar app, but this is unconfirmed.
- **Lee Robinson**: his site now says he works "on ML at SpaceX (formerly at Cursor)" — [leerob.com](https://leerob.com/uses). There is no /uses page any more, so his old stack cannot be cited.
- Primary quotes for Karpathy (X post and bearblog) and Boris Cherny (X/Threads) could not be fetched.

## Which "uses this" style pages list such stacks for senior engineers at big companies?

### Takeaway
Personal /uses pages are the most reliable source of exact quotes: Kent C. Dodds and Wes Bos, plus Cassidy Williams' yearly "productivity apps" posts. usesthis.com interviews from 2023–2026 are almost all indie developers, game developers or artists, not big-tech engineers.

### Cited Findings
- kentcdodds.com/uses lists Cursor, Raycast, Wispr Flow and Notion Calendar — [source](https://kentcdodds.com/uses)
- wesbos.com/uses lists VS Code, Warp, Raycast and Things — [source](https://wesbos.com/uses)
- cassidoo.co publishes a yearly "productivity apps" post (2022, 2023 and 2024 exist) — [2024](https://cassidoo.co/post/producivity-apps-2024/), [2023](https://cassidoo.co/post/producivity-apps-2023/)
- I scanned 60 usesthis.com interviews (about Apr 2023 to Sep 2026) for productivity tools. Matches include Miriam Suzanne, "Artist, author, web developer" (Sep 21, 2024), who mentions Notion Calendar/Cron and Obsidian, and Izzy Muerte, "Software engineer (C++)" (Jan 27, 2025), who mentions Todoist and Obsidian. None of the people interviewed is a senior engineer at a well-known big tech company. [usesthis.com/interviews/miriam.suzanne](https://usesthis.com/interviews/miriam.suzanne/); [usesthis.com/interviews/izzy.muerte](https://usesthis.com/interviews/izzy.muerte/)
- The usesthis interview with Casey Liss (June 30, 2026; "Developer, podcaster, writer") mentions Claude Code. I did not extract quotes from it — [usesthis.com/interviews/casey.liss](https://usesthis.com/interviews/casey.liss/)
- These /uses pages returned 404 in Oct 2026: cassidoo.co, addyosmani.com, swyx.io, joshwcomeau.com, una.im, rauchg.com, mattpocock.com, t3.gg, jakearchibald.com, brittanychiang.com (I tested them myself with curl).

### Inferences
- uses.tech is a directory that links to pages like these. Big-company engineers seldom keep /uses pages. Developer educators and founders do, so carousels will lean on "famous engineer" framing more than "Meta/Google engineer" framing.

### Gaps
- I did not crawl the uses.tech directory itself, so there may be big-tech engineers listed there whom I missed.
- I did not extract exact quotes from the Miriam Suzanne and Izzy Muerte interviews, only keyword matches.

## Any viral "engineer at Meta/Google reveals setup" posts and how they performed?

### Takeaway
The best-documented viral "setup reveal" is Boris Cherny's Claude Code workflow thread from January 2026, at a reported 8–8.5M views. Its key point was that the setup was "surprisingly vanilla". I did not verify view counts for Instagram/TikTok "Meta/Google engineer reveals setup" posts.

### Cited Findings
- Secondary sources say the thread reached about 8.5M views, about 49K likes and about 6.4K reposts (Jan 31, 2026 thread). Another source gives about 8M views for a Jan 2, 2026 Threads post. The sources disagree on which post went viral — [jitendrazaa.com](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/); [Yahoo Tech](https://tech.yahoo.com/articles/claude-codes-creator-says-setup-091701435.html)
- Commentators called the reaction a "watershed moment" because the setup was so simple — [karozieminski](https://karozieminski.substack.com/p/boris-cherny-claude-code-workflow)
- Coverage of Karpathy's August 2025 workflow post spread to Chinese, Spanish and German outlets, which suggests it reached a large audience — [Wallstreetcn](https://wallstreetcn.com/articles/3754010); [Genbeta](https://www.genbeta.com/inteligencia-artificial/cofundador-openai-alucina-que-esta-pasando-programacion-ia-futuro-sera-tab-tab-tab)

### Inferences
- The hook that performs is "a famous builder's surprisingly simple stack" plus a concrete habit. That supports a 3-tool format where tool 3 is a habit or focus tool.

### Gaps
- I did not search Instagram or TikTok for "Meta engineer / Google engineer reveals setup" creator posts or their performance numbers, because of the time budget.
- View counts for the Cherny thread come only from secondary sources and need checking on X directly.
