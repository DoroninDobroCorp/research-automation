The Transparency Mandate: A Comprehensive Analysis of EU AI Act Obligations for Deepfakes and Synthetic Media
Executive Summary
As of February 2026, the European Union finds itself in the decisive "last mile" of implementing the world’s first comprehensive legal framework for artificial intelligence. The EU AI Act (Regulation (EU) 2024/1689), having entered into force in August 2024, has moved beyond theoretical debate into the granular reality of compliance. While the initial prohibitions on "unacceptable risk" systems took effect in early 2025, the attention of the global technology and media sectors is now fixed on August 2, 2026. This date marks the full application of Article 50 (formerly Article 52 in legislative drafts), which establishes a rigorous transparency regime for AI-generated content and deepfakes.1
This report provides an exhaustive analysis of the transparency obligations that will govern the European digital single market. It dissects the shift from the draft text to the final regulation, clarifying the critical re-numbering that has caused confusion in compliance circles. It explores the operational realities of the "Code of Practice" currently being finalized by the AI Office, specifically addressing the technical standards for machine-readable watermarking and the design of the "Common Icon".3
Furthermore, this analysis delves into the sensitive and complex intersection of the AI Act with the Digital Services Act (DSA) regarding adult content and non-consensual deepfakes—a domain where algorithmic transparency meets fundamental rights. Finally, it details the fragmented landscape of national implementation, profiling how major Member States like Italy, Spain, France, and Germany are diverging in their enforcement strategies, with some introducing criminal penalties that go far beyond the administrative fines of the Brussels regulation.5
With potential penalties reaching up to €15 million or 3% of global turnover for transparency violations, and the reputational risk of "naming and shaming" by new market surveillance authorities, the stakes for providers and deployers of generative AI are unprecedented.7 This document serves as a strategic roadmap for navigating this new regulatory epoch.
________________
Part I: The Regulatory Architecture of Trust
To understand the specific mandates for deepfakes, one must first situate Article 50 within the broader architectural philosophy of the AI Act. The Regulation is not merely a safety rulebook; it is a market-making instrument designed to foster "Trustworthy AI." The legislator’s premise is that without transparency, the information ecosystem—and by extension, democratic discourse—cannot survive the flood of synthetic reality.
1.1 The Evolution from Draft Article 52 to Final Article 50
A persistent source of confusion in early 2026 compliance literature is the reference to "Article 52." During the extensive trilogue negotiations between the European Parliament, the Council, and the Commission (2021–2024), the transparency obligations were indeed housed in Article 52. However, in the final text published in the Official Journal on July 12, 2024, these obligations were re-codified as Article 50.8
Clarification of the Shift:
* Article 50 (Final Text): "Transparency Obligations for Providers and Deployers of Certain AI Systems." This is the binding provision for deepfakes, chatbots, and emotional recognition systems.
* Article 52 (Final Text): Now pertains to "General-Purpose AI Models," specifically the procedural rules for notifying the Commission about systemic risks.10
For the purposes of this report, all references to the binding transparency obligations will use the correct final citation: Article 50. Legal counsel reviewing contracts or compliance policies drafted prior to mid-2024 must update their internal references to reflect this shift, as Article 52 now governs a completely different set of obligations related to GPAI model classification.
1.2 The Risk-Based Pyramid and "Limited Risk"
The AI Act classifies systems into four risk categories: Unacceptable (Prohibited), High Risk, Limited Risk, and Minimal Risk. Deepfakes and most generative AI systems fall into the Limited Risk category.11
The regulatory logic here is distinct from High-Risk systems (like AI in medical devices or hiring), which require conformity assessments and fundamental rights impact assessments. For Limited Risk systems, the regulator’s primary concern is deception. The harm is not necessarily physical injury or discrimination, but the erosion of truth and the manipulation of the user’s perception of reality. Therefore, the primary remedy is transparency—ensuring the user knows they are interacting with a machine or viewing synthetic content.8
1.3 The "Code of Practice" as the Operational Engine
While Article 50 sets the legal requirement, it does not specify the pixel-level technical details. Instead, the Act empowers the newly established AI Office to facilitate a "Code of Practice." As of February 2026, this Code is in its critical drafting phase, with a final version expected by June 2026.4
The Code is formally voluntary, but practically mandatory. It establishes a "presumption of conformity." Providers who adhere to the Code are deemed compliant. Those who choose alternative technical solutions bear the burden of proving that their methods are at least as effective as the Code—a high technical and legal bar that effectively forces industry standardization.12
________________
Part II: Deep Dive into Article 50 Transparency Obligations
Article 50 constitutes a dual regime, splitting responsibilities between the Provider (the developer of the AI model, e.g., OpenAI, Google, Midjourney) and the Deployer (the user who employs the system to create and publish content, e.g., a media company, an influencer, or a marketing agency).
2.1 Obligations for Providers: The "Watermarking" Mandate
Paragraph 2 of Article 50 places a direct, inescapable obligation on the creators of generative AI systems.
The Core Mandate: Providers must ensure that AI systems generating synthetic audio, image, video, or text content are designed to mark outputs in a machine-readable format and ensure they are detectable as artificially generated or manipulated.8
This is a "Privacy by Design" (or rather, "Transparency by Design") requirement. It prevents the release of "naked" generative models that produce untraceable content.
2.1.1 Machine-Readability and Detectability
The text specifies that the marking must be machine-readable. This goes beyond a visible watermark (like a logo in the corner). It requires metadata injection or steganographic encoding that automated systems (crawlers, content moderation bots, browser plugins) can read.
* Technical Standard: While the Act is technology-neutral, the industry and the draft Code of Practice are coalescing around the C2PA (Coalition for Content Provenance and Authenticity) standard. This open technical standard allows publishers to embed tamper-evident provenance data into media files.13
* Implementation: The provider must integrate this capability into the API or the user interface of the tool. A user generating an image on a compliant platform should not be able to "opt-out" of the machine-readable watermark, although they might control the visible label.
2.1.2 The "State of the Art" and Technical Feasibility
The obligation is bound by the principle of technical feasibility. Providers must ensure solutions are "effective, interoperable, robust and reliable," but this is balanced against the "state of the art".8
* The Text Problem: Watermarking text (LLM output) is significantly more difficult than watermarking images. Techniques like statistical watermarking (altering token probabilities) are robust but can degrade the quality of the text or be defeated by light editing. The Regulation acknowledges this, implying that the "robustness" requirement for text might be lower than for video until the technology matures.
* Robustness Definition: The mark must survive "standard editing." If a user crops an image or compresses a video for Instagram, the machine-readable mark should ideally remain detectable. This is a massive technical challenge that the Code of Practice Working Groups are currently debating.14
2.1.3 Exceptions for Assistive Tools
Not all AI use requires labeling. The obligation does not apply if the AI system performs an "assistive function for standard editing" or does not "substantially alter the input data or the semantics thereof".8
* Examples of Exemptions: AI-powered noise reduction in microphones, color correction in photography, or spell-checkers. These tools use AI but do not generate "synthetic" content in a way that alters the reality of the input.
* Ambiguity: The line between "standard editing" and "substantial alteration" is thin. Is an AI "Magic Eraser" that removes a person from a photo standard editing, or a substantial alteration? The prevailing legal view is that if it changes the semantic meaning of the image (e.g., removing a political rival from a photo), it triggers the obligation.15
2.2 Obligations for Deployers: The "Disclosure" Mandate
While providers handle the invisible technical marking, deployers are responsible for the visible truth. Article 50(4) bifurcates this obligation into two distinct categories: Deepfakes and Public Interest Text.
2.2.1 The Deepfake Disclosure (Article 50(4), Paragraph 1)
Deployers who use AI to generate or manipulate image, audio, or video content that constitutes a "deepfake" must disclose that the content has been artificially generated or manipulated.8
Definition of a Deepfake: The Act provides a precise three-part definition 15:
1. Generated or Manipulated: The content is not raw footage.
2. Resemblance: It resembles existing persons, objects, places, or events.
3. Verisimilitude: It would "falsely appear to a person to be authentic or truthful."
The Disclosure Standard: The disclosure must be "clear and distinguishable" and provided at the "first interaction or exposure".8 This prevents "bait-and-switch" tactics where the disclosure is hidden in a footer or revealed only after the video ends.
The "Evidently Artistic" Exemption: Crucially, the regulation creates a nuanced regime for creative industries. Where the content forms part of an "evidently artistic, creative, satirical, fictional or analogous work or programme," the transparency obligations are limited but not removed.8
* Application: A sci-fi movie using AI aliens does not need a watermark on every frame. A satirical sketch show using deepfakes of politicians does not need a flashing "FAKE" warning if the satire is evident.
* Requirement: The deployer must still disclose the existence of the content in an "appropriate manner that does not hamper the display or enjoyment of the work" (e.g., in the opening credits or end roll).8
2.2.2 The Public Interest Text Disclosure (Article 50(4), Paragraph 2)
Deployers generating text published to "inform the public on matters of public interest" must disclose the AI origin. This specifically targets the news media and political communication.8
The Editorial Responsibility Exemption:
This is perhaps the most significant concession to the publishing industry. The obligation to label text does not apply if:
1. The content has undergone a process of human review or editorial control; AND
2. A natural or legal person holds editorial responsibility for the publication.3
* Strategic Implication: A newspaper using AI to summarize earnings reports does not need to tag articles as "AI-written" if a human editor checks them and the newspaper accepts liability. However, a "content farm" publishing thousands of unreviewed AI articles would be in violation if they fail to label.
* Draft Code Clarification: The Draft Code (Measure 5) warns that this human review cannot be a rubber stamp. It effectively requires a documented editorial workflow identifying the responsible persons. A mere assertion of review without evidence of a process may be challenged by authorities.3
________________
Part III: Technical Compliance and the Code of Practice
As we approach the August 2026 deadline, the "how" of compliance is being defined by the AI Office's Code of Practice. The draft released in December 2025 provides granular details that go beyond the high-level legal text.
3.1 The "Common Icon" (AI / KI / IA)
To avoid consumer confusion caused by a proliferation of proprietary symbols (e.g., Google’s sparkles vs. OpenAI’s logo), the Commission is driving towards a standardized European icon.
* The Interim Solution: The Draft Code proposes a visual label containing the acronym "AI" (or local language equivalents like "KI" in Germany, "IA" in France/Spain/Italy).3
* Design Constraints: The icon must be simple, scalable, and high-contrast. It serves as a visual "stop sign" for reality.
* Future Vision: The long-term goal is an interactive EU-wide symbol. When a user hovers over or clicks this icon, it would read the embedded C2PA metadata and display a "Provenance Card"—showing the software used, the date of creation, and whether the content was edited.17
3.2 Modality-Specific Disclosure Rules
The Draft Code acknowledges that a label suitable for an image does not work for a podcast or a VR experience. It proposes a matrix of disclosure methods 13:
Content Modality
	Disclosure Requirement (Draft Code 2026)
	Technical Specification
	Real-time Video
	Persistent Overlay
	A non-intrusive icon must remain visible throughout the stream plus a disclaimer at the start.
	Non-real-time Video
	Hybrid
	Opening disclaimer + persistent icon + end credits.
	Static Images
	Fixed Overlay
	Clearly visible icon placed in a corner (not cropped out).
	Audio-only
	Audible Disclaimer
	A spoken "watermark" or distinct sound cue at the start. For long formats, it must be repeated.
	Multimodal/VR
	Visual/Haptic
	Visible icon within the user's field of view without requiring interaction.
	3.3 The Challenge of Detection
