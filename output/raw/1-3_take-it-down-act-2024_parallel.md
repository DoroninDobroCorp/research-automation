# Take It Down Act (2024–2026): What Platforms Must Build Now to Meet the 48‑Hour NCII Takedown Rule

## Executive Summary

As of February 17, 2026, online platforms are in the final compliance sprint for the **TAKE IT DOWN Act** (Public Law 119-12), enacted on May 19, 2025. While the Act’s criminal provisions for individuals took effect immediately upon signing, the mandatory civil compliance deadline for "covered platforms" is **May 19, 2026**.

The Act establishes a strict federal floor for handling Non-Consensual Intimate Images (NCII) and AI-generated "digital forgeries." Unlike the flexible "expeditious" standard of the DMCA, this law imposes a hard **48-hour deadline** for removal upon valid notice. Failure to comply is treated as a *per se* violation of the Federal Trade Commission (FTC) Act, exposing platforms to civil penalties of up to ~$53,088 per violation.

**Key Strategic Insights:**
* **The Clock is Ticking:** Platforms have less than three months to finalize 24/7 intake queues, verify moderation workflows, and deploy duplicate detection systems before the May 19, 2026 enforcement date [1] [2].
* **AI is Explicitly Covered:** The Act codifies "digital forgeries" (deepfakes) as a specific category of NCII, applying a "reasonable person" indistinguishability standard that requires updated moderation guidelines [1] [3].
* **Dual-Track Enforcement:** While the DOJ prosecutes individuals (up to 2–3 years prison), the FTC enforces platform obligations. The Act uniquely expands FTC jurisdiction to non-profit organizations for these violations [1] [4].
* **"Reasonable Efforts" for Duplicates:** Platforms must not only remove the reported URL but also make reasonable efforts to remove "known identical copies," necessitating the use of hashing technologies (e.g., PDQ, PhotoDNA) [5] [3].
* **No Preemption:** The federal law does not preempt stricter state laws. Platforms must simultaneously navigate the federal 48-hour rule and state-level civil liability regimes in California, New York, and others [6] [7].

---

## 1. Statute, Structure, and Full Text

The **"Tools to Address Known Exploitation by Immobilizing Technological Deepfakes on Websites and Networks Act"** (TAKE IT DOWN Act) was enacted as **Public Law 119-12** on May 19, 2025 [8] [1]. It amends the Communications Act of 1934 (47 U.S.C. § 223) and creates new statutory obligations for online platforms.

### Enactment & Codification
* **Public Law:** 119-12 (139 Stat. 55) [1].
* **Codification:**
 * **47 U.S.C. § 223(h):** Establishes criminal prohibitions for intentional disclosure [1] [9].
 * **47 U.S.C. § 223a (note):** Establishes the civil "Notice and Removal" process for platforms [10] [5].

### Key Definitions
The Act introduces precise definitions that determine the scope of liability:
* **Digital Forgery:** An intimate visual depiction created via software, AI, or machine learning that is "indistinguishable from an authentic visual depiction" to a reasonable person [1] [3].
* **Intimate Visual Depiction:** Defined by reference to 15 U.S.C. § 6851 (sexual explicit conduct or nudity) [1] [3].
* **Consent:** Must be affirmative, conscious, and voluntary; consent to create an image does not imply consent to publish it [1] [3].
* **Identifiable Individual:** A person whose face, likeness, or distinguishing characteristic (e.g., unique birthmark) is displayed [1] [3].

---

## 2. Coverage & Exclusions: Are You a "Covered Platform"?

The Act applies broadly to services that host user-generated content (UGC), but it carves out specific infrastructure providers.

### The "Covered Platform" Test
A "covered platform" is any website, online service, or mobile application that:
1. **Serves the public**; AND
2. **Primarily provides a forum for UGC** (messages, videos, images, games, audio); OR
3. **Regularly publishes/hosts NCII** in the ordinary course of its trade or business [1] [5].

