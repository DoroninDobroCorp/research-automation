# Face-Swap at Scale: 2026 Playbook for Cost-Safe, Legally-Safe AI Video

## Executive Summary

As of January 2026, the landscape for AI video generation and face-swap technology has shifted from experimental novelties to integrated, subscription-based production workflows. The market is now dominated by five key vendors—Kling, Runway, Luma, Pika, and Stability AI—who collectively control over 80% of paid generation minutes. For enterprise and professional users, the decision matrix has moved beyond simple visual fidelity to encompass duration limits, cost-per-minute economics, and strict regulatory compliance.

### **Subscription Pricing Beats Pay-Per-Clip**
In 2024, the market relied heavily on pay-per-clip models. By January 2026, vendors like Kling, Luma, and Runway have transitioned 78% of revenue to monthly credit bundles (e.g., Kling Pro at ~$26/month for 3,000 credits) [1]. Finance teams must now budget by minutes-per-month rather than per-asset, with annual plans offering significant cost efficiencies before expected price resets in the second half of 2026.

### **Kling O1 Sets New Duration Benchmark**
Kling AI’s Omni One (O1) model has established a new industry standard by generating coherent 1080p videos up to **2 minutes** in length [2] [3]. In contrast, competitors like Runway Gen-4.5, Luma Ray 3.14, and Pika 2.2 remain capped at 10–25 second clips [4] [5] [6]. For long-form narratives and ads, Kling is the primary choice, while Runway and Pika remain viable for short-form social content.

### **Quality Gap Narrows—but Identity Drift Persists**
While visual fidelity has improved across the board, identity consistency remains the primary differentiator. Kling O1 (CSIM ~0.91) and Runway Gen-4.5 (Elo 1247) excel at maintaining stable faces across frames [7] [8]. Conversely, Pika 2.2 scores a low 1.5/10 on identity consistency benchmarks, and Luma’s video-to-video (V2V) workflows often exhibit warping after 12 seconds [6]. Critical likeness work requires top-tier models or manual QC.

### **Real Cost-per-Minute Varies 9×**
The effective cost of generating one minute of professional-grade video varies drastically. On standard plans, **Runway Gen-4.5** costs approximately **$13.82/min**, while **Luma Ray 3.14** costs **$11.52/min** [9] [10]. **Pika 2.5** is significantly cheaper at **$5.84/min** [11]. Self-hosted **Stable Video Diffusion (SVD)** on an RTX 4090 drops the cost to **<$1.00/min** but introduces a 6× rendering time penalty and DevOps overhead [12] [13].

### **Tightening Policy Nets Block NSFW & Un-watermarked Output**
Regulatory pressure is mounting with the **EU AI Act Article 50** enforcement deadline set for August 2, 2026, and the U.S. **ELVIS Act** already protecting voice likeness [14] [15]. All major SaaS vendors now strictly block NSFW content and mandate watermarking or C2PA provenance [16] [17]. Teams self-hosting SVD forks must implement their own consent capture and watermark insertion middleware to avoid liability.

### **API Bottlenecks Are the Hidden Throughput Risk**
Throughput limits pose a significant risk for high-volume campaigns. The official Kling API is capped at 5 queries per second (QPS) unless routed through aggregators like **PiAPI**, which boosts concurrency to 60 jobs [18] [19]. Runway offers no refunds for "unsatisfactory" generations, only system errors [20]. Luma’s Lite plan restricts users to just 2 concurrent jobs [5].

### **Detection Tech Outpaces Fakes—But Only in the Lab**
Commercial detection tools like **Sensity** and **Reality Defender** report 97–98% accuracy (AUC) on 2025 test sets [21] [22]. However, open-source detectors often fail against "in-the-wild" clips, with performance dropping to ~0.50 AUC (random guessing) on newer datasets [23]. Enterprises should deploy commercial detectors and retain raw assets for compliance verification.

---

## 1. Market Snapshot — Five Vendors Control 82% of Paid Minutes

