# Slidev Editors

Editor support and tooling for Slidev.

## Integrated Editor

Slidev comes with a built-in editor that loads in the browser. Click the edit icon <carbon-edit /> in the navigation bar to open it. Changes are saved directly to your markdown file.

## VS Code Extension

Install the [Slidev VS Code extension](https://marketplace.visualstudio.com/items?itemName=antfu.slidev) from the marketplace.

### Features

- Preview slides in a side panel
- Slide tree view for navigation
- Drag-and-drop slide reordering
- Fold/unfold slide blocks
- Multiple project support
- One-click dev server start

### Usage

1. Click the Slidev icon in the activity bar
2. The **projects tree view** shows all Slidev projects in your workspace
3. The **slides tree view** shows all slides in the active project — click to navigate, drag to reorder
4. The **preview webview** shows the slides — click <codicon-run-all /> to start, <codicon-globe /> to open in browser

Configure included files:
```json
{
  "slidev.include": ["**/*.md"]
}
```

## Prettier Plugin

Install the [Slidev Prettier plugin](https://github.com/slidevjs/prettier-plugin) to format slides correctly:

```bash
npm install -D prettier @slidev/prettier-plugin
```

This prevents formatting conflicts with Slidev's custom markdown syntax.

## Alternative Frontmatter Syntax for Prettier

If you can't use the Prettier plugin, use a `yaml` code block instead of frontmatter `---` blocks:

````md
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