### Explicit Statutory Exclusions
The following are **exempt** from the platform notice-and-removal mandates (though criminal liability for individuals still applies):
* **Broadband Internet Access Services:** As defined in 47 CFR 8.1(b) [1] [5].
* **Electronic Mail (Email):** Services primarily providing email [1] [5].
* **Preselected Content Services:** Sites where content is primarily preselected by the provider (e.g., streaming services like Netflix) and interactive features (comments/chat) are merely incidental [5] [3].

**Strategic Note:** Mixed-service entities (e.g., a company offering both ISP services and a public web forum) must distinguish between these functions. The forum portion is likely covered, while the ISP portion is excluded [11].

---

## 3. Compliance Timeline

The Act creates a bifurcated timeline for implementation.

| Provision | Effective Date | Status (as of Feb 17, 2026) |
| :--- | :--- | :--- |
| **Criminal Prohibitions** (Individuals) | **May 19, 2025** | **Active.** DOJ can prosecute intentional disclosure now [2] [12]. |
| **Platform Notice & Removal** (Civil) | **May 19, 2026** | **Pending.** Platforms have <3 months to finalize systems [2] [5]. |

**Critical Milestones:**
* **Now (Feb 2026):** Finalize engineering for 48-hour removal workflows and duplicate detection.
* **March 2026:** Conduct "stress tests" of intake queues; train Trust & Safety staff on "digital forgery" recognition.
* **May 19, 2026:** Hard deadline for public-facing notice forms and full operational compliance [2] [13].

---

## 4. Notice & Takedown Procedures (48-Hour Requirement)

Section 3 of the Act mandates a rigorous removal process that exceeds voluntary industry standards.

### The 48-Hour Mandate
Upon receiving a valid removal request, a covered platform must remove the depiction **"as soon as possible, but not later than 48 hours"** after receipt [1] [5]. This is a strict liability standard for the timeline; "expeditious" removal (as in the DMCA) is not sufficient if it exceeds 48 hours.

### Valid Notice Requirements
To trigger the 48-hour clock, a notice must be in writing and include [5] [3]:
1. **Signature:** Physical or electronic signature of the identifiable individual (or authorized representative).
2. **Identification:** Information reasonably sufficient to locate the depiction (e.g., URLs).
3. **Statement of Belief:** A brief statement of "good faith belief" that the depiction is non-consensual.
4. **Contact Info:** Information to contact the requester.

### Duty to Remove Duplicates
Platforms must make **"reasonable efforts"** to identify and remove any **"known identical copies"** of the depiction [1] [5].
* **Interpretation:** This implies the use of hashing technology (e.g., MD5 for exact matches). While "reasonable efforts" is not defined, industry standards suggest perceptual hashing (like PDQ) is necessary to catch resized or re-encoded versions [14] [15].

### Transparency
Platforms must provide a **"clear and conspicuous notice"** of this process in **"plain language"** [5] [3].

---

## 5. Penalties for Non-Compliance

### Civil Penalties (Platforms)
Failure to reasonably comply with notice-and-takedown obligations is treated as a violation of a rule defining an **"unfair or deceptive act or practice" (UDAP)** under Section 18(a)(1)(B) of the FTC Act [1] [4].
* **Financial Risk:** Civil penalties are indexed for inflation, set at approximately **$53,088 per violation** as of 2025 [16] [17].
* **Jurisdiction:** The Act explicitly grants the FTC jurisdiction over **non-profit organizations** for these violations, closing a common enforcement gap [1] [4].

### Criminal Penalties (Individuals)
The Act amends 47 U.S.C. § 223 to impose federal criminal liability for intentional disclosure [1] [18]:
* **Adult Victims:** Up to **2 years** imprisonment.
* **Minor Victims:** Up to **3 years** imprisonment.
* **Threats:** Threats to publish digital forgeries carry up to **18 months** (adults) or **30 months** (minors).
* **Restitution:** Mandatory restitution to victims under 18 U.S.C. § 2264 [1] [3].

---

## 6. AI & "Digital Forgeries"

The Act is the first major federal law to explicitly regulate AI-generated deepfake pornography [19] [20].

### The "Indistinguishable" Standard
A "digital forgery" is covered if it is created via AI/ML and is **"indistinguishable from an authentic visual depiction"** to a **reasonable person** [1] [3].
* **Implication:** Obvious cartoons or low-quality edits may not be covered, but hyper-realistic AI generations are. Platforms must train moderators to apply this "reasonable person" test consistently.

