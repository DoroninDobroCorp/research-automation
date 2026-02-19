# Precision Playbook: Navigating GDPR Rules for Biometric Face Generation & Voice Cloning in 2026

## Executive Summary

As of February 2026, the regulatory landscape for AI-driven biometric processing has shifted from theoretical guidance to active enforcement. European Data Protection Authorities (DPAs) have clarified that the "biometric" classification applies not just to raw images but to the mathematical templates (embeddings) extracted from them. Consequently, AI models that generate or clone faces and voices are increasingly treated as processing special category data under Article 9 of the GDPR, triggering strict consent and impact assessment obligations.

**Key Strategic Insights:**
* **Biometric = "Template", not just "Photo":** Recent enforcement actions confirm that 512-dimensional identity embeddings used in AI synthesis are functionally equivalent to biometric templates because they allow unique identification [1] [2]. Deleting the original photo is insufficient if the embedding remains; the embedding itself triggers Article 9 protections [3] [4].
* **Explicit-Consent Gap:** Major fines against Clearview AI (€20M+) and Mercadona (€2.5M) demonstrate that "legitimate interest" is rarely a valid basis for commercial biometric identification [5] [6]. Valid consent must be "explicit" and "freely given," which regulators interpret to mean users must have a genuine, non-biometric alternative (e.g., a badge or PIN) without detriment [3] [7].
* **Erasure = Machine Unlearning:** The "Right to be Forgotten" (Article 17) now extends to the influence of data on a trained model. The CNIL and EDPB have indicated that if a model "memorizes" personal data (common in generative AI), controllers may need to retrain the model or use "exact unlearning" techniques like SISA (Sharded, Isolated, Sliced, and Aggregated) to effectively remove a person's data [8] [9].
* **DPIA Is Not Optional:** Processing biometric data for identification is widely classified as "high risk," making a Data Protection Impact Assessment (DPIA) mandatory before processing begins [10] [11]. Failure to conduct a DPIA is a primary citation in recent high-profile fines [12] [13].
* **International Transfers:** Post-Schrems II, transferring biometric data to jurisdictions with surveillance laws (like the US) requires rigorous Transfer Impact Assessments (TIAs). Encryption is only considered an effective supplementary measure if the decryption keys remain solely within the EEA or an adequate jurisdiction [14] [15].
* **Deepfake Duty Shift:** The EU AI Act (Article 50) and Digital Services Act (DSA) impose new transparency obligations. Platforms must label AI-generated content ("deepfakes"), but for non-consensual sexual or defamatory content, labeling is insufficient—removal is required [16] [17].

---

## 1. What Counts as "Biometric Data" in 2026 — Templates, Embeddings & Edge-Cases

The definition of biometric data has evolved to capture the technical reality of modern AI. It is no longer just about the source image but the derived data used for processing.

### Definition Deep-Dive: Article 4(14) + Recital 51
Under Article 4(14) of the GDPR, "biometric data" is personal data resulting from **specific technical processing** relating to physical, physiological, or behavioral characteristics that allow or confirm the **unique identification** of a natural person [18] [19].

* **The "Template" Threshold:** A digital photograph itself is not biometric data unless it undergoes specific technical processing to extract unique features (a "template" or "embedding") for identification [18] [3].
* **EDPB 3-Criteria Test:** To trigger Article 9 (special category) protections, three cumulative criteria must be met [3]:
 1. **Nature of data:** Relates to physical/physiological/behavioral characteristics.
 2. **Means of processing:** Results from specific technical processing (e.g., feature extraction).
 3. **Purpose of processing:** Used for the purpose of **uniquely identifying** a natural person.

### Technical Mapping: AI Pipelines & Biometric Status
In AI face generation and voice cloning, the creation of an "identity embedding" (a vector representation of a face or voice) is the critical regulatory trigger.

