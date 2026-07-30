import { defineMermaidSetup } from '@slidev/types'

export default defineMermaidSetup(() => {
  return {
    theme: 'dark',
    themeVariables: {
      fontFamily: 'Inter, sans-serif',
      primaryColor: '#242730', /* bg-raised */
      primaryTextColor: '#f0efe8',
      primaryBorderColor: '#333845',
      lineColor: '#8892a4',
      secondaryColor: '#1e2128',
      tertiaryColor: '#1a1c23'
    },
  }
})
