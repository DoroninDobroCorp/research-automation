Biometric data used for AI face generation and voice cloning is almost always “special category” data under GDPR/UK GDPR, so it generally requires both an Article 6 lawful basis and an Article 9 condition, typically explicit consent, plus strong safeguards and DPIAs. Supervisory authorities have repeatedly fined providers of facial recognition and AI tools for scraping images or using biometric identifiers without a valid legal basis, inadequate transparency, missing DPIAs, and failure to honour erasure and access rights.
hunton
+6

Biometric data under GDPR

GDPR defines biometric data in Article 4(14) as personal data resulting from specific technical processing of physical, physiological, or behavioural characteristics that allow or confirm the unique identification of a person (e.g. facial images, fingerprints). Regulators and guidance clarify that both facial templates and voice “prints” generated through technical processing to recognise or authenticate a person are biometric data, even if only an AI model can interpret them. Ordinary photos or voice recordings are not biometric data unless they are processed with specific technology for unique identification, but they are still personal data if individuals are identifiable.
gdprlearninghub
+5

Special category and Article 9

Biometric data become “special category” data when processed “for the purpose of uniquely identifying a natural person” (Article 9(1) GDPR/UK GDPR). This means most facial recognition and voiceprint systems for authentication, surveillance, or identity verification fall under Article 9, triggering a general prohibition unless a specific exception applies. Regulators treat biometric recognition as inherently high‑risk, emphasising heightened necessity, proportionality, and security standards.
yourdata-yourrights
+4

Legal bases and consent for AI face/voice systems

Controllers must have both an Article 6 lawful basis (e.g. consent, legitimate interests, contract, legal obligation) and an Article 9 condition (e.g. explicit consent, employment/social security, substantial public interest) to process biometric identifiers. For commercial face‑generation and voice‑cloning services, DPAs and the ICO say explicit consent is usually the only realistic Article 9 condition, because “legitimate interests” generally fails the balancing test given the intrusiveness and lack of reasonable expectations. The CNIL and others have rejected attempts to rely on legitimate interest for large‑scale scraping of images for facial recognition, as in the Clearview AI decisions, finding no valid legal basis and ordering cessation and deletion.
privacyworld
+6

Templates, embeddings, and synthetic data

Biometric templates (e.g. facial feature vectors, voice embeddings) created for recognition or authentication are themselves biometric data and, when used for unique identification, special‑category data, regardless of whether humans can interpret them directly. The EDPB’s Opinion on AI models stresses that models trained on personal data (including biometric templates) are not “anonymous” merely because data are embedded; the anonymity threshold is very high and requires a negligible risk of extracting personal data for every data subject. Purely synthetic faces or voices that cannot be linked to an identifiable person fall outside GDPR, but if models can be prompted to reproduce or infer specific individuals’ likenesses or voice characteristics, GDPR duties re‑attach because personal data are again at stake.
privacymatters.dlapiper
+7

Data subject rights and AI training data

Training on facial images, voice recordings, or related metadata triggers full GDPR/UK GDPR obligations: transparency (Articles 13–14), access (Article 15), rectification, erasure, restriction, objection, and data portability where applicable. The EDPB’s AI model Opinion emphasises that controllers must design training and deployment so data subjects can effectively exercise their rights, including providing opt‑out from use of their data for training and implementing technical measures to reduce personal data in models. Supervisory authorities can order not only deletion of unlawfully collected training data, but in serious cases restrictions on or even destruction of AI models built on such data.
clydeco
+7

Right to erasure and AI‑generated outputs

DPAs have ordered controllers using facial recognition to erase scraped images, derived biometric templates, and profiles relating to individuals who invoke their rights or where processing lacked a legal basis, as in the Clearview AI decisions in Italy, France, and the UK. The EDPB has indicated