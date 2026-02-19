Most of the mainstream text‑/image‑to‑video models you named can technically be used as building blocks for “deepfake‑style” content, but all of the hosted services (Runway, Luma, Kling, Pika, HeyGen) explicitly prohibit NSFW and non‑consensual or deceptive face‑swap uses in their policies, so production deepfake work today is still done mainly with open‑source tools you self‑host (DeepFaceLab, FaceFusion, DeepFaceLive, etc.).
klingaiprompt
+6

Below is a model‑by‑model view focused on practical capabilities, quality, performance, terms, and realistic cost‑per‑minute ranges as of early 2026.

Big picture for “deepfake” use

Hosted, general video models (Runway Gen‑3, Luma Dream Machine, Kling, Pika) excel at generating or restyling entire shots but do not give you fine‑grained, controllable, identity‑preserving face swap comparable to classic deepfake pipelines; they also block explicit and non‑consensual uses.
mixhubai
+6

Specialized avatar / talking‑head services (HeyGen, Pika’s Pikaformance) are good for ethical, consented lip‑sync / dubbing and avatar work, but again prohibit deceptive impersonation and NSFW.
linkedin
+3

True “deepfake” face‑swap pipelines with maximum control and no upstream policy constraints still come from self‑hosted tools (DeepFaceLab, FaceFusion, DeepFaceLive, Roop‑style single‑image swappers), where your cost is GPU time and your own legal risk rather than API credits.

The tables and sections below assume legal, consented business use (e.g., dubbing your own spokesperson, stylized ads), not covert impersonation.

Capabilities & quality overview
High‑level capabilities
Model / family	Face‑swap specific tools	Lip‑sync / talking head	Full text‑/image‑to‑video	Face quality & consistency (practical)
Stable Video Diffusion (SVD)	No dedicated face‑swap; you can approximate by image‑to‑video + inpainting; best treated as a general open‑weights video model.	None built‑in; need separate lip‑sync model.	Image‑to‑video and short text‑conditioned clips via open‑source pipelines.	Good motion/temporal coherence for short clips; identity retention is weaker than dedicated face‑swap models and needs extra work.
Runway Gen‑3 (Alpha / Turbo)	No explicit “face‑swap” tool; you can do video‑to‑video restyling, masking, and extensions, but identity‑perfect swap is not guaranteed and impersonation is disallowed.	Not a talking‑head engine; lip motion quality is prompt‑driven, not phoneme‑driven.	Strong text‑to‑video and image‑to‑video, with a focus on expressive human characters and cinematic motion.
techcrunch
+1
	Among the best SaaS options for realistic humans; very good temporal consistency but still occasional artifacts with complex interactions.
techcrunch
+1

Kling	No official face‑swap tool; text‑/image‑to‑video plus some editing; policies explicitly disallow NSFW and abusive uses.
klingaiprompt
+4
	No dedicated lip‑sync module.	High‑quality text‑ and image‑to‑video in cinematic and photorealistic styles.
mixhubai
​	Very strong overall motion and consistency; user reports often put it at or above Runway/Luma for realism.
Luma Dream Machine	No turnkey face‑swap; you can animate portraits or do video‑to‑video style changes.	No phoneme‑accurate lip‑sync; faces move according to higher‑level motion in the prompt.	Fast, high‑quality text‑ and image‑to‑video with strong physics and character consistency.
aicreators
+1
	Physically accurate motion and high character consistency are core selling points; outputs often look the most coherent of current web UIs.
aicreators
+1

Pika (2.x / Turbo / Pikaformance)	Pika includes “Pikaswaps” and related tools for swapping characters/faces using reference images (within policy), plus more general video‑editing.
pikartai
​	Pikaformance is a dedicated model that turns still images into talking avatars, syncing expressions and lip movement to arbitrary audio.
pikartai
​	Strong text‑to‑video and image‑to‑video; Turbo variant emphasizes speed over peak fidelity.
imagine
+4
	Good character consistency with keyframing (Pikaframes) and reference‑image guidance; Turbo trades some detail for speed but is still solid.
imagine
+2

HeyGen (avatars / video translate)	Yes: avatar creation and translation workflows effectively implement consented face‑swap (you clone a face and map it to new speech and languages), with strict consent requirements.
linkedin
+2
	Strong, production‑grade lip‑sync and multilingual dubbing for avatars and video translation.
heygen
+1
	Not a general text‑to‑video generator; more of an avatar / presentation / translation platform.	Avatar quality is high enough that business users report “almost indistinguishable” results, but subtle uncanny‑valley micro‑motions remain.
linkedin
​
Performance & cost per minute (approximate)
Measured generation speeds

Where there are published or benchmarked numbers:

Runway Gen‑3

5‑second clip in ~45–60 seconds; 10‑second clip in ~90 seconds (Alpha).
techcrunch
+1

That’s around 9–12 seconds of GPU time per second of output.

Runway Gen‑3 credit usage

Gen‑3 Alpha: 10 credits per second of video; Gen‑3 Alpha Turbo: 5 credits per second.
help.runwayml
​

Max base length per clip 10–20 seconds depending on workflow, with “Extend” for longer sequences.
runwayml
+1

Luma Dream Machine

Reports vary by version and host: some benchmarks show 120 frames (≈5 seconds) in about 20 seconds, others in about 120 seconds, and Luma’s own marketing currently claims “create stunning videos in under two minutes” for 120 frames.
lummi
+2

A safe planning assumption is roughly 4–24 seconds of compute per second of video, depending on resolution and load.
aicreators
+3

Kling

Third‑party testing reports “under 25 seconds per 8‑second clip,” i.e., about 3 seconds of compute per second of output at current scale.
mixhubai
​

Pika (2.x / Turbo)

Pika 2.2: 5–10 second 720p or 1080p clips generated in “a few minutes,” with longer, higher‑res clips taking more time.
imagine
​

Pika Turbo: 3–5 second clips “in under a minute,” ~3× faster than Pro / 2.2, implying roughly 6–12 seconds of compute per second of video for Turbo and more like 15–30 seconds per second for high‑quality Pro.
pika-art
+2

HeyGen

Vendor blogs emphasize overall turnaround (“make professional AI videos quickly”) rather than raw seconds, but user reports and marketing both suggest typical avatar generations complete in a few minutes for 30–60 second clips (slightly slower than real‑time).
heygen
​

Stable Video Diffusion (self‑hosted)

Performance depends entirely on your GPU; on a single modern prosumer GPU, practitioners typically see tens of seconds to render a 4–6 second 576p–720p clip, i.e., on the order of 5–15 seconds of compute per second of output. (This comes from open‑source benchmarks and will vary with optimization; no specific vendor numbers in the retrieved docs.)

Rough cost‑per‑minute ranges

Because cr