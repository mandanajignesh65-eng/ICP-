# Meta setup, verification and compliance before Chat360 launches CTWA ads in India, and what an MDF Path 1 claim needs (as of Oct 2026)

> **How these notes were researched.** On 11 Oct 2026 the sandbox's egress proxy blocked direct page fetches from facebook.com, developers.facebook.com and docs.360dialog.com (CONNECT 403 / DNS failure). Every finding below therefore comes from web-search result summaries of the cited pages, not from reading the full pages. Treat exact menu labels and numbers as "verify in-product". Items marked **[UNVERIFIED]** are practitioner knowledge with no source found in this session.
>
> Context: Chat360 is an Indian WhatsApp BSP, a Meta Business Partner at Incubate tier. It plans about ₹22.4 lakh (about $23,333) of CTWA spend from 26 Oct to 9 Dec 2026, 75% reimbursed under MDF Path 1. The team has never run Meta ads. **Today is 11 Oct 2026, so there are 15 days until launch.** Several steps below can take up to 14 business days, so they belong on the critical path.

---

## Q1. Business portfolio (Business Manager) setup, Business Verification in India, 2FA, admin roles, system users

### Takeaway
Use the **same business portfolio that already holds Chat360's partner relationship and WABA**, because the MDF claim asks for the partner business ID, and it should own the ad account. If Business Verification is not done yet, submit it **today**. Meta says a decision can take up to 14 business days. Indian GST, PAN and certificate of incorporation are all accepted documents. The single biggest reason for rejection is a business name that does not match character for character.

