---
name: teaching-pedagogy
description: A comprehensive playbook for designing understanding instead of transferring information. Use this skill ANY TIME the user is creating or revising educational content — slides, presentation decks, Slidev decks, video scripts, course material, tutorials, explainers, blog posts, papers, technical documentation, lesson plans, training material, onboarding content, README files meant to teach, or curriculum design. Also use when reviewing existing teaching content for quality, when the user asks how to explain a concept, when designing the structure of a lesson, when picking visual metaphors or analogies, when deciding what to put on a slide, when the user complains that content is "boring" or "info-dumping" or "textbook-y", or whenever pedagogical choices are being made. Covers narrative architecture (the discovery arc), cognitive load management, visual semantics (color as teaching tool, motion as meaning), embodied/physical metaphors (kinesthetic intuition, tactile language, scale anchoring), temporal pacing (rhythm, tension/release, the "ohhh" pause), emotional design (curiosity → tension → insight → loop closure), compositional rules at the slide level, subject-specific patterns for mathematics / programming / cybersecurity / ML+AI, named techniques like "predict-then-reveal" and "metaphor-then-mechanism", common failure modes with named diagnoses, and a pre-flight checklist. Synthesizes 3Blue1Brown-style cognitive scaffolding, embodied cognition research (Lakoff & Johnson, Barsalou), Cognitive Load Theory (Sweller), and the Cognitive Theory of Multimedia Learning (Mayer). Consult this skill BEFORE writing any teaching artifact, not after — the playbook is for design, not retrospective grading.
---

# TEACHING.md

A playbook for designing **understanding**, not delivering information.

Applies to slides, videos, papers, blog posts, technical docs, video scripts, course outlines — anything where you're trying to put an idea into someone else's head.

This document complements the technical Slidev `SKILL.md`. That one is *how* to render the deck. This one is *what to put on the slides and why.*

---

## §0 — The one-sentence philosophy

> You are not teaching a topic. You are reconstructing the discovery of an idea inside the learner's mind so that, when the formal statement appears, it feels inevitable.

Every rule in this document is a corollary of that sentence. When in doubt, return to it.

---

## §1 — What this rejects, what it embraces

### Rejects

- **Definition-first teaching.** "A monad is a monoid in the category of endofunctors." The student leaves more confused than they started.
- **The textbook voice.** "We will now consider the case where..." Nobody reads this voluntarily.
- **Information density as a virtue.** A slide full of bullets feels thorough; it teaches almost nothing.
- **Premature formalism.** Equations, notation, jargon dropped before intuition exists. The learner memorizes shapes without meaning.
- **Corporate-training tone.** "By the end of this module, learners will be able to..." Skip.
- **Encyclopedic completeness.** Saying everything that's true. The job is to say the *one* thing that makes the rest fall into place.
- **Decorative visuals.** Stock photos, generic icons, gradient backgrounds that mean nothing. If the picture doesn't carry meaning, cut it.
- **The illusion of finished knowledge.** Pretending the field is settled when researchers are actively confused.

### Embraces

- **Discovery rhythm.** The student feels: confusion → curiosity → tension → insight → compression → "of course."
- **Semantic anchoring.** Every symbol stays attached to a meaning. The learner can always say "this letter represents *that thing*."
- **Multi-dimensional encoding.** Same idea expressed visually, kinesthetically, verbally, mathematically — at least two modes always overlapping.
- **Earned formalism.** The equation appears only when the student already mentally wants it.
- **Genuine uncertainty.** "We don't fully know why this works" beats fake confidence every time.
- **Honest difficulty.** Hard things stay hard; we just give the student footholds.
- **One mental leap per slide.** Hand them ladders, not pole vaults.
- **The teacher's voice.** A real researcher thinking aloud, surprised by their own subject.

---

## §2 — The narrative architecture (the discovery arc)

Most lessons should follow some version of this arc. Not every slide hits every step; the *deck* hits them in order across the whole story.

```
┌─────────────────────────────────────────────────────────────┐
│  1. Wonder           — open with a question, mystery, fact   │
│  2. Human stakes     — why anyone should care                │
│  3. Concrete example — one specific instance, not abstract   │
│  4. Naive attempt    — try the obvious thing                 │
│  5. Failure          — show why naive thinking breaks        │
│  6. Tension          — "so how could it possibly work?"      │
│  7. Visual intuition — geometry / motion / picture           │
│  8. Mechanism reveal — the actual idea, gradually            │
│  9. Formalization    — equations as compression of intuition │
│ 10. Generalization   — same idea in other domains            │
│ 11. Edge cases       — where the mental model breaks         │
│ 12. Loop closure     — return to the opening mystery         │
└─────────────────────────────────────────────────────────────┘
```

### The loop closure principle

The biggest single technique most teachers miss. Open with a question. Develop the idea. **At the end, return to the question and answer it.**

The student feels closure. The mystery that propelled them through the lesson now feels solved. Memory cements around the resolution.

Without loop closure the lesson feels like it just stopped.

### What to put in the cold open

A cold open (slide 1–3) must do one of:

- **Pose an impossibility.** "How does your phone know your face from one camera angle?"
- **Show a paradox.** "Why does a 99% accurate medical test mean almost nothing?"
- **Reveal a hidden pattern.** "These three things are secretly the same problem."
- **Bring a known thing into question.** "You think you know what multiplication is. Watch."
- **Start with a real artifact.** Show a real CVE, a real paper title, a real attack — say "by the end you'll understand this."

Never start with a learning objective. Never start with an outline. Both kill curiosity.

---

## §3 — The cognitive dimension

### §3.1 Working memory is the bottleneck

The learner has about 4±1 "chunks" available at once. Every new concept temporarily occupies a chunk. This is a hard biological limit.

Implications:

