---
name: slidev-branding-uiux
description: Use whenever building or restyling a Slidev deck (educational or technical). Governs color, typography, grid/spacing, motion, imagery, and cognitive-load rules so every deck ships with a coherent, research-grounded visual system instead of ad-hoc styling. Trigger on "slidev", "slides", "deck", "presentation", ".md slides", or any request to theme/brand a slide deck.
---

# Slidev Branding & UI/UX System

This is not a moodboard. Every rule below exists because it either reduces
the audience's cognitive load, increases retention, or keeps an AI-generated
deck visually consistent slide-to-slide without a human tuning each one by
hand. Follow it as a system, not a menu — the parts reinforce each other.

Two structural systems are supported. Pick one per deck, don't mix:

- **Bento** (default) — modular grid of variable-size cards. Use for any deck
  with images, diagrams, stats, or code alongside text — i.e. almost
  everything. Maps directly onto CSS Grid / UnoCSS, so an AI can regenerate
  any slide's layout without breaking the system.
- **Brutalism** (fallback) — huge type, black borders, flat background, no
  imagery. Use only when content is pure argument/definition with no visual
  evidence available, or when you explicitly want a stripped-down, fast-to-
  generate deck.

---

## 0) The one law everything else serves: cognitive load

Working memory holds ~4 chunks at once (Cowan, 2010). Every design choice
below is in service of not exceeding that. Concretely:

1. **One idea per slide.** If a slide needs "and" to describe its content
   ("mitosis and meiosis"), it's two slides.
2. **One idea per Bento card.** A card is a single claim, a single number,
   a single image, a single formula — never a paragraph plus a chart plus
   a caption stacked in one box.
3. **Never require simultaneous reading and listening of different text**
   (the "split-attention effect", Chandler & Sweller, 1992). If the speaker
   will explain an image aloud, do not also caption it with a full sentence
   on-slide — pick one channel.
4. **Sentence headlines, not topic phrases.** "Mitochondria produce ATP
   through oxidative phosphorylation" beats the header "Mitochondria" —
   the assertion-evidence approach (Alley et al., Penn State) shows this
   measurably improves retention (p < .01) over topic-phrase + bullet list.
   Headline = the one thing you want remembered if nothing else is.
5. **Evidence, not bullets.** Support the headline with an image, diagram,
   equation, or a single stat — not a bulleted list of sub-points. If a list
   is truly unavoidable, cap it at 3–4 items, no nesting.
6. **Reading budget: ~20 words per minute of slide time.** If a slide will
   be on screen 30 seconds, it gets ~10 words of body text, max.
7. **Remove before you add.** Every element on a slide should be load-
   bearing. If removing it changes nothing about what's understood, cut it.
8. **Chunk across slides, not within one.** A dense topic becomes a ladder
   of 4–6 slides (intuition → mechanism → example → practice → summary),
   never one slide with 4–6 ideas compressed in.

---

## 1) Color system

**60-30-10 rule**: 60% dominant/background, 30% secondary (surfaces, cards),
10% accent (the one color that means "pay attention here" — CTAs, current
step, key number). If everything is accented, nothing is.

- **One accent color per deck.** Not one per slide, not one per topic — one,
  used consistently so the eye learns "that color = important" within the
  first two slides.
- **Semantic, not decorative, color roles.** Define color variables by
  function, not by name: `--surface`, `--surface-raised` (Bento cards sit
  one step lighter/darker than background), `--text-primary`,
  `--text-muted`, `--accent`, `--accent-soft` (accent at low opacity for
  card backgrounds), `--success`, `--warning`, `--danger`. Never hardcode a
  hex value inline in a slide — always reference the role.
- **Contrast is non-negotiable, not aesthetic.** WCAG AA minimums:
  4.5:1 for body text, 3:1 for large text (24px+/18px+bold) and for UI
  borders/icons carrying meaning. Check every text-on-card-background pair,
  not just text-on-page-background.
- **Dark mode is the default for technical/dev decks** (screens are usually
  projected in dimmer rooms, and code blocks read better on dark). Light or
  warm-neutral backgrounds work better for educational decks with lots of
  diagrams/photos, since white balances image colors correctly.
