<script setup>
import { ref, computed } from 'vue'
import { VueFlow } from '@vue-flow/core'

const props = defineProps({
  variant: { type: String, default: 'generic' }
})

const variants = {
  generic: { init: 'Init Pop', eval: 'Evaluate', gen: 'Generate New', accept: 'Select/Accept', term: 'Terminate?' },
  sa: { init: 'Init x₀, T₀', eval: 'Eval f(x)', gen: 'Perturb → x\'', accept: 'P(accept) = min(1, e^{–Δ/T})', term: 'T < T_min?' },
  ga: { init: 'Init Population', eval: 'Eval Fitness', gen: 'Select → Crossover → Mutate', accept: 'Replace Population', term: 'Gen = Max?' },
  pso: { init: 'Init Particles', eval: 'Eval f(xᵢ)', gen: 'Update vᵢ, xᵢ', accept: 'Update pBest, gBest', term: 'Max iter?' }
}

const v = computed(() => variants[props.variant] || variants.generic)

const nodes = ref([
  { id: 'start', position: { x: 200, y: 0 }, data: { label: 'Start' }, style: { border: '1px solid #111', background: '#fff', borderRadius: 0, padding: '6px 14px', fontWeight: 700, fontSize: '12px' } },
  { id: 'init', position: { x: 200, y: 70 }, data: { label: '' }, style: { border: '1px solid #111', background: '#fff', borderRadius: 0, padding: '6px 14px', fontSize: '11px' } },
  { id: 'eval', position: { x: 200, y: 140 }, data: { label: '' }, style: { border: '1px solid #111', background: '#fff', borderRadius: 0, padding: '6px 14px', fontSize: '11px' } },
  { id: 'gen', position: { x: 200, y: 210 }, data: { label: '' }, style: { border: '1px solid #111', background: '#fff', borderRadius: 0, padding: '6px 14px', fontSize: '11px' } },
  { id: 'accept', position: { x: 200, y: 280 }, data: { label: '' }, style: { border: '1px solid #111', background: '#fff', borderRadius: 0, padding: '6px 14px', fontSize: '11px' } },
  { id: 'term', position: { x: 200, y: 350 }, data: { label: '' }, style: { border: '1px solid #d92d20', background: '#fff', borderRadius: 0, padding: '6px 14px', fontSize: '11px', color: '#d92d20' } },
  { id: 'end', position: { x: 200, y: 420 }, data: { label: 'End' }, style: { border: '1px solid #111', background: '#fff', borderRadius: 0, padding: '6px 14px', fontWeight: 700, fontSize: '12px' } }
])

const edges = ref([
  { id: 'e1', source: 'start', target: 'init', style: { stroke: '#111', strokeWidth: 1 } },
  { id: 'e2', source: 'init', target: 'eval', style: { stroke: '#111', strokeWidth: 1 } },
  { id: 'e3', source: 'eval', target: 'gen', style: { stroke: '#111', strokeWidth: 1 } },
  { id: 'e4', source: 'gen', target: 'accept', style: { stroke: '#111', strokeWidth: 1 } },
  { id: 'e5', source: 'accept', target: 'term', style: { stroke: '#111', strokeWidth: 1 } },
  { id: 'e6', source: 'term', target: 'eval', label: 'no', animated: true, style: { stroke: '#111', strokeWidth: 1, strokeDasharray: '4 2' } },
  { id: 'e7', source: 'term', target: 'end', label: 'yes', style: { stroke: '#111', strokeWidth: 1 } }
])
</script>

<template>
  <div style="height:500px;">
    <VueFlow :nodes="nodes" :edges="edges" :fit-view-on-init="true" :nodes-draggable="false" :nodes-connectable="false">
      <template #node-default="nodeProps">
        <div>{{ nodeProps.data?.label || v[nodeProps.id] }}</div>
      </template>
    </VueFlow>
  </div>
</template>