### Cited Findings
- **Review time.** Meta's help page says a verification decision can take **up to 14 business days**. Meta developer docs say most are processed **within 48 hours**. Indian guides report **2–10 working days** for registered entities, longer if the name or address doesn't match or the phone is unreachable. Unofficial blogs say domain-based checks take 1–2 business days. — [Meta: Verify your business](https://www.facebook.com/business/help/2058515294227817); [Meta developers: Business verification](https://developers.meta.com/horizon/resources/publish-organization-verification-business/); [richautomate.in 2026 guide](https://richautomate.in/blog/meta-business-verification-whatsapp-api-india-2026); [saurabhdhar.com 2026 guide](https://www.saurabhdhar.com/blog/meta-business-verification-guide-2026)
- **Accepted India documents.** BSP guides list the same set: business bank statement, business licence, Certificate of Incorporation, **GST certificate**, **PAN card**, Shop & Establishment certificate, Udyog Aadhaar, and utility bill. — [360dialog: Meta Business Verification](https://docs.360dialog.com/docs/resources/meta-business-verification); [Gallabox](https://docs.gallabox.com/~/changes/A8xmww5XU9i8x7QbfPLe/set-up-gallabox-account/meta-business-verification); [Wati docs-by-country](https://support.wati.io/en/articles/11463208-meta-business-verification-required-documents-by-country)
- **GST is accepted but not mandatory.** For a GSTIN certificate to work, the legal business name and address on it must match Business Manager, and the document must be legible. — [Exotel](https://developer.exotel.com/docs/whatsapp-support/business-verification); [Zoko](https://www.zoko.io/post/whatsapp-business-api-no-gst-number)
- **Documents that are NOT accepted:** invoices, purchase orders, self-filled applications and website printouts. — [Gallabox](https://docs.gallabox.com/~/changes/A8xmww5XU9i8x7QbfPLe/set-up-gallabox-account/meta-business-verification)
- **Name mismatch.** Meta lists "business name on the document does not match the business name on the account" as a top rejection reason. Blogs warn that a brand or DBA name (for example "Chat360" when the legal name is "XYZ Technologies Pvt Ltd") or a shortened name will trigger it. They advise copying the name character for character from the GST or MCA record. — [Meta developers](https://developers.meta.com/horizon/resources/publish-organization-verification-business/); [anylinga.com](https://anylinga.com/blog/en/meta-business-verification-rejected-7-fixes.html); [singhamandeep.com](https://singhamandeep.com/meta-business-verification-documents-required/)
- **Contact confirmation.** Guides recommend a business phone number that can be verified and an email on the company domain, not Gmail. One unofficial guide says not to use a phone number that is already registered on WhatsApp for the verification call or SMS. — [richautomate.in](https://richautomate.in/blog/meta-business-verification-whatsapp-api-india-2026); [kewbot.com](https://kewbot.com/minisite/en/guides/business-verification.html)
- **Verification and scaling.** A guide says Meta requires a verified Business Manager before ad spend can scale, and that a missing verification is a common cause of restrictions on new accounts. — [adnova.ai](https://www.adnova.ai/blogs/facebook-ad-account-disabled)
- **Two-factor authentication.** One vendor help page says Meta now requires 2FA on accounts that run ads. The excerpt was truncated, so the exact scope is unconfirmed. — [Metricool help](https://help.metricool.com/why-meta-may-restrict-a-new-business-account-connected-to-metricool-4hsnq)
- **Appeals.** Only admins can request a manual review of a restriction. The request goes through Business Support Home → "Request review", within 180 days. Sources warn against creating a replacement account while one is restricted, because it can escalate to a permanent ban. — [adnova.ai](https://www.adnova.ai/blogs/facebook-ad-account-disabled); [leadsie.com](https://www.leadsie.com/blog/recover-disabled-facebook-ad-account)

### Inferences
- As a BSP, Chat360 has almost certainly already verified its business portfolio, because verification is a precondition for being a WhatsApp Solution Partner and running a WABA above the base tier. **Action:** in Business Settings → Security Center, confirm the portfolio shows "Verified". If it does, no new submission is needed. Just make sure the new ad account is created **inside this same portfolio**.
- Owner checklist: (1) Business Settings → People: at least **2 full-control admins**, so the account is never locked to one person, each with 2FA switched on. (2) Business Settings → Security Center: switch on "Require two-factor authentication" for everyone. (3) Create a **System User** (admin) for the CAPI and webhook integration and give it access to the ad account, dataset and WABA. Tokens should not hang off a personal profile **[UNVERIFIED as a Meta requirement; it is best practice]**.
- Leave ample buffer. Re-verifying, or verifying for the first time, can take 14 business days, which pushes past 26 Oct. Do not change the business name or address in the portfolio right before launch, because that can trigger re-verification **[UNVERIFIED]**.

### Gaps
- Could not read Meta's live help page to confirm the 2026 India document list or whether PAN alone is enough. Sources disagree on the PAN point.
- Could not confirm Meta's current portfolio-wide 2FA mandate or its exact wording.

---

## Q2. Creating the ad account in India: INR/IST, payment methods, GSTIN and tax invoices, spending limits, risk on a new account

### Takeaway
Create the ad account in the business portfolio with **country India, currency INR, time zone Asia/Kolkata**. **Pick the payment method carefully at creation**, because India's manual and prepaid route (UPI, netbanking) can only be chosen then. Enter the company **GSTIN** in Payment settings **before the first charge**, so every invoice from Facebook India Online Services Pvt Ltd is a valid GST tax invoice for MDF receipts and input tax credit.

### Cited Findings
- **India payment options.** Credit cards and co-branded debit cards, plus local **manual** methods: netbanking, Paytm Wallet and **UPI**. Manual payment is only available when the ad account's country is India **and** its currency is INR. — [Meta Help: India payment methods](https://www.facebook.com/business/help/1410784518969094); [Meta Help: Accepted payment options](https://www.facebook.com/business/help/212763688755026)
- **The first payment method sets the billing mode.** A manual method can only be added if one was chosen when the ad account was first set up. A card whose bank supports recurring payments (or PayPal) puts the account on **automatic payments**, billed at thresholds or monthly. UPI or netbanking puts the account on **prepaid "available funds"**. The ad account's country and currency must match the payment method's. — [Meta Help: Accepted payment options](https://www.facebook.com/business/help/212763688755026); [Meta Help: manual payment methods](https://en-gb.facebook.com/business/help/311330675698510)
- **RBI e-mandate.** Since 2021, RBI requires an additional factor of authentication for recurring card payments. Auto-charges to Meta failed for many Indian cards and campaigns were paused. Google's help page cites per-transaction e-mandate ceilings of ₹15,000, and in a later version ₹5,000. Prepaid funds are deducted automatically, which avoids failures. A 2023 vendor note says some Indian banks still handle e-mandates badly. — [Velocity blog](https://blog.velocity.in/facebook-ads-blocked-it-could-be-because-of-the-rbis-new-guidelines/); [Google Ads help: RBI changes](https://support.google.com/google-ads/answer/10557975); [Mailgun help](https://help.mailgun.com/hc/en-us/articles/4409231431835)
- **Who bills.** Since Meta's local selling model, ads bought by Indian advertisers are billed by the Indian entity, **Facebook India Online Services Pvt Ltd**, in **INR**, with Indian GST. — [Meta Newsroom: Local selling model in India](https://about.fb.com/news/h/local-selling-model-in-india); [namomarketing.com 2026 guide](https://namomarketing.com/gst-on-google-ads-meta-ads-india/)
- **GST rate.** 18% on advertising services, SAC 998361. — [taxaj.com](https://www.taxaj.com/learn/?p=519)
  - One blog claims Meta charges no GST and the advertiser pays it under reverse charge. That conflicts with Meta's own statement about the local entity, so treat the blog as wrong for India-entity billing. — [savemyleads.com](https://www.savemyleads.com/blog/other/do-meta-ads-include-gst)
- **Entering the GSTIN.** Ad account admin → Payment settings → Business info. The account's business country must be India. Enter the 15-character GSTIN, business name and address. Sources disagree on whether this is required:
  - 360dialog says Meta won't accept a payment method without a valid GSTIN and prompts for it before the first purchase. — [360dialog: GST registration number](https://docs.360dialog.com/docs/resources/meta-business-manager/gst-registration-number)
  - namomarketing says it is optional but needed for input tax credit. — [namomarketing.com](https://namomarketing.com/gst-on-google-ads-meta-ads-india/)
  - Changing these details later may not update past invoices. — [watsspace.com](https://watsspace.com/blog/how-to-download-invoice-from-meta-ads/)
- **Getting invoices.** Business Manager / Billing & payments → Invoices (or Transactions/Payment activity). Pick a date range and download individual PDFs or "Download all invoices". A CSV export is available for reconciliation. — [Meta Help: View and download monthly invoices](https://en-gb.facebook.com/business/help/497115331725169); [watsspace.com](https://watsspace.com/blog/how-to-download-invoice-from-meta-ads/)
- **TDS — UNRESOLVED.** One blog says payments on Meta India invoices attract TDS under **s.194C**. A user-uploaded invoice references **2% TDS** on the pre-GST amount, which is consistent with 194C for a company payee. No Meta source was found. — [legalsuvidha.com](https://legalsuvidha.com/blog/facebook-ads-tds-refund-provisions); [Scribd user invoice (unofficial)](https://www.scribd.com/document/858535515/2380587694)
- **Equalisation Levy abolished.** The 6% levy on online advertising was **abolished from 1 Apr 2025** by the Finance Act 2025, so it is irrelevant now. It was also never relevant to INR billing by the Indian entity. — [YourStory](https://yourstory.com/2025/03/equalisation-levy-online-advertisements-abolished-google-meta-x-ads); [Social Samosa](https://www.socialsamosa.com/industry-updates/government-moves-abolish-6-equalisation-levy-online-ads-8888476)
- **Account spending limit.** Billing & payments → Payment settings → Account spending limit → "Set limit".
  - When the limit is reached, all campaigns stop spending but still show "Active".
  - Changes take about 15 minutes to apply.
  - The limit can't be set below about 10% above what has already been spent.
  - **It is not available for manual-payment (prepaid) accounts.**
  - Sources conflict on whether it is lifetime (Jon Loomer: lifetime, cumulative) or monthly.
  - — [Jon Loomer](https://www.jonloomer.com/campaign-spending-limits-account-spending-limits-daily-spending-limits/); [Orbee KB](https://kb.orbee.com/meta-ads-spending-limit)
- **Campaign spending limit.** A hard cap on a campaign's total spend. It doesn't change delivery. When reached, the campaign stops, which can look like a delivery problem. — [Jon Loomer](https://www.jonloomer.com/campaign-spending-limits-account-spending-limits-daily-spending-limits/); [theadspend.com](https://theadspend.com/blog/facebook-ads-not-spending)
- **Meta-imposed "daily spending limit".** Applied to new businesses, ad accounts or Pages, and after policy violations or low quality. It should rise over time while the account stays in good standing. **No source confirmed a specific starting figure** (the "$50/day" folklore is unverified). — [Jon Loomer glossary](https://www.jonloomer.com/glossary/daily-spending-limit/)
- **Budget flexibility.** Meta may spend **up to 75% over** a daily campaign budget on a given day, but no more than **7× the daily budget per week**. — [Jon Loomer](https://www.jonloomer.com/qvt/increased-budget-flexibility/)
- **Upfront charging (reported).** In Aug 2025 Meta reportedly began charging some advertisers upfront for the total campaign budget instead of at thresholds. — [Social Media Today](https://www.socialmediatoday.com/news/meta-changes-ad-budgets-charges-for-campaigns/758359/)
- **Risk on brand-new accounts.** Some new advertisers report accounts disabled on first use with no spend history. A declined or unverified payment method is cited as the most common trigger. — [Shopify community](https://community.shopify.com/t/facebook-banned-ad-account-on-my-first-day-need-help-to-appeal/64475); [adnova.ai](https://www.adnova.ai/blogs/facebook-ad-account-disabled)

### Inferences
- **Recommended setup for an MDF claim: a prepaid (available funds) INR account topped up via UPI or netbanking.** Reasons:
  - It avoids e-mandate card failures.
  - Each top-up produces a clean payment record.
  - Spend is capped by the funds loaded, which replaces the account spending limit that prepaid accounts lack.
  - Trade-off: someone must top up the balance, roughly ₹50k/day at plan pace, so ads don't stop for lack of funds.
  - If a corporate credit card is used instead, have the bank pre-register the e-mandate and raise the per-transaction ceiling. Also set an Account Spending Limit of about ₹22.5 lakh as a hard ceiling.
- **Pace check.** ₹22.4 lakh over 45 days is about ₹50k/day. A brand-new ad account may hit Meta's new-advertiser daily limit, so:
  - Launch on day 1 (26 Oct) with a smaller budget and ramp up.
  - Check Billing → "Daily spending limit" in the first week.
  - Underspending puts the MDF budget at risk, because only actual spend is reimbursed.
- **Currency and time zone.** Set INR and Asia/Kolkata at creation. **[UNVERIFIED]** Practitioners report that changing currency or time zone later creates a new ad account ID and closes the old one. That would split the campaign IDs and ad account IDs needed for the MDF claim.
- **Invoices as MDF receipts.** The GST tax invoices from Facebook India Online Services Pvt Ltd (PDF) plus the payment receipts or transaction CSV are the natural "receipts". Make sure the GSTIN, legal name and billing address match the Chat360 entity named in the MDF fund request.
- **Tax.** Agree the TDS treatment (194C at 2% is the likely default for a company payee) with the CA **before** the first payment. Under prepaid UPI, TDS is usually handled via Meta's TDS-refund or certificate process **[UNVERIFIED]**.

### Gaps
- No Meta source for the starting daily spending limit of a new Indian ad account in 2026.
- Not confirmed whether currency or time zone can be edited in place in 2026.
- Not confirmed whether a GSTIN is mandatory (360dialog) or optional (namomarketing).
- No official Meta position on TDS.
- Not confirmed whether Meta's Aug 2025 upfront-billing change applies to Indian prepaid accounts.

---

## Q3. Facebook Page, Instagram, WABA/number linking for CTWA; API number vs Business app; OBA, display name, messaging limits

### Takeaway
CTWA needs a **Facebook Page** (admin access) linked to a **WhatsApp Business number**. A Cloud API number from Chat360's own WABA is supported and preferred, because the AI agent can answer automatically and webhooks carry the CTWA click ID. Link the number to the Page and keep the Page, ad account and WABA in the same portfolio, or accept the cross-portfolio linking request. Since 7 Oct 2025 messaging limits apply to the whole portfolio, but CTWA conversations are **user-initiated** and are not bound by the business-initiated limit.

### Cited Findings
- **Basic requirements.** A Meta Business account, a Facebook Page, and a WhatsApp Business presence (Business app or WhatsApp Business Platform). Personal WhatsApp numbers can't be used. The WABA or number must be **associated with the Facebook Page** before the ads can be created. — [Infobip](https://www.infobip.com/blog/how-to-use-ads-that-click-to-whatsapp); [UChat guide](https://uchat.atlassian.net/wiki/x/FAFQLw)
- **Linking path.** You need admin rights on the Page → Page Settings → **WhatsApp / Linked accounts** → enter the number → confirm with the verification code. — [UChat guide](https://uchat.atlassian.net/wiki/x/FAFQLw)
- **Cross-portfolio linking.** If the Page and the WABA are in different Business Manager accounts, the **WABA owner must accept the binding request**. — [YCloud help](https://helpdocs.ycloud.com/help-center/ctwa-dian-ji-whatsapp-guang-gao/chuang-jian-dian-ji-whatsapp-guang-gao-ctwa)
- **Ad account readiness.** It needs a valid payment method, admin permissions and no restrictions. — [Woztell CTWA guide](https://support.woztell.com/portal/en/kb/articles/how-to-create-click-to-whatsapp)
- **Supported campaign objectives.** OUTCOME_ENGAGEMENT, OUTCOME_LEADS, OUTCOME_SALES and OUTCOME_TRAFFIC. The ad set's promoted object requires the **Page ID**; the WhatsApp number is optional. — [Meta Marketing API: Ads that Click to WhatsApp](https://developers.facebook.com/docs/marketing-api/ad-creative/messaging-ads/click-to-whatsapp)
- **API vs Business app.** Vendors recommend the API (Cloud API) for automation, reporting and scale. The app has limited automation and no advanced reporting. — [Woztell](https://support.woztell.com/portal/en/kb/articles/how-to-create-click-to-whatsapp); [Infobip](https://www.infobip.com/blog/how-to-use-ads-that-click-to-whatsapp)
- **Twilio caveat.** Twilio notes that for some older ISV accounts (registered on or before Mar 2022), each Page↔sender connection request needed approval. — [Twilio blog](https://www.twilio.com/en-us/blog/how-to-create-ads-that-click-to-whatsapp)
- **72-hour free entry point (FEP) window.** Conversations started from a CTWA ad open a 72-hour window in which eligible messages, reportedly including templates, are free. Sources differ on whether the business must reply within 24 hours to open it. — [SleekFlow](https://help.sleekflow.io/en_US/understanding-click-to-whatsapp-ads-ctwa-and-the-72-hour-free-window); [360dialog CTWA](https://docs.360dialog.com/docs/whatsapp-marketing/ads-that-click-to-whatsapp-ctwa-en); [Mastermind/HelpScout](https://mastermind.helpscoutdocs.com/article/916-workflow-trigger-click-to-whatsapp-ads)
- **Messaging limits (from 7 Oct 2025).** Limits are set per business portfolio and shared by all its numbers.
  - Unverified portfolios start at 250 unique users per 24h. Tiers are 250 → 2,000 → 10,000 → 100,000 → unlimited.
  - Upgrades need good quality and use of at least 50% of the current limit over 7 days. Some sources say evaluation runs every 6h.
  - Sources conflict on whether the first verified step is 1,000 or 2,000.
  - The limit counts business-initiated (template) conversations.
  - — [8x8](https://cpaas.8x8.com/en/blog/important-update-whatsapp-messaging-limits-changing-october-7-2025/); [Gallabox](https://gallabox.com/whatsapp-business-pricing-october-2025-update); [Bloomreach](https://documentation.bloomreach.com/engagement/docs/whatsapp-messaging-limits); [Blueticks](https://blueticks.co/blog/whatsapp-broadcast-limit)

### Inferences
- **Use a dedicated Cloud API number** on Chat360's own WABA for the campaign, for example a "Chat360 Sales AI" number. Before launch it needs:
  - a **display name that Meta has approved** and that matches the brand on the Page/ads; an "In review" or rejected name blocks sending
  - a business profile with logo, description, website and email
  - quality rating "Green"
  - the AI-agent flow wired to the webhook, including capture of `referral.ctwa_clid`
- **Official Business Account (blue/green check).** Nice to have for trust; not required for CTWA **[UNVERIFIED — no current source found on OBA as a CTWA requirement]**.
- **Instagram.** Link the professional account to the Page (Business Settings → Instagram accounts) so CTWA can run on Instagram placements. Without it, ads run on Instagram "as the Page" **[UNVERIFIED]**.
- **Page hygiene.** Make sure the Page has a profile and cover image, a "Software Company" category, website, some posts, and a clear name matching "Chat360". A thin Page raises review and trust risk for a new advertiser **[UNVERIFIED best practice]**.
- **Ads Manager path:** Campaign objective **Engagement** (or Leads) → Conversion location **"Messaging apps" → WhatsApp** → select the Page and the linked number → in the ad, set a **message template / greeting with ice-breakers** that triggers the AI agent.

### Gaps
- Could not read Meta's current Help Center article for the exact 2026 Page↔WhatsApp linking UI.
- Could not confirm the current FEP eligibility rule (the reply-within-24h condition) from Meta's pricing doc.
- No source on whether OBA or display-name status affects CTWA delivery.

---

## Q4. Datasets: Pixel, Conversions API, Conversions API for Business Messaging (WhatsApp), domain verification, AEM

### Takeaway
To optimise or measure CTWA beyond "conversations started", Chat360 should send **LeadSubmitted** (and optionally Purchase) events from its WhatsApp backend via **Conversions API for Business Messaging**. Each event needs the WABA-linked **dataset**, `action_source=business_messaging`, `messaging_channel=whatsapp`, and the **ctwa_clid** from the first inbound message. The token needs `whatsapp_business_management` + `whatsapp_business_manage_events`. A website Pixel and CAPI are useful for retargeting but not required for CTWA. AEM's eight-event setup and the domain-verification requirement were removed in 2023.

### Cited Findings
- **Required fields.** `action_source = business_messaging`, `messaging_channel = whatsapp`, and **ctwa_clid** inside `user_data`. The ctwa_clid comes from the `referral` object on the first inbound message. — [Meta: CAPI for Business Messaging onboarding guide](https://developers.facebook.com/docs/marketing-api/conversions-api/business-messaging); [Zernio docs](https://docs.zernio.com/whatsapp/send-whatsapp-conversion)
- **Cloud API recommended.** Meta recommends Cloud API for the integration. ctwa_clid is only available in the messages webhook on Business API v2.45.1+. — [Meta onboarding guide](https://developers.facebook.com/docs/marketing-api/conversions-api/business-messaging)
- **Dataset.** Retrieved or created per WABA via the **Dataset API**; events are POSTed to `/{dataset_id}/events`. — [Meta onboarding guide](https://developers.facebook.com/docs/marketing-api/conversions-api/business-messaging)
- **Access token.** Needs `whatsapp_business_management` and `whatsapp_business_manage_events`. Meta recommends reusing the Embedded Signup token where possible. Tokens can also be generated in Events Manager → dataset → Settings → Conversions API. Meta doesn't store them, so copy and save the token when it is generated. — [Infobip docs](https://www.infobip.com/docs/integrations/meta-ads-reporting-for-business-messaging); [Datahash docs](https://www.datahash.com/docs/signals/destinations/messaging-conversions/meta-whatsapp-conversions-api/)
- **Allowed event names.**
  - Standard **`Lead` is rejected** for business_messaging; use **`LeadSubmitted`**. Purchase is also accepted.
  - A Meta developer-forum error shows an event named 'LeadQualified' rejected as invalid, with Purchase and LeadSubmitted suggested instead.
  - Zernio lists LeadSubmitted, Purchase, AddToCart, InitiateCheckout and ViewContent.
  - Infobip's older integration supports only Purchase and LeadSubmitted.
  - — [Meta developer community thread](https://developers.secure.facebook.com/community/threads/1076478633997788); [Zernio](https://docs.zernio.com/whatsapp/send-whatsapp-conversion); [Infobip](https://www.infobip.com/docs/integrations/meta-ads-reporting-for-business-messaging)
- **Attribution window.** One source says 7 days from click. — [Zernio](https://docs.zernio.com/platforms/whatsapp/ctwa)
- **Page ID.** Sources conflict on whether `page_id` is needed for WhatsApp events. The forum example includes it. — [Zernio](https://docs.zernio.com/platforms/whatsapp/ctwa)
- **AEM.** The eight-event prioritisation and the domain-verification requirement for event configuration were removed (announced 2023). Domain verification is still recommended for link-ownership control. — [DEPT](https://www.deptagency.com/en-dk/insight/metas-removal-of-aggregated-event-measurement-aem-and-its-implications-for-advertisers/); [Jon Loomer](https://www.jonloomer.com/qvt/the-changes-to-aem-and-conversion-campaigns/); [Adviso](https://www.adviso.ca/en/blog/evolution-aggregated-measurement-meta)

### Inferences
- **Minimum before launch (about 1–3 dev days for a BSP):**
  1. In Events Manager, confirm or create the dataset tied to the campaign WABA and assign the ad account to it.
  2. Persist `ctwa_clid`, `source_id` (the ad ID) and `source_url` from webhook `referral` objects into the CRM. These map each lead to the campaign and ad IDs, which also helps MDF proof.
  3. Send `LeadSubmitted` when the AI agent captures a qualified enterprise lead (name, company, size). Optionally send `Purchase` on a closed deal.
  4. Test with the Test Events tool.
- Install a **Meta Pixel + CAPI** on chat360.io (PageView, Lead on demo form) for retargeting and lookalikes. Verify the domain in Brand Safety → Domains so link previews can't be edited by others. This is useful but not a launch blocker.
- AEM has no special relevance to India (it is an iOS 14.5 framework) and no longer needs configuring.

### Gaps
- Could not read Meta's current reference (developers.facebook.com blocked) to confirm the 2026 list of allowed business_messaging events or whether `page_id` is required for WhatsApp.

---

## Q5. Ad review, rejection risks, logos/UI in creatives, brand approval, partner badge, special ad categories / BFSI

### Takeaway
Review is usually **within 24 hours** but can run 48–72h or more for a new advertiser, so submit ads **2–3 days before 26 Oct**. Ads running on Meta's own surfaces go through Ad Review and **don't need separate brand-resource permission**. However, the MDF guide's rule that Meta logos need Meta brand approval, plus the "Partnering with Meta" page, mean any creative showing WhatsApp/Meta logos or claiming partnership must be pre-approved. WhatsApp's brand team quotes **2–3 weeks**, which is already too late for creatives that start on 26 Oct. Advertising **to** BFSI firms does not trigger the Financial category.

### Cited Findings
- **Review time.** Review starts automatically before delivery and "is typically completed within 24 hours, although it may take longer". Ads can be re-reviewed after launch. A violation leads to rejection and possible restriction of the account or its assets. — [Meta Transparency Center: Advertising Standards intro](https://transparency.meta.com/policies/ad-standards/)
- **Escalation and appeals.** Third-party guides suggest escalating via Meta Business Support if review exceeds about 48–72h, and requesting a second review for rejections. — [agrowth.io](https://agrowth.io/blogs/facebook-ads/fix-facebook-ads-in-review-too-long); [bir.ch](https://bir.ch/blog/facebook-ad-in-review)
- **Brand Resource Center.** "Advertising appearing on our products will be reviewed by our Ad Policy team and does not require permission here … All other forms of marketing do not require permission but must use the officially provided assets." — [Meta Brand Resource Center](https://www.meta.com/brand/resources/)
- **"Partnering with Meta".** Content featuring Meta, Facebook, Instagram or WhatsApp assets in a partnership context **requires prior approval**. Use only official files, primary brand/sub-brand, custom lockups via the Meta contact. — [Meta: Partnering with Meta](https://www.meta.com/brand/resources/meta/partnering-with-meta/)
- **WhatsApp brand rules.** Don't modify logos, colours, or combine the logo with other words or images. Permission requests "normally take 2–3 weeks". — [WhatsApp brand guidelines](https://www.meta.com/brand/resources/whatsapp/whatsapp-brand/)
- **Partner badge.** Third-party sources say it can be verified in Meta's partner directory. Usage rules are not public in the results. — [OnBrand](https://www.onbrand.co.uk/blog/meta-business-partner-agency/); [Stackmatix](https://www.stackmatix.com/blog/meta-business-partner-program)
- **India financial ads.** Since **31 Jul 2025**, ads in India promoting **securities and investments** must verify payer and beneficiary via SEBI registration, or identity/business verification for non-SEBI entities. Brand ads by banks and insurers, news and financial literacy are exempt from SEBI verification. — [Meta developers blog, 26 Jun 2025](https://developers.facebook.com/blog/post/2025/06/26/verification-and-transparency-requirements-for-advertisers-targeting-users-in-india-with-securities-and-investments-ads/); [MediaNama](https://www.medianama.com/2025/07/223-meta-sebi-verification-indian-investment-ads/); [Outlook Business](https://www.outlookbusiness.com/news/meta-mandates-sebi-verification-for-investment-ads-targeting-indian-users)
- **Special Ad Category name.** One blog says Meta now calls it "Financial and Insurance Products and Services". Not confirmed with Meta. — [Brandshark](https://brandshark.com/sebi-meta-special-ad-category-6-marketing-moves-financial-services-cant-ignore/)
- **Longer reviews.** Secondary sources say health and financial-services creative may take longer to review. — [seolocale](https://seolocale.com/how-long-does-meta-ad-review-take-tips-for-faster-approval/)

### Inferences
- **Special ad categories.** Chat360 is selling SaaS, not a financial, credit, housing or employment product, so it should declare **none**.
  - A BFSI-vertical ad such as "AI WhatsApp agent for NBFC collections" promotes software, not a financial product. It should not need the financial category or SEBI verification.
  - Avoid copy that reads like a loan or investment offer (e.g. "get instant loans"), which could misclassify the ad.
  - Similarly, healthcare and real-estate vertical ads must not imply medical claims or a housing offer. Housing would trigger the Housing special category, which restricts targeting.
- **Creative risk list for B2B SaaS / WhatsApp:**
  - Don't mock up WhatsApp UI with a fake "Meta verified" badge or official WhatsApp logo without approval.
  - Avoid "official WhatsApp partner"-style claims unless brand-approved.
  - Avoid personal-attribute phrasing ("Are you a struggling hospital admin?").
  - Avoid exaggerated ROI guarantees.
  - The landing experience (WhatsApp chat) must match the ad promise.
  - Use the plain WhatsApp word mark only per brand guidelines.
- **MDF-specific.**
  - **The MDF guide requires screenshots of execution showing Meta logos.** Start the Meta brand-approval request (via the Partner Manager / Partner Portal brand-approval flow) for any creative or landing page carrying Meta/WhatsApp logos or the partner badge **immediately**. At 2–3 weeks that runs past launch, so either launch first with logo-free creatives and add approved logo creatives later, or confirm a faster partner-track approval with the Meta Partner Manager.
  - **Confirm with the Partner Manager what "screenshots with Meta logos" means for an ads-only Path 1 activity.** It probably means the ad as it appears on Facebook, Instagram or WhatsApp, which inherently shows Meta surfaces.

### Gaps
- No official Meta source on Partner badge usage rules, or on the MDF-specific brand-approval turnaround.
- Meta's 2026 Special Ad Category list was not confirmed directly.

---

## Q6. What to submit to Meta (Partner Portal) for an MDF Path 1 claim

### Takeaway
No public Meta documentation on the Meta Business Partner MDF "Path 1" claim process was found. The program guide is behind the Partner Portal login. The claim pack below is built from the rules Chat360 already has plus how Meta billing exports work, and should be confirmed with the Partner Manager.

### Cited Findings
- Searches for Meta MDF / Path 1 / Partner Portal claims returned only generic MDF material (other vendors). It describes the standard pattern: pre-approval, then execution, then a claim with proof-of-execution package (invoices, performance reports) validated against the approved request. — [Zinfi glossary](https://www.zinfi.com/?p=41918); [Pega MDF guide](https://partners.pega.com/system/files?file=resources%2F2022-01%2Fpega-partners-program-market-development-funds-guide-jan-2022-v3.pdf); [Partner Standard](https://pro.partnerstandard.com/guides/market-development-funds-mdf)
- Meta's developer docs say Solution Partners are eligible for the Meta Business Partner SMB Accelerator Program (incentives, accreditation, enablement). No MDF or Incubate terms were found publicly. — [Meta: Solution Partner overview](https://developers.facebook.com/documentation/business-messaging/whatsapp/solution-providers/overview)
- Invoices can be downloaded as monthly PDFs (Billing → Invoices, date range, "Download all"). Transaction CSVs can be exported. — [Meta Help: View and download monthly invoices](https://en-gb.facebook.com/business/help/497115331725169); [watsspace.com](https://watsspace.com/blog/how-to-download-invoice-from-meta-ads/)

### Inferences — recommended claim pack (rules from Chat360's own MDF guide plus Meta tooling)
1. **IDs**
   - Partner Business (portfolio) ID: Business Settings → Business info.
   - Ad account ID (act_…): Ads Manager account dropdown.
   - Every campaign ID: Ads Manager → Columns → customise → add "Campaign ID".
   - The ad account must sit in the same portfolio as the partner business ID.
2. **Receipts**
   - All Facebook India Online Services GST tax invoices (PDF) for 26 Oct–9 Dec (and up to 15 Dec if any spend runs that late).
   - Payment receipts or UPI/netbanking transaction confirmations.
   - Billing "Payment activity" CSV.
   - Totals should reconcile to Ads Manager "Amount spent" (pre-GST). **[UNVERIFIED]** whether Meta reimburses GST-inclusive or GST-exclusive amounts; confirm, since GST is recoverable as ITC.
3. **Execution proof**
   - Ads Manager export (Reports → Export .xlsx/.csv) at campaign and ad level, with Campaign ID, Ad ID, date range, amount spent, impressions, reach, link clicks, "Messaging conversations started", and cost per conversation.
   - Dated screenshots of the live ads on Facebook, Instagram and WhatsApp-chat-open views. Ad previews via "Preview → Share" links or Ad Library snapshots also work.
   - Screenshots of campaigns in "Active" status showing dates.
   - Any Meta-logo creative screenshots, plus the brand-approval email.
4. **Timing**
   - Don't start any spend before the fund-request approval date. Campaign "Created" or "Start" dates must be on or after approval.
   - One claim per fund request, filed within 60 days of the request end date. With an end date of 9 Dec that means by about 7 Feb 2027; confirm the exact end date on the approved request.
   - Last run day is 15 Dec. Set campaign end dates in Ads Manager so no spend leaks past the approved window.
5. **Record-keeping**
   - Use a dedicated ad account, or at least a naming convention such as "MDF-FY26-P1-…", so only MDF campaigns appear in the claim.
   - Don't mix non-MDF spend into the same campaigns.

### Gaps
- **Key gap:** no public source on the exact Partner Portal claim form fields, file-format limits, whether GST is reimbursable, the reimbursement mechanism (ad credit vs bank payment), or how the 75% share is calculated. These must come from the MDF program guide in the Partner Portal or the Meta Partner Manager.

---

## Q7. India-specific gotchas (summary)

### Takeaway
The India-specific risks are: auto-charges on cards failing under the RBI e-mandate (use prepaid UPI/netbanking), the GSTIN missing from invoices, 194C TDS, and the payment method locked at account creation. The Equalisation Levy is gone since Apr 2025. The SEBI ad-verification rule applies only to investment and securities ads, not to SaaS sold to BFSI.

### Cited Findings
- **RBI e-mandate (2021).** Requires extra authentication for recurring card debits. Auto-charges to Meta failed and paused ads. Prepaid funds avoid this. — [Velocity](https://blog.velocity.in/facebook-ads-blocked-it-could-be-because-of-the-rbis-new-guidelines/); [Google Ads help](https://support.google.com/google-ads/answer/10557975)
- **Manual India methods** (UPI, netbanking, Paytm) only work on INR + India accounts and only if chosen at setup. — [Meta Help: Accepted payment options](https://www.facebook.com/business/help/212763688755026); [Meta Help: India](https://www.facebook.com/business/help/1410784518969094)
- **GST and the local seller.** Facebook India Online Services Pvt Ltd invoices in INR with 18% GST. ITC can be claimed if the GSTIN is on the invoice. — [Meta Newsroom](https://about.fb.com/news/h/local-selling-model-in-india); [namomarketing.com](https://namomarketing.com/gst-on-google-ads-meta-ads-india/)
- **TDS.** 194C per one blog; not confirmed by Meta. — [legalsuvidha.com](https://legalsuvidha.com/blog/facebook-ads-tds-refund-provisions)
- **Equalisation Levy** abolished from 1 Apr 2025. — [YourStory](https://yourstory.com/2025/03/equalisation-levy-online-advertisements-abolished-google-meta-x-ads)
- **SEBI verification** for securities and investment ads in India from 31 Jul 2025. — [Meta developers blog](https://developers.facebook.com/blog/post/2025/06/26/verification-and-transparency-requirements-for-advertisers-targeting-users-in-india-with-securities-and-investments-ads/)

### Inferences — consolidated pre-launch timeline (today = 11 Oct; launch = 26 Oct)

| Day | Step | Owner | Est. time |
|---|---|---|---|
| D0 (11–12 Oct) | Confirm the MDF fund request is **approved** in writing. Confirm the portfolio shows Verified. Add a 2nd admin and enforce 2FA. Ask the Partner Manager for the claim template and for brand approval of any Meta/WhatsApp logo creative. | Founder / partnerships | 1h + wait (brand approval 2–3 wks) |
| D0–1 | Create the ad account in the partner portfolio: India / INR / Asia/Kolkata. Choose **UPI/netbanking (prepaid)** or a corporate card with e-mandate. Enter GSTIN, legal name and address in Payment settings. Assign people and the system user. | Growth lead + finance | 30–60 min |
| D1–2 | Page hygiene; link Instagram. Link the campaign Cloud API number to the Page (Page Settings → Linked accounts → WhatsApp). Check display name approved, profile complete, quality Green. | Growth + WhatsApp ops | 1–2h; display-name review typically ~1–2 days **[UNVERIFIED]** |
| D1–5 | Dataset for WABA + CAPI for Business Messaging (LeadSubmitted). Capture `ctwa_clid` / `source_id` in the CRM. Pixel + CAPI on the website. Domain verification. | Engineering | 1–3 dev days |
| D3–7 | Build campaigns (Engagement → Messaging apps → WhatsApp), apply the MDF naming convention, set end dates ≤ 9 Dec. Set the Account Spending Limit (card) or top up funds (prepaid). | Growth | 1 day |
| D8–10 (by ~22 Oct) | Submit ads for review. Allow 24–72h, plus time to fix rejections. | Growth | 1–3 days |
| 26 Oct | Go live at a modest budget, ramp toward ~₹50k/day. Watch for a "daily spending limit" notice on the new account. Screenshot live ads for MDF proof each week. | Growth | ongoing |
| 9–15 Dec | Stop spend. Export invoices, payment receipts, Ads Manager reports and screenshots. File one claim within 60 days of the request end date. | Finance + partnerships | 1 day |

### Gaps
- No authoritative source on the display-name review SLA, the starting daily spend cap for new Indian ad accounts, TDS on Meta India invoices, or the MDF Path 1 claim form. All must be confirmed in-product, with the CA, or with the Meta Partner Manager.