| AI Pipeline Stage | Data Type | GDPR Status | Regulatory Note |
| :--- | :--- | :--- | :--- |
| **Raw Input** (Photo/Audio) | Personal Data | Art. 6 (General) | Becomes Art. 9 if used for ID [18]. |
| **Feature Extraction** | Biometric Data | **Art. 9 (Special)** | The act of extraction is "specific technical processing" [3]. |
| **Embedding/Template** | Biometric Data | **Art. 9 (Special)** | Unique identifier; allows re-identification [2] [20]. |
| **Synthesis/Output** | Personal Data | Art. 6 (General) | If the output makes a person recognizable, it "relates to" them [21]. |

### Non-Obvious Cases
* **Classification vs. Identification:** If a system processes facial features solely to classify demographics (e.g., age, gender, emotion) *without* generating a unique template to identify the person, it may not fall under Article 9, provided no unique identifiers are stored [3] [22]. However, this is a high-risk area; inferring emotion is increasingly restricted under the AI Act [16].
* **On-Device Processing:** Storing biometric templates locally on a user's device (e.g., smartphone) is preferred and reduces risk, but the initial generation of the template still constitutes biometric processing [23] [24].

---

## 2. Lawful Bases & Explicit-Consent Mechanics That Survive Audit

Processing biometric data for identification is generally prohibited under Article 9(1). To proceed, organizations must secure a valid exception under Article 9(2), typically **explicit consent**.

### Article 6 vs Article 9 Double-Lock
Controllers must identify a lawful basis under **Article 6** (e.g., consent or contract) AND a separate condition under **Article 9** (e.g., explicit consent) [25] [26]. "Legitimate interest" (Art. 6(1)(f)) is **insufficient** to lift the Article 9 prohibition for biometric identification in most commercial contexts [5] [6].

### Designing "Freely Given" Flows
Consent is invalid if the user has no genuine choice.
* **No "Pay-or-Okay" for Biometrics:** Access to a service cannot be conditional on biometric consent if the biometrics are not strictly necessary for the service itself [27] [7].
* **Mandatory Alternatives:** For access control (e.g., building entry), controllers *must* offer a non-biometric alternative (key card, PIN) without penalty or cost to ensure consent is freely given [3] [28].
* **Easy Withdrawal:** Users must be able to withdraw consent as easily as they gave it (e.g., a "one-click" withdrawal option) [7] [29].

### Invalid Bases Hall-of-Fame
* **Retail/Security Scanning:** Mercadona was fined €2.5M for using facial recognition to detect individuals with restraining orders. The AEPD ruled that "public interest" did not apply to a private entity, and consent was impossible to obtain from every shopper entering the store [6] [13].
* **Employee Attendance:** The Swedish DPA fined a school for using facial recognition for attendance, ruling that the power imbalance between students/school made "consent" invalid [12].
* **Web Scraping:** Clearview AI's argument that scraping public images relied on "legitimate interest" was rejected by multiple DPAs (Italy, France, Greece), confirming that mere public availability does not waive Article 9 protections [5] [30].

---

## 3. Special-Category Processing Rules & DPIA Must-Haves

Because biometric identification is inherently high-risk, procedural compliance is strictly enforced.

### Article 9(2) Exceptions Matrix

| Exception | Applicability to AI Face/Voice | Risk Level |
| :--- | :--- | :--- |
| **(a) Explicit Consent** | **Primary Basis.** Required for commercial cloning, apps, and authentication. | High (Must be uncoerced) [7] |
| **(b) Employment/Social Security** | **Rare.** Only if authorized by specific Member State law (e.g., high-security clearance). | Very High (Power imbalance) [31] |
| **(g) Substantial Public Interest** | **Strict.** Requires basis in EU/Member State law (e.g., national security). Not for private firms. | N/A for most private AI [32] |
| **(j) Research/Statistics** | **Conditional.** Possible for academic research with strict safeguards (pseudonymization). | Medium (Requires Art. 89 safeguards) [33] |

### DPIA Checklist
A Data Protection Impact Assessment (DPIA) is **mandatory** for systematic monitoring of public areas or large-scale processing of special category data [10] [11].
* **EDPB 9-Risk Criteria:** A DPIA is required if processing meets two or more criteria (e.g., sensitive data + innovative use) [34] [35].
* **Assessment Scope:** Must cover necessity, proportionality, risks to rights (discrimination, errors), and security measures [10] [36].
* **Prior Consultation (Art. 36):** If the DPIA reveals high risks that cannot be mitigated, the controller *must* consult the DPA before processing [37].

