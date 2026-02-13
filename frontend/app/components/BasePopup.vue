<script setup lang="ts">
const props = defineProps<{
  extraClass?: string
}>()
</script>

<template>
    <div :class="[
        'border border-stone-400/50 rounded-xl bg-black font-medium relative z-20 overflow-hidden',
        extraClass
      ]">
      <slot></slot>
    </div>
    <div class="absolute inset-1 rounded-xl blur-md bg-stone-50/40 z-10"></div>
</template>