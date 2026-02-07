<template>
  <div class="top-0 sticky w-full border-b border-white/20 bg-black/50 backdrop-blur-md flex">
    <div class="flex-1 flex flex-col items-center h-13 hover:bg-white/15 transition-all duration-150">
      <div class="flex flex-1 items-center justify-center font-medium">
        <p>{{$props.page}}</p>
      </div>
      <div class="h-1 w-15 rounded-full bg-blue-400"></div>
    </div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
  page: string
}>()
</script>

<style scoped>

</style>