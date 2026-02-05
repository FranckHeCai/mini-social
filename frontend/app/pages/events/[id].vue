<script setup lang="ts">
const nuxt = useNuxtApp()
console.log(nuxt)
</script>
<template>
  <h1>Events {{ $route.params.id }} page</h1>
</template>