# Section 230 and AI-Generated Adult Content (2024–2026): What Survives, What Doesn’t, and How to Operate Now

## Executive Summary

Between 2024 and early 2026, the legal shield provided by Section 230 of the Communications Decency Act has significantly eroded for platforms hosting AI-generated adult content. While the statute still protects neutral hosting of third-party files, courts and legislators have increasingly targeted the *creation* and *facilitation* aspects of generative AI. The passage of the **TAKE IT DOWN Act** in May 2025 established a federal criminal carve-out for non-consensual intimate imagery (NCII), mandating a strict 48-hour removal window that bypasses Section 230 immunity.

Simultaneously, courts are applying the "material contribution" test to AI features. Platforms that offer "nudify" presets or "spicy modes" are being treated as content developers rather than neutral intermediaries, stripping them of immunity. The legal landscape has bifurcated: platforms acting as passive hosts retain some protection, while those designing tools that facilitate the creation of illegal content face direct liability under product design and federal criminal statutes.

### Product Design Beats Publisher Immunity
Courts are increasingly distinguishing between "publisher" functions (which are immune) and "product design" flaws (which are not). The Ninth Circuit's reasoning in *Lemmon v. Snap* has been extended to AI, where the duty to design a reasonably safe product is separate from the duty to monitor content [1] [2]. For AI platforms, this means features that foreseeably encourage illegal acts—such as "undress" buttons or face-swap tools for real people—are treated as negligent design rather than protected speech [3].

### "Material Contribution" is the Fault Line
The "material contribution" test remains the primary judicial tool for piercing Section 230. Platforms lose immunity if they are "responsible, in whole or in part, for the creation or development" of unlawful content [4]. Courts have held that providing neutral tools (like a blank search bar) is protected, but designing systems that "induce" or "force" illegal inputs (like discriminatory dropdowns) constitutes development [5] [6]. In the context of AI, "spicy modes" or prompts structured to generate NCII are increasingly viewed as material contributions to illegality [7] [8].

### Federal Criminal Carve-Outs Are Active
The **TAKE IT DOWN Act** (2025) explicitly utilizes the Section 230(e)(1) exception for federal criminal law [9]. By criminalizing the publication of "digital forgeries" and mandating a 48-hour takedown process, Congress has removed the Section 230 shield for platforms that fail to act on verified reports of NCII [10]. This creates a strict liability regime for non-compliance, enforced by the FTC [11].

### Courts Sidestep "AI-as-Publisher" Rulings
Despite the focus on Section 230, recent major cases like *Walters v. OpenAI* (2025) have been resolved on traditional tort elements (e.g., lack of actual malice or damages) rather than a definitive ruling on whether AI outputs are protected third-party content [12] [13]. This suggests that while Section 230 is weakening, platforms can still win on the merits if they demonstrate robust safety measures and lack of intent.

---

## What Section 230 Does—and Doesn’t—Cover in the AI Era

The application of Section 230 to generative AI turns on whether the platform is merely a "host" of user prompts or a "creator" of the resulting output.

### Current Statutory Baseline and Carve-outs
Section 230(c)(1) states that "No provider or user of an interactive computer service shall be treated as the publisher or speaker of any information provided by another information content provider" [4]. This provides immunity for hosting third-party content. However, Section 230(e) lists explicit exceptions where immunity does not apply:
* **Federal Criminal Law:** Section 230(e)(1) states that "Nothing in this section shall be construed to impair the enforcement of... any other Federal criminal statute" [4]. This is the mechanism used by the TAKE IT DOWN Act to enforce liability for NCII.
* **Intellectual Property:** Section 230(e)(2) excludes intellectual property claims, a common vector for deepfake litigation involving right of publicity [4].
* **Sex Trafficking:** The FOSTA-SESTA amendments (Section 230(e)(5)) exclude civil and criminal claims related to sex trafficking [14].

Crucially, Section 230(c)(2) provides a "Good Samaritan" shield, protecting platforms from liability for "any action voluntarily taken in good faith to restrict access to or availability of material that the provider or user considers to be... objectionable" [4].

### Core Doctrines Courts Still Apply
Courts continue to rely on established pre-AI doctrines to adjudicate generative AI cases:

* **Material Contribution Test:** Established in *Fair Housing Council v. Roommates.com* (2008), this test holds that a platform becomes an "information content provider" (and loses immunity) if it "contributes materially to the alleged illegality of the conduct" [6]. If a platform's design "induces" users to create illegal content, it is liable [5].
* **Neutral Tools Doctrine:** Also from *Roommates.com*, this doctrine protects platforms that provide "neutral tools" for general use, even if users employ them for illegal purposes [6]. For example, a generic search bar is neutral; a dropdown menu forcing discriminatory choices is not [15].
* **Product Design Exception:** In *Lemmon v. Snap* (2021), the Ninth Circuit ruled that Section 230 does not bar claims based on a "duty to design a reasonably safe product" [2]. This distinguishes between the "publisher" role (deciding what to display) and the "manufacturer" role (designing the tool itself) [3].

---

## Case Law Deep Dives (2024–2026): What We Know from the Record

Recent litigation highlights how courts are navigating the intersection of AI, defamation, and non-consensual imagery without always issuing broad Section 230 rulings.

### Walters v. OpenAI, L.L.C. (Ga. Super. Ct., 2025)
This case is a critical bellwether for AI liability, even though it was resolved on state tort grounds.
* **Facts:** Radio host Mark Walters sued OpenAI for defamation after ChatGPT generated a "hallucinated" legal complaint accusing him of embezzlement [16] [17].
* **Ruling:** On May 19, 2025, the court granted summary judgment for OpenAI [18]. The court "declined to reach" the Section 230 question because the defamation claim failed on its merits [13].
* **Reasoning:**
 * **No Actual Malice:** As a public figure, Walters failed to prove OpenAI acted with "actual malice" (knowledge of falsity). The court accepted expert testimony that OpenAI takes steps to reduce hallucinations [12].
 * **Reasonable Reader:** The court found that a "reasonable reader" (a journalist familiar with AI) would not interpret the output as "actual facts" given the platform's disclaimers about accuracy [12] [13].
 * **No Damages:** Walters admitted in deposition that he suffered no actual financial harm [12].
* **Significance:** This case demonstrates that platforms can defeat liability through traditional defenses (lack of malice, disclaimers) without relying solely on Section 230, provided they can show "safety-by-design" efforts [19].

### Doctrinal Bookends Shaping AI Sexual Content Risk
While *Walters* addressed text, cases involving visual media establish stricter boundaries for sexual content:
* **United States v. Hotaling (2011):** The Second Circuit affirmed that child pornography created by digitally altering photographs of adults is not protected speech if it is indistinguishable from a real minor [20].
* **Doe v. Boland (2012):** The Sixth Circuit held that "morphing" the faces of identifiable children onto adult bodies violates federal law and is not protected by the First Amendment [21] [22].
* **United States v. Whorley (2008):** The Fourth Circuit ruled that obscene cartoons of minors are not protected, establishing that "virtual" depictions can still be criminal if they meet obscenity standards [23] [24].

These cases confirm that AI-generated CSAM or obscene deepfakes of minors are categorically unprotected, regardless of whether the "child" is real or synthetic.

---

## Mapping AI Design Choices to §230 Outcomes

The specific design of an AI tool determines its liability. Features that "neutralize" user intent retain immunity, while those that "enhance" or "solicit" illegality forfeit it.

### Feature Taxonomy vs. Likely §230 Posture

| Feature | Examples | Likely §230 Posture | Case/Doctrine Anchor | Risk-Lowering Design Step |
| :--- | :--- | :--- | :--- | :--- |
| **Open Text Prompt** | "Generate an image of a woman on a beach" | **Neutral Tool** (Immune) | *Roommates.com* (neutral tools) [6] | Implement default blocklists for sexual terms and non-consensual contexts. |
| **"Undress" Preset** | Button to remove clothes from an uploaded photo | **Material Contribution** (Liable) | *Roommates.com* (inducing illegality) [5] | Remove specific "undress" presets; block image-to-image edits on detected persons. |
| **Face-Swap Mode** | Swapping a user's face onto a pornographic video | **Material Contribution** (Liable) | *Doe v. Boland* (morphing) [22] | Require identity verification/consent for the target face; default deny for public figures. |
| **"Spicy Mode"** | Toggle to loosen safety filters for "edgy" content | **Design Defect** (Risk) | *Lemmon v. Snap* (negligent design) [1] | Avoid "modes" that broadly disable safety; use context-aware classifiers instead. |
| **Algorithmic Ranking** | Recommending "trending" deepfake content | **Neutral Tool** (Usually Immune) | *Force v. Facebook* (neutral ranking) [25] | Ensure ranking signals are content-neutral (e.g., engagement) and not based on the *illegal nature* of the content. |

### Practical Design Recommendations
* **Avoid Structured Illegality:** Do not provide dropdown menus, buttons, or presets that specifically facilitate the creation of non-consensual sexual imagery. If a tool is "designed to force subscribers to divulge... discriminatory preferences," it loses immunity [5].
* **Implement "Good Samaritan" Filters:** Section 230(c)(2) protects voluntary efforts to restrict objectionable material [4]. Platforms should document their content moderation policies and the technical measures (classifiers, hash matching) used to enforce them.
* **Transparency and Disclaimers:** As seen in *Walters*, clear warnings about the potential for inaccuracy or "hallucination" can defeat claims that the content asserts "actual facts" [12].

### Counterarguments and Defenses
* **"We Only Predict Tokens":** Platforms often argue they are merely predicting the next pixel or word based on user input. However, courts may view the *synthesis* of a new, defamatory, or illegal image as "development" if the AI adds material elements not present in the prompt [26].
* **"Users Are Solely Responsible":** While true for open tools, this defense fails if the platform "solicits" or "encourages" the illegal content, as seen in *FTC v. Accusearch* [27].

---

## First Amendment Boundaries for Synthetic Sexual Imagery

The First Amendment provides robust protection for speech, but it has clear limits regarding obscenity and child sexual abuse material (CSAM).

* **Adult Deepfakes:** Non-consensual deepfakes of adults are generally subject to tort liability (defamation, privacy, right of publicity) rather than criminal bans, unless they cross into obscenity or specific harassment statutes [28]. However, the **TAKE IT DOWN Act** criminalizes "digital forgeries" intended to cause harm, narrowing the First Amendment shield for malicious deepfakes [10].
* **Minors and Obscenity:** The Supreme Court's ruling in *New York v. Ferber* (1982) and subsequent circuit decisions (*Hotaling*, *Whorley*) establish that visual depictions of minors engaged in sexually explicit conduct are not protected speech [20] [23]. This applies to AI-generated images if they are "obscene" or depict an "identifiable minor" [22].
* **Virtual CSAM:** While *Ashcroft v. Free Speech Coalition* (2002) struck down a ban on "virtual" child porn that didn't use real children, the PROTECT Act (18 U.S.C. § 1466A) successfully criminalized "obscene" virtual depictions [29] [30].

---

## Risk Operations for AI Adult-Content Platforms

To operate within the current legal framework, platforms must adopt a "safety-by-design" approach that aligns with the **TAKE IT DOWN Act** and judicial expectations.

### Moderation and Escalation Workflows
* **48-Hour Takedown:** The TAKE IT DOWN Act mandates that covered platforms remove reported NCII within 48 hours of receiving a valid request [10]. Platforms must establish a dedicated channel for these reports.
* **Dual Gating:** Implement filters at both the *input* stage (blocking prompts like "naked [celebrity]") and the *output* stage (scanning generated images for nudity/CSAM) [31].
* **Real-Person Detection:** Use biometric or facial recognition technology to detect when a user attempts to modify an image of a real person, triggering additional consent checks or blocks [32].

### Documentation That Wins in Court
* **Safety Tuning Records:** Maintain logs of "red teaming" and safety training to demonstrate a lack of "actual malice" or negligence [12].
* **Incident Response Logs:** Document the timeline of every takedown request to prove compliance with the 48-hour mandate [11].
* **User Warnings:** Log user acknowledgments of terms of service and specific warnings about illegal content generation [33].

### Vendor and Tech Stack Options
* **Detection:** Vendors like **Reality Defender** and **Paravision** offer deepfake detection with low error rates [32].
* **Provenance:** Adopting **C2PA** standards (Content Credentials) helps verify the origin of media, though platforms must ensure metadata is not stripped during upload [34].
* **Hashing:** Utilize hash-matching databases (like those from NCMEC or IWF) to instantly block known illegal images [31].

### Insurance and Contracting
* **Coverage Gaps:** Insurers like **AXA XL** and **Chubb** are introducing specific endorsements for Generative AI risks, covering data poisoning and regulatory violations [35] [36]. Standard cyber policies may exclude "deepfake fraud" or AI-generated liability [37].
* **Safety Contingencies:** Coverage is increasingly contingent on demonstrating "safety-by-design" protocols, such as MFA and robust content moderation [38].

---

## Litigation and Enforcement Landscape Watchlist

The legal environment is dynamic, with several key indicators to watch in 2026–2028.

* **Circuit Split on Algorithms:** A "national chasm" exists between the Third Circuit (*Anderson v. TikTok*), which treats algorithmic recommendations as first-party speech (not immune), and the Ninth Circuit (*Doe v. Grindr*), which maintains broader immunity [39] [40]. The Supreme Court may resolve this split.
* **Product Defect Claims:** Plaintiffs are increasingly framing AI harms as "product defects" (negligent design) rather than "publisher" liability to bypass Section 230 [1].
* **FTC Enforcement:** The FTC has new authority under the TAKE IT DOWN Act to treat non-compliance as an unfair or deceptive act [11]. Expect aggressive enforcement against platforms that miss the 48-hour removal window.
* **State Laws:** States like Texas and California have enacted their own strict liability laws for AI deepfakes, creating a patchwork of compliance requirements [41] [42].

### Appendix: Quick-Reference Tables

#### Table: Doctrinal Anchors for Design
| Doctrine | Key Takeaway | Design Implication |
| :--- | :--- | :--- |
| **Zeran v. AOL (1997)** | Broad publisher immunity [43] | Don't treat notice as automatic liability; build consistent triage. |
| **Roommates.com (2008)** | Material contribution [5] | Eliminate modes that *induce* illegal inputs (e.g., "undress"). |
| **Dyroff (2019)** | Neutral recommendations [44] | Avoid recommender objectives that target non-consensual content. |
| **LeadClick (2016)** | Participation in deception [45] | Don't solicit or purchase workflows that produce unlawful content. |
| **Lemmon v. Snap (2021)** | Product design duty [2] | Run safety design reviews; document risk mitigations. |

#### Why This Matters Now
* **What’s Really Happening:** Courts are reapplying settled Section 230 doctrines to AI, focusing on whether features "develop" illegal content or constitute negligent design.
* **Why You Should Care:** If you build "nudify" or "face-swap" affordances, you move from host to creator, losing the shield and inviting criminal exposure.
* **What to Do Now:** Treat safety gating as product design, keep tools neutral, maintain Good Samaritan records, and prepare to win on classic tort elements via warnings and documented mitigation.

## References

