# AI-Generated CSAM in U.S. Law (2024–2026): What’s Illegal Now, What’s Changing, and How Platforms Must Respond

## Executive Summary

As of February 2026, the U.S. federal legal landscape for AI-generated Child Sexual Abuse Material (CSAM) has bifurcated into two distinct enforcement pathways: "child pornography" statutes for material depicting identifiable or "indistinguishable" minors, and "obscenity" statutes for wholly synthetic or virtual content. While the Department of Justice (DOJ) and FBI actively prosecute AI-generated CSAM under existing laws, courts are beginning to draw constitutional lines regarding private possession of purely virtual material.

**Key Findings:**
* **Dual Enforcement Tracks:** Prosecutors use **18 U.S.C. § 2252A** for "morphed" images (deepfakes of real children) and **18 U.S.C. § 1466A** for wholly synthetic content. Section 1466A explicitly states that the minor depicted need not actually exist, provided the material meets the legal standard for obscenity [1] [2].
* **Legislative Surge:** The **ENFORCE Act of 2025** (S. 3021), passed by the Senate in December 2025, aims to align penalties for synthetic CSAM with traditional CSAM, including mandatory sex offender registration and the removal of statutes of limitations [3] [4]. The **REPORT Act** (enacted May 2024) has already expanded reporting triggers for platforms to include child sex trafficking and enticement [5] [6].
* **Constitutional Friction:** In *United States v. Anderegg* (W.D. Wis. Feb 2025), a federal district court dismissed a possession charge for purely AI-generated CSAM on First Amendment grounds, citing *Stanley v. Georgia*, while allowing production and distribution charges to proceed. This signals a critical legal battleground over the private possession of virtual contraband [7] [8].
* **Explosive Growth in Reports:** NCMEC reported a **1,325% increase** in AI-related reports in 2024 (67,000 reports), surging to over **440,000 reports** in the first half of 2025 alone [9] [10].
* **Detection Gap:** Traditional hash-matching (PhotoDNA) is ineffective against novel AI-generated content. Industry standards are shifting toward hybrid models combining hashing with machine learning classifiers to detect synthetic abuse material [11] [12].

---

## 1. Federal Statutory Map: What Covers AI-Generated Content Now

Federal law criminalizes realistic AI-generated CSAM through two primary statutory vehicles. The choice of statute depends on whether the image depicts (or appears to depict) a real child or is a purely fictional creation.

### 1.1 Definitions That Capture Synthetic Content
The **PROTECT Act of 2003** established the foundational definitions used to prosecute modern AI crimes.
* **"Child Pornography" (18 U.S.C. § 2256(8)):** Includes any visual depiction that is a "computer or computer-generated image or picture" where the image is:
 * **(B) Indistinguishable:** A digital image that is "virtually indistinguishable" from that of a minor engaging in sexually explicit conduct [13] [14].
 * **(C) Identifiable Minor:** An image created, adapted, or modified to appear that an "identifiable minor" is engaging in such conduct. This subsection is the primary tool for prosecuting "deepfakes" or "morphed" images where a real child's face is superimposed onto sexually explicit material [13] [15].
* **"Indistinguishable" (18 U.S.C. § 2256(11)):** Defined as a depiction where "an ordinary person viewing the depiction would conclude that the depiction is of an actual minor." Crucially, this definition *excludes* drawings, cartoons, sculptures, or paintings, which are instead covered under obscenity laws [13] [16].

### 1.2 Prohibitions and Elements: §§ 2251–2252A vs. § 1466A
The DOJ utilizes different statutes based on the nature of the generated content.

| Statute | Target Content | Key Element | Penalty Range (First Offense) |
| :--- | :--- | :--- | :--- |
| **18 U.S.C. § 2251** | Production | Use of a minor (or persuasion/enticement) to produce sexually explicit material. | 15–30 years [17] |
| **18 U.S.C. § 2252A** | Distribution/Possession | Material containing "child pornography" (real or indistinguishable). | Dist: 5–20 years<br>Poss: Max 10 years (20 if prepubescent) [18] [19] |
| **18 U.S.C. § 1466A** | Obscenity (Virtual) | "Obscene visual representations" of sexual abuse. **Minor need not exist.** | Same as § 2252A [1] [2] |