- **One new idea at a time.** Adding two simultaneously means the learner can hold neither.
- **Chunking is teaching.** Once a concept is consolidated (becomes one unit), it frees up a slot. The discovery arc is fundamentally about building chunks the student can later treat as primitives.
- **Pre-existing knowledge is leverage.** Tie new concepts to chunks the learner already has. A new idea anchored to an old one is much cheaper than a free-floating one.

### §3.2 Cognitive Load Theory — three types of load

From Sweller (1988+):

| Load type | What it is | What to do |
|---|---|---|
| **Intrinsic** | Inherent difficulty of the material | Can't eliminate; reduce by chunking |
| **Extraneous** | Cost imposed by bad presentation | Eliminate ruthlessly. Every formatting choice is fighting this. |
| **Germane** | Cost of building mental models | Maximize — this is the productive work |

Most teaching failures are extraneous load: bad layout, irrelevant decoration, inconsistent notation, jargon used before introduction. Cut these and the student's brain has more left for the actual learning.

### §3.3 The "one leap" rule

Between any two consecutive slides, the cognitive distance must be small enough that the student can step across without searching.

Diagnostic question: *Could a smart student who just understood slide N predict roughly what slide N+1 will be about?*

If yes — good pacing. If no — you skipped a step.

### §3.4 Semantic anchoring (the symbols-must-stay-attached rule)

Every variable, every symbol, every Greek letter must remain attached to a meaning the student can name in plain language.

**Wrong:** "Let θ be the parameter vector..." (vague — what *is* θ?)

**Right:** "θ collects every weight and bias in the network — every number we'll tweak during training. When you see θ later, picture the giant pile of numbers the optimizer is adjusting."

Once you've anchored θ, every later mention of θ has a hook in the student's mind. They never have to ask "what was θ again?"

### §3.5 The principle of "earned formalism"

Equations are *compression of understanding,* not its introduction.

The student should already mentally want the equation before it appears. They should be thinking "okay, but how do you write that down?" — and then the equation arrives as the answer.

If you write an equation before the student wants it, you've created jargon. If you write it after, you've created notation.

### §3.6 Anticipate the inner monologue

While teaching, simulate the student's running thoughts. Address them out loud.

- "You might be wondering why we use logarithm here — wait three slides, it'll make sense."
- "If you're thinking 'this looks like the chain rule,' you're right, and we'll see why."
- "The natural question at this point is: what about higher dimensions?"

This makes the lesson feel like a conversation with someone who's reading your mind. Massively higher retention than passive narration.

### §3.7 Expertise reversal — what works for novices fails for experts

A worked example helps a beginner more than a problem to solve. The reverse holds for experts.

Implication: know who you're writing for and stay consistent. Don't oscillate between "explaining 1+1" and "assuming the reader knows category theory." Pick a level and hold it for the whole deck. Note assumed prerequisites up front.

---

## §4 — The visual dimension

This is what the brief mentioned briefly and we're expanding deeply. Visual design isn't decoration; it's a second teaching channel that runs parallel to your words.

### §4.1 Visuals are not illustration — they are an independent argument

The picture should *make the same argument* the words make, in a different language. If you cover the words, the picture should still teach. If you cover the picture, the words should still teach. The redundancy is the point — it's how the brain triangulates.

**Bad use of visuals:** decorative photos, generic icons, gradient backgrounds, stock images of "data" or "AI."

**Good use of visuals:** the actual structure of the thing. A logic gate looks like a logic gate. A vector is an arrow. A distribution is a curve. A network packet is a labeled byte layout.

### §4.2 Color is a teaching tool, not a style choice

Pick a **fixed semantic palette** at the start of a deck and use it consistently across every slide. Color carries meaning the way variable names do.

Example palette for ML/security content:

| Role | Color | Hex |
|---|---|---|
| Primary signal / input / "the thing we care about" | cyan | `#22d3ee` |
| Intermediate / "stuff in between" | amber | `#f59e0b` |
| Output / "the answer" | emerald | `#10b981` |
| Adversary / attacker / wrong answer | red | `#ef4444` |
| Caution / surprising | yellow | `#fbbf24` |
| Dimmed / contextual | slate | `#94a3b8` |

Once the student associates cyan with "input vector" on slide 3, every cyan thing across the next 50 slides feels familiar. You've made a visual vocabulary.

**Rules:**
- Don't change a color's meaning mid-deck.
- Don't use more than ~6 semantic colors. Adding a 7th saturates the palette and breaks the system.
- Reserve red for genuine attention. If you red-highlight everything, nothing is highlighted.

### §4.3 Motion as meaning

Animation should answer questions, not entertain.

| What motion communicates | When to use it |
|---|---|
| "These two things are the same" | Morphing one shape into another |
| "This depends on that" | One slider changing causes another element to move |
| "Order matters here" | Sequential reveal (v-clicks) |
| "These happen in parallel" | Simultaneous fade-ins |
| "Causation flows this way" | Animate arrows in the direction of cause |
| "Watch this transformation" | Smooth state change over 1–2 seconds |

3Blue1Brown's `manim` excels because every animation has a teaching purpose. A rotation isn't "for the camera" — it's revealing that the object has rotational symmetry. A morph isn't a transition — it's saying "this is literally the same object under a new representation."

**Rule:** if you can't articulate what the animation is teaching, cut it.

### §4.4 The pre-attentive layer

Some visual features the brain processes *before conscious attention.* Use them to direct the eye:

- **Color difference** — one red dot in a field of grey ones
- **Size** — large vs small
- **Orientation** — one tilted line among vertical ones
- **Motion** — one moving thing among still ones
- **Position/grouping** — proximity implies relationship

Designing a slide is partly an exercise in **engineering where the eye goes first.** The eye should land on the hero element — the thing that carries this slide's one job.

### §4.5 Visual hierarchy

Every slide should have:

