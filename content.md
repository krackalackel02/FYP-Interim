# Section 1: Background & Literature Review
*(Matches Slide 3 in your PDF)*

**Slide Text (Keep it brief):**
* **The CFD Bottleneck:** Spectral/hp element methods (Nektar++) offer high fidelity but are constrained by dense matrix multiplications (DGEMM) in key operators (e.g., BwdTrans).
* **The Hardware Shift (Speeds):** Modern AI architectures (Tensor Cores) process low-precision compute (FP32/INT8) exponentially faster than standard FP64.
* **The Ozaki Algorithm:** A mathematical scheme that splits an FP64 matrix into several FP32/low-precision chunks. 
* **Applicability:** These chunks are computed on fast AI hardware and recombined, preserving exact FP64 accuracy while exploiting modern hardware speeds.

**Talking Points (What you say):**
"To understand the background, we must look at how the Ozaki algorithm works. It takes a standard double-precision matrix and splits it into several lower-precision components based on the magnitude of the floating-point values. By multiplying these smaller chunks on ultra-fast AI hardware—like Tensor Cores—and accumulating the results, we achieve the exact same FP64 accuracy but at a fraction of the time. This is perfectly applicable to Nektar++ because its core operators, like BwdTrans and IProdWRTBase, are essentially just massive dense matrix multiplications. By hacking this AI hardware trend, we can theoretically achieve massive speedups for fluid dynamics."

---

# Section 2: Project Aims & Objectives
*(Matches Slide 4 with the 3 boxes in your PDF)*

**Slide Text:**
* **Box 1 (Priority 1): Nektar++ Integration.** Implement the Ozaki scheme algorithm directly into Nektar++ backend operators.
* **Box 2 (Priority 2): Profiling & Benchmarking.** Benchmark the new implementation against Nektar++'s existing, highly performant standard operators.
* **Box 3 (Priority 3): INT8 Algorithm Integration.** Explore and integrate the extreme low-precision (INT8) variant of the algorithm from existing literature for maximum acceleration.

**Talking Points:**
"Because the mathematical validity of the Ozaki scheme has already been proven in the literature, my objectives are strictly implementation and performance-driven. My first aim is to natively implement the Ozaki algorithm into the Nektar++ codebase. Second, I will rigorously benchmark and profile this new code against Nektar++'s existing, highly optimized standard operators to quantify the actual speedup. Finally, my stretch objective is to attempt integrating the newer INT8 variant of the algorithm, which leverages integer tensor cores to push computational speeds even further."

---

# Section 3: Progress to Date
*(Matches Slides 5 & 6 in your PDF)*

**Slide Text:**
* **[15%] Literature & Scheme Validation:** Completed literature review, S3E plan, and locally validated the Ozaki mathematical splitting bounds. 
* **[35%] Baseline Profiling:** Successfully profiled standard Nektar++ execution to isolate and quantify peak DGEMM loads.
* **[50%] Algorithm Translation:** Translated the algorithm into standalone C++ code, ready for injection into the Nektar++ codebase.

**Talking Points (Crucial for the Rubric - focus on your methods):**
"I have structured my progress across key percentage milestones. The 0 to 15% mark involved completing my S3E requirements and mathematically validating the Ozaki scheme locally—proving the theory works. By the 35% mark, I completed a rigorous baseline profiling of standard Nektar++ runs. This was a critical methodological step to isolate exactly where the DGEMM bottlenecks occur. Today, I am at the 50% mark: I have translated the algorithm into standalone, optimized C++ code, and I am now fully prepared to begin the heavy integration phase into the Nektar++ library."

---

# Section 4: Plan for Remainder (Gantt Chart)
*(Matches Slide 7 in your PDF)*

**Slide Text:**
*(Use the exact dates we calculated earlier on your timeline Graphic)*
* **Aim 1 (20th Mar):** Optimise BwdTrans (Initial integration).
* **Aim 2 (17th Apr):** Implement Others (IProdWRTBase) & INT8 Integration.
* **Aim 3 (18th May):** HPC Benchmarking & Contingency block.
* **Finalise (25th May):** First Draft complete.
* **Deadline (1st Jun):** Thesis Submission.

**Talking Points:**
"Looking at the timeline for the remainder of the project, I have front-loaded the heavy C++ integration to be completed by mid-April, which includes exploring the INT8 variant. You will notice a large, 4-week window allocated for Benchmarking. I have intentionally built in this massive contingency buffer because hardware benchmarking on shared HPC clusters is notorious for queue delays and unpredicted GPU architecture bugs. This structure guarantees a hard-stop on coding by May 18th, leaving me exactly two full weeks dedicated entirely to drafting and finalizing the thesis."

---

# Section 5: Summary & Conclusion
*(Matches Slides 8, 9, 10 in your PDF)*

**Slide Text:**
* **Key Point 1: The Bottleneck.** Nektar++ CFD solvers are constrained by FP64 matrix multiplication limits.
* **Key Point 2: The Solution.** The Ozaki scheme exploits AI hardware (Tensor Cores) to process these matrices faster without losing precision.
* **Key Point 3: Current Status.** Mathematical validation and baseline profiling are complete (50%); the project is on track for codebase integration and HPC benchmarking.

**Talking Points:**
"To conclude, I want to leave you with three key takeaways. First, we are addressing a fundamental computational bottleneck in high-fidelity CFD. Second, our proposed solution effectively hacks modern AI hardware trends to accelerate scientific computing without compromising the double-precision accuracy that fluid dynamics demands. Finally, the project is exactly where it needs to be: the math is validated, the baseline is established, and we have a risk-mitigated plan to execute the codebase integration and benchmarking. Thank you for your time, I welcome any questions."s