**18 U.S.C. § 1466A (Child Obscenity):** This is the "workhorse" statute for wholly synthetic AI content. Subsection (c) explicitly states: *"It is not a required element of any offense under this section that the minor depicted actually exist"* [1] [2]. This allows prosecution of realistic AI images that do not correspond to any specific real-world child, provided the content meets the *Miller* test for obscenity (lacks serious literary, artistic, political, or scientific value) [20] [1].

### 1.3 Affirmative Defenses and Their Limits
Under **18 U.S.C. § 2252A(c)**, a defendant may assert an affirmative defense if the material was produced using only adults or was "not produced using any actual minor" [18] [19].
* **Morphing Exception:** This defense is **unavailable** for prosecutions involving "morphed" images (§ 2256(8)(C)), because the use of a real child's likeness is considered a harm in itself [18] [21].
* **Virtual Defense:** For purely synthetic content charged under § 2252A, defendants can argue the "virtual" defense. To circumvent this, prosecutors charge such content under § 1466A, where the non-existence of the minor is irrelevant [22] [23].

---

## 2. Constitutional Guardrails and Litigation Risk

The prosecution of AI-generated CSAM navigates a complex constitutional landscape defined by Supreme Court precedents on "virtual" pornography.

### 2.1 Supreme Court Pillars
* **Ashcroft v. Free Speech Coalition (2002):** The Court struck down bans on "virtual" child pornography that merely "appeared to be" minors, holding that if no real child was abused in the production, the speech is protected unless it is legally obscene [24] [25].
* **United States v. Williams (2008):** The Court upheld the criminalization of "pandering" or soliciting material as child pornography, even if the material offered is fake or virtual. This allows prosecution based on the *intent* to traffic in illegal material [26] [27].

### 2.2 2024–2026 Developments: The Possession Split
A significant legal fissure emerged in **United States v. Anderegg** (W.D. Wis. Feb 2025).
* **The Ruling:** The district court dismissed a charge of *possessing* AI-generated CSAM under § 1466A. The judge ruled that under *Stanley v. Georgia* (1969), the First Amendment protects the private possession of obscene material in one's home, provided no real child was involved in its creation [7] [8].
* **The Distinction:** The court allowed charges for *production* and *distribution* to proceed, reasoning that the creation and dissemination of such material fall outside *Stanley's* narrow protection for private possession [7].
* **Status:** The DOJ has appealed this dismissal to the Seventh Circuit (Case No. 25-1354), setting up a potential circuit split on the regulation of private AI generation [7].

### 2.3 Risk Matrix
* **High Risk:** Possession-only cases of wholly synthetic content (no real victim identified).
* **Low Risk:** Cases involving "morphed" images of real children (deepfakes), production, distribution, or solicitation/pandering.

---

## 3. 2024–2026 Legislation: What Changed and What’s Next

Recent legislative activity has focused on closing loopholes for synthetic media and increasing platform accountability.

### 3.1 REPORT Act (Enacted May 2024)
**Public Law 118-59** significantly expanded the obligations of online service providers [5] [6].
* **Expanded Triggers:** Providers must now report apparent violations of **child sex trafficking** (18 U.S.C. § 1591) and **enticement** (18 U.S.C. § 2422(b)) to the NCMEC CyberTipline [28].
* **Preservation:** The mandatory data preservation period for reported content increased from **90 days to 1 year** [28] [6].
* **Security:** Preservation must comply with the **NIST Cybersecurity Framework** [28].

### 3.2 ENFORCE Act (Passed Senate Dec 2025)
The **ENFORCE Act of 2025** (S. 3021) passed the Senate unanimously on December 16, 2025. If enacted by the House, it will fundamentally alter the treatment of synthetic CSAM [3] [29].

