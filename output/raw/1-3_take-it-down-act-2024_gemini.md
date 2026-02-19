The Take It Down Act: A Comprehensive Legal, Operational, and Technical Analysis of Federal Mandates on Nonconsensual Intimate Imagery and Deepfake Regulation
Executive Summary
The enactment of the Tools to Address Known Exploitation by Immobilizing Technological Deepfakes on Websites and Networks Act (commonly referred to as the TAKE IT DOWN Act), signed into law as Public Law 119-12 on May 19, 2025, represents a watershed moment in United States internet regulation.1 For the first time, federal law explicitly criminalizes the publication of "digital forgeries" (deepfakes) and establishes a unified federal framework for the rapid removal of nonconsensual intimate imagery (NCII).
This report provides an exhaustive examination of the Act’s statutory requirements, compliance obligations, and legal implications. As of February 2026, covered platforms are in the final stages of preparing for the May 19, 2026 compliance deadline for the Act's civil notice-and-takedown provisions.3 Meanwhile, the criminal provisions of the Act have been in force since enactment, empowering the Department of Justice (DOJ) to prosecute individuals who knowingly publish or threaten to publish NCII and malicious deepfakes.5
The Act introduces a strict 48-hour removal mandate for covered platforms upon receipt of a valid notice, enforced by the Federal Trade Commission (FTC).6 Unlike previous internet safety legislations that relied heavily on platform self-regulation or the good-faith protections of Section 230 of the Communications Decency Act, the TAKE IT DOWN Act imposes affirmative duties on platforms to not only remove reported content but also make "reasonable efforts" to identify and remove identical copies.8
This document serves as a detailed operational and legal guide for stakeholders, analyzing the technical standards for "digital forgeries," the interplay between federal and state jurisdiction, and the constitutional challenges anticipated as enforcement ramps up.
________________
1. Legislative Framework, History, and Intent
1.1 The Genesis of the Act: Closing the "Deepfake Loophole"
The TAKE IT DOWN Act did not emerge in a vacuum; it was the legislative response to a rapidly deteriorating digital landscape where technological capability outpaced legal accountability. Historically, federal law regarding sexual exploitation was predicated on the existence of a "real" victim depicted in the imagery. Statutes governing Child Sexual Abuse Material (CSAM) or video voyeurism generally required proof that an actual minor was filmed or that a camera was physically placed in a private area.
The proliferation of Generative Adversarial Networks (GANs) and diffusion models created a "Deepfake Loophole." Perpetrators could generate hyper-realistic, sexually explicit imagery of identifiable individuals—often women and minors—without ever capturing a real photograph. The incident involving high school students in Aledo, Texas, served as a primary catalyst for this legislation.1 In that case, seemingly innocent social media photos of minors were harvested and processed through AI "undressing" software to create realistic nude depictions. Because the resulting images were technically "fake," they fell outside the scope of traditional CSAM or revenge porn laws in many jurisdictions, leaving victims without recourse and law enforcement without a predicate offense.1
Sponsored by Senator Ted Cruz (R-TX) and Senator Amy Klobuchar (D-MN), the bill achieved rare bipartisan consensus, passing the Senate unanimously and the House by a vote of 409-2.8 This legislative history is crucial for legal interpretation; the overwhelming support signals a clear Congressional intent to prioritize victim privacy over the absolute immunity often claimed by platforms under Section 230.
1.2 Statutory Objectives
The legislative intent is strictly bifurcated into deterrence and remediation:
1. Deterrence (Criminal): To create a federal floor for criminal liability that is technology-neutral, ensuring that "digital forgeries" carry the same penal weight as authentic NCII. This standardizes the risk for perpetrators who previously jurisdiction-shopped for states with lax cyber-harassment laws.12
2. Remediation (Civil/Administrative): To force online platforms—historically criticized for slow or non-existent response times to user reports—to act with urgency. The Act shifts the paradigm from "moderation at will" to "moderation as obligation" regarding NCII, backed by the enforcement power of the Federal Trade Commission (FTC).13
________________
2. Comprehensive Statutory Definitions and Scope
The Act amends Section 223 of the Communications Act of 1934 (47 U.S.C. § 223), embedding its provisions deep within the foundational architecture of telecommunications law.3 A nuanced understanding of its definitions is prerequisite for compliance.
2.1 The Two Categories of Prohibited Content
The Act regulates two distinct but legally equivalent categories of content. Understanding the distinction is vital for content moderation teams and legal counsel.
2.1.1 Authentic Intimate Visual Depiction
This category covers traditional "revenge porn" or "nonconsensual pornography." It includes images or videos of identifiable individuals engaging in sexually explicit conduct or displaying intimate body parts (genitals, pubic areas, anus, or female nipple).14
* The Privacy Threshold: For the content to be illicit, it must have been obtained or created under circumstances where the individual had a reasonable expectation of privacy.
* Exclusions: Content voluntarily exposed by the subject in a public or commercial setting (e.g., commercial pornography, public nudity) is excluded. This distinction protects the legitimate adult industry and free expression regarding public acts.9
2.1.2 Digital Forgery (The AI Standard)
The definition of "digital forgery" is the Act's most innovative contribution. It is defined as any intimate visual depiction created through software, machine learning, artificial intelligence, or other technological means.15
* The "Indistinguishable" Test: The crucial legal standard is that the depiction, "when viewed as a whole by a reasonable person, is indistinguishable from an authentic visual depiction of the individual".2
* Implications for Moderators: This standard effectively carves out obvious cartoons, anime, or low-fidelity "photoshops" that a reasonable person would not mistake for reality. However, it captures the high-fidelity outputs of modern AI, such as "deepfake" videos or "nudified" static images. Platforms must now train moderators (and algorithms) to assess "realism" rather than just "explicitness."
2.2 "Covered Platforms": Inclusions and Exclusions
The Act casts a wide net, defining a "covered platform" as any public website, online service, or mobile application that primarily provides a forum for user-generated content.6
2.2.1 Inclusions
* Social Media: Facebook, X (formerly Twitter), Instagram, TikTok.
* Image Boards & Forums: Reddit, 4chan, Discord (public servers).
* Content Hosting: Imgur, specialized video hosting sites.
* Search Engines (Partial): While search engines index content, if they host cached versions or allow user uploads, they may fall under the definition depending on their primary function.
2.2.2 Exclusions and Carve-Outs
The Act includes specific carve-outs to prevent breaking the underlying infrastructure of the internet 9:
* Broadband Internet Access Providers (ISPs): Verizon, Comcast, etc., acting as mere conduits.
* Email Services: Gmail, Outlook. This exclusion is critical to protect the privacy of private correspondence.
* Incidental Interactivity: Websites where user content is incidental to pre-selected content (e.g., the comment section of a curated news site like The New York Times) are likely excluded, provided the primary purpose is not user-generated forums.
2.3 The Definition of Consent
Consent is defined rigorously to prevent defenses based on coercion or prior relationships. It must be an "affirmative, conscious, and voluntary authorization made by an individual free from force, fraud, duress, misrepresentation, or coercion".15
* The Revocability Doctrine: The Act clarifies that consent to capture an image does not equate to consent to distribute it. Furthermore, consent to share privately (e.g., sending a photo to a partner) does not constitute consent for public publication. This codifies the "contextual privacy" theory—that privacy is not binary (public vs. private) but contextual.9
________________
3. The Civil Mandate: Notice, Takedown, and the 48-Hour Rule
The core operational burden of the TAKE IT DOWN Act falls on the Civil Notice-and-Takedown provisions, which become enforceable on May 19, 2026.3 This section outlines the mandatory procedures platforms must engineer.
3.1 The Notice-and-Takedown Process
Platforms are statutorily required to establish a "clear and accessible process" for victims to submit takedown requests.9 This cannot be a generic "Contact Us" form; it must be a specialized workflow designed for NCII.
3.1.1 Elements of a Valid Notice
For a notice to be legally binding and trigger the 48-hour clock, it must contain specific evidentiary elements 9:
1. Identification: Information reasonably sufficient to locate the content (e.g., specific URLs, post IDs).
2. Good Faith Statement: A sworn or affirmed brief statement that the individual has a good faith belief the depiction is nonconsensual.
3. Identity Verification: An electronic signature of the depicted individual (or their authorized representative).
4. Contact Information: Sufficient details for the platform to contact the complainant for follow-up.
Operational Insight: This structure mirrors the Digital Millennium Copyright Act (DMCA) notice but with higher stakes regarding personal dignity. Unlike the DMCA, which often allows for automated notices from bots, the requirement for a victim's signature and good faith statement suggests a more manual, high-touch intake process.
3.2 The 48-Hour Removal Mandate
Upon receipt of a valid notice, the platform must remove or disable access to the content "as soon as possible" but no later than 48 hours after receipt.3
3.2.1 Operational Implications of "48 Hours"
* Continuous Clock: The statute specifies "48 hours," not "two business days".17 This implies a continuous clock that runs through weekends and federal holidays.
* Staffing Requirements: Platforms must maintain moderation coverage 24/7/365. For smaller platforms or startups, this eliminates the possibility of "Monday morning" moderation queues.
* Verification Latency: The 48-hour window includes the time required to verify the notice. If a platform takes 36 hours to verify the identity of the requester, they have only 12 hours remaining to technically remove the content and scan for duplicates.19
3.3 The "Reasonable Efforts" Standard for Duplicates
Perhaps the most technically demanding requirement is the obligation to "make reasonable efforts to identify and remove any known identical copies" of the depiction.3 This moves the burden from the victim (who previously had to play "whack-a-mole" with every individual URL) to the platform.
3.3.1 Technical Interpretation: Hashing vs. AI Analysis
"Reasonable efforts" in the context of 2026 technology effectively mandates the use of perceptual hashing (e.g., PhotoDNA, PDQ hashing).
* The Workflow: When a verified image is taken down, the platform must generate a cryptographic or perceptual hash of the file.
* Retrospective Scanning: The platform must scan its public repositories for matches to this hash to remove existing copies.
* Prevention (Implied): While the Act does not explicitly mandate proactive filtering of all uploads before they are posted (upload filters), "reasonable efforts" implies preventing the re-upload of the same hash once it is known to be illicit.20
The "Identical" Constraint: The Act specifies "identical copies." This protects platforms from the impossible burden of finding "deepfake variants"—where the same face is grafted onto a different body. Hashing technologies are adept at finding identical or near-identical (cropped, resized) copies, but they cannot reliably detect if a face has been used in a new deepfake generation without a complex facial recognition sweep, which raises separate privacy concerns.22
3.4 Liability Shield and Safe Harbor
To incentivize rapid compliance and prevent "moderation paralysis," the Act includes a "Good Samaritan" safe harbor. Platforms are not liable for any claim (e.g., wrongful removal, breach of contract, defamation) based on the good-faith removal of material claimed to be NCII, even if the material is later found to be lawful or consensual.3
* Strategic Impact: This provision is critical. It signals to platforms that they should err on the side of removal. If a user sues because their consensual image was removed by mistake, the platform can cite this safe harbor. This aligns the platform's incentives with the victim's interests rather than the uploader's.
3.5 Transparency Obligations
Platforms must provide "clear and conspicuous" notice of these procedures.3 This requirement aims to demystify the reporting process, which has historically been buried in obscure "Help Center" articles. The notice must be in plain language, explaining the mechanism for reporting and the platform’s obligations.
________________
4. Criminal Provisions and Department of Justice (DOJ) Enforcement
While the civil provisions govern platforms, the criminal provisions target the perpetrators. The TAKE IT DOWN Act significantly expands Title 18 and Title 47 of the U.S. Code to address the modern reality of digital abuse.
4.1 Prohibited Conduct and Mens Rea
It is unlawful for any person to use an interactive computer service to knowingly publish an intimate visual depiction (authentic or digital forgery) if:
* Adult Victims: The intent is to cause harm, or the publication effectively causes harm, and the content was obtained under circumstances of privacy.9
* Minor Victims: The intent is to abuse, humiliate, harass, degrade, or to arouse/gratify sexual desire of any person.6
Analysis of Mens Rea: The requirement for "knowing" publication protects individuals who might unknowingly share a deepfake they believed was real news or public domain content. However, legal precedence suggests that "willful blindness"—ignoring obvious signs that content is nonconsensual—may satisfy this standard.3
4.2 Criminal Penalties
The penalties are structured to be severe enough to act as a deterrent, with enhanced sentencing for crimes involving minors.