1. **One hero.** The main visual or idea. ~60% of the visual weight.
2. **One supporting element.** A code snippet, second visual, or annotation. ~25%.
3. **One framing element.** Title, caption, or one-line context. ~15%.

If you can't identify what's the hero, the slide has no hero — which means it has no job.

### §4.6 Negative space is teaching

Empty space tells the student: "stop here, look at this, don't look anywhere else."

A slide that fills every pixel is screaming. A slide with whitespace gives the eye somewhere to rest, the brain somewhere to think.

Rule of thumb: if a slide feels "balanced," it probably has the right amount of space. If it feels "full," cut 30% of the content.

### §4.7 Annotation — guiding the eye

Within a complex figure, annotations tell the student where to look:

- **Arrows** pointing at the part that matters right now
- **Callouts** labeling specific structures
- **Highlight boxes** isolating one region
- **Color emphasis** on the relevant element
- **Dimming** the irrelevant ones

A reader who knows where to look has done 80% of the cognitive work of reading the diagram.

### §4.8 Transformations reveal structure

Two key visualizable transformations:

- **Before/after.** Show the world before the concept, then after. The difference is what the concept teaches. ("Here's data unsorted. Here's it sorted. The algorithm is the arrow in between.")
- **Morph.** One representation gradually becomes another. Reveals that two things are secretly the same. ("Watch the truth table become a Karnaugh map.")

Both work in static slides (two side-by-side panels) or in video (real animation).

### §4.9 Scale and zoom

When teaching a system, move between scales:

- **Macro** — the whole system, schematic, all parts visible
- **Meso** — one component, opened up
- **Micro** — inside the component, the mechanism
- **Macro again** — back out, now with deeper understanding

This is how electronics is taught (computer → board → chip → transistor → silicon → atom → electron). Each zoom level adds meaning to the level above.

### §4.10 Spatial metaphors

Use 2D and 3D space as a teaching tool. The brain reuses its spatial-reasoning circuits for abstract reasoning:

- "Closer together" → more similar (embeddings, clustering)
- "Higher up" → more abstract or larger (hierarchies, magnitudes)
- "To the right" → later in time
- "Above the line" → positive / above threshold
- "Inside the box" → a member of a category
- "Connected" → causally or structurally related

Once you've established a spatial convention, *consistency matters more than the choice.* If "up" means "more accurate" on slide 5, don't flip it to "less accurate" on slide 20.

### §4.11 Diagrammatic vocabularies

Different fields have canonical visual languages. Use them:

- **Circuit diagrams** — D-shapes for AND, triangles for NOT, junction dots for branching
- **Sequence diagrams** — vertical lifelines, horizontal arrows, time flowing down
- **Network topologies** — boxes for hosts, clouds for networks, lines for links
- **Commutative diagrams** — objects as nodes, morphisms as arrows
- **Packet layouts** — labeled byte fields, fixed-width columns
- **State machines** — circles for states, arrows for transitions

When you use a canonical visual language, the reader's existing familiarity does work for you. When you invent a new one, you're spending free attention on the syntax of your diagram instead of the content.

### §4.12 Visual rhythm across a deck

A deck of slides has a rhythm. Some slides are dense (a worked example with code + math). Others are sparse (a single hero question in 48-point type).

Healthy rhythm alternates:

```
dense → sparse → dense → sparse → dense → dense → SPARSE (cliffhanger)
```

The sparse slides are breathing room. They prevent cognitive overload and create emphasis when they appear after a dense passage. **A "single statement" slide after three dense ones is the slide everyone remembers.**

### §4.13 The hero-and-quiet pattern

Two slide archetypes carry most of the load:

- **Hero slide.** One large visual occupying most of the canvas, minimal text. Used at openings, big reveals, principle statements.
- **Quiet slide.** Dense but clean. Multiple components arranged in a grid. Used for working through mechanisms.

A deck made entirely of hero slides feels light but shallow. A deck of all quiet slides feels exhausting. Alternate.

### §4.14 Captions as guidance, not redundancy

Every visual deserves a caption — but the caption shouldn't repeat the title. It should add the *one thing the picture alone won't say.*

Caption *adding* meaning:
> "The amber wire is the un-inverted intermediate signal."

Caption *just repeating:*
> "Diagram of an AND gate made from NAND and NOT."

The second one is dead weight; the first is teaching.

---

## §5 — The physical / embodied dimension

The brief barely touched this. It's enormous. The body shapes how we think — abstract concepts are processed through metaphors grounded in physical experience (Lakoff & Johnson, *Metaphors We Live By*, 1980). You can lean on this hard.

### §5.1 Embodied cognition — the basic claim

Abstract reasoning reuses circuits originally evolved for spatial, motor, and sensory tasks. When you "grasp an idea," your brain is partially activating the same systems used to grasp an object.

Implication: **explaining abstractions through bodily metaphors isn't fluffy — it's directly leveraging the brain's actual machinery.**

### §5.2 Physical metaphors that work

Every abstract concept should, where possible, be grounded in a verb you can do with your body:

| Abstract concept | Physical metaphor |
|---|---|
| Function | Machine you put things into and get things out of |
| Recursion | Russian nesting dolls / mirrors facing each other |
| Optimization | Ball rolling downhill |
| Gradient descent | Walking down a foggy slope, feeling for steepest direction |
| Linear transformation | Stretching, rotating, shearing a grid |
| Eigenvector | Direction that doesn't change when you push the space |
| Hash function | Shredder — same input shreds the same way; different inputs shred unrecognizably |
| Encryption | A locked box where only the key-holder can open |
| Bit | A switch that's on or off |
| Stack | A pile of plates — last in, first out |
| Pointer | A handwritten address |
| Mutex | A bathroom key — only one person at a time |
| Convolution | Sliding a stencil across an image |
| Attention | Spotlight that moves across the input |
| Backpropagation | Blame propagating backward through a chain of causes |
| Adversary | A pickpocket — exploits whatever you don't watch |

