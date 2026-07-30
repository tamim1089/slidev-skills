<script setup>
import { ref } from 'vue'
import { VueFlow } from '@vue-flow/core'
import { Background } from '@vue-flow/background'

const nodes = ref([
  {
    id: 'coreA',
    position: { x: 50, y: 50 },
    data: { label: 'Core A\n(Private Cache)' },
    style: { border: '1px solid #111', background: '#fff', padding: '10px', width: '150px', textAlign: 'center', borderRadius: '0' }
  },
  {
    id: 'coreB',
    position: { x: 50, y: 150 },
    data: { label: 'Core B\n(Private Cache)' },
    style: { border: '1px solid #111', background: '#fff', padding: '10px', width: '150px', textAlign: 'center', borderRadius: '0' }
  },
  {
    id: 'bus',
    position: { x: 300, y: 100 },
    data: { label: 'The Bus\n(Shared Medium)' },
    style: { border: '1px solid #d92d20', background: '#fff', color: '#d92d20', padding: '10px', width: '150px', textAlign: 'center', borderRadius: '0', fontWeight: 'bold' }
  },
  {
    id: 'memory',
    position: { x: 550, y: 100 },
    data: { label: 'Main Memory\n(Public Truth)' },
    style: { border: '1px solid #111', background: '#fff', padding: '10px', width: '150px', textAlign: 'center', borderRadius: '0' }
  }
])

const edges = ref([
  { id: 'e-a-bus', source: 'coreA', target: 'bus', animated: true, style: { stroke: '#111', strokeWidth: 1 } },
  { id: 'e-b-bus', source: 'coreB', target: 'bus', animated: true, style: { stroke: '#111', strokeWidth: 1 } },
  { id: 'e-bus-mem', source: 'bus', target: 'memory', animated: true, style: { stroke: '#111', strokeWidth: 1 } }
])
</script>

<template>
  <div style="height: 300px; border: 1px solid rgba(17,17,17,0.15);">
    <VueFlow :nodes="nodes" :edges="edges" :fit-view-on-init="true">
      <Background pattern-color="#ccc" :gap="16" />
    </VueFlow>
  </div>
</template>
