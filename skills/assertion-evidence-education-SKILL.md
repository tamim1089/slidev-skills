# Assertion-Evidence Education Aesthetic

## What this is, and what it is not

This is the Assertion-Evidence structure (Michael Alley, Penn State College
of Engineering), grounded in Mayer's Cognitive Theory of Multimedia Learning.
It is a peer-reviewed pedagogical slide methodology, not a visual trend.
Garner & Alley 2013 (International Journal of Engineering Education) found
audiences who received assertion-evidence slides understood and recalled
technical content significantly better (p < .01) than audiences given the
same lecture content via topic-headline/bullet slides.

This is NOT Swiss International Typographic Style, NOT a minimalist
marketing deck, NOT a pitch deck. Marketing slides sell one mood or
impression per slide, standalone. Educational slides here build one
continuous argument, where each slide is evidence for a claim, chained
into the next claim. If a slide could stand alone divorced from the talk
and still fully "sell" itself, it has drifted toward marketing and is
wrong for this skill.

## Rule 1: Every title is a complete sentence, not a topic label

Wrong: "Autoencoders: Background"
Right: "Loss function doesn't use any labels!!"

Wrong: "Supervised vs Unsupervised Learning"
Right: keep as a comparison title ONLY when the slide's entire job is
literally defining two terms side by side — otherwise convert to the
claim the comparison proves.

The title states the takeaway. The speaker never has to say "on this
slide we'll talk about X" — the audience already knows the point; the
speaker's job is now to justify it out loud, in sentences that are NOT
written down, using the visual as evidence.

## Rule 2: No bullet lists as the primary content of a slide

Bullets are permitted only as ingredient lists for a build the speaker
walks through verbally (e.g. numbered VAE summary slide, added one line
per frame). They are never permitted as the sole content replacing a
diagram, chart, or image. If the content is inherently a list of facts,
convert to a labeled diagram, small multiple, or timeline instead of a
bulleted paragraph.

## Rule 3: One diagram evolves across multiple slides — build, don't replace

The single most load-bearing pattern in this style. Identify 2-4 "spine"
diagrams for the entire deck up front, before writing any slide. Every
new concept gets added TO an existing spine diagram by annotation, not
introduced as an unrelated new graphic.

Concretely:
- Same diagram, more elements colored/boxed/labeled each frame
  (e.g. VAE loss equation: reconstruction term appears, then
  regularization term appears, then KL divergence expanded, then priors
  labeled — same diagram, 5-6 incremental frames)
- Same diagram, one half greyed out then fully revealed
  (progressive disclosure via literal slide duplication with opacity
  change — this is a deliberate two-frame build, not a mistake)
- Same box-diagram skeleton reused across a subsection, with internal
  labels changing (encoder/decoder trapezoids: plain -> gains μ/σ split
  -> gains loss equation underneath -> gains KL term boxed)

Implementation in Slidev: use `v-click` / `v-motion` staged reveals
within ONE slide component where possible; where the reference material
instead duplicates the whole slide per frame (common in Keynote-sourced
decks), replicate that pattern — do not silently compress it into one
overloaded slide, and do not fragment one clean diagram into unrelated
new diagrams per concept.

## Rule 4: Color is a fixed, deck-wide semantic key — decide it before slide 1

Before writing any content, write down the color legend:
- What does the accent/highlight color mean, and does it mean that
  ONE thing for the entire deck (e.g. green = real data, red = generated
  data, for every single slide touching that comparison, no exceptions)
- Section-divider slides get their own single flat color, distinct from
  the content-accent color, used ONLY for dividers
- Never reuse a color for a second, unrelated meaning later in the deck

## Rule 5: Density alternates — never more than 2 dense slides in a row

Text-and-equation-dense slides (definitions, derivations) must be
followed within 1-2 slides by a near-empty, image-or-diagram-dominant
slide. This is not decoration — it's load management. Plan the deck's
density sequence (dense/light/dense/light) at the outline stage, before
writing slide content.

## Rule 6: One non-diagram cognitive-metaphor slide per major concept, used once

A single vivid metaphor image (e.g. Plato's Cave for latent variables)
is permitted exactly once per concept it illustrates, and must not
recur as a running visual theme. If it recurs, it stops functioning as
an anchor and becomes decoration — cut the repeat.

## Rule 7: Section dividers are content-free

Solid single color, one short line of white/contrast text, nothing
else — no logo clutter, no bullet preview of what's coming. One divider
per MAJOR section only (not per subtopic). If the deck has more than
5-6 dividers, the sectioning is too fine-grained.

## Rule 8: Every image is evidentiary, never decorative stock

Screenshots of real tool output, real experimental results, real
photographs relevant to the specific claim on that slide. No generic
stock photography, no clipart standing in for a concept that could
instead be a real diagram or real data visualization.

## Pre-flight checklist before generating any slide content

1. Write the color legend. Does every color mean exactly one thing?
2. Identify the 2-4 spine diagrams. Which concepts build onto which
   spine, and in what order?
3. Write every slide title as a complete sentence-claim first, separate
   from the content — if you can't state the claim in one sentence,
   you don't understand the slide's job yet.
4. Sequence density: mark each planned slide dense/light before
   generating content, confirm no 3-in-a-row dense run.
5. Confirm zero bullet-only slides exist outside of speaker-walked
   builds.
6. Confirm each divider slide is truly content-free and section-level
   only.

## QA gate

Export to PDF, rasterize with pdftoppm, and visually check:
- Do the progressive-build sequences read as one diagram evolving, or
  as disconnected images that happen to look similar? If disconnected,
  fix positioning/scale consistency across frames.
- Does the color legend hold with zero violations across every slide?
- Does density actually alternate, or does it drift dense for 3+ slides?
- Does any slide read as a mood/impression (marketing) rather than a
  claim-with-evidence (education)? If so, rewrite the title as a
  sentence-claim and rebuild the slide around proving it.