Notice: each metaphor names a *physical action.* Picking up, sliding, pushing, walking, locking. The body knows these motions; the abstraction inherits the body's understanding.

### §5.3 Tactile language

When describing transformations, use verbs from manipulation:

- "We're going to **stretch** this dimension"
- "**Squeeze** all the probability mass into the corner"
- "**Fold** the space onto itself"
- "**Spin** the basis vectors"
- "**Carve** the input space into regions"
- "**Stack** these layers"
- "**Wrap** the values around at the modulus"
- "**Project** onto the plane"

These verbs make the math feel handleable. Compare to passive: "we apply a transformation that increases variance along the principal axis." The student does nothing in the second version.

### §5.4 Kinesthetic intuition — feel the math

For some concepts, ask the student to imagine *doing* something with their body:

- **Vector addition:** "Walk three steps east, then four steps north. Where do you end up?"
- **Cross product:** "Point your right index finger at A, middle at B. Thumb gives the direction of A × B."
- **Rotation:** "Spin in place. The point on top of your head stays on its axis. That axis is the eigenvector."
- **Gradient:** "Imagine you're blindfolded on a hill. Your feet feel the slope. Step in the direction your feet say is steepest down."
- **Convex vs non-convex:** "A convex landscape is a single bowl. A non-convex one is a mountain range with many valleys."

Even when reading silently, the student's motor system partially fires. You've added a third channel beyond visual and verbal.

### §5.5 Manipulation and interaction

Where the medium allows (web pages, interactive notebooks, animations), let the student *move* something and see the effect:

- A slider that changes a hyperparameter → graph updates
- A draggable vector → its components update
- A toggle that swaps two algorithms → results compared side-by-side

In Slidev, this is what Vue components and `v-motion` enable. The student doesn't just see X causes Y; they *make* X happen and watch Y respond. Causation goes from claim to felt experience.

### §5.6 Scale anchoring

Numbers in the abstract are meaningless. The brain needs physical anchors:

- "A neutron star is denser than the entire population of Earth squeezed into a sugar cube."
- "If the atom were the size of a football stadium, the nucleus would be a grain of rice at center field."
- "GPT-3 has 175 billion parameters. If each one were a grain of sand, you'd have a beach."
- "AES has 2^128 keys. Brute-forcing at a trillion tries per second per gram of silicon on Earth, with the sun as your energy budget, takes longer than the heat death of the universe."

Once an abstract number is anchored to a physical scale, the student carries the intuition forever.

### §5.7 Time as a physical dimension

For concepts involving time, *show time elapsing.* Real-time animation is the strongest version, but even static "tick 1 / tick 2 / tick 3" panels work:

- A network handshake unfolding step by step
- A neural net training over epochs (loss curve appearing left-to-right)
- A sort algorithm with successive snapshots
- A virus propagating across a graph

Time isn't an abstract index — it's a thing that *passes.* Treat it as a physical dimension, not a variable.

### §5.8 Forces and constraints

Many abstract systems are best taught through physical-mechanical metaphors:

- **Optimization** as a ball under gravity, with constraints as walls
- **Equilibrium** as opposing forces balanced
- **Phase transition** as ice → water → steam
- **Information bottleneck** as a narrow pipe restricting flow
- **Entropy** as gas spreading into a room until it fills evenly
- **Selection pressure** as a filter passing only certain shapes

These metaphors aren't just analogies — they often share *mathematical structure* with the abstract system, which is why they work. (Gradient descent literally is gravity on a loss surface.)

### §5.9 Construction as understanding

When teaching how a complex thing works, **build it in front of the student** from parts they already know:

- A CPU built from gates → flip-flops → registers → ALU → control unit
- An OS built from interrupts → scheduling → memory → file system
- A neural net built from neuron → layer → network → loss → training loop
- A cryptosystem built from XOR → permutation → S-box → round → cipher

The constructive approach makes the final system feel inevitable: of course it works this way; we just watched it being assembled.

This is what Nand2Tetris does and why it's effective. The student isn't told what a computer is — they build one.

### §5.10 Body-mapped abstractions

Some abstractions map directly onto body geography:

- **Levels of abstraction** map onto vertical stacking (low → high)
- **Sequential time** maps onto left-to-right reading direction (in LTR languages)
- **Inside/outside** maps onto containment
- **Self vs other** maps onto inside-the-body vs external

When designing visuals, respect these mappings. "Input on the left, output on the right" is right because that's the direction of reading. "Stack of layers, lowest at the bottom" is right because gravity pulls things down.

Violating these mappings creates extraneous cognitive load — the student has to translate before they can think.

---

## §6 — The temporal dimension (rhythm and pacing)

How time flows through the lesson matters as much as what's in it. This is the dimension videos handle natively and slides have to fake.

### §6.1 The "ohhh" pause

After delivering a key insight, *stop.* Let it land.

In a video: silence for 2 seconds.
In a slide deck: a sparse slide with just the insight, in big type, on a quiet background.
In a paper: a paragraph break and a one-line statement.

The pause says "this was important — take a moment." Without it, the student keeps reading and the insight blurs into the next sentence.

### §6.2 Tension and release

Build tension. Then release.

Tension comes from: an unsolved question, a paradox, a failure of a naive approach, a "but wait" moment.

Release comes from: the answer, the resolution, the mechanism that fixes the failure.

A good lesson has multiple tension/release cycles. Each cycle gives the student a small dopamine hit — the "oh!" feeling that 3B1B is famous for engineering.

**Antipattern:** "Here's the answer. Now let me motivate it." Backwards. The student already saw the answer; the motivation feels like padding.

### §6.3 Speed control

