# GPU Inference Costs 2026: Where A100/H100 Are Cheapest, Reliable, and Scalable

## Executive Summary

As of January 2026, the GPU cloud market has bifurcated into two distinct tiers: specialized providers offering aggressive pricing for raw compute, and hyperscalers focusing on enterprise integration and capacity reservations.

**Specialized clouds are 2–5x cheaper for on-demand inference.**
Lambda Labs and RunPod consistently offer the lowest on-demand rates. Lambda prices A100 40GB instances at **$1.29/hr** and A100 80GB at **$1.79/hr**, while RunPod's Secure Cloud offers A100 80GB at **$1.49/hr** [1] [2]. In contrast, hyperscalers like Azure and Google Cloud price equivalent H100 capacity between **$11.06/hr** and **$12.29/hr** for on-demand usage [3] [4]. For pure inference workloads where enterprise support is not a blocker, specialized clouds offer immediate cost reduction.

**AWS Capacity Blocks unlock H100 affordability for planned workloads.**
While AWS on-demand P5 (H100) pricing is high (~$55–$98/hr for 8-GPU nodes), the **Capacity Blocks for ML** program reduces the effective rate to **$31.46/hr** (approx. **$3.93/GPU-hr**) for reserved durations of 1–14 days [5]. This makes AWS competitive with mid-tier providers for scheduled campaigns, product launches, or batch inference jobs, provided users can book capacity up to 8 weeks in advance.

**Managed inference services impose significant "idle taxes."**
Services like Google Vertex AI and AWS SageMaker Real-Time Inference charge for instance uptime, not just active compute. Vertex AI bills A100 80GB nodes at **~$4.52/hr** even when idle [6]. For spiky traffic, **RunPod Serverless** (Flex) offers true scale-to-zero billing at **$0.00076/second** ($2.72/hr active) for A100 80GB, eliminating costs during quiet periods [7].

**Spot instances offer 60–90% savings but break real-time SLAs.**
AWS Spot Instances can reduce P4d (A100) costs by up to **90%** (down to ~$3.90/hr for an 8-GPU node) [8]. However, interruption notices range from **2 minutes** on AWS to just **5 seconds** on RunPod [9] [10]. These options are viable only for fault-tolerant batch inference or asynchronous processing, not for user-facing synchronous APIs.

**Per-image costs are negligible; utilization is the primary cost driver.**
On a low-cost A100 40GB ($1.29/hr), generating an SDXL image (5s) costs just **$0.00179**. Even on premium H100 instances, costs remain under **$0.02** per image. The real cost driver is low utilization; an endpoint running at 20% utilization effectively quintuples the per-image cost.

## Scope and Methodology

This report benchmarks GPU pricing for **NVIDIA A100 (40GB/80GB)** and **H100 (80GB)** across six major providers. Data was retrieved between January and February 2026.

**Normalization Standards:**
* **Per-GPU Hourly Rate:** Where providers price by node (e.g., 8-GPU clusters), the rate is divided by the GPU count to allow direct comparison.
* **Currency:** All prices are in **USD**.
* **Region:** Primary benchmarks use **US East (N. Virginia)** or **US Central (Iowa)** regions. Regional variances are noted where significant.
* **Inference Cost Formula:**
 * `Cost per Image = (Per-GPU Hourly Rate / 3600) × Seconds per Image`
 * **SDXL:** Assumed latency of **5 seconds** on A100.
 * **Flux:** Assumed latency of **10 seconds** on A100.

## Normalized Price Benchmark: A100/H100 Per-GPU Hourly

The table below normalizes on-demand pricing to a single GPU hourly rate. Specialized providers (Lambda, RunPod, CoreWeave) consistently undercut hyperscalers (AWS, Azure, GCP) by significant margins.