### Operational Impact
Platforms cannot dismiss reports simply because an image is "fake." If it depicts an identifiable person and looks authentic, it triggers the same 48-hour removal duty as real NCII [21] [13].

---

## 7. Difference from Existing State NCII Laws

The federal Act does **not** preempt state laws [6] [7]. Platforms must comply with both the federal 48-hour rule and potentially stricter state civil liability regimes.

| Feature | Federal TAKE IT DOWN Act | California (Civ. Code § 1708.86) | New York (Civ. Rights Law § 52-b) |
| :--- | :--- | :--- | :--- |
| **Primary Focus** | Criminal & Regulatory (FTC) | Civil Liability & Private Right of Action | Civil Liability & Private Right of Action |
| **Deepfakes** | Covered ("Digital Forgery") | Covered ("Digitization") | Covered ("Digitization") |
| **Removal SLA** | **48 Hours** (Mandatory) | No specific hourly SLA; focuses on damages | Court orders for permanent removal |
| **Private Right of Action** | **No** (FTC enforcement only) | **Yes** (Statutory damages up to $150k) | **Yes** (Punitive & compensatory damages) |
| **Preemption** | No preemption clause | N/A | N/A |

**Insight:** Victims in states like CA and NY can sue platforms or perpetrators for damages, whereas the federal law primarily offers a mechanism for removal and regulatory fines [6] [22] [7].

---

## 8. Implementation Guidance from FTC/DOJ

As of February 17, 2026, formal implementation guidance is limited but emerging.

* **FTC Status:** The FTC has listed the statute in its Legal Library and requested **$10 million** in FY 2026 funding specifically to enforce it [4] [23].
 * **Guidance Gap:** No specific "Small Entity Compliance Guide" has been released yet.
 * **Data Collection:** An Information Collection Request (ICR) notice published on Feb 9, 2026, suggests the FTC is preparing reporting requirements for platforms [24].
* **DOJ/Sentencing:** The U.S. Sentencing Commission proposed amendments in Dec 2025 to incorporate the new offenses into sentencing guidelines (Section 2A6.1), treating them as high-level harassment [18].
* **Enforcement Posture:** FTC officials have stated they will be "prepared to enforce this statute on day one" (May 19, 2026) [25].

---

## 9. Compliance Checklist for Covered Platforms

To meet the May 19, 2026 deadline, platforms should implement the following:

### Governance & Policy
* [ ] **Update Terms of Service:** Explicitly prohibit NCII and "digital forgeries" [13].
* [ ] **Designate Owner:** Appoint a specific team or individual responsible for NCII compliance and FTC liaison [13].

### Intake & Triage
* [ ] **Create Reporting Form:** Build a dedicated, easy-to-find web form that captures all statutory requirements (signature, location/URL, good faith statement) [5] [26].
* [ ] **Verify Identity:** Implement a mechanism to verify the requester is the "identifiable individual" or their authorized representative (e.g., ID check or sworn statement) [5].

### Adjudication & Removal
* [ ] **48-Hour Workflow:** Configure ticketing systems to flag NCII reports as "Critical" with a hard 48-hour SLA countdown [5] [13].
* [ ] **Duplicate Detection:** Integrate hashing tools (e.g., PDQ, PhotoDNA) to scan for and remove "known identical copies" upon validating a report [5] [14].
* [ ] **Safe Harbor Documentation:** Log every removal decision and the "facts or circumstances" relied upon to qualify for the Act's "good faith" liability shield [3] [26].

### Transparency
* [ ] **Publish Notice:** Post a plain-language explanation of the removal process and platform responsibilities in a conspicuous location (e.g., Help Center) [5].

---

## 10. Technical Implementation: Duplicate Detection

The Act requires "reasonable efforts" to remove identical copies. Relying solely on exact-match hashing (MD5) is likely insufficient given industry standards.