| Speed | When to use |
|---|---|
| **Fast** | Familiar territory, recap, mechanical computation |
| **Medium** | Standard explanation, new but well-supported concept |
| **Slow** | Critical insight, first introduction of a key idea, the "this is the moment" beat |
| **Stop** | After a major insight — let it land |

In a slide deck, "speed" maps onto slide density. Fast = dense slides with lots of info. Slow = sparse slides with one idea. Stop = a hero slide with a single statement.

### §6.4 The 7-second rule for visuals

Any visual that takes longer than ~7 seconds to parse is too complex for one slide. Either:

- Simplify it
- Break it into a sequence of slides, each showing one more piece
- Add annotations that direct the eye

If you find yourself thinking "they just need to look at it long enough" — you've shipped a bad visual. The student is reading at 200 words per minute; they're not going to puzzle over your diagram.

### §6.5 The reveal cadence

For a multi-step idea, use a click-by-click reveal (v-clicks in Slidev). Each click adds one element.

This forces the student to track *with* the explanation, not race ahead or fall behind. It also mimics how an instructor at a chalkboard would build the idea step by step.

**Rule:** if the slide would benefit from being shown gradually rather than all-at-once, use clicks. If it works equally well static, don't.

### §6.6 Pacing across the deck

A typical 60-slide lesson has roughly this shape:

```
slides 1–5    cold open + motivation  | sparse, hero-heavy
slides 6–15   foundational concepts   | medium density
slides 16–35  core development        | dense, lots of mechanism
slides 36–50  applications, examples  | medium-to-dense
slides 51–55  edge cases, subtleties  | dense
slides 56–60  recap, loop closure     | sparse again
```

The energy curve goes: build → climb → plateau → descend. Match the visual rhythm to the conceptual one.

---

## §7 — The emotional dimension

Learning is mediated by emotion. Engaged learners retain; bored learners forget.

### §7.1 The emotions you're conducting

| Emotion | When | How to create |
|---|---|---|
| **Curiosity** | Opening, before each new section | Pose a question they can't answer yet |
| **Tension** | When naive thinking fails | Show the gap between expectation and reality |
| **Surprise** | At the reveal of the mechanism | Make sure the mechanism is non-obvious |
| **Recognition** | When the formal equation appears | Make sure the equation matches the intuition just built |
| **Satisfaction** | At loop closure | Return to the opening question, now answerable |
| **Awe** | At generalization | Show the idea applies far beyond the original context |
| **Discomfort** | At edge cases / "this method can fool you" | Show what the model misses |

A lesson hitting all of these feels like a story. A lesson hitting none feels like a syllabus.

### §7.2 Your enthusiasm is data

The student is reading not just *what* you wrote but *how excited you seem.* Authentic enthusiasm transfers; manufactured enthusiasm reads as fake and hurts.

If you're bored writing it, the student will be bored reading it. **If you can't find the part of the topic that genuinely interests you, don't teach it yet** — find that part first.

### §7.3 Anthropomorphize the math objects

Treat abstract objects like characters with personalities:

- "NAND is the workhorse — boring, but stubborn enough that everything else gets built from it."
- "Sigmoid is the optimistic activation — it can't really say no, just 'maybe.'"
- "The attention head is greedy — it wants to look at every token equally and then learns who matters."

This isn't unrigorous; it's pedagogically useful anthropomorphism. The student now has a *relationship* with these objects, which means they'll remember them.

### §7.4 Acknowledge difficulty

Saying "this part is hard" *helps* the student. They were going to find it hard anyway; pretending it's easy makes them feel stupid.

> "The chain rule looks like nothing when written in a textbook, and then it powers the entire deep learning revolution. This is the moment where it stops being a formula and becomes a worldview. Read it twice."

This sentence buys you the student's attention for the next paragraph. It also accurately calibrates their expectation — they know to slow down.

### §7.5 Honest uncertainty

When the field is genuinely uncertain, say so:

- "Nobody fully understands why neural networks generalize. Several theories exist. Here's the one with the most evidence right now..."
- "This proof works but the bound is loose. The tight bound is an open problem."
- "We use this loss function because it works. Why it works better than alternatives is partially understood."

Honest uncertainty doesn't undermine authority — it *establishes* it. The student now trusts you to be honest about everything else.

### §7.6 The "I think you could have invented this" feeling

The strongest learning experience is when the student feels they could have arrived at the idea themselves, given the right setup.

To engineer this:

- Show the problem before showing the solution
- Show the naive attempt and let the student feel its failure
- Pose the question: "what would *you* do?"
- Then present the actual solution as the natural next step

The result is: "of course it has to work like that." That feeling is the gold standard.

---

## §8 — The compositional dimension (slide-level design)

Now zooming into the individual artifact — what makes one slide work.

### §8.1 One job per slide

Every slide should do exactly one of:

- Pose a question (open a curiosity gap)
- Introduce one new concept
- Reveal one mechanism
- Show one example
- Prompt one prediction
- Compress one insight
- Recap one section

If you're trying to do two of these on one slide, split it. The Slidev cost is trivial; the cognitive cost of cramming is enormous.

### §8.2 The hero element test

For each slide, ask: *what is the hero?*

The hero is the one thing the student should remember from this slide if they remember nothing else.

- On a "single idea" slide, the hero is the statement.
- On a worked example, the hero is the diagram or final answer.
- On a code slide, the hero is the key 3–5 lines.
- On a recap slide, the hero is the principle in big text.

If you can't name the hero, the slide has no purpose. Cut it or restructure.

### §8.3 The minimum viable concept

For each concept, find the smallest possible version that still teaches the idea.

- The smallest neural network is 1 neuron. Teach with that first.
- The smallest cryptosystem is XOR with a one-time pad. Teach with that first.
- The smallest sort is on 3 elements. Teach with that first.
- The smallest matrix is 2×2. Teach with that.

Then generalize. Most pedagogical failures come from starting with the realistic case (which is also the complicated case).