| Provider | A100 40GB (OD) | A100 80GB (OD) | H100 80GB (OD) | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Lambda Labs** | **$1.29** | **$1.79** | **$3.44 – $3.78** | Lowest on-demand rates; simple per-minute billing [1] [11]. |
| **RunPod** | **$1.39** | **$1.49** | **$2.39 – $2.69** | "Secure Cloud" pricing; Community Cloud is cheaper but less reliable [2]. |
| **CoreWeave** | $2.06 | $2.21 | ~$6.15 | Base GPU price; CPU/RAM are add-ons. H100 rate normalized from 8x node [12]. |
| **AWS** | ~$4.10 | ~$3.43 | ~$6.88 | Based on 8-GPU node division. Capacity Blocks offer lower rates (~$3.93 for H100) [5] [13]. |
| **Azure** | ~$3.40 | ~$4.10 | ~$12.29 | East US pricing. H100 rate is significantly higher than AWS [4] [14]. |
| **Google Cloud** | ~$3.67 | ~$5.07 | ~$11.06 | A3 High (H100) pricing. A2 Ultra (A100 80GB) is premium priced [15] [3]. |

**Key Takeaway:** For raw compute, **RunPod** and **Lambda Labs** are the price leaders. AWS becomes competitive only when using **Capacity Blocks** for H100s ($3.93/hr), undercutting CoreWeave's on-demand rate.

## Provider Deep Dives

### 1. Lambda Labs
Lambda Labs focuses on providing the lowest possible cost for raw GPU compute with minimal overhead.

* **Hourly Rates:**
 * **A100 40GB:** $1.29/hr (SXM or PCIe) [1].
 * **A100 80GB:** $1.79/hr (SXM) [1].
 * **H100 80GB:** $3.44/hr (8x cluster) to $3.78/hr (1x instance) [1].
* **Reserved Discounts:**
 * **1-Click Clusters:** Reserved rates for H100 systems drop to **$2.19/hr** (3-month to 3-year term) [1].
 * **B200 Systems:** 1-year reservation at **$3.49/hr** vs $3.79/hr on-demand [1].
* **Spot/Preemptible:** No explicit spot tier listed; pricing is flat per-minute on-demand.
* **Minimum Commitments:** On-demand clusters have minimums as short as **1 week** for H100s [1].
* **Inference Specifics:** No managed inference endpoint service; users must manage their own serving infrastructure (e.g., vLLM, TGI) on bare metal or VMs.

### 2. CoreWeave
CoreWeave offers highly configurable "a la carte" instances, but users must account for add-on costs for CPU and RAM.

* **Hourly Rates (GPU Component Only):**
 * **A100 40GB:** $2.06/hr [12].
 * **A100 80GB:** $2.21/hr [12].
 * **H100 80GB:** $4.25/hr (PCIe) or ~$6.15/hr (HGX 8x node normalized) [12].
* **Add-on Costs:**
 * **vCPU:** $0.01/hr per vCPU.
 * **RAM:** $0.005/GB per hour [12].
 * *Impact:* A usable A100 instance typically exceeds **$3.00/hr** total [16].
* **Reserved Discounts:** Up to **60%** off on-demand rates for committed usage (typically 1–3 years) [17].
* **Spot/Preemptible:** Not publicly tiered in standard pricing; focus is on reserved capacity.
* **Inference Specifics:** CoreWeave Inference Service allows auto-scaling, but pricing is based on underlying compute resource consumption.

### 3. RunPod
RunPod offers the most granular options, including a "Community Cloud" (vetted peer-to-peer) and a "Secure Cloud" (datacenter), plus a true serverless option.

* **Hourly Rates (Secure Cloud):**
 * **A100 40GB:** $1.39/hr [18].
 * **A100 80GB:** $1.49/hr [18].
 * **H100 80GB:** $2.39/hr (PCIe) to $2.69/hr (SXM) [18].
* **Spot/Community Pricing:**
 * **A100 80GB:** As low as **$1.19/hr** [19].
 * **H100:** ~$1.99/hr [2].
 * *Risk:* Spot instances have a **5-second** termination warning [9].
* **Serverless Inference (Per-Second):**
 * **A100 80GB:** $0.00076/s ($2.72/hr) for Flex; $0.00060/s ($2.16/hr) for Active [7].
 * **H100 80GB:** $0.00116/s ($4.18/hr) for Flex; $0.00093/s ($3.35/hr) for Active [7].
 * *Flex:* Scales to zero (no cost when idle). *Active:* Always-on with ~30% discount vs Flex.

### 4. AWS (Amazon Web Services)
AWS pricing is bifurcated between high on-demand rates and significantly discounted "Capacity Blocks" for planned usage.

