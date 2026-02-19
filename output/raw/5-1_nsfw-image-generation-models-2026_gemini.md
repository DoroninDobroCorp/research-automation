Technical Analysis of Generative AI Architectures for Adult Content Production (January 2026)
1. Introduction: The Bifurcation of the Generative Landscape
As of January 2026, the domain of generative artificial intelligence for adult (NSFW) content production has undergone a fundamental architectural schism. The era of monolithic dominance—characterized by the near-universal adoption of Stability AI’s Stable Diffusion 1.5 and subsequently Stable Diffusion XL (SDXL) throughout 2023 and 2024—has formally concluded. In its place, a complex, multi-polar ecosystem has emerged, defined by three competing architectural paradigms: the established Latent Diffusion Models (LDMs), the ascendant Rectified Flow Transformers, and the experimental integration of massive multimodal text encoders.
This fragmentation is driven by a divergence in user requirements. On one vector, there is an insatiable demand for hyper-fidelity and photorealism, pushed forward by Black Forest Labs’ Flux architecture. This vector prioritizes anatomical correctness, skin texture simulation, and complex lighting, often at the cost of computational intensity. On the opposing vector lies the demand for extreme stylization, concept density, and high-throughput efficiency—segments currently dominated by highly fine-tuned SDXL derivatives like Pony Diffusion V6 and the emergent Flux.2 [klein] distilled models.
The implications for commercial deployment are profound. The "prompt and pray" methodologies of early generative AI have been replaced by sophisticated pipelines requiring precise control over character identity and scene composition. Workflows now necessitate "20% variation" consistency—a technical threshold where an image can be altered or swapped to fit a new context while retaining 80% of its original identity and structural integrity.
This report provides an exhaustive technical and commercial analysis of the primary models defining this landscape in early 2026: SDXL (specifically Pony Diffusion V6), Flux.1 and the newly released Flux.2 [klein], Pony Diffusion V7 (AuraFlow), and Stable Diffusion 3.5. The analysis is grounded in performance benchmarks on NVIDIA A100 hardware, legal scrutiny of licensing terms, and an evaluation of the tooling ecosystems (ControlNet, IP-Adapter) that render these models viable for production.
________________
2. The Legacy Incumbent: SDXL and the Pony Ecosystem
Despite the rapid pace of innovation in AI architectures, Stable Diffusion XL (SDXL) remains a colossus in the NSFW sector as of January 2026. Its continued relevance is not due to superior base architecture compared to newer Transformers, but rather due to the "ecosystem inertia" of community fine-tunes, specifically the Pony Diffusion lineage.
2.1 Architectural Foundation and Obsolescence
SDXL, released in mid-2023, is a Latent Diffusion Model utilizing a dual text-encoder system (OpenCLIP ViT-bigG/14 and CLIP ViT-L/14) coupled with a UNet backbone. By 2026 standards, the UNet architecture is showing signs of age, particularly in its handling of complex prompt adherence and spatial relationships compared to Diffusion Transformers (DiTs).
However, the sheer volume of training hours pumped into SDXL fine-tunes has created a "moat" of concept knowledge. The model’s relatively smaller parameter count (approx. 2.6B UNet + text encoders) compared to Flux (12B+) or AuraFlow (7B) allows for extremely efficient inference, which is a critical factor for high-volume commercial services.
2.2 Pony Diffusion V6 XL: The Community Standard
Pony Diffusion V6 XL, developed by PurpleSmartAI, stands as the apotheosis of the SDXL era. It is not merely a fine-tune but a comprehensive re-alignment of the model's latent space, achieved through training on millions of aesthetically ranked images with a heavy bias toward Danbooru-style tagging.1
2.2.1 Quality for Face and Character Generation
Pony V6 excels in stylized fidelity. It is the undisputed market leader for anime, cartoon, and 2.5D semi-realistic generation. Its mastery of specific character designs—ranging from popular media figures to obscure OCs—is unmatched by any base model.
* Face Generation: For stylized content, Pony V6 produces crisp, expressive faces. It allows for extreme expression control (e.g., distinctive anime tropes like "ahegao" or exaggerated grimaces) that are often filtered out of safety-aligned corporate models.
* Photorealism Limitations: When pushed toward photorealism, Pony V6 often exhibits a characteristic "plasticity." Skin textures can appear airbrushed or waxy. While numerous "Realism" LoRAs exist to counteract this, they often conflict with the model's core weights, leading to uncanny valley artifacts where realistic textures are applied to stylized underlying geometry.2
2.2.2 The "Score" Prompting Meta
Pony V6 introduced a unique prompting paradigm that remains dominant in 2026. Unlike natural language models, Pony relies on "score tags" to direct aesthetic quality:
score_9, score_8_up, score_7_up, rating_explicit,...
This "score stacking" method provides granular control over the aesthetic output but creates a high barrier to entry for users accustomed to natural language prompting (e.g., ChatGPT-style descriptions).3
2.3 Ecosystem and Tooling Support
The greatest strength of SDXL in 2026 is its mature tooling.
* ControlNet: A full suite of mature ControlNets exists for SDXL, including OpenPose, Canny, Depth, Lineart, and Scribble. These are essential for the "20% variation" workflows, allowing creators to lock a pose while changing the character or lighting.4
* IP-Adapter: The IP-Adapter FaceID and IP-Adapter Plus models for SDXL are highly refined. They allow for "zero-shot" face swapping and style transfer with high fidelity, a capability that newer models are still struggling to replicate with equal versatility.5
* LoRA Library: There are over 100,000 LoRAs available for SDXL, covering virtually every conceivable art style, character, and NSFW concept. This vast library creates a network effect that keeps users locked into the SDXL ecosystem.
2.4 Commercial Licensing and Legal Status
The licensing of Pony Diffusion V6 is a critical consideration for commercial entities.
* Base License: SDXL is OpenRAIL++.
* Pony V6 License: This model utilizes a custom license. It permits commercial use for individual creators (e.g., Patreon artists) but imposes restrictions on "Inference Services" and entities with greater than $1 million in annual revenue. Large-scale commercial deployment requires a negotiated license with PurpleSmartAI.1
2.5 Benchmarks (A100)
On NVIDIA A100 (80GB) hardware, SDXL remains highly performant due to extensive optimization libraries like TensorRT and Xformers.
* Throughput: Using Turbo or Lightning schedulers (4-8 steps), SDXL can achieve upwards of 50-60 images per minute per GPU in batch sizes of 4-8.
* VRAM: The model comfortably fits in <8GB of VRAM for inference, meaning an A100 can run multiple concurrent instances, maximizing ROI for server operators.6
________________
3. The Photorealism Frontier: Flux.1 and the Rectified Flow Revolution
In mid-2025, Black Forest Labs (BFL)—founded by the original creators of Stable Diffusion—disrupted the market with Flux.1. This model marked a departure from standard Latent Diffusion, utilizing a Rectified Flow Transformer architecture. By January 2026, Flux.1 has established itself as the new standard for photorealistic NSFW content.7
3.1 Architectural Shift: Transformers and Flow Matching
Flux utilizes a Multimodal Diffusion Transformer (MMDiT). Unlike the UNet used in SDXL, the MMDiT processes text and image tokens in a unified attention space. This allows for significantly superior prompt adherence and spatial reasoning. The "Rectified Flow" training objective simplifies the path from noise to data, allowing the model to generate high-quality images in fewer steps (typically 20–30 for Dev, 4 for Schnell) without the distillation artifacts seen in SDXL Turbo.8
3.2 Model Variants: Dev vs. Schnell
* Flux.1 [dev]: The open-weight (but restricted license) variant. It uses 12 billion parameters and a massive T5xxl text encoder. It produces the highest fidelity images in the open ecosystem, capable of rendering distinct skin pores, vellus hair, and complex lighting interactions that SDXL cannot match.
* Flux.1 [schnell]: A distilled 4-step version. While significantly faster, it suffers from "distillation collapse," where fine details and texture variety are smoothed out. It is released under the permissive Apache 2.0 license.
3.3 The "Chroma" Solution: Uncensored Photorealism
The base Flux.1 models were released with safety alignment. However, the community quickly produced fine-tunes to unlock NSFW capabilities. Chroma, a fine-tune based on Flux architecture, has emerged as a leader in this space.9
* Purpose: Chroma aims to restore the anatomical knowledge suppressed in the base model while maintaining Flux’s photorealistic texture.
* License: Because it is often based on the Apache 2.0 Schnell architecture or de-distilled Dev weights, Chroma offers a legally safer route for some commercial entities compared to the restrictive Dev license.10
* Quality: Chroma bridges the gap between the plastic skin of Pony V6 and the hyper-realism of Flux Dev, making it the preferred model for "realistic" NSFW content production in 2026.
3.4 Face Generation and Tooling
* Face Quality: Flux.1 [dev] is currently the benchmark for photorealistic faces. It avoids the "same face syndrome" often seen in SDXL by utilizing the T5 text encoder’s vast semantic knowledge.
* ControlNet: As of Jan 2026, the ControlNet ecosystem for Flux is growing but immature. X-Labs and InstantX have released Canny and Depth ControlNets, but they lack the robustness of the SDXL suite. A dedicated "OpenPose" for Flux is available but can be computationally expensive.11
* IP-Adapter: The Flux IP-Adapter has been released, enabling face transfer. However, benchmarks suggest it is heavier on VRAM and slightly less "sticky" regarding identity preservation compared to the SDXL equivalents.12
3.5 Commercial Constraints
* Flux.1 [dev] License: Non-Commercial. Using this model for a paid generation service is a violation of terms. BFL aggressively protects this license.
* Flux.1 [schnell] License: Apache 2.0. This allows for unrestricted commercial use, modification, and redistribution. Consequently, most commercial "Flux" services in 2026 are actually running fine-tuned versions of Schnell or Chroma.7
________________
4. The Speed Demon: Flux.2 [klein] and Unified Editing
On January 15, 2026, Black Forest Labs released Flux.2 [klein], a model family designed to address the high computational cost of Flux.1. The "Klein" (German for "small") series is a direct response to the market's need for high-quality, low-latency generation.8
4.1 Technical Specifications
Flux.2 [klein] is available in two parameter counts, each with a specific licensing structure:
* 4B Model: 4 Billion parameters. Licensed under Apache 2.0. Optimized for consumer hardware and edge deployment.
* 9B Model: 9 Billion parameters. Licensed under Flux Non-Commercial. Designed to balance speed with the high fidelity of the original Flux.1 Dev.16
Both models utilize a step-distilled flow matching technique, allowing them to generate final images in just 4 steps.
4.2 The "In-Context" Editing Breakthrough
The most significant innovation in Flux.2 [klein] is its unified generation and editing architecture. Unlike previous models that required separate pipelines (e.g., generating an image, then passing it to an inpainting model), Flux.2 supports in-context editing.
* Mechanism: The model accepts both text prompts and reference images simultaneously in the latent space. Users can provide a reference image and a prompt like "change the background to a beach," and the model performs the edit in a single inference pass.17
* Relevance to Face Swap: This architecture natively supports face swapping without external adapters like ReActor. By passing a source face as a reference and prompting for the target scene, Flux.2 performs a "latent swap," blending the identity with the target lighting more naturally than pixel-based methods.18
4.3 Benchmarks (A100)
Flux.2 [klein] 4B is currently the fastest high-quality model available on the market.
* Speed: On an A100, the 4B model can generate images in ~0.2 seconds per image (batch 1). In high-throughput batching, it can theoretically exceed 100 images per minute, essentially enabling real-time video generation frame-by-frame.16
* VRAM: The 4B model requires only ~8-12GB of VRAM, allowing for massive parallelization on an 80GB A100.19
4.4 Limitations
* Over-Sharpening: Early analysis indicates that the 9B model can suffer from "over-sharpening" artifacts, a common side-effect of aggressive distillation.20
* NSFW Filtering: The official weights for Flux.2 are filtered. While the architecture is capable, commercial users must rely on "de-distilled" community weights or fine-tunes to reliably generate adult content, adding a step of friction to deployment.21
________________
5. The Pivot: Pony Diffusion V7 and AuraFlow
In late 2025, the developer of Pony Diffusion announced a controversial pivot: Version 7 would not be based on SDXL, nor Flux, but on AuraFlow.22
5.1 AuraFlow Architecture
AuraFlow is an open-source Flow Matching model similar to Flux but developed by FAL.ai and the open-source community. It features 7 Billion parameters and uses the Aura architecture.22
* Resolution: It supports native generation up to 1536x1536 pixels, significantly higher than the native 1024x1024 of SDXL or Flux.23
* Text Encoder: Like Flux, it utilizes a T5-based text encoder, granting it superior natural language understanding.
5.2 Performance vs. Pony V6
* Prompting Shift: Pony V7 abandons the "score tag" meta in favor of natural language. Users must now describe scenes ("An anime girl standing in a kitchen") rather than stacking tags ("score_9, 1girl, kitchen"). This has caused friction with the established user base.22
* Spatial Coherence: V7 demonstrates significantly better spatial reasoning (e.g., "girl on the left, boy on the right") compared to the "concept bleeding" often seen in SDXL.
* Tooling Vacuum: As of Jan 2026, AuraFlow lacks the robust ControlNet ecosystem of SDXL. There are no mature OpenPose or Depth adapters for AuraFlow, severely limiting its utility for precise pose-control workflows.24
5.3 License
Pony License: The V7 model retains the restrictive Pony license structure. Commercial use is allowed for creators but restricted for "inference services" or large companies (>$1M revenue), unless they use the official partner API (FAL.ai).22
________________
6. The Corporate Contender: Stable Diffusion 3.5
Stability AI’s release of Stable Diffusion 3.5 (SD3.5) in late 2025 was an attempt to regain market share after the disastrous SD3 Medium release.
6.1 Model Variants
* SD3.5 Large (8B): The flagship model. It offers excellent prompt adherence and anatomy.
* SD3.5 Large Turbo: A distilled version for faster inference.
* SD3.5 Medium (2.5B): A highly efficient model designed to run on consumer hardware.25
6.2 Suitability for Adult Content
SD3.5 is "safety aligned" by default. While it is not "lobotomized" like SD2.0, it resists generating explicit content without "jailbreak" prompting or fine-tuning.
* Community Reception: The NSFW community has largely ignored SD3.5 in favor of Flux and Pony. There are fewer fine-tunes and LoRAs for SD3.5 compared to the other architectures.
* Tooling: Stability AI released official ControlNets (Blur, Canny, Depth) for SD3.5, giving it a theoretical advantage in structured workflows over AuraFlow/Pony V7.26
6.3 License
Stability AI Community License: This is a key differentiator. It allows for free commercial use for entities with under $1M in annual revenue. This is significantly more permissive than the Flux [dev] license (Non-Commercial) but less permissive than Apache 2.0 (Flux Klein 4B).27
________________
7. Comparative Analysis: Hardware, Licensing, and Capabilities
The following tables summarize the critical metrics for decision-makers evaluating these models for commercial deployment.
7.1 General Capabilities Matrix
Feature
	SDXL (Pony V6)
	Flux.1 [dev] / Chroma
	Flux.2 [klein] 4B
	Pony V7 (AuraFlow)
	SD 3.5 Large
	Architecture
	Latent Diffusion (UNet)
	Flow Transformer (MMDiT)
	Flow Transformer (MMDiT)
	Flow Transformer (Aura)
	MM-DiT
	Native Resolution
	1024x1024
	1024x1024
	1024x1024
	1536x1536
	1024x1024
	Face Quality
	High (Stylized)
	Best (Photoreal)
	Good
	High (Versatile)
	Very Good
	Prompting Style
	Tag-based (Score_9)
	Natural Language (T5)
	Natural Language
	Natural Language
	Natural Language
	NSFW Native?
	Yes (Native)
	Via Fine-tune (Chroma)
	Via Fine-tune
	Yes (Native)
	Moderate
	ControlNet Support
	Mature (Full Suite)
	Partial (Canny/Depth)
	Native Editing (Latent)
	Immature
	Official Suite
	7.2 A100 Benchmarks (Performance & Efficiency)