### §8.4 Density rules

| Element | Soft max per slide |
|---|---|
| Words in body text | ~50 |
| Bullet points | 5 (and only if a list is actually the right form) |
| Code lines | 15–20 |
| Equations (block) | 1–2 |
| Diagrams | 1 |
| Different colors used semantically | 4 |
| Different font sizes | 3 |

These are soft limits. Crossing them occasionally is fine. Crossing them all on the same slide is a disaster.

### §8.5 The eye-flow path

Design slides so the eye moves in a natural reading path. For Western readers:

```
1. Title (top-left, briefly)
2. Hero element (center-ish)
3. Supporting text (left side or below hero)
4. Code / equation / detail (right side or further below)
5. Caption / annotation (bottom)
```

A slide with elements scattered randomly forces the eye to hunt. A slide with elements arranged in a clear flow reads itself.

### §8.6 The boring opening

The first ~2 seconds of a slide is "what is this." If those 2 seconds are spent decoding visual layout, the rest of the slide is spent recovering.

Make the first 2 seconds easy: a clear title, an obvious hero element, no surprises about layout. Save the cleverness for the content, not the design.

### §8.7 The handoff principle

Every slide should set up the next slide.

- A question slide → answered on the next slide
- A naive attempt → its failure on the next slide
- A failure → the fix on the next slide
- An insight → an application on the next slide

The student should always feel the deck is *going somewhere*. Slides that don't hand off feel like list items, not narrative.

### §8.8 The slide that earns its place

Final test before keeping any slide: *what does the student lose if I cut this slide?*

If the answer is "nothing important" — cut it. Decks always benefit from being shorter than you first thought.

---

## §9 — Subject-specific patterns

The general principles get more concrete when applied to specific fields.

### §9.1 Mathematics

**Start from:** motion, geometry, physical intuition, measurement problems, patterns, impossibility.

**Avoid starting with:** definitions, axioms, symbol manipulation.

**Specific techniques:**

- **Two-views technique.** For every concept, give both an algebraic and a geometric form. Dot product = sum of products = projection times length. Eigenvector = vector that stays put = solution to det(A−λI)=0.
- **Build from numbers.** Before introducing variables, work an example with concrete numbers.
- **Generalize last.** Solve the specific case fully, *then* generalize. "Now suppose n instead of 2."
- **Let the formula compress the picture.** Show the picture first. Then say "we can write this as..." and the equation arrives as shorthand.

**Equations as stories:** Every equation tells a story when read aloud. "Loss equals sum, over examples, of negative log probability of true label. Plus lambda times norm of weights squared." Train yourself to read equations as English sentences. Train students the same way.

### §9.2 Programming

**Start from:** human limitations, repetition, automation, the question "what if I had to do this 10,000 times?"

**Avoid starting with:** syntax, language features, type systems.

**Specific techniques:**

- **Show the manual version first.** Before introducing the loop, show the unrolled code. The loop is then "what we wrote when we got tired."
- **The code should run.** Every example, ideally, should be paste-and-run. Pseudo-code is a last resort.
- **Errors are teachable.** Showing a typical bug and how to debug it teaches more than the correct version alone.
- **Reveal abstraction in layers.** Concrete → repeat → loop → function → module → library. Each layer is "I got tired of the previous layer."

### §9.3 Cybersecurity

**Start from:** trust, adversaries, asymmetry, deception, human behavior, real incidents.

**Avoid starting with:** protocols, RFC numbers, port lists.

**Specific techniques:**

- **The adversary's POV.** For every defense, narrate the attack first. The student must feel why the defense exists before the defense makes sense.
- **Real incidents as scaffolding.** Every concept should be tied to a real incident — a CVE, a published breach, a known attack. Abstract security teaching is unmemorable.
- **Asymmetry framing.** Defenders must defend everywhere; attackers need one hole. This frame organizes most of the field.
- **Threat model first.** "What are we worried about?" before "what should we do?" Every solution implicitly assumes a threat model; surface it.

### §9.4 Machine learning / AI

**Start from:** prediction, pattern recognition, the question "how would a child learn this?"

**Avoid starting with:** loss functions, gradient calculations, architecture diagrams.

**Specific techniques:**

- **Data first.** Show the data before the model. Half the discipline is understanding what the data looks like.
- **The simplest model.** Linear regression before deep learning. Logistic regression before transformers. Build the conceptual ladder.
- **Failure modes as teaching.** Show what the model gets wrong. Adversarial examples, distribution shift, spurious correlations. The failures *are* the discipline.
- **Distinguish observation from explanation.** A LM produces fluent text — that's an observation. Whether it "understands" is an explanation, and it's debated.
- **Honest uncertainty.** Generalization, scaling laws, interpretability — all partially understood. Say so.

### §9.5 Systems / hardware / low-level

**Start from:** what physically happens, where the electrons go, how the bits actually move.

**Specific techniques:**

- **Construction.** Build the system from primitives the student already has. Nand2Tetris is the canonical example.
- **Trace execution.** Walk through what happens cycle by cycle, or instruction by instruction.
- **Show the registers.** Whenever possible, show the actual state of memory, registers, the stack. Abstract talk about "the program" hides the machine.
- **Real silicon, not abstract gates.** Mention transistor counts, energy, propagation delay. The physical reality grounds the abstraction.

---

## §10 — Concrete techniques (named patterns)

Reusable recipes. Each has a name so you can think "I'll use the X technique here."

### §10.1 The "but wait" technique

Set up an expectation. Defeat it. Use the defeat as motivation for the real idea.

> "We could just use a hash table. Lookup is O(1). Done.
> But wait — what if the input is a string of unknown length? Hashing it is already O(n). And what if we expect collisions? And what if we don't have memory for a hash table?
> This is why we need..."

The "but wait" creates the tension that motivates the real solution.

