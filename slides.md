---
theme: default
title: Introduction to Metaheuristics
colorSchema: light
transition: fade
mdc: true
---

<!--
COLOR LEGEND (deck-wide, do not violate):
  #e8703a  orange  = exploitation / current best / accepted move
  #3b6fe0  blue    = exploration / candidate move / new area searched
  #cc3333  red     = local optimum / trap / rejected
  #2e8b57  green   = global optimum / target solution
  #1a1f36  navy    = section divider background only
-->

<style>
.hill-svg { width: 100%; max-width: 620px; margin: 0 auto; display:block; }
.legend-dot { display:inline-block; width:10px; height:10px; border-radius:50%; margin-right:6px; }
</style>

# Introduction to Metaheuristics

### Search strategies for problems too large to solve exactly

<div class="pt-12 text-sm opacity-60">
Exact methods guarantee the best answer. Metaheuristics trade that guarantee for speed.
</div>

---
layout: center
class: text-white
style: background:#1a1f36
---

# The problem

---

# Exact search explodes long before problems get interesting

<div class="grid grid-cols-2 gap-8 pt-6">
<div>

**Traveling Salesman Problem**
checking every route through *n* cities

| Cities | Possible routes |
|---|---|
| 5 | 12 |
| 10 | 181,440 |
| 15 | 43,589,145,600 |
| 20 | 6.1 × 10¹⁶ |

</div>
<div class="flex items-center justify-center text-sm opacity-70">
At 20 cities, checking every route on today's fastest computer
still takes longer than the age of the universe.
</div>
</div>

---

# A greedy heuristic finds *a* solution fast — often the wrong one

<svg class="hill-svg" viewBox="0 0 700 300">
  <path d="M0,220 C100,220 120,120 200,130 C280,140 300,250 400,240 C480,230 500,60 560,70 C620,80 650,180 700,200"
        stroke="#334155" fill="none" stroke-width="3"/>
  <circle cx="205" cy="128" r="10" fill="#cc3333"/>
  <text x="150" y="105" font-size="15" fill="#cc3333">greedy search stops here</text>
  <text x="470" y="50" font-size="15" fill="#334155" opacity="0.5">true best solution</text>
</svg>

<div class="text-center pt-4 text-sm opacity-70">
A greedy hill-climber takes the first improving step it finds — and stays there.
It has no way to know a deeper valley exists further along.
</div>

---

# Metaheuristics guide the search past that trap

<svg class="hill-svg" viewBox="0 0 700 300">
  <path d="M0,220 C100,220 120,120 200,130 C280,140 300,250 400,240 C480,230 500,60 560,70 C620,80 650,180 700,200"
        stroke="#334155" fill="none" stroke-width="3"/>
  <circle cx="205" cy="128" r="8" fill="#cc3333" opacity="0.4"/>
  <path d="M205,128 Q350,20 560,68" stroke="#3b6fe0" stroke-width="2.5" stroke-dasharray="6,5" fill="none"/>
  <circle cx="560" cy="68" r="10" fill="#2e8b57"/>
  <text x="330" y="20" font-size="15" fill="#3b6fe0">deliberately accepted a worse move</text>
</svg>

<div class="text-center pt-4 text-sm opacity-70">
Every metaheuristic in this deck does one thing a greedy search refuses to do:
sometimes step toward a <em>worse</em> solution on purpose, to see what's past it.
</div>

---

# Every metaheuristic balances exploring against exploiting

<svg class="hill-svg" viewBox="0 0 700 300">
  <path d="M0,220 C100,220 120,120 200,130 C280,140 300,250 400,240 C480,230 500,60 560,70 C620,80 650,180 700,200"
        stroke="#334155" fill="none" stroke-width="3"/>
  <circle cx="205" cy="128" r="9" fill="#cc3333" opacity="0.5"/>
  <circle cx="560" cy="68" r="9" fill="#2e8b57" opacity="0.5"/>
  <path d="M205,150 L340,230" stroke="#3b6fe0" stroke-width="3" marker-end="url(#arrowblue)"/>
  <path d="M205,150 L260,175" stroke="#e8703a" stroke-width="3" marker-end="url(#arroworange)"/>
  <defs>
    <marker id="arrowblue" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto">
      <path d="M0,0 L8,4 L0,8 Z" fill="#3b6fe0"/>
    </marker>
    <marker id="arroworange" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto">
      <path d="M0,0 L8,4 L0,8 Z" fill="#e8703a"/>
    </marker>
  </defs>
  <text x="345" y="245" font-size="14" fill="#3b6fe0">explore: jump somewhere new</text>
  <text x="255" y="195" font-size="14" fill="#e8703a">exploit: refine what's working</text>
