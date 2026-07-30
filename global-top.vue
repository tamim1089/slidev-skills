<template></template>

<style>
@import '@vue-flow/core/dist/style.css';
@import '@vue-flow/core/dist/theme-default.css';

:root {
  --bg-primary: #fdfdfc;
  --text-primary: #111111;
  --text-muted: #555555;

  --accent: #d92d20;

  --hairline: rgba(17, 17, 17, 0.15);

  --slide-padding: 64px;
}

.slidev-layout {
  color: var(--text-primary);
  background-color: var(--bg-primary) !important;
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  text-align: left;
}

.slidev-layout h1 {
  font-size: 64px;
  font-weight: 700;
  line-height: 1.05;
  letter-spacing: -0.03em;
  margin-bottom: 2rem;
}

.slidev-layout p, .slidev-layout li {
  font-size: 20px;
  line-height: 1.5;
  color: var(--text-muted);
}

.slidev-layout b, .slidev-layout strong {
  color: var(--text-primary);
  font-weight: 700;
}

.swiss-grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 24px;
  padding: var(--slide-padding);
  height: 100%;
  align-items: start;
}

.hairline-top { border-top: 1px solid var(--hairline); }
.hairline-bottom { border-bottom: 1px solid var(--hairline); }
.hairline-left { border-left: 1px solid var(--hairline); }
.hairline-right { border-right: 1px solid var(--hairline); }

.accent-text { color: var(--accent); }

.card, .slidev-layout .card {
  background: none;
  border: 1px solid var(--hairline);
  box-shadow: none;
  border-radius: 0;
  padding: 1.5rem;
}

.label-small {
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  font-weight: 700;
  color: var(--text-primary);
}

.mono {
  font-family: 'JetBrains Mono', 'Courier New', monospace;
}

.checkpoint-slide {
  background: var(--text-primary) !important;
  color: var(--bg-primary) !important;
}
.checkpoint-slide h1, .checkpoint-slide h2, .checkpoint-slide p, .checkpoint-slide .label-small {
  color: var(--bg-primary) !important;
}
.checkpoint-slide .hairline-top, .checkpoint-slide .hairline-bottom {
  border-color: rgba(253,253,252,0.22) !important;
}
</style>
