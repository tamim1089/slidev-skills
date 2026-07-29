# Slidev Vue Global Context

Slidev injects a global Vue context for advanced conditions and navigation controls.

## `$slidev` Global Property

Accessible anywhere in markdown and Vue templates.

```md
Current page is: {{ $slidev.nav.currentPage }}
```

```html
<button @click="$slidev.nav.next">Next</button>
```

## `$clicks`

Current click count on the current slide. Use for conditional rendering.

```html
<div v-if="$clicks > 3">Visible after 3 clicks</div>
```

Prefer `$clicks` over `$slidev.nav.clicks` to avoid cross-slide click state issues.

## `$page`

Current page number (1-indexed).

```md
Page: {{ $page }}
```

## `$renderContext`

Current render context: `'slide'`, `'overview'`, `'presenter'`, `'previewNext'`

```md
<div v-if="$renderContext === 'slide'">
  Only visible in main slide view
</div>
```

## `$slidev.nav` / `$nav`

Navigation controls and state. `$nav` is shorthand (since v0.43).

```js
$nav.next()           // Go to next click/slide
$nav.nextSlide()      // Go to next slide (skip v-clicks)
$nav.prev()           // Go to previous
$nav.go(10)           // Go to slide number 10
$nav.currentPage      // Current slide number
$nav.currentLayout    // Current layout name
$nav.total            // Total number of slides
$nav.clicks           // Global click count
$nav.isPresenter      // Whether in presenter mode
```

## `$slidev.configs`

Reactive parsed headmatter config.

```yaml
---
title: My Presentation
---
```

```
{{ $slidev.configs.title }}  // 'My Presentation'
```

## `$slidev.themeConfigs`

Reactive parsed theme configuration.

```yaml
---
themeConfig:
  primary: '#213435'
---
```

```
{{ $slidev.themeConfigs.primary }}  // '#213435'
```

## Composable API (Since v0.48)

Import public composables from `@slidev/client`:

```vue
<script setup>
import {
  onSlideEnter,
  onSlideLeave,
  useDarkMode,
  useIsSlideActive,
  useNav,
  useSlideContext
} from '@slidev/client'

const { $slidev } = useSlideContext()
const { currentPage, currentLayout, currentSlideRoute } = useNav()
const { isDark } = useDarkMode()
const isActive = useIsSlideActive()

onSlideEnter(() => { /* runs when slide becomes active */ })
onSlideLeave(() => { /* runs when slide becomes inactive */ })
</script>
```

Import types from `@slidev/types`:

```vue
<script setup>
import type { TocItem } from '@slidev/types'

function tocFunc(tree: TocItem[]): TocItem[] {
  // ...
}
</script>
```

## Anti-Pattern: Internal Imports

Do NOT import from internal `@slidev/client` subpaths:

```ts
// WRONG - internal paths break between versions
import { isDark } from '@slidev/client/logic/dark'

// CORRECT - use public API
import { useDarkMode, useNav } from '@slidev/client'
```