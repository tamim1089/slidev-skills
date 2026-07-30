import os

BASE = "/home/hex/University/Fall26/Educational/Slides/slidev-skills"

L = []
def A(s=""):
    L.append(s + "\n")

A("""
---
theme: default
title: Introduction to Metaheuristics
titleTemplate: '%s'
info: A discovery-arc deck on metaheuristics via TSP, simulated annealing, and genetic algorithms
author: Slidev Skills
keywords: metaheuristics,simulated annealing,genetic algorithms,optimization
transition: slide-left
colorSchema: dark
routerMode: hash
fonts:
  sans: Inter
  mono: JetBrains Mono
defaults:
  layout: default
layout: cover
---

# Introduction to Metaheuristics

When perfect is too expensive

<div class="muted-text mt-4">
A discovery-arc deck
</div>

---
layout: default
---

# You have 50 cities

<div class="grid grid-cols-2 gap-6 items-center">
<div>
<p>Visit each exactly once. Shortest route back to start.</p>
<p class="muted-text mt-4">This is the Traveling Salesman Problem - TSP.</p>
</div>
<div class="card">
<p class="muted-text">50 cities - 49! possible routes</p>
</div>
</div>

---
layout: default
---

# 49! is not a big number. It is an impossible one.

<div class="grid grid-cols-3 gap-6 mt-8">
<div class="card text-center">
<div class="hero-stat">49!</div>
<p class="muted-text mt-2">Possible routes</p>
</div>
<div class="card text-center">
<div class="hero-stat" style="color:var(--warning)">6 x 10<sup>62</sup></div>
<p class="muted-text mt-2">Routes in standard form</p>
</div>
<div class="card text-center">
<div class="hero-stat" style="color:var(--danger)">Infinite</div>
<p class="muted-text mt-2">Brute force feasibility</p>
</div>
</div>

<p class="mt-6">More possible routes than atoms in the Milky Way. Brute force at a trillion checks per second takes longer than the Sun lifetime.</p>

---
layout: default
---

# What if we just pick the nearest unvisited city?

<div class="grid grid-cols-2 gap-6 mt-6">
<div>
<p>The nearest-neighbor heuristic: start anywhere, always go to the closest city you have not visited yet.</p>
<p class="muted-text mt-4">Simple. Obvious. Fast. And the route is usually 25-40% longer than optimal.</p>
</div>
<div class="card">
<p>Route length: 14,327 km</p>
<p>Known optimal: 10,241 km</p>
<p>Wasted: 4,086 km</p>
<p>Greedy leaves money on the table.</p>
</div>
</div>

---
layout: default
---

# The combinatorial explosion

<div class="grid grid-cols-2 gap-8 items-center">
<div>
<div class="card">
<div class="flex justify-between mb-2"><span>Cities</span><span style="color:var(--accent)">Routes</span></div>
<div class="flex justify-between mb-1"><span class="muted-text">5</span><span>120</span></div>
<div class="flex justify-between mb-1"><span class="muted-text">10</span><span>3.6 million</span></div>
<div class="flex justify-between mb-1"><span class="muted-text">15</span><span>87 billion</span></div>
<div class="flex justify-between mb-1"><span class="muted-text">20</span><span style="color:var(--danger)">2.4 x 10<sup>18</sup></span></div>
<div class="flex justify-between"><span class="muted-text">50</span><span style="color:var(--danger)">6 x 10<sup>62</sup></span></div>
</div>
</div>
<div>
<p style="font-size:2rem;color:var(--accent)">n!</p>
<p>n! grows faster than any polynomial.</p>
<p class="muted-text mt-4">At 20 cities, exhaustive search is already impractical. At 50, it is physically impossible.</p>
</div>
</div>

---
layout: default
---

# So how do delivery companies solve this?

<div class="card text-center mt-8" style="padding:3rem">
<p style="font-size:2rem; font-weight:700">Thousands of routes per day. Millions of stops.</p>
<p class="muted-text mt-4" style="font-size:1.3rem">They cannot brute force. They cannot afford optimal. They need good enough, fast enough.</p>
</div>

---
layout: default
---

# What if we do not need the absolute best?

<div class="grid grid-cols-3 gap-6 mt-8 text-center">
<div class="card">
<div style="font-size:2.5rem; font-weight:800; color:var(--success)">Optimal</div>
<p class="muted-text mt-2">Exhaustive search. Works for n less than 20. Fails for everything real.</p>
</div>
<div class="card" style="border-color:var(--accent)">
<div style="font-size:2.5rem; font-weight:800; color:var(--accent)">Good enough</div>
<p class="muted-text mt-2">Within 2-5% of optimal. Takes seconds, not centuries.</p>
</div>
<div class="card">
<div style="font-size:2.5rem; font-weight:800; color:var(--danger)">Fast garbage</div>
<p class="muted-text mt-2">Greedy heuristics. Fast but wasteful.</p>
</div>
</div>

---
layout: default
---

# Imagine a ball bearing on a metal surface

<div class="grid grid-cols-2 gap-6 items-center">
<div>
<p>The ball wants to roll downhill. The lowest point is the optimal solution.</p>
<p class="mt-4">But the surface is bumpy. The ball gets trapped in dimples. Local optima.</p>
<p class="muted-text mt-4">The ball does not know which dimple is the deepest.</p>
</div>
<div class="card">
<pre>
  \  /
   \/    __
   / \__/  \__
  /          \___
 /               \___
 Energy landscape
 (x = solution, y = cost)</pre>
</div>
</div>

---
layout: default
---

# Shake the table

<div class="grid grid-cols-2 gap-6 items-center">
<div>
<p>High temperature = lots of shaking. The ball can bounce out of any dimple.</p>
<p class="mt-4">Low temperature = calm surface. The ball settles in the deepest valley it can find.</p>
<p class="muted-text mt-4">This is the core idea behind Simulated Annealing.</p>
</div>
<div class="card text-center">
<div style="font-size:1.5rem">
High T
<div style="height:3px;background:var(--accent);width:100%;margin:8px 0"></div>
Low T
</div>
<p class="muted-text mt-2">Temperature controls how much randomness we allow.</p>
</div>
</div>

---
layout: default
---

# The cooling schedule

<div class="grid grid-cols-2 gap-8 items-center">
<div class="card text-center">
<pre style="font-size:1rem">
T
|
|         __
|     __/
|  __/
|_/
|/___________________ time
</pre>
<p class="muted-text mt-2">Temperature decreases over time. Fast at first, then slower.</p>
</div>
<div>
<p>High T: explore freely. Accept worse solutions.</p>
<p>Mid T: mostly exploit. Some exploration.</p>
<p>Low T: pure exploit. Only accept improvements.</p>
</div>
</div>

---
layout: default
---

# Let us write this down

<div class="grid grid-cols-2 gap-6 items-center">
<div>
<p>If a new solution is better: take it.</p>
<p>If it is worse: take it with probability</p>
<div class="card text-center mt-4" style="font-size:1.8rem; font-weight:700; color:var(--accent)">
P = e<sup>-ΔE/T</sup>
</div>
</div>
<div>
<p class="muted-text"><strong>ΔE</strong> = how much worse the new solution is</p>
<p class="muted-text mt-2"><strong>T</strong> = remaining temperature (shaking)</p>
<p class="muted-text mt-2"><strong>e<sup>-ΔE/T</sup></strong> = high when T is high (accept anything), low when T is low (only accept good moves)</p>
</div>
</div>

---
layout: default
---

# Simulated Annealing, step by step

```mermaid {theme: dark, scale: 0.9}
flowchart TD
  A[Start with random solution] --> B[Pick neighbor solution]
  B --> C{Is neighbor better?}
  C -->|Yes| D[Accept neighbor]
  C -->|No| E[Accept with probability e^{-ΔE/T}]
  D --> F[Cool down: T = T * alpha]
  E --> F
  F --> G{Still above T_min?}
  G -->|Yes| B
  G -->|No| H[Return best solution found]
```

<p class="muted-text mt-2 text-sm">Alpha (cooling rate) is usually 0.95-0.99. Slower cooling = better results.</p>

---
layout: default
---

# Greedy vs Simulated Annealing

<div class="grid grid-cols-3 gap-6 mt-6 text-center">
<div class="card">
<div style="font-size:1.8rem; font-weight:700">Greedy</div>
<div class="hero-stat mt-4" style="font-size:2.5rem; color:var(--danger)">14,327 km</div>
<p class="muted-text mt-2">Fast. Wasteful. Stuck.</p>
</div>
<div class="card" style="border-color:var(--accent)">
<div style="font-size:1.8rem; font-weight:700; color:var(--accent)">SA</div>
<div class="hero-stat mt-4" style="font-size:2.5rem; color:var(--accent)">10,512 km</div>
<p class="muted-text mt-2">Within 2.6% of optimal.</p>
</div>
<div class="card">
<div style="font-size:1.8rem; font-weight:700; color:var(--success)">Optimal</div>
<div class="hero-stat mt-4" style="font-size:2.5rem; color:var(--success)">10,241 km</div>
<p class="muted-text mt-2">Impossible at scale.</p>
</div>
</div>
<p class="mt-6 text-center" style="font-size:1.3rem;color:var(--accent)">SA found a route 27% shorter than greedy. In seconds, not millennia.</p>

---
layout: default
---

# This is a metaheuristic

<div class="card text-center mt-8" style="padding:2.5rem; border-color:var(--accent)">
<p style="font-size:1.8rem; font-weight:700">Metaheuristic: a high-level strategy that guides a lower-level heuristic to escape local optima.</p>
</div>
<p class="mt-6">Simulated Annealing is one example. The idea is general: how do you avoid getting stuck while still making progress?</p>

---
layout: default
---

# The explore/exploit tradeoff

<div class="grid grid-cols-2 gap-6 mt-6">
<div class="card text-center">
<div style="font-size:1.5rem; font-weight:700; color:var(--accent)">Explore</div>
<p class="muted-text">Try completely new regions of the search space. High risk, high reward.</p>
</div>
<div class="card text-center">
<div style="font-size:1.5rem; font-weight:700; color:var(--accent)">Exploit</div>
<p class="muted-text">Refine the best solution found so far. Safe but limited.</p>
</div>
</div>
<p class="mt-4 text-center">Every metaheuristic is a recipe for balancing these two forces.</p>

---
layout: default
---

# Two more metaheuristics

<div class="grid grid-cols-2 gap-6 mt-6">
<div class="card">
<div style="font-size:1.3rem; font-weight:700; color:var(--accent)">Genetic Algorithms</div>
<p class="mt-2">Keep a population of solutions. Select the best, combine them (crossover), mutate randomly. Repeat.</p>
<p class="muted-text mt-2">Explore via mutation. Exploit via selection pressure.</p>
</div>
<div class="card">
<div style="font-size:1.3rem; font-weight:700; color:var(--accent)">Tabu Search</div>
<p class="mt-2">Greedy descent with a twist: forbid recent moves so you cannot cycle back to where you were stuck.</p>
<p class="muted-text mt-2">Explore via tabu list. Exploit via greedy selection.</p>
</div>
</div>

---
layout: default
---

# Same question, different answers

<div class="grid grid-cols-3 gap-4 mt-6 text-center">
<div class="card">
<div style="font-size:1.5rem; font-weight:700; color:var(--accent)">SA</div>
<p class="muted-text text-sm mt-2">Shake the table. Shake less over time.</p>
</div>
<div class="card">
<div style="font-size:1.5rem; font-weight:700; color:var(--accent)">GA</div>
<p class="muted-text text-sm mt-2">Evolve a population. Mix parents. Mutate children.</p>
</div>
<div class="card">
<div style="font-size:1.5rem; font-weight:700; color:var(--accent)">Tabu</div>
<p class="muted-text text-sm mt-2">Climb greedily. Remember where you were. Do not go back.</p>
</div>
</div>
<p class="mt-6 text-center" style="font-size:1.3rem;color:var(--accent)">Three strategies. One universal tension: explore vs exploit.</p>

---
layout: default
class: checkpoint-slide
---

# Checkpoint

<div class="card text-center" style="background:rgba(0,0,0,0.1);border:none;margin-top:2rem">
<p style="font-size:1.5rem; color:#0d0f12">You shake a ball bearing on a bumpy surface as it cools. The ball settles in the deepest valley. Which concept does this illustrate?</p>
</div>

<div class="grid grid-cols-2 gap-4 mt-8" style="max-width:600px;margin:2rem auto">
<div class="card" style="background:rgba(0,0,0,0.1);border:2px solid rgba(0,0,0,0.2)"><p style="color:#0d0f12;font-weight:700">A) Genetic Algorithms</p></div>
<div class="card" style="background:rgba(0,0,0,0.1);border:2px solid var(--accent)"><p style="color:#0d0f12;font-weight:700">B) Simulated Annealing</p></div>
<div class="card" style="background:rgba(0,0,0,0.1);border:2px solid rgba(0,0,0,0.2)"><p style="color:#0d0f12;font-weight:700">C) Greedy Search</p></div>
<div class="card" style="background:rgba(0,0,0,0.1);border:2px solid rgba(0,0,0,0.2)"><p style="color:#0d0f12;font-weight:700">D) Tabu Search</p></div>
</div>

---
layout: default
---

# Genetic Algorithms: the biological metaphor

<div class="grid grid-cols-2 gap-6 items-center">
<div>
<p>What if you kept a population of solutions and let them reproduce?</p>
<p class="mt-4"><strong>Selection:</strong> the better solutions are more likely to become parents.</p>
<p class="mt-2"><strong>Crossover:</strong> combine two parents to make a child.</p>
<p class="mt-2"><strong>Mutation:</strong> randomly tweak the child to keep diversity.</p>
<p class="muted-text mt-4">Repeat for many generations. The population evolves better solutions.</p>
</div>
<div class="card text-center">
<p>A population of candidate solutions evolves over generations.</p>
</div>
</div>

---
layout: default
---

# How a GA works

```mermaid {theme: dark, scale: 0.9}
flowchart LR
  A[Initial population] --> B[Evaluate fitness]
  B --> C[Select parents]
  C --> D[Crossover]
  D --> E[Mutation]
  E --> F[New generation]
  F --> B
```

---
layout: default
---

# Crossover on TSP

<div class="grid grid-cols-2 gap-6 items-center">
<div>
<p><span style="color:var(--accent)">Parent A:</span> A-B-C-D-E-F-G-H</p>
<p><span style="color:var(--accent)">Parent B:</span> A-D-G-B-E-C-F-H</p>
<p class="mt-4"><strong>Crossover</strong> picks a segment from Parent A and fills the rest from Parent B in order.</p>
<p class="mt-4"><span style="color:var(--accent)">Child:</span> A-B-C-D-G-E-F-H</p>
<p class="muted-text mt-4">The child inherits structural features from both parents.</p>
</div>
<div class="card">
<pre>
Parent A: [A-B-C-D-E-F-G-H]
Parent B: [A-D-G-B-E-C-F-H]
             ^^^^ segment
Child:   [A-B-C-D-G-E-F-H]
        ^^^^ from A
        rest from B</pre>
</div>
</div>

---
layout: default
---

# Mutation keeps things fresh

<div class="grid grid-cols-2 gap-6 items-center">
<div>
<p>Without mutation, the population converges too fast. Everyone becomes too similar.</p>
<p class="mt-4">Mutation randomly swaps two cities in a route.</p>
<p class="muted-text mt-4">A small mutation rate (0.5-1%) keeps exploration alive without destroying good solutions.</p>
</div>
<div class="card text-center">
<pre>
Before: A-B-C-D-E-F
             ^ ^
After:  A-B-E-D-C-F
     swapped C and E</pre>
</div>
</div>

---
layout: default
---

# The knobs we turn

<div class="grid grid-cols-3 gap-6 mt-6">
<div class="card text-center">
<div style="font-size:1.5rem; font-weight:700; color:var(--accent)">SA</div>
<div class="hero-stat mt-4" style="font-size:2rem">Cooling rate</div>
<p class="muted-text mt-2">How fast temperature drops. Fast = quick but risky. Slow = thorough but expensive.</p>
</div>
<div class="card text-center">
<div style="font-size:1.5rem; font-weight:700; color:var(--accent)">GA</div>
<div class="hero-stat mt-4" style="font-size:2rem">Mutation rate</div>
<p class="muted-text mt-2">How often we mutate. High = explore more. Low = exploit more.</p>
</div>
<div class="card text-center">
<div style="font-size:1.5rem; font-weight:700; color:var(--accent)">Tabu</div>
<div class="hero-stat mt-4" style="font-size:2rem">Tabu tenure</div>
<p class="muted-text mt-2">How long we forbid a move. Short = might cycle. Long = might miss good solutions.</p>
</div>
</div>

---
layout: default
---

# No free lunch

<div class="card mt-8" style="padding:2rem; border-color:var(--warning)">
<p style="font-size:1.3rem; font-weight:700">No metaheuristic is best for all problems.</p>
</div>
<p class="mt-6">SA works well for continuous landscapes. GA excels at discrete combinatorial problems. Tabu Search shines when the search space has strong local structure.</p>
<p class="muted-text mt-4">The No Free Lunch theorem (Wolpert and Macready, 1997) proves that averaged over all possible problems, all search algorithms perform equally. The art is picking the right one for your problem.</p>

---
layout: default
---

# Honest difficulty

<div class="card mt-8" style="padding:2rem">
<p style="font-size:1.3rem">Tuning the knobs (cooling schedule, mutation rate, tabu tenure) is still an art, not a science.</p>
</div>
<div class="card mt-4" style="padding:2rem">
<p style="font-size:1.3rem">People actively research how to adapt parameters automatically. Metaheuristics for tuning metaheuristics.</p>
</div>
<div class="card mt-4" style="padding:2rem">
<p style="font-size:1.3rem">You never know how far you are from the true optimum. That is the price of speed.</p>
</div>

---
layout: default
---

# So what do you actually lose?

<div class="grid grid-cols-2 gap-6 mt-8 items-center">
<div>
<p>You lose the guarantee of optimality.</p>
<p class="mt-4">You gain the ability to solve problems that are otherwise computationally impossible.</p>
<p class="muted-text mt-4">For most real-world problems, a solution within 2-5% of optimal that arrives in seconds beats a perfect solution that arrives after the heat death of the universe.</p>
</div>
<div class="card text-center">
<div style="font-size:1.5rem">Optimal guarantee</div>
<div style="font-size:2.5rem; font-weight:800; color:var(--danger);margin:1rem 0">VS</div>
<div style="font-size:1.5rem; color:var(--accent)">Computational possibility</div>
</div>
</div>

---
layout: default
---

# Back to our 50 cities

<div class="card text-center mt-8" style="padding:3rem">
<p style="font-size:2rem; font-weight:700">Remember this?</p>
<div class="hero-stat mt-6" style="font-size:4rem">49! = 6 x 10<sup>62</sup></div>
<p class="mt-4" style="font-size:1.3rem">Brute force: impossible. Greedy: wasteful. Metaheuristics: done in seconds.</p>
</div>

---
layout: default
---

# The comparison

<div class="grid grid-cols-4 gap-4 mt-6 text-center">
<div class="card">
<div style="font-weight:700">Brute force</div>
<div class="hero-stat" style="font-size:1.8rem;color:var(--danger)">N/A</div>
<p class="muted-text text-sm">Never finishes</p>
</div>
<div class="card">
<div style="font-weight:700">Greedy</div>
<div class="hero-stat" style="font-size:1.8rem;color:var(--warning)">14,327 km</div>
<p class="muted-text text-sm">Instant, wasteful</p>
</div>
<div class="card" style="border-color:var(--accent)">
<div style="font-weight:700;color:var(--accent)">Metaheuristic</div>
<div class="hero-stat" style="font-size:1.8rem;color:var(--accent)">10,512 km</div>
<p class="muted-text text-sm">Seconds, great</p>
</div>
<div class="card">
<div style="font-weight:700;color:var(--success)">Optimal</div>
<div class="hero-stat" style="font-size:1.8rem;color:var(--success)">10,241 km</div>
<p class="muted-text text-sm">Impossible at scale</p>
</div>
</div>
<p class="mt-6 text-center" style="font-size:1.3rem;color:var(--accent)">Metaheuristics got within 2.6% of optimal. That is usually good enough.</p>

---
layout: default
---

# What we learned

<div class="grid grid-cols-3 gap-6 mt-6">
<div class="card">
<div style="font-size:1.3rem; font-weight:700; color:var(--accent)">1. The problem</div>
<p class="muted-text mt-2">Combinatorial explosion makes exact search impossible for real problems.</p>
</div>
<div class="card">
<div style="font-size:1.3rem; font-weight:700; color:var(--accent)">2. The strategy</div>
<p class="muted-text mt-2">Metaheuristics balance explore vs exploit to find good solutions fast.</p>
</div>
<div class="card">
<div style="font-size:1.3rem; font-weight:700; color:var(--accent)">3. The tools</div>
<p class="muted-text mt-2">SA (shake and cool), GA (evolve and mutate), Tabu Search (climb and remember).</p>
</div>
</div>

---
layout: end
---

# Questions?

<div class="text-center mt-8">
<p class="muted-text">Introduction to Metaheuristics</p>
</div>
"""


base = "/home/hex/University/Fall26/Educational/Slides/slidev-skills"
with open(os.path.join(base, "slides.md"), "w") as f:
    f.writelines(L)

print(f"Wrote {len(L)} lines to slides.md")