* **Perceptual Hashing:** Use algorithms like **PDQ** (Meta) or **PhotoDNA** (Microsoft) to detect images that have been resized or re-encoded [14] [27].
* **Video Hashing:** Implement **TMK+PDQF** for video content to detect matches across different frame rates or resolutions [14].
* **Shared Databases:** Integrate with repositories like **StopNCII.org** (adults) and **NCMEC's Take It Down** (minors) to proactively detect known hashes [28] [29].
 * *Benchmark:* StopNCII processed over 1 million hashes by late 2024, with a >90% removal rate on participating platforms [30].

---

## 11. Privacy & Law Enforcement Coordination

* **Minors:** If NCII involves a minor, platforms **must** report it to the NCMEC CyberTipline immediately (18 U.S.C. § 2258A). This is a separate, mandatory obligation distinct from the 48-hour removal rule [31] [32].
* **Evidence Preservation:** Under 18 U.S.C. § 2703(f), platforms must preserve records for 90 days upon government request. Platforms should preserve evidence of removed NCII securely before deletion to comply with potential law enforcement requests [33] [34].
* **Data Minimization:** While the Act requires identifying info for the notice, platforms should minimize retention of victim data and use hashing to avoid storing raw NCII content longer than necessary [35].

## References

1. *PLAW-119publ12.xml*. https://www.govinfo.gov/bulkdata/PLAW/119/public/PLAW-119publ12.xml
2. *The TAKE IT DOWN Act: A Federal Law Prohibiting the Nonconsensual Publication of Intimate Images | Congress.gov | Library of Congress*. https://www.congress.gov/crs-product/LSB11314
3. *Public Law 119–12 119th Congress An Act*. https://www.congress.gov/119/plaws/publ12/PLAW-119publ12.pdf
4. *Tools to Address Known Exploitation by Immobilizing Technological Deepfakes on Websites and Networks Act ("TAKE IT DOWN Act") | Federal Trade Commission*. https://www.ftc.gov/legal-library/browse/statutes/tools-address-known-exploitation-immobilizing-technological-deepfakes-websites-networks-act-take-it
5. *Text - S.146 - 119th Congress (2025-2026): TAKE IT DOWN Act | Congress.gov | Library of Congress*. https://www.congress.gov/bill/119th-congress/senate-bill/146/text
6. *Congress’s Attempt to Criminalize Nonconsensual Intimate Imagery: The Benefits and Potential Shortcomings of the TAKE IT DOWN Act - National Association of Attorneys General*. https://www.naag.org/attorney-general-journal/congresss-attempt-to-criminalize-nonconsensual-intimate-imagery-the-benefits-and-potential-shortcomings-of-the-take-it-down-act/
7. * New York Civil Rights Law § 52-B (2025) - Private Right of Action for Unlawful Dissemination or Publication of an Intimate Image. :: 2025 New York Laws :: U.S. Codes and Statutes :: U.S. Law :: Justia*. https://law.justia.com/codes/new-york/cvr/article-5/52-b/
8. *Public Law 119 - 12 - Tools to Address Known Exploitation ...*. https://www.govinfo.gov/app/details/PLAW-119publ12
9. *47 USC 223: Obscene or harassing telephone calls in ...*. https://uscode.house.gov/view.xhtml?req=(title:47%20section:223%20edition:prelim)
10. *Notice and removal of nonconsensual intimate visual ...*. https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title47-section223a&num=0&edition=prelim
11. *TAKE IT DOWN Act [Public Law 119–12] [This ...*. https://www.govinfo.gov/content/pkg/COMPS-18158/pdf/COMPS-18158.pdf
12. *President Trump Signs Take It Down Act Into Law*. https://www.lw.com/en/insights/president-trump-signs-take-it-down-act-into-law
13. *TAKE IT DOWN Act Becomes Law, Introducing Landmark Federal Protections to Combat Online Exploitation and Deepfakes*. https://www.orrick.com/en/Insights/2025/05/TAKE-IT-DOWN-Act-Becomes-Law
14. *THE TMK+PDQF VIDEO-HASHING ALGORITHM AND THE ...*. https://raw.githubusercontent.com/facebook/ThreatExchange/main/hashing/hashing.pdf
15. *Bing Systemic Risk Assessment Report*. https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/August-2024-Microsoft-Bing-Systemic-Risk-Assessment-Report-EU-Digital-Services-Act.pdf
16. *The Take it Down Act: Federal Protections Against Digital Exploitation Bring Compliance Obligations for Online Platforms: Law Firm, Attorneys, Lawyers - Honigman*. https://www.honigman.com/the-matrix/the-take-it-down-act-federal-protections-against-digital-exploitation-bring-compliance-obligations-for-online-platforms
17. *Another Take on the TAKE IT DOWN Act | Perkins Coie*. https://perkinscoie.com/insights/blog/another-take-take-it-down-act
18. *Sentencing Guidelines for United States Courts*. https://www.federalregister.gov/documents/2025/12/19/2025-23473/sentencing-guidelines-for-united-states-courts
19. *President Trump Signs AI Deepfake Act into Law and House Passes AI Measures — AI: The Washington Report | Mintz - Antitrust Viewpoints - JDSupra*. https://www.jdsupra.com/legalnews/president-trump-signs-ai-deepfake-act-9585376/
20. *President Trump Signs AI Deepfake Act into Law and House Passes AI Measures — AI: The Washington Report | Mintz*. https://www.mintz.com/insights-center/viewpoints/54731/2025-05-22-president-trump-signs-ai-deepfake-act-law-and-house
21. *
        TAKE IT DOWN Act Targets Deepfakes: Are Online Platforms Caught in the Crosshairs? – Publications
    *. https://www.morganlewis.com/pubs/2025/06/take-it-down-act-targets-deepfakes-are-online-platforms-caught-in-the-crosshairs
22. * California Civil Code § 1708.86 (2025) :: 2025 California Code :: U.S. Codes and Statutes :: U.S. Law :: Justia*. https://law.justia.com/codes/california/code-civ/division-3/part-3/section-1708-86/
23. *Congressional Budget Justification Fiscal Year 2026*. https://www.ftc.gov/system/files/ftc_gov/pdf/fy-2026-cbj.pdf
24. *
      Federal Register
       :: 
      Information Collection Being Submitted for Review and Approval to Office of Management and Budget
    *. https://www.federalregister.gov/documents/2026/02/09/2026-02506/information-collection-being-submitted-for-review-and-approval-to-office-of-management-and-budget
25. *FTC shares insight into its children's privacy priorities | IAPP*. https://iapp.org/news/a/ftc-shares-insight-into-its-childrens-privacy-priorities
26. *'Take It Down Act' Requires Online Platforms To Remove ...*. https://www.skadden.com/insights/publications/2025/06/take-it-down-act
27. *Microsoft removes revenge porn from Bing search using new tool*. https://www.bleepingcomputer.com/news/security/microsoft-removes-revenge-porn-from-bing-search-using-new-tool/
28. *StopNCII.org Being Used to Protect 2,000,000 Images Online in the Fight Against Intimate Image Abuse*. https://swgfl.org.uk/magazine/stopncii-org-being-used-to-protect-2-000-000-images-online-in-the-fight-against-intimate-image-abuse/
29. *The Tech Coalition's Impact*. https://technologycoalition.org/mission/impact/
30. *Revenge Porn Helpline 2024 Report*. https://swgfl.org.uk/assets/documents/revenge-porn-helpline-2024-annual-report.pdf
31. *18 U.S. Code § 2258A - Reporting requirements of providers | U.S. Code | US Law | LII / Legal Information Institute*. https://www.law.cornell.edu/uscode/text/18/2258A
32. *18 U.S.C. § 2258A - Reporting requirements of providers*. https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title18-section2258A&num=0&edition=prelim
33. *18 U.S. Code § 2703 - Required disclosure of customer communications or records | U.S. Code | US Law | LII / Legal Information Institute*. https://www.law.cornell.edu/uscode/text/18/2703
34. *Obtaining and Admitting Electronic Evidence*. https://www.justice.gov/sites/default/files/usao/legacy/2011/11/30/usab5906.pdf
35. *Privacy Policy | StopNCII.org*. https://stopncii.org/privacy-policy/?lang=en-gb