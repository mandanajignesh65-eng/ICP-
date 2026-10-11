# Meta campaign architecture, audiences and creatives for B2B Click-to-WhatsApp (CTWA) lead gen in India (Chat360, 26 Oct – 9 Dec 2026)

> Method note: WebFetch could not reach any target host in this session (DNS/egress blocked for developers.facebook.com, whatsappbusiness.com, jonloomer.com, saashero.net, etc.). All findings come from web-search result extracts of the cited pages, not full-page reads. Exact UI labels, limits and numbers should be checked in Ads Manager or Meta Help Center before launch. Vendor and agency numbers are marked **[vendor]**. Meta success stories are marked **[Meta, self-reported]**.

## 1. Campaign options for B2B leads in 2026: CTWA (Engagement vs Leads), Instant Forms, Advantage+ leads, Andromeda

### Takeaway
For a WhatsApp-native qualification funnel, run CTWA under the **Leads objective (or Engagement with a "Leads" performance goal) with WhatsApp as the conversion location**, and pass a "qualified lead" event back through the Conversions API for Business Messaging. Meta's own tests show lower cost per result when optimizing for leads instead of raw conversations. A small Higher-Intent Instant Form control cell (about 10–15% of test budget) is worth running, because Instant Forms are Meta's most mature B2B lead path and give a CPL and lead-to-SQL baseline. Under Andromeda, creative diversity does the targeting work, so the number of genuinely different concepts per ad set matters more than audience slicing.