</svg>

<div class="text-center pt-4 text-sm">
<span class="legend-dot" style="background:#3b6fe0"></span>exploration
&nbsp;&nbsp;
<span class="legend-dot" style="background:#e8703a"></span>exploitation
&nbsp;&nbsp; — this pair of colors means the same thing for the rest of the deck.
</div>

---
layout: center
class: text-white
style: background:#1a1f36
---

# Trajectory methods
### Simulated annealing

---

# Simulated annealing accepts worse moves early, rarely late

<div class="grid grid-cols-2 gap-6 items-center pt-4">
<svg viewBox="0 0 350 260">
  <path d="M0,190 C50,190 60,100 100,110 C140,120 150,210 200,200 C240,195 250,40 280,50 C310,60 330,140 350,160"
        stroke="#334155" fill="none" stroke-width="3"/>
  <circle cx="60" cy="150" r="6" fill="#e8703a"><animate attributeName="cx" values="60;140;200;280;280" dur="4s" repeatCount="indefinite"/><animate attributeName="cy" values="150;190;195;55;55" dur="4s" repeatCount="indefinite"/></circle>
</svg>
<div class="text-sm">

High <strong style="color:#3b6fe0">temperature</strong> → the search accepts almost
any move, wandering freely across the landscape.

As temperature drops, it accepts fewer and fewer worse moves, until it
only ever steps downhill — settling near the deepest valley it found
while it still had freedom to wander.

</div>
</div>

---

# Acceptance probability decays with temperature, not with luck

<div class="pt-6 text-center text-2xl font-mono">
P(accept) = exp( − ΔE / T )
</div>

<div class="grid grid-cols-3 gap-4 pt-8 text-sm">
<div v-click class="p-4 border rounded">
<strong style="color:#cc3333">ΔE</strong> — how much worse the new
solution is. Bigger jump down in quality, smaller chance it's accepted.
</div>
<div v-click class="p-4 border rounded">
<strong style="color:#3b6fe0">T</strong> — temperature. High T makes
even a big ΔE tolerable; low T makes even a small ΔE rejected.
</div>
<div v-click class="p-4 border rounded">
<strong style="color:#e8703a">P</strong> — the resulting probability
the worse move gets accepted anyway, on this step.
</div>
</div>

---
layout: center
class: text-white
style: background:#1a1f36
---

# Population methods
### Genetic algorithms

---

# A population searches many solutions in parallel, not just one

<div class="flex justify-center pt-8">
<svg viewBox="0 0 500 200">
  <circle cx="60" cy="40" r="7" fill="#3b6fe0"/>
  <circle cx="120" cy="90" r="7" fill="#3b6fe0"/>
  <circle cx="90" cy="150" r="7" fill="#3b6fe0"/>
  <circle cx="180" cy="60" r="7" fill="#3b6fe0"/>
  <circle cx="220" cy="130" r="7" fill="#3b6fe0"/>
  <circle cx="270" cy="30" r="7" fill="#3b6fe0"/>
  <circle cx="300" cy="170" r="7" fill="#3b6fe0"/>
  <circle cx="350" cy="90" r="7" fill="#3b6fe0"/>
  <circle cx="400" cy="50" r="7" fill="#3b6fe0"/>
  <circle cx="440" cy="140" r="7" fill="#3b6fe0"/>
  <text x="150" y="195" font-size="13" fill="#334155" opacity="0.6">generation 0 — a random population of candidate solutions</text>
</svg>
</div>

---

# Selection keeps the fittest, crossover recombines, mutation adds noise

<div class="grid grid-cols-3 gap-6 pt-6 text-sm">

<div v-click>
<div class="font-bold pb-2" style="color:#e8703a">1. Selection</div>
Solutions that scored well are more likely to be chosen as parents
for the next generation. Weak solutions are gradually filtered out.
</div>

