---
theme: default
title: Introduction to Metaheuristics
titleTemplate: '%s'
info: When brute force can't find the answer, how do algorithms search?
author: Slidev Skills
transition: slide-up
colorSchema: light
routerMode: hash
fonts:
  sans: '"Helvetica Neue", Helvetica, Arial, sans-serif'
  mono: 'JetBrains Mono'
layout: default
---

<div class="swiss-grid">

<div class="col-span-7 col-start-1 flex flex-col justify-center">
  <div class="label-small accent-text mb-4">Metaheuristics</div>
  <h1>Search, when the search space is too large for brute force</h1>
  <p class="mt-4">10<sup>100</sup> solutions. You can test 10<sup>9</sup>. What do you do?</p>
</div>

<div class="col-span-4 col-start-9 hairline-left pl-6 h-full flex flex-col justify-end pb-8">
  <div class="text-6xl font-bold accent-text mb-2" style="line-height: 1;">10<sup>100</sup></div>
  <p class="label-small mb-2" style="color: #111;">States in a typical search space</p>
  <p class="text-sm">More than atoms in the observable universe. Brute force is not an option.</p>
</div>

</div>

---

<div class="swiss-grid">

<div class="col-span-6 col-start-1 h-full hairline-right pr-6 flex flex-col justify-center">
  <div class="label-small accent-text mb-4">01 / The Scale</div>
  <h1>A needle in a universe-sized haystack</h1>
  <p class="mt-4">TSP with 50 cities: ~10<sup>64</sup> routes. Branch-and-bound at 10<sup>9</sup> routes/sec: 10<sup>47</sup> years.</p>
  <div class="hairline-top pt-4 mt-4">
    <p class="text-sm mb-2">The best we can hope for is <b>good enough, fast enough</b>.</p>
  </div>
</div>

<div class="col-span-5 col-start-8 flex flex-col h-full justify-between">
  <div>
    <div class="mono text-sm" style="background:#f2f2ef;padding:16px;">
      <div style="color:#a0a0a0;">TSP scaling</div>
      <div class="mt-2">10 cities → <span class="accent-text">3.6 × 10<sup>6</sup></span> routes</div>
      <div class="mt-1">20 cities → <span class="accent-text">1.2 × 10<sup>18</sup></span> routes</div>
      <div class="mt-1">50 cities → <span class="accent-text">3.0 × 10<sup>64</sup></span> routes</div>
    </div>
  </div>
  <div class="hairline-top pt-6 mt-8">
    <p class="text-sm">Exact optimization is tractable for n &lt; ~20. Beyond that, we need heuristics.</p>
  </div>
</div>

</div>

---

<div class="swiss-grid">

<div class="col-span-12 hairline-bottom pb-8 mb-8">
  <div class="label-small accent-text mb-4">02 / The Naive Approach</div>
  <h1>Hill climbing: always go uphill</h1>
  <p class="mt-4 w-2/3">Pick a random point. Move to a neighbor if it improves the objective. Repeat until stuck.</p>
</div>

