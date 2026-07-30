<script setup>
import { ref, onMounted } from 'vue'
import * as d3 from 'd3'

const svgRef = ref(null)

const W = 600, H = 320
const margin = { top: 20, right: 60, bottom: 30, left: 50 }
const innerW = W - margin.left - margin.right
const innerH = H - margin.top - margin.bottom

function makeData(offset, decay) {
  const pts = []
  for (let t = 0; t < 500; t++) {
    const val = Math.exp(-t / (50 * decay)) + offset * (1 + Math.sin(t * 0.05) * 0.3) * Math.exp(-t / 200)
    pts.push({ t, val: Math.max(0.01, val) })
  }
  return pts
}

function render() {
  const svg = d3.select(svgRef.value)
  svg.selectAll('*').remove()
  svg.attr('width', W).attr('height', H)

  const g = svg.append('g').attr('transform', `translate(${margin.left},${margin.top})`)

  const x = d3.scaleLinear().domain([0, 500]).range([0, innerW])
  const y = d3.scaleLog().domain([0.01, 10]).range([innerH, 0])

  const lines = [
    { data: makeData(0.8, 1.0), label: 'SA (logarithmic)', color: '#d92d20', dash: '' },
    { data: makeData(1.2, 0.6), label: 'GA (stepwise)', color: '#555', dash: '4 2' },
    { data: makeData(0.5, 1.5), label: 'PSO (fast)', color: '#333', dash: '2 2' }
  ]

  const line = d3.line().x(d => x(d.t)).y(d => y(d.val))

  lines.forEach(l => {
    g.append('path')
      .attr('d', line(l.data))
      .attr('fill', 'none')
      .attr('stroke', l.color)
      .attr('stroke-width', 1.5)
      .attr('stroke-dasharray', l.dash)
  })

  g.append('g').call(d3.axisLeft(y).ticks(5, '.1f'))
    .selectAll('text').attr('font-size', '9px').attr('color', '#555')
  g.append('g').attr('transform', `translate(0,${innerH})`).call(d3.axisBottom(x).ticks(5))
    .selectAll('text').attr('font-size', '9px').attr('color', '#555')

  g.append('text').attr('x', -30).attr('y', 10).attr('transform', 'rotate(-90)').attr('font-size', '9px').attr('fill', '#555').text('best fitness (log)')
  g.append('text').attr('x', innerW / 2).attr('y', innerH + 22).attr('text-anchor', 'middle').attr('font-size', '9px').attr('fill', '#555').text('iteration')

  const legend = svg.append('g').attr('transform', `translate(${W - margin.right + 10}, ${margin.top})`)
  lines.forEach((l, i) => {
    const ley = i * 18
    legend.append('line').attr('x1', 0).attr('y1', ley + 6).attr('x2', 16).attr('y2', ley + 6).attr('stroke', l.color).attr('stroke-width', 1.5).attr('stroke-dasharray', l.dash)
    legend.append('text').attr('x', 22).attr('y', ley + 10).attr('font-size', '9px').attr('fill', '#555').text(l.label)
  })
}

onMounted(render)
</script>

<template>
  <svg ref="svgRef"></svg>
</template>