1. *Lemmon v. Snap, Inc.: Ninth Circuit Chips Away at Tech Companies’ Section 230 Immunity - Harvard Journal of Law & Technology*. https://jolt.law.harvard.edu/digest/lemmon-v-snap-inc-ninth-circuit-chips-away-at-tech-companies-section-230-immunity
2. *Lemmon v. Snap Inc.*. https://cdn.ca9.uscourts.gov/datastore/opinions/2021/05/04/20-55295.pdf
3. *Section 230: An Overview - EveryCRSReport.com*. https://www.everycrsreport.com/reports/R46751.html
4. *47 USC 230: Protection for private blocking and screening ...*. https://uscode.house.gov/view.xhtml?req=(title:47%20section:230%20edition:prelim)
5. *Fair Housing Council of San Fernando Valley v. Roommates.com, LLC, 521 F.3d 1157 (9th Cir. 2008) | Electronic Frontier Foundation*. https://www.eff.org/issues/cda230/cases/fair-housing-council-san-fernando-valley-v-roommatescom
6. *  An Open Internet Law Casebook : Fair Housing Council of San Fernando Valley v. Roommates.com LLC   | H2O*. https://opencasebook.org/casebooks/409-an-open-internet-law-casebook/resources/7.5-fair-housing-council-of-san-fernando-valley-v-roommatescom-llc/
7. *Hundreds of nonconsensual AI images being created by Grok on X, data shows | Grok AI | The Guardian*. https://www.theguardian.com/technology/2026/jan/08/grok-x-nonconsensual-images
8. *The Policy Implications of Grok's 'Mass Digital Undressing Spree' | TechPolicy.Press*. https://techpolicy.press/the-policy-implications-of-groks-mass-digital-undressing-spree
9. *Text - S.146 - 119th Congress (2025-2026): TAKE IT DOWN Act | Congress.gov | Library of Congress*. https://www.congress.gov/bill/119th-congress/senate-bill/146/text
10. *S.146 - TAKE IT DOWN Act 119th Congress (2025-2026)*. https://www.congress.gov/bill/119th-congress/senate-bill/146
11. *Overview of FTC’s 2026 Children’s Privacy Focus: Expect Ongoing, if not More, Attention | Womble Bond Dickinson*. https://www.womblebonddickinson.com/us/insights/alerts/overview-ftcs-2026-childrens-privacy-focus-expect-ongoing-if-not-more-attention#:~:text=II.-,The%20TAKE%20IT%20DOWN%20Act,imagery%2C%20including%20imagery%20of%20minors.
12. *Walters v. OpenAI, L.L.C.*. https://www.loeb.com/en/insights/publications/2025/05/walters-v-openai-llc
13. *ChatGPT Defeats Defamation Lawsuit Over Hallucination-Walters v. OpenAI - Technology & Marketing Law Blog*. https://blog.ericgoldman.org/archives/2025/05/chatgpt-defeats-defamation-lawsuit-over-hallucination-walters-v-openai.htm
14. *47 USC 230: Protection for private blocking and screening ...*. https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title47-section230&num=0&edition=prelim
15. *FAIR HOUSING COUNCIL v. ROOMMATES.COM*. https://cdn.ca9.uscourts.gov/datastore/opinions/2008/04/02/0456916.pdf
16. *IN THE SUPERIOR COURT OF GWINNETT COUNTY ...*. https://medialaw.org/wp-content/uploads/2024/11/Opening-Brief-ISO-MSJ.pdf
17. *walters-openai-complaint-gwinnett-county.pdf*. https://www.courthousenews.com/wp-content/uploads/2023/06/walters-openai-complaint-gwinnett-county.pdf
18. *23-A-04860-2 5/19/2025 11:31 AM*. https://reason.com/wp-content/uploads/2025/05/WaltersvOpenAISJOrder.pdf
19. *Georgia Court Dismisses Defamation Claim Against OpenAI: A Win for AI Developers and Legal Clarity in Defamation Defense*. https://www.bfvlaw.com/georgia-court-dismisses-defamation-claim-against-openai-a-win-for-ai-developers-and-legal-clarity-in-defamation-defense/
20. *US v. Hotaling, 02/28/2011, 09-3935 - US 2nd Circuit*. https://caselaw.findlaw.com/summary/opinion/us-2nd-circuit/2011/02/28/254262.html
21. *                Doe v. Boland, No. 11-4237 (6th Cir. 2012) :: Justia    *. https://law.justia.com/cases/federal/appellate-courts/ca6/11-4237/11-4237-2012-11-09.html
22. *UNITED STATES COURT OF APPEALS*. https://cases.justia.com/federal/appellate-courts/ca6/11-4237/11-4237-2012-11-09.pdf?ts=1411026305
23. *US v. Whorley, 12/18/2008, 06-4288 - US 4th Circuit | FindLaw*. https://caselaw.findlaw.com/summary/opinion/us-4th-circuit/2008/12/18/157587.html
24. *UNITED STATES v. WHORLEY (2008) | FindLaw*. https://caselaw.findlaw.com/court/us-4th-circuit/1431669.html
25. *Force v. Facebook, Inc. - Wikipedia*. https://en.wikipedia.org/wiki/Force_v._Facebook,_Inc.
26. *Beyond the Search Bar: Generative AI’s Section 230 Tightrope Walk*. https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-november/beyond-search-bar-generative-ai-section-230-tightrope-walk/
27. *Paying for Nude Celebrities: Testing the Outer Limits of ...*. https://digitalcommons.law.uw.edu/cgi/viewcontent.cgi?article=1239&context=wjlta
28. *Deeply Fake, Deeply Disturbing, Deeply Constitutional: Why the First Amendment Likely Protects the Creation of Pornographic Deepfakes | Cardozo Law Review*. https://cardozolawreview.com/deeply-fake-deeply-disturbing-deeply-constitutional-why-the-first-amendment-likely-protects-the-creation-of-pornographic-deepfakes/
29. * Ashcroft v. Free Speech Coalition | 535 U.S. 234 (2002) | Justia U.S. Supreme Court Center*. https://supreme.justia.com/cases/federal/us/535/234/
30. * United States v. Williams | 553 U.S. 285 (2008) | Justia U.S. Supreme Court Center*. https://supreme.justia.com/cases/federal/us/553/285/
31. *Guidance A safer life online for women and girls*. https://www.ofcom.org.uk/siteassets/resources/documents/consultations/category-1-10-weeks/consultation-on-draft-guidance-a-safer-life-online-for-women-and-girls/statement-docs/guidance-a-safer-life-online-for-women-and-girls.pdf?v=408215
32. *2025 Deepfake Detection Market Report and Buyers Guide*. https://www.biometricupdate.com/wp-content/uploads/2025/11/BU-Deepfake-Detection-Market-Report-Buyers-Guide.pdf
33. *frequently asked questions*. https://www.meity.gov.in/static/uploads/2025/10/065b6deb585441b5ccdf8be42502a49c.pdf
34. *How digital forensics could prove what’s real in the age of deepfakes | Scientific American*. https://www.scientificamerican.com/article/how-digital-forensics-could-prove-whats-real-in-the-age-of-deepfakes/
35. *Gen AI endorsement for CyberRiskConnect*. https://axaxl.com/-/media/axaxl/files/pdfs/insurance/cyber-uk/axa-xl-cyberriskconnect-gen-ai-global-product-sheet.pdf?rev=1b5df87f39bf4bc98a3066c58fc6e0a8&sc_lang=en-gb&hash=D6C711F0DD771031751961EBC9D64604
36. *MediaGuard Insurance*. https://www.chubb.com/content/dam/chubb-sites/chubb-com/ca-en/business-insurance/mediaguard-by-chubb/documents/pdf/mediaguard-insurance.pdf
37. *The Deepfake Coverage Gap - InsuranceIndustry.AI*. https://insuranceindustry.ai/the-deepfake-coverage-gap/
38. *Deepfakes whitepaper*. https://axaxl.com/-/media/axaxl/files/pdfs/insurance/cyber-north-america/cyber_deepfakes-whitepaper_axa-xl_us.pdf?rev=f8b1ce21fd3b4059acaa7a04a365236e&sc_lang=pt&hash=1228CE34C222CEECBCBDD8DC48449AC5
39. *Supreme Court of the United States*. https://www.supremecourt.gov/DocketPDF/24/24-1202/374178/20250909165722399_24-1202%20Reply%20Brief.pdf
40. *                Anderson v. TikTok Inc, No. 22-3061 (3d Cir. 2024) :: Justia    *. https://law.justia.com/cases/federal/appellate-courts/ca3/22-3061/22-3061-2024-08-27.html
41. *Texas 89th Legislature: Key Artificial Intelligence Legislation – Jackson Walker*. https://www.jw.com/news/insights-texas-89th-legislature-ai/
42. *SB25-288 Intimate Digital Depictions Crim & Civil Actions | Colorado General Assembly*. https://leg.colorado.gov/bills/sb25-288
43. *                Kenneth M. Zeran, Plaintiff-appellant, v. America Online, Incorporated, Defendant-appellee, 129 F.3d 327 (4th Cir. 1997) :: Justia    *. https://law.justia.com/cases/federal/appellate-courts/F3/129/327/621462/
44. *                Dyroff v. The Ultimate Software Group, No. 18-15175 (9th Cir. 2019) :: Justia    *. https://law.justia.com/cases/federal/appellate-courts/ca9/18-15175/18-15175-2019-08-20.html
45. *2nd Circuit Denies Section 230 Immunity for Acts of Affiliate Marketers | Media Law Monitor | Davis Wright Tremaine*. https://www.dwt.com/blogs/media-law-monitor/2017/10/second-circuit-denies-section-230-immunity-for-act

---
## Sources