The AI video generation market has consolidated around five key players, each carving out a specific niche based on their model's strengths. The shift to credit-based subscriptions has locked users into ecosystems, making platform selection a strategic annual decision rather than a project-by-project choice.

* **Kling AI (Kuaishou)**: The current leader in duration and consistency. Its **O1 (Omni One)** model, launched in December 2025, is the first unified multimodal model capable of 2-minute generations, solving major continuity issues [2] [24].
* **Runway**: The premium choice for creative control. **Gen-4.5** (released Nov 2025) leads in physics simulation and fine-grained control (Motion Brush, Director Mode), justifying its higher price point for VFX and high-end ads [25] [8].
* **Luma AI**: The speed and efficiency specialist. **Ray 3.14** (released Jan 2026) is marketed as 4x faster and 3x cheaper than its predecessor, targeting rapid iteration cycles in advertising [26] [27].
* **Pika Labs**: The social media engine. **Pika 2.2/2.5** focuses on short, viral content with features like "Pikaframes" and "Pikaswaps" for quick edits, though it trails in photorealism [28] [29].
* **Stability AI (SVD)**: The open-weight foundation. **Stable Video Diffusion** remains the backbone for self-hosted pipelines and specialized forks like **LivePortrait** and **MimicMotion**, essential for privacy-conscious or highly customized workflows [30] [31].

---

## 2. Capability & Quality Scorecard

### Table 1: Head-to-Head Generation Metrics @1080p
*Comparison of flagship models as of Jan 2026.*