---

## 4. Data-Subject Power Stack — Access, Erasure & Objection in Generative AI

Data subjects have robust rights over their biometric data, extending into the AI models themselves.

### Access: Disclosing Embeddings & Provenance
* **Right of Access (Art. 15):** Includes "inferred" and "derived" data. If an AI generates a biometric profile or embedding, the user has a right to know it exists and understand the logic used [38].
* **Transparency:** Controllers should provide information on data sources (e.g., scraped URLs) if data wasn't collected directly from the subject [39].

### Erasure: Machine Unlearning
* **Right to Erasure (Art. 17):** Applies to training data. If a user withdraws consent, their data must be deleted [40].
* **Model Impact:** The CNIL and EDPB state that if a model "memorizes" personal data (e.g., a voice clone), simply deleting the training file is insufficient. The controller may need to **retrain the model** or use **machine unlearning** techniques (like SISA) to remove the data's influence [8] [9].
* **Proportionality:** Retraining may be batched (e.g., quarterly), but indefinite retention in a live model is non-compliant [39].

### Objection & Opt-Out
* **Right to Object (Art. 21):** Users can object to processing based on legitimate interest. For generative AI training, DPAs recommend implementing "opt-out" registries or respecting machine-readable signals (like robots.txt) [39].

---

## 5. Security & Minimisation Across the Model Lifecycle

Security measures must be specific to the risks of biometric data (e.g., irreversibility).

### Collection Controls
* **Liveness Detection:** Implement Presentation Attack Detection (PAD) to prevent spoofing (masks, deepfakes) during enrollment [41] [42].
* **Injection Attack Detection (IAD):** Monitor for digital injection attacks (virtual cameras) which are increasingly common with deepfakes [41].

### Storage & Retention
* **Diversified Templates:** Use cancelable biometrics or salted hashes so that if a database is breached, the template cannot be used across other systems [43] [44].
* **Separation:** Store biometric templates separately from identity data (names, IDs) using pseudonymization [45].
* **Auto-Purge:** Intermediate templates created "on the fly" for matching must be deleted immediately after the comparison [3] [28].

### Inference & Output
* **Watermarking:** AI-generated content should be marked (e.g., C2PA, SynthID) to ensure provenance and detectability [46] [17].
* **Human Oversight:** High-risk biometric identification (e.g., remote ID) requires human-in-the-loop verification to prevent automated discrimination [47].

---

## 6. International Transfers & Schrems-II Proof Architectures

Transferring biometric data outside the EEA (e.g., to US cloud providers) is legally complex following the *Schrems II* judgment.

### TIA 6-Step Roadmap
1. **Map Transfers:** Identify all flows of biometric data to third countries [48].
2. **Identify Tool:** Use Standard Contractual Clauses (SCCs) (Module 1 or 2) [49].
3. **Assess Law:** Determine if the destination country's laws (e.g., US FISA 702) allow disproportionate government access [14].
4. **Supplementary Measures:** If laws are problematic, implement technical measures. **Encryption is only effective if the keys are held solely in the EEA** [14] [15].
5. **Procedural Steps:** Document the TIA and measures.
6. **Re-evaluate:** Monitor legal changes.

### Split-Processing
For sensitive biometrics, "split processing" (sharding data across multiple jurisdictions so no single provider has the full dataset) is a recognized supplementary measure [14] [15].

---

## 7. Children, Vulnerable Persons & Heightened Safeguards

Children's biometric data merits "specific protection" (Recital 38).

### Member-State Age Thresholds
The GDPR default age for digital consent is 16, but Member States can lower it to 13.
* **13:** UK, ES, SE, PL, IE, DK [50].
* **14:** AT, IT, BG [50].
* **15:** FR [50].
* **16:** DE, NL, HU [50].