<div v-click>
<div class="font-bold pb-2" style="color:#3b6fe0">2. Crossover</div>
Two parent solutions swap parts of their structure, producing a
child that inherits traits from both.
</div>

<div v-click>
<div class="font-bold pb-2" style="color:#cc3333">3. Mutation</div>
A small random change is applied to a child solution — the source
of new genetic material the population didn't already have.
</div>

</div>

<div v-click class="text-center pt-8 text-sm opacity-70">
Repeat for many generations: the population's average fitness rises
even though no single solution was ever solved for directly.
</div>

---
layout: center
class: text-white
style: background:#1a1f36
---

# Swarm methods
### Particle swarm optimization

---

# Every particle remembers its own best position and the swarm's best

<div class="flex justify-center pt-6">
<svg viewBox="0 0 500 220">
  <circle cx="420" cy="60" r="10" fill="#2e8b57"/>
  <text x="435" y="65" font-size="12" fill="#2e8b57">swarm best</text>

  <circle cx="80" cy="150" r="6" fill="#3b6fe0"/>
  <path d="M80,150 L200,110" stroke="#e8703a" stroke-width="2" stroke-dasharray="4,4"/>
  <circle cx="200" cy="110" r="4" fill="#e8703a"/>
  <text x="30" y="175" font-size="11" fill="#334155" opacity="0.6">particle + its own best</text>
  <path d="M80,150 L410,65" stroke="#3b6fe0" stroke-width="1.5" stroke-dasharray="2,4" opacity="0.5"/>

  <circle cx="160" cy="40" r="6" fill="#3b6fe0"/>
  <path d="M160,40 L410,58" stroke="#3b6fe0" stroke-width="1.5" stroke-dasharray="2,4" opacity="0.5"/>

  <circle cx="300" cy="170" r="6" fill="#3b6fe0"/>
  <path d="M300,170 L415,68" stroke="#3b6fe0" stroke-width="1.5" stroke-dasharray="2,4" opacity="0.5"/>
</svg>
</div>

<div class="text-center pt-2 text-sm opacity-70">
<span style="color:#e8703a">orange</span> = a particle's personal best find &nbsp;·&nbsp;
<span style="color:#2e8b57">green</span> = the best any particle in the swarm has found
</div>

---

# Each particle's next move blends memory, swarm knowledge, and randomness

<div class="pt-6 text-center text-xl font-mono">
v ← v + c₁·rand·(pbest − x) + c₂·rand·(gbest − x)
</div>

<div class="grid grid-cols-3 gap-4 pt-8 text-sm">
<div v-click class="p-4 border rounded">
<strong style="color:#3b6fe0">v</strong> — the particle's current
velocity, carried over from its last move (momentum).
</div>
<div v-click class="p-4 border rounded">
<strong style="color:#e8703a">pbest − x</strong> — pull back toward
this particle's own best-known position.
</div>
<div v-click class="p-4 border rounded">
<strong style="color:#2e8b57">gbest − x</strong> — pull toward the
best position found anywhere in the swarm.
</div>
</div>

---

# No metaheuristic guarantees the optimum — all trade certainty for speed

| | Exact search | Metaheuristic |
|---|---|---|
| Guarantees best answer | yes | no |
| Scales to large problems | no | yes |
| Runtime | grows combinatorially | bounded, tunable |
| Typical use | small / structured problems | large, messy, real-world problems |

---
layout: center
---

# Checkpoint

<div class="text-xl pt-6 text-center max-w-xl mx-auto">
Simulated annealing sometimes accepts a move that makes the solution
<em>worse</em>. Why does that improve its chances of finding the
global optimum, instead of just wasting time?
</div>

---

# Three families, one shared idea: balance exploring against exploiting

<div class="grid grid-cols-3 gap-6 pt-6 text-sm text-center">
<div>
<div class="font-bold pb-2">Simulated annealing</div>
one solution, temperature controls how freely it wanders
</div>
<div>
<div class="font-bold pb-2">Genetic algorithms</div>
a population, evolved generation by generation
</div>
<div>
<div class="font-bold pb-2">Particle swarm</div>
many solutions, pulled by memory and shared knowledge
</div>
</div>

<div class="text-center pt-8 text-sm opacity-70">
Different mechanisms, same trade: give up the guarantee of the exact
answer, in exchange for finding a very good answer fast.
</div>