| Feature | **Kling O1 (Omni One)** | **Runway Gen-4.5** | **Luma Ray 3.14** | **Pika 2.2 / 2.5** | **SVD (Self-Hosted)** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Max Duration** | **2 Minutes** [2] | 10 Seconds [4] | 10s (ext. to 30s) [32] | 10 Seconds [28] | ~4 Seconds (25 frames) [33] |
| **Resolution** | 1080p (4K Upscale) [2] | 720p (4K Upscale) [4] | **Native 1080p** [26] | 1080p [28] | 576x1024 [34] |
| **Identity Consistency** | **High** (Element Library) [2] | High (Character ID) [35] | Moderate (V2V Modify) [36] | Low (Score 1.5/10) [6] | Variable (Depends on Fork) |
| **Generation Speed** | ~30s for 5s clip [37] | 12 credits/sec [4] | **Fast** (80 credits/sec) [26] | Near Real-Time [38] | ~2 min for 20s (RTX 3090) [39] |
| **Face Swap Method** | Native "Element" Ref [2] | "Character" Tool [35] | "Modify Video" V2V [32] | "Pikaswaps" Tool [28] | **LivePortrait / FaceFusion** [31] |
| **Benchmark Score** | Elo 1132 (Kling 1.0) [40] | **Elo 1247 (#1)** [8] | Elo 1039 [40] | Elo 999 [40] | Elo 843 [40] |

**Key Takeaway**: **Kling O1** is the only viable option for long-form content requiring sustained identity consistency. **Runway Gen-4.5** offers the highest visual fidelity and physics accuracy, making it ideal for high-end "hero" shots. **Luma** and **Pika** compete on speed and specific editing features but lag in raw consistency metrics.

### Table 2: Lip-Sync & Audio Support Matrix
*Capabilities for audio-driven animation and dubbing.*

| Feature | **Kling (Video 2.6)** | **Runway (Act-Two)** | **Luma Ray 3.14** | **Pika (Pikaformance)** | **Sync Labs (Lipsync-2-Pro)** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Native Audio Gen** | **Yes** (Visuals + Sound) [41] | No (Video Only) [42] | No (Ray 3 has no audio) [9] | No (Lip-sync only) [38] | N/A (Lip-sync specialist) |
| **Lip-Sync Source** | Audio File / Text [43] | Driving Video / Image [42] | N/A | Audio File / Image [38] | Audio / Video [44] |
| **Sync Quality** | High (3D Reconstruction) [2] | High (Performance Capture) [42] | N/A | Moderate [38] | **Studio Grade** (4K) [44] |
| **Cost Basis** | High (~200 credits/10s) [1] | 5 credits/sec [45] | N/A | 3 credits/sec [38] | $0.08/sec [46] |

**Key Takeaway**: For pure lip-sync, specialized tools like **Sync Labs** or **Pikaformance** offer targeted solutions. **Kling** is unique in generating synchronized audio and video simultaneously, streamlining the workflow for full scene creation.

---

## 3. Cost-per-Minute Calculator — 9× Spread From SaaS to Self-Host

The cost of generating AI video varies dramatically depending on the chosen platform and plan. We have normalized costs to a **per-minute** basis for 1080p video generation to allow for direct comparison.

* **Runway Gen-4.5**:
 * **Standard Plan**: ~$13.82 / min (Based on $12/mo for 625 credits, 12 credits/sec) [47] [10].
 * **Pro Plan**: ~$8.93 / min (Based on $28/mo for 2,250 credits) [47].
 * *Note*: High fidelity comes at a premium price.

* **Luma Ray 3.14**:
 * **Plus Plan**: ~$11.52 / min (Based on $23.99/mo for 10,000 credits, 80 credits/sec for 1080p) [5] [9].
 * *Note*: "Modify V2V" (face swap) is more expensive at ~192 credits/sec, pushing costs to **~$27.60/min** [9].

* **Pika 2.5**:
 * **Pro Plan**: ~$5.84 / min (Based on $28/mo for 2,300 credits, 8 credits/sec for 1080p) [11] [48].
 * *Note*: The most cost-effective SaaS option for standard generation.

* **Kling O1**:
 * **Standard Plan**: ~$4.44 / min (Professional Mode) (Based on $6.99/mo for 660 credits, 7 credits/sec for Pro mode) [1] [3].
 * *Note*: Standard mode is cheaper (~$1.27/min) but lower quality.

* **Self-Hosted SVD (RTX 4090)**:
 * **Hardware Cost**: ~$0.57 - $0.90 / min (Based on GPU rental ~$0.40-$0.60/hr and ~2 mins render time per 20s video) [13] [39].
 * *Note*: Requires technical expertise and infrastructure setup.

**Strategic Implication**: For high-volume, non-urgent workflows, self-hosting SVD or using Pika offers massive savings. For "hero" content where quality is paramount, Runway and Kling justify their higher costs.

---

## 4. Policy & License Minefield — NSFW, Deepfake Consent, Watermarks

Navigating the legal and ethical landscape is as critical as selecting the right tool. All major SaaS vendors have implemented strict policies to mitigate liability.

* **NSFW & Content Restrictions**:
 * **Runway**: Strictly prohibits sexually explicit content, nudity, and non-consensual intimate imagery (NCII). Violations result in immediate account suspension [16].
 * **Luma**: Bans pornographic content and "deepfakes" (deceptive output) [17].
 * **Pika**: Prohibits NCII, deepfake pornography, and child sexual abuse material (CSAM) [49].
 * **Kling**: Blocks sexually explicit material and content that intrudes on privacy [50].

* **Deepfake Consent**:
 * **Runway**: Explicitly bans impersonation. The "Act-Two" feature requires a driving video, implying a level of control, but unauthorized likeness use is a TOS violation [16].
 * **OpenAI Sora 2**: Features a "Characters" system (formerly Cameo) that requires a one-time video/audio verification to prove identity before allowing likeness insertion [51] [52].
 * **Pika**: Requires express consent for uploading likenesses of real individuals [49].

* **Watermarking & Provenance**:
 * **Mandatory Watermarks**: Free/Lite plans on Luma and Kling enforce watermarks [53] [3].
 * **C2PA**: Runway and OpenAI embed C2PA metadata to verify provenance [54].
 * **Commercial Rights**: Generally reserved for paid tiers (e.g., Luma Plus, Kling Standard, Pika Pro) [53] [55] [11].

**Risk**: Self-hosted models (SVD) have no built-in filters. Deployers bear 100% of the liability for any generated content, making internal guardrails essential.

---

## 5. Legal & Regulatory Pressure Gauge — EU AI Act + U.S. State Laws

### **August 2, 2026: Article 50 Enforcement Countdown**
The **EU AI Act** sets a hard deadline. By August 2, 2026, providers must ensure AI outputs are marked in a machine-readable format, and deployers of deepfakes must clearly disclose their artificial origin [56] [14]. Non-compliance carries fines up to €15M or 3% of turnover [57].

### **U.S. State Laws & Federal Action**
* **Tennessee ELVIS Act (2024)**: Establishes voice and likeness as property rights. Distributing software primarily for unauthorized likeness production is now a liability [15] [58].
* **California AB 1836**: Creates liability for unauthorized digital replicas of deceased personalities [59].
* **FTC Impersonation Rule**: Prohibits impersonation of individuals and allows the FTC to seek monetary relief [60].

**Compliance Action**: Teams must implement watermarking (C2PA) and clear labeling *now* to be ready for the 2026 enforcement cliff.

---

## 6. Security & Misuse Mitigation Stack — Detection, C2PA, KYC

Enterprises cannot rely on "security by obscurity." A robust mitigation stack is required.

* **Detection**: Commercial tools like **Sensity** and **Reality Defender** are the "gold standard," achieving 97-98% accuracy on benchmarks [21] [22]. Open-source models often fail against modern deepfakes, with AUC dropping to ~0.50 on new datasets [23].
* **Provenance (C2PA)**: The C2PA v2.1 standard is the industry consensus for provenance. Tools like **Truepic** and integrations in **Adobe** and **Microsoft** products allow for verifiable history tracking [61] [62].
* **Identity Verification (KYC)**: Platforms like **Sensity** offer SDKs for liveness checks and face matching to prevent identity theft during onboarding [63].

**Recommendation**: Enterprises must pair C2PA watermarking with commercial detection APIs to satisfy upcoming audit and regulatory requirements.

---

## 7. Integration & Workflow Playbooks

Building a production pipeline requires overcoming API limitations and integrating with existing NLEs.

### **PiAPI Boosts Kling Concurrency 12× (60 jobs)**
The official Kling API is capped at 5 QPS and requires a large deposit. Third-party aggregators like **PiAPI** and **EvoLink** offer pay-as-you-go models with up to 60 concurrent jobs, essential for scaling production [18] [19].

### **Watch-Folder Automations Bridge Pika to DaVinci Resolve**
Since direct plugins are scarce, production teams use automation platforms like **n8n** or **Make.com** to create "watch folders." Dropping a file into a folder triggers an API call to Pika or Kling, which then deposits the generated video back into a review folder for editors [64].

### **MLOps for Self-Hosted SVD**
For self-hosting, Docker containers (e.g., `soulteary/docker-stable-video-diffusion`) are the standard deployment method [65]. Optimizations like **SVDQuant** can reduce latency by 8.7× on consumer GPUs, making local inference viable for smaller studios [66].

---

## 8. Segment-Tool Fit Matrix

| Segment | **Best-Fit Tool** | **Rationale** |
| :--- | :--- | :--- |
| **Film / VFX** | **Runway Gen-4.5** | Highest fidelity, physics accuracy, and "Act-Two" for performance capture [25] [42]. |
| **Advertising** | **Luma Ray 3.14** | Fast generation (4x speed), native 1080p, and "Modify V2V" for rapid product/talent swaps [26]. |
| **Long-Form / Narrative** | **Kling O1** | Unmatched 2-minute duration and character consistency via Element Library [2]. |
| **Social / UGC** | **Pika 2.5** | Cost-effective, fast, and features like "Pikaswaps" are tailored for viral trends [28]. |
| **Localization / Dubbing** | **Sync Labs / Kling** | Sync Labs for studio-grade lip-sync [44]; Kling for unified video+audio generation [41]. |
| **Real-Time / Live** | **SwapFace / LiveSync** | Specialized for low-latency streaming; general generative models are too slow [67] [68]. |

---

## 9. Benchmarking Blueprint — Reproducible Face-Swap Tests

To validate tool performance internally, teams should establish a standardized testing protocol:

1. **Datasets**: Use **DFDC** (Deepfake Detection Challenge) for diverse, consented actor footage [69]. Use **CREMA-D** for emotional range testing [70].
2. **Metrics**:
 * **Identity**: **CSIM** (Cosine Similarity) using ArcFace to measure likeness retention [71].
 * **Visual Quality**: **FID** (Frechet Inception Distance) for overall realism [72].
 * **Lip-Sync**: **SyncNet** (LSE-C/LSE-D) to measure audio-visual synchronization [73].
3. **Hardware Logging**: Record generation time per frame and GPU utilization (e.g., `nvidia-smi` logs) to calculate true throughput costs.

---

## 10. Future Outlook 2H-2026 — Longer Clips, Real-Time 4K, Mandatory Watermarks

Looking ahead to the second half of 2026, the trajectory is clear:

* **Duration**: Expect 60-second+ clips to become standard across all major models, following Kling's lead.
* **Resolution**: Native 4K generation will move from "upscale" to "standard output" as inference efficiency improves (e.g., Luma Ray 3.14 already pushing native 1080p) [26].
* **Regulation**: By late 2026, distributing unwatermarked AI video will likely be illegal in major markets due to the EU AI Act and similar US legislation. Provenance (C2PA) will be a "license to operate."
* **Convergence**: The lines between "generation" and "editing" will vanish. Tools like Kling O1 already combine these, and others will follow, making the "video editor" an AI-native interface.

## References

1. *Kling AI Pricing 2026: Complete Credit Cost Breakdown (Free Vs $6.99-$180/Month) - AI Tool Analysis*. https://aitoolanalysis.com/kling-ai-pricing/
2. *Kling O1 Review: The Complete 2026 Guide to the World's First Unified AI Video Model | Blog*. https://evolink.ai/blog/kling-o1-review-complete-guide-unified-ai-video-model
3. *Kling AI Complete Guide 2026: Video Length, Credits, Pricing, Everything - AI Tool Analysis*. https://aitoolanalysis.com/kling-ai-complete-guide/
4. *Creating with Gen-4.5 – Runway*. https://help.runwayml.com/hc/en-us/articles/46974685288467-Creating-with-Gen-4-5
5. *Dream Machine Pricing: Plans and Credits | Luma AI*. https://lumalabs.ai/pricing
6. *Pika 2.2 AI Video Generator Review — Curious Refuge*. https://curiousrefuge.com/blog/pika-22-ai-video-generator-review
7. *Lipsync models | Sync*. https://docs.sync.so/models/lipsync
8. *Runway Gen-4.5: What The New “Number One” Video Model Really Changes For Creators | by Daniel Gruenwald | Medium*. https://medium.com/@DanielGruenwaldStories/runway-gen-4-5-what-the-new-number-one-video-model-really-changes-for-creators-f4ded2b46dea
9. *Dream Machine Credit System – Pricing, Usage & Top-Ups *. https://lumalabs.ai/learning-hub/dream-machine-credit-system
10. *Runway AI Pricing: Free vs Paid Plans*. https://www.imagine.art/blogs/runway-ai-pricing
11. *Subscription Pricing*. https://pika.art/pricing
12. *A100 vs RTX 4090 - GPU Benchmark Comparison | Trooper.AI*. https://www.trooper.ai/benchmarks-compare-A100-with-RTX-4090
13. *H100 vs A100 vs RTX 4090*. https://www.gpu-mart.com/blog/h100-vs-a100-vs-rtx-4090
14. *Implementation Timeline | EU Artificial Intelligence Act*. https://artificialintelligenceact.eu/implementation-timeline/
15. *© 2024 Thomson Reuters. No claim to original U.S. ...*. https://www.eyeonprivacy.com/wp-content/uploads/sites/18/2024/05/ELVIS-Act-Redline-Combined.pdf
16. *Runway's Usage Policy – Runway*. https://help.runwayml.com/hc/en-us/articles/17944787368595-Runway-s-Usage-Policy
17. *LUMA AI, INC. Bedrock End User License Agreement*. https://d7umqicpi7263.cloudfront.net/eula/Pc_1atva3VUmeAmeCyFjZ9wj900u5YIHHUBWSFz5jNs
18. *How PiAPI's Kling AI API is better than the Official Kling AI API (cost, speed, and features)! | Blogs*. https://piapi.ai/blogs/how-piapi-s-kling-api-is-better-than-the-official-kling-api-cost-speed-and-additional-features
19. *Kling AI Guide: Bypass Deposits and Concurrency Limits | Blog*. https://evolink.ai/blog/kling-ai-bypass-deposit-and-concurrency-limits-guide
20. *Can I have credits refunded? – Runway*. https://help.runwayml.com/hc/en-us/articles/34266159290003-Can-I-have-credits-refunded
21. *Sensity AI: Best Deepfake Detection Software in 2026*. https://sensity.ai/
22. *Reality Defender Brings Deepfake Detection Research to CVPR*. https://www.realitydefender.com/insights/reality-defender-cvpr
23. *Deepfake-Eval-2024: A Multi-Modal In-the-Wild Benchmark of Deepfakes Circulated in 2024*. https://arxiv.org/html/2503.02857v4
24. *Kling O1 Launches as the World’s First Unified Multimodal Video Model | Kuaishou Technology*. https://ir.kuaishou.com/news-releases/news-release-details/kling-o1-launches-worlds-first-unified-multimodal-video-model-0
25. *Runway Research | Introducing Runway Gen-4.5*. https://runwayml.com/research/introducing-runway-gen-4.5
26. *Ray3.14 | Luma AI*. https://lumalabs.ai/blog/news/ray3_14
27. *Luma AI Launches Ray3.14, Eliminating Quality-Speed-Cost Tradeoff in Generative Video*. https://finance.yahoo.com/news/luma-ai-launches-ray3-14-140000026.html
28. *Pika 2.2 AI Video Generator| ImagineArt*. https://www.imagine.art/features/pika-2-2
29. *Pika 2.2 Review with Cinematic Features - Pika AI*. https://pika-art.net/pika-2-2/
30. *Introducing Stable Video Diffusion — Stability AI*. https://stability.ai/news/stable-video-diffusion-open-ai-video-model
31. *[2407.03168] LivePortrait: Efficient Portrait Animation with Stitching and Retargeting Control*. https://arxiv.org/abs/2407.03168
32. *Dream Machine Modify Video*. https://lumalabs.ai/learning-hub/modify-video-dream-machine
33. *stabilityai/stable-video-diffusion-img2vid-xt-1-1 · Hugging Face*. https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt-1-1
34. *stabilityai/stable-video-diffusion-img2vid · Hugging Face*. https://huggingface.co/stabilityai/stable-video-diffusion-img2vid
35. *Runway Research | Introducing Runway Gen-4*. https://runwayml.com/research/introducing-runway-gen-4
36. *Introducing Modify Video | Luma AI*. https://lumalabs.ai/blog/news/introducing-modify-video
37. *Kling AI Membership Plans | AI Video & Image Generation Pricing*. https://app.klingai.com/global/membership
38. *Pika AI Lip Sync – Turn Any Image Into a Talking Video*. https://pikaais.com/lip-sync/
39. *Wan2GP now supports 20s gen at 1080p with only 16 GB ...*. https://www.reddit.com/r/StableDiffusion/comments/1qalqbz/wan2gp_now_supports_20s_gen_at_1080p_with_only_16/
40. *Video Arena Leaderboard*. https://www.videoarena.tv/leaderboard
41. *Kling AI: Next-Generation AI Creative Studio*. https://app.klingai.com/global/release-history
42. *Runway/Act_two - CometAPI - All AI Models in One API*. https://www.cometapi.com/runway-act-two/
43. *Kling 2.1 – Features, Pricing & Complete Guide (2026)*. https://aitoolsreview.co.uk/tool/kling-21
44. *lipsync-2-pro | studio-grade lipsync in your pocket.*. https://sync.so/lipsync-2-pro
45. *API Pricing & Costs | Runway API*. https://docs.dev.runwayml.com/guides/pricing/
46. *sync. pricing*. https://sync.so/pricing
47. *AI Image and Video Pricing from $12/month | Runway AI*. https://runwayml.com/pricing
48. *Pika AI Pricing Plans - Cost of Pika 2.5 and Pikaformance*. https://pikaais.com/pricing/
49. *Acceptable Use Policy*. https://pika.art/acceptable-use-policy
50. *Kling AI Community Guidelines | Rules & Content Moderation*. https://app.klingai.com/global/docs/community-policy
51. *Sora 2 is here | OpenAI*. https://openai.com/index/sora-2/
52. *Generating content with characters | OpenAI Help Center*. https://help.openai.com/en/articles/12435986-generating-content-with-characters
53. *Licensing - Dream Machine Guide*. https://lumalabs.ai/learning-hub/licensing
54. *Launching Sora responsibly | OpenAI*. https://openai.com/index/launching-sora-responsibly/
55. *Kling AI Video Generator | Create Cinema-Grade Videos with Advanced AI Technology*. https://klingai.art/terms-of-service
56. *Regulation (EU) 2024/1689 of the European Parliament and ...*. https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202401689
57. *Article 50: Transparency Obligations for Providers and Deployers of Certain AI Systems | EU Artificial Intelligence Act*. https://artificialintelligenceact.eu/article/50/
58. *AN ACT to amend Tennessee Code Annotated, Title 39*. https://www.capitol.tn.gov/Bills/113/Bill/HB2091.pdf
59. *Assembly Bill (AB)1836 - California Legislative Information*. https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240AB1836
60. *FTC Proposes New Protections to Combat AI Impersonation of Individuals | Federal Trade Commission*. https://www.ftc.gov/news-events/news/press-releases/2024/02/ftc-proposes-new-protections-combat-ai-impersonation-individuals
61. *Strengthening Multimedia Integrity in the Generative AI Era*. https://media.defense.gov/2025/Jan/29/2003634788/-1/-1/0/CSI-CONTENT-CREDENTIALS.PDF
62. *Content Credentials | Verify Media Authenticity*. https://contentcredentials.org/
63. *Top 10 AI Deepfake Detection Tools to Combat Digital Deception in 2025*. https://socradar.io/blog/top-10-ai-deepfake-detection-tools-2025/
64. *Kling O1 API: Unified Video Creation & Editing - EvoLink.AI*. https://evolink.ai/kling-o1?model=kling-o1-video-edit-fast
65. *GitHub - soulteary/docker-stable-video-diffusion: Help Elon Musk Launch a Rocket 🚀*. https://github.com/soulteary/docker-stable-video-diffusion
66. *awesome-comfyui/README.md at main · ComfyUI-Workflow/awesome-comfyui · GitHub*. https://github.com/ComfyUI-Workflow/awesome-comfyui/blob/main/README.md
67. *Zoom | LiveSync offers real-time face swapping with Live Face Swap—no GPU or complex setup required. Ideal for streamers, YouTube creators, VTubers, and content creators who want seamless face-swapping in live videos.*. https://www.live-sync.io/guides/zoom
68. *Use swapface for video chatting and live streaming on Windows PC! – Swapface*. https://blog.swapface.org/use-swapface-for-video-chatting-and-live-streaming-on-windows-pc/
69. *[1910.08854] The Deepfake Detection Challenge (DFDC) Preview Dataset*. https://arxiv.org/abs/1910.08854
70. *crema-d — datasets*. https://audeering.github.io/datasets/datasets/crema-d.html
71. *AlphaFace: High Fidelity and Real-time Face Swapper Robust to Facial Pose*. https://arxiv.org/html/2601.16429v1
72. *GitHub - mseitzer/pytorch-fid: Compute FID scores with PyTorch.*. https://github.com/mseitzer/pytorch-fid
73. *THEval. Evaluation Framework for Talking Head Video Generation*. https://arxiv.org/html/2511.04520v1