| Provision | Current Law | ENFORCE Act Change |
| :--- | :--- | :--- |
| **Pretrial Detention** | § 1466A not listed in § 3142 presumption. | Adds § 1466A to **presumption of detention** list [30] [4]. |
| **Statute of Limitations** | Standard federal limits apply. | **Removes statute of limitations** for § 1466A [30] [4]. |
| **Sex Offender Registry** | § 1466A not explicitly listed in SORNA. | Adds § 1466A to **SORNA registration** requirements [30] [4]. |
| **Production** | Ambiguity on interstate commerce hooks. | Clarifies § 2252A covers production of AI/modified images [3]. |

### 3.3 STOP CSAM Act (S. 1829)
Introduced in 2025, this bill proposes a "Victims' Right to Sue" provision that would allow civil lawsuits against platforms that "knowingly promote or facilitate" CSAM, potentially piercing Section 230 immunity for AI-generated content [31] [32].

---

## 4. Enforcement Patterns & Case Law (2024–2026)

The DOJ has aggressively prosecuted AI-generated CSAM, treating it as a priority threat.

### 4.1 Representative Federal Cases
* **U.S. v. Cody L. Prater (S.D. Ohio, Feb 2026):** Convicted of receiving/possessing AI-generated CSAM. The court explicitly ruled that **generative AI material depicting child abuse is "obscene" and not constitutionally protected speech**. Prater faces 15–40 years [33] [34].
* **U.S. v. Jeremy Weber (D. Kan., Nov 2025):** Sentenced to **25 years** for using AI to "morph" photos of 32 real children and women into sexually explicit images. Charged under § 2251 (Production) due to the use of real likenesses [35] [36].
* **U.S. v. William Michael Haslach (D. Minn., Feb 2025):** School employee charged with **Production of an Obscene Visual Representation** (§ 1466A) for using AI to morph photos of students. Faces mandatory minimum of 15 years [37] [38].

### 4.2 DOJ Policy
Assistant Attorney General A. Tysen Duva stated in February 2026: *"Child sexual abuse material, including that which is AI-generated, causes substantial harm. It further creates depraved and sadistic desires to harm real children"* [33]. The FBI's March 2024 PSA reinforced that *"Child Sexual Abuse Material Created by Generative AI... is Illegal"* under federal law [39].

---

## 5. "Aged-Up" Fictional Characters and Obscenity

The legal status of "aged-up" characters (fictional depictions appearing to be minors but claimed to be adults) is determined by **appearance**, not user labels.

* **"Indistinguishable" Standard:** Under § 2256(8)(B), if an ordinary person would conclude the image is of a minor, it is illegal. User tags claiming a character is "18+" or "3000-year-old vampire" are legally irrelevant if the visual depiction appears to be a child [13] [40].
* **Obscenity Application:** For stylized content (anime/cartoons) that is not "indistinguishable" from a real child, § 1466A applies. Courts have upheld convictions for obscene cartoons of minors (e.g., *U.S. v. Whorley*), ruling that the "virtual" nature does not protect obscene speech [41] [42].

---

## 6. NCMEC Reporting Framework for AI Platforms

Under **18 U.S.C. § 2258A**, AI platforms (as Electronic Service Providers) have strict reporting duties.

### 6.1 Reporting Triggers
Providers must report to the NCMEC CyberTipline "as soon as reasonably possible" after obtaining **actual knowledge** of:
* Child Pornography (§§ 2251, 2252A, etc.)
* Child Sex Trafficking (§ 1591)
* Enticement/Coercion (§ 2422(b)) [28] [43].

### 6.2 Compliance Requirements
* **Preservation:** Must preserve reported content and "commingled" context data for **1 year** [28].
* **Security:** Storage must comply with **NIST Cybersecurity Framework** standards [28].
* **Penalties:** Fines for knowing failure to report range from **$850,000 to $1,000,000** per violation for large providers (>100M users) [28].