Article 50(2) mentions that content must be "detectable." This implies that providers must not only watermark content but also provide tools to detect those watermarks.
* API Mandate: The Draft Code suggests that major providers (like Midjourney or OpenAI) must offer APIs that allow platforms (like Facebook or X) to check for these watermarks automatically.14
* The False Positive Problem: The Code acknowledges technical limitations. Detection tools are probabilistic. Therefore, the "detectability" requirement is framed as a "best effort" based on the state of the art, protecting providers from liability if a sophisticated adversary successfully scrubs the watermark.
________________
Part IV: Deepfakes, Adult Content, and the Digital Services Act
The regulation of deepfakes does not occur in a vacuum. It intersects heavily with the Digital Services Act (DSA), particularly concerning the explosive growth of AI-generated adult content and non-consensual deepfake pornography (NCDP).
4.1 The Regulatory Interplay: Transparency vs. Takedown
It is critical to distinguish the roles of the AI Act and the DSA.
* AI Act (Article 50): Regulates the tool and the label. If an adult content platform (e.g., OnlyFans) uses AI to create synthetic performers, Article 50 mandates they be labeled. It does not ban the content itself, provided it is legal.
* DSA: Regulates the platform and the dissemination. Large platforms (VLOPs) must mitigate systemic risks, including the spread of illegal content. Non-consensual deepfakes are generally considered illegal content (violation of privacy/dignity) and must be removed.13
4.2 The "Grok" Case Study (2025-2026)
In late 2025, the interaction between these laws was tested when X (formerly Twitter) launched its "Grok" AI chatbot, which users immediately exploited to generate non-consensual sexually explicit images of celebrities and private citizens.
* DSA Enforcement: The European Commission opened formal proceedings against X under the DSA. The charge was not just the existence of the content, but the failure to conduct a Systemic Risk Assessment before launching the tool.19
* The AI Act Angle: Although Article 50 was not fully applicable at the time of the incident, the Commission cited the lack of effective watermarking and safety guardrails as a failure of "safety by design." This case serves as a precedent: post-August 2026, a similar incident would trigger dual penalties—Article 50 fines for the lack of transparency/watermarking, and DSA fines for the failure to moderate the content.
4.3 The "Nudification" App Crackdown
A specific category of concern is "nudification" apps—AI services designed solely to strip clothes from images of women.
* Legislative Gap: MEPs have argued that transparency is insufficient for these apps—labeling a non-consensual deepfake does not mitigate the harm to the victim.21
* Potential Bans: While the AI Act does not explicitly ban these apps in Article 5 (Prohibited Practices), Member States are using the Directive on combating violence against women to criminalize them. Italy, for instance, has criminalized the creation of such content, effectively banning these tools within its jurisdiction.22
________________
Part V: Member State Implementation - A Patchwork in Progress
While the AI Act is a Regulation (directly applicable), enforcement is delegated to National Competent Authorities (NCAs). As of February 2026, the landscape is fragmented, with significant divergence in how Member States are preparing for the August 2026 deadline.
5.1 Italy: The Vanguard of Criminalization
Italy has taken the most aggressive stance in Europe, moving faster and harder than the harmonized framework.
* The New AI Law (Law No. 132/2025): Enacted in late 2025, this law criminalizes the misuse of AI.5
* Criminal Penalties: While the EU AI Act imposes administrative fines, Italy imposes prison sentences. Creating deepfakes to harm a person carries a sentence of 1 to 5 years.6
* Authority: The Agency for Digital Italy (AgID) and the National Cybersecurity Agency (ACN) are the designated enforcers. This dual structure emphasizes that Italy views AI as both a digital market issue and a national security issue.23
5.2 Spain: The Institutional Pioneer
Spain was the first EU country to establish a dedicated AI supervision agency, positioning itself as a regulatory hub.
* AESIA (Agencia Española de Supervisión de la Inteligencia Artificial): This agency has broad powers and has been operational since late 2025.
* Serious Offense: Spanish legislation classifies the failure to label AI content as a "serious offense," explicitly referencing the AI Act’s maximum penalties to signal a zero-tolerance approach to misinformation.24
* Scope: AESIA oversees all AI compliance except for data privacy (handled by the AEPD), financial markets, and electoral integrity, ensuring specialized oversight.25
5.3 France: The "Tandem" Coordination Model
France has faced legislative delays but has outlined a complex, decentralized governance model that reflects its robust administrative state.
* The "Tandem": Governance is split between the CNIL (Data Protection) and the DGCCRF (Consumer Protection/Fraud).26
* Jurisdiction Split:
   * CNIL: Oversees AI systems that involve personal data (e.g., biometric categorization, training data for deepfakes).
   * ARCOM: The media regulator oversees AI in broadcasting and audiovisual content.
   * DGCCRF: Acts as the Single Point of Contact and coordinator for market surveillance.