* **Hourly Rates (On-Demand):**
 * **p4d.24xlarge (8x A100 40GB):** ~$32.77/hr (~$4.10/GPU) [20].
 * **p5.48xlarge (8x H100 80GB):** ~$55.04/hr (~$6.88/GPU) [21].
* **Capacity Blocks (Reserved):**
 * **p5.48xlarge:** **$31.46/hr** (~$3.93/GPU) for 1–14 day reservations [5].
 * **p4d.24xlarge:** **$11.80/hr** (~$1.48/GPU) [5].
* **Spot Pricing:**
 * **p4d.24xlarge:** Can drop to ~$3.90 – $7.20/hr (up to 90% off) [22] [8].
 * *Risk:* 2-minute interruption notice [10].
* **Inference Specifics:**
 * **SageMaker Real-Time:** Billed per instance-hour (e.g., ml.p4d.24xlarge at ~$21.95/hr) [23].
 * **SageMaker Async:** Supports scale-to-zero.
 * **SageMaker Serverless:** Does **not** support GPUs as of Feb 2026 [24].

### 5. Google Cloud Platform (GCP)
GCP offers strong H100 availability via A3 instances but charges a premium for on-demand usage.

* **Hourly Rates (us-central1):**
 * **A2 Standard (A100 40GB):** ~$3.67/hr [15].
 * **A2 Ultra (A100 80GB):** ~$5.07/hr [15].
 * **A3 High (H100 80GB):** ~$11.06/GPU-hr (derived from 8-GPU node price of ~$88.49/hr) [15] [3].
* **Discounts:**
 * **Committed Use Discounts (CUDs):** 1-year (~37% off) and 3-year (~55% off) options [15].
 * **Spot VMs:** A100 40GB Spot at ~$1.43/hr; H100 Spot at ~$2.85/hr [25].
 * *Risk:* 30-second preemption notice [26].
* **Inference Specifics (Vertex AI):**
 * **A100 80GB:** ~$4.52/hr (billed per node-hour, includes idle time) [6].
 * **H100 80GB:** ~$11.27/hr [6].

### 6. Microsoft Azure
Azure's H100 pricing is the highest among the hyperscalers for on-demand usage in the East US region.

* **Hourly Rates (East US):**
 * **ND96amsr A100 v4 (8x A100 80GB):** $32.77/hr (~$4.10/GPU) [27].
 * **ND96isr H100 v5 (8x H100 80GB):** $98.32/hr (~$12.29/GPU) [4].
 * **NC H100 v5 (1x H100 80GB):** $6.98/hr [28].
* **Discounts:**
 * **Savings Plans:** 16% (1-year) to 38% (3-year) savings [14].
 * **Spot VMs:** ND96amsr A100 v4 Spot at ~$8.52/hr (74% savings) [29].
 * *Risk:* 30-second eviction notice [30].
* **Inference Specifics:** Azure ML managed endpoints charge the underlying VM rate with no additional surcharge [31].

## Per-Image Cost Modeling

Using the lowest on-demand rates for A100 instances, we calculated the cost per image generation.

**Assumptions:**
* **SDXL:** 5 seconds per image.
* **Flux:** 10 seconds per image.
* **Formula:** `(Hourly Rate / 3600) * Seconds per Image`

| Provider | A100 SKU | Hourly Rate | Cost per SDXL Image (5s) | Cost per Flux Image (10s) |
| :--- | :--- | :--- | :--- | :--- |
| **Lambda Labs** | A100 40GB | $1.29 | **$0.00179** | **$0.00358** |
| **RunPod** | A100 80GB | $1.49 | **$0.00207** | **$0.00414** |
| **CoreWeave** | A100 40GB | $2.06 | $0.00286 | $0.00572 |
| **AWS** | A100 40GB | ~$4.10 | $0.00569 | $0.01139 |
| **Azure** | A100 80GB | ~$4.10 | $0.00569 | $0.01139 |
| **Google Cloud** | A100 40GB | ~$3.67 | $0.00510 | $0.01020 |

**Sensitivity Analysis:**
* **Utilization Impact:** The costs above assume 100% utilization. If an endpoint runs at **70% utilization** (due to idle time or queuing), the effective cost per image increases by **~43%**. For example, on Lambda, the SDXL cost rises to **$0.00256**.
* **Latency Impact:** If Flux optimization reduces generation time to **6 seconds**, the cost on RunPod drops to **$0.00248** per image.

