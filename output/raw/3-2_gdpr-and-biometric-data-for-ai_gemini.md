The Biometric Paradox: GDPR Compliance in the Age of Generative AI Face and Voice Synthesis
Executive Summary
The rapid ascendancy of generative artificial intelligence (AI) has precipitated a profound collision between technological capability and fundamental rights, nowhere more acutely than in the processing of biometric data. As of 2026, the proliferation of systems capable of hyper-realistic face generation, voice cloning, and synthetic identity creation has forced a rigorous re-examination of the European Union’s General Data Protection Regulation (GDPR). The regulatory landscape has transitioned from theoretical debate to active enforcement, characterized by high-profile sanctions against entities like Clearview AI and strict preemptive warnings from authorities such as the Italian Garante regarding non-consensual deepfakes.
This report offers an exhaustive legal and technical analysis of the GDPR requirements governing the processing of biometric data within AI ecosystems. It explores the intricate definition of biometric data under Article 4(14), the collapsing viability of "legitimate interest" as a legal basis for biometric processing, and the severe challenges posed by the "Right to Erasure" (Article 17) in the context of immutable neural networks. Furthermore, it examines the intersection of the GDPR with the newly enforceable EU AI Act, highlighting the dual burden of transparency and risk management that now rests on developers.
The analysis reveals that the distinction between "raw data" (images/audio) and "biometric templates" is pivotal yet increasingly porous under regulatory scrutiny. Authorities like the CNIL (France) and AEPD (Spain) are adopting expansive interpretations of "biometric processing," effectively treating the training of generative models on identifiable human features as a high-risk activity subject to the prohibition-by-default regime of Article 9. Consequently, the "move fast and break things" ethos is legally untenable in the EU market. Compliance now demands a "Privacy by Design" architecture that prioritizes unlinkability, utilizing advanced cryptographic techniques such as homomorphic encryption and cancelable biometrics to navigate the high-stakes intersection of innovation and privacy.
________________
Part I: The Ontology of Biometric Data in AI Systems
To construct a compliant framework for AI face generation and voice cloning, one must first dissect the legal and technical taxonomy that triggers the GDPR’s most stringent protections. The classification of data as "biometric" is not merely a technical descriptor but a legal tripwire that shifts processing activities from the permissive regime of Article 6 to the prohibitive strictures of Article 9.
1.1 The Definitional Threshold: Article 4(14) and "Specific Technical Processing"
Article 4(14) of the GDPR defines biometric data as "personal data resulting from specific technical processing relating to the physical, physiological or behavioural characteristics of a natural person, which allow or confirm the unique identification of that natural person." In the context of generative AI, this definition is undergoing a stress test by technologies that do not merely identify individuals but generate, infer, and synthesize their likenesses.
The critical legal nuance lies in the phrase "specific technical processing." The mere presence of a face in a digital photograph or a voice in an audio recording does not, in itself, constitute biometric data under Article 9. As clarified by the European Data Protection Board (EDPB) and recent enforcement actions, the data elevates to the status of "biometric" only when it is subjected to technical analysis designed to extract unique identifiers or templates.1
In the domain of AI face generation, this distinction creates a complex bifurcation of data status:
* Raw Data Processing: A training dataset containing millions of facial images scraped from the public web constitutes "personal data" (assuming individuals are identifiable) but may not constitute "biometric data" if the AI system uses these images solely to learn general aesthetic features—such as texture, lighting, or the statistical distribution of pixels—without mapping the unique geometry of specific faces for the purpose of identification.
* Biometric Template Extraction: However, modern face generation and "swapping" technologies invariably cross this threshold. To maintain identity consistency in a generated video (e.g., placing a user's face onto a target actor), the AI system must vectorize the user's face. This involves converting physical distances—between the eyes, the width of the nose, the contours of the jawline—into a numerical vector or "embedding." This vectorization process constitutes "specific technical processing." The resulting embedding is, unequivocally, biometric data because it is a unique digital representation of the individual’s physical characteristics.3
The UK Information Commissioner’s Office (ICO) and the Upper Tribunal in the Clearview AI judgment have reinforced this interpretation, ruling that vectors derived from facial images constitute special category data because they allow for the unique identification of the natural person, even if the controller claims the primary purpose is not "identification" in the traditional security sense but rather "matching" or "generation".3
1.2 Voice Cloning: The Audit of Auditory Biometrics
While facial recognition has historically dominated the biometric discourse, the rapid maturation of AI voice cloning technologies (e.g., ElevenLabs, resemblance.ai) has necessitated urgent regulatory clarification regarding auditory data. The Spanish Data Protection Agency (AEPD) and the ICO have issued guidance establishing that voice recordings are personal data, which ascend to the category of biometric data when processed to identify a speaker or verify identity.5
The technical architecture of voice cloning presents unique compliance challenges compared to facial recognition. An AI voice cloning system analyzes the spectral properties, cadence, pitch, and timbre of a "target" voice to create a synthetic model or "voice print."
* The Input-Output Dichotomy: The AEPD has introduced a critical distinction between the input data and the output data. The processing of the original voice recordings to train the model involves the extraction of unique physiological characteristics (biometric processing) and is therefore subject to Article 9. However, the synthetic voice output, if sufficiently modified to be unlinkable to the original speaker (e.g., a generic "narrator" voice derived from multiple speakers), may fall outside the definition of personal data.5
* Identifiability of Clones: Conversely, if the system is designed to produce a "deepfake" or a high-fidelity clone that listeners would identify as the original speaker, the output itself remains personal data. The "identifiability" threshold in voice is lower than often assumed; a voice is not just a biometric identifier but a social identifier, often recognizable even without algorithmic analysis.
* Inference of Special Categories: Voice data carries a high risk of "data leakage." Beyond identity, voice analysis can inadvertently reveal other special categories of data under Article 9, such as health status (e.g., respiratory conditions, Parkinson’s markers), emotional state, or even ethnic origin. The processing of voice for cloning purposes, therefore, requires a Data Protection Impact Assessment (DPIA) that accounts for these collateral inferences.6
1.3 The Categorization Hierarchy: Identification vs. Verification vs. Classification
The regulatory risk profile of biometric processing is determined not just by the nature of the data, but by the purpose of the processing. Both the GDPR (as interpreted by the EDPB) and the EU AI Act distinguish between three primary functional uses of biometric data.2
1.3.1 Remote Biometric Identification (RBI)
This category involves the identification of individuals at a distance, often without their active participation or knowledge, such as scanning CCTV footage to find a match in a watchlist. Under the AI Act, "real-time" RBI is largely prohibited for law enforcement (with narrow exceptions for terrorism or missing persons), while "post" RBI is classified as High Risk. In the context of generative AI, if a platform allows users to upload a photo of a crowd and uses facial recognition to "unblur" or "generate" high-resolution faces for specific individuals, it may inadvertently cross into the domain of RBI, triggering severe compliance obligations and potential prohibitions.2
1.3.2 Biometric Verification (1:1)
Verification involves a one-to-one comparison to confirm a claimed identity (e.g., FaceID unlocking a phone). This is generally permitted but requires strict security measures. For generative AI platforms, this is relevant for "identity proofing"—verifying that the user requesting a voice clone is indeed the owner of the voice. The AEPD and CNIL emphasize that while this use is lawful, it requires explicit consent and must not lead to the creation of a centralized biometric database unless strictly necessary.7
1.3.3 Biometric Categorization and Emotion Recognition
This involves inferring attributes (age, gender, ethnicity) or internal states (emotions, intent) from biometric data. The AI Act classifies biometric categorization systems as High Risk. Crucially, systems that categorize individuals based on sensitive or prohibited characteristics (e.g., political orientation, sexual orientation, race) are banned. For generative AI, this poses a risk for "style transfer" features. A feature that modifies a face to look "more feminine" or "happier" relies on biometric categorization. If the underlying model infers race or ethnicity to perform these transformations, it enters a zone of high regulatory scrutiny. The EDPB has stated that using facial recognition to infer emotions is "highly undesirable" and should be prohibited in many contexts.1
________________
Part II: The Legal Basis Labyrinth (Article 9 & 6)
The processing of biometric data for the purpose of uniquely identifying a natural person—a prerequisite for training effective face generation and voice cloning models—is "prohibited by default" under Article 9(1) of the GDPR. To proceed, an organization must not only identify a lawful basis under Article 6 (such as contract or legitimate interest) but also satisfy one of the specific exceptions under Article 9(2). This "dual lock" mechanism is the primary barrier for commercial AI development in Europe.
2.1 The Erosion of "Legitimate Interest" for Biometrics
Historically, data controllers have relied heavily on "legitimate interest" (Article 6(1)(f)) to justify data processing for commercial improvement, fraud detection, or service optimization. However, Article 9 does not list legitimate interest as an available exception for special category data. This creates a hard stop: AI companies cannot scrape or process biometric data simply because it is necessary for their business model or benefits their algorithm's accuracy.8
The Dutch Data Protection Authority (DPA) explicitly ruled in the Clearview AI case that legitimate interest cannot serve as a valid legal basis for biometric processing of this magnitude. The DPA clarified that the intrusion into fundamental rights posed by the creation of a biometric database outweighs almost any commercial interest the controller might claim.10 This interpretation effectively closes the door on "opt-out" models for biometric AI training; active authorization is required.
2.2 The Consent Dilemma (Article 9(2)(a))
Explicit consent is the most robust and frequently cited exception under Article 9(2)(a). It is the primary legal vehicle for user-facing features, such as a mobile app that asks a user to upload a selfie to generate an avatar. However, the standard for "explicit consent" under the GDPR is rigorous, and for foundational model training, it presents significant practical hurdles.
2.2.1 The "Freely Given" Standard and Platform Economics
For consent to be valid, it must be "freely given," "specific," "informed," and "unambiguous." In the context of AI platforms, the "freely given" requirement is often compromised by "bundling." If a platform makes the provision of its service conditional on the user consenting to the use of their biometric data for model training (e.g., "Allow us to train on your voice, or you cannot use the voice cloner"), the consent is likely invalid under Article 7(4) GDPR.8 Regulators require "granularity." Users must be able to consent to the immediate processing (generating the clone) without consenting to the secondary processing (improving the global model). The CNIL’s AI recommendations emphasize that users must have distinct choices for distinct processing operations.11
2.2.2 The Retrospective Consent Impossibility
For the training of Large Multimodal Models (LMMs) that rely on datasets scraped from the open web (containing millions of faces), obtaining explicit consent from every data subject is practically impossible. This "consent gap" leaves developers of foundational models in a precarious position, forcing them to seek alternative Article 9 exceptions, most of which are proving to be legally fragile.
2.3 The "Manifestly Made Public" Defense (Article 9(2)(e))
A common defense mounted by AI developers, including Clearview AI, is the reliance on Article 9(2)(e), which permits the processing of special category data if it relates to data which are "manifestly made public by the data subject." The argument posits that individuals who upload photos to public social media profiles have effectively waived their privacy rights regarding that data.
This interpretation has been comprehensively rejected by European regulators.
* The Clearview Rejection: The French CNIL, Italian Garante, Austrian DSB, and UK ICO have all ruled that "manifestly made public" requires an affirmative act of publication combined with a specific intent or understanding of the data's widespread availability.
* Contextual Integrity: The regulators argue that uploading a photo to a social media platform for social interaction does not constitute making that biometric data "public" for the purpose of mass surveillance, algorithmic training, or inclusion in a global facial recognition database.10 The data subject’s "reasonable expectation of privacy" limits the scope of the publication.
* Burden of Proof: The burden lies on the controller to prove that every single individual in the scraped dataset actively and intentionally made their data public. For a dataset of billions of images, this burden is insurmountable.
2.4 The Scientific Research Exemption (Article 9(2)(j))
The most dynamic and evolving area of legal debate in 2025-2026 is the applicability of the "scientific research" exemption under Article 9(2)(j). This article allows Member States to provide for exemptions for processing necessary for archiving purposes in the public interest, scientific or historical research purposes, or statistical purposes, subject to Article 89(1) safeguards.
2.4.1 Kneschke v. LAION (2024): A Partial Opening?
The Hamburg Regional Court’s decision in Kneschke v. LAION (September 2024) provided a pivotal, albeit narrow, interpretation of "scientific research" in the context of AI.13
* The Ruling: The court held that the creation of a dataset (LAION-5B) for AI training purposes could qualify as "scientific research" under the text and data mining (TDM) exceptions of copyright law. Crucially, it ruled that "research" includes the preparatory steps of data curation, even if the entity creating the dataset (LAION) is not the one performing the final model training.
* Commercial vs. Non-Commercial: The court accepted that a non-profit organization (LAION) could claim this status even if its datasets were subsequently used by commercial entities. This suggests a potential pathway for "data laundering" where non-profits curate biometric datasets under the research exemption, which are then utilized by commercial labs.
* GDPR Limitations: However, legal scholars and the EDPB caution against over-interpreting this ruling for GDPR compliance. While it aids with copyright liability, the Article 9(2)(j) exemption in the GDPR is strictly defined by Member State law. Many Member States (e.g., Italy, France) restrict this exemption to research that serves a "public interest" or is conducted by accredited academic institutions. Commercial AI training by private tech giants is unlikely to satisfy the strict "public interest" test required to bypass the ban on biometric processing.13
2.5 Summary of Legal Bases for Biometric AI
The following table summarizes the viability of different legal bases for processing biometric data in AI face/voice generation:
Processing Scenario
	Primary Legal Basis (Art 6)
	Article 9 Exception Strategy
	Regulatory Viability Assessment
	User-Initiated Features (e.g., Face Swap App)
	Contract (Art 6(1)(b)) or Consent (Art 6(1)(a))
	Explicit Consent (Art 9(2)(a))
	High. Requires granular, unbundled consent.
	Mass Web Scraping for Foundational Model
	Legitimate Interest (Art 6(1)(f)) (Weak)
	Manifestly Made Public (Art 9(2)(e))
	Very Low. Rejected by CNIL, ICO, Garante, & AP.
	Academic/Non-Profit Dataset Creation
	Public Task (Art 6(1)(e)) or Legitimate Interest
	Scientific Research (Art 9(2)(j))
	Medium. Contingent on "Research" definition (Kneschke) and local Member State law.
	Fraud Detection / Security (Voice Auth)
	Legitimate Interest
	Substantial Public Interest (Art 9(2)(g))
	Medium. Highly dependent on specific national laws (e.g., UK DPA 2018 Sch 1).
	________________
Part III: Data Subject Rights and the "Unlearning" Dilemma
The "Right to be Forgotten" (Article 17) poses an existential engineering challenge to Generative AI. Unlike a relational database where a row can be deleted, a neural network "learns" features that are distributed across billions of parameters. When a model "memorizes" a face or a voice, removing that data is akin to trying to remove a specific ingredient from a baked cake.
3.1 The Right to Erasure in Training Data vs. Models
Regulators, particularly the CNIL and ICO, have established a bifurcation in how the Right to Erasure applies to AI: erasing data from the source dataset versus erasing the influence of data from the trained model.16
* Source Data Erasure: This is the baseline compliance requirement. If a user requests erasure, the controller must remove their image or voice recording from the training repository. This prevents the data from being used in future retraining cycles.
* Model Erasure (The "Unlearning" Problem): This is the conflict zone. If a model has already been trained and has "memorized" a user's face (evidenced by the ability to generate their likeness), does Article 17 require the model itself to be modified or destroyed? The EDPB’s 2025 guidance suggests that if the personal data is "identifiable" within the model (e.g., through inversion attacks), the right to erasure extends to the model parameters.18
3.2 Machine Unlearning: Technical Standards and Legal Sufficiency
To address the tension between immutable models and erasure rights, the field of "Machine Unlearning" has emerged. The EDPB categorizes acceptable methods based on their effectiveness in removing the data's influence.18
3.2.1 Full Retraining
This is the only method guaranteed to fully satisfy Article 17. The model is deleted, the specific data point is removed from the dataset, and the model is retrained from scratch.
* Implication: For massive models (LLMs, Diffusion Models), this is economically prohibitive, costing millions in compute time for a single erasure request.
3.2.2 Exact Unlearning (SISA)
"Sharded, Isolated, Sliced, and Aggregated" (SISA) training is a technique championed by privacy researchers. It involves splitting the training data into multiple independent "shards." The model is an aggregation of sub-models trained on these shards.
* Mechanism: When an erasure request is received, only the specific sub-model (shard) containing that data point needs to be retrained.
* Viability: This reduces the retraining cost by orders of magnitude and is likely to be accepted by regulators as a "proportionate" implementation of Article 17, provided the aggregation logic effectively removes the data's influence.
3.2.3 Approximate Unlearning
This involves mathematically adjusting the model's weights to "minimize" the probability of the data appearing, without full retraining.
* Regulatory Skepticism: The CNIL and EDPB view this with caution. If the data can still be "regurgitated" via adversarial prompting (e.g., "Show me the face of User X"), the erasure is legally incomplete. However, regulators acknowledge that "absolute" erasure is technically difficult, and a "best effort" approximate unlearning that reduces risk below a certain threshold may be accepted if combined with output filters.18
3.3 The "Disproportionate Effort" Defense
AI companies frequently attempt to rely on Article 14(5)(b) or general proportionality principles to argue that retraining a model for a single erasure request constitutes "disproportionate effort."
Regulatory Rebuttal:
* Design Responsibility: The CNIL has stated that "design choices" (e.g., choosing a monolithic architecture over a sharded one) cannot be used as a shield against fundamental rights. If a company builds a system that is inherently difficult to correct, they bear the cost of that architectural decision.16
* Model Retiring Policies: The EDPB suggests a compromise: "Model Retiring Policies." Instead of instant unlearning, controllers may aggregate erasure requests over a set period (e.g., quarterly) and apply them in a batch during a scheduled model update. This balances the right to erasure with the economic reality of model training.18
3.4 Rights to Rectification and Access
* Right to Rectification (Article 16): In the context of "hallucinations" or deepfakes (e.g., an AI generating a video of a person doing something they never did), the Right to Rectification is powerful. The user can demand the "correction" of the data. Since "correcting" a neural weight is abstract, this often translates to a demand for suppression—preventing the model from generating that specific output.16
* Right to Access (Article 15): Users have the right to know if their data was used for training. This creates a transparency obligation. AI platforms must maintain searchable indices of their training data to respond to "Did you train on me?" requests. The "black box" excuse is increasingly rejected; if you cannot know what is in your data, you cannot lawfully process it.
________________
Part IV: Transparency and The Intersection with the AI Act
Transparency is the precondition for exercising all other rights. If a user is unaware their face has been scraped, they cannot object or request erasure. The interplay between the GDPR’s transparency obligations (Articles 13/14) and the new EU AI Act creates a comprehensive disclosure regime.
4.1 The Article 14 Notification Crisis and "Public Transparency"
Article 14 GDPR requires data controllers to notify individuals when their data is collected from indirect sources (e.g., web scraping).
* The Practical Impossibility: Notifying billions of individuals that their social media images were scraped is practically impossible.
* The Exemption: Controllers often invoke Article 14(5)(b), which provides an exemption if notification proves "impossible or involves disproportionate effort."
* The "Public Info" Counter-Measure: The ICO and EDPB dictate that relying on this exemption requires public transparency as a counter-measure. Controllers must publicly declare their scraping activities, the sources used, and the categories of data collected. You do not have to email every individual, but you must make the information publicly available so that interested users can find it.20
4.2 The AI Act Public Summary Template (PST)
To formalize this transparency, the EU AI Act (Article 53) mandates that providers of General Purpose AI (GPAI) models publish a detailed summary of the content used for training. In July 2025, the European Commission released the Public Summary Template (PST) to standardize this disclosure.21
* Content Requirements: The PST does not require a list of every single URL (protecting trade secrets), but it mandates the disclosure of "main data collections," the time period of crawling, and the types of content (e.g., "facial images from social media platforms X, Y, Z").
* Weaponization of Transparency: This summary effectively "weaponizes" Article 15 rights. By reviewing the PST, individuals and civil society groups can infer whether their data was likely processed. If a user sees "Data scraped from LinkedIn 2020-2024" in the PST, they have reasonable grounds to submit a Data Subject Access Request (DSAR) or a complaint to their DPA.
4.3 Provenance and Watermarking
For the outputs of generative AI (deepfakes, clones), transparency is enforced through technical standards.
* Labeling (Article 50 AI Act): Users must be informed if they are interacting with an AI system.
* C2PA and Watermarking: The Coalition for Content Provenance and Authenticity (C2PA) standard is becoming the de facto compliance mechanism. AI platforms are expected to embed cryptographically signed metadata into generated files, verifying the "provenance" of the content. This allows platforms to distinguish between "authorized" synthetic media and malicious deepfakes, facilitating the enforcement of the "Right to Rectification" and preventing fraud.23
________________
Part V: Enforcement Landscape & Case Studies
The theoretical requirements of the GDPR are being hardened in the crucible of enforcement. The period from 2024 to 2026 has witnessed a shift from regulatory warnings to structural separation orders and massive financial penalties, signaling the end of the "wild west" era of biometric scraping.
5.1 The Clearview AI Precedent: The Death of "Offshore" Immunity
Clearview AI remains the definitive case study for biometric AI enforcement, establishing the extraterritorial reach of the GDPR.
5.1.1 The UK Upper Tribunal Judgment (October 2025)
In Information Commissioner vs. Clearview AI Inc. UKUT 319 (AAC), the UK Upper Tribunal delivered a landmark ruling that settled the question of jurisdiction.4
* The Defense: Clearview argued it was a US company providing services to non-UK law enforcement, and thus its processing was outside the material scope (national security exemption) and territorial scope of the UK GDPR.
* The Ruling: The Tribunal rejected these arguments.
   * Behavioral Monitoring: The court adopted a broad definition of "monitoring." It held that the passive collection, indexing, and vectorization of facial images constitute "monitoring of behavior" under Article 3(2)(b), even without active "watchfulness" by a human. The creation of a searchable database enables monitoring, which is sufficient.
   * Jurisdiction: Because Clearview monitored the behavior of UK residents (by creating biometric profiles of them), the GDPR applied. The fact that the clients were foreign was irrelevant to Clearview's own liability as a controller.
* Implication: This judgment closes the "offshore loophole." AI companies cannot evade GDPR by locating their servers and clients outside Europe if they scrape European data to build their models.
5.1.2 The Dutch DPA Fine (2024)
The Dutch Data Protection Authority imposed a €30.5 million fine on Clearview AI, one of the highest for a biometric violation.10
* Key Finding: The creation of the database itself was a violation of Article 9. The DPA explicitly warned that using Clearview’s services is also illegal for Dutch organizations, creating potential liability for any EU company that attempts to subscribe to such "intelligence" services.
5.2 The Italian Garante vs. Deepfakes (Provision 789)
In December 2025, the Italian Garante issued Provision No. 789, a targeted enforcement action against the proliferation of non-consensual deepfakes and voice cloning.25
* The Trigger: The rise of apps allowing users to "undress" photos or clone voices of acquaintances for bullying or fraud.
* The Ruling: The Garante mandated that any platform allowing the generation of realistic biometric content must:
   1. Verify Age: To protect minors.
   2. Obtain Consent: Obtain explicit consent not just from the creator (user) but from the subject of the generation, or demonstrate a robust legal basis (which is nearly impossible for non-consensual deepfakes).
* Biometric Classification: The Provision confirmed that voice and image data used for these purposes are biometric data because they are processed to mimic the unique characteristics of the individual.
5.3 Emerging Enforcement Trends
* Joint Controllership: The CNIL has indicated that if an AI provider (e.g., a Voice Cloning API) and a client (e.g., a Call Center) collaborate to create a fine-tuned dataset, they are Joint Controllers. This implies that the client is jointly liable for the legality of the underlying training data.27
* Scraping Taskforces: The EDPB’s "ChatGPT Taskforce" and subsequent guidelines on scraping have harmonized the view that "legitimate interest" is an invalid basis for scraping biometric data. This is leading to a wave of "deletion orders" where DPAs order the destruction of models trained on unlawfully scraped data, a penalty far more costly than any fine.
________________
Part VI: Practical Compliance Framework for AI Platforms
Based on the legal analysis and enforcement precedents, this section outlines a comprehensive compliance framework for organizations developing or deploying AI face generation and voice cloning systems.
6.1 Privacy by Design (PbD) and Technical Architectures
"Privacy by Design" (Article 25) requires the integration of data protection into the technical architecture. For biometric AI, this necessitates moving away from raw data storage.28
6.1.1 Cancelable Biometrics & BioHashing
Storing raw biometric templates (face vectors) creates a permanent risk. If a database is breached, users cannot change their face.
* Compliance Strategy: Implement "Cancelable Biometrics."
   * Mechanism: The biometric vector is distorted using a non-invertible mathematical transform, "salted" with a specific key (BioHash). The system stores only the hash, not the raw vector.
   * Revocability: If the database is compromised, the system can issue a new salt key and re-generate the templates, effectively "revoking" the compromised biometrics. This aligns with the Article 32 security principle.
6.1.2 Homomorphic Encryption (HE)
HE allows computations to be performed on encrypted data without decrypting it.
* Compliance Strategy: Use HE for the inference stage. When a user uploads a photo for face swapping, the photo is encrypted. The AI model processes the encrypted data and generates an encrypted result, which is only decrypted on the user's device.
* Benefit: The AI provider never "sees" the raw biometric data in the clear, significantly reducing the risk of Article 9 violations and data breaches.30
6.2 Data Protection Impact Assessment (DPIA)
A DPIA is mandatory for all biometric AI systems under Article 35. It must specifically address the following risks 31:
Risk Category
	Specific AI Challenge
	Mitigation Strategy
	Bias & Discrimination
	Models may perform poorly on certain demographics (e.g., darker skin tones, non-standard accents).
	Fairness Testing: rigorous testing of False Acceptance/Rejection Rates (FAR/FRR) across demographic groups. Data Balancing: curating training sets to ensure representation.
	Spoofing / Presentation Attacks
	Malicious users using deepfakes to bypass biometric auth.
	Liveness Detection: Implementation of active (e.g., "blink now") or passive (texture analysis) liveness checks.
	Data Scraping Legality
	Training data containing non-consensual or "poisoned" data.
	Data Provenance Audits: Using tools to verify the source of scraped data. Exclusion Lists: Proactively blocking known "high risk" URLs (e.g., social media profiles of minors).
	Re-Identification / Regurgitation
	The model generating the likeness of a training subject.
	Adversarial Testing: "Red-teaming" the model to attempt to extract training data. Output Filters: Blocking the generation of known public figures or private individuals.
	6.3 Governance Structure and The AI Act
Compliance requires a convergence of legal and technical governance.
* High-Risk Classification: Acknowledge that most biometric AI systems will be classified as "High Risk" under the AI Act.
   * Quality Management System (QMS): Implement a QMS to track data quality, version control of models, and logging of events.
   * Human Oversight: Incorporate "Human-in-the-Loop" measures for critical decisions (e.g., banning a user for deepfake misuse).
* Prohibited Practices: Strictly ensure the system is not used for "untargeted scraping" to build facial recognition databases (AI Act Art 5), which is a banned practice.
6.4 The "Exit Strategy": Managing Data Subject Rights
Organizations must architect their systems to handle the "Unlearning" requirement.
* SISA Architecture: Adopt the SISA (Sharded) training approach to allow for low-cost retraining when erasure requests are received.
* Withdrawal Protocols: If a user withdraws consent for their voice clone, the system must have an automated "kill switch" that prevents the generation of new content with that voice model and schedules the deletion of the embedding.
________________
Conclusion
The era of unrestricted biometric data scraping for AI training has ended in the European Union. The convergence of the GDPR’s rigorous "prohibition by default" on biometric processing and the AI Act’s transparency mandates has created a regulatory environment where provenance, consent, and reversibility are not just ethical best practices but existential legal requirements.
For AI platforms, the legal risks associated with "black box" scraping—exemplified by the severe sanctions against Clearview AI—far outweigh the efficiency gains. The future of compliant AI face generation and voice cloning lies in consented, curated datasets and privacy-preserving architectures that allow for the granular exercise of rights. Technologies like cancelable biometrics and machine unlearning are no longer academic curiosities but essential components of a defensible compliance strategy.
As we move toward full enforcement of the AI Act in 2026, the regulatory focus will increasingly shift from the input (collection) to the output (deepfakes). Organizations that fail to implement robust governance—verifying the identity of users, watermarking outputs, and ensuring the "unlearning" of personal data—risk not only massive financial penalties but the forced deletion of their core models. The path forward demands that we treat digital biometrics with the same sanctity as the biological characteristics they represent: unique, immutable, and requiring the highest standard of protection.
Citations
1
Источники
1. Guidelines 05/2022 on the use of facial recognition technology in the area of law enforcement - European Data Protection Board, дата последнего обращения: февраля 17, 2026, https://www.edpb.europa.eu/system/files/2023-05/edpb_guidelines_202304_frtlawenforcement_v2_en.pdf
2. Biometrics in the EU: Navigating the GDPR, AI Act | IAPP, дата последнего обращения: февраля 17, 2026, https://iapp.org/news/a/biometrics-in-the-eu-navigating-the-gdpr-ai-act
3. ua-2024-001563-gia ncn [2025] ukut 319 (aac) in the upper tribunal ..., дата последнего обращения: февраля 17, 2026, https://ico.org.uk/media2/mc5bjzsg/ua-2024-001563-gia.pdf
4. UK Upper Tribunal hands down judgment on Clearview AI Inc | ICO, дата последнего обращения: февраля 17, 2026, https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2025/10/uk-upper-tribunal-hands-down-judgment-on-clearview-ai-inc/
5. AI voice transcription: Implications for data protection | AEPD, дата последнего обращения: февраля 17, 2026, https://www.aepd.es/en/press-and-communication/blog/ai-voice-transcription
6. Spain: AEPD issues advisory on AI voice transcription | News - DataGuidance, дата последнего обращения: февраля 17, 2026, https://www.dataguidance.com/news/spain-aepd-issues-advisory-ia-voice-transcription
7. Biometric data & biometric systems: European & Spanish legal framework - Veridas, дата последнего обращения: февраля 17, 2026, https://veridas.com/docs/Veridas-Biometric-data-biometric-systems.pdf
8. The Intersection of GDPR and AI and 6 Compliance Best Practices | Exabeam, дата последнего обращения: февраля 17, 2026, https://www.exabeam.com/explainers/gdpr-compliance/the-intersection-of-gdpr-and-ai-and-6-compliance-best-practices/
9. How do we process biometric data lawfully? | ICO, дата последнего обращения: февраля 17, 2026, https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/biometric-data-guidance-biometric-recognition/how-do-we-process-biometric-data-lawfully/
10. Dutch Supervisory Authority imposes a fine on Clearview because of ..., дата последнего обращения: февраля 17, 2026, https://www.edpb.europa.eu/news/national-news/2024/dutch-supervisory-authority-imposes-fine-clearview-because-illegal-data_en
11. AI: The CNIL finalises its recommendations on the development of artificial intelligence systems and announces its upcoming work, дата последнего обращения: февраля 17, 2026, https://www.cnil.fr/en/ai-cnil-finalises-its-recommendations-development-artificial-intelligence-systems
12. CNIL Fines Clearview AI 20 Million Euros for Unlawful Use of Facial Recognition Technology - Hunton Andrews Kurth LLP, дата последнего обращения: февраля 17, 2026, https://www.hunton.com/privacy-and-cybersecurity-law-blog/cnil-fines-clearview-ai-20-million-euros-for-unlawful-use-of-facial-recognition-technology
13. AI development and scientific research: A way out of the GDPR's ..., дата последнего обращения: февраля 17, 2026, https://iapp.org/news/a/ai-development-and-scientific-research-a-way-out-of-the-gdpr-s-article-9-2-
14. Germany - Hamburg District Court, 310 O.22723, LAION v Robert Kneschke - EUIPO, дата последнего обращения: февраля 17, 2026, https://www.euipo.europa.eu/en/law/recent-case-law/germany-hamburg-district-court-310-o-22723-laion-v-robert-kneschke
15. Specific measures for data-intensive health research without consent: a systematic review of soft law instruments and academic literature - PMC, дата последнего обращения: февраля 17, 2026, https://pmc.ncbi.nlm.nih.gov/articles/PMC10772063/
16. Ensuring and facilitating the exercise of data subjects' rights - CNIL, дата последнего обращения: февраля 17, 2026, https://www.cnil.fr/en/ensuring-and-facilitating-exercise-data-subjects-rights
17. Erasing personal data in an AI era - Leiden Law Blog, дата последнего обращения: февраля 17, 2026, https://www.leidenlawblog.nl/articles/erasing-personal-data-in-an-ai-era
18. AI-Complex Algorithms and effective Data Protection Supervision ..., дата последнего обращения: февраля 17, 2026, https://www.edpb.europa.eu/system/files/2025-01/d2-ai-effective-implementation-of-data-subjects-rights_en.pdf
19. Bridge the Gaps between Machine Unlearning and AI Regulation - arXiv, дата последнего обращения: февраля 17, 2026, https://arxiv.org/html/2502.12430v1
20. What Does It Mean to Be GDPR Compliant? A Complete Guide for Web Scrapers, дата последнего обращения: февраля 17, 2026, https://www.octoparse.com/blog/gdpr-compliance-in-web-scraping
21. Addressing GDPR's Shortcomings in AI Training Data Transparency ..., дата последнего обращения: февраля 17, 2026, https://www.techpolicy.press/addressing-gdprs-shortcomings-in-ai-training-data-transparency-with-the-ai-act/
22. Commission presents template for General-Purpose AI model providers to summarise the data used to train their model, дата последнего обращения: февраля 17, 2026, https://digital-strategy.ec.europa.eu/en/news/commission-presents-template-general-purpose-ai-model-providers-summarise-data-used-train-their
23. High-level summary of the AI Act | EU Artificial Intelligence Act, дата последнего обращения: февраля 17, 2026, https://artificialintelligenceact.eu/high-level-summary/
24. ICO's Appeal in Clearview AI Case Upheld | URM Consulting, дата последнего обращения: февраля 17, 2026, https://www.urmconsulting.com/blog/icos-appeal-in-clearview-ai-case-upheld
25. Garante issues warning against generating non-consensual ..., дата последнего обращения: февраля 17, 2026, https://www.aoshearman.com/en/insights/ao-shearman-on-data/garante-issues-warning-against-generating-non-consensual-deepfakes
26. Italy: Garante warns against deepfakes | News - DataGuidance, дата последнего обращения: февраля 17, 2026, https://www.dataguidance.com/news/italy-garante-warns-against-deepfakes
27. Determining the legal qualification of AI system providers | CNIL, дата последнего обращения: февраля 17, 2026, https://www.cnil.fr/node/164396
28. Privacy by Design and AI - TechGDPR, дата последнего обращения: февраля 17, 2026, https://techgdpr.com/blog/how-to-build-trustworthy-ai-from-the-ground-up-with-privacy-by-design/
29. Cancelable Biometrics: A Review, дата последнего обращения: февраля 17, 2026, https://engineering.jhu.edu/vpatel36/wp-content/uploads/2018/08/SPM_CB_v6.pdf
30. Hybrid Protection of Biometric Templates by Combining Homomorphic Encryption and Cancelable Biometrics - Idiap Publications, дата последнего обращения: февраля 17, 2026, https://publications.idiap.ch/downloads/papers/2022/OtroshiShahreza_IJCB_2022.pdf
31. The ICO's AI and biometrics strategy | Inside Global Tech, дата последнего обращения: февраля 17, 2026, https://www.insideglobaltech.com/2025/07/11/the-icos-ai-and-biometrics-strategy/
32. Discrimination and Bias | ICO, дата последнего обращения: февраля 17, 2026, https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/discrimination-and-bias/
33. Opinion 28/2024 on certain data protection aspects related to the processing of personal data in the context of AI models, дата последнего обращения: февраля 17, 2026, https://www.edpb.europa.eu/system/files/2024-12/edpb_opinion_202428_ai-models_en.pdf
34. CNIL Publishes Recommendations on AI and GDPR - Hunton Andrews Kurth LLP, дата последнего обращения: февраля 17, 2026, https://www.hunton.com/privacy-and-cybersecurity-law-blog/cnil-publishes-recommendations-on-ai-and-gdp
35. Privacy of Personal Data in the Generative AI Data Lifecycle – NYU ..., дата последнего обращения: февраля 17, 2026, https://jipel.law.nyu.edu/privacy-of-personal-data-in-the-generative-ai-data-lifecycle/