### §10.2 The before/after technique

Show the world without the concept, then with it. The difference is what the concept teaches.

> Before: code with 50 if-statements branching on type
> After: same code, 5 lines, with polymorphism
> The thing in between is "what polymorphism is for"

### §10.3 The two-views technique

Present every concept in two complementary frames. Switch between them.

- Algebraic and geometric (math)
- Functional and imperative (programming)
- Attacker view and defender view (security)
- Generative and discriminative (ML)

Fluency in switching between views *is* understanding.

### §10.4 The progressive zoom

Start with the big picture, zoom into one part, zoom into one part of that, ..., return to the big picture.

- Computer architecture → CPU → ALU → adder → full adder → half adder → XOR gate → NAND → transistor → silicon → atom → quantum
- Then back up: now the whole system feels different because you've seen what's inside.

### §10.5 The metaphor-then-mechanism

Introduce the idea via metaphor. Once the student gets the shape of it, drop the metaphor and explain the actual mechanism.

> "Think of attention like a spotlight scanning the input...
> [several slides later]
> The 'spotlight' is actually a dot product between query and key vectors, followed by a softmax that turns the scores into a probability distribution over the input. Same idea — now we know how it's computed."

Metaphor brings the student in; mechanism makes them an insider.

### §10.6 The historical detour

Use history when it answers the question "why does this exist?"

> "Shannon was working at Bell Labs in 1948, thinking about how to send messages over noisy wires. The question 'how much information is in a message?' had never been mathematically posed before. He came up with a measure he called entropy..."

History is justified when it provides motivation. It's not justified when it's trivia.

### §10.7 The "predict, then reveal"

Before showing the answer, ask the student to predict.

> "Look at this code. What do you think it prints?
> [pause]
> [reveal: surprising output]
> If you predicted wrong, congratulations — you've found the bug we're about to fix."

The prediction makes the answer *meaningful.* Without the prediction, the answer is just a fact.

### §10.8 The "this looks like that" pattern

When introducing concept B that resembles concept A, name the resemblance explicitly:

> "This is going to feel like the chain rule, because it is the chain rule, just written in tensor notation."

The student loves this — they get to use existing knowledge.

### §10.9 The honest dead end

Mention the wrong approaches *first*. Acknowledge they're wrong. Move on to the right one.

> "You might think we should just minimize squared error here. That's the wrong choice — squared error assumes Gaussian noise, and our labels are binary. The right loss is..."

The dead end prevents the student from going down it on their own.

### §10.10 The deferred payoff

Plant a question early. Don't answer it for several slides. Answer it at a moment when answering is dramatic.

> Slide 3: "Why does this matter? You'll see — slide 27 will be wild."
> Slide 27: [callback to the planted question, now resolved]

This is the cinematic equivalent of foreshadowing. Massively increases engagement.

---

## §11 — Failure modes and corrections

The patterns where teaching breaks. Recognize these in your own work.

### §11.1 The corporate creep

**Symptom:** "By the end of this lesson, learners will be able to..." Bullet points labeled "Key Takeaways." Anything that sounds like a training department wrote it.

**Correction:** Cold open with a question or mystery. Save learning objectives for an appendix if you must have them.

### §11.2 The textbook regression

**Symptom:** "We will now consider..." "Let X be..." "Definition: ..." Passive voice. Sentences that sound like they were written to be cited rather than read.

**Correction:** Read your draft aloud. If you wouldn't say it to a friend over coffee, rewrite it. Use first-person ("I"), second-person ("you"), active voice.

### §11.3 The premature formalism

**Symptom:** Equation appears before the student has any intuition for what it means. The student memorizes the shape without internal meaning.

**Correction:** Move the equation later. Add 2–3 slides of geometric/intuitive content before it.

### §11.4 The orphaned definition

**Symptom:** A term is defined in one slide and never referred to again. The student wonders why they learned it.

**Correction:** Either use the term in subsequent slides until it sticks, or remove the definition entirely.

### §11.5 The metaphor that breaks

**Symptom:** Your metaphor works for the basic case but misleads on edge cases. Student is now confused because their mental model doesn't match the math.

**Correction:** When a metaphor breaks, acknowledge it: "the spotlight metaphor breaks here — attention can attend to multiple places at once. Let's drop the metaphor and look at the actual computation."

### §11.6 The Christmas-tree slide

**Symptom:** A slide with 7 colors, 4 font sizes, 3 emoji, 2 boxes, 1 gradient. Looks busy. Communicates nothing.

**Correction:** Identify the one job. Cut everything that doesn't serve it. Use semantic colors only.

### §11.7 The disconnected example

**Symptom:** "Here's an example: [contrived case with no real-world stakes]." The student feels the example is a chore.

**Correction:** Tie every example to something the student would actually do or see. Real datasets, real CVEs, real bugs, real papers.

### §11.8 The "more slides = more taught" fallacy

**Symptom:** Deck length is treated as proportional to depth. 200 slides feels thorough. Most slides are filler.

**Correction:** Cut by 30%. Test: does the cut version still convey the same understanding? If yes, ship the shorter version.

### §11.9 The wrong reading level

**Symptom:** Some slides explain 1+1; others assume category theory. Whiplash.

**Correction:** Pick a reader profile. List assumed prerequisites at the top. Stay consistent.

### §11.10 The unmotivated proof

**Symptom:** "Proof: [chain of manipulations] ∎" The student followed every step and still doesn't understand the theorem.

**Correction:** Before the proof, give the *idea* of the proof in one paragraph of English. "We're going to show this by contradiction — assume the opposite, derive an impossibility." Then do the formal version.

### §11.11 The "obvious" trap

**Symptom:** "Obviously, this implies that..." "Clearly..." If something were obvious, you wouldn't need to write it.

**Correction:** Either drop the word or — if the inference is genuinely non-obvious — actually explain why.

