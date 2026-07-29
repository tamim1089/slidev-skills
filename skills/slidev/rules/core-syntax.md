# Slidev Core Syntax

Fundamental syntax for creating Slidev presentations.

## Slide Separators

Slides are separated by `---` at the start of a line.
```markdown
---
layout: cover
---

# First Slide

Welcome to my presentation

---

# Second Slide

More content here

---

# Third Slide

And so on
```

Use `---` on its own line. Content before the first `---` with frontmatter becomes the first slide.

## Headmatter vs Per-Slide Frontmatter

The FIRST frontmatter block (headmatter) configures the ENTIRE presentation. Per-slide frontmatter configures only that slide.
```markdown
---
# HEADMATTER - applies to entire deck
theme: seriph
title: My Presentation
info: |
  Presentation description here
drawings:
  persist: false
transition: slide-left
mdc: true
---

# First Slide

---
# PER-SLIDE frontmatter - applies only to this slide
layout: center
transition: fade
---

# Second Slide
```

## Common Headmatter Options
```yaml
---
theme: seriph              # Theme name
title: Presentation Title  # Browser tab title
titleTemplate: '%s - Slidev'
info: |                    # Presentation metadata
  Multi-line description
author: Your Name
keywords: slidev,presentation
download: true             # Show download button
exportFilename: my-slides  # Export filename
highlighter: shiki         # Code highlighter (shiki only)
lineNumbers: false         # Code line numbers
monaco: true               # Enable Monaco editor
drawings:
  enabled: true
  persist: false
  presenterOnly: false
  syncAll: true
transition: slide-left     # Default slide transition
mdc: true                  # Enable MDC syntax
---
```

## Common Per-Slide Frontmatter
```yaml
---
layout: center          # Slide layout
class: text-center      # CSS classes for slide
transition: fade        # Override transition for this slide
clicks: 3               # Manual click count
disabled: false         # Disable slide
hide: false             # Hide from presentation
hideInToc: true         # Hide from table of contents
level: 2                # Heading level for TOC
title: Custom Title     # Override title in TOC
preload: false          # Preload slide
zoom: 0.8               # Zoom scale
dragPos:                # Draggable element positions
---
```

## Speaker Notes

Add notes after the slide content using HTML comments.
```markdown
---
layout: default
---

# My Slide

Slide content here.

<!--
These are speaker notes.
They appear in presenter mode.
Can be multiple lines.
-->
```

Notes support Markdown formatting and are visible in presenter mode.

## MDC Syntax

With `mdc: true` in headmatter, use MDC for inline styling.
```markdown
---
mdc: true
---

This is [red text]{style="color: red"}.

This has a [tooltip]{title="Hello!"}.

This is **bold**{.text-blue-500} with a class.
```

## Escaping

To show literal `---` without creating a new slide:
```markdown
Use `\---` to escape the separator.

\---

This stays on the same slide.
```

## LaTeX Math

Built-in LaTeX support via KaTeX.

### Inline Math
```markdown
Inline: $\sqrt{3x-1}+(1+x)^2$
```

### Block Math
```latex
$$
\begin{array}{c}
\nabla \times \vec{\mathbf{B}} -\, \frac1c\, \frac{\partial\vec{\mathbf{E}}}{\partial t}
= \frac{4\pi}{c}\vec{\mathbf{j}}
\end{array}
$$
```

### LaTeX Line Highlighting
```latex
$$ {1|3|all}
\begin{array}{c}
\nabla \times \vec{\mathbf{B}} \\
= \frac{4\pi}{c}\vec{\mathbf{j}}
\end{array}
$$
```

## Import Code Snippets

Import code from files using `<<<` syntax (since v0.47):
```markdown
<<< @/snippets/snippet.js

<<< @/snippets/example.ts {2,3}
```

`@` resolves to the `slides.md` directory.

## Multiple Entries

Split slides across files using `src:` in frontmatter:

`slides.md`:
```markdown
# Page 1

---
src: ./subpage2.md
---
```

`subpage2.md`:
```markdown
# Page 2

This page is from another file
```

### Frontmatter Merging

Main entry frontmatter has higher priority than included files.

### Page Reuse

Include the same file multiple times:
```markdown
---
src: ./cover.md
---
---
src: ./content.md
---
---
src: ./content.md
---
```

## Embedded Styles

Use `<style>` in markdown for slide-specific scoped styles:
```markdown
# This is Red

<style>
h1 {
  color: red
}
</style>
```

With UnoCSS directives:
```markdown
<style>
blockquote {
  code {
    --uno: text-teal-500 dark:text-teal-400;
  }
}
</style>
```

## Prettier Support

Use yaml code block as alternative frontmatter to avoid Prettier conflicts:
````markdown
---
layout: cover
---

# Slidev

---

```yaml
layout: center
class: 'text-white'
```

# Page 2
````