### Risk-Based Age Assurance
* **Verification:** Controllers must make "reasonable efforts" to verify age. For high-risk biometric services, simple self-declaration is insufficient; robust methods (e.g., nominal bank transaction) may be required [7].
* **Default Deny:** Processing biometric data of children for marketing or profiling is generally considered disproportionate and should be blocked by default [27] [51].

---

## 8. Deepfakes & Voice Cloning — From Watermarking to Takedown

The EU regulatory framework for deepfakes combines the AI Act, DSA, and GDPR.

### Preventive Controls
* **Transparency (AI Act Art. 50):** Providers must ensure AI outputs are machine-readable/detectable. Deployers must disclose deepfakes to viewers [16].
* **Consent for Cloning:** Cloning a real person's voice/face requires their explicit consent. Non-consensual cloning violates GDPR and potentially criminal laws [52] [21].

### Post-Generation & Takedown
* **Illegal Content (DSA):** Non-consensual sexual deepfakes are "illegal content." Platforms must have notice-and-action mechanisms to remove them promptly; labeling is not a defense [17].
* **Trusted Flaggers:** Platforms must prioritize reports from trusted flaggers regarding deepfake abuse [53].

---

## 9. Enforcement Heat-Map 2019-2026: Who Was Fined, For What, How Much

| Year | Entity | DPA | Violation | Fine / Order | Lesson |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **2022** | **Clearview AI** | CNIL (FR), Garante (IT), HDPA (GR) | Art 6, 9, 14 (Unlawful processing, no transparency) | **€20M** + deletion orders | Scraping public images is **not** a legitimate interest; Art 9 applies. [5] [30] |
| **2021** | **Mercadona** | AEPD (ES) | Art 9, 35 (No valid basis, bad DPIA) | **€2.5M** | "Public interest" exception is strict; cannot scan all customers to find a few. [6] [13] |
| **2024** | **Worldcoin** | AEPD (ES), BayLDA (DE) | Art 9 (Consent withdrawal, minors) | **Ban** / Data Purge | Consent must be withdrawable; high risk to minors justifies precautionary bans. [54] [55] |
| **2021** | **Swedish Police** | IMY (SE) | Art 9 (Unlawful use of Clearview) | **€250k** | Using 3rd-party biometric tools without a DPIA/legal basis is unlawful. [56] |
| **2019** | **School Board** | IMY (SE) | Art 9 (Invalid consent) | **€20k** | Consent is invalid where there is a power imbalance (student/school). [12] |

---

## 10. Governance & Audit Evidence for Proving Compliance

DPAs require documented evidence, not just policy statements.

### Core Artefacts
* **RoPA (Art. 30):** Must explicitly list biometric data categories, retention periods, and technical security measures [57].
* **DPIA Sign-offs:** Completed and signed DPIA *before* processing starts [10].
* **Consent Logs:** Records of who consented, when, and to what specific version of the privacy notice [29].
* **Unlearning Tickets:** Logs showing execution of erasure requests, including model retraining or shard deletion [8].

### KPIs/KRIs
* **DSAR SLA:** % of access/erasure requests fulfilled within 1 month.
* **Biometric Accuracy:** False Match Rate (FMR) / False Non-Match Rate (FNMR) across demographics to monitor bias [58].
* **PAD Metrics:** Attack Presentation Classification Error Rate (APCER) to measure anti-spoofing effectiveness [41].

---

## 11. Non-EU Benchmarks — BIPA, Brazil LGPD/ANPD, China Deep-Synthesis, UK ICO

| Feature | **EU GDPR** | **Illinois BIPA (USA)** | **UK ICO (UK GDPR)** | **China Deep Synthesis** |
| :--- | :--- | :--- | :--- | :--- |
| **Consent** | Explicit, freely given (Art 9). | Written release required. | Explicit consent (Art 9). | Separate consent for editing biometrics. |
| **Scope** | Templates = Biometric data. | "Biometric Identifier" (scan of face geometry). | "Biometric Recognition" vs "Classification". | Face/voice editing requires consent. |
| **Enforcement** | DPA Fines (up to 4% turnover). | Private Right of Action ($1k-$5k per violation). | DPA Fines + Enforcement Notices. | Admin penalties + Criminal liability. |
| **Key Risk** | Lack of valid legal basis (Art 9). | Class action lawsuits. | High-risk processing (DPIA mandatory). | Content security & labeling. |