Offense Category
	Maximum Imprisonment
	Additional Penalties
	Legal Basis
	NCII / Deepfake (Adult Victim)
	Up to 2 Years
	Fines, Restitution, Forfeiture
	9
	NCII / Deepfake (Minor Victim)
	Up to 3 Years
	Fines, Restitution, Forfeiture
	9
	Threat to Publish (Adult)
	Up to 18 Months
	Fines
	9
	Threat to Publish (Minor)
	Up to 30 Months
	Fines
	9
	4.3 DOJ Enforcement Priorities and Restitution
The Department of Justice has signaled that enforcement will prioritize "high-impact" cases that set precedents or involve systemic abuse.25
* Sextortion Rings: The Act is a critical tool against organized sextortion rings. Previously, prosecutors often had to rely on wire fraud or generic stalking statutes, which fit poorly. The TAKE IT DOWN Act provides a direct predicate offense for threatening to release AI-generated images to extort money or compliance.10
* Restitution: Courts are empowered to order restitution to victims. This is expansive and can cover the costs of reputation management services, legal fees to scrub content from the web, and psychological counseling.24
________________
5. Civil Enforcement: The FTC and Platform Liability
The Federal Trade Commission (FTC) serves as the regulatory watchdog for the Act's civil provisions. This choice of agency is significant; the FTC regulates "unfair and deceptive practices," framing the failure to remove NCII not just as a safety failure, but as a consumer protection violation.
5.1 FTC Authority and UDAP Violations
Failure to comply with the notice-and-removal obligations—either by failing to provide the mechanism, failing to meet the 48-hour deadline, or failing to look for duplicates—is treated as a violation of a rule defining an unfair or deceptive act or practice (UDAP) under Section 18(a)(1)(B) of the FTC Act.2
* Civil Penalties: The FTC can levy substantial civil penalties. As of the 2025/2026 inflation adjustments, the maximum civil penalty is approximately $53,088 per violation.26 If a platform systematically ignores 1,000 notices, the theoretical liability could exceed $53 million.
* Injunctive Relief: Beyond fines, the FTC can seek injunctive relief (consent decrees). These decrees often mandate 20-year compliance monitoring, third-party audits, and forced restructuring of trust and safety teams.23
5.2 Interaction with Section 230
The TAKE IT DOWN Act navigates the complex waters of Section 230 of the Communications Decency Act (47 U.S.C. § 230), the law that generally immunizes platforms from liability for user-generated content.
5.2.1 The "Repeal" Debate
* Civil Enforcement Exception: Section 230 does not immunize platforms against federal government enforcement. The TAKE IT DOWN Act explicitly authorizes the FTC to enforce its provisions, effectively overriding Section 230 immunity for this specific regulatory context.8
* Private Lawsuits: Crucially, the Act does not create a general exception to Section 230 for private civil lawsuits. A victim cannot sue Facebook in federal court for damages under the TAKE IT DOWN Act if the platform fails to remove the content (unless a separate exception applies). They must rely on the FTC to bring an enforcement action.13 This "lack of a private right of action" is a major point of contention for victim advocates, who argue that FTC resources are limited.27
* Criminal Exception: Section 230 has always had an exception for federal criminal law. Therefore, platforms have no immunity if they are found to be criminally complicit in the distribution of NCII, though this requires a high bar of intent.3
________________
6. AI Applications and the "Digital Forgery" Standard
The TAKE IT DOWN Act is widely cited as the first major federal legislation to specifically regulate harmful AI-generated content, setting the template for future AI regulation.8
6.1 Regulating "Digital Forgeries"
The inclusion of "digital forgeries" addresses the "Deepfake Loophole." Previously, a perpetrator could argue that an AI-generated nude was not a "depiction of the victim" because the victim's body was not actually photographed. The Act closes this by focusing on the likeness and the reasonable person's perception.15
6.2 Technical Challenges in Identification
* Detection vs. Hashing: While the Act requires removing "identical copies," it is silent on the proactive detection of new deepfakes. Platforms are not explicitly required to use AI classifiers to detect deepfakes upon upload (which yields high false positives). However, once a deepfake is reported and confirmed, the platform must handle it as NCII.
* Watermarking: The Act does not mandate watermarking (provenance) for AI tools, though separate legislative proposals (e.g., the DEFIANCE Act) have explored this.13 The focus here is on removal of harmful output, not the architecture of the generation tools themselves.
6.3 Implications for Generative AI Platforms
While the Act targets "covered platforms" that host user content, it indirectly impacts Generative AI providers (like Midjourney, OpenAI, or open-source model hosts). If these tools host galleries of user creations, they are "covered platforms." If a user generates a deepfake and posts it to the tool's community showcase, the tool provider is subject to the 48-hour takedown rule just like a social network.28
________________
7. Comparative Analysis: Federal vs. State Laws
The TAKE IT DOWN Act sets a "federal floor" but does not preempt stricter state laws. This creates a complex patchwork for compliance, where platforms must navigate overlapping jurisdictions.
7.1 Preemption Analysis
The Act does not contain a preemption clause.13 This means state laws that provide greater protections or different remedies remain in effect. Victims can pursue remedies under both federal law (via DOJ/FTC reporting) and state law (civil lawsuits).
7.2 Detailed Comparison: Federal vs. Key State Statutes
The following table contrasts the Federal Act with key state legislations in California, New York, Texas, and Illinois, highlighting the disparate compliance obligations.