---

## 7. Detection Technology: Hash-Matching vs. AI

The surge in synthetic content has rendered traditional detection methods insufficient.

### 7.1 The Technology Gap
* **PhotoDNA (Hash-Matching):** Effective only for **known** CSAM (images already in a database). It cannot detect unique, newly generated AI images [44] [11].
* **AI Classifiers:** Essential for detecting **novel** synthetic content. Tools like Thorn's classifier and Discord's "Clip" analyze visual features to identify potential abuse in new images [11] [45].

### 7.2 Industry Best Practices
NCMEC and the Tech Coalition recommend a **hybrid approach**:
1. **Hashing:** Use PhotoDNA/PDQ to block known abuse material instantly.
2. **Classifiers:** Deploy ML models to flag novel AI outputs and prompts.
3. **Provenance:** Implement standards like **C2PA** to track content origin and manipulation [46] [47].

---

## 8. Penalties and Enforcement Trends

Penalties for AI-generated CSAM are severe and increasingly aligned with those for abuse of real children.

### 8.1 Statutory Penalties
* **Production (§ 2251 / § 1466A):** 15–30 years imprisonment [17].
* **Distribution (§ 2252A / § 1466A):** 5–20 years (15–40 years with priors) [18] [1].
* **Possession (§ 2252A / § 1466A):** Up to 10 years (up to 20 years if involving prepubescent minor) [18] [1].

### 8.2 Enforcement Trends (2024–2026)
* **Volume:** NCMEC reports involving Generative AI skyrocketed from **4,700** in 2023 to **67,000** in 2024, and **440,419** in the first half of 2025 [9] [10].
* **State Action:** 45 states have enacted laws explicitly criminalizing AI-generated CSAM as of 2025. For example, **Virginia's SB 731** (effective July 2024) criminalizes depictions "sufficiently realistic" to believe they are minors, even if the minor does not exist [48] [49].
* **Sentencing:** Courts are handing down lengthy sentences for AI-enabled crimes, such as the **75-year sentence** for Justin Ryan Culmo (2025) and **40 years** for the Charlotte psychiatrist (2023/2024) [39] [50].

### 8.3 Future Outlook
If the **ENFORCE Act** is enacted, expect immediate shifts in pretrial handling (presumption of detention) and long-term offender tracking (SORNA registration) for all synthetic CSAM defendants. Platforms should anticipate increased liability pressure and stricter enforcement of reporting timelines as AI-generated volume continues to grow.

## References

