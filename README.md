# Slidev Agent Skills

Agent Skills for [Slidev](https://sli.dev) — the developer-friendly presentation tool that turns Markdown into beautiful slides with live coding, diagrams, LaTeX, and interactive Vue components.

Use these skills when writing or editing Slidev presentations. They encode best practices, provide complete configuration references, and prevent common mistakes — saving you from incorrect asset paths, deprecated features, non-existent layouts, and syntax errors.

## Installation

```bash
npx skills add tamim1089/slidev-skills
```

Or manually copy `skills/slidev` to `.claude/skills/` or `.github/skills/` in your project.

## Skills Overview

### Core Slide Authoring
| File | Covers |
|------|--------|
| `core-syntax.md` | Slide separators, frontmatter structure, headmatter vs per-slide config, speaker notes, MDC syntax, escaping |
| `syntax-advanced.md` | LaTeX math, import code snippets, multiple entries, embedded styles, template slots, Prettier support |
| `layouts.md` | All built-in layouts, two-column/two-cols-header, image/iframe layouts, named slots, custom layouts, layout props |
| `code-blocks.md` | Shiki highlighting, line highlighting with clicks, Monaco editor/runner/diff/write, Magic Move, TwoSlash, line numbers |
| `animations.md` | v-click/v-after/v-clicks directives, click positioning, v-switch, v-motion, v-mark, slide transitions (built-in, custom, view-transitions), element transition CSS classes, v-click-gap |

### Content
| File | Covers |
|------|--------|
| `components.md` | Arrow, VDragArrow, Link, Toc, SlidevVideo, Youtube, Tweet, Transform, AutoFitText, LightOrDark, RenderWhen, VSwitch, VDrag, Titles, PoweredBySlidev, VAfter |
| `diagrams.md` | Mermaid (flowchart, sequence, class, state, ER, pie, gantt) with options, PlantUML with server config, click animations workaround |
| `assets.md` | Public folder, absolute paths, images, backgrounds, remote images, videos, fonts (Google/local/providers/weights), Iconify icons |

### Configuration & Customization
| File | Covers |
|------|--------|
| `frontmatter-config.md` | Complete headmatter reference (theme, metadata, presenter, export, code, assets, appearance, fonts, drawing, HTML attrs) + per-slide + defaults block |
| `customization.md` | Vite config, Vue app setup, UnoCSS, Shiki themes/languages, Monaco config/types/themes, KaTeX, Mermaid setup, shortcut bindings, parser extensions |
| `themes.md` | Using official/community themes, theme config, local themes, ejecting, overriding styles/layouts/components, addons, writing themes (conventions, defaults, color schema, metadata) |
| `global-layers.md` | global-top/bottom, slide-top/bottom, custom-nav-controls with examples (footer, page numbers, conditional visibility) |

### Presentation & Export
| File | Covers |
|------|--------|
| `presenter.md` | Presenter mode, speaker notes with click markers, timer, remote control (with password), recording, drawing (stylus, SVG persist), keyboard shortcuts, dual screen setup |
| `export.md` | PDF/PNG/PPTX/MD export, SPA build, Playwright setup, range export, wait options, multiple entries, dark mode, export-notes, hosting (GitHub Pages, Netlify, Vercel) |
| `navigation.md` | Navigation bar buttons, keyboard shortcuts table, slides overview, remote control, custom shortcut bindings via setup/shortcuts.ts |

### Architecture & Context
| File | Covers |
|------|--------|
| `directory-structure.md` | Project layout: components, layouts, public, setup, styles, index.html, global layers — all conventions explained |
| `vue-context.md` | $slidev global, $clicks, $page, $renderContext, $nav/$slidev.nav, $slidev.configs, $slidev.themeConfigs, composable API, anti-pattern note on internal imports |
| `tips.md` | CSS Grid layouts, absolute positioning, font-size adjustments, canvasWidth scaling, Transform component |
| `addons.md` | Using addons (install via npm, configure in frontmatter or package.json), addons vs themes, examples |
| `editors.md` | Integrated editor, VS Code extension features/installation/usage, Prettier plugin |

### Safety
| File | Covers |
|------|--------|
| `anti-patterns.md` | Asset paths, removed Prism, non-existent layouts, internal client imports, click animation syntax, code block highlighting, Monaco syntax, Magic Move syntax, two-cols slots, Node.js version |

## Links

- [Slidev Documentation](https://sli.dev)
- [Agent Skills Specification](https://agentskills.io)

## License

MIT