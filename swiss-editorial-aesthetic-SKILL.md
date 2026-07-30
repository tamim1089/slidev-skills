---
name: swiss-editorial-aesthetic
description: Use for Slidev decks marked "editorial," "academic," or "Harvard-style" — supersedes the Bento-grid defaults in slidev-branding-uiux-SKILL.md with the Swiss/International Typographic Style system (Müller-Brockmann, Hofmann, Ruder). Trigger on "swiss style", "editorial", "academic deck", "minimalist rich", or when the user explicitly asks for this look.
---

# Swiss / International Typographic Style for Slidev

This supersedes `slidev-branding-uiux-SKILL.md`'s Bento-card default for any
deck using this skill. Where the two conflict, this file wins. Where this
file is silent (motion durations, checkpoint slide behavior, etc.), fall
back to the branding skill's rules.

The philosophy, in one line: design is a rational, problem-solving
discipline, not personal expression. Fact over feeling. Clarity over
decoration. Every rule below exists to serve that, grounded in the teachings
of the movement's pioneers:

- **Josef Müller-Brockmann:** The grid system as a philosophy of objective, mathematical order.
- **Armin Hofmann:** Mastery of graphic form (point, line, shape) and sensitivity to contrast, rhythm, and proportion.
- **Emil Ruder:** Typography exists first and foremost to communicate information clearly; asymmetrical layout and sans-serif type as structural tools.

---

## 1) The grid (Müller-Brockmann's rigorous structure)

- Base every slide on a strict mathematical grid (e.g. 12-column) with a fixed gutter (24px). All text blocks, images, and diagrams snap to column boundaries — no freeform placement.
- Define a baseline grid (e.g. 8px line-height unit) and align all text baselines to it, not just block tops. This makes the layout feel engineered rather than eyeballed.
- Margins are generous and consistent: minimum 64px on all four edges of a 16:9 slide. Content never touches the frame edge.
- Implement in Slidev/UnoCSS as a fixed grid utility (`grid grid-cols-12 gap-6`) applied at the slide-container level, with every content block given explicit `col-start`/`col-span`.

## 2) Typography (Ruder's communication clarity)

- Two sizes carry the entire deck: one large display size for headlines (huge — 56-80px) and one small, precise body size (18-20px). The contrast between them IS the hierarchy — no intermediate sizes filling gaps. Real scale contrast, not a 1.25 bump.
- Flush-left, ragged-right for all text, always. Never centered, never justified.
- One sans-serif grotesque typeface for the whole deck (Suisse Int'l, Neue Haas Grotesk, Helvetica Now, or a close system equivalent). 
- Headlines set tight (line-height ~1.0-1.1), body set generously (line-height ~1.5) — the contrast in tightness reinforces the contrast in role.
- Numerals, labels, and captions may use a monospace or condensed variant for a technical/documentary feel, but only as a supporting role.

## 3) Color (Restraint and function)

- Near-monochrome by default: black/near-black text on white/off-white, or the inverse for dark decks. No secondary neutral tones — commit to one direction.
- Exactly one ink accent color, used only as a precise functional signal (the one figure, the one state being emphasized, the current step) — never as decoration, never as a background wash, never gradiented.
- No gradients of any kind. Flat color only.

## 4) Composition (Hofmann's contrast and rhythm)

- Asymmetric, deliberately. Content is not centered and not evenly balanced — a large headline can anchor one side of the grid while a diagram or dense data block anchors the other, with intentional negative space doing structural work.
- Negative space is a design element, not a gap to be filled. Resist the urge to add a decorative element into empty grid columns.
- Scale contrast over color contrast: make the important thing big, not colorful. A single oversized statistic or word can outweigh a whole paragraph in visual weight.

## 5) Dividers and structure

- Hairline rules (1-2px lines, full column-width or full-bleed) are the primary divider between content regions — replacing rounded "card" containers as the default division method.
- Cards/boxes are the exception, used only when content genuinely needs visual containment (e.g. a code block, a data table).
- Page/slide numbers set small, in a corner, as part of the grid system (e.g. bottom-right, aligned to the same margin as body text).

## 6) Imagery (Objective visual evidence)

- Real photographs, real screenshots, real data visualizations only. Real photographic/diagrammatic content over any illustrative or decorative graphic.
- Images are never cropped into rounded corners or given drop shadows — hard rectangular edges, full-bleed or grid-aligned, matching the overall rejection of soft/glassy treatment.

## 7) Anti-pattern checklist (Swiss-specific)

- [ ] Any centered body text → left-align it.
- [ ] Any rounded card used as the default container instead of a hairline rule → replace with a rule unless containment is genuinely required.
- [ ] Any gradient, however subtle → flatten to solid color.
- [ ] Any second accent color → cut to one.
- [ ] Any headline/body size gap smaller than roughly 3x → increase the contrast.
- [ ] Any decorative image, icon, or illustration with no factual content → remove.
- [ ] Any element placed off the 12-column grid → snap it back.
