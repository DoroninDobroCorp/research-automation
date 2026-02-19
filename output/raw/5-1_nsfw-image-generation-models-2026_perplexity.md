For consensual adult work where you care about controllable identity variation, SDXL (especially its NSFW-focused fine‑tunes) and mature SD 1.5-based photo models are still the most practical options; Flux.1 dev offers very strong faces but is heavy and license‑constrained for NSFW, while Stable Diffusion 3 is currently a poor fit due to aggressive safety filtering and a restrictive, revocable license. None of these models’ official licenses allow non‑consensual face‑swaps or other harmful deepfake uses, and several explicitly prohibit impersonation without consent and sexual content without consent.
baseten
+6

Legal and safety constraints (important)

Stable Diffusion 1.5’s official documentation explicitly prohibits impersonating individuals without their consent and generating sexual content without the consent of the people who might see it, alongside other harmful uses. A recent overview of NSFW use around Stable Diffusion notes that many third‑party forks deliberately bypass filters for pornography and deepfakes, but stresses that this raises serious legal and ethical concerns around consent and privacy.
cometapi
+1

Flux.1’s license was updated in mid‑2025; community analysis indicates the updated “Flux.1 dev” license applies across all base Flux models and has been used to force removal of some NSFW LoRAs, indicating a move away from permissive NSFW and deepfake usage even if the raw weights are technically capable. Stable Diffusion 3’s new “community” and commercial licenses are explicitly revocable and include detailed use‑restriction and termination language, which commentators have flagged as risky for commercial workflows, especially where content might be ethically controversial.
reddit
+2
YouTube
​

For any explicit face‑swap/variation work, using real people without their informed consent will almost certainly violate both these licenses and, in many jurisdictions, local law; even for consensual adult work, reviewing the specific model license and your jurisdiction’s rules is essential.
huggingface
+1

High‑level comparison for NSFW / face‑variation
Model family	License & NSFW stance	Face/identity quality	Speed on A100 (very rough)	VRAM needs (typical)	Ecosystem & fine‑tuning
SD 1.5 + NSFW/photoreal fine‑tunes	CreativeML Open RAIL‑M; allows commercial use of model and outputs but bans illegal/harmful uses, impersonation without consent, non‑consensual sexual content.
ai-image-journey
+1
 Many NSFW fine‑tunes piggy‑back this and add their own clauses.	Mature photo models (RealisticVision, etc.) give strong, consistent faces; widely used for deepfake‑style work in third‑party tools, which is exactly what raises ethical scrutiny.
cometapi
​	Baseline SD ~5 s per 512×512 image and ~5 GB VRAM on consumer GPUs; an A100 is about 33 % faster and, with batching, reaches 2.5× the throughput of a 3080.
lambda
​ With heavy optimization, SD 1.5 can do 20‑step images in under 0.5 s per image on A100‑class hardware.
baseten
​	Around 5 GB VRAM for 512×512 at default settings; more for larger images or aggressive batching.
lambda
​	Richest ecosystem: mature ControlNet variants, IP‑Adapter‑style reference condition, countless LoRA/DreamBooth tools; most face‑swap pipelines in the wild are still SD 1.5‑based.
SDXL 1.0 + NSFW SDXL fine‑tunes (e.g., anime/“Pony‑like” and photo NSFW XL models)	SDXL 1.0 uses CreativeML Open RAIL++‑M; community and Stability sources describe it as allowing commercial use of outputs, subject to familiar RAIL restrictions.
ai-image-journey
+1
 Some NSFW SDXL models (e.g., WAI‑NSFW‑Illustrious‑SDXL) layer on a “fair‑ai‑public‑license‑1.0‑SD” that permits commercial use of generated images but adds conditions on model redistribution and harmful content.
note
​	SDXL is noticeably stronger than SD 1.5 for high‑res photoreal faces; well‑trained NSFW SDXL models tend to preserve identity reliably while allowing style/body variation, which is attractive for consensual adult work.	Out‑of‑the‑box SDXL 1.0 needs about 8–10 s to generate a 1024×1024 image on an A100; with optimizations (fewer steps, compilation) this can be cut to around 1.9 s for 20 steps, i.e., roughly 0.1–0.5 images per second at that resolution.
baseten
​	Significantly heavier than SD 1.5; practical 1024×1024 work typically targets 10–12 GB+ VRAM, with more VRAM enabling larger batches and higher resolutions (inferred from SDXL’s size and A100 benchmarks).
baseten
​	Strong ecosystem: SDXL‑specific ControlNets exist; IP‑Adapter‑style reference encoders and many XL LoRAs are available; several NSFW SDXL fine‑tunes are explicitly marketed for adult content under custom licenses.
note
+1

Flux.1 dev	Flux.1 models from Black Forest Labs ship under a custom “Flux.1 dev” license; community discussion notes a mid‑2025 ToS/license update that tightened terms across all base Flux models, and some NSFW LoRAs have reportedly been taken down for license violations.
reddit
​ Many hosted UIs advertise “no‑restrictions/NSFW modes” at the service level, but that is governed by the host’s own ToS, not necessarily by the base model license.
fluxai
+2
	Flux.1 dev is a 12 B‑parameter DiT model with state‑of‑the‑art human rendering; users consistently report excellent face detail and coherence, making it technically very strong for identity‑driven work if license constraints are satisfied.
hardware-corner
+1
	A performance study for Flux.1 reports that generating a 2048‑px image with the schnell variant in 4 steps on a single A100 takes ~10 s, and that the dev/pro variants with 30–50 steps are significantly slower, highlighting high latency compared with SD 1.5/SDXL for similar resolutions.
github
​	Hardware‑oriented testing finds official FP16 Flux.1 models need about 24 GB VRAM to run comfortably, with FP8/NF4 quantizations bringing this down to roughly 13 GB and lower‑precision GGUF variants spanning ~6–16 GB VRAM depending on quantization level.
hardware-corner
​ Advanced optimizations can push a single 1024×1024 generation down to ~2.6 GB baseline VRAM and even ~0.8 GB with aggressive offloading, at the cost of speed.
YouTube
​	Ecosystem and tooling are improving quickly but remain less mature than SD; some LoRA approaches exist, but lic