### §11.12 The "look how complicated this is" tone

**Symptom:** "This formula looks intimidating, but..." The student now finds the formula intimidating because you told them to.

**Correction:** Just present the formula calmly, with intuition. The student forms their own difficulty assessment.

### §11.13 The dead recap

**Symptom:** Last slide is bullet points repeating the deck. Adds nothing.

**Correction:** Use the last slide for **loop closure** — return to the opening question and answer it. Or pose a new question that the next deck will answer.

---

## §12 — The pre-flight checklist

Before shipping any teaching artifact, walk through this checklist.

### §12.1 Narrative

- [ ] The first slide poses a question, mystery, or stakes — not an outline
- [ ] The arc moves from concrete to abstract, not the reverse
- [ ] Every section's purpose is visible: the student knows why they're here
- [ ] The closing returns to the opening question

### §12.2 Cognitive

- [ ] Each slide does exactly one job
- [ ] No slide introduces more than one new concept
- [ ] No equation appears before the intuition that motivates it
- [ ] Every symbol used is anchored to a plain-language meaning
- [ ] Reading level is consistent across the deck

### §12.3 Visual

- [ ] Colors carry consistent semantic meaning throughout the deck
- [ ] Every visual has a hero — one thing the eye lands on first
- [ ] No purely decorative imagery (stock photos, generic icons, gradients)
- [ ] Diagrammatic conventions match the field's standards
- [ ] Annotations guide the eye where it should go
- [ ] At least 30% of every slide is whitespace

### §12.4 Physical / embodied

- [ ] Abstract concepts are tied to bodily metaphors at least once
- [ ] Manipulation verbs are used in explanations (stretch, fold, slide, push)
- [ ] Numbers are anchored to physical scales where relevant
- [ ] Time, where it appears, is treated as something that elapses

### §12.5 Temporal

- [ ] Key insights are followed by sparse "let it land" slides
- [ ] Dense slides alternate with sparse ones — rhythm exists
- [ ] No visual takes more than ~7 seconds to parse
- [ ] Click-by-click reveals are used where order matters

### §12.6 Emotional

- [ ] At least one moment of genuine surprise per major section
- [ ] Difficulty is acknowledged where it exists
- [ ] Uncertainty is acknowledged where it exists
- [ ] My own enthusiasm for the subject is visible

### §12.7 Compositional

- [ ] Every slide that doesn't earn its place is cut
- [ ] Deck is shorter than my first draft suggested
- [ ] Reading the deck cold, can I follow it without external context?
- [ ] If I cover the words, do the pictures still teach?
- [ ] If I cover the pictures, do the words still teach?

### §12.8 The final test

After every deck, ask:

> Would the student feel "I could have invented this," or would they feel "I memorized that"?

If the latter, restart and simplify.

---

## §13 — On using this document

This document is not a checklist to be applied mechanically. The point isn't to score 100/100 on §12. Some of the best decks break some of these rules intentionally.

The point is to have **vocabulary** for what's working and what isn't. When a slide feels wrong, you can now name why: "the metaphor breaks here," "this is premature formalism," "no hero element," "wrong reading level."

Once you have the names, you can fix the problem. Without the names, you can only feel that something is off and not know what.

### §13.1 The hierarchy of priorities

If you have to violate a rule, violate them in this order (least costly first):

1. Density rules (occasional dense slide is fine)
2. Visual rhythm (sometimes you need three dense slides in a row)
3. Subject-specific patterns (you might have a better approach for your specific topic)
4. Concrete techniques (some lessons don't need a "but wait")
5. Compositional rules (most have exceptions)
6. **Never violate:** semantic anchoring, earned formalism, the loop closure principle, one-job-per-slide, the "this is for the learner not the teacher" principle.

### §13.2 The deepest principle

Every other rule in this document is downstream of one fact:

**The learner is a person, not a vessel.** They have a working memory limit, a body, emotions, a curiosity drive, and a deeply human pattern-recognition system. Teaching that works *uses all of these.* Teaching that fails treats the learner as a hard drive being written to.

When you forget every rule in this doc and revert to first principles, remember this one. The rest follows.

### §13.3 Continuous improvement

This document is a draft. Every deck I write should teach me something to add. When a new failure mode appears, name it and add it to §11. When a new technique works, document it and add it to §10.

The playbook grows. The skill improves. The next deck is better than this one.

---

## Appendix A — Inspiration sources

This document synthesizes ideas from many places. None are exhaustively credited inline but all deserve mention:

- **Grant Sanderson (3Blue1Brown)** — the cinematic discovery arc, semantic color, manim animation philosophy.
- **Bret Victor** — "Inventing on Principle," "Up and Down the Ladder of Abstraction," tools for interactive understanding.
- **Edward Tufte** — visual display of quantitative information, data-ink ratio, small multiples.
- **Richard Feynman** — "If you can't explain it simply..." — and the technique of grounding every abstraction in physical intuition.
- **Donald Knuth** — literate programming as teaching code.
- **John Sweller** — Cognitive Load Theory.
- **Richard Mayer** — Cognitive Theory of Multimedia Learning (CTML).
- **George Lakoff & Mark Johnson** — *Metaphors We Live By*, embodied cognition.
- **Lawrence Barsalou** — grounded cognition research.
- **Nisan & Schocken** — *Elements of Computing Systems* (Nand2Tetris), constructive teaching.

These are the giants. This document tries to stand on their shoulders without breaking them.

---

## Appendix B — Quick reference

If you only remember three things:

1. **You're reconstructing the discovery of an idea inside the learner's mind.** Not transferring information.
2. **Use every dimension you have.** Visual, physical, cognitive, emotional, temporal. The brain triangulates from multiple channels.
3. **The student must feel "I could have invented this."** Engineer for that feeling. Everything else follows.

The rest is implementation detail.
