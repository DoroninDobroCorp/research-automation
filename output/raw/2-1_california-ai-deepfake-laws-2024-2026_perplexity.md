California now has a layered framework regulating AI‑generated content, deepfakes, and digital likeness that combines traditional publicity and privacy law with new, AI‑specific statutes. As of 2024–26, the key pillars for your issues are Civil Code §3344, AB 602, the expired AB 730, the new digital‑replica law AB 2602, and CCPA/CPRA treatment of biometric/AI training data, plus newer AI‑labeling and deepfake bills.

Civil Code §3344 right of publicity (and digital likeness)

California’s statutory right of publicity (Cal. Civ. Code §3344) makes a person liable if they knowingly use another’s name, voice, signature, photograph, or likeness on products or for advertising or selling purposes without prior consent.
law.justia
​

Key points relevant to AI/deepfakes:

“Likeness” and “photograph” have been interpreted broadly in case law to include realistic drawings, avatars, and other depictions that evoke the person’s identity; courts have applied §3344 and the parallel common‑law right to things like celebrity look‑alike ads (e.g., White v. Samsung), video‑game avatars (Keller v. EA, No Doubt v. Activision), and other non‑photo depictions.

A realistic AI‑generated image or video that is “readily identifiable” as a person (for commercial use or advertising) fits comfortably within §3344, even if no original photograph was used, so long as the identity can be recognized and there is a commercial purpose.

Remedies under §3344 include actual damages and profits plus a statutory minimum (commonly understood in practice to be significant), as well as attorneys’ fees and injunctive relief; plaintiffs often also plead common‑law right of publicity and related torts such as defamation and intentional infliction of emotional distress.

For AI platforms: if AI outputs or marketing use a person’s image/voice to promote a product or service without consent, expect §3344 claims alongside privacy and “digital replica” claims.

Deepfake statutes: AB 602 and AB 730
AB 602 – sexually explicit deepfakes

AB 602 (effective 2020) created a specific civil cause of action for sexually explicit deepfakes.
dailyjournal
+1

Scope: covers “depicted individuals” who appear, as a result of digitization, to perform in sexually explicit material they did not actually perform in or whose depiction has been materially altered.
akingump
​

Liability: a person is liable if they (1) create and intentionally disclose sexually explicit material knowing or having reason to know the depicted person did not consent to creation or disclosure, or (2) intentionally disclose such material created by someone else knowing the depicted person did not consent.
akingump
​

Exemptions: no liability for disclosures in legal proceedings, for reporting unlawful activity, or for matters of legitimate public concern, political or newsworthy works, or otherwise constitutionally protected speech.
akingump
​

Remedies: plaintiffs can recover either (a) actual economic and noneconomic damages (including emotional distress) or (b) statutory damages of at least 1,500 dollars and up to 30,000 dollars, or up to 150,000 dollars if the act was committed with malice, plus punitive damages, attorneys’ fees, costs, and injunctive relief.
akingump
​

AB 602 sits on top of existing “revenge porn” statutes, including Penal Code 647(j)(4) and Civil Code 1708.85, which already cover nonconsensual distribution of explicit images but were not drafted for AI‑generated content; AB 602 explicitly closes that gap for synthetic pornography.
ridleydefense
+2

AB 730 – political deepfakes around elections (now expired)

AB 730 targeted politically deceptive deepfakes close to elections but sunset on January 1, 2023, and is no longer in force.
dwt
+2

Scope (while in force): prohibited malicious creation or distribution of “materially deceptive” audio or visual media about a candidate within 60 days of an election, where a reasonable person would form a “fundamentally different” impression than from the unaltered media.
jolt.law.harvard
​

Remedies: candidates could seek damages and injunctive relief, but broadcasters and sites paid to disseminate content had safe harbors if they provided clear disclosures that the media was manipulated.
news.slashdot
+2

Status for 2024–26: the sunset clause means AB 730 no longer applies, though newer 2024 bills (discussed below) address election‑related deepfakes in different ways.
dwt
+2

Platforms should not rely on AB 730’s specific safe harbors going forward, but its structure (narrow window, candidate‑focused, disclosure‑based defenses) is a useful template for internal policies and for predicting how new election‑deepfake bills may be designed.

AB 2602 (2024) – digital replicas and voice‑cloning consent

AB 2602, signed September 17, 2024, will be codified as Labor Code §927 and addresses “digital replicas” of performers in film, TV, music, and related entertainment.
proskauer
+4

Definition of “digital replica”

AB 2602 defines a “digital replica” as a computer‑generated, highly realistic electronic representation that is readily identifiable as an individual’s voice or visual likeness in a sound recording, image, audiovisual work, or transmission where the person did not actually perform or appear, or did, but the fundamental character of the performance or appearance is materially altered.
perkinscoie
+2

This definition directly fits high‑fidelity AI voice clones and photorealistic AI faces used in entertainment content.

Core consent/contract rules

For agreements for personal or professional services that provide for creation or use of a digital replica in performances fixed on or after January 1, 2025, AB 2602 makes certain contract provisions contrary to public policy and unconscionable if:
manatt
+3

The provision allows creation and use of a digital replica of the performer’s voice or likeness in place of work they would otherwise have performed in person.
proskauer
+2

The provision does not include a “reasonably specific description” of intended uses of the digital replica, or allows uses that fundamentally change the nature of the original performance beyond what the contract contemplates.
legiscan
+3

The provision authorizes use of the digital replica to train a generative AI system without appropriate specificity and consent.
legiscan
​

Consequences and timing:

Such provisions are deemed contrary to public policy and unconscionable; contracts relying on them are unenforceable as to new digital‑replica performances fixed on or after January 1, 2025.
perkinscoie
+3

