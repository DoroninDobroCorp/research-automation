# Texas Deepfakes Law 2026 — What’s Illegal, Who’s Liable, and How to Comply

## Executive Summary
As of February 2026, Texas has established one of the nation's most comprehensive legal frameworks for artificial intelligence (AI) and deepfakes, shifting from narrow, video-specific bans to a broad regime covering all synthetic media types and imposing intent-based civil liability on AI developers.

**Key Strategic Insights:**
* **The "Image Loophole" is Closed:** Effective September 1, 2025, House Bill 449 and Senate Bill 441 expanded Texas Penal Code §21.165 to cover "deep fake media," explicitly criminalizing AI-generated still images alongside videos. The law now punishes the "knowing" production or distribution of non-consensual intimate deepfakes as a Class A misdemeanor, with felony enhancements for repeat offenses or minor victims. [1] [2] [3]
* **Civil Liability Targets "Intent":** The Texas Responsible AI Governance Act (TRAIGA), effective January 1, 2026, introduces a regulatory framework enforced exclusively by the Attorney General (AG). It prohibits developing or deploying AI systems with the *sole intent* of producing unlawful deepfakes or child sexual abuse material (CSAM). Violations carry civil penalties up to $200,000, but the law offers a safe harbor for companies that align with the NIST AI Risk Management Framework. [4] [5] [6]
* **Adult Content is a High-Risk Zone:** New laws have tightened the net around non-consensual intimate media. Penal Code §43.26 was amended to criminalize "computer-generated" CSAM that is virtually indistinguishable from real children. Additionally, the U.S. Supreme Court's 2025 ruling in *Free Speech Coalition v. Paxton* upheld Texas's age-verification mandates for adult websites, cementing strict compliance requirements for platforms hosting sexual content. [7] [8] [9]
* **Political Deepfakes Face Constitutional Headwinds:** While Texas was the first state to ban election deepfakes (SB 751, 2019), the Texas Court of Criminal Appeals' 2024 decision in *Ex parte Stafford* struck down a related "true source" disclosure law as unconstitutional. This casts a shadow over the enforceability of election-specific speech restrictions, though the deepfake-specific provision (§255.004(d)) remains on the books. [10] [11]
* **Platform Immunity Remains Strong but Porous:** TRAIGA protects developers from liability for end-user misuse absent prohibited intent. However, platforms may face liability under federal sex-trafficking exceptions (FOSTA-SESTA) if they "knowingly benefit" from unlawful conduct, a risk heightened by algorithmic amplification of harmful content. [6] [12] [13]

---

## Scope, Statutes, and What Changed Since 2023
Texas has moved from a patchwork of specific bans to a cohesive regulatory environment that targets both the creators of harmful content and the developers of the tools used to create it.

### Core Criminal Statutes and Elements
The primary criminal statutes governing deepfakes are found in the Texas Penal Code.

| Statute | Target Content | Key Elements & Mens Rea | Penalty Class | Effective Date |
| :--- | :--- | :--- | :--- | :--- |
| **Penal Code §21.165** (via SB 1361, HB 449, SB 441) | **Sexually Explicit Deepfakes** (Video & Image) | **Knowingly** produce/distribute deep fake media appearing to depict intimate parts or sexual conduct without effective consent. Includes **threats** to distribute. | **Class A Misdemeanor**<br>Enhancements: 3rd Degree Felony (victim <18 or prior conviction). | Sept 1, 2025 (Current version) [1] [3] |
| **Penal Code §43.26** (via SB 20, SB 1621) | **CSAM & AI-Generated Children** | Possession/promotion of visual material depicting a "computer-generated child" virtually indistinguishable from a real minor. | **State Jail Felony** to **2nd Degree Felony** depending on quantity and intent. | Sept 1, 2025 [7] [9] |
| **Election Code §255.004** (via SB 751) | **Election Deepfakes** | Creating/distributing a deep fake video within **30 days** of an election with intent to injure a candidate or influence the result. | **Class A Misdemeanor** | Sept 1, 2019 [14] [15] |

**Key Definitions:**
* **"Deep Fake Media":** A visual depiction created or altered through software, machine learning, or AI that appears to a reasonable person to depict a real person, indistinguishable from an authentic depiction, performing an action that did not occur in reality. [2] [16]
* **"Consent":** Under §21.165(b-2), consent is valid *only* if the depicted person knowingly and voluntarily signs a written agreement drafted in plain language describing the media and its intended use. [3]

### Civil AI Regulation (TRAIGA)
The **Texas Responsible AI Governance Act (TRAIGA)** (HB 149), effective January 1, 2026, creates a civil regulatory layer on top of criminal laws.

