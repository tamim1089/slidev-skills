# Slidev Advanced Syntax

Additional markdown features beyond basic slide syntax.

## LaTeX Math

Slidev includes built-in LaTeX support via KaTeX.

### Inline Math

Surround with single `$`:

```md
Inline: $\sqrt{3x-1}+(1+x)^2$
```

### Block Math

Surround with double `$$`:

```latex
$$
\begin{array}{c}
\nabla \times \vec{\mathbf{B}} -\, \frac1c\, \frac{\partial\vec{\mathbf{E}}}{\partial t}
= \frac{4\pi}{c}\vec{\mathbf{j}} \\
\nabla \cdot \vec{\mathbf{E}} = 4 \pi \rho
\end{array}
$$
```

### LaTeX Line Highlighting

Highlight lines using `{}` with click steps (since v0.43):

```latex
$$ {1|3|all}
\begin{array}{c}
\nabla \times \vec{\mathbf{B}}  // Highlighted at click 1
= \frac{4\pi}{c}\vec{\mathbf{j}} \\
\nabla \times \vec{\mathbf{E}}  // Highlighted at click 3
\end{array}
$$
```

## Import Code Snippets

Import code from files using `<<<` syntax (since v0.47):

```md
<<< @/snippets/snippet.js

<<< @/snippets/example.ts {2,3}
```

`@` resolves to the directory containing `slides.md`.

## Multiple Entries

Split slides across multiple files using `src:` in frontmatter.

`slides.md`:
```md
# Page 1

This is a normal page

---
src: ./subpage2.md
---
```

`subpage2.md`:
```md
# Page 2

This page is from another file
```

### Frontmatter Merging

Main entry frontmatter has **higher priority** than included files:

`slides.md`:
```md
---
src: ./cover.md
background: https://sli.dev/bar.png
class: text-center
---
```

`cover.md`:
```md
---
layout: cover
background: https://sli.dev/foo.png
---
```

Result: `layout: cover` + `background: https://sli.dev/bar.png` + `class: text-center`

### Page Reuse

Include the same file multiple times:
```md
---
src: ./cover.md
---

---
src: ./intro.md
---

---
src: ./content.md
---

---
src: ./content.md  <!-- reused -->
---
```

## Embedded Styles

Use `<style>` in markdown for slide-specific styles. Styles are **scoped** to the current slide.

```md
# This is Red

<style>
h1 {
  color: red
}
</style>

---

# Next slide is not affected
```

With UnoCSS directives:
```md
# Slidev

> Hello `world`

<style>
blockquote {
  code {
    --uno: text-teal-500 dark:text-teal-400;
  }
}
</style>
```

For global style overrides, use `styles/index.css` instead.

## Slots with Template Syntax

In addition to `::name::` shorthand, use Vue's `<template v-slot:name>` syntax:

```md
---
layout: two-cols
---

<template v-slot:default>

# Left

This shows on the left

</template>
<template v-slot:right>

# Right

This shows on the right

</template>
```

Both syntaxes work. `::name::` is shorthand for the template syntax.

## Prettier Support

Slidev's custom syntax may conflict with Prettier. Use a `yaml` code block as alternative frontmatter:

````md
---
layout: cover
---

# Slidev

---

```yaml
# The first yaml block is treated as frontmatter
layout: center
class: 'text-white'
```

# Page 2
````

Install the [Prettier plugin](https://github.com/slidevjs/prettier-plugin) for compatibility.