Estimates based on batch processing on NVIDIA A100 80GB.
Model
	Generation Speed (Batch 1)
	Est. Throughput (Img/Min)
	VRAM (Inference)
	Commercial License
	SDXL Turbo (Pony)
	~0.8s
	~60+
	Low (8GB)
	Pony (Restrictive >$1M)
	Flux.1 [dev]
	~1.5s
	~20
	High (16-24GB)
	Non-Commercial
	Flux.1 [schnell]
	~0.4s
	~50
	High (16GB)
	Apache 2.0
	Flux.2 [klein] 4B
	~0.2s
	~100+
	Very Low (8GB)
	Apache 2.0
	Pony V7
	~1.0s
	~30
	Medium (12GB)
	Pony (Restrictive >$1M)
	SD 3.5 Large
	~1.2s
	~25
	Medium (16GB)
	Community (<$1M Free)
	7.3 Tooling and Ecosystem Maturity
Feature
	SDXL
	Flux
	AuraFlow (Pony V7)
	SD 3.5
	LoRA Library
	Massive (>100k)
	Growing Rapidly
	Emerging
	Moderate
	Face Swap (ReActor)
	Native/Stable
	Via Adapter (PulID)
	Native (In-Context)
	Moderate
	IP-Adapter
	High Fidelity
	Moderate Fidelity
	Low Availability
	Low Availability
	Video Consistency
	Moderate (AnimateDiff)
	High (Hunyuan/Flux)
	Unknown
	Moderate
	________________