* **Prohibited Intents:** It is unlawful to develop or deploy an AI system with the **sole intent** of producing child pornography or unlawful deepfakes (as defined in §21.165). It also bans systems intended for behavioral manipulation (inciting self-harm or crime) or unlawful discrimination. [5] [17] [18]
* **Enforcement:** Exclusive authority lies with the Texas Attorney General. There is **no private right of action**. The AG may issue Civil Investigative Demands (CIDs) to inspect algorithms and training data. [6] [18]
* **Regulatory Sandbox:** The Department of Information Resources (DIR) administers a sandbox allowing approved applicants to test AI systems for up to 36 months with limited regulatory waivers. [17] [6]

### Election-Related Deepfakes (SB 751)
Enacted in 2019, **Texas Election Code §255.004(d)** criminalizes creating a "deep fake video" with the intent to deceive and influence an election within 30 days of the vote.
* **Status:** While this specific provision remains active, the Texas Court of Criminal Appeals struck down a related subsection (§255.004(b)) in *Ex parte Stafford* (2024), ruling that a ban on misrepresenting the "true source" of campaign communications was unconstitutionally overbroad. This precedent suggests §255.004(d) could face similar scrutiny if challenged, particularly regarding satire or parody. [10] [11]

---

## Criminal vs. Civil Liability
Texas law distinguishes sharply between the criminal liability of individual bad actors and the civil compliance obligations of AI companies.

### Criminal Penalties Matrix
Criminal penalties focus on the non-consensual exploitation of individuals.

| Offense | Classification | Potential Sentence | Fine |
| :--- | :--- | :--- | :--- |
| **Production/Distribution of Deepfake Porn** (§21.165) | Class A Misdemeanor | Up to 1 year in jail | Up to $4,000 [19] [20] |
| **...with Minor Victim (<18)** | 3rd Degree Felony | 2 to 10 years in prison | Up to $10,000 [19] [3] |
| **Threatening to Distribute** (§21.165(b-1)) | Class B Misdemeanor | Up to 180 days in jail | Up to $2,000 [19] [3] |
| **Possession of AI CSAM** (§43.26) | State Jail Felony | 180 days to 2 years | Up to $10,000 [7] [21] |

**Restitution:** Courts *must* order restitution for psychological, financial, or reputational harm resulting from §21.165 offenses. [22]

### Civil Enforcement and Private Suits
Civil liability is bifurcated between state enforcement and private torts.

* **TRAIGA Civil Penalties (AG Only):**
 * **Curable Violations:** $10,000 – $12,000 per violation (if cured within 60 days).
 * **Uncurable Violations:** $80,000 – $200,000 per violation.
 * **Continuing Violations:** Up to $40,000 per day. [5] [23]
* **Private Civil Suits (CPRC Chapter 98B):** Victims of "artificial intimate visual material" can sue creators and "reckless" facilitators for damages, mental anguish, and injunctive relief. Platforms may be liable if they fail to remove content within **72 hours** of a request. [24] [3]
* **DTPA:** Deceptive AI practices (e.g., misleading consumers about AI capabilities) can trigger treble damages under the Deceptive Trade Practices Act if the conduct is "knowing" or "intentional." [25] [26]

---

## Adult Content and Age-Gating
The intersection of AI and adult content is heavily regulated, with strict requirements for consent and access control.

### Synthetic Intimate Media
Penal Code §21.165 (Deepfakes) and §21.16 (Revenge Porn) work in tandem. §21.165 explicitly incorporates definitions of "intimate parts" and "sexual conduct" from §21.16.
* **Consent:** The 2025 amendments introduced a rigorous consent standard. A signed, plain-language written agreement is required to validate consent for deepfake depictions. [3]
* **No Disclaimer Defense:** It is *not* a defense to prosecution that the media contains a label or disclaimer stating it is unauthorized or inauthentic. [3]

### HB 1181: Age Verification Enforceability
Following the U.S. Supreme Court's June 2025 ruling in *Free Speech Coalition v. Paxton*, Texas's age-verification law (HB 1181) is enforceable.
* **Requirement:** Commercial websites where >1/3 of content is "harmful to minors" must verify users are 18+ using government ID or transactional data. [8] [27]
* **Status:** The age-verification requirement was upheld as a valid measure to protect children. However, the Fifth Circuit previously enjoined the portion of the law requiring "health warnings" on pornographic sites, a ruling left undisturbed by the Supreme Court. [28] [8]

---

## Platform Liability vs. Creator Liability
Texas law attempts to thread the needle between holding bad actors accountable and preserving innovation, often deferring to federal immunity for neutral platforms.