* Implication: A media company in France faces a multi-headed hydra; it must answer to ARCOM for the visible label on TV, and to the CNIL for the biometric data used to generate the synthetic anchor.
5.4 Germany: The Centralized Service Desk
Germany has opted for a centralized approach leveraging its powerful network regulator.
* Bundesnetzagentur (BNetzA): The Federal Network Agency is set to be the central market surveillance authority.28
* AI Service Desk: BNetzA has launched a "Service Desk" to guide companies, focusing on technical compliance and standards.
* Federalism Issues: Tensions remain regarding the role of the BfDI (Federal Data Protection Commissioner), who retains jurisdiction over data-driven AI, creating potential friction between the federal network regulator and data protection independent bodies.30
5.5 Other Member States
* Netherlands: The Data Protection Authority (AP) is taking a lead role, integrating AI oversight closely with privacy regulation.31
* Poland: The Data Protection Office (UODO) is actively campaigning for new legislation to specifically address deepfakes, arguing that current civil laws are insufficient for the speed of AI harm.32
* Sweden: The Post and Telecom Authority (PTS) is designated as the coordinator, with a government bill expected in Spring 2026 to formalize powers.33
________________
Part VI: Compliance Timeline (2025–2027)
The implementation of the AI Act is a phased process. We are currently in the transition period.
6.1 The Implementation Schedule
Phase
	Date
	Milestone
	Status (Feb 2026)
	Entry into Force
	Aug 1, 2024
	Regulation becomes law.
	Completed
	Prohibitions
	Feb 2, 2025
	Ban on "unacceptable risk" systems (social scoring, untargeted scraping).
	Active
	GPAI Rules
	Aug 2, 2025
	Governance for General Purpose AI; Art 53 applies.
	Active
	Transparency (Art. 50)
	Aug 2, 2026
	Deepfake labeling, watermarking, and chatbot disclosures apply.
	UPCOMING (6 Months)
	High-Risk Systems
	Aug 2, 2027
	Full obligations for Annex III systems (critical infra, employment).
	Future
	6.2 The "Crunch Time" (Feb - Aug 2026)