Feature
	Federal TAKE IT DOWN Act
	California (SB 981 / Civil Code)
	New York (Civ. Rights § 52-b)
	Texas (Penal Code / NCII Laws)
	Takedown Deadline
	48 Hours 6
	30 days (investigation period) 29
	Varies / "Reasonable time"
	Immediate / Criminalized
	Private Right of Action
	No (FTC Enforcement only) 13
	Yes (Civil damages available) 14
	Yes (Explicit for digital forgeries) 13
	Yes (Civil damages)
	Digital Forgeries
	Explicitly Included 15
	Explicitly Included 31
	Explicitly Included 30
	Included in penal codes
	Identical Copies
	"Reasonable efforts" to remove 8
	Removal of specific reported instance 29
	Varies
	Varies
	Scope of Victim
	Minors & Adults
	Minors & Adults
	Adults (Minors under penal law)
	Minors & Adults
	Enforcement Mechanism
	FTC (Administrative) & DOJ (Criminal)
	Private Lawsuit & State AG
	Private Lawsuit & State AG
	Criminal Prosecution & Civil Suit
	Strategic Insight: The Federal 48-hour requirement is significantly stricter than California's 30-day allowance. Platforms operating nationally effectively must adopt the federal 48-hour standard to avoid FTC liability, rendering the slower state timelines moot for compliance purposes. However, the liability risk is arguably higher in states like NY and CA because victims can sue directly for damages (potentially millions in class actions), whereas under the federal act, they rely on the FTC to intervene, which is a political and bureaucratic process.