1. *18 U.S. Code § 1466A - Obscene visual representations of the sexual abuse of children | U.S. Code | US Law | LII / Legal Information Institute*. https://www.law.cornell.edu/uscode/text/18/1466A
2. *18 USC 1466A: Obscene visual representations ...*. https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title18-section1466A&num=0&edition=prelim
3. *Text - S.3021 - 119th Congress (2025-2026): ENFORCE Act | Congress.gov | Library of Congress*. https://www.congress.gov/bill/119th-congress/senate-bill/3021/text
4. *BILLS-119s3021es.xml*. https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3021es.xml
5. *S.474 - 118th Congress (2023-2024): REPORT Act | Congress.gov | Library of Congress*. https://www.congress.gov/bill/118th-congress/senate-bill/474
6. *Text - S.474 - 118th Congress (2023-2024): REPORT Act | Congress.gov | Library of Congress*. https://www.congress.gov/bill/118th-congress/senate-bill/474/text
7. *Court Rules That Constitution Protects Private Possession of AI-Generated CSAM | TechPolicy.Press*. https://techpolicy.press/court-rules-that-constitution-protects-private-possession-of-aigenerated-csam
8. *Possession of AI-generated child sexual abuse imagery may be protected by First Amendment in some cases, judge rules*. https://www.nbcnews.com/tech/tech-news/ai-generated-child-sexual-abuse-imagery-judge-ruling-rcna196710
9. *Spike in online crimes against children a “wake-up call”*. https://www.missingkids.org/blog/2025/spike-in-online-crimes-against-children-a-wake-up-call
10. *2024-CyberTipline-Report.pdf*. http://ncmec.org/content/dam/missingkids/pdfs/cybertiplinedata2024/2024-CyberTipline-Report.pdf
11. *CSAM Classifiers: Find Novel Content with Predictive AI | Safer by Thorn*. https://safer.io/resources/comprehensive-csam-detection-combines-hashing-and-matching-with-classifiers/
12. *Artificial Intelligence and 'Gen AI' - WeProtect Global Alliance*. https://www.weprotect.org/thematic/artificial-intelligence-and-gen-ai/
13. *18 U.S. Code § 2256 - Definitions for chapter | U.S. Code | US Law | LII / Legal Information Institute*. https://www.law.cornell.edu/uscode/text/18/2256
14. *18 USC 2256: Definitions for chapter*. https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title18-section2256&num=0&edition=prelim
15. *                United States v. Mecham, No. 19-40319 (5th Cir. 2020) :: Justia    *. https://law.justia.com/cases/federal/appellate-courts/ca5/19-40319/19-40319-2020-02-14.html
16. *Page 491 TITLE 18—CRIMES AND CRIMINAL ...*. https://www.govinfo.gov/content/pkg/USCODE-2011-title18/pdf/USCODE-2011-title18-partI-chap110-sec2256.pdf
17. *18 U.S.C. § 2251 - U.S. Code Title 18. Crimes and Criminal Procedure § 2251 | FindLaw*. https://codes.findlaw.com/us/title-18-crimes-and-criminal-procedure/18-usc-sect-2251/
18. *18 U.S. Code § 2252A - Certain activities relating to material ...*. https://www.law.cornell.edu/uscode/text/18/2252A
19. *2252A: Certain activities relating to material constituting or ...*. https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title18-section2252A&num=0&edition=prelim
20. * Criminal Division |  Citizen's Guide To U.S. Federal Law On Obscenity*. https://www.justice.gov/criminal/criminal-ceos/citizens-guide-us-federal-law-obscenity
21. *S. Rept. 108-2 - THE PROTECT ACT OF 2003 | Congress.gov | Library of Congress*. https://www.congress.gov/committee-report/108th-congress/senate-report/2/1
22. *Crafting New Boundaries: Model Legislation to Address the ...*. https://scholarship.stu.edu/cgi/viewcontent.cgi?article=1673&context=stlr
23. *Child Pornography: Constitutional Principles and Federal Statutes - EveryCRSReport.com*. https://www.everycrsreport.com/reports/95-406.html
24. *Ashcroft v. Free Speech Coalition*. https://en.wikipedia.org/wiki/Ashcroft_v._Free_Speech_Coalition
25. * Ashcroft v. Free Speech Coalition | 535 U.S. 234 (2002) | Justia U.S. Supreme Court Center*. https://supreme.justia.com/cases/federal/us/535/234/
26. *United States v. Williams (2008) - Free Speech Center - MTSU*. https://firstamendment.mtsu.edu/article/united-states-v-williams/
27. * United States v. Williams | 553 U.S. 285 (2008) | Justia U.S. Supreme Court Center*. https://supreme.justia.com/cases/federal/us/553/285/
28. *18 USC 2258A: Reporting requirements of providers*. https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title18-section2258A&num=0&edition=prelim
29. *Congressional Record | Congress.gov | Library of Congress*. https://www.congress.gov/congressional-record/volume-171/issue-212/senate-section/article/S8754-1
30. *H.R.4831 - 119th Congress (2025-2026): ENFORCE Act*. https://www.congress.gov/bill/119th-congress/house-bill/4831/text
31. *Text - S.1829 - 119th Congress (2025-2026): STOP CSAM Act of 2025 | Congress.gov | Library of Congress*. https://www.congress.gov/bill/119th-congress/senate-bill/1829/text
32. *Durbin Calls On Congress To Pass His Bil... | United States Senate Committee on the Judiciary*. https://www.judiciary.senate.gov/press/dem/releases/durbin-calls-on-congress-to-pass-his-bill-combatting-online-child-sexual-abuse-material
33. * Office of Public Affairs |  Repeat Sex Offender Convicted of Child Exploitation Offenses, Including Receiving and Possessing AI-Generated Child Sexual Abuse Material | United States Department of Justice*. https://www.justice.gov/opa/pr/repeat-sex-offender-convicted-child-exploitation-offenses-including-receiving-and-possessing
34. *Vinton County Man Convicted for Possession and Creation of Child*. https://hoodline.com/2026/02/vinton-county-man-convicted-for-possession-and-creation-of-child-pornography-including-ai-generated-material/
35. *Topeka Man Sentenced to 25 Years for Artificial ...*. https://www.justice.gov/usao-ks/pr/topeka-man-sentenced-25-years-artificial-intelligence-related-child-exploitation
36. *Topeka man sentenced for AI related child exploitation offenses*. https://www.wibw.com/2025/11/06/topeka-man-sentenced-ai-related-child-exploitation-offenses/
37. *Former School District Employee Charged with Using AI ...*. https://www.justice.gov/usao-mn/pr/former-school-district-employee-charged-using-ai-technology-produce-sexual-abuse-0
38. * District of Minnesota |  Haslach Child Exploitation Case (School District Employee) | United States Department of Justice*. https://www.justice.gov/usao-mn/haslach-child-exploitation-case-school-district-employee-0
39. *Internet Crime Complaint Center (IC3) | Child Sexual Abuse Material Created by Generative AI and Similar Online Tools is Illegal*. https://www.ic3.gov/PSA/2024/PSA240329
40. *Common Terms | Federal Internet Sex Crimes*. https://www.jzcclaw.com/handbook/chapter-1-common-terms/
41. *File:United States v Whorley.pdf - Wikisource, the free online library*. https://en.wikisource.org/wiki/File:United_States_v_Whorley.pdf
42. *1 It was never so stated, but is likely that the cartoons are ...*. https://www.govinfo.gov/content/pkg/USCOURTS-tned-2_13-cr-00090/pdf/USCOURTS-tned-2_13-cr-00090-0.pdf
43. *18 U.S. Code § 2258A - Reporting requirements of providers | U.S. Code | US Law | LII / Legal Information Institute*. https://www.law.cornell.edu/uscode/text/18/2258A
44. *PhotoDNA | Microsoft*. https://www.microsoft.com/en-us/photodna
45. *Annual Report 2024*. https://technologycoalition.org/wp-content/uploads/Tech-Coalition-Annual-Report-2024.pdf
46. *Strengthening Multimedia Integrity in the Generative AI Era*. https://media.defense.gov/2025/Jan/29/2003634788/-1/-1/0/CSI-CONTENT-CREDENTIALS.PDF
47. *NIST: Reducing Risks Posed by Synthetic Content An Overview of Technical Approaches to Digital Content Transparency*. https://www.aigl.blog/nist-reducing-risks-posed-by-synthetic-content-an-overview-of-technical-approaches-to-digital-content-transparency/
48. *State Laws Criminalizing AI-generated or Computer-Edited CSAM - Enough Abuse*. https://enoughabuse.org/get-vocal/laws-by-state/state-laws-criminalizing-ai-generated-or-computer-edited-child-sexual-abuse-material-csam/
49. *Virginia Expands Definition of Child Pornography to Include Fictional Depictions — Northern Valley Law*. https://www.northernvalleylaw.com/blog/virginia-expands-definition-of-child-pornography-to-include-fictional-depictions
50. *Oldsmar Man Sentenced To 75 Years For Producing And ...*. https://www.justice.gov/usao-mdfl/pr/oldsmar-man-sentenced-75-years-producing-and-distributing-child-sexual-abuse-and-ai