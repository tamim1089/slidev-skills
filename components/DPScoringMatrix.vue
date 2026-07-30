<script setup>
import { ref, onMounted, watch } from 'vue'
import * as d3 from 'd3'

const props = defineProps({
  showTraceback: { type: Boolean, default: false }
})

const tbSvg = ref(null)

const seq1 = ['A', 'C', 'G', 'T', 'A', 'C']
const seq2 = ['G', 'C', 'G', 'T', 'A', 'C', 'G']

const matrix = [
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 2, 1, 0],
  [0, 0, 2, 1, 0, 1, 3, 2],
  [0, 2, 1, 4, 3, 2, 2, 5],
  [0, 1, 1, 0, 6, 5, 4, 4],
  [0, 0, 0, 0, 5, 8, 7, 6],
  [0, 0, 2, 1, 4, 7, 10, 9]
]

const tracebackPath = [[6, 6], [5, 5], [4, 4], [3, 3], [2, 2]]
const tracebackSet = new Set(
  tracebackPath.map(([r, c]) => `${r},${c}`)
)
const maxScore = 10

const cellW = 52
const cellH = 30
const gap = 1
const headerW = 32
const headerH = 28

const gridW = 2 + headerW + gap + 8 * (cellW + gap)
const gridH = 2 + headerH + gap + 7 * (cellH + gap)

function cellBg(v) {
  if (v === 0) return '#fdfdfc'
  const g = Math.round(240 - (v / maxScore) * 120)
  return `rgb(${g},${g},${g})`
}

function cellColor(v) {
  if (v === 0) return '#bbb'
  return v > 4 ? '#fff' : '#111'
}

function cx(j) {
  return 1 + headerW + gap + j * (cellW + gap) + cellW / 2
}

function cy(i) {
  return 1 + headerH + gap + i * (cellH + gap) + cellH / 2
}

function renderTraceback() {
  const svg = d3.select(tbSvg.value)
  svg.selectAll('*').remove()

  if (!props.showTraceback) return

  svg.attr('width', gridW).attr('height', gridH)
    .style('position', 'absolute')
    .style('top', '0')
    .style('left', '0')
    .style('pointer-events', 'none')

  const pts = tracebackPath.map(([r, c]) => ({
    x: cx(c), y: cy(r)
  }))

  svg.append('path')
    .attr('d', d3.line().x(d => d.x).y(d => d.y)(pts))
    .attr('fill', 'none')
    .attr('stroke', '#d92d20')
    .attr('stroke-width', 3)
    .attr('stroke-linecap', 'round')
    .attr('stroke-linejoin', 'round')

  tracebackPath.forEach(([r, c]) => {
    svg.append('rect')
      .attr('x', 1 + headerW + gap + c * (cellW + gap) + 2)
      .attr('y', 1 + headerH + gap + r * (cellH + gap) + 2)
      .attr('width', cellW - 4)
      .attr('height', cellH - 4)
      .attr('fill', 'none')
      .attr('stroke', '#d92d20')
      .attr('stroke-width', 2.5)
  })

  const [mr, mc] = tracebackPath[0]
  svg.append('text')
    .attr('x', cx(mc))
    .attr('y', 1 + headerH + gap + mr * (cellH + gap) - 4)
    .attr('text-anchor', 'middle')
    .attr('font-size', '9px')
    .attr('font-weight', '700')
    .attr('fill', '#d92d20')
    .text('MAX')

  const [er, ec] = tracebackPath[tracebackPath.length - 1]
  svg.append('text')
    .attr('x', cx(ec))
    .attr('y', 1 + headerH + gap + (er + 1) * (cellH + gap) + 10)
    .attr('text-anchor', 'middle')
    .attr('font-size', '9px')
    .attr('font-weight', '700')
    .attr('fill', '#d92d20')
    .text('STOP')
}

onMounted(renderTraceback)
watch(() => props.showTraceback, renderTraceback)
</script>

<template>
  <div style="position:relative;display:inline-block;font-family:'JetBrains Mono','Courier New',monospace">
    <div style="display:grid;grid-template-columns:32px repeat(8,52px);gap:1px;background:#e0ddd5;border:1px solid #e0ddd5;">

      <div style="background:#fdfdfc;"></div>
      <div style="background:#fdfdfc;text-align:center;font-size:10px;color:#a0a0a0;line-height:28px;">0</div>
      <div v-for="(ch,ci) in seq2" :key="'ch'+ci"
        style="background:#fdfdfc;text-align:center;font-size:13px;font-weight:700;color:#111;line-height:28px;">{{ ch }}</div>

      <template v-for="(row, i) in matrix" :key="'r'+i">
        <div v-if="i===0" style="background:#fdfdfc;text-align:center;font-size:10px;color:#a0a0a0;line-height:30px;">0</div>
        <div v-else style="background:#fdfdfc;text-align:center;font-size:13px;font-weight:700;color:#111;line-height:30px;">{{ seq1[i-1] }}</div>
        <div v-for="(v, j) in row" :key="'c'+i+j"
          :style="{
            background: cellBg(v),
            textAlign: 'center',
            fontSize: '12px',
            fontWeight: v > 0 ? 700 : 400,
            color: cellColor(v),
            lineHeight: cellH + 'px'
          }">{{ v }}</div>
      </template>
    </div>

    <svg ref="tbSvg"></svg>
  </div>
</template>
