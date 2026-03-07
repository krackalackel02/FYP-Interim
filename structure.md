# Interim Presentation Skeleton: Accelerating Nektar++ via Ozaki Scheme

**Total Time:** 10 Minutes
**Target:** 10-12 Slides Maximum (approx. 1 minute per slide)

## 1. Title Slide (0.5 mins)

* **Visuals:** Imperial College Logo, Clean Title (e.g., "Accelerating Nektar++ Solvers: DGEMM Emulation via the Ozaki Scheme"), Your Name, Supervisor's Name.

* **Speaking Notes:** Introduce yourself, your course, and state the title of your project clearly.

## 2. Background: The Bottleneck in Nektar++ (1 min)

* *Rubric Target: Background (Context & Literature)*

* **Visuals:** A simple diagram showing the Nektar++ pipeline (World Space <-> Modal Space). Highlight `BwdTrans` and `IProdWRTBase`.

* **Key Points:**

  * High-fidelity CFD (spectral/hp element methods) is incredibly accurate but computationally expensive.

  * The core bottleneck is dense matrix multiplication (DGEMM) when transforming between coefficient and physical space.

  * We are limited by standard FP64 (Double Precision) hardware throughput.

## 3. Background: The Hardware Shift & The Solution (1.5 mins)

* *Rubric Target: Background (Literature & Past Works)*

* **Visuals:** A chart comparing FP32/FP16 (Tensor Core) vs. FP64 performance on modern GPUs (e.g., NVIDIA A100 or H100).

* **Key Points:**

  * *The Literature:* Cite the paper by Ogita, Mukunoki, et al.

  * *The Solution:* The AI boom has made low-precision compute (SGEMM/HGEMM) exponentially faster.

  * The Ozaki Scheme allows us to split FP64 matrices into FP32 chunks, compute them on fast hardware, and recombine them without losing precision.

## 4. Project Aims & Objectives (1 min)

* *Rubric Target: Aims and Objectives (Clear, Measurable, Prioritized)*

* **Visuals:** A numbered, bulleted list with clear visual tags for Priority (High/Medium/Low).

* **Key Points (Read these out as your measurable goals):**

  1. **\[High Priority\]** Profile Nektar++ operators to isolate peak DGEMM loads.

  2. **\[High Priority\]** Implement a standalone C++ version of the Ozaki scheme for DGEMM emulation.

  3. **\[High Priority\]** Integrate the emulation into Nektar++'s backend.

  4. **\[Medium Priority\]** Benchmark accuracy (error-free transformation check) against standard BLAS.

  5. **\[Low/Stretch\]** Optimize the underlying SGEMM calls specifically for NVIDIA Tensor Cores.

## 5. Progress to Date: Setup & Literature (1 min)

* *Rubric Target: Progress to Date (Methods and Reasoning)*

* **Visuals:** Screenshots of code setup, or a summary of papers read.

* **Key Points:**

  * Completed thorough literature review of error-free transformations.

  * Secured reference code/formulations (mentioning outreach to Prof. Ogita).

  * Passed S3E requirements (Sustainability, Security, Safety, Ethics) focusing on computational sustainability.

## 6. Progress to Date: Implementation / Profiling (1.5 mins)

* *Rubric Target: Progress to Date (Excellent progress using appropriate methods)*

* **Visuals:** A code snippet of your work so far, OR a profiling graph showing Nektar++ execution time.

* **Key Points:**

  * Show *what* you have actually done. Have you written the matrix splitting logic? Have you profiled a standard 1D/2D Nektar++ run?

  * Discuss the *methodology* used for your progress (e.g., "I used Intel VTune/Nsight to profile the baseline...").

## 7. Plan for Remainder: Methodology & Approach (1.5 mins)

* *Rubric Target: Plans for Remainder (Methods thoroughly discussed)*

* **Visuals:** A flowchart showing how you will validate your code. (e.g., Ozaki Code -> Unit Test -> Nektar++ Integration -> CFD Benchmark).

* **Key Points:**

  * How will you prove it works? (Explain your testing methodology: e.g., comparing the L2 norm of the Nektar++ solution using standard BLAS vs. your Ozaki BLAS).

  * What hardware will you test it on? (e.g., Imperial's HPC cluster).

## 8. Plan for Remainder: Timeline / Gantt Chart (1.5 mins)

* *Rubric Target: Plans for Remainder (Well-developed plan, appropriate timescales)*

* **Visuals:** A clean, easy-to-read Gantt chart. Do *not* make it too small. Group tasks by weeks or months.

* **Key Points:**

  * Walk the audience through the remaining weeks.

  * Highlight key milestones: "By Week X, integration complete. By Week Y, benchmarking complete. Week Z dedicated entirely to thesis writing."

  * Show that you have built-in buffer time for debugging C++ / GPU issues.

## 9. Summary & Conclusion (0.5 mins)

* *Rubric Target: Quality of Presentation (Clear, logical conclusion)*

* **Visuals:** 3 simple bullet points summarizing the core message.

* **Key Points:**

  * We are solving the FP64 bottleneck in Nektar++.

  * Using the Ozaki scheme on AI hardware.

  * Progress is on track, with a clear roadmap to the final thesis.

  * "Thank you for listening, I welcome any questions."s