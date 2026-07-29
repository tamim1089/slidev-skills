# Slidev Directory Structure

Standard project layout for Slidev presentations.

## Root Structure

```
your-slidev/
  ├── components/       # Custom Vue components (auto-imported)
  ├── layouts/          # Custom layout components
  ├── public/           # Static assets served at root /
  ├── setup/            # Setup hooks (shiki, monaco, mermaid, etc.)
  ├── styles/           # Global styles (style.css or styles/index.ts)
  ├── index.html        # Injections to the main index.html
  ├── slides.md         # Main slides entry file
  └── vite.config.ts    # Extending Vite configuration
```

All directories are optional.

## Components

Place custom Vue components in `components/` for auto-importing.

```
your-slidev/
  └── components/
      ├── MyComponent.vue
      └── HelloWorld.ts
```

Use them directly in slides:
```md
<MyComponent :count="4"/>
<hello-world foo="bar">Slot</hello-world>
```

## Layouts

Place custom layout Vue components in `layouts/`.

```
your-slidev/
  └── layouts/
      ├── cover.vue
      └── my-cool-layout.vue
```

Reference by filename:
```yaml
---
layout: my-cool-layout
---
```

Priority: `local > theme > built-in`

Layout component template:
```html
<template>
  <div class="slidev-layout default">
    <slot />
  </div>
</template>
```

## Public

Assets in `public/` are served at root path `/` during dev and copied as-is to dist.

```md
![My Image](/images/photo.png)
```

## Styles

Global styles:
- `style.css` at root
- Or `styles/index.ts` with multiple imports

```ts
// styles/index.ts
import './base.css'
import './code.css'
import './layouts.css'
```

Supports UnoCSS `@apply` and CSS nesting out-of-box.

## Setup

Configuration files in `setup/`:

- `setup/shiki.ts` - Configure Shiki syntax highlighting
- `setup/monaco.ts` - Configure Monaco editor
- `setup/mermaid.ts` - Configure Mermaid diagrams
- `setup/katex.ts` - Configure KaTeX LaTeX rendering
- `setup/main.ts` - Vue app setup (plugins, etc.)
- `setup/shortcuts.ts` - Custom keyboard shortcuts
- `setup/preparser.ts` - Custom markdown preparser extensions

## index.html

Inject custom meta tags or scripts:
```html
<!-- ./index.html -->
<head>
  <link rel="preconnect" href="https://fonts.gstatic.com">
</head>
<body>
  <script src="./your-scripts"></script>
</body>
```

## Global Layers

- `global-top.vue` - Persistent component above all slides
- `global-bottom.vue` - Persistent component below all slides
- `custom-nav-controls.vue` - Custom navigation buttons
- `layouts/slide-top.vue` - Component at top of each slide
- `layouts/slide-bottom.vue` - Component at bottom of each slide