- [Zeran v. America Online, Inc. - Wikipedia](https://en.wikipedia.org/wiki/Zeran_v._America_Online,_Inc.)
- [                Fair Housing Council, et al v. Roommates.com, LLC, No. 04-56916 (9th Cir. 2008) :: Justia    ](https://law.justia.com/cases/federal/appellate-courts/ca9/04-56916/0456916-2011-02-25.html)
- [Page 89 TITLE 47—TELECOMMUNICATIONS § 230 and ...](https://www.govinfo.gov/link/uscode/47/230)
- [How Broad Is Web Publisher Immunity Under Â§230 of ...](https://www.floridabar.org/the-florida-bar-journal/how-broad-is-web-publisher-immunity-under-230-of-the-communications-decency-act-of-1996/)
- [Zeran v. AOL: Why the Fourth Circuit is Wrong - FindLaw](https://corporate.findlaw.com/law-library/zeran-v-aol-why-the-fourth-circuit-is-wrong.html)
- [Major court cases over the past 30 years involving Section ...](https://www.dailyjournal.com/articles/389669-major-court-cases-over-the-past-30-years-involving-section-230-of-the-communications-decency-act)
- [47 USC 230: Protection for private blocking and screening ...](https://uscode.house.gov/view.xhtml?req=(title:47%20section:230%20edition:prelim))
- [47 USC 230: Protection for private blocking and screening ...](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title47-section230&num=0&edition=prelim)
- [47 U.S. Code § 230 - Protection for private blocking and screening of offensive material | U.S. Code | US Law | LII / Legal Information Institute](https://www.law.cornell.edu/uscode/text/47/230)
- [U.S.C. Title 47 - TELECOMMUNICATIONS](https://www.govinfo.gov/content/pkg/USCODE-2020-title47/html/USCODE-2020-title47-chap5-subchapII-partI-sec230.htm)
- [Zeran v. America Online, Inc., 129 F.3d 327 (4th Cir. 1997) | Electronic Frontier Foundation](https://www.eff.org/issues/cda230/cases/zeran-v-america-online-inc)
- [Zeran v. America Online, Inc. (4th Cir.) (1997) | The First Amendment Encyclopedia](https://firstamendment.mtsu.edu/article/zeran-v-america-online-inc-4th-cir/)
- [                Kenneth M. Zeran, Plaintiff-appellant, v. America Online, Incorporated, Defendant-appellee, 129 F.3d 327 (4th Cir. 1997) :: Justia    ](https://law.justia.com/cases/federal/appellate-courts/F3/129/327/621462/)
- [published](https://www.ca4.uscourts.gov/opinions/published/971523.p.pdf)
- [Fair Housing Council of San Fernando Valley v. Roommates.com, LLC, 521 F.3d 1157 (9th Cir. 2008) | Electronic Frontier Foundation](https://www.eff.org/issues/cda230/cases/fair-housing-council-san-fernando-valley-v-roommatescom)
- [  An Open Internet Law Casebook : Fair Housing Council of San Fernando Valley v. Roommates.com LLC   | H2O](https://opencasebook.org/casebooks/409-an-open-internet-law-casebook/resources/7.5-fair-housing-council-of-san-fernando-valley-v-roommatescom-llc/)
- [FAIR HOUSING COUNCIL v. ROOMMATES.COM](https://cdn.ca9.uscourts.gov/datastore/opinions/2008/04/02/0456916.pdf)
- [Fair Housing Council of San Fernando Valley v. ...](https://www.dwt.com/insights/2008/06/fair-housing-council-of-san-fernando-valley-v-room)
- [interactive computer service from 47 USC § 230(f)(2)](https://www.law.cornell.edu/definitions/uscode.php?def_id=47-USC-1900800046-1237841278)
- [Fair Housing Council V. Roommates.com](http://www.btlj.org/data/articles2015/vol24/24_1_AR/24-berkeley-tech-l-j-0563-0592.pdf)
- [Fair Housing Council v. Roommates](http://files.grimmelmann.net/cases/Roommates.pdf)
- [47 U.S.C. 230 - Protection for private blocking and screening of offensive material - Content Details - USCODE-2011-title47-chap5-subchapII-partI-sec230](https://www.govinfo.gov/app/details/USCODE-2011-title47/USCODE-2011-title47-chap5-subchapII-partI-sec230)
- [IN THE SUPERIOR COURT OF GWINNETT COUNTY ...](https://medialaw.org/wp-content/uploads/2024/11/Opening-Brief-ISO-MSJ.pdf)
- [Georgia Court Dismisses Defamation Claim Against OpenAI: A Win for AI Developers and Legal Clarity in Defamation Defense](https://www.bfvlaw.com/georgia-court-dismisses-defamation-claim-against-openai-a-win-for-ai-developers-and-legal-clarity-in-defamation-defense/)
- [23-A-04860-2 5/19/2025 11:31 AM](https://images.assettype.com/barandbench/2025-06-19/0rtb594b/Mark_Walters_v_OpenAI_1750311692.pdf)
- [walters-openai-complaint-gwinnett-county.pdf](https://www.courthousenews.com/wp-content/uploads/2023/06/walters-openai-complaint-gwinnett-county.pdf)
- [IN THE SUPERIOR COURT OF GWINNETT COUNTY ...](https://medialaw.org/wp-content/uploads/2024/01/01.16.24walters.pdf)
- [Mark-Walters-v-OpenAI-23-A-04860-2-6-5-2023.pdf](https://cdn.arstechnica.net/wp-content/uploads/2023/06/Mark-Walters-v-OpenAI-23-A-04860-2-6-5-2023.pdf)
- [Walters v. OpenAI, L.L.C.](https://www.loeb.com/en/insights/publications/2025/05/walters-v-openai-llc)
- [Walters v. Open AI Memorandum of Law ISO MTD (State ...](https://reason.com/wp-content/uploads/2024/01/WaltersvOpenAIStateMTD.pdf)
- [23-A-04860-2 5/19/2025 11:31 AM](https://reason.com/wp-content/uploads/2025/05/WaltersvOpenAISJOrder.pdf)
- [Georgia Court Dismisses Defamation Suit Against AI ...](https://www.insideglobaltech.com/2025/06/16/georgia-court-dismisses-defamation-suit-against-ai-developer-openai/)
- [23-A-04860-2 4/15/2025 1:33 PM](https://firstamendment.law.uga.edu/wp-content/uploads/2025/04/Walters-Unsealing-Order.pdf)
- [Libel Lawsuit Filed in Georgia Against ChatGPT Parent Company OpenAI](https://firstamendmentwatch.org/libel-lawsuit-filed-in-georgia-against-chatgpt-parent-company-openai/)
- [Walters v. OpenAI: When AI Hallucinations Meet Defamation ...](https://daveadr.com/blog/disregardingmanifestdisregardagain-nwkfh)
- [Walters v. OpenAI](https://knowingmachines.org/knowing-legal-machines/legal-explainer/cases/walters-v-openai)
- [Walters v. OpenAI, L.L.C., 1:23-cv-03122 – CourtListener.com](https://www.courtlistener.com/docket/67617826/walters-v-openai-llc/)
- [ChatGPT Defeats Defamation Lawsuit Over Hallucination-Walters v. OpenAI - Technology & Marketing Law Blog](https://blog.ericgoldman.org/archives/2025/05/chatgpt-defeats-defamation-lawsuit-over-hallucination-walters-v-openai.htm)
- [Beyond Section 230: Principles for AI Governance - Harvard Law Review](https://harvardlawreview.org/print/vol-138/beyond-section-230-principles-for-ai-governance/)
- [
              Generative AI Meets Section 230: The Future of Liability and Its Implications for Startup Innovation | The University of Chicago Business Law Review
          ](https://businesslawreview.uchicago.edu/print-archive/generative-ai-meets-section-230-future-liability-and-its-implications-startup)
- [Courts test new frontier of defamation law as AI enters mix](https://minnlawyer.com/2025/11/17/ai-defamation-lawsuits-libel-liability/)
- [Notes Artificial Intelligence & Defamation Law](https://www.uclawjournal.org/wp-content/uploads/I-Note-Binder.pdf)
- [Deepfake Porn Lawsuit Exposes Alarming Legal Loopholes in ...](https://www.mexc.co/news/460860)
- [This N.J. girl was a victim of deepfake porn. She's suing the ...](https://www.nj.com/news/2026/01/this-nj-girl-was-a-victim-of-deepfake-porn-shes-suing-the-app-that-generated-it.html)
- [A New Jersey lawsuit shows how hard it is to fight ...](https://techcrunch.com/2026/01/12/a-new-jersey-lawsuit-shows-how-hard-it-is-to-fight-deepfake-porn/)
- [When AI Crosses the Line: Jane Doe v. ClothOff and Minors’ Digital Privacy](https://www.americanbar.org/groups/health_law/news/2025/when-ai-crosses-line-jane-doe-v-clothoff-minors-digital-privacy/)
- [Case 2:25-cv-16671 Document 1 Filed 10/16/25 Page 1 of ...](https://law.yale.edu/sites/default/files/area/center/isp/documents/2025.10.16-ecf-1-complaint.pdf)
- [Clinics File Suit Against Website that Generates Nonconsensual Nude Images | Yale Law School](https://law.yale.edu/yls-today/news/clinics-file-suit-against-website-generates-nonconsensual-nude-images)
- [Minor Sues Over ClothOff  AI That Turns Images Into ‘Hyperrealistic’ Porn - Mealey's](https://www.mealeys.com/mealeys/articles/2401619/minor-sues-over-clothoff-ai-that-turns-images-into-hyperrealistic-porn)
- [AI-Report-United-States.pdf](https://futurefreespeech.org/wp-content/uploads/2025/10/AI-Report-United-States.pdf)
- [Technology News 18.10.2025](https://www.bez-kabli.pl/technology-news-18-10-2025/)
- [Jane-Doe-v-ClothOff-Telegram-Complaint-10-16-25. ...](https://cdn.arstechnica.net/wp-content/uploads/2025/10/Jane-Doe-v-ClothOff-Telegram-Complaint-10-16-25.pdf)
- [DOE et al v. AI/ROBOTICS VENTURE STRATEGY 3 LTD et al
         2:2025cv16671        | U.S. District Court for the District of New Jersey        | Justia](https://dockets.justia.com/docket/new-jersey/njdce/2:2025cv16671/585002)
- [San Francisco files first-of-its-kind lawsuit to tackle AI deepfake nudes - POLITICO](https://www.politico.com/news/2024/08/17/san-francisco-lawsuit-ai-deepfake-nudes-00174487)
- [SF City Attorney's Office takes down websites spreading ...](https://www.nbcbayarea.com/news/local/san-francisco/sf-city-attorneys-office-deepfake-nudes/3821669/)
- [City Attorney shuts down 10 websites that create nonconsensual deepfake pornography – City Attorney of San Francisco](https://sfcityattorney.org/city-attorney-shuts-down-10-websites-that-create-nonconsensual-deepfake-pornography/)
- [City Attorney sues most-visited websites that create nonconsensual deepfake pornography – City Attorney of San Francisco](https://sfcityattorney.org/city-attorney-sues-most-visited-websites-that-create-nonconsensual-deepfake-pornography/)
- [
    Deepfake porn website operator settles with San Francisco, agrees to shut down - CBS San Francisco](https://www.cbsnews.com/sanfrancisco/news/san-francisco-deepfake-porn-lawsuit-settlement-briver-llc-shutdown/)
- [San Francisco Moves to Lead Fight Against Deepfake Nudes - The New York Times](https://www.nytimes.com/2024/08/15/us/deepfake-pornography-lawsuit-san-francisco.html)
- [1 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ...](https://www.sfcityattorney.org/wp-content/uploads/2024/08/Complaint_Final_Redacted.pdf)
- [Deepfake porn: San Francisco shuts down 10 of the world's ...](https://abc7news.com/post/deepfake-porn-san-francisco-shuts-down-10-worlds-most-visited-websites-using-ai-generate-explicit-content/16638231/)
- [Chiu-v-Sol-Ecom-6-13-25-Declaration-of-Karun-Tilak.pdf](https://cdn.arstechnica.net/wp-content/uploads/2025/07/Chiu-v-Sol-Ecom-6-13-25-Declaration-of-Karun-Tilak.pdf)
- [People of the State of California v. Sol Ecom, et al. | TechPolicy.Press](https://techpolicy.press/tracker/people-of-the-state-of-california-v-sol-ecom)
- [Digital Evidence and Deepfakes in the Age of AI](https://www.nawj.org/uploads/files/annual_conference/2024-annual-conference/fri845a-sgipsonrankinnawjhandout.pdf)
- [DAVID CHIU, SBN 189542 City Attorney](https://kernochan.law.columbia.edu/sites/kernochan.law.columbia.edu/files/content/2025%20Symposium/People%20v.%20Sol%20Ecom%20Inc%20(Briver%20Stipulated%20Final%20Judgment.PI).pdf)
- [Popular AI “nudify” sites sued amid shocking rise in victims globally - Ars Technica](https://arstechnica.com/tech-policy/2024/08/popular-ai-nudify-sites-sued-amid-shocking-rise-in-victims-globally/)
- ["People v. Sol Ecom" by California Superior Court](https://digitalcommons.law.scu.edu/historical/2869/)
- [People v. Sol Ecom Inc (Second Amended Complaint). ...](https://kernochan.law.columbia.edu/sites/kernochan.law.columbia.edu/files/content/2025%20Symposium/People%20v.%20Sol%20Ecom%20Inc%20(Second%20Amended%20Complaint).pdf)
- [People Of The State Of California, Acting By And Vs. Sol Ecom, Inc. Et Al Lawsuit | Trellis.Law](https://trellis.law/case/cgc24617237/people-state-california-acting-by-vs-sol-ecom-inc-et-al)
- [San Francisco secures $100K settlement, injunction in deepfake pornography case](https://www.dailyjournal.com/article/385943-san-francisco-secures-100k-settlement-injunction-in-deepfake-pornography-case)
- [analysis of SB 11](https://apcp.assembly.ca.gov/system/files/2025-07/sb-11-ashby-apcp-analysis.pdf)
- [Symposium 2025: Deepfakes: In Search of Global Solutions | Kernochan](https://kernochan.law.columbia.edu/content/symposium-2025-deepfakes)
- [AB 621 (Bauer-Kahan)](https://apcp.assembly.ca.gov/system/files/2025-03/ab-621-bauer-kahan.pdf)
- [2024-08-16-First-Amended-Complaint_Redacted.pdf](https://www.sfcityattorney.org/wp-content/uploads/2024/08/2024-08-16-First-Amended-Complaint_Redacted.pdf)
- [People v. Sol Ecom](https://digitalcommons.law.scu.edu/cgi/viewcontent.cgi?article=3871&context=historical)
- [San Francisco lawsuit goes after websites that create sexually explicit 'deepfakes' : NPR](https://www.npr.org/2024/08/16/nx-s1-5078574/san-francisco-lawsuit-goes-after-websites-that-create-sexually-explicit-deepfakes)
- [1 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ...](https://www.courthousenews.com/wp-content/uploads/2024/08/nudify-websites-lawsuit.pdf)
- [Global Freedom of Expression | Jones v. Dirty World Entm't Recordings LLC - Global Freedom of Expression](https://globalfreedomofexpression.columbia.edu/cases/jones-v-dirty-world-entmt-recordings-llc/)
- [FAIR HOUSING COUNCIL v. ROOMMATES.COM](https://cdn.ca9.uscourts.gov/datastore/opinions/2008/04/02/0456916.pdf)
- [Liability for Algorithmic Recommendations | Congress.gov | Library of Congress](https://www.congress.gov/crs-product/R47753)
- [brief in opposition](https://www.supremecourt.gov/DocketPDF/21/21-1333/229391/20220705140634781_Gonzalez%20Brief%20in%20Opposition.pdf)
- [Gonzalez v. Google, LLC](https://cdn.ca9.uscourts.gov/datastore/opinions/2021/06/22/18-16700.pdf)
- [reply brief](https://www.supremecourt.gov/DocketPDF/21/21-1333/230445/20220719235239080_GonzalezPetReplyPDF.pdf)
- [Force v. Facebook, Inc. - Wikipedia](https://en.wikipedia.org/wiki/Force_v._Facebook,_Inc.)
- [Fair Housing Council of San Fernando Valley v. Roommates.com, LLC - Wikipedia](https://en.wikipedia.org/wiki/Fair_Housing_Council_of_San_Fernando_Valley_v._Roommates.com,_LLC)
- [No Protection for Network Marketing Provider That Had ...](https://www.eyeonprivacy.com/2016/10/no-protection-for-network-marketing-provider-that-had-knowledge-and-authority-to-control-deceptive-conduct-of-affiliates/)
- [Second Circuit Holds Marketing Campaign Organizer Liable Under FTC Act for Deceptive Representations of Its Marketing “Affiliates” | Broadcast Law Blog](https://www.broadcastlawblog.com/2016/10/articles/second-circuit-holds-marketing-campaign-organizer-liable-under-ftc-act-for-deceptive-representations-of-its-marketing-affiliates/)
- [U.S. Circuit Court Finds Operator of Affiliate Marketing ...](https://www.ftc.gov/news-events/news/press-releases/2016/10/us-circuit-court-finds-operator-affiliate-marketing-network-responsible-deceptive-third-party-claims)
- [Does the FTC Get a Free Pass From Section 230?](https://blog.ericgoldman.org/archives/2016/09/does-the-ftc-get-a-free-pass-from-section-230-ftc-v-leadclick.htm)
- [Second Circuit Affirms Liability for Manager of Affiliate ...](https://www.manatt.com/insights/articles/2016/second-circuit-affirms-liability-for-manager-of-af)
- [Fair Housing Council of San Fernando Valley v. Roommates.com, LLC, 521 F.3d 1157 (9th Cir. 2008) | Electronic Frontier Foundation](https://www.eff.org/issues/cda230/cases/fair-housing-council-san-fernando-valley-v-roommatescom)
- [Fair Housing Coun., San Fernando v. Roommates. Com – CourtListener.com](https://www.courtlistener.com/opinion/1301306/fair-housing-coun-san-fernando-v-roommates-com/)
- [Jones v. Dirty World Entertainment Recordings LLC - Wikipedia](https://en.wikipedia.org/wiki/Jones_v._Dirty_World_Entertainment_Recordings_LLC)
- [                Jones v. Dirty World Entm't, No. 13-5946 (6th Cir. 2014) :: Justia    ](https://law.justia.com/cases/federal/appellate-courts/ca6/13-5946/13-5946-2014-06-16.html)
- [Sarah Jones v. Dirty World Entertainment Recordings LLC](https://www.opn.ca6.uscourts.gov/opinions.pdf/14a0125p-06.pdf)
- [Jones v. Dirty World Entertainment](https://digitalcommons.law.scu.edu/cgi/viewcontent.cgi?article=1630&context=historical)
- [2nd Circuit Denies Section 230 Immunity for Acts of Affiliate Marketers | Media Law Monitor | Davis Wright Tremaine](https://www.dwt.com/blogs/media-law-monitor/2017/10/second-circuit-denies-section-230-immunity-for-act)
- [                FTC v. LeadClick Media, LLC, No. 15-1009 (2d Cir. 2016) :: Justia    ](https://law.justia.com/cases/federal/appellate-courts/ca2/15-1009/15-1009-2016-09-23.html)
- [15-1009-cv FTC v. LeadClick Media, LLC](https://www.ftc.gov/system/files/documents/cases/160923leanspaopinion.pdf)
- [                Fair Housing Council, et al. v. Roommates.com, LLC, No. 09-55272 (9th Cir. 2012) :: Justia    ](https://law.justia.com/cases/federal/appellate-courts/ca9/09-55272/09-55272-2012-02-02.html)
- [Section 230 Immunity and the Roommates.com Case](https://cyberlaw.stanford.edu/blog/2008/05/section-230-immunity-and-roommatescom-case/)
- [Fair Housing Council V. Roommates.com](http://www.btlj.org/data/articles2015/vol24/24_1_AR/24-berkeley-tech-l-j-0563-0592.pdf)
- [Fair Housing Council of San Fernando Valley v. ...](https://www.dwt.com/insights/2008/06/fair-housing-council-of-san-fernando-valley-v-room)
- [Jones v. Dirty World Entm't Recordings LLC (Jones v. Dirty World Entm't Recordings LLC, 755 F.3d 398 (6th Cir. 2014)) - vLex United States
        ](https://case-law.vlex.com/vid/jones-v-dirty-world-891203850)
- [Dyroff v. Ultimate Software Group, Inc.](https://digitalcommons.law.ggu.edu/cgi/viewcontent.cgi?article=2242&context=ggulrev)
- [Snapchat Case May Offer Opening For Design Defect ...](https://www.daypitney.com/wp-content/uploads/c796d4b9fbb248bda99be291bffdb88a.pdf)
- [Section 230: An Overview | Congress.gov | Library of Congress](https://www.congress.gov/crs-product/R46751)
- [The Internet’s Wild West: Section 230 and Why Platforms Don’t Owe You Anything – NYU Journal of Intellectual Property & Entertainment Law](https://jipel.law.nyu.edu/the-internets-wild-west-section-230-and-why-platforms-dont-owe-you-anything/)
- [                Dyroff v. The Ultimate Software Group, No. 18-15175 (9th Cir. 2019) :: Justia    ](https://law.justia.com/cases/federal/appellate-courts/ca9/18-15175/18-15175-2019-08-20.html)
- [Lemmon v. Snap, Inc.: Ninth Circuit Chips Away at Tech Companies’ Section 230 Immunity - Harvard Journal of Law & Technology](https://jolt.law.harvard.edu/digest/lemmon-v-snap-inc-ninth-circuit-chips-away-at-tech-companies-section-230-immunity)
- [Section 230: An Overview - EveryCRSReport.com](https://www.everycrsreport.com/reports/R46751.html)
- [Lemmon v. Snap Inc.](https://cdn.ca9.uscourts.gov/datastore/opinions/2021/05/04/20-55295.pdf)
- [FTC v. LeadClick Media, LLC, 2016/09/23, 15-1009 - US 2nd Circuit | FindLaw](https://caselaw.findlaw.com/summary/opinion/us-2nd-circuit/2016/09/23/277574.html)
- [Attorney General Bonta Launches Investigation into xAI, Grok Over Undressed, Sexual AI Images of Women and Children | State of California - Department of Justice - Office of the Attorney General](https://oag.ca.gov/news/press-releases/attorney-general-bonta-launches-investigation-xai-grok-over-undressed-sexual-ai)
- [Grok blocked from undressing images with AI in places where it's illegal, X says | PBS News](https://www.pbs.org/newshour/world/grok-blocked-from-undressing-images-with-ai-in-places-where-its-illegal-x-says)
- [Grok's deepfake images which 'digitally undress' women ...](https://www.theguardian.com/technology/2026/jan/07/grok-deepfake-images-sexualise-women-children-investigated-australia-esafety)
- [X just paywalled Grok's deepfakes. They're still everywhere.](https://www.vox.com/future-perfect/474563/grok-x-ai-bikini-deepfake-liability-section-230)
- [Grok being used to create sexually violent videos featuring women, research finds | X | The Guardian](https://www.theguardian.com/technology/2026/jan/09/grok-ai-create-sexually-violent-videos-featuring-women-research-finds)
- [Opinion | Grok Is Undressing People Online. Here’s How to Fix It. - The New York Times](https://www.nytimes.com/2026/01/12/opinion/grok-digital-undressing.html)
- [
    Grok chatbot allowed users to create digitally altered photos of minors in "minimal clothing" - CBS News](https://www.cbsnews.com/news/grok-safeguard-lapses-minors-minimal-clothing-ai/)
- [The latest on Grok’s gross AI deepfakes problem | The Verge](https://www.theverge.com/news/859715/x-grok-ai-deepfakes)
- [Grok Is Generating Sexual Content Far More Graphic Than What's on X | WIRED](https://www.wired.com/story/grok-is-generating-sexual-content-far-more-graphic-than-whats-on-x/)
- [Hundreds of nonconsensual AI images being created by Grok on X, data shows | Grok AI | The Guardian](https://www.theguardian.com/technology/2026/jan/08/grok-x-nonconsensual-images)
- [Musk’s Grok AI Generated Thousands of Undressed Images Per Hour on X - Bloomberg](https://www.bloomberg.com/news/articles/2026-01-07/musk-s-grok-ai-generated-thousands-of-undressed-images-per-hour-on-x)
- [Grok’s "Spicy" AI Video Setting Will Lead to Sexual Abuse - RAINN](https://rainn.org/groks-spicy-ai-video-setting-will-lead-to-sexual-abuse-2026/)
- [Grok’s Image Generator Turns X Into a Deepfake Nudity Factory - Bloomberg](https://www.bloomberg.com/news/newsletters/2026-01-09/grok-s-image-generator-turns-x-into-a-deepfake-nudity-factory)
- [Musk’s Grok to bar users from generating sexual images of real people | Elon Musk News | Al Jazeera](https://www.aljazeera.com/news/2026/1/15/musks-grok-to-bar-users-from-generating-sexual-images-of-real-people)
- [Musk's xAI curbs sexually explicit image generation in Grok](https://www.dw.com/en/musks-xai-curbs-sexually-explicit-image-generation-in-grok/a-75511331)
- [Elon Musk’s Grok still being used to generate explicit images despite new safeguards, study finds | Euronews](https://www.euronews.com/next/2026/01/21/elon-musks-grok-still-being-used-to-generate-explicit-images-despite-new-safeguards-study-)
- [US senators demand answers from X, Meta, Alphabet, and others on sexualized deepfakes | TechCrunch](https://techcrunch.com/2026/01/15/us-senators-demand-answers-from-x-meta-alphabet-on-sexualized-deepfakes/)
- [Last year, our Take It Down Act became law to protect ...](https://www.facebook.com/RepMadeleineDean/posts/last-year-our-take-it-down-act-became-law-to-protect-americans-online-as-reports/1279174214035319/)
- [California AG launches investigation into X’s sexualized deepfakes | CyberScoop](https://cyberscoop.com/california-ag-investigates-xai-grok-nonconsensual-deepfakes-defiance-act/)
- [The Policy Implications of Grok's 'Mass Digital Undressing Spree' | TechPolicy.Press](https://techpolicy.press/the-policy-implications-of-groks-mass-digital-undressing-spree)
- [Grok 'undresses' women in a series of posts. It's not the first time.](https://www.usatoday.com/story/life/health-wellness/2026/01/06/grok-women-minors-social-media/88048266007/)
- [Elon Musk’s AI chatbot Grok under fire for failing to rein in ‘digital undressing’ | CNN Business](https://www.cnn.com/2026/01/08/tech/elon-musk-xai-digital-undressing)
- [Elon Musk says his AI tool Grok will be restricted from ...](https://www.facebook.com/VirginMediaNews/posts/elon-musk-says-his-ai-tool-grok-will-be-restricted-from-editing-or-generating-im/1293449329481353/)
- [India, EU investigate Musk's X after Grok created deepfake child porn](https://www.cnbc.com/2026/01/05/india-eu-investigate-musks-x-after-grok-created-deepfake-child-porn.html)
- [California investigates Grok over AI deepfakes](https://www.bbc.com/news/articles/cpwnqlpw7gxo)
- [Regulators around the world are scrutinizing Grok over sexual deepfakes | Malwarebytes](https://www.malwarebytes.com/blog/news/2026/01/regulators-around-the-world-are-scrutinizing-grok-over-sexual-deepfakes)
- [Elon Muskâs AI company xAI has imposed... - FRANCE 24 English | Facebook](https://www.facebook.com/FRANCE24.English/posts/elon-musks-ai-company-xai-has-imposed-limits-on-its-grok-chatbots-image-editing-/1189226293376745/)
- [ND AG Wrigley joins 34 states demanding action on AI deepfakes](https://www.valleynewslive.com/2026/01/27/nd-ag-wrigley-joins-34-states-demanding-action-ai-deepfakes/)
- [Why Grok restrictions won't stop society's latest AI scourge](https://www.rte.ie/news/primetime/2026/0118/1553516-grok-restrictions/)
- [Grok Is Pushing AI ‘Undressing’ Mainstream | WIRED](https://www.wired.com/story/grok-is-pushing-ai-undressing-mainstream/)
- [Elon Musk’s Grok A.I. Chatbot Made Millions of Sexualized Images, New Estimates Show - The New York Times](https://www.nytimes.com/2026/01/22/technology/grok-x-ai-elon-musk-deepfakes.html)
- [Washington Post - Elon Muskâs social media platform, X,... | Facebook](https://www.facebook.com/washingtonpost/posts/elon-musks-social-media-platform-x-announced-that-to-comply-with-local-laws-it-w/1254410663217473/)
- [
              Generative AI Meets Section 230: The Future of Liability and Its Implications for Startup Innovation | The University of Chicago Business Law Review
          ](https://businesslawreview.uchicago.edu/print-archive/generative-ai-meets-section-230-future-liability-and-its-implications-startup)
- [California orders Elon Musk company to stop explicit ...](https://calmatters.org/economy/technology/2026/01/california-investigates-deepfakes-elon-musk-company/)
- [Federal and State Regulators Target AI Chatbots and Intimate Imagery | Crowell & Moring LLP](https://www.crowell.com/en/insights/client-alerts/federal-and-state-regulators-target-ai-chatbots-and-intimate-imagery)
- [The TAKE IT DOWN Act’s 48-Hour Deadline: What Does It Mean When Section 230 Still Shields Platforms? – University of Baltimore Law Review](https://ubaltlawreview.com/2025/11/03/the-take-it-down-acts-48-hour-deadline-what-does-it-mean-when-section-230-still-shields-platforms/)
- [Text - H.R.6334 - 119th Congress (2025-2026): Deepfake Liability Act | Congress.gov | Library of Congress](https://www.congress.gov/bill/119th-congress/house-bill/6334/text)
- [Section 230 is Not Fit for AI - Brown Political Review](https://brownpoliticalreview.org/section-230-is-not-fit-for-ai/)
- [Grok AI Exploitation Crisis in Spicy Mode](https://www.lawyer-monthly.com/2026/01/grok-ai-spicy-mode-crisis/)
- [Recent Developments in Artificial Intelligence Cases and Legislation 2025](https://www.americanbar.org/groups/business_law/resources/business-law-today/2025-august/recent-developments-artificial-intelligence-cases-legislation/)
- [The Take It Down Act - Federal Law Addresses Online Abuse and Deepfakes - Roth Jackson](https://www.rothjackson.com/blog/2025/05/the-take-it-down-act-federal-law-addresses-online-abuse-and-deepfakes/)
- [ A Swift Response: Call to Action on Deepfake Non-Consensual Pornography](https://ktslaw.com/Blog/artificial%20intelligence%20and%20crypto/2024/3/a%20swift%20response)
- [Take It Down or Take It Too Far? The Legal Fallout of New ...](https://scholarship.law.unc.edu/cgi/viewcontent.cgi?article=1521&context=ncjolt)
- [Assessing Section 230 Reform Proposals in the 119th Congress - Public Knowledge](https://publicknowledge.org/assessing-section-230-reform-proposals-in-the-119th-congress/)
- [New Federal Law Targets Deepfakes and AI Nonconsensual Intimate I](https://natlawreview.com/article/take-it-down-act-signed-law-offering-tools-fight-non-consensual-intimate-images-and)
- [Appeals court questions Section 230 shield for social media | Virginia Lawyers Weekly](https://valawyersweekly.com/2026/01/07/appeals-court-section-230-social-media-lawsuits/)
- [AI-Report-United-States.pdf](https://futurefreespeech.org/wp-content/uploads/2025/10/AI-Report-United-States.pdf)
- [Case 4:22-md-03047-YGR Document 2480 Filed 11/21/ ...](https://www.lieffcabraser.com/pdf/2025-11-21-Brief-dckt-2480_0.pdf)
- [2026 Facial Abuse Lawsuit Guide: Victim Rights & Real Cases](https://bestlawyersinunitedstates.com/facial-abuse-lawsuit-explained-with-shocking-real-cases/)
- [The Policy Implications of Grok's 'Mass Digital Undressing Spree' | TechPolicy.Press](https://techpolicy.press/the-policy-implications-of-groks-mass-digital-undressing-spree)
- [                Artificial Intelligence and the Law | Communications and Internet Law Center | Justia    ](https://www.justia.com/communications-internet/artificial-intelligence-and-the-law/)
- [AI-Generated Child Sexual Abuse Material](https://stacks.stanford.edu/file/mn692xc5736/AI-CSAM-paper-2025-05-29.pdf)
- [artificial intelligence discovery & admissibility case law and ...](https://www.njcourts.gov/sites/default/files/attorneys/attorney-resources/airesources.pdf)
- [Lawmakers want to carve out intimate AI deepfakes from Section 230 immunity | U.S. Congressman Jake Auchincloss Of Massachusetts 4th District](https://auchincloss.house.gov/news/in-the-news/lawmakers-want-to-carve-out-intimate-ai-deepfakes-from-section-230-immunity)
- [Deepfake policy in the United States, 2019 - Present - Ballotpedia](https://ballotpedia.org/Deepfake_policy_in_the_United_States,_2019_-_Present)
- [Section 230 Immunity and Generative Artificial Intelligence | Congress.gov | Library of Congress](https://www.congress.gov/crs-product/LSB11097)
- [Section 230: Key Legal Cases | Electronic Frontier Foundation](https://www.eff.org/issues/cda230/legal)
- [Legislating Deepfakes and AI Tort Liability, Matthew Richardson, Jase Panebianco](https://briefings.brownrudnick.com/post/102lqka/legislating-deepfakes-and-ai-tort-liability)
- [S.146 - TAKE IT DOWN Act 119th Congress (2025-2026)](https://www.congress.gov/bill/119th-congress/senate-bill/146)
- [President Trump Signs Take It Down Act Into Law](https://www.lw.com/en/insights/president-trump-signs-take-it-down-act-into-law)
- [Take it Down Act Signed into Law, Offering Tools to Fight Non-Consensual Intimate Images and Creating a New Image Takedown Mechanism - Insights - Proskauer Rose LLP](https://www.proskauer.com/blog/take-it-down-act-signed-into-law-offering-tools-to-fight-non-consensual-intimate-images-and-creating-a-new-image-takedown-mechanism)
- [‘Take It Down Act’ Requires Online Platforms To Remove Unauthorized Intimate Images and Deepfakes When Notified | Insights | Skadden, Arps, Slate, Meagher & Flom LLP](https://www.skadden.com/insights/publications/2025/06/take-it-down-act)
- [Congress's Attempt to Criminalize Nonconsensual Intimate ...](https://www.naag.org/attorney-general-journal/congresss-attempt-to-criminalize-nonconsensual-intimate-imagery-the-benefits-and-potential-shortcomings-of-the-take-it-down-act/)
- [TAKE IT DOWN Act - Wikipedia](https://en.wikipedia.org/wiki/TAKE_IT_DOWN_Act)
- [Text - S.146 - 119th Congress (2025-2026): TAKE IT DOWN Act | Congress.gov | Library of Congress](https://www.congress.gov/bill/119th-congress/senate-bill/146/text)
- [TAKE IT DOWN Act - S.146 | TechPolicy.Press](https://techpolicy.press/tracker/take-it-down-act-s146)
- [The TAKE IT DOWN Act: A Federal Law Prohibiting the Nonconsensual Publication of Intimate Images | Congress.gov | Library of Congress](https://www.congress.gov/crs-product/LSB11314)
- [Nelson Mullins - The TAKE IT DOWN Act Targets AI-Generated and Authentic Nonconsensual Intimate Images](https://www.nelsonmullins.com/insights/blogs/ai-task-force/ai/ai-task-force-the-take-it-down-act-targets-ai-generated-and-authentic-nonconsensual-intimate-images)
- [Tools to Address Known Exploitation by Immobilizing Technological Deepfakes on Websites and Networks Act ("TAKE IT DOWN Act") | Federal Trade Commission](https://www.ftc.gov/legal-library/browse/statutes/tools-address-known-exploitation-immobilizing-technological-deepfakes-websites-networks-act-take-it)
- [Statutes | Federal Trade Commission](https://www.ftc.gov/legal-library/browse/statutes)
- [S.146 - 119th Congress (2025-2026): TAKE IT DOWN Act](https://www.congress.gov/bill/119th-congress/senate-bill/146/all-info)
- [US SB146 | 2025-2026 | 119th Congress | LegiScan](https://legiscan.com/US/bill/SB146/2025)
- [Overview of FTC’s 2026 Children’s Privacy Focus: Expect Ongoing, if not More, Attention | Womble Bond Dickinson](https://www.womblebonddickinson.com/us/insights/alerts/overview-ftcs-2026-childrens-privacy-focus-expect-ongoing-if-not-more-attention#:~:text=II.-,The%20TAKE%20IT%20DOWN%20Act,imagery%2C%20including%20imagery%20of%20minors.)
- [Public Law 119–12 119th Congress An Act](https://www.congress.gov/119/plaws/publ12/PLAW-119publ12.pdf)
- [TAKE IT DOWN Act [Public Law 119–12] [This ...](https://www.govinfo.gov/content/pkg/COMPS-18158/pdf/COMPS-18158.pdf)
- [TAKE IT DOWN Act signed into law | National Association of Counties](https://www.naco.org/news/take-it-down-act-signed-law)
- [S.146 - TAKE IT DOWN Act 119th Congress (2025-2026)](https://www.congress.gov/bill/119th-congress/senate-bill/146/titles)
- [The Take It Down Act Becomes Law: Combatting Revenge ...](https://www.pryorcashman.com/publications/the-take-it-down-act-becomes-law-combatting-revenge-porn-and-deepfakes-in-the-digital-age)
- [H.R. 6334: Deepfake Liability Act](https://www.govtrack.us/congress/bills/119/hr6334)
- [H.R.6334 - 119th Congress (2025-2026): Deepfake Liability Act | Congress.gov | Library of Congress](https://www.congress.gov/bill/119th-congress/house-bill/6334)
- [Text - H.R.6334 - 119th Congress (2025-2026): Deepfake Liability Act | Congress.gov | Library of Congress](https://www.congress.gov/bill/119th-congress/house-bill/6334/text)
- [New Deepfake Liability Act to push against abusive AI images – Deseret News](https://www.deseret.com/politics/2025/12/03/reps-maloy-and-auchincloss-introduce-deepfake-liability-act/)
- [
	Maloy and Auchincloss Introduce Deepfake Liability Act | U.S. Representative Celeste Maloy
](https://maloy.house.gov/news/documentsingle.aspx?DocumentID=1798)
- [A BILL](https://www.commerce.senate.gov/services/files/A42A827D-03B5-4377-9863-3B1263A7E3B2)
- [Establishing Legal Incentives to Hold Big Tech Accountable | TechPolicy.Press](https://techpolicy.press/establishing-legal-incentives-to-hold-big-tech-accountable)
- [Auchincloss, Maloy introduce bipartisan bill carving out bots & deepfakes from social media platforms' Section 230 liability shield | U.S. Congressman Jake Auchincloss Of Massachusetts 4th District](https://auchincloss.house.gov/media/press-releases/auchincloss-maloy-introduce-bipartisan-bill-on-section-230-liability-shield)
- [Text - S.1829 - 119th Congress (2025-2026): STOP CSAM Act of 2025 | Congress.gov | Library of Congress](https://www.congress.gov/bill/119th-congress/senate-bill/1829/text)
- [
              Generative AI Meets Section 230: The Future of Liability and Its Implications for Startup Innovation | The University of Chicago Business Law Review
          ](https://businesslawreview.uchicago.edu/print-archive/generative-ai-meets-section-230-future-liability-and-its-implications-startup)
- [Section 230: An Overview | Congress.gov | Library of Congress](https://www.congress.gov/crs-product/R46751)
- [Durbin, Graham Introduce Bill To Sunset ... | United States Senate Committee on the Judiciary](https://www.judiciary.senate.gov/press/dem/releases/durbin-graham-introduce-bill-to-sunset-section-230-immunity-for-tech-companies-protect-americans-online)
- [US Congress HR6334 - Deepfake Liability Act](https://trackbill.com/bill/us-congress-house-bill-6334-deepfake-liability-act/2753268/)
- [Text - S.3546 - 119th Congress (2025-2026): Sunset Section 230 Act | Congress.gov | Library of Congress](https://www.congress.gov/bill/119th-congress/senate-bill/3546/text)
- [Platforms Face Section 230 Shift From Take It Down Act](https://www.troutman.com/insights/platforms-face-section-230-shift-from-take-it-down-act/)
- [Durbin, Graham Introduce Bill To Sunset Section 230 Immunity For Tech Companies, Protect Americans Online | U.S. Senator Dick Durbin of Illinois](https://www.durbin.senate.gov/newsroom/press-releases/durbin-graham-introduce-bill-to-sunset-section-230-immunity-for-tech-companies-protect-americans-online)
- [Federal Bills - Enough Abuse](https://enoughabuse.org/get-vocal/federal-bills/)
- [119th Congress (2025-2026): Deepfake Liability Act](https://www.congress.gov/bill/119th-congress/house-bill/6334/actions)
- [Lawmakers Unveil New Bills to Curb Big Tech’s Power and Profit | U.S. Congressman Jake Auchincloss Of Massachusetts 4th District](https://auchincloss.house.gov/media/in-the-news/lawmakers-unveil-new-bills-to-curb-big-techs-power-and-profit)
- [U.S. Representative Celeste Maloy - House.gov](https://maloy.house.gov/)
- [Should online platforms face legal consequences for ...](https://www.stgeorgeutah.com/news/should-online-platforms-face-legal-consequences-for-abusive-deepfakes-this-utah-rep-says-yes/article_57fb452e-83a9-400c-a821-38fee8426b9f.html)
- [All Info - H.R.6334 - 119th Congress (2025-2026): Deepfake Liability Act | Congress.gov | Library of Congress](https://www.congress.gov/bill/119th-congress/house-bill/6334/all-info)
- [Cosponsors - H.R.6334 - 119th Congress (2025-2026): Deepfake Liability Act | Congress.gov | Library of Congress](https://www.congress.gov/bill/119th-congress/house-bill/6334/cosponsors)
- [Press Releases | Newsroom | U.S. Congressman Jake Auchincloss Of Massachusetts 4th District](https://auchincloss.house.gov/media/press-releases)
- [
	News List | U.S. Representative Celeste Maloy
](https://maloy.house.gov/news/documentquery.aspx?DocumentTypeID=27)
- [Maloy and Auchincloss Introduce Deepfake Liability Act in ...](https://www.quiverquant.com/news/Press+Release%3A+Maloy+and+Auchincloss+Introduce+Deepfake+Liability+Act+in+Congress)
- [Latest News | U.S. Representative Celeste Maloy - House.gov](https://maloy.house.gov/news/)
- [Section 230: An Overview | Congress.gov | Library of Congress](https://www.congress.gov/crs-product/R46751)
- [Tech Regulation Digest: Sunsetting Section 230—The Future of Content Moderation, Ads, and AI | Milken Institute](https://milkeninstitute.org/content-hub/collections/articles/tech-regulation-digest-sunsetting-section-230-future-content-moderation-ads-and-ai)
- [[Document title] - Speaker.gov](https://www.speaker.gov/wp-content/uploads/2024/12/AI-Task-Force-Report-FINAL.pdf)
- [Digital Replicas, Part I: Defining the Harms - Public Knowledge](https://publicknowledge.org/digital-replicas-part-i-defining-the-harms/)
- [Take It Down or Take It Too Far? The Legal Fallout of New ...](https://scholarship.law.unc.edu/cgi/viewcontent.cgi?article=1521&context=ncjolt)
- [Section 230: A Brief Overview | Congress.gov | Library of Congress](https://www.congress.gov/crs-product/IF12584)
- [S.3696 - 118th Congress (2023-2024): DEFIANCE Act of 2024 | Congress.gov | Library of Congress](https://www.congress.gov/bill/118th-congress/senate-bill/3696)
- [Text - S.3696 - 118th Congress (2023-2024): DEFIANCE Act of 2024 | Congress.gov | Library of Congress](https://www.congress.gov/bill/118th-congress/senate-bill/3696/text)
- [Durbin, Graham, Reps. Ocasio-Cortez & Lee Introduce ...](https://www.durbin.senate.gov/newsroom/press-releases/durbin-graham-reps-ocasio-cortez-and-lee-introduce-bipartisan-legislation-to-combat-non-consensual-sexually-explicit-deepfake-imagery)
- [US Congress S3696 - DEFIANCE Act of 2024](https://trackbill.com/bill/us-congress-senate-bill-3696-defiance-act-of-2024/2503027/)
- [DEFIANCE Act of 2024](https://www.durbin.senate.gov/download/defiance-act-of-2024)
- [Durbin, Graham, Klobuchar, Hawley Introd... | United States Senate Committee on the Judiciary](https://www.judiciary.senate.gov/press/releases/durbin-graham-klobuchar-hawley-introduce-defiance-act-to-hold-accountable-those-responsible-for-the-proliferation-of-nonconsensual-sexually-explicit-deepfake-images-and-videos)
- [📱 Tech: DEFIANCE Act prospects](https://www.axios.com/pro/tech-policy/newsletters/2024/09/19/tech-defiance-act-prospects)
- [All Info - S.3696 - 118th Congress (2023-2024): DEFIANCE Act of 2024 | Congress.gov | Library of Congress](https://www.congress.gov/bill/118th-congress/senate-bill/3696/all-info)
- [S.1993 - 118th Congress (2023-2024): A bill to waive immunity under section 230 of the Communications Act of 1934 for claims and charges related to generative artificial intelligence. | Congress.gov | Library of Congress](https://www.congress.gov/bill/118th-congress/senate-bill/1993)
- [Bipartisan Energy and Commerce Leaders Announce ...](https://energycommerce.house.gov/posts/bipartisan-energy-and-commerce-leaders-announce-legislative-hearing-on-sunsetting-section-230)
- [AI-Generated Deepfakes and the Emerging Legal Landscape](https://perkinscoie.com/insights/blog/ai-generated-deepfakes-and-emerging-legal-landscape)
- [Copyright and Artificial Intelligence, Part 1: Digital Replicas](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-1-Digital-Replicas-Report.pdf)
- [Energy and Commerce Leaders Unveil Bipartisan Draft Legislation to Sunset Section 230](https://energycommerce.house.gov/posts/energy-and-commerce-leaders-unveil-bipartisan-draft-legislation-to-sunset-section-230)
- [US SB3696 | 2023-2024 | 118th Congress | LegiScan](https://legiscan.com/US/bill/SB3696/2023)
- [
			The Senate unanimously passed the DEFIANCE Act, a bill to address and prevent non-consensual deepfake pornography — SVPA		](https://s-v-p-a.org/defiance-passed-senate/)
- [Ocasio-Cortez, Lee, Durbin, Graham Introduce Bipartisan ...](http://ocasio-cortez.house.gov/media/press-releases/ocasio-cortez-lee-durbin-graham-introduce-bipartisan-bicameral-legislation)
- [
			Pass the DEFIANCE Act - End Deepfake Porn — SVPA		](https://s-v-p-a.org/defiance/)
- [Congress’s Attempt to Criminalize Nonconsensual Intimate Imagery: The Benefits and Potential Shortcomings of the TAKE IT DOWN Act - National Association of Attorneys General](https://www.naag.org/attorney-general-journal/congresss-attempt-to-criminalize-nonconsensual-intimate-imagery-the-benefits-and-potential-shortcomings-of-the-take-it-down-act/)
- [Ocasio-Cortez, Lee Join House Members and Advocates in Calling to Pass DEFIANCE Act | Representative Ocasio-Cortez](http://ocasio-cortez.house.gov/media/press-releases/ocasio-cortez-lee-join-house-members-and-advocates-calling-pass-defiance-act)
- [Defiance Act: Paris Hilton's push against deepfakes](https://thehill.com/policy/technology/5702191-paris-hilton-calls-for-deepfake-law/)
- [Iconic: Laurel Lee champions bill to protect victims of deepfake porn alongside Paris Hilton, Alexandria Ocasio-Cortez](https://floridapolitics.com/archives/775540-iconic-laurel-lee-champions-bill-to-protect-victims-of-deepfake-porn-alongside-paris-hilton-alexandria-ocasio-cortez/)
- [Cosponsors - S.3696 - 118th Congress (2023-2024): DEFIANCE Act of 2024 | Congress.gov | Library of Congress](https://www.congress.gov/bill/118th-congress/senate-bill/3696/cosponsors)
- [Durbin Applauds Senate Passage Of His Bi... | United States Senate Committee on the Judiciary](https://www.judiciary.senate.gov/press/dem/releases/durbin-applauds-senate-passage-of-his-bipartisan-bill-to-tackle-nonconsensual-sexually-explicit-deepfakes)
- [Durbin Celebrates Passage Of His Bill To Tackle Nonconsensual, Sexually-Explicit Deepfakes In Speech On The Senate Floor | U.S. Senator Dick Durbin of Illinois](https://www.durbin.senate.gov/newsroom/press-releases/durbin-celebrates-passage-of-his-bill-to-tackle-nonconsensual-sexually-explicit-deepfakes-in-speech-on-the-senate-floor)
- [Senate passes DEFIANCE Act to deal with sexually explicit deepfakes](https://19thnews.org/2026/01/senate-defiance-act-nonconsensual-images-deepfakes/)
- [Durbin Successfully Passes Bill To Combat Nonconsensual, Sexually-Explicit Deepfake Images | U.S. Senator Dick Durbin of Illinois](https://www.durbin.senate.gov/newsroom/press-releases/durbin-successfully-passes-bill-to-combat-nonconsensual-sexually-explicit-deepfake-images)
- [Legislative Proposal to Sunset Section 230 of the Communications Decency Act | Congress.gov | Library of Congress](https://www.congress.gov/event/118th-congress/house-event/117342)
- [Energy and Commerce Leaders Unveil Bipartisan Draft ...](http://democrats-energycommerce.house.gov/media/press-releases/energy-and-commerce-leaders-unveil-bipartisan-draft-legislation-sunset-section)
- [Pallone Stresses Need to Hold Big Tech Accountable by ...](http://democrats-energycommerce.house.gov/media/press-releases/pallone-stresses-need-hold-big-tech-accountable-sunsetting-section-230)
- [Transcript: House Hearing on “Proposal to Sunset Section ...](https://techpolicy.press/transcript-house-hearing-on-proposal-to-sunset-section-230-of-the-communications-decency-act)
- [Committees - H.R.7569 - 118th Congress (2023-2024): DEFIANCE Act of 2024 | Congress.gov | Library of Congress](https://www.congress.gov/bill/118th-congress/house-bill/7569/committees)
- [H.R.7569 - 118th Congress (2023-2024): DEFIANCE Act of ...](https://www.congress.gov/bill/118th-congress/house-bill/7569/text/ih)
- [Ocasio-Cortez Statement on Senate Passage of the DEFIANCE Act | Representative Ocasio-Cortez](http://ocasio-cortez.house.gov/media/press-releases/ocasio-cortez-statement-senate-passage-defiance-act)
- [DEFIANCE Act of 2024 (2024; 118th Congress S. 3696) - GovTrack.us](https://www.govtrack.us/congress/bills/118/s3696)
- [H.R.7569 - 118th Congress (2023-2024): DEFIANCE Act of 2024 | Congress.gov | Library of Congress](https://www.congress.gov/bill/118th-congress/house-bill/7569)
- [Cosponsors - H.R.7569 - 118th Congress (2023-2024): DEFIANCE Act of 2024 | Congress.gov | Library of Congress](https://www.congress.gov/bill/118th-congress/house-bill/7569/cosponsors)
- [Texas Expands Laws to Protect Survivors from AI-Generated Sexual Deepfakes | Dallas Area Rape Crisis Center](https://www.dallasrapecrisis.org/radiant-report/texas-strengthens-protections-against-ai-generated-sexual-content-what-survivors-need-to-knownbsp)
- [AI-Report-United-States.pdf](https://futurefreespeech.org/wp-content/uploads/2025/10/AI-Report-United-States.pdf)
- [A Deep Dive into Colorado’s Artificial Intelligence Act - National Association of Attorneys General](https://www.naag.org/attorney-general-journal/a-deep-dive-into-colorados-artificial-intelligence-act/)
- [SB24-205 Consumer Protections for Artificial Intelligence | Colorado General Assembly](https://leg.colorado.gov/bills/sb24-205)
- [Utah, Colorado and Other States Lead Groundbreaking AI Legislation in U.S. - Davis+Gilbert LLP](https://www.dglaw.com/utah-colorado-and-other-states-lead-groundbreaking-ai-legislation-in-u-s/)
- [What Is the New AI Law in Colorado? Business Guide (2026) | CO-AIMS - Colorado AI Compliance](https://co-aims.com/blog/new-ai-law-colorado-what-businesses-need-to-know)
- [Comprehensive List of State Artificial Intelligence Legislation](https://stackcybersecurity.com/posts/ai-state-laws)
- [Colorado Enacts Artificial Intelligence Legislation Affecting AI Systems Developers, Deployers - Jackson Lewis](https://www.jacksonlewis.com/insights/colorado-enacts-artificial-intelligence-legislation-affecting-ai-systems-developers-deployers)
- [Texas 89th Legislature: Key Artificial Intelligence Legislation – Jackson Walker](https://www.jw.com/news/insights-texas-89th-legislature-ai/)
- [Texas Joins the Fray and Enacts AI Legislation | Littler](https://www.littler.com/news-analysis/asap/texas-joins-fray-and-enacts-ai-legislation)
- [AI-Report-2025-Full-Report.pdf](https://futurefreespeech.org/wp-content/uploads/2025/10/AI-Report-2025-Full-Report.pdf)
- [Colorado Anti-Discrimination in AI Law (ADAI) Rulemaking | Colorado Attorney General](https://coag.gov/ai/)
- [Senate Bill 24-205](https://leg.colorado.gov/bill_files/47770/download)
- [Deepfakes and AI-Generated Intimate Images Involving ...](https://content.leg.colorado.gov/sites/default/files/R25-1018_Deepfakes_Intimate%20Images_Minors.pdf)
- [AI deepfake policy in Colorado - Ballotpedia](https://ballotpedia.org/AI_deepfake_policy_in_Colorado)
- [                People ex rel. S.G.H. :: 2025 :: Colorado Supreme Court Decisions :: Colorado Case Law :: Colorado Law :: U.S. Law :: Justia    ](https://law.justia.com/cases/colorado/supreme-court/2025/25sa29.html)
- [HB24-1147 Candidate Election Deepfake Disclosures | Colorado General Assembly](http://leg.colorado.gov/bills/hb24-1147)
- [96%](https://capitol.texas.gov/tlodocs/89R/analysis/html/SB00441F.htm)
- [TX HB449 | BillTrack50](https://www.billtrack50.com/billdetail/1750970/43948)
- [Colorado Lawmakers Send Bills on AI, Deepfakes to Governor](https://www.govtech.com/policy/colorado-lawmakers-send-bills-on-ai-deepfakes-to-governor)
- [Texas Takes a Shot at AI Regulation With ‘Responsible Artificial Intelligence Governance Act’ - Ogletree](https://ogletree.com/insights-resources/blog-posts/texas-takes-a-shot-at-ai-regulation-with-responsible-artificial-intelligence-governance-act/)
- [Texas bill seeks to regulate AI's use in the state](https://www.texastribune.org/2025/05/23/texas-ai-bill-legislation-regulation/)
- [Colorado Governor Signs Broad AI Bill Regulating ...](https://www.seyfarth.com/news-insights/colorado-governor-signs-broad-ai-bill-regulating-employment-decisions.html)
- [REVISED - Colorado General Assembly](https://leg.colorado.gov/bill_files/85456/download)
- [INTRODUCED - Colorado General Assembly](https://leg.colorado.gov/bill_files/85500/download)
- [Deepfakes and AI-Generated Intimate Images Involving ...](https://content.leg.colorado.gov/sites/default/files/r25-1018-deepfakes-intimate-images-minors-accessible.pdf)
- [Colorado Child Safety & Digital Protection Act of 2026 ...](https://leg.colorado.gov/sites/default/files/initiatives/2025-2026%2520%2523133.pdf)
- [Deepfakes and AI-Generated Intimate Images Involving Minors | Colorado General Assembly](https://content.leg.colorado.gov/publications/deepfakes-and-ai-generated-intimate-images-involving-minors)
- [SB25-288 Intimate Digital Depictions Crim & Civil Actions | Colorado General Assembly](https://leg.colorado.gov/bills/sb25-288)
- [REENGROSSED - Colorado General Assembly](https://leg.colorado.gov/sites/default/files/documents/2025A/bills/2025a_288_ren.pdf)
- [89th Legislative Session Policy Brief: Artificial Intelligence and Social Media - Texas Policy Research](https://www.texaspolicyresearch.com/89th-legislative-session-policy-brief-artificial-intelligence-and-social-media/)
- [HB 449 - 89th Legislature](https://www.texaspolicyresearch.com/bills/89th-legislature-hb-449/)
- [89(R) HB 449 - Enrolled version - Bill Text](https://capitol.texas.gov/tlodocs/89R/billtext/html/HB00449F.HTM)
- [Artificial Intelligence](https://www.ftc.gov/industry/technology/artificial-intelligence)
- [Artificial Intelligence and Civil Rights](https://www.justice.gov/archives/crt/ai)
- [International Monthly: April 2019 | Federal Trade Commission](https://www.ftc.gov/policy/international/ftc-international-monthly/april-2019)
- [Congress’s Attempt to Criminalize Nonconsensual Intimate Imagery: The Benefits and Potential Shortcomings of the TAKE IT DOWN Act - National Association of Attorneys General](https://www.naag.org/attorney-general-journal/congresss-attempt-to-criminalize-nonconsensual-intimate-imagery-the-benefits-and-potential-shortcomings-of-the-take-it-down-act/)
- [FTC Proposes New Protections to Combat AI Impersonation of Individuals | Federal Trade Commission](https://www.ftc.gov/news-events/news/press-releases/2024/02/ftc-proposes-new-protections-combat-ai-impersonation-individuals)
- [Statutes | Federal Trade Commission](https://www.ftc.gov/legal-library/browse/statutes)
- [FTC Announces Crackdown on Deceptive AI Claims and Schemes | Federal Trade Commission](https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-crackdown-deceptive-ai-claims-schemes)
- [Emp Media Inc. (MyEx.com) | Federal Trade Commission](https://www.ftc.gov/legal-library/browse/cases-proceedings/162-3052-emp-media-inc-myexcom)
- [Emp Media Inc. (MyEx.com): Order Granting Motion for ...](https://www.ftc.gov/system/files/documents/cases/emp_order_granting_default_judgment_6-22-18.pdf)
- [
	Attorney General Laxalt and Federal Trade Commission Obtain Federal Judgment Against Parties Responsible for Revenge Pornography Website
](https://ag.nv.gov/News/PR/2018/Attorney_General_Laxalt_and_Federal_Trade_Commission_Obtain_Federal_Judgment_Against_Parties_Responsible_for_Revenge_Pornography_Website/)
- [Ocasio-Cortez, Lee, Durbin, Graham Introduce Bipartisan, Bicameral Legislation to Combat Non-Consensual, Sexually Explicit Deepfake Imagery | Representative Ocasio-Cortez](http://ocasio-cortez.house.gov/media/press-releases/ocasio-cortez-lee-durbin-graham-introduce-bipartisan-bicameral-legislation)
- [Federal Bills - Enough Abuse](https://enoughabuse.org/get-vocal/federal-bills/)
- [The TAKE IT DOWN Act: A Federal Law Prohibiting the Nonconsensual Publication of Intimate Images | Congress.gov | Library of Congress](https://www.congress.gov/crs-product/LSB11314)
- [FTC Finalizes Order with DoNotPay That Prohibits ...](https://www.ftc.gov/news-events/news/press-releases/2025/02/ftc-finalizes-order-donotpay-prohibits-deceptive-ai-lawyer-claims-imposes-monetary-relief-requires)
- [Nonconsensual Distribution of Intimate Images: What To ...](https://consumer.ftc.gov/articles/nonconsensual-distribution-intimate-images)
- [Generative AI's New & Continued Impacts](https://epic.org/wp-content/uploads/2024/05/EPIC-Generative-AI-II-Report-May2024-1.pdf)
- [Overview of FTC’s 2026 Children’s Privacy Focus: Expect Ongoing, if not More, Attention | Womble Bond Dickinson](https://www.womblebonddickinson.com/us/insights/alerts/overview-ftcs-2026-childrens-privacy-focus-expect-ongoing-if-not-more-attention)
- [One Year In, FTC’s “Operation AI Comply” Continues Under New Administration, Signaling Enduring Enforcement Focus | Benesch, Friedlander, Coplan & Aronoff LLP](https://www.beneschlaw.com/resources/one-year-in-ftcs-operation-ai-comply-continues-under-new-administration-signaling-enduring-enforcement-focus.html)
- [FTC Takes Action Against Evolv Technologies for Deceiving Users About its AI-Powered Security Screening Systems | Federal Trade Commission](https://www.ftc.gov/news-events/news/press-releases/2024/11/ftc-takes-action-against-evolv-technologies-deceiving-users-about-its-ai-powered-security-screening)
- [The Federal Trade Commission 2023 Privacy and Data ...](https://www.ftc.gov/system/files/ftc_gov/pdf/2024.03.21-PrivacyandDataSecurityUpdate-508.pdf)
- [Commission Policy Statement on Biometric Information](https://www.ftc.gov/system/files/ftc_gov/pdf/p225402biometricpolicystatement.pdf)
- [Update on Deputy Attorney General Lisa Monaco's ...](https://www.justice.gov/archives/opa/pr/update-deputy-attorney-general-lisa-monacos-justice-ai-convenings-0)
- [Attorney General James Protects New Yorkers from AI-Created Election Misinformation](https://ag.ny.gov/press-release/2024/attorney-general-james-protects-new-yorkers-ai-created-election-misinformation)
- [Deepfake Legislation Tracker: Federal &amp; State Laws | STACK Cybersecurity](https://stackcybersecurity.com/posts/ai-deepfake-laws)
- [Market Scan Report - By Infosys Responsible AI Office](https://www.infosys.com/services/data-ai-topaz/insights/market-scan-report.pdf)
- [Privacy and Security Enforcement | Federal Trade Commission](https://www.ftc.gov/news-events/topics/protecting-consumer-privacy-security/privacy-security-enforcement)
- [Grok AI Exploitation Crisis in Spicy Mode](https://www.lawyer-monthly.com/2026/01/grok-ai-spicy-mode-crisis/)
- [Take it Down Act Signed into Law, Offering Tools to Fight Non-Consensual Intimate Images and Creating a New Image Takedown Mechanism - Insights - Proskauer Rose LLP](https://www.proskauer.com/blog/take-it-down-act-signed-into-law-offering-tools-to-fight-non-consensual-intimate-images-and-creating-a-new-image-takedown-mechanism)
- [Attorney General James Demands More Action from xAI to Stop Grok Chatbot from Producing Inappropriate Images to Protect Children and Adult Users](https://ag.ny.gov/press-release/2026/attorney-general-james-demands-more-action-xai-stop-grok-chatbot-producing)
- [January 23, 2026 xAI 1450 Page Mill Rd Palo Alto, CA ...](https://www.attorneygeneral.gov/wp-content/uploads/2026/01/2026-01-26-Letter-to-xAI_FINAL.pdf)
- [Search and Payment Platforms Urged to Address Deepfake Nonconsensual Intimate Imagery (NCII) - National Association of Attorneys General](https://www.naag.org/policy-letter/search-and-payment-platforms-urged-to-address-deepfake-nonconsensual-intimate-imagery-ncii/)
- [Acting AG Davenport Demands Immediate Action from xAI to Stop Production of Nonconsensual Intimate Images and Child Sexual Abuse Material - New Jersey Office of Attorney General](https://www.njoag.gov/acting-ag-davenport-demands-immediate-action-from-xai-to-stop-production-of-nonconsensual-intimate-images-and-child-sexual-abuse-material/)
- [FTC and DOJ Crack Down on Deepfake Fraud May Indicate Future Liability for Corporations, Timothy Howard, Brock Dahl, Gabby Levikow, Aedan Collins](https://blog.freshfields.us/post/102j1zw/ftc-and-doj-crack-down-on-deepfake-fraud-may-indicate-future-liability-for-corpor)
- [FTC Announces Impersonation Rule Goes into Effect Today | Federal Trade Commission](https://www.ftc.gov/news-events/news/press-releases/2024/04/ftc-announces-impersonation-rule-goes-effect-today)
- [FTC Highlights Actions to Protect Consumers from Impersonation Scams | Federal Trade Commission](https://www.ftc.gov/news-events/news/press-releases/2025/04/ftc-highlights-actions-protect-consumers-impersonation-scams)
- [S.146 - 119th Congress (2025-2026): TAKE IT DOWN Act | Congress.gov | Library of Congress](https://www.congress.gov/bill/119th-congress/senate-bill/146)
- [Ashcroft v. Free Speech Coalition - Wikipedia](https://en.wikipedia.org/wiki/Ashcroft_v._Free_Speech_Coalition)
- [Deepfakes and the First Amendment: Are Deepfakes Illegal?](https://www.freedomforum.org/deepfakes-protected-by-first-amendment/)
- [ Ashcroft v. Free Speech Coalition | 535 U.S. 234 (2002) | Justia U.S. Supreme Court Center](https://supreme.justia.com/cases/federal/us/535/234/)
- [Unmasking deepfake porn creators won’t be easy - POLITICO](https://www.politico.com/newsletters/digital-future-daily/2026/01/26/how-do-you-sue-an-anonymous-deepfake-creator-00746752)
- [Take It Down or Take It Too Far? The Legal Fallout of New ...](https://scholarship.law.unc.edu/cgi/viewcontent.cgi?article=1521&context=ncjolt)
- [When AI Crosses the Line: Jane Doe v. ClothOff and Minors’ Digital Privacy](https://www.americanbar.org/groups/health_law/news/2025/when-ai-crosses-line-jane-doe-v-clothoff-minors-digital-privacy/)
- [Ashcroft, Virtual Child Pornography and First Amendment ...](https://sjlr.law.ucdavis.edu/sites/g/files/dgvnsk15361/files/media/documents/SJLR-11-1-Liu-11-1.pdf)
- [California orders Elon Musk company to stop explicit deepfakes](https://calmatters.org/economy/technology/2026/01/california-investigates-deepfakes-elon-musk-company/)
- [Deepfakes and AI-Generated Intimate Images Involving ...](https://content.leg.colorado.gov/sites/default/files/R25-1018_Deepfakes_Intimate%20Images_Minors.pdf)
- [Undressed victims file class action lawsuit against xAI for Grok deepfakes | CyberScoop](https://cyberscoop.com/grok-undressed-victims-file-class-action-lawsuit-against-xai-elon-musk/)
- [Grok AI Deepfake Lawsuit - Wallace Miller](https://www.wallacemiller.com/all-litigations/cases-under-investigation/grok-ai-deepfake-lawsuit/)
- [Court Rules That Constitution Protects Private Possession of AI-Generated CSAM | TechPolicy.Press](https://techpolicy.press/court-rules-that-constitution-protects-private-possession-of-aigenerated-csam)
- [Crafting New Boundaries: Model Legislation to Address the ...](https://scholarship.stu.edu/cgi/viewcontent.cgi?article=1673&context=stlr)
- [Miller v. California - Wikipedia](https://en.wikipedia.org/wiki/Miller_v._California)
- [ Miller v. California | 413 U.S. 15 (1973) | Justia U.S. Supreme Court Center](https://supreme.justia.com/cases/federal/us/413/15/)
- [Dealing with deepfakes: What the First Amendment says | The Free Speech Center](https://firstamendment.mtsu.edu/post/dealing-with-deepfakes-what-the-first-amendment-says/)
- [Ashcroft v. Free Speech Coalition](https://www.oyez.org/cases/2001/00-795)
- [DUBRISKE, Judge: Contrary to his pleas, Appellant was ...](https://afcca.law.af.mil/content/afcca_opinions/cp/taylor-38700.u.pdf)
- [Security and Censorship - Ithaka S+R](https://sr.ithaka.org/publications/security-and-censorship/)
- [An Explanation of the Miller Test for Obscenity](https://www.milibraries.org/assets/docs/IFToolkit/Explaining%20the%20Miller%20Test.pdf)
- [Deeply Fake, Deeply Disturbing, Deeply Constitutional: Why the First Amendment Likely Protects the Creation of Pornographic Deepfakes | Cardozo Law Review](https://cardozolawreview.com/deeply-fake-deeply-disturbing-deeply-constitutional-why-the-first-amendment-likely-protects-the-creation-of-pornographic-deepfakes/)
- [Miller Test | The First Amendment Encyclopedia - MTSU](https://firstamendment.mtsu.edu/article/miller-test/)
- [Global Freedom of Expression | Miller v. California - Global Freedom of Expression](https://globalfreedomofexpression.columbia.edu/cases/miller-v-california/)
- [Law enforcement cracking down on creators of AI-generated child sexual abuse images | PBS News](https://www.pbs.org/newshour/nation/law-enforcement-cracking-down-on-creators-of-ai-generated-child-sexual-abuse-images)
- [United States v. Williams, 553 U.S. 285 (2008).](https://tile.loc.gov/storage-services/service/ll/usrep/usrep553/usrep553285/usrep553285.pdf)
- [Child Pornography: Constitutional Principles and Federal ...](https://www.everycrsreport.com/reports/95-406A.html)
- [Ashcroft v. Free Speech Coalition (2002)](https://firstamendment.mtsu.edu/article/ashcroft-v-free-speech-coalition/)
- [11a0016p.06](http://www.ca6.uscourts.gov/opinions.pdf/11a0016p-06.pdf)
- [Sexual Ageplay in Virtual Reality: Practicing Free Speech or Producing Child Pornography | Cardozo Law Review](https://cardozolawreview.com/sexual-ageplay-in-virtual-reality-practicing-free-speech-or-producing-child-pornography/)
- [U.S. v. Whorley](https://case-law.vlex.com/vid/u-s-v-whorley-889859244)
- [US v. Hotaling, 02/28/2011, 09-3935 - US 2nd Circuit](https://caselaw.findlaw.com/summary/opinion/us-2nd-circuit/2011/02/28/254262.html)
- [Why California Should Adopt the Federal Standard for Child ...](https://digitalcommons.lmu.edu/cgi/viewcontent.cgi?article=1570&context=elr)
- [Ashcroft v. Free Speech Coalition, 535 U.S. 234 (2002).](https://tile.loc.gov/storage-services/service/ll/usrep/usrep535/usrep535234/usrep535234.pdf)
- [ASHCROFT V. FREE SPEECH COALITION](https://www.law.cornell.edu/supct/html/00-795.ZO.html)
- [ASHCROFT V. FREE SPEECH COALITION](https://www.law.cornell.edu/supct/html/00-795.ZS.html)
- [ASHCROFT V. FREE SPEECH COALITION](https://www.law.cornell.edu/supct/html/00-795.ZC.html)
- [US v. Whorley, 12/18/2008, 06-4288 - US 4th Circuit | FindLaw](https://caselaw.findlaw.com/summary/opinion/us-4th-circuit/2008/12/18/157587.html)
- [ United States v. Williams | 553 U.S. 285 (2008) | Justia U.S. Supreme Court Center](https://supreme.justia.com/cases/federal/us/553/285/)
- [                Doe v. Boland, No. 11-4237 (6th Cir. 2012) :: Justia    ](https://law.justia.com/cases/federal/appellate-courts/ca6/11-4237/11-4237-2012-11-09.html)
- [UNITED STATES COURT OF APPEALS](https://cases.justia.com/federal/appellate-courts/ca6/11-4237/11-4237-2012-11-09.pdf?ts=1411026305)
- [The Legal Gray Zone of Deepfake Political Speech](https://publications.lawschool.cornell.edu/jlpp/2025/10/24/the-legal-gray-zone-of-deepfake-political-speech/)
- [Deepfakes, Synthetic Media, and the First Amendment](https://digitalcommons.mainelaw.maine.edu/sjipl/vol3/iss1/5/)
- [00-795. Ashcroft v. Free Speech Coalition (10/30/01)](https://www.supremecourt.gov/pdfs/transcripts/2001/00-795.pdf)
- [
	Deceptive Audio or Visual Media (“Deepfakes”) 2024 Legislation
](https://www.ncsl.org/technology-and-communication/deceptive-audio-or-visual-media-deepfakes-2024-legislation)
- ['Deepfake abuse is abuse'](https://www.unicef.org/press-releases/deepfake-abuse-is-abuse)
- [UNITED STATES v. WHORLEY (2008) | FindLaw](https://caselaw.findlaw.com/court/us-4th-circuit/1431669.html)
- [The Safety Net Is Shrinking: Insurers Move to Exclude AI Risks](https://www.marketingaiinstitute.com/blog/insurers-move-to-exclude-ai-risks)
- [Entertainment and Media Liability](https://axaxl.com/-/media/axaxl/files/pdfs/insurance/specialty/professional-entertainment-and-media-liability-insurance/comm-eoentertainment-and-media-liability-product-sheet.pdf?rev=bb7874af01de4fc1b7069a3ffdc61ebd&sc_lang=pt&hash=E387E087EAC1402B7D1B008D7756CD7A)
- [2024: An Outlook on Artificial Intelligence](https://www.beazley.com/en-CH/articles/2024-an-outlook-on-artificial-intelligence?pdf=1)
- [Media Liability Insurance Coverage | Chubb](https://www.chubb.com/us-en/business-insurance/professional-liability-protection-for-media-organizations.html)
- [Chubb Report Reveals Cybersecurity as Leading Risk Threatening Business Growth, with Technology Disruption Following Closely Behind - Jan 6, 2025](https://news.na.chubb.com/2025-01-06-Chubb-Report-Reveals-Cybersecurity-as-Leading-Risk-Threatening-Business-Growth,-with-Technology-Disruption-Following-Closely-Behind)
- [Deepfakes whitepaper](https://axaxl.com/-/media/axaxl/files/pdfs/insurance/cyber-north-america/cyber_deepfakes-whitepaper_axa-xl_us.pdf?rev=f8b1ce21fd3b4059acaa7a04a365236e&sc_lang=pt&hash=1228CE34C222CEECBCBDD8DC48449AC5)
- [Frequently Asked Questions:](https://axaxl.com/-/media/axaxl/files/pdfs/insurance/cyber-international/downloads/axa-xl_faqs-gen-ai-endorsment.pdf?rev=16d2021a36e64b6c91f02793c79f57f3&sc_lang=pt&hash=3A25AC7127A23F4919469F8F7C8D5FB9)
- [Contents](https://www.beazley.com/globalassets/product-documents/policy-form/beazley-ae-professional-liabilitymediatech-policy.pdf)
- [Beazley MediaTech](https://www.beazley.com/globalassets/product-documents/policy-form/beazley-media-tech-policy-us.pdf)
- [MediaTech | beazley](https://beazley.com/en-150/products-and-solutions/corporate-solutions/cyber-and-tech/mediatech/)
- [Professional Entertainment & Media Liability Insurance](https://axaxl.com/insurance/products/professional-entertainment-and-media-liability-insurance)
- [MEDIAGUARDSM by CHUBB](https://www.chubb.com/content/dam/chubb-sites/chubb-com/document_search/us-en/doc/14-03-0888-mediaguard-nb-app.pdf)
- [bbr-5.0-enhancements-and-clarifications. ...](https://www.beazley.com/globalassets/full-spectrum-cyber/bbr-5.0-enhancements-and-clarifications.pdf)
- [Gen AI endorsement for CyberRiskConnect](https://axaxl.com/-/media/axaxl/files/pdfs/insurance/cyber-uk/axa-xl-cyberriskconnect-gen-ai-global-product-sheet.pdf?rev=1b5df87f39bf4bc98a3066c58fc6e0a8&sc_lang=en-gb&hash=D6C711F0DD771031751961EBC9D64604)
- [AXA XL unveils new cyber insurance extending coverage to help businesses manage emerging Gen AI risks | AXA XL](https://axaxl.com/press-releases/axa-xl-unveils-new-cyber-insurance-extending-coverage-to-help-businesses-manage-emerging-gen-ai-risks)
- [2025 tech trends report • 18th edition - financial services & ...](https://ftsg.com/wp-content/uploads/2025/03/Financial-Services-Insurance_FINAL_LINKED.pdf?ref=blog.anq.finance)
- [MediaGuard Insurance](https://www.chubb.com/content/dam/chubb-sites/chubb-com/ca-en/business-insurance/mediaguard-by-chubb/documents/pdf/mediaguard-insurance.pdf)
- [MediaGuard® Liability Insurance](https://www.chubb.com/content/dam/chubb-sites/chubb-com/us-en/business-insurance/professional-liability-protection-for-media-organizations/documents/pdf/14010992-mediaguard-liability-insurance-1.17.pdf)
- [Spotlight On Cyber & Technology Risk 2024](https://www.beazley.com/globalassets/2024-08/beazley-cyber-tech-risk-2024-report.final.2.9.24.pdf)
- [Comprehensive Cyber Insurance - Europe and APAC](https://axaxl.com/insurance/products/cyber-insurance-international)
- [Social Engineering Fraud: A Growing Crime Problem](https://www.chubb.com/content/dam/chubb-sites/chubb-com/us-en/business-insurance/social-engineering-fraud-coverage-for-crime-insurance/documents/pdf/chubb_socialengineeringfraud_final.pdf)
- [Global Insurance Market Report (GIMAR)](https://www.iais.org/uploads/2025/12/Global-Insurance-Market-Report-2025.pdf)
- [
    LMA - Understanding AI Exposures: AI Loss Scenarios Survey Results  ](https://lmalloyds.com/campaigns/understanding-ai-exposures-ai-loss-scenarios-survey-results/)
- [
    LMA - Understanding artificial intelligence risk in insurance products – the challenges  ](https://lmalloyds.com/understanding-artificial-intelligence-risk-in-insurance-products-the-challenges/)
- [
    LMA - The Impact of Artificial Intelligence on the International E&O Market  ](https://lmalloyds.com/campaigns/the-impact-of-artificial-intelligence-on-the-international-eo-market/)
- [Generative AI: An insurer’s perspective on the promises and perils](https://axaxl.com/fast-fast-forward/articles/generative-ai-an-insurer-s-perspective-on-the-promises-and-perils)
- [MediaGuard |  Media Organization Professional Liability Insurance | E&O Insurance | Chubb](https://www.chubb.com/ca-en/business-insurance/mediaguard-by-chubb.html)
- [The Deepfake Coverage Gap - InsuranceIndustry.AI](https://insuranceindustry.ai/the-deepfake-coverage-gap/)
- [Media Liability | beazley](https://beazley.com/en/products/specialty-risk-usa/media-liability/)
- [Deepfakes: The latest weapon in the cyber security arms race | beazley](https://www.beazley.com/en/news-and-events/deepfakes-the-latest-weapon-in-the-cyber-security-arms-race/)
- [The evolution of cyber insurance: lessons for the future](https://axaxl.com/fast-fast-forward/articles/the-evolution-of-cyber-insurance-lessons-for-the-future)
- [MeitY SOP on non-consensual intimate imagery](https://www.scconline.com/blog/post/2025/11/12/meity-non-consensual-intimate-imagery-sop-24-hour-takedown-policy-scctimes/)
- [MeitY Outlines How to Report Non-Consensual Intimate ...](https://www.medianama.com/2025/11/223-meity-sop-non-consensual-intimate-imagery-intermediaries/)
- [
	Press Release: Press Information Bureau
](https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2226617)
- [Digital Provenance & Content Authentication: Trust in AI Media (2026)](https://thetraceabilityhub.com/digital-provenance-why-content-authentication-matters-in-2026/)
- [National AI Forensic Grid: Federated Multi-Modal Deepfake ...](https://www.tdcommons.org/cgi/viewcontent.cgi?article=10607&context=dpubs_series)
- [New Law Criminalises Deepfake Creation | Olliers Solicitors](https://www.olliers.com/news/new-law-criminalises-deepfake-creation/)
- [Overview of the NetzDG Network Enforcement Law - Center for Democracy and Technology](https://cdt.org/insights/overview-of-the-netzdg-network-enforcement-law/)
- [Image-Based Abuse Scheme](https://www.esafety.gov.au/sites/default/files/2024-02/Image-Based-Abuse-Scheme-Regulatory-Guidance-Feb2024.pdf)
- [SOP NCII vers.1](https://www.meity.gov.in/static/uploads/2025/11/a2c9500ef5f8b62a43bfc68747de592d.pdf)
- ['What Is Illegal Offline, Should Be Illegal Online': The ...](https://academic.oup.com/book/56385/chapter/448321003)
- [
        TAKE IT DOWN Act Targets Deepfakes: Are Online Platforms Caught in the Crosshairs? – Publications
    ](https://www.morganlewis.com/pubs/2025/06/take-it-down-act-targets-deepfakes-are-online-platforms-caught-in-the-crosshairs)
- [Guidance A safer life online for women and girls](https://www.ofcom.org.uk/siteassets/resources/documents/consultations/category-1-10-weeks/consultation-on-draft-guidance-a-safer-life-online-for-women-and-girls/statement-docs/guidance-a-safer-life-online-for-women-and-girls.pdf?v=408215)
- [Tackling non-consensual intimate image abuse](https://committees.parliament.uk/publications/47984/documents/250956/default/)
- [Government crackdown on explicit deepfakes - GOV.UK](https://www.gov.uk/government/news/government-crackdown-on-explicit-deepfakes)
- [Development Of Artificial Intelligence-Based Model for Forensic Analysis of Cross-Platform Deepfakes | Request PDF](https://www.researchgate.net/publication/397763470_Development_Of_Artificial_Intelligence-Based_Model_for_Forensic_Analysis_of_Cross-Platform_Deepfakes)
- [2025 Deepfake Detection Market Report and Buyers Guide](https://www.biometricupdate.com/wp-content/uploads/2025/11/BU-Deepfake-Detection-Market-Report-Buyers-Guide.pdf)
- [How digital forensics could prove what’s real in the age of deepfakes | Scientific American](https://www.scientificamerican.com/article/how-digital-forensics-could-prove-whats-real-in-the-age-of-deepfakes/)
- [2026 Look Ahead: What's to Come in the World of Deepfake Detection](https://www.realitydefender.com/insights/2026-look-forward)
- [TAKE IT DOWN Act - Wikipedia](https://en.wikipedia.org/wiki/TAKE_IT_DOWN_Act)
- [What to Know about the Take It Down Act - All In Together](https://aitogether.org/what-to-know-about-the-take-it-down-act/)
- [President Trump Signs Take It Down Act Into Law](https://www.lw.com/en/insights/president-trump-signs-take-it-down-act-into-law)
- [MeitY issues SOP mandating 24-hour takedown of non- ...](https://www.moneycontrol.com/technology/meity-issues-sop-mandating-24-hour-takedown-of-non-consensual-intimate-imagery-online-article-13668129.html)
- [Breaking: Govt tightens NCII takedown norms, makes ...](https://www.storyboard18.com/digital/breaking-govt-tightens-ncii-takedown-norms-makes-intermediaries-directly-accountable-84001.htm)
- [Report image-based abuse | eSafety Commissioner](https://www.esafety.gov.au/key-topics/image-based-abuse/report-image-based-abuse)
- [Congress’s Attempt to Criminalize Nonconsensual Intimate Imagery: The Benefits and Potential Shortcomings of the TAKE IT DOWN Act - National Association of Attorneys General](https://www.naag.org/attorney-general-journal/congresss-attempt-to-criminalize-nonconsensual-intimate-imagery-the-benefits-and-potential-shortcomings-of-the-take-it-down-act/)
- [Tools to Address Known Exploitation by Immobilizing Technological Deepfakes on Websites and Networks Act ("TAKE IT DOWN Act") | Federal Trade Commission](https://www.ftc.gov/legal-library/browse/statutes/tools-address-known-exploitation-immobilizing-technological-deepfakes-websites-networks-act-take-it)
- [The TAKE IT DOWN Act: A Federal Law Prohibiting the Nonconsensual Publication of Intimate Images | Congress.gov | Library of Congress](https://www.congress.gov/crs-product/LSB11314)
- [Take It Down Act](https://rainn.org/federal-legislation/take-it-down-act/)
- [Text - S.146 - 119th Congress (2025-2026): TAKE IT DOWN Act | Congress.gov | Library of Congress](https://www.congress.gov/bill/119th-congress/senate-bill/146/text)
- [SOP to Ensure Swift and Uniform Action Against NCII Content](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2188886&reg=3&lang=2)
- [MeitY Issues Standard Operating Procedure to Curtail ...](https://avantiscdnprodstorage.blob.core.windows.net/legalupdatedocs/49250/MeitY-issued-SOP-to-Curb-Non-Consensual-Intimate-Imagery-NCII-Content-Online-November122025.pdf)
- [frequently asked questions](https://www.meity.gov.in/static/uploads/2025/10/065b6deb585441b5ccdf8be42502a49c.pdf)
- [ACMA and eSafety corporate plan 2024-25](https://www.acma.gov.au/sites/default/files/2024-07/ACMA%20and%20eSafety%20corporate%20plan%202024-25.pdf)
- [Regulatory Index](https://www.esafety.gov.au/sites/default/files/2025-11/GOSRN-Regulation-Index-2025.pdf)
- [S.146 - 119th Congress (2025-2026): TAKE IT DOWN Act | Congress.gov | Library of Congress](https://www.congress.gov/bill/119th-congress/senate-bill/146)
- [TAKE IT DOWN Act signed into law | National Association of Counties](https://www.naco.org/news/take-it-down-act-signed-law)
- [Trump Signs Law Expanding Tech Platform Requirements and FTC Enforcement on Intimate AI Deepfakes and Images: Wiley](https://www.wiley.law/alert-Trump-Signs-Law-Expanding-Tech-Platform-Requirements-and-FTC-Enforcement-on-Intimate-AI-Deepfakes-and-Images)
- [Another Take on the TAKE IT DOWN Act | Perkins Coie](https://perkinscoie.com/insights/blog/another-take-take-it-down-act)
- [The TAKE IT DOWN Act Targets AI-Generated and ...](https://www.nelsonmullins.com/insights/blogs/ai-task-force/ai/ai-task-force-the-take-it-down-act-targets-ai-generated-and-authentic-nonconsensual-intimate-images)
- [इलेक्ट्रॉनिकी और सूचिा प्रौद्योनिकी मंत्रालय](https://egazette.gov.in/WriteReadData/2026/269993.pdf)
- [IT Intermediary Amendment Rules, 2026 contradict their purpose](https://internetfreedom.in/it-intermediary-amendment-rules-2026-contradict-their-purpose/)
- [The Information Technology (Intermediary Guidelines and ...](https://www.meity.gov.in/static/uploads/2026/02/550681ab908f8afb135b0ad42816a1c9.pdf)
- [Data (Use and Access) Act 2025 | ICO](https://ico.org.uk/about-the-ico/what-we-do/legislation-we-cover/data-use-and-access-act-2025/)
- [Government crackdown on explicit deepfakes - GOV.UK](https://www.gov.uk/government/news/government-crackdown-on-explicit-deepfakes)
- [Non-Consensual Sexually Explicit Images and Videos ( ...](https://researchbriefings.files.parliament.uk/documents/LLN-2024-0070/LLN-2024-0070.pdf)
- [Data (Use and Access) Act 2025 - Parliamentary Bills - UK Parliament](https://bills.parliament.uk/bills/3825)
- [Data (Use and Access) Act 2025 - Parliamentary Bills](https://bills.parliament.uk/bills/3825/publications)
- [Data (Use And Access) Act 2025](https://www.legislation.gov.uk/ukpga/2025/18/notes/division/17/index.htm)
- [EXPLANATORY NOTES Data (Use and Access) Act 2025](https://www.legislation.gov.uk/ukpga/2025/18/pdfs/ukpgaen_20250018_en.pdf)
- [Data (Use and Access) Act 2025: data protection and privacy changes - GOV.UK](https://www.gov.uk/guidance/data-use-and-access-act-2025-data-protection-and-privacy-changes)
- [Understanding the Data (Use and Access) Act: what businesses need to know | Womble Bond Dickinson](https://www.womblebonddickinson.com/uk/insights/articles-and-briefings/understanding-data-use-and-access-act-what-businesses-need-know)
- [UK - The Online Safety Act 2023 – the landscape two years ...](https://www.linklaters.com/en/insights/blogs/digilinks/2025/september/uk-the-online-safety-act-2023-the-landscape-two-years-on)
- [Online Safety Act: explainer - GOV.UK](https://www.gov.uk/government/publications/online-safety-act-explainer/online-safety-act-explainer)
- [The UK Online Safety Regime: Five Months On | Insights | Mayer Brown](https://www.mayerbrown.com/en/insights/publications/2024/03/the-uk-online-safety-regime-five-months-on)
- [Tackling digital exploitation of women and girls - House of Commons Library](https://commonslibrary.parliament.uk/research-briefings/cdp-2026-0016/)
- [New Law Criminalises Deepfake Creation | Olliers Solicitors](https://www.olliers.com/news/new-law-criminalises-deepfake-creation/)
- [Government leads global fight against deepfake threats - GOV.UK](https://www.gov.uk/government/news/government-leads-global-fight-against-deepfake-threats)
- [Non-Consensual Sexually Explicit Images and Videos (Offences) Bill [HL]: HL Bill 26 of 2024–25 - House of Lords Library](https://lordslibrary.parliament.uk/research-briefings/lln-2024-0070/)
- [Victims urge tougher action on deepfake abuse as new law comes into force | Deepfake | The Guardian](https://www.theguardian.com/technology/2026/feb/07/campaigners-call-stronger-protection-against-ai-generated-explicit-imagery)
- [Non-consensual deepfakes are now illegal in the UK](https://www.bbc.com/news/live/czx394lee0vt)
- [UK Online Safety Act Explained: Goals, Penalties & Age Checks | Ondato](https://ondato.com/blog/online-safety-bill/)
- [UK Online Safety Act 2023](https://www.lw.com/en/insights-landing/admin/upload/SiteAttachments/UK-Online-Safety-Act-2023.pdf)
- [What is 'illegal content' and what are the key duties under ...](https://www.hsfkramer.com/insights/2024-10/what-is-illegal-content-and-what-are-the-key-duties-under-the-osa)
- [Social Media: Non-consensual Sexual Deepfakes - Hansard - UK Parliament](https://hansard.parliament.uk/Commons/2026-01-12/debates/BF27124F-41F4-48A9-9042-1B74795942BE/SocialMediaNon-ConsensualSexualDeepfakes)
- [Ofcom investigates Elon Musk's X over Grok AI sexual ...](https://www.bbc.com/news/articles/cwy875j28k0o)
- [UK data regulator opens probe into Elon Musk's X and XAI ...](https://www.euronews.com/next/2026/02/03/uk-data-regulator-opens-probe-into-elon-musks-x-and-xai-over-sexual-ai-deepfakes)
- [Expert Comment: Chatbot-driven sexual abuse? The Grok case is just the tip of the iceberg | University of Oxford](https://www.ox.ac.uk/news/2026-01-14-expert-comment-chatbot-driven-sexual-abuse-grok-case-just-tip-iceberg)
- [Other Provisions in the Data (Use and Access) Act 2025 | Stephenson Harwood](https://www.stephensonharwood.com/insights/other-provisions-in-the-data-use-and-access-act-2025/)
- [Ofcom urges social media platforms to combat abuse and limit online ‘pile-ons’ | Social media | The Guardian](https://www.theguardian.com/media/2025/nov/25/ofcom-social-media-platforms-online-abuse-measures-limit-pile-ons)
- [Secretary of State statement to the House of Commons: 12 January 2026 - GOV.UK](https://www.gov.uk/government/speeches/secretary-of-state-statement-to-the-house-of-commons-12-january-2026)
- [ICO announces investigation into Grok | ICO](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/02/ico-announces-investigation-into-grok/)
- [Ofcom update: Investigation into X, and scope of the Online Safety Act](https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/investigation-into-x-and-scope-of-the-online-safety-act)
- [UK investigates Musk's X over Grok deepfake concerns | Reuters](https://www.reuters.com/business/media-telecom/uk-regulator-launches-investigation-into-x-over-grok-sexualised-imagery-2026-01-12/)
- [Ofcom launches investigation into X over Grok sexualised imagery](https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/ofcom-launches-investigation-into-x-over-grok-sexualised-imagery)
- [Data (Use and Access) Bill [HL] - Hansard](https://hansard.parliament.uk/lords/2025-01-28/debates/AABE348A-4DCF-4355-A420-6C5FC3DF0A52/Data(UseAndAccess)Bill)
- [Illegal Content Judgements Guidance](https://www.ofcom.org.uk/siteassets/resources/documents/online-safety/information-for-industry/illegal-harms/illegal-content-judgements-guidance-statement-updated-30-july-2025.pdf?v=403556)
- [Grok AI generation and dissemination of sexually explicit and ...](https://edm.parliament.uk/early-day-motion/65027/grok-ai-generation-and-dissemination-of-sexually-explicit-and-nonconsensual-images-of-women-and-children-on-x)
- [Guidance on a safer life online for women and girls](https://www.ofcom.org.uk/siteassets/resources/documents/consultations/category-1-10-weeks/consultation-on-draft-guidance-a-safer-life-online-for-women-and-girls/statement-docs/statement-guidance-on-a-safer-life-online-for-women-and-girls.pdf?v=408227)
- [The Data (Use and Access) Act 2025 (Commencement No. 1) Regulations 2025](https://www.legislation.gov.uk/id/uksi/2025/904)
- [Online Safety Act 2023](https://www.legislation.gov.uk/ukpga/2023/50/contents)
- [Data (Use and Access) Bill [HL] - Hansard](https://hansard.parliament.uk/lords/2025-02-05/debates/9103AF53-5257-437F-84B0-01E483443B39/Data(UseAndAccess)Bill(HL))
- [The legal response to AI-generated sexual deepfakes](https://insights.doughtystreet.co.uk/post/102mdvo/the-legal-response-to-ai-generated-sexual-deepfakes)
- [Data Use and Access Act 2025: plans for commencement - GOV.UK](https://www.gov.uk/guidance/data-use-and-access-act-2025-plans-for-commencement)
- [
      Data (Use And Access) Act 2025
    ](https://www.legislation.gov.uk/ukpga/2025/18/notes/division/1/index.htm)
- [
      Data (Use And Access) Act 2025
    ](https://www.legislation.gov.uk/ukpga/2025/18/notes/division/12/index.htm)
- [Government accused of dragging its heels on deepfake law over Grok AI](https://www.bbc.com/news/articles/cp9jxvx0zjmo)
- [Implementation of the Online Safety Act - House of Commons Library](https://commonslibrary.parliament.uk/research-briefings/cdp-2025-0043/)
- [Online Safety Act 2023](https://www.legislation.gov.uk/ukpga/2023/50)
- [Important dates for Online Safety compliance](https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/important-dates-for-online-safety-compliance)
- [
              Generative AI Meets Section 230: The Future of Liability and Its Implications for Startup Innovation | The University of Chicago Business Law Review
          ](https://businesslawreview.uchicago.edu/print-archive/generative-ai-meets-section-230-future-liability-and-its-implications-startup)
- [Beyond the Search Bar: Generative AI’s Section 230 Tightrope Walk](https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-november/beyond-search-bar-generative-ai-section-230-tightrope-walk/)
- [Section 230 Immunity and Generative Artificial Intelligence | Congress.gov | Library of Congress](https://www.congress.gov/crs-product/LSB11097)
- [Section 230 and AI-Driven Platforms | The Regulatory Review](https://www.theregreview.org/2026/01/17/seminar-section-230-and-ai-driven-platforms/)
- [Section 230 is Not Fit for AI](https://brownpoliticalreview.org/section-230-is-not-fit-for-ai/)
- [Section 230 Under Fire: Recent Cases, Legal ...](https://www.dynamisllp.com/knowledge/section-230-immunity-changes)
- [Beyond Section 230: Principles for AI Governance - Harvard Law Review](https://harvardlawreview.org/print/vol-138/beyond-section-230-principles-for-ai-governance/)
- [Addicted by Design: Reassessing Section 230 in the New ...](https://uclawreview.org/2025/12/04/addicted-by-design-reassessing-section-230-in-the-new-era-of-social-media-addiction-litigation/)
- [Deepfake detection in generative AI: A legal framework ...](https://www.sciencedirect.com/science/article/pii/S2212473X25000355)
- [Grok AI Exploitation Crisis in Spicy Mode](https://www.lawyer-monthly.com/2026/01/grok-ai-spicy-mode-crisis/)
- [Federal and State Regulators Target AI Chatbots and Intimate Imagery | Crowell & Moring LLP](https://www.crowell.com/en/insights/client-alerts/federal-and-state-regulators-target-ai-chatbots-and-intimate-imagery)
- [Fair Housing Council of San Fernando Valley v. Roommates.com, LLC, 521 F.3d 1157 (9th Cir. 2008) | Electronic Frontier Foundation](https://www.eff.org/issues/cda230/cases/fair-housing-council-san-fernando-valley-v-roommatescom)
- [Paying for Nude Celebrities: Testing the Outer Limits of ...](https://digitalcommons.law.uw.edu/cgi/viewcontent.cgi?article=1239&context=wjlta)
- [Fair Housing Council of San Fernando Valley v. Roommates.com, LLC - Wikipedia](https://en.wikipedia.org/wiki/Fair_Housing_Council_of_San_Fernando_Valley_v._Roommates.com,_LLC)
- [Zeran v. America Online, Inc.](https://en.wikipedia.org/wiki/Zeran_v._America_Online,_Inc.)
- [Zeran v. America Online, Inc. (4th Cir.) (1997)](https://firstamendment.mtsu.edu/article/zeran-v-america-online-inc-4th-cir/)
- [John Doe v. Grindr](https://www.supremecourt.gov/DocketPDF/24/24-1202/359343/20250521152440744_24-%20Petition.pdf)
- [
	Deceptive Audio or Visual Media (“Deepfakes”) 2024 Legislation
](https://www.ncsl.org/technology-and-communication/deceptive-audio-or-visual-media-deepfakes-2024-legislation)
- [Section 230 Requires a Balanced Approach that Protects Civil Rights and Free Expression | ACS](https://www.acslaw.org/expertforum/section-230-requires-a-balanced-approach-that-protects-civil-rights-and-free-expression/)
- [FAIR HOUSING COUNCIL v. ROOMMATES.COM](https://cdn.ca9.uscourts.gov/datastore/opinions/2008/04/02/0456916.pdf)
- [Deepfake Liability Act (H.R. 6334) - GovTrack.us](https://www.govtrack.us/congress/bills/119/hr6334)
- [U.S. Senate Passes Salazar's Bill to Protect Deepfake ...](http://salazar.house.gov/media/press-releases/us-senate-passes-salazars-bill-protect-deepfake-revenge-porn-victims)
- [Text - H.R.6943 - 118th Congress (2023-2024): No AI ...](https://www.congress.gov/bill/118th-congress/house-bill/6943/text)
- [Cruz-Klobuchar Bill to Protect Teenagers from Deepfake ...](https://www.commerce.senate.gov/index.php/2025/2/cruz-klobuchar-bill-to-protect-teenagers-from-deepfake-revenge-porn-unanimously-passes-the-senate)
- [
	Maloy and Auchincloss Introduce Deepfake Liability Act | U.S. Representative Celeste Maloy
](https://maloy.house.gov/news/documentsingle.aspx?DocumentID=1798)
- [Is Section 230 Going to Change? The FTC, DOJ and FCC Signal Significant Change for Online Businesses | Crowell & Moring LLP](https://www.crowell.com/en/insights/client-alerts/is-section-230-going-to-change-the-ftc-doj-and-fcc-signal-significant-change-for-online-businesses)
- [2024-06-12-Doe-Grindr-Ninth-Cir- ...](https://cdt.org/wp-content/uploads/2024/06/2024-06-12-Doe-Grindr-Ninth-Cir-Amicus_61724_as-filed.pdf)
- [Section 230 Under Fire: Recent Cases, Legal ...](https://www.dynamisllp.com/knowledge/section-230-immunity-changes)
- [Design-Based Lawsuits Against Platform Companies Reveal Fault Lines in Courts’ Section 230 Interpretations – EPIC – Electronic Privacy Information Center](https://epic.org/design-based-lawsuits-against-platform-companies-reveal-fault-lines-in-courts-section-230-interpretations/)
- [Judge Goes Rogue and Rejects Snap's Section 230 Defense for [Reasons]-Neville v. Snap - Technology & Marketing Law Blog](https://blog.ericgoldman.org/archives/2024/01/judge-goes-rogue-and-rejects-snaps-section-230-defense-for-reasons-neville-v-snap.htm)
- [Section 230: A Brief Overview | Congress.gov | Library of Congress](https://www.congress.gov/crs-product/IF12584)
- [Section 230: An Overview | Congress.gov | Library of Congress](https://www.congress.gov/crs-product/R46751)
- [Text - S.3193 - 119th Congress (2025-2026): Algorithm Accountability Act | Congress.gov | Library of Congress](https://www.congress.gov/bill/119th-congress/senate-bill/3193/text)
- [Text - H.R.6334 - 119th Congress (2025-2026): Deepfake Liability Act | Congress.gov | Library of Congress](https://www.congress.gov/bill/119th-congress/house-bill/6334/text)
- [H.R.6334 - 119th Congress (2025-2026): Deepfake Liability Act | Congress.gov | Library of Congress](https://www.congress.gov/bill/119th-congress/house-bill/6334)
- [Estate of Carson Bride v. YOLO Technologies, Inc.](https://cdn.ca9.uscourts.gov/datastore/opinions/2024/08/22/23-55134.pdf)
- [Supreme Court of the United States](https://www.supremecourt.gov/DocketPDF/24/24-1202/374178/20250909165722399_24-1202%20Reply%20Brief.pdf)
- [Doe v. Grindr, Inc.](https://cdn.ca9.uscourts.gov/datastore/opinions/2025/02/18/24-475.pdf)
- [John Doe v. Grindr](https://www.supremecourt.gov/DocketPDF/24/24-1202/359343/20250521152440744_24-%20Petition.pdf)
- [Interpreting the ambiguities of Section 230](https://www.brookings.edu/articles/interpreting-the-ambiguities-of-section-230/)
- [Section 230 | Electronic Frontier Foundation](https://www.eff.org/issues/cda230)
- [Social Media: Content Dissemination and Moderation Practices | Congress.gov | Library of Congress](https://www.congress.gov/crs-product/R46662)
- [Regulatory, Legal, and Policy Considerations for the 119th ...](https://www.everycrsreport.com/reports/IF12904.html)
- [47 U.S. Code § 230 - Protection for private blocking and screening of offensive material | U.S. Code | US Law | LII / Legal Information Institute](https://www.law.cornell.edu/uscode/text/47/230)
- [Auchincloss, Maloy introduce bipartisan bill carving out bots & deepfakes from social media platforms' Section 230 liability shield | U.S. Congressman Jake Auchincloss Of Massachusetts 4th District](https://auchincloss.house.gov/media/press-releases/auchincloss-maloy-introduce-bipartisan-bill-on-section-230-liability-shield)
- [                Anderson v. TikTok Inc, No. 22-3061 (3d Cir. 2024) :: Justia    ](https://law.justia.com/cases/federal/appellate-courts/ca3/22-3061/22-3061-2024-08-27.html)
- [No. 22-3061 ______________ TAWAINNA ANDERSON, I](https://www2.ca3.uscourts.gov/opinarch/223061p.pdf)
- [The Past, Present, and Future of Section 230 — Northwestern Undergraduate Law Journal](https://www.thenulj.com/nuljforum/luo9d1bastuy0vz0u8i6qyszjjex3s)
- [Take It Down or Take It Too Far? The Legal Fallout of New ...](https://scholarship.law.unc.edu/cgi/viewcontent.cgi?article=1521&context=ncjolt)
- [Exceptions to Section 230 Immunity for Online Platforms](https://www.bloomberglaw.com/external/document/X4B8CITG000000/corporate-compliance-overview-exceptions-to-section-230-immunity)
- [DEPARTMENT OF JUSTICE'S REVIEW OF SECTION 230 ...](https://www.justice.gov/archives/ag/department-justice-s-review-section-230-communications-decency-act-1996)
- [N.Y. Appellate Court Holds That Section 230 and First Amendment Protect Social Media Algorithmic Content Recommendation | Cahill Gordon & Reindel LLP](https://www.cahill.com/publications/client-alerts/2025-10-07-ny-appellate-court-holds-that-section-230-and-first-amendment-protect-social-media-algorithmic-content-recommendation)
- [Text - H.R.2794 - 119th Congress (2025-2026): NO FAKES Act of 2025 | Congress.gov | Library of Congress](https://www.congress.gov/bill/119th-congress/house-bill/2794/text)
- [All Info - H.R.6334 - 119th Congress (2025-2026): Deepfake Liability Act | Congress.gov | Library of Congress](https://www.congress.gov/bill/119th-congress/house-bill/6334/all-info)
- [H.R.6334 - 119th Congress (2025-2026): Deepfake Liability Act | Congress.gov | Library of Congress](https://www.congress.gov/bill/119th-congress/house-bill/6334/history)
- [Recent Developments in Artificial Intelligence Cases and Legislation 2025](https://www.americanbar.org/groups/business_law/resources/business-law-today/2025-august/recent-developments-artificial-intelligence-cases-legislation/)
- [
	Maloy and Auchincloss Introduce Deepfake Liability Act | U.S. Representative Celeste Maloy
](https://maloy.house.gov/news/documentsingle.aspx?DocumentID=1798)
- [Grok AI Exploitation Crisis in Spicy Mode](https://www.lawyer-monthly.com/2026/01/grok-ai-spicy-mode-crisis/)
- [Federal and State Regulators Target AI Chatbots and Intimate Imagery | Crowell & Moring LLP](https://www.crowell.com/en/insights/client-alerts/federal-and-state-regulators-target-ai-chatbots-and-intimate-imagery)
- [Recent Developments in Artificial Intelligence Cases and Legislation 2025](https://www.americanbar.org/groups/business_law/resources/business-law-today/2025-august/recent-developments-artificial-intelligence-cases-legislation/)
- [Generative AI Meets Section 230: The Future of Liability ...](https://businesslawreview.uchicago.edu/print-archive/generative-ai-meets-section-230-future-liability-and-its-implications-startup)
- [Take It Down or Take It Too Far? The Legal Fallout of New ...](https://scholarship.law.unc.edu/cgi/viewcontent.cgi?article=1521&context=ncjolt)
- [How AI-Generated Content Laws Are Changing Across the Country | MultiState](https://www.multistate.us/insider/2026/2/12/how-ai-generated-content-laws-are-changing-across-the-country)
- [The TAKE IT DOWN Act’s 48-Hour Deadline: What Does It Mean When Section 230 Still Shields Platforms? – University of Baltimore Law Review](https://ubaltlawreview.com/2025/11/03/the-take-it-down-acts-48-hour-deadline-what-does-it-mean-when-section-230-still-shields-platforms/)
- [The TAKE IT DOWN Act: A Federal Law Prohibiting the Nonconsensual Publication of Intimate Images | Congress.gov | Library of Congress](https://www.congress.gov/crs-product/LSB11314)
- [Beyond Section 230: Principles for AI Governance - Harvard Law Review](https://harvardlawreview.org/print/vol-138/beyond-section-230-principles-for-ai-governance/)
- [Text - H.R.6334 - 119th Congress (2025-2026): Deepfake Liability Act | Congress.gov | Library of Congress](https://www.congress.gov/bill/119th-congress/house-bill/6334/text)
- [Section 230 Under Fire: Recent Cases, Legal Workarounds, and Reforms - Dynamis LLP - Dynamis LLP](https://www.dynamisllp.com/knowledge/section-230-immunity-changes)
- [Platforms Face Section 230 Shift From Take It Down Act - Troutman Pepper Locke](https://www.troutman.com/insights/platforms-face-section-230-shift-from-take-it-down-act/)
- [Section 230 - Wikipedia](https://en.wikipedia.org/wiki/Section_230)
- [Section 230: A Juridical History](https://law.stanford.edu/wp-content/uploads/2025/02/A-Juridical-History-of-Section-230.pdf)
- [Page 89 TITLE 47—TELECOMMUNICATIONS § 230 and ...](https://www.govinfo.gov/link/uscode/47/230)
- [AI deepfakes testimony (May 2025) - Google Docs](https://advocacy.consumerreports.org/wp-content/uploads/2025/05/AI-deepfakes-testimony-May-2025-Google-Docs.pdf)
- [AI Porn Lawsuit: Can You Sue if You or Your Child is Victimized?](https://versustexas.com/blog/sue-for-ai-pornography/)
- [Section 230](https://www.eff.org/issues/cda230)
- [Section 230: A Brief Overview | Congress.gov | Library of Congress](https://www.congress.gov/crs-product/IF12584)
- [47 U.S. Code § 230 - Protection for private blocking and screening of offensive material | U.S. Code | US Law | LII / Legal Information Institute](https://www.law.cornell.edu/uscode/text/47/230)
- [Section 230: An Overview | Congress.gov | Library of Congress](https://www.congress.gov/crs-product/R46751)
- [47 USC 230: Protection for private blocking and screening ...](https://uscode.house.gov/view.xhtml?req=(title:47%20section:230%20edition:prelim))
- [Musk-Challenged California Anti-Deepfake Law Struck by Judge](https://news.bloomberglaw.com/litigation/musk-challenged-california-anti-deepfake-law-struck-by-judge)
- [AB 621 (Bauer-Kahan)](https://apcp.assembly.ca.gov/system/files/2025-03/ab-621-bauer-kahan.pdf)
- [California orders Elon Musk company to stop explicit deepfakes](https://calmatters.org/economy/technology/2026/01/california-investigates-deepfakes-elon-musk-company/)
