<script setup>
import { ref, onMounted, watch } from 'vue'
import * as d3 from 'd3'

const props = defineProps({
  showExploration: { type: Boolean, default: false },
  showSATrajectory: { type: Boolean, default: false },
  showGAPopulation: { type: Boolean, default: false },
  showPSOSwarm: { type: Boolean, default: false }
})

const svgRef = ref(null)

const W = 640
const H = 480
const margin = { top: 10, right: 30, bottom: 30, left: 30 }
const innerW = W - margin.left - margin.right
const innerH = H - margin.top - margin.bottom

const xScale = d3.scaleLinear().domain([-2, 2]).range([0, innerW])
const yScale = d3.scaleLinear().domain([-2, 2]).range([innerH, 0])

function f(x, y) {
  const a = 1 + (x + y + 1) ** 2 * (19 - 14 * x + 3 * x ** 2 - 14 * y + 6 * x * y + 3 * y ** 2)
  const b = 30 + (2 * x - 3 * y) ** 2 * (18 - 32 * x + 12 * x ** 2 + 48 * y - 36 * x * y + 27 * y ** 2)
  return Math.log(a * b)
}

function render() {
  const svg = d3.select(svgRef.value)
  svg.selectAll('*').remove()
  svg.attr('width', W).attr('height', H)

  const g = svg.append('g').attr('transform', `translate(${margin.left},${margin.top})`)

  const n = 180
  const grid = new Float64Array(n * n)
  for (let j = 0; j < n; j++) {
    for (let i = 0; i < n; i++) {
      const x = -2 + (4 * i) / (n - 1)
      const y = -2 + (4 * j) / (n - 1)
      grid[j * n + i] = f(x, y)
    }
  }

  const thresholds = d3.ticks(d3.min(grid), d3.max(grid), 10)
  const contours = d3.contours().size([n, n]).thresholds(thresholds)(grid)

  const xS = d3.scaleLinear().domain([0, n - 1]).range([0, innerW])
  const yS = d3.scaleLinear().domain([0, n - 1]).range([innerH, 0])

  g.selectAll('path.contour')
    .data(contours)
    .join('path')
    .attr('d', d => {
      const t = { type: 'MultiPolygon', coordinates: d.coordinates.map(p => p.map(r => r.map(([x, y]) => [xS(x), yS(y)]))) }
      return d3.geoPath()(t)
    })
    .attr('fill', 'none')
    .attr('stroke', 'rgba(17,17,17,0.1)')
    .attr('stroke-width', 0.8)

  const globalX = xScale(0), globalY = yScale(-1)
  g.append('circle').attr('cx', globalX).attr('cy', globalY).attr('r', 5).attr('fill', '#d92d20')
  g.append('circle').attr('cx', globalX).attr('cy', globalY).attr('r', 10).attr('fill', 'none').attr('stroke', '#d92d20').attr('stroke-width', 1.5).attr('opacity', 0.3)
  g.append('text').attr('x', globalX + 14).attr('y', globalY + 4).attr('font-size', '10px').attr('font-weight', '700').attr('fill', '#d92d20').text('f(0, –1) = 3')

  const locMin = [[-0.6, -0.4], [1.2, 0.8], [1.8, 0.2]]
  locMin.forEach(([lx, ly]) => {
    g.append('circle').attr('cx', xScale(lx)).attr('cy', yScale(ly)).attr('r', 3).attr('fill', 'rgba(217,45,32,0.3)')
  })

  if (props.showExploration) {
    g.append('path')
      .attr('d', `M${xScale(-1.5)},${yScale(-0.5)} Q${xScale(-0.5)},${yScale(-1.8)} ${xScale(0.5)},${yScale(-0.3)}`)
      .attr('fill', 'none').attr('stroke', '#555').attr('stroke-width', 2).attr('stroke-dasharray', '6 3')
      .attr('marker-end', 'url(#arrowGray)')
    g.append('text').attr('x', xScale(-0.5)).attr('y', yScale(-1.7)).attr('font-size', '10px').attr('font-weight', '700').attr('fill', '#555').text('exploration')

    g.append('path')
      .attr('d', `M${xScale(0.1)},${yScale(-0.8)} L${xScale(0.3)},${yScale(-1.0)}`)
      .attr('fill', 'none').attr('stroke', '#333').attr('stroke-width', 2).attr('marker-end', 'url(#arrowDark)')
    g.append('text').attr('x', xScale(0.15)).attr('y', yScale(-0.75)).attr('font-size', '10px').attr('font-weight', '700').attr('fill', '#333').text('exploitation')
  }

  if (props.showSATrajectory) {
    const pts = []
    let cx = 1.2, cy = 0.5
    for (let t = 0; t < 60; t++) {
      const T = Math.max(0.01, 5 / (1 + t * 0.08))
      cx += (Math.random() - 0.5) * T * 0.12
      cy += (Math.random() - 0.5) * T * 0.12
      cx += (0 - cx) * 0.008
      cy += (-1 - cy) * 0.008
      pts.push({ x: cx, y: cy })
    }
    const line = d3.line().x(d => xScale(d.x)).y(d => yScale(d.y))
    g.append('path').attr('d', line(pts)).attr('fill', 'none').attr('stroke', '#d92d20').attr('stroke-width', 2).attr('opacity', 0.7)
    g.append('circle').attr('cx', xScale(pts[0].x)).attr('cy', yScale(pts[0].y)).attr('r', 4).attr('fill', '#d92d20').attr('opacity', 0.5)
    g.append('text').attr('x', xScale(pts[0].x) - 10).attr('y', yScale(pts[0].y) - 10).attr('font-size', '9px').attr('fill', '#d92d20').attr('opacity', 0.7).text('start')
  }

  if (props.showGAPopulation) {
    const pop = []
    for (let i = 0; i < 25; i++) {
      pop.push({ x: -1.5 + Math.random() * 3, y: -1.5 + Math.random() * 3 })
    }
    g.selectAll('circle.ga').data(pop).join('circle')
      .attr('cx', d => xScale(d.x)).attr('cy', d => yScale(d.y))
      .attr('r', 4).attr('fill', '#555').attr('opacity', 0.6).attr('class', 'ga')
  }

  if (props.showPSOSwarm) {
    const particles = []
    for (let i = 0; i < 12; i++) {
      const px = -1 + Math.random() * 2
      const py = -1 + Math.random() * 2
      particles.push({ x: px, y: py, vx: (0 - px) * 0.15 + (Math.random() - 0.5) * 0.2, vy: (-1 - py) * 0.15 + (Math.random() - 0.5) * 0.2 })
    }
    g.selectAll('circle.pso').data(particles).join('circle')
      .attr('cx', d => xScale(d.x)).attr('cy', d => yScale(d.y))
      .attr('r', 5).attr('fill', '#d92d20').attr('opacity', 0.7).attr('class', 'pso')
    g.selectAll('line.pso').data(particles).join('line')
      .attr('x1', d => xScale(d.x)).attr('y1', d => yScale(d.y))
      .attr('x2', d => xScale(d.x + d.vx * 0.3)).attr('y2', d => yScale(d.y + d.vy * 0.3))
      .attr('stroke', '#d92d20').attr('stroke-width', 1.5).attr('opacity', 0.5).attr('class', 'pso')
      .attr('marker-end', 'url(#arrowRed)')
  }

  svg.append('defs').html(`
    <marker id="arrowGray" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10" fill="#555"/></marker>
    <marker id="arrowDark" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10" fill="#333"/></marker>
    <marker id="arrowRed" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10" fill="#d92d20"/></marker>
  `)
}

onMounted(render)
watch(() => [props.showExploration, props.showSATrajectory, props.showGAPopulation, props.showPSOSwarm], render)
</script>

<template>
  <div style="position:relative;display:inline-block;">
    <svg ref="svgRef"></svg>
  </div>
</template>
