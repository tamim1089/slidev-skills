# Slidev Global Layers

Persistent components that render across slides.

## Available Layers

Create these files in the project root:

- `global-top.vue` - Renders above all slide content (single instance)
- `global-bottom.vue` - Renders below all slide content (single instance)
- `custom-nav-controls.vue` - Custom navigation buttons in the nav bar
- `layouts/slide-top.vue` - Renders at top of each slide (per-slide instance)
- `layouts/slide-bottom.vue` - Renders at bottom of each slide (per-slide instance)

## Z-Order (Top to Bottom)

1. NavControls (with `custom-nav-controls.vue`)
2. Global Top (`global-top.vue`)
3. Slide Top (`slide-top.vue`)
4. Slide Content
5. Slide Bottom (`slide-bottom.vue`)
6. Global Bottom (`global-bottom.vue`)

## Examples

### Global Footer
```html
<!-- global-bottom.vue -->
<template>
  <footer class="absolute bottom-0 left-0 right-0 p-2">
    Your Name
  </footer>
</template>
```

### Conditional Footer
```html
<!-- global-bottom.vue -->
<template>
  <footer
    v-if="$nav.currentLayout !== 'cover'"
    class="absolute bottom-0 left-0 right-0 p-2"
  >
    {{ $nav.currentPage }} / {{ $nav.total }}
  </footer>
</template>
```

### Page Numbers
```html
<!-- slide-bottom.vue -->
<template>
  <div class="absolute bottom-2 right-4 text-sm opacity-50">
    {{ $nav.currentPage }}
  </div>
</template>
```

### Custom Nav Button
```html
<!-- custom-nav-controls.vue -->
<template>
  <button class="icon-btn" title="Next" @click="$nav.next">
    <carbon:arrow-right />
  </button>
</template>
```

## Export Note

When exporting, use the `--per-slide` option to ensure global layers apply to each slide correctly.