The law applies retroactively: any party with existing contracts that include prohibited digital‑replica provisions must notify affected performers in writing by February 1, 2025, that those provisions are unenforceable.
babl
+1

Practically, AB 2602 functions as a consent regime for high‑fidelity AI voice and likeness in the entertainment sector: consent must be informed, specific as to use, and not buried in broad grants of rights.

Related law: AB 1836 and deceased performers

AB 1836, enacted alongside AB 2602, extends protections to digital replicas of deceased performers, strengthening estate rights and allowing heirs to sue for unauthorized use of a deceased personality’s voice or likeness in audiovisual or audio works, specifically targeting AI‑generated replicas, with minimum statutory damages.
babl
+2

For AI/voice‑cloning vendors working with performers, expect AB 2602 and AB 1836 to serve as baselines for contract structure, disclosure of AI training uses, and estate‑consent workflows.

CCPA/CPRA and AI face/voice/biometric data
Biometric and AI‑relevant data as “personal information”

Under the CCPA/CPRA, “personal information” is defined very broadly and explicitly includes “biometric information,” which in turn covers imagery of the face and voice recordings from which a template such as a faceprint or voiceprint can be extracted, as well as gait, keystroke patterns, and similar behavioral biometric data.
clarip
+5

Biometric information is treated as a category of personal information, and in many contexts as “sensitive personal information,” triggering heightened obligations.
casemine
+2

The definition specifically includes facial imagery and voice recordings used for identification, which clearly encompass training data and embeddings for facial recognition and voice‑clone models.
privacy.gtlaw
+4

Consumer rights affecting AI training and outputs

Because biometric data is personal information under CCPA/CPRA, the full set of consumer rights applies to face/voice data used for AI:
clarip
+2

Right to know/access: consumers can request categories and specific pieces of personal information collected, including biometric templates, although regulations prohibit disclosure of a consumer’s actual “unique biometric data” in access responses (you must disclose that you hold this category, not the raw template).
clarip
+1

Right to delete: subject to exceptions, businesses must delete personal information—including biometric templates and possibly derived embeddings—upon verifiable request.
jdsupra
+2

Right to opt‑out of “sale” or “sharing”: if biometric/AI training data is sold, shared for cross‑context behavioral advertising, or disclosed in a way that meets statutory thresholds, consumers must be able to opt‑out.
privacy.gtlaw
+2

Right to limit use of sensitive personal information: consumers can limit use and disclosure of sensitive data (including certain biometric information) to specific permissible purposes.
casemine
+1

Regulators have emphasized that AI model training is not a regulatory “black hole.” AB 1008, passed by the California Senate in August 2024, would revise the CCPA’s definition of “personal information” to explicitly include “abstract digital formats” such as AI systems that are capable of outputting personal information, clarifying that models trained on personal data themselves can be subject to access, deletion, and correction rights.
technologylaw.fkks
​

AB 1008 also clarifies that “publicly available information” does not include biometric information collected without the consumer’s knowledge (e.g., surreptitious facial‑recognition capture), closing a potential loophole.
technologylaw.fkks
​

(As of the cited source, AB 1008 was pending final gubernatorial action, so confirmation of its effective date should be checked when performing a real‑world compliance review. )
technologylaw.fkks
​

Security and breach exposure

The CCPA requires businesses to implement reasonable security procedures and practices to protect personal information, including biometric data.
clarip
​

Failure leading to a data breach exposing certain personal information can trigger statutory damages in private actions, and the exposure of biometric templates or identifiers (faceprints, voiceprints) is particularly high‑risk given their permanence.
clarip
​

New 2024–25 AI/deepfake and watermarking measures

In September 2024, the governor announced additional AI‑related bills aimed at deepfakes and AI‑generated content labeling:
gov.ca
​

One measure (described as SB 942) requires large generative AI companies to label AI‑generated content and provide an AI‑detection capability, moving toward mandatory watermarking and provenance tools.
gov.ca
​

Other contemporaneous bills (as referenced by law‑firm summaries) target deepfakes in elections and sexually explicit deepfakes, and expand digital‑replica protections, alongside AB 2602 and AB 1836.
manatt
+2

This emerging layer directly affects platforms and AI developers by imposing affirmative labeling and detection obligations, supplementing the more general tort and privacy frameworks.

Penalties and enforcement landscape
Deepfakes and digital replicas

AB 602 provides statutory damages (1,500–30,000 dollars per work, up to 150,000 dollars for malicious acts), plus punitive damages, attorneys’ fees, and injunctive relief.
akingump
​

Penal Code 647(j)(4) and related “revenge porn” statutes can support criminal charges for nonconsensual distribution, including AI deepfake pornography, when the statutory elements (intent to cause emotional distress, expectation of privacy, etc.) are met.
ridleydefense
+1

AB 2602/AB 1836 render certain contract provisions unconscionable and unenforceable; violations may not create standalone damages by themselves but underpin contract challenges, unfair‑competition (Bus. & Prof. Code §17200) claims, and union/agency enforcement in the labor context.
proskauer
+4

CCPA/CPRA

Under CCPA/CPRA as amended:

The California Attorney General and the California Privacy Protection Agency (CPPA) can bring enforcement actions, with per‑violation civil penalties (commonly understood to be up to 2,500 dollars per violation and 7,500 dollars for intentional violations or those involving minors).

Consumers have a limited private right of action for certain data breaches resulting from unreasonable security, with statutory damages per consumer per incident; this can be significant when biometric training data or model weights tied to personal information are exposed.
clarip
​

Elect