### TRAIGA’s Intent Standard
TRAIGA explicitly shields developers and deployers from liability if an end-user utilizes their AI system for a prohibited purpose, provided the developer did not have the **sole intent** to facilitate that violation. [6] [18]
* **Safe Harbor:** Developers can assert an affirmative defense if they discover violations through internal "red-teaming" or if they substantially comply with the **NIST AI Risk Management Framework (RMF)**. [5] [18]

### Section 230 and Federal Preemption
While TRAIGA creates state-level duties, federal law (47 U.S.C. § 230) generally immunizes platforms from liability for third-party content. However, exceptions exist:
* **FOSTA-SESTA:** Section 230 does not protect platforms from state criminal prosecutions or civil claims related to sex trafficking if the platform "knowingly benefits" from the conduct. [12] [29]
* **Texas Case Law:** In *In re Facebook* (2021), the Texas Supreme Court ruled that Section 230 did not bar statutory human trafficking claims where the platform allegedly facilitated the crime. This precedent could potentially extend to platforms that knowingly host and profit from non-consensual deepfake markets. [13]

---

## Enforcement History
While the legal framework is new, enforcement patterns are beginning to emerge.

### Criminal Prosecutions
* **Aledo High School Case (2023/2024):** A juvenile student was charged with "sale/distribution/display of harmful material to a minor" for creating AI-generated nude images of classmates. The case highlighted the accessibility of deepfake tools and led to calls for federal legislation (the "Take It Down Act"). [30] [31]
* **Prosecutorial Trends:** Defense firms report that prosecutors in major counties (Harris, Dallas) are actively charging individuals under §21.165, treating it as a priority sex crime. [19] [32]

### Civil Actions
* **State of Texas v. Snap, Inc. (Feb 2026):** Attorney General Paxton filed suit against Snap, Inc., alleging deceptive trade practices regarding parental warnings and safety features. While not exclusively a deepfake case, it signals the AG's aggressive stance on platform accountability and child safety. [33]

---

## Constitutional and Preemption Risk
The durability of Texas's deepfake laws depends on their ability to survive First Amendment scrutiny.

* **Revenge Porn Upheld:** In *Ex parte Jones* (2021), the Texas Court of Criminal Appeals (TCCA) upheld the "revenge porn" statute (§21.16), ruling it was narrowly tailored to protect substantial privacy interests. This precedent strongly supports the constitutionality of §21.165, which mirrors its structure. [34] [35]
* **Election Law Struck Down:** In *Ex parte Stafford* (2024), the TCCA declared Election Code §255.004(b) (the "true source" provision) unconstitutional for being overbroad. While §255.004(d) (the deepfake provision) remains, it faces similar risks if applied to satire or parody without clear evidence of intent to deceive. [10] [11]

---

## Compliance Playbooks and Safe Harbors
For organizations operating in Texas, compliance requires a mix of technical safeguards and documentation.

### TRAIGA-Aligned Controls
To leverage TRAIGA's affirmative defenses, organizations should:
1. **Adopt NIST AI RMF:** Map internal governance to the NIST "Govern, Map, Measure, Manage" functions. [18] [36]
2. **Document Intent:** Maintain records of design decisions, intended use cases, and safeguards to disprove "sole intent" to create harm. [37]
3. **Red-Teaming:** Conduct and log adversarial testing to identify potential misuse vectors before deployment. [18]

### 60-Day Cure Period
TRAIGA requires the AG to provide a 60-day notice before filing suit. Companies should have a "Cure Protocol" ready:
* **Immediate Remediation:** Fix the identified violation.
* **Documentation:** Submit a written statement and proof of cure to the AG.
* **Policy Update:** Revise internal policies to prevent recurrence. [5] [23]

### Sector-Specific Actions
| Sector | Priority Action |
| :--- | :--- |
| **AI Developers** | Implement content filters for CSAM/Nudity; publish transparency reports; align with NIST RMF. |
| **Platforms** | Establish 48-72 hour takedown SLAs for deepfakes; implement hash-matching for known CSAM. |
| **Adult Sites** | Implement age-verification (HB 1181); secure written consent for all synthetic performers. |
| **Campaigns** | Label all AI-generated content; archive provenance data to defend against §255.004 claims. |

---

## Insurance and Contracts
Risk transfer strategies are evolving to match the new liability landscape.

