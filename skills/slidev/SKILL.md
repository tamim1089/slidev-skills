---
name: slidev
description: Use ONLY when writing or editing Slidev presentations. Covers slide syntax, frontmatter config, layouts, click animations, code highlighting (Shiki/Monaco/Magic Move), diagrams (Mermaid/PlantUML), LaTeX, components, themes, presenter mode, export, and hosting. Prevents common mistakes with asset paths, deprecated features, non-existent layouts, and click animation syntax.
compatibility: Node.js >= 18
---

Use this skill whenever working with Slidev code. Read individual rule files for detailed explanations and code examples. Follow these principles:

- Use absolute paths for assets from `public/` — never relative paths
- Use curly braces for code block line highlighting — e.g. `{2,3}`
- Quote relative click positions — e.g. `v-click="'+1'"` not `v-click="+1"`
- Use four backticks for Magic Move, not three
- Split complex slides into multiple simpler ones rather than overloading a single slide

- rules/anti-patterns.md - Critical mistakes to avoid: deprecated features, incorrect paths, non-existent layouts
- rules/core-syntax.md - Slide separators, frontmatter structure, headmatter vs per-slide configuration
- rules/layouts.md - Built-in layouts, named slots, custom layout creation
- rules/code-blocks.md - Shiki highlighting, line highlighting syntax, Monaco editor, Magic Move
- rules/animations.md - Click animations (v-click, v-after), slide transitions, v-motion
- rules/components.md - Built-in components: Arrow, Link, Toc, SlidevVideo, RenderWhen
- rules/diagrams.md - Mermaid and PlantUML integration and configuration
- rules/assets.md - Images, videos, fonts - correct paths and public folder usage
- rules/themes.md - Using themes, theme configuration, ejecting themes
- rules/export.md - PDF, PNG, PPTX export and SPA build configuration
- rules/presenter.md - Presenter mode, speaker notes, timer
- rules/directory-structure.md - Project layout: components, layouts, public, setup, styles dirs
- rules/frontmatter-config.md - Complete headmatter and per-slide frontmatter reference
- rules/vue-context.md - Vue global context: $slidev, $clicks, $nav, composables
- rules/syntax-advanced.md - LaTeX, import code snippets, multiple entries, embedded styles
- rules/navigation.md - Keyboard shortcuts, navigation bar, slides overview
- rules/addons.md - Using addons with Slidev presentations
- rules/customization.md - Configuring Vite, Vue, UnoCSS, Monaco, Shiki, shortcuts, parser
- rules/global-layers.md - Persistent components: global-top, global-bottom, per-slide layers
- rules/tips.md - CSS Grid, absolute positioning, font-size, canvas scaling, color schema, router mode
- rules/editors.md - Integrated editor, VS Code extension, Prettier plugin