<script setup>
import { ref } from 'vue'
import { VueFlow } from '@vue-flow/core'
import { Background } from '@vue-flow/background'
import { siLinux, siApple } from 'simple-icons'

const nodes = ref([
  {
    id: 'userA',
    position: { x: 50, y: 50 },
    type: 'custom',
    data: { label: 'Alice (Core A)', icon: siLinux.svg },
    style: { border: '1px solid #111', background: '#fff', width: '180px', borderRadius: '0' }
  },
  {
    id: 'userB',
    position: { x: 50, y: 200 },
    type: 'custom',
    data: { label: 'Bob (Core B)', icon: siApple.svg },
    style: { border: '1px solid #111', background: '#fff', width: '180px', borderRadius: '0' }
  },
  {
    id: 'whiteboard',
    position: { x: 400, y: 125 },
    data: { label: 'Public Whiteboard\n(Main Memory)' },
    style: { border: '1px solid #111', background: '#fff', padding: '10px', width: '180px', textAlign: 'center', borderRadius: '0', fontWeight: 'bold' }
  }
])

const edges = ref([
  { id: 'e1', source: 'userA', target: 'whiteboard', label: 'Yells update across room', animated: true, style: { stroke: '#d92d20', strokeWidth: 1 } },
  { id: 'e2', source: 'userB', target: 'whiteboard', label: 'Listens', animated: false, style: { stroke: '#111', strokeWidth: 1, strokeDasharray: '5 5' } }
])
</script>

<template>
  <div style="height: 350px; border: 1px solid rgba(17,17,17,0.15);">
    <VueFlow :nodes="nodes" :edges="edges" :fit-view-on-init="true">
      <Background pattern-color="#ccc" :gap="16" />
      <template #node-custom="props">
        <div style="display: flex; align-items: center; padding: 10px;">
          <div v-html="props.data.icon" style="width: 24px; height: 24px; margin-right: 12px; fill: #111;"></div>
          <span style="font-weight: 700; font-size: 14px;">{{ props.data.label }}</span>
        </div>
      </template>
    </VueFlow>
  </div>
</template>
