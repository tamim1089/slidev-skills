# Slidev Navigation

Navigation controls, keyboard shortcuts, and slides overview.

## Navigation Bar

Move mouse to bottom-left corner to reveal the navigation bar.

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `Space` / `→` / `↓` | Next animation/slide |
| `←` / `↑` | Previous animation/slide |
| `F` | Toggle fullscreen |
| `O` | Toggle slides overview |
| `D` | Toggle dark mode |
| `P` | Toggle presenter mode |
| `R` | Toggle recording |
| `G` | Show go-to dialog |
| `Escape` | Exit current mode |

## Slides Overview

Press `O` or click the grid icon to see all slides at once for quick navigation.

## Navigation Bar Buttons

- <carbon-arrow-right /> - Next animation or slide
- <carbon-arrow-left /> - Previous animation or slide
- <carbon-apps /> - Toggle slides overview
- <carbon-sun /> / <carbon-moon /> - Toggle dark mode
- <carbon-user-avatar /> - Toggle camera view
- <carbon-video /> - Toggle recording
- <carbon-user-speaker /> - Enter presenter mode
- <carbon-edit /> - Toggle integrated editor
- <carbon-download /> - Download slides (SPA build only)
- <carbon-information /> - Show slide information
- <carbon-settings-adjust /> - Show settings menu

## Remote Control

Start with remote access:
```bash
slidev --remote            # Anyone on network can control
slidev --remote=mypassword  # Password-protected
```

Displays a QR code for mobile access.

## Custom Shortcuts

Create `setup/shortcuts.ts` to customize keyboard shortcuts:

```ts
import type { NavOperations, ShortcutOptions } from '@slidev/types'
import { defineShortcutsSetup } from '@slidev/types'

export default defineShortcutsSetup((nav: NavOperations, base: ShortcutOptions[]) => {
  return [
    ...base,
    {
      key: 'enter',
      fn: () => nav.next(),
      autoRepeat: true,
    },
    {
      key: 'ShiftLeft+ArrowRight',
      fn: () => nav.next(),
      autoRepeat: true,
    },
  ]
})
```