8. Practical Workflows: Face Swap and Consistency ("The 20% Change")
A critical requirement for modern NSFW content pipelines is the ability to generate variations of a character or swap faces while maintaining identity consistency. The "20% change" metric refers to the Denoising Strength (0.2) used in Image-to-Image workflows. This is the technical threshold where the model has enough freedom to blend lighting and texture (healing the image) without hallucinating new facial features that destroy identity.
8.1 The "20% Variation" Logic Explained
* 0.0 - 0.15 Denoise: The model changes almost nothing. Pasted faces (from tools like ReActor) look "stuck on" with sharp seams and mismatched lighting.
* 0.20 - 0.30 Denoise ("The Sweet Spot"): The model hallucinates skin texture, subsurface scattering, and lighting interactions on top of the provided pixel data. It "heals" the image, making the face look native to the scene.
* >0.40 Denoise: The model begins to override the structural geometry of the face, leading to identity drift (the character looks like a different person).
8.2 Workflow A: The Photorealist (Flux + PulID)
Target: High-end static imagery where skin texture must be perfect.
Tools: ComfyUI, Flux.1 [dev] (or Chroma), PulID (Identity Adapter).
1. Generation: Generate the target NSFW scene using Flux.1.
2. Identity Injection: Use the PulID node. Load the reference face image. Set the weight to 0.8.
3. Differential Diffusion: Use a mask on the face area. Apply Differential Diffusion with a denoising strength of 0.25 (25%).
   * Mechanism: Differential diffusion allows the model to change the high-frequency details (texture, lighting) while ignoring the low-frequency details (structure, identity) within the masked area.