**Harmonization Strategy:** Adopt a "strictest common denominator" approach: obtain explicit, written/recorded consent (satisfies GDPR, BIPA, UK) and implement strict retention schedules (e.g., 3 years or upon purpose fulfillment) [59] [60].

---

## 12. Rapid-Action Compliance Roadmap

**Phase 1 (Days 1-30): Assessment & Stops**
* **Inventory:** Map all flows of face/voice embeddings. Identify where "templates" are created.
* **Stop Gaps:** Suspend any biometric processing relying solely on "legitimate interest" or bundled consent.
* **DPIA:** Launch a DPIA for any identification features.

**Phase 2 (Days 31-60): Remediation & Architecture**
* **Consent UX:** Redesign enrollment to require explicit, granular consent with a non-biometric alternative.
* **Data Hygiene:** Purge legacy biometric data lacking valid consent.
* **Security:** Implement encryption with EU-held keys for transfers.

**Phase 3 (Days 61-120): Operationalization**
* **Rights Portal:** Build self-service tools for access and erasure (including model unlearning workflows).
* **Watermarking:** Integrate C2PA/SynthID for generated content.
* **Audit:** Conduct a mock audit of RoPA, DPIA, and consent logs.

## References

1. *Guidelines 3/2019 on processing of personal data through video devices | European Data Protection Board*. https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-32019-processing-personal-data-through-video_en
2. *Opinion 11/2024 on the use of facial recognition to streamline ...*. https://www.edpb.europa.eu/system/files/2024-05/edpb_opinion_202411_facialrecognitionairports_en.pdf
3. *Guidelines 3/2019 on processing of personal data through ...*. https://www.edpb.europa.eu/sites/default/files/files/file1/edpb_guidelines_201903_video_devices_en_0.pdf
4. *Opinion 28/2024 on certain data protection aspects related to ...*. https://www.edpb.europa.eu/system/files/2024-12/edpb_opinion_202428_ai-models_en.pdf
5. *Facial recognition: Italian SA fines Clearview AI EUR 20 million | European Data Protection Board*. https://www.edpb.europa.eu/news/national-news/2022/facial-recognition-italian-sa-fines-clearview-ai-eur-20-million_en
6. *€2,5 million GDPR fine to Spanish supermarket chain Mercadona – Data Privacy Manager*. https://dataprivacymanager.net/e25-million-gdpr-fine-to-spanish-supermarket-chain-mercadona/
7. *Guidelines 05/2020 on consent under Regulation 2016/679 ...*. https://www.edpb.europa.eu/sites/default/files/files/file1/edpb_guidelines_202005_consent_en.pdf
8. *Effective implementation of data subjects' rights*. https://www.edpb.europa.eu/system/files/2025-01/d2-ai-effective-implementation-of-data-subjects-rights_en.pdf
9. *Développement des systèmes d’IA : les recommandations de la CNIL pour respecter le RGPD | CNIL*. https://www.cnil.fr/fr/developpement-des-systemes-dia-les-recommandations-de-la-cnil-pour-respecter-le-rgpd
10. *Art. 35 GDPR – Data protection impact assessment - General Data Protection Regulation (GDPR)*. https://gdpr-info.eu/art-35-gdpr/
11. *List of Types of Data Processing Operations Which Require ...*. https://www.dataprotection.ie/sites/default/files/uploads/2018-11/Data-Protection-Impact-Assessment.pdf
12. *Facial recognition in school renders Sweden’s first GDPR fine | European Data Protection Board*. https://www.edpb.europa.eu/news/national-news/2019/facial-recognition-school-renders-swedens-first-gdpr-fine_sv
13. *Spanish DPA Fines Supermarket Chain 2,520,000 EUR for Unlawful Use of Facial Recognition System*. https://www.hunton.com/privacy-and-information-security-law/spanish-dpa-fines-supermarket-chain-2520000-eur-for-unlawful-use-of-facial-recognition-system
14. *Recommendations 01/2020 on measures that supplement ...*. https://www.edpb.europa.eu/system/files/2021-06/edpb_recommendations_202001vo.2.0_supplementarymeasurestransferstools_en.pdf
15. *EDPB Recommendations on Tools for the Transfer of ...*. https://www.mosessinger.com/publications/edpb-recommendations-on-tools-for-the-transfer-of-personal-data-from-the-eu-under-gdpr
16. *Article 50: Transparency Obligations for Providers and Deployers of Certain AI Systems | EU Artificial Intelligence Act*. https://artificialintelligenceact.eu/article/50/
17. *What the EU’s New AI Code of Practice Means for Labeling Deepfakes | TechPolicy.Press*. https://techpolicy.press/what-the-eus-new-ai-code-of-practice-means-for-labeling-deepfakes
18. *L_2016119EN.01000101.xml*. https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679
19. *Art. 4 GDPR – Definitions - General Data Protection Regulation (GDPR)*. https://gdpr-info.eu/art-4-gdpr/
20. *Guidelines 05/2022 on the use of facial recognition ...*. https://www.edpb.europa.eu/system/files/2023-05/edpb_guidelines_202304_frtlawenforcement_v2_en.pdf
21. *Deepfakes and the GDPR | Privacy Company Blog*. https://www.privacycompany.eu/blog/deepfakes-and-the-gdpr
22. *Opinion 3/2012 on developments in biometric technologies*. https://ec.europa.eu/justice/article-29/documentation/opinion-recommendation/files/2012/wp193_en.pdf
23. *Biométrie dans les smartphones des particuliers : application du cadre de protection des données | CNIL*. https://www.cnil.fr/fr/biometrie-dans-les-smartphones-des-particuliers-application-du-cadre-de-protection-des-donnees
24. *White paper - On the record*. https://www.cnil.fr/sites/cnil/files/atoms/files/cnil_white-paper-on_the_record.pdf
25. *Guidelines 02/2021 on virtual voice assistants Version 2.0*. https://www.edpb.europa.eu/system/files/2021-07/edpb_guidelines_202102_on_vva_v2.0_adopted_en.pdf
26. *Facial Recognition Technology (FRT) and surveillance | ICO*. https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/cctv-and-video-surveillance/guidance-on-video-surveillance-including-cctv/additional-considerations-for-technologies-other-than-cctv/facial-recognition-technology-frt-and-surveillance/?search=Taxi
27. *General Data Protection Regulation (EU) 2016/679 - EUR-Lex*. https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng
28. *Guidelines 3/2019 on processing of personal data through ...*. https://www.edpb.europa.eu/sites/default/files/files/file1/edpb_guidelines_201903_video_devices.pdf
29. *How should we obtain, record and manage consent? | ICO*. https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/consent/how-should-we-obtain-record-and-manage-consent/
30. *The French SA fines Clearview AI EUR 20 million | European Data Protection Board*. https://www.edpb.europa.eu/news/national-news/2022/french-sa-fines-clearview-ai-eur-20-million_en
31. *guidelines-clocking-and-attendance-control-processing- ...*. https://www.aepd.es/guides/guidelines-clocking-and-attendance-control-processing-using-biometric-systems.pdf
32. *B REGULATION (EU) 2016/679 OF THE EUROPEAN ...*. https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:02016R0679-20160504
33. *Consolidated TEXT: 32016R0679 — EN — 04.05.2016*. https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02016R0679-20160504
34. *When do we need to do a DPIA? | ICO*. https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/data-protection-impact-assessments-dpias/when-do-we-need-to-do-a-dpia/
35. *Be compliant - European Data Protection Board*. https://www.edpb.europa.eu/sme-data-protection-guide/be-compliant_en
36. *Guidance Note:*. https://www.dataprotection.ie/sites/default/files/uploads/2019-10/Guide%20to%20Data%20Protection%20Impact%20Assessments%20(DPIAs)_Oct19.pdf
37. *Art. 36 GDPR – Prior consultation - General Data Protection Regulation (GDPR)*. https://gdpr-info.eu/art-36-gdpr/
38. *Guidelines 01/2022 on data subject rights - Right of access ...*. https://www.edpb.europa.eu/system/files/2023-04/edpb_guidelines_202201_data_subject_rights_access_v2_en.pdf
39. *AI system development: CNIL’s recommendations to comply with the GDPR | CNIL*. https://www.cnil.fr/en/ai-system-development-cnils-recommendations-to-comply-gdpr
40. *Right to erasure | ICO*. https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/individual-rights/right-to-erasure/
41. *REMOTE ID PROOFING GOOD PRACTICES - ENISA*. https://www.enisa.europa.eu/sites/default/files/2024-11/Remote%20ID%20Proofing%20Good%20Practices_en_0.pdf
42. *ENISA Report - Remote Identity Proofing - Attacks ...*. https://www.enisa.europa.eu/sites/default/files/publications/ENISA%20Report%20-%20Remote%20Identity%20Proofing%20-%20Attacks%20%26%20Countermeasures.pdf
43. *ISO/IEC 24745:2022 - Biometric information protection*. https://www.iso.org/standard/75302.html
44. *ISO/IEC DIS 24745*. https://cdn.standards.iteh.ai/samples/75302/5f55429f9cea4901b01c380636fb7cbf/ISO-IEC-DIS-24745.pdf
45. *Biometric Data GDPR: Compliance Tips for Businesses*. https://www.gdprregister.eu/articles/biometric-data-gdpr/
46. *Code of Practice on marking and labelling of AI-generated content | Shaping Europe’s digital future*. https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content
47. *Regulation - 2016/679 - EN - gdpr - EUR-Lex - European Union*. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32016R0679
48. *EDPB Recommendations on supplementary measures*. https://www.edps.europa.eu/sites/default/files/publication/edpb_recommendations_on_supplementary_measures_-_dpo_meeting_11_dec_2020_en.pdf
49. *Implementing decision - 2021/914 - EN - EUR-Lex*. https://eur-lex.europa.eu/eli/dec_impl/2021/914/oj/eng
50. *Consent to use data on children | European Union Agency for Fundamental Rights*. https://fra.europa.eu/en/publication/2017/mapping-minimum-age-requirements-concerning-rights-child-eu/consent-use-data-children
51. *Statement 1/2025 on Age Assurance Adopted on 11 February ...*. https://www.edpb.europa.eu/system/files/2025-04/edpb_statement_20250211ageassurance_v1-2_en.pdf
52. *France: CNIL issues guidance on deepfakes and illegal AI‑generated content | News | DataGuidance*. https://www.dataguidance.com/news/france-cnil-issues-guidance-deepfakes-and-illegal-ai
53. *Commission publishes guidelines under the DSA*. https://ec.europa.eu/commission/presscorner/detail/en/ip_24_1707
54. *The Agency orders a precautionary measure which prevents Worldcoin from continuing to process personal data in Spain | AEPD*. https://www.aepd.es/en/press-and-communication/press-releases/agency-orders-precautionary-measure-which-prevents-Worldcoin-from-continuing-toprocess-personal-data-in-spain
55. *Orders: - European Data Protection Board*. https://www.edpb.europa.eu/system/files/2025-02/decision1594_0.pdf
56. *Swedish DPA: Police unlawfully used facial recognition app | European Data Protection Board*. https://www.edpb.europa.eu/news/national-news/2021/swedish-dpa-police-unlawfully-used-facial-recognition-app_en
57. *Guidance Note:*. https://www.dataprotection.ie/sites/default/files/uploads/2023-04/Records%20of%20Processing%20Activities%20%28RoPA%29%20under%20Article%2030%20GDPR.pdf
58. *How do we process biometric data fairly? | ICO*. https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/biometric-data-guidance-biometric-recognition/how-do-we-process-biometric-data-fairly/
59. *(740 ILCS 14/) Biometric Information Privacy Act.*. https://www.ilga.gov/Legislation/ILCS/Articles?ActID=3004&ChapterID=57&Print=True
60. *740 ILCS 14/15*. https://www.ilga.gov/documents/legislation/ilcs/documents/074000140K15.htm