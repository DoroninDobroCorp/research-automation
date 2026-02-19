For an adult AI companion voice in early‑2026, ElevenLabs or XTTS‑v2 (self‑hosted) are the most practical primary options; RVC is excellent as a real‑time “voice skin” on top of another TTS, while Bark and Tortoise are more niche due to latency and control issues. OpenAI’s own voice stack is powerful but its adult‑content policy is in flux, so it is riskier if you want clearly permitted explicit content.
docs.coqui
+12

Quick comparison table
Model	Quality (naturalness / emotion)	Cloning data needed	Real‑time suitability	Cost model	Adult / NSFW policy & license	Languages
ElevenLabs (cloud)	Widely treated as a quality benchmark; third‑party XTTS UI explicitly notes “Don’t expect EL level quality, it is not there yet.”
github
​	Built‑in “instant” and “professional” cloning in paid tiers; no training pipeline needed.
margabagus
​	Designed for real‑time conversational agents via API / startup grants.
elevenlabs
​	Free tier, then paid plans (e.g. Starter 5 USD, Creator 11 USD); usage overages around 0.30 USD/1k chars on Creator, dropping to 0.12 USD/1k on high tiers.
margabagus
+2
	Prohibited Use Policy bans using the service to create sexually explicit material that threatens child safety; community interpretations say consensual adult erotica is broadly allowed if you do not impersonate real people or defame them.
elevenlabs
+1
	Commercial “Multilingual” TTS models; pricing docs distinguish multilingual vs Flash models, implying broad language support for major languages.
flexprice
+1

XTTS v2 (Coqui, open‑source)	High‑quality, multi‑speaker neural TTS; HF card notes “better prosody and audio quality across the board” vs XTTS‑v1, but community UIs still rate it below ElevenLabs.
huggingface
+2
	Clones a voice from a single short reference clip (~3–6 s according to docs / HF card), with support for multiple references and interpolation.
docs.coqui
+2
	Supports streaming inference with <200 ms latency, explicitly targeting voice chat / streaming voice‑chat demos.
docs.coqui
+1
	Self‑hosted; main cost is a GPU (e.g. typical PyTorch setup). No per‑character fees.
docs.coqui
+1
	Licensed under Coqui Public Model License (CPML), a custom model license; no hardcoded adult‑content filters in the model itself, so compliance is mainly about following CPML and local law.
huggingface
+1
	Officially supports 16–17 languages including English, Spanish, French, German, Italian, Portuguese, Polish, Turkish, Russian, Dutch, Czech, Arabic, Chinese (zh‑cn), Japanese, Hungarian, Korean.
docs.coqui
+2

RVC (voice conversion, open‑source)	Converts one voice into another while preserving intonation and emotional tone; Wikipedia and project docs describe outputs as near‑indistinguishable from real speech when trained and run on adequate hardware.
wikipedia
+2
	Training typically uses on the order of ≤10 minutes of clean voice data to get good results according to the WebUI README.
github
​	WebUI supports a dedicated “realtime‑gui” mode; authors report end‑to‑end latency around 170 ms, and as low as ~90 ms with ASIO audio drivers on suitable hardware.
github
​	Fully self‑hosted; you pay only for your GPU / compute. Documentation stresses that it trains “even on relatively poor graphics cards.”
github
​	Open‑source GitHub project without built‑in content filters; license details are in‑repo but there is no central “adult‑content” service policy like a SaaS API.
github
+2
	Language‑agnostic speech‑to‑speech: it converts whatever spoken language is in the source audio; UI docs are localized to multiple languages but the model itself is not text‑based.
wikipedia
+2

Bark (Suno, open‑source)	Generative text‑to‑audio that can produce realistic, multilingual speech with nonverbal sounds (laughing, sighing, etc.), but authors warn it is not a conventional TTS and may “deviate in unexpected ways” from the script.
github
+2
	No true cloning: it offers 100+ fixed speaker presets and random voices; README explicitly says it does not currently support custom voice cloning.
github
+1
	Optimized for ~13–14 s audio generations per call; conversations need multiple chunks, which is awkward for responsive, streaming companions.
github
​	MIT‑licensed and available for commercial use; you host it yourself, so cost is GPU time.
github
+1
	MIT license places essentially no content‑type restrictions; Suno’s disclaimer focuses on responsible use but does not impose a SaaS‑style adult‑content gate.
github
+1
	Supports 10+ languages including English, German, Spanish, French, Hindi, Italian, Japanese, Korean, Polish, Portuguese, Russian, Turkish, Simplified Chinese.
github
+2

Tortoise TTS (neonbjb, open‑source)	High‑fidelity, multi‑voice TTS; maintainers and users describe “ultra_fast” preset as close to Google Cloud TTS quality at much lower cost.
github
+1
	Uses reference samples per “voice” folder rather than a single tiny clip; community work focuses more on inference/latency than a minimal‑seconds guarantee.
github
+1
	Upstream README says “this model is insanely slow” due to autoregressive + diffusion decoders; even aggressive optimizations and “fast” forks only reach 5–10× speed‑ups, with reports of ~430–800 ms just to first chunk on a modern GPU for short sentences.
github
+4
	Open‑source and self‑hosted; no per‑character cost, but GPUs are heavily loaded for each generation.
github
+3
	Core repo is open‑source; popular “tortoise‑tts‑fast” forks add AGPL‑licensed code, which affects how you can distribute services built on them.
github
+2
	Primarily trained on English voices; community experiments exist for other languages, but there is no official broad multilingual list like XTTS.
github
+1

OpenAI voice / TTS (API)	Not covered in detail in the retrieved docs here, but OpenAI markets ChatGPT with more human‑like, multi‑personality voices; focus is on “more human‑like” interaction rather than detailed TTS specs.
cnbc
+1
	Voice creation is handled by OpenAI; public docs and model spec focus on safety/usage constraints, not user‑side cloning pipelines.
model-spec.openai
+1
	Designed for interactive chat; policy docs and news focus on moderation, not latency, but ChatGPT is deployed for real‑time dialog at scale.
cnbc
+2
	API is u		