# Slidev Styling

Visual design patterns for professional presentations.

## UnoCSS Utilities

Slidev uses UnoCSS. Apply classes directly in Markdown or HTML.
````html
<div class="text-center text-4xl font-bold text-blue-500">
  Styled heading
</div>
````

## Typography Scale

Use consistent, hierarchical sizing:
````html
<h1 class="text-5xl font-bold">Main Title</h1>
<h2 class="text-3xl font-semibold">Section Title</h2>
<p class="text-xl leading-relaxed">Body text</p>
<p class="text-sm text-gray-500">Caption or note</p>
````

Recommended title sizes by slide type:
- Cover slides: `text-6xl` or `text-7xl`
- Section headers: `text-4xl` or `text-5xl`
- Content slides: `text-3xl`
- Body text: `text-lg` or `text-xl`

## Spacing

Use consistent spacing for visual rhythm:
````html
<div class="space-y-4">
  <p>Item with consistent vertical spacing</p>
  <p>Between all children</p>
</div>

<div class="mt-8 mb-4">Manual margins</div>

<div class="p-8">Generous padding</div>
````

Spacing scale to prefer: `4`, `8`, `12`, `16` (multiples of 4).

## Color Patterns

### Professional palettes:
````html
<!-- Blue professional -->
<div class="bg-blue-600 text-white">Primary action</div>
<div class="text-blue-500">Accent text</div>
<div class="bg-blue-50 text-blue-900">Subtle background</div>

<!-- Neutral elegant -->
<div class="bg-slate-900 text-slate-100">Dark mode</div>
<div class="text-slate-600">Secondary text</div>
<div class="bg-slate-50">Light background</div>

<!-- Warm accent -->
<div class="bg-amber-500 text-white">Highlight</div>
<div class="text-amber-600">Warm accent</div>
````

### Gradient backgrounds:
````html
<div class="bg-gradient-to-br from-blue-600 to-purple-700 text-white">
  Gradient background
</div>

<div class="bg-gradient-to-r from-slate-900 to-slate-700">
  Subtle dark gradient
</div>
````

## Layout Composition

### Centered hero content:
````html
<div class="h-full flex flex-col items-center justify-center text-center">
  <h1 class="text-6xl font-bold mb-4">Title</h1>
  <p class="text-2xl text-gray-500">Subtitle</p>
</div>
````

### Content with visual balance:
````html
<div class="grid grid-cols-2 gap-12 items-center h-full">
  <div>
    <h2 class="text-4xl font-bold mb-6">Heading</h2>
    <p class="text-xl leading-relaxed">Description text</p>
  </div>
  <img src="/image.png" class="rounded-xl shadow-2xl" />
</div>
````

### Card-style content blocks:
````html
<div class="bg-white rounded-xl shadow-lg p-8">
  <h3 class="text-2xl font-semibold mb-4">Card Title</h3>
  <p class="text-gray-600">Card content</p>
</div>
````

## Visual Effects

### Shadows for depth:
````html
<div class="shadow-sm">Subtle lift</div>
<div class="shadow-lg">Prominent card</div>
<div class="shadow-2xl">Hero element</div>
````

### Rounded corners:
````html
<div class="rounded">Slight rounding (4px)</div>
<div class="rounded-lg">Medium rounding (8px)</div>
<div class="rounded-xl">Large rounding (12px)</div>
<div class="rounded-full">Pill or circle</div>
````

### Borders and dividers:
````html
<div class="border border-gray-200 rounded-lg p-4">Bordered box</div>
<div class="border-l-4 border-blue-500 pl-4">Accent border</div>
<hr class="border-gray-200 my-8" />
````

## Code Block Styling

Enhance code presentation:
````html
<div class="rounded-lg overflow-hidden shadow-xl">
```ts
const example = "styled code block"
```

</div>
````

## Image Styling
````html
<!-- Rounded with shadow -->
<img src="/photo.jpg" class="rounded-xl shadow-2xl" />

<!-- Contained with border -->
<img src="/diagram.png" class="rounded-lg border border-gray-200" />

<!-- Full bleed -->
<img src="/hero.jpg" class="w-full h-full object-cover" />
````

## Dark Mode Considerations

Use color classes that adapt or explicitly handle both modes:
````html
<!-- Adapts to theme -->
<div class="bg-gray-100 dark:bg-gray-800">
  <p class="text-gray-900 dark:text-gray-100">Adaptive text</p>
</div>
````

## Slide Design Principles

1. **One idea per slide** — Don't overcrowd
2. **Visual hierarchy** — Clear title → subtitle → content
3. **Whitespace** — Let content breathe, use generous padding
4. **Consistency** — Same fonts, colors, spacing throughout
5. **Contrast** — Ensure text is readable against backgrounds
6. **Alignment** — Use grid or flex for clean alignment

## Quick Professional Template
````markdown
---
layout: center
class: text-center
---

<div class="space-y-6">
  <h1 class="text-6xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
    Compelling Title
  </h1>
  <p class="text-2xl text-gray-500 max-w-2xl mx-auto">
    A clear, concise subtitle that explains the value
  </p>
</div>
````