4. Result: A swapped face that retains the reference identity but perfectly matches the dramatic lighting of the generated scene.
8.3 Workflow B: The Speed Specialist (Flux.2 In-Context Editing)
Target: High-volume generation or video frames where speed is critical.
Tools: Flux.2 [klein] 4B.
1. Input: Two images—Image A (Reference Face) and Image B (Target Body/Scene).
2. Prompt: "Transfer the identity of the person in Image A to the pose in Image B. Cinematic lighting."
3. Process: Flux.2 utilizes its unified architecture to perform this swap in the latent space during the initial generation pass.
4. Consistency Check: If the identity is weak, run a second pass at 0.2 Denoise using the same prompt to refine the features.
5. Advantage: This workflow avoids the complex node chains of ControlNet and ReActor, running in sub-second time on A100s.18
8.4 Workflow C: The Stylized Standard (SDXL + ReActor)
Target: Anime or semi-realistic content where "plastic" skin is acceptable.
Tools: Pony V6, ReActor (InsightFace), ControlNet OpenPose.
1. Pose Control: Use ControlNet OpenPose to define the explicit act or position.
2. Generation: Generate the base image using Pony V6.
3. Swap: Use the ReActor Node to swap the face.
4. The "20% Fix": The output from ReActor often looks low-res or mismatched in style. Pass the image back into Pony V6 (Img2Img).
   * Mask: Face only (dilated).
   * Denoise: 0.25.
   * Prompt: Include the original style tags (e.g., score_9, anime style).
