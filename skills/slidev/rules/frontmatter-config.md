# Slidev Frontmatter Configuration

Complete reference for headmatter and per-slide frontmatter.

## Headmatter (First Frontmatter Block)

The first frontmatter block configures the entire presentation.

```yaml
---
# THEME
theme: default                    # Theme id or npm package name
# METADATA
title: Slidev                     # Browser tab title
titleTemplate: '%s - Slidev'      # Title template (%s = page title)
info: false                       # Presentation description (markdown string)
author: Your Name                 # Author for exported PDF/PPTX
keywords: keyword1,keyword2       # Keywords for exported PDF
# PRESENTER
presenter: true                   # Enable presenter mode (boolean, 'dev', or 'build')
# EXPORT / DOWNLOAD
download: false                   # PDF download in SPA (boolean or URL)
exportFilename: slidev-exported   # Export filename
export:                           # Export options (camelCase CLI options)
  format: pdf
  timeout: 30000
  dark: false
  withClicks: false
  withToc: false
# CODE
highlighter: shiki                # Syntax highlighter (shiki only, prism removed)
lineNumbers: false                # Show line numbers in code blocks
monaco: true                      # Enable Monaco editor (boolean, 'dev', or 'build')
monacoTypesSource: local          # Monaco types source ('cdn', 'local', 'ata', 'none')
monacoTypesAdditionalPackages: [] # Extra packages for Monaco type imports
monacoRunAdditionalDeps: []       # Extra modules for Monaco runner
# ASSETS
remoteAssets: false               # Cache remote assets locally (boolean, 'dev', 'build')
# LAYOUT
selectable: true                  # Whether text is selectable
# RECORDING
record: dev                       # Enable recording (boolean, 'dev', or 'build')
# UI
contextMenu: true                 # Enable Slidev context menu (boolean, 'dev', 'build')
wakeLock: true                    # Enable wake lock (boolean, 'dev', 'build')
# APPEARANCE
colorSchema: auto                 # Color scheme ('auto', 'light', 'dark')
routerMode: history               # Vue-router mode ('history' or 'hash')
aspectRatio: 16/9                 # Slide aspect ratio
canvasWidth: 980                  # Canvas width in px
# THEME CONFIG
themeConfig:
  primary: '#5d8392'              # Theme customization vars
# FAVICON
favicon: 'https://...'            # Favicon URL or local path
# DIAGRAMS
plantUmlServer: 'https://www.plantuml.com/plantuml'
# FONTS
fonts:
  sans: Roboto
  serif: Roboto Slab
  mono: Fira Code
# DEFAULTS (applied to all slides)
defaults:
  layout: default
# DRAWING
drawings:
  enabled: true
  persist: false
  presenterOnly: false
  syncAll: true
# HTML
htmlAttrs:
  dir: ltr
  lang: en
---
```

## Per-Slide Frontmatter

These options go in frontmatter blocks between slides:

```yaml
---
layout: center              # Slide layout
class: text-center          # CSS classes for this slide
transition: fade            # Override transition
clicks: 3                   # Manual click count
disabled: false             # Completely hide slide
hide: false                 # Same as disabled
hideInToc: true             # Hide from table of contents
level: 2                    # Heading level for TOC
title: Custom Title         # Override title in TOC/Title component
preload: false              # Disable next-slide preloading
routeAlias: solutions       # Named route for Link component
src: ./subpage.md           # Include external markdown file
zoom: 0.8                   # Custom zoom scale
dragPos:                    # Positions for draggable elements
  left: '100px'
  top: '200px'
---
```

## Defaults Block

Set default frontmatter for all slides using the `defaults` key in headmatter:

```yaml
---
defaults:
  layout: default
  class: text-center
---
```

Individual slide frontmatter overrides these defaults.