* **Insurance:**
 * **Media Liability:** The primary coverage for defamation and privacy torts arising from deepfakes. [38] [39]
 * **Cyber Insurance:** Increasingly covers "AI-Related Security Events" and social engineering fraud. [40]
 * **CGL Exclusions:** Be aware that new ISO endorsements (CG 40 47/48) specifically exclude generative AI liability from standard Commercial General Liability policies. [41]
* **Contractual Protections:**
 * **Indemnities:** Seek specific indemnity for "intentional misuse" of AI tools.
 * **Warranties:** Require vendors to warrant compliance with TRAIGA and NIST standards.
 * **Disclosure:** Mandate disclosure of AI use in deliverables to comply with state transparency laws. [42]

---

## Forward Look: 2026 and Beyond
The regulatory environment will continue to tighten.

* **2027 Legislative Session:** Interim charges released in January 2026 indicate a focus on expanding deepfake penalties and closing disclosure gaps for non-political synthetic media. [43]
* **AI Advisory Council:** The newly formed council will issue reports on ethical AI use and legal risks, likely shaping the next wave of legislation. [17] [44]
* **Federal Preemption:** Watch for potential conflicts between Texas laws and any emerging federal AI regulations, though TRAIGA is designed to be consistent with federal standards like NIST.

## References

