# Anthropic engineers' public Claude Code setups (fact base for "Anthropic engineer reveals his Claude Code setup" carousels)

Research date: 2026-10-15. How I checked: Boris Cherny's thread text is VERIFIED word for word from Thread Reader App unrolls (threadreaderapp.com mirrors the X posts; x.com would not load from this environment). The view, like and repost numbers come from the public fxtwitter API (api.fxtwitter.com) on 2026-10-15. They are lifetime totals as of that day, not totals at the time of posting. Anything I took from secondary sources is marked REPORTED.

## 1. What exactly did Boris Cherny list in his January 2026 setup thread?

### Takeaway
Boris Cherny (creator and head of Claude Code, Anthropic) posted a 13-tip "my setup" thread on **2 Jan 2026**. It is the original "Claude Code creator reveals his setup" post. He followed it with a 10-tip "how the Claude Code team uses it" thread on **31 Jan 2026**, a 15-tip "hidden features" thread on **30 Mar 2026**, and a 6-tip Opus 4.7 thread on **16 Apr 2026**. Each one works as a ready-made carousel, and each has between 1.6M and 9.2M views.

### Cited Findings

**Person:** Boris Cherny, creator and Head of Claude Code at Anthropic. Lenny's Podcast describes him as "the creator and head of Claude Code at Anthropic" — [Lenny's Newsletter](https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens). X handle: @bcherny.

