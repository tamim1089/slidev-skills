# Slidev Tips & FAQ

Practical tips for slide layout, positioning, and styling.

## CSS Grid Layout

Use UnoCSS grid utilities for custom layouts beyond `two-cols`:

```html
<div class="grid grid-cols-2 gap-4">
<div>

First column content

</div>
<div>

Second column content

</div>
</div>
```

Custom column sizes:
```html
<div class="grid grid-cols-[200px_1fr_10%] gap-4">
<div>

First column (200px)

</div>
<div>

Second column (auto fill)

</div>
<div>

Third column (10% width)

</div>
</div>
```

## Absolute Positioning

Slides render at fixed size (default 980x552px) and scale to fit the screen. Absolute positioning works safely:

```html
<div class="absolute left-30px bottom-30px">
  Left-bottom aligned footer
</div>
```

## Font Size Adjustments

### Per-Slide Override

```md
<style>
h1 { font-size: 3em; }
</style>
```

### Global Override

Create `style.css`:
```css
h1 { font-size: 3em !important; }
```

### Scale the Canvas

Reducing canvas width makes all content appear larger:
```yaml
---
canvasWidth: 800   # default is 980
---
```

### Transform Component

Scale specific content:
```html
<Transform :scale="1.4">

- Item 1
- Item 2

</Transform>
```

## Selectable Text

By default, slide text is selectable. Disable globally:
```yaml
---
selectable: false
---
```

## Disable Context Menu

Hide Slidev's context menu:
```yaml
---
contextMenu: false     # or 'dev' / 'build'
---
```

## Wake Lock

Prevent screen from sleeping during presentation:
```yaml
---
wakeLock: true   # default. Set false to disable
---
```

## Color Schema

Force light or dark mode:
```yaml
---
colorSchema: light    # 'auto', 'light', or 'dark'
---
```

## Router Mode

Use hash-mode routing for file:// or simple hosting:
```yaml
---
routerMode: hash      # 'history' (default) or 'hash'
---
```

## Favicon

Set a custom favicon:
```yaml
---
favicon: '/images/my-favicon.png'
---
```

## Preloading

The next slide is preloaded by default for smooth transitions. Disable per-slide if motion animations trigger too early:
```yaml
---
preload: false
---
```

Or use `v-if` with `$slidev.nav.currentPage` to delay rendering.

## LaTeX Block Highlighting

Highlight lines in LaTeX blocks (same as code blocks):
```latex
$$ {1|3|all}
\begin{array}{c}
\nabla \times \vec{\mathbf{B}} \\
= \frac{4\pi}{c}\vec{\mathbf{j}} \\
\nabla \cdot \vec{\mathbf{E}} = 4 \pi \rho
\end{array}
$$
```

## Drag Positions

Set initial positions for draggable elements in frontmatter:
```yaml
---
dragPos:
  left: '100px'
  top: '200px'
---
```