The period between February and August 2026 is critical.
* Draft Code Feedback: The window for feedback on the Draft Code closed in Jan 2026.
* Final Code Publication: Expected June 2026. This leaves companies only two months between the final technical spec and the enforcement date.4
* Risk: Companies waiting for the "Final" Code in June will likely miss the August deadline. The strategic advice is to build compliance based on the Draft Code now, as the core requirements (C2PA, "AI" icon) are unlikely to change fundamentally.
________________
Part VII: Penalties for Non-Compliance
The AI Act is not a "toothless tiger." The penalties are structured to be dissuasive, rivaling the GDPR in magnitude.
7.1 The Fine Structure (Article 99)
Fines are tiered based on the severity of the offense. Article 50 violations fall under Tier 3.
* Tier 1 (Prohibited Practices): Up to €35M or 7% of turnover.
* Tier 2 (High Risk Obligations): Up to €15M or 3% of turnover.
* Tier 3 (Transparency/Article 50):
   * Maximum Fine: €15,000,000 OR 3% of total worldwide annual turnover, whichever is higher.7
   * Note: For a tech giant like Google, 3% of turnover is billions. For a smaller media firm, €15M is existential.
7.2 SME and Start-up Exceptions
The Act includes a specific mercy clause for SMEs and start-ups. For these entities, the fine is capped at the lower of the two thresholds.7 This ensures that a small startup isn't bankrupted by a €15M minimum if their turnover is only €1M (in which case, the fine would be calculated based on the percentage, or a lower proportionate amount).
7.3 Calculation Factors
National authorities have discretion. They will calculate fines based on:
* Nature and Duration: Was the deepfake live for an hour or a month?
* Intent: Was the watermarking stripped intentionally or due to a bug?
* Cooperation: Did the company self-report the breach?
* Mitigation: Did the company take immediate steps to label the content once discovered?
________________
Part VIII: Strategic Outlook and Recommendations
8.1 The "Zero Trust" Information Environment
The cumulative effect of Article 50 is the creation of a "Zero Trust" media environment. Users will be trained to look for the "AI" icon. Content without the icon that looks synthetic will be viewed with suspicion, or flagged by browser plugins checking for missing C2PA signatures.
8.2 Strategic Roadmap for Compliance
For Providers (Model Builders):
1. Integrate C2PA: Do not wait for June. Implement C2PA metadata injection immediately.
2. Stress Test Detectability: Conduct internal "Red Teaming" to see if your watermarks survive social media compression.
3. API Readiness: Prepare APIs for detecting your own content, as required by the Code.14
For Deployers (Media/Corporate):
1. Audit Content Pipelines: Map every tool used by marketing and creative teams. Which ones use Generative AI?
2. Define "Standard Editing": Create a clear internal policy on what constitutes "standard editing" (exempt) vs. "substantial alteration" (labeled).
3. Document Editorial Review: To claim the Article 50(4) exemption for text, implement a formal "Human in the Loop" log. If the regulator asks, you must prove a human read the article.
4. Prepare the UX: Redesign video players and image viewers to support the overlay of the "AI" Common Icon.
For Adult Content Platforms:
1. Label Everything: The risk of non-consensual deepfake liability is too high. If synthetic performers are used, label them aggressively.
2. Verify Consent: Implement strict identity verification (ID checks) for creators uploading realistic content to distinguish between consensual deepfakes (labeled) and non-consensual (banned).
8.3 Conclusion
The EU AI Act’s Article 50 is a defining moment for the digital age. It attempts to legislate truth in an era of synthetic fiction. While the burden on industry is heavy—requiring new technical standards, new editorial workflows, and new legal oversight—the alternative is an information ecosystem collapsed by distrust. By August 2, 2026, the "AI" icon will likely become as ubiquitous as the copyright symbol, marking the boundary between the human and the machine.
Источники
1. Implementation Timeline | EU Artificial Intelligence Act, дата последнего обращения: февраля 17, 2026, https://artificialintelligenceact.eu/implementation-timeline/
2. AI Act | Shaping Europe's digital future - European Union, дата последнего обращения: февраля 17, 2026, https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
3. Taking the EU AI Act to Practice Understanding the Draft Transparency Code of Practice, дата последнего обращения: февраля 17, 2026, https://www.twobirds.com/en/insights/2026/taking-the-eu-ai-act-to-practice-understanding-the-draft-transparency-code-of-practice
4. Commission publishes first draft of Code of Practice on marking and ..., дата последнего обращения: февраля 17, 2026, https://digital-strategy.ec.europa.eu/en/news/commission-publishes-first-draft-code-practice-marking-and-labelling-ai-generated-content
5. Italy New AI Law vs EU AI Act - What you need to know - GamingTechLaw, дата последнего обращения: февраля 17, 2026, https://www.gamingtechlaw.com/2025/09/italy-new-ai-law-vs-eu-ai-act-what-you-need-to-know/
6. Italy Becomes the First EU Member to Pass Thorough Legislation on AI Use - ASIS, дата последнего обращения: февраля 17, 2026, https://www.asisonline.org/security-management-magazine/latest-news/today-in-security/2025/september/italy-ai-law/
7. Article 99: Penalties | EU Artificial Intelligence Act, дата последнего обращения: февраля 17, 2026, https://artificialintelligenceact.eu/article/99/
8. Article 50: Transparency Obligations for Providers and Deployers of Certain AI Systems | EU Artificial Intelligence Act, дата последнего обращения: февраля 17, 2026, https://artificialintelligenceact.eu/article/50/
9. Article 52: Transparency Obligations for Providers and Users of Certain AI Systems and GPAI Models | AI Act made searchable by Algolia. Chapters, articles and recitals easily readable, дата последнего обращения: февраля 17, 2026, https://aiact.algolia.com/article-52/
10. Article 52: Procedure | EU Artificial Intelligence Act, дата последнего обращения: февраля 17, 2026, https://artificialintelligenceact.eu/article/52/
11. High-level summary of the AI Act | EU Artificial Intelligence Act, дата последнего обращения: февраля 17, 2026, https://artificialintelligenceact.eu/high-level-summary/
12. European Commission Publishes Draft Code of Practice on AI Labelling and Transparency, дата последнего обращения: февраля 17, 2026, https://www.jonesday.com/en/insights/2026/01/european-commission-publishes-draft-code-of-practice-on-ai-labelling-and-transparency
13. What the EU's New AI Code of Practice Means for Labeling Deepfakes | TechPolicy.Press, дата последнего обращения: февраля 17, 2026, https://www.techpolicy.press/what-the-eus-new-ai-code-of-practice-means-for-labeling-deepfakes/
14. The EU's First Draft Code of Practice on AI Transparency - E+H ..., дата последнего обращения: февраля 17, 2026, https://www.eh.at/the-eus-first-draft-code-of-practice-on-ai-transparency/
15. What constitutes a Deep Fake? The blurry line between legitimate processing and manipulation under the EU AI Act - arXiv, дата последнего обращения: февраля 17, 2026, https://arxiv.org/html/2412.09961v2
16. EU AI Act unpacked #8: New rules on deepfakes - Freshfields Technology Quotient, дата последнего обращения: февраля 17, 2026, https://technologyquotient.freshfields.com/post/102jb19/eu-ai-act-unpacked-8-new-rules-on-deepfakes
17. AI ACT: How do companies need to label AI-generated content? | HEUKING, дата последнего обращения: февраля 17, 2026, https://www.heuking.de/en/news-events/newsletter-articles/detail/ai-act-how-do-companies-need-to-label-ai-generated-content.html
18. Deepfake Laws: Global Overview and Emerging Regulations - Ondato, дата последнего обращения: февраля 17, 2026, https://ondato.com/blog/deepfake-laws/
19. Tackling AI deepfakes and sexual exploitation on social media | 19-01-2026 | News, дата последнего обращения: февраля 17, 2026, https://www.europarl.europa.eu/news/en/agenda/plenary-news/2026-01-19/8/tackling-ai-deepfakes-and-sexual-exploitation-on-social-media
20. Deepfake Regulation Accelerates After Grok Controversy, дата последнего обращения: февраля 17, 2026, https://bisi.org.uk/reports/deepfake-regulation-accelerates-after-grok-controversy
21. MEPs press European Commission for clarity on legality of deepfake ..., дата последнего обращения: февраля 17, 2026, https://iapp.org/news/a/meps-press-european-commission-for-clarity-on-legality-of-deepfake-apps
22. Deepfakes – can the AI Act protect Europe? | International Bar Association, дата последнего обращения: февраля 17, 2026, https://www.ibanet.org/deepfakes-can-the-ai-act-protect-europe
23. Italy's AI Law: the good, the bad…and the actual substance - Hogan Lovells, дата последнего обращения: февраля 17, 2026, https://www.hoganlovells.com/en/publications/italys-ai-law-the-good-the-badand-the-actual-substance
24. China and Spain Introduce Strict AI Labelling Requirements to Combat Misinformation, дата последнего обращения: февраля 17, 2026, https://www.cepic.org/post/china-and-spain-introduce-strict-ai-labelling-requirements-to-combat-misinformation
25. AI Watch: Global regulatory tracker - Spain | White & Case LLP, дата последнего обращения: февраля 17, 2026, https://www.whitecase.com/insight-our-thinking/ai-watch-global-regulatory-tracker-spain
26. EU AI Act Implementation: France Still Without Designated National ..., дата последнего обращения: февраля 17, 2026, https://ai-regulation.com/eu-ai-act-implementation-france-still-without-designated-national-competent-authorities/
27. AI Regulatory Horizon Tracker - France - Bird & Bird, дата последнего обращения: февраля 17, 2026, https://www.twobirds.com/en/capabilities/artificial-intelligence/ai-legal-services/ai-regulatory-horizon-tracker/france
28. AI - Bundesnetzagentur, дата последнего обращения: февраля 17, 2026, https://www.bundesnetzagentur.de/EN/Areas/Digitalisation/AI/start_ki.html
29. Market surveillance and AI: Who will monitor whom in the future? - SKW Schwarz, дата последнего обращения: февраля 17, 2026, https://www.skwschwarz.de/en/news/market-surveillance-and-AI
30. German Federal Government Publishes Draft Law on Application and Enforcement of the EU Data Act - Latham & Watkins LLP, дата последнего обращения: февраля 17, 2026, https://www.lw.com/en/insights/german-federal-government-publishes-draft-law-on-application-and-enforcement-of-the-eu-data-act
31. AI Act - Digital Government, дата последнего обращения: февраля 17, 2026, https://www.nldigitalgovernment.nl/overview/artificial-intelligence-ai/ai-act/
32. Poland: UODO calls for renewed legislative action to protect against deepfakes | News, дата последнего обращения: февраля 17, 2026, https://www.dataguidance.com/news/poland-uodo-calls-renewed-legislative-action-protect
33. IAPP Global Legislative Predictions 2026, дата последнего обращения: февраля 17, 2026, https://iapp.org/resources/article/global-legislative-predictions