5. Result: The realistic face from ReActor is "stylized" back into the anime aesthetic, removing the uncanny valley effect.
________________
9. Specialized and Emerging Models
While the "Big Three" (SDXL, Flux, Pony) dominate, other models play niche roles in the 2026 ecosystem.
9.1 Hunyuan Video 1.5
Though primarily a video model, Hunyuan Video 1.5 is critical for consistency workflows.
* Relevance: It can take a static image generated by Flux or Pony and animate it for 5-10 seconds with high temporal coherence.
* Face Consistency: Benchmarks indicate it holds facial identity better than Stability’s video models during movement.28
9.2 Z-Image
An Asian-market competitor to Flux.
* Performance: Comparable to Flux in photorealism but optimized for Asian facial aesthetics.
* Licensing: Often ambiguous or restrictive compared to Apache 2.0 models like Flux.2 Klein 4B.30
________________
10. Strategic Recommendations and Future Outlook
The choice of model in January 2026 is no longer about "which is best," but "which fits the business model."
10.1 For SaaS / High-Volume Platforms
Recommendation: Flux.2 [klein] 4B.
* Reasoning: The Apache 2.0 license eliminates legal risk. The sub-second generation speed minimizes GPU costs, allowing for profitable tiered subscriptions. The "In-Context" editing capability simplifies the backend pipeline by removing the need for separate face-swap servers.
10.2 For High-End Content Studios
Recommendation: Flux.1 [dev] (with License) or Chroma.
* Reasoning: Quality is paramount. The "plastic" look of SDXL is no longer acceptable for premium photorealistic content. Studios should negotiate a commercial license for Flux Dev or utilize the Chroma fine-tune to ensure the highest visual fidelity.
10.3 For Niche / Anime Communities
Recommendation: Pony Diffusion V6 (SDXL).
* Reasoning: Do not switch to Pony V7 yet. The V7 ecosystem is immature. The sunk cost of V6 LoRAs and the effectiveness of the "score tag" system mean that V6 will remain the standard for stylized content through at least Q2 2026.
10.4 The "Consistency" Future
The industry is moving away from "Generation" toward "Manipulation." The ability of Flux.2 to edit images via natural language ("Make her smile," "Change the room to a dungeon") without breaking the image structure represents the future of NSFW content interaction—interactive, personalized, and real-time.
11. Conclusions
The generative AI landscape for adult content in 2026 is defined by a trade-off between Control (SDXL/Pony), Quality (Flux.1), and Speed (Flux.2). While SDXL remains the "workhorse" due to its ecosystem, the Rectified Flow architecture of Flux is undeniably the superior technology. For commercial entities, the release of Flux.2 [klein] 4B under an Apache 2.0 license is the most disruptive event of the year, offering a clear path to high-margin, high-speed, and legally safe content generation. However, the legacy of SDXL will persist in niche communities where stylization and concept density outweigh pure photorealism. The future lies in hybrid workflows that leverage the strengths of each—using Flux for the base generation and SDXL/ControlNet for the structural guidance.
Источники
1. Pony Diffusion V6 XL - V6 (start with this one) | Stable Diffusion XL ..., дата последнего обращения: февраля 17, 2026, https://civitai.com/models/257749/pony-diffusion-v6-xl
2. [Guide] Helpful tags for image generation (SDXL/Pony) - SFW & NSFW | Civitai, дата последнего обращения: февраля 17, 2026, https://civitai.com/articles/8284/guide-helpful-tags-for-image-generation-sdxlpony-sfw-and-nsfw
3. Pony Diffusion XL v6 prompt tags, дата последнего обращения: февраля 17, 2026, https://stable-diffusion-art.com/pony-diffusion-prompt-tags/
4. Stable Diffusion 3.5 Medium model on ComfyUI, дата последнего обращения: февраля 17, 2026, https://stable-diffusion-art.com/stable-diffusion-3-5-medium-comfyui/
5. IP Adapter seems more powerful in SD 1.5 than SDXL . . . am I imagining things? - Reddit, дата последнего обращения: февраля 17, 2026, https://www.reddit.com/r/StableDiffusion/comments/1j1cp8a/ip_adapter_seems_more_powerful_in_sd_15_than_sdxl/
6. GPU Benchmark Comparison - A100 vs V100 - Trooper.AI, дата последнего обращения: февраля 17, 2026, https://www.trooper.ai/benchmarks-compare-A100-with-V100
7. flux/model_licenses/LICENSE-FLUX1-dev at main · black-forest-labs/flux - GitHub, дата последнего обращения: февраля 17, 2026, https://github.com/black-forest-labs/flux/blob/main/model_licenses/LICENSE-FLUX1-dev
8. Black Forest Labs - Frontier AI Lab, дата последнего обращения: февраля 17, 2026, https://bfl.ai/
9. Chroma - Open-source Model, Uncensored, Community-Drivent - Sogni AI, дата последнего обращения: февраля 17, 2026, https://www.sogni.ai/flux-chroma
10. Chroma Guide v0.6 | Civitai, дата последнего обращения: февраля 17, 2026, https://civitai.com/articles/19951/chroma-guide-v06
11. XLabs-AI/flux-controlnet-collections - Hugging Face, дата последнего обращения: февраля 17, 2026, https://huggingface.co/XLabs-AI/flux-controlnet-collections
12. InstantX/SD3.5-Large-IP-Adapter · ControlNet support? - Hugging Face, дата последнего обращения: февраля 17, 2026, https://huggingface.co/InstantX/SD3.5-Large-IP-Adapter/discussions/4
13. Flux IPAdapter: Comprehensive Guide with LoRA & ControlNet Integration - YouTube, дата последнего обращения: февраля 17, 2026, https://www.youtube.com/watch?v=KvrRlVFZjVo
14. black-forest-labs/FLUX.1-schnell - Hugging Face, дата последнего обращения: февраля 17, 2026, https://huggingface.co/black-forest-labs/FLUX.1-schnell
15. FLUX.2 [klein]: Towards Interactive Visual Intelligence | Black Forest Labs, дата последнего обращения: февраля 17, 2026, https://bfl.ai/blog/flux2-klein-towards-interactive-visual-intelligence
16. FLUX.2 [klein] - Fast, Efficient Image Generation | Black Forest Labs, дата последнего обращения: февраля 17, 2026, https://bfl.ai/models/flux-2-klein
17. black-forest-labs/FLUX.2-klein-9B - Hugging Face, дата последнего обращения: февраля 17, 2026, https://huggingface.co/black-forest-labs/FLUX.2-klein-9B
18. Best Face Swap in ComfyUI (2026): FLUX.2 Klein 9B + BFS LoRA - YouTube, дата последнего обращения: февраля 17, 2026, https://www.youtube.com/watch?v=ps7yl5ePIfU
19. black-forest-labs/FLUX.2-klein-4B - Hugging Face, дата последнего обращения: февраля 17, 2026, https://huggingface.co/black-forest-labs/FLUX.2-klein-4B
20. FLUX.2 [klein] Test: “Sub-Second” Generation Speed Stuns, While Quality Faces Trade-offs | 302.AI Benchmark Lab, дата последнего обращения: февраля 17, 2026, https://medium.com/@302.AI/flux-2-klein-test-sub-second-generation-speed-stuns-while-quality-faces-trade-offs-302-ai-c197a73df052
21. Just so you guys know, Flux 2 doesn't allow spicy images or IP-infringing content as per their inference filters : r/StableDiffusion - Reddit, дата последнего обращения: февраля 17, 2026, https://www.reddit.com/r/StableDiffusion/comments/1p6o9tl/just_so_you_guys_know_flux_2_doesnt_allow_spicy/
22. purplesmartai/pony-v7-base · Hugging Face, дата последнего обращения: февраля 17, 2026, https://huggingface.co/purplesmartai/pony-v7-base
23. Pony V7 is coming, here's some improvements over V6! : r/StableDiffusion - Reddit, дата последнего обращения: февраля 17, 2026, https://www.reddit.com/r/StableDiffusion/comments/1jm7ukk/pony_v7_is_coming_heres_some_improvements_over_v6/
24. is AI generation stagnate now? where is pony v7? : r/StableDiffusion - Reddit, дата последнего обращения: февраля 17, 2026, https://www.reddit.com/r/StableDiffusion/comments/1lcciff/is_ai_generation_stagnate_now_where_is_pony_v7/
25. Getting Started with Stable Diffusion 3.5 - Civitai Education, дата последнего обращения: февраля 17, 2026, https://education.civitai.com/getting-started-with-stable-diffusion-3-5/
26. ControlNets for Stable Diffusion 3.5 Large - Stability AI, дата последнего обращения: февраля 17, 2026, https://stability.ai/news/sd3-5-large-controlnets
27. Stable Diffusion 3.5: Stability AI Redeems Itself With New Models and Expanded Features - Decrypt, дата последнего обращения: февраля 17, 2026, https://decrypt.co/287807/stable-diffusion-3-5-stability-ai-redeems-itself-with-new-models-and-expanded-features
28. HunyuanVideo-1.5: A leading lightweight video generation model - GitHub, дата последнего обращения: февраля 17, 2026, https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5
29. Can Hunyuan Video 1.5 actually do more than 5 seconds unlike WAN? : r/StableDiffusion, дата последнего обращения: февраля 17, 2026, https://www.reddit.com/r/StableDiffusion/comments/1p3babt/can_hunyuan_video_15_actually_do_more_than_5/
30. ComfyUI | Generate video, images, 3D, audio with AI, дата последнего обращения: февраля 17, 2026, https://www.comfy.org/