### Cited Findings
- Meta's Marketing API docs list **Engagement objective** optimization for CTWA as CONVERSATIONS or LINK_CLICKS, and the **Leads objective** as able to optimize for CONVERSATIONS with a WhatsApp destination. Campaigns that use **call prompts must be OUTCOME_ENGAGEMENT**. Meta is also rolling out a new "recommended setup" for Traffic, Awareness and Engagement, with manual options still available — [Meta for Developers: Ads that Click to WhatsApp](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/messaging-ads/click-to-whatsapp) (via search extract)
- WhatsApp Business's own "down-funnel optimizations" resource describes picking Engagement and then setting **Leads as the performance goal**. In one Meta experiment, lead optimization gave **24% lower cost per lead** than optimizing for conversations. This is **not available in the EU, UK, Japan or South Korea**, so India is eligible — [WhatsApp Business: Down-funnel optimizations](https://whatsappbusiness.com/resources/resource-library/down-funnel-optimizations-whatsapp/) (single one-week experiment, not independently verified)
- Meta's published CTWA A/B tests, as summarized by a vendor: switching from conversation or message optimization to **lead or purchase optimization cut cost per result by 12%–79%**. Nutryfit (India/Gulf) saw **12% lower CPL** after the switch — [Spur: CTWA benchmarks](https://www.spurnow.com/en/blogs/click-to-whatsapp-ads-benchmarks) **[vendor summary of Meta tests]**
- Braip success story: CTWA with lead optimization gave **+45% qualified leads and −30% CPL** compared with message-optimized ads. Braip defined "qualified" by its own eligibility criteria — [WhatsApp Business: Braip](https://whatsappbusiness.com/resources/success-stories/braip/) **[Meta, self-reported]**
- Sending downstream qualification events through the **Conversions API for Business Messaging**, tied to the CTWA click ID, teaches Meta which users become qualified leads. Vendors advise against judging CTWA by "chats started" — [YCloud](https://www.ycloud.com/blog/how-to-improve-click-to-whatsapp-ads-performance.md); [Qiscus](https://www.qiscus.com/en/blog/whatsapp-lead-generation/); [360dialog: Meta Pixel and CTWA optimization](https://docs.360dialog.com/360pilot/integrations-and-optimization/meta-pixel-and-ctwa-optimization). Standard event name is "Lead". The exact event name and availability for a "qualified lead" CTWA event were **not confirmed** — [Netcore conversion tracking](https://emaildocs.netcorecloud.com/reference/conversion-tracking)
- **Advantage+ leads campaigns** (Meta page): they need fewer inputs, every leads conversion location supports end-to-end automation, and mixing locations can lower cost. Meta's figure is that pairing website-form and instant-form campaigns gave **60% lower CPL and 125% more lead volume** — [Meta: Advantage+ leads campaigns](https://www.facebook.com/business/ads/meta-advantage-plus/leads)
- Third-party reports on 2026 changes:
  - The Leads objective now defaults to "Website and Instant Forms".
  - New Leads campaigns launch with all Advantage+ Creative enhancements pre-selected (since about Feb 2026).
  - Instant Forms have added optional SMS verification and a work-email filter.
  - Sources: [LeadSync](https://leadsync.me/blog/create-facebook-lead-ad-campaign/); [AdAdvisor](https://adadvisor.ai/blog/meta-advantage-plus); [AdMove](https://www.admove.ai/blog/meta-advantage-creative-best-practices-for-2026) **[vendor, unverified against Meta]**
  - No source confirmed whether messaging/WhatsApp is a supported conversion location *inside* Advantage+ leads automation.
- **Instant Form types:**
  - "More Volume" is the default and has no review step.
  - "Higher Intent" adds a review/confirm step before submit, which reduces volume but removes many "I don't remember filling this" leads. It is recommended for B2B decision-maker campaigns and whenever a human will call the lead.
  - Conditional questions can skip questions or end the form early based on answers. They are driven by a CSV upload.
  - Practitioners advise 2–3 qualifying questions for B2B (company size, challenge, timeline). Five or more questions hurts completion.
  - Sources: [LeadsBridge](https://leadsbridge.com/blog/instant-forms-example/); [Qwestyon](https://www.qwestyon.com/blog/why-are-my-meta-lead-form-leads-so-bad-7-fixes-that-usually-improve-quality); [ClickyOwl](https://clickyowl.com/meta-instant-forms-lead-quality/); [Milap Chavda](https://www.milapchavda.com/meta-ads-instant-forms-best-practices/) **[vendor/agency]**. One source cites roughly 10–20% higher CPL for Higher Intent **[unverified]**.
- India agency benchmark: CTWA B2B leads cost **₹200–₹800**, against **₹400–₹1,500 for Meta lead forms**. Lead-to-SQL is **15–25% for CTWA vs 5–12% for lead forms**, based on the agency's own SaaS, services and EdTech campaigns in 2025–26 — [Sotros Infotech](https://sotrosinfotech.com/blog/whatsapp-click-to-chat-ads-b2b-lead-generation-2026/) **[vendor, self-reported, unaudited]**
- **Andromeda / creative-as-targeting:** Jon Loomer argues that "creative diversification" has replaced targeting as Meta's main lever. It gives the system options to optimize, prevents fatigue, and reaches different people — [Jon Loomer Pubcast, Sept 2025](https://pubcast.jonloomer.com/creative-diversification-is-the-new-targeting/). For B2B SaaS, one agency recommends **10–15 genuinely different concepts** that vary format, persona, setting or benefit, with a **50/30/20 budget split** (proven / iterations / new concepts) — [SaaS Hero: Andromeda for B2B](https://www.saashero.net/strategy/meta-andromeda-b2b-facebook-ads/) **[agency]**. A further claim that after an April 2026 Andromeda update more edits reset learning, and exit takes 7–14 days, comes from a single vendor — [Jetfuel](https://jetfuel.agency/what-is-the-meta-ads-learning-phase-how-to-exit-it-faster-in-2026/) **[unverified]**

### Inferences
- **Primary cells:** CTWA in a Leads-objective campaign with WhatsApp destination. If the Leads-goal option is not available in the account, use Engagement → Conversations at launch and switch to Leads once the CAPI qualified-lead event is firing.
  - Pre-launch dependency: Chat360's own AI agent must post a `Lead`/qualified event via CAPI for Business Messaging when the Flow captures company size 201–5,000 and a buyer role that is not Sales.
  - Without that event, Meta will optimize toward cheap chatters such as students and job seekers.
- **Control cell:** one Higher-Intent Instant Form ad set (about $40–50/day during test) with 3 conditional questions: company size, role, and use case or timeline.
  - Turn on the work-email filter or SMS verification if it is visible in the account.
  - Add an "instant form → WhatsApp follow-up" variant. The thank-you screen CTA opens WhatsApp, and the AI agent sends a utility/marketing template within minutes.
  - This gives a defensible CPL and SQL baseline against CTWA, which matters for a Meta-partner case study.
- **Advantage+ leads campaign:** do not use it as the primary vehicle in a 45-day flight, because messaging-destination support is unconfirmed. Test it only in the SCALE phase if Instant Forms prove competitive.
- **Creative over audiences:** treat creative concepts, not the 4 vertical ad sets, as the main targeting lever. The vertical split is still useful because each vertical gets its own creative, welcome message and Flow branch.

### Gaps
- No primary Meta page was readable to confirm the current Ads Manager labels in Oct 2026 ("Leads objective + Messaging apps destination" vs "Engagement + Leads goal").
- No confirmation that WhatsApp is a conversion location inside Advantage+ leads campaigns.
- No public head-to-head data on CTWA vs Instant Forms for Indian enterprise (201–5,000 staff) buyers. Only the vendor ranges above exist.

## 2. Audience building: Advantage+ audience, custom audiences, lookalikes, exclusions, retargeting, geo/age, placements, minimum sizes

### Takeaway
Run broad Advantage+ audience across the 7 metros, using vertical and role interests only as *suggestions*. Put customer and existing-pipeline lists under **Audience Controls (hard exclusions)**, because detailed-targeting exclusions were removed in March 2025. Build a retargeting layer from video viewers, IG/FB engagers, website visitors and the WhatsApp-chatter list uploaded by phone number. Exclude Audience Network, since it is the usual source of low-quality conversions.

### Cited Findings
- **Exclusions:**
  - Detailed-targeting *exclusions* (interests/behaviors) were removed from active campaigns on **31 March 2025**, and from boosted posts on 10 June 2025.
  - **Custom-audience exclusions still work** when placed in **Audience Controls**. If the customer list sits under "Suggestions", Advantage+ can still serve ads to existing customers.
  - Sources: [AdsUploader: exclusions 2026](https://adsuploader.com/blog/facebook-custom-audience-exclusions); [Conversios](https://www.conversios.io/blog/meta-advantage-audience-vs-detailed-targeting-2026-guide/); [Involve Digital B2B](https://www.involvedigital.com/insights/meta-ads-b2b-lead-generation-strategy) **[agency]**
- Detailed targeting such as job titles and interests is a **suggestion by default**. Meta expands beyond it when it predicts better results. No source said job-title targeting itself was removed — [Conversios](https://www.conversios.io/blog/meta-advantage-audience-vs-detailed-targeting-2026-guide/); [TrueFuture Media](https://www.truefuturemedia.com/articles/advantage-plus-audience) **[agency]**
- **CTWA retargeting audiences:** upload past WhatsApp leads by phone number as a customer-list Custom Audience, select it in the campaign, and exclude customers — [DoubleTick: CTWA retargeting](https://learn.doubletick.io/ctwa-retargeting/using-your-ctwa-custom-audience-in-meta-ads-manager). "Retargeting people who messaged" can mean two things: follow-up inside WhatsApp under the 24-hour window and templates, or exporting WhatsApp engagers to a Meta custom audience — [Nimblebiz](https://nimblebiz.ai/blog/whatsapp-retargeting-meta-ad-leads) **[vendor]**. The current official name and availability of a native "people who messaged your business on WhatsApp" engagement audience were **not confirmed**.
- **Lookalikes:** reported minimum seed is **100 people**, with about 1,000 as a practical minimum and 5,000–10,000 for good quality — [Lionelz](https://lionelz.com/en/blog/facebook-lookalike-audiences-opportunities/) **[unverified vs Meta]**
- **Placements:**
  - Jon Loomer: use Advantage+ placements by default and remove a placement only if it produces low-quality conversions. **Audience Network** is the placement group most associated with accidental clicks, bots and click fraud, and the usual source of Meta's invalid-traffic refunds — [Jon Loomer: Guide to placements](https://www.jonloomer.com/a-guide-to-meta-ads-placements/)
  - A B2B case cited by Strike Social found Advantage+ placements gave more leads but **lower-quality** leads than manual placement controls — [Strike Social](https://strikesocial.com/?p=355675) **[agency]**

### Inferences
- **Prospecting (4 vertical ad sets during TEST):**
  - Geography: 7 metros (Mumbai, Delhi NCR, Bengaluru, Hyderabad, Chennai, Pune, Kolkata — confirm list) with "people living in" these locations.
  - Age: 25–55+. A floor of about 25 cuts students and job seekers who chat on WhatsApp ads. Do not set an upper cap, because CXOs skew older.
  - Advantage+ audience with suggestions: vertical interests (e.g. automotive industry, real estate, healthcare, banking) plus role suggestions (CTO, CMO, founder, digital marketing, product management).
  - Each ad set's creative carries the vertical signal, so Andromeda finds the buyers.
- **Hard exclusions in Audience Controls, on every ad set:**
  - Customer list (phones and emails).
  - Open-pipeline CRM list.
  - Chat360 employees.
  - Partner and BSP-competitor staff lists, if available.
  - Lead-form submitters and WhatsApp chatters from the previous 30 days, so prospecting does not pay for people already in the funnel.
- **Seed audiences to build now (lookalike seeds and retargeting):**
  - Website visitors, 30 and 180 days. Needs pixel and CAPI.
  - Video viewers at 50%/ThruPlay, 30 days.
  - IG/FB engagers, 60 days.
  - Uploaded WhatsApp chatters by phone number, refreshed weekly via the Chat360 API.
  - Customer list as a lookalike seed: 1% India and 1% metros only, if the seed is at least 1,000.
- **Retargeting in a 45-day flight:**
  - Retargeting pools will be small before about week 3.
  - From the creative-refresh round (about 13–15 Nov), add one retargeting ad set at roughly 10–15% of budget (website, video viewers, engagers, chatters who did not qualify).
  - Run proof-heavy creative here: case-study carousel, Voice AI demo, ROI static.
- **Placements:**
  - Start with Advantage+ placements minus Audience Network, and check that WhatsApp Status (if offered) is reporting separately.
  - After 7 days, break down qualified-lead rate by placement. If Messenger inbox, right column or Threads deliver junk, narrow to FB/IG Feed, Stories, Reels and Explore.
- **Minimum sizes:**
  - B2B role suggestions under Advantage+ will be broad, so size is not a concern for prospecting.
  - Retargeting below about 1,000 matched users will under-deliver. Merge retargeting sources into one ad set rather than splitting them.

### Gaps
- Meta's official minimum audience size for delivery was not found.
- Exact native name and availability of a "WhatsApp messaging engagement" custom audience were not found.
- No India-specific data on how Advantage+ audience behaves for job-title-led B2B targeting.

## 3. CTWA chat entry: welcome messages, ice breakers, prefilled messages, Flows from the ad, per-industry welcome

### Takeaway
Each vertical ad should carry its **own ad-level welcome-message sequence**: a greeting plus a prefilled message or up to 4 ice breakers. Where possible, launch a **WhatsApp Flow straight from the ad** to qualify on company size, role, use case and timeline in a few taps. Meta's Learnwise case reported about 4x qualified leads and −31% cost per qualified lead from doing exactly this.

### Cited Findings
- **Customer action types:**
  - The default greeting is generic ("Can I get more info…").
  - The ad's greeting can be customized via `page_welcome_message` in `object_story_spec`.
  - Meta's examples cover customer action types of **autofill (prefilled text), ice breakers, and WhatsApp Flow**.
  - Source: [Meta for Developers: CTWA](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/messaging-ads/click-to-whatsapp) (via search extract)
- **Ice breakers and welcome sequences:**
  - Up to **4 ice breakers**, **80 characters each, no emojis**, shown when a user starts a chat for the first time.
  - Ad-level welcome-message sequences can include text, a prefilled message and FAQs, and apply only to people who tap that ad.
  - Sources: [AdLibrary guide](https://adlibrary.com/posts/meta-click-to-whatsapp-ads-guide); [Zoko: set up ice breakers](https://www.zoko.io/learning-article/setup-icebreakers) **[vendor]**
- If a user opens a wa.me link with prefilled text, the ice-breaker interface is **dismissed automatically**, so pick one per entry point — [360dialog: Conversational components](https://docs.360dialog.com/docs/messaging/conversational-components)
- One guide claims Meta removed the old "welcome message" option from conversational components on **27 March 2026**, leaving ice breakers and commands. The 360dialog page still lists welcome messages, so this is **conflicting/unverified** — [AdLibrary guide](https://adlibrary.com/posts/meta-click-to-whatsapp-ads-guide) vs [360dialog](https://docs.360dialog.com/docs/messaging/conversational-components)
- **Learnwise (Kerala EdTech)** used an automated screening Flow inside CTWA ads and reported about **4x more qualified leads, 60% less staff time qualifying, and 31% lower cost per qualified lead** — [WhatsApp Business: Learnwise](https://whatsappbusiness.com/resources/success-stories/learnwise/) **[Meta, self-reported]**
- **Free entry point:** replying to a CTWA lead opens a free window. Sources give it as **72 hours** or as "may remain open for up to 7 days" — [AdLibrary guide](https://adlibrary.com/posts/meta-click-to-whatsapp-ads-guide); [Codingclave](https://codingclave.com/blog/whatsapp-ads-cost-india-2026) **[conflicting; verify]**
- **India WhatsApp pricing:**
  - Per-message pricing has applied since **1 July 2025**, with utility volume tiers — [Zoho Help](https://help.zoho.com/portal/id/community/topic/whatsapp-message-pricing-changes-effective-july-1-2025?page=10)
  - India marketing rate is about **₹0.86/message** after a roughly 10% rise on 1 Jan 2026, and utility/authentication about ₹0.115–0.13. Service replies are free — [MyOperator support](https://support.myoperator.com/portal/en/kb/articles/whatsapp-has-shifted-to-per-message-pricing-effective-july-1-2025-based-on-message-categories-and-your-recipient-s-country-in-india-there-are-three-paid-categories); [eCorpIT](https://ecorpit.com/whatsapp-business-api-cost-india-d2c-2026/) **[third-party; verify on Meta rate card]**

### Inferences
- **Per-vertical entry design (one ad-level welcome per ad set):**
  - **Auto & EV**
    - Greeting: "Hi 👋 I'm Chat360's AI agent. Want to see how dealers turn ad clicks into booked test drives on WhatsApp?"
    - Ice breakers: (1) "Show me a test-drive booking demo" (2) "How does AI qualify car leads?" (3) "Call me on WhatsApp (Voice AI)" (4) "Pricing for 50+ dealer outlets"
    - Ice breakers must have no emojis. The greeting emoji is fine, but test without it.
  - **Healthcare & Diagnostics:** appointment and home-collection booking, report-ready reminders and OTP, Voice AI reminder calls.
  - **Real estate:** site-visit booking, lead qualification by budget and location, Voice AI callback.
  - **BFSI:** loan/insurance lead qualification, KYC document collection via Flows, payment reminders. Add a compliance note: no promises about interest rates.
- **Entry mechanics:**
  - Prefer a **Flow-from-ad** variant against an **ice-breaker** variant as an A/B inside each vertical.
  - Flow screen 1 (four taps): role (CXO/Founder, CTO/IT, Marketing/Growth/Digital, Product, Sales, Other), company size band, use case, timeline.
  - Have the AI agent route Sales-function and <200-staff leads to a self-serve or nurture path. They should not trigger the CAPI qualified-lead event.
- **Demo-in-chat:** because Chat360 sells the very thing the ad uses, the chat itself should be the demo. Explicitly tell the user "You're experiencing exactly what your customers will", and offer a live Voice AI call-back inside WhatsApp as the "aha" moment.

### Gaps
- Could not confirm whether WhatsApp Flows can be attached directly in Ads Manager UI in India in Oct 2026, or only via Marketing API or partner tools.
- Could not confirm the 27 March 2026 welcome-message deprecation.
- No CTWA reply-latency benchmark for B2B was found.

## 4. Creatives for B2B on Meta: formats, safe zones, hooks, concept count, refresh, Advantage+ creative, language, India examples, compliance

### Takeaway
Produce **about 4–5 distinct concepts per vertical**, each in 9:16 and 4:5 (plus 1:1 for carousel), so the 4 ad sets carry about 16–20 concepts. Mix formats: founder or expert talking head, a real phone-screen recording of the WhatsApp flow, a problem-agitate static, and a use-case carousel. Keep text inside Reels safe zones (top 14%, bottom 35%, about 6% each side). Use English as the base, with a Hinglish test variant. Remove third-party brand names and Meta/WhatsApp logo misuse.

### Cited Findings
- **Safe zones:** keep text and logos out of the **top 14%, bottom 35% and about 6% each side** on 9:16. Recommended canvas is **1440×2560**, with 1080×1920 still accepted. Some 2026 guides describe a unified Stories+Reels zone with a 20–35% bottom margin, so design to 35%. Use Ads Manager's safe-zone overlay — [Billo: 2026 safe zones](https://billo.app/blog/meta-ads-safe-zones); [Superscale](https://superscale.ai/learn/meta-ad-sizes); [1ClickReport](https://www.1clickreport.com/blog/meta-ads-creative-safe-zones-2026-guide) **[vendor; conflicting bottom %]**. Feed images: 4:5 at 1440×1800 or 1080×1350 — same sources.
- **B2B formats that work:**
  - Founder-to-camera on the problem is called one of the top B2B formats for 2026.
  - Phone-filmed founder or employee video beats polished video on CPC for cold audiences, while polished creative wins for warm retargeting.
  - Carousels suit consideration: sequential story, use cases, objections.
  - A "pain → process → proof" sequential series is recommended.
  - Sources: [Elevarus](https://elevarus.com/meta-ad-creatives-lead-generation-2026/); [Flighted](https://www.flighted.co/blog/b2b-saas-ad-creative-the-ultimate-guide); [SaaS Hero creative guide](https://saashero.net/strategy/b2b-ad-creative-design-guide/) **[agency]**
- **Hooks and demos:**
  - Open with the product's most striking screen in the first 3 seconds. A sharp line of copy with no imagery can also work for B2B — [Flighted](https://www.flighted.co/blog/meta-ads-creative-strategy-guide-for-b2b-saas-brands)
  - About 67% of mobile viewers swipe away if the first 3 seconds don't grab them — [Elevarus](https://elevarus.com/meta-ad-creatives-lead-generation-2026/) **[unsourced vendor stat]**
- Motion's Dec 2025 talk says creator-led B2B ads raised efficiency "up to 32%", attributed to a Meta study, and advises against over-produced founder ads — [Motion](https://motionapp.com/library/talk/the-creator-led-strategy-boosting-b2b-ad-efficiency-32-meta-study/) **[not verified]**
- **Concept count:** 10–15 genuinely different concepts for B2B SaaS under Andromeda, with a 50/30/20 split — [SaaS Hero](https://www.saashero.net/strategy/meta-andromeda-b2b-facebook-ads/) **[agency]**
- **Fatigue signals and refresh cadence:**
  - Frequency above 2.5 on cold audiences, or CTR down 20–30% from baseline over 3–7 days, or CPA rising without an auction cause — [Superads](https://www.superads.ai/blog/creative-refresh-cadence)
  - Frequency above 4.0, or CTR down more than 20% over 2 weeks — [Billo](https://billo.app/?p=51744)
  - Frequency above 3.0 — [Rocketium](https://rocketium.ai/academy/all/ad-fatigue-statistics)
  - B2B SaaS creative lifespan of about **12 days on Meta** vs about 43 on LinkedIn — [Growthspree](https://www.growthspreeofficial.com/blogs/b2b-saas-ad-creative-benchmarks-2026)
  - A 2–4 week starting cadence — [Segwise](https://segwise.ai/blog/how-often-refresh-ad-creatives)
  - All **[vendor]**.
- **Advantage+ Creative:** reported to be pre-selected on new Leads campaigns since about Feb 2026 — [AdMove](https://www.admove.ai/blog/meta-advantage-creative-best-practices-for-2026) **[vendor]**
- **Language:**
  - No B2B Hinglish vs English study was found.
  - Consumer research (Ahluwalia & Krishna, JCR) links Hindi with "belongingness" and English with "sophistication", and finds mixed-language ads also received favorably — [VOA summary](https://learningenglish.voanews.com/a/a-23-2008-12-09-voa3-83140112/117492.html)
  - Practitioner guidance advises against Hindi/regional copy for B2B SaaS — [eChai Ventures](https://echai.ventures/startingup/copywriting-messaging/when-should-i-write-copy-in-hindi-or-a-regional-language-versus-english-for-an-indian-consumer-product-and-how-do-i-get-the-tone-right)
- **Competitor positioning:**
  - Interakt is pitched at D2C/Shopify.
  - AiSensy is the most tied to Meta CTWA ads, with an "AI ad creative generator".
  - WATI is pitched as CRM plus chatbot.
  - Gupshup is the technical, high-volume option.
  - Sources: [eChai Ventures comparison](https://echai.ventures/d2c/d2c-whatsapp-sms/wati-interakt-aisensy-gupshup-which-to-use); [AiSensy vs Interakt vs WATI](https://aisensy.com/aisensy-vs-interakt-vs-wati) **[vendor]**
  - No Meta Ad Library observations could be retrieved; the Ad Library is not reachable from this environment.
- **Brand compliance:**
  - Ads on Meta products are reviewed by Meta's Ad Policy team and don't need Brand Resource Center permission. Other marketing must use only official assets and follow the guidelines — [Meta Brand Resource Center](https://www.meta.com/brand/resources/)
  - **All use of the Meta logo requires approval** via Brand Review — [Meta brand: company brand](https://www.meta.com/brand/resources/meta/company-brand/)
  - WhatsApp's name must appear in the same font size and style as the surrounding text, using only official assets — [WhatsApp brand guidelines](https://www.meta.com/brand/resources/whatsapp/whatsapp-brand/)
  - Don't combine the WhatsApp logo with other logos or imply partnership or endorsement — [Infobip compliance guide](https://www.infobip.com/docs/whatsapp/compliance) **[third-party]**
  - Partnership lockups exist only for Meta's primary brands under approved guidelines — [Partnering with Meta](https://www.meta.com/brand/resources/meta/partnering-with-meta/)
  - No public rules were found for a "Meta Business Partner" badge in ads.

### Inferences — complete creative production list (TEST + refresh)

Global rules for every asset:
- English base copy.
- No Meta logo.
- No WhatsApp logo combined with the Chat360 logo. Write "WhatsApp" in plain text at body size, and get Meta brand review for any partner-badge use.
- No real third-party brands, cars, hospitals or banks. Use fictional "Your Dealership" style UI mockups.
- Burned-in captions on all video.
- Hook in the first 1–2 seconds.
- 9:16 at 1440×2560 inside safe zones, plus a 4:5 at 1440×1800 cut of every asset.
- Videos 15–30 seconds; demos up to 45 seconds.
- CTA "Send WhatsApp message".

**A. Cross-vertical "hero" concepts. Make each once, then version the end-card and first line per vertical.**
1. **Founder/CXO talking head (selfie-style, 20–30 s):**
   - Hook: "Your Meta leads are going cold in 5 minutes. Here's how we fixed it."
   - Then: CTWA → AI agent qualifies → booked meeting.
   - Shoot 4 opening lines, one per vertical, as cheap variants.
2. **Live phone-screen recording (25–40 s):**
   - The real Chat360 flow on a phone: ad tap → WhatsApp opens → Flow (role, size, timeline) → slot booked → reminder.
   - On-screen counter: "47 seconds from ad click to booked demo".
   - Make one per vertical, with fictional brand UI.
3. **Voice AI demo (20–30 s):**
   - Audio-first: an AI voice call inside WhatsApp confirming a test drive, site visit or sample collection.
   - Hook: "This call wasn't made by a human."
   - Captions mandatory.
4. **Problem-agitate static (4:5 and 9:16):**
   - Bold headline such as "₹40 lakh on Meta ads. 70% of leads never answer the call." with a sub-line on the fix.
   - Make 2 headline variants per vertical.
   - Use only numbers Chat360 can substantiate.
5. **Use-case carousel (1:1 or 4:5, 4–5 cards):**
   - One card each: CTWA ads + AI qualification, Voice AI, reminders/OTP, Flows, and a proof card with case-study metrics.
   - Best for retargeting and the refresh round.
6. **Customer proof/testimonial (refresh round):**
   - A customer talking head or quote static with metrics, with the customer's written consent.
   - Brand name only with permission, and no customer logos without rights.
7. **"Ad → WhatsApp in 3 steps" static (compliant rebuild of the current creative):**
   - Generic icons instead of the Meta logo or third-party brands.
   - Headline per vertical: "From ad click to test drive / site visit / sample pickup / KYC done — on WhatsApp."

**B. Per-vertical TEST set (about 4–5 concepts per ad set):** each ad set gets versions of #1 (founder hook variant), #2 (screen demo), #3 (Voice AI), #4 (static ×2) and #7 (3-step static). Vertical cues:
- **Auto & EV:** test-drive booking, EV charging-slot and service reminders.
- **Healthcare & Diagnostics:** home sample collection, report-ready, appointment reminders. No medical claims.
- **Real estate:** site-visit booking, budget/locality qualification, RERA-safe language.
- **BFSI:** lead qualification for loans/insurance, document collection by Flow, EMI/OTP reminders. Avoid return or rate claims.

Total for TEST: about 20 ads (4 verticals × 5), plus about 2 Hinglish variants of the best-performing hooks per vertical, launched at refresh.

**C. Refresh round (around day 14–18, about 9–13 Nov, right after the Diwali CPM peak):**
- Kill the bottom 50% by cost per qualified lead.
- Add 2 new concepts per vertical: customer proof (#6), plus a new hook on the winning format (e.g. "CTO-to-CTO" architecture explainer, or "Head of Growth" ROI angle).
- Add the carousel (#5) to retargeting.
- Test Hinglish versions of the 2 best hooks.

**Count and cadence:**
- Expect B2B fatigue around 12–21 days at this audience breadth.
- Watch for frequency above 2.5–3 on prospecting, CTR down more than 20% vs the first-week baseline, or cost per qualified lead up more than 30% without a CPM rise.

**Advantage+ Creative enhancements:**
- Keep enhancements that change visual presentation (brightness, aspect fit).
- Switch off text generation and "add music" for founder and Voice AI videos, because audio is the message.
- Review auto-generated text variants for compliance.

### Gaps
- No live Meta Ad Library observations of Zoho, Freshworks, LeadSquared, Gupshup, Interakt, WATI or AiSensy ads could be made. The Ad Library was unreachable, and search returned only vendor comparison pages.
- No B2B-specific evidence on Hinglish vs English, or on hook-rate and video-length benchmarks for Indian enterprise audiences.
- Meta's official 2026 safe-zone spec page was not readable.

## 5. Budget pacing and bidding: bid strategy, learning phase, scaling, festive CPM

### Takeaway
At **$75/day per ad set**, CTWA can exit learning on *conversations*, which needs about 50 conversations per week, i.e. ≤$10.5 per conversation. It probably cannot exit learning on *qualified leads*. Start with Highest Volume, consolidate rather than fragment, and scale winners in roughly 20% steps or by duplicating into a consolidated scale campaign. Expect festive CPM inflation around Diwali (8 Nov). Keep TEST spend modest through roughly 10 Nov and push SCALE spend into the post-Diwali window of 12 Nov – 9 Dec.

### Cited Findings
- **Learning phase:** an ad set usually needs **about 50 optimization events in a rolling 7 days** to exit. The count is **per ad set**. Significant edits (targeting, optimization event, bid strategy, roughly 20%+ budget change) reset learning — [Cometly](https://www.cometly.com/post/facebook-ads-learning-phase-optimization); [Adtribute](https://www.adtribute.io/glossary/learning-phase); [JumpFly](https://www.jumpfly.com/blog/what-can-you-learn-from-the-meta-learning-phase/) **[third-party; 20% threshold not confirmed in Meta docs]**
- Some accounts reportedly exit learning with 20–30 events, with no Meta confirmation — [Aimerce newsletter](https://newsletter.aimerce.ai/p/stuck-in-meta-s-learning-phase-here-s-how-to-fix-it) **[unverified]**. Exits reportedly lengthened to 7–14 days after April 2026 — [Jetfuel](https://jetfuel.agency/what-is-the-meta-ads-learning-phase-how-to-exit-it-faster-in-2026/) **[unverified]**
- **Festive CPM:** Meta CPMs rise sharply through Diwali, but no source gave a reliable percentage — [Linkrunner](https://deeplinks.linkrunner.io/blog/meta-ads-structure-diwali-campaigns); [Graas](https://www.graas.ai/blog/meta-vs-google-ads-indian-festive-budget-allocation). Google CPCs can rise 25–40% in the same period — [Razorpay Rize](https://rizevault.razorpay.com/p/ad-spend-and-cac-survival-guide-for-festive-season). Consumer brands are raising festive budgets 15–20% — [Graas](https://www.graas.ai/blog/meta-vs-google-ads-indian-festive-budget-allocation)
- Meta promotes AI and Reels tools for India festive advertising — [exchange4media](https://www.exchange4media.com/festive-season-news/meta-bets-on-ai-and-reels-to-power-festive-sales-in-india-147214.html); [Campaign India](https://www.campaignindia.in/article/meta-rolls-out-festive-tools-for-indias-ad-market/504618)

### Inferences
- **Budget arithmetic:**
  - $23,333 over 45 days is about $518/day on average.
  - TEST is 4 × $75 = $300/day. An optional Instant Form control at about $40/day brings it to about $340/day.
  - SCALE at about $688/day implies roughly 26–28 SCALE days. Confirm with the media plan: about 10 TEST days at $340 is about $3.4k, leaving about $19.9k, which is about 29 days at $688.
- **Learning-phase feasibility at $75/day ($525/week):**
  - On conversations: feasible if cost per conversation is ≤ ~₹900. Vendor India click costs are ₹5–25 — [Codingclave](https://codingclave.com/blog/click-to-whatsapp-ads-india-2026). B2B conversation costs will be higher **[vendor]**.
  - On qualified leads: likely infeasible. At ₹200–800 per lead, about 50 *leads* per week fits, but qualified leads at 15–25% of those would be only about 8–15 per week.
  - **Plan:** optimize on Leads/conversations, and measure cost per qualified lead (CPQL) in Chat360's CRM.
  - Consider **consolidating to 2 ad sets** (e.g. Auto+Real estate "booking" vs Healthcare+BFSI "reminders/compliance") if learning stalls after 7 days.
- **Bidding:**
  - Use Highest Volume (no cap) in TEST.
  - In SCALE, add a cost-per-result goal at about 1.2–1.3× the TEST CPL only if CPMs spike and CPL drifts. This is a practitioner convention, not cited.
- **Scaling:**
  - Raise winning ad sets 15–20% every 48–72 hours, or move winners into a single SCALE campaign (Advantage campaign budget) with the top 6–10 ads by cost per qualified lead.
  - Do not edit the TEST cells during learning.
- **Festive mitigation:**
  - Hold TEST at a steady spend 26 Oct – 10 Nov.
  - Do not scale into Diwali week (5–9 Nov).
  - Ramp to $688/day from about 12 Nov, when consumer advertisers pull back and the B2B work calendar resumes.
  - Keep 10–15% in reserve for the strongest week (late Nov – early Dec, before year-end freeze).

### Gaps
- No primary Meta documentation for the 20% budget-edit threshold.
- No India-specific Meta CPM inflation figure for Diwali 2025.
- No Meta-published minimum budget per ad set for CTWA in INR.

## 6. Benchmarks: India CTWA cost per conversation, CPQL, conversation→qualified rates, Meta case studies

### Takeaway
There is **no independent public benchmark** for B2B CTWA in India. Meta itself does not publish CTWA industry benchmarks. Planning ranges from vendors:
- CPL about ₹200–800, against ₹400–1,500 for lead forms.
- Lead-to-SQL about 15–25%.

Meta's self-reported cases show 12–79% lower cost per result from lead optimization, and 31% lower cost per qualified lead from Flows. Chat360 should treat TEST as the benchmark-setting exercise.

### Cited Findings
- Spur states there are **no independent public CTWA benchmarks** for CTR or cost per conversation, and that Meta does not publish industry benchmarks. It recommends judging by CPQL, booking rate and revenue per conversation — [Spur](https://www.spurnow.com/en/blogs/click-to-whatsapp-ads-benchmarks) **[vendor]**
- **Sotros Infotech:**
  - CTWA B2B CPL is **$8–35 globally and ₹200–800 in India**, vs ₹400–1,500 for lead forms.
  - Lead-to-SQL is **15–25%** (CTWA) vs **5–12%** (lead forms).
  - Conversation start costs **$5–25 globally**.
  - Source: [Sotros Infotech](https://sotrosinfotech.com/blog/whatsapp-click-to-chat-ads-b2b-lead-generation-2026/) **[agency, self-reported]**
- India CTWA click costs of about **₹5–25** — [Codingclave](https://codingclave.com/blog/click-to-whatsapp-ads-india-2026) **[vendor]**
- A vendor claim that Indian SMBs see **3–4x lower CPL** with WhatsApp vs form ads — [Kraya AI](https://blog.kraya-ai.com/whatsapp-advertising-campaign) **[unsourced]**
- A local agency case of **3,572 WhatsApp chats at ₹1.93 each**, consumer and not B2B — [Dizispark](https://dizispark.com/meta-ads-case-study-3572-whatsapp-chats-rs-1-93/) **[agency]**
- An agency case reporting 40x growth in WhatsApp conversations for an Indian bank — [The Marketing Buddies](https://themarketingbuddies.notion.site/40x-Growth-in-WhatsApp-Conversations-1c6b6bfbb56a805e92cde60138bd1db7) **[agency]**
- **Meta success stories:**
  - Learnwise (India): about 4x qualified leads, −31% CPQL with Flows — [WhatsApp Business](https://whatsappbusiness.com/resources/success-stories/learnwise/)
  - Braip: +45% qualified leads, −30% CPL with lead optimization — [WhatsApp Business](https://whatsappbusiness.com/resources/success-stories/braip/)
  - Nutryfit (India/Gulf): −12% CPL — [Spur summary](https://www.spurnow.com/en/blogs/click-to-whatsapp-ads-benchmarks)
  - Meta experiment: −24% CPL from lead optimization — [WhatsApp Business](https://whatsappbusiness.com/resources/resource-library/down-funnel-optimizations-whatsapp/)
  - All **[Meta, self-reported]**
- **General B2B CPL context (not WhatsApp):** median B2B CPL about **$213** (HubSpot 2026, as cited) and blended SaaS CPL about **$237** (First Page Sage 2026, as cited) — via [Prospeo](https://prospeo.io/s/b2b-lead-generation-guide) **[secondary citation]**
- MyOperator reports conversation-start (reply) rates up to 60% from its own message analysis — [MyOperator](https://myoperator.com/blog/why-whatsapp-converts-better-than-b2b-websites-2026) **[vendor]**

### Inferences
- **Planning guardrails for TEST (to validate, not to promise):**
  - Cost per conversation started: ₹150–600. This is B2B in metros during festive CPMs, so it should be well above consumer ₹2–25.
  - Conversation → Flow completed: 30–50%.
  - Flow completed → ICP-qualified (201–5,000 staff, non-Sales buyer role): 15–30%.
  - Implied CPQL: about ₹1,500–6,000 ($17–70).
  - All of these are inferences from the vendor ranges above, not sourced benchmarks.
- **Kill/keep rule:**
  - After about $300–400 spend per ad set (4–5 days), cut any ad with zero qualified leads and above-median cost per conversation.
  - After 7 days, re-allocate budget toward the vertical with the lowest CPQL.
- **Case study:** Chat360's own campaign can become a Meta-partner case study (CTWA + Flows + CAPI lead optimization), mirroring the Learnwise and Braip format. Record a baseline now.

### Gaps
- No independent or audited India B2B CTWA cost-per-conversation or CPQL benchmark exists in public sources.
- No Meta case study of a BSP or SaaS company running CTWA for its own B2B acquisition was found.
- No published conversation→qualified rate specific to enterprise (201–5,000 staff) buyers was found.
