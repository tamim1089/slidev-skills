# Slidev Addons

Addons extend Slidev with additional components, layouts, styles, and configuration.

## Using Addons

Unlike themes, addons don't affect global styles and multiple addons can be used together.

### Installation

```bash
npm install slidev-addon-package
```

### Configuration

Add to frontmatter:
```yaml
---
addons:
  - slidev-addon-package1
  - slidev-addon-package2
---
```

Or in `package.json`:
```json
{
  "slidev": {
    "addons": ["slidev-addon-package1"]
  }
}
```

## Addons vs Themes

| Aspect | Theme | Addon |
|--------|-------|-------|
| Global styles | Yes | No (minimal) |
| Multiple at once | No (one theme) | Yes |
| Purpose | Visual design | Feature extension |

## Examples

- `slidev-addon-qrcode` - Embed QR codes in slides
- `slidev-addon-remoji` - Replace emoji with icons for consistent rendering
- `slidev-addon-citations` - Citation/reference support