## Discount and Commitment Strategies

For sustained workloads, commitments can bridge the price gap between hyperscalers and specialized clouds.

| Provider | Program | Term | Typical Discount | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **AWS** | Capacity Blocks | 1–14 days | **~45–50%** | Best for short-term bursts (e.g., launches). H100 drops to ~$3.93/hr [5]. |
| **AWS** | Savings Plans | 1 or 3 years | **~25–45%** | Flexible across instance families. P5 (H100) 3-year plan offers ~45% off [32]. |
| **Google** | Committed Use (CUD) | 1 or 3 years | **~37–55%** | Requires attaching a reservation. 3-year CUD on A3 High drops H100 to ~$38.86/node (~$4.85/GPU) [15]. |
| **Azure** | Reserved Instances | 1 or 3 years | **~38–60%** | 3-year reservation on NC H100 v5 offers ~60% savings [14]. |
| **CoreWeave** | Reserved Capacity | 1–3 years | **Up to 60%** | Negotiated contracts for large clusters [17]. |
| **Lambda** | Reserved Clusters | 1–3 years | **~30–40%** | 1-year H100 reservation at $2.19/hr [1]. |

## Spot and Preemptible Options

Spot instances offer the lowest absolute price but introduce interruption risks that must be managed via checkpointing or asynchronous processing.

| Provider | Option Name | Discount | Interruption Notice | Best For |
| :--- | :--- | :--- | :--- | :--- |
| **AWS** | Spot Instances | Up to 90% | **2 minutes** [10] | Fault-tolerant batch processing. |
| **Google** | Spot VMs | 60–91% | **30 seconds** [26] | Stateless workloads, queue-based inference. |
| **Azure** | Spot VMs | Up to 90% | **30 seconds** [30] | Dev/test, batch jobs. |
| **RunPod** | Spot Pods | ~20–50% | **5 seconds** [9] | Highly fault-tolerant tasks only. |

## Availability and Procurement Constraints

Despite pricing improvements, procuring H100s remains non-trivial for large-scale deployments.

* **AWS:** **Capacity Blocks** are the primary mechanism for guaranteeing H100 access. Reservations can be made up to 8 weeks in advance, with a cap of 256 instances per account [33].
* **Azure:** Quotas for H100 (NDv5) are "not a capacity guarantee." High demand in regions like East US 2 has led to waitlists, and support tickets are often required to unlock quotas [34].
* **Google Cloud:** Introduced "future reservation requests" to allow users to view and book A3 capacity in advance [35].
* **New Hardware:** The rollout of **H200** and **Blackwell (B200)** instances is beginning to alleviate pressure on H100 supply, with AWS and CoreWeave listing these new SKUs [33] [36].

## Strategic Recommendations

1. **For Maximum Cost Efficiency:** Default to **Lambda Labs** or **RunPod** for on-demand inference. Their rates ($1.29–$1.49/hr for A100) are unbeatable for steady-state workloads that don't require hyperscaler ecosystems.
2. **For Spiky Workloads:** Use **RunPod Serverless (Flex)** or **AWS SageMaker Asynchronous Inference**. These allow scaling to zero, eliminating the "idle tax" that destroys unit economics on standard VMs.
3. **For Enterprise Scale:** Leverage **AWS Capacity Blocks** for predictable, high-volume events (e.g., model training runs or marketing campaigns). The ~45% discount brings H100 pricing in line with mid-tier providers while retaining AWS reliability.
4. **For Reliability:** Avoid Spot instances for user-facing inference. The 5–30 second interruption windows on RunPod, Azure, and GCP are too short for graceful handoffs in synchronous applications. Use Spot only for background batch processing.

## References

