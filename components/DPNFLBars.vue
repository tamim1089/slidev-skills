<script setup>
import { ref, onMounted } from 'vue'
import * as d3 from 'd3'

const svgRef = ref(null)

const data = [
  { problem: 'P₁', perf: 0.85 },
  { problem: 'P₂', perf: 0.32 },
  { problem: 'P₃', perf: 0.71 },
  { problem: 'P₄', perf: 0.94 },
  { problem: 'P₅', perf: 0.18 },
  { problem: 'P₆', perf: 0.57 }
]
const avg = d3.mean(data, d => d.perf)

const W = 500, H = 280
const margin = { top: 20, right: 20, bottom: 30, left: 40 }
const innerW = W - margin.left - margin.right
const innerH = H - margin.top - margin.bottom

function render() {
  const svg = d3.select(svgRef.value)
  svg.selectAll('*').remove()
  svg.attr('width', W).attr('height', H)

  const g = svg.append('g').attr('transform', `translate(${margin.left},${margin.top})`)

  const x = d3.scaleBand().domain(data.map(d => d.problem)).range([0, innerW]).padding(0.3)
  const y = d3.scaleLinear().domain([0, 1]).range([innerH, 0])

  g.selectAll('rect')
    .data(data)
    .join('rect')
    .attr('x', d => x(d.problem))
    .attr('y', d => y(d.perf))
    .attr('width', x.bandwidth())
    .attr('height', d => innerH - y(d.perf))
    .attr('fill', '#555')
    .attr('opacity', 0.6)

  g.append('line')
    .attr('x1', 0).attr('x2', innerW)
    .attr('y1', y(avg)).attr('y2', y(avg))
    .attr('stroke', '#d92d20').attr('stroke-width', 1.5).attr('stroke-dasharray', '4 2')

  g.append('text')
    .attr('x', innerW).attr('y', y(avg) - 6)
    .attr('text-anchor', 'end').attr('font-size', '9px').attr('font-weight', '700').attr('fill', '#d92d20')
    .text(`average = ${avg.toFixed(2)}`)

  g.append('g').call(d3.axisLeft(y).ticks(5).tickFormat(d3.format('.0%')))
    .selectAll('text').attr('font-size', '9px').attr('color', '#555')

  g.append('g').attr('transform', `translate(0,${innerH})`).call(d3.axisBottom(x))
    .selectAll('text').attr('font-size', '9px').attr('color', '#555')
}

onMounted(render)
</script>

<template>
  <svg ref="svgRef"></svg>
</template>
