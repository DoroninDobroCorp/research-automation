Here is a January‑2026 snapshot of approximate GPU pricing and per‑image costs for the requested providers; all values are indicative, region‑dependent, and should be verified against the linked pricing pages before you commit workloads.
lambda
+8

Assumptions for cost‑per‑image: A100 runs SDXL at 5 seconds/image and Flux at 10 seconds/image, so SDXL images/hour ≈ 720 and Flux images/hour ≈ 360 per GPU.
verda
+1

Core pricing snapshot (USD / GPU‑hour)

Approximate on‑demand pricing for A100 and H100 as of late‑2025 / early‑2026 (single‑GPU equivalent, excluding CPU/RAM mark‑ups where those are quoted separately):

Provider	GPU	VRAM	Approx on‑demand GPU‑hr	Notes
Lambda	A100	40GB	1.29	Lambda instances page lists A100 SXM 40GB at 1.29 $/GPU‑hr.
lambda
​
Lambda	A100	80GB	1.79	Lambda instances page lists A100 SXM 80GB at 1.79 $/GPU‑hr.
lambda
​
Lambda	H100	80GB	3.44	Lambda instances page lists H100 SXM 80GB at 3.44 $/GPU‑hr.
lambda
​
CoreWeave	A100	80GB	2.21 (GPU only)	Analyses of CoreWeave pricing cite A100 80GB GPU component at 2.21 $/hr before CPU/RAM, with typical full instances >3 $/hr.
thundercompute
​
CoreWeave	H100	80GB	≈6.15–6.16	8×H100 HGX nodes around 49.24 $/hr, ≈6.15 $/GPU‑hr; independent trackers list H100 ≈6.16 $/GPU‑hr.
thundercompute
+2

RunPod (pods)	A100	40GB	1.19	Northflank comparison using RunPod data shows A100 40GB pods at ≈1.19 $/hr.
northflank
​
RunPod (pods)	A100	80GB	1.39	Same source lists A100 SXM 80GB pods ≈1.39 $/hr.
northflank
​
RunPod (pods)	H100	80GB	1.99	H100 PCIe 80GB pods ≈1.99 $/hr.
northflank
​
RunPod (serverless)	A100	80GB	2.74 (2.16 discounted)	Serverless pricing table: A100 80GB at 0.00076 $/s (≈2.74 $/hr) and 0.00060 $/s (≈2.16 $/hr) for discounted tier.
runpod
+1

RunPod (serverless)	H100	80GB	4.18 (3.35 discounted)	H100 80GB at 0.00116 $/s (≈4.18 $/hr) and 0.00093 $/s (≈3.35 $/hr) for discounted tier.
runpod
+1

AWS (p4d)	A100	40GB	≈2.74	Cloud GPU comparison shows 8×A100 40GB p4d at about 21.95 $/hr ⇒ ≈2.74 $/GPU‑hr.
verda
​
AWS (p5)	H100	80GB	≈3.93	H100 pricing guide normalizes p5.48xlarge to ≈3.93 $/GPU‑hr on‑demand (8×H100).
intuitionlabs
​
GCP (Vertex / A2/A3)	A100	80GB	≈4.52	Vertex AI pricing lists A100 80GB GPUs at about 4.51729 $/GPU‑hr.
cloud.google
​
GCP (Compute Engine)	A100	80GB	≈6.25	A2‑ultragpu‑1g (1×A100 80GB) quoted around 6.25 $/hr.
verda
​
GCP (Compute Engine)	A100	40GB	≈4.05	A2‑highgpu‑8g (8×A100 40GB) at ≈32.40 $/hr ⇒ ≈4.05 $/GPU‑hr.
verda
​
GCP (Compute Engine)	H100	80GB	≈11.06	a3‑highgpu‑1g H100 80GB quoted ≈11.06 $/GPU‑hr; other analysis notes newer pricing nearer 3 $/GPU‑hr depending on discounts.
verda
+1

Azure	A100	40–80GB	≈3.67 (1×GPU)	Comparison article lists Azure A100 options from ≈3.67 $/hr for 1×A100 up to ≈14.69 $/hr for 4×A100 VMs.
verda
​
Azure ND H100 v5	H100	80GB	≈12.29 (per GPU)	ND96isr H100 v5 VM (8×H100) about 98.32 $/hr ⇒ ≈12.29 $/GPU‑hr on‑demand.
cyfuture
+2

Prices vary by region, instance shape, and whether CPU/RAM is bundled or billed separately; where only node‑level prices were available, per‑GPU figures are simple divisions for comparison rather than exact SKU prices.
thundercompute
+9

Reserved, spot, and commitments (by provider)
Lambda Labs

Reserved / committed capacity:

“1‑Click Clusters” for H100 show on‑demand pricing “as low as” 2.29 $/GPU‑hr for short commitments (1 week–3 months) and reserved pricing from 2.19 $/GPU‑hr for 3‑month to 3‑year terms.
lambda
​

Spot / preemptible:

Lambda advertises first‑come self‑serve instances; public docs emphasize on‑demand and cluster reservations, not classic spot markets, so interruptions are not priced as a separate “spot” SKU.
lambda
​

Minimum commitment:

Single instances are pay‑as‑you‑go; cluster commitments range from 1 week to multi‑year contracts for best H100/B200 rates.
lambda
​

Inference‑specific pricing:

Lambda’s public pricing is per GPU instance; there is no separate per‑request inference SKU in the main pricing page, so inference and training use the same GPU‑hour prices.
lambda
​

CoreWeave

Reserved / committed capacity:

Documentation and third‑party analyses describe configurable instances where GPU, CPU, RAM, and storage are billed separately; discounts for larger clusters and long‑term commitments are negotiated with sales rather than published as fixed percentages.
coreweave
+2

Spot / preemptible:

Market overviews note that CoreWeave offers spot/preemptible capacity with lower rates than standard on‑demand, although precise discounts are not listed publicly.
neosignal
​

Minimum commitment:

On‑demand instances are hourly with no long‑term commitment; reserved and dedicated clusters are enterprise contracts with bespoke terms.
coreweave
+2

Inference‑specific pricing:

CoreWeave mainly exposes raw GPU nodes (including H100 HGX) with Kubernetes and orchestration support; pricing does not distinguish training vs inference beyond instance choice.
thundercompute
+2

RunPod

Reserved / committed capacity:

GPU pods (e.g., A100 40GB at ≈1.19 $/hr, A100 80GB at ≈1.39 $/hr, H100 80GB at ≈1.99 $/hr) are billed per second with no fixed minimum term beyond the running time.
northflank
​

Serverless GPU “workers” bill per‑se