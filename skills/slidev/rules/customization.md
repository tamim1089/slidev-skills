# Slidev Customization

Configuring tools and extending Slidev functionality.

## Configure Vite

Slidev uses Vite under the hood. Create `vite.config.ts`:

```ts
import { defineConfig } from 'vite'

export default defineConfig({
  slidev: {
    vue: { /* vue options */ },
    markdown: {
      markdownItSetup(md) {
        md.use(/* custom markdown-it plugins */)
      },
    },
  },
})
```

Pre-installed plugins:
- `@vitejs/plugin-vue`
- `unplugin-vue-components`
- `unplugin-icons`
- `vite-plugin-vue-markdown`
- `vite-plugin-remote-assets`
- `unocss/vite`

## Configure Vue

Create `setup/main.ts` for Vue app extensions:

```ts
import { defineAppSetup } from '@slidev/types'

export default defineAppSetup(({ app, router }) => {
  app.use(YourPlugin)
})
```

## Configure UnoCSS

Create `uno.config.ts`:

```ts
import { defineConfig } from 'unocss'

export default defineConfig({
  shortcuts: {
    'bg-main': 'bg-white text-[#181818] dark:(bg-[#121212] text-[#ddd])',
  },
})
```

Built-in presets: `@unocss/preset-uno`, `@unocss/preset-attributify`, `@unocss/preset-icons`, `@unocss/preset-web-fonts`, `@unocss/transformer-directives`.

## Configure Shiki

Create `setup/shiki.ts`:

```ts
import { defineShikiSetup } from '@slidev/types'

export default defineShikiSetup(() => {
  return {
    themes: {
      dark: 'min-dark',
      light: 'min-light',
    },
    transformers: [],
  }
})
```

For custom themes/languages:
```ts
import customTheme from './customTheme.tmTheme.json'

export default defineShikiSetup(() => ({
  themes: { dark: customTheme, light: 'min-light' },
  langs: ['js', 'typescript', customLanguage],
}))
```

## Configure Monaco

Create `setup/monaco.ts`:

```ts
import { defineMonacoSetup } from '@slidev/types'

export default defineMonacoSetup(async (monaco) => {
  return {
    editorOptions: {
      wordWrap: 'on',
    },
  }
})
```

### TypeScript Types

Types for dependencies are auto-imported from locally installed packages:

```md
---
monacoTypesAdditionalPackages:
  - lodash-es
---
```

Use Auto Type Acquisition (ATA) from CDN:
```md
---
monacoTypesSource: ata
---
```

### Monaco Theme

Since v0.48, Monaco reuses the Shiki theme automatically via `@shikijs/monaco`.

### Disable Monaco

```yaml
---
monaco: false   # or 'dev' / 'build'
---
```

## Configure Parser

Custom markdown preparser extensions via `setup/preparser.ts`:

```ts
import { definePreparserSetup } from '@slidev/types'

export default definePreparserSetup(({ filepath, headmatter, mode }) => {
  return [
    {
      transformRawLines(lines) {
        // Mutate raw lines before parsing
      },
      transformSlide(content, frontmatter) {
        // Transform each slide after splitting
      },
      name: 'my-extension',
    },
  ]
})
```

## Configure KaTeX

Create `setup/katex.ts`:

```ts
import { defineKatexSetup } from '@slidev/types'

export default defineKatexSetup(() => {
  return {
    /* KaTeX options */
  }
})
```

## Configure Mermaid

Create `setup/mermaid.ts`:

```ts
import { defineMermaidSetup } from '@slidev/types'

export default defineMermaidSetup(() => {
  return {
    theme: 'forest',
    themeVariables: {
      noteBkgColor: '#181d29',
      noteTextColor: '#F3EFF5cc',
      noteBorderColor: '#404551',
      actorBkg: '#0E131F',
      actorBorder: '#44FFD2',
      actorTextColor: '#F3EFF5',
      signalColor: '#F3EFF5',
      signalTextColor: '#F3EFF5',
    },
  }
})
```