1. *AI Cloud Pricing | GPU Compute & AI Infrastructure | Lambda*. https://lambda.ai/pricing
2. *GPU Pricing*. https://www.runpod.io/gpu-pricing
3. *Google Compute Engine Machine Type a3-highgpu-8g*. https://gcloud-compute.com/a3-highgpu-8g.html
4. *Standard_ND96isr_H100_v5 specs and pricing | Azure | CloudPrice*. https://cloudprice.net/vm/Standard_ND96isr_H100_v5
5. *Amazon EC2 Capacity Blocks for ML Pricing – AWS*. https://aws.amazon.com/ec2/capacityblocks/pricing/
6. *Vertex AI pricing | Google Cloud*. https://cloud.google.com/vertex-ai/pricing
7. *Pricing - Runpod Documentation*. https://docs.runpod.io/serverless/pricing
8. *
      Spot Instances and Preemptible GPUs: Cutting AI Costs by 70% | Introl Blog
    *. https://introl.com/blog/spot-instances-preemptible-gpus-ai-cost-savings
9. *Pricing - Runpod Documentation*. https://docs.runpod.io/pods/pricing
10. *Spot Instance interruption notices - Amazon Elastic Compute Cloud*. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-instance-termination-notices.html
11. *Instances | Lambda*. https://lambda.ai/instances
12. *CoreWeave Classic Pricing | CoreWeave*. https://www.coreweave.com/pricing/classic
13. *GPU cloud pricing US East*. https://scouts.yutori.com/6ca313ec-5167-4371-876a-f19937ac0aea
14. *Pricing - Windows Virtual Machines | Microsoft Azure*. https://azure.microsoft.com/en-us/pricing/details/virtual-machines/windows/
15. *VM instance pricing | Google Cloud*. https://cloud.google.com/compute/vm-instance-pricing
16. *How Much Does CoreWeave Cost? GPU Pricing Guide (December 2025)*. https://www.thundercompute.com/blog/coreweave-gpu-pricing-review
17. *GPU Cloud Pricing | CoreWeave*. https://www.coreweave.com/pricing
18. *Pricing | Runpod GPU cloud computing rates*. https://www.runpod.io/pricing
19. *RunPod Pricing 2025 Complete Guide (GPU Cloud Costs ...*. https://flexprice.io/blog/runprod-pricing-guide-with-gpu-costs
20. *p4d.24xlarge Pricing and Specs: AWS EC2*. https://costcalc.cloudoptimo.com/aws-pricing-calculator/ec2/p4d.24xlarge
21. *p5.48xlarge pricing and specs - Vantage*. https://instances.vantage.sh/aws/ec2/p5.48xlarge
22. *p4d.24xlarge pricing and specs - Vantage*. https://instances.vantage.sh/aws/ec2/p4d.24xlarge
23. *Amazon SageMaker AI Pricing*. https://aws.amazon.com/sagemaker/ai/pricing/
24. *Deploy models with Amazon SageMaker Serverless Inference - Amazon SageMaker AI*. https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html
25. *Spot VMs pricing*. https://cloud.google.com/spot-vms/pricing
26. *Spot VMs  |  Compute Engine  |  Google Cloud Documentation*. https://docs.cloud.google.com/compute/docs/instances/spot
27. *Standard_ND96amsr_A100_v4 specs and pricing*. https://cloudprice.net/vm/Standard_ND96amsr_A100_v4
28. *NC40ads H100 v5 pricing and specs - Vantage*. https://instances.vantage.sh/azure/vm/nc40adsh100-v5
29. *ND96amsr A100 v4 pricing and specs - Vantage*. https://instances.vantage.sh/azure/vm/nd96amsr
30. *Use Azure Spot Virtual Machines - Azure Virtual Machines | Microsoft Learn*. https://learn.microsoft.com/en-us/azure/virtual-machines/spot-vms
31. *Online endpoints for real-time inference - Azure Machine Learning | Microsoft Learn*. https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints-online?view=azureml-api-2
32. *AWS EC2 Pricing Update 2025: Major Price Cuts*. https://www.pump.co/blog/aws-ec2-pricing-update
33. *Capacity Blocks for ML - Amazon Elastic Compute Cloud*. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-blocks.html
34. *Urgent Quota Request for A100/H100 GPU VMs in East US 2 Due to NC6s_v3 Retirement. - Microsoft Q&A*. https://learn.microsoft.com/en-us/answers/questions/5538289/urgent-quota-request-for-a100-h100-gpu-vms-in-east
35. *Compute Engine release notes  |  Google Cloud Documentation*. https://docs.cloud.google.com/compute/docs/release-notes
36. *CoreWeave GPU Pricing: Compare 8+ GPUs*. https://computeprices.com/providers/coreweave