- **Don't use pure black (#000) or pure white (#fff).** Use near-black
  (e.g. #0d0f12) and off-white (e.g. #f7f6f3) — pure values create harsh
  contrast that fatigues the eye across a long deck.
- **Warmth beats sterility for educational content.** A slightly warm
  neutral base (cream/peach-tinted grays) reads as more approachable than
  cold gray defaults — relevant for anything aimed at learners rather than
  executives.
- **Color-code categories consistently across the whole deck.** If biology
  slides use green accents for "process" callouts, every process callout in
  every slide uses that same green — never reassign a color's meaning
  mid-deck.
- **Never rely on color alone to convey meaning** (colorblind accessibility)
  — pair a color-coded state with an icon, label, or position, not color in
  isolation.

---

## 2) Typography

- **Modular type scale**, not arbitrary sizes. Pick one ratio (1.25 "major
  third" for most decks, 1.333 "perfect fourth" for punchier headline decks)
  and derive every size from the base (usually 16–18px body):
  `base → base×ratio → base×ratio² → ...` This is what makes an AI-
  generated deck's hierarchy feel deliberate instead of guessed.
- **Concrete sizes for in-room legibility** (Alley's assertion-evidence
  spec, adapted to screen/16:9): headline ≥ 40px, body 24–32px, captions/
  code annotations 16–20px minimum. Never go below ~16px on a slide meant
  to be read from a distance.
- **Two-line headline cap.** If the assertion doesn't fit in two lines at
  headline size, the assertion is too complex for one slide — split it.
- **Two typefaces max per deck**: one for display/headlines (can have
  personality), one for body/code (must be built for long-form legibility).
  A third "accent" display face is acceptable only for a title slide, never
  in the body.
- **Sans-serif for headlines and UI text**, always — this is not a style
  preference, it's what every cited study used and what projects legibly at
  distance. Monospace only for code/data, never for body prose.
- **No ALL CAPS body text, no underlines for emphasis, minimal italics** —
  all three measurably slow reading. Use weight and color for emphasis
  instead of decoration.
- **Line length (measure): 45–75 characters per line.** Wider text blocks
  need to be split into columns/cards, not stretched full-width.
- **Line height 1.4–1.6× for body text**, tighter (1.1–1.2×) for large
  display headlines.
- **Weight hierarchy, not size hierarchy alone**: use 2–3 font weights
  (e.g. 400 body, 600 emphasis, 800 headline) so hierarchy reads even at a
  glance, not just on close reading.

---

## 3) Grid, spacing, and Bento layout rules

- **Base spacing unit: 8px** (or 4px for tighter technical decks). Every
  margin, padding, and gap is a multiple of this unit — no arbitrary
  13px/17px paddings. This alone is what makes AI-generated layouts look
  intentional instead of randomly spaced.
- **Consistent grid gaps.** Pick one gap value (16px or 24px) and use it
  everywhere in the Bento grid — uneven gaps are the single fastest way to
  break the "grid" illusion.
- **Card sizing in fixed units, not guessed spans**: define a base cell
  (e.g. 120px), then Micro-card = 1×1, Secondary = 2×1 or 1×2, Hero = 2×2.
  Card size must map to content importance — never make a card big because
  content overflowed into it; shrink the content or split the card instead.
- **One-idea-per-cell discipline** (see Section 0): a cell holds one claim,
  one stat+caption, one image, one small diagram, or one short code snippet
  — never a mixed bag.
- **Hero placement**: the most important card anchors top-left (F-pattern
  scanning — that's where the eye lands first and forms a first impression
  in under 6 seconds). Secondary content fills right and below.
- **Proportional responsiveness**: if a card spans half the width on the
  editing viewport, it should span half (or full) width on any other
  viewport — never let a "big" card become disproportionately tiny.
- **Modularity**: every card is swappable in isolation. Changing one card's
  content must never require reflowing the whole slide — this is what lets
  an AI iterate slide-by-slide without breaking the deck.
- **Whitespace is a design element, not empty space.** Assertion-evidence
  spec: leave at least ~24–32px of clear space below a headline before any
  evidence starts. Don't fill whitespace with decoration just because it's
  empty.
- **Alignment discipline**: pick one alignment axis (usually left-aligned
  text, edge-aligned cards) and never mix centered and left-aligned text
  blocks within the same deck.

---

## 4) Motion

- **Motion has a job: directing attention or showing sequence — never
  decoration.** If an animation doesn't help the audience know what to look
  at next or how steps relate, cut it.
- **Duration**: 200–400ms for UI-scale transitions (a card entering, an
  emphasis pulse). Slide-to-slide transitions 300–500ms. Anything slower
  reads as sluggish; anything faster is imperceptible and pointless.
- **Easing**: ease-out for things entering (fast start, gentle stop — feels
  responsive), ease-in for things leaving. Avoid linear easing — it reads
  as mechanical, not natural.
- **Use `v-click` for progressive reveal of evidence that maps to spoken
  sequence** — reveal a Bento card or bullet exactly when the speaker
  reaches it, not all at once (supports the one-idea-at-a-time rule from
  Section 0).
- **Use `v-motion` (`@vueuse/motion`, built into Slidev) sparingly**: entry
  animation for a hero number/stat, a subtle slide-in for a diagram
  appearing — not on every single element, which creates visual noise and
  actually increases perceived load.
- **Respect `prefers-reduced-motion`.** Any non-essential animation should
  be disabled or reduced when the OS/browser signals reduced-motion
  preference — this is an accessibility requirement, not optional polish.
- **No motion on text the audience needs to read immediately** — don't
  animate in a headline the speaker is about to reference; animate
  supporting evidence instead.

---

## 5) Imagery and diagrams

- **Every image needs a job**: illustrate a mechanism, show real data,
  provide visual evidence for the headline assertion, or orient (a map, a
  screenshot). "Looks nice" is not a job — cut purely decorative stock
  imagery.
- **Prefer diagrams over photos for mechanisms/processes** — Mermaid
  (native in Slidev via ` ```mermaid ` code fences) for flowcharts, sequence
  diagrams, state machines; a labeled static diagram for spatial/structural
  concepts.
- **Consistent diagram styling across the deck**: same node shape
  vocabulary, same arrow weight, same accent-color usage in every diagram —
  treat diagrams as part of the type system, not one-off graphics.
- **Real screenshots for technical/dev decks** over generic icons —
  concrete over abstract, per the same principle that kills vague AI prose
  ("a system" vs. an actual terminal output).
- **Captions only when the image needs one to be understood without narration
  — otherwise let the speaker's voice carry it** (split-attention rule,
  Section 0).
- **Crop tight, avoid dead space inside an image card** — an image in a
  Bento cell should fill the cell, not float in a sea of padding.

---

## 6) Deck-level structure

- **Title slide**: deck title as a two-line-max sentence-style statement of
  what the audience will walk away knowing (not just a topic name), one
  hero visual, minimal chrome.
- **Mapping/agenda slide** for decks over ~15 slides: shows the ladder of
  sections so the audience always knows where they are — reuse this same
  slide, highlighting the current section, as section dividers throughout.
- **Ladder every complex topic**: intuition → mechanism → formal
  definition/derivation → worked example → practice/checkpoint → summary
  (matches the tutoring protocol's own scaffolding logic — this skill is
  the visual expression of that pedagogy, not a separate one).
- **Checkpoint slides**: a recall/prediction question slide every 4–6
  content slides, styled distinctly (e.g. accent-colored full-bleed
  background) so it's immediately recognizable as "pause and think," not
  "keep reading."
- **Summary slide per section, not just at the end** — short-term recall
  degrades fast; recap before moving on, not only in a final review.
- **Consistent footer/pagination** in a fixed, low-emphasis position
  (bottom, muted color) — never top, never bold — so it never competes with
  headline hierarchy.
- **Code block theme matches the deck's dark/light system** — don't drop in
  Slidev's default Shiki theme unmodified if it clashes with your palette;
  pick a Shiki theme that shares the deck's background tone.

---

## 7) Slidev/UnoCSS implementation notes

- Define the whole color/type/spacing system as UnoCSS theme tokens /
  CSS custom properties in `styles/index.ts` or a `<style>` block in
  `global-top.vue`, not repeated inline styles per slide — one source of
  truth an AI can update once to reskin the entire deck.
- Build Bento layouts with CSS Grid utility classes
  (`grid grid-cols-4 gap-4 auto-rows-[120px]`, `col-span-2 row-span-2` for
  hero cards) directly in slide markdown/HTML — this is a near 1:1 mapping
  of Section 3's rules onto UnoCSS.
- Put reusable card/hero/checkpoint patterns in `layouts/` as custom Slidev
  layouts (e.g. `layout: bento-hero`, `layout: checkpoint`) so slides invoke
  them by frontmatter instead of rebuilding markup each time — this is what
  keeps hundreds of AI-generated slides visually identical in structure.
- Use Slidev's built-in `<Transform>`, `v-click`, `v-motion`, and slide
  `transition:` frontmatter rather than hand-rolled CSS animations — they're
  already tuned to reasonable durations and integrate with click-through
  pacing.
- Keep one `UnoCSS` shortcut per semantic role (e.g. `shortcuts: { 'card':
  'bg-surface-raised rounded-xl p-6 border border-white/5' }`) so every card
  across every slide is generated from the same utility, not hand-tuned per
  slide.

---

## 8) AI-generated design pattern ban

Never use, under any framing: Inter as the primary typeface (pick something
with more character — e.g. a grotesque like Suisse Int'l, Neue Haas, or
system alternatives with real personality), blue-to-purple/indigo
gradients of any kind, glassmorphism/frosted-glass panels, drop shadows on
cards as a default (only for genuine elevation, never decoration), glow/
neon effects, more than one shade of "rounded corner" card as the entire
layout strategy, centered body text, emoji used as icons, or any palette
built on Tailwind's default indigo/violet scale. If a generated slide could
be mistaken for a generic SaaS landing page, it fails — redo it.

---

## 9) Diagram and visual libraries beyond Mermaid

- **Real brand/tech logos** (Linux, Windows, language/tool logos): use
  `simple-icons` (npm) for brand marks and `devicon` for language/tool
  icons — never approximate a logo with a generic Unicode icon.
- **Connecting logos/entities to each other** (e.g. "Linux logo → kernel →
  syscall interface"): use Vue Flow (`@vue-flow/core` for Vue environments, similar to React Flow) with custom node
  components that embed the actual SVG icon — Mermaid cannot host real
  logo SVGs as first-class nodes, Vue/React Flow can, and gives full control
  over edge routing so it never collides like Mermaid's dagre layout does.
- **Genuine data-structure visuals** (arrays, trees, linked lists, graphs):
  build with D3.js as custom SVG, not a markdown table dressed up — a
  table is not a data structure diagram no matter how it's styled.
- **Math**: KaTeX (Slidev supports it natively via `$...$` / `$$...$$`) for
  any real equation — never render math as an image or plain text.
- **Keep Mermaid only for what it's actually good at**: linear sequence
  diagrams and simple flowcharts under 5 nodes (per the existing Section
  5.5 diagram-discipline rules) — not for anything branded or structurally
  complex.

---

## 8) Anti-pattern checklist — scan every generated deck against this

- [ ] Any slide with more than one assertion/idea → split it.
- [ ] Any bulleted list longer than 4 items, or nested bullets → convert to
      evidence (image/diagram/stat) or split across slides.
- [ ] Any headline that's a topic phrase, not a sentence assertion → rewrite.
- [ ] Any text-on-card contrast below 4.5:1 (body) or 3:1 (large text) →
      fix the color pair.
- [ ] Any uneven Bento grid gap → normalize to the one gap value.
- [ ] Any card sized by "however much content it got" rather than by
      importance → resize card or trim content.
- [ ] Any more than one accent color doing "attention" duty on a slide →
      cut to one.
- [ ] Any decorative image with no explanatory job → remove or replace with
      real evidence.
- [ ] Any animation on content the audience must read immediately → move
      the animation to supporting evidence instead.
- [ ] Any ALL-CAPS body text, underlined emphasis, or more than 2 typefaces
      → fix.
- [ ] Any slide exceeding ~20 words per minute of expected screen time →
      cut text, move detail to speaker notes.
- [ ] Any color used to convey meaning with no secondary cue (icon/label)
      → add one, for colorblind accessibility.