1. *Sec. 21.165.ï¿½ UNLAWFUL PRODUCTION OR ...*. https://capitol.texas.gov/tlodocs/89R/analysis/html/HB00449E.htm
2. *89(R) HB 449 - Enrolled version - Bill Text*. https://capitol.texas.gov/tlodocs/89R/billtext/html/HB00449F.HTM
3. *Bill Text: TX SB441 | 2025-2026 | 89th Legislature | Enrolled | LegiScan*. https://legiscan.com/TX/text/SB441/id/3249644
4. *Texas Enters the AI Sandbox with TRAIGA*. https://www.americanbar.org/groups/business_law/resources/business-law-today/2025-july/texas-enters-ai-sandbox-with-traiga-implications-business-trials/
5. *Texas Enacts AI Consumer Protection Law | Inside Privacy*. https://www.insideprivacy.com/artificial-intelligence/texas-enacts-ai-consumer-protection-law/
6. *Texas Signs Responsible AI Governance Act Into Law*. https://www.lw.com/en/insights/texas-signs-responsible-ai-governance-act-into-law
7. *Possession or Promotion of Child Pornography - Texas PC §43.26*. https://saputo.law/criminal-law/texas/possession-of-child-pornography/
8. *23-1122 Free Speech Coalition, Inc. v. Paxton (06/27/2025)*. https://www.supremecourt.gov/opinions/24pdf/23-1122_3e04.pdf
9. *Supplement: TX SB1621 | 2025-2026 | 89th Legislature | Analysis (Enrolled) | LegiScan*. https://legiscan.com/TX/supplement/SB1621/id/615571
10. *                EX PARTE STAFFORD :: 2024 :: Texas Court of Criminal Appeals Decisions :: Texas Case Law :: Texas Law :: U.S. Law :: Justia    *. https://law.justia.com/cases/texas/court-of-criminal-appeals/2024/pd-0310-23.html
11. *EX PARTE JOHN MORGAN STAFFORD v. << (2024) | FindLaw*. https://caselaw.findlaw.com/court/tx-court-of-criminal-appeals/116545511.html
12. *47 U.S. Code § 230 - Protection for private blocking and screening of offensive material | U.S. Code | US Law | LII / Legal Information Institute*. https://www.law.cornell.edu/uscode/text/47/230
13. *In re Facebook, Inc. | No. 20-0434 | Tex. | Judgment | Law | CaseMine*. https://www.casemine.com/judgement/us/60d8fc404653d0241a1f3c49
14. *86(R) SB 751*. https://capitol.texas.gov/tlodocs/86R/billtext/pdf/SB00751F.pdf
15. *Texas Election Code - ELEC § 255.004 | FindLaw*. https://codes.findlaw.com/tx/election-code/elec-sect-255-004.html
16. *21.165. Unlawful Production or Distribution of Certain Sexually Explicit Videos | WomensLaw.org*. https://www.womenslaw.org/laws/tx/statutes/21165-unlawful-production-or-distribution-certain-sexually-explicit-videos
17. *Responsible Artificial Intelligence Governance Act*. https://capitol.texas.gov/tlodocs/89R/analysis/html/HB00149S.htm
18. *89(R) HB 149 - Enrolled version - Bill Text*. https://capitol.texas.gov/tlodocs/89R/billtext/html/HB00149F.htm
19. *Is Deepfake Porn Illegal in Texas? 2026 Laws & Defense*. https://mcconathylaw.com/blog/deepfake-defense-lawyer/
20. *Are Deepfake Videos Illegal in Texas?*. https://www.nealdavislaw.com/criminal-defense-guides/deepfake-videos/
21. *Texas Constitution and Statutes*. https://statutes.capitol.texas.gov/GetStatute.aspx?Code=PE&Value=43.21
22. *Texas Deepfake Porn Law: Production of Sexually Explicit ...*. https://saputo.law/criminal-law/texas/unlawful-production-or-distribution-of-certain-sexually-explicit-videos-deep-fake-pornography/
23. *The Texas Responsible AI Governance Act*. https://www.nortonrosefulbright.com/en/knowledge/publications/c6c60e0c/the-texas-responsible-ai-governance-act
24. *Texas-2025-SB441-Enrolled*. https://legiscan.com/TX/text/SB441/id/3249644/Texas-2025-SB441-Enrolled.html
25. *Texas Deceptive Trade Practices-Consumer Protection Act*. https://www.templelawoffice.com/wp-content/uploads/sites/1501901/2020/01/Texas-Deceptive-Trade-Practices.pdf
26. * Texas Business and Commerce Code Section 17.49 (2024) - Exemptions :: 2024 Texas Statutes :: U.S. Codes and Statutes :: U.S. Law :: Justia*. https://law.justia.com/codes/texas/business-and-commerce-code/title-2/chapter-17/subchapter-e/section-17-49/
27. *88(R) HB 1181 - House Committee Report version - Bill Text*. https://capitol.texas.gov/tlodocs/88R/billtext/html/HB01181H.htm
28. *Free Speech Coal. Inc. v. Paxton*. https://www.ca5.uscourts.gov/opinions/pub/23/23-50627-CV0.pdf
29. *Public Law 115–164 115th Congress An Act*. https://www.congress.gov/115/plaws/publ164/PLAW-115publ164.pdf
30. *North Texas teen victim of deepfake calls for federal law*. https://spectrumlocalnews.com/tx/south-texas-el-paso/news/2024/06/19/aledo-high-school-teen-deepfake-victim-ted-cruz-legislation
31. *Aledo youth, mom lobby for protection with the Take it Down Act to combat revenge social media posts | The Community News*. https://www.community-news.com/stories/article,85003
32. *AI Deepfake Porn — Texas Laws Explained | Thiessen Law Firm*. https://www.thetexastrialattorney.com/blog/ai-deepfake-porn-texas/
33. *News Releases | Office of the Attorney General*. https://www.texasattorneygeneral.gov/news/releases
34. *IN THE COURT OF CRIMINAL APPEALS OF TEXAS*. https://www.courthousenews.com/wp-content/uploads/2021/05/Texas-revenge-porn-ruling.pdf
35. *EX PARTE JONES v. << (2021) | FindLaw*. https://caselaw.findlaw.com/court/tx-court-of-criminal-appeals/2128800.html
36. *TRAIGA Compliance Guide: Texas AI Law Requirements for 2026 | Modulos Blog | Modulos*. https://modulos.ai/blog/traiga-compliance-guide-texas-ai-law-requirements-for-2026/
37. *Texas Enacts Responsible AI Governance Act*. https://www.bakerbotts.com/thought-leadership/publications/2025/july/texas-enacts-responsible-ai-governance-act-what-companies-need-to-know
38. *Insurance Coverage Issues for Deepfakes, Part II: Providing Protection*. https://www.americanbar.org/groups/litigation/resources/newsletters/insurance-coverage/insurance-coverage-issues-deepfakes-part-two-protection/
39. *Media Liability | beazley*. https://beazley.com/en/products/specialty-risk-usa/media-liability/
40. *AI Advancements Are Reshaping Cyber Insurance Coverage*. https://www.coalitioninc.com/blog/cyber-insurance/ai-advancements-are-reshaping-cyber-insurance-coverage
41. *New Generative AI Insurance Exclusions: What Businesses Need to Know in 2026*. https://phl-firm.com/generative-ai-insurance-exclusions-2026/
42. *City of Fort Worth - Generative AI Policy*. https://www.fortworthtexas.gov/files/assets/public/v/1/hr/documents/employees/2024-docs/generative-artificial-intelligence-ai-policy_approved-12.18.23.pdf
43. *First Round of Texas Senate Interim Charges Sets Early 2026 Priorities - Texas Policy Research*. https://www.texaspolicyresearch.com/first-round-of-texas-senate-interim-charges-sets-early-2026-priorities/
44. *The AI Advisory Council: What you need to know - Texas 2036*. https://texas2036.org/posts/the-ai-advisory-council-what-you-need-to-know/