________________
8. Constitutional and Legal Challenges
As with any legislation regulating speech, the TAKE IT DOWN Act faces intense scrutiny under the First Amendment. The tension lies between the state's compelling interest in preventing sexual exploitation and the constitutional protection of free expression.
8.1 First Amendment Overbreadth
Critics, including the Electronic Frontier Foundation (EFF) and the Cato Institute, argue the Act is overbroad.13
* The Argument: The 48-hour deadline forces platforms to remove content without sufficient time to adjudicate complex context (e.g., is an image a "deepfake" or "parody"? Is it "harmful" or "newsworthy"?). To avoid FTC fines, platforms may default to "depublishing" protected speech—a "heckler's veto" where a mere complaint silences speech.19
* Strict Scrutiny: Because the law is a content-based restriction (regulating speech based on its sexual/intimate nature), it must satisfy strict scrutiny. The government must prove the law is narrowly tailored to serve a compelling state interest. While preventing sexual exploitation is a compelling interest, the "narrow tailoring" of the 48-hour rule will be the battleground in court.32
8.2 Due Process for Uploaders
The Act does not explicitly mandate a "counter-notice" process for the uploader (the person who posted the image) to defend the content before removal, unlike the DMCA. This lack of procedural due process for the speaker is a potential constitutional vulnerability. If a politician's head is superimposed on a nude body as "satire," and it is removed within 48 hours without a chance to appeal, the Act could be challenged as a prior restraint on political speech.27
8.3 Encryption and Privacy Concerns
Technical and privacy advocates express concern that the "reasonable efforts" to identify copies could be interpreted to require scanning of private, encrypted messaging (e.g., WhatsApp, Signal).
* The "Client-Side Scanning" Fear: If "reasonable efforts" implies finding all copies, does that mean Apple must scan iCloud photos? The Act targets "public websites" and "forums," which should exclude private encrypted communications. However, if the FTC interprets "covered platform" broadly to include cloud storage that facilitates sharing, it could trigger a massive legal battle over encryption backdoors.8
________________
9. Compliance Timeline and Implementation Strategy
As the May 19, 2026 enforcement deadline approaches, organizations must transition from planning to operational readiness.
9.1 Key Dates
Milestone
	Date
	Status
	Enactment
	May 19, 2025
	Completed (Criminal provisions effective)
	FTC Rulemaking/Guidance
	2025-2026
	Ongoing (Procedural guidance)
	Civil Compliance Deadline
	May 19, 2026
	Upcoming (Mandatory Takedown Processes)
	9.2 Compliance Checklist for Platforms
