<script setup lang="ts">
const props = defineProps<{
  src: string
  size: string | number
  addClass?: string
}>()

</script>

<template>
  <div>
    <div :class="[addClass , 'rounded-full overflow-hidden']" :style="{width:`${Number(props.size) * 4}px`, height:`${Number(props.size) * 4}px`}">
      <img class="h-full w-full" src="../assets/feitan.jpg" alt="profile-picture">
    </div>
  </div>
</template>


<style scoped>

</style>