#### Thread A: "my setup" (VERIFIED text)
- URL: https://x.com/bcherny/status/2007179832300581177 (unrolled: [Thread Reader](https://threadreaderapp.com/thread/2007179832300581177.html))
- Date: Fri 2 Jan 2026, 19:58 UTC.
- Stats (fxtwitter API, as of 15 Oct 2026), first tweet: **8,233,176 views, 54,207 likes, 6,937 reposts, 1,307 replies, 102,933 bookmarks**. Tweet 1/ alone had 1.195M views and 3,202 likes — [fxtwitter API](https://api.fxtwitter.com/bcherny/status/2007179832300581177)
- Opening quote: "I'm Boris and I created Claude Code. Lots of people have asked how I use Claude Code, so I wanted to show off my setup a bit. My setup might be surprisingly vanilla! Claude Code works great out of the box, so I personally don't customize it much." … "Each person on the Claude Code team uses it very differently." — [Thread Reader](https://threadreaderapp.com/thread/2007179832300581177.html)
- The 13 items, quoted exactly — [Thread Reader](https://threadreaderapp.com/thread/2007179832300581177.html):
  1. **5 parallel Claudes in the terminal, numbered tabs and system notifications:** "I run 5 Claudes in parallel in my terminal. I number my tabs 1-5, and use system notifications to know when a Claude needs input." He links the docs section "iterm-2-system-notifications", which suggests **iTerm2**. He does not name his terminal anywhere in the thread, so treat iTerm2 as an inference.
  2. **5–10 more on the web, plus the phone:** "I also run 5-10 Claudes on claude.ai/code, in parallel with my local Claudes… I will often hand off local sessions to web (using &), or manually kick off sessions in Chrome, and sometimes I will --teleport back and forth. I also start a few sessions from my phone (from the Claude iOS app) every morning and throughout the day, and check in on them later." (Morning-routine habit.)
  3. **Model:** "I use Opus 4.5 with thinking for everything. It's the best coding model I've ever used, and even though it's bigger & slower than Sonnet, since you have to steer it less and it's better at tool use, it is almost always faster than using a smaller model in the end."
  4. **Shared CLAUDE.md:** "Our team shares a single CLAUDE.md for the Claude Code repo. We check it into git, and the whole team contributes multiple times a week. Anytime we see Claude do something incorrectly we add it to the CLAUDE.md, so Claude knows not to do it next time."
  5. **@.claude in code review:** "During code review, I will often tag @.claude on my coworkers' PRs to add something to the CLAUDE.md as part of the PR. We use the Claude Code Github action (/install-github-action)… It's our version of @danshipper's Compounding Engineering."
  6. **Plan mode:** "Most sessions start in Plan mode (shift+tab twice)… go back and forth with Claude until I like its plan. From there, I switch into auto-accept edits mode and Claude can usually 1-shot it. A good plan is really important!"
  7. **Slash commands:** "I use slash commands for every 'inner loop' workflow that I end up doing many times a day… Commands are checked into git and live in .claude/commands/. For example, Claude and I use a /commit-push-pr slash command dozens of times every day."
  8. **Subagents:** "code-simplifier simplifies the code after Claude is done working, verify-app has detailed instructions for testing Claude Code end to end."
  9. **Hook:** "We use a PostToolUse hook to format Claude's code… the hook handles the last 10% to avoid formatting errors in CI later." InfoQ shows the command as `bun run format || true` — [InfoQ](https://www.infoq.com/news/2026/01/claude-code-creator-workflow/).
  10. **Permissions:** "I don't use --dangerously-skip-permissions. Instead, I use /permissions to pre-allow common bash commands that I know are safe… Most of these are checked into .claude/settings.json and shared with the team."
  11. **Tools via MCP and CLI:** "Claude Code uses all my tools for me. It often searches and posts to Slack (via the MCP server), runs BigQuery queries… (using bq CLI), grabs error logs from Sentry, etc. The Slack MCP configuration is checked into our .mcp.json."
  12. **Long-running tasks:** a background agent to verify, "an agent Stop hook", or "the ralph-wiggum plugin (originally dreamt up by @GeoffreyHuntley)". He also uses "--permission-mode=dontAsk or --dangerously-skip-permissions in a sandbox… so Claude can cook without being blocked on me."
  13. **Verification (his "most important" tip):** "give Claude a way to verify its work. If Claude has that feedback loop, it will 2-3x the quality of the final result. Claude tests every single change I land to claude.ai/code using the Claude Chrome extension."
- Clarifications he gave in replies, as summarized by InfoQ (REPORTED, with the reply-tweet links InfoQ cites): each local session uses "its own git checkout, rather than branches or worktrees"; "10-20% of those sessions are abandoned due to unexpected scenarios"; the team's CLAUDE.md "is 2.5k tokens" — [InfoQ, 10 Jan 2026, Sergio De Simone](https://www.infoq.com/news/2026/01/claude-code-creator-workflow/)

#### Thread B: "tips sourced directly from the Claude Code team" (VERIFIED text)
- URL: https://x.com/bcherny/status/2017742741636321619 ([Thread Reader](https://threadreaderapp.com/thread/2017742741636321619.html))
- Date: Sat 31 Jan 2026, 23:32 UTC. Stats: **9,245,889 views, 50,347 likes, 5,752 reposts, ~102k bookmarks** — [fxtwitter API](https://api.fxtwitter.com/bcherny/status/2017742741636321619)
- Key items, quoted exactly:
  - Parallel worktrees: "Spin up 3–5 git worktrees at once, each running its own Claude session in parallel. It's the single biggest productivity unlock, and the top tip from the team. Personally, I use multiple git checkouts." Some teammates use "shell aliases (za, zb, zc) so they can hop between them in one keystroke"; others keep "a dedicated 'analysis' worktree".
  - Plan mode: "Start every complex task in plan mode. Pour your energy into the plan so Claude can 1-shot the implementation." One teammate has "a second Claude to review it as a staff engineer"; another says "the moment something goes sideways… switch back to plan mode and re-plan."
  - CLAUDE.md: "After every correction, end with: 'Update your CLAUDE.md so you don't make that mistake again.' Claude is eerily good at writing rules for itself." One engineer keeps "a notes directory for every task/project, updated after every PR." (Notes habit.)
  - Skills: "If you do something more than once a day, turn it into a skill or command"; "a /techdebt slash command… at the end of every session"; "a slash command that syncs 7 days of Slack, GDrive, Asana, and GitHub into one context dump." (A weekly catch-up / context habit.)
  - Bugs: "Enable the Slack MCP, then paste a Slack bug thread into Claude and just say 'fix.' **Zero context switching required.**"
  - Prompting: "Grill me on these changes and don't make a PR until I pass your test"; "Knowing everything you know now, scrap this and implement the elegant solution."
  - **Terminal:** "The team loves **Ghostty**! Multiple people like its synchronized rendering, 24-bit color, and proper unicode support." Also "/statusline to… always show context usage and current git branch", "color-code and name our terminal tabs, sometimes using **tmux** — one tab per task/worktree", and "Use **voice dictation**. You speak 3x faster than you type… (hit fn x2 on macOS)."
  - Subagents: "Append 'use subagents' to any request"; "Route permission requests to Opus 4.5 via a hook."
  - Data: "We have a BigQuery skill… Personally, I haven't written a line of SQL in 6+ months."
  - Learning: "Explanatory" / "Learning" output style; HTML slide presentations; ASCII diagrams; "a spaced-repetition learning skill."

#### Thread C: "favorite hidden and under-utilized features" (VERIFIED text)
- URL: https://x.com/bcherny/status/2038454336355999749 ([Thread Reader](https://threadreaderapp.com/thread/2038454336355999749.html))
- Date: Mon 30 Mar 2026, 03:12 UTC. Stats: **3,986,360 views, 22,991 likes, 2,478 reposts, 51,163 bookmarks** — [fxtwitter API](https://api.fxtwitter.com/bcherny/status/2038454336355999749)
- Key quotes:
  - Mobile: "Personally, I write a lot of my code from the iOS app. It's a convenient way to make changes without opening a laptop."
  - Remote control: "I have 'Enable Remote Control for all sessions' set in my /config."
  - Loops: "/loop 5m /babysit, to auto-address code review, auto-rebase, and shepherd my PRs to production"; "/loop 30m /slack-feedback"; "/loop /post-merge-sweeper"; "/loop 1h /pr-pruner."
  - Hooks: SessionStart to load context; PreToolUse to log bash; "Route permission prompts to WhatsApp for you to approve/deny (PermissionRequest)"; a Stop hook to "Poke Claude to keep going."
  - **Cowork Dispatch (an inbox/email habit):** "I use Dispatch every day to catch up on Slack and emails, manage files, and do things on my laptop when I'm not at a computer. When I'm not coding, I'm dispatching."
  - Chrome extension: "I use the Chrome extension every time I work on web code."
  - /btw: "I use this all the time to answer quick questions while the agent works."
  - Worktrees: "I have dozens of Claudes running at all times, and this is how I do it." (`claude -w`)
  - **Voice:** "Fun fact: I do most of my coding by speaking to Claude, rather than typing." (/voice, then hold space)
  - Also: /branch to fork a session, /batch, --bare, --add-dir, --agent.

#### Thread D: Opus 4.7 tips (VERIFIED text; includes the clearest focus quotes)
- URL: https://x.com/bcherny/status/2044847848035156457 ([Thread Reader](https://threadreaderapp.com/thread/2044847848035156457.html))
- Date: Thu 16 Apr 2026. Stats: **1,660,444 views, 11,705 likes, 1,043 reposts** — [fxtwitter API](https://api.fxtwitter.com/bcherny/status/2044847848035156457)
- Quotes:
  - Auto mode: "no more babysitting while the model runs… you can run more Claudes in parallel. **Once a Claude is cooking, you can switch focus to the next Claude.**"
  - /fewer-permission-prompts skill.
  - Recaps: "Very useful when returning to a long-running session after a few minutes or a few hours."
  - **Focus mode:** "I've been loving the new focus mode in the CLI, which hides all the intermediate work to just focus on the final result… I just look at the final result. /focus to toggle on/off."
  - Effort: "Personally, I use xhigh effort for most tasks, and max effort for the hardest tasks."
  - /go skill: "many of my prompts these days look like 'Claude do blah blah /go'." /go has Claude test end to end, run /simplify, and put up a PR.

#### Other Boris posts
- 21 Feb 2026, built-in git worktree support: 1.31M views, 10,894 likes — [Thread Reader](https://threadreaderapp.com/thread/2025007393290272904.html), [fxtwitter](https://api.fxtwitter.com/bcherny/status/2025007393290272904)
- 28 Feb 2026, the /simplify and /batch skills ("I have been using both daily"): 2.54M views, 12,787 likes — [Thread Reader](https://threadreaderapp.com/thread/2027534984534544489.html)
- 11 Feb 2026, a customizability thread (hooks, plugins, LSPs, MCPs, skills, status lines, output styles): 596K views — [Thread Reader](https://threadreaderapp.com/thread/2021699851499798911.html)
- 13 Jan 2026, an origin story: he says he used the early CLI "as a note taker mostly" before using it for git — [Thread Reader](https://threadreaderapp.com/thread/2010923222813065308.html)
- Lenny's Podcast, "Head of Claude Code: What happens after coding is solved", **19 Feb 2026**, 1:27:44 long (YouTube We7BZVKbCVw). The show notes list "Practical tips for getting the most out of Claude Code and Cowork" and say Claude Code reached "4% of public GitHub commits" — [Lenny's Newsletter](https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens)
- Every's "AI & I" podcast with Cat Wu and Boris Cherny, **29 Oct 2025**. Timestamps: "Boris and Cat's favorite slash commands: 00:14:06"; "How Boris uses Claude Code to plan feature development: 00:15:49"; "sub-agents: 00:21:53" — [Every](https://every.to/podcast/how-to-use-claude-code-like-the-people-who-built-it), [transcript page](https://elevenreader.io/audiobooks/transcript-how-to-use-claude-code-like-the-people-who-built-it-audiobook/yf2WG4cgRH3oSbXqiCXp)

### Inferences
- Best carousel numbers to use: "5 Claudes in terminal + 5–10 on web", "Opus with thinking for everything", "/commit-push-pr dozens of times a day", "2–3x quality from verification", and later "dozens of Claudes running at all times".
- His setup changed over 2026: numbered iTerm-style tabs and notifications (January), then the phone, voice and /loop (March), then auto mode, /focus and xhigh effort (April). A "then vs now" carousel would be accurate.
- Thread B is about the **team's** habits, not only Boris's. Ghostty, tmux, voice dictation and the za/zb/zc aliases come from teammates, so the carousel should label them that way.

### Gaps
- Boris never names his own terminal app in Thread A. iTerm2 is only implied by the docs link.
- YouTube pages were bot-blocked from this environment, so I have no timestamps for Boris's Lenny episode.
- The stats are lifetime figures as of Oct 2026. I could not get the counts at the time each thread went viral. A third-party blog reported 8.5M views, 49K likes and 6.4K reposts for Thread B at some earlier point (REPORTED) — [jitendrazaa.com](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/)

## 2. What setups, tools and habits did other Anthropic staff share?

### Takeaway
Cat Wu (Head of Product, Claude Code and Cowork) and Thariq Shihipar (Claude Code engineer) share the most specific personal habits, mostly on podcasts and conference stages rather than in X threads. Anthropic's official July 2025 report adds team-level habits, such as the "slot machine" approach and the checkpoint-heavy workflow.

### Cited Findings

**Cat Wu, Head of Product for Claude Code and Cowork, Anthropic** (X @_catwu)
- Lenny's Podcast, "How Anthropic's product team moves faster than anyone else", **23 Apr 2026**, YouTube PplmzlgE0kg. Topics include "Cat's most underrated AI skill: asking the model to introspect on its own mistakes" and "Why 'just do things' is the most important principle" — [Lenny's Newsletter](https://www.lennysnewsletter.com/p/how-anthropics-product-team-moves)
- REPORTED: Anthropic cut feature timelines through an "evergreen launch room" and ships rough versions labeled "research previews" — [SignalCast summary](https://www.signalcast.app/episode/lennys-podcast/how-anthropics-product-team-moves-faster-than-anyone-else-cat-wu-head-of-product-claude-code)
- AI Engineer World's Fair fireside chat with Simon Willison (writeup dated **21 Jul 2026**; video uU5Gv2h8-9g, about 12:54) — [Simon Willison](https://simonwillison.net/2026/Jul/21/cat-and-thariq/):
  - Her mobile habit: "I just kick off the task directly on mobile and it runs in a cloud session without using my local environment."
  - The team's evening habit she describes: people "plug their laptop into a power charger, open a bunch of remote control sessions, lock the screen, and then use their mobile phone from their couch to control Claude Code."
  - **Calendar/async quote:** "let's automate figuring out our whole launch calendar, let's automate getting those status updates asynchronously so we're not bugging people."
  - "Broadly within Anthropic, almost every single person uses auto mode."
  - Personal use: a climbing-log app, plus Claude "workflows" for researching travel and team offsites, including filtering climbs by a "very short approach."
- REPORTED (secondary blog, not verified against a primary source): she recommends Plan Mode before code changes, keeping testing instructions in CLAUDE.md, and `/rename [label]` to name each session when running several — [Vibe Coder Blog](https://blog.vibecoder.me/multi-claude-parallel-agents-anthropic-workflow)

**Thariq Shihipar, engineer on Anthropic's Claude Code team** (X @trq212)
- How I AI (Lenny's Podcast Network), "HTML is the new Markdown", **18 May 2026**, recorded at Code with Claude, YouTube Qrpm7E80wQ0 — [Lenny's Newsletter](https://www.lennysnewsletter.com/p/how-i-ai-html-is-the-new-markdown):
  - Uses HTML artifacts instead of Markdown for plans, specs, throwaway micro-apps and a "living design system".
  - His prompt: "Create an HTML file with a plan. Help me visualize. Include excerpts, mockups, code, whatever is needed to give me maximum context."
  - "Only about 1% of the tokens Thariq generates go into production code." The rest go into "dashboards, custom interfaces, weekly status updates." (Episode summary, paraphrased)
  - "Thariq sends his manager weekly HTML status updates because they're more likely to actually get read." (summary)
  - Engineers are becoming "compute allocators".
- Behind the Craft (Peter Yang), "How I Plan, Build, and Run Loops with Claude Code in 40 Minutes", **19 Jul 2026**, YouTube aVO6E181cNU. Timestamps: /goal loops at 00:00; "Plan by removing unknowns" at 08:17 (t=497s); HTML planning at 14:32; "Running parallel Claude tasks through Slack" at 18:35; creator and verifier subagents at 27:34; **"How Thariq stays focused while Claude works in parallel" at 31:08 (https://www.youtube.com/watch?v=aVO6E181cNU&t=1868s)**; system prompt cut by 80% at 34:07 — [creatoreconomy.so](https://creatoreconomy.so/p/how-i-plan-build-and-run-loops-with-claude-code-thariq-shihipar)
  - Host takeaway: "Use /goal only if you have a verifiable finish line"; "he actually reads the plan manually instead of just trusting AI."
- At the AIE fireside: "I don't even remember pressing yes and allow" (auto mode). He is building a 2D Street Fighter-style game featuring himself, where Claude Code prompts Gemini and Seedance for animations and checks the frames — [Simon Willison](https://simonwillison.net/2026/Jul/21/cat-and-thariq/)
- 18 Sep 2026: announced AGENTS.md support (v2.1.277) through Claude Code "mods" — [Simon Willison](https://simonwillison.net/tags/thariq-shihipar/)

**Anthropic official sources**
- "How Anthropic teams use Claude Code", **24 Jul 2025** (datePublished in page metadata) — [Anthropic](https://www.anthropic.com/news/how-anthropic-teams-use-claude-code). Covers Product Engineering's "first stop" for any programming task; Security Engineering's TDD loop and 3x faster incident tracing; the Product Design team's Figma-to-autonomous loops; Growth Marketing's two sub-agents generating hundreds of ads; Legal's phone-tree prototype; and Inference's 80% reduction in research time.
- The companion 23-page PDF report (created June 2025) — [Anthropic PDF](https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf):
  - Data Science/ML: "Treat it like a slot machine. Save your state before letting Claude work, let it run for 30 minutes, then either accept the result or start fresh."
  - "Use a checkpoint-heavy workflow. Regularly commit your work."
  - Claude Code team: "auto-accept mode (shift+tab)" for prototyping at the product's edges, with "synchronous supervision" for core logic.
  - "multiple instances of Claude Code in different repositories" for parallel tasks.
  - Asking Claude directly instead of "waiting for Slack responses… saving significant time in context switching."
- "Claude Code: Best practices for agentic coding" was originally an Anthropic Engineering post (anthropic.com/engineering/claude-code-best-practices). That URL now redirects to the docs page "Best practices for Claude Code", which says it covers "patterns that have proven effective across Anthropic's internal teams". It covers plan mode (Shift+Tab), "If you could describe the diff in one sentence, skip the plan", parallel sessions through worktrees, the Desktop app, agent teams, and /batch across "5 to 30 subagents" — [Claude Code Docs](https://www.anthropic.com/engineering/claude-code-best-practices)
- Official docs on notifications: desktop notifications work by default in Ghostty, Kitty and iTerm2 (REPORTED through a search snippet) — [code.claude.com terminal-config](https://code.claude.com/docs/en/terminal-config.md)

### Inferences
- Cat and Thariq work well as carousel subjects 2 and 3. Cat fits "the PM who codes from her phone and automates the launch calendar"; Thariq fits "the engineer who replaced Markdown with HTML, where 1% of tokens ship."
- The "slot machine, 30 minutes" tip is a short, memorable habit that comes straight from Anthropic's own team.

### Gaps
- I found no written "my setup" thread from Cat Wu or Thariq; their material is in podcasts and talks. Paywalls (Lenny, Every, Behind the Craft) and YouTube's bot block kept me from reading full transcripts.
- I could not verify setup posts by other team members (for example Lydia Hallie, Ado Kukic, Sid Bidasaria or Adam Wolff); my search found nothing citable.
- I could not confirm the original publish date and author line of the Engineering best-practices post, because it now redirects. From memory (UNVERIFIED): April 2025, by Boris Cherny.

## 3. Did any of them mention focus/deep work, context switching, notifications, calendar or meeting habits?

### Takeaway
Yes, but the habits are about managing agents, not classic calendar routines. Notifications to know when a Claude needs input, "switch focus to the next Claude", the /focus mode, "zero context switching", async status updates, an automated launch calendar, and starting sessions from the phone every morning all appear. No one shared calendar-blocking or meeting rules.

### Cited Findings
- "use system notifications to know when a Claude needs input" (Boris, 2 Jan 2026) — [Thread Reader](https://threadreaderapp.com/thread/2007179832300581177.html)
- "I also start a few sessions from my phone… every morning and throughout the day, and check in on them later" (Boris) — [Thread Reader](https://threadreaderapp.com/thread/2007179832300581177.html)
- "Once a Claude is cooking, you can switch focus to the next Claude" and the /focus mode (Boris, 16 Apr 2026) — [Thread Reader](https://threadreaderapp.com/thread/2044847848035156457.html)
- "Zero context switching required" (Slack MCP plus "fix"); a 7-day Slack/GDrive/Asana/GitHub context-dump command; a per-project notes directory (Claude Code team, 31 Jan 2026) — [Thread Reader](https://threadreaderapp.com/thread/2017742741636321619.html)
- "I use Dispatch every day to catch up on Slack and emails… When I'm not coding, I'm dispatching" (Boris, 30 Mar 2026) — [Thread Reader](https://threadreaderapp.com/thread/2038454336355999749.html)
- Permission prompts routed to WhatsApp with a PermissionRequest hook (Boris) — [Thread Reader](https://threadreaderapp.com/thread/2038454336355999749.html)
- Cat Wu: "automate figuring out our whole launch calendar… status updates asynchronously so we're not bugging people" — [Simon Willison](https://simonwillison.net/2026/Jul/21/cat-and-thariq/)
- Thariq: a segment titled "How Thariq stays focused while Claude works in parallel" at 31:08 — [creatoreconomy.so](https://creatoreconomy.so/p/how-i-plan-build-and-run-loops-with-claude-code-thariq-shihipar). I could not read what he said, because the post is paywalled and YouTube was blocked.
- Anthropic report: asking Claude instead of waiting on Slack saves "significant time in context switching" — [Anthropic PDF](https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf)

### Inferences
- The strongest focus/productivity angle for a carousel: "The creator of Claude Code doesn't babysit AI. He numbers his tabs, lets notifications pull him back, and switches focus to the next Claude."

### Gaps
- None of the sources mention Raycast, a calendar app, a notes app (Notion, Obsidian and so on), or meeting-free blocks. Do not attribute these to anyone.
- I don't know the content of Thariq's "stays focused" segment.

## 4. How did these posts perform, and how were they covered?

### Takeaway
Boris's January threads are among the most-viewed developer posts of 2026, with about 8.2M and 9.2M views and about 100K bookmarks each. VentureBeat, InfoQ and Slashdot covered the first one within a week, and dozens of blogs and newsletters followed.

### Cited Findings
- Stats as of 15 Oct 2026 (fxtwitter API):

| Thread | Date | Views | Likes | Reposts | Bookmarks |
|---|---|---|---|---|---|
| A: "my setup" | 2 Jan 2026 | 8,233,176 | 54,207 | 6,937 | 102,933 |
| B: team tips | 31 Jan 2026 | 9,245,889 | 50,347 | 5,752 | 101,998 |
| C: hidden features | 30 Mar 2026 | 3,986,360 | 22,991 | 2,478 | 51,163 |
| D: Opus 4.7 tips | 16 Apr 2026 | 1,660,444 | 11,705 | 1,043 | 15,411 |

  Sources: [A](https://api.fxtwitter.com/bcherny/status/2007179832300581177), [B](https://api.fxtwitter.com/bcherny/status/2017742741636321619), [C](https://api.fxtwitter.com/bcherny/status/2038454336355999749), [D](https://api.fxtwitter.com/bcherny/status/2044847848035156457)
- VentureBeat, "The creator of Claude Code just revealed his workflow, and developers are losing their minds" (early January 2026). It says the community spent "the past week" dissecting the thread and that it became a "viral manifesto" (REPORTED through search snippets and Slashdot's excerpt; VentureBeat's own page would not load from here) — [VentureBeat](https://venturebeat.com/technology/the-creator-of-claude-code-just-revealed-his-workflow-and-developers-are), [Slashdot, 6 Jan 2026](https://developers.slashdot.org/story/26/01/06/2239243/creator-of-claude-code-reveals-his-workflow)
- Slashdot's framing: a "deceptively simple workflow that uses parallel AI agents, verification loops, and shared memory to let one developer operate with the output of an entire engineering team" — [Slashdot](https://developers.slashdot.org/story/26/01/06/2239243/creator-of-claude-code-reveals-his-workflow)
- InfoQ, "Inside the Development Workflow of Claude Code's Creator", by Sergio De Simone, 10 Jan 2026 — [InfoQ](https://www.infoq.com/news/2026/01/claude-code-creator-workflow/)
- Yahoo Tech and Business Insider-style coverage (REPORTED; the page would not load): it reportedly says the January post "had 8.1 million views" when published and quotes "surprisingly vanilla" — [Yahoo Tech](https://tech.yahoo.com/articles/claude-codes-creator-says-setup-091701435.html)
- Newsletter and blog coverage includes a Substack piece ([Karo Zieminski](https://karozieminski.substack.com/p/boris-cherny-claude-code-workflow)), a Korean breakdown on WikiDocs ([wikidocs](https://wikidocs.net/blog/@jaehong/8587/)), Towards AI ([pub.towardsai.net](https://pub.towardsai.net/claude-codes-creator-stopped-prompting-claude-he-writes-loops-and-merges-150-prs-from-his-phone-b096ba603c13)), and a "boris" skill on skills.sh packaging his workflow ([skills.sh](https://skills.sh/yldgio/vibe-grimoire/boris)).
- Podcast engagement on Substack (likes / comments / restacks shown on page): Boris Lenny episode 230/1/15; Cat Wu Lenny episode 212/2/22; Thariq How I AI 367/10 — [Lenny Boris](https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens), [Lenny Cat](https://www.lennysnewsletter.com/p/how-anthropics-product-team-moves), [How I AI](https://www.lennysnewsletter.com/p/how-i-ai-html-is-the-new-markdown)

### Inferences
- The bookmark-to-like ratio of about 2:1 on Threads A and B shows people saved them as references. That supports "save this post" calls to action on Instagram.
- The "creator reveals his setup" framing was already a media headline pattern (VentureBeat, Slashdot, Yahoo), so a carousel with that title follows proven framing.

### Gaps
- I could not verify a Hacker News thread or its points, because I did not search HN.
- The 8.1M figure in the Yahoo article and the VentureBeat article body could not be fetched (DNS/TLS failure), so their exact wording is unverified beyond the search snippets and Slashdot's excerpt.
- Wrong or doubtful claims seen in secondary sources: one blog (winzheng.com) said Boris uses tmux and Neovim. This contradicts his own thread, which says he uses separate git checkouts and does not name an editor. Do not use it.