Platforms providing user-generated content services must implement the following by the deadline 20:
1. Update Terms of Service (ToS):
   * Explicitly prohibit NCII and "digital forgeries" (deepfakes).
   * Define "consent" in alignment with the federal statute.
   * Disclose the platform's policy on immediate termination for repeat offenders.
2. Deploy Reporting Mechanisms:
   * Create a dedicated "Report NCII" flow distinct from general abuse reporting.
   * Ensure the tool collects necessary legal attestations (good faith belief, signature).
   * Accessibility: The reporting tool should be accessible to non-users (victims who do not have an account on the platform).26
3. Engineering the 48-Hour Workflow:
   * Triage: Automated prioritizing of NCII reports over other content moderation queues (e.g., spam).
   * Staffing: Ensure 24/7 or sufficient coverage to meet the 48-hour statutory limit.
   * Hashing Integration: Integrate hash-matching databases (e.g., participating in cross-industry shared databases like StopNCII.org) to identify identical copies.
4. Transparency Reporting:
   * While not explicitly detailed in every snippet as a statutory mandate, best practices and FTC expectations for "unfair/deceptive" practices suggest keeping detailed logs of notices received, time-to-removal, and number of duplicates removed.20
________________
10. Conclusion and Strategic Outlook
The TAKE IT DOWN Act marks the end of the laissez-faire era for online intimate content. For platforms, the shift is from reactive moderation (shielded by Section 230) to statutory obligation (monitored by the FTC).
10.1 Strategic Recommendations for Platforms
1. Invest in Hash-Matching: Manual review will not scale to meet the 48-hour deadline for "identical copies." Licensing hash databases of known NCII is now a compliance necessity.
2. Audit Reporting Flows: Ensure the "Report" button for NCII is not buried. A "clear and conspicuous" process is a statutory requirement.
3. Prepare for State Litigation: While complying with the federal 48-hour rule protects against the FTC, platforms must still navigate state-level private right of action lawsuits. Compliance with the stricter federal standard acts as a strong defense in state courts regarding "reasonableness" of conduct.
10.2 Final Outlook
By May 19, 2026, the US digital landscape will operate under a new presumption: that intimate privacy is a right actively protected by platform architecture, not just a policy preference. While constitutional challenges regarding free speech are inevitable, the bipartisan support and the specific focus on "nonconsensual" and "harmful" content suggest the core of the Act will endure, permanently raising the bar for digital safety. The convergence of criminal liability for creators and administrative liability for platforms creates a pincer movement designed to eradicate the "Deepfake Loophole" once and for all.
Источники
1. TAKE IT DOWN Act - Wikipedia, дата последнего обращения: февраля 17, 2026, https://en.wikipedia.org/wiki/TAKE_IT_DOWN_Act
2. Text - S.146 - 119th Congress (2025-2026): TAKE IT DOWN Act, дата последнего обращения: февраля 17, 2026, https://www.congress.gov/bill/119th-congress/senate-bill/146/text
3. The TAKE IT DOWN Act: A Federal Law Prohibiting the Nonconsensual Publication of Intimate Images | Congress.gov, дата последнего обращения: февраля 17, 2026, https://www.congress.gov/crs-product/LSB11314
4. U.S. Artificial Intelligence Law Update: Navigating the Evolving State ..., дата последнего обращения: февраля 17, 2026, https://www.bakerbotts.com/thought-leadership/publications/2026/january/us-ai-law-update
5. Take It Down Act: How to use it to remove revenge porn - The 19th News, дата последнего обращения: февраля 17, 2026, https://19thnews.org/2025/05/take-it-down-act-signing-explicit-images/
6. S.4569 - TAKE IT DOWN Act 118th Congress (2023-2024), дата последнего обращения: февраля 17, 2026, https://www.congress.gov/bill/118th-congress/senate-bill/4569
7. President Trump Signs Take It Down Act Into Law - Latham & Watkins LLP, дата последнего обращения: февраля 17, 2026, https://www.lw.com/en/insights/president-trump-signs-take-it-down-act-into-law
8. Take it Down Act Signed into Law, Offering Tools to Fight Non-Consensual Intimate Images and Creating a New Image Takedown Mechanism - Proskauer, дата последнего обращения: февраля 17, 2026, https://www.proskauer.com/blog/take-it-down-act-signed-into-law-offering-tools-to-fight-non-consensual-intimate-images-and-creating-a-new-image-takedown-mechanism
9. 'Take It Down Act' Requires Online Platforms To Remove ..., дата последнего обращения: февраля 17, 2026, https://www.skadden.com/insights/publications/2025/06/take-it-down-act
10. What They're Saying | The TAKE IT DOWN Act - Senate Commerce Committee, дата последнего обращения: февраля 17, 2026, https://www.commerce.senate.gov/services/files/3EED5B40-FE58-4799-A191-F477C147A7C0
11. House approves Take It Down Act, sending bill on intimate images to Trump's desk, дата последнего обращения: февраля 17, 2026, https://19thnews.org/2025/04/take-it-down-act-house-passes/
12. Take It Down Act - RAINN, дата последнего обращения: февраля 17, 2026, https://rainn.org/federal-legislation/take-it-down-act/
13. Congress's Attempt to Criminalize Nonconsensual Intimate Imagery: The Benefits and Potential Shortcomings of the TAKE IT DOWN Act - National Association of Attorneys General, дата последнего обращения: февраля 17, 2026, https://www.naag.org/attorney-general-journal/congresss-attempt-to-criminalize-nonconsensual-intimate-imagery-the-benefits-and-potential-shortcomings-of-the-take-it-down-act/
14. 2025 California Code Civil Code - CIV DIVISION 3 - OBLIGATIONS PART 3 - OBLIGATIONS IMPOSED BY LAW Section 1708.85. - Justia, дата последнего обращения: февраля 17, 2026, https://law.justia.com/codes/california/code-civ/division-3/part-3/section-1708-85/
15. Text - S.4569 - 118th Congress (2023-2024): TAKE IT DOWN Act ..., дата последнего обращения: февраля 17, 2026, https://www.congress.gov/bill/118th-congress/senate-bill/4569/text
16. New Federal AI Deepfake Law Takes Effect: 4 Steps Schools Must Take Under the “Take It Down” Act | Fisher Phillips - JDSupra, дата последнего обращения: февраля 17, 2026, https://www.jdsupra.com/legalnews/new-federal-ai-deepfake-law-takes-2360005/
17. Navigating the TAKE IT DOWN Act in Litigation - Dynamis LLP, дата последнего обращения: февраля 17, 2026, https://www.dynamisllp.com/knowledge/navigating-take-it-down-act-in-litigation
18. Text - H.R.633 - 119th Congress (2025-2026): TAKE IT DOWN Act, дата последнего обращения: февраля 17, 2026, https://www.congress.gov/bill/119th-congress/house-bill/633/text
19. Congress Passes TAKE IT DOWN Act Despite Major Flaws | Electronic Frontier Foundation, дата последнего обращения: февраля 17, 2026, https://www.eff.org/deeplinks/2025/04/congress-passes-take-it-down-act-despite-major-flaws
20. TAKE IT DOWN Act Becomes Law, Introducing Landmark Federal ..., дата последнего обращения: февраля 17, 2026, https://www.orrick.com/en/Insights/2025/05/TAKE-IT-DOWN-Act-Becomes-Law
21. TAKE IT DOWN Act Becomes Law, Introducing Landmark Federal Protections to Combat Online Exploitation and Deepfakes | Orrick, Herrington & Sutcliffe LLP - JDSupra, дата последнего обращения: февраля 17, 2026, https://www.jdsupra.com/legalnews/take-it-down-act-becomes-law-8498490/
22. Take It Down Act: U.S. enacts law targeting sexually explicit deepfakes and “revenge porn”, дата последнего обращения: февраля 17, 2026, https://www.hoganlovells.com/en/publications/take-it-down-act-us-enacts-law-targeting-sexually-explicit-deepfakes-and-revenge-porn
23. TAKE IT DOWN Act Targets Deepfakes: Are Online Platforms Caught in the Crosshairs?, дата последнего обращения: февраля 17, 2026, https://www.morganlewis.com/pubs/2025/06/take-it-down-act-targets-deepfakes-are-online-platforms-caught-in-the-crosshairs
24. U.S. Enacts Take It Down Act - Hunton Andrews Kurth LLP, дата последнего обращения: февраля 17, 2026, https://www.hunton.com/privacy-and-cybersecurity-law-blog/u-s-enacts-take-it-down-act
25. U.S. Department of Justice Criminal Division May 12, 2025 MEMORANDUM TO, дата последнего обращения: февраля 17, 2026, https://www.justice.gov/criminal/media/1400046/dl?inline
26. Another Take on the TAKE IT DOWN Act | Perkins Coie, дата последнего обращения: февраля 17, 2026, https://perkinscoie.com/insights/blog/another-take-take-it-down-act
27. The TAKE IT DOWN Act: A Flawed Attempt to Protect Victims That Will Lead to Censorship, дата последнего обращения: февраля 17, 2026, https://www.eff.org/deeplinks/2025/02/take-it-down-act-flawed-attempt-protect-victims-will-lead-censorship
28. The Policy Implications of Grok's 'Mass Digital Undressing Spree' | TechPolicy.Press, дата последнего обращения: февраля 17, 2026, https://www.techpolicy.press/the-policy-implications-of-groks-mass-digital-undressing-spree/
29. Congress Passes Take It Down Act, Imposing New Burdens on ..., дата последнего обращения: февраля 17, 2026, https://www.willkie.com/publications/2025/05/congress-passes-take-it-down-act
30. Is This Video Real? The Principal Mischief of Deepfakes and How the Lanham Act Can Address It - Columbia Journal of Law & Social Problems, дата последнего обращения: февраля 17, 2026, https://jlsp.law.columbia.edu/wp-content/blogs.dir/213/files/2022/01/Vol55-Ullrich.pdf
31. SB 646 (Cortese) - Senate Judiciary Committee, дата последнего обращения: февраля 17, 2026, https://sjud.senate.ca.gov/sites/sjud.senate.ca.gov/files/sb_646.pdf
32. Take It Down or Take It Too Far? The Legal Fallout of New Online Takedown Powers - Carolina Law Scholarship Repository, дата последнего обращения: февраля 17, 2026, https://scholarship.law.unc.edu/cgi/viewcontent.cgi?article=1521&context=ncjolt