<div class="col-span-5">
  <div class="mono text-sm" style="background:#f2f2ef;padding:16px;">
    <div style="color:#a0a0a0;">Hill climbing</div>
    <div class="mt-2">x ← random()</div>
    <div class="mt-1"><b>repeat</b>:</div>
    <div class="mt-1 ml-4">x' ← neighbor(x)</div>
    <div class="mt-1 ml-4"><b>if</b> f(x') > f(x):</div>
    <div class="mt-1 ml-8">x ← x'</div>
    <div class="mt-1"><b>until</b> converged</div>
  </div>
</div>

<div class="col-span-6 col-start-7 hairline-left pl-6">
  <div style="font-size:60px;font-weight:700;line-height:1;letter-spacing:-0.04em;color:#d92d20;">Local</div>
  <p class="label-small mt-2">Hill climbing finds the nearest optimum</p>
  <p class="text-sm mt-2">If you start near a local peak, you climb it. You never see the taller peak across the valley because going downhill is disallowed.</p>
  <div class="hairline-top pt-4 mt-6">
    <p class="text-sm">The algorithm has no mechanism to escape local optima. It converges to whatever attractor basin it lands in.</p>
  </div>
</div>

</div>

---

<div class="swiss-grid">

<div class="col-span-5 h-full hairline-right pr-6 flex flex-col justify-center">
  <div class="label-small accent-text mb-4">03 / The Landscape</div>
  <h1>A landscape is a function f: X → ℝ</h1>
  <p class="mt-4">Each point in the search space has a fitness. Optimization algorithms are walkers on this terrain. They need a strategy to find the highest peak.</p>
  <div class="hairline-top pt-4 mt-4">
    <p class="text-sm">Goldstein-Price function shown. One global minimum (f = 3), three local minima.</p>
  </div>
</div>

<div class="col-span-6 col-start-7 flex flex-col justify-center items-center">
  <DPSearchLandscape />
</div>

</div>

---

<div class="swiss-grid">

<div class="col-span-12 hairline-bottom pb-6 mb-6">
  <div class="label-small accent-text mb-4">04 / No Free Lunch</div>
  <h1>No algorithm dominates</h1>
  <p class="mt-4 w-2/3">Averaged over all possible problems, every search algorithm performs the same as random search.</p>
</div>

<div class="col-span-6 hairline-right pr-6">
  <p class="label-small mb-4" style="color:#111;">The NFL theorem (Wolpert & Macready, 1997)</p>
  <div class="p-4" style="background:#f2f2ef;">
    $$ \sum_{P \in \mathcal{P}} \mathbb{E}[f(A, P)] = \text{const} \quad \forall A $$
  </div>
  <p class="text-sm mt-4">Any algorithm's wins on some problems are exactly balanced by its losses on others.</p>
</div>

<div class="col-span-6 pl-6 flex flex-col items-center justify-center">
  <DPNFLBars />
  <p class="text-sm mt-4" style="color:#555;">Performance of algorithm A across six problem classes. The red line is the average — same for all algorithms.</p>
</div>

</div>

---

<div class="swiss-grid">

<div class="col-span-5 h-full hairline-right pr-6 flex flex-col justify-center">
  <div class="label-small accent-text mb-4">05 / The Menagerie</div>
  <h1>Metaheuristics are strategies, not formulas</h1>
  <p class="mt-4">They trade guarantees for generality. No optimality proof. No runtime bound. In exchange: they work on problems where exact methods cannot even start.</p>
</div>

<div class="col-span-6 col-start-7 flex flex-col justify-center items-center" style="max-height:80%;overflow:hidden;">
  <img src="./assets/metaheuristics_classification.svg" style="max-width:100%;height:auto;" />
</div>

</div>

---

<div class="swiss-grid">

<div class="col-span-12 hairline-bottom pb-6 mb-6">
  <div class="label-small accent-text mb-4">06 / The Central Trade-off</div>
  <h1>Explore vs Exploit</h1>
  <p class="mt-4 w-2/3">Every metaheuristic allocates budget between exploring new regions and refining known good ones.</p>
</div>

<div class="col-span-7 flex flex-col items-center justify-center">
  <DPSearchLandscape showExploration />
</div>

<div class="col-span-4 col-start-9 hairline-left pl-6 flex flex-col justify-center">
  <div class="hairline-bottom pb-4 mb-4">
    <div style="font-size:36px;font-weight:700;line-height:1.1;color:#333;">Exploitation</div>
    <p class="text-sm mt-1">Refine the current best. Local search around promising regions.</p>
  </div>
  <div>
    <div style="font-size:36px;font-weight:700;line-height:1.1;color:#555;">Exploration</div>
    <p class="text-sm mt-1">Search broadly. Visit distant regions to find new attractor basins.</p>
  </div>
</div>

</div>

---

<div class="swiss-grid">

<div class="col-span-6 col-start-1 h-full hairline-right pr-6 flex flex-col justify-center">
  <div class="label-small accent-text mb-4">07 / Simulated Annealing</div>
  <h1>Escaping local optima by controlled randomness</h1>
  <p class="mt-4">SA accepts worse solutions with probability $$P = e^{-\Delta / T}$$. Temperature T starts high (lots of exploration) and cools toward zero (pure exploitation).</p>
  <div class="hairline-top pt-4 mt-4">
    <p class="text-sm">If T cools slowly enough, SA is guaranteed to find the global optimum (with probability → 1 as time → ∞).</p>
  </div>
</div>

<div class="col-span-5 col-start-8 flex flex-col items-center justify-center">
  <DPSearchLandscape showSATrajectory />
  <p class="text-sm mt-2" style="color:#555;">Red path: SA trajectory. Early steps jump freely; later steps converge to the global basin.</p>
</div>

</div>

---

<div class="swiss-grid">

<div class="col-span-12 hairline-bottom pb-6 mb-6">
  <div class="label-small accent-text mb-4">08 / Cooling Schedules</div>
  <h1>How fast to cool determines success</h1>
  <p class="mt-4 w-2/3">The cooling schedule is the algorithm. Too fast — freeze into a local optimum. Too slow — waste evaluations.</p>
</div>

<div class="col-span-6 hairline-right pr-6">
  <p class="label-small mb-4" style="color:#111;">Acceptance probability</p>
  <div class="p-4" style="background:#f2f2ef;">
    $$ P(\text{accept}) = \min\left(1,\; e^{-\Delta / T}\right) $$
  </div>
  <div class="hairline-top pt-4 mt-4">
    <p class="label-small mb-4" style="color:#111;">Common schedules</p>
    <div class="p-4" style="background:#f2f2ef;">
      $$ T_k = T_0 \cdot \alpha^k \quad (\text{exponential}) $$
      $$ T_k = T_0 / \log(k + 1) \quad (\text{logarithmic}) $$
      $$ T_k = T_0 \cdot (1 - k/K) \quad (\text{linear}) $$
    </div>
  </div>
</div>

<div class="col-span-6 pl-6 flex flex-col justify-center">
  <p class="label-small mb-4" style="color:#111;">Hajek's condition for convergence</p>
  <div class="p-4" style="background:#f2f2ef;">
    $$ \sum_{k=1}^{\infty} e^{-\delta / T_k} = \infty $$
  </div>
  <p class="text-sm mt-4">If the cooling schedule satisfies this, SA converges to the global optimum with probability 1. Logarithmic cooling satisfies it. Exponential does not.</p>
</div>

</div>

---

<div class="swiss-grid">

<div class="col-span-5 h-full hairline-right pr-6 flex flex-col justify-center">
  <div class="label-small accent-text mb-4">09 / Genetic Algorithm</div>
  <h1>Breeding solutions through selection, crossover, and mutation</h1>
  <p class="mt-4">A population of candidate solutions evolves. Fit individuals reproduce. Their offspring inherit traits from both parents, plus random mutations.</p>
</div>

<div class="col-span-6 col-start-7 flex flex-col items-center justify-center">
  <DPSearchLandscape showGAPopulation />
  <p class="text-sm mt-2" style="color:#555;">Grey dots: population individuals spread across the landscape, concentrated in promising basins.</p>
</div>

</div>

---

<div class="swiss-grid">

<div class="col-span-12 hairline-bottom pb-6 mb-6">
  <div class="label-small accent-text mb-4">10 / GA Flow</div>
  <h1>Selection, crossover, mutation — repeat</h1>
  <p class="mt-4 w-2/3">A single iteration cycle: evaluate fitness, select parents, produce offspring, mutate, replace.</p>
</div>

<div class="col-span-12 flex justify-center">
  <img src="./assets/ga_flowchart_arxiv-2.png" style="max-height:480px;border:1px solid rgba(17,17,17,0.15);" />
</div>

</div>

---

<div class="swiss-grid">

<div class="col-span-5 h-full hairline-right pr-6 flex flex-col justify-center">
  <div class="label-small accent-text mb-4">11 / Schema Theorem</div>
  <h1>Building blocks of good solutions grow exponentially</h1>
  <p class="mt-4">Holland's schema theorem: short, low-order schemata with above-average fitness receive exponentially increasing trials in subsequent generations.</p>
</div>

<div class="col-span-6 col-start-7 flex flex-col justify-center">
  <p class="label-small mb-4" style="color:#111;">Expected number of schema H copies at generation t+1</p>
  <div class="p-4" style="background:#f2f2ef;">
    $$ \mathbb{E}[m(H, t+1)] \geq m(H, t) \cdot \frac{\hat{f}(H, t)}{\bar{f}(t)} \cdot \left(1 - p_c \cdot \frac{\delta(H)}{L-1} - p_m \cdot o(H)\right) $$
  </div>
  <div class="hairline-top pt-4 mt-4">
    <table style="font-size:12px;width:100%;">
      <tbody>
      <tr><td style="padding:4px 8px;"><b>m(H, t)</b></td><td>number of schema H instances at generation t</td></tr>
      <tr><td style="padding:4px 8px;"><b>f̂(H, t)</b></td><td>average fitness of schema H</td></tr>
      <tr><td style="padding:4px 8px;"><b>f̄(t)</b></td><td>average population fitness</td></tr>
      <tr><td style="padding:4px 8px;"><b>δ(H)</b></td><td>defining length of schema</td></tr>
      <tr><td style="padding:4px 8px;"><b>o(H)</b></td><td>order (fixed positions) of schema</td></tr>
      </tbody>
    </table>
  </div>
</div>

</div>

---

<div class="swiss-grid">

<div class="col-span-6 col-start-1 h-full hairline-right pr-6 flex flex-col justify-center">
  <div class="label-small accent-text mb-4">12 / Particle Swarm</div>
  <h1>Collective intelligence through velocity updates</h1>
  <p class="mt-4">Each particle remembers its best-known position and the swarm's global best. Velocity blends personal history, social influence, and inertia.</p>
  <div class="hairline-top pt-4 mt-4">
    <p class="text-sm">No crossover. No selection. Just three weighted forces pulling each particle through the space.</p>
  </div>
</div>

<div class="col-span-5 col-start-8 flex flex-col items-center justify-center">
  <DPSearchLandscape showPSOSwarm />
  <p class="text-sm mt-2" style="color:#555;">Red dots: particles with velocity vectors pointing toward their personal + global best.</p>
</div>

</div>

---

<div class="swiss-grid">

<div class="col-span-12 hairline-bottom pb-6 mb-6">
  <div class="label-small accent-text mb-4">13 / PSO Velocity</div>
  <h1>Three forces, one update rule</h1>
  <p class="mt-4 w-2/3">Inertia keeps the particle moving. Cognitive component pulls it toward its own best. Social component pulls it toward the swarm's best.</p>
</div>

<div class="col-span-6 hairline-right pr-6">
  <div class="p-4" style="background:#f2f2ef;">
    $$ v_{i}(t+1) = w \cdot v_{i}(t) + c_1 r_1 (p_i - x_i(t)) + c_2 r_2 (g - x_i(t)) $$
  </div>
  <div class="p-4 mt-4" style="background:#f2f2ef;">
    $$ x_{i}(t+1) = x_{i}(t) + v_{i}(t+1) $$
  </div>
  <div class="hairline-top pt-4 mt-4">
    <table style="font-size:12px;width:100%;">
      <tbody>
      <tr><td style="padding:2px 8px;">w</td><td>inertia weight</td></tr>
      <tr><td style="padding:2px 8px;">c₁, c₂</td><td>cognitive / social acceleration</td></tr>
      <tr><td style="padding:2px 8px;">r₁, r₂</td><td>random ∈ [0,1]</td></tr>
      <tr><td style="padding:2px 8px;">p_i</td><td>particle's personal best</td></tr>
      <tr><td style="padding:2px 8px;">g</td><td>swarm's global best</td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="col-span-5 col-start-8 flex flex-col justify-center items-center">
  <img src="./assets/vector_subtraction.svg" style="max-width:180px;" />
  <p class="text-sm mt-2" style="color:#555;">Vector subtraction: the direction from current position to a known best.</p>
</div>

</div>

---

<div class="swiss-grid">

<div class="col-span-12 hairline-bottom pb-6 mb-6">
  <div class="label-small accent-text mb-4">14 / Comparison</div>
  <h1>Three strategies, one skeleton</h1>
</div>

<div class="col-span-4 hairline-right pr-6">
  <div class="hairline-bottom pb-4 mb-4">
    <div class="label-small accent-text">SA</div>
    <p class="text-sm mt-1">Single walker. Accepts worst solutions probabilistically. Temperature controls exploration. Guaranteed convergence with logarithmic cooling.</p>
  </div>
  <p class="text-sm"><b>Best for:</b> rugged landscapes, any-time stopping</p>
</div>

<div class="col-span-4 hairline-right pr-6">
  <div class="hairline-bottom pb-4 mb-4">
    <div class="label-small accent-text">GA</div>
    <p class="text-sm mt-1">Population-based. Recombines building blocks via crossover. Schema theorem explains why good partial solutions spread.</p>
  </div>
  <p class="text-sm"><b>Best for:</b> combinatorial optimization, discrete search spaces</p>
</div>

<div class="col-span-4">
  <div class="hairline-bottom pb-4 mb-4">
    <div class="label-small accent-text">PSO</div>
    <p class="text-sm mt-1">Swarm-based. Three-parameter velocity update. No crossover, no selection pressure gradient — just attraction to known bests.</p>
  </div>
  <p class="text-sm"><b>Best for:</b> continuous optimization, real-parameter problems</p>
</div>

</div>

---

<div class="swiss-grid">

<div class="col-span-12 hairline-bottom pb-6 mb-6">
  <div class="label-small accent-text mb-4">15 / Convergence</div>
  <h1>Different mechanisms, different trajectories</h1>
  <p class="mt-4 w-2/3">SA converges smoothly (slow but steady). GA converges in steps (discovery of building blocks). PSO converges fast (directed pull) but can stagnate.</p>
</div>

<div class="col-span-12 flex justify-center">
  <DPConvergence />
</div>

</div>

---

<div class="swiss-grid">

<div class="col-span-12 hairline-bottom pb-6 mb-6">
  <div class="label-small accent-text mb-4">16 / The Common Structure</div>
  <h1>Every metaheuristic follows the same loop</h1>
  <p class="mt-4 w-2/3">Initialize → Evaluate → Generate → Accept → Repeat. The differences are in the Generate and Accept steps.</p>
</div>

<div class="col-span-12 flex justify-center">
  <v-clicks>
    <DPAlgorithmSkeleton variant="generic" />
  </v-clicks>
</div>

</div>

---

<div class="swiss-grid">

<div class="col-span-12 hairline-bottom pb-6 mb-6">
  <div class="label-small mb-4" style="opacity:0.8;">Loop Closure</div>
  <h1>Remember the opening question?</h1>
</div>

<div class="col-span-6 hairline-right pr-6">
  <p class="text-xl" style="color:var(--text-primary);">10<sup>100</sup> solutions. You can test 10<sup>9</sup>.</p>
  <p class="mt-4">Metaheuristics don't find the best answer. They find a good answer fast, by exploiting problem structure and exploring strategically.</p>
  <p class="mt-4">SA, GA, and PSO are three different answers to the same question: <b>how do you allocate the budget between exploration and exploitation?</b></p>
</div>

<div class="col-span-5 col-start-8 flex flex-col justify-center">
  <div class="hairline-bottom pb-4 mb-4">
    <div class="label-small accent-text">SA</div>
    <p class="text-sm">Temperature controls the explore/exploit ratio over time</p>
  </div>
  <div class="hairline-bottom pb-4 mb-4">
    <div class="label-small accent-text">GA</div>
    <p class="text-sm">Population diversity + recombination maintain exploration</p>
  </div>
  <div>
    <div class="label-small accent-text">PSO</div>
    <p class="text-sm">Personal vs social memory balances the two forces</p>
  </div>
</div>

</div>
