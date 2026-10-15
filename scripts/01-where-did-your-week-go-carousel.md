# Script 1 — "Where did your week go?" (Carousel)

**Format:** Instagram carousel, 10 slides, 1080×1350 (4:5)
**Goal:** Saves + shares. Real value first (a DIY audit), ZeroAI only on slide 9.
**Big idea:** It's not you. It's your calendar.
**Note:** The week shown is an EXAMPLE. Label it "example week" on slide 1 so nobody thinks it is real user data.

---

## Design notes (for Claude Design)

- Look: a developer's screen, not an ad. Dark editor-style background, one accent colour for "focus time" (green) and one for "meetings" (red/orange).
- Font: one clean sans-serif for headlines, one monospace for numbers and labels.
- Max ~20 words per slide. Big text. One idea per slide.
- Same layout every slide: small label top-left (`week_audit.log`), slide number top-right (`3/10`).
- Small source line at the bottom of every stat slide.

---

## Slides

| # | Text on slide | Visual |
|---|---|---|
| 1 | **Where did your week go?** <br> I audited a developer's calendar. (example week) → | A full Mon–Fri calendar packed with red meeting blocks. Tiny grey gaps between them. |
| 2 | **Monday** <br> 10:00 standup · 11:30 sync · 2:00 "quick call" · 4:30 client call <br> **Longest free block: 1h 10m** | Monday column zoomed in. Free gaps highlighted with a dotted outline. |
| 3 | **The full week (40 hours)** <br> Meetings + quick calls: 12h <br> Free, but in gaps under 1 hour: 16h <br> Free in 1–2 hour gaps: 8h <br> **Free in 2+ hour blocks: 4h** | Horizontal bar split into 4 colours. The 4h green part is tiny. |
| 4 | **16 hours of "free" time.** <br> But nobody writes good code in 30-minute pieces. | Many small grey squares scattered like confetti. |
| 5 | **Why small gaps don't work** <br> After an interruption, it took about 23 minutes on average to get back to the task. <br> *Source: Gloria Mark, UC Irvine (via Gallup)* | A simple timer graphic: "ping" → 23 min → "back to code". |
| 6 | **You're not alone** <br> Half of developers lose 10+ hours a week to non-coding work. <br> *Source: Atlassian State of Developer Experience 2025* | Big "50%" number. Half-filled circle. |
| 7 | **Do this audit yourself (5 min)** <br> 1. Open last week's calendar <br> 2. Count blocks of 2+ hours with no meeting <br> 3. Count the "quick calls" <br> 4. Fewer than 3 long blocks? Your calendar is the problem, not you. | Checklist style, like a terminal: `[ ]` boxes. |
| 8 | **3 small fixes** <br> 1. Put all meetings in one half of the day <br> 2. Book one 2-hour focus block every day, like a meeting <br> 3. Turn Slack asks into a to-do list, not an interruption | Three cards. Same style as slide 7. |
| 9 | **Or let a tool do the audit (ours)** <br> ZeroAI scans your next 2 weeks and shows where focus time goes. It books Deep Work blocks and turns Slack, Jira and Linear asks into tasks. Free Chrome extension. | Screenshot of the real ZeroAI calendar scan (ask the client for one). "(ours)" visible. |
| 10 | **It's not you. It's your calendar.** <br> Save this for Monday. Send it to the teammate with 9 back-to-back calls. | Clean calendar with two big green focus blocks. ZeroAI logo small at the bottom. |

---

## Caption

> We audited a developer's week. 40 hours on the calendar. Only 4 hours of real focus time. 😶
>
> Do the 5-minute audit on slide 7. If you get fewer than 3 long blocks, it's not you. It's your calendar.
>
> Want the audit done for you? ZeroAI (our free Chrome extension) scans your calendar and books focus time. Link in bio.
>
> Sources: Atlassian State of Developer Experience 2025; Gloria Mark (UC Irvine) via Gallup. The week shown is an example.

**Optional CTA instead of "link in bio":** "Comment AUDIT and we'll DM you the link." This needs a comment-to-DM tool such as ManyChat set up first.

---

## Check before posting

- [ ] Client confirms the 2-week scan feature and its wording.
- [ ] Get a real screenshot of the scan for slide 9.
- [ ] Check the Atlassian 2025 "half lose 10+ hours" wording against the report.